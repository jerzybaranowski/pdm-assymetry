# Core concept: structural asymmetry in predictive maintenance

## 1. Problem statement

Conventional predictive-maintenance narratives often assume that maintenance-relevant condition data can be acquired directly if needed: add vibration, temperature, current, acoustic, pressure, or other sensors; collect fault/degradation data; train a diagnostic/prognostic model; then optimize maintenance.

The project targets a different observation regime. For some asset populations, **maintenance decisions matter while direct condition information remains weak, indirect, or absent**. The limitation may arise from retrofit cost, legacy infrastructure, access constraints, scale, organizational conditions, or the low marginal value of instrumenting every asset.

The manuscript’s canonical term is **Limited-Data Predictive Maintenance (LD-PdM)**. “Limited observability” and “low instrumentation” describe the regime more precisely than sample count alone.

## 2. Two economically different PdM regimes

### Critical or expensive installations

Examples include generators, chemical reactors, and other unique or high-consequence installations. Dedicated condition monitoring can be comparatively easy to justify because the value of avoiding unplanned downtime, secondary damage, safety consequences, or major production loss may dominate instrumentation cost.

### Mass-deployed, individually less critical assets

Examples discussed in the project include:

- automatic door openers;
- escalators;
- elevators;
- air-conditioning/HVAC equipment;
- vehicle fleets;
- tool fleets;
- other repeated electromechanical devices in public or industrial infrastructure.

Such populations can create meaningful aggregate maintenance burden. Yet a rich sensor package on every asset may be unattractive once installation, wiring, networking, commissioning, validation, integration, cybersecurity, data infrastructure, and lifecycle maintenance are counted.

The central asymmetry is therefore between **maintenance decision value** and **economically/operationally available direct observability**.

## 3. Data limitation is multi-layered

The paper should not reduce the problem to a single “small dataset” statement. Relevant limitations include:

- direct condition variables may not be measured at all;
- fault examples are rare relative to healthy operation;
- run-to-failure trajectories are uncommon;
- maintenance records can be sparse, inconsistent, or censored;
- operating load is often unobserved;
- contextual variables may exist only at coarse spatial/temporal resolution;
- asset populations are heterogeneous despite nominally identical hardware;
- interventions truncate or alter degradation trajectories.

A dataset can therefore be large in raw row count while carrying little direct information about the latent maintenance-relevant state.

## 4. Evidence sources in LD-PdM

When dedicated condition sensing is absent or incomplete, useful evidence may already exist for other operational reasons:

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

These sources do not replace condition sensors equivalently. Their role is to update probabilistic beliefs about latent usage, degradation pressure, and risk.

## 5. Canonical proxy-data example

For an escalator at a railway station, actual passenger load may not be measured. The station may nevertheless possess tickets, train schedules, platform assignments, occupancy estimates, gate counts, or device event logs.

These variables are **proxy evidence** for usage. They must not be interpreted as exact load measurements. A probabilistic observation model should represent the uncertainty from station context to latent device usage and then from usage to degradation/risk.

## 6. Why a probabilistic/Bayesian framing is natural

Indirect evidence creates uncertainty at each inferential layer:

1. contextual data only imperfectly represent local usage;
2. usage only partially explains degradation;
3. degradation is latent and heterogeneous across assets;
4. maintenance decisions depend on asymmetric consequences of early intervention, delayed intervention, and failure.

Bayesian/probabilistic modelling is therefore structurally motivated because it can combine prior engineering knowledge, fleet-level information, sparse service observations, proxy variables, censored/missing data, and posterior predictive risk.

The paper should not present Bayesian modelling as novelty by itself. Its role is to make the epistemic gap created by weak direct observation explicit and auditable.

## 7. Main system-level case

The planned application is a railway station containing repeated asset classes and heterogeneous evidence sources. The station is attractive because it combines:

- many maintenance-relevant devices;
- uneven instrumentation;
- operational context collected for non-maintenance reasons;
- strong temporal variation in usage;
- service histories;
- fleet/system-level scheduling opportunities;
- a natural path toward integration with a digital representation of the station.

The current manuscript uses this as an **illustrative architecture**, not yet as a validated numerical simulation. The audit in `../AUDIT.md` recommends either adding a compact decision-level simulation or explicitly repositioning the manuscript as a concept/perspective paper.

## 8. Relationship to small-data PHM

The distinction must be stated carefully in light of Li et al. (2024).

Li et al. already recognize limited quantity/quality of monitoring data, heavy investment and ROI barriers, sensor deployment cost at scale, incomplete/imbalanced data, complex conditions, and uncertainty. Therefore LD-PdM must not be presented simply as “structural data scarcity whereas existing work is temporary small data.”

The more defensible distinction is:

> **Small-data PHM is primarily concerned with performing PHM tasks reliably when monitoring/status datasets are limited in quantity or quality. LD-PdM focuses on maintenance settings in which direct condition channels may themselves be persistently weak or absent, so indirect/contextual/historical evidence becomes a primary observation mechanism and the main target is maintenance decision support under partial observability.**

The areas overlap. The paper’s contribution depends on explaining the overlap honestly and then identifying the narrower observation/decision regime.

See `../literature/02_positioning_vs_li2024.md`.
