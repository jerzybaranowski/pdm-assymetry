# Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems

This repository is the canonical working repository for the paper **“Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems”**, currently prepared for *Symmetry*.

The manuscript uses **Limited-Data Predictive Maintenance (LD-PdM)** for a maintenance regime in which direct condition information is structurally weak, indirect, incomplete, or economically difficult to acquire, while maintenance decisions still have meaningful operational or economic value.

> **Current status:** the bounded Round 1 revision is implemented after checkpoint commit `0f7a169` and remains an uncommitted author-review draft. It adds dominance filtering, minimax-regret/maximin-gain comparisons, a completed decision record, focused literature positioning, and a decision-region figure. The draft has 18 pages. The author approved the current two-panel figure, 138.6 × 85 mm dimensions, vector PDF, and 300 dpi PNG on 2026-10-26. See [`notes/17_round1_revision_report.md`](notes/17_round1_revision_report.md) for verification; [`AUDIT.md`](AUDIT.md) remains the current action plan. The AI disclosure is deferred.

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
| [`paper/generated/two_door_results.tex`](paper/generated/two_door_results.tex) | Exact numerical comparison table generated by the approved two-door calculation. |
| [`paper/diagram.tex`](paper/diagram.tex) | Conceptual asymmetric-observability figure. |
| [`paper/inferencechain.tex`](paper/inferencechain.tex) | Historical station-chain diagram; removed from the active article during Round 1 to reduce duplication. |
| [`paper/figures/two_door_decisions.pdf`](paper/figures/two_door_decisions.pdf) | New comparison of decision regions, generated from calculator-exported geometry. |
| [`paper/conceptual_heatmap.tex`](paper/conceptual_heatmap.tex) | Historical schematic exposure map, retained but not used in the revised manuscript. |
| [`paper/pioritisationoutput.tex`](paper/pioritisationoutput.tex) | Historical priority schematic, retained but not used. The filename typo is outside the active submission source. |
| `paper/sources/tikz/`, `paper/figures/tikz/` | Standalone wrappers and previews of the retained and historical conceptual diagrams. |
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
| [`literature/05_round0_source_checks.md`](literature/05_round0_source_checks.md) | Targeted usage/load, soft-sensing and inspection-planning checks, with source-access limits. |
| [`literature/06_round1_source_checks.md`](literature/06_round1_source_checks.md) | Verified suitability, decision-analysis, robust-maintenance, and reliability-history sources added in Round 1. |
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
| [`notes/10_round0_revision_plan.md`](notes/10_round0_revision_plan.md) | Eight revision packages responding to the four simulated reviews. |
| [`notes/11_round0_revision_outline.md`](notes/11_round0_revision_outline.md) | Paragraph-level outline for the checklist, procedure, analytical comparison, and approved numerical continuation. |
| [`notes/12_two_door_model_specification.md`](notes/12_two_door_model_specification.md) | Model and numerical inputs explicitly approved by the author on 2026-10-23. |
| [`notes/13_round0_revision_report.md`](notes/13_round0_revision_report.md) | Historical symbolic revision and its verification before numerical approval. |
| [`notes/14_numerical_example_report.md`](notes/14_numerical_example_report.md) | Approved calculation, numerical findings, tests, manuscript integration, and 2026-10-23 PDF verification. |
| [`notes/15_editorial_consistency_report.md`](notes/15_editorial_consistency_report.md) | 2026-10-25 procedure/definition/caption corrections and current PDF verification. |
| [`notes/16_round1_revision_assessment.md`](notes/16_round1_revision_assessment.md) | Historical 2026-10-26 assessment and bounded revision proposal, subsequently authorized. |
| [`notes/17_round1_revision_report.md`](notes/17_round1_revision_report.md) | Implemented Round 1 changes, verification, supplement, and remaining author checks. |
| [`reviews/round0/response_matrix.md`](reviews/round0/response_matrix.md) | Point-by-point dispositions, including partial and unimplemented requests. |
| [`reviews/round1/README.md`](reviews/round1/README.md) | Four simulated reviews of the October 25 manuscript and their common findings. |
| [`reviews/round1/response_matrix.md`](reviews/round1/response_matrix.md) | Dispositions of all major Round 1 comments and grouped minor issues. |
| [`notes/CONVERSATION_INDEX.md`](notes/CONVERSATION_INDEX.md) | Index of the main ChatGPT project conversations and the durable conclusions recovered from them. |

## `simulations/two_door/` — approved hypothetical calculation

[`README.md`](simulations/two_door/README.md) describes the deterministic calculation, exact input file, generated JSON and LaTeX results, and regeneration commands. The example uses rational arithmetic without random sampling. [`tests/test_two_door.py`](tests/test_two_door.py) checks outcome accounting, policy comparisons, ties, continuous bounds, invalid inputs, and artifact regeneration.

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

The Round 1 working draft implements the bounded proposal after checkpoint `0f7a169`. Current author review concerns:

1. The revised scientific argument and declared decision objectives. The current two-door figure render, dimensions, and formats were explicitly approved on 2026-10-26.
2. The red AI declaration, deliberately deferred by the author.
3. Final affiliation presentation and submission-history declarations. Funding scope is retained as instructed.
4. Interpretation of the criterion tradeoff: minimax regret may allow a negative gain in one retained model. Broader model extensions remain separate scope decisions.

## Build/reproducibility status

The Round 1 review draft has 18 pages and compiles without unresolved citations/references, missing characters, or overfull/underfull boxes. The existing non-fatal `xcolor` warning remains. Current visual checks, test evidence, figure approval, and limitations are recorded in [`notes/17_round1_revision_report.md`](notes/17_round1_revision_report.md). Supplement S1 is prepared at [`output/supplement/two-door-calculation.zip`](output/supplement/two-door-calculation.zip), with instructions in [`paper/supplement/README.md`](paper/supplement/README.md); it is not a public deposit. No figure package or external upload was made, and the article has not been submitted.

Build the article from `paper/`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=../build/manuscript template.tex
```

The optional shared diagram renderer has wrappers in `paper/sources/tikz/` and outputs in `paper/figures/tikz/`. Its pinned declarations and instructions are in [`tools/diagrams/README.md`](tools/diagrams/README.md). Compiling the article does not refresh separate diagram previews. The new numerical figure uses [`scripts/plot_two_door.py`](scripts/plot_two_door.py) and [`config/figures.yaml`](config/figures.yaml); see [`tools/figures/README.md`](tools/figures/README.md) for rendering and validation. After the explicit figure approval was recorded on 2026-10-26, the full suite passed 18 tests and 69 subtests, all 16 catalog entries validated, and figure configuration/schema/project-state checks reported zero blockers and zero warnings. The implementation report records the non-fatal warnings and verification limits.

Regenerate the exact numerical artifacts from the repository root with `python3 simulations/two_door/calculate.py`. This standard-library calculation requires no package installation or random seed. Its generated table and continuous analytical boundaries provide the numerical illustration; no empirical station result or stochastic simulation is claimed.
