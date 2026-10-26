# Round 0 revision outline

**Date:** 2026-10-23  
**Status:** implemented outline for the authorized manuscript revision and its subsequently approved numerical continuation. Completion is recorded in the [numerical report](14_numerical_example_report.md), [response matrix](../reviews/round0/response_matrix.md), and [AUDIT.md](../AUDIT.md). The initial symbolic outline below is preserved; the numerical continuation at the end supersedes its statements that numerical inputs remain unapproved.  
**Basis:** [revision plan](10_round0_revision_plan.md), the four [simulated reviews](../reviews/round0/README.md), and the current [manuscript](../paper/template.tex).

The present pass retains the invited title, LD-PdM terminology, conceptual contribution, and hypothetical station setting. It develops a symbolic decision comparison without supplying unapproved numerical probabilities, costs, effect sizes, sensitivity ranges, or station observations. A numerical experiment remains a separate proposed extension; this pass must not be described as satisfying requests for numerical validation. Existing analytical results, published companion results, and hypothetical assumptions remain distinguishable.

Each bullet below describes one intended paragraph or one separately identified table/figure. Paragraph identifiers are editing aids, not proposed manuscript headings. Adjacent paragraphs may be combined only if their messages remain clear. The abstract, Introduction, and Conclusions should be finalized after the procedure and example.

## Abstract

- **A1 — Paragraph:** State the maintenance problem, identify the applicability checklist and five-step procedure, and report the symbolic example's actual result: a passenger/exposure ordering and an inspection choice agree only under stated conditions; different consequences, inspection effectiveness, or routing interpretations can reverse or leave the choice unresolved. Describe the example as hypothetical and symbolic, and reserve predictive calibration and operational benefit for later evaluation.

## 1. Introduction

- **I1 — Paragraph:** Introduce the need to select maintenance actions when consequential asset functions have limited condition information; distinguish the maintenance choice from the size of a training dataset through one concrete station-device example.
- **I2 — Paragraph:** Position the problem within the broad small-data PHM scope documented by Li et al.; acknowledge persistent acquisition constraints, heterogeneous records, physical knowledge, uncertainty, fleet information, and maintenance decisions without claiming these ingredients as new.
- **I3 — Paragraph:** Define LD-PdM as a decision-relative information regime and explain the title's mismatch: operational consequences can require a maintenance choice even when feasible channels leave the relevant condition uncertain. Identify what is being compared without asserting a new mathematical symmetry theory.
- **I4 — Paragraph:** Introduce usage/load-based maintenance, soft sensing, and Bayesian inspection planning as existing methods that can be used once their evidence and action assumptions are justified; state the role of the proposed checklist and procedure in examining those assumptions.
- **I5 — Paragraph:** Map the contribution to concrete outputs: an applicability checklist in the regime section, a five-step procedure in the decisions section, and a symbolic two-door comparison with an explicit fallback in the station section. State what an analyst can record or decide using each output.
- **I6 — Paragraph:** Give the section roadmap using those outputs rather than repeating the abstract's contribution claim.

## 2. The LD-PdM regime and its asymmetries

- **R1 — Paragraph:** Define the unit of assessment as a specified asset function or population, decision, planning horizon, and feasible information set; explain that one asset can satisfy the criteria for one choice and fail them for another.
- **R2 — Table:** Present each applicability criterion as a question with required evidence or justification and a yes/no/unresolved outcome. Address consequential differences between feasible actions, relevant uncertainty remaining after feasible condition-sensitive channels, persistence over the horizon, and the contribution of indirect evidence to the choice or its justification.
- **R3 — Paragraph:** Explain how to read the checklist: all defining conditions need support, a negative answer excludes the stated case, and an unresolved answer identifies missing justification. A case can belong to the regime while its available evidence supports no differentiated action. Information content, acquisition cost, and value of information are separate assessments.
- **R4 — Paragraph:** Apply the checklist qualitatively to the hypothetical door-inspection decision using declared assumptions, then contrast it with a few-sample case in which a condition channel resolves the quantity needed for the same decision. Do not introduce empirical claims about doors, elevators, or escalators.
- **R5 — Paragraph:** Explain the logical roles of the four asymmetries before their detailed treatment: condition information and acquisition constraints define the mismatch; sparse/selective failure observations complicate learning; population scale supplies allocation opportunities and shared dependencies. The latter two are not mandatory membership tests.
- **R6 — Paragraph:** Explain condition observability through the difference between passenger/usage records and the particular condition quantity required for an action; use a representative checked indirect-sensing source only for the relationship it actually supports.
- **R7 — Paragraph:** Distinguish right censoring, interval censoring, selective inspection, missing records, and condition change after service; explain why a station application must specify its observation and maintenance process. Avoid prescribing an unverified typical repair model for the example assets.
- **R8 — Paragraph:** Describe acquisition constraints and lifecycle effort conditional on the chosen function and horizon; explain that unit price does not establish consequence or the economic case for monitoring.
- **R9 — Paragraph:** Explain partial pooling across suitably related assets, the relevance of between-unit variation, and the difference between estimating a population quantity and ordering individual inspections; make no claim that a large population removes shared proxy error.
- **R10 — Figure decision:** Retain a conceptual diagram only if it performs a job not already done by the station evidence diagram and checklist. A removal or merge should reduce duplication; any changed TikZ content follows the diagram workflow.

## 3. Evidence and inference

- **E1 — Paragraph:** Define evidence, usage, accumulated exposure, physical condition, event probability, consequence, and action priority through their distinct engineering roles; establish separate usage and exposure notation if those variables remain in equations.
- **E2 — Table:** Retain a compact quantity table only where it helps the reader locate the transition requiring an assumption; each row should identify the quantity, a concrete example, and the additional evidence needed for the next inference.
- **E3 — Paragraph:** Explain how passenger counts, route assignments, service histories, and documentation inform different quantities; identify dependence when two records originate from the same upstream measurement.
- **E4 — Paragraph:** Describe probabilistic inference at the level needed by the decision comparison; remove an unused general belief-state equation, or explicitly connect its marginal quantities to the example. Do not retain a physical-failure equation solely to provide formal appearance.
- **E5 — Paragraph:** State the bounded identifiability result supported by the example: route/use information alone does not determine the parameters of the finding or consequence model. Distinguish assumed quantities from parameters estimable from the hypothetical observations; do not import an unproved hazard-confounding theorem.
- **E6 — Paragraph with derivation:** Under explicitly stated assumptions, show how a shared additive error remains in a population average and cancels in a pairwise difference, while group-specific errors can alter a difference. Distinguish a fixed bias from a random common error before making any variance statement.

## 4. Procedure for a maintenance choice

- **D1 — Paragraph:** Introduce the procedure's input as a documented decision and evidence record, and its output as an admissible choice with assumptions, an unresolved comparison with an executable fallback, or a justified information request with a deadline.
- **D2 — Table or numbered procedure:** Give five steps with inputs and recorded outputs: specify the decision; assess the information regime; trace the evidence; compare admissible choices; record the outcome and trigger for reconsideration. Refer the applicability step to the checklist and the comparison step to the expected-loss formulation.
- **D3 — Paragraph:** Separate mandatory requirements from the discretion assumed in this illustration: an additional inspection, its order within an allowed window, or an information-gathering action. Require an admissible baseline schedule and escalation when changed circumstances make it inadmissible; do not invent jurisdiction-specific intervals.
- **D4 — Paragraph with equation:** Define the common planning horizon and time basis, admissible policies, expected total loss, and model alternatives. An inspection policy includes the action taken after each possible finding, so its cost and benefit are evaluated under that information pattern.
- **D5 — Paragraph with equation:** Compare policy losses across declared plausible models. State the strict-sign condition for a supported pairwise order and the treatment of ties or reversals; distinguish supported robustness within the specified set from correctness of that set.
- **D6 — Paragraph:** State the fallback: retain the pre-existing admissible schedule or documented tie-break when evidence cannot justify reordering, obtain information only if it can inform the decision before the window closes, and escalate when mandatory or consequence-based requirements supersede the baseline.
- **D7 — Paragraph:** Explain population allocation under the same resource and service constraints; exposure, expected consequence, and expected inspection benefit answer different questions. Use the two-door calculation to demonstrate the distinction without adding an unneeded three-asset model.

## 5. Worked symbolic station example

- **S1 — Paragraph:** Declare the example hypothetical; distinguish its shared station motivation and passenger proxy from the companion GPECOM paper's technical proxy-flow/service-condition/scheduling implementation. State any actual reused material explicitly and avoid suggesting that the present assumptions are station measurements.
- **S2 — Paragraph:** Apply procedure step 1: identify the two door functions, inspection-capacity constraint, planning interval, admissible choices, contingent response to an inspection finding, and the existing admissible schedule. Limit discretionary reordering to the assumed window.
- **S3 — Paragraph:** Apply step 2: supply the case-specific yes/no answers for the checklist, name the condition information that is missing, and identify the reason the limitation persists during the comparison interval.
- **S4 — Paragraph:** Apply step 3 to passenger counts, route assignments, and door operation; distinguish passenger passages from opening cycles and accumulated exposure, and explain the role of grouping and controller behavior without assigning numerical factors.
- **S5 — Table:** Trace each source to the quantity it informs, the assumption required for the next link, and a possible check. Keep this table distinct from the applicability checklist and decision-results table.
- **S6 — Figure:** Use the retained conceptual station diagram to locate evidence-to-quantity links. Caption it as a schematic with no measured or estimated station outputs, and ensure prose supplies the assumptions hidden by arrows.
- **S7 — Paragraph with equations:** Specify the bounded symbolic comparison through the expected gain $G_i=q_i d_i v_i-k_i$ relative to the same admissible baseline: $q_i$ is the probability of an actionable condition, $d_i$ the conditional detection probability, $v_i$ the avoided loss from the stated contingent action, and $k_i$ the inspection burden in the same loss units. State the assumed absence of false positives and the treatment of intervention cost in $v_i$. Define the baseline consistently across A, B, and retaining the schedule; a probability of a detected finding must not be multiplied by detection again.
- **S8 — Paragraph:** Apply step 4 to the agreement case: under the stated comparability conditions, derive when greater exposure supports the same door as the policy-loss comparison. State the premise that connects exposure to the relevant event or finding.
- **S9 — Paragraph:** Derive a contrasting case with unequal effectiveness, consequences, or costs where the inspection-policy comparison favors the other door despite the exposure ordering. Use symbolic inequalities, retaining the conditions of the result and reporting no numerical magnitude or operational improvement.
- **S10 — Paragraph:** Reconsider the ranking across plausible routing or finding-model alternatives. Preserve the historical timing: a corrected route assignment was already in force during the interval whose exposure is assessed. State when the loss difference changes sign or includes a tie and the ordering becomes unresolved.
- **S11 — Table:** Collect agreement, reversal, and unresolved comparison cases with their symbolic conditions and operational outputs. Include the baseline schedule or tie-break for unresolved cases and explain how to read across the table.
- **S12 — Paragraph:** Apply step 5: record the chosen inspection or baseline schedule, the premises on which it rests, the observation that would change it, and the latest useful time for new information. Do not present an unevaluated local counting exercise as having positive net value.
- **S13 — Paragraph:** State the treatment of service and observation in this bounded comparison: no lifetime model is fitted to censored records, any baseline condition or finding parameter is assumed, and the effect of the contingent action is part of the consequence model. Identify what actual records would be needed to estimate these inputs.
- **S14 — Paragraph:** Explain the population consequence of the comparison and shared-error derivation: group workload and individual inspection order require different information, and a shared uncertain mapping can limit both. Keep this application short rather than repeating the full inference chain.

## Approved numerical continuation, 2026-10-23

The author subsequently approved the complete numerical specification. This addition supersedes the no-numerical-input statements for the earlier symbolic pass; the analytical derivation remains in place.

- **N1 — Paragraph:** State the two historical routing interpretations, dimensionless exposure, affine condition probability, detection range, common loss scale, and the approved net response and inspection values. Identify every input as hypothetical.
- **N2 — Paragraph with equations:** Substitute the approved values into the gain expressions and derive the continuous ordering and baseline boundaries. Distinguish fixed-parameter robustness across routes from robustness across the full parameter rectangle.
- **N3 — Table:** Replace the redundant symbolic-scenario table with exact representative numerical gains, model-specific best policies, and the stipulated model-set action; preserve ties and label fallback explicitly.
- **N4 — Paragraph:** Explain agreement and exposure-order reversal, historical route correction, and the distinction between accepting the corrected route and retaining both interpretations as plausible.
- **N5 — Paragraph:** Expose the cost of strict unanimous preference: B can improve on the baseline in both models despite unresolved A/B ordering. Identify the adopted baseline fallback as a conservative protocol rather than a benefit-maximizing rule.
- **N6 — Paragraph:** State exact corner bounds over the full parameter rectangle and the limits of the result. Identify the deterministic calculation, tests, and generated artifacts, and revise abstract, conclusion and data availability to match the numerical work actually performed.

## 6. Discussion

- **C1 — Paragraph:** Summarize the demonstrated contribution in ordinary maintenance terms: specify applicability, document inferential assumptions, compare admissible inspection policies, and state an executable outcome when the comparison is unresolved.
- **C2 — Table:** Compare small-data PHM, usage/load-based maintenance, soft/virtual sensing, and Bayesian/POMDP inspection planning by question addressed, required evidence and assumptions, overlap, and role in the procedure. Cite inspected sources; do not assign exclusive capabilities to LD-PdM or imply that established methods cannot use indirect evidence or support decisions.
- **C3 — Paragraph:** Give a concise substantive comparison with Li et al. and the companion work, with no internal section-number recital or claim of novelty for persistent scarcity, uncertainty, indirect sensing, or Bayesian action choice.
- **C4 — Paragraph:** Consolidate scope and limitations: the example supplies conditional algebra, not calibrated finding probabilities, a numerical sensitivity experiment, failure prediction, or measured maintenance benefit. Explain why the absent parameters require evidence before operational deployment.
- **C5 — Paragraph:** State evaluation recommendations: independently check proxy relationships and finding models, examine uncertainty/calibration and context changes, and compare policy consequences under identical resources. Distinguish recommendations from an author's committed research programme.
- **C6 — Paragraph:** Explain the title's structural mismatch in light of the outputs and the limits of applicability. Preserve the invited title and leave editorial journal-fit judgment open without inventing information-theoretic novelty.

## 7. Conclusions

- **K1 — Paragraph:** Answer the Introduction's characterization question using the checklist and procedure; state the applicable condition and what a reader records when it remains unresolved.
- **K2 — Paragraph:** State the symbolic example's result and its assumptions: exposure and inspection priority agree only under suitable finding/consequence relations; different action effects can reverse the order; model-dependent reversals or ties trigger the admissible fallback. Keep the conclusion within the analysis performed.
- **K3 — Paragraph:** Identify the evidence required to move from the conceptual procedure to evaluated maintenance performance, without recasting optional future work as an implemented model.

## Closing matter and verification

- **V1 — Author-declaration paragraph:** Preserve the author-deferred AI statement and other declarations as pending author confirmation; record actual assistance and verification without inventing tool/version history or claiming every source was read in full.
- **V2 — Verification artifact:** Update the response matrix with disposition, actual manuscript location, and verification evidence for every review point; distinguish previous completed work, this pass, partially met requests, and author-deferred items.
- **V3 — Verification artifact:** Compile and inspect the revised manuscript, check citations and equation/table references, inspect all rendered pages, and record the outcome. A successful previous build is not validation of the new source.
