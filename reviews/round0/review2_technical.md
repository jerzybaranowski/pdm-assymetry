# Review Report — Reviewer 2 (general PdM background, strong technical/mathematical orientation)

**Manuscript:** Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems
**Journal:** Symmetry (MDPI)
**Version reviewed:** PDF dated October 21, 2026

## Summary

The paper argues for a maintenance regime (LD-PdM) in which condition-sensitive measurements are weak and decisions rely on proxies, context and history. It introduces a belief state over usage, condition and parameters (Eq. 1), an action-conditioned failure probability (Eq. 2) and an expected-loss decision rule (Eq. 3), and then discusses a qualitative two-door railway-station example. All quantitative content is explicitly deferred to future work.

## General assessment

I read the paper hoping for a formal model of the proposed regime. What is provided is mainly a carefully worded verbal argument with three generic equations that are not used anywhere afterward. The equations are correct in spirit but are textbook Bayesian decision theory; none of the subsequent claims is derived from them. Several statements that are presented as conceptual insights (shared bias does not average out; pooling needs exchangeability; inspection is valuable only if it can change the decision; ranking stability is not correctness) are standard results that could be shown in a few lines of mathematics or a small simulation. The paper would be considerably stronger and shorter if it formalized its core objects and demonstrated them numerically.

## Required revisions (ordered from most to least important)

1. **Turn the conceptual chain into an explicit generative model.** Figure 2 and Table 3 describe a chain station flow → device use → exposure → condition → event → action. Write it as a model, e.g.

   - passenger totals N_t with observation error;
   - routing shares π ~ Dirichlet(α), dependent on platform assignment;
   - door cycles C_i = g(π_i N_t, κ_i) with a grouping/reopening factor κ_i;
   - cumulative exposure X_i = Σ C_i;
   - hazard h_i(t) = h_0(t) exp(β X_i) or a degradation process driven by X_i;
   - inspection outcome Y_i | D_i with detection probability.

   This does not need to be fitted to real data. It would make every "assumption" in Table 3 a named parameter or structural choice, and would allow the reader to see exactly which ones are identifiable.

2. **Compute the worked example.** With the model above, Section 5.3 can be computed: expected loss of "inspect A first" vs. "inspect B first" vs. "default schedule", before and after the platform reassignment. Report the value of information of the local counting exercise. This would make the claim "the ordering must be withdrawn" a result rather than a narrative, and would show under which parameter ranges the ordering is robust. A sensitivity plot over the exposure–finding coefficient β and the routing uncertainty would be the natural figure.

3. **Formalize "weakly informed" and the regime criteria.** Section 2.1 is the core definition of the paper, yet "weakly informed", "material contribution" and "consequential" are undefined. Possible formalizations: (a) the decision-relevant quantity θ has small mutual information with the available dedicated channels, I(θ; Z_dedicated | E_other) < ε; (b) the expected value of sample information of the dedicated channel is below its lifecycle cost; (c) the posterior of θ remains prior-dominated (e.g., prior-to-posterior contraction below a threshold). Choose one and state the criteria in terms of it. Table 1 then becomes a set of illustrative cases of the formal definition.

4. **Fix the notation in Eq. 2 and clarify its causal semantics.** Writing Pr(· | E_{1:t}, M, a) with an action inside the conditioning bar is ambiguous. The text (lines 192–193) explicitly wants an interventional quantity "rather than an association conditional on an action selected by an earlier policy". Use an interventional notation (e.g., Pr_a(·) or Pr(· | do(a), E_{1:t}, M)) or define a as an index of the transition kernel. Also clarify whether S^a in Eq. 3 is the same object as the state D in Eq. 1, or a richer system trajectory, and how T^F relates to D.

5. **Connect Eq. 1 to the rest of the paper or remove it.** The belief state b_{i,t}(u,d,θ) is never used. Either use it (e.g., to show that under the station observation model the marginal over d equals the prior conditional on u, which is the formal statement of "exposure does not establish condition"), or drop it and keep Eq. 3 only.

6. **Formalize the shared-bias and pooling claims.** Sections 2.5, 3.3 and Table 4 state that common proxy errors do not average out and that duplicated sources are not independent confirmation. Write a short derivation: if X̂_i = X_i + b + ε_i with common bias b, then the variance of a population mean shrinks only in the ε component, and the ranking of i vs. j is unaffected by b but affected by group-specific routing errors. This is two lines of algebra and directly supports the "uniform offset vs. group-specific error" remark in Table 4, which is currently unexplained.

7. **State identifiability results, not only warnings.** Section 6.4 ("different combinations of deterioration parameters and prior condition can explain the same records") is an identifiability statement. In the proposed model it can be made precise: e.g., with only exposure and right-censored replacement records, β and the baseline hazard are confounded unless some failure/inspection outcomes are observed. Give the condition.

8. **Define the decision objective for population allocation.** Section 4.3 states that ranking by exposure, expected consequence and expected inspection value "can give different orders". Provide the three objectives formally and a minimal example (three assets) where they disagree. This is the kind of result a technical reader expects in a framework paper.

9. **Reduce verbal redundancy.** Many paragraphs restate that a proxy does not establish condition (Sections 2.2, 3.1, 5.2, Table 2, Table 3, Table 4, Figure 1 caption, Figure 2 caption, Section 6.4). Once the model is explicit, most of these can be replaced by a single reference to the model structure. The freed space should go to the computation in item 2.

10. **Relation to Symmetry.** The journal is concerned with symmetry/asymmetry as a structural concept. If the asymmetry is to be more than a title word, it should be expressed formally, e.g., as an asymmetric relation between the loss function's sensitivity to the condition variable and the Fisher information (or mutual information) available about it. Otherwise the editor may consider the paper out of scope.

## Minor issues

- Eq. 3: the arg min over A_t yields a set; the notation a* ∈ arg min is fine, but specify the information pattern (open-loop vs. closed-loop) since the text then says inspection must be valued with subsequent conditional actions, i.e., a closed-loop policy.
- Line 184: U_{i,t} is described as "usage or accumulated exposure"; these are different quantities in Table 2. Use two symbols.
- Line 190: define Δ units and whether the horizon is calendar time or operating time.
- Table 1 and Table 4 are difficult to parse in the PDF because of column wrapping; consider a different layout or shorter cells.
- Figure 1: arrows from "Probabilistic inference" to all inferred quantities do not distinguish which inputs inform which outputs; the dashed/solid convention used in Figure 2 should also be used in Figure 1.
- Single-author paper using "We" (line 40).
- Several references (e.g., [8], [9], [17]) are odd choices as representatives of virtual sensing; standard soft-sensor and virtual-sensing reviews would be more appropriate.

## Recommendation

**Major revision.**

The idea is reasonable, but the paper currently has the form of an essay with decorative equations. A minimal generative model and a computed version of the station example are needed to substantiate the claims and to justify publication in a journal that expects technical content.

## MDPI evaluation grid

| Criterion | Rating |
|---|---|
| Originality / novelty | Average |
| Significance of content | Average |
| Quality of presentation | Average (verbose) |
| Scientific soundness | Low–Average (claims not derived) |
| Interest to the readers | Average |
| Overall merit | Below average |
| English level | Good; overly dense |
