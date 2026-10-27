#!/usr/bin/env python3
"""Resolve project defaults and export-profile values for one figure."""

from __future__ import annotations

import argparse
from copy import deepcopy
from pathlib import Path
import sys
from typing import Any, Mapping

from _common import default_assets_dir, deep_merge, dump_json, dump_yaml, load_yaml
from validate_figure_config import validate_configuration


def _profile_to_layout(profile: Mapping[str, Any]) -> dict[str, Any]:
    dimensions = profile.get("dimensions", {})
    result: dict[str, Any] = {
        "class": profile.get("layout_class"),
        "strategy": profile.get("layout_strategy", "profile-defined"),
    }
    if isinstance(dimensions, Mapping):
        if "width_in" in dimensions:
            result["width_in"] = dimensions["width_in"]
        if "height_in" in dimensions:
            result["height_in"] = dimensions["height_in"]
    if isinstance(profile.get("slide"), Mapping):
        slide = dict(profile["slide"])
        if "intended_placement" in slide and "placement" not in slide:
            slide["placement"] = slide.pop("intended_placement")
        result["slide"] = slide
    return result


def _profile_to_outputs(
    profile_name: str,
    profile: Mapping[str, Any],
    export_defaults: Mapping[str, Any],
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "export_profile": profile_name,
        "formats": deepcopy(profile.get("formats", [])),
        "transparent": profile.get("transparent", export_defaults.get("transparent", False)),
        "pad_inches": export_defaults.get("pad_inches", 0.05),
        "exact_physical_size_required": profile.get("exact_physical_size_required", False),
    }
    if isinstance(profile.get("png"), Mapping):
        result["png"] = deepcopy(profile["png"])
    if isinstance(profile.get("pdf"), Mapping):
        result["pdf"] = deepcopy(profile["pdf"])
    if profile.get("style_asset"):
        result["style_asset"] = profile["style_asset"]
    return result


def resolve_figure(
    config: Mapping[str, Any],
    figure_id: str,
    *,
    assets_dir: Path | None = None,
) -> dict[str, Any]:
    """Return a typed-by-convention resolved configuration mapping.

    Only technical defaults are inherited. Scientific intent, analytical
    source, content selection, and approvals always come from the figure entry.
    """

    assets = assets_dir or default_assets_dir()
    export_document = load_yaml(assets / "export-profiles.yaml")
    palette_document = load_yaml(assets / "palette.yaml")
    export_profiles = export_document.get("profiles", {})
    export_defaults = export_document.get("defaults", {})
    palettes = palette_document.get("palettes", {})

    figures = config.get("figures", {})
    if figure_id not in figures:
        raise KeyError(f"Unknown figure identifier: {figure_id}")
    figure = deepcopy(figures[figure_id])
    specification = figure["specification"]
    project_defaults = deepcopy(config.get("defaults", {}))

    output_spec = specification.get("outputs", {})
    export_profile_name = output_spec.get("export_profile")
    export_profile = export_profiles.get(export_profile_name, {}) if export_profile_name else {}

    resolved_layout = deep_merge(
        _profile_to_layout(export_profile),
        specification.get("layout", {}),
    )
    resolved_outputs = deep_merge(
        _profile_to_outputs(export_profile_name, export_profile, export_defaults)
        if export_profile_name
        else {},
        project_defaults.get("outputs", {}),
    )
    resolved_outputs = deep_merge(resolved_outputs, output_spec)

    selected_palette = (
        specification.get("visual", {}).get("palette")
        or project_defaults.get("palette")
        or palette_document.get("defaults", {}).get("sequential_palette")
    )
    neutral_palette = (
        project_defaults.get("neutral_palette")
        or palette_document.get("defaults", {}).get("neutral_palette")
    )
    resolved_visual = deep_merge(
        {"palette": selected_palette} if selected_palette else {},
        specification.get("visual", {}),
    )
    resolved_accessibility = deep_merge(
        project_defaults.get("accessibility", {}),
        specification.get("accessibility", {}),
    )

    result = {
        "schema_version": config.get("schema_version"),
        "project": deepcopy(config.get("project", {})),
        "figure_id": figure_id,
        "profile": specification.get("profile"),
        "intent": deepcopy(specification.get("intent", {})),
        "analytical_source": deepcopy(specification.get("analytical_source", {})),
        "content": deepcopy(specification.get("content", {})),
        "layout": resolved_layout,
        "visual": resolved_visual,
        "captions": deepcopy(specification.get("captions", {})),
        "outputs": resolved_outputs,
        "accessibility": resolved_accessibility,
        "approvals": deepcopy(specification.get("approvals", {})),
        "implementation": deepcopy(figure.get("implementation", {})),
        "resolved_assets": {
            "assets_dir": str(assets),
            "export_profile": export_profile_name,
            "style_asset": export_profile.get("style_asset"),
            "palette": selected_palette,
            "neutral_palette": neutral_palette,
            "palette_definition": deepcopy(palettes.get(selected_palette, {})),
            "neutral_palette_definition": deepcopy(palettes.get(neutral_palette, {})),
        },
    }
    return result


def resolve_from_file(
    config_path: Path,
    figure_id: str,
    *,
    assets_dir: Path | None = None,
) -> dict[str, Any]:
    """Validate and resolve one figure from a project configuration file."""

    config, issues = validate_configuration(config_path, assets_dir=assets_dir)
    blockers = [issue for issue in issues if issue.severity == "blocking"]
    if blockers:
        details = "; ".join(f"{item.location}: {item.message}" for item in blockers[:5])
        raise ValueError(f"Cannot resolve invalid configuration: {details}")
    return resolve_figure(config, figure_id, assets_dir=assets_dir)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    parser.add_argument("figure_id")
    parser.add_argument("--assets-dir", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--format", choices=("yaml", "json"), default="yaml")
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    try:
        resolved = resolve_from_file(
            args.config,
            args.figure_id,
            assets_dir=args.assets_dir,
        )
    except (FileNotFoundError, KeyError, ValueError, TypeError) as exc:
        print(f"Configuration resolution failed: {exc}", file=sys.stderr)
        return 2

    if args.output:
        if args.format == "json":
            dump_json(resolved, args.output)
        else:
            dump_yaml(resolved, args.output)
    else:
        import yaml

        print(yaml.safe_dump(resolved, sort_keys=False, allow_unicode=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
