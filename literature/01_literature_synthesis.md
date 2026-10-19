# Literature synthesis recovered from the project

This note captures the durable result of the project’s literature-review work. It is not a complete bibliography export because the canonical `.bib` file is not currently available.

## 1. Main synthesis result

The most important literature-search result was that an apparently heterogeneous group of papers forms a coherent methodological cluster.

Across examples involving bridges, engines, HVAC systems, compressors, photovoltaics, elevators, wastewater systems, rail infrastructure and other assets, the same epistemic pattern repeatedly appears:

> A maintenance- or operation-relevant state cannot be observed directly and is instead inferred from proxy signals, indirect measurements, contextual variables, or historical information under constraints of cost, accessibility, scale, or legacy infrastructure.

This observation materially strengthened the intellectual basis of LD-PdM.

## 2. Why this literature matters

The literature is useful precisely because much of it does **not** call itself predictive maintenance.

Relevant work may instead appear under labels such as:

- virtual sensing / soft sensing;
- indirect condition estimation;
- load estimation;
- usage estimation;
- anomaly detection;
- reliability modelling;
- remaining-life estimation;
- structural health monitoring;
- building/transport operations;
- maintenance optimization;
- digital twins;
- fleet analytics.

The paper can therefore argue that LD-PdM is not based on an absence of prior methods. Its value is to **connect and reinterpret these dispersed methods as components of a common maintenance regime**.

## 3. Second synthesis result: probabilistic treatment is often missing

A further observation from the review was that many proxy-based studies produce a point estimate of an inaccessible variable but do not carry uncertainty through to the maintenance decision.

For LD-PdM, this gap is central. If the evidence is indirect, the maintenance system should represent uncertainty in:

- the proxy-to-usage relationship;
- usage-to-degradation relationship;
- latent degradation state;
- future load;
- failure risk;
- intervention consequence/cost.

This supports the Bayesian framing of the paper.

## 4. Literature strands that should remain distinct

### A. General PdM/PHM and maintenance decision making

Purpose: establish PdM as a decision problem, not only a diagnostic-model problem.

### B. Data scarcity, rare faults and class imbalance

Purpose: establish that failure evidence is structurally sparse and healthy operation dominates most industrial datasets.

### C. Small-data PHM

Purpose: acknowledge an established field dealing with limited fault/condition datasets and methods such as transfer learning, few-shot learning and data augmentation.

This strand overlaps with LD-PdM but does not define it.

### D. Sensor economics / deployment barriers

Purpose: support the claim that the real cost of condition monitoring includes installation and system integration, not only sensor hardware.

This literature is essential because the paper’s central asymmetry is partly economic. Unsupported statements about sensor cost would leave the conceptual contribution vulnerable.

### E. Indirect sensing and proxy variables

Purpose: show that meaningful latent operational states can be inferred from non-condition-monitoring data.

This is the most important empirical support for the LD-PdM direction.

### F. Maintenance records, documentation and expert knowledge

Purpose: support the use of sparse service histories and prior engineering knowledge when direct data are weak.

### G. Bayesian/probabilistic prognostics and maintenance

Purpose: provide established machinery for latent-state inference, hierarchical fleet models, uncertainty propagation and decision making.

### H. Digital twins and system-level data integration

Purpose: motivate the train-station digital twin as an organizing layer for heterogeneous evidence rather than as a claim that every asset is richly instrumented.

## 5. Key conceptual warning from the literature review

The paper must not equate the following:

- **small sample size**;
- **class imbalance**;
- **missing data**;
- **weak observability**;
- **absence of dedicated sensors**;
- **indirect proxy observation**.

They can coexist but they are different problems requiring different treatments.

A central contribution of the paper should be to organize these issues under the broader structural relationship between decision need and information availability while retaining their distinctions.

## 6. Bibliographic items explicitly recoverable from project context

### Li et al. (2024)

Chuanjiang Li, Shaobo Li, Yixiong Feng, Konstantinos Gryllias, Fengshou Gu, and Michael Pecht, “Small data challenges for intelligent prognostics and health management: a review,” *Artificial Intelligence Review*, vol. 57, no. 8, article 214, 2024. DOI: 10.1007/s10462-024-10820-4.

This paper requires explicit positioning; see `02_positioning_vs_li2024.md`.

### Bauer and Baranowski (2025)

Waldemar Bauer and Jerzy Baranowski, “A Comparison of Deep Recurrent Neural Networks and Bayesian Neural Networks for Detecting Electric Motor Damage Through Sound Signal Analysis,” *Energies*, vol. 18, no. 18, 2025. DOI: 10.3390/en18184997.

This was supplied during the manuscript-finishing discussion as a possible self-citation. It should only be retained if it supports a concrete point in the final text, not merely to increase self-citation.

### `Çınar2020`

A previous outline contained or discussed a key rendered as `Çınar2020`, and its identity was explicitly questioned. Treat this key as **unverified** until the canonical bibliography is imported.

## 7. What remains to recover

The earlier literature-search workflow contained more individual papers and BibTeX keys than are available in the retained context. Once the Overleaf source is imported, recover the complete `.bib` first and use it to rebuild a source-by-source literature map rather than trying to recreate missing citations from memory.
