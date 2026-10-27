#!/usr/bin/env python3
"""Render the calculator's two-door decision geometry without recomputing policies."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
import math
from pathlib import Path
import sys
from typing import Any

import matplotlib as mpl
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.patches import Polygon

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "figures" / "scripts"))
from resolve_figure_config import resolve_from_file

FIGURE_ID = "two-door-decisions"
PANEL_IDS = ("minimax_regret", "maximin_gain")
POLICIES = frozenset(("A", "B", "baseline"))
Point = tuple[float, float]


@dataclass(frozen=True)
class Region:
    """Prepared polygon and its calculator-supplied policy label location.

    Parameters
    ----------
    policy : str
        Calculator policy identifier: A, B, or baseline.
    polygon : tuple of (float, float)
        Closed beta/d_A boundary coordinates in source order.
    label_anchor : tuple of float
        Source-provided location identifying the region interior.
    """

    policy: str
    polygon: tuple[Point, ...]
    label_anchor: Point


@dataclass(frozen=True)
class Panel:
    """Prepared regions and ties for one decision objective.

    Parameters
    ----------
    title : str
        Source-provided human-readable objective name.
    regions : tuple of Region
        Complete source-exported regions; none are selected or recomputed.
    boundaries : tuple of coordinate tuples
        Source-sampled curves or straight segments denoting tied optima.
    tie_points : tuple of (float, float)
        Isolated multiple-policy ties supplied by the calculator.
    """

    title: str
    regions: tuple[Region, ...]
    boundaries: tuple[tuple[Point, ...], ...]
    tie_points: tuple[Point, ...]


@dataclass(frozen=True)
class PlotData:
    """Immutable geometry on dimensionless beta and detection-probability axes.

    Parameters
    ----------
    beta, d_a : tuple of float
        Lower and upper domain endpoints from the analytical artifact.
    policy_labels : tuple of (str, str)
        Source policy identifiers paired with human-readable labels.
    panels : tuple of Panel
        Minimax-regret and maximin-gain geometry in the approved display order.
    """

    beta: tuple[float, float]
    d_a: tuple[float, float]
    policy_labels: tuple[tuple[str, str], ...]
    panels: tuple[Panel, ...]


@dataclass(frozen=True)
class FigureConfig:
    """Resolved rendering dimensions, paths and draft overwrite permission.

    Parameters
    ----------
    size_inches : tuple of float
        Page width and height in inches, without export cropping.
    dpi : int
        PNG dots per inch; PDF geometry remains vector.
    style_path, stem, source_path : pathlib.Path
        Local style, draft output stem, and authoritative drawing artifact.
    overwrite : bool
        Whether existing draft outputs may be replaced.
    colors : tuple of (str, str)
        Fixed policy-to-color mapping from the project palette.
    boundary_color : str
        Shared color of tie boundaries, tie markers, and label leaders.
    """

    size_inches: tuple[float, float]
    dpi: int
    style_path: Path
    stem: Path
    source_path: Path
    overwrite: bool
    colors: tuple[tuple[str, str], ...]
    boundary_color: str


def load_plot_data(path: Path) -> PlotData:
    """Validate and load already computed polygons, tie lines and label anchors.

    Parameters
    ----------
    path : pathlib.Path
        Calculator-produced ``plot_data.json``. Coordinates must be finite
        rational strings within the declared dimensionless parameter domain.

    Returns
    -------
    data : PlotData
        Immutable drawing geometry, with rational coordinates converted to
        floating point solely for Matplotlib rendering. No policy is computed.

    Raises
    ------
    ValueError
        If the schema, policy labels, domain, coordinate shape, or geometry
        is missing or invalid, including coordinates outside the domain.
    """
    raw = json.loads(path.read_text())

    def number(value: Any) -> float:
        if not isinstance(value, str):
            raise ValueError("Plot coordinates must be rational strings.")
        result = float(Fraction(value))
        if not math.isfinite(result):
            raise ValueError("Plot coordinates must be finite.")
        return result

    try:
        if raw["schema_version"] != 1 or set(raw["panels"]) != set(PANEL_IDS):
            raise ValueError("Unsupported plot-data schema or panel selection.")
        domain = raw["domain"]
        beta, d_a = (tuple(number(v) for v in domain[key]) for key in ("beta", "d_a"))
        if any(len(bounds) != 2 or bounds[0] >= bounds[1] for bounds in (beta, d_a)):
            raise ValueError("Each parameter domain must have increasing endpoints.")
        labels = raw["policy_labels"]
        if set(labels) != POLICIES or not all(isinstance(v, str) and v for v in labels.values()):
            raise ValueError("Every supported policy requires a nonempty label.")

        def point(value: Any) -> Point:
            if not isinstance(value, list) or len(value) != 2:
                raise ValueError("Each coordinate must contain beta and d_A.")
            pair = tuple(number(v) for v in value)
            if not all(lo <= coordinate <= hi for coordinate, (lo, hi) in zip(pair, (beta, d_a))):
                raise ValueError("Drawing coordinate lies outside the declared domain.")
            return pair

        def tie_policies(value: Any) -> None:
            if not isinstance(value, list) or len(value) < 2 or not set(value) <= POLICIES:
                raise ValueError("A tie must name at least two supported policies.")

        panels = []
        for key in PANEL_IDS:
            source = raw["panels"][key]
            if not isinstance(source["title"], str) or not source["title"]:
                raise ValueError("A panel requires a nonempty title.")
            regions = []
            for region in source["regions"]:
                polygon = tuple(point(value) for value in region["polygon"])
                if region["policy"] not in POLICIES or len(polygon) < 4 or polygon[0] != polygon[-1]:
                    raise ValueError("A region needs a supported policy and a closed polygon.")
                regions.append(Region(region["policy"], polygon, point(region["label_anchor"])))
            if not regions:
                raise ValueError("A panel requires at least one region.")
            boundaries = []
            for boundary in source["boundaries"]:
                tie_policies(boundary["policies"])
                coordinates = tuple(point(value) for value in boundary["points"])
                if len(coordinates) < 2:
                    raise ValueError("A boundary needs at least two points.")
                boundaries.append(coordinates)
            tie_points = []
            for tie in source["tie_points"]:
                tie_policies(tie["policies"])
                tie_points.append(point(tie["point"]))
            panels.append(Panel(source["title"], tuple(regions), tuple(boundaries), tuple(tie_points)))
        return PlotData(beta, d_a, tuple(labels.items()), tuple(panels))
    except (KeyError, TypeError, ZeroDivisionError, OverflowError) as exc:
        raise ValueError("Incomplete or invalid calculator plot artifact.") from exc


def load_figure_config(path: Path = ROOT / "config" / "figures.yaml") -> FigureConfig:
    """Resolve the publication specification into an immutable rendering contract.

    Parameters
    ----------
    path : pathlib.Path, optional
        Project scientific-figure configuration. The default is canonical.

    Returns
    -------
    config : FigureConfig
        Physical dimensions in inches, raster DPI, local style/source paths,
        and the draft output stem. Final outputs are never selected here.
    """
    resolved = resolve_from_file(path, FIGURE_ID, assets_dir=ROOT / "tools" / "figures" / "assets")
    palette = resolved["resolved_assets"]["palette_definition"]["colors"]
    return FigureConfig(
        (resolved["layout"]["width_in"], resolved["layout"]["height_in"]),
        resolved["outputs"]["png"]["dpi"],
        ROOT / "tools" / "figures" / "assets" / resolved["outputs"]["style_asset"],
        ROOT / resolved["outputs"]["paths"]["draft_stem"],
        ROOT / resolved["analytical_source"]["artifact"],
        resolved["outputs"]["overwrite"]["draft"],
        (("A", palette["inspect_a"]), ("B", palette["inspect_b"]), ("baseline", palette["baseline"])),
        palette["boundary"],
    )


def build_two_door_decisions(data: PlotData, config: FigureConfig) -> tuple[Figure, tuple]:
    """Draw both approved policy maps from supplied geometry without analysis.

    Parameters
    ----------
    data : PlotData
        Validated polygons, ties and labels from the authoritative calculator.
    config : FigureConfig
        Publication dimensions and local style. Layout preserves the full
        shared domain; colors are redundant with text and boundary lines.

    Returns
    -------
    figure : matplotlib.figure.Figure
        Two-panel vector figure at the configured physical dimensions.
    axes : tuple of matplotlib.axes.Axes
        Minimax-regret and maximin-gain panels in the declared reading order.
    """
    with mpl.rc_context(fname=config.style_path, rc={
        "font.size": 8.5, "xtick.labelsize": 8, "ytick.labelsize": 8,
        "pdf.fonttype": 42, "savefig.bbox": None,
    }):
        fig = Figure(figsize=config.size_inches, layout="constrained")
        FigureCanvasAgg(fig)
        axs = tuple(fig.subplots(1, 2, sharex=True, sharey=True))
        colors = dict(config.colors)
        labels = dict(data.policy_labels)
        for ax, panel in zip(axs, data.panels):
            for region in panel.regions:
                patch = Polygon(region.polygon, facecolor=colors[region.policy],
                                edgecolor="none", closed=True, zorder=1)
                patch.set_gid("policy-" + region.policy)
                ax.add_patch(patch)
            for index, boundary in enumerate(panel.boundaries):
                line, = ax.plot(*zip(*boundary), color=config.boundary_color, linewidth=0.9, zorder=3)
                line.set_gid(f"tie-boundary-{index}")
            for index, point in enumerate(panel.tie_points):
                marker, = ax.plot(*point, marker="o", markersize=3.5, markerfacecolor="white",
                                  markeredgecolor=config.boundary_color, markeredgewidth=0.8, zorder=4)
                marker.set_gid(f"tie-point-{index}")
            for region in panel.regions:
                if region.policy == "baseline":
                    # A leader preserves legibility without widening the narrow region.
                    ax.annotate(labels[region.policy], xy=region.label_anchor,
                                xytext=(19, 24), textcoords="offset points", ha="left", va="center",
                                fontsize=8.5, arrowprops={"arrowstyle": "-", "lw": 0.65,
                                                         "color": config.boundary_color}, zorder=5)
                else:
                    ax.text(*region.label_anchor, labels[region.policy], ha="center", va="center",
                            fontsize=8.5, fontweight="medium", color="#1A1A1A", zorder=5)
            ax.set(xlim=data.beta, ylim=data.d_a, xlabel=r"$\beta$", title=panel.title)
            ax.set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5])
            ax.set_yticks([0.25, 0.4, 0.6, 0.8, 0.9])
            ax.tick_params(labelsize=8)
        axs[0].set_ylabel(r"Inspection sensitivity $d_A$", fontsize=8.5)
        return fig, axs


def render_figure(figure: Figure, config: FigureConfig) -> tuple[Path, Path]:
    """Save the review PDF and 300-dpi PNG without cropping their physical size.

    Parameters
    ----------
    figure : matplotlib.figure.Figure
        Figure returned by the builder.
    config : FigureConfig
        Draft paths, export DPI and draft overwrite permission.

    Returns
    -------
    paths : tuple of pathlib.Path
        Written PDF and PNG files, in that order.

    Raises
    ------
    FileExistsError
        If an output exists and the resolved draft overwrite policy forbids it.
    """
    paths = tuple(config.stem.with_suffix("." + suffix) for suffix in ("pdf", "png"))
    if not config.overwrite and any(path.exists() for path in paths):
        raise FileExistsError("Draft overwrite is disabled for an existing artifact.")
    config.stem.parent.mkdir(parents=True, exist_ok=True)
    with mpl.rc_context({"pdf.fonttype": 42, "savefig.bbox": None}):
        figure.savefig(paths[0], dpi=config.dpi, facecolor="white", transparent=False,
                       metadata={"CreationDate": None, "ModDate": None, "Title": FIGURE_ID})
        figure.savefig(paths[1], dpi=config.dpi, facecolor="white", transparent=False,
                       metadata={"Title": FIGURE_ID})
    return paths


def main() -> None:
    """Render the configured draft artifact from the calculator's exported geometry."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=ROOT / "config" / "figures.yaml")
    args = parser.parse_args()
    config = load_figure_config(args.config)
    figure, _ = build_two_door_decisions(load_plot_data(config.source_path), config)
    for path in render_figure(figure, config):
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
