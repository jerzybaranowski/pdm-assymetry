# Submission-readiness history and current status

This file originally captured the March 2026 pre-submission discussion. It is retained for provenance, but the live prioritized checklist is now [`../AUDIT.md`](../AUDIT.md).

## Current status

**Not submission-ready.** The Overleaf source has been imported and several previously unresolved migration issues are now closed (`Cinar2020`, abstract, keywords, abbreviations, source availability), but substantive scientific issues remain.

## Historical concerns that remain active

- explicit positioning against Li et al. (2024);
- an operational definition of LD-PdM that is more precise than “small data”;
- stronger support for instrumentation/retrofit economics;
- careful separation of proxy evidence from direct measurement;
- a decision on whether to add a quantitative station simulation or reposition as a concept/perspective paper;
- ensuring that “asymmetry” is an organizing construct throughout the paper rather than only a title word;
- preserving the article’s non-review identity while acknowledging adjacent literature fairly.

## Concerns that are now resolved as migration issues

- canonical LaTeX source is available in `../paper/`;
- canonical bibliography is available as `../paper/extracted.bib`;
- `Cinar2020` is identified correctly;
- abstract, keyword list, and abbreviation block are present;
- station figures and companion GPECOM citation are present in the imported source.

## Important update after re-reading Li et al. (2024)

Earlier project shorthand treated Li et al. mainly as a review of learning remedies for a small fault dataset. That is incomplete. Li et al. also explicitly discuss heavy investment/ROI, installing sensors across many machines, incomplete and imbalanced data, complex conditions, and uncertainty under small-data PHM.

Therefore **instrumentation cost is not by itself a novelty claim**. The manuscript must differentiate itself through persistent weak direct observability, proxy/context/history as primary evidence, population-level decision value, and decision-oriented evaluation.

See `../literature/02_positioning_vs_li2024.md` and `../AUDIT.md`.

## Submission gate

Do not return to line-level polishing until the P0 scientific issues in `AUDIT.md` are resolved. In particular, a reviewer must be able to understand from the manuscript itself:

1. what LD-PdM adds beyond small-data PHM;
2. why the proposed regime is meaningfully distinct;
3. what evidence the station case supplies for the paper’s claims;
4. what the framework would allow a maintenance decision maker to do better than a simpler baseline.
