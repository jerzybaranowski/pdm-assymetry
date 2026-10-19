# Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems

This repository is the canonical working repository for the paper **“Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems”**, currently prepared for *Symmetry*.

The manuscript defines **Limited-Data Predictive Maintenance (LD-PdM)** as a predictive-maintenance regime in which maintenance needs remain operationally meaningful while direct condition information is structurally scarce, indirect, incomplete, or economically difficult to acquire. “Low-instrumentation” and “low-observability” describe the regime; the manuscript’s canonical expansion of LD-PdM is **Limited-Data Predictive Maintenance**.

## Core research idea

The central contrast is between:

- expensive or critical assets, where dedicated condition-monitoring instrumentation can often be justified by avoided downtime, damage, or safety consequences; and
- large populations of comparatively ordinary assets—automatic doors, escalators, elevators, HVAC units, vehicle/tool fleets and similar equipment—where aggregate maintenance value may be substantial but rich per-asset sensing can be difficult to justify.

For the second regime, maintenance reasoning can use already-available operational data, proxy variables, contextual information, maintenance histories, documentation, and prior engineering knowledge. Because these sources are only indirectly informative about latent load, degradation, and risk, uncertainty is part of the problem formulation rather than a residual modelling nuisance.

The main illustrative setting is a **railway station**, where passenger-flow and ticketing information can provide indirect evidence of device usage and where maintenance reasoning may ultimately be integrated with a digital representation of the station.

## Canonical manuscript source

The current Overleaf source was imported into `paper/` on 2026-10-19.

- `paper/template.tex` — main manuscript file
- `paper/extracted.bib` — canonical manuscript bibliography at the time of import
- `paper/diagram.tex` — asymmetry/observability figure
- `paper/inferencechain.tex` — inference-chain figure
- `paper/conceptual_heatmap.tex` — station exposure-map figure
- `paper/pioritisationoutput.tex` — prioritisation-output figure
- `paper/Definitions/` — MDPI class, bibliography styles and template assets

The LaTeX source is authoritative for exact wording, section structure, citations, and BibTeX keys. Markdown files preserve project rationale, literature synthesis, decisions, and migration history.

## Repository structure

- `paper/` — canonical manuscript source and figures.
- `notes/` — recovered project discussions, conceptual decisions, case-study notes, and writing rules.
- `literature/` — literature synthesis and positioning notes.
- `references/` — recovered seed references from conversations; `paper/extracted.bib` is the canonical manuscript bibliography.
- `migration/` — provenance, source reconciliation, and recovery status.
- `AGENTS.md` — instructions for future AI-assisted research/coding work in this repository.

## Current migration status

The conceptual material from the ChatGPT project and the current Overleaf source are now both in the repository. The exact historical attachments `Predictive_Maintenance_Concept-submission.pdf`, `Predictive_Maintenance_Concept.zip`, and `outline.pdf` are still not available through the current ChatGPT file interface, but this no longer blocks manuscript work because the current LaTeX source is present.

See `migration/RECOVERY_STATUS.md` and `migration/SOURCE_RECONCILIATION.md` for details.
