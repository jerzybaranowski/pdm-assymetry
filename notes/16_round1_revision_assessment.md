# Round 1 review assessment and proposed revision

**Date:** 2026-10-26  
**Status:** Historical assessment and proposal. On 2026-10-26 the author instructed implementation after checkpoint commit `0f7a169`; see [the specification addendum](12_two_door_model_specification.md#9-decision-rule-revision-authorized-on-2026-10-26). Approval statements below describe the assessment stage before that instruction.
**Reviewed version:** 2026-10-25 manuscript and 18-page PDF, SHA-256 `476c89fe8dd86bd3e7e21c8a9ca2e7c8fc9b682e6b13e31ac5ea8e0e660bb8c4`.  
**Reviews:** Four [simulated internal reviews](../reviews/round1/README.md), not journal decisions. Review references below identify numbered major comments, for example R2.1.

## Assessment

The reviews identify a substantive weakness that the October 25 editorial correction did not resolve: the example still selects the existing schedule when an available inspection improves on it under every retained model. Explaining this opportunity cost makes the rule transparent but does not make it a defensible recommended decision procedure. The calculation implements the approved specification correctly; the problem is the choice rule, not numerical arithmetic.

The second weakness is the gap between the proposed assessment procedure and its demonstration. The manuscript provides criteria, a five-step procedure, and a numerical final decision link, but does not supply a completed assessment record connecting them. Existing negative and unresolved examples are useful but stipulated; they do not establish usability. The strongest bounded revision would deliver a checkable decision record and an undominated action comparison, while narrowing the claims to what these demonstrate.

The reviewers also overreach. Several suggested mathematical corrections are wrong or require additional assumptions. A full Bayesian observation model, a population simulation, empirical validation, and a value-of-counting experiment are distinct extensions. Combining all of them would replace the agreed conceptual paper with a substantially different project.

The invited title, canonical **Limited-Data Predictive Maintenance (LD-PdM)** term, conceptual contribution, railway-station setting, and absence of available empirical data remain the protected scope. The approved numerical inputs can be retained while revising the decision criterion, subject to author agreement on that scientific change.

## Priorities and review coverage

| Priority | Review comments | Assessment and proposed response |
|---|---|---|
| P0 | R1.2; R2.1; R3.4; R4.1 | Accept. Filter dominated policies, distinguish feasibility from decision-theoretic admissibility, and declare the criterion used among the survivors. A disclaimer about conservative fallback is insufficient. |
| P0 | R1.3–4; R2.2,7,9; R3.2–3,7–8; R4.4 | Accept the need for an executable assessment and completed record. Specify yes/no/unresolved consequences and case-specific evidence requirements. Do not invent universal thresholds or claim validated usability. An empirical case is unavailable under the confirmed scope. |
| P0 | R1.1; R2.6; R4.5,12 | Accept the positioning gap. Compare directly with PdM suitability assessment and established uncertainty-aware decision analysis. Make the increment over the companion paper more visible without claiming that indirect inference or checklists are new. |
| P0 | R2.3; R3.5; R4.9 | Accept the narrative ambiguity. Separate records that invalidate a routing model from evidence that merely challenges it. Define the model set used for each decision and distinguish it from the parameter sensitivity rectangle. |
| P1 | R1.5–6; R2.5,8; R3.6; R4.2–3 | Partially accept. Define the actionable condition, inspection sensitivity, contingent response, and conditional benefit more clearly. State which links are stipulated. A learned observation model, nonlinear degradation, or Monte Carlo benchmark requires a separate scientific specification. |
| P1 | R1.7,9; R2.8 | Accept the engineering evidence gap. Audit available controller/service channels before assuming a proxy is necessary; distinguish absence from lack of access. Keep schedule constraints explicit. Ground retained claims about informative maintenance records in appropriate sources; avoid adding an unimplemented repair or censoring model. |
| P1 | R1.10; R2.2,5; R3.1,9; R4.6 | Clarify one central asymmetry: consequential maintenance choices can coexist with weak feasible condition information. Do not invent a symmetry theorem or measured consequence–observability ordering. Equal response values in the example do not logically refute this mismatch. Journal fit remains an editorial risk. |
| P1 | R1.8; R2.4; R3.9; R4.11 | Accept reduced prominence and tighter scope for the shared-error identity. Exposure-error cancellation does not generally imply cancellation in decision gains. Do not substitute the reviewer's conserved two-route model for the approved three-passage narrative. |
| P1 | R1.11; R4.8,10; R2.9; R3.8 | Replace repeated generalities with the completed record and a decision-region figure. Reduce duplicated conceptual diagrams and repeated caveats. Describe a proposed assessment procedure, not demonstrated operational usefulness. Phrase counts do not establish AI authorship. |
| P1/P2 | R3.10; R4.7,13; associated minor comments | Make the eventual code/data-access statement concrete, prepare inspectable supplementary material, and resolve author declarations. Local verification is not public availability. Deposit, submission, and unconfirmed disclosure or funding details require separate action or confirmation. |

## Checked decision analysis

### Dominance is the immediate repair

The approved example compares three deterministic policies: retain the schedule, inspect A, or inspect B, with a contingent feasible service response after a positive finding. Relative gains are

\[
G_0=0,\qquad
G_A(m_1)=d_A(1+10\beta)-1,\qquad
G_A(m_2)=d_A(1+3.5\beta)-1,\qquad
G_B=4.5\beta-0.1.
\]

At the existing case \((\beta,d_A)=(0.2,0.9)\):

| Policy | Gain under \(m_1\) | Gain under \(m_2\) | Minimum gain | Maximum regret |
|---|---:|---:|---:|---:|
| Schedule | 0 | 0 | 0 | 1.7 |
| Inspect A | 1.7 | 0.53 | 0.53 | 0.27 |
| Inspect B | 0.8 | 0.8 | 0.8 | 0.9 |

Both inspections improve on the schedule under both models. A rule requiring a common strict winner before permitting any departure from the schedule discards that information.

First remove policy \(\pi\) if another feasible policy has at least as much gain in every retained model and strictly more in at least one. Then apply a declared selection criterion to the remaining policies. If the criterion or relevant inputs are unresolved, report the remaining alternatives and the missing decision commitment; do not silently reinstate an eliminated baseline.

### Recommended comparison of two objectives

Use minimax regret as the proposed main illustrative selector, with maximin incremental gain as a conservative comparator. This recommendation concerns their different decision objectives, not a claim that regret is universally preferable:

- **Maximin incremental gain** maximizes the minimum improvement over the existing schedule. It selects B in the displayed case.
- **Minimax regret** minimizes the largest loss of gain relative to the best feasible policy within each model. It selects A in the displayed case.

These alternatives require no new primary numerical inputs. Selection of the objective is a substantive author decision and must be explicit in any revised specification. The analysis is restricted to the three declared deterministic policies; allowing randomized policies would change the optimization problem.

Dominance filtering does not itself guarantee improvement over the baseline in every model. At the existing case \(\beta=1/45,d_A=0.9\), minimax regret selects A with gains \(0.10,-0.03\), while both the baseline and B give \(0,0\). Thus the proposal only partly accepts R3.4's suggestion of a robust-improvement gate: it accepts elimination of dominated fallback, but presents a criterion that can trade a small loss in one model for reduced opportunity loss in another. If nonnegative gain under every retained model is a mandatory requirement, impose that feasibility constraint before selection and revise the boundaries accordingly. The author's choice must cover this tradeoff, not just the criterion's name.

Do not call maximin gain “minimax total loss” without an additional assumption. Since

\[
R_m(\pi_i)=R_m(\pi_0)-G_i(m),
\]

unknown model-dependent baseline losses affect worst-case absolute loss. They cancel from within-model dominance and regret, and from expected-policy comparisons under fixed model weights, but not generally from the worst-case loss objective.

Over the existing parameter rectangle, maximin gain selects B for \(\beta>1/45\), the baseline for \(\beta<1/45\), and ties B with the baseline at equality. It is independent of \(d_A\) after the comparison across both routes. For minimax regret among the three deterministic policies:

- If \(\beta>1/45\), select A above \(d_A=(1.8+9\beta)/(2+13.5\beta)\), B below, and report a tie on the boundary.
- If \(\beta<1/45\), select A above \(d_A=2/(2+13.5\beta)\), the baseline below, and report a tie on the boundary. Only the part within the approved rectangle is relevant.
- At \(\beta=1/45\), A is selected above \(d_A=20/23\); the baseline and B tie below it, and all three tie at equality.

These checked formulas specify a possible later figure; they are not generated manuscript artifacts or an approved replacement calculation.

The reviewers' approximately 44.12% dominated-fallback area is correct as a geometric fraction of the chosen parameter rectangle. The approximately 99.67% figure refers only to the unresolved-fallback region, excluding justified baseline choices; among all baseline selections the dominated share is approximately 90.85%. None is an empirical frequency or a probability of operational occurrence. The explicit counterexample already establishes the defect, so percentages need not become headline findings.

### Mathematical objections that require correction

| Review claim or suggestion | Finding |
|---|---|
| Multiplying \(qdv\) requires independence of detection and benefit. | Incorrect under the manuscript's conditional definition of \(v\). With actionable condition \(C\), detection \(D\), and net avoided loss \(V\), \(\mathbb E[1_C1_DV]=P(C)P(D\mid C)\mathbb E[V\mid C,D]\). Dependence on severity is permitted. Make this conditioning explicit. |
| Conditional probabilities and an unweighted set of routing models are inconsistent. | Incorrect. Probabilities within a model can coexist with ambiguity between models. The example does assign probabilities to actionable condition and detection; it does not learn a posterior over routing models. |
| A shared additive exposure error cancels from the inspection comparison. | Generally incorrect. A shift \(s\) changes \(G_A-G_B\) by \(\beta s(d_Av_A-d_Bv_B)\). Exposure order and decision order are different objects. |
| The reviewer's shift of \(-0.6\) is an admissible reversal in the exposure example. | It makes \(x_B=-0.1\), outside a nonnegative-exposure interpretation. The underlying objection remains valid: near the approved tie at \((0.2,0.6)\), small positive or negative shifts can reverse the comparison while exposures remain positive. |
| Conservation of A/B flow is “exactly” the existing routing example. | Incorrect. The approved alternative sends some A traffic to a third passage and leaves B unchanged. A complementary A/B allocation model is a different assumption. |
| A fixed bias cannot have a variance. | Conditional on a known fixed bias, its sampling variance is zero; epistemic uncertainty about an unknown bias can still be represented probabilistically. Specify the conditioning rather than making a categorical statement. |
| EVPI/EVSI thresholds should replace the regime definition. | Not required. Consequential choices can have zero EVPI when one action is best in every state. Low EVSI can reflect restricted actions or decision insensitivity. These are useful optional diagnostics, not equivalent definitions of weak condition information. |

The general expected-loss formulation can indicate that condition beliefs depend on both evidence and the historical observation/intervention policy. A bare likelihood factorization would not solve informative observation by itself. A full longitudinal model would require observation timing, intervention rules, state evolution, and a justified ignorability statement; these are not supplied by the present example.

### Optional information-value calculation

At \((0.2,0.9)\), if an additional hypothetical model weight \(w=P(m_1)\) is supplied, A has greater expected gain than B when \(w>3/13\). The value of perfect information about which routing model applies is

\[
\mathrm{EVPI}(w)=
\begin{cases}
0.9w,&w\leq3/13,\\
0.27(1-w),&w\geq3/13.
\end{cases}
\]

This confirms the relevant reviewer arithmetic, including 0.135 at equal weights. It is not the value of an actual counting exercise. That requires its observation likelihood, cost, timing, and decision consequences. Inspection burden \(k=1\) is not the cost of counting. This extension is optional and should not displace the core repair.

## Proposed bounded revision package

### 1. Make the assessment record the concrete contribution

Give one compact, completed record with: the maintenance choice and horizon; feasible policies and schedule constraints; actionable condition and response; available condition channels; indirect evidence and inferential links; acquisition/access constraints; fixed assumptions; retained uncertainties; model exclusions; dominance result; selection objective; recommendation and conditions for reconsideration.

For the checklist, explain what yes, no, and unresolved mean. A failed criterion limits classification as LD-PdM; an unresolved criterion identifies an evidence or specification gap. Classification should trigger particular scrutiny of indirect links and uncertainty, not claim a unique algorithm. Remove the implication that weak direct information necessarily entails useful indirect evidence.

Classify relative to a declared feasible-information set and decision horizon. Distinguish hard access/resource constraints from an untested judgment that monitoring would be uneconomic. Expanding the evidence set is a separate monitoring-investment decision that can change the classification; this addresses R1.4's endogeneity objection without pretending the available information is an immutable asset property.

Use the existing contrasting cases to demonstrate these branches: directly observed obstruction, the hypothetical two-door choice, and passenger counts without a justified link to device use. Specify a relevant condition distinction and the resolution needed for the choice. “Material” should concern a documented effect on condition assessment or action comparison, not require the preferred action to change. Robust action can coexist with uncertain condition.

### 2. Separate evidence states and levels of uncertainty

Distinguish a record establishing the corrected routing model, which excludes the contradicted model, from a record leaving both interpretations plausible. The parameter rectangle is an illustrative sensitivity domain, not an elicited uncertainty distribution. A comparison at fixed \(\beta,d_A\) across two routing models is different from a decision robust over the entire rectangle.

The example demonstrates propagation of stipulated exposure interpretations through the final condition-to-action link. It does not estimate exposure or condition from passenger records. Remove “Bayesian inference” from the keywords unless a genuinely implemented inference step is added. Retain partial observability as a relevant conceptual descriptor without suggesting that a POMDP algorithm is implemented.

### 3. Strengthen positioning with a small number of direct predecessors

Tiddens et al. already combine criticality, technical/economic/organizational feasibility, and Yes/No/Maybe assessment. Checklist format and the distinction between consequence and monitoring feasibility cannot establish novelty. The narrower proposed contribution is an assessment of an already specified maintenance choice that traces indirect evidence through intermediate quantities and tests the resulting action rationale. This is an organizing emphasis, not a claim that existing frameworks cannot do so.

Add a direct decision-analysis basis for dominance and alternative objectives. If model uncertainty remains prominent, include one closely relevant maintenance-planning comparison. Retain the Li comparison. The companion GPECOM paper should have a visible contribution boundary: it supplies related station routing/cycle inference; this paper proposes a decision-regime assessment and examines action dependence on uncertain indirect evidence. Preserve the completed full-text check and author-confirmed version identity. Explain the companion's “Low-Data” wording once without renaming LD-PdM.

Address the separate objection to “predictive maintenance” in R1.4: this illustration supports an inspection choice from stipulated condition probabilities, but does not establish a prognostic model or a complete PdM implementation. Explain that scope and the overlap with condition-based and risk-based inspection planning. Retaining the invited title and canonical term does not itself answer the objection. Any appeal to a formal standards definition requires verification of the original source before manuscript use.

### 4. Ground the station assumptions without inventing a deployment

Require an inventory of controller counters, fault logs, service records, and accessible OEM/contractor channels before motivating passenger proxies. Available usage counters may resolve usage uncertainty without resolving condition uncertainty. In the hypothetical example, absence or inaccessibility must remain a stated scenario assumption, not a factual claim about a station population.

Define the condition that makes the contingent service response worthwhile and distinguish it from failure. Clarify “reference inspection” so that the event underlying sensitivity is unambiguous. Unequal sensitivity remains hypothetical; do not assign a real mechanism or empirical range without evidence and author agreement. Keep early inspection additional to the admissible schedule. Do not insert generic standards as though they establish a particular station's legal or contractual obligations.

If detailed statements on intervention-dependent histories are retained, add focused reliability support after checking original sources; otherwise shorten them to a limitation. The review's proposed censoring and imperfect-repair references are candidates, not verified additions to the bibliography in this assessment.

### 5. Reduce repetition and align figures with the argument

Retain one necessary conceptual overview and replace overlapping explanatory material with the completed record. Add a data-based figure comparing decision regions for the declared objectives, with exact ties and the feasible parameter domain. Choose the scientific criterion before designing the figure.

Remove the elementary shared-error identity from the Abstract. Either shorten the subsection to an exposure-level caution or connect it explicitly to the gain-error expression above. Clarify that the population calculation counts assets, not repeated independent records, and avoid presenting it as demonstrated fleet optimization. Disambiguate the shared-error symbol from door B.

Rewrite Abstract, contribution statement, and Conclusions around the delivered assessment record and conditional decision illustration. Remove claims of demonstrated usability, improved maintenance performance, or an implemented complete Bayesian chain. Keep assumptions beside the claims they qualify and remove repeated generic qualifications. The hostile review's stylistic counts are not evidence of authorship, but several identified sentences can still be improved on clarity grounds.

### 6. Complete delivery and declarations after scientific revision

Prepare an inspectable supplement containing the approved inputs, calculation source, outputs, and regeneration instructions once the revised criterion is settled. A public repository or persistent deposit would require separate authorization. Do not claim that a local source tree is publicly accessible or that a deposit already exists.

Resolve the deferred AI declaration using confirmed roles and records. Do not invent historical model versions. Verify any grant identifier against authoritative project records; a reviewer's number is not author confirmation. Affiliation and submission-history checks remain pending author matters. These declarations do not resolve the scientific criticisms.

## Proposed paragraph and artifact sequence

Each item below represents one paragraph or one separately identified artifact. It replaces overlapping material rather than appending another general framework section.

1. Introduction paragraph: the specified maintenance decision and the practical mismatch between its consequence and feasible direct condition information.
2. Positioning paragraph: overlap with small-data PHM and PdM feasibility assessment; narrower organizing purpose of this contribution.
3. Contribution paragraph: assessment criteria, documented decision record, and conditional illustration with explicit selection objectives.
4. Definition paragraph: unit of classification, horizon, feasible evidence set, and meaning of yes/no/unresolved.
5. Checklist table: criteria, required evidence, and consequence of an unresolved assessment.
6. Boundary-case paragraph: the directly observed obstruction and the unsupported passenger-to-device link.
7. Inference paragraph: what each intermediate quantity means and which links remain stipulated or uncertain.
8. Conceptual figure: retain the single overview needed to connect those quantities.
9. Decision paragraph: feasible policies, within-model gains, dominance filtering, and declared objective.
10. Assumption table: existing approved inputs and their hypothetical status, including condition, detection, response, and constraints.
11. Evidence-state paragraph: corrected routing versus unresolved routing; fixed-case comparison versus sensitivity analysis.
12. Completed assessment record table: all procedure steps for the two-door case, including the action rationale.
13. Numerical comparison table: existing cases under the revised selector and conservative comparator, with ties explicit.
14. Decision-region figure: sensitivity of the policy choice to \(\beta,d_A\) under the declared objectives.
15. Interpretation paragraph: why exposure ranking, guaranteed improvement, and opportunity-loss control can disagree.
16. Shared-error paragraph: limited exposure claim and its decision-level qualification, if retained.
17. Discussion paragraph: increment over feasibility frameworks and the companion station work.
18. Scope paragraph: conceptual demonstration, missing learned observation process, and untested usability/operational performance.
19. Conclusion paragraph: what the completed assessment makes inspectable and what remains a decision-maker commitment.

## Acceptance criteria for a later implementation

- Every numerical recommendation is feasible, undominated, and traceable to its stated criterion and uncertainty set; equality cases are explicit.
- The same evidence state produces the same model set in the symbolic narrative, worked record, table, and figure.
- The inputs retain their approved provenance; no hypothetical quantity becomes an empirical estimate.
- Conditional benefit is defined consistently, and no independence assumption is added unnecessarily.
- At least one completed classification/application and the existing no/unresolved cases are visible; usefulness claims match the evidence supplied.
- Literature comparisons acknowledge direct predecessors and distinguish full-text support from metadata-only checks.
- Any production-code change receives meaningful regression tests under `testing-workflow`; figure work follows `scientific-figures`; conceptual diagram changes follow `tikz-diagrams` and the approved content plan.
- Rebuild and visually inspect the PDF after implementation. The October 25 checks remain evidence for the unchanged reviewed version, not for this proposed revision.

The present request authorizes assessment. It does not by itself select a new scientific objective, approve model extensions, finalize a new figure, or authorize publication. The next concrete author decision is whether to adopt dominance filtering plus the proposed minimax-regret illustration and maximin-gain comparator, together with the bounded textual revision above.

## Verified literature for the proposed positioning

- **Tiddens, W. W.; Braaksma, A. J. J.; Tinga, T. (2018).** “Selecting Suitable Candidates for Predictive Maintenance.” *International Journal of Prognostics and Health Management*, 9(1), article 020. DOI: `10.36001/ijphm.2018.v9i1.2699`. The original paper's feasibility stages and Yes/No/Maybe procedure were inspected, particularly pp. 5–7. [Publisher full text](https://papers.phmsociety.org/index.php/ijphm/article/download/2699/1647/7584).
- **Troffaes, M. C. M. (2007).** “Decision making under uncertainty using imprecise probabilities.” *International Journal of Approximate Reasoning*, 45(1), 17–29. DOI: `10.1016/j.ijar.2006.06.001`. The author manuscript supports dominance filtering and distinctions among decision criteria; map its state-dependent gains carefully to model-specific expected gains here. [Author manuscript](https://arxiv.org/html/1807.03705v1); [institutional publication record](https://durham-repository.worktribe.com/output/1576888/decision-making-under-uncertainty-using-imprecise-probabilities).
- **Arcieri, G.; Hoelzl, C.; Schwery, O.; Straub, D.; Papakonstantinou, K. G.; Chatzi, E. (2023).** “Bridging POMDPs and Bayesian decision making for robust maintenance planning under model uncertainty: An application to railway systems.” *Reliability Engineering & System Safety*, 239, 109496. DOI: `10.1016/j.ress.2023.109496`. Optional comparison: the authors' preprint and institutional account support maintenance planning with inferred model uncertainty, not equivalence to an unweighted unanimity rule. Final-version identity was not established. [Author preprint](https://arxiv.org/pdf/2212.07933); [ETH account](https://chatzi.ibk.ethz.ch/smm-news/2023/07/bridging-pomdps-and-bayesian-decision-making.html).

Existing reference 19 has a matching publisher record; one reviewer's inability to retrieve it does not establish a fabricated citation. The Srinivasan–Parlikad POMDP characterization is supported by the original publisher text. The related HVAC work warrants a more specific comparison. These checks do not authorize importing every reference proposed by the reviewers. No bibliography entries were added during this assessment.
