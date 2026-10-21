# Review Report — Reviewer 3 (assesses the scope of work strictly from the manuscript itself)

**Manuscript:** Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems
**Journal:** Symmetry (MDPI)
**Version reviewed:** PDF dated October 21, 2026

## Approach of this review

I evaluated the manuscript only on what it states and shows, without relying on outside knowledge of the author's other work. My main question was: after reading the paper, can I say clearly what was done, what was found, and what I can now do that I could not do before?

## Summary as I understood it

The paper introduces a name (LD-PdM) for situations where maintenance decisions matter but direct condition data are weak. It lists three conditions for this situation, describes four "asymmetries", separates six quantities (evidence, usage/exposure, condition, event probability, risk, priority), writes three general equations, and walks through an invented station example with two doors. It ends by saying that predictive and operational performance are for future work.

## General assessment

The paper is written carefully and is internally cautious. However, I found it difficult to identify the concrete outcome of the work. The abstract and introduction promise "criteria for identifying the regime", "tracing an action rationale" and "recognizing when an ordering must be withheld". In the body, the criteria are qualitative and explicitly come without thresholds, the rationale-tracing is shown only through a single narrative example with assumed inputs, and the "withholding" rule amounts to "stop if the assumptions turn out false". The paper repeatedly tells the reader what it does *not* claim; it is much less clear about what it *does* deliver. A reader who is not already persuaded will likely finish the paper unsure whether anything was produced beyond vocabulary.

## Required revisions (ordered from most to least important)

1. **State the deliverables of the paper concretely and map them to sections.** Add, at the end of the Introduction, a short list or table: "Contribution — where in the paper — what form it takes (definition, table, equation, procedure, example)". At present the three contributions on lines 57–65 are phrased abstractly ("gives operational inclusion criteria", "separates the inferential links", "applies these distinctions"). The reader should be able to point at the artefact for each.

2. **Resolve the inconsistency in the role of the four asymmetries.** The abstract (lines 5–9) says four asymmetries "organize the argument" and the Introduction (line 58) says the criteria are "organized around four asymmetries". However, Section 2.5 (lines 158–160) states that only weak information and consequential choices are defining conditions, while rare events and population scale "need not occur in every LD-PdM setting". Then it is unclear why the title, abstract and section structure are built around four asymmetries. Either explain the logical status of each asymmetry (defining / contributory / opportunity) early in the paper, or restructure.

3. **Provide a usable procedure.** The Conclusions (lines 506–508) state a three-step examination: establish the regime, identify what each source informs, state the assumptions linking it to an action. This procedure is the most usable output of the paper but appears only in the conclusions. Present it explicitly in the body as a numbered procedure with inputs and outputs for each step, and then apply it step by step in Section 5.

4. **Define the key terms of the inclusion criteria.** "Consequential", "weakly informed", "feasible set of condition-sensitive channels", "material contribution" and "persistent" are central to deciding whether a case belongs to LD-PdM. Only "persistent" is defined (lines 80–82). Without definitions, two readers applying the criteria to the same case could reach opposite conclusions, which contradicts the claim that the criteria are "operational".

5. **Make the worked example deliver a non-trivial conclusion.** In Section 5.3, the reader is asked to assume comparable mechanisms, controller settings, baseline beliefs, inspection burdens, detectability, benefits, greater cycle exposure for A, and an exposure–finding relationship (lines 345–353). Given all these assumptions, "inspect A first" follows immediately. The second half (lines 360–369) shows that if one assumption fails, the conclusion fails. Neither part shows the framework doing work that ordinary reasoning would not. Consider an example in which the framework leads to a conclusion that a naive approach (e.g., "rank by passenger count") would get wrong, and show why.

6. **Clarify what "conceptual" covers and what is out of scope, in one place.** Statements limiting scope appear throughout (lines 19–20, 65, 186–188, 234–235, 258–259, 286, 332, 367–369, 399–400, 453–455, 476–478, 511–512). Collect them into a short "Scope and limitations" subsection, and remove the repeated disclaimers elsewhere. This would also make the paper shorter and easier to follow.

7. **Explain the connection between the title and the content.** The title speaks of "asymmetric relations between needs and data availability". The body discusses four asymmetries of different kinds. A one-paragraph explanation of what exactly is asymmetric in each case — two quantities, and in what sense they are not aligned — would make the title meaningful. Also explain why this is relevant to a journal focused on symmetry.

8. **Explain the evidential status of the station setting.** Line 65 says that "the station setting and evidence are hypothetical", while Section 5.2 refers to a "related door-and-elevator study" (ref. [23]). The reader needs to know whether the station, its devices and its data exist, whether any element of the example comes from that study, and what the relationship between the two works is.

9. **Make the tables self-explanatory.** Table 1 mixes three types of statements in one row without telling the reader how to read across. Table 4 has five scenarios but the text (line 378) introduces it in one sentence. Add a sentence per table explaining how it should be read and what the reader should take from it.

10. **Small clarity issues.**
    - Line 40, "We call this regime" — single author.
    - Lines 37–39: "the question here is how to characterize..." reads as if a research question is stated, but no answer in the form of a characterization is later summarized. Restate the answer in the Conclusions.
    - Section 6.3 describes evaluation that "would" be needed; it is unclear whether the author plans it or recommends it to others.
    - The abbreviation list omits terms used in the figures (e.g., HVAC is not expanded at first use, line 175).

## Recommendation

**Major revision.**

The manuscript is coherent and cautious, but its actual outputs are not clearly identifiable, the central criteria are not defined sharply enough to be applied, and the example does not demonstrate value beyond common sense. With a clearer statement of deliverables, a usable procedure and a more discriminating example, it could become a useful position paper.

## MDPI evaluation grid

| Criterion | Rating |
|---|---|
| Originality / novelty | Average |
| Significance of content | Low–Average |
| Quality of presentation | Average (clear sentences, unclear outcome) |
| Scientific soundness | Average |
| Interest to the readers | Average |
| Overall merit | Average |
| English level | Good |
