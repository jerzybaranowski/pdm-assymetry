# Conceptual manuscript revision report

**Date:** 2026-10-19\
**Latest update:** 2026-10-21\
**Status:** revised draft for author review; AI disclosure deferred by the author.

The revision implements `07_publication_completion_plan.md` in `paper/template.tex` while preserving the invited title and the canonical LD-PdM name. The author confirmed that empirical data are unavailable, allowed a high-level simulation if useful, and asked to retain the funding scope and mark the AI statement red for later revision.

## Scientific changes

- Added an operational definition relative to a maintenance choice, horizon, and feasible evidence set. A missing channel alone does not establish LD-PdM if other channels suffice. Explicit uncertainty treatment is a framework requirement rather than a condition determining whether the physical regime exists.
- Integrated Li et al. before introducing LD-PdM and acknowledged the overlap with small-data PHM. A focused full-text comparison added a dedicated Discussion subsection: records, physical knowledge, fleet reasoning, uncertainty, and maintenance decisions are shared ingredients; the proposed difference is organizing emphasis, operational criteria, explicit inferential links, and limits on differentiated action. Added existing POMDP/information-value maintenance work to the novelty boundary.
- Preserved all four asymmetries while distinguishing defining conditions from complications and opportunities. Economics is framed conditionally, with function-specific consequences rather than blanket claims about low-criticality asset classes.
- Separated usage/exposure, condition, future-event probability, consequences, and action priority. Added conceptual belief, event, and action-dependent expected-loss notation without claiming an implemented model.
- Replaced the previous architectural case/output sections with a worked qualitative station example, an assumption register, and five decision scenarios. The positive inspection comparison includes an explicit exposure-to-actionable-finding premise and comparable inspection burdens/consequences.
- Distinguished the published GPECOM technical example from this conceptual contribution. Service-condition probabilities are not relabelled as physical-failure probabilities.
- Removed unsupported prevalence, superiority, and literature-absence claims. Cross-domain sensing papers are presented as analogies with explicit transfer limits.

The author approved a bounded follow-up on 2026-10-21: concretize the two-door example and sharpen the positive account of the contribution. Section 5.3 now follows hypothetical doors A and B from available records through a conditional exposure contrast to inspecting A first. Comparable baseline beliefs, detectability, burdens, and benefits from acting on findings are explicit assumptions. Dated routing evidence then reveals an allocation error during the exposure interval itself; the revised allocations no longer support greater exposure for A, so the ordering is withdrawn without automatically prioritizing B. A later route change is not treated as erasing accumulated exposure. The example demonstrates this part of LD-PdM reasoning; a predictive policy would additionally need justified future-state/event and consequence models.

The Abstract, Introduction, Discussion, and Conclusions now emphasize how the criteria, quantity distinctions, and scenarios let a reader identify the regime and examine an action rationale. Repeated qualifications were reduced while retaining the shared foundations with Li et al. and existing decision analysis. All vignette inputs and relationships remain hypothetical; no simulation, empirical result, or new algorithm was added.

The subsequent GPECOM content check on 2026-10-21 used the public full text, which the author confirmed is identical to the final published version. The current attribution and separation of contributions are consistent with that text; no further manuscript correction was needed. The cover-letter draft now states the division concretely. The comparison is recorded in [`../literature/04_gpecom_contribution_boundary.md`](../literature/04_gpecom_contribution_boundary.md). Deferred author declarations remain separate.

No simulation was added in this revision: the current claims concern a definition, a modelling framework, and traceable qualitative reasoning. A computational illustration remains an optional future choice, not an outstanding prerequisite disguised as an achieved result.

## Length and content preservation

The original compiled manuscript had 23 pages. The first revised version had 14 pages. After the author asked about the reduction, a separate comparison of the original and revised station/Discussion sections identified useful explanations that had become too thin. The revision restored station topology and redistribution after closures, temporal demand aggregation, spatial/group planning outputs, planner-facing uncertainty communication, and why a decision can be useful without exact health reconstruction.

The restoration produced a 15-page draft, and the focused Li comparison produced a 16-page draft. The current PDF after the 2026-10-21 refinement still has **16 pages**. The recorded approximate main-text counts below compare the original with the 2026-10-19 Li revision, before the two-door refinement:

| Section | Original | 2026-10-19 Li revision |
|---|---:|---:|
| Introduction | 1,038 | 489 |
| Regime and asymmetries | 1,553 | 1,193 |
| Evidence and inference | 1,163 | 790 |
| Maintenance decisions | 893 | 626 |
| Station case and outputs combined | 3,027 | 1,781 |
| Discussion | 1,827 | 987 |
| Conclusions | 404 | 179 |
| Total | 9,905 | 6,045 |

Counts include table/caption wording, exclude main-section titles, and are approximate; they are not a journal word-count declaration. The reduction comes from condensation of active prose and removal of repeated framing. Deleting commented draft blocks does not change PDF length. No target page count was imposed.

Two active conceptual diagrams remain. The manually shaded heatmap and the undefined relevance/uncertainty priority plot were removed from the active manuscript; their source files remain for provenance. Four tables now describe regime boundaries, quantity definitions, assumptions, and decision scenarios.

## References and technical validation

`literature/03_claim_source_matrix.md` records the source checks, safe uses, and full-text limitations. The bibliography contains 30 records, with 26 cited in the revised manuscript. All records now have pagination or an article identifier; publisher-deposited Crossref metadata closed the remaining pagination checks. BibTeX keys were preserved. Corrected metadata include author-name ordering and the published GPECOM record.

The revised manuscript builds with TeX Live 2024 and latexmk 4.83. The build has no unresolved citations/references, missing characters, or overfull/underfull boxes. A remaining `xcolor` load-time-option warning arises within the bundled class/PGF loading sequence and has no observed rendering effect. Header-height warnings and the malformed abstract/keywords have been repaired.

All 16 pages of the 2026-10-21 revision were rendered and visually inspected. Tables, equations, diagram links, bibliography, and the red AI statement were checked. The abbreviations heading and table are kept together to prevent an isolated heading at the preceding page end. The review PDF is `output/pdf/ld-pdm-conceptual-revision.pdf`.

A fresh temporary copy of the earlier 15-page manuscript source also compiled successfully, with generated auxiliaries and the EPS-converted logo excluded from the copied input; all pages matched that reviewed build pixel-for-pixel. The 2026-10-21 source was rebuilt and visually checked as described above. Its exported PDF has SHA-256 `eba4fa61aef7f2020257b00e4b4d1624c74fb968e6e0cb9e5807906c4c04f488`. Static checks confirmed 26 cited keys, 30 unique library records, two existing active figure inputs, and valid local Markdown links. `git diff --check` passed.

The diagrams have a shared preview renderer, standalone wrappers, and separate PNG/PDF previews. Rendering completed without warnings; static verification reported zero issues. Three pipeline tests and the test-case catalog check passed. Optional Python tooling is declared under `tools/diagrams/` with exact observed pins and a uv-generated lockfile. No packages, interpreters, or installed environments were changed.

## Remaining author work

1. Review the revised scientific argument and the retained balance of explanation, especially the operational definition and worked station decision.
2. Replace/approve the red AI disclosure when ready, including the historical tool/version information and actual scope of assistance.
3. Confirm the final affiliation presentation and submission-history declarations when preparing the submission. Funding scope is retained as instructed; no grant identifier was invented.

The revision is a reviewable manuscript, not an assertion that the author has approved every sentence or authorized submission. No external message, upload, or submission has been performed.
