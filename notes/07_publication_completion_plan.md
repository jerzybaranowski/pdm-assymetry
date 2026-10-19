# Publication completion plan for the conceptual LD-PdM paper

**Review date:** 2026-10-19\
**Manuscript reviewed:** `paper/template.tex`, repository HEAD `2f6436b`\
**Status:** revision plan prepared; manuscript revision remains open.

The author confirmed on 2026-10-19 that the paper is conceptual, no empirical data are available, and submission should follow as soon as possible. The author subsequently allowed a high-level simulation if useful and confirmed that the manuscript is invited under its existing title. Preserve that title and keep publication-type selection off the critical path. Completion requires a defensible conceptual contribution and a worked example; a compact synthetic illustration is optional, while field validation and a detailed station model are outside the current scope.

`AUDIT.md` remains the authoritative issue register. This document supplies its execution sequence, proposed paragraph outline, acceptance criteria, and stopping rules. It does not record approval of new scientific claims or figure changes.

## Completion target

Preserve **Limited-Data Predictive Maintenance (LD-PdM)** and the paper's system-level identity. The proposed contribution is a precise description of an observation and decision regime: consequential maintenance choices must be made when dedicated condition-sensitive information is persistently weak and heterogeneous indirect evidence plays a material role.

The completed paper should supply four things:

1. An operational definition with inclusion criteria, boundary cases, and explicit overlap with adjacent approaches.
2. A coherent framework connecting available evidence, assumptions, latent quantities, uncertainty, and maintenance choices.
3. A railway-station example that follows those connections through to qualitative decisions and shows where inference must stop.
4. A bounded research agenda describing how the framework could be evaluated later, without claiming that such evaluation has occurred.

The paper may establish conceptual distinctions and conditional implications. It cannot establish prevalence, industrial ROI, calibrated failure probabilities, improved scheduling, or reduced downtime from its present materials. An optional synthetic illustration would support only conclusions within its declared assumptions.

## Findings that change the existing plan

### Positioning must extend beyond Li et al.

Li et al. already cover limited monitoring quantity/quality, investment barriers, incomplete and imbalanced evidence, uncertainty, and the PHM maintenance-execution stage. Integrating that review is necessary; a contrast between classification and decisions would misrepresent it. See the [publisher's full text](https://link.springer.com/article/10.1007/s10462-024-10820-4) and `literature/02_positioning_vs_li2024.md`.

Partial observability, maintenance decisions, and information value also have established treatments. Two verified starting points are [Value of condition monitoring in infrastructure maintenance](https://doi.org/10.1016/j.cie.2013.05.022) and Memarzadeh and Pozzi's [Value of information in sequential decision making](https://doi.org/10.1016/j.ress.2016.05.014). The latter explicitly connects noisy observations, component inspection, permanent monitoring, and system-level scheduling through partially observable Markov decision processes (POMDPs). Their publisher abstracts and indexed introductory material were available; a detailed claim audit still requires reading the relevant full passages.

The defensible contribution must therefore be an engineering synthesis and operational characterization of the proposed regime. Neither Bayesian beliefs nor decision support under partial observability should be presented as newly introduced by LD-PdM.

### GPECOM is published and already contains the technical example

The [AGH publication record](https://badap.agh.edu.pl/publikacja/169113) lists Bauer and Baranowski's GPECOM paper on pages 987–992, available online from 2026-07-02, DOI `10.1109/GPECOM70462.2026.11578618`. Its [public preprint](https://arxiv.org/html/2603.14384v1) contains proxy-flow modelling, cycle estimates, probabilities of reaching service conditions, and cost-aware scheduling. Those service-condition probabilities must not be relabelled as probabilities of physical failure. The preprint also cites this conceptual manuscript as submitted work; reciprocal citations do not independently validate either paper's claims.

Keep GPECOM as an attributed technical instantiation. The conceptual paper should stand on its own definition and argument. Check the version of record before reusing text, results, or artwork; its complete content was not compared with the preprint in this review.

### The model vocabulary needs repair

At `paper/template.tex:668`–`676`, risk, degradation pressure, condition, urgency, and priority are not sufficiently separated. Dedicated sensors also provide indirect evidence of condition; latent degradation and RUL are not exclusive to LD-PdM. Define the distinction through the availability and informativeness of condition-sensitive channels rather than a literal measured-state/latent-state division.

Population evidence can support aggregate decisions under suitable pooling assumptions. It cannot automatically resolve individual rankings, shared proxy bias, or differences between asset classes. Higher uncertainty can justify information gathering under a suitable decision criterion; it does not automatically justify intervention.

### A successful build hides a front-matter defect

A clean temporary copy compiled with `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error template.tex`: 23 pages, no unresolved citations/references, and no BibTeX errors. All 27 bibliography entries are cited in the active manuscript.

Visual inspection of six pages exposed a more serious defect: `template.tex:126` starts the document before the abstract and keywords, and `:129` uses an `abstract` environment although the bundled MDPI class expects the one-argument `\abstract{...}` command. The PDF loses the initial “P” of “Predictive” and displays neither the Abstract nor Keywords label. See `paper/Definitions/mdpi.cls:638`–`639`.

There are also two overfull boxes, in the proxy table (`template.tex:625`) and inference-chain figure (`inferencechain.tex:73`), repeated header-height warnings, and an `xcolor` warning. Fifteen article entries have empty pagination and no alternative article identifier. Bibliographic author fields also need checking against publisher records. Compilation is established for the current clean source copy; final layout and submission readiness are not established.

## Ordered work packages and closure criteria

All packages below are open except the author's choice of a conceptual route and the baseline build check. Package completion requires the listed artifact or check, rather than an assertion that an issue was considered.

| Order | Work package | Concrete deliverable | Closure criterion |
|---|---|---|---|
| 1 | Freeze the contribution | One contribution paragraph and operational inclusion criteria | Preserve LD-PdM and the invited title; distinguish the contribution from Li, virtual sensing, risk-based maintenance, and POMDP/VoI work. |
| 2 | Audit consequential claims and references | A compact claim–source matrix under `literature/`, plus verified metadata for the references retained | Each consequential claim is supported at its stated strength, explicitly conditional, or removed. Li is cited before/at the definition; GPECOM metadata and contribution boundary are corrected. |
| 3 | Specify the conceptual framework | A consistent glossary, assumption register, qualitative decision rule, and worked station scenario | Evidence, usage, exposure, condition, event probability, consequences, and priority remain distinct. Every inferential link has a stated assumption and limitation. No fabricated parameters or results. |
| 4 | Revise the manuscript around that framework | Revised Sections 2–6, then Introduction, Discussion, abstract, and conclusion | All sections state the same conceptual contribution. Remove unsupported promises of simulation, superiority, validation, or an existence proof; describe any actual synthetic illustration precisely. |
| 5 | Align figures, tables, and technical source | Approved figures and captions, corrected front matter, verified bibliography, clean source | Conceptual visuals are explicitly schematic; any generated results are labelled synthetic. Visuals agree with the prose. Abstract and keywords render correctly. Significant layout warnings and metadata defects are resolved. |
| 6 | Complete the submission review | Final PDF, build record, source bundle prepared locally, declarations, and cover-letter draft | Every applicable AUDIT item has closure evidence; author facts are confirmed; final PDF is inspected. Submission itself requires separate authorization. |

Packages 1–3 define the scientific content before package 4. Source verification and routine technical fixes can proceed alongside them. Publication metadata supplied only by the author can be collected while the revision proceeds.

## Minimum conceptual specification

### Operational definition and boundary cases

Use qualitative inclusion criteria rather than invented numerical cutoffs:

- A specified maintenance choice has a consequential operational or economic outcome.
- At least one relevant condition-sensitive channel is persistently weak, unavailable, or constrained within the feasible information budget.
- Proxy, contextual, historical, or prior evidence materially affects reasoning about that choice.
- The framework explicitly represents the limitations of that evidence and their implications for action.

Show one station example that satisfies the criteria and one counterexample: a small labelled condition dataset with an otherwise informative monitoring channel does not, by sample count alone, establish the proposed regime. Describe mixed cases as overlapping regimes rather than forcing mutually exclusive labels.

The four existing asymmetries can remain the organizing framework. Explain whether each is a defining condition, a common complication, or a possible consequence. Sparse failures and a large population need not become universal prerequisites unless the definition explicitly requires them.

### Glossary and assumption register

| Concept | Meaning to keep distinct | Required treatment |
|---|---|---|
| Available evidence | Observations, context, histories, documentation | State what is assumed available in the illustrative setting; do not imply an actual station dataset exists. |
| Usage and load | Device-specific operating activity and mechanical burden | Explain the link from passenger traffic separately for each illustrated asset function. |
| Exposure and stress | Accumulated operational burden | Present as a model-dependent intermediate quantity, distinct from measured damage. |
| Condition or degradation | Physical state and its evolution | Identify what proxy evidence cannot determine without additional assumptions or inspection. |
| Event probability | Probability of a specified future event over a stated horizon | Distinguish failure, service-condition exceedance, and inspection findings. Do not invent a calibrated probability. |
| Risk and consequences | Event likelihood together with the relevant consequences | Keep monetary loss, service disruption, accessibility, and safety conceptually distinct. |
| Priority and action | Choice made using beliefs, consequences, and constraints | Explain the action rule; avoid treating priority as another physical latent state. |

For each arrow in the case, record: evidence source, variable informed, engineering assumption, possible confounder, and what would require inspection or calibration. This can be one concise manuscript table instead of an additional model or figure.

### Worked qualitative station decision

Develop a hypothetical comparison of two similar automatic-door assets with different assumed traffic exposure, together with a case where uncertainty prevents a reliable ordering. Keep elevator examples as attributed illustrations of different passenger-to-cycle relationships. Do not classify an entire asset class as non-critical: specify the service function and decision being discussed.

Use a qualitative table with columns **available evidence → conditional inference → candidate action → rationale → limitation**. It should cover:

1. Repeated proxy evidence suggesting higher exposure, sufficient to consider earlier inspection under otherwise comparable conditions.
2. Similar expected exposure but weaker evidence, where the value of resolving uncertainty depends on consequences and whether inspection could change the action.
3. Conflicting evidence or a changed traffic regime, where a previously useful proxy relationship should be reconsidered.
4. A common source of bias across all assets, where aggregation does not remove the uncertainty.
5. An uninformative proxy, where the framework cannot justify differentiating assets and the planner retains the applicable existing service rule or seeks better evidence.

The qualitative example demonstrates traceable reasoning and its limits. It does not establish that the proposed action outperforms a calendar policy. Existing safety and mandatory service requirements remain constraints on the example, without making claims about particular regulations.

A short symbolic expected-loss rule is an optional clarification, not a new optimization contribution. A clearly specified qualitative rule is sufficient if it explains the same connection between beliefs, consequences, feasible actions, and information gathering. If notation is retained, define its event and horizon and stop conflating urgency with probability.

### Economics and uncertainty

Treat sensing economics as a condition of applicability. Separate acquisition, installation/integration, and operation/maintenance costs. Where sources do not establish station-specific economics, use conditional wording and qualitative trade-offs. Do not add assumed monetary values to make the argument appear empirical.

State the conditions for pooling information across assets and the effects of shared bias and heterogeneous device mechanisms. Separate uncertainty about an asset from the decision value of an inspection. Censoring can remain a methodological limitation and future evaluation requirement; implementing a censoring model is outside this conceptual revision.

## Optional high-level synthetic illustration

**Recommendation:** complete the conceptual specification first. A worked qualitative decision is sufficient for the conceptual claim. Add one small synthetic illustration only if it clarifies an implication that the tables and diagrams leave unconvincing. It should answer **when weak proxy information can differentiate inspection attention, and when noise or misspecification prevents useful differentiation**. Repeating the GPECOM scheduling example would add little to this paper.

A bounded design would generate heterogeneous latent usage/exposure for similar hypothetical assets and expose the planner to a noisy proxy. Compare a fixed inspection order, proxy-based prioritisation, and an ideal exposure-information reference under the same inspection budget. Vary proxy informativeness and shared bias, including an uninformative case and a misleading case. Use selection of high-exposure assets or exposure captured by the inspection budget as the outcome. These are exposure-based inspection objectives, not failure-risk reduction or demonstrated maintenance savings. The reference is ideal for that stated objective, not a universal optimal maintenance policy.

Specify how shared error affects the objective: a uniform offset can distort absolute exposure without changing its ordering, whereas a shared routing error affecting a particular zone or group can distort rankings. Do not interpret unchanged rankings under a uniform offset as general robustness to common bias.

If implemented, the illustration must separate its data-generating assumptions from what the planner knows, and define how uncertainty affects the selection rule. A simple noisy-score ranking is insufficient to demonstrate the paper's broader claims about uncertainty-aware decision support. A single compact result figure or table and a short methods description should suffice. Asset count, budget, distributions, noise levels, bias mechanisms, repetitions, and uncertainty summaries must be specified before implementation; no such numerical protocol has yet been approved.

This illustration is optional, not an unresolved prerequisite. Its implementation would add a small reproducible Python script, fixed seeds, an explicit assumptions file, appropriate behavioural tests, and generated outputs clearly identified as synthetic. Any data-based figure follows the scientific-figures workflow. The data-availability statement would then need to acknowledge generated synthetic data. If the illustration grows into degradation calibration, failure simulation, scheduling optimization, or industrial cost estimation, defer that extension and finish the conceptual paper.

## Proposed paragraph outline

Each paragraph bullet below carries one intended message. Figure/table bullets are separate. The outline is a revision proposal within the existing invited title.

### 1 Introduction

- **Background:** PdM includes maintenance decisions as well as condition assessment and prognostics. Use the established reviews without portraying all PdM as classification (`Selcuk20171670`, `Carvalho2019`, `Cinar2020`).
- **Prior art:** Small-data PHM already addresses limited monitoring evidence and persistent acquisition barriers; acknowledge Li et al. before naming LD-PdM.
- **Gap:** Explain why the availability and interpretation of indirect evidence deserve an explicit system-level characterization, while acknowledging existing Bayesian maintenance and information-value analysis.
- **Contribution:** State the operational definition, four-asymmetry synthesis, evidence-to-action framework, and worked conceptual station example.
- **Scope:** Identify the paper as conceptual and provide a roadmap matching the revised sections.

### 2 The LD-PdM regime and its asymmetries

- **Definition:** State inclusion criteria and the distinction between sample scarcity and weak decision-relevant information channels.
- **Boundary:** Explain overlapping and counterexample cases; condition information is inferential even in many sensor-rich systems.
- **Observability:** Describe the availability and limitations of dedicated versus indirect evidence.
- **Failure evidence:** Explain rarity, heterogeneity, missing records, and censoring as distinct complications, with appropriately scoped sources.
- **Economics:** Describe the conditional lifecycle trade-off governing additional information acquisition.
- **Population:** Explain how aggregate planning value can coexist with unresolved individual states, including pooling assumptions and common bias.
- **Table:** Map the four asymmetries to their modelling implications and limits; retain the existing observability diagram only if it adds a necessary distinction.

### 3 Evidence and belief formation

- **Variables:** Separate observed inputs, contextual assumptions, usage, exposure, condition, event probability, and consequences.
- **Proxy interpretation:** Explain that each source informs a particular link; cross-domain indirect-sensing studies support analogies, not station validation.
- **Priors:** Explain the contribution of documentation and engineering judgment, including their sensitivity and provenance.
- **Representation:** Present a transparent dependency/belief structure and identify unidentifiable links. One explicit formulation replaces repeated generic justifications of Bayesian methods.

### 4 Maintenance choices under weak information

- **Decision:** Specify the candidate actions, planning horizon, and consequences at a conceptual level.
- **Rule:** Explain how beliefs, constraints, and consequences affect inspection, service, or deferment.
- **Information:** Distinguish intervention priority from the value of collecting evidence.
- **Population:** Explain resource allocation without asserting that aggregation creates informative rankings automatically.

### 5 Worked station example

- **Setting:** Introduce a hypothetical station configuration and the available evidence assumed for the example.
- **Mapping:** Trace passenger context to device usage and exposure; distinguish this from unmeasured degradation.
- **Table:** Present the evidence/assumption register for the inference chain.
- **Figure:** Retain a corrected conceptual inference-chain diagram if approved.
- **Decisions:** Walk through the qualitative scenarios above and explain the limits of each action rationale.
- **Table:** Show evidence, conditional inference, action, rationale, and limitation; no numerical rankings or results.
- **Companion work:** Explain the specific role and distinct contribution of the published GPECOM instantiation.
- **Optional synthetic illustration:** If included under the bounded design above, state its question, assumptions, result, and interpretation in separate short paragraphs, with a separate figure/table bullet in the implementation outline.

### 6 Discussion and research implications

- **Positioning:** Compare LD-PdM with small-data PHM, indirect/virtual sensing, risk-based maintenance, and POMDP/information-value work; identify the synthesis being offered.
- **Decision relevance:** Explain what a later evaluation should measure; distinguish proposed evaluation criteria from achieved improvements.
- **Failure conditions:** Discuss weak or misleading proxies, non-transferable priors, common bias, and changing context.
- **Applicability:** Explain conditional sensing economics and asset/function criticality without prevalence or ROI claims.
- **Digital representation:** Keep a concise optional integration-layer discussion; avoid requiring a full digital twin.
- **Research agenda:** State bounded empirical and computational questions for future work.

### 7 Conclusions

- **Contribution:** Restate the conceptual characterization and evidence-to-action logic actually developed.
- **Boundary:** State what the station illustration clarifies and what still requires empirical evaluation.

Merge the current Sections 5 and 6 into the worked example and remove repeated framing across Sections 2–4 and Discussion. The current paper already has ample prose; completion should replace repetition with precise content rather than expand every section.

## Claim and citation audit priorities

| Claim or source | Required action before closure |
|---|---|
| Novelty based on scarcity, costs, uncertainty, or decisions | Rewrite around the conceptual synthesis; acknowledge Li and established decision-analysis approaches. |
| Directly measured degradation in ordinary PdM | Replace the false dichotomy with condition-sensitive evidence channels and their informativeness. |
| Station sensing is usually uneconomic | Support the stated scope or make it a conditional applicability assumption. |
| Aggregation stabilizes inference and improves decisions | State pooling conditions and distinguish aggregate burden from individual ranking. |
| Most proxy literature omits uncertainty / LD-PdM lacks a canon | Verify a bounded source set or remove the prevalence/absence claim. A systematic review is not needed for this paper. |
| `Straub2015` | Verify what the Bayesian updating algorithm paper supports; narrow broad decision-theory attributions or cite a directly relevant source. |
| `Bourinet2016210` | Separate computational rare-event estimation from scarcity of historical failure observations. |
| `Zeng2016253` | Use for interval-censoring methodology; do not present it as evidence about station maintenance records. |
| `Baraldi2015176`, indirect-sensing papers, `Ma2020` | Retain useful methodological analogies with their actual application and data assumptions. |
| `GPECOM2026LdPDM` | Update publication metadata; distinguish service thresholds from failure probability and avoid circular validation. |

Check publisher metadata for every retained bibliography entry, including author surname ordering, article numbers, page ranges, year, title, and DOI. Preserve established BibTeX keys. Add candidates to `paper/extracted.bib` when they are actually cited. `Bauer2025` remains optional and can be explicitly declined if it supports no necessary claim.

## Figure and source work

| Existing source | Planned treatment for the conceptual route |
|---|---|
| `paper/diagram.tex` | Review “unobservable” and risk/probability labels against the definition; preserve explicitly conceptual status. |
| `paper/inferencechain.tex` | Correct the direction/meaning of the prior-knowledge link and the excessive width; align node vocabulary with the glossary. |
| `paper/conceptual_heatmap.tex` | Keep only if the schematic spatial message adds information. Any retained shading must be described as hand-specified schematic emphasis, not inferred output. |
| `paper/pioritisationoutput.tex` | Replace undefined relevance/uncertainty regions with the qualitative decision table, or revise the figure under an approved specification. Avoid arbitrary quantitative priority thresholds; correct the filename if retained. |

Figure content changes follow `tikz-diagrams` with a concrete approval plan. A data plot is needed only if the optional synthetic illustration is selected. Inspect the final article PDF after source changes; successful compilation alone is insufficient.

Fix the MDPI abstract/keyword declaration, single-author class option, year inconsistency, affiliation presentation, funding grammar, conflicts grammar, and AI statement. Record actual AI assistance and tools used; do not infer a historical tool version or reduce substantive assistance to language correction. The [MDPI AI policy](https://www.mdpi.com/ethics) requires appropriate disclosure of substantive GenAI use. Without a synthetic illustration, retain a truthful statement that the conceptual study created no new data; if an illustration is added, disclose its generated data and code instead.

## Invitation and remaining author facts

The author confirms an invitation under **Asymmetric Relations Between Needs and Data Availability in Predictive Maintenance Systems**. Retain the title and Symmetry destination. Publication category is an administrative detail to settle when preparing the submission, not a reason to expand the research or delay the rewrite. The cover letter should explain the actual conceptual contribution and its relationship to the invitation. No external message or submission is authorized by this plan.

Only a short list of facts remains author-dependent: exact affiliation, complete funding/grant wording, actual AI assistance history, any previous submission of this manuscript, and the status/version/permissions of material proposed for reuse from GPECOM. These facts need not delay the conceptual rewrite.

## Full coverage of the existing audit

| AUDIT items | Treatment under the confirmed scope |
|---|---|
| P0.1–P0.2 | Packages 1–3: positioning, operational definition, and boundary cases. |
| P0.3 | Conceptual core confirmed; a high-level synthetic illustration is permitted but optional. Preserve the invited title. |
| P0.4–P0.5 | Packages 2–3: conditional economics and a traceable worked qualitative decision. |
| P0.6–P0.7 | Packages 1–3: broader prior art, consistent variables, inference limitations, and action logic. |
| P1.1–P1.6 | Package 4: remove scaffolding and unsupported simulation promises; describe any actual synthetic illustration and bound all claims. |
| P1.7 | Packages 1–2: published GPECOM record and distinct conceptual contribution. |
| P2.1 | Baseline compilation completed; final clean build and complete visual review remain open. |
| P2.2–P2.3, P2.6–P2.7 | Packages 5–6: truthful declarations, metadata, abstract/keywords, bibliography and layout. |
| P2.4–P2.5 | Package 5 after substantive revision: remove commented duplicate drafts and repair figure naming if retained. |
| P3 | Keep repository navigation consistent with the conceptual route. Add minimal simulation infrastructure only if the optional illustration is implemented. |

Migration recovery is operationally complete. Missing historical PDFs, ZIPs, and outlines are not publication blockers. Existing abstract, keywords, abbreviations, and `Cinar2020` have been recovered; their rendering and editorial adequacy are separate current tasks. Historical bulk-citation rules and a previously “locked” paragraph do not constrain this revision.

## Stopping rules and submission gate

Stop literature expansion when every consequential claim has an adequate source or has been narrowed, and all neighboring approaches needed to explain the conceptual contribution are addressed. Stop figure expansion when the definition, inference chain, and worked decision are understandable from the existing diagrams and tables. Additional self-citations, CI, a full digital twin, and quantitative demonstrations are not prerequisites for this completion scope.

The manuscript is ready for the author's submission decision when:

- A reader can identify the regime and classify a boundary case from the definition.
- The contribution remains defensible after acknowledging Li, indirect sensing, and existing probabilistic decision analysis.
- The worked station example traces evidence to a conditional action and explicitly identifies where the evidence cannot support a conclusion.
- Abstract, roadmap, figures, Discussion, and conclusion consistently describe the conceptual study and any explicitly synthetic illustration actually included.
- Empirical station validation, economic prevalence, or operational benefit is not claimed without supporting evidence; synthetic results, if present, are confined to their stated objective and assumptions.
- Bibliographic metadata and front/end matter have been checked; submission administration reflects the author's invitation.
- A final clean build succeeds and every page has been visually inspected after the final changes.
- All applicable audit items have a recorded disposition and closure evidence.

Meeting these criteria makes a complete conceptual submission possible; editorial acceptance remains a separate assessment. Further empirical work belongs to the research agenda rather than an unfinished prerequisite hidden in the conclusion.
