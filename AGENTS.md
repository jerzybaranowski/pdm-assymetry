# AGENTS.md

## Project scope

This repository supports the paper **“Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems”** and related simulations/figures.

The manuscript’s canonical term is **Limited-Data Predictive Maintenance (LD-PdM)**. “Low-instrumentation” and especially “limited/low observability” are useful descriptors of the regime, but should not silently replace the established acronym in manuscript-facing text unless the author explicitly decides to rename it.

The paper is a high-concept research statement, not a conventional systematic review and not primarily an algorithm paper. Its purpose is to identify and formalize a maintenance regime in which maintenance decision value and the availability of direct condition information are structurally asymmetric.

## Current work plan

Before editing the manuscript substantively, read [`AUDIT.md`](AUDIT.md). It is the current prioritized action plan and supersedes older statements that the paper is close to submission.

## Canonical source

- Main manuscript: `paper/template.tex`
- Canonical manuscript bibliography: `paper/extracted.bib`
- Manuscript figures: `paper/diagram.tex`, `paper/inferencechain.tex`, `paper/conceptual_heatmap.tex`, `paper/pioritisationoutput.tex`
- MDPI template assets: `paper/Definitions/`

If a Markdown research/migration note conflicts with the imported manuscript on exact wording, terminology, section numbering, citations, or BibTeX keys, the LaTeX source is authoritative **for current manuscript state**. Markdown notes may nevertheless identify changes that the manuscript still needs.

## Research stance

- Be critical but not contrarian.
- Challenge unsupported assumptions, especially claims about sensor economics, prevalence of PdM practices, and generality across asset classes.
- Do not manufacture novelty by renaming established small-data PHM, CBM, virtual sensing, sensorless diagnostics, or risk-based maintenance concepts.
- The intended contribution is the **system-level framing of persistent weak direct observability as a maintenance decision regime**, together with proxy/context/history-based probabilistic inference and decision-oriented evaluation.
- Do not define the novelty simply as “structural rather than temporary data scarcity”; adjacent literature also recognizes persistent economic and operational causes of small data.

## Language and writing

- Research/manuscript content is written **exclusively in English**.
- If Polish appears in draft research text, translate/correct it rather than continuing in Polish.
- Use LaTeX and BibTeX for the paper and Python for computation/simulation.
- Do not invent references, BibTeX keys, numerical claims, industrial costs, or empirical findings.
- Preserve established BibTeX keys in `paper/extracted.bib` unless there is a concrete reason to change them.
- Prefer precise engineering language over promotional or generic AI phrasing.
- Distinguish measured, simulated, inferred, and purely conceptual quantities explicitly.

## Manuscript structure rules recovered from the project

- Detailed outlines should be built as chains of bullets in which **one bullet corresponds to one intended paragraph and one coherent message**.
- Figures/tables needed by a section are represented as separate outline bullets.
- The December 2025 outline used a convention in which references were attached to paragraph-level bullets and collected at subsection ends. Treat this as an outlining aid; do not force it onto the current manuscript if the imported LaTeX uses normal in-text citations.
- Figures in the Introduction should be used only when they make a necessary conceptual point.

## Core claims that must remain distinct

1. Fault/condition data are often scarce and strongly imbalanced toward healthy operation.
2. Adding sensors to existing infrastructure has installation, integration, validation, networking, maintenance, and lifecycle costs—not merely sensor purchase cost.
3. Critical/high-consequence assets can justify dedicated condition monitoring because avoided failure consequences can dominate instrumentation cost.
4. Large populations of less critical assets may offer substantial aggregate maintenance value while rich sensing of each unit remains unattractive or unavailable.
5. In such settings, maintenance reasoning may need to use already-available signals, event logs, contextual variables, proxy measurements, documentation, and service history.
6. Indirect evidence creates an observation problem: uncertainty must be represented explicitly rather than hidden inside a point score.
7. The primary research target is maintenance decision support under weak direct observability, not merely recovery of classifier/RUL accuracy from a small dataset.

## Main case-study direction

Use devices in a railway station as the principal system-level example. The current manuscript contains a station-based illustrative architecture and a probabilistic interpretation of proxy-based load/degradation/risk. Candidate assets include automatic doors, escalators, elevators, and related service infrastructure.

A canonical proxy example is passenger/ticket-flow information as indirect evidence of device usage when direct load/condition sensing is absent.

The related GPECOM work on railway-station doors and elevators may be reused/cited where scientifically appropriate, but it must remain clearly distinguished from the present conceptual paper.

## Relationship to Li et al. (2024)

The paper **“Small data challenges for intelligent prognostics and health management: a review”** (*Artificial Intelligence Review*, 57:214, DOI `10.1007/s10462-024-10820-4`) is mandatory positioning material.

Important correction to earlier project shorthand: Li et al. do **not** only discuss temporary sample scarcity. They explicitly cover limited quantity/quality of monitoring data, heavy investment and ROI barriers, large-scale sensor installation, incomplete and imbalanced data, complex operating conditions, and uncertainty under small-data conditions. Their main solution families are data augmentation, transfer learning, and few-shot learning.

Therefore:

- do not claim novelty for data scarcity, imbalance, sensor cost, or uncertainty alone;
- do not claim that small-data PHM is only fault classification;
- position LD-PdM around **persistent weak direct observability**, heterogeneous indirect evidence, and maintenance decisions;
- make proxy/context/history evidence and population-level decision value central;
- evaluate proposed methods by decision relevance/robustness in addition to predictive metrics.

Read `literature/02_positioning_vs_li2024.md` before revising the Introduction or Discussion.

At the time of this audit, Li et al. are not yet integrated into `paper/template.tex` or `paper/extracted.bib`; `literature/candidate_references.bib` contains a candidate BibTeX entry.

## Repository discipline

- GitHub is the canonical project record.
- `AUDIT.md` is the current task/status document.
- Put durable research decisions in Markdown under `notes/` or `literature/` rather than leaving them only in chat.
- Put reproducible simulations in Python source with fixed seeds and explicit assumptions.
- Keep generated numerical figures reproducible from code where possible.
- Do not replace canonical manuscript text with reconstructed chat text without comparing the two.
- Do not add candidate references to `paper/extracted.bib` unless they are actually used in the manuscript.
- When modifying `paper/template.tex`, keep the paper’s distinction between conceptual/system-level contribution and algorithmic novelty visible throughout.

## Handling uncertainty in user intent

The project owner sometimes submits an incomplete message accidentally. If a request is genuinely incomplete or ambiguous in a way that changes the research result, ask rather than guessing.
