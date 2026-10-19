# Migration manifest

## Repository artifacts created from ChatGPT project context

| Path | Purpose | Status |
|---|---|---|
| `README.md` | Project overview and repository structure | migrated; reconciled with source |
| `AGENTS.md` | Durable instructions for AI-assisted work | migrated; reconciled with source |
| `migration/RECOVERY_STATUS.md` | Recovery limitations and source status | migrated; updated after source import |
| `migration/MANIFEST.md` | Migration inventory | migrated |
| `migration/SOURCE_RECONCILIATION.md` | Differences between recovered notes and imported manuscript | migrated |
| `notes/CONVERSATION_INDEX.md` | Reconstructed index of project conversations | migrated |
| `notes/01_core_concept.md` | Core LD-PdM/asymmetry concept | migrated |
| `notes/02_contribution_statement.md` | Recovered contribution logic | migrated |
| `notes/03_paper_structure.md` | Recovered Introduction structure and outlining rules | migrated |
| `notes/04_train_station_case_study.md` | Train-station, proxy-data and digital-twin case direction | migrated |
| `notes/05_submission_readiness.md` | Symmetry pre-submission issues/checklist | migrated |
| `notes/06_manuscript_components.md` | Historical record of abstract/keywords/abbreviation work | migrated |
| `literature/01_literature_synthesis.md` | Recovered literature-review synthesis | migrated |
| `literature/02_positioning_vs_li2024.md` | Positioning against the 2024 small-data PHM review | migrated |
| `references/recovered.bib` | Small seed of references explicitly recoverable from conversations | migrated; non-canonical |

## Canonical manuscript source imported from Overleaf

Imported by the project owner in commit `3015f9b285d5333768cc446a04e4278fc547743c`.

| Path | Role | Status |
|---|---|---|
| `paper/template.tex` | Main manuscript source | canonical |
| `paper/extracted.bib` | Manuscript bibliography | canonical |
| `paper/diagram.tex` | Asymmetry/observability figure | canonical source asset |
| `paper/inferencechain.tex` | Proxy-to-belief inference-chain figure | canonical source asset |
| `paper/conceptual_heatmap.tex` | Station exposure heatmap | canonical source asset |
| `paper/pioritisationoutput.tex` | Maintenance-prioritisation figure | canonical source asset |
| `paper/Definitions/journalnames.tex` | MDPI support file | imported |
| `paper/Definitions/mdpi.cls` | MDPI class | imported |
| `paper/Definitions/mdpi.bst` | MDPI bibliography style | imported |
| `paper/Definitions/mdpi_apacite.bst` | MDPI support file | imported |
| `paper/Definitions/mdpi_apacite.sty` | MDPI support file | imported |
| `paper/Definitions/mdpi_chicago.bst` | MDPI support file | imported |
| `paper/Definitions/logo-mdpi.eps` | MDPI asset | imported |
| `paper/Definitions/logo-orcid.pdf` | MDPI asset | imported |
| `paper/Definitions/logo-updates.eps` | MDPI asset | imported |
| `paper/README-kopia.md` | File included in source import | preserved as uploaded |

## Historical files known from project conversations

| Historical file | Role | Current migration status |
|---|---|---|
| `Predictive_Maintenance_Concept-submission.pdf` | Near-submission manuscript PDF | exact historical bytes unavailable |
| `Predictive_Maintenance_Concept.zip` | Earlier source package supplied in March 2026 | exact historical bytes unavailable; current Overleaf source now imported |
| `outline.pdf` | Detailed paper outline used in Dec 2025 | exact historical bytes unavailable |

## Important reconciliation results

- The manuscript’s canonical term is **Limited-Data Predictive Maintenance (LD-PdM)**, not “Low-Data Predictive Maintenance.”
- `Cinar2020` is now resolved from the canonical bibliography.
- The current source already contains the abstract, keywords and abbreviation list that earlier migration notes could only describe indirectly.
- The source contains the station-based illustrative case and cites a companion GPECOM paper for the more technical door/elevator implementation.
- Li et al. (2024), identified in the March 2026 review as an important adjacent work, are not present in the imported manuscript bibliography/source and remain a known finalization task.

## Migration completion criterion

The migration is considered **operationally complete**: current manuscript source + bibliography + figures + recovered research context are all in GitHub. Historical PDFs/transcripts can still be added later for provenance, but they are not required to continue research and manuscript preparation.
