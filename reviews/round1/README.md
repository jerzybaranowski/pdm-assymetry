# Review round 1 — simulated reviews

Simulated peer reviews of `output/pdf/ld-pdm-conceptual-revision.pdf` (version dated October 25, 2026), prepared for a planned submission to *Symmetry* (MDPI). Line numbers refer to the PDF's line numbering.

## How this round was produced

Each review was written by a separate agent that worked independently. No agent saw the round-0 reviews, the response matrix, the other round-1 reviews, or any other repository file. Each worked only from the extracted manuscript text and the rendered page images. Reviewers 1, 2 and 4 could also use web search to check literature and references. Reviewer 3 used the manuscript only, with no outside sources.

| File | Reviewer persona | Recommendation |
|---|---|---|
| `review1_pdm_expert.md` | Domain expert in predictive maintenance | Major revision |
| `review2_technical.md` | General PdM background, strong technical/mathematical orientation | Major revision |
| `review3_scope_reader.md` | Judges scope of work strictly from the manuscript | Major revision |
| `review4_ai_skeptic.md` | Hostile to AI-assisted manuscripts | Reject |

## Issues raised independently by several reviewers

1. **The fallback rule selects a dominated action (all four).** In the two-door example, keeping the schedule (π0) is chosen even where inspecting B gains under both routing models (Table 4; lines 472–479). Reviewers 2 and 4 each estimate that this happens over about 44% of the declared (β, d_A) parameter box. Reviewers 1 and 2 ask for an admissible rule such as maximin, minimax regret or model averaging, and they note that these criteria disagree at β = 0.2, d_A = 0.9.
2. **The definition and checklist are not operational (all four).** "Consequential", "weakly informed" and "material" have no test or threshold. Reviewers 1 and 2 suggest value-of-information criteria. Reviewers ask for worked "no" and "unresolved" cases.
3. **"Asymmetry" is not defined as an object of analysis (all four).** The term labels the title and Section 2 but is not used in the procedure or the example. Reviewer 2 notes that the example holds consequences equal, so it does not exercise the asymmetry. Journal fit with *Symmetry* is questioned.
4. **The example does not exercise the proxy evidence chain (2, 3, 4).** The paper assumes q_i = 0.1 + βx_i directly, and the evidence never enters a calculation. "Bayesian inference" in the keywords is not matched by any inference.
5. **Results follow from the inputs (1, 2, 4).** Reversals are built into the parameter choices: d_A < d_B, and m2 changes only x_A. Reviewers ask for a decision-region figure over (β, d_A).
6. **Positioning against existing maintenance theory (1, 2, 4).** Reviewers name RCM/P-F interval logic, risk-based and delay-time inspection, preposterior and value-of-information analysis, and PdM feasibility frameworks.
7. **Increment over the companion paper [20] is unclear (1, 4).** Its public abstract already contains the station graph, Bayesian routing shares and cycle conversion. It uses "Low-Data" where this paper uses "Limited-Data".
8. **The name "Limited-Data PdM" conflicts with the definition (1, 2, 3, 4).** The paper separates the regime from sample count, yet the name points to data quantity.
9. **Eq. (1) on shared error is overstated and unused (2, 3, 4).** Reviewer 2 shows that a shared exposure error cancels in exposure differences but not in the inspection comparison.
10. **Reproducibility (all four).** The data availability statement points to "the manuscript source", which readers cannot access.
11. **Back matter (1, 3, 4).** The Funding statement has no grant agreement number. The Acknowledgments paragraph is printed in red. Reviewer 4 asks for a more specific AI-use disclosure.

## Notes on verification

- Reviewers 1, 2 and 4 independently recomputed Eq. 6, Table 4 and the Section 5.4 boundaries. All three report that the arithmetic in the paper is correct. Reviewer 3 checked the same from the manuscript alone and agrees.
- Reviewer 4 resolved all 23 DOIs in Crossref with matching metadata. The only differences are online-first years for [1] and [14].
- Reviewer 1 could not confirm the title and authors behind the DOI of [19]. Reviewers 1, 2 and 4 found [20] as arXiv:2603.14384 but could not confirm the GPECOM proceedings record.
- Reviewer 1 states a specific grant agreement number for FP3-IAM4Rail. Check it against the grant documents before using it.
- The reviewers' recomputation scripts are in the session scratchpad, not in the repository.
