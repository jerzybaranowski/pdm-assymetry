# Round 0 revision report

**Date:** 2026-10-23  
**Historical status:** symbolic conceptual revision implemented and verified before the author approved the numerical continuation on the same date.

**Current continuation:** the approved numerical calculation and 18-page review PDF are documented in [the numerical report](14_numerical_example_report.md). This report preserves the earlier 17-page state, its checks and hash, and the decisions pending at that stage. The review PDF path below now contains the numerical revision.

The author instructed continuation of the corrections after reviewing their status. The revision follows the eight packages in [the Round 0 plan](10_round0_revision_plan.md), preserving the invited title, LD-PdM name, conceptual scope, and station setting. It does not claim that every simulated review request is satisfied. The [response matrix](../reviews/round0/response_matrix.md) records each numbered point and minor issue separately.

## Implemented changes

- Replaced the descriptive boundary table with an applicability checklist: each criterion has a question, required justification, and yes/no/unresolved outcome. Boundary cases distinguish decisions about the same asset and informative small-sample monitoring. The logical roles of the four asymmetries are explained before their individual subsections.
- Added a five-step procedure with inputs, outputs, evidence tracing, admissible policy comparison, and a deadline-aware fallback to the existing admissible schedule or documented tie-break.
- Replaced unused general belief and failure-probability equations with notation actually used in the inspection comparison. Usage and accumulated exposure are separate glossary entries. The decision horizon is future calendar time, distinct from the historical exposure interval.
- Derived the expected gain of inspecting a door and responding to a positive finding, relative to the same existing schedule. Defined actionable-condition probability, conditional detection, net response value, inspection burden, and the false-positive extension. Stated capacity and contingent-response feasibility.
- Derived agreement and reversal conditions for exposure versus inspection order. A preference must beat both the other door and the baseline throughout the declared model set. Ties, sign changes, and uncertainty about benefit relative to the baseline lead to a documented fallback; the fallback is not claimed to be robust-optimal.
- Preserved the temporal meaning of the routing correction: a record correction changes the interpretation of past use; later rerouting does not erase historical exposure.
- Added an explicit shared-error calculation distinguishing mean uncertainty from pairwise ranking, and an example-specific observation that positive-finding rates alone identify the product of condition prevalence and detection under the stated simplification.
- Added a focused comparison with small-data PHM, usage/load-based maintenance, soft sensing, and POMDP/information-value maintenance. Added two cited, verified records (Tinga; Kadlec et al.) and removed peripheral cross-domain examples from the active argument without deleting their bibliography records.
- Made the GPECOM relationship explicit in the article. The new example does not reproduce that companion's equations, figures, or numerical results.
- Rewrote the abstract, contribution paragraph, decision section, discussion and conclusions around the actual outputs. Consolidated scope limits, clarified that future evaluation is recommended rather than promised, removed plural authorial voice, expanded HVAC, and reduced abstract or repetitive framing.

## Editorial choices and limits

The two existing conceptual diagrams are retained: the first separates evidence classes and inference targets; the second traces the station-specific dependencies and decision inputs. Their source and arrow conventions were not changed. A request to unify their semantics is therefore not claimed as implemented. Five tables now have separate functions: applicability, quantity definitions, station assumptions, symbolic policy cases, and prior-work comparison.

The numerical requests are partially answered by an analytical example, not by computation. [The model specification](12_two_door_model_specification.md) supplies the complete outcome accounting and a separate proposed numerical protocol. Its numerical values have not been approved or calculated. No synthetic dataset, Python calculation, numerical figure, fitted degradation model, computed counting value, or empirical performance result has been added. The manuscript's no-new-data declaration remains applicable.

The passage-level editorial pass replaced vague claims of usefulness with named outputs, moved the four-asymmetry hierarchy earlier, and used the reversal inequality to explain why decision sensitivity matters. It retained technical distinctions where removing qualifications would overstate the claim. The independent source/response review identified residual wording and scope issues, which were corrected or recorded as partial in the matrix. This is not a declaration that an unfamiliar human reader has approved the prose.

## Verification

- Compiled the revised source in `build/round0/` using the repository's existing `latexmk` command. No unresolved citations/references, missing characters, overfull boxes, or underfull boxes remain. The known non-fatal bundled-class `xcolor` warning persists.
- Rendered all **17 pages** with native PDFKit because Poppler is unavailable; visually inspected pages 1–9 and independently inspected pages 10–17. Tables, diagrams, equations, bibliography and abbreviations are legible without clipping or overlap. The AI declaration remains red as previously requested.
- Independently reviewed the gain formula, prospective-policy notation, shared-error identity, reversal condition and finite/compact-model-set criterion. Corrected equality assumptions in the agreement statement, conditional false-positive notation, and the fallback table's baseline comparison.
- Static source check: **32 unique bibliography records, 23 cited keys, 5 tables, 5 referenced equations, 2 existing figure inputs**, with no missing citation keys, duplicate keys or unresolved labels.
- Review PDF: `output/pdf/ld-pdm-conceptual-revision.pdf`; SHA-256 `e690f731a8b5213bad4ccfa2d02952dfe1ae6d308c77d59919f4da131d6109f6`.
- No production Python or diagram code changed; no package or interpreter installation was performed. Source checking and mathematical review, rather than unrelated pipeline tests, validate this revision.

## Remaining decisions

The author should review the revised scientific argument and decide whether to add the proposed numerical illustration. The revised text provides a coherent symbolic route, but it does not fully satisfy the numerical demands of reviewers 1 and 2. The original deferred checks remain: AI disclosure, affiliation presentation, and submission-history declarations. Funding scope is unchanged. No submission, upload, external message, commit, or push was performed in this revision.
