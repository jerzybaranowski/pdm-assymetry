# Positioning against Li et al. (2024): small-data PHM versus LD-PdM

## Reference

Chuanjiang Li, Shaobo Li, Yixiong Feng, Konstantinos Gryllias, Fengshou Gu, and Michael Pecht, **“Small data challenges for intelligent prognostics and health management: a review,”** *Artificial Intelligence Review*, 57(8), Article 214, 2024. DOI: 10.1007/s10462-024-10820-4.

The paper explicitly identifies high-cost data collection and complex operating conditions as causes of small-data problems in PHM and reviews mainstream methodological responses including data augmentation, transfer learning and few-shot learning.

## Why the overlap matters

Li et al. already establish several claims that the present paper must **not** present as novel:

- PHM frequently operates under limited data;
- fault information is costly to obtain;
- real operating conditions complicate data collection;
- modern deep-learning PHM methods can fail when data are limited;
- data-efficient methods are an active research topic.

A manuscript that only states that “PdM has too little fault data” would therefore be insufficiently differentiated.

## Main distinction

The strongest distinction is the nature of the problem being solved.

### Li et al.: small-data learning problem

The central question is approximately:

> How can intelligent PHM models still be trained effectively when the desired fault/condition dataset is small?

This naturally motivates:

- data augmentation;
- transfer learning;
- few-shot learning;
- benchmark datasets;
- experimental protocols for evaluating models under limited training data.

The implicit goal remains to obtain a better diagnostic/prognostic model from scarce condition/fault data.

### Present paper: structurally weak observation and maintenance decision problem

The central question is instead:

> How should predictive maintenance be formulated when direct condition data may remain weak or unavailable because acquiring them is economically or operationally unjustified?

This changes the methodological center of gravity toward:

- proxy and contextual observations;
- maintenance/service history;
- prior engineering knowledge;
- latent-state probabilistic models;
- uncertainty propagation;
- fleet-level inference;
- value of information;
- sensing/inspection economics;
- maintenance decisions under partial observability.

The scarcity is not necessarily something that should or can be “fixed” by collecting a larger labeled condition dataset.

## Structural versus accidental scarcity

A useful formulation for the manuscript is to distinguish:

- **accidental/temporary small data** — the desired variables exist conceptually, but too few training examples have been collected; and
- **structural low observability** — the desired condition variables are not measured, are only indirectly observed, or are unlikely to be measured because richer instrumentation does not pass an economic/operational justification test.

The present paper is primarily about the second case.

## Economic asymmetry as the differentiator

The paper’s distinctive claim should be that **maintenance value and sensing value are not the same quantity**.

A fleet may have high aggregate maintenance cost and therefore strong motivation for better maintenance decisions, while the marginal value of adding a condition sensor to each individual asset remains below its lifecycle deployment cost.

This produces an asymmetry that is not captured by treating data scarcity solely as a machine-learning sample-efficiency problem.

## Asset-class distinction

Li et al. cover PHM generally. The present paper can sharpen its own contribution by contrasting:

- high-value/high-consequence assets that can justify dedicated condition monitoring; with
- repeated, individually less critical devices where the business case for rich sensing is weaker despite aggregate maintenance burden.

Automatic doors, escalators, elevators and HVAC-related devices are useful because they make this distinction intuitive.

## Recommended manuscript changes

To avoid conceptual collision with Li et al.:

1. **Cite Li et al. early** when introducing data scarcity in PHM.
2. State explicitly that the present work does not claim discovery of the small-data problem.
3. Define LD-PdM through **persistent low instrumentation / indirect observability**, not merely through sample count.
4. Include sensor/deployment economics as part of the problem definition.
5. Make proxy/context/history-based evidence central rather than incidental.
6. Use Bayesian/probabilistic modelling to represent uncertainty created by indirect evidence.
7. Show at least one decision-level simulation or quantitative example; otherwise the paper risks appearing as an essay adjacent to an existing review literature.
8. Avoid presenting transfer learning, few-shot learning or data augmentation as the principal remedy, because doing so would move the paper back into Li et al.’s territory.

## One-sentence positioning statement

A concise distinction suitable for the Introduction is:

> Existing small-data PHM research primarily asks how to learn effectively from limited condition and fault data; we address the complementary regime in which direct condition data are structurally limited because instrumentation itself may be economically unjustified, requiring maintenance decisions to be built from uncertain proxy, contextual and historical evidence.

This sentence should be adapted to the manuscript’s exact terminology but captures the strategic boundary that must remain visible throughout the paper.
