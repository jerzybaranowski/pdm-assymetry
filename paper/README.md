# Manuscript source

The current Overleaf source was imported into this directory on 2026-10-19 (commit `3015f9b285d5333768cc446a04e4278fc547743c`).

## Main files

- `template.tex` — main manuscript source for *Symmetry*.
- `extracted.bib` — canonical bibliography used by the manuscript at import time.
- `diagram.tex` — conceptual figure for asymmetric observability.
- `inferencechain.tex` — station-data/proxy/latent-belief inference chain.
- `conceptual_heatmap.tex` — conceptual station maintenance-exposure map.
- `pioritisationoutput.tex` — illustrative maintenance-prioritisation output.
- `Definitions/` — MDPI class, bibliography styles and template graphics.

## Canonical terminology

The imported manuscript defines **Limited-Data Predictive Maintenance (LD-PdM)**. Earlier project conversations also used descriptions such as “low-data,” “low-instrumentation,” and “low-observability”; these remain useful descriptors but should not silently redefine the manuscript acronym.

## Canonical-source rule

For exact wording, manuscript structure, current citations and BibTeX keys:

1. `template.tex` is authoritative for manuscript text;
2. `extracted.bib` is authoritative for current bibliography keys;
3. Markdown files under `../notes/` and `../literature/` preserve rationale, earlier decisions, literature-search conclusions, and unresolved manuscript tasks.

If a research note identifies a missing comparison or reference that is not yet present in the LaTeX source, treat that as an explicit finalization task rather than deleting the note because it conflicts with the current manuscript.

## Immediate source-reconciliation findings

- The abstract and keyword list are already present in `template.tex`.
- The abbreviation list currently contains PdM, LD-PdM, and RUL.
- The previously questioned key `Cinar2020` is present in `extracted.bib` and resolves to Çınar et al. (2020), DOI `10.3390/su12198211`.
- The manuscript cites a companion conference paper `GPECOM2026LdPDM` for the more technical railway-station door/elevator implementation.
- Li et al. (2024), identified during the project review as an important adjacent small-data PHM review, are not currently present in `template.tex` or `extracted.bib` and should be integrated during final manuscript revision.

See `../migration/SOURCE_RECONCILIATION.md` for the full reconciliation note.
