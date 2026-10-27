# Manuscript source and revision status

The Overleaf source was imported on 2026-10-19 in commit `3015f9b285d5333768cc446a04e4278fc547743c`. The current source contains a substantive conceptual revision under the existing invited title. It is ready for author review, with the AI disclosure deliberately red for later revision.

The live issue dispositions are in [`../AUDIT.md`](../AUDIT.md). Current implementation and artifact checks are in [`../notes/17_round1_revision_report.md`](../notes/17_round1_revision_report.md), with the [Round 1 response matrix](../reviews/round1/response_matrix.md). Checkpoint commit `0f7a169` preserves the preceding draft and review assessment. Earlier reports retain their historical verification scope.

## Canonical files

- `template.tex` — manuscript wording, structure, abstract, keywords, citations, and declarations.
- `extracted.bib` — canonical reference library: 36 entries, 26 cited in the revised text.
- `generated/two_door_results.tex` — numerical comparison table generated from `../simulations/two_door/parameters.json`; do not edit the table manually.
- `diagram.tex` — the active conceptual overview.
- `figures/two_door_decisions.pdf` — the active numerical figure, generated from calculator-exported geometry using `../scripts/plot_two_door.py` and `../config/figures.yaml`.
- `inferencechain.tex`, `conceptual_heatmap.tex`, and `pioritisationoutput.tex` — historical conceptual sources, no longer included in the article.
- `supplement/README.md` — instructions included in the locally prepared Supplement S1 archive.
- `Definitions/` — MDPI class/styles/assets; no vendor source was edited.

Exact manuscript wording and keys are authoritative here; historical notes preserve rationale and earlier proposals. Limited-Data Predictive Maintenance (LD-PdM) and the invited title are retained.

## Current content

The Round 1 revision provides an applicability checklist, a five-step procedure, a completed decision record, and an exact two-door comparison. Six tables, two figures, and seven numbered equations support the argument. Dominance filtering precedes the main minimax-regret criterion and maximin-incremental-gain comparator. Their different choices and exact ties are explicit, including a case where minimax regret accepts negative gain in one model. Numerical inputs remain unchanged; the old strict fallback survives only as an identified historical code diagnostic. The example stipulates the exposure/condition relationships and makes no empirical performance or learned-inference claim.

Reference verification, claim scope, and full-text limitations are recorded in [`../literature/03_claim_source_matrix.md`](../literature/03_claim_source_matrix.md). Retain candidates outside `extracted.bib` until they are actually cited.

## Build and inspection

From this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=../build/manuscript template.tex
```

The generated table and figure are included. To regenerate the analytical artifacts, run `python3 simulations/two_door/calculate.py` from the repository root; see the [calculation guide](../simulations/two_door/README.md). Figure rendering and its approval state are described in the [figure guide](../tools/figures/README.md). The standalone calculation is also supplied in `../output/supplement/two-door-calculation.zip`; extracted regeneration was checked byte-for-byte.

The 2026-10-26 Round 1 draft builds to 18 pages without unresolved citations/references, missing characters, or overfull/underfull boxes. The implementation report records the visual inspection and post-approval checks: 18 tests and 69 subtests passed, 16 catalog entries validated, and figure configuration/schema/project-state checks reported zero blockers and zero warnings. The existing non-fatal `xcolor` and PyMuPDF SWIG warnings remain. On 2026-10-26 the author explicitly approved the current two-door figure, its two-panel 138.6 × 85 mm layout, vector PDF, and 300 dpi PNG. No figure package or external upload was made; neither the supplement nor article has been submitted.

The review PDF is saved as `../output/pdf/ld-pdm-conceptual-revision.pdf`. The revision remains an uncommitted author-review draft with the requested red AI disclosure; figure approval does not authorize submission.

## Diagram previews

`sources/tikz/` contains standalone wrappers for the canonical inline pictures; generated previews are in `figures/tikz/`. From the repository root, with the declared optional environment available:

```sh
python scripts/render_tikz.py --strict paper
python scripts/render_tikz.py --verify paper
```

See [`../tools/diagrams/README.md`](../tools/diagrams/README.md) for exact dependency pins and setup commands. TeX Live with TikZ, `standalone`, and Palatino is a separate system requirement. Rendering the article does not regenerate preview images.
