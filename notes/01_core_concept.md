# Core concept: structural asymmetry in predictive maintenance

## 1. Problem statement

Conventional predictive-maintenance narratives often assume that maintenance-relevant condition data can be acquired directly if needed: add vibration, temperature, current, acoustic, pressure or other sensors; collect run-to-failure data; train a diagnostic/prognostic model; then optimize maintenance.

The project targets a different regime. For many real asset populations, **the need to reduce maintenance cost is substantial while direct condition information is structurally scarce**. The scarcity is not merely a temporary dataset defect. It can be the economically rational consequence of the asset class and deployment context.

This motivates the working concept of **LD-PdM: low-data / low-instrumentation predictive maintenance**.

## 2. Two economically different PdM regimes

### Critical or expensive installations

Examples include generators, chemical reactors and other unique or high-consequence installations. Dedicated condition monitoring is comparatively easy to justify because the value of avoiding unplanned downtime, secondary damage, safety consequences or a major production loss may dominate the cost of instrumentation.

In this regime, PdM is frequently justified primarily as a **risk-avoidance / availability mechanism**, not simply as a way to reduce routine maintenance expenditure.

### Mass-deployed, individually less critical assets

Examples discussed in the project include:

- automatic door openers;
- escalators;
- elevators;
- air-conditioning/HVAC equipment;
- vehicle fleets;
- tool fleets;
- other repeated electromechanical devices in public or industrial infrastructure.

These populations can create a large aggregate maintenance burden. They therefore have genuine cost-cutting potential. Yet a rich sensor package on every asset can be difficult to justify once installation, wiring, networking, commissioning, validation, integration, cybersecurity, data infrastructure and lifecycle maintenance are counted.

This is the central **asymmetry between maintenance need and data availability**.

## 3. Data scarcity is multi-layered

The paper should avoid reducing the problem to a single “small dataset” statement. The regime combines several distinct shortages:

- direct condition variables may not be measured at all;
- fault examples are rare relative to long healthy operation;
- run-to-failure trajectories are uncommon;
- maintenance records can be sparse, inconsistent or censored;
- operating load is often unobserved;
- contextual variables may exist only at a coarser spatial or temporal scale;
- asset populations are heterogeneous despite nominally identical hardware;
- interventions alter the subsequent degradation process, making histories non-exchangeable.

The resulting dataset may be large in raw row count while still carrying little information about the latent maintenance-relevant state.

## 4. Evidence sources in LD-PdM

When dedicated condition sensing is absent, the system should exploit evidence that already exists for other operational reasons:

- event logs and controller states;
- duty-cycle or activation counts;
- energy/current measurements already present in control electronics;
- ambient/weather data;
- timetables and operational schedules;
- passenger or traffic flows;
- ticketing data;
- building-management-system information;
- service/repair history;
- inspection records;
- manufacturer documentation;
- nominal lifetime information;
- known failure modes;
- fleet-level information shared across similar assets.

These are not perfect replacements for condition sensors. Their value lies in updating probabilistic beliefs about latent usage, degradation and failure risk.

## 5. Canonical proxy-data example

For an escalator at a railway station, the number of people actually transported may not be measured directly. Yet the station can possess passenger-flow information: tickets to/from the relevant platform, train schedules, platform assignments, station occupancy estimates or gate counts.

Such variables are **proxy evidence** for escalator load. They should not be treated as exact measurements. A probabilistic observation model can represent how uncertain passenger-flow data map to latent escalator usage and then to degradation/risk.

This example captures the intended epistemic structure of LD-PdM better than a conventional sensor-classification pipeline.

## 6. Why a probabilistic/Bayesian framing is natural

Indirect evidence introduces uncertainty at every inferential step:

1. contextual data only imperfectly represent actual usage;
2. actual usage only partially explains degradation;
3. degradation is latent and heterogeneous across assets;
4. maintenance actions depend on asymmetric costs of early intervention, delayed intervention and failure.

Bayesian modelling is therefore motivated by the problem structure because it can combine:

- prior engineering knowledge;
- fleet-level information;
- sparse service observations;
- proxy variables;
- censored or missing data;
- posterior predictive failure/degradation risk;
- explicit uncertainty used in maintenance decisions.

The paper should not present “Bayesian” as a stylistic preference. Its role is to represent the epistemic gap created by weak observation.

## 7. Main system-level case study

The planned application is a railway station containing multiple repeated asset classes. The station is useful because it naturally combines:

- many maintenance-relevant devices;
- uneven instrumentation;
- operational context already captured for non-maintenance reasons;
- strong temporal variation in usage;
- service histories;
- opportunities for fleet-level scheduling;
- an existing or plausible digital-twin representation of the station.

The maintenance layer can be integrated into a digital twin not by pretending that the twin contains perfectly observed condition states, but by storing **beliefs and uncertainty about asset condition** alongside geometry, topology, usage and service history.

## 8. Key distinction from conventional “small-data PHM”

The project must keep the following distinction explicit:

> **Small-data PHM asks how to perform learning when the desired condition/fault dataset is small. LD-PdM asks how to support maintenance when direct condition data may remain sparse or unavailable because obtaining them is not economically justified.**

The former naturally leads to data augmentation, transfer learning, few-shot learning and representation learning. The latter requires observation modelling, proxy evidence, prior knowledge, uncertainty propagation, value-of-information reasoning and maintenance decision analysis.

The two research areas overlap but are not equivalent.
