# Positioning against Li et al. (2024): small-data PHM versus LD-PdM

## Reference

Chuanjiang Li, Shaobo Li, Yixiong Feng, Konstantinos Gryllias, Fengshou Gu, and Michael Pecht, **“Small data challenges for intelligent prognostics and health management: a review,”** *Artificial Intelligence Review*, 57(8), Article 214, 2024. DOI: `10.1007/s10462-024-10820-4`.

## Why this paper is strategically important

Li et al. are not merely a review of few-shot fault diagnosis. Their scope overlaps with several foundations of the present manuscript. They define small-data PHM in terms of equipment/system status information collected from sensors that is limited in **quantity or quality**, and they discuss causes including heavy investment, access restrictions, complex operating conditions, and multi-factor coupling. They also discuss incomplete and imbalanced data and note that uncertainty quantification becomes more difficult under small-data conditions.

This means the present paper cannot create its novelty boundary by claiming that existing PHM assumes abundant data while LD-PdM uniquely notices cost, imbalance, or uncertainty. Those points already exist explicitly in the literature.

## Claims that Li et al. already establish

The present manuscript should treat the following as prior art rather than novelty:

- PHM often operates with limited high-quality data;
- healthy/normal observations dominate while abnormal/fault data are scarce;
- data can be incomplete, unlabeled, mislabeled, or imbalanced;
- industrial data acquisition can be expensive;
- digital upgrading and installing sensors across many machines can create an ROI barrier;
- changing/complex working conditions make complete data collection unrealistic;
- small-data conditions weaken model generalization and increase predictive uncertainty;
- data augmentation, transfer learning, and few-shot/meta-learning are established responses to small-data PHM.

Li et al. also include maintenance execution within the functional PHM lifecycle, so the distinction cannot simply be “they do diagnosis while we do maintenance.”

## The distinction that remains defensible

The strongest boundary is **not temporary versus structural scarcity alone**. Li et al. already identify economic and operational causes that can persist.

The more defensible distinction is the **observation architecture and the role of the model in the decision process**.

### Li et al.: small-data PHM

Their problem formulation remains centered on limited equipment/system status datasets and the question of how intelligent PHM tasks can be performed reliably when monitoring data are insufficient in quantity or quality. The methodological center of gravity is therefore model learning and generalization under limited condition/fault data.

### LD-PdM: weak direct observability as the maintenance regime

The present paper should focus on settings in which direct condition channels may be absent or too weak to constitute the main data source at all. Evidence can instead consist primarily of:

- proxy variables collected for non-maintenance purposes;
- contextual/operational information;
- maintenance and inspection histories;
- documentation and engineering priors;
- fleet/population information.

The central object is then not a small labeled condition dataset but a **belief state over latent maintenance-relevant quantities under heterogeneous indirect evidence**.

The primary output is also different: the paper should emphasize inspection priority, maintenance attention, resource allocation, risk bands, and value of information rather than the accuracy of a classifier or RUL predictor.

## Comparison table

| Dimension | Li et al. (2024) | LD-PdM direction |
|---|---|---|
| Data limitation | limited quantity and/or quality of sensor-collected status data | direct condition data can be persistently absent; indirect evidence can dominate |
| Economic barriers | explicitly recognized as a cause of small data | used to define the observation regime and motivate whether information acquisition is worthwhile |
| Typical evidence | equipment monitoring/status samples | proxies, context, service history, priors, partial sensing, fleet information |
| Main methodological focus | data-efficient AD/FD/RUL learning | structured inference under partial observability + maintenance decision support |
| Main remedies | augmentation, transfer learning, few-shot/meta-learning | observation models, hierarchical/probabilistic inference, uncertainty propagation, decision/value-of-information logic |
| Evaluation emphasis | model performance and fair small-data evaluation | decision relevance, ranking/prioritisation, robustness, cost/risk consequences |
| Scale argument | not the main organizing principle | weak asset-level evidence can still support useful population-level allocation decisions |

## Important consequence for the term “Limited-Data Predictive Maintenance”

The term itself is vulnerable to being read as a synonym for small-data PHM. Therefore the manuscript must define “limited data” in a more specific way than sample size.

A useful operational definition should state that LD-PdM applies when:

1. a maintenance decision has meaningful operational/economic value;
2. at least one decision-relevant direct condition variable is persistently unavailable, weakly observed, or uneconomic to obtain;
3. indirect/contextual/historical evidence therefore plays a material role in inference; and
4. the objective is maintenance action or prioritisation under uncertainty, not merely recovery of predictive accuracy from a small condition dataset.

If this remains difficult to communicate after revision, “limited-observability” should be used prominently as a descriptor even if the canonical acronym remains LD-PdM.

## How Li et al. should enter the manuscript

### Introduction

Cite Li et al. after establishing data scarcity and before claiming a distinct LD-PdM regime. Acknowledge that small-data PHM already covers economic, incomplete, and imbalanced-data causes. Then state the narrower gap: small-data methods still generally presuppose a direct monitoring/status dataset, whereas LD-PdM is concerned with maintenance when the relevant condition channels themselves may be absent and indirect evidence becomes primary.

The current sentence implying that data scarcity is typically treated merely as an engineering inconvenience should be rewritten; it is too strong in light of Li et al.

### Asymmetry of failure data

Li et al. can support the background claim about incomplete and imbalanced PHM data. The manuscript must then move beyond this to censoring, intervention-truncated trajectories, and the weak observation of the latent maintenance state.

### Asymmetry of costs and incentives

Li et al. are directly relevant because they identify heavy investment and large-scale sensor installation as causes of small-data PHM. This strengthens the economic motivation but simultaneously removes “sensors are costly” as a novelty claim. The novelty must lie in what follows from that constraint for the observation and decision architecture.

### Discussion

Add small-data PHM explicitly alongside CBM, sensor-rich PdM, risk-based maintenance, and digital-twin approaches. The discussion should explain overlap as well as difference rather than presenting LD-PdM as an isolated category.

## Recommended positioning paragraph

A manuscript-ready paragraph should be drafted during the substantive revision, but the intended logic is:

> Recent small-data PHM research already recognizes that monitoring datasets may be limited, incomplete, or imbalanced because of economic and operational constraints, and it develops data-efficient methods such as augmentation, transfer learning, and few-shot learning. The regime considered here overlaps with that literature but is narrower in a different dimension: the direct condition variables required by conventional PHM may themselves remain persistently unobserved, so maintenance reasoning must rely materially on proxy, contextual, historical, and prior evidence. We therefore treat the central problem as partial observability and decision support rather than sample efficiency alone.

Do not copy this mechanically; it should be integrated into the narrative and supported by the surrounding references.

## What the paper should no longer say

Avoid formulations equivalent to:

- “existing PHM treats data scarcity only as a temporary problem”;
- “our novelty is that sensing is expensive”;
- “small-data PHM is only about classification”;
- “Bayesian uncertainty treatment is absent from small-data PHM.”

Li et al. explicitly discuss persistent causes, PHM tasks beyond classification, and uncertainty quantification. The present paper’s contribution must therefore be more precise.

## One-sentence strategic boundary

> **LD-PdM should be positioned as predictive maintenance under persistently weak direct observability, where heterogeneous indirect evidence is used to support decisions, rather than as another method for learning from a small condition-monitoring dataset.**
