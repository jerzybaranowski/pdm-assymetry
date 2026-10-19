# Migration manifest

## Current repository organization

The ChatGPT-project migration and the current Overleaf source are both present. The repository has subsequently been cleaned so that manuscript source, literature notes, research notes, and migration provenance have distinct roles.

### Root working documents

| Path | Purpose | Status |
|---|---|---|
| `README.md` | Project overview and full repository map | current |
| `AUDIT.md` | Prioritized scientific/editorial audit and submission gate | current working plan |
| `AGENTS.md` | Durable instructions for AI-assisted work | current |
| `.gitignore` | LaTeX/Python/editor artifact exclusions | current |

### Research context migrated from ChatGPT

| Path | Purpose |
|---|---|
| `notes/CONVERSATION_INDEX.md` | Reconstructed index of important project conversations |
| `notes/01_core_concept.md` | Core LD-PdM/asymmetry concept, now reconciled with Li et al. positioning |
| `notes/02_contribution_statement.md` | Historical contribution logic |
| `notes/03_paper_structure.md` | Historical paragraph-level outlining method + current structural guidance |
| `notes/04_train_station_case_study.md` | Station case logic and quantitative extension plan |
| `notes/05_submission_readiness.md` | Historical readiness note, now pointing to `AUDIT.md` |
| `notes/06_manuscript_components.md` | Verified record of current abstract/keywords/abbreviations and candidate self-citation |
| `literature/01_literature_synthesis.md` | Cross-domain literature synthesis |
| `literature/02_positioning_vs_li2024.md` | Detailed Li et al. comparison and novelty boundary |
| `literature/candidate_references.bib` | Candidate, non-canonical BibTeX entries (currently Li et al. and Bauer2025) |

### Canonical manuscript source imported from Overleaf

Imported by the project owner in commit `3015f9b285d5333768cc446a04e4278fc547743c`.

| Path | Role | Status |
|---|---|---|
| `paper/template.tex` | Main manuscript source | canonical |
| `paper/extracted.bib` | Manuscript bibliography | canonical |
| `paper/diagram.tex` | Asymmetry/observability figure | canonical source asset |
| `paper/inferencechain.tex` | Proxy-to-belief inference-chain figure | canonical source asset |
| `paper/conceptual_heatmap.tex` | Station exposure heatmap | canonical source asset |
| `paper/pioritisationoutput.tex` | Maintenance-prioritisation figure | canonical source asset; filename cleanup pending |
| `paper/README.md` | Manuscript-directory guide and known source issues | current |
| `paper/Definitions/` | MDPI support files/assets | imported vendor/template material |

## Repository cleanup performed after source import

- Removed redundant `paper/README-kopia.md` (`# Asymmetry_PdM` only).
- Removed ambiguous `references/recovered.bib` after moving useful candidate entries to `literature/candidate_references.bib`.
- Added `.gitignore` for common LaTeX/Python/editor artifacts.
- Added `AUDIT.md` as a single prioritized source for remaining manuscript work.
- Expanded `README.md` into a file-by-file project map.
- Updated the Li et al. positioning after direct re-reading of the review: sensor economics, incomplete/imbalanced data, and uncertainty are acknowledged as overlap rather than claimed novelty.
- Reconciled stale notes that still described the LaTeX source, abstract, or `Cinar2020` as unavailable.

## Migration provenance files

| Path | Purpose |
|---|---|
| `migration/RECOVERY_STATUS.md` | What was recovered and what historical material remains unavailable |
| `migration/SOURCE_RECONCILIATION.md` | First comparison between recovered notes and imported source |
| `migration/MANIFEST.md` | This current inventory |

`SOURCE_RECONCILIATION.md` is a dated first-pass record. Where later scientific interpretation differs (especially the stronger overlap with Li et al.), use `AUDIT.md` and `literature/02_positioning_vs_li2024.md` as the current guidance.

## Historical attachments still unavailable

| Historical file | Role | Current status |
|---|---|---|
| `Predictive_Maintenance_Concept-submission.pdf` | Earlier near-submission PDF | exact historical bytes unavailable |
| `Predictive_Maintenance_Concept.zip` | Earlier source package | exact historical bytes unavailable; current Overleaf source is present |
| `outline.pdf` | Detailed Dec 2025 outline | exact historical bytes unavailable |

## Migration completion criterion

The migration is **operationally complete**. Current manuscript source + bibliography + figures + recovered research context are in GitHub. Remaining work is manuscript research/revision, tracked in `AUDIT.md`, rather than migration recovery.
