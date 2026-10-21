# Proposed revision plan after round 0

**Date:** 2026-10-21  
**Basis:** the four simulated reviews in [`reviews/round0/`](../reviews/round0/README.md), the current `paper/template.tex`, and the current revision status in [`AUDIT.md`](../AUDIT.md).  
**Status:** proposal for author review. This plan does not change the manuscript or the accepted scope; `AUDIT.md` remains the authoritative status register.

The recommended revision should make the conceptual contribution usable: a procedure for assessing a maintenance decision under weak condition information, explicit criteria for applying it, and a worked example that exposes a misleading proxy-based ordering. A small, exactly calculated synthetic example would make the strongest response to the reviews while preserving the paper's conceptual identity. A complete station simulation, fitted degradation model, or new inference algorithm is unnecessary for this revision.

Retain the invited title, **Limited-Data Predictive Maintenance (LD-PdM)**, and the railway-station setting. The existing author decision permits a high-level simulation if useful but makes quantitative demonstration optional. These simulated reports identify weaknesses to address; their recommendations are not journal decisions or authority to expand the project.

## Assessment of the reviews

The recurring weakness is that the manuscript promises operational criteria and traceable decisions but delivers mostly qualitative distinctions and an example whose conclusion follows directly from its comparability assumptions. The three generic equations do little subsequent work. Repeated qualifications then occupy space that could show the procedure in use.

The reports should be consolidated into work packages rather than implemented as four independent checklists. R1 and R2 explicitly request computation; R3 requires a usable procedure and a discriminating example but does not make numerical simulation a prerequisite. R4 identifies substantive problems with abstraction, repetition, terminology, and reference support. Address these through close reading and scientific revision.

**Author clarification, 2026-10-21:** AI assistance is acknowledged. The editorial goal is proper literary quality and readability for human researchers. Review the prose for formulaic contrasts such as “this is not X; this is Y”, vague abstractions, and other constructions whose apparent fluency exceeds their meaning. Use established maintenance and reliability terminology; preserve LD-PdM as the agreed name of the regime while describing its ingredients with their existing field names. This requires judgment about complete passages, beyond what a Python phrase search can establish.

Several issues need clearer presentation rather than reversal of an established conclusion:

- The manuscript already distinguishes the defining conditions from rare-event and population complications, but explains that hierarchy too late.
- Decision theory, inspection value, and partial observation are already attributed to existing work. The gap is their use in the example and the specificity of the contribution.
- The source matrix records checks for the questioned `Xin2026` entry and for GPECOM. A reviewer's unsuccessful search does not establish that a reference is false.
- The GPECOM content comparison is already documented as complete using the public full text and the author's confirmation of version identity. Its contribution boundary still needs to be more visible to a reader of this manuscript alone.

## Revision packages and acceptance criteria

| Priority | Package | Main review points | Deliverable and completion criterion |
|---|---|---|---|
| P0 | 1. Specify the contribution and its relation to prior work | R1.1, R1.5–6; R3.1; R4.1, R4.4 | A concise contribution statement mapped to concrete manuscript artifacts, supported by a focused comparison with adjacent approaches. No claimed capability is incorrectly denied to prior work. |
| P0 | 2. Turn the characterization into a procedure | R1.3; R2.3; R3.2–4, R3.7 | A procedure with inputs, outputs, applicability checks, and unresolved cases; a worked inclusion case and counterexample; an early explanation of each asymmetry's logical role. |
| P0 | 3. Make the example and mathematics do useful work | R1.2; R2.1–2, R2.4–8; R3.5; R4.5–6 | A reproducible decision comparison that can differ from naive passenger/exposure ordering, with sensitivity and an explicit stopping condition. Every retained equation is used and every symbol is defined consistently. |
| P1 | 4. State the operator's remaining choices and fallback | R1.4, R1.7–8; R2 minor information-pattern point | Mandatory actions, discretionary inspection order, subsequent actions, and the fallback after an unresolved comparison are distinguished. The example ends with an executable planning choice. |
| P1 | 5. Strengthen source support and expose provenance | R1.5–6; R2 reference points; R3.8; R4.3–4 | Targeted prior-art coverage, source checks at the strength of each retained claim, and a short manuscript-level explanation of the relation to GPECOM. |
| P1 | 6. Rebuild the argument and remove duplication | R1.9–10; R2.9–10; R3.6–7, R3.9; R4.7–8 | Sections follow the procedure; tables and figures have distinct jobs; the title's central mismatch is explained without inventing mathematical novelty. |
| P1 | 7. Edit for human readers and disciplinary terminology | Author clarification; R3.10; R4.1–2, R4.4, R4.9 | A terminology review and contextual editorial reading establish that each paragraph communicates a concrete scientific point, uses established terms, and connects clearly to the argument. |
| P2 | 8. Verify the revised artifact and close the response record | All minor points; R4.10 | Clean build, complete visual inspection, consistent voice and abbreviations, and a response matrix recording a disposition for each review point. Author-deferred declarations remain separate. |

### 1. Specify what the paper contributes

Organize the contribution around three inspectable outputs: an applicability checklist, a procedure connecting evidence to an admissible action, and an example demonstrating the consequences of an unsupported link. The Introduction should point directly to each artifact. The Conclusions should state what applying them establishes.

Extend positioning beyond Li et al. and the currently cited decision-theory papers. The focused comparison should cover small-data PHM, usage/load-based maintenance, virtual or soft sensing, and Bayesian/POMDP inspection planning. Use columns such as **question addressed**, **required evidence and assumptions**, **overlap**, and **role in the proposed procedure**. Avoid a binary table implying that established approaches cannot use indirect evidence or support decisions.

The reviewers' suggested sources are search leads, not pre-approved references. Inspect the relevant original passages before adopting their claims or adding them to `paper/extracted.bib`. Add citations to close identifiable gaps; a larger reference count is not a completion criterion. Preserve the broader Li overlap established in [`literature/02_positioning_vs_li2024.md`](../literature/02_positioning_vs_li2024.md), while replacing detailed section-number citations in the manuscript with a concise substantive comparison.

### 2. Present a procedure that an analyst can apply

Move the useful examination currently summarized in the Conclusions into the body and expand it into five steps:

1. **Specify the decision:** asset function, mechanism, horizon, consequences, available actions, resource constraints, and mandatory requirements.
2. **Assess the information regime:** identify feasible condition-sensitive channels, the unresolved quantity, the reason the limitation persists over the horizon, and the role of indirect evidence.
3. **Trace the evidence:** connect each source to the quantity it informs, state the assumptions for the next link, and identify shared sources or competing interpretations.
4. **Compare admissible choices:** evaluate the action rationale across the stated plausible assumptions, including the actions that follow an inspection finding.
5. **Record the outcome:** supported choice, unresolved comparison, or information request, together with the applicable fallback and the observation that would trigger reconsideration.

For each inclusion criterion, provide a question, required justification, and possible **yes / no / unresolved** outcome. Explain consequentiality through specified differences in operational or economic outcomes; weak information through the relevant uncertainty left by feasible channels; and material contribution through whether indirect evidence changes the assessment or its justification. Document case-specific judgments rather than inventing a universal threshold.

Apply the checklist to the door-inspection choice and to a boundary case with few samples but an informative condition channel. Show that one asset can belong to different regimes for different decisions. The checklist should distinguish membership of the regime from whether the current evidence supports a differentiated action.

Explain the four asymmetries before their detailed subsections: observability and acquisition constraints concern the defining mismatch, sparse/selective failures complicate learning, and population scale creates opportunities and additional dependencies. Do not make all four mandatory conditions. Do not substitute low net information value for weak observability: information content, decision sensitivity, and acquisition cost are different quantities.

### 3. Use a bounded analytical example

The recommended extension is an exactly calculated synthetic example with two doors, a stated inspection-capacity constraint, and a finite set of possible observations and subsequent actions. It can be small enough to reproduce from an input table and a short Python script. Its purpose is to reveal a decision-relevant distinction, not to estimate station performance.

Prepare a concrete model specification for author review before calculation, covering:

- A hypothetical routing/use interpretation and at least one plausible alternative.
- An explicitly assumed link to an actionable inspection finding, with its observation uncertainty.
- A consequence table and the action available after each finding.
- Candidate choices such as inspecting A first, inspecting B first, or retaining the existing schedule, compared under the same resources and service obligations.
- A naive comparator based on passenger count or exposure and a sensitivity range justified as illustrative assumptions.

Use unequal inspection effectiveness, consequences, or routing ambiguity to examine when the naive order agrees with the decision comparison and when it does not. Show a region of agreement as well as disagreement or unresolved ordering; do not select one numerical configuration and present it as general superiority. Report the result actually obtained, including the possibility that the chosen illustration adds little.

A precise stopping condition can compare the expected-loss difference between the two choices over a declared set of plausible models or parameters. A common strict sign supports that ordering within the set; sign changes or ties require a more qualified conclusion. This is an application of established decision reasoning. It does not, by itself, choose the operational fallback.

Preserve the current example's temporal meaning: the corrected route assignment was already in force during the exposure interval being assessed. A later rerouting cannot erase accumulated historical exposure. Calculate the value of a local counting exercise only if its observation model, cost, and possible effect on the subsequent choice are specified.

Repair notation while building the example: separate usage from accumulated exposure, define the horizon and time basis, make prospective action effects explicit, relate physical condition to the system trajectory, and represent inspection together with the contingent action that follows. Retain a belief-state equation only if it is used. A physical-failure probability need not be calculated if the demonstration concerns inspection findings; shorten or relocate unused general formalism accordingly.

One short derivation may clarify why a shared error can survive aggregation while a common additive offset cancels in a difference. State the assumptions and distinguish fixed bias from uncertain common error. Add a model-specific identifiability observation only if it helps the example. The reviewer's suggested hazard-confounding claim is not a general theorem to import without checking its model and observation assumptions.

This package does not require a Dirichlet routing model, a fitted hazard, RUL prediction, a complete POMDP, a separate three-asset example, or a new pooling experiment. If the author retains a wholly qualitative route, use explicit contrasting cases and an auditable decision table, and limit claims of quantitative or formal demonstration accordingly. Qualitative criteria can still be operational when their application and evidential requirements are clear. That route can address R3 but leaves more of R1/R2's request unanswered.

### 4. Complete the operational decision

The manuscript already excludes mandatory requirements from the discretionary ordering, but should identify what remains adjustable: additional inspections, their order within a permissible window, information gathering, or coordination of visits. Check applicable standards and jurisdiction before naming specific legal duties or intervals. Do not infer that a rule covers every illustrated asset or that mandatory maintenance eliminates all planning discretion.

After withdrawing a proxy-based preference, explicitly retain the pre-existing admissible schedule or its documented tie-break rule. If a mandatory or consequence-based requirement determines the order, it takes precedence. An unresolved model comparison should not leave the planner waiting indefinitely for information that cannot arrive within the window.

Give a compact account of how observation and maintenance affect the records: distinguish right/interval censoring, missing records, selective inspection, and condition change after service. State the treatment assumed in the illustration. Do not attach a full survival-analysis model merely to enumerate possible methods.

### 5. Resolve literature and provenance concerns proportionately

Use [`literature/03_claim_source_matrix.md`](../literature/03_claim_source_matrix.md) as the starting point. It records metadata/abstract checks for `Xin2026`, `Ren2018261`, and `Buznikov20181216`; these are not equivalent to full methodological reading. Reassess whether the cross-domain examples help the argument, and prefer representative maintenance or soft-sensing sources where they support the actual claim. Replace peripheral examples for relevance, without repeating unverified allegations about a venue.

Expose the GPECOM distinction already documented in [`literature/04_gpecom_contribution_boundary.md`](../literature/04_gpecom_contribution_boundary.md): its technical proxy-flow/service-condition/scheduling model versus this paper's applicability and evidence-to-action assessment. State the hypothetical status of the present example and identify any actual reuse explicitly. A new toy computation should serve the distinct conceptual question and should not reproduce the companion's results as new evidence. The current overlap check need not be repeated wholesale; revisit it for newly added material.

### 6. Rewrite around the outputs

Retain the broad progression from regime definition to evidence, decisions, station example, and Discussion, but give each part a concrete output. Write a paragraph-level outline before prose: one bullet per intended paragraph and separate bullets for tables or figures.

Use the applicability table for classification, the evidence/assumption table for the inference chain, and the example table for the decision comparison. Merge overlapping visuals if the revised material no longer gives both a distinct explanatory role. Keep one primary explanation of each limitation and retain short local provenance and event-definition labels where readers could otherwise mistake a schematic or synthetic result for evidence from a real station.

Explain the title through the mismatch between decision consequences and available condition information. An information-theoretic formula should be introduced only if it serves the argument; adding notation alone does not resolve journal fit. The invited title remains in place. Discuss fit through the actual contribution rather than promising a new mathematical symmetry theory.

Rewrite the Introduction, abstract, Discussion, and Conclusions after the procedure and example are stable. Replace abstract claims of usefulness with the specific distinctions the example demonstrates. Use consistent authorial voice, expand HVAC, shorten dense table cells, and clarify whether future evaluation is a recommendation or a committed research programme. Reduce repetition by function rather than imposing an arbitrary one-third cut.

### 7. Edit for human readers and disciplinary terminology

Give literary revision its own pass after the scientific argument is stable. A maintenance researcher should be able to follow the article without translating its vocabulary into familiar concepts or consulting the repository to discover what a paragraph means. AI assistance remains accurately disclosed; prose quality is judged by clarity, precision, coherence, and useful content.

First, review terminology against the inspected literature. Use conventional names consistently for condition monitoring, usage/load-based maintenance, partial observability, inspection planning, censoring, and value of information. Check proposed synonyms for hidden changes of meaning. Keep usage, exposure, physical condition, event probability, risk, and action priority distinct where the argument requires them, and define the distinction once in concrete engineering terms. Introduce a new term only when an existing term fails to express a necessary distinction; explain and justify that exception. LD-PdM must not become a reason to rename established methods or quantities.

Second, read each paragraph for its scientific message and its place in the argument. Identify what it says about a maintenance problem, which evidence or assumption supports it, and why the next paragraph follows. Rewrite passages that merely announce the usefulness of a framework or repeat the paper's intentions. Name the asset, evidence, quantity, or action wherever a generic noun conceals the referent. Preserve the qualifications that determine the truth of the claim.

Third, edit sentence construction and rhythm in context. Examine repeated “not X, but Y” contrasts, paired “equally/conversely” transitions, abstract nominalizations, generic topic sentences, balanced closing aphorisms, and repeated three-part lists. Keep a contrast when it establishes a necessary technical distinction; otherwise state the scientific point directly. Simple substitutions for flagged words will often leave the underlying vagueness intact.

Finally, perform a continuous read of the revised manuscript and ask a reader unfamiliar with the drafting history to explain its contribution, procedure, and example from the article alone. Any passage that needs an oral explanation should be revisited. Automated checks can locate inconsistent terms and recurring phrases, but cannot certify human readability or literary quality. The editorial review should record important passage-level changes and their reasons, without reducing the assessment to a phrase count or an AI-detection score.

Completion requires that the contribution is stated in ordinary disciplinary language, every paragraph advances the argument, terminology remains stable across prose and equations, and the example can be followed without reconstructing unstated steps. Read the abstract again after this pass: it should give a clear account of the problem, the work performed, and the resulting insight.

### 8. Verify and record closure

Create a response matrix with one row per numbered review point: accepted, partially accepted, or declined; reason; manuscript location; and verification evidence. A declined request should explain the scope or technical reason, especially for a full generative model, empirical validation, and journal/title changes.

If calculation code is added, use declared synthetic inputs, reproducible computation, and tests of the consequential decision and sensitivity behavior. Use the required testing and scientific-figure workflows when those artifacts are implemented. Conceptual TikZ changes follow the diagram workflow. No package installation is needed to propose the model.

After content stabilizes, compile the manuscript, check references and layout warnings, and inspect every rendered page. Reconcile the abstract and data-availability statement with any synthetic computation actually included. Keep AI disclosure as the existing author-deferred closing item; describe actual tool use and verification without inventing its history. Reconfirm affiliation and other author declarations at the existing final review stage.

## Execution order and stopping rule

Start packages 1 and 5 together: the contribution and source support constrain one another. Complete the procedure in package 2, then specify the small example and operational fallback in packages 3 and 4. Write the core sections first and revise framing and visuals afterward. Complete the terminology and literary review before the final response matrix and artifact checks. Record accepted work and closure evidence in `AUDIT.md` when implementation proceeds, while preserving its historical audit.

The revision is ready for another internal read when a reader can apply the criteria, trace a source to the quantity it informs, reproduce the example's choice or unresolved comparison, and identify the remaining operator action. Every contribution claim should point to one of these outputs. Synthetic calculation can demonstrate conditional behavior; it does not establish calibrated failure prediction, industrial savings, or superiority in deployment.
