# Review Report — Reviewer 1 (domain expert in predictive maintenance)

**Manuscript:** Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems
**Journal:** Symmetry (MDPI)
**Version reviewed:** PDF dated October 21, 2026 (16 pp., 26 references)

## Summary of the submission

The manuscript proposes "Limited-Data Predictive Maintenance" (LD-PdM) as a named decision regime in which maintenance choices are consequential while dedicated condition information is persistently weak. It organizes the argument around four asymmetries (observability, failure evidence, information cost vs. decision consequence, scale), introduces a conceptual belief state (Eq. 1), an action-conditioned event probability (Eq. 2) and a Bayes-decision rule (Eq. 3), and illustrates the reasoning with a qualitative, hypothetical railway-station example in which an inspection ordering between two automatic doors is first justified and then withdrawn after routing evidence changes. No data, simulation or quantitative result is reported.

## General assessment

The author identifies a real and practically important situation: large populations of moderately critical infrastructure assets (doors, lifts, escalators) for which dense condition monitoring is not deployed, yet maintenance has to be planned. The text is careful not to overclaim and correctly positions itself against Li et al. (2024). The distinction between usage, exposure, condition, event probability, risk and priority (Table 2) is sound and is something practitioners frequently blur.

However, from the standpoint of the PdM/PHM and maintenance-optimization communities, the manuscript currently does not demonstrate a contribution beyond a careful restatement of well-established principles. Each building block — usage/load-based maintenance, covariate-driven reliability models, informative inspection and censoring, POMDP inspection planning, value of information, hierarchical pooling — has a mature literature, much of which is not cited. The "regime" is defined by qualitative conditions that cannot be checked in practice, and the worked example reaches a conclusion that follows trivially from its stated assumptions. In its current form, I do not think the paper would change how a maintenance engineer or researcher approaches such a problem.

## Required revisions (ordered from most to least important)

1. **Demonstrate the added value of the framework against existing maintenance theory.** The decision-theoretic core (Eqs. 2–3, Section 4.2) is the standard POMDP / Bayesian decision formulation; the inspection-as-information argument is the standard value-of-information argument (refs. [5,6]). The paper should state explicitly what an analyst can do with LD-PdM that they could not do with (a) usage/load-based maintenance (e.g., Tinga, 2010, *Reliability Engineering & System Safety*, "Application of physical failure models to enable usage and load based maintenance"), (b) covariate/use-rate reliability prediction (e.g., Hong & Meeker, 2010 and 2013, *Technometrics*), and (c) POMDP inspection planning (e.g., Papakonstantinou & Shinozuka, 2014, *RESS* 130). A comparison table "existing approach — what it assumes — what LD-PdM adds" would be the minimum. Without it, the contribution reads as a renaming exercise, which the author explicitly says they want to avoid.

2. **Provide at least one quantitative illustration.** A conceptual paper may be acceptable, but the central claims (that proxy-based reasoning can support an ordering, that shared bias is not removed by pooling, that an ordering must be withdrawn under changed routing) are all easily demonstrated with a small synthetic model: passenger totals → Dirichlet routing shares → door cycles → exposure-dependent hazard → inspection finding. The author's own companion work (ref. [23]) already contains such a model. Even a two-door toy computation showing the expected value of inspecting A vs. B, and how it changes after the platform reassignment, would turn Section 5.3 from an assertion into evidence.

3. **Make the inclusion criteria operational.** The three conditions in Section 2.1 (lines 73–79) rely on "consequential", "weakly informed" and "material contribution", none of which is defined. Table 1 explicitly disclaims any threshold. A practitioner cannot decide whether their fleet is "in" the regime. I suggest expressing the criteria through quantities already in the paper: e.g., expected value of perfect/sample information of condition channels relative to the cost of acquiring them, or the posterior contraction of the decision-relevant quantity when the dedicated channel is removed. Even a qualitative checklist with worked yes/no answers for door, lift and escalator would help.

4. **Engage with the domain-specific regulatory and maintenance context of the example assets.** Lifts, escalators and powered pedestrian doors are maintained under regulated regimes (e.g., EN 13015 on maintenance instructions for lifts and escalators; EN 16005 on safety in use of power-operated pedestrian doorsets; national inspection rules). The paper says mandatory requirements "constrain the feasible actions" (lines 288–290), but does not discuss what decision freedom actually remains for the operator once these are respected. If mandatory periodic maintenance already fixes most actions, the population-level decision value claimed in Asymmetry 4 needs to be argued, not assumed.

5. **Strengthen and rebalance the literature base.** 26 references is thin for a positioning paper in maintenance. Missing are standard CBM/PHM reviews (e.g., Jardine, Lin & Banjevic, 2006, *MSSP*; Si et al., 2011, *EJOR*), maintenance-optimization reviews (e.g., de Jonge & Scarf, 2020, *EJOR*), soft-sensor literature (e.g., Kadlec, Gabrys & Strandt, 2009), and any PdM work on escalators, lifts, platform doors or station assets, of which there is a growing body. Conversely, several cited works are weak or tangential choices for the claims they support: ref. [8] (feedforward control of a pulp dissolver) and ref. [17] (a journal with a contested indexing record) as evidence for "virtual sensing". Replace them with representative, high-quality sources.

6. **Clarify the relationship to the companion GPECOM study (ref. [23]).** The companion paper contains the actual Bayesian proxy-flow model and scheduling integration for the same station setting. The present manuscript must make clear what is new here relative to [23], and should consider whether the two contributions belong in one paper. A reviewer will otherwise suspect salami slicing in the opposite direction: the conceptual layer of a technical paper published separately.

7. **Discuss the informative-maintenance and censoring issues more concretely.** Section 2.3 correctly notes informative observation, but stops at "a later quantitative model must justify its treatment". Give the reader the relevant modelling options (competing risks, imperfect repair / virtual age models, informative inspection designs) and say which assumptions are typical for the example assets.

8. **Address what happens when the ordering is withdrawn.** In Section 5.3 the decision after withdrawal is "request local usage evidence" and "B does not automatically acquire priority". In practice the planner must still act within the capacity window. Explain the default (calendar policy? random order? both?) and argue why this default is acceptable; otherwise the framework's practical output in the most interesting case is "no recommendation".

9. **Justify the fit with Symmetry.** The "asymmetry" in the title is a metaphor for mismatch between decision value and information availability; no mathematical or physical symmetry concept is used. The author should explain why this is a Symmetry paper rather than one for *Reliability Engineering & System Safety*, *IEEE Transactions on Reliability*, *Eksploatacja i Niezawodność*, or *Applied Sciences*. If possible, formalize the asymmetry (e.g., as a relation between the decision's loss sensitivity and the information content of available channels).

10. **Minor domain points.**
    - Line 40: "We call this regime" in a single-author paper; use consistent voice.
    - Section 2.5: the hierarchical-pooling argument should mention partial pooling explicitly and the dependence of its benefit on between-unit variance.
    - Table 4, row 2: "inspect the less understood asset" is a value-of-information heuristic; say so and cite.
    - Figure 1 duplicates much of Figure 2; consider merging and using the freed space for a quantitative example.
    - Section 6.1 cites section numbers of Li et al. (2024) in detail; this is unusual and can be shortened to the substantive claims.

## Recommendation

**Major revision.**

The topic is relevant and the author clearly understands the pitfalls of proxy-based maintenance reasoning. The manuscript needs a demonstrated contribution beyond existing decision-theoretic maintenance literature, operational inclusion criteria, and at least a minimal quantitative illustration before it can be considered for publication.

## MDPI evaluation grid

| Criterion | Rating |
|---|---|
| Originality / novelty | Low–Average |
| Significance of content | Average |
| Quality of presentation | Average |
| Scientific soundness | Average (sound but largely unverified) |
| Interest to the readers | Average |
| Overall merit | Below average |
| English level | Fine; minor style issues |
