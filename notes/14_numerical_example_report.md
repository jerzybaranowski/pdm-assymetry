# Approved numerical example: implementation and verification

**Date:** 2026-10-23  
**Status:** approved calculation implemented, integrated into the manuscript, and verified; review PDF has 18 pages.

**Subsequent editorial pass:** [the 2026-10-25 report](15_editorial_consistency_report.md) documents later wording and caption corrections and the current PDF hash. The calculation, inputs, and numerical results recorded here are unchanged. The PDF hash below describes the 2026-10-23 artifact, not the file currently at the review-output path.

The author explicitly approved [Section 8 of the model specification](12_two_door_model_specification.md#8-optional-numerical-inputs-proposed-for-author-review) and its calculation, replying “I approve the specification and calculations” (translated from Polish). This continuation follows the [symbolic revision](13_round0_revision_report.md) and the numerical paragraph outline appended to [the revision outline](11_round0_revision_outline.md). The invited title, LD-PdM name, conceptual scope, and hypothetical station setting are preserved.

## Implementation and provenance

The [calculation directory](../simulations/two_door/README.md) contains the standard-library Python implementation, exact input file, generated JSON results, and regeneration instructions. All numerical inputs are strings converted directly to rational numbers with `fractions.Fraction`. There is no random sampling, fitted model, empirical dataset, or seed. The approved inputs were not tuned after inspecting the results.

The two routing interpretations give exposures $(x_A,x_B)=(1,0.5)$ and $(0.35,0.5)$. Both use $q_i=0.1+\beta x_i$, $\beta\in[0,0.5]$, $d_B=0.9$, $d_A\in[0.25,0.9]$, net response value 10, and inspection burden 1. Losses share an arbitrary scale. The finding event, absence of false positives, at most one optional early inspection, and separately feasible contingent service response are the approved assumptions. A corrected historical interpretation diverts traffic away from A to a third passage; it does not transfer that traffic to B or erase exposure through later rerouting.

The gain $G_i=q_i d_i v_i-k_i$ is measured relative to the same existing admissible schedule. It concerns detection and response to an actionable condition, not physical failure. Each routing interpretation is evaluated separately. When both remain plausible, the calculation checks strict preference across both without assigning model probabilities.

Generated artifacts are [exact JSON results](../simulations/two_door/results.json) and [the LaTeX table](../paper/generated/two_door_results.tex). Terminating values are displayed as exact decimals and other values as fractions, without rounding. Rectangle extrema follow from corner values of bilinear gains and differences; a sampled grid is not used as evidence of continuous robustness.

## Numerical findings

The manuscript table contains six cases covering an uninformative exposure link, equal and unequal detection, a door-choice tie, a baseline tie, and the upper exposure-coefficient endpoint. Three representative comparisons at $\beta=0.2$ are:

| $d_A$ | $G_A(m_1)$ | $G_A(m_2)$ | $G_B$ under either route | Strict common-preference outcome |
|---|---:|---:|---:|---|
| 0.9 | 1.7 | 0.53 | 0.8 | Fallback: modelwise optima differ |
| 0.4 | 0.2 | -0.32 | 0.8 | Inspect B |
| 0.6 | 0.8 | 0.02 | 0.8 | Fallback: A and B tie under $m_1$ |

These results expose a limitation of the stipulated strict rule. In the first row, both early policies improve on the baseline under both routing interpretations, but neither strictly beats the other throughout the set. The rule therefore retains the schedule despite B guaranteeing a gain of 0.8. In the third row B weakly dominates A, but their tie under $m_1$ again prevents a strict common preference. Fallback does not establish that no beneficial action exists or that retaining the schedule is robust-optimal.

For a fixed coefficient and sensitivity, strict preference for B across both routes holds exactly when

$$
\beta>\frac{1}{45},\qquad
d_A<c(\beta)=\frac{0.9(1+5\beta)}{1+10\beta}.
$$

There is no strict common preference for A within the approved rectangle. The existing schedule weakly dominates both early policies throughout the routing set exactly when $\beta\leq1/45$ and $d_A\leq1/(1+10\beta)$. Equality boundaries and the distinction between baseline dominance and stipulated fallback are retained in the output.

If the corrected interpretation $m_2$ is established as the sole remaining model, B is preferred for $\beta>1/45$ throughout the stated sensitivity range. This differs from retaining both interpretations as plausible. If the entire parameter rectangle and both routes remain plausible, A's gain spans $[-0.75,4.4]$ and B's spans $[-0.1,2.15]$; no early policy has a uniform strict preference over that larger set. These are conditional hypothetical results, not station-performance estimates.

## Manuscript integration

Section 5.4, `sec:numerical`, states all inputs, introduces the numerical gains and threshold in Equation 6, and interprets the generated Table 4. The table replaces the preceding symbolic scenario table, leaving five tables in total. The abstract, contribution statement, scope, conclusions, future-evaluation paragraph, and data-availability statement now reflect the actual calculation. They state the fallback's opportunity cost and separate exact hypothetical enumeration from later empirical or stochastic evaluation.

The two existing conceptual diagrams remain unchanged. No numerical plot is required to establish the analytical regions or exact tabulated results. No new bibliographic record or companion-paper result was added in this continuation. The [response matrix](../reviews/round0/response_matrix.md) records which numerical requests are now addressed and which broader requests remain partial.

## Verification

- The full existing suite passed: **10 tests and 58 subtests**, comprising three existing diagram-pipeline tests and seven numerical tests. All **10** test-catalog entries validate. Tests cover independent outcome-loss accounting, the baseline, reversals, ties, distinct uncertainty sets, continuous bounds, invalid inputs, and byte-for-byte regeneration of both artifacts.
- The tests and catalog check used the already available `/opt/anaconda3/bin/python`. The calculation and its seven tests also run with the system interpreter using only the standard library. No package, interpreter, dependency declaration, or installed environment was changed.
- Independent rational recomputation matched all 12 case/model rows, policy optima, 18 per-model rectangle extrema, and 30 numerical table cells. The continuous boundaries and manuscript interpretation were independently checked.
- Compiled in `build/numerical/` with the existing `latexmk` command. No unresolved citations/references, duplicate labels, missing characters, overfull boxes, or underfull boxes remain. The known non-fatal bundled-class `xcolor` warning persists.
- Rendered all **18 pages** with native PDFKit because Poppler is unavailable. Pages 1–9 were independently inspected and pages 10–18 inspected by the primary editor. Final layout has no clipping, overlap, or isolated one-letter line in the numerical discussion. Tables, equations, diagrams, references, and abbreviations are legible. The deferred AI declaration remains red.
- Recursive source verification includes both diagrams and the generated table: **32 unique bibliography records, 23 cited and rendered references, 23 unique labels, 5 tables, 2 figures, and 6 numbered equations**, with no missing keys or references.
- Review PDF: [`output/pdf/ld-pdm-conceptual-revision.pdf`](../output/pdf/ld-pdm-conceptual-revision.pdf). SHA-256: `54c2bf2fc4eb79867b5d551cc3c304cca749545dff76a55db618cde66779c9b2`.

Validation commands, from the repository root:

```sh
python3 simulations/two_door/calculate.py
/opt/anaconda3/bin/python -m pytest tests -q
/opt/anaconda3/bin/python tools/testing/validate_test_catalog.py
```

Build command, from `paper/`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=../build/numerical template.tex
```

These checks establish the stated calculation and document checks; they are not a full-project reproducibility audit.

## Remaining author review

The revised scientific argument and numerical interpretation are ready for author review. Counting-exercise information value, a full generative or physical-failure model, empirical validation, and a broader multi-asset allocation example were not part of this numerical specification. The diagram arrow-convention request remains unimplemented. The previously deferred AI declaration, affiliation presentation, and submission-history declarations remain author items; funding scope is unchanged. No submission, upload, external message, commit, or push was performed.
