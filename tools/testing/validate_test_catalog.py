#!/usr/bin/env python3
"""Validate docs/testing/test-cases.yaml against the test-case catalog schema.

Copy this script to tools/testing/validate_test_catalog.py in your project
and version it there. Do not call the globally installed skill script directly.

Usage:
    python tools/testing/validate_test_catalog.py [CATALOG] [--config CONFIG]

CATALOG defaults to docs/testing/test-cases.yaml.
CONFIG  defaults to docs/testing/test-catalog-config.yaml.

Configuration file (test-catalog-config.yaml):
    block_on_proposed: true   # fail when any entry has status "proposed" (default)
    block_on_proposed: false  # allow proposed entries without failing

Exit codes:
    0  All checks passed.
    1  One or more validation errors.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Schema constants
# ---------------------------------------------------------------------------

REQUIRED_FIELDS = frozenset({"id", "component", "behavior", "level", "status", "origin"})
VALID_STATUSES = frozenset({"proposed", "implemented", "deferred", "blocked", "not-applicable"})
VALID_LEVELS = frozenset({"unit", "integration", "e2e", "contract", "property"})
VALID_ORIGINS = frozenset({"feature", "regression", "audit", "contract"})


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_yaml(path: Path) -> object:
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _load_config(config_path: Path) -> dict:
    if config_path.exists():
        data = _load_yaml(config_path)
        return data if isinstance(data, dict) else {}
    return {}


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate(catalog_path: Path, config_path: Path) -> list[str]:
    errors: list[str] = []

    try:
        data = _load_yaml(catalog_path)
    except yaml.YAMLError as exc:
        return [f"YAML parse error: {exc}"]

    if not isinstance(data, dict) or "cases" not in data:
        return ["top-level key 'cases' is missing"]

    cases = data["cases"]
    if not isinstance(cases, list):
        return ["'cases' must be a list"]

    config = _load_config(config_path)
    block_on_proposed: bool = config.get("block_on_proposed", True)

    seen_ids: set[str] = set()

    for i, case in enumerate(cases):
        if not isinstance(case, dict):
            errors.append(f"cases[{i}]: entry must be a mapping, got {type(case).__name__}")
            continue

        entry_id: str = case.get("id") or f"<missing id at index {i}>"
        loc = entry_id

        # Required fields
        missing = REQUIRED_FIELDS - case.keys()
        if missing:
            errors.append(f"{loc}: missing required fields: {sorted(missing)}")

        # ID uniqueness
        raw_id = case.get("id")
        if raw_id is not None:
            if raw_id in seen_ids:
                errors.append(f"{loc}: duplicate id '{raw_id}'")
            else:
                seen_ids.add(raw_id)

        # Status
        status = case.get("status")
        if status is not None and status not in VALID_STATUSES:
            errors.append(
                f"{loc}: invalid status '{status}'; must be one of {sorted(VALID_STATUSES)}"
            )

        # Level
        level = case.get("level")
        if level is not None and level not in VALID_LEVELS:
            errors.append(
                f"{loc}: invalid level '{level}'; must be one of {sorted(VALID_LEVELS)}"
            )

        # Origin
        origin = case.get("origin")
        if origin is not None and origin not in VALID_ORIGINS:
            errors.append(
                f"{loc}: invalid origin '{origin}'; must be one of {sorted(VALID_ORIGINS)}"
            )

        # Implemented entries must have test_refs
        if status == "implemented":
            refs = case.get("test_refs")
            if not refs:
                errors.append(
                    f"{loc}: status is 'implemented' but 'test_refs' is missing or empty"
                )
            else:
                repo_root = Path.cwd()
                for ref in refs:
                    # Strip optional ::test_function suffix before checking path
                    path_part = ref.split("::")[0]
                    if not (repo_root / path_part).exists():
                        errors.append(f"{loc}: test_refs path not found: {path_part}")

        # Blocked entries must have a blocker
        if status == "blocked" and not case.get("blocker"):
            errors.append(f"{loc}: status is 'blocked' but 'blocker' field is missing")

        # Proposed blocking (configurable)
        if status == "proposed" and block_on_proposed:
            errors.append(
                f"{loc}: status is 'proposed' "
                f"(set block_on_proposed: false in test-catalog-config.yaml to allow)"
            )

    return errors


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate docs/testing/test-cases.yaml.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "catalog",
        nargs="?",
        default="docs/testing/test-cases.yaml",
        help="Path to test-cases.yaml (default: docs/testing/test-cases.yaml)",
    )
    parser.add_argument(
        "--config",
        default="docs/testing/test-catalog-config.yaml",
        help="Path to test-catalog-config.yaml (default: docs/testing/test-catalog-config.yaml)",
    )
    args = parser.parse_args()

    catalog_path = Path(args.catalog)
    config_path = Path(args.config)

    if not catalog_path.exists():
        print(f"error: catalog not found: {catalog_path}", file=sys.stderr)
        return 1

    errors = validate(catalog_path, config_path)

    if errors:
        print(f"Validation failed — {len(errors)} error(s) in {catalog_path}:")
        for err in errors:
            print(f"  {err}")
        return 1

    data = yaml.safe_load(catalog_path.read_text(encoding="utf-8"))
    count = len(data.get("cases", []))
    print(f"OK: {catalog_path} ({count} entr{'y' if count == 1 else 'ies'}, all checks passed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
