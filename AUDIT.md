# Manuscript and repository audit

**Audit date:** 2026-10-19  
**Target:** *Symmetry*, Engineering and Materials  
**Current assessment:** **not submission-ready**

This audit is the current working plan for bringing the manuscript to a defensible submission state. It supersedes older “almost ready” language in historical notes. The paper has a coherent conceptual spine, but the novelty boundary, the evidential support for several claims, and the status of the station case still need substantive work.

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

The distinction should be formulated around the **information structure and decision target**:

| Dimension | Li et al. small-data PHM | Proposed LD-PdM focus |
|---|---|---|
| Primary data object | condition/status data collected from sensors, but limited in quantity/quality | direct condition channels may be absent; proxy/context/history can be the primary evidence |
| Main technical problem | learning reliable AD/FD/RUL models from limited data | maintaining decision-relevant beliefs under structural partial observability |
| Typical remedy | augmentation, transfer learning, few-shot/meta-learning | observation modelling, proxy interpretation, priors, uncertainty propagation, decision analysis |
| Instrumentation cost | recognized as a cause of small data | treated as part of the persistent observation regime and potentially as a decision variable |
| Main output | improved PHM model performance | inspection/maintenance priority, risk bands, resource allocation, value of information |
| Scale | mostly model/task centered | explicit asset-population asymmetry: weak unit evidence but meaningful fleet/system decisions |

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

The canonical term **Limited-Data Predictive Maintenance** is close to the established phrase “small-data PHM.” This is a positioning risk. The manuscript should repeatedly clarify that “limited data” refers to the **available maintenance evidence structure**, not merely sample count. If this remains difficult to communicate after Li et al. are integrated, consider whether “limited-observability” should become a stronger descriptor in the title/definition, while retaining or revisiting the acronym only by explicit author decision.

## P0.3 Decide whether the paper contains a quantitative demonstration or is explicitly a concept/perspective paper

The current source is inconsistent on this point.

- The Introduction says Sections 5–6 present an **“illustrative simulation.”**
- The station section explicitly says it is **not** a detailed simulation benchmark or validation study.
- The active figures are conceptual and the prose describes an architecture, exposure map, and prioritisation logic rather than numerical results.

For an `article` submission, the current state risks being read as a well-written position essay without enough research evidence.

### Preferred route

Add a **small, controlled simulation** whose purpose is decision-level illustration, not algorithm benchmarking. The minimum useful experiment would compare:

1. calendar/fixed-priority maintenance;
2. history-only probabilistic prioritisation;
3. proxy-informed LD-PdM;
4. an idealized direct-condition-information upper bound.

Vary proxy quality and report at least:

- decision/ranking quality;
- failures or high-risk assets missed;
- premature inspections/interventions;
- expected maintenance/failure cost under declared assumptions;
- sensitivity to proxy quality;
- value of additional information or break-even sensing value.

This would directly support the central asymmetry claim while remaining consistent with the paper’s non-algorithmic identity.

### Alternative route

If no quantitative demonstration is added, then:

- remove all promises of simulation/results;
- reduce empirical-sounding claims;
- consider whether MDPI’s `conceptpaper`, `perspective`, or another manuscript type fits better than `article`;
- make the paper’s contribution explicitly taxonomic/conceptual and adjust abstract/conclusion accordingly.

This is a strategic author decision and should be made before polishing prose.

## P0.4 Strengthen the economic argument with evidence

The economic asymmetry is central, but several current claims are stronger than the cited evidence shown in the manuscript.

Li et al. can support the general statement that ROI, digital upgrading, sensor deployment at scale, and data processing are barriers. It does **not** by itself establish that doors, elevators, escalators, or similar station assets usually fail a sensing ROI test.

Needed work:

- separate sensor purchase cost from installation, wiring, networking, commissioning, integration, cybersecurity, calibration, maintenance, and replacement costs;
- find evidence specific to retrofit / distributed infrastructure where possible;
- avoid unsupported prevalence claims (“often,” “typically,” “systematically”) unless references justify them;
- if no strong cost data exist, frame the point as a **decision condition**: LD-PdM applies when the lifecycle value of added direct sensing is not justified under the operator’s constraints.

## P0.5 Make the proxy-to-maintenance chain falsifiable

The current notation

`p(r_i, d_i, l_i | x_i, c_i, h_i)`

is useful conceptually, but the paper currently stops before specifying what would count as evidence that the proxy chain is informative enough for action.

At least one of the following should be added:

- an explicit generative model for proxy → usage → degradation pressure → priority;
- a Bayesian-network example with declared conditional probabilities;
- a simulation-based sensitivity analysis;
- a value-of-information formulation showing when an extra inspection/sensor becomes worthwhile.

Without this, the paper’s Bayesian language risks remaining architectural rather than analytical.

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

If a simulation is added, rewrite Sections 5–6 around actual model assumptions, experiment design, and results. If not, change the Introduction road map from “illustrative simulation” to “illustrative station-based architecture and decision-oriented outputs.”

## P1.4 Recalibrate claims of generality

Statements such as “a large class of real systems” and claims that the economic justification for individual-device sensing is weak need either support or narrower wording. The paper should define a regime, not imply prevalence that has not been established.

## P1.5 Distinguish conceptual inference from measured results

The heatmap and prioritisation figures are conceptual. Avoid language suggesting that they are derived from actual station data unless numerical data are added. Terms such as “inferred exposure” should be clearly labeled illustrative when the values are synthetic or schematic.

## P1.6 Revisit “existence proof” wording

The station case is described as an “existence proof.” In its current non-computational form it is better described as an **illustrative instantiation** or **worked conceptual architecture**. “Proof” suggests a stronger result than is supplied.

## P1.7 Check relationship with the GPECOM paper

The manuscript cites `GPECOM2026LdPDM` as a companion paper and the bibliography currently labels it “Submitted for publication.” Before submission:

- verify its actual publication/acceptance status and update the BibTeX entry;
- ensure the Symmetry paper does not duplicate the conference contribution without clear extension/differentiation;
- use the door/elevator work as supporting technical evidence, not as a substitute for validation of claims made only in the present paper.

---

# P2 — LaTeX/template and submission hygiene

## P2.1 Compile cleanly from a fresh checkout

Compilation has not yet been independently verified after migration. Before substantive final editing, run a clean build and record warnings/errors. At minimum check:

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

Future reproducibility work should add, if a simulation is chosen:

- `code/` or `simulation/` with Python source;
- fixed random seeds and a single configuration file;
- generated data separated from source assumptions;
- figure generation scripts rather than manually edited numerical figures;
- a short reproducibility section in the README.

---

# Recommended work sequence

1. **Integrate Li et al. intellectually first**, before polishing any manuscript prose.
2. Fix the operational definition of LD-PdM and the novelty statement.
3. Decide **quantitative simulation vs explicit concept/perspective paper**.
4. If simulation: implement the minimum decision-level experiment and regenerate the station-output sections around actual results.
5. Strengthen sensor-economics support and narrow unsupported generality claims.
6. Rewrite the Introduction and Discussion around the revised novelty boundary.
7. Remove placeholder headings, future-tense figure captions, and stale drafting text.
8. Clean LaTeX front matter/end matter and verify GPECOM bibliographic status.
9. Run a clean compile and citation/reference audit.
10. Only then perform final language polishing and submission-format checks.

## Submission gate

Do **not** label the manuscript submission-ready until all P0 items are resolved and the P1/P2 items have been checked explicitly. The central criterion is not cosmetic completeness: a reviewer should be able to answer, from the paper alone, **what LD-PdM adds beyond small-data PHM and why the station example constitutes evidence for that claim**.
