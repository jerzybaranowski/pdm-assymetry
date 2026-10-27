"""Protect the analytical-artifact boundary and the fixed-size figure export."""

from __future__ import annotations

from dataclasses import replace
from fractions import Fraction
import json
from pathlib import Path
import tempfile
import unittest

import fitz
import numpy as np
from PIL import Image

from scripts import plot_two_door as plot


class TestTwoDoorFigure(unittest.TestCase):
    """Check scientific geometry fidelity and inspect actual saved artifacts."""

    def setUp(self) -> None:
        self.config = plot.load_figure_config()
        self.data = plot.load_plot_data(self.config.source_path)

    def test_invalid_geometry_is_rejected(self) -> None:
        raw = json.loads(self.config.source_path.read_text())
        mutations = [
            lambda x: x.pop("panels"),
            lambda x: x["domain"].update(beta=["1/2", "0"]),
            lambda x: x["panels"]["minimax_regret"]["regions"][0].update(policy="unknown"),
            lambda x: x["panels"]["minimax_regret"]["regions"][0]["polygon"].__setitem__(0, ["nan", "1/2"]),
            lambda x: x["panels"]["minimax_regret"]["regions"][0]["polygon"].__setitem__(0, ["-1", "1/2"]),
        ]
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / "invalid.json"
            for mutation in mutations:
                case = json.loads(json.dumps(raw))
                mutation(case)
                source.write_text(json.dumps(case))
                with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                    plot.load_plot_data(source)

    def test_panels_preserve_exported_geometry_and_legible_labels(self) -> None:
        raw = json.loads(self.config.source_path.read_text())
        figure, axes = plot.build_two_door_decisions(self.data, self.config)
        figure.canvas.draw()
        self.assertEqual(len(axes), 2)
        for ax, panel_id in zip(axes, plot.PANEL_IDS):
            panel = raw["panels"][panel_id]
            self.assertEqual(len(ax.patches), len(panel["regions"]))
            for patch, region in zip(ax.patches, panel["regions"]):
                expected = [[float(Fraction(v)) for v in point] for point in region["polygon"]]
                np.testing.assert_array_equal(patch.get_xy(), expected)
                self.assertEqual(patch.get_gid(), "policy-" + region["policy"])
            self.assertEqual(len(ax.lines), len(panel["boundaries"]) + len(panel["tie_points"]))
            for line, boundary in zip(ax.lines, panel["boundaries"]):
                expected = [[float(Fraction(v)) for v in point] for point in boundary["points"]]
                np.testing.assert_array_equal(line.get_xydata(), expected)
            for line, tie in zip(ax.lines[len(panel["boundaries"]):], panel["tie_points"]):
                np.testing.assert_array_equal(line.get_xydata()[0], [float(Fraction(v)) for v in tie["point"]])
            self.assertEqual(set(text.get_text() for text in ax.texts),
                             {raw["policy_labels"][r["policy"]] for r in panel["regions"]})
            # Test text extents rather than annotation extents, which include leaders.
            boxes = [text.get_bbox_patch().get_window_extent() if text.get_bbox_patch()
                     else text._get_layout(figure.canvas.get_renderer())[0].translated(*text.get_transform().transform(text.get_position()))
                     for text in ax.texts]
            for index, box in enumerate(boxes):
                for other in boxes[index + 1:]:
                    self.assertFalse(box.overlaps(other), "Region labels must not collide.")

    def test_exports_preserve_physical_size_vector_pdf_and_draft_guard(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            config = replace(self.config, stem=Path(temporary) / "figure", overwrite=False)
            figure, _ = plot.build_two_door_decisions(self.data, config)
            pdf, png = plot.render_figure(figure, config)
            with Image.open(png) as raster:
                for measured, inches in zip(raster.size, config.size_inches):
                    self.assertLessEqual(abs(measured - inches * config.dpi), 1)
                self.assertAlmostEqual(raster.info["dpi"][0], config.dpi, places=1)
            with fitz.open(pdf) as document:
                self.assertEqual(len(document), 1)
                for measured, inches in zip(document[0].rect[2:], config.size_inches):
                    self.assertAlmostEqual(measured, 72 * inches, places=3)
                self.assertFalse(document[0].get_images(), "PDF must preserve vector regions and text.")
                self.assertIn("Minimax regret", document[0].get_text())
                self.assertIn("Maximin incremental gain", document[0].get_text())
                self.assertTrue(all(document.extract_font(font[0])[3] for font in document[0].get_fonts()))
            with self.assertRaises(FileExistsError):
                plot.render_figure(figure, config)


if __name__ == "__main__":
    unittest.main()
