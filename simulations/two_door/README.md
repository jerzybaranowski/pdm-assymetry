# Exact two-door inspection example

This deterministic calculation implements the hypothetical protocol in
[`notes/12_two_door_model_specification.md`, Section 8](../../notes/12_two_door_model_specification.md#8-optional-numerical-inputs-proposed-for-author-review),
which the author approved for calculation on 2026-10-23. The earlier proposal
records the assumptions; [`parameters.json`](parameters.json) is the single
authoritative numerical input file for computation. No inputs are station
estimates, physical-failure rates, or empirical inspection-performance results.

Run commands from the repository root:

```sh
python3 simulations/two_door/calculate.py
python3 -m unittest discover -s tests -p test_two_door.py -v
```

The calculation and its seven tests use only the Python standard library.
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

Regeneration replaces two generated files:

- [`results.json`](results.json): exact rational values, original inputs,
  representative comparisons, continuous-boundary coefficients, and rectangle
  extrema with their corner evaluations.
- [`paper/generated/two_door_results.tex`](../../paper/generated/two_door_results.tex):
  the manuscript table. Terminating rational values appear as exact decimals;
  other values remain fractions. No rounding is used.

Neither artifact contains timestamps or machine-specific paths. There is no
random sampling, so no random seed is needed. The export test regenerates both
files and checks their bytes against the versioned artifacts. The calculation
also accepts `--config`, `--json-output`, and `--tex-output` paths.

## Reading the comparison

At a **fixed** exposure coefficient and detection sensitivity, the routing set
contains the two alternative interpretations of historical exposure. They are
evaluated separately, without assigning probabilities to the interpretations.
The `model_set` field asks whether one early-inspection policy strictly improves
on both the other door and the existing schedule under both interpretations.

The `full_rectangle` field asks the stronger question in which the entire
approved coefficient/sensitivity rectangle and both routing interpretations
remain plausible. These are different uncertainty sets. Each gain and gain
difference is bilinear in the two parameters; its values within the rectangle
are convex combinations of the corner values. The reported corner extrema
therefore certify the continuous bounds, rather than approximating them with
a grid. `boundary_values()` also evaluates the exact equality thresholds at
any rational coefficient within the approved range.

`baseline` means the existing schedule weakly dominates the two early policies
throughout the set. `fallback` means the stipulated strict-preference rule
does not support a common early policy and retains the admissible schedule.
**Fallback is not an optimality claim.** It can forgo a positive gain that an
early policy guarantees throughout the routing set. The fields
`common_improving_policies` and `baseline_dominated_by` expose that situation;
a dagger marks fallback in the manuscript table. Mandatory requirements and
feasibility of the contingent service response remain assumptions of the
comparison.
