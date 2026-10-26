# Review Report — Reviewer 1 (domain expert in predictive maintenance)

- **Manuscript:** *Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems*
- **Journal:** *Symmetry* (MDPI)
- **Version reviewed:** "Version October 25, 2026 submitted to Symmetry" (18 pages, line-numbered PDF)

---

## 1. Summary of the submission

The manuscript proposes a named maintenance regime, *Limited-Data Predictive Maintenance* (LD-PdM). A maintenance choice falls into this regime when three conditions hold together (lines 70–77, Table 1):

1. the choice is consequential;
2. a decision-relevant condition quantity stays weakly informed by the feasible condition-sensitive channels, because of persistent deployment, access or acquisition constraints;
3. proxy, contextual, historical or prior evidence makes a material contribution to the assessment.

The author describes four "asymmetries" (observability, failure evidence, information cost versus decision consequence, and scale; Sections 2.2–2.5). The paper also separates evidence, usage, exposure, condition, event probability, risk and action (Table 2, Figure 1). A simple additive shared-error model (Eq. 1) shows that a common error component inflates the error of a population mean but cancels in pairwise differences.

Section 4 sets out a five-step assessment procedure that starts from a reference schedule and ends either in a documented action or in a fallback. Policies are compared through model-indexed expected loss (Eq. 2).

Section 5 works through a hypothetical railway station. Two doors, A and B, compete for one optional early-inspection slot. The gain of inspecting door *i* is G_i = q_i·d_i·v_i − k_i (Eq. 3), where q_i is the probability of an actionable condition, d_i the detection probability, v_i the net value of the response and k_i the inspection burden. This gives a reversal condition (Eq. 4) and a strict common-preference condition over a model set (Eq. 5). The numerical part uses two routing interpretations (m1, m2), a linear condition model q_i = 0.1 + βx_i, and sweeps over β and d_A (Eq. 6, Table 4). The main reported findings are:

- the exposure order can be reversed by lower detection at the more exposed door;
- routing ambiguity can prevent a strict common preference;
- the adopted fallback (keep the existing schedule) can forgo an inspection that improves on that schedule under both models.

The author describes the work as a conceptual synthesis that organises established small-data PHM, usage-based maintenance, soft sensing and decision analysis (lines 61–63, 530–537). No empirical data are used.

## 2. General assessment

**Strengths**

- The paper is unusually careful about what it does and does not claim. It distinguishes measured, inferred and assumed quantities (Tables 2 and 3). It warns against reading exposure as condition, or a service threshold as a failure probability. It states its limitations explicitly (Section 6.3). This epistemic discipline is commendable and, sadly, uncommon in the PdM literature.
- The core practical message is correct and relevant to infrastructure maintenance: an exposure or usage ranking is not an inspection priority. The step from one to the other needs explicit assumptions about the actionable condition, detection, response value and inspection cost. The insistence on comparing complete inspection-and-response policies against a reference schedule (Section 4.2, Eq. 3) is sound decision practice.
- The author correctly positions the work against Li et al. (2024) [4] and does not claim novelty for data scarcity, sensor cost or uncertainty as such.
- The algebra in Section 5 is correct. I recomputed every entry of Table 4, the boundary c(β), the thresholds β = 1/45 and d_A = 1/(1+10β), and the ranges −0.75 to 4.4 (for G_A) and −0.1 to 2.15 (for G_B). All agree with the manuscript.

**Weaknesses**

From the standpoint of maintenance engineering and PHM, the contribution is currently thin and not well positioned.

1. **The central idea is already embedded in established maintenance frameworks that the paper does not discuss.** The idea is a mismatch between the consequence of a failure mode and the feasibility of observing its condition, with a fallback to indirect evidence or time/usage-based tasks when condition monitoring is not feasible. It appears in:
   - the RCM task-selection logic (technical feasibility of on-condition tasks, the P-F interval);
   - FMECA's separate severity and detectability ratings;
   - risk-based inspection;
   - delay-time inspection models;
   - published frameworks for selecting *suitable and feasible* PdM approaches given the available data.

   None of these is cited. The added value of LD-PdM over them is never stated.
2. **The deliverables are generic.** The checklist and the five-step procedure amount to decision-analysis hygiene: specify the decision, check applicability, trace evidence, compare alternatives, record. The paper itself says the contribution "rests on whether the checklist and procedure make this assessment usable" (lines 535–537), yet it provides no evidence of usability: no real case, no practitioner involvement, and no comparison with what an RCM/RBI analysis would have produced.
3. **The worked example is algebraically trivial and leaves out the features the paper calls central to LD-PdM.** The comparison is a one-shot, single-slot expected-value comparison of two doors. It does not include:
   - the value of acquiring information (e.g., a counting exercise);
   - learning the exposure-to-condition relation from inspection outcomes;
   - population-level pooling.
4. **The decision rule built into the procedure is defective.** It selects a policy that is strictly dominated under every model in the set (see Required revision 2). The paper then presents this self-imposed cost as a finding (abstract lines 12–14; Conclusions lines 612–615).
5. **The station premise needs a practitioner reality check.** Modern door operators, lift controllers and escalators often already log cycles, trips or run-hours and fault codes, and OEM remote monitoring is commercially available for lifts and escalators. The binding constraint is often access to data held by contractors, not its absence. The regulatory inspection regime for these devices also shapes the "existing schedule".

I think the framing can become a useful short position paper or a methodological note, but only if it is anchored in the maintenance-engineering literature and backed by a non-trivial demonstration. The present manuscript needs major revision.

## 3. Required revisions (ordered from most to least important)

### 1. **Position LD-PdM against established maintenance-engineering decision frameworks and state the added value precisely**

**Problem.** The manuscript positions itself mainly against small-data PHM [4], usage-based maintenance [8], soft sensing [9] and POMDP/VoI [5,6] (Table 5; Section 6.1). The closest existing frameworks are absent:

- **RCM task-selection logic.** It asks whether an on-condition task is technically feasible: is there a detectable potential failure, and is the P-F interval long and consistent enough? If not, it falls back to scheduled restoration or discard, failure-finding, or redesign, depending on the consequence category. This is very close to criteria 1 and 2 of Table 1 and to the "keep the schedule" fallback of Section 4.1. References: Nowlan & Heap, *Reliability-Centered Maintenance*, United Airlines report for the US DoD, 1978; Moubray, *Reliability-Centred Maintenance*, 2nd ed., Butterworth-Heinemann, 1997; SAE JA1011; IEC 60300-3-11:2009.
- **FMECA.** Its separate severity (S) and detection (D) ratings (IEC 60812:2018) already encode "high consequence, poor observability" at the failure-mode level. This is exactly the "central asymmetry" of lines 44–47.
- **Frameworks for choosing whether and how to do PdM given data availability:**
  - Tiddens, Braaksma & Tinga, "Selecting suitable candidates for predictive maintenance", *Int. J. Prognostics and Health Management* 9(1), 2018 (doi:10.36001/ijphm.2018.v9i1.2699);
  - Tiddens, Braaksma & Tinga, "Exploring predictive maintenance applications in industry", *J. Quality in Maintenance Engineering* 28(1):68–85, 2022;
  - da Silveira, Meghoe & Tinga, "Quantifying the suitability and feasibility of predictive maintenance approaches", *Computers & Industrial Engineering* 194:110342, 2024.

  These are direct competitors to the applicability checklist (Table 1), and they come from the same group as Tinga [8], whom the paper already cites.
- **Risk-based inspection and maintenance:**
  - Khan & Haddara, "Risk-based maintenance (RBM)…", *J. Loss Prevention in the Process Industries* 16(6):561–573, 2003;
  - Straub & Faber, "Risk based inspection planning for structural systems", *Structural Safety* 27(4):335–355, 2005;
  - API RP 580/581.
- **Delay-time inspection modelling.** Its imperfect-inspection variants are the natural home for the q·d·v − k structure of Eq. 3:
  - Christer & Waller, *J. Oper. Res. Soc.* 35:401–406, 1984;
  - W. Wang, "An overview of the recent advances in delay-time-based maintenance modelling", *Reliability Engineering & System Safety* 106:165–178, 2012.
- **Covariate- and usage-driven reliability prediction.** This is the statistical counterpart of "usage proxies":
  - Jardine, Lin & Banjevic, *Mechanical Systems and Signal Processing* 20(7):1483–1510, 2006;
  - Hong & Meeker, "Field-failure predictions based on failure-time data with dynamic covariate information", *Technometrics* 55:135–149, 2013.
- **Maintenance-optimisation reviews:** de Jonge & Scarf, *EJOR* 285(3):805–824, 2020.

**Where.** Introduction (lines 32–63), Section 2.1 (lines 70–103), Section 6.1 and Table 5 (lines 522–546).

**What to do.**
- Add these families to the Introduction and to Table 5.
- For each family, state concretely what LD-PdM adds. For example: probabilistic use of heterogeneous indirect evidence to *prioritise within a population*, rather than RCM's fixed-interval fallback; or explicit model-set robustness, which is absent from standard RBI.
- If the honest answer is that LD-PdM is a re-description of the RCM "on-condition task not feasible" branch enriched with Bayesian proxy reasoning, say so. Then narrow the novelty claim accordingly.
- The current bibliography (23 items) is thin for a paper whose stated contribution is a synthesis. Several entries are only tangential to the claims they support (see Minor issue 7).

### 2. **Replace the fallback rule: it selects strictly dominated actions**

**Problem.** Step 5 (lines 246–249) and the example (lines 424–429, 472–479; Table 4) adopt the following rule: if no policy is strictly preferred to *all* alternatives under *every* model, retain π0. I recomputed Table 4. In three of the four rows marked with a dagger, π0 is *strictly dominated under both routing models by both A and B*:

| β | d_A | Result |
|---|---|---|
| 0.2 | 0.9 | G_A = 1.7 / 0.53, G_B = 0.8 / 0.8 |
| 0.2 | 0.6 | G_A = 0.8 / 0.02, G_B = 0.8 / 0.8; B is optimal, weakly, under both models |
| 0.5 | 0.9 | G_A = 4.4 / 1.475, G_B = 2.15 / 2.15 |

A rule that picks a dominated action violates admissibility. Such a rule would not survive review by a maintenance planner, and certainly not by a decision analyst. The paper acknowledges the cost for one row (lines 472–479) and calls it a finding (abstract lines 12–14; lines 612–615). But the cost is a property of the chosen rule, not of LD-PdM. It is also an established property of unanimity-type rules under model ambiguity.

**What to do.**
- At minimum, step 4/5 must exclude any policy that is strictly dominated across the model set. The paper already computes the needed check: "whether a policy improves on the reference schedule throughout the model set" (lines 243–245).
- Then declare an explicit criterion for choosing among the non-dominated policies, and show what each criterion yields in Table 4. Candidate criteria:
  - maximin expected gain (Gilboa & Schmeidler, *J. Math. Econ.* 18:141–153, 1989);
  - minimax regret (Savage, *JASA* 46:55–67, 1951);
  - a weighted or Bayesian model average (Hoeting et al., *Statistical Science* 14:382–417, 1999);
  - an info-gap robustness criterion (Ben-Haim, *Info-Gap Decision Theory*, 2nd ed., Academic Press, 2006).
- My recomputation shows that the criteria disagree, which is informative. At β = 0.2, d_A = 0.9:
  - maximin selects B;
  - minimax regret selects A (regret 0.27 versus 0.9);
  - Bayesian averaging selects A if the weight on m1 exceeds 3/13 ≈ 0.23.

  Showing this would turn a self-inflicted limitation into a genuine illustration of how the operator's attitude to ambiguity enters an LD-PdM decision.
- Revise the abstract and Conclusions accordingly.
- The sentence "B does not acquire priority merely because A's rationale failed" (line 425) should be reconsidered. Under m2, B can be preferred on its own merits.

### 3. **Demonstrate the checklist and procedure on a non-hypothetical case and show that they discriminate**

**Problem.** Everything in Sections 4–5 is hypothetical (lines 62–63, 292–316, 548–553). The checklist is only ever applied to a case built to answer "yes" three times (lines 308–316). The "no" and "unresolved" outcomes appear only as hypotheticals (lines 87–95, 312–316). By the paper's own admission (lines 535–537), its value depends on usability, which is untested. The companion study [20] (Bauer & Baranowski, GPECOM 2026; also arXiv:2603.14384) already has a simulated case built on a real station layout. The present paper deliberately reproduces nothing from it (lines 362–366).

**What to do.** Provide at least one of the following:

- (a) A retrospective application of Table 1, the five steps and the assumption register (Table 3) to a real station asset population. The IAM4Rail funding (lines 621–625) suggests such access may exist. Use real record types, real gaps and the real inspection regime, even if the numbers are anonymised.
- (b) An application to the case of [20], with a clear statement of what the procedure changes relative to [20]'s scheduler.
- (c) A structured walk-through with maintenance planners or engineers (even a small number), reporting whether the checklist gives consistent classifications across assessors and what it changes in their recommendations.

In addition, show three contrasting cases side by side:

- an LD-PdM case;
- a small-data-but-observable case (lines 91–92);
- a critical asset with justified dedicated monitoring.

Showing the checklist produce different answers would show that it discriminates.

### 4. **Make the definition operational and resolve the endogeneity of the "acquisition constraint"; reconsider the terminology**

**Problem (a): the criteria are qualitative.** "Consequential", "weakly informed" and "material contribution" (lines 72–77; Table 1) have no operational test. Two analysts could reach different classifications for the same asset. Table 1 asks for justification but gives no criterion for when the justification suffices.

**What to do (a).** Give a decision-theoretic operationalisation that is consistent with the paper's own Eq. 2. For example:

- (i) consequential: the expected-loss range across admissible actions exceeds a stated materiality level;
- (ii) weakly informed: the expected value of perfect information about the condition variable, *given the feasible condition channels*, stays material;
- (iii) material indirect evidence: including the proxy, context or history evidence changes the optimal action or its expected loss by a material amount.

This makes "applicability" checkable and connects directly to [5,6].

**Problem (b): LD-PdM status is endogenous to the monitoring-investment decision.** Section 2.4 (lines 137–139) makes applicability conditional on better information not being obtainable "within the operator's feasible resources". That is itself a value-of-information decision. Lines 101–103, however, say that low net information value is not a measure of weak observability. These statements are in tension.

**What to do (b).** Treat "install or acquire better condition information" as an admissible action within the decision (as in Srinivasan & Parlikad [5] and Memarzadeh & Pozzi [6]), rather than as a precondition for classification. Alternatively, explain precisely how the two are separated.

**Problem (c): the terminology.**
- The paper's own definition is about weak *condition observability*, not about limited *data*. By lines 91–95 and Table 1, a data-rich setting can be LD-PdM and a small-data setting need not be. "Limited-Data" therefore invites exactly the confusion with small-data PHM [4] that the paper tries to avoid.
- EN 13306:2017 defines *predictive* maintenance as condition-based maintenance carried out following a forecast derived from the analysis and evaluation of significant parameters of the item's degradation. A regime defined by weak condition channels sits awkwardly under that label unless the author explains how proxy-based inference satisfies it.
- The companion paper [20] uses "Low-Data Predictive Maintenance" for apparently the same idea.

**What to do (c).** Justify the name against EN 13306, harmonise it with [20], or adopt a term that matches the definition.

### 5. **Extend the worked example to exercise the elements that define LD-PdM: information acquisition, learning, and population scale**

**Problem.** The paper's distinctive claims concern:
- when to acquire evidence instead of acting (Figure 2, "seek better evidence"; step 5, lines 248–249; lines 273–275, 431–433, 500–501);
- the role of populations (Sections 2.5 and 5.5).

The example evaluates none of these. Its only uncertainty is a static choice between m1 and m2 plus parameter sweeps. Lines 431–433 decline to compute any information value, although every ingredient is available.

**What to do.**
- (a) Add the routing-resolution action, such as a short passage count or reading door-controller cycle counters, as a policy. Compute its value. For example, at β = 0.2 and d_A = 0.9, the expected value of perfect routing information is 0.9w for w ≤ 3/13 and 0.27(1 − w) above, where w is the weight on m1. Its maximum is about 0.21 loss units, about one fifth of one inspection burden. This immediately tells the planner how much a counting exercise may cost. Such a result would be far more useful to practitioners than the current fallback discussion.
- (b) Inspections are the main source of condition data in this regime, so show how an inspection outcome updates β (or q). Show how this changes the value of inspecting the more *informative* rather than the more *exposed* door (the exploration/exploitation trade-off).
- (c) Scale the example to n doors with partial pooling of β. This would show the population-level asymmetry (aggregate decision value versus per-unit sensing cost) that the abstract and Section 2.5 present as central.

### 6. **Strengthen the engineering justification and presentation of the two-door model**

**Problem.**
- (a) **The reversal is driven by detection.** The only reversal mechanism is lower d_A at the more exposed door (lines 446–448; Table 4; Conclusions lines 610–612). The doors are of the same type on alternative routes, so the paper must explain why one inspection procedure would have such different detection probabilities (0.25–0.9). If anything, more advanced wear tends to be *more* detectable. Meanwhile v_i is held equal, although the paper stresses that consequences depend on function and alternatives (lines 296–299). An accessibility-critical door or lift is the obvious practical source of reversal, and it ties directly to the title's "needs".
- (b) **v_i is a black box.** v_i absorbs the timing benefit of early versus scheduled inspection, response effectiveness and disruption (lines 382–386). A simple delay-time formulation would derive v_i from the defect-arrival rate, which depends on exposure, and from the time to the next scheduled inspection. That would make "early inspection" meaningful and connect to the established literature.
- (c) **The nonlinearity warning is untested.** Lines 402–404 warn that ordering mean exposures need not order q_i under a nonlinear relation. Section 5.4 then uses a linear q_i with point exposures under each model, so the warning is never exercised.
- (d) **Narrative inconsistency.** Lines 420–423 state that dated records *show* the reassignment was in force, which appears to refute m1. Lines 469–471 nevertheless keep both models "plausible". Clarify the evidential status of m1.
- (e) **Uncertainties are treated asymmetrically.** Routing is a model set subject to the robustness rule, while β and d_A are swept as parameters outside it (lines 480–486). Justify this, or treat all epistemic uncertainties consistently.
- (f) **No figure for the "continuous decision boundaries".** Section 5.4 is titled "continuous decision boundaries", yet only six points are tabulated.

**What to do.**
- Motivate or replace the detection asymmetry. A consequence asymmetry is preferable.
- Derive or bound v_i from an explicit inspection model.
- Use a nonlinear q, or an exposure distribution, if the warning is to be retained.
- Fix the m1/m2 narrative.
- Add a 2-D decision-region figure over (β, d_A). It should mark c(β), d_A = 1/(1+10β) and β = 1/45, label the optimal policy under m1, under m2 and under the chosen robust rule, and shade the region where π0 is dominated.

### 7. **Reality-check the station premise against current practice, regulation and organisation**

**Problem.**
- **Usage may already be recorded.** The canonical proxy chain from passenger counts to device cycles (lines 318–339) assumes that device usage is unknown. Many automatic door operators record cycle counts and fault codes. Lift controllers log trips or starts and door cycles. Escalators have run-hour and fault logs. The major lift and escalator OEMs sell remote-monitoring services commercially. Condition-related signals can also be extracted from signals the drive already has, for example motor current for railway door systems (Shimizu, Perinpanayagam, Namoano & Starr, *IEEE Access* 11:28724–28734, 2023). Field-defect records have also been used to model in-service lift reliability (Q. Wang et al., *Proc. IMechE Part O: J. Risk and Reliability* 238(6):1271–1286, 2024).
- **The binding constraint is often organisational.** It is frequently *data access* (data held by maintenance contractors or OEMs, multi-vendor legacy fleets, contractual ownership) rather than physical absence of channels. This information asymmetry between stakeholders is highly relevant to the paper's thesis but is not discussed.
- **The existing schedule is regulated.** For lifts, escalators and powered pedestrian doors it is largely set by regulation and standards: statutory periodic inspections, maintenance instructions per EN 13015, and safety requirements per EN 81-20, EN 115-1 and EN 16005. The manuscript treats it abstractly ("mandatory requirements", lines 233, 376–377).

**What to do.**
- Justify, for the station example, why controller counters and OEM data are unavailable or unusable. Otherwise the routing ambiguity at the heart of Section 5.4 could be resolved cheaply. Note that this would remove the usage uncertainty but not the condition uncertainty, which is worth saying explicitly.
- Discuss organisational data access as a source of persistent weak observability.
- Describe how the early-inspection slot interacts with the regulatory and contractual inspection regime.

### 8. **Model allocation (routing) errors properly in Section 3.4**

**Problem.** Eq. 1 models a shared *additive* error B that cancels in pairwise differences. In a station, the dominant error is usually *allocation* under flow conservation: a fraction p of a known flow goes to route A and 1 − p to route B. An error in p induces *perfectly negatively correlated* errors between the two devices. These errors leave the total untouched but *amplify* the pairwise difference: Var(x̂_A − x̂_B) = 4N²·Var(p̂), with N the total flow. This is the opposite of the case formalised in Eq. 1, and it is exactly the m1/m2 situation of Section 5.4. The text states it only verbally (lines 221–223). As written, the formal result (lines 219, 506–507: "a shared source can leave total burden uncertain even when a pairwise contrast is stable") may mislead readers about which case is typical.

**What to do.**
- Add the allocation-error model next to Eq. 1, or replace Eq. 1 with it.
- State which structure is expected for each evidence source.
- Link the result explicitly to m1/m2.

### 9. **Ground the treatment of maintenance-censored and intervention-affected records in the reliability literature**

**Problem.** Section 2.3 (lines 117–131) and lines 352–354 and 434–440 raise the right issues: preventive replacement censors lifetimes, inspections triggered by suspected deterioration make the observation process informative, and service may not restore the asset to as-new condition. The only citation, however, is a general interval-censoring paper [10].

**What to do.** Cite and briefly discuss the maintenance-specific literature:

- On *dependent competing risks* between failure and preventive maintenance and their non-identifiability:
  - Cooke & Bedford, "Reliability databases in perspective", *IEEE Trans. Reliability* 51(3):294–310, 2002;
  - Bunea & Bedford, "The effect of model uncertainty on maintenance optimization", *IEEE Trans. Reliability* 51(4):486–493, 2002. This paper shows the optimisation consequences, which matter directly for LD-PdM.
- On *imperfect repair*:
  - Kijima, *J. Applied Probability* 26:89–102, 1989;
  - Doyen & Gaudoin, *RESS* 84:45–56, 2004.

State what modelling choice the procedure would recommend in each case.

### 10. **Clarify the meaning of "asymmetry" and the fit with the journal**

**Problem.** "Asymmetry" is used throughout as a synonym for "mismatch" or "need not increase together" (lines 44–47, 96–103, 606–607). The four "asymmetries" of Sections 2.2–2.5 have different logical types: an observability gap, a censoring problem, a cost/benefit distinction, and a pooling opportunity. None is formalised. For a submission to *Symmetry*, readers will expect the central notion to be defined precisely.

**What to do.** Either formalise the central asymmetry, or present "asymmetry" explicitly as an informal descriptor and let the editor judge scope. One way to formalise it: define a consequence ordering and an achievable-information ordering over choices or assets, for example by expected loss of a wrong action and by attainable posterior precision or detection power. The asymmetry is then the lack of comonotonicity between the two orderings, which could be shown as a 2-D consequence × observability map.

### 11. **Reduce hedging and improve readability**

**Problem.** Almost every paragraph contains one or more negative qualifications: "need not", "does not establish", "is not a theorem", "does not estimate". Examples are lines 17–19, 85–86, 153–154, 285–289, 363–366, 428–433, 449–451, 485–488, 548–553 and 577–600. The precision is appreciated, but the cumulative effect hides the positive content. The paper reads as a list of disclaimers, which will discourage the practitioner audience it targets.

**What to do.**
- Consolidate the caveats in Section 6.3.
- State each positive result once and plainly, especially in the abstract and conclusions.
- Use the freed space for the substantive additions requested above.

## 4. Minor issues (ordered by importance)

1. **Figure 1 (page 4).**
   - The label "Weak or unavailable condition-sensitive channels" floats above the inference block with no box or arrow. Its role as an evidence source is unclear. Draw it as an input with a visibly weak link.
   - The four outputs (usage, exposure, condition, event probability) appear as parallel outputs of one block. This contradicts the sequential chain stressed in Section 3.1, Table 3 and Figure 2. A small DAG or Bayesian-network sketch, with each evidence type entering at the node it informs, would convey the paper's main point much better.
2. **Figure 2 (page 11).** It largely repeats Table 3. It lists "seek better evidence" as a candidate action, but that action is never evaluated (see Required revision 5). Consider merging Figure 2 with Table 3, or making the action concrete.
3. **Eq. 4 (line 406).**
   - The equivalence G_B > G_A ⇔ d_B·v_B/(d_A·v_A) > q_A/q_B holds for any positive q's under equal k. The side condition q_A > q_B > 0 is only needed to call it a "reversal". Say so, and state the equal-burden assumption in the equation itself.
   - Also give the unequal-burden form, because inspection access costs differ between devices in practice.
4. **"Actionable condition" (lines 378–380).** The definition ("one that a reference inspection could confirm") is close to circular. Relate it to the established notion of a *potential failure* (P-F concept) or to a documented service-limit criterion.
5. **Identifiability of q·d (lines 586–593).** This is an important point. Suggest established remedies: latent-class or two-test designs (Hui & Walter, "Estimating the error rates of diagnostic tests", *Biometrics* 36:167–171, 1980), and probability-of-detection characterisation of inspection procedures (MIL-HDBK-1823A, 2009).
6. **Eq. 2 and lines 262–265.** The distinction between prospective (interventional) and historical-policy-conditioned expectations is the causal-inference / off-policy-evaluation issue known from maintenance data, where inspections and repairs are triggered by suspected deterioration. A sentence connecting it to that literature would help readers.
7. **References.**
   - Several citations support claims only tangentially:
     - [13] covers opportunistic maintenance of manufacturing lines, and [19] RCM in power distribution; both are cited for station access dependencies.
     - [14] is HVAC deep-learning FDD, cited for "operating context".
     - [22] is a coal-terminal conveyor digital twin and [23] a tunnel digital twin, cited for asset identity and topology.
     - [16] covers structural-reliability Bayesian updating, cited for "Bayesian updating" in general.
   - The canonical references for multi-component dependencies would serve better: Dekker, Wildeman & van der Duyn Schouten, *Math. Methods Oper. Res.* 45:411–435, 1997; Olde Keizer, Flapper & Teunter, *EJOR* 261(2):405–420, 2017.
   - For POMDP-based inspection and VoI in deteriorating systems: Papakonstantinou & Shinozuka, *RESS* 130:202–213 and 214–224, 2014; Straub, *Structural Safety* 49:75–85, 2014; Andriotis, Papakonstantinou & Chatzi, *Structural Safety* 93:102072, 2021.
   - I was able to locate all cited works except that, for [19], I could only confirm that the DOI resolves to an *Electric Power Systems Research* article; I could not independently confirm its title and authors. Please double-check that entry.
8. **Relationship to the companion paper [20] (lines 359–366).** [20] shares the same author, setting and proxy idea. Its public abstract reports a simulated case study with improved maintenance timing relative to a calendar policy. State explicitly which results are new here and which are inherited. As noted above, harmonise the terminology ("Low-Data" in [20] versus "Limited-Data" here).
9. **Keywords (lines 20–22).** "Bayesian inference" is listed, but no Bayesian inference is performed. Consider "inspection planning under model uncertainty", "value of information", "reliability-centred maintenance".
10. **Table 4.**
    - Explain the notation "{A,B}/B" and "A/{0,B}" in the caption more directly.
    - Add a column for the policy chosen by at least one admissible robust rule (see Required revision 2).
    - Flag rows in which π0 is strictly dominated.
11. **Data Availability (lines 628–630).** "Included with the manuscript source" is not accessible to readers or reviewers. Deposit the script and input file in a public repository with a persistent identifier (e.g., Zenodo).
12. **Funding (lines 621–625).** Give the grant agreement number required by MDPI. FP3-IAM4Rail is Horizon Europe / Europe's Rail JU grant agreement No. 101101966.
13. **Formatting.** The Acknowledgments paragraph (lines 631–634) is rendered in red. Use normal text colour.
14. **Section 5.6 (lines 510–520).** A filled-in example of the planner-facing record for the two-door case (one short table) would make the "communication" recommendations concrete.
15. **Title.** "Predictive Maintenance Systems" and "needs" are vague. A title that names the actual contribution would serve readers better: an applicability assessment for maintenance decisions under persistently weak condition observability, with a railway-station example.

## 5. Recommendation

**Major revision.**

The manuscript is careful, internally consistent, and correct in its algebra. Its central message is practically relevant: exposure rankings are not inspection priorities, and indirect evidence must be carried with explicit assumptions and uncertainty.

However:

- it is not positioned against the maintenance-engineering frameworks that already address consequence versus observability (RCM/P-F, FMECA detectability, RBI, delay-time inspection models, PdM suitability/feasibility selection);
- its deliverables are generic and are not shown to be usable or discriminating on any real case;
- the worked example leaves out the information-acquisition, learning and population elements that would make LD-PdM distinctive;
- the procedure's fallback rule selects strictly dominated actions.

These problems are fixable, and the revision requested above would make the paper a useful contribution. I would want to see the revised version.

## 6. MDPI evaluation grid

| Criterion | Rating | Comment |
|---|---|---|
| Originality / novelty | Low–Average | The framing is a reasonable synthesis but overlaps strongly with RCM task-selection logic, FMECA detectability, RBI and PdM suitability/feasibility frameworks that are not discussed. |
| Significance of content | Average | Relevant to infrastructure asset maintenance; the significance depends on demonstrating usability and added value over existing frameworks. |
| Quality of presentation | Average | Precise and well organised, but dense and heavily hedged. Figure 1 is ambiguous, and a decision-region figure is missing. |
| Scientific soundness | Average | The algebra is correct (verified). The fallback rule violates dominance; the example parameters are weakly motivated; there is no validation. |
| Interest to the readers | Average | Of interest to PdM/asset-management readers; of limited interest to the core *Symmetry* readership unless "asymmetry" is formalised. |
| Overall merit | Average | Potentially useful position paper after major revision. |
| English level | High | Grammatically correct and precise. Stylistic tightening (less hedging, fewer abstract nouns) would improve readability. |
