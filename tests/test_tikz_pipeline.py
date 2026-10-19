"""Static checks of the project's TikZ pipeline; none of them needs LaTeX.

Copied from the tikz-diagrams skill. Save as tests/test_tikz_pipeline.py,
adjust the constants below to the project, and keep it with the other tests.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RENDERER = REPO_ROOT / "scripts" / "render_tikz.py"

# Directories never searched for forked renderers or stray sources.
EXCLUDED_PARTS = {"archive", ".git", "build", "work-scripts", "__pycache__"}
# Tests may name LaTeX engines (skip conditions, these checks) without driving them.
FORK_EXCLUDED_PARTS = EXCLUDED_PARTS | {"tests"}
LATEX_ENGINES = ("pdflatex", "lualatex", "xelatex", "latexmk", "tectonic")


def _load_renderer():
    spec = importlib.util.spec_from_file_location("project_render_tikz", RENDERER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


render_tikz = _load_renderer()
CONFIG = render_tikz.load_config(REPO_ROOT / render_tikz.CONFIG_NAME, REPO_ROOT)


def _project_files(pattern: str, excluded: set[str]) -> list[Path]:
    return sorted(
        path for path in REPO_ROOT.rglob(pattern)
        if not excluded & set(path.relative_to(REPO_ROOT).parts)
    )


def test_every_diagram_source_has_its_rendered_image_and_resolvable_includes() -> None:
    units = render_tikz.discover_units(CONFIG)
    assert units, "no unit with TikZ sources found; check tikz-render.yaml"
    issues = [issue for unit_dir in units.values() for issue in render_tikz.verify_unit(CONFIG, unit_dir)]
    assert not issues, "\n".join(issues)


def test_no_other_script_drives_latex() -> None:
    """A second renderer drifts from the shared one; one project had six versions."""
    forks = [
        path.relative_to(REPO_ROOT).as_posix()
        for path in _project_files("*.py", FORK_EXCLUDED_PARTS)
        if path.resolve() != RENDERER.resolve()
        and any(engine in path.read_text(encoding="utf-8", errors="replace") for engine in LATEX_ENGINES)
    ]
    assert not forks, "scripts calling a LaTeX engine besides the shared renderer: " + ", ".join(forks)


def test_no_diagram_source_sits_outside_a_source_directory() -> None:
    """A standalone source outside source_dir is invisible to the renderer and never refreshed."""
    units = render_tikz.discover_units(CONFIG)
    source_dirs = {(unit_dir / CONFIG.source_dir).resolve() for unit_dir in units.values()}
    strays = [
        path.relative_to(REPO_ROOT).as_posix()
        for path in _project_files("*.tex", EXCLUDED_PARTS)
        if path.resolve().parent not in source_dirs
        and render_tikz.STANDALONE_RE.search(path.read_text(encoding="utf-8", errors="replace"))
    ]
    assert not strays, "standalone TikZ sources outside the configured source directories: " + ", ".join(strays)
