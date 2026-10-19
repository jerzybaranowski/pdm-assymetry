# AGENTS.md

## Project scope

This repository supports the paper **“Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems”** and related simulations/figures.

The manuscript’s canonical term is **Limited-Data Predictive Maintenance (LD-PdM)**. “Low-instrumentation” and “low-observability” describe the regime, but should not silently replace the established expansion of the acronym in manuscript text.

The paper is a high-concept research statement, not a conventional systematic review and not primarily an algorithm paper. Its purpose is to identify and formalize a maintenance regime in which the economic/operational need for predictive maintenance and the availability of direct condition data are structurally asymmetric.

## Canonical source

- Main manuscript: `paper/template.tex`
- Canonical manuscript bibliography: `paper/extracted.bib`
- Manuscript figures: `paper/diagram.tex`, `paper/inferencechain.tex`, `paper/conceptual_heatmap.tex`, `paper/pioritisationoutput.tex`
- MDPI template assets: `paper/Definitions/`

If a Markdown migration/research note conflicts with the imported manuscript on exact wording, terminology, section numbering, citations, or BibTeX keys, the LaTeX source is authoritative unless the project owner explicitly decides to revise it.

## Research stance

- Be critical but not contrarian.
- Challenge unsupported assumptions, especially claims about sensor economics, prevalence of PdM practices, and generality across asset classes.
- Do not manufacture novelty by renaming established “small data”, PHM, CBM, virtual sensing, or sensorless-diagnostics concepts.
- The intended novelty is the **system-level framing of persistent low observability / limited instrumentation as a structurally constrained PdM regime**, together with proxy/context/history-based probabilistic inference and a decision-oriented perspective.
- Clearly distinguish a dataset that happens to be small from a system that is expected to remain weakly observed because collecting direct condition data is unavailable, impractical, or economically unjustified.

## Language and writing

- Research/manuscript content is written **exclusively in English**.
- If Polish appears in draft research text, translate/correct it rather than continuing in Polish.
- Use LaTeX and BibTeX for the paper and Python for computation/simulation.
- Do not invent references, BibTeX keys, numerical claims, industrial costs, or empirical findings.
- Preserve established BibTeX keys in `paper/extracted.bib` unless there is a concrete reason to change them.
- Prefer precise engineering language over promotional or generic AI phrasing.

## Manuscript structure rules recovered from the project

- Detailed outlines should be built as chains of bullets in which **one bullet corresponds to one intended paragraph and one coherent message**.
- Figures/tables needed by a section are represented as separate outline bullets.
- The December 2025 outline used a convention in which references were attached to paragraph-level bullets and collected at subsection ends. Treat this as an outlining aid; do not force it onto the current manuscript if the imported LaTeX uses normal in-text citations.
- Figures in the Introduction should be used only when they make a necessary conceptual point.

## Core claims that must remain distinct

1. Fault/condition data are often scarce and strongly imbalanced toward healthy operation.
2. Adding sensors in existing industrial infrastructure has installation, integration, validation, networking, maintenance, and lifecycle costs—not merely sensor purchase cost.
3. Critical or very expensive assets can justify dedicated condition monitoring because avoided consequences of failure can dominate instrumentation cost.
4. Large populations of less critical assets may offer substantial aggregate maintenance value while individual assets do not justify rich instrumentation.
5. In that regime, PdM may have to use already-available signals, event logs, contextual variables, proxy measurements, documentation, and service history.
6. The uncertainty introduced by indirect evidence should be represented explicitly; Bayesian/probabilistic modelling is therefore structurally motivated rather than ornamental.

## Main case-study direction

Use devices in a railway station as the principal system-level example. The current manuscript uses a station-based illustrative case and a probabilistic interpretation of proxy-based load/degradation/risk. Candidate asset classes discussed in the project include automatic doors, escalators, elevators and HVAC-related equipment.

A canonical proxy example is passenger/ticket-flow information as indirect evidence of device usage when direct load/condition sensing is absent.

The related GPECOM work on railway-station doors and elevators may be reused/cited where scientifically appropriate, but it must remain clearly distinguished from the present conceptual paper.

## Relationship to Li et al. (2024)

The paper **“Small data challenges for intelligent prognostics and health management: a review”** (*Artificial Intelligence Review*, 57:214, DOI 10.1007/s10462-024-10820-4) is close enough conceptually that positioning against it is mandatory.

Do not claim novelty for observing that PHM faces small-data problems. Li et al. treat small data mainly as a methodological obstacle and review remedies such as data augmentation, transfer learning and few-shot learning. This project must instead emphasize persistent, economically induced low observability and maintenance decision-making when direct sensing is structurally unavailable or unjustified.

At the time of source import (2026-10-19), Li et al. were **not yet present in `paper/extracted.bib` or cited in `paper/template.tex`**. This is a known manuscript-finalization task, not an optional literature expansion.

## Repository discipline

- GitHub is now the canonical project record.
- Put durable research decisions in Markdown under `notes/` or `literature/` rather than leaving them only in chat.
- Put reproducible simulations in Python scripts/notebooks with fixed seeds and explicit assumptions.
- Keep generated figures reproducible from code where possible.
- Do not replace canonical manuscript text with reconstructed chat text without comparing the two.
- When modifying `paper/template.tex`, keep the paper’s central distinction between conceptual/system-level contribution and algorithmic novelty visible throughout.

## Handling uncertainty in user intent

The project owner sometimes submits an incomplete message accidentally. If a request is genuinely incomplete or ambiguous in a way that changes the research result, ask rather than guessing.
