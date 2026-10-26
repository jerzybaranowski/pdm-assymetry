# Manuscript source and revision status

The Overleaf source was imported on 2026-10-19 in commit `3015f9b285d5333768cc446a04e4278fc547743c`. The current source contains a substantive conceptual revision under the existing invited title. It is ready for author review, with the AI disclosure deliberately red for later revision.

The live issue dispositions are in [`../AUDIT.md`](../AUDIT.md). Current editorial and artifact checks are recorded in [`../notes/15_editorial_consistency_report.md`](../notes/15_editorial_consistency_report.md); the approved numerical calculation and its tests are documented in [`../notes/14_numerical_example_report.md`](../notes/14_numerical_example_report.md). The preceding revisions remain in [`../notes/13_round0_revision_report.md`](../notes/13_round0_revision_report.md) and [`../notes/08_manuscript_revision_report.md`](../notes/08_manuscript_revision_report.md).

## Canonical files

- `template.tex` — manuscript wording, structure, abstract, keywords, citations, and declarations.
- `extracted.bib` — canonical reference library: 32 entries, 23 cited in the revised text.
- `generated/two_door_results.tex` — numerical comparison table generated from `../simulations/two_door/parameters.json`; do not edit the table manually.
- `diagram.tex` and `inferencechain.tex` — the two active inline conceptual diagrams.
- `conceptual_heatmap.tex` and `pioritisationoutput.tex` — historical schematic sources, no longer inputs to the revised article.
- `Definitions/` — MDPI class/styles/assets; no vendor source was edited.

Exact manuscript wording and keys are authoritative here; historical notes preserve rationale and earlier proposals. Limited-Data Predictive Maintenance (LD-PdM) and the invited title are retained.

## Current content

The Round 0 revision provides an applicability checklist, a five-step assessment procedure, and an analytical and numerical two-door policy comparison with explicit baseline and fallback. Five tables distinguish applicability, quantities, station assumptions, numerical choices, and adjacent approaches. Six equations are used in the argument. The numerical illustration implements the author's approved hypothetical inputs with exact arithmetic and continuous decision boundaries. It explicitly shows that the stipulated fallback can forgo beneficial early inspection; the procedure now separates that illustrative convention from the requirement to specify an operational fallback. The 2026-10-25 pass also clarifies definitions, historical intervals, empirical-evidence limits, and existing figure-arrow conventions. No empirical performance result is claimed. Individual review dispositions are in [`../reviews/round0/response_matrix.md`](../reviews/round0/response_matrix.md).

Reference verification, claim scope, and full-text limitations are recorded in [`../literature/03_claim_source_matrix.md`](../literature/03_claim_source_matrix.md). Retain candidates outside `extracted.bib` until they are actually cited.

## Build and inspection

From this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=../build/manuscript template.tex
```

The numerical table is already included. To regenerate it first, run `python3 simulations/two_door/calculate.py` from the repository root; see the [calculation guide](../simulations/two_door/README.md).

TeX Live 2024 and latexmk 4.83 produce an 18-page PDF after the editorial continuation on 2026-10-25, without unresolved citations/references, missing characters, or overfull/underfull boxes. All pages were rendered and visually inspected; the abbreviations heading and table are kept together. The abstract/keywords, single-author option, year, header height, and previous width problems are repaired. A non-fatal `xcolor` load-time-option warning remains within the bundled class/PGF loading sequence.

The review PDF is saved as `../output/pdf/ld-pdm-conceptual-revision.pdf`. It is a review draft with the requested red AI disclosure, not a submission authorization.

## Diagram previews

`sources/tikz/` contains standalone wrappers for the canonical inline pictures; generated previews are in `figures/tikz/`. From the repository root, with the declared optional environment available:

```sh
python scripts/render_tikz.py --strict paper
python scripts/render_tikz.py --verify paper
```

See [`../tools/diagrams/README.md`](../tools/diagrams/README.md) for exact dependency pins and setup commands. TeX Live with TikZ, `standalone`, and Palatino is a separate system requirement. Rendering the article does not regenerate preview images.
