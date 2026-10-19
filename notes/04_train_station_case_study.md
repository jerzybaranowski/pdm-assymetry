# Railway-station case study and optional quantitative extension

**Scope update, 2026-10-19:** the author confirms a conceptual paper with no empirical data and permits a high-level synthetic illustration if useful. The current task is a worked conceptual station decision, with a bounded optional illustration described in `07_publication_completion_plan.md`. The broader simulation proposal below is historical and is not a publication prerequisite.

## Current manuscript role

The revised source (`../paper/template.tex`) uses the station case as a **worked qualitative example**, with an assumption register and conditional inspection scenarios. It makes the structural-asymmetry argument concrete and shows where maintenance reasoning from indirect evidence is possible and where it must stop. No station measurements or simulation outcomes are claimed.

The case should preserve the contrast between:

- maintenance decision value at fleet/system level; and
- weak direct observability of individual devices.

## Candidate asset classes

The project discussions identify:

- escalators;
- elevators;
- automatic doors;
- HVAC / air-conditioning-related equipment;
- other repeated station electromechanical assets.

The related GPECOM paper focuses more technically on railway-station doors and elevators. Reuse/citation is appropriate where it supports the present conceptual argument, but the Symmetry paper must remain a distinct contribution.

## Evidence sources

A station contains data not collected as condition-monitoring signals but potentially informative about asset usage and burden:

- train timetables;
- platform assignments;
- ticketing and passenger-flow data;
- gate/entry counts;
- station occupancy estimates;
- device activation/event logs;
- controller alarms;
- building-management-system data;
- weather/ambient conditions;
- maintenance work orders;
- inspection records;
- replacement history;
- manufacturer recommendations.

These sources differ in spatial/temporal resolution and reliability. They should be represented as heterogeneous evidence, not concatenated as equivalent sensor channels.

## Canonical proxy example

For an escalator, actual passenger load may be unmeasured while ticketing, train schedules, platform assignments, occupancy estimates, and coarse counters are available.

A useful hierarchy is:

1. station context → latent local passenger flow;
2. local passenger flow → latent device usage/load;
3. usage/load + asset parameters → latent degradation pressure;
4. degradation pressure → maintenance risk/urgency;
5. posterior belief + intervention/failure costs → maintenance action.

The uncertainty in each arrow is part of the model.

## Digital representation / digital-twin direction

A station digital representation can organize:

- asset identity and topology/location;
- asset class/component metadata;
- operational context;
- observed events;
- maintenance history;
- probability distributions/belief states for usage and condition;
- predicted risk or priority;
- uncertainty and provenance of evidence;
- proposed inspection/maintenance action.

The important point is that the representation is **not assumed to provide complete observability**. Its role can be evidence integration and uncertainty-aware maintenance reasoning.

## Historical quantitative extension proposal

An earlier audit proposed the following simulation as a possible extension. It has not been implemented or approved as an experimental protocol. The current completion plan does not require this broader experiment.

### Asset population

Simulate a population of nominally similar devices with heterogeneous degradation sensitivities.

### Latent usage

Generate time-varying device usage from station traffic patterns (rush-hour, weekday/weekend, platform/zone differences).

### Proxy observation

Expose the maintenance model only to a noisy/coarse proxy of usage, not to the latent true usage.

### Degradation and interventions

Let degradation pressure depend probabilistically on usage and asset-specific parameters. Include inspection/preventive/corrective actions at a level sufficient to calculate decision consequences.

### Policies to compare

At minimum:

1. calendar/fixed-priority maintenance;
2. history-only probabilistic prioritisation;
3. proxy-informed LD-PdM;
4. idealized direct-condition-information upper bound.

### Outputs

Useful decision-level quantities include:

- maintenance/failure cost under declared assumptions;
- high-risk assets missed;
- premature interventions;
- ranking quality or top-k capture of truly stressed assets;
- value of proxy information;
- sensitivity to proxy quality;
- break-even value of an extra inspection/direct sensor.

The idealized direct-condition case should be presented as an **upper-information benchmark**, not as a free realistic alternative.

## Main caution

The current station case supplies a conceptual illustration, not quantitative evidence. Align claims with that role; label any optional synthetic results separately. The author confirms an invitation under the existing title, so publication-type deliberation should not delay the conceptual revision. See `../AUDIT.md`.
