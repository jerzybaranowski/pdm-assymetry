# Manuscript and repository audit

**Audit date:** 2026-10-19  
**Target:** *Symmetry*, Engineering and Materials  
**Current assessment:** **substantively revised draft for author review; AI disclosure deferred**

## Revision status on 2026-10-19

The agreed conceptual revision is implemented in `paper/template.tex`. The invited title and LD-PdM name are retained. The current review PDF has 16 pages after the focused Li comparison; the first revision had 14, followed by a 15-page draft restoring useful explanatory material after the author's question about the reduction. Details and section counts are in [`notes/08_manuscript_revision_report.md`](notes/08_manuscript_revision_report.md).

| Audit items | Current disposition |
|---|---|
| P0.1–P0.2 | Addressed in the draft: Li integration, operational definition, and boundary cases. A focused comparison additionally acknowledges records, physical knowledge, fleet information, and uncertainty; differences concern organizing emphasis, not exclusive capabilities. |
| P0.3 | Conceptual route implemented with a worked qualitative example. No simulation is claimed or required by the current conclusions. |
| P0.4–P0.5 | Addressed through conditional economics, an assumption register, and explicit evidence-to-action scenarios. No station ROI or performance result is claimed. |
| P0.6–P0.7 | Existing partial-observation/information-value work is acknowledged; variables, action dependence, inspection value, pooling assumptions, and proxy limits are separated. |
| P1.1–P1.6 | Active drafting language and unsupported simulation promises removed. Case/output sections combined and strengthened; all active figures are explicitly conceptual. |
| P1.7 | GPECOM publication metadata corrected and the contribution boundary stated. No conference figures or numerical results are reproduced. |
| P2.1–P2.2 | Revised source builds successfully; first-page abstract/keywords, single-author option, year, and header height corrected. Final affiliation presentation remains an author check. |
| P2.3 | Funding scope retained as instructed, with grammatical corrections. AI disclosure is red and explicitly deferred by the author. |
| P2.4–P2.5 | Commented duplicate drafts removed. The misspelled prioritisation filename is retained only as an inactive historical source, so renaming it is unnecessary for this submission. |
| P2.6–P2.7 | Abstract/keyword rendering repaired. Metadata checked for all 30 bibliography records; all have pagination/article identifiers. 26 records are cited. Claim-support limits are recorded in the source matrix. |
| P3 | Navigation updated; shared diagram previews, static checks, and optional pinned tooling declarations added. No simulation infrastructure is required. |

Validation found no unresolved citations/references, missing characters, or overfull/underfull boxes. All 16 pages were rendered and visually inspected after the focused Li comparison. A non-fatal `xcolor` warning remains in the bundled class/PGF loading sequence. Three diagram-pipeline tests and the test catalog check pass. The source matrix distinguishes abstract/metadata checks from full-text reading.

**Remaining author work:** review the scientific revision and content balance; replace/approve the red AI declaration; confirm affiliation presentation and submission-history declarations. Funding scope is confirmed. Submission is not authorized. A cover-letter draft is in [`notes/09_cover_letter_draft.md`](notes/09_cover_letter_draft.md).

The detailed findings below preserve the initial audit and its rationale. Their implementation status is the table above; descriptions of defects in the original source are not a second current task list.

This audit is the current working plan for bringing the manuscript to a defensible submission state. It supersedes older “almost ready” language in historical notes. The paper has a coherent conceptual spine, but the novelty boundary, the evidential support for several claims, and the status of the station case still need substantive work.

**Author clarification, 2026-10-19:** the contribution is conceptual; no empirical data are available; a high-level simulation is permitted if useful. The manuscript is invited under its existing title, which is retained. Publication-type selection is not a scientific blocker. A quantitative demonstration is optional, not a prerequisite for completion.

The detailed execution plan, proposed paragraph outline, closure criteria, and bounded optional simulation are in [`notes/07_publication_completion_plan.md`](notes/07_publication_completion_plan.md). This audit remains the authoritative issue register. The follow-up review also verified a baseline build and identified an abstract/keywords rendering defect, incomplete bibliography metadata, and additional conceptual issues below.

## Executive diagnosis

The strongest version of the paper is **not** “PHM has too little data.” That territory is already well established. The paper is strongest when it formulates a narrower regime in which:

1. maintenance decisions have non-negligible operational or economic value;
2. direct condition variables are absent, weak, or persistently unavailable because of deployment, legacy, access, or economic constraints;
3. maintenance reasoning therefore relies materially on proxy, contextual, historical, or prior information rather than on a small direct-condition dataset alone; and
4. success is evaluated primarily by decision quality, prioritisation, robustness, and information value rather than by diagnostic or RUL accuracy alone.

The main scientific risk is that the current manuscript sometimes treats “small data,” instrumentation cost, uncertainty, and low observability as if their combination were itself novel. Li et al. (2024) substantially narrows that claim. The manuscript must position LD-PdM as a **decision and observation-architecture regime**, not as a newly discovered data-scarcity problem.

---

# P0 — Scientific issues that must be resolved before submission

## P0.1 Integrate Li et al. (2024) explicitly and revise the novelty boundary

**Reference:** C. Li, S. Li, Y. Feng, K. Gryllias, F. Gu, and M. Pecht, “Small data challenges for intelligent prognostics and health management: a review,” *Artificial Intelligence Review*, 57, 214 (2024), DOI `10.1007/s10462-024-10820-4`.

Li et al. overlap with the present paper more strongly than a simple “few-shot learning review” characterization suggests. They explicitly:

- define small-data PHM in terms of limited **quantity or quality** of sensor-collected system-status information;
- identify **heavy investment / ROI** as a cause of small-data PHM, including digital upgrades and installing sensors across many machines;
- discuss incomplete, imbalanced, missing, unlabeled, and noisy data;
- treat uncertainty quantification under small-data conditions as an open issue;
- review data augmentation, transfer learning, and few-shot learning as the main solution families.

Therefore the present paper must **not** claim novelty for any of the following by themselves:

- scarcity of fault data;
- class imbalance;
- the fact that instrumentation is costly;
- the fact that small data increase uncertainty;
- the general need for data-efficient PHM.

### Defensible distinction

The distinction concerns **organizing emphasis**, not exclusive information sources, methods, or outputs. This initial comparison has been refined after checking Li's broader scope; see `literature/02_positioning_vs_li2024.md` and the dedicated Discussion subsection.

| Dimension | Li et al. small-data PHM | Proposed LD-PdM focus |
|---|---|---|
| Organizing question | methods and challenges of data-efficient PHM | applicability of a joint observation and maintenance-decision regime |
| Concrete contribution sought here | established neighboring literature | inclusion/boundary criteria, explicit inferential links, and conditions for withholding differentiated action |
| Relationship | overlapping perspectives | established learning and decision methods can be used within the characterization |

### Required manuscript changes

- Add Li et al. to the canonical bibliography and cite it in the Introduction **before or at the point where LD-PdM is defined**.
- Replace the current implication that data scarcity is generally treated merely as an inconvenience. Li et al. already treat causes and impacts systematically.
- State explicitly that LD-PdM is **adjacent to and overlapping with small-data PHM**, not a replacement for it.
- Add a short distinction between **small direct-condition datasets** and **weak/indirect observation architectures**.
- Revisit the Discussion subsection “Relation to existing maintenance paradigms” and include small-data PHM as an explicit neighboring paradigm.
- Avoid using “structural versus accidental scarcity” as the sole differentiator: Li et al. already identify persistent economic and operational causes of small data.

A safe positioning sentence is:

> Small-data PHM research has already established that limited, incomplete, and imbalanced monitoring data can arise from economic and operational constraints; LD-PdM focuses on the complementary observation regime in which direct condition information may itself be persistently unavailable, so maintenance decisions must be formed from indirect, contextual, historical, and prior evidence.

This wording should be adapted during manuscript editing rather than copied mechanically.

## P0.2 Define LD-PdM operationally enough that it is more than a label

The present definition is conceptually clear but still qualitative. A reviewer can reasonably ask: *when does a problem become LD-PdM rather than ordinary PdM with missing data?*

The paper needs an explicit operational definition or taxonomy. A useful definition should require, at minimum:

- a maintenance decision with meaningful consequence/value;
- persistent weakness or absence of at least one decision-relevant direct condition channel;
- reliance on indirect evidence for a non-trivial part of the inference chain;
- uncertainty that cannot be eliminated simply by applying a different classifier to the same dataset.

Consider expressing the regime using two axes:

1. **decision/maintenance value**; and
2. **economically available direct observability**.

This would make the title’s “asymmetry” a formal organizing idea rather than a descriptive metaphor.

### Terminology risk

The canonical term **Limited-Data Predictive Maintenance** is close to the established phrase “small-data PHM.” This is a positioning risk. Clarify in the definition and manuscript text that “limited data” refers to the **available maintenance evidence structure**, not merely sample count. Use “limited observability” as a descriptor where useful. Preserve the existing invited title and canonical LD-PdM name.

## P0.3 Align the evidence with the confirmed conceptual contribution

The current source is inconsistent on this point.

- The Introduction says Sections 5–6 present an **“illustrative simulation.”**
- The station section explicitly says it is **not** a detailed simulation benchmark or validation study.
- The active figures are conceptual and the prose describes an architecture, exposure map, and prioritisation logic rather than numerical results.

**Route resolved by the author:** retain the conceptual contribution and invited title. A worked qualitative station decision, explicit assumptions, applicability criteria, and fair positioning are the required evidence of conceptual coherence. The earlier recommendation to require a four-policy simulation is superseded.

Required changes:

- remove promises of simulation or numerical results unless such an illustration is actually added;
- state what the definition, taxonomy, and worked example establish;
- replace claims of validation, improved maintenance, or an “existence proof” with conclusions supported by a conceptual argument;
- align the abstract, section roadmap, station case, Discussion, and conclusion.

A high-level synthetic illustration may examine when proxy quality, noise, and shared bias permit or undermine exposure-informed inspection prioritisation. Keep its objective distinct from failure prediction and industrial cost savings. A bounded design and stopping rule are in `notes/07_publication_completion_plan.md`; no numerical protocol is yet fixed. The conceptual revision can close without it.

## P0.4 Strengthen the economic argument with evidence

The economic asymmetry is central, but several current claims are stronger than the cited evidence shown in the manuscript.

Li et al. can support the general statement that ROI, digital upgrading, sensor deployment at scale, and data processing are barriers. It does **not** by itself establish that doors, elevators, escalators, or similar station assets usually fail a sensing ROI test.

Needed work:

- separate sensor purchase cost from installation, wiring, networking, commissioning, integration, cybersecurity, calibration, maintenance, and replacement costs;
- find evidence specific to retrofit / distributed infrastructure where possible;
- avoid unsupported prevalence claims (“often,” “typically,” “systematically”) unless references justify them;
- if no strong cost data exist, frame the point as a **decision condition**: LD-PdM applies when the lifecycle value of added direct sensing is not justified under the operator’s constraints.

## P0.5 Make the proxy-to-maintenance argument traceable and bounded

The current notation

`p(r_i, d_i, l_i | x_i, c_i, h_i)`

is useful conceptually, but the paper currently stops before specifying what would count as evidence that the proxy chain is informative enough for action.

For the conceptual paper, add an assumption register and a worked qualitative decision linking proxy evidence, inferred usage/exposure, possible actions, consequences, and limitations. Show both a case in which evidence could differentiate inspection attention and a case in which the available evidence cannot justify an ordering. A symbolic decision rule may clarify the argument, but numerical probabilities and an implemented optimizer are not required.

State what later observations could challenge each proxy interpretation. Do not imply that an explicit probability distribution guarantees identifiability, calibration, or operational usefulness.

## P0.6 Address established partial-observation and information-value maintenance work

Li et al. integration alone does not establish novelty. Existing work already connects partial/noisy observations, maintenance choices, information acquisition, and population-level inspection allocation. Verified starting points include [Value of condition monitoring in infrastructure maintenance](https://doi.org/10.1016/j.cie.2013.05.022) and [Value of information in sequential decision making](https://doi.org/10.1016/j.ress.2016.05.014).

Position LD-PdM as an operational characterization and synthesis of a maintenance evidence regime. Acknowledge overlap with virtual/soft sensing, risk-based maintenance, Bayesian inspection planning, and partially observable Markov decision processes. Audit claims that other literature omits uncertainty or that no relevant methodological canon exists; narrow or remove them unless supported by a defined source set.

## P0.7 Separate physical quantities, uncertainty, and decisions

The active manuscript needs a consistent glossary and reasoning boundary:

- dedicated sensors also provide evidence about latent condition; weak condition-sensitive channels, rather than latent states alone, distinguish the proposed regime;
- usage, exposure, degradation, future-event probability, consequences, urgency, and action priority are not interchangeable;
- define the event and horizon if probability notation is retained; a service-condition threshold is not a failure event;
- explain the pooling assumptions behind population-level inference and the effect of common proxy bias;
- distinguish intervention from information gathering: greater uncertainty alone does not establish greater intervention priority;
- describe asset function and consequences rather than declaring doors, elevators, or escalators non-critical as entire classes;
- treat censoring and intervention effects as explicit limitations where they are not represented in the example.

---

# P1 — Manuscript coherence and unfinished text

## P1.1 Remove active placeholder headings

The active manuscript contains headings that read like drafting scaffolding:

- `\subsection{Section positioning}`
- `\subsection{Section opening paragraph}`

These should be removed or replaced with substantive headings. A section-opening paragraph normally does not need its own subsection.

## P1.2 Fix figure captions/prose that still describe already-created figures as future work

The source already inputs the figures, but the active text still says:

- “The planned diagram should show ...”
- “The figure should visualize ...”
- “The planned figure may take the form ...”
- “The specific graphical form can be chosen later ...”

This is clearly pre-final drafting language. Rewrite captions to describe what the figures **do show**, and remove planning commentary from manuscript prose.

## P1.3 Resolve the simulation/architecture contradiction

Rewrite the roadmap and Sections 5–6 around the worked conceptual station example. If the optional synthetic illustration is added, label its methods and results separately and limit their interpretation to the declared synthetic objective.

## P1.4 Recalibrate claims of generality

Statements such as “a large class of real systems” and claims that the economic justification for individual-device sensing is weak need either support or narrower wording. The paper should define a regime, not imply prevalence that has not been established.

## P1.5 Distinguish conceptual inference from measured results

The heatmap and prioritisation figures are conceptual. Avoid language suggesting that they are derived from actual station data unless numerical data are added. Terms such as “inferred exposure” should be clearly labeled illustrative when the values are synthetic or schematic.

## P1.6 Revisit “existence proof” wording

The station case is described as an “existence proof.” In its current non-computational form it is better described as an **illustrative instantiation** or **worked conceptual architecture**. “Proof” suggests a stronger result than is supplied.

## P1.7 Check relationship with the GPECOM paper

The manuscript cites `GPECOM2026LdPDM` as a companion paper and the bibliography currently labels it “Submitted for publication.” The [AGH record](https://badap.agh.edu.pl/publikacja/169113) identifies the published paper, pages 987–992, online from 2026-07-02, DOI `10.1109/GPECOM70462.2026.11578618`. Its [preprint](https://arxiv.org/html/2603.14384v1) already develops proxy-flow/cycle modelling and scheduling. Before submission:

- update the BibTeX entry from the verified published record;
- ensure the Symmetry paper does not duplicate the conference contribution without clear extension/differentiation;
- use the door/elevator work as supporting technical evidence, not as a substitute for validation of claims made only in the present paper.

Check the version of record before reuse. Its service-condition probabilities do not validate physical failure probabilities, and its citation of this conceptual manuscript does not independently establish the present contribution.

---

# P2 — LaTeX/template and submission hygiene

## P2.1 Compile cleanly from a fresh checkout

**Baseline build verified on 2026-10-19:** clean temporary copy of the source at HEAD `2f6436b478e608ddfc73eb37b57deec126844234`, using TeX Live 2024 and latexmk 4.83. This was not a fresh clone. Command: `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error template.tex`. Exit 0, 23 pages, no unresolved citations/references and no BibTeX errors.

Temporary review artifacts: `/tmp/pdm-latex-audit-3q67w2nv/paper/template.pdf`, `template.log`, `template.blg`, and `build.stdout`. These are local, disposable artifacts rather than a repository build archive. Pages 1, 4, 13, 14, 15, and 16 were rendered with existing Ghostscript and visually inspected.

Open findings: two overfull boxes (16.46 pt in the proxy table; 25.95 pt in the inference-chain diagram), underfull table/abbreviation text, repeated header-height warnings, and an `xcolor` warning. Visual inspection also revealed P2.6 below. After revision, run a final clean build and inspect every page. At minimum check:

- unresolved references/citations;
- overfull boxes;
- figure placement;
- bibliography generation;
- MDPI class warnings.

A lightweight CI build can be added later if useful.

## P2.2 Correct MDPI front-matter inconsistencies

Current source items to verify/fix:

- one author is declared while the class option is `moreauthors`; the MDPI template comments indicate `oneauthor` for a single author;
- `\pubyear{2026}` but `\copyrightyear{2025}`;
- affiliation/address is minimal and should be checked against MDPI formatting requirements;
- verify whether author-contribution text is required/appropriate for a single-author paper.

## P2.3 Language cleanup in declarations

Current end matter contains small but visible issues, including:

- “The author declare no conflicts of interest” → grammatical correction required;
- AI acknowledgment grammar (“the author ... take full responsibility”) requires correction;
- funding disclaimer wording should be normalized (“views and opinions ...”).

Also verify the current journal policy for disclosure of AI-assisted language/writing tools and update the model/version description so it reflects the tools actually used during final manuscript preparation.

## P2.4 Remove duplicated draft blocks from `template.tex` after content stabilizes

The manuscript contains long commented-out earlier versions of active sections. Git already preserves history; keeping duplicate drafts inside the submission source increases editing risk and makes diffs harder to review.

Do this **after** the substantive revision, not before, so useful fragments are not lost during restructuring.

## P2.5 Clean figure naming after manuscript logic is stable

`pioritisationoutput.tex` contains a filename typo. Rename to a consistent form such as `prioritisation_output.tex` and update the corresponding `\input{...}` once substantive editing of `template.tex` begins.

## P2.6 Repair abstract and keyword rendering

`paper/template.tex:126` starts the document before the abstract and keywords. At `:129`, the source uses an `abstract` environment, whereas the bundled class defines the one-argument `\abstract{...}` command (`paper/Definitions/mdpi.cls:638`–`639`). The PDF loses the first “P” in “Predictive” and displays neither the Abstract nor Keywords label.

Use the correct MDPI front-matter commands before `\begin{document}` and verify the rendered first page. A successful LaTeX exit code does not close this issue.

## P2.7 Verify bibliography metadata and claim support

All 27 bibliography entries are used, and all active citation keys resolve. Fifteen article entries nevertheless have empty pagination and no alternative article identifier: `Carvalho2019`, `Cinar2020`, `Straub2015`, `vanDinter2022`, `Ma2020`, `Zhou2025`, `Guo2025`, `Haruehansapong2023`, `Burnac2025`, `Mahmoodian2022`, `Yeter2020`, `Yang2024`, `Xin2026`, `Enjavimadar2022`, and `Yu2021`.

Check all retained records against publisher metadata, including surname ordering and author initials; the `Xin2026` and `Baraldi2015176` author fields need particular attention. Preserve canonical keys. Separately check claim support: `Straub2015` is a Bayesian updating algorithm paper, `Bourinet2016210` concerns computational rare-event estimation, and `Zeng2016253` supports interval-censoring methodology rather than station-specific evidence. Adding an accurate identifier does not repair an inaccurate attribution.

---

# P3 — Repository organization and reproducibility

The repository cleanup associated with this audit does the following:

- establishes this `AUDIT.md` as the current prioritized task list;
- expands the root `README.md` into a file map;
- updates the Li et al. positioning note to reflect the stronger overlap found in the paper itself;
- moves non-canonical candidate BibTeX entries from the ambiguous `references/` area to `literature/candidate_references.bib`;
- removes the redundant `paper/README-kopia.md`;
- adds a LaTeX-oriented `.gitignore`;
- reconciles stale research notes with the imported source while preserving their historical role.

For the conceptual route, keep a reproducible LaTeX build and traceable sources/diagram assumptions. If the optional synthetic illustration is implemented, add only the infrastructure it requires:

- `code/` or `simulation/` with Python source;
- fixed random seeds and a single configuration file;
- generated data separated from source assumptions;
- figure generation scripts rather than manually edited numerical figures;
- a short reproducibility section in the README.

---

# Recommended work sequence

1. Fix the contribution and operational definition, acknowledging Li and established partial-observation/decision-analysis work.
2. Map consequential claims to their sources and verify retained bibliography records.
3. Specify the evidence/assumption chain and worked qualitative station decision.
4. Rewrite the core sections; add only a bounded high-level synthetic illustration if it resolves a specific remaining explanatory gap.
5. Rewrite the Introduction, Discussion, abstract, and conclusion to match the completed conceptual argument.
6. Align schematic figures/tables and remove placeholder headings, future captions, unsupported performance claims, and duplicate draft blocks.
7. Repair abstract/keywords, front/end matter, bibliography, and layout.
8. Run a final clean build, inspect every page, and prepare submission materials under the existing invitation.

Detailed deliverables and stopping rules: `notes/07_publication_completion_plan.md`.

## Submission gate

Do **not** label the manuscript submission-ready until all P0 items have an explicit disposition and the P1/P2 items have been checked. A reviewer should be able to identify **the proposed regime, its relationship to prior art, the assumptions connecting proxy evidence to action, and what the conceptual station example establishes**. Quantitative validation is not a prerequisite for this scope; conclusions must stay within the conceptual argument and any explicitly synthetic illustration actually included.
