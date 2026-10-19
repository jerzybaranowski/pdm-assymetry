# Contribution statement — recovered working version

This note reconstructs the contribution logic from retained project conversations. It is **not guaranteed to be the exact final wording** used in the March 2026 manuscript; the canonical LaTeX source should replace this text where it differs.

The retained project context preserves the opening logic:

> This paper challenges prevailing assumptions in predictive maintenance by focusing on industrial systems where maintenance needs are high but condition-monitoring data are scarce, indirect, or entirely unavailable. Instead of proposing a new diagnostic algorithm, the paper advances a system-level perspective on predictive maintenance under structural asymmetry.

The first contribution was explicitly formulated as **reframing predictive maintenance for low-instrumentation systems**.

A faithful reconstruction of the intended contribution set is:

## 1. Reframing predictive maintenance for low-instrumentation systems

The paper identifies a PdM regime involving mass-deployed, individually non-critical assets for which direct condition monitoring can be economically difficult to justify. The maintenance problem remains important at population level even when the observation model is weak at individual-asset level.

The contribution is therefore a **problem formulation / regime identification**, not another fault-classification algorithm.

## 2. Structural asymmetry between maintenance value and information availability

The paper separates two quantities that conventional PdM discussions can implicitly conflate:

- the economic/operational value of making better maintenance decisions; and
- the economic/technical feasibility of collecting direct condition data.

The key argument is that high maintenance value does not imply that rich sensing is economically rational. This creates an asymmetric decision problem that should be analysed explicitly.

## 3. Proxy-, context-, history- and knowledge-based evidence model

The proposed direction is to infer maintenance-relevant latent states from evidence already available in the surrounding system:

- operational logs;
- contextual variables;
- usage proxies;
- documentation;
- inspection and service history;
- fleet-level experience.

The evidence is treated as uncertain and only indirectly informative. This motivates probabilistic/Bayesian modelling of the mapping from available information to latent usage, degradation and failure risk.

## 4. System-level demonstration in a train-station environment

The station case study is intended to show how LD-PdM can be embedded in an environment containing many repeated assets and heterogeneous data sources. Candidate examples include escalators, elevators and automatic doors, with integration into a station digital twin.

The station example is valuable because context collected for traffic/operations can act as maintenance evidence without requiring a dedicated sensor stack on every device.

## 5. Intended research contribution versus review contribution

The paper should not present itself as a comprehensive review of small-data PdM. Literature is used to establish that the relevant ingredients already appear across multiple domains, but the paper’s contribution is the **unifying system-level formulation and research direction**.

## 6. Claims that need especially careful wording

The following formulations are too strong unless backed by evidence:

- “these devices are almost never instrumented”;
- “sensor installation is never economically justified”;
- “PdM is not used for cost cutting on critical installations”;
- “proxy data can replace condition monitoring”.

Preferred formulations should distinguish tendency from universality, for example:

- instrumentation **may be difficult to justify** for large populations of low-unit-value assets;
- critical-asset PdM is **often justified primarily** by avoided downtime, damage or risk;
- proxy/contextual variables provide **partial evidence**, not equivalent measurements;
- the proposed framework addresses cases where direct condition sensing is **unavailable, incomplete or economically unattractive**.

These wording constraints are scientifically important because the paper’s concept is strongest when presented as a distinct regime, not as an overgeneralization about all industrial PdM.
