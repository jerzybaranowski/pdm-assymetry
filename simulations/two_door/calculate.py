#!/usr/bin/env python3
"""Exact synthetic inspection comparisons for the approved two-door example.

The arithmetic implements Sections 3--5 and 8 of
``notes/12_two_door_model_specification.md``. Inputs describe actionable
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


def model_set_decision(evaluations: list[dict[str, Any]]) -> dict[str, Any]:
    """Apply the stipulated strict-preference rule to a nonempty finite set.

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
        and strict-preference decisions per model and across all models.

    Notes
    -----
    Each gain and A-minus-B difference is affine in either coordinate with the
    other fixed. Every interior value is a convex combination of the four
    corner values. Corner extrema therefore bound the continuous rectangle
    exactly, rather than approximating it by a sampled grid.
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
        }
    return {
        "justification": "Gains and differences are bilinear; extrema occur at rectangle corners.",
        "models": models,
        "all_models_decision": model_set_decision(all_corners),
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
        "continuous_regions": {
            "coefficients": coefficients,
            "A_strictly_preferred": "d_A > max(a_positive_above_d_a, a_beats_b_above_d_a)",
            "B_strictly_preferred": "beta > b_positive_above_beta and d_A < a_beats_b_above_d_a",
            "baseline_weakly_dominates": "beta <= b_positive_above_beta and d_A <= a_positive_above_d_a",
            "ties": "Equality in a required comparison prevents strict preference.",
        },
        "representative_cases": cases,
        "full_rectangle": rectangle_summary(config),
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
    """Format exact policy comparisons without treating fallback as optimal.

    Parameters
    ----------
    report : dict
        Report produced by ``build_report``, with rational gains for m1 and m2.
    """
    lines = [
        "% Generated by simulations/two_door/calculate.py; do not edit.",
        r"\begin{table}[t]",
        r"\centering",
        r"\caption{Exact hypothetical inspection comparisons. Gains use arbitrary loss units. The $m_1/m_2$ column lists the loss-minimizing policies within each model; $0$ denotes the existing schedule and braces denote ties. The final column applies the strict common-preference rule to both routing models. A dagger marks its stipulated fallback, which need not minimize loss.}",
        r"\label{tab:two-door-numerical}",
        r"\small",
        r"\begin{tabular}{@{}ccccccc@{}}",
        r"\toprule",
        r"$\beta$ & $d_A$ & $G_A(m_1)$ & $G_A(m_2)$ & $G_B$ & $m_1/m_2$ & Both models \\",
        r"\midrule",
    ]
    for case in report["representative_cases"]:
        first, second = case["models"]["m1"], case["models"]["m2"]
        numeric = [case["beta"], case["d_a"], first["g_a"], second["g_a"], first["g_b"]]
        cells = ["$" + _tex_number(value) + "$" for value in numeric]
        cells.append("$" + _tex_policies(first["optimal_policies"]) + "/"
                     + _tex_policies(second["optimal_policies"]) + "$")
        choice = case["model_set"]["choice"]
        cells.append({"baseline": "$0$", "fallback": r"$0^{\dagger}$"}.get(choice, "$" + choice + "$"))
        lines.append(" & ".join(cells) + r" \\")
    lines.extend([r"\bottomrule", r"\end{tabular}", r"\end{table}"])
    return "\n".join(lines) + "\n"


def write_artifacts(report: dict[str, Any], json_path: Path, tex_path: Path) -> None:
    """Write byte-stable exact results and the generated manuscript table.

    Parameters
    ----------
    report : dict
        Output of ``build_report``; Fractions serialize as exact rational strings.
    json_path, tex_path : pathlib.Path
        Destinations, with parent directories created if absent. Existing generated
        files are replaced; no timestamp or machine-specific path is embedded.

    Returns
    -------
    None
        Results are written to the two requested paths.
    """
    for path in (json_path, tex_path):
        path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(_exact_json(report), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tex_path.write_text(_latex_table(report), encoding="utf-8")


def main() -> None:
    """Regenerate both artifacts from the configured exact input file.

    Returns
    -------
    None
        Command-line destinations receive JSON and LaTeX; errors propagate.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DIRECTORY / "parameters.json")
    parser.add_argument("--json-output", type=Path, default=DIRECTORY / "results.json")
    parser.add_argument("--tex-output", type=Path, default=REPOSITORY / "paper/generated/two_door_results.tex")
    args = parser.parse_args()
    write_artifacts(build_report(load_config(args.config)), args.json_output, args.tex_output)


if __name__ == "__main__":
    main()
