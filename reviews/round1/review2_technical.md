# Review Report — Reviewer 2 (general PdM background, strong technical/mathematical orientation)

- **Manuscript:** *Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems*
- **Journal:** *Symmetry* (MDPI)
- **Version reviewed:** "Version October 25, 2026 submitted to Symmetry" (PDF header), 18 pages, single author

---

## 1. Summary of the submission

The manuscript proposes the term Limited-Data Predictive Maintenance (LD-PdM). It defines LD-PdM relative to a specific maintenance choice and planning horizon. A choice qualifies when three conditions hold together: (1) the choice is consequential; (2) feasible condition-sensitive channels leave a relevant condition quantity weakly informed, because of persistent constraints; (3) proxy, contextual, historical or prior evidence makes a material contribution. The paper discusses four "asymmetries": observability, failure evidence, information cost versus decision consequence, and scale.

The paper has three intended outputs:

- an applicability checklist (Table 1);
- a five-step assessment procedure (Section 4.1);
- a railway-station example (Section 5).

On the technical side, the paper contains:

- a shared-plus-idiosyncratic error model for exposure estimates (Eq. 1);
- a generic expected-loss policy comparison (Eq. 2);
- a two-door early-inspection model (Eqs. 3–5). It gives the gain $G_i = q_i d_i v_i - k_i$ relative to the existing schedule $\pi_0$, a reversal condition, and a strict common-preference condition over a finite model set;
- a numerical illustration (Eq. 6, Table 4). It uses two routing interpretations $m_1, m_2$, a linear condition model $q_i = 0.1 + \beta x_i$, $\beta\in[0,0.5]$, $d_A\in[0.25,0.9]$, $d_B=0.9$, $v_i=10$ and $k_i=1$.

When no policy is strictly preferred under every model, the procedure falls back to $\pi_0$. The paper notes that this can forgo a gain available under both models. All inputs are declared hypothetical, and no empirical data are used.

## 2. General assessment

The manuscript is carefully written and unusually explicit about what it does not claim. It separates measured, assumed and inferred quantities, and it keeps exposure distinct from condition and from event probability. It also labels every numerical input as hypothetical. The distinction between a small-sample learning problem and weak condition information relevant to a specific decision (lines 91–95) is useful. The two-door model makes a correct and practically relevant point: an exposure ranking does not by itself give an inspection ranking, because detection probability and response value enter multiplicatively.

**Verification performed.** I independently recomputed every quantity in Section 5.4 from the stated model:

- the four expressions in Eq. (6);
- the thresholds $\beta = 1/45$ and $d_A = 1/(1+10\beta)$;
- the region statements in lines 454–464;
- all 30 numerical entries and all decision labels of Table 4;
- the gain ranges in lines 483–484;
- the probability bounds claimed in line 451.

I used exact rational arithmetic and found **no arithmetic errors**. The reversal condition (Eq. 4), the false-positive correction (line 393) and the corner argument for bilinear gains (lines 481–483) are also correct.

**Weaknesses.** Correctness of arithmetic is not the main issue. From a technical standpoint the manuscript has six substantive weaknesses:

1. **The decision rule chooses dominated policies.** The rule built into the procedure (strict unanimity, otherwise retain $\pi_0$) returns a policy that is strictly dominated under every model in most of the region where it is invoked. The paper presents this as an "opportunity cost" finding. In decision-theoretic terms it is an inadmissible rule (Required revision 1).
2. **The definition is not operational.** The central contribution, the definition and checklist, uses undefined qualitative thresholds ("consequential", "weakly informed", "material", "persistent", "feasible"). The title's "asymmetry" is never stated formally.
3. **Uncertainty is treated inconsistently.** The paper frames itself in Bayesian terms, but the decision analysis uses a set-valued model with unanimity. Routing is treated as a model set while $\beta$ and $d_A$ are swept as coordinates. Applied consistently to all declared uncertainty, the procedure becomes uninformative.
4. **Eq. (1) is overstated and unused.** The shared-error result (Eq. 1) is used to support a claim it does not support for decision-relevant quantities. It also does not connect to the routing error used in the example.
5. **The example does not test the stated asymmetry.** It holds consequences fixed, although consequence is what the title asymmetry is about, and some of its conclusions hold by construction.
6. **The mathematics is elementary and incompletely positioned.** Eqs. (3)–(5) are a single-stage preposterior analysis. They should be positioned against risk-based inspection and value-of-information theory, and described more modestly.

**Journal fit.** For *Symmetry*, "asymmetry" is used here in a purely descriptive sense. Several of my suggestions below would make the notion precise and give the paper a stronger mathematical core: a value-of-information formalisation of the regime, and invariance ("symmetry") properties of decision comparisons under classes of proxy error.

All of the above can be addressed without field data. I therefore recommend major revision rather than rejection.

## 3. Required revisions (ordered from most to least important)

### 1. **The fallback rule selects strictly dominated policies; replace it with an admissible decision rule**

*Where:* Section 4.1 step 5 (lines 246–249, 250–255); Section 4.3 (lines 284–289); Section 5.3 (lines 412–433, Eq. 5); Section 5.4 (lines 458–479); Table 4; Abstract (lines 12–14); Conclusions (lines 612–615).

*Problem.* The procedure keeps an early-inspection policy only if Eq. (5) holds, that is, only if the policy is strictly preferred to both alternatives under every model in $\mathcal M$. Otherwise it reverts to $\pi_0$. In Table 4 this produces the following:

- **$(\beta,d_A)=(0.2,0.9)$.** $\pi_0$ is strictly worse than *both* early policies under *both* models: $G_A = 1.7/0.53$ and $G_B = 0.8/0.8$.
- **$(0.2,0.6)$.** $B$ weakly dominates $A$ (tie under $m_1$, $0.8>0.02$ under $m_2$) and strictly dominates $\pi_0$ under both models, yet the rule returns $\pi_0$.
- **$(0.5,0.9)$.** $\pi_0$ yields 0 while $B$ guarantees 2.15 and $A$ guarantees 1.475.

I computed the regions of the declared rectangle $[0,0.5]\times[0.25,0.9]$ under a uniform measure, using closed-form integrals cross-checked on a $1300\times1300$ grid:

| Region | Share of rectangle |
|---|---|
| $B$ strictly common-preferred | 51.4% |
| Rule falls back to $\pi_0$ although $B$ improves on $\pi_0$ under both models ($\beta>1/45$, $d_A \ge c(\beta)$) | 44.1% |
| $\pi_0$ weakly dominates both early policies | 4.3% |
| Genuine disagreement: no policy improves on $\pi_0$ under both models | 0.14% |

So in about 99.7% of the area where the fallback is triggered, it selects a policy that is strictly dominated under every model in $\mathcal M$. Such a rule is not "conservative" in any loss sense. $\pi_0$ has the *worst* guaranteed gain in that region. The rule violates the most basic admissibility requirement. The manuscript recognises the forgone gain (lines 472–479). It still keeps the rule in the procedure, however, and presents its cost as a finding in the Abstract and Conclusions.

*What to do.*

(a) In step 4/5, first remove policies that are dominated across $\mathcal M$ (admissibility/maximality).

(b) Choose among the remaining policies by a declared criterion, for example:

- maximin expected gain over $\mathcal M$ (Γ-maximin; Gilboa & Schmeidler 1989);
- minimax regret (Savage 1951);
- Bayesian model averaging with stated model weights (Hoeting et al. 1999).

Troffaes (2007) compares these criteria (maximality, E-admissibility, Γ-maximin) concisely. Berger (1985) gives the standard treatment of admissibility and Bayes risk.

(c) Show how the choice depends on the criterion. In the paper's own row $(0.2, 0.9)$:

- maximin selects $B$ (guaranteed gain 0.8 versus 0.53);
- minimax regret selects $A$ (maximum regret 0.27 versus 0.90);
- equal-weight averaging selects $A$ (1.115 versus 0.8);
- $A$ is preferred under model averaging exactly when $P(m_1) > 3/13 \approx 0.231$.

This criterion-dependence is the scientifically interesting result. It also identifies precisely what the operator must decide.

(d) Retain $\pi_0$ as fallback only when it is itself undominated and the declared criterion is indeterminate, or when a mandatory requirement applies.

(e) Rewrite the Abstract and Conclusions accordingly.

### 2. **Make the operational definition and checklist precise, and formalise the "asymmetry"**

*Where:* Section 2.1 (lines 70–86, 96–103), Table 1, Section 2.4 (lines 133–139), Section 5.1 (lines 293–295, 308–316), Introduction (lines 44–47), Conclusions (lines 602–607).

*Problem.* The definition and checklist are a main claimed contribution. Their key terms have no criteria that two assessors could apply reproducibly: "consequential outcome", "weakly informed", "material contribution", "persistent" and "feasible set of channels". It is also unclear whether "feasible" means technically possible, affordable within budget, or decision-theoretically worthwhile. Lines 137–139, 294–295 and 101–103 point in different directions. Criterion (3) begins with "therefore" (line 76), as if it followed from (2). It is an independent condition. The checklist is never seen to discriminate: in Section 5.1 all three answers are stipulated as "conditional affirmative". Finally, the title's asymmetry is stated only verbally ("need not increase together", lines 44–47).

*What to do.* Give each criterion an operational counterpart with explicit, user-set tolerances. A natural choice uses value of information, which matches the paper's own separation of "information content, its effect on a choice, and acquisition cost" (lines 101–103). Let:

- $\theta$ be the decision-relevant condition quantity;
- $Y_f$ be the condition channels obtainable within the horizon under the operator's constraints;
- $Z$ be the indirect evidence.

The criteria could then read:

- **(1)** $\mathrm{EVPI}_\theta \ge \delta_1$, i.e. resolving $\theta$ could change the expected loss materially.
- **(2)** $\mathrm{EVSI}(Y_f) \le \kappa\,\mathrm{EVPI}_\theta$, i.e. the feasible channels recover only a small fraction of the attainable value. The binding constraint should be recorded. A mutual-information version, $I(\theta;Y_f)$, is an alternative if a decision-free measure is preferred.
- **(3)** $\mathrm{EVSI}(Z\mid Y_f) \ge \delta_3$, or the optimal action changes for plausible values of $Z$.

The "asymmetry" can then be stated as high $\mathrm{EVPI}_\theta$ combined with low achievable $\mathrm{EVSI}(Y_f)$. This gives a precise object in a decision-value/information plane, which would suit this journal.

In addition, apply Table 1 to three or four contrasting decisions and show at least one "no" and one "unresolved" outcome. Candidates are already in the text: clearing an obstruction versus early wear inspection (lines 87–90), and few labelled samples with an informative channel (lines 91–92).

### 3. **Use one consistent representation of uncertainty (probabilistic versus set-valued; models versus parameters)**

*Where:* Keywords (lines 20–22); Sections 3.2–3.3 (lines 189–211); Section 4.3 (lines 284–289); Section 5.3 (lines 412–427); Section 5.4 (lines 442–451, 480–488).

*Problem.* Several inconsistencies interact:

- **Bayesian framing, set-valued analysis.** The paper is framed around Bayesian updating (keywords; lines 189–192, 205–211). The decision analysis, however, never assigns a probability to anything uncertain. Routing interpretations form a set $\mathcal M$ subject to unanimity, while $\beta$ and $d_A$ are swept as plot coordinates.
- **Ranges used as uncertainty sets.** Lines 449–450 state that the ranges are "not … elicited uncertainty bounds". Lines 480–486 then use the same rectangle as an uncertainty set for robustness.
- **Unanimity over everything is uninformative.** If the unanimity rule is applied to all declared uncertainty, $\{m_1,m_2\}\times$ rectangle, no early policy improves everywhere ($\min G_A=-0.75$, $\min G_B=-0.10$; lines 483–484). The procedure then returns $\pi_0$ irrespective of the evidence. By contrast, independent uniform priors on $\beta$ and $d_A$ with equal model weights give $\mathbb E[G_B]=1.025$, $\mathbb E[G_A]=0.545$ and $\mathbb E[G_0]=0$, so $B$ is selected. The two treatments give opposite recommendations.
- **$\mathcal M$ is not constructed.** How $\mathcal M$ is built ("plausible", lines 284–289 and 412) is never stated.
- **The narrative contradicts the model set.** Lines 420–422 say that dated route records *show* the reassignment, which would establish $m_2$. Section 5.4 nevertheless keeps $m_1$ as plausible.

*What to do.*

- State, for each uncertain quantity, whether it is treated probabilistically (prior/posterior) or as ambiguity (a set), and justify the choice.
- Derive $\mathcal M$ or the model weights from the evidence, for example from a posterior credible set or a likelihood-ratio threshold over routing shares. The arXiv version of the author's companion work [20] describes a Bayesian routing-share model on a station graph, which could supply exactly this.
- Apply the decision rule to the full declared uncertainty.
- Compute the value of resolving the routing ambiguity, to give substance to step 5 and lines 431–433. At $(\beta,d_A)=(0.2,0.9)$, the expected value of perfect information about the routing model is 0.135 loss units at $P(m_1)=0.5$ (0.2025 at 0.25, 0.0675 at 0.75). That is far below the inspection burden $k=1$, which is a concrete and instructive output.
- Remove the keywords "Bayesian inference" and "partial observability" if the revised paper still performs no inference and uses no partially observable model.

### 4. **Section 3.4 / Eq. (1): the shared-error result is overstated and not connected to the example**

*Where:* Eq. (1) and lines 213–225; Section 5.5 (lines 505–507); Abstract (lines 14–15).

*Problem.* There are four separate issues.

(a) **Assets versus records.** In Eq. (1), $n$ counts *assets*. Lines 223–225, however, draw a conclusion about "more records from the same source". Note also that $\mathrm{Var}(\hat x_i-\hat x_j)=2\sigma_\varepsilon^2$ does not depend on $n$. With $r$ independent records per asset, the pairwise variance becomes $2\sigma_\varepsilon^2/r\to0$ while the shared component persists. The stated claim needs this record dimension in the model.

(b) **Cancellation does not carry over to decisions.** Cancellation holds for exposure differences but not for the decision quantities. With the paper's own linear condition model and a shared additive exposure error $B_s$:

$$\hat G_A-\hat G_B=(G_A-G_B)+\beta B_s\,(d_A v_A-d_B v_B),\qquad \hat G_i - G_i=\beta d_i v_i B_s .$$

At $(\beta,d_A)=(0.2,0.4)$ under $m_1$, the $A$–$B$ gain difference changes by $-1.0$ per unit $X_{\rm ref}$ of shared error and changes sign at $B_s=-0.6$. $G_A$ and $G_B$ themselves shift by $0.8B_s$ and $1.8B_s$. So the shared component does *not* cancel in the unequal-detection setting that the paper emphasises. It also does not cancel in the comparison with $\pi_0$ that the paper stresses (lines 410–411, 472–479). The Abstract ("separates aggregation uncertainty from pairwise ranking") and lines 505–507 overstate what Eq. (1) shows.

(c) **The example's error is a different kind.** The routing ambiguity in Section 5.4 is a *group-specific reallocation*: $m_2$ moves $A$'s passengers to a third passage. Eq. (1) does not cover this case; it is only mentioned verbally (line 221). Eq. (1) is therefore never used in the example.

(d) **Notation clash.** $B$ denotes both the shared error and door $B$, and $\sigma_B^2$ reads as a door-$B$ quantity.

*What to do.* Replace or extend Eq. (1) with a routing-share model, for example $\hat{\mathbf x}=A(\theta)\mathbf N+\boldsymbol\varepsilon$ with a shared routing parameter $\theta$ and record multiplicity. Then derive the covariance of the decision-relevant differences. State the invariance conditions explicitly:

- Pairwise policy comparisons are invariant under a common *translation* of exposures iff $\beta=0$ or $d_Av_A=d_Bv_B$, given linear $q$.
- They are invariant under a common *scaling* iff $d_Av_Ax_A=d_Bv_Bx_B$.
- Comparisons with $\pi_0$ are invariant under neither.

Stated this way, as invariance of decisions under classes of proxy error, the result becomes a precise and natural contribution for *Symmetry*.

### 5. **The worked example does not exercise the paper's central asymmetry, and some of its conclusions hold by construction**

*Where:* Section 5.3 (lines 378–386, 399–411); Section 5.4 (lines 442–464); Table 4; section title "continuous decision boundaries" (line 441).

*Problem.*

- **Consequences are held fixed.** The paper's thesis concerns the mismatch between *consequences* and information (lines 44–47, 606–607). In the example, however, $v_A=v_B$ and $k_A=k_B$, and only exposure and detection vary.
- **$v_i$ is a black box.** It is defined as the "conditional expected net loss avoided" (lines 382–385). Yet the value of *early* detection depends on three things: the time gap to the scheduled inspection, the hazard of losing function in that gap, and the consequence of the specific function. The paper itself stresses the last of these (lines 296–299).
- **Conclusions follow from the parameter box.** "No point in the declared rectangle gives a strict preference for A under both interpretations" (lines 460–461) follows immediately from $x_A(m_2)=0.35<x_B=0.5$ together with $d_A\le d_B=0.9$. It is a property of the chosen box, not a finding. The box also never lets the more exposed door be easier to inspect, and the paper gives no reason why it should be harder (lower $d_A$).
- **No figure of the boundaries.** The section promises continuous decision boundaries, but no figure shows them.

*What to do.*

- Decompose $v_i$, for example as $v_i = P_i(\text{loss of function before the scheduled inspection}\mid\text{condition})\cdot C_i - c_{\mathrm{resp},i}$. Let $C_A\neq C_B$ reflect function and accessibility.
- Either widen the $d_A$ range to overlap $d_B$ or justify $d_A\le d_B$ physically.
- Add a 2-D decision-region figure over $(\beta,d_A)$, and possibly $v_A/v_B$. It should show $d_A=c(\beta)$, $d_A=1/(1+10\beta)$ and $\beta=1/45$, with the regions labelled under the rule(s) adopted after Revision 1. Report region areas (see Revision 1) or a comparable summary.
- State explicitly which conclusions follow from the parameter box.

### 6. **Position the two-door analysis against established inspection-planning theory and describe the analytical content accurately**

*Where:* Section 4.2; Section 5.3; Table 5; line 58 ("derives"); line 577 ("conditional analytical results"); Abstract (line 10, "Exact calculations").

*Problem.* Eq. (3) is a single-stage preposterior (value-of-information) analysis of an inspection with a probability of detection. This is the standard object of risk-based inspection (RBI) planning for structures (Straub & Faber 2005) and of classical decision analysis (Raiffa & Schlaifer 1961; Howard 1966), and it overlaps with [6]. Table 5 omits both RBI/probability-of-detection (PoD) modelling and robust/imprecise decision theory, which are the closest formalisms to Sections 4.2–5.4.

There is also a technical point. If detection depends on defect severity $s$, then $q_i d_i = \int \mathrm{PoD}(s)\,f_i(s)\,ds$, and $v_i$ conditioned on detection is severity-weighted. The factorisation $q_i\cdot d_i\cdot v_i$ silently assumes independence between detectability and benefit.

Eqs. (3)–(5) are rearrangements of an expected value, as the author partly concedes (lines 534–537). The wording "derives" and "analytical results" overstates them.

*What to do.*

- Add RBI/PoD and robust decision rules to Table 5 and to the text of Section 4.2.
- State the independence assumption behind the $q\,d\,v$ factorisation, or generalise it.
- Calibrate the language describing the analytical contribution.

### 7. **Formalise the five-step procedure and trace it end-to-end on the example**

*Where:* Section 4.1 (lines 228–255); Section 5.

*Problem.* The procedure is described only in prose. Its inputs and outputs are not typed. The rule "request further information only when it can usefully arrive before the decision deadline" (lines 248–249) is not defined. The station example never shows steps 1–5 being executed in sequence with their intermediate outputs.

*What to do.*

- Provide an algorithm box. Inputs: $\Pi$, $\mathcal M$ or prior, loss/gain model, constraints, deadline. Outputs: selected policy or documented indeterminacy, assumption register, reconsideration triggers.
- Define the information-request rule, e.g. EVSI net of acquisition cost, subject to arrival before the deadline.
- Add a one-table trace of the station example through all five steps.

### 8. **Formalise the informative observation process inside Eq. (2)**

*Where:* Section 2.3 (lines 125–131); Section 4.2 (lines 258–265); Section 5.3 (lines 434–440).

*Problem.* The paper correctly stresses that inspections, replacements and missing work orders may be informative. Eq. (2), however, hides how the evidence $E$ enters. The remark that the superscript $\pi$ "does not condition on an action selected by a historical policy" (lines 262–264) cannot be checked without the likelihood of the records.

*What to do.*

- Write $p_m(s\mid E)\propto p_m(E\mid s,\pi_{\rm hist})\,p_m(s)$.
- State the condition under which the historical policy is ignorable (missing-at-random/ignorability; Rubin 1976).
- Indicate where $q_i(m)$ would come from in this structure.

### 9. **Provide evidence that the procedure improves decisions, or weaken the claims of usefulness**

*Where:* Section 6.2 (lines 548–575); Sections 4.3 and 5.5 (lines 284–289, 505–507); Conclusions (lines 608–620).

*Problem.* All evaluation is deferred. The example is a deterministic two-door calculation. Nothing shows that the checklist and procedure lead to better decisions than naive exposure ranking.

*What to do.* Run a modest Monte Carlo study on a synthetic station with known ground truth: routing shares, a shared count bias, and a simple degradation model. Compare realised loss or regret for:

- exposure ranking;
- the strict-unanimity-plus-fallback rule;
- maximin and minimax-regret rules;
- Bayesian model averaging.

This needs no field data, and it would directly support the robustness and shared-error claims. If the author regards it as out of scope, the claims about the procedure's usefulness should be reduced accordingly.

## 4. Minor issues (ordered by importance)

1. **Identification (lines 586–590).** In the compact model with known $v_i$ and $k_i$, the decision depends on $(q_i,d_i)$ *only* through the product $q_id_i$. Non-identifiability of prevalence versus detection is therefore decision-irrelevant here. Historical positive-finding rates, if the inspection type and timing are comparable and selection is modelled, identify exactly the decision-relevant quantity. Separate identification matters only once false positives are included, through $(1-q_i)f_ih_i$, or when detection is extrapolated to a different inspection. Saying so would strengthen the decision-oriented argument of line 563.
2. **Eq. (4).** State the hypotheses separately: "Assume $k_A=k_B$, $q_B>0$, $d_Av_A>0$; then $G_B>G_A \iff \ldots$". The side condition $q_A>q_B>0$ is not part of the equivalence; it only makes the statement a reversal. Also give the general form $q_Bd_Bv_B-q_Ad_Av_A>k_B-k_A$.
3. **Lines 402–404 (nonlinear exposure–condition map).** Give a precise sufficient condition. If the exposure of $A$ first-order stochastically dominates that of $B$ and the map is increasing, then $q_A\ge q_B$ (e.g. Shaked & Shanthikumar 2007). Ordering of means alone suffices only for linear maps, as in Section 5.4.
4. **Eq. (1).** Define $\bar x$ and $\bar{\hat x}$ explicitly. Line 220 says a fixed bias "should not be described as a variance component". This conflicts with the epistemic (Bayesian) representation of an unknown fixed bias by a prior variance, which the paper elsewhere advocates. Clarify which interpretation is intended.
5. **Notation.**
   - $B$ (shared error, $\sigma_B^2$) clashes with door $B$.
   - $E$ (evidence) sits next to $\mathbb E$ (expectation).
   - $R_m(\pi)$ is a posterior expected loss (Bayes risk), whereas Table 2 defines "Risk" verbally in a different way; align them.
   - $\pi^\star_m$ and $\Pi$ are introduced in Eq. (2) but never used. State $\Pi=\{\pi_0,\pi_A,\pi_B\}$ in Section 5.3.
   - $G_B$ in Eq. (6) has no model argument because it is model-invariant; say so.
   - $d_i$ is called "detection probability" (line 380) and "inspection sensitivity" (line 447); use one term.
   - $x_i$ denotes dimensional exposure in Eq. (1) and dimensionless exposure in Section 5.4.
6. **Lines 455–458.** "B improves on the baseline exactly when $\beta>1/45$" should add "under both models". "Model $m_2$ gives B greater gain than A whenever $\beta>0$" relies on $d_A\le d_B$; make this explicit. The statement also holds at $\beta=0$ when $d_A<0.9$.
7. **Table 4.**
   - Rename the column "Both models" to "Strict common-preference rule".
   - Add a column with the minimum over models of each gain, which makes the forgone gain visible.
   - Flag rows 2, 4 and 6, where $\pi_0$ is strictly worse than an early policy under every model.
8. **Figure 1.**
   - The label "Weak or unavailable condition-sensitive channels" floats unconnected. Show it as a (weak) evidence input.
   - The outputs are drawn in parallel, whereas the text (lines 166–171) describes a chain usage → exposure → condition → event.
   - Figures 1 and 2 overlap substantially; consider merging them.
9. **Figure 2.** There is no feedback from inspection findings, or from "seek better evidence", back to beliefs. This matters because the decision object is an inspection policy that specifies actions after each observation (lines 257–258).
10. **Terminology.** The label "Limited-Data" fits a definition centred on weak condition information poorly, since the paper explicitly allows extensive data (lines 92–93). Justify the name or align it with the definition, and check the keywords against the content.
11. **Readability.** Negative qualifications ("need not", "does not establish", "is not") are very dense; see e.g. lines 143–146, 359–366, 428–433, 449–451, 486–488 and 548–553. Consolidating the caveats in Section 6.3 and stating positive claims directly would make the argument easier to follow and shorten Sections 2–3. The English itself is correct.
12. **Section 2.1.** "The four asymmetries" (line 96) are referenced before they are introduced. The word "therefore" in criterion (3) (line 76) suggests a dependence on criterion (2) that does not exist.
13. **Reproducibility (lines 486–488, 628–630).** The Python calculation is said to be "included with the manuscript source", but it was not available to me as a reviewer. Deposit it with a persistent identifier and cite it. To the author's credit, every number can be reproduced by hand from the closed forms, and I did so. Emphasising "exact rational results" for two-parameter linear arithmetic is unnecessary.
14. **References.**
    - For [20] I located the arXiv preprint (arXiv:2603.14384, Bauer & Baranowski, 2026), but I could not confirm the GPECOM proceedings record or the DOI given. Please check them.
    - For hierarchical modelling (lines 150–151), cite a standard reference (e.g. Gelman et al., *Bayesian Data Analysis*, 3rd ed., 2013) in addition to the author's own [11].
    - I spot-checked [10], [13] and [14]; they exist as cited.
15. **MDPI formatting.**
    - Use the "Equation (2)" style (lines 265–266, 404, 424, 440, 452, 506, 564).
    - The affiliation lacks department, postal address and country.
    - The funding statement should give the FP3-IAM4Rail grant agreement number.
    - The AI-use statement (lines 631–634) is typeset in red.

**Works referred to in this report (not in the manuscript):**

- Berger, J.O. *Statistical Decision Theory and Bayesian Analysis*, 2nd ed.; Springer: New York, 1985.
- Gelman, A.; Carlin, J.B.; Stern, H.S.; Dunson, D.B.; Vehtari, A.; Rubin, D.B. *Bayesian Data Analysis*, 3rd ed.; CRC Press: Boca Raton, 2013.
- Gilboa, I.; Schmeidler, D. Maxmin expected utility with non-unique prior. *J. Math. Econ.* **1989**, *18*, 141–153.
- Hoeting, J.A.; Madigan, D.; Raftery, A.E.; Volinsky, C.T. Bayesian model averaging: a tutorial. *Stat. Sci.* **1999**, *14*, 382–417.
- Howard, R.A. Information value theory. *IEEE Trans. Syst. Sci. Cybern.* **1966**, *2*, 22–26.
- Raiffa, H.; Schlaifer, R. *Applied Statistical Decision Theory*; Harvard University: Boston, 1961.
- Rubin, D.B. Inference and missing data. *Biometrika* **1976**, *63*, 581–592.
- Savage, L.J. The theory of statistical decision. *J. Am. Stat. Assoc.* **1951**, *46*, 55–67.
- Shaked, M.; Shanthikumar, J.G. *Stochastic Orders*; Springer: New York, 2007.
- Straub, D.; Faber, M.H. Risk based inspection planning for structural systems. *Struct. Saf.* **2005**, *27*, 335–355.
- Troffaes, M.C.M. Decision making under uncertainty using imprecise probabilities. *Int. J. Approx. Reason.* **2007**, *45*, 17–29.

## 5. Recommendation

**Major revision.**

The manuscript is careful and honest about its scope, and its arithmetic is correct throughout. It does not yet meet the standard of technical soundness its own framing calls for, for four reasons:

- the decision rule embedded in the proposed procedure selects strictly dominated actions in almost all cases where it is invoked;
- the defining criteria are not operational;
- uncertainty is represented inconsistently, so that, applied consistently, the procedure is uninformative;
- the shared-error result is overstated for decision-relevant quantities.

All of these can be fixed with analysis alone, without new data. The additions requested above — an admissible decision rule, a value-of-information formalisation of the regime, invariance results for proxy errors, and a decision-region figure — would also give the paper a mathematical core appropriate for *Symmetry*.

## 6. MDPI evaluation grid

| Criterion | Rating | Comment |
|---|---|---|
| Originality / novelty | Average | The decision-relative definition of the regime is a reasonable conceptual contribution. The formal content (Eqs. 1–6) is standard. |
| Significance of content | Average | Relevant to large populations of weakly instrumented assets. Significance is currently limited by the non-operational definition and the absence of any evaluation. |
| Quality of presentation | Average | Precise wording and honest scope statements. However, the text is heavily hedged and abstract, the two figures are largely redundant, there is no decision-region figure, and the procedure is never traced end-to-end. |
| Scientific soundness | Average | Arithmetic verified correct. The decision rule is inadmissible, the uncertainty treatment is inconsistent, and the Eq. (1) claim is overstated (Required revisions 1, 3, 4). |
| Interest to the readers | Average | Of interest to maintenance-decision and reliability readers; the link to the *Symmetry* readership is currently only terminological. |
| Overall merit | Average | Major revision. |
| English level | The English is fine and does not require any improvement | Grammar and vocabulary are good. Readability would benefit from fewer stacked qualifications (Minor issue 11). |
