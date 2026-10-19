"""Render TikZ diagram sources of a project to PNG (and optionally PDF).

The project copies this script into its own `scripts/` directory and uses it
as its only TikZ renderer. Layout comes from `tikz-render.yaml` at the project
root:

    version: 1
    units: "lectures/[0-9][0-9]-*"     # glob of unit directories
    source_dir: sources/tikz-diagrams  # TikZ sources, relative to a unit
    output_dir: figures                # rendered files, relative to a unit
    dpi_scale: 6.0                     # PDF points are rasterised at 72 * scale dpi
    keep_pdf: false                    # also copy the vector PDF beside the PNG
    engine: pdflatex

Every `*.tex` in a source directory whose name does not start with `_` is a
standalone document and renders to `<output_dir>/<stem>.png`. Files starting
with `_` are shared includes (`_style.tex`) or the optional `_outputs.yaml`
manifest, which declares parameterised variants and extra output names:

    version: 1
    sources:
      cycle:
        - name: cycle-full
          parameters: {stage: 0}
        - name: cycle-data
          parameters: {stage: 2}

Each parameter is defined as a TeX macro (`\\def\\stage{2}`) before the source
is read, so the source keeps a default with `\\ifdefined\\stage\\else ... \\fi`.

The pipeline is: engine in nonstop mode with shell escape disabled, run from
the source directory with a temporary output directory; overfull boxes and
missing characters read from the log; the single page of the PDF rasterised
by PyMuPDF without alpha.

Exit status:
    0  every requested action succeeded
    1  a diagram failed, verification found issues, or a unit was not found
    2  invalid command line, configuration, or manifest
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

import yaml

CONFIG_NAME = "tikz-render.yaml"
MANIFEST_NAME = "_outputs.yaml"
SUPPORTED_ENGINES = ("pdflatex", "lualatex", "xelatex")
DEFAULT_DPI_SCALE = 6.0

OUTPUT_NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")
PARAMETER_NAME_RE = re.compile(r"^[A-Za-z]+$")
FORBIDDEN_PARAMETER_CHARS = set("{}%\\\n\r")
STANDALONE_RE = re.compile(r"^[^%\n]*\\documentclass\s*(\[[^\]]*\])?\s*\{standalone\}", re.MULTILINE)
INPUT_RE = re.compile(r"^[^%\n]*?\\(?:input|include)\{([^}]+)\}", re.MULTILINE)
WARNING_PREFIXES = ("Overfull \\hbox", "Overfull \\vbox", "Missing character:")


class ConfigError(Exception):
    """The project configuration or a manifest cannot be used."""


@dataclass(frozen=True)
class RenderConfig:
    root: Path
    units: str
    source_dir: str
    output_dir: str
    dpi_scale: float = DEFAULT_DPI_SCALE
    keep_pdf: bool = False
    engine: str = "pdflatex"


@dataclass(frozen=True)
class RenderJob:
    """One compilation: a source with fixed parameters, saved under one or more names."""

    source: Path
    parameters: tuple[tuple[str, str], ...]
    names: tuple[str, ...]


@dataclass
class RenderResult:
    written: list[Path]
    warnings: list[str]


# --- Configuration ----------------------------------------------------------


def load_config(config_path: Path, root: Path) -> RenderConfig:
    """Read and validate `tikz-render.yaml`."""
    if not config_path.is_file():
        raise ConfigError(f"configuration not found: {config_path}")
    try:
        data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as error:
        raise ConfigError(f"{config_path.name}: invalid YAML: {error}") from error
    if not isinstance(data, dict):
        raise ConfigError(f"{config_path.name}: expected a mapping")
    if data.get("version") != 1:
        raise ConfigError(f"{config_path.name}: 'version' must be 1")

    known = {"version", "units", "source_dir", "output_dir", "dpi_scale", "keep_pdf", "engine"}
    unknown = sorted(set(data) - known)
    if unknown:
        raise ConfigError(f"{config_path.name}: unknown keys: {', '.join(unknown)}")

    for key in ("units", "source_dir", "output_dir"):
        value = data.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ConfigError(f"{config_path.name}: '{key}' must be a non-empty string")
        if Path(value).is_absolute() or ".." in Path(value).parts:
            raise ConfigError(f"{config_path.name}: '{key}' must be a relative path inside the project")

    dpi_scale = data.get("dpi_scale", DEFAULT_DPI_SCALE)
    if isinstance(dpi_scale, bool) or not isinstance(dpi_scale, (int, float)) or dpi_scale <= 0:
        raise ConfigError(f"{config_path.name}: 'dpi_scale' must be a positive number")
    keep_pdf = data.get("keep_pdf", False)
    if not isinstance(keep_pdf, bool):
        raise ConfigError(f"{config_path.name}: 'keep_pdf' must be true or false")
    engine = data.get("engine", "pdflatex")
    if engine not in SUPPORTED_ENGINES:
        raise ConfigError(f"{config_path.name}: 'engine' must be one of {', '.join(SUPPORTED_ENGINES)}")

    return RenderConfig(
        root=root,
        units=data["units"],
        source_dir=data["source_dir"],
        output_dir=data["output_dir"],
        dpi_scale=float(dpi_scale),
        keep_pdf=keep_pdf,
        engine=engine,
    )


def unit_id(config: RenderConfig, unit_dir: Path) -> str:
    return "." if unit_dir.resolve() == config.root.resolve() else unit_dir.name


def discover_units(config: RenderConfig) -> dict[str, Path]:
    """Unit directories whose source directory holds a compilable source, by directory name."""
    candidates = [config.root] if config.units == "." else sorted(config.root.glob(config.units))
    units: dict[str, Path] = {}
    for candidate in candidates:
        if not diagram_sources(candidate / config.source_dir):
            continue
        name = unit_id(config, candidate)
        if name in units:
            raise ConfigError(
                f"two units share the name {name!r}; narrow the 'units' glob so names are unique"
            )
        units[name] = candidate
    return units


def resolve_unit(fragment: str, units: dict[str, Path]) -> str | None:
    """Exact unit name, or the only unit whose name contains the fragment."""
    if fragment in units:
        return fragment
    matches = [name for name in units if fragment in name]
    return matches[0] if len(matches) == 1 else None


def diagram_sources(source_dir: Path) -> list[Path]:
    """Compilable sources, in a stable order; `_`-prefixed files are includes."""
    return sorted(path for path in source_dir.glob("*.tex") if not path.name.startswith("_"))


# --- Manifest and render plan -----------------------------------------------


def _parameter_items(raw: object, where: str) -> tuple[tuple[str, str], ...]:
    if raw is None:
        return ()
    if not isinstance(raw, dict):
        raise ConfigError(f"{where}: 'parameters' must be a mapping")
    items = []
    for name, value in raw.items():
        if not isinstance(name, str) or not PARAMETER_NAME_RE.match(name):
            raise ConfigError(f"{where}: parameter name {name!r} must contain letters only")
        if isinstance(value, bool) or not isinstance(value, (str, int, float)):
            raise ConfigError(f"{where}: parameter {name!r} must be a string or a number")
        text = str(value)
        if FORBIDDEN_PARAMETER_CHARS & set(text):
            raise ConfigError(f"{where}: parameter {name!r} contains a brace, backslash, percent or newline")
        items.append((name, text))
    return tuple(sorted(items))


def load_manifest(source_dir: Path) -> dict[str, list[tuple[str, tuple[tuple[str, str], ...]]]]:
    """Declared outputs per source stem; empty when the directory has no manifest."""
    path = source_dir / MANIFEST_NAME
    if not path.is_file():
        return {}
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as error:
        raise ConfigError(f"{path}: invalid YAML: {error}") from error
    if not isinstance(data, dict) or data.get("version") != 1:
        raise ConfigError(f"{path}: expected a mapping with 'version: 1'")
    sources = data.get("sources")
    if not isinstance(sources, dict) or not sources:
        raise ConfigError(f"{path}: 'sources' must be a non-empty mapping")

    declared: dict[str, list[tuple[str, tuple[tuple[str, str], ...]]]] = {}
    for stem, entries in sources.items():
        where = f"{path.name}: {stem}"
        if not (source_dir / f"{stem}.tex").is_file():
            raise ConfigError(f"{where}: no source {stem}.tex in {source_dir}")
        if not isinstance(entries, list) or not entries:
            raise ConfigError(f"{where}: expected a non-empty list of outputs")
        outputs = []
        for entry in entries:
            if not isinstance(entry, dict) or set(entry) - {"name", "parameters"}:
                raise ConfigError(f"{where}: each output is a mapping with 'name' and optional 'parameters'")
            name = entry.get("name")
            if (not isinstance(name, str) or not OUTPUT_NAME_RE.match(name)
                    or name.lower().endswith((".png", ".pdf"))):
                raise ConfigError(f"{where}: invalid output name {name!r} (no extension, no spaces)")
            outputs.append((name, _parameter_items(entry.get("parameters"), f"{where}/{name}")))
        declared[stem] = outputs
    return declared


def plan_unit(config: RenderConfig, unit_dir: Path) -> list[RenderJob]:
    """Compilations needed for one unit, grouping outputs that share parameters."""
    source_dir = unit_dir / config.source_dir
    manifest = load_manifest(source_dir)
    jobs: list[RenderJob] = []
    seen: dict[str, str] = {}
    for source in diagram_sources(source_dir):
        outputs = manifest.get(source.stem, [(source.stem, ())])
        grouped: dict[tuple[tuple[str, str], ...], list[str]] = {}
        for name, parameters in outputs:
            if name in seen:
                raise ConfigError(
                    f"{unit_id(config, unit_dir)}: output {name!r} is produced by both "
                    f"{seen[name]} and {source.name}"
                )
            seen[name] = source.name
            grouped.setdefault(parameters, []).append(name)
        for parameters, names in grouped.items():
            jobs.append(RenderJob(source=source, parameters=parameters, names=tuple(names)))
    return jobs


def expected_outputs(config: RenderConfig, unit_dir: Path, jobs: list[RenderJob]) -> list[Path]:
    output_dir = unit_dir / config.output_dir
    suffixes = (".png", ".pdf") if config.keep_pdf else (".png",)
    return [output_dir / f"{name}{suffix}" for job in jobs for name in job.names for suffix in suffixes]


# --- Static verification ----------------------------------------------------


def verify_unit(config: RenderConfig, unit_dir: Path) -> list[str]:
    """Problems that can be found without LaTeX or PyMuPDF."""
    name = unit_id(config, unit_dir)
    source_dir = unit_dir / config.source_dir
    try:
        jobs = plan_unit(config, unit_dir)
    except ConfigError as error:
        return [str(error)]

    issues = []
    for source in diagram_sources(source_dir):
        if not STANDALONE_RE.search(source.read_text(encoding="utf-8", errors="replace")):
            issues.append(f"{name}/{source.name}: not a standalone document")
    for tex in sorted(source_dir.glob("*.tex")):
        for included in INPUT_RE.findall(tex.read_text(encoding="utf-8", errors="replace")):
            if "\\" in included or "#" in included:
                continue
            target = source_dir / included
            if not target.suffix:
                target = target.with_suffix(".tex")
            if not target.is_file():
                issues.append(f"{name}/{tex.name}: \\input{{{included}}} does not resolve beside the source")
    for path in expected_outputs(config, unit_dir, jobs):
        if not path.is_file():
            issues.append(f"{name}: missing rendered output {path.relative_to(unit_dir).as_posix()}")
    return issues


# --- Rendering --------------------------------------------------------------


def parse_log_warnings(log_text: str) -> list[str]:
    """Overfull boxes and missing glyphs: content the reader will not see correctly."""
    return [line.strip() for line in log_text.splitlines() if line.startswith(WARNING_PREFIXES)]


def parse_log_errors(log_text: str, context: int = 2) -> list[str]:
    """TeX error lines (starting with `!`) with the lines that locate them."""
    lines = log_text.splitlines()
    errors = []
    for index, line in enumerate(lines):
        if line.startswith("!"):
            errors.extend(item.rstrip() for item in lines[index:index + 1 + context])
    return errors


def engine_command(config: RenderConfig, job: RenderJob, build_dir: Path) -> list[str]:
    definitions = "".join(f"\\def\\{key}{{{value}}}" for key, value in job.parameters)
    return [
        config.engine,
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-no-shell-escape",
        f"-output-directory={build_dir}",
        f"-jobname={job.names[0]}",
        f"{definitions}\\input{{{job.source.name}}}",
    ]


def rasterise(pdf_path: Path, png_path: Path, dpi_scale: float) -> None:
    try:
        import fitz  # PyMuPDF; imported here so static modes work without it
    except ImportError as error:
        raise RuntimeError("PyMuPDF (fitz) is required to rasterise the PDF") from error

    with fitz.open(pdf_path) as document:
        if document.page_count != 1:
            raise RuntimeError(f"{pdf_path.name}: {document.page_count} pages; one source must be one figure")
        pixmap = document[0].get_pixmap(matrix=fitz.Matrix(dpi_scale, dpi_scale), alpha=False)
        # Record the true resolution so the PNG's physical size equals the
        # diagram's TeX size; PyMuPDF would otherwise write 96 dpi.
        dpi = round(72 * dpi_scale)
        pixmap.set_dpi(dpi, dpi)
        pixmap.save(png_path)


def render_job(config: RenderConfig, job: RenderJob, output_dir: Path) -> RenderResult:
    """Compile one job and write its PNG (and PDF) files under every declared name."""
    with tempfile.TemporaryDirectory(prefix=f"{job.names[0]}-") as tmp:
        build_dir = Path(tmp)
        completed = subprocess.run(
            engine_command(config, job, build_dir),
            cwd=job.source.parent,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            # TeX echoes source text in its own encoding; strict decoding would
            # crash on exactly the logs worth reading.
            text=True,
            errors="replace",
        )
        log_path = build_dir / f"{job.names[0]}.log"
        log_text = log_path.read_text(encoding="utf-8", errors="replace") if log_path.is_file() else completed.stdout
        if completed.returncode != 0:
            details = parse_log_errors(log_text) or completed.stdout.splitlines()[-10:]
            raise RuntimeError("compilation failed:\n    " + "\n    ".join(details))

        output_dir.mkdir(parents=True, exist_ok=True)
        pdf_path = build_dir / f"{job.names[0]}.pdf"
        first_png = output_dir / f"{job.names[0]}.png"
        rasterise(pdf_path, first_png, config.dpi_scale)
        written = [first_png]
        for name in job.names[1:]:
            written.append(Path(shutil.copyfile(first_png, output_dir / f"{name}.png")))
        if config.keep_pdf:
            for name in job.names:
                written.append(Path(shutil.copyfile(pdf_path, output_dir / f"{name}.pdf")))
        return RenderResult(written=written, warnings=parse_log_warnings(log_text))


def render_unit(config: RenderConfig, unit_dir: Path, *, check: bool, strict: bool) -> int:
    name = unit_id(config, unit_dir)
    jobs = plan_unit(config, unit_dir)
    if check:
        print(f"{name}: {len(jobs)} compilation(s)")
        for job in jobs:
            parameters = ", ".join(f"{key}={value}" for key, value in job.parameters)
            suffix = f" [{parameters}]" if parameters else ""
            print(f"  {job.source.name}{suffix} -> {', '.join(job.names)}")
        return 0

    failures = 0
    output_dir = unit_dir / config.output_dir
    for job in jobs:
        try:
            result = render_job(config, job, output_dir)
        except (RuntimeError, OSError) as error:
            print(f"  ERROR {name}/{job.source.name}: {error}", file=sys.stderr)
            failures += 1
            continue
        for path in result.written:
            print(path.relative_to(config.root).as_posix())
        for warning in result.warnings:
            print(f"  WARNING {name}/{job.source.name}: {warning}")
        if strict and result.warnings:
            failures += 1
    return failures


# --- Command line -----------------------------------------------------------


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Render TikZ diagram sources to PNG.")
    parser.add_argument("unit", nargs="*", help="unit names or unique fragments, e.g. 01 or ode-stiff")
    parser.add_argument("--all", action="store_true", help="every unit with TikZ sources")
    parser.add_argument("--list", action="store_true", help="list units and their source counts")
    parser.add_argument("--check", action="store_true", help="print the render plan without compiling")
    parser.add_argument("--verify", action="store_true",
                        help="static checks without LaTeX: sources, includes, manifest, rendered outputs")
    parser.add_argument("--strict", action="store_true", help="treat overfull boxes and missing characters as failures")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="project root (default: parent of this script's directory)")
    parser.add_argument("--config", type=Path, help=f"configuration file (default: <root>/{CONFIG_NAME})")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        config = load_config(args.config or root / CONFIG_NAME, root)
        units = discover_units(config)
    except ConfigError as error:
        print(f"configuration error: {error}", file=sys.stderr)
        return 2
    if not units:
        print(f"no unit matches units={config.units!r} with TikZ sources in {config.source_dir}/",
              file=sys.stderr)
        return 1

    if args.list:
        for name, unit_dir in units.items():
            print(f"{name}  ({len(diagram_sources(unit_dir / config.source_dir))})")
        return 0

    if args.all or (args.verify and not args.unit):
        selected = list(units)
    elif args.unit:
        selected = []
        for fragment in args.unit:
            resolved = resolve_unit(fragment, units)
            if resolved is None:
                candidates = [name for name in units if fragment in name] or list(units)
                print(f"unit {fragment!r} not found or ambiguous; candidates: {', '.join(candidates)}",
                      file=sys.stderr)
                return 1
            selected.append(resolved)
    else:
        parser.error("name a unit or use --all")

    if args.verify:
        issues = [issue for name in selected for issue in verify_unit(config, units[name])]
        for issue in issues:
            print(issue)
        print(f"{len(issues)} issue(s) in {len(selected)} unit(s)")
        return 1 if issues else 0

    try:
        failures = sum(render_unit(config, units[name], check=args.check, strict=args.strict)
                       for name in selected)
    except ConfigError as error:
        print(f"configuration error: {error}", file=sys.stderr)
        return 2
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
