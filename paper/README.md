# Manuscript source

The current Overleaf source was imported into this directory on 2026-10-19 (commit `3015f9b285d5333768cc446a04e4278fc547743c`).

The manuscript is **not currently submission-ready**. For the live prioritized scientific/editorial checklist, see [`../AUDIT.md`](../AUDIT.md).

## Main files

- `template.tex` — canonical manuscript source for *Symmetry*.
- `extracted.bib` — canonical bibliography currently compiled by the manuscript.
- `diagram.tex` — conceptual asymmetric-observability figure.
- `inferencechain.tex` — station context / proxy / latent-belief / maintenance-priority chain.
- `conceptual_heatmap.tex` — conceptual station maintenance-exposure map.
- `pioritisationoutput.tex` — illustrative maintenance-prioritisation output. The filename typo is known and should be cleaned when `template.tex` is next edited substantively.
- `Definitions/` — MDPI class, bibliography styles, journal-name definitions, and template graphics.

## Canonical-source rule

For exact current manuscript state:

1. `template.tex` is authoritative for manuscript wording, section structure, declarations, and citations;
2. `extracted.bib` is authoritative for currently available manuscript BibTeX keys;
3. `../AUDIT.md` is authoritative for what still needs to change;
4. `../notes/` and `../literature/` preserve research rationale, positioning, and historical decisions.

A note can legitimately disagree with the current LaTeX when it records a **required revision**. Do not delete such a note merely because the manuscript has not yet been updated.

## Canonical terminology

The imported manuscript defines **Limited-Data Predictive Maintenance (LD-PdM)**. “Limited/low observability” and “low instrumentation” are useful descriptors, but the current acronym expansion should only be changed by explicit author decision.

Because Li et al. (2024) use a broad notion of small-data PHM, the manuscript must clarify that LD-PdM is not defined by sample count. The intended focus is persistent weak direct observability, heterogeneous indirect evidence, and maintenance decision support.

## Known source-level issues

These are documented in detail in `../AUDIT.md`:

- Li et al. (2024) are not yet integrated into `template.tex` / `extracted.bib`;
- the Introduction promises an “illustrative simulation,” while active station sections describe a conceptual architecture;
- active draft headings include “Section positioning” and “Section opening paragraph”;
- several captions/prose passages still say “planned figure,” “should show,” or “can be chosen later” although figure sources are already present;
- the manuscript currently lacks a quantitative station demonstration;
- MDPI front matter uses `moreauthors` despite one author and has `\pubyear{2026}` with `\copyrightyear{2025}`;
- end-matter grammar and the AI-use statement need verification/cleanup;
- a clean build from a fresh checkout has not yet been recorded.

## Bibliography workflow

`extracted.bib` is the manuscript bibliography. Candidate references that are not yet cited belong in `../literature/candidate_references.bib`, not in a parallel “canonical” bibliography.

In particular, `../literature/candidate_references.bib` currently contains:

- Li et al. (2024), which **should** be integrated during the next substantive manuscript revision;
- Bauer and Baranowski (2025), which should only be integrated if it supports a specific argument.

## Build status

The directory contains the MDPI support files needed by the imported Overleaf project, but this repository does not yet contain a recorded clean-build check.

Expected conventional build sequence (to be verified, not yet recorded as CI):

```text
pdflatex template
bibtex template
pdflatex template
pdflatex template
```

Do not commit auxiliary LaTeX files; the root `.gitignore` excludes common build artifacts.

## Future simulation code

If the audit decision is to add a quantitative station example, place reproducible Python code outside `paper/` (recommended: `simulation/`) and keep `paper/` limited to manuscript source and manuscript-facing figure assets.
