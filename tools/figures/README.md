# Two-door publication figure tooling

The figure specification is `config/figures.yaml`, ID `two-door-decisions`.
`scripts/plot_two_door.py` consumes only the polygons, ties and labels in
`simulations/two_door/plot_data.json`. It never imports the policy calculator.
Generate that analytical artifact through the calculation's documented command
before rendering. The author approved the concrete two-panel figure on
2026-10-26, including its 138.6 × 85.0 mm dimensions, vector PDF and 300-dpi
PNG outputs in `paper/figures/`. This approval is recorded in the configuration
and validation report. Captions and validation records are under
`output/figures/`. No figure package has been created.

The scripts and assets in this directory were copied from the
`scientific-figures` skill on 2026-10-26. The only asset extension is the
categorical `two_door_policy_v1` palette. The builder overrides tick sizes to
8 points and uses 8.5-point labels. It preserves dimensions without tight-bbox
cropping. Use the installed interpreter; no environment installation is part
of these commands:

```sh
MPLCONFIGDIR=/private/tmp/pdm-mpl-cache /opt/anaconda3/bin/python scripts/plot_two_door.py
/opt/anaconda3/bin/python tools/figures/scripts/validate_figure_config.py config/figures.yaml --project-root . --check-project-state
/opt/anaconda3/bin/python tools/figures/scripts/resolve_figure_config.py config/figures.yaml two-door-decisions
MPLCONFIGDIR=/private/tmp/pdm-mpl-cache /opt/anaconda3/bin/python -m pytest -q tests/test_two_door_figure.py
```

The bundled `inspect_figure_artifact.py` and `validate_figure.py` could not run
in the existing interpreter because `pypdf` is absent. They were not modified
or presented as passing. Installed PyMuPDF and Pillow instead inspected the
saved page/pixel dimensions, DPI, embedded fonts and vector content; these
checks are also covered by the export test. The separate validation report
records their results and manual inspection.

The 96-dpi PDF preview was inspected at the physical target scale, together
with grayscale and severity-100 protanopia/deuteranopia review previews.
The latter apply the published Machado matrices to linearized sRGB, then
return to sRGB and clip display gamut; only review pixels are transformed,
never analytical data or publication outputs. Matrix values and the linear
RGB application were checked against the original Colorspacious sources:
[matrices](https://raw.githubusercontent.com/njsmith/colorspacious/master/colorspacious/cvd.py),
[conversion](https://raw.githubusercontent.com/njsmith/colorspacious/master/colorspacious/conversion.py).
The method is Machado, Oliveira and Fernandes (2009),
DOI `10.1109/TVCG.2009.113`. The validation report preserves the exact matrices.

The thin A region near the upper-left corner has limited visual resolution
at the approved full-domain scale. No inset, axis transformation or omission
was introduced; its exact extent is supplied by the analytical boundary
equations. The caption records this limitation.
