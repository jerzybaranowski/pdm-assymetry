# AGENTS.md

## Project scope

This repository supports the paper **“Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems”** and related simulations/figures.

The paper is a high-concept research statement, not a conventional systematic review and not primarily an algorithm paper. Its purpose is to identify and formalize a maintenance regime in which the economic need for predictive maintenance and the availability of direct condition data are structurally asymmetric.

## Research stance

- Be critical but not contrarian.
- Challenge unsupported assumptions, especially claims about sensor economics, prevalence of PdM practices, and generality across asset classes.
- Do not manufacture novelty by renaming established “small data”, PHM, CBM, or sensorless-diagnostics concepts.
- The intended novelty is the **system-level framing of persistent low observability / low instrumentation as an economically induced PdM regime**, together with proxy/context/history-based probabilistic inference and a decision-oriented perspective.
- Clearly distinguish a dataset that happens to be small from a system that is expected to remain weakly observed because collecting direct condition data is not economically justified.

## Language and writing

- Research/manuscript content is written **exclusively in English**.
- If Polish appears in draft research text, translate/correct it rather than continuing in Polish.
- Use LaTeX and BibTeX for the paper and Python for computation/simulation.
- Do not invent references, BibTeX keys, numerical claims, industrial costs, or empirical findings.
- Preserve established BibTeX keys once the canonical bibliography is imported.
- Prefer precise engineering language over promotional or generic AI phrasing.

## Manuscript structure rules recovered from the project

- Detailed outlines should be built as chains of bullets in which **one bullet corresponds to one intended paragraph and one coherent message**.
- Figures/tables needed by a section are represented as separate outline bullets.
- For the Introduction, references were intended to be concentrated in Sections 1.1–1.3; Section 1.4 (contribution statement) was treated as effectively locked during the outline phase.
- A previous working convention requested a bulk citation list at the end of each subsection in the detailed LaTeX outline. Preserve this convention unless the manuscript source shows it was subsequently changed.

## Core claims that must remain distinct

1. Fault/condition data are often scarce and strongly imbalanced toward healthy operation.
2. Adding sensors in existing industrial infrastructure has a real installation, integration, validation, networking, maintenance, and lifecycle cost—not merely a sensor purchase price.
3. Critical or very expensive assets can justify dedicated condition monitoring because the avoided consequence of failure dominates instrumentation cost.
4. Large populations of less critical assets may offer large aggregate cost-saving potential while individual assets do not justify rich instrumentation.
5. In that regime, PdM must often use already-available signals, event logs, contextual variables, proxy measurements, documentation, and service history.
6. The uncertainty introduced by indirect evidence should be represented explicitly; Bayesian/probabilistic modelling is therefore a natural framework, not an ornamental choice.

## Main case-study direction

Use devices in a train station as the principal system-level example, potentially integrated with a station digital twin. Candidate asset classes include automatic doors, escalators, elevators and HVAC-related equipment. Reuse the elevator and automatic-door examples from the related GPECOM work where scientifically appropriate.

A canonical proxy example is passenger/ticket-flow information as indirect evidence of escalator usage when direct people/load sensing is absent.

## Relationship to Li et al. (2024)

The paper **“Small data challenges for intelligent prognostics and health management: a review”** (Artificial Intelligence Review, 57:214, DOI 10.1007/s10462-024-10820-4) is close enough conceptually that positioning against it is mandatory.

Do not claim novelty for observing that PHM faces small-data problems. Li et al. study small data mainly as a methodological obstacle and review remedies such as data augmentation, transfer learning and few-shot learning. This project must instead emphasize persistent, economically induced low observability and maintenance decision-making when direct sensing is structurally unavailable or unjustified.

## Repository discipline

- Treat GitHub as the canonical project record once the Overleaf source is imported.
- Put durable research decisions in Markdown under `notes/` or `literature/` rather than leaving them only in chat.
- Put reproducible simulations in Python scripts/notebooks with fixed seeds and explicit assumptions.
- Keep generated figures reproducible from code where possible.
- Never overwrite the canonical manuscript with a reconstructed version when an exact source can be obtained from Overleaf.

## Handling uncertainty in user intent

The project owner sometimes submits an incomplete message accidentally. If a request is genuinely incomplete or ambiguous in a way that changes the research result, ask rather than guessing.
