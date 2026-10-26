# Editorial consistency after numerical integration

**Date:** 2026-10-25  
**Status:** targeted editorial changes implemented and verified; current review PDF has 18 pages.

The [numerical revision](14_numerical_example_report.md) and its checks were complete at the pause on 2026-10-23. The author resumed work on 2026-10-25. A continuous reading of the manuscript and three independent reviews identified the following bounded clarifications. They preserve the approved model, parameter values, decision rule used in the example, and results. No new model, source claim, empirical estimate, or diagram dependency is proposed.

## Implemented paragraph-level revisions

- **Introduction, decision-analysis paragraph:** describe the assessment as preceding commitment to a method or policy, without implying that an action comparison can be performed without stated models.
- **Figure 1 caption:** explain the existing dashed-input and dotted-output convention and the overview role of the common inference block. Do not claim that it supplies a source-specific dependency map.
- **Usage/load-maintenance paragraph:** attribute the physical-model formulation to the cited Tinga work rather than implying that every usage-based approach requires it.
- **Evidence-integration paragraph:** replace the characterization of the station as sensorless with the manuscript's actual condition-information limitation.
- **Procedure step 4:** distinguish improvement over the reference schedule from preference over the other candidate actions.
- **Procedure step 5:** require a documented admissible fallback; identify retention of the reference schedule as the example's selected convention.
- **Paragraph after the procedure:** explain that failure to identify one common optimum need not preclude improvement over the baseline, and point to the demonstrated cost of the selected fallback.
- **Station evidence paragraph:** state a common historical exposure interval, without inventing its calendar duration.
- **Assumption table:** align routing validity with the interval represented by the records, and include condition probability, detection, contingent response, and inspection burden in the action row.
- **Figure 2 caption:** explain the existing solid and dashed links while making clear that the solid links also depend on assumptions. Preserve the diagram sources.
- **Symbolic example, input-definition paragraph:** define the actionable condition using the approved model specification before introducing its probability and detection sensitivity.
- **Numerical input paragraph:** state the approved normalization to a common positive reference exposure; preserve every numerical input.
- **Population interpretation paragraph:** remove wording that implies the gain equation necessarily excludes cross-door effects, which the derivation allows within conditional consequences.
- **Evaluation opening paragraph:** distinguish conditional synthetic comparisons from empirical evidence of calibration or realized industrial savings in the target setting.

## Verification and limits

An independent read of the revised procedure, definitions, normalization, population interpretation, and evaluation paragraph confirmed that the approved model, numerical results, policy set, and illustrative fallback remain unchanged. The calculation and generated table were not edited; their previously passed numerical tests remain the relevant evidence and were not rerun during this editorial pass.

- Compiled successfully in `build/editorial-20261025/` using the existing `latexmk` command. The only warning is the known non-fatal `xcolor` load-time warning from the bundled class. No unresolved citations or references, duplicate labels, missing characters, overfull boxes, or underfull boxes remain.
- Rendered all 18 pages through the existing native PDFKit workflow. Independent reviewers visually inspected pages 1–6 and 7–12; the primary editor inspected pages 13–18. The revised procedure, both figure captions, assumption table, equations, numerical table, and closing material are legible without clipping or overlap. No layout correction was needed after rendering.
- The figure captions were checked against the actual arrow styles in the unchanged TikZ sources and the final manuscript render. Standalone diagram previews were not regenerated; no claim of style harmonization or a new dependency map is made.
- Static source verification confirms 23 unique labels, 32 unique bibliography records, 23 cited keys, five tables, two figures, and six numbered equations. No missing keys or references were found.
- The [response matrix](../reviews/round0/response_matrix.md) records the bounded closure and preserves the earlier numerical-test evidence: 10 tests, 58 subtests, and 10 valid catalog entries on 2026-10-23. This is not a claim of a new test run or a full-project reproducibility audit.
- The current [review PDF](../output/pdf/ld-pdm-conceptual-revision.pdf) has SHA-256 `476c89fe8dd86bd3e7e21c8a9ca2e7c8fc9b682e6b13e31ac5ea8e0e660bb8c4`. It supersedes the PDF hash recorded for the 2026-10-23 numerical stage.

The caption clarifications partially address the arrow-convention review point. The author-deferred AI declaration, affiliation presentation, and submission-history declarations remain separate. Broader models and empirical evaluation remain outside this bounded continuation. No package installation, submission, external message, commit, or push was performed. All edits and the review PDF are saved locally.
