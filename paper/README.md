# Manuscript source and revision status

The Overleaf source was imported on 2026-10-19 in commit `3015f9b285d5333768cc446a04e4278fc547743c`. The current source contains a substantive conceptual revision under the existing invited title. It is ready for author review, with the AI disclosure deliberately red for later revision.

The live issue dispositions are in [`../AUDIT.md`](../AUDIT.md). The implemented changes, length comparison, checks, and remaining author work are recorded in [`../notes/08_manuscript_revision_report.md`](../notes/08_manuscript_revision_report.md).

## Canonical files

- `template.tex` — manuscript wording, structure, abstract, keywords, citations, and declarations.
- `extracted.bib` — canonical reference library: 30 entries, 26 cited in the revised text.
- `diagram.tex` and `inferencechain.tex` — the two active inline conceptual diagrams.
- `conceptual_heatmap.tex` and `pioritisationoutput.tex` — historical schematic sources, no longer inputs to the revised article.
- `Definitions/` — MDPI class/styles/assets; no vendor source was edited.

Exact manuscript wording and keys are authoritative here; historical notes preserve rationale and earlier proposals. Limited-Data Predictive Maintenance (LD-PdM) and the invited title are retained.

## Current content

The revision integrates Li et al. and established maintenance decision/information-value work, gives operational regime criteria and boundary cases, separates the inferential variables from actions, and develops a worked qualitative station example. Four tables describe boundaries, quantities, assumptions, and decision scenarios. No empirical data or simulation results are claimed. The unused synthetic-extension proposal is not a submission prerequisite.

Reference verification, claim scope, and full-text limitations are recorded in [`../literature/03_claim_source_matrix.md`](../literature/03_claim_source_matrix.md). Retain candidates outside `extracted.bib` until they are actually cited.

## Build and inspection

From this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=../build/manuscript template.tex
```

TeX Live 2024 and latexmk 4.83 produce a 16-page PDF after the focused Li comparison, without unresolved citations/references, missing characters, or overfull/underfull boxes. All pages were rendered and visually inspected. The abstract/keywords, single-author option, year, header height, and previous width problems are repaired. A non-fatal `xcolor` load-time-option warning remains within the bundled class/PGF loading sequence.

The review PDF is saved as `../output/pdf/ld-pdm-conceptual-revision.pdf`. It is a review draft with the requested red AI disclosure, not a submission authorization.

## Diagram previews

`sources/tikz/` contains standalone wrappers for the canonical inline pictures; generated previews are in `figures/tikz/`. From the repository root, with the declared optional environment available:

```sh
python scripts/render_tikz.py --strict paper
python scripts/render_tikz.py --verify paper
```

See [`../tools/diagrams/README.md`](../tools/diagrams/README.md) for exact dependency pins and setup commands. TeX Live with TikZ, `standalone`, and Palatino is a separate system requirement. Rendering the article does not regenerate preview images.
