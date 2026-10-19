# Manuscript structure and outlining rules

This file preserves the paragraph-level outlining method developed during the 2025-12 project phase. The current manuscript source is now available in `../paper/template.tex`; therefore this note is a **writing method and historical design record**, not an authoritative table of contents.

## Historical Introduction logic

The Introduction was designed around four conceptual moves:

1. **PdM as decision-making under uncertainty.** Predictive maintenance is not merely signal processing/classification; it supports actions under uncertain condition and future evolution.
2. **LD-PdM as a distinct observation regime.** Maintenance decisions can remain important while direct condition information is structurally weak, sparse, indirect, or absent.
3. **Probabilistic/Bayesian motivation.** Proxy, contextual, historical, and prior evidence require explicit uncertainty representation.
4. **Contribution statement.** The contribution is a problem formulation/system-level framing rather than a new diagnostic algorithm.

This logic remains useful, but the current Introduction must now be revised to incorporate Li et al. (2024) and to avoid overstating novelty for data scarcity, instrumentation cost, or uncertainty themselves.

## Paragraph-level outlining convention

For future restructuring:

- one bullet = one future paragraph;
- one paragraph = one coherent message;
- do not combine independent claims merely to shorten the outline;
- attach references to the message they actually support;
- treat required figures/tables as separate outline bullets;
- explicitly mark whether a paragraph contains background, gap, contribution, evidence, or limitation.

This convention is particularly useful for the next Introduction/Discussion rewrite because the Li et al. comparison needs to be integrated without turning the paper into a review.

## Citation rule

The historical outline concentrated background references before the contribution statement. The current manuscript uses normal in-text citations. Do not force historical bulk-citation formatting into the source.

The key current citation requirement is that Li et al. (2024) must appear **before or at the point where LD-PdM is defined**, because the manuscript must acknowledge the existing small-data PHM framing before stating the narrower gap.

## Figures in the Introduction

Keep the original rule: include an Introduction figure only if it is necessary to formalize the asymmetry. A two-axis regime figure (maintenance decision value versus economically available direct observability) could justify itself because it would operationalize the title concept; purely decorative figures should remain outside the Introduction.

## Current source issues relevant to structure

See `../AUDIT.md`. In particular:

- the Introduction currently promises an “illustrative simulation” although the active station sections are conceptual;
- active drafting headings such as “Section positioning” and “Section opening paragraph” remain in the manuscript;
- the Discussion should explicitly position LD-PdM relative to small-data PHM, not only CBM/risk-based maintenance/digital twins.
