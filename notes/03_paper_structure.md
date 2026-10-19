# Manuscript structure and outlining rules

This file preserves the paragraph-level outlining method developed during the 2025-12 project phase. The current manuscript source is now available in `../paper/template.tex`; therefore this note is a **writing method and historical design record**, not an authoritative table of contents.

## Historical Introduction logic

The Introduction was designed around four conceptual moves:

1. **PdM as decision-making under uncertainty.** Predictive maintenance is not merely signal processing/classification; it supports actions under uncertain condition and future evolution.
2. **LD-PdM as a distinct observation regime.** Maintenance decisions can remain important while direct condition information is structurally weak, sparse, indirect, or absent.
3. **Probabilistic/Bayesian motivation.** Proxy, contextual, historical, and prior evidence require explicit uncertainty representation.
4. **Contribution statement.** The contribution is a problem formulation/system-level framing rather than a new diagnostic algorithm.

This logic informed the 2026-10-19 revision, which now incorporates Li et al. and existing decision-analysis work without claiming novelty for scarcity, instrumentation cost, or uncertainty alone.

## Paragraph-level outlining convention

For future restructuring:

- one bullet = one future paragraph;
- one paragraph = one coherent message;
- do not combine independent claims merely to shorten the outline;
- attach references to the message they actually support;
- treat required figures/tables as separate outline bullets;
- explicitly mark whether a paragraph contains background, gap, contribution, evidence, or limitation.

The convention was used for the revision plan in `07_publication_completion_plan.md`. The revised manuscript has seven main sections and retains its conceptual, non-review identity.

## Citation rule

The historical outline concentrated background references before the contribution statement. The current manuscript uses normal in-text citations. Do not force historical bulk-citation formatting into the source.

The key current citation requirement is that Li et al. (2024) must appear **before or at the point where LD-PdM is defined**, because the manuscript must acknowledge the existing small-data PHM framing before stating the narrower gap.

## Figures in the Introduction

Keep the original rule: include an Introduction figure only if it is necessary to formalize the asymmetry. A two-axis regime figure (maintenance decision value versus economically available direct observability) could justify itself because it would operationalize the title concept; purely decorative figures should remain outside the Introduction.

## Original source issues addressed by the revision

See the current dispositions in `../AUDIT.md` and the implementation report in `08_manuscript_revision_report.md`:

- unsupported simulation promises were removed;
- drafting headings such as “Section positioning” and “Section opening paragraph” were removed;
- the Discussion now positions LD-PdM relative to small-data PHM and established indirect-sensing and decision-analysis approaches.
