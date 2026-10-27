# Exact two-door inspection example

This deterministic calculation implements the hypothetical protocol in
[`notes/12_two_door_model_specification.md`, Section 8](../../notes/12_two_door_model_specification.md#8-optional-numerical-inputs-proposed-for-author-review),
which the author approved for calculation on 2026-10-23. The earlier proposal
records the assumptions; [`parameters.json`](parameters.json) is the single
authoritative numerical input file for computation. No inputs are station
estimates, physical-failure rates, or empirical inspection-performance results.
The author authorized the decision-rule revision described in
[`notes/16_round1_revision_assessment.md`](../../notes/16_round1_revision_assessment.md)
on 2026-10-26. It changes policy selection while preserving those numerical
inputs: dominance filtering followed by minimax regret is the main rule, with
maximin incremental gain as a conservative comparator.

Run commands from the repository root:

```sh
python3 simulations/two_door/calculate.py
python3 -m unittest discover -s tests -p test_two_door.py -v
```

The calculation and its tests use only the Python standard library.
For the existing repository-wide test suite and catalog validator, the already
available project interpreter supplies the existing test dependencies:

```sh
/opt/anaconda3/bin/python -m pytest tests -q
/opt/anaconda3/bin/python tools/testing/validate_test_catalog.py
```

These commands do not install or change packages. The default system interpreter
can run the calculation and its tests but may lack the packages needed by the
repository's catalog validator or other tests.

## Inputs and generated artifacts

All numerical inputs are strings converted directly to `fractions.Fraction`.
The model uses an affine probability of an actionable condition, a probability
of detecting that condition, a net value of the contingent service response,
and an unconditional inspection burden. False positives are assumed absent.
The response value excludes inspection burden and already includes conditional
service effort. All losses share an arbitrary scale over the common planning
window; no duration or currency value is inferred.

Regeneration replaces three generated files:

- [`results.json`](results.json): exact rational values, original inputs,
  representative comparisons, continuous-boundary coefficients, and rectangle
  extrema with their corner evaluations.
- [`plot_data.json`](plot_data.json): the approved domain, analytical selector
  coefficients, and exact rational drawing coordinates for both criteria.
  Closed region polygons, sampled equality curves, straight tie segments,
  triple-tie points, and label anchors are supplied to the figure renderer.
  The renderer only converts these coordinates for drawing; it does not
  calculate a decision or infer a boundary.
- [`paper/generated/two_door_results.tex`](../../paper/generated/two_door_results.tex):
  the manuscript table. Terminating rational values appear as exact decimals;
  other values remain fractions. No rounding is used.

No artifact contains timestamps or machine-specific paths. There is no
random sampling, so no random seed is needed. The export test regenerates all three
files and checks their bytes against the versioned artifacts. The calculation
also accepts `--config`, `--json-output`, `--tex-output`, and `--plot-output`
paths. The polygon curves contain 201 rational points per branch; interpolation
is solely a rendering approximation, not the basis for a policy choice.

## Reading the comparison

At a **fixed** exposure coefficient and detection sensitivity, the routing set
contains the two alternative interpretations of historical exposure. They are
evaluated separately, without assigning probabilities to the interpretations.
The `model_set` field first removes pointwise-dominated policies: another
policy must have at least as much gain in every model and strictly more in at
least one. Equivalent gain vectors remain distinct policies. It then reports
all optimizers of each criterion among the remaining deterministic policies:

- **Minimax regret:** minimize `max_m(max_j G_j(m) - G_i(m))`. The reference
  best policy in each model ranges over all three feasible policies.
- **Maximin incremental gain:** maximize `min_m G_i(m)`.

The baseline has zero gain in each model. No probabilities over routing models,
randomized policy mixtures, or robust nonnegative-gain gate are imposed. In
particular, minimax regret can select an inspection that is worse than the
baseline under one retained model: at `beta=1/45, d_A=0.9`, policy A is selected
with gains `0.1` and `-0.03`. `policy_metrics.negative_gain_states` lists the
zero-based positions of evaluations with negative gain. Ties are returned as
policy lists, never silently resolved to baseline. The scalar `choice` is the
unique minimax-regret policy or the string `tie`.

Maximin incremental gain is not minimax absolute loss. Model-dependent baseline
losses cancel within each regret comparison and dominance comparison, but do
not generally cancel across models in a worst-absolute-loss calculation.
Such baseline losses are not specified here. At fixed parameters, the approved
example's maximin-gain choice is B for `beta > 1/45`, baseline below that value,
and both at equality, independently of A's sensitivity. The minimax-regret
choice also depends on sensitivity, as the exported exact boundaries show.

The `full_rectangle` field asks the stronger question in which the entire
approved coefficient/sensitivity rectangle and both routing interpretations
remain plausible. These are different uncertainty sets. Each gain and gain
difference is bilinear in the two parameters; its values within the rectangle
are convex combinations of the corner values. The reported corner extrema
therefore certify the continuous bounds, rather than approximating them with
a grid. Worst regret is a maximum of pairwise gain differences, so its full
rectangle maximum also follows from these corner evaluations. For this larger
uncertainty set, minimax regret selects B (worst regret `9/4`) and maximin gain
selects baseline (worst gain zero). These are not the pointwise choices shown
in the figure. `boundary_values()` evaluates model-specific equality thresholds;
`selector_boundaries()` gives the revised two-model selector curves.

The superseded common-strict-preference rule survives only in the explicitly
named `historical_strict_rule` fields and `historical_strict_decision()` API.
Its `fallback` retains the existing schedule and can forgo guaranteed positive
gain, even choosing a dominated baseline. It is neither the main rule nor an
optimality claim. The original regression assertions remain as historical
diagnostics; the revised table reports both current criteria instead.

Mandatory requirements and feasibility of the contingent service response
remain assumptions. Pointwise admissibility and maximin expected utility are
established decision concepts; see Troffaes (2007), Sections 1 and 3.1,
[doi:10.1016/j.ijar.2006.06.001](https://doi.org/10.1016/j.ijar.2006.06.001).
The project-specific regret formulas and boundary derivation are recorded in
the Round 1 assessment linked above. The calculation does not claim a new
decision criterion or empirical validation of either rule.
