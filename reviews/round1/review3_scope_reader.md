# Review Report — Reviewer 3 (assesses the scope of work strictly from the manuscript itself)

**Manuscript title:** Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems
**Journal:** *Symmetry* (MDPI)
**Version reviewed:** "Version October 25, 2026 submitted to Symmetry" (as printed in the PDF page header), 18 pages

---

## Approach of this review

I read the whole manuscript: abstract, all sections, Figures 1–2, Tables 1–5, Equations (1)–(6) and the back matter. I judged the work only on what the manuscript itself states or shows. I did not consult the cited references or any outside source, so anything not in the paper counts as absent. My questions were: What exactly was done and found? Where in the paper is each deliverable? Do the title, abstract, contribution statement (lines 56–63), body and conclusions agree? Are the key terms defined well enough to be applied? Could a reader apply or reproduce the work from the paper alone? I recomputed Equation (6), every entry of Table 4, the boundaries c(β), d_A = 1/(1+10β) and β = 1/45, and the gain ranges stated at lines 483–484 from the inputs at lines 442–451. All of them are correct. Line numbers below refer to the PDF line numbering.

---

## Summary as I understood it

**What was done.** The paper proposes a "regime" called Limited-Data Predictive Maintenance (LD-PdM). It is defined for a triple (asset or population, maintenance choice, planning horizon) by three joint conditions (lines 70–77): a consequential choice, persistently weak condition information about a decision-relevant quantity, and a material contribution from proxy, contextual, historical or prior evidence. These conditions become a yes/no/unresolved checklist with required justifications (Table 1). Section 2 describes four "asymmetries" in prose: observability, failure evidence, information cost versus decision consequence, and scale. Section 3 separates evidence, usage, exposure, condition, event probability, risk and action (Table 2, Figure 1). It also gives an elementary shared-error identity (Eq. 1), which shows that a common error term stays in a population mean but cancels in pairwise differences. Section 4 gives a five-step assessment procedure (Section 4.1) and a policy expected-loss criterion (Eq. 2). Section 5 builds a hypothetical railway-station example with an assumption register (Table 3) and a schematic (Figure 2). It then sets out a two-door, one-slot early-inspection model with gain G_i = q_i d_i v_i − k_i (Eq. 3), a reversal condition (Eq. 4) and a strict common-preference condition over a finite model set (Eq. 5). The model is evaluated with two routing interpretations (m1, m2) and a declared parameter rectangle (β, d_A) (Eq. 6, Table 4). Section 6 relates the approach to small-data PHM, usage-based maintenance, soft sensing and POMDP/value-of-information work (Table 5), outlines what a later evaluation should test, and lists limitations.

**What was found.** All results come from the stylized two-door model with hypothetical inputs:
- With equal burdens, an exposure order becomes an inspection order only if detection and response value do not offset it. Lower detection at the more exposed door (d_A < c(β)) reverses the order.
- Across the two routing interpretations, a strict common preference for door B holds exactly when β > 1/45 and d_A < c(β). In the declared rectangle, no point gives a strict common preference for door A.
- The adopted fallback (keep the existing schedule whenever no strict common preference exists) can forgo a policy that improves on the schedule under both models (B with gain 0.8 at β = 0.2, d_A = 0.9).
- Over the full declared parameter rectangle, no single policy is best everywhere.

No empirical data are used. The author describes the contribution as a "conceptual synthesis" (line 62).

**Deliverables and where they are.** (i) Applicability checklist: Table 1, p. 3. (ii) Five-step procedure: Section 4.1, p. 7. (iii) Two-door model and numerical illustration: Eqs. (3)–(6), Table 4, pp. 10–13. Secondary items are the assumption-register template (Table 3), the quantity taxonomy (Table 2) and the positioning table (Table 5).

---

## General assessment

The manuscript is careful and internally consistent about what it does **not** claim. It repeatedly says that the station is hypothetical, that no failure probabilities, costs or savings are estimated, and that the expected-loss algebra is standard (lines 534–537). The derivations in Section 5 are correct. Tables 2 and 3 usefully separate evidence from the quantities a maintenance decision needs. The limitations section (6.3) is candid.

Measured against my central questions, however, the deliverables are thinner than the title and framing suggest, and several are incomplete:

1. The title's central object, the "asymmetric relation between needs and data availability", is never defined as something a reader can apply. It is described in three non-identical ways.
2. Classifying a choice as LD-PdM has no stated consequence for the procedure that follows.
3. The criteria for that classification are mostly qualitative, and the regime's name contradicts its own definition.
4. The paper shows that the procedure's final decision step forgoes a robust improvement in its own example, but leaves the repair to the user.
5. The procedure never states which uncertainty set step 4 must use. Applied literally to the paper's own declared assumptions, it outputs "retain the schedule" in every case.
6. The quantitative example does not use the probabilistic, proxy-based evidence chain that Sections 3 and 5.2 and Figures 1–2 present as central.
7. The paper says its contribution "rests on whether the checklist and procedure make this assessment usable" (lines 535–537), but usability is not assessed.

These are fixable, but together they mean the paper does not yet deliver what its title and contribution statement promise.

---

## Required revisions (ordered from most to least important)

### 1. **The title's "asymmetry" is not defined or delivered as something a reader can apply**

*Problem.* The title promises a study of "asymmetric relations between needs and data availability" in "predictive maintenance systems." The paper never defines "needs" or "data availability" as quantities, and it never formalizes, measures or illustrates a relation between them. The asymmetry is stated in three different ways:
- "the central asymmetry is that the consequence of a maintenance choice and the availability of informative evidence need not increase together" (lines 44–47);
- "the four asymmetries" (line 96, used before the four are introduced). These are observability, failure evidence, information cost versus decision consequence, and scale (Sections 2.2–2.5), of which only the first and third are said to be "defining" (lines 96–98);
- "the title's asymmetry is the mismatch between the consequences of a choice and the information available to support it" (lines 606–607).

Each subsection 2.2–2.5 amounts to an "X does not imply Y" statement. "Asymmetry" works as a synonym for "mismatch", not as a defined property. None of the three main deliverables uses or tests it: Table 1 has no asymmetry row, and Eqs. (3)–(6) compare two doors with identical consequence parameters (v_i = 10, k_i = 1). The needs-versus-data mismatch is therefore invisible in the only quantitative result. "Systems" and "predictive" are also not matched by the content. The quantitative object is a one-shot allocation of one inspection slot between two non-interacting doors, and lines 193–196 explicitly exclude degradation trajectories and failure prediction.

*Where.* Title; abstract lines 2–5; lines 44–47, 96–103; Sections 2.2–2.5; lines 606–607.

*What to do.* Choose one of two routes:
- **(a) Define and demonstrate the asymmetry.** Give one explicit definition using quantities the paper already has. For example, set the spread of expected loss across admissible actions (what is at stake) against how informative the feasible condition channels are about the decision-relevant distinction. State the definition once in Section 2 and show it in the example, for instance with a pair of assets where consequence and informativeness move in opposite directions.
- **(b) Retitle and reframe.** Base the title and abstract on what the paper actually delivers: an applicability checklist and assessment procedure for maintenance choices under weak condition information. Present the asymmetries as motivation.

In either case, merge lines 44–47, 96–103 and 606–607 into one consistent statement, and name the four asymmetries where they are first mentioned.

### 2. **Classifying a choice as LD-PdM has no stated consequence in the procedure**

*Problem.* Step 2 says "Complete Table 1" (lines 235–237), but nothing in steps 3–5 depends on the answer. There is no branch for "no" or "unresolved." The paper itself says:
- neither outcome establishes whether an inspection order is justified (lines 83–86);
- classification and action selection are "separate judgments" (lines 250–252);
- other methods may be used inside the procedure (lines 538–542).

Steps 3–5 (trace evidence, compare policies across a model set, record and act) are generic. They would apply equally to a choice classified "no." A reader therefore cannot tell what the classification is for, or what an operator does differently after a "yes", "no" or "unresolved" answer. The regime definition is the paper's lead contribution (abstract lines 3–5; conclusions lines 602–605), so this gap is central.

*Where.* Section 2.1 (lines 81–86); Section 4.1 step 2; lines 250–255; Section 6.1 (lines 538–542).

*What to do.* State explicitly what follows from each outcome. For example: which steps become mandatory or optional; whether a "no" on criterion 2 sends the decision to conventional condition-based reasoning; how an "unresolved" answer is carried forward and when it is revisited. A flow diagram of the procedure with these branches would make this clear. If the classification has no operational consequence, say so and explain what it adds beyond steps 3–5.

### 3. **The applicability criteria are not operational, and the regime's name contradicts its definition**

*Problem.*
- **(a) Criterion 1 does not discriminate.** It asks "Could admissible actions differ in service, safety, resource use, or economic outcome?" (Table 1). Almost any maintenance choice with more than one option passes.
- **(b) Criterion 2 has no threshold or test.** It depends on "weakly informed" (line 73) and "leave a relevant condition distinction unresolved" (Table 1). Lines 101–103 rule out net information value as the measure but offer no replacement. Lines 93–95 note that dedicated measurements also need interpretation. Two assessors could therefore reach different answers for the same case.
- **(c) Only criterion 3 has an operational test**, namely showing which inference changes when the evidence changes (Table 1, column 3). "Material" (line 76) is otherwise undefined. "Therefore" at line 76 makes criterion 3 read as a consequence of criterion 2, while Table 1 treats it as independent.
- **(d) The name contradicts the definition.** The definition explicitly decouples the regime from data quantity. A few labelled samples with an informative channel are not LD-PdM, and extensive traffic records may still be LD-PdM (lines 91–93; abstract line 7). The name "Limited-Data" thus labels the regime by a property the paper says does not define it. In addition, reference [20], a companion study on the same setting, is titled "Low-Data Predictive Maintenance…". The manuscript does not say whether LD-PdM there and here are the same concept.

*Where.* Lines 70–77, 87–103; Table 1; abstract lines 3–7; reference [20].

*What to do.*
- Give each criterion an operational test with an explicit decision rule. For criterion 2, for example: after using the feasible channels, the condition distinction that would change the preferred action is still unresolved. For criterion 1: the expected-loss difference between admissible actions exceeds a declared materiality level.
- Add at least two short worked contrasts in which the checklist returns "no" and "unresolved", recorded with the justification and source that Table 1 itself requires. The one-sentence obstruction example at lines 87–90 is a start.
- Justify the term "Limited-Data" or adopt a name that matches the definition.
- State how this paper's term relates to "Low-Data PdM" in [20].

### 4. **The procedure's final step is shown to be deficient but is not repaired**

*Problem.* Step 5 applies "the documented admissible fallback" when "no common preference is supported" (lines 246–249). The example adopts retention of π0 (lines 253–254, 420–433). Section 5.4 then shows that this rule rejects π_B, which improves on the schedule by 0.8 under both routing models (lines 472–475; Table 4, row β = 0.2, d_A = 0.9). The paper concludes that "operational deployment requires an explicit rule for resolving such conflicts" (lines 478–479; also lines 254–255). The abstract (lines 12–14) and conclusions (lines 613–615) present this as a finding.

The procedure, however, is itself a declared deliverable (line 57). If its own example shows that its decision step forgoes a robust improvement, and the needed rule is left to the user, the deliverable is incomplete. Step 4 already asks the operator to check "separately whether a policy improves on the reference schedule" (lines 243–245), but step 5 never uses that check. Likewise, "request further information only when it can usefully arrive before the decision deadline" (lines 248–249) gives no criterion for "usefully." Lines 431–433 add that no information-value figure is computed without its observations, likelihoods, burden and resulting actions, and the example computes none.

*Where.* Section 4.1 steps 4–5; lines 250–255, 420–433, 472–479; Table 4 "Both models" column; abstract lines 12–14; conclusions lines 613–615.

*What to do.* Revise step 5 so that it uses the step-4 robust-improvement check:
- If one or more policies improve on the reference under every model in the set, select among them by a declared rule, such as maximin gain, minimax regret or an operator-declared priority. The paper names such rules at lines 476–477 but adopts none.
- Fall back to the reference schedule only if no policy robustly improves on it.

Recompute the last column of Table 4 under the revised rule and update the abstract and conclusions. For instance, from the Table 4 entries, a maximin-gain rule would select B in all three β = 0.2 rows and in the β = 0.5 row, and would retain π0 only at β = 0 and β = 1/45. The procedure's output therefore depends heavily on this choice, which is why the procedure must specify it. Also give at least a qualitative criterion for when an information request (such as the counting exercise at lines 431–433) is worth making.

### 5. **The uncertainty set used in step 4 is never specified, and the example applies it inconsistently**

*Problem.* Step 4 requires preference "throughout the model set" (lines 244–245). Eq. (5) defines this over "a declared nonempty finite set M of plausible models", with an extension to compact parameter sets (lines 415–416). The paper never says how M is built, what makes a model "plausible", or how structural uncertainty (routing) and parameter uncertainty (β, d_A, v_i, k_i) are to be combined.

In the example, the "Both models" column of Table 4 applies the rule across routing interpretations only, with (β, d_A) held fixed. Yet β and d_A are no better determined by the evidence than the routing is. They are "not … elicited uncertainty bounds" (lines 449–450), and "passenger records alone supply no observations of the targeted condition or inspection sensitivity" (lines 586–589). Applying Eq. (5) to the full declared set {m1, m2} × [0, 0.5] × [0.25, 0.9] is what step 4 literally asks for. It gives no common preference and no robust improvement (lines 483–486), so for the paper's own example the procedure's output would be "retain π0" in every case. The reader cannot tell which output is intended.

*Where.* Section 4.1 step 4; Section 4.3 (lines 284–289); Eq. (5) and lines 412–419; Section 5.4 (lines 442–451, 480–486); Table 4 caption.

*What to do.*
- In Section 4.1, specify how the model set is formed: which quantities may be fixed, which must be varied, and who declares the set.
- Report the procedure's actual output for the example under that specification.
- Add a figure of the (β, d_A) plane showing, for m1, for m2 and for the common set, the regions bounded by c(β), d_A = 1/(1+10β) and β = 1/45. The subsection title promises "continuous decision boundaries" (line 441), but the paper presents them only in prose and as six table rows.

### 6. **The quantitative example does not use the probabilistic, proxy-based evidence chain that the framework emphasizes**

*Problem.* Several parts of the paper present a chain from passenger flow through routing, device use, exposure, condition and event probability to action, with uncertainty carried explicitly throughout. These are Sections 3.1–3.3 and 5.2, Figure 1 ("Belief updating", "Uncertainty propagation"), Figure 2 ("Uncertainty is retained through the reasoning chain"), Table 3, and the keyword "Bayesian inference."

Section 5.4 collapses this chain:
- each routing model assigns fixed point exposures (x_A, x_B) (lines 443–444);
- q_i is a deterministic linear function of x_i (line 446);
- uncertainty appears only as a two-element scenario set plus a parameter rectangle.

No passenger quantity, prior, likelihood, posterior or exposure distribution appears. This conflicts with line 402–403, which says "the condition probability must account for the exposure distribution." Equation (1), the paper's only formal treatment of proxy error, is not used in the example. Moreover, the m1/m2 discrepancy is a group-specific allocation error, which is exactly the case Eq. (1) does not cover (line 221). The paper says the companion study [20] develops "a particular Bayesian proxy-flow model" for the same setting (lines 359–361), but does not explain why it is not used to instantiate even one link.

*Where.* Sections 3.2–3.4, 5.2, 5.4; Figures 1–2; Table 3; keywords; lines 359–366, 399–403, 442–451.

*What to do.* Choose one of two routes:
- **Instantiate at least one link probabilistically.** For example, derive a routing-share distribution from counts, propagate it to an exposure distribution and then to q_i. The example would then show how evidence and its uncertainty reach the decision.
- **Describe the example accurately.** Present it as a scenario-based sensitivity analysis of the final decision link only, and adjust the captions of Figures 1–2, Section 3.2, the keywords and the abstract to match.

In either case, state why the companion study's model is not used here.

### 7. **The procedure is never shown as a complete, documented application**

*Problem.* The procedure's stated output is "a documented action rationale or an unresolved comparison with a specified fallback" (lines 229–230). Table 1 requires each answer to be recorded "with the justification and its source" (line 82). In Section 5:
- the five steps are spread over Sections 5.1–5.4 without being labelled;
- the Table 1 answers appear in one paragraph as "three conditional affirmative answers" (lines 308–316), without the justification fields Table 1 requires;
- the final action record is described only in prose (lines 424–427).

A reader who wants to apply the procedure has no template showing what a completed output looks like.

*Where.* Section 4.1; Sections 5.1–5.4; lines 82, 229–230, 308–316, 424–427.

*What to do.* Add a compact, completed procedure record for the station example, for instance a table with steps 1–5 as rows and columns for inputs, assumptions and output. It should include:
- a completed Table 1 with the required justification fields;
- the assumption register (Table 3), linked to the step that uses it;
- the declared model set;
- the comparison result;
- the selected action or fallback;
- the triggers for reconsidering the decision.

Cross-reference each entry to the section where it is derived.

### 8. **The claims of practicality and usability are not supported by any evaluation**

*Problem.* The Introduction calls the outputs "three practical outputs" (line 56). The Discussion says "the contribution rests on whether the checklist and procedure make this assessment usable" (lines 535–537). The manuscript contains no evaluation of usability or decision benefit: no application to a documented case, no comparison with an existing practice, and no practitioner assessment. Section 6.2 lists what a later evaluation should establish but explicitly is "not a committed experimental programme" (line 554). By the paper's own criterion, therefore, the contribution is not yet demonstrated.

The analytical "findings" in the conclusions (lines 609–612) also follow directly from how Eq. (3) is defined. Because G_i = q_i d_i v_i − k_i, it is true by construction that turning an exposure order into an inspection order requires assumptions about detection, response value and burden.

*Where.* Lines 56–63, 535–537, 548–575, 608–620.

*What to do.* Choose one of two routes:
- **(a) Add a minimal evaluation.** For example, apply the checklist and procedure to a second, structurally different decision, such as an elevator or escalator choice. Lines 333–339 argue that these assets differ in mechanism, so this would test whether the procedure transfers beyond the two-door case. In addition, or instead, quantify over the declared parameter set how often naive exposure ranking picks a different action than the procedure, and what expected loss that difference causes. This would show the procedure's value within the example itself.
- **(b) Revise the claims.** Replace "practical" with an accurate term such as "proposed", and state in the abstract and conclusions that usability and decision benefit are untested.

In both cases, present the Section 5.4 results as illustrations of how the model is structured rather than as findings.

### 9. **Population- and system-level scope is claimed more strongly than it is delivered**

*Problem.* The title ("Systems"), Section 2.5 ("Asymmetry of scale"), Section 3.4, Section 5.5 and the abstract sentence "A shared-error calculation separates aggregation uncertainty from pairwise ranking" (lines 14–15) all present population scale as part of the contribution. The only formal content is Eq. (1), an elementary variance identity with independent errors. The only quantitative example has n = 2 assets with no interaction: cross-door effects are assumed negligible or absorbed into the losses (lines 395–396). Station topology and redirection (lines 325–332) and coordinated maintenance (lines 280–283, 507–509) are discussed only in prose. Section 5.1 introduces elevators and escalators, but only doors are modelled.

*Where.* Title; abstract lines 14–15; Sections 2.5, 3.4, 5.5; lines 395–396.

*What to do.* Choose one of two routes:
- **Connect Eq. (1) to the example.** For example, show that adding a shared offset B leaves the Table 4 ordering unchanged, while the m1→m2 allocation error changes it. Add one population-level illustration.
- **Reduce the claims.** Make population and system claims less prominent in the title and abstract, and state explicitly that the quantitative scope is a pairwise comparison of non-interacting assets.

In both cases, say at the start of Section 5 that only doors are modelled.

### 10. **The reproducibility statement points to a location readers cannot access**

*Problem.* The Data Availability Statement says the Python calculation and its generated results are "included with the manuscript source" (lines 628–630). Lines 486–488 say the results are generated "from a single input file." Readers of the published article will not have access to "the manuscript source."

*Where.* Lines 486–488, 628–630.

*What to do.* Deposit the script and input file as Supplementary Material or in a public repository with a persistent identifier, and cite it. For the record, I independently recomputed Eq. (6), all Table 4 entries, the boundaries c(β), 1/(1+10β) and β = 1/45, and the stated gain ranges (−0.75 to 4.4 for A; −0.1 to 2.15 for B). All are correct. The problem is accessibility, not correctness.

---

## Minor issues (ordered by importance)

1. **Parameter design shapes the headline results.** Only d_A varies while d_B = 0.9 is fixed, and m2 changes only x_A (lines 443–447). Statements such as "No point in the declared rectangle gives a strict preference for A under both interpretations" (lines 460–461) are therefore direct consequences of the chosen design. Say so, and give at least a qualitative physical reason why two doors of the same type would differ in detection probability. Lines 399–401 justify only the exposure difference.
2. **Several key terms are undefined.** "Condition-sensitive channel" (lines 73, 235), "admissible" (used for actions, schedules and fallbacks; lines 8, 233, 247, 258, 429), "plausible model" (lines 241, 284, 379), "information budget" (line 41), "mechanism" in step 1 (line 232), "consequence-based requirement" (line 249) and "consequence-based choice" (line 59) are used without definition. Line 378 distinguishes a "reference inspection" from the "actual inspection" (line 381) without explaining either. Define these at first use or add a short glossary.
3. **Notation in Eq. (1).** The symbol x̄ and the mean of the estimates x̂ are not defined. State that they are averages over the n assets. It would also help to give the pairwise error variance (2σ_ε²), because the argument at lines 219–225 depends on comparing it with the variance of the mean.
4. **Unused or incomplete notation in Eqs. (2) and (6).** π*_m (Eq. 2) is defined but never used, and the evidence E is never instantiated in the example. G_B in Eq. (6) has no model index; state that it is the same under m1 and m2 because x_B is unchanged.
5. **Cross-reference.** The Introduction points to Section 5.3 for the "worked two-door inspection comparison" (lines 57–58). Section 5.3 is titled "symbolic"; the worked numbers are in Section 5.4.
6. **Figure 1.** The label "Weak or unavailable condition-sensitive channels" floats above the inference block without any arrow, so its role is unclear. "Failure-event records" appears as an input although the example uses none. Consider drawing the weak channels as a greyed or absent input, and adding the decision node the caption refers to.
7. **Figure 2** has no feedback from inspection findings to beliefs, although Table 3 (column 3) and lines 426–427 rely on findings to revise the assessment.
8. **Table 4.** The column header "m1/m2" can be misread as a ratio; consider "Best under m1 / m2." Explain why these six (β, d_A) points were chosen. Once required revision 4 is addressed, add a column showing the outcome under the revised selection rule.
9. **The abstract overstates where the separation is made.** "The checklist separates weak condition information from small sample count" (abstract line 7), but Table 1 has no item about sample count. The separation is made in the text (lines 91–93) and in Table 5. Adjust the wording.
10. **Keywords.** "Bayesian inference" and "risk-based maintenance" describe nothing performed in the paper, and "partial observability" appears only through cited POMDP work. Align the keywords with the actual content, or see required revision 6.
11. **Table 2** defines "Risk" and "Event probability", but neither is used in the formal part (Section 5.3 deliberately avoids event probabilities, lines 193–196). Either connect them to the example or note that they are included only for completeness.
12. **False-positive extension (lines 393–394).** State that h_i ≥ 0. Note also that, with false positives, the observed positive-finding rate identifies q_i d_i + (1 − q_i) f_i, not q_i d_i (compare lines 589–590).
13. **Density of disclaimers.** I count about 30 instances of "does not / do not", 11 of "need not", and 14 of "hypothetical." Many sentences say what something is not, which makes the positive deliverables harder to extract. Gathering the scope disclaimers into one paragraph (for example in Section 1 or 6.3) and cutting the repetition elsewhere would improve readability without weakening the paper's caution.
14. **Back matter.** The Funding statement names a project (FP3-IAM4Rail) but gives no grant agreement number. The template's placeholders (Received/Revised/Accepted, DOI) are expected at this stage. Check whether an Author Contributions statement is required for a single-author submission.

---

## Recommendation

**Major revision.**

The manuscript is careful, honest about its limits, and mathematically correct. Every reported number checks out. It does not reach the threshold for rejection. But the deliverables, read strictly from the paper, are thinner than the title and contribution statement suggest:
- the title's central concept is not defined in a form a reader can apply;
- classification as LD-PdM has no stated effect on what the operator does next;
- the criteria and the regime's name do not match;
- the paper shows the procedure's decision step is deficient but leaves the fix to the user;
- the uncertainty set is unspecified, so the procedure's output for the paper's own example is ambiguous;
- the quantitative example does not use the evidence chain the framework is built around;
- usability, which the paper names as the basis of its contribution, is not assessed.

All of these can be addressed with the material already in the paper, chiefly by revisions 1–7, without new empirical data. The required changes go beyond editing, however, and the revised version should be reviewed again.

---

## MDPI evaluation grid

| Criterion | Rating | Comment |
|---|---|---|
| Originality / Novelty | Average | The paper itself says the ingredients are established (lines 534–537). The novelty lies in framing a decision-specific applicability test, which is plausible but not yet operational. |
| Significance of Content | Low | As submitted, the deliverables are a qualitative three-row checklist, a procedure with an incomplete final step, and an elementary two-asset calculation. Their value to practice is not demonstrated. Revisions 2–5 and 8 could raise this rating. |
| Quality of Presentation | Average | Well structured, with useful tables (Tables 2–3). The text is dense and heavy with negations, the deliverables are scattered across sections, and the decision regions are not shown in a figure. |
| Scientific Soundness | Average | The derivations and numbers are correct and the claims carefully hedged. The core classification is not operational, and the procedure's uncertainty set and decision rule are underspecified. |
| Interest to the Readers | Average | Of interest to maintenance-planning readers if the procedure is completed and demonstrated. The link to the journal's symmetry theme currently rests only on the undefined word "asymmetry." |
| Overall Merit | Average | Coherent and cautious conceptual work whose promised deliverables are only partly delivered. |
| English Language | English is fine; no language issues detected | Grammar and terminology are precise. The readability problems are about density and structure (Minor issue 13), not language. |
