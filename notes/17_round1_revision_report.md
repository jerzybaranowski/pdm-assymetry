# Round 1 implementation and verification

**Date:** 2026-10-26  
**Checkpoint:** `0f7a169` — the manuscript, approved calculation, reviews, and assessment before this revision.  
**Authorization:** The author requested committing the existing state and implementing the corrections after reviewing the [Round 1 proposal](16_round1_revision_assessment.md). The [specification addendum](12_two_door_model_specification.md#9-decision-rule-revision-authorized-on-2026-10-26) records the revised objective and unchanged numerical inputs.

## Implemented scientific changes

The manuscript now removes dominated policies before applying a declared selection objective. Minimax regret is the main illustration, with maximin incremental gain as the comparator. Both operate on the three original deterministic complete policies. Ties remain explicit. A selected policy may have negative gain under one retained model; the text and the existing `beta=1/45, d_A=0.9` row demonstrate this tradeoff. No robust nonnegative-gain constraint, model probabilities, new input values, or observation model were added.

The calculation exports dominance witnesses, worst gains, worst regrets, tie sets, and negative-gain diagnostics. The earlier strict-common-preference rule is retained only as an identified historical diagnostic with its original tests. It is no longer the manuscript selector. The six numerical rows, exact continuous boundaries, and whole-rectangle stress comparison agree with the independent mathematical review.

The distinction between uncertainty sets is explicit. At fixed `beta=0.2, d_A=0.9`, minimax regret selects A and maximin gain selects B. Over the entire declared rectangle and both routes, minimax regret selects B (maximum regret 2.25), whereas maximin gain selects the schedule. The rectangle remains an illustrative sensitivity domain, not an elicited distribution or operational frequency.

The manuscript also implements:

- A completed five-step decision record, including conditional classification, stipulated inputs, retained models, dominance, criterion, action, and reconsideration triggers.
- More specific checklist evidence requirements and yes/no/unresolved examples, while distinguishing uncertain condition from uncertain action.
- An explicit feasible-information set and distinction between access constraints and an untested economic judgment.
- Separation of evidence that excludes a routing interpretation from evidence that leaves both plausible.
- Conditional semantics of `q d v`, with no unnecessary independence assumption, and a clearer actionable-condition definition.
- A narrowed shared-error claim and its decision-level qualification; the shared-error symbol no longer collides with door B.
- Direct positioning against Tiddens' PdM suitability assessment, Troffaes' dominance/decision-criteria discussion, Arcieri's model-uncertain maintenance planning, and Cooke–Bedford's treatment of maintenance-dependent histories.
- A more visible companion-paper boundary and explicit limits on prognostic implementation, learned inference, population optimization, and demonstrated usability.
- Revised Abstract, keywords, conclusions, and cover-letter draft; one overlapping conceptual diagram removed from the article while its source remains in the repository.

The invited title and LD-PdM term are unchanged. Empirical validation, a full Bayesian observation chain, noisy-count information value, and population simulation remain outside this bounded implementation. The [response matrix](../reviews/round1/response_matrix.md) distinguishes implemented, partial, declined, and deferred requests rather than treating every review item as closed.

## Figure and supplement

The new `two-door-decisions` figure consumes only calculator-exported geometry from `simulations/two_door/plot_data.json`. Its two panels compare the criteria over the same parameter ranges. The renderer contains no policy calculation. Exact boundaries are specified in the manuscript; the small low-beta region is included but visually narrow at full-domain scale.

Approved render: `paper/figures/two_door_decisions.pdf` and `.png`. On 2026-10-26 the author explicitly approved this exact two-panel figure, its 138.6 × 85 mm dimensions, vector PDF, and 300 dpi PNG. Target-size and grayscale inspection found readable labels and no clipping. The PDF has embedded fonts and vector content. The approval closes the earlier custom-dimension and concrete-render approval requests; it does not authorize a figure package, upload, or submission. Configuration and the validation record preserve the approval status.

The bundled PDF figure inspector requires unavailable `pypdf`. Installed PyMuPDF and Pillow were used for size, embedded-font, vector/raster, PNG-resolution, and rendering checks; no package was installed. This fallback is recorded explicitly and must not be reported as execution of the unavailable inspector. Explicit custom-dimension and render approval is recorded; the updated configuration passed schema and project-state validation with zero blockers and zero warnings. The figure's implementation status is `technically-validated`; no figure package or final designation was added.

Supplement S1 is `output/supplement/two-door-calculation.zip`. Its six-file allowlist contains the calculation, inputs, exact JSON results, drawing geometry, generated LaTeX table, and regeneration instructions. The archive was extracted into a temporary directory and executed using only the standard library; all three regenerated outputs matched the supplied files byte-for-byte. This verifies the included calculation, not the entire project or an external deposit. No upload, public release, or submission occurred.

## Verification

- Before the figure approval-metadata correction, the full suite passed **18 tests and 69 subtests**, and all **16 test-catalog entries** validated. After the author's explicit approval was recorded on 2026-10-26, the full suite passed again with **18 tests and 69 subtests**, and all **16 catalog entries** validated. The five existing non-fatal PyMuPDF SWIG deprecation warnings remain.
- The approved figure configuration passed schema and project-state validation with **zero blockers and zero warnings**. The approved PDF/PNG, analytical source and renderer hashes are unchanged; the manuscript PDF and supplement also remain unchanged. Approval and verification did not alter scientific content.
- Numerical input file unchanged relative to checkpoint `0f7a169`.
- LaTeX build: **18 pages**, no unresolved citations/references, missing characters, or overfull/underfull boxes. The existing non-fatal `xcolor` option warning remains.
- Current bibliography: **36 entries, 26 cited**. All four additions are used; existing keys were preserved.
- Article structure: **six tables, two figures, seven numbered equations**.
- Independent review checked the mathematics, source attribution, scope, and rendered table/figure consistency. A sensitivity-versus-exposure wording error and a probability factor split across pages were repaired.
- All 18 rendered pages were visually inspected, including a second check of pages 10–13 after those repairs. The six tables, two figures, back matter, and four new bibliography entries render without clipping or overlap.

The current build is `build/round1/template.pdf`, SHA-256 `713d6d1ce1dc49feb1c21726e5f513d5dcc38fae5964e2ec824b0d6f476be3c5`. The identical review copy is saved at `output/pdf/ld-pdm-conceptual-revision.pdf`.

## Remaining author matters

The AI declaration remains red and deferred as previously instructed. Affiliation presentation, grant-identifier verification, and originality/submission-history declarations require confirmed author records. The current two-door figure render, dimensions, and formats are approved; no figure package has been created or finalized. The revision demonstrates conditional decision reasoning and does not establish field usability or resolve journal fit by itself.

Only the initial checkpoint was committed in this task. Subsequent revision files remain an uncommitted author-review draft in the working tree. No push, external upload, or submission was performed.
