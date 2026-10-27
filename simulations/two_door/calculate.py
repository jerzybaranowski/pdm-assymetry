#!/usr/bin/env python3
"""Exact synthetic inspection comparisons for the approved two-door example.

The arithmetic implements Sections 3--5 and 8 of
``notes/12_two_door_model_specification.md`` and the approved decision revision
in ``notes/16_round1_revision_assessment.md``. Inputs describe actionable
conditions and detection, not physical-failure probabilities. No random
sampling, fitted parameters, or floating-point arithmetic is used.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Any

DIRECTORY = Path(__file__).resolve().parent
REPOSITORY = DIRECTORY.parents[1]
POLICIES = ("baseline", "A", "B")


@dataclass(frozen=True)
class Configuration:
    """Validated constants for the affine, zero-false-positive illustration.

    Attributes
    ----------
    q0, d_b : Fraction
        Baseline actionable-condition probability and detection sensitivity.
    beta_bounds, d_a_bounds : tuple of Fraction
        Closed parameter intervals; exposure and probabilities are dimensionless.
    response_value, inspection_cost : Fraction
        Net true-positive response value and unconditional visit burden, on the
        common arbitrary loss scale. Response value excludes inspection cost.
    exposures : dict
        Model identifiers mapped to the dimensionless exposures of A and B.
    raw : dict
        Original JSON input, retained verbatim as provenance in exported results.
    """

    q0: Fraction
    beta_bounds: tuple[Fraction, Fraction]
    d_a_bounds: tuple[Fraction, Fraction]
    d_b: Fraction
    response_value: Fraction
    inspection_cost: Fraction
    exposures: dict[str, tuple[Fraction, Fraction]]
    raw: dict[str, Any]


def _fraction(value: str) -> Fraction:
    if not isinstance(value, str):
        raise ValueError("Configuration numbers must be exact strings.")
    return Fraction(value)


def load_config(path: Path = DIRECTORY / "parameters.json") -> Configuration:
    """Read exact hypothetical inputs and check the supported model domain.

    Parameters
    ----------
    path : pathlib.Path, optional
        JSON source; defaults to the approved input file beside this script.

    Returns
    -------
    config : Configuration
        Rational constants, bounds, exposures, and original input provenance.

    Raises
    ------
    ValueError
        If numeric values are not strings, bounds or probabilities are invalid,
        positive denominators are absent, or false positives are nonzero.
    """
    raw = json.loads(path.read_text(encoding="utf-8"))
    config = Configuration(
        q0=_fraction(raw["q0"]),
        beta_bounds=tuple(map(_fraction, raw["beta_bounds"])),
        d_a_bounds=tuple(map(_fraction, raw["d_a_bounds"])),
        d_b=_fraction(raw["d_b"]),
        response_value=_fraction(raw["response_value"]),
        inspection_cost=_fraction(raw["inspection_cost"]),
        exposures={
            key: (_fraction(model["x_a"]), _fraction(model["x_b"]))
            for key, model in raw["models"].items()
        },
        raw=raw,
    )
    if _fraction(raw["false_positive_probability"]) != 0:
        raise ValueError("This approved calculation assumes zero false positives.")
    if not config.exposures or not 0 < config.q0 <= 1:
        raise ValueError("Models must be nonempty and q0 must be in (0, 1].")
    for bounds in (config.beta_bounds, config.d_a_bounds):
        if len(bounds) != 2 or not 0 <= bounds[0] <= bounds[1]:
            raise ValueError("Parameter bounds must be ordered nonnegative pairs.")
    if config.d_a_bounds[1] > 1 or not 0 < config.d_b <= 1:
        raise ValueError("Detection sensitivities must be probabilities.")
    if config.response_value <= 0 or config.inspection_cost < 0:
        raise ValueError("Response value must be positive and burden nonnegative.")
    for x_a, x_b in config.exposures.values():
        if x_a < 0 or x_b <= 0:
            raise ValueError("Exposures require x_A >= 0 and x_B > 0.")
        if any(config.q0 + config.beta_bounds[1] * x > 1 for x in (x_a, x_b)):
            raise ValueError("The affine condition probability exceeds one.")
    return config


def evaluate(
    config: Configuration, model_id: str, beta: Fraction, d_a: Fraction
) -> dict[str, Any]:
    """Compare three complete policies at one exact parameter point.

    Parameters
    ----------
    config : Configuration
        Validated hypothetical inputs with feasible contingent service assumed.
    model_id : str
        Routing interpretation in ``config.exposures``.
    beta, d_a : Fraction
        Dimensionless exposure coefficient and A sensitivity within the closed
        configured intervals. Floats are rejected to preserve exact ties.

    Returns
    -------
    result : dict
        Condition probabilities, expected loss reductions ``g_a`` and ``g_b``
        in arbitrary loss units, their difference, and all maximizing policies.
        Baseline has gain zero; inspection burden is subtracted exactly once.

    Raises
    ------
    ValueError
        If parameters are not Fractions, lie outside the configured rectangle,
        or the requested model is absent.
    """
    if model_id not in config.exposures:
        raise ValueError("Unknown routing model.")
    for value, bounds in ((beta, config.beta_bounds), (d_a, config.d_a_bounds)):
        if not isinstance(value, Fraction) or not bounds[0] <= value <= bounds[1]:
            raise ValueError("Parameters must be Fractions in the approved rectangle.")
    x_a, x_b = config.exposures[model_id]
    q_a, q_b = (config.q0 + beta * x for x in (x_a, x_b))
    g_a = q_a * d_a * config.response_value - config.inspection_cost
    g_b = q_b * config.d_b * config.response_value - config.inspection_cost
    gains = {"baseline": Fraction(0), "A": g_a, "B": g_b}
    best_gain = max(gains.values())
    return {
        "model": model_id, "beta": beta, "d_a": d_a,
        "q_a": q_a, "q_b": q_b, "g_a": g_a, "g_b": g_b,
        "a_minus_b": g_a - g_b,
        "optimal_policies": [key for key, value in gains.items() if value == best_gain],
    }


def historical_strict_decision(evaluations: list[dict[str, Any]]) -> dict[str, Any]:
    """Retain the superseded strict-preference rule as a historical diagnostic.

    Parameters
    ----------
    evaluations : list of dict
        Results from ``evaluate`` for the models/parameters declared plausible.

    Returns
    -------
    decision : dict
        ``choice`` is A or B for strict preference over both alternatives,
        ``baseline`` for baseline weak dominance, and ``fallback`` otherwise.
        ``common_improving_policies`` exposes early policies that strictly beat
        baseline everywhere even when A/B disagreement triggers fallback.
        Fallback retains the admissible schedule; it does not claim optimality.

    Raises
    ------
    ValueError
        If the model set is empty.
    """
    if not evaluations:
        raise ValueError("The plausible model set must be nonempty.")
    lower_a = min(row["g_a"] for row in evaluations)
    lower_b = min(row["g_b"] for row in evaluations)
    lower_delta = min(row["a_minus_b"] for row in evaluations)
    upper_delta = max(row["a_minus_b"] for row in evaluations)
    if lower_a > 0 and lower_delta > 0:
        choice = "A"
    elif lower_b > 0 and upper_delta < 0:
        choice = "B"
    elif all(row["g_a"] <= 0 and row["g_b"] <= 0 for row in evaluations):
        choice = "baseline"
    else:
        choice = "fallback"
    improving = [name for name, lower in (("A", lower_a), ("B", lower_b)) if lower > 0]
    return {
        "choice": choice,
        "operational_action": "baseline" if choice == "fallback" else choice,
        "common_improving_policies": improving,
        "baseline_dominated_by": improving,
        "minimum_g_a": lower_a, "minimum_g_b": lower_b,
        "minimum_a_minus_b": lower_delta, "maximum_a_minus_b": upper_delta,
    }


def model_set_decision(evaluations: list[dict[str, Any]]) -> dict[str, Any]:
    """Filter dominated policies and compare two finite-model decision criteria.

    Parameters
    ----------
    evaluations : list of dict
        Nonempty ``evaluate`` results for every retained model/parameter point.
        Gains share an arbitrary loss scale and are relative to each model's
        own baseline. Models receive no probability weights.

    Returns
    -------
    decision : dict
        Undominated policies, dominance witnesses, exact worst regret and worst
        incremental gain per policy, and all minimizers/maximizers respectively.
        ``choice`` names the unique minimax-regret policy or ``tie``. A tie is
        not silently resolved to baseline. Negative gains remain admissible.

    Raises
    ------
    ValueError
        If the retained model set is empty.

    Notes
    -----
    Policy j dominates i when its gain is no smaller in every model and larger
    in at least one. Regret is max_m(max_j G_j(m) - G_i(m)); its reference best
    policy ranges over all three feasible deterministic policies. Maximin gain
    maximizes min_m G_i(m), which is not minimax absolute loss when model-specific
    baseline losses differ. Both criteria select only undominated policies.
    There is deliberately no requirement that a selected policy improve on the
    baseline in every model; ``negative_gain_states`` exposes such cases.

    References
    ----------
    .. [1] M. C. M. Troffaes, "Decision making under uncertainty using imprecise
       probabilities," International Journal of Approximate Reasoning 45(1),
       17--29 (2007), doi:10.1016/j.ijar.2006.06.001. Sections 1 and 3.1 support
       pointwise admissibility and maximin expected utility, respectively.
    .. [2] ``notes/16_round1_revision_assessment.md``, "Checked decision analysis":
       project-specific minimax-regret comparison and exact selector boundaries.
    """
    if not evaluations:
        raise ValueError("The plausible model set must be nonempty.")
    gain_rows = [{"baseline": Fraction(0), "A": row["g_a"], "B": row["g_b"]}
                 for row in evaluations]
    dominated_by = {
        policy: [other for other in POLICIES if other != policy
                 and all(row[other] >= row[policy] for row in gain_rows)
                 and any(row[other] > row[policy] for row in gain_rows)]
        for policy in POLICIES
    }
    undominated = [policy for policy in POLICIES if not dominated_by[policy]]
    metrics = {
        policy: {
            "minimum_gain": min(row[policy] for row in gain_rows),
            "maximum_regret": max(max(row.values()) - row[policy] for row in gain_rows),
            "negative_gain_states": [index for index, row in enumerate(gain_rows)
                                     if row[policy] < 0],
        }
        for policy in POLICIES
    }
    least_regret = min(metrics[policy]["maximum_regret"] for policy in undominated)
    greatest_lower_gain = max(metrics[policy]["minimum_gain"] for policy in undominated)
    regret_policies = [policy for policy in undominated
                       if metrics[policy]["maximum_regret"] == least_regret]
    gain_policies = [policy for policy in undominated
                     if metrics[policy]["minimum_gain"] == greatest_lower_gain]
    improving = [policy for policy in POLICIES if metrics[policy]["minimum_gain"] > 0]
    return {
        "choice": regret_policies[0] if len(regret_policies) == 1 else "tie",
        "selected_policies": regret_policies,
        "undominated_policies": undominated,
        "dominated_by": dominated_by,
        "policy_metrics": metrics,
        "minimax_regret": {"policies": regret_policies, "maximum_regret": least_regret},
        "maximin_gain": {"policies": gain_policies, "minimum_gain": greatest_lower_gain},
        "common_improving_policies": improving,
        "baseline_dominated_by": dominated_by["baseline"],
    }


def boundary_values(
    config: Configuration, model_id: str, beta: Fraction
) -> dict[str, Fraction]:
    """Locate exact equality boundaries without discretizing sensitivity.

    Parameters
    ----------
    config : Configuration
        Validated affine-model inputs; positive denominators are required.
    model_id : str
        Declared routing interpretation.
    beta : Fraction
        Exposure coefficient in the configured interval.

    Returns
    -------
    boundaries : dict of Fraction
        A beats baseline above ``a_positive_above_d_a`` and beats B above
        ``a_beats_b_above_d_a``. B beats baseline above
        ``b_positive_above_beta``. Equality is a tie; thresholds may lie outside
        the approved rectangle. All thresholds are dimensionless.
    """
    row = evaluate(config, model_id, beta, config.d_a_bounds[0])
    denominator = row["q_a"] * config.response_value
    x_b = config.exposures[model_id][1]
    return {
        "a_positive_above_d_a": config.inspection_cost / denominator,
        "a_beats_b_above_d_a": (row["g_b"] + config.inspection_cost) / denominator,
        "b_positive_above_beta": (
            config.inspection_cost / (config.d_b * config.response_value) - config.q0
        ) / x_b,
    }


def rectangle_summary(config: Configuration) -> dict[str, Any]:
    """Bound gains and comparisons over the full closed parameter rectangle.

    Parameters
    ----------
    config : Configuration
        Validated affine-model inputs and closed beta/sensitivity intervals.

    Returns
    -------
    summary : dict
        Exact minimum/maximum gains and differences per model, corner witnesses,
        and both revised criteria per model and across all models, alongside
        the explicitly historical strict-rule diagnostic.

    Notes
    -----
    Each gain and A-minus-B difference is affine in either coordinate with the
    other fixed. Every interior value is a convex combination of the four
    corner values. Corner extrema therefore bound the continuous rectangle
    exactly, rather than approximating it by a sampled grid.
    Worst regret is the maximum over pairwise gain differences, so maximizing
    it over the rectangle likewise reduces exactly to these corner witnesses.
    """
    models = {}
    all_corners = []
    for model_id in config.exposures:
        corners = [
            evaluate(config, model_id, beta, d_a)
            for beta, d_a in product(config.beta_bounds, config.d_a_bounds)
        ]
        all_corners.extend(corners)
        models[model_id] = {
            "bounds": {
                key: {"minimum": min(row[key] for row in corners),
                      "maximum": max(row[key] for row in corners)}
                for key in ("g_a", "g_b", "a_minus_b")
            },
            "corner_evaluations": corners,
            "decision": model_set_decision(corners),
            "historical_strict_rule": historical_strict_decision(corners),
        }
    return {
        "justification": "Gains and differences are bilinear; extrema occur at rectangle corners.",
        "models": models,
        "all_models_decision": model_set_decision(all_corners),
        "historical_strict_rule": historical_strict_decision(all_corners),
    }


def build_report(config: Configuration) -> dict[str, Any]:
    """Calculate representative cases, continuous boundaries, and exact bounds.

    Parameters
    ----------
    config : Configuration
        Authoritative input configuration; no values are estimated or fitted.

    Returns
    -------
    report : dict
        Deterministic report retaining Fractions until serialization, including
        input provenance and baseline-dominance diagnostics for every case.
    """
    cases = []
    for case in config.raw["representative_cases"]:
        beta, d_a = _fraction(case["beta"]), _fraction(case["d_a"])
        models = {
            model_id: evaluate(config, model_id, beta, d_a)
            for model_id in config.exposures
        }
        cases.append({
            "id": case["id"], "beta": beta, "d_a": d_a, "models": models,
            "model_set": model_set_decision(list(models.values())),
            "historical_strict_rule": historical_strict_decision(list(models.values())),
            "boundaries": {
                model_id: boundary_values(config, model_id, beta)
                for model_id in config.exposures
            },
        })
    coefficients = {
        model_id: {
            "g_a_constant": -config.inspection_cost,
            "g_a_d_a": config.q0 * config.response_value,
            "g_a_beta_d_a": x_a * config.response_value,
            "g_b_constant": config.q0 * config.d_b * config.response_value - config.inspection_cost,
            "g_b_beta": x_b * config.d_b * config.response_value,
        }
        for model_id, (x_a, x_b) in config.exposures.items()
    }
    return {
        "inputs": config.raw,
        "interpretation": "Exact hypothetical decision calculation; no physical-failure or station-performance estimates.",
        "model_specific_regions": {
            "coefficients": coefficients,
            "A_strictly_preferred": "d_A > max(a_positive_above_d_a, a_beats_b_above_d_a)",
            "B_strictly_preferred": "beta > b_positive_above_beta and d_A < a_beats_b_above_d_a",
            "baseline_weakly_dominates": "beta <= b_positive_above_beta and d_A <= a_positive_above_d_a",
            "ties": "Equality in a required comparison prevents strict preference.",
        },
        "decision_protocol": {
            "main": "Minimax regret among pointwise-undominated deterministic policies.",
            "comparator": "Maximin incremental gain among the same undominated policies.",
            "ties": "All equal criterion optimizers are retained; equivalent gain vectors do not dominate each other.",
            "nonnegative_gain_gate": False,
            "negative_gain_states": "Zero-based indices of the supplied evaluations; a selected policy can lose relative to baseline in a retained model.",
            "historical_strict_rule": "Retired diagnostic only; its fallback can select a dominated baseline.",
            "absolute_loss_caution": "Maximin incremental gain need not minimize worst absolute loss when model-specific baseline losses differ.",
        },
        "selector_boundaries": selector_boundaries(config),
        "representative_cases": cases,
        "full_rectangle": rectangle_summary(config),
    }


def selector_boundaries(config: Configuration) -> dict[str, Any]:
    """Derive the two-route selector curves from the approved coefficients.

    Parameters
    ----------
    config : Configuration
        Inputs for the approved two-route geometry: common B exposure, ordered
        A exposures, and B weakly preferable to A under the second route.

    Returns
    -------
    boundaries : dict
        Exact rational coefficients of the lower (A/baseline) and upper (A/B)
        minimax-regret curves, their junction, top-domain entry, and the common
        beta threshold for B's positive gain and the maximin-gain selector.
        Curves have the form (numerator_constant + numerator_beta * beta) /
        (denominator_constant + denominator_beta * beta).

    Raises
    ------
    ValueError
        If a configuration changes the approved two-route geometry. Generic
        finite-set evaluation is available independently of this plot helper.

    Notes
    -----
    Below B's zero-gain threshold, equal A/baseline regret requires
    G_A(m1) = -G_A(m2); above it equal A/B regret requires
    G_A(m1) - G_B = G_B - G_A(m2). These yield the two curves in the project's
    Round 1 assessment. No empirical parameters or sampled inference are added.
    """
    if set(config.exposures) != {"m1", "m2"}:
        raise ValueError("Selector geometry requires the two approved routing models.")
    x_a1, x_b1 = config.exposures["m1"]
    x_a2, x_b2 = config.exposures["m2"]
    if not (x_b1 == x_b2 and x_a1 > x_a2 and config.d_a_bounds[1] <= config.d_b):
        raise ValueError("Selector geometry requires common B exposure and ordered A routes.")
    if x_a2 > x_b2:
        raise ValueError("Selector geometry requires B to weakly beat A under route m2.")
    denominator_constant = 2 * config.q0 * config.response_value
    denominator_beta = (x_a1 + x_a2) * config.response_value
    beta_zero_b = (config.inspection_cost / (config.d_b * config.response_value)
                   - config.q0) / x_b1
    lower = {
        "numerator_constant": 2 * config.inspection_cost,
        "numerator_beta": Fraction(0),
        "denominator_constant": denominator_constant,
        "denominator_beta": denominator_beta,
    }
    upper = {
        "numerator_constant": 2 * config.q0 * config.d_b * config.response_value,
        "numerator_beta": 2 * x_b1 * config.d_b * config.response_value,
        "denominator_constant": denominator_constant,
        "denominator_beta": denominator_beta,
    }
    beta_entry = (2 * config.inspection_cost / config.d_a_bounds[1]
                  - denominator_constant) / denominator_beta
    junction = curve_sensitivity(lower, beta_zero_b)
    if not (config.beta_bounds[0] <= beta_entry < beta_zero_b < config.beta_bounds[1]
            and config.d_a_bounds[0] < junction < config.d_a_bounds[1]
            and config.d_a_bounds[0] < curve_sensitivity(upper, config.beta_bounds[1])
            < config.d_a_bounds[1]):
        raise ValueError("Selector curves no longer have the approved domain intersections.")
    return {
        "beta_zero_b": beta_zero_b,
        "beta_entry_a": beta_entry,
        "triple_tie": [beta_zero_b, junction],
        "minimax_regret": {
            "below_beta_zero_b": lower,
            "above_beta_zero_b": upper,
            "interpretation": "A above each curve; baseline below the lower-beta curve; B below the upper-beta curve. Equality retains both, with a triple tie at their junction.",
        },
        "maximin_gain": {
            "beta_boundary": beta_zero_b,
            "interpretation": "Baseline below this beta, B above it, and baseline/B tied at equality for all approved d_A.",
        },
    }


def curve_sensitivity(coefficients: dict[str, Fraction], beta: Fraction) -> Fraction:
    """Evaluate an exported rational equality curve at an exact coefficient.

    Parameters
    ----------
    coefficients : dict of Fraction
        Numerator/denominator constant and beta coefficients from
        ``selector_boundaries``. The configured denominator is positive.
    beta : Fraction
        Dimensionless exposure coefficient on the stated branch interval.

    Returns
    -------
    d_a : Fraction
        Exact dimensionless detection sensitivity at equality.
    """
    return ((coefficients["numerator_constant"] + coefficients["numerator_beta"] * beta)
            / (coefficients["denominator_constant"] + coefficients["denominator_beta"] * beta))


def build_plot_data(config: Configuration, samples_per_curve: int = 201) -> dict[str, Any]:
    """Export complete drawing geometry without delegating analysis to a plotter.

    Parameters
    ----------
    config : Configuration
        Authoritative inputs for the approved two-route parameter domain.
    samples_per_curve : int, optional
        Number of equally spaced rational beta coordinates per curved boundary,
        including both endpoints. This controls drawing interpolation only;
        analytic boundaries and decisions are independent of sampling density.

    Returns
    -------
    plot_data : dict
        Exact domain, closed region polygons, sampled equality curves, straight
        tie segments, tie points, and label anchors for the two criteria. Region
        polygons share tie boundaries; their interiors denote unique choices.

    Raises
    ------
    ValueError
        If fewer than two curve coordinates are requested or the supported
        domain geometry is changed.
    """
    if not isinstance(samples_per_curve, int) or samples_per_curve < 2:
        raise ValueError("At least two drawing coordinates per curve are required.")
    bounds = selector_boundaries(config)
    beta_min, beta_max = config.beta_bounds
    d_min, d_max = config.d_a_bounds
    entry, threshold = bounds["beta_entry_a"], bounds["beta_zero_b"]
    junction = bounds["triple_tie"][1]

    def points(curve: dict[str, Fraction], start: Fraction, stop: Fraction) -> list[list[Fraction]]:
        coordinates = [start + (stop - start) * index / (samples_per_curve - 1)
                       for index in range(samples_per_curve)]
        return [[beta, curve_sensitivity(curve, beta)] for beta in coordinates]

    lower = points(bounds["minimax_regret"]["below_beta_zero_b"], entry, threshold)
    upper = points(bounds["minimax_regret"]["above_beta_zero_b"], threshold, beta_max)
    mid_beta = (threshold + beta_max) / 2
    mid_curve = curve_sensitivity(bounds["minimax_regret"]["above_beta_zero_b"], mid_beta)
    baseline_anchor = [(beta_min + entry) / 2, (d_min + d_max) / 2]
    regions = [
        {"policy": "baseline", "polygon": [[beta_min, d_min], [threshold, d_min],
             *reversed(lower), [beta_min, d_max], [beta_min, d_min]],
         "label_anchor": baseline_anchor},
        {"policy": "A", "polygon": [*lower, *upper[1:], [beta_max, d_max], lower[0]],
         "label_anchor": [mid_beta, (mid_curve + d_max) / 2]},
        {"policy": "B", "polygon": [[threshold, d_min], [beta_max, d_min],
             *reversed(upper), [threshold, d_min]],
         "label_anchor": [mid_beta, (d_min + mid_curve) / 2]},
    ]
    return {
        "schema_version": 1,
        "domain": {"beta": config.beta_bounds, "d_a": config.d_a_bounds},
        "policy_labels": {"baseline": "Schedule", "A": "Inspect A", "B": "Inspect B"},
        "interpretation": "Each point retains both routing models at fixed beta and d_A; no model probabilities or robust nonnegative-gain gate are imposed.",
        "geometry_note": "Polygons use exact rational samples of analytical curves for rendering only. Shared edges are ties, not assignments to either adjacent interior.",
        "samples_per_curve": samples_per_curve,
        "analytical_boundaries": bounds,
        "panels": {
            "minimax_regret": {
                "title": "Minimax regret", "regions": regions,
                "boundaries": [
                    {"policies": ["baseline", "A"], "points": lower},
                    {"policies": ["A", "B"], "points": upper},
                    {"policies": ["baseline", "B"], "points": [[threshold, d_min], [threshold, junction]]},
                ],
                "tie_points": [{"policies": list(POLICIES), "point": [threshold, junction]}],
            },
            "maximin_gain": {
                "title": "Maximin incremental gain",
                "regions": [
                    {"policy": "baseline", "polygon": [[beta_min, d_min], [threshold, d_min],
                         [threshold, d_max], [beta_min, d_max], [beta_min, d_min]],
                     "label_anchor": [(beta_min + threshold) / 2, (d_min + d_max) / 2]},
                    {"policy": "B", "polygon": [[threshold, d_min], [beta_max, d_min],
                         [beta_max, d_max], [threshold, d_max], [threshold, d_min]],
                     "label_anchor": [mid_beta, (d_min + d_max) / 2]},
                ],
                "boundaries": [{"policies": ["baseline", "B"],
                                "points": [[threshold, d_min], [threshold, d_max]]}],
                "tie_points": [],
            },
        },
    }


def _exact_json(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, dict):
        return {key: _exact_json(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_exact_json(item) for item in value]
    return value


def _tex_number(value: Fraction) -> str:
    """Display terminating rationals as exact decimals and others as fractions.

    Parameters
    ----------
    value : Fraction
        Exact value; no precision or rounding tolerance is introduced.

    Returns
    -------
    text : str
        Minimal decimal text when the denominator contains only factors two and
        five; otherwise a signed LaTeX fraction.
    """
    if value.denominator == 1:
        return str(value.numerator)
    sign = "-" if value < 0 else ""
    remaining = value.denominator
    twos = fives = 0
    while remaining % 2 == 0:
        remaining //= 2
        twos += 1
    while remaining % 5 == 0:
        remaining //= 5
        fives += 1
    if remaining == 1:
        places = max(twos, fives)
        scaled = abs(value.numerator) * 2 ** (places - twos) * 5 ** (places - fives)
        digits = str(scaled).zfill(places + 1)
        return sign + digits[:-places] + "." + digits[-places:].rstrip("0")
    return rf"{sign}\frac{{{abs(value.numerator)}}}{{{value.denominator}}}"


def _tex_policies(policies: list[str]) -> str:
    labels = ["0" if policy == "baseline" else policy for policy in policies]
    return labels[0] if len(labels) == 1 else r"\{" + ",".join(labels) + r"\}"


def _latex_table(report: dict[str, Any]) -> str:
    """Format the approved gains and both criteria with explicit policy ties.

    Parameters
    ----------
    report : dict
        Report produced by ``build_report``, with rational gains for m1 and m2.
    """
    lines = [
        "% Generated by simulations/two_door/calculate.py; do not edit.",
        r"\begin{table}[t]",
        r"\centering",
        r"\caption{Exact hypothetical inspection comparisons under the two routing models. Gains use arbitrary loss units; $0$ denotes the existing schedule and braces denote ties. Both criteria operate on the undominated deterministic policies. Minimax regret can select a policy with negative gain under one retained model; maximin refers to incremental gain relative to the model-specific baseline.}",
        r"\label{tab:two-door-numerical}",
        r"\small",
        r"\begin{tabular}{@{}ccccccc@{}}",
        r"\toprule",
        r"$\beta$ & $d_A$ & $G_A(m_1)$ & $G_A(m_2)$ & $G_B$ & Minimax regret & Maximin gain \\",
        r"\midrule",
    ]
    for case in report["representative_cases"]:
        first, second = case["models"]["m1"], case["models"]["m2"]
        numeric = [case["beta"], case["d_a"], first["g_a"], second["g_a"], first["g_b"]]
        cells = ["$" + _tex_number(value) + "$" for value in numeric]
        for criterion in ("minimax_regret", "maximin_gain"):
            cells.append("$" + _tex_policies(case["model_set"][criterion]["policies"]) + "$")
        lines.append(" & ".join(cells) + r" \\")
    lines.extend([r"\bottomrule", r"\end{tabular}", r"\end{table}"])
    return "\n".join(lines) + "\n"


def write_artifacts(
    report: dict[str, Any], json_path: Path, tex_path: Path,
    plot_data: dict[str, Any], plot_path: Path,
) -> None:
    """Write byte-stable exact results and the generated manuscript table.

    Parameters
    ----------
    report : dict
        Output of ``build_report``; Fractions serialize as exact rational strings.
    json_path, tex_path, plot_path : pathlib.Path
        Destinations, with parent directories created if absent. Existing generated
        files are replaced; no timestamp or machine-specific path is embedded.
    plot_data : dict
        Authoritative drawing geometry from ``build_plot_data``. The renderer
        consumes these coordinates without recomputing decisions.

    Returns
    -------
    None
        Results are written to the three requested paths.
    """
    for path in (json_path, tex_path, plot_path):
        path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(_exact_json(report), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tex_path.write_text(_latex_table(report), encoding="utf-8")
    plot_path.write_text(json.dumps(_exact_json(plot_data), indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    """Regenerate all artifacts from the configured exact input file.

    Returns
    -------
    None
        Command-line destinations receive JSON and LaTeX; errors propagate.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DIRECTORY / "parameters.json")
    parser.add_argument("--json-output", type=Path, default=DIRECTORY / "results.json")
    parser.add_argument("--tex-output", type=Path, default=REPOSITORY / "paper/generated/two_door_results.tex")
    parser.add_argument("--plot-output", type=Path, default=DIRECTORY / "plot_data.json")
    args = parser.parse_args()
    config = load_config(args.config)
    write_artifacts(build_report(config), args.json_output, args.tex_output,
                    build_plot_data(config), args.plot_output)


if __name__ == "__main__":
    main()
