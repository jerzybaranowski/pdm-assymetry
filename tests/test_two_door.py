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
        self.assertEqual(calculate.model_set_decision(rows)["choice"], "fallback")
        self.assertEqual(calculate.model_set_decision(rows)["baseline_dominated_by"], ["A", "B"])

        boundary_rows = [calculate.evaluate(self.config, model, F(1, 45), F(9, 10))
                         for model in self.config.exposures]
        self.assertEqual(boundary_rows[0]["g_a"], F(1, 10))
        self.assertEqual(boundary_rows[1]["g_a"], F(-3, 100))
        self.assertEqual(boundary_rows[1]["g_b"], 0)
        self.assertEqual(boundary_rows[1]["optimal_policies"], ["baseline", "B"])
        self.assertEqual(calculate.model_set_decision(boundary_rows)["choice"], "fallback")
        self.assertEqual(calculate.model_set_decision(boundary_rows)["common_improving_policies"], [])

    def test_model_disagreement_and_rectangle_bounds(self) -> None:
        rows = [calculate.evaluate(self.config, model, F(1, 5), F(9, 10))
                for model in self.config.exposures]
        self.assertEqual([row["optimal_policies"] for row in rows], [["A"], ["B"]])
        decision = calculate.model_set_decision(rows)
        self.assertEqual(decision["choice"], "fallback")
        self.assertEqual(decision["baseline_dominated_by"], ["A", "B"])

        supported = [calculate.evaluate(self.config, model, F(1, 5), F(2, 5))
                     for model in self.config.exposures]
        self.assertEqual(calculate.model_set_decision(supported)["choice"], "B")
        self.assertEqual(calculate.model_set_decision(supported)["common_improving_policies"], ["B"])

        rectangle = calculate.rectangle_summary(self.config)
        self.assertEqual(rectangle["all_models_decision"]["choice"], "fallback")
        self.assertEqual(rectangle["all_models_decision"]["common_improving_policies"], [])
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
            command = [sys.executable, str(calculate.DIRECTORY / "calculate.py"),
                       "--json-output", str(json_path), "--tex-output", str(tex_path)]
            subprocess.run(command, check=True, capture_output=True, text=True)
            initial = (json_path.read_bytes(), tex_path.read_bytes())
            calculate.write_artifacts(calculate.build_report(self.config), json_path, tex_path)
            self.assertEqual(initial, (json_path.read_bytes(), tex_path.read_bytes()))
            self.assertEqual(initial[0], (calculate.DIRECTORY / "results.json").read_bytes())
            self.assertEqual(initial[1], (calculate.REPOSITORY / "paper/generated/two_door_results.tex").read_bytes())
            parsed = json.loads(initial[0])
            tie = next(case for case in parsed["representative_cases"] if case["id"] == "inspection_tie")
            self.assertEqual(tie["models"]["m1"]["g_a"], "4/5")
            self.assertEqual(tie["model_set"]["choice"], "fallback")
            table = initial[1].decode()
            self.assertIn(r"\label{tab:two-door-numerical}", table)
            self.assertIn("$1.475$", table)
            self.assertIn("$-0.32$", table)
            self.assertIn(r"$\frac{1}{45}$", table)


if __name__ == "__main__":
    unittest.main()
