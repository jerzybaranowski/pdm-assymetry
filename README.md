# Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems

This repository is the working repository for the paper currently titled **“Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems”**, intended for submission to *Symmetry* (Engineering and Materials section).

The repository is intended to become the single source of truth for the project: manuscript source, bibliography, simulations, figures, literature notes, and research decisions should live here rather than only in ChatGPT conversations or Overleaf.

## Core research idea

The paper studies a structural asymmetry in predictive maintenance (PdM): assets may create a meaningful maintenance burden while providing too little direct condition information to support conventional sensor-centric PdM economically.

The central contrast is between:

- expensive or critical assets, where dedicated condition-monitoring instrumentation can be justified mainly by avoided downtime, damage, or safety consequences; and
- large populations of comparatively ordinary assets—automatic doors, escalators, elevators, HVAC units, vehicle/tool fleets and similar equipment—where substantial aggregate maintenance savings may exist but per-asset sensing can be difficult to justify.

For the second regime, the paper develops the idea of **low-data / low-instrumentation PdM (LD-PdM)** based on already available operational data, proxy variables, contextual information, documentation and maintenance histories, represented probabilistically rather than assuming that missing condition sensors can simply be added.

The main application setting is a **train station**, with possible integration of maintenance reasoning into a station digital twin. A key proxy-data example is using passenger-flow or ticketing information as indirect evidence of escalator usage when the escalator itself is not instrumented for load estimation.

## Repository structure

- `paper/` — manuscript source. The latest Overleaf/LaTeX source still has to be imported.
- `notes/` — recovered project discussions, conceptual decisions, case-study notes, and writing rules.
- `literature/` — literature synthesis and positioning notes.
- `references/` — recovered/seed BibTeX entries; not yet a complete bibliography.
- `migration/` — provenance and recovery status for the ChatGPT-project migration.
- `AGENTS.md` — instructions for future work performed by AI coding/research agents in this repository.

## Current status

A near-submission manuscript existed in March 2026 and was reviewed in the ChatGPT project before intended submission to *Symmetry*. The current ChatGPT file interface does **not** expose the previously uploaded `Predictive_Maintenance_Concept-submission.pdf`, `Predictive_Maintenance_Concept.zip`, or `outline.pdf`, so their bytes have not been copied here. The latest LaTeX source should therefore be imported from Overleaf (or re-uploaded) before manuscript editing continues.

See `migration/RECOVERY_STATUS.md` for details.
