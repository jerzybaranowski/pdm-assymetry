# Manuscript source

The canonical manuscript source is not yet present in this repository.

A near-submission version existed in the ChatGPT project in March 2026, with attachments named:

- `Predictive_Maintenance_Concept-submission.pdf`
- `Predictive_Maintenance_Concept.zip`

The current migration environment cannot retrieve those attachments, and the latest LaTeX source is believed to remain available in Overleaf.

## Import rule

When the Overleaf project is exported, copy the source tree into this directory **without reconstructing or renaming BibTeX keys unnecessarily**.

The imported source should include:

- `.tex` files;
- `.bib` files;
- figures;
- custom `.sty`/`.cls` files where used;
- any data or code needed to reproduce figures.

After import, compile the project and compare the resulting PDF with the last known submission-ready PDF before making substantive edits.

## Canonical-source rule

If any Markdown note in `../notes/` conflicts with the imported LaTeX manuscript, the actual manuscript source is authoritative for exact wording, section numbering, citations and bibliography keys. The notes preserve research rationale and decisions, not exact source text.
