# Train-station case study and digital-twin direction

## Purpose of the case study

The station case is not intended to prove that one specific PdM algorithm is superior. Its role is to make the structural-asymmetry argument concrete and to demonstrate how a maintenance system can operate when direct condition sensing is incomplete or economically unjustified.

The case study should therefore preserve the contrast between:

- the **maintenance decision need** at fleet/system level; and
- the **limited observability** of individual devices.

## Candidate asset classes

The project discussions identify the following as particularly useful examples:

- escalators;
- elevators;
- automatic doors;
- HVAC / air-conditioning-related equipment;
- potentially other repeated station electromechanical assets.

The elevator and automatic-door examples from the related GPECOM paper were specifically proposed for reuse in the Symmetry manuscript where scientifically appropriate.

## Evidence sources

A station contains substantial data that are not collected as condition-monitoring data but may still be informative about asset usage and degradation:

- train timetables;
- platform assignments;
- ticketing and passenger-flow data;
- gate/entry counts where available;
- station occupancy estimates;
- device activation/event logs;
- controller alarms;
- building-management-system data;
- weather/ambient conditions;
- maintenance work orders;
- inspection records;
- component-replacement history;
- manufacturer lifetime/maintenance recommendations.

The important modelling principle is that these sources have different spatial/temporal resolution and different reliability. They should enter the model as heterogeneous evidence rather than being concatenated as if they were equivalent sensor channels.

## Canonical escalator example

Suppose direct passenger load on an escalator is not measured.

The station may nevertheless know:

- the number of tickets associated with a platform or destination;
- the trains arriving/departing from that platform;
- expected or measured passenger counts;
- the times during which the escalator was available;
- coarse usage/event counters.

These quantities can be used to define a distribution for latent escalator usage. A simple hierarchy is:

1. station context -> latent passenger flow near the escalator;
2. latent passenger flow -> latent escalator usage/load;
3. usage/load + asset parameters -> latent degradation;
4. degradation -> failure/maintenance risk;
5. posterior risk + maintenance costs -> action decision.

The key contribution is not any one mathematical choice for these arrows, but the recognition that the arrows are uncertain and must be represented as such.

## Digital-twin integration

A station digital twin can provide the organizing layer for this information. In the proposed conception, the twin should not be treated as an omniscient high-fidelity sensor replica.

Instead, each asset can carry:

- identity and topology/location;
- asset class and component metadata;
- operating context;
- observed events;
- maintenance history;
- probability distributions / belief states for usage and condition;
- predicted risk over a chosen horizon;
- uncertainty and provenance of evidence;
- proposed inspection or maintenance action.

This turns the digital twin into an integration environment for weak and heterogeneous maintenance evidence.

## Simulation direction

The paper was intended to rely mainly on desktop research, simulations and clear visuals rather than a new full-scale industrial experiment. A useful simulation design consistent with the project concept is:

### Asset population

Simulate a fleet of nominally similar station assets with heterogeneous latent degradation rates.

### Latent usage

Generate time-varying usage from station traffic, including rush-hour, weekday/weekend and platform-specific patterns.

### Proxy observation

Generate a noisy/coarse proxy of usage from passenger/ticket-flow information rather than revealing the true usage directly.

### Degradation and interventions

Let degradation depend probabilistically on usage and asset-specific parameters. Include inspections, corrective maintenance and preventive interventions.

### Policies to compare

At minimum, conceptually compare:

- fixed calendar maintenance;
- history-only probabilistic maintenance;
- proxy-informed LD-PdM;
- an idealized directly observed condition-monitoring benchmark.

The idealized benchmark should be presented as an upper-information reference, not as a realistic free alternative.

### Evaluation quantities

Potential outputs include:

- total maintenance cost;
- unplanned failures/downtime;
- premature interventions;
- calibration of predicted risk;
- value of proxy information;
- sensitivity to proxy quality;
- break-even value of adding a direct sensor/inspection.

These simulations would directly support the paper’s thesis by showing how decision quality changes as information availability changes.

## Main caution

The case study becomes weak if it is only a list of plausible data sources. It should contain at least one explicit probabilistic model or simulation that demonstrates the asymmetry quantitatively. Otherwise reviewers may read the paper as a position essay rather than a research contribution.
