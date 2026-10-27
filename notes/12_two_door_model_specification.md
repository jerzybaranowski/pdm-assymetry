# Bounded two-door decision example

**Date:** 2026-10-23

**Status:** the author explicitly approved the complete Section 8 specification and numerical calculation on 2026-10-23. Implementation, tests, manuscript integration, and PDF verification are complete; see [the numerical report](14_numerical_example_report.md). The inputs remain hypothetical, not empirical estimates.

**Basis:** [`10_round0_revision_plan.md`](10_round0_revision_plan.md), the existing two-door vignette in `paper/template.tex`, and the technical and scope reviews in `reviews/round0/`.

This example applies established expected-loss reasoning to a discretionary inspection choice. Its purpose is to expose assumptions that passenger/exposure ordering leaves implicit. It introduces no new inference or optimization method and estimates no station performance or physical-failure probability. The symbolic derivation can support the conceptual manuscript independently of the optional numerical proposal.

## 1. Decision, horizon, and feasible policies

At the present decision time $t$, the planner has capacity for **at most one additional early inspection** of door A or B before the next scheduled review at $t+\Delta$. Here $\Delta$ is a specified interval of calendar time; no numerical duration is needed for the symbolic comparison. Existing mandatory work and the established service schedule remain in force under every choice. Any condition requiring immediate mandatory action is outside this discretionary comparison.

The three policies are:

- $a_0$: retain the existing admissible schedule, with no additional early inspection.
- $a_A$: inspect A early; perform the predefined feasible service response if the inspection confirms the specified actionable finding; otherwise retain the existing schedule.
- $a_B$: apply the same observation-and-response policy to B.

All three face the same upper bound of one early inspection, access constraints, service obligations, and response capability. This is equal available capacity, not equal realized expenditure: $a_0$ leaves the discretionary slot unused. If an early visit is compulsory, replace $a_0$ with the documented default allocation of that visit. Do not compare an optional inspection against a fictional no-maintenance baseline.

Inspection and the contingent response must be feasible together. The capacity statement counts the early inspection; available response capacity must separately permit the specified service after a positive result. If inspection and repair compete for the same indivisible slot, these policies are infeasible and require a different resource model.

Loss includes inspection effort, service effort, disruption, and the specified avoidable consequences over $[t,t+\Delta]$, on one common **arbitrary loss scale**. These units are neither euros nor reported industrial costs. Either restrict the claim to this horizon or include an explicitly specified terminal consequence at $t+\Delta$ consistently across all policies. A difference in repair cost is measured relative to the existing schedule: repair that would also occur under $a_0$ is not automatically a wholly additional cost.

## 2. Evidence, accumulated exposure, and the actionable finding

Let $E$ denote the assumed available counts, dated routing records, device information, and service histories. A model $m\in\mathcal M$ specifies one plausible interpretation of these sources and the unmeasured links. The set $\mathcal M$ must be declared; robustness within it does not protect against an omitted interpretation.

Let $U_i(s)$ denote the usage rate and

$$
X_i=\int_{t_0}^{t} U_i(s)\,\mathrm ds
$$

the accumulated cycle exposure over the historical interval being assessed, with a common stated reference $t_0$. $U_i$ has units of cycles per calendar-time unit and $X_i$ has units of cycles. Counts may inform $U_i$ only through routing, passenger grouping, and controller assumptions. The toy calculation may instead use $x_i=X_i/X_{\rm ref}$, a dimensionless exposure relative to a fixed declared reference; it must not call $x_i$ measured damage.

Define $Z_i=1$ when the targeted **actionable condition is present at the early inspection**. It is the condition that an adequate reference inspection could confirm and for which the predefined response is applicable. Define

$$
q_i(m)=\Pr_m(Z_i=1\mid E),\qquad
d_i(m)=\Pr_m(Y_i=1\mid Z_i=1,E),
$$

where $Y_i=1$ is the actual inspection's positive result. Thus $q_i$ is the probability that there is an actionable finding to discover, and $d_i$ is inspection sensitivity. Their product is the probability of a **true positive actionable finding**, not the probability of physical failure. Neither probability follows from passenger counts alone.

An exposure–finding premise can be represented by $\Pr_m(Z_i=1\mid x_i,H_i)=g_m(x_i,H_i)$, where $H_i$ contains relevant baseline and service history. A monotone $g_m$ with comparable $H_i$ makes larger exposure support larger $q_i$ when exposure is fixed under the model. With uncertain exposure, use the probability averaged over its declared distribution; ordering mean exposure alone does not generally order this average for a nonlinear $g_m$. The numerical proposal below uses fixed exposure within each discrete routing interpretation and an explicitly assumed affine relationship.

## 3. Outcome table and expected improvement

Define $k_i\geq0$ as the expected incremental inspection burden, incurred whether or not a finding occurs. Define $v_i$ as the conditional expected **net reduction in loss** from the specified response, relative to $a_0$, given a true positive result. It incorporates response effectiveness, service cost, disruption, the relevant horizon, and terminal accounting if used. Its conditioning on detection is deliberate: if inspection preferentially detects more severe conditions, an unconditional mean consequence cannot simply replace $v_i$.

To expose the diagnostic assumption, also define

$$
f_i=\Pr_m(Y_i=1\mid Z_i=0,E),
$$

the false-positive probability, and $h_i\geq0$, the conditional expected extra loss of responding to a false positive. The binary policy acts after every positive result. Alternatively, if positive results trigger confirmatory diagnosis, $Y_i$ must denote the result **after that full diagnostic process**, and its effort belongs in $k_i$ or in the applicable conditional response term. Confirmation does not justify assuming zero false positives without stating that simplification.

| Underlying condition and result | Probability under $m$ | Subsequent action | Incremental loss relative to $a_0$, excluding inspection burden |
|---|---|---|---|
| Actionable condition; positive result | $q_i d_i$ | Predefined service response | $-v_i$ |
| Actionable condition; negative result | $q_i(1-d_i)$ | Retain existing schedule | $0$ |
| No actionable condition; positive result | $(1-q_i)f_i$ | Erroneous response | $h_i$ |
| No actionable condition; negative result | $(1-q_i)(1-f_i)$ | Retain existing schedule | $0$ |

The zero entries require that inspection without response does not itself change condition or subsequent scheduling; all visit burden still belongs in $k_i$. They do not mean the unaddressed condition has no consequences: those consequences are already in the baseline loss. No independence between the two doors is required for this comparison. It does require that inspecting one door leaves the other door's relevant outcomes unchanged, or that all resulting station-level effects are already included in the conditional loss differences.

By conditioning on the four outcomes,

$$
\begin{aligned}
G_i(m)&=q_i d_i v_i-(1-q_i)f_i h_i-k_i,\\
\mathbb E_m[L(a_i)\mid E]&=\mathbb E_m[L(a_0)\mid E]-G_i(m).
\end{aligned}
$$

Here $G_i$ is the expected net loss reduction from the complete inspection-and-response policy. It is not the value of raw information under every possible future action, and it is not a standalone failure-risk score. A negative $G_i$ means this particular policy has higher expected loss than $a_0$ under $m$.

For a compact manuscript derivation, state the simplifying assumption $f_i=0$ and retain

$$
G_i=q_i d_i v_i-k_i.
$$

Keep the false-positive limitation in prose. Positive $v_i$ is also an assumption about the predefined response; merely calling a finding actionable does not establish that its net benefit exceeds its cost over the selected horizon.

## 4. Agreement, reversal, and unresolved comparison

The exposure comparator chooses A when $x_A>x_B$. Under comparable histories and the monotone exposure–finding premise, suppose this implies $q_A>q_B>0$. For the zero-false-positive illustration with equal inspection burden and $d_i v_i>0$,

$$
\begin{aligned}
G_A>G_B
&\iff q_A d_A v_A>q_B d_B v_B,\\
G_B>G_A
&\iff \frac{d_B v_B}{d_A v_A}>\frac{q_A}{q_B}.
\end{aligned}
$$

The following are symbolic regions, not numerical or simulated findings:

| Parameter region | Comparison with exposure order | Operational interpretation |
|---|---|---|
| $q_A>q_B$, $d_A=d_B>0$, $v_A=v_B>0$, $k_A=k_B$ | $G_A>G_B$: agreement | Inspect A early only if its improvement also exceeds zero. |
| $q_A>q_B$ and $d_Bv_B/(d_Av_A)>q_A/q_B$, equal $k$ | $G_B>G_A$: disagreement | Lower exposure can warrant the earlier inspection because confirmed action has greater expected value. Inspect B only if its improvement also exceeds zero. |
| $q_A d_Av_A-k_A=q_B d_Bv_B-k_B$ | Equal expected improvement | This model does not give a unique inspection order. |
| Plausible models give both signs of $G_A-G_B$ | No common order across $\mathcal M$ | Record which assumption changes the choice and apply the documented fallback. |
| $G_A\leq0$ and $G_B\leq0$ | Neither early policy improves on $a_0$ under that model | Retaining the existing schedule is at least as good among these three policies. |

For unequal costs, the threshold for A under the same simplification is

$$
d_A>\frac{q_B d_B v_B+k_A-k_B}{q_A v_A},
$$

provided $q_Av_A>0$. A threshold outside $[0,1]$ may make that strict ordering impossible or automatic over the feasible sensitivity range. With false positives, use the full $G_i$ expression instead of this threshold. This establishes why exposure alone cannot rank inspection policies without assertions about detection, consequences, and burdens.

## 5. Stopping rule and executable fallback

For a nonempty finite model set, or a compact parameter set on which the improvements are continuous, define

$$
D_{AB}^{-}=\min_{m\in\mathcal M}\{G_A(m)-G_B(m)\},\qquad
G_A^{-}=\min_{m\in\mathcal M}G_A(m).
$$

A strict preference for $a_A$ over **both** $a_B$ and $a_0$ is supported throughout the declared set when $D_{AB}^{-}>0$ and $G_A^{-}>0$. Reverse A and B for the analogous B criterion. Comparison with the baseline is essential: a stable A/B ranking can rank two harmful early-inspection policies. The baseline weakly dominates both early policies throughout the set if $\max_mG_A(m)\leq0$ and $\max_mG_B(m)\leq0$.

A sign change in $G_A-G_B$ defeats a common A/B order. A tie defeats a **strict, unique** order at that model; it may still permit a weak dominance statement. If an arbitrary noncompact model set is used, replace minima by pointwise conditions or state that positive infima supply a sufficient uniform-margin criterion. Do not equate an infimum of zero with an attained tie without the required assumptions.

The chosen conservative decision procedure withholds a new differentiated recommendation when no early policy strictly improves on both alternatives throughout the stated set. It then retains the existing admissible schedule or its documented tie-break rule; it identifies evidence that could change the comparison and a review trigger. This fallback is an explicitly chosen operational rule, **not** a theorem that the baseline minimizes worst-case loss. Mandatory or consequence-based requirements continue to take precedence. If the baseline has ceased to be admissible, the operator must resolve that constraint instead of treating uncertainty as authorization to defer.

## 6. Temporal meaning of the routing correction

The original vignette's correction concerns the interval $[t_0,t]$: the alternative route assignment was **already in force during the exposure interval**, but omitted from the original interpretation. Correcting dated records revises the inferred allocation of past passages and therefore $x_i$ and $q_i$. It does not undo actual historical cycles or repair the door.

A routing change introduced only after $t$ changes prospective use; it cannot erase past exposure. Local observations made at $t$ support an interpretation of historical routing only with dated records or an explicit assumption of persistence. A change in $q_A>q_B$ alone does not logically force B to become preferred: recompute the full policy comparison over the revised model set.

No value-of-information number is assigned to a local counting exercise. Such a calculation would require its possible observations, their likelihoods under the competing routes, its burden, the time available, and the policy selected after each result. These are outside the bounded illustration.

## 7. LaTeX-ready compact passage

The following passage can replace the unsupported inference from exposure order to inspection order once its surrounding text supplies the existing-schedule baseline and horizon:

```latex
Let $q_i$ be the probability that the specified actionable condition is
present, $d_i$ the probability that inspection detects it, and $v_i$ the
conditional expected net loss avoided by the predefined response after a
true positive finding, relative to the existing schedule. Inspection has
incremental burden $k_i$. Assume that false positives do not occur in this
bounded illustration and that the response is feasible within the service
constraints. The expected net loss reduction from inspecting door $i$ and
acting on a positive result is
\begin{equation}
G_i=q_i d_i v_i-k_i.
\label{eq:inspection-gain}
\end{equation}
These probabilities concern an actionable finding at inspection, rather
than physical failure. With equal inspection burdens and positive $d_iv_i$,
even $q_A>q_B$ supports inspecting B first when
$d_Bv_B/(d_Av_A)>q_A/q_B$. Under equal positive detection probabilities and response values,
the same premise instead supports A. Thus the exposure comparison depends
on inspection and consequence assumptions that traffic data do not supply.
An early inspection must also improve on retaining the existing schedule.
Across a nonempty finite declared set of plausible models $\mathcal M$, A has a
strict preference over both alternatives only when
\begin{equation}
\min_{m\in\mathcal M}[G_A(m)-G_B(m)]>0,
\qquad
\min_{m\in\mathcal M}G_A(m)>0.
\label{eq:inspection-stability}
\end{equation}
When neither early policy satisfies the analogous conditions, the planner
records the unresolved assumptions and retains the existing admissible
schedule or its documented tie-break rule. This is the fallback adopted
for the illustration, rather than a claim of robust optimality.
```

Use the existing expected-loss and inspection-planning citations around this passage; do not present the algebra or stopping criterion as LD-PdM methodological novelty. The local symbolic example does not require a latent-state posterior equation, a hazard model, or a new physical-failure formula elsewhere in the manuscript.

## 8. Optional numerical inputs proposed for author review

**Approved on 2026-10-23.** The author explicitly approved the specification and calculations in response to the question linking this section and stating the model, parameter ranges, benefits, and inspection burden. Approval covers the complete specification, including the finding event, observation simplification, response, loss scale, model set, and baseline. These remain hypothetical scenario choices, not estimates, literature-derived ranges, or confirmed physical constraints. Their purpose is an exactly enumerated illustration of the symbolic boundaries. The section heading is retained to preserve links to the reviewed specification.

| Input | Approved illustrative choice | Purpose and limitation |
|---|---|---|
| Historical exposure scale | Dimensionless $x_i=X_i/X_{\rm ref}$; same $X_{\rm ref}$ for both doors | Defines only relative accumulated use; no station cycle count is claimed. |
| Original routing interpretation $m_1$ | $x_A=1$, $x_B=0.5$ | Declares greater historical exposure for A. |
| Corrected historical interpretation $m_2$ | $x_A=0.35$, $x_B=0.5$ | Represents diversion to a third open passage already in force during $[t_0,t]$; traffic removed from A is not automatically assigned to B. |
| Actionable-condition probability | $q_i=q_0+\beta x_i$, with $q_0=0.1$ | Affine illustrative exposure–finding assumption, common baseline history; no failure model. |
| Exposure coefficient | $\beta\in[0,0.5]$ | Includes an uninformative-exposure boundary; the range is chosen for illustration, not elicited. |
| Detection | $d_B=0.9$; $d_A\in[0.25,0.9]$ | Allows equal sensitivity and lower sensitivity at A; does not imply actual door-inspection performance. |
| Net response value | $v_A=v_B=10$ arbitrary loss units | Already net of conditional service effort and relative to the existing schedule; no extra repair cost is subtracted again. |
| Inspection burden | $k_A=k_B=1$ arbitrary loss unit | Burden is incurred even after a negative finding. |
| False-positive behavior | $f_A=f_B=0$ in the initial illustration | Explicit observation simplification; a later extension would need proposed $f_i$ and $h_i$. |
| Horizon | Common $[t,t+\Delta]$, with $v_i$ defined only over that interval | No calendar duration, terminal effect, or failure timing is inferred. |
| Policy alternatives | $a_0,a_A,a_B$ as defined above | Same upper bound of one optional early inspection; feasible contingent service response. |

Do not assign probabilities to $m_1$ and $m_2$ merely to average away routing disagreement. Treat each interpretation separately and, where both remain plausible, include both in the robustness set. A corrected record may justify removing an obsolete interpretation, but requires its explicit evidential rationale.

Evaluate the continuous symbolic thresholds over the stated rectangle and report a small exact table of representative points, including equal detection, unequal detection, a tie boundary, and the exposure-uninformative boundary. A plotted grid can illustrate those thresholds but cannot by itself prove continuous sign stability; use the formulas or bound the full parameter set. Report agreement, disagreement, baseline preference, and unresolved model comparisons wherever obtained. Do not imply that the approved inputs guarantee every desired regime, or tune them after seeing the results without recording the change.

Implementation uses a small deterministic calculation and tests of policy comparison, the baseline check, and ties; it requires no random simulation, package installation, or station data. The results are presented in a numerical table and exact analytical boundaries. The manuscript's data-availability statement must identify the actual synthetic calculation. Execution and validation evidence are recorded separately from these approved inputs.

## 9. Decision-rule revision authorized on 2026-10-26

After reviewing [the Round 1 assessment](16_round1_revision_assessment.md) and the accompanying recommendation, the author instructed: “Zacommituj to co jest i zacznij wdrazac poprawki” (commit the current state and begin implementing the corrections). Commit `0f7a169` preserves the preceding specification, manuscript, results, and reviews. This addendum supersedes the strict-common-preference/fallback selection in Sections 5–8; their historical descriptions are retained as the record of the earlier approved rule.

Keep all Section 8 numerical inputs unchanged. Compare the same three deterministic complete policies, without assigning probabilities to the routing models. At each fixed parameter pair:

1. Remove a policy if another feasible policy has at least as much gain in every retained routing model and strictly more in at least one.
2. Use minimax regret among the remaining policies as the main illustrative selector: minimize the largest within-model gap to the best feasible gain.
3. Report maximin incremental gain as a comparator: maximize the smallest gain relative to the model-specific schedule.
4. Preserve exact tie sets and separately identify any selected policy with a negative gain in a retained model.

No additional nonnegative-gain constraint is imposed. As explained in the approved proposal, minimax regret can select A at `beta=1/45, d_A=0.9`, with gains `0.10/-0.03`; the comparator ties B with the schedule. A future requirement to forbid losses against the baseline would change the feasible set and needs an explicit decision. Maximin incremental gain is not identified with minimax absolute loss when model-specific baseline losses are unknown.

Keep the sensitivity rectangle distinct from the routing set at fixed parameters. Report the whole-rectangle stress comparison separately. The original strict rule may remain in code as a historical diagnostic, but it is no longer the manuscript's recommended selector. Generate the numerical table and geometry for the two-panel decision-region figure from the authoritative calculation; the figure renderer must not repeat the policy analysis. No observation likelihood, population model, randomization, or empirical calibration is added.
