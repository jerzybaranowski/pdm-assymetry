# Symmetry submission-readiness notes

## Target

The working target is *Symmetry*, section **Engineering and Materials**.

By March 2026 the manuscript was described as almost ready and underwent a final project-level review before submission.

## Main remaining scientific issue identified before submission

The most important positioning issue is overlap with Li et al. (2024), *Small data challenges for intelligent prognostics and health management: a review*.

The manuscript must not claim novelty for the existence of data scarcity in PHM. Its novelty has to rest on the structural asymmetry between maintenance need and direct data availability, the economics of instrumentation, and the use of uncertain proxy/context/history information for decision support.

See `../literature/02_positioning_vs_li2024.md`.

## Case-study strengthening

A concrete way to strengthen the paper was to reuse the **elevator and automatic-door examples from the related GPECOM work**. These examples fit the paper better than another highly instrumented rotating-machine example because they illustrate assets that are widespread, maintenance-relevant and not obviously candidates for expensive bespoke condition-monitoring systems.

The station case should preferably connect these examples into one system-level argument rather than present them as unrelated mini-cases.

## Critical checks before submission

### 1. Define LD-PdM operationally

The term should be defined through observability/instrumentation/evidence structure, not through an arbitrary sample-count threshold.

A useful definition must answer:

- what makes an asset low-instrumentation;
- what kinds of evidence remain available;
- what distinguishes LD-PdM from conventional PdM with a small training set;
- what decision problem LD-PdM is intended to solve.

### 2. Substantiate sensor-economics claims

The paper’s central economic argument is vulnerable if sensing cost is treated rhetorically.

Where possible, distinguish:

- sensor hardware cost;
- installation and wiring;
- gateway/network integration;
- commissioning/validation;
- data infrastructure;
- cybersecurity/IT integration where relevant;
- ongoing calibration/maintenance;
- lifecycle replacement.

The paper does not need a universal cost model, but it needs credible evidence that instrumentation decisions are asset- and context-dependent.

### 3. Avoid universal claims

Statements such as “mass-deployed devices are almost never instrumented” are too broad. The scientifically defensible claim is that for some large asset populations, **additional dedicated condition sensing may be economically difficult to justify** even when aggregate maintenance burden is high.

### 4. Keep proxy evidence probabilistic

Ticketing/passenger information is not “the escalator load”. It is uncertain evidence about a latent usage variable. The paper’s Bayesian framing becomes convincing only if this distinction is explicit.

### 5. Provide a quantitative demonstration

A purely conceptual station example may be insufficient for a research article. At least one simulation should demonstrate how:

- degraded information quality changes decision quality;
- proxy information improves over history/calendar-only maintenance;
- a direct sensor provides additional value at additional cost;
- conclusions depend on the relative costs of failure, inspection, maintenance and information acquisition.

### 6. Make the “asymmetry” explicit enough for Symmetry

Because the paper is submitted to *Symmetry*, the asymmetry should not appear only in the title. It should be a formal organizing construct throughout the manuscript.

A useful representation is a two-axis or two-regime diagram:

- horizontal axis: maintenance/decision value or consequence of failure;
- vertical axis: economically available condition information / observability.

The target quadrant is high maintenance value with low direct information availability. A related figure could contrast information demand and economically feasible information supply.

The journal fit is much stronger if the paper develops this asymmetry explicitly rather than using “asymmetric” as a descriptive adjective.

### 7. Preserve the article’s identity as a research statement

Do not expand the literature section until the paper turns into a review. Literature should establish:

- the problem exists;
- the components have precedent;
- the proposed synthesis is not terminological invention;
- the paper is positioned against adjacent work.

The intellectual center should remain the proposed regime/framework plus quantitative illustration.

## Manuscript components known to have been prepared

A March 2026 finishing pass requested and produced work on:

- abstract;
- keywords;
- abbreviations;
- candidate citations of prior author work.

The exact final text is currently unavailable and should be imported from the LaTeX source rather than regenerated without need.

## Practical submission gate

The paper should not be treated as submission-ready again until:

1. the canonical Overleaf source is imported into `paper/`;
2. the compiled manuscript is compared against the March 2026 near-submission PDF;
3. the Li et al. positioning is visibly integrated;
4. the station/elevator/automatic-door material is checked for adequate quantitative support;
5. the bibliography is validated and unresolved keys such as `Çınar2020` are fixed;
6. the title/abstract/conclusion consistently communicate the same definition of asymmetry.
