# Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems

This repository is the canonical working repository for the paper **“Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems”**, currently prepared for *Symmetry*.

The manuscript uses **Limited-Data Predictive Maintenance (LD-PdM)** for a maintenance regime in which direct condition information is structurally weak, indirect, incomplete, or economically difficult to acquire, while maintenance decisions still have meaningful operational or economic value.

> **Current status:** the paper is **not submission-ready**. The prioritized scientific and editorial audit is in [`AUDIT.md`](AUDIT.md).

## Core research idea

The paper is built around a structural asymmetry between **maintenance decision value** and **economically available direct observability**. The motivating contrast is between:

- expensive or critical assets, for which dedicated condition-monitoring instrumentation can often be justified by avoided downtime, damage, or safety consequences; and
- large populations of comparatively ordinary assets—automatic doors, escalators, elevators, HVAC units, vehicle/tool fleets and similar devices—where aggregate maintenance value can be meaningful while rich per-asset sensing is difficult to justify.

In the second regime, maintenance reasoning may need to use operational logs, contextual variables, proxy measurements, service history, documentation, and prior engineering knowledge. Because these sources are only indirectly informative about latent load, degradation, and risk, uncertainty is part of the problem formulation rather than a residual modelling nuisance.

The principal illustrative setting is a **railway station**, where passenger-flow and timetable information can act as proxy evidence for device usage and where maintenance decisions are made across a population of distributed assets.

## Immediate scientific priority: Li et al. (2024)

The closest adjacent work currently identified is:

> C. Li, S. Li, Y. Feng, K. Gryllias, F. Gu, and M. Pecht, “Small data challenges for intelligent prognostics and health management: a review,” *Artificial Intelligence Review*, 57, 214 (2024), DOI `10.1007/s10462-024-10820-4`.

Li et al. already cover limited/imbalanced/incomplete PHM data, costly data acquisition and sensor deployment, and uncertainty under small-data conditions. The present paper therefore cannot claim novelty for data scarcity or sensor economics alone. The intended distinction is the **observation architecture and decision target**: direct condition channels may be persistently absent, proxy/context/history can become primary evidence, and the main objective is maintenance prioritisation and decision support under partial observability.

See [`literature/02_positioning_vs_li2024.md`](literature/02_positioning_vs_li2024.md) and [`AUDIT.md`](AUDIT.md).

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
| [`paper/conceptual_heatmap.tex`](paper/conceptual_heatmap.tex) | Conceptual station maintenance-exposure heatmap. |
| [`paper/pioritisationoutput.tex`](paper/pioritisationoutput.tex) | Illustrative maintenance-prioritisation output. Filename contains a known typo; cleanup is listed in `AUDIT.md`. |
| [`paper/README.md`](paper/README.md) | Manuscript-directory guide, source authority, and build/status notes. |
| `paper/Definitions/` | MDPI class, bibliography styles, journal-name definitions, and template graphics. Treat as vendor/template files unless an MDPI update requires replacement. |

The current Overleaf source was imported in commit `3015f9b285d5333768cc446a04e4278fc547743c`.

## `literature/` — literature synthesis and positioning

| File | What it contains |
|---|---|
| [`literature/01_literature_synthesis.md`](literature/01_literature_synthesis.md) | Cross-domain synthesis of indirect/proxy inference literature and the main literature strands relevant to LD-PdM. |
| [`literature/02_positioning_vs_li2024.md`](literature/02_positioning_vs_li2024.md) | Detailed comparison with Li et al. (2024), including overlap, defensible novelty boundary, and manuscript integration plan. |
| [`literature/candidate_references.bib`](literature/candidate_references.bib) | Candidate references recovered from project discussions that are **not automatically part of the manuscript bibliography**. Includes Li et al. and the optional Bauer–Baranowski paper. |

## `notes/` — durable research decisions and historical project reasoning

| File | What it contains |
|---|---|
| [`notes/01_core_concept.md`](notes/01_core_concept.md) | Core LD-PdM concept, asymmetry, evidence sources, Bayesian motivation, and relation to small-data PHM. |
| [`notes/02_contribution_statement.md`](notes/02_contribution_statement.md) | Recovered contribution logic from the earlier manuscript-development phase. Historical/strategic, not exact current manuscript text. |
| [`notes/03_paper_structure.md`](notes/03_paper_structure.md) | Historical paragraph-level outlining rules plus current guidance on how they relate to the imported source. |
| [`notes/04_train_station_case_study.md`](notes/04_train_station_case_study.md) | Station case-study logic, proxy evidence, digital representation direction, and the proposed quantitative simulation route. |
| [`notes/05_submission_readiness.md`](notes/05_submission_readiness.md) | Historical pre-submission concerns reconciled with the current source; points to `AUDIT.md` for the live checklist. |
| [`notes/06_manuscript_components.md`](notes/06_manuscript_components.md) | Verified record of the current abstract themes, keywords, abbreviations, and candidate self-citation. |
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

## Current major decisions still open

The audit identifies three decisions that dominate the next phase:

1. **Li et al. integration:** redefine the novelty boundary around structural partial observability and decision support, not merely “small data.”
2. **Evidence level:** add a compact quantitative simulation or explicitly reposition the manuscript as a concept/perspective paper and reduce claims accordingly.
3. **Operational definition:** make clear what conditions distinguish LD-PdM from ordinary PdM with a small or incomplete training dataset.

## Build/reproducibility status

The repository contains the MDPI source tree and appears complete relative to the imported Overleaf project, but a clean compilation from a fresh checkout has **not yet been independently recorded in this repository**. This is a P2 task in `AUDIT.md`.

If a quantitative station simulation is added, create a dedicated `simulation/` or `code/` directory with reproducible Python source, fixed seeds, configuration/assumption files, and generated-figure scripts.
