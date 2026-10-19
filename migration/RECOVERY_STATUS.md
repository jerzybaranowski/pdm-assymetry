# ChatGPT project migration — recovery status

**Migration date:** 2026-10-19  
**Manuscript-source import:** 2026-10-19, commit `3015f9b285d5333768cc446a04e4278fc547743c`

The migration now contains both (i) durable research context reconstructed from the ChatGPT project and (ii) the current Overleaf/LaTeX manuscript source committed by the project owner.

## Recovered from project conversation context

The following durable project information was reconstructed and committed before the source import:

- the structural-asymmetry concept underlying LD-PdM;
- the distinction between critical, heavily instrumented assets and mass-deployed assets for which additional sensing may be economically difficult to justify;
- the railway-station case-study direction, including escalators, elevators and automatic doors;
- the proxy-data idea, including passenger/ticket-flow information as indirect evidence of device usage;
- the intended Bayesian/probabilistic framing for uncertain proxy, contextual and historical evidence;
- the high-concept/non-review character of the article;
- the paragraph-level outlining rules used during manuscript development;
- the literature-synthesis result that indirect/proxy inference appears across many domains without being unified under PdM terminology;
- the required positioning against Li et al. (2024), *Small data challenges for intelligent prognostics and health management: a review*;
- the March 2026 pre-submission discussion for *Symmetry*;
- the plan to reuse/cite railway-station door/elevator material from the related GPECOM work where appropriate.

These materials are stored in `notes/` and `literature/` as research records rather than as purported verbatim chat transcripts.

## Current canonical manuscript source

The source imported into `paper/` contains:

- `template.tex` — main manuscript;
- `extracted.bib` — manuscript bibliography;
- `diagram.tex` — conceptual asymmetry/observability figure;
- `inferencechain.tex` — inference-chain figure;
- `conceptual_heatmap.tex` — station exposure-map figure;
- `pioritisationoutput.tex` — prioritisation figure;
- `Definitions/` — MDPI class/styles/assets.

The source confirms the canonical expansion **Limited-Data Predictive Maintenance (LD-PdM)** and contains the current abstract, keywords, contribution statement, station-based illustrative case, discussion, conclusions, acknowledgments and bibliography.

The previously unresolved citation key `Cinar2020` is now identified from `paper/extracted.bib` as the 2020 *Sustainability* paper by Çınar et al., “Machine learning in predictive maintenance towards sustainable smart manufacturing in industry 4.0,” DOI `10.3390/su12198211`.

## Source-versus-notes rule

Where the imported LaTeX differs from reconstructed notes:

- `paper/template.tex` is authoritative for exact manuscript wording and section structure;
- `paper/extracted.bib` is authoritative for current BibTeX keys;
- Markdown notes remain authoritative only for research rationale, earlier decisions, literature-search conclusions and migration provenance that are not yet reflected in the manuscript.

See `SOURCE_RECONCILIATION.md` for the main discrepancies detected immediately after import.

## Historical attachments still unavailable

The project conversation history refers to:

- `Predictive_Maintenance_Concept-submission.pdf`;
- `Predictive_Maintenance_Concept.zip`;
- `outline.pdf`.

Their exact historical bytes are still not exposed by the current ChatGPT file interface. This is no longer a blocker for manuscript work because the current Overleaf source is now in the repository, but the historical files would still be useful for forensic comparison if they are ever recovered.

## Material not recoverable exactly from chat history

The retained project context does not provide a complete verbatim export of all historical conversations. In particular, the exact historical detailed outline and some intermediate literature-review outputs cannot be reproduced word-for-word. Their durable conclusions were migrated instead.

No missing source text has been silently invented.
