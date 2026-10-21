# Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems

This repository is the canonical working repository for the paper **“Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems”**, currently prepared for *Symmetry*.

The manuscript uses **Limited-Data Predictive Maintenance (LD-PdM)** for a maintenance regime in which direct condition information is structurally weak, indirect, incomplete, or economically difficult to acquire, while maintenance decisions still have meaningful operational or economic value.

> **Current status:** a revised conceptual draft is ready for author review. The AI disclosure is red for later revision. Current issue dispositions are in [`AUDIT.md`](AUDIT.md); changes and checks are recorded in [`notes/08_manuscript_revision_report.md`](notes/08_manuscript_revision_report.md).

**Completion scope confirmed by the author on 2026-10-19:** a conceptual paper, with no available empirical data and an optional high-level synthetic illustration. The existing title is invited and retained. The execution plan and closure criteria are in [`notes/07_publication_completion_plan.md`](notes/07_publication_completion_plan.md).

## Core research idea

The paper is built around a structural asymmetry between **maintenance decision value** and **economically available direct observability**. The motivating contrast is between:

- expensive or critical assets, for which dedicated condition-monitoring instrumentation can often be justified by avoided downtime, damage, or safety consequences; and
- large populations of comparatively ordinary assets—automatic doors, escalators, elevators, HVAC units, vehicle/tool fleets and similar devices—where aggregate maintenance value can be meaningful while rich per-asset sensing is difficult to justify.

In the second regime, maintenance reasoning may need to use operational logs, contextual variables, proxy measurements, service history, documentation, and prior engineering knowledge. Because these sources are only indirectly informative about latent load, degradation, and risk, uncertainty is part of the problem formulation rather than a residual modelling nuisance.

The principal illustrative setting is a **railway station**, where passenger-flow and timetable information can act as proxy evidence for device usage and where maintenance decisions are made across a population of distributed assets.

## Positioning against Li et al. and decision analysis

The closest adjacent work currently identified is:

> C. Li, S. Li, Y. Feng, K. Gryllias, F. Gu, and M. Pecht, “Small data challenges for intelligent prognostics and health management: a review,” *Artificial Intelligence Review*, 57, 214 (2024), DOI `10.1007/s10462-024-10820-4`.

Li et al. already cover limited/imbalanced/incomplete PHM data, costly data acquisition and sensor deployment, and uncertainty under small-data conditions. The present paper therefore cannot claim novelty for data scarcity or sensor economics alone. The intended distinction is the **observation architecture and decision target**: direct condition channels may be persistently absent, proxy/context/history can become primary evidence, and the main objective is maintenance prioritisation and decision support under partial observability.

The revision integrates Li et al. and existing POMDP/information-value maintenance work. See [`literature/02_positioning_vs_li2024.md`](literature/02_positioning_vs_li2024.md), the checked [`claim–source matrix`](literature/03_claim_source_matrix.md), and [`AUDIT.md`](AUDIT.md).

---

# Repository map

## Root files

| File | What it contains | Status / authority |
|---|---|---|
| [`README.md`](README.md) | Project overview and map of the repository | navigation document |
| [`AUDIT.md`](AUDIT.md) | Prioritized audit of missing work, inconsistencies, Li integration, and submission gates | **current action plan** |
| [`AGENTS.md`](AGENTS.md) | Rules for AI-assisted research/coding/writing in this repository | durable working instructions |
| [`.gitignore`](.gitignore) | LaTeX/Python/editor build-artifact exclusions | repository hygiene |

## `paper/` — canonical manuscript source

| File / directory | What it contains |
|---|---|
| [`paper/template.tex`](paper/template.tex) | **Main manuscript source**. Authoritative for exact manuscript wording, structure, citations, abstract, keywords, declarations, and section order. |
| [`paper/extracted.bib`](paper/extracted.bib) | **Canonical bibliography currently used by the manuscript**. |
| [`paper/diagram.tex`](paper/diagram.tex) | Conceptual asymmetric-observability figure. |
| [`paper/inferencechain.tex`](paper/inferencechain.tex) | Station context → proxy evidence → latent beliefs → maintenance-priority inference chain. |
| [`paper/conceptual_heatmap.tex`](paper/conceptual_heatmap.tex) | Historical schematic exposure map, retained but not used in the revised manuscript. |
| [`paper/pioritisationoutput.tex`](paper/pioritisationoutput.tex) | Historical priority schematic, retained but not used. The filename typo is outside the active submission source. |
| `paper/sources/tikz/`, `paper/figures/tikz/` | Standalone wrappers and generated previews of the two active diagrams; canonical picture content remains in `paper/diagram.tex` and `paper/inferencechain.tex`. |
| [`paper/README.md`](paper/README.md) | Manuscript-directory guide, source authority, and build/status notes. |
| `paper/Definitions/` | MDPI class, bibliography styles, journal-name definitions, and template graphics. Treat as vendor/template files unless an MDPI update requires replacement. |

The current Overleaf source was imported in commit `3015f9b285d5333768cc446a04e4278fc547743c`.

## `literature/` — literature synthesis and positioning

| File | What it contains |
|---|---|
| [`literature/01_literature_synthesis.md`](literature/01_literature_synthesis.md) | Cross-domain synthesis of indirect/proxy inference literature and the main literature strands relevant to LD-PdM. |
| [`literature/02_positioning_vs_li2024.md`](literature/02_positioning_vs_li2024.md) | Detailed comparison with Li et al. (2024), including overlap, defensible novelty boundary, and manuscript integration plan. |
| [`literature/03_claim_source_matrix.md`](literature/03_claim_source_matrix.md) | Source checks, verified metadata, permissible claim strength, and full-text access limits. |
| [`literature/04_gpecom_contribution_boundary.md`](literature/04_gpecom_contribution_boundary.md) | Full-text comparison with the companion GPECOM paper and the author-confirmed identity of preprint and final version. |
| [`literature/candidate_references.bib`](literature/candidate_references.bib) | Unused candidate references. Li et al. is integrated into the canonical bibliography; Bauer–Baranowski remains optional. |

## `notes/` — durable research decisions and historical project reasoning

| File | What it contains |
|---|---|
| [`notes/01_core_concept.md`](notes/01_core_concept.md) | Core LD-PdM concept, asymmetry, evidence sources, Bayesian motivation, and relation to small-data PHM. |
| [`notes/02_contribution_statement.md`](notes/02_contribution_statement.md) | Recovered contribution logic from the earlier manuscript-development phase. Historical/strategic, not exact current manuscript text. |
| [`notes/03_paper_structure.md`](notes/03_paper_structure.md) | Historical paragraph-level outlining rules plus current guidance on how they relate to the imported source. |
| [`notes/04_train_station_case_study.md`](notes/04_train_station_case_study.md) | Station case-study logic and a historical quantitative-extension proposal, distinguished from the confirmed completion scope. |
| [`notes/05_submission_readiness.md`](notes/05_submission_readiness.md) | Historical pre-submission concerns reconciled with the current source; points to `AUDIT.md` for the live checklist. |
| [`notes/06_manuscript_components.md`](notes/06_manuscript_components.md) | Verified record of the current abstract themes, keywords, abbreviations, and candidate self-citation. |
| [`notes/07_publication_completion_plan.md`](notes/07_publication_completion_plan.md) | Follow-up review, ordered work packages, proposed paragraph outline, complete audit coverage, and submission gate. |
| [`notes/08_manuscript_revision_report.md`](notes/08_manuscript_revision_report.md) | Implemented changes, section-length comparison, validation evidence, and remaining author checks. |
| [`notes/09_cover_letter_draft.md`](notes/09_cover_letter_draft.md) | Draft invitation response/cover letter for author review; not sent. |
| [`notes/CONVERSATION_INDEX.md`](notes/CONVERSATION_INDEX.md) | Index of the main ChatGPT project conversations and the durable conclusions recovered from them. |

## `migration/` — provenance only

| File | What it contains |
|---|---|
| [`migration/RECOVERY_STATUS.md`](migration/RECOVERY_STATUS.md) | What was and was not recoverable from the original ChatGPT project and historical attachments. |
| [`migration/SOURCE_RECONCILIATION.md`](migration/SOURCE_RECONCILIATION.md) | First reconciliation between recovered notes and the imported Overleaf source. |
| [`migration/MANIFEST.md`](migration/MANIFEST.md) | Migration inventory and file provenance. |

These files are useful for provenance, but they should not drive manuscript content when they conflict with `paper/template.tex` or the current `AUDIT.md`.

---

# Source-of-truth rules

1. **Manuscript wording and citation keys:** `paper/template.tex` + `paper/extracted.bib`.
2. **Current work plan and unresolved issues:** `AUDIT.md`.
3. **Literature interpretation / novelty boundary:** `literature/`.
4. **Conceptual rationale and historical design decisions:** `notes/`.
5. **Migration history only:** `migration/`.

Do not silently copy historical note wording into the manuscript. Compare it with the current source first.

## Current author review

The conceptual revision implements the definition, literature positioning, and worked station decision. The remaining author review concerns:

1. The scientific argument and balance of explanation after substantive editing.
2. The red AI declaration, deliberately deferred by the author.
3. Final affiliation presentation and submission-history declarations. Funding scope is retained as instructed.

## Build/reproducibility status

The current review PDF has 16 pages after the two-door example and contribution refinement on 2026-10-21. It compiles without unresolved citations/references, missing characters, or overfull/underfull boxes. All pages were rendered and visually inspected; abstract, keywords, diagrams, and tables render correctly. A non-fatal `xcolor` warning remains within the bundled template. See `notes/08_manuscript_revision_report.md` for the verification scope.

Build the article from `paper/`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=../build/manuscript template.tex
```

The optional shared diagram renderer has standalone wrappers in `paper/sources/tikz/` and outputs in `paper/figures/tikz/`. Its pinned Python/uv declaration and setup instructions are in [`tools/diagrams/README.md`](tools/diagrams/README.md). With that environment available, run `python scripts/render_tikz.py --strict paper`, followed by `--verify paper`. It requires TeX Live with TikZ, `standalone`, and Palatino support. Compiling the article uses inline sources and does not refresh the separate diagram previews. Three static pipeline tests and the test-case catalog validator pass.

If the optional synthetic illustration is added, use a small dedicated directory with reproducible Python source, fixed seeds, explicit assumptions, and generated-figure scripts. A simulation is not a prerequisite for completing the conceptual paper.
