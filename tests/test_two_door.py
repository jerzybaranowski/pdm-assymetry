"""Behavioral checks of the exact hypothetical inspection comparison."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction as F
from pathlib import Path

from simulations.two_door import calculate


class TestTwoDoor(unittest.TestCase):
    """Protect consequential policy comparisons and reproducible exports."""

    def setUp(self) -> None:
        self.config = calculate.load_config()

    def test_dominated_baseline_is_not_reinstated_on_route_disagreement(self) -> None:
        rows = [calculate.evaluate(self.config, model, F(1, 5), F(9, 10))
                for model in self.config.exposures]
        decision = calculate.model_set_decision(rows)
        self.assertEqual(decision["choice"], "A")
        self.assertEqual(decision["dominated_by"]["baseline"], ["A", "B"])
        self.assertEqual(decision["maximin_gain"]["policies"], ["B"])
        self.assertEqual(calculate.historical_strict_decision(rows)["choice"], "fallback")

    def test_gain_matches_independent_outcome_losses(self) -> None:
        for model in self.config.exposures:
            for beta in (F(0), F(1, 5), F(1, 2)):
                for d_a in (F(1, 4), F(2, 5), F(3, 5), F(9, 10)):
                    row = calculate.evaluate(self.config, model, beta, d_a)
                    for suffix, sensitivity in (("a", d_a), ("b", self.config.d_b)):
                        with self.subTest(model=model, beta=beta, d_a=d_a, door=suffix):
                            q = row["q_" + suffix]
                            burden = self.config.inspection_cost
                            avoidable_loss = self.config.response_value
                            # A finite loss fixture: no condition, missed condition,
                            # detected condition. Repair removes the avoidable loss;
                            # the visit is charged even when nothing is detected.
                            outcomes = [
                                (1 - q, F(0), burden),
                                (q * (1 - sensitivity), avoidable_loss, burden + avoidable_loss),
                                (q * sensitivity, avoidable_loss, burden),
                            ]
                            self.assertEqual(sum(prob for prob, _, _ in outcomes), 1)
                            baseline = sum(prob * loss for prob, loss, _ in outcomes)
                            inspection = sum(prob * loss for prob, _, loss in outcomes)
                            self.assertEqual(baseline - inspection, row["g_" + suffix])

    def test_negative_gains_keep_baseline(self) -> None:
        rows = [calculate.evaluate(self.config, model, F(0), F(1, 4))
                for model in self.config.exposures]
        for row in rows:
            self.assertEqual((row["g_a"], row["g_b"]), (F(-3, 4), F(-1, 10)))
            self.assertEqual(row["optimal_policies"], ["baseline"])
        decision = calculate.model_set_decision(rows)
        self.assertEqual(decision["choice"], "baseline")
        self.assertEqual(decision["common_improving_policies"], [])

    def test_inspection_and_baseline_ties(self) -> None:
        rows = [calculate.evaluate(self.config, model, F(1, 5), F(3, 5))
                for model in self.config.exposures]
        self.assertEqual((rows[0]["g_a"], rows[0]["g_b"]), (F(4, 5), F(4, 5)))
        self.assertEqual(rows[0]["optimal_policies"], ["A", "B"])
        self.assertEqual(calculate.historical_strict_decision(rows)["choice"], "fallback")
        self.assertEqual(calculate.historical_strict_decision(rows)["baseline_dominated_by"], ["A", "B"])
        self.assertEqual(calculate.model_set_decision(rows)["selected_policies"], ["B"])

        boundary_rows = [calculate.evaluate(self.config, model, F(1, 45), F(9, 10))
                         for model in self.config.exposures]
        self.assertEqual(boundary_rows[0]["g_a"], F(1, 10))
        self.assertEqual(boundary_rows[1]["g_a"], F(-3, 100))
        self.assertEqual(boundary_rows[1]["g_b"], 0)
        self.assertEqual(boundary_rows[1]["optimal_policies"], ["baseline", "B"])
        self.assertEqual(calculate.historical_strict_decision(boundary_rows)["choice"], "fallback")
        self.assertEqual(calculate.historical_strict_decision(boundary_rows)["common_improving_policies"], [])

    def test_model_disagreement_and_rectangle_bounds(self) -> None:
        rows = [calculate.evaluate(self.config, model, F(1, 5), F(9, 10))
                for model in self.config.exposures]
        self.assertEqual([row["optimal_policies"] for row in rows], [["A"], ["B"]])
        decision = calculate.historical_strict_decision(rows)
        self.assertEqual(decision["choice"], "fallback")
        self.assertEqual(decision["baseline_dominated_by"], ["A", "B"])

        supported = [calculate.evaluate(self.config, model, F(1, 5), F(2, 5))
                     for model in self.config.exposures]
        self.assertEqual(calculate.model_set_decision(supported)["choice"], "B")
        self.assertEqual(calculate.model_set_decision(supported)["common_improving_policies"], ["B"])

        rectangle = calculate.rectangle_summary(self.config)
        self.assertEqual(rectangle["historical_strict_rule"]["choice"], "fallback")
        self.assertEqual(rectangle["all_models_decision"]["common_improving_policies"], [])
        self.assertEqual(rectangle["all_models_decision"]["minimax_regret"],
                         {"policies": ["B"], "maximum_regret": F(9, 4)})
        self.assertEqual(rectangle["all_models_decision"]["maximin_gain"],
                         {"policies": ["baseline"], "minimum_gain": F(0)})
        self.assertEqual({policy: scores["maximum_regret"] for policy, scores
                          in rectangle["all_models_decision"]["policy_metrics"].items()},
                         {"baseline": F(22, 5), "A": F(197, 80), "B": F(9, 4)})
        expected = {
            "m1": {"g_a": (F(-3, 4), F(22, 5)), "g_b": (F(-1, 10), F(43, 20)),
                   "a_minus_b": (F(-33, 20), F(9, 4))},
            "m2": {"g_a": (F(-3, 4), F(59, 40)), "g_b": (F(-1, 10), F(43, 20)),
                   "a_minus_b": (F(-197, 80), F(0))},
        }
        for model, quantities in expected.items():
            for key, limits in quantities.items():
                self.assertEqual(rectangle["models"][model]["bounds"][key],
                                 {"minimum": limits[0], "maximum": limits[1]})

    def test_continuous_boundaries(self) -> None:
        for model in self.config.exposures:
            bounds = calculate.boundary_values(self.config, model, F(1, 5))
            self.assertEqual(bounds["b_positive_above_beta"], F(1, 45))
            zero_a = calculate.evaluate(self.config, model, F(1, 5), bounds["a_positive_above_d_a"])
            self.assertEqual(zero_a["g_a"], 0)
        bounds = calculate.boundary_values(self.config, "m1", F(1, 5))
        self.assertEqual(bounds["a_beats_b_above_d_a"], F(3, 5))
        self.assertEqual(calculate.evaluate(self.config, "m1", F(1, 5), F(3, 5))["a_minus_b"], 0)
        corrected = calculate.boundary_values(self.config, "m2", F(1, 5))
        self.assertEqual(corrected["a_beats_b_above_d_a"], F(18, 17))
        self.assertGreater(corrected["a_beats_b_above_d_a"], self.config.d_a_bounds[1])
        # At beta=0 the models coincide; above it, B's larger exposure and
        # no-worse detection rule out a strictly preferred A under m2.
        self.assertEqual(calculate.boundary_values(self.config, "m2", F(0))["a_beats_b_above_d_a"], F(9, 10))

    def test_dominance_and_policy_equivalence(self) -> None:
        # B equals A under m1 and improves it under m2: weak dominance must
        # exclude A even though the first model alone retains an A/B tie.
        rows = [calculate.evaluate(self.config, model, F(1, 5), F(3, 5))
                for model in self.config.exposures]
        decision = calculate.model_set_decision(rows)
        self.assertEqual(decision["dominated_by"]["A"], ["B"])
        self.assertEqual(decision["undominated_policies"], ["B"])
        # At this lower sensitivity B and baseline have equivalent gain
        # vectors. Neither dominates the other; A is strictly inferior.
        rows = [calculate.evaluate(self.config, model, F(1, 45), F(1, 4))
                for model in self.config.exposures]
        decision = calculate.model_set_decision(rows)
        self.assertEqual(decision["undominated_policies"], ["baseline", "B"])
        self.assertEqual(decision["dominated_by"]["A"], ["baseline", "B"])
        self.assertEqual(decision["selected_policies"], ["baseline", "B"])
        self.assertEqual(decision["choice"], "tie")
        # A separate finite-set fixture makes all worst gains equal. Dominance
        # must still remove A and baseline before maximin reports its choices.
        decision = calculate.model_set_decision([
            {"g_a": F(0), "g_b": F(0)}, {"g_a": F(1), "g_b": F(2)}])
        self.assertEqual(decision["maximin_gain"]["policies"], ["B"])
        self.assertEqual(decision["policy_metrics"]["A"]["minimum_gain"], F(0))

    def test_criteria_scores_and_negative_gain_selection(self) -> None:
        report = calculate.build_report(self.config)
        expected = [
            (["baseline"], ["baseline"], F(0), F(0)),
            (["A"], ["B"], F(27, 100), F(4, 5)),
            (["B"], ["B"], F(0), F(4, 5)),
            (["B"], ["B"], F(0), F(4, 5)),
            (["A"], ["baseline", "B"], F(3, 100), F(0)),
            (["A"], ["B"], F(27, 40), F(43, 20)),
        ]
        for case, (regret_policies, gain_policies, regret, lower_gain) in zip(
                report["representative_cases"], expected):
            with self.subTest(case=case["id"]):
                decision = case["model_set"]
                self.assertEqual(decision["minimax_regret"],
                                 {"policies": regret_policies, "maximum_regret": regret})
                self.assertEqual(decision["maximin_gain"],
                                 {"policies": gain_policies, "minimum_gain": lower_gain})
        boundary = report["representative_cases"][4]["model_set"]
        self.assertEqual(boundary["policy_metrics"]["A"]["minimum_gain"], F(-3, 100))
        self.assertEqual(boundary["policy_metrics"]["A"]["negative_gain_states"], [1])
        self.assertEqual(boundary["selected_policies"], ["A"])

    def test_regret_matches_independent_absolute_losses(self) -> None:
        # Arbitrary, unequal model baselines cancel in within-model regret.
        # This fixture checks the definition through absolute losses and also
        # exposes why maximin *gain* is not minimax absolute loss.
        rows = [calculate.evaluate(self.config, model, F(1, 5), F(9, 10))
                for model in self.config.exposures]
        decision = calculate.model_set_decision(rows)
        losses = [
            {"baseline": F(100), "A": F(983, 10), "B": F(496, 5)},
            {"baseline": F(10), "A": F(947, 100), "B": F(46, 5)},
        ]
        for policy in calculate.POLICIES:
            regret = max(row[policy] - min(row.values()) for row in losses)
            self.assertEqual(regret, decision["policy_metrics"][policy]["maximum_regret"])
        worst_losses = {policy: max(row[policy] for row in losses)
                        for policy in calculate.POLICIES}
        self.assertEqual(min(worst_losses, key=worst_losses.get), "A")
        self.assertEqual(decision["maximin_gain"]["policies"], ["B"])

    def test_selector_boundaries_and_plot_regions(self) -> None:
        boundaries = calculate.selector_boundaries(self.config)
        self.assertEqual(boundaries["beta_zero_b"], F(1, 45))
        self.assertEqual(boundaries["beta_entry_a"], F(4, 243))
        self.assertEqual(boundaries["triple_tie"], [F(1, 45), F(20, 23)])
        plot = calculate.build_plot_data(self.config)
        for criterion, panel in plot["panels"].items():
            for region in panel["regions"]:
                self.assertEqual(region["polygon"][0], region["polygon"][-1])
                for beta, d_a in region["polygon"]:
                    self.assertTrue(self.config.beta_bounds[0] <= beta <= self.config.beta_bounds[1])
                    self.assertTrue(self.config.d_a_bounds[0] <= d_a <= self.config.d_a_bounds[1])
                beta, d_a = region["label_anchor"]
                rows = [calculate.evaluate(self.config, model, beta, d_a)
                        for model in self.config.exposures]
                self.assertEqual(calculate.model_set_decision(rows)[criterion]["policies"],
                                 [region["policy"]])
            for boundary in panel["boundaries"]:
                for beta, d_a in boundary["points"]:
                    rows = [calculate.evaluate(self.config, model, beta, d_a)
                            for model in self.config.exposures]
                    tied = calculate.model_set_decision(rows)[criterion]["policies"]
                    self.assertTrue(set(boundary["policies"]).issubset(tied))
                    # Samples lie on exact ties; arbitrarily fine drawing
                    # coordinates must never determine the analytic selector.
                    if criterion == "minimax_regret" and "A" in boundary["policies"]:
                        for direction, expected_policy in ((-1, boundary["policies"][0]
                                if boundary["policies"][0] != "A" else "B"), (1, "A")):
                            shifted = d_a + direction * F(1, 10**8)
                            if self.config.d_a_bounds[0] <= shifted <= self.config.d_a_bounds[1] and beta != F(1, 45):
                                shifted_rows = [calculate.evaluate(self.config, model, beta, shifted)
                                                for model in self.config.exposures]
                                self.assertEqual(calculate.model_set_decision(shifted_rows)[criterion]["policies"],
                                                 [expected_policy])
        triple_rows = [calculate.evaluate(self.config, model, F(1, 45), F(20, 23))
                       for model in self.config.exposures]
        self.assertEqual(calculate.model_set_decision(triple_rows)["selected_policies"],
                         ["baseline", "A", "B"])
        with self.assertRaises(ValueError):
            calculate.build_plot_data(self.config, samples_per_curve=1)

    def test_invalid_inputs_are_rejected(self) -> None:
        for beta, d_a in ((F(-1), F(1, 2)), (F(1), F(1, 2)),
                          (F(0), F(1, 5)), (F(0), F(1)), (0.2, F(1, 2))):
            with self.subTest(beta=beta, d_a=d_a), self.assertRaises(ValueError):
                calculate.evaluate(self.config, "m1", beta, d_a)
        with self.assertRaises(ValueError):
            calculate.model_set_decision([])
        with self.assertRaises(ValueError):
            calculate.evaluate(self.config, "absent", F(0), F(1, 2))
        for key, value in (("false_positive_probability", "0.1"), ("q0", 0.1),
                           ("q0", "0.8"), ("beta_bounds", ["0.5", "0"]),
                           ("response_value", "0")):
            with tempfile.TemporaryDirectory() as directory:
                raw = dict(self.config.raw)
                raw[key] = value
                path = Path(directory) / "invalid.json"
                path.write_text(json.dumps(raw), encoding="utf-8")
                with self.subTest(key=key), self.assertRaises(ValueError):
                    calculate.load_config(path)

    def test_artifacts_reproduce_exactly(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            json_path, tex_path = Path(directory) / "results.json", Path(directory) / "table.tex"
            plot_path = Path(directory) / "plot.json"
            command = [sys.executable, str(calculate.DIRECTORY / "calculate.py"),
                       "--json-output", str(json_path), "--tex-output", str(tex_path),
                       "--plot-output", str(plot_path)]
            subprocess.run(command, check=True, capture_output=True, text=True)
            initial = (json_path.read_bytes(), tex_path.read_bytes(), plot_path.read_bytes())
            calculate.write_artifacts(calculate.build_report(self.config), json_path, tex_path,
                                      calculate.build_plot_data(self.config), plot_path)
            self.assertEqual(initial, (json_path.read_bytes(), tex_path.read_bytes(), plot_path.read_bytes()))
            self.assertEqual(initial[0], (calculate.DIRECTORY / "results.json").read_bytes())
            self.assertEqual(initial[1], (calculate.REPOSITORY / "paper/generated/two_door_results.tex").read_bytes())
            self.assertEqual(initial[2], (calculate.DIRECTORY / "plot_data.json").read_bytes())
            parsed = json.loads(initial[0])
            tie = next(case for case in parsed["representative_cases"] if case["id"] == "inspection_tie")
            self.assertEqual(tie["models"]["m1"]["g_a"], "4/5")
            self.assertEqual(tie["historical_strict_rule"]["choice"], "fallback")
            self.assertEqual(tie["model_set"]["choice"], "B")
            table = initial[1].decode()
            self.assertIn(r"\label{tab:two-door-numerical}", table)
            self.assertIn("$1.475$", table)
            self.assertIn("$-0.32$", table)
            self.assertIn(r"$\frac{1}{45}$", table)
            self.assertIn(r"$\{0,B\}$", table)
            self.assertIn("Minimax regret", table)
            self.assertIn("Maximin gain", table)


if __name__ == "__main__":
    unittest.main()
