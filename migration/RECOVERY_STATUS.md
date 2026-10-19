# ChatGPT project migration — recovery status

**Migration date:** 2026-10-19

This directory records what could be recovered from the ChatGPT project and what still requires import from the original manuscript source.

## Recovered from project conversation context

The following durable project information has been reconstructed and committed to this repository:

- the core LD-PdM / low-instrumentation predictive-maintenance concept;
- the distinction between critical, heavily instrumented assets and mass-deployed assets for which dedicated sensing may be economically unjustified;
- the train-station case-study direction, including escalators, elevators and automatic doors;
- the proxy-data idea, including passenger/ticket-flow information as indirect evidence of escalator usage;
- the intended Bayesian/probabilistic framing for uncertain proxy, contextual and historical evidence;
- the high-concept/non-review character of the article;
- the recovered Introduction outline and paragraph-level outlining rules;
- the literature-synthesis result that indirect/proxy inference appears across many domains without being unified under PdM terminology;
- the required positioning against Li et al. (2024), *Small data challenges for intelligent prognostics and health management: a review*;
- the March 2026 pre-submission discussion for *Symmetry*;
- the plan to reuse elevator and automatic-door examples from the related GPECOM paper where appropriate;
- manuscript-preparation tasks involving abstract, keywords, abbreviations and candidate self-citations.

The recovered material is stored as research notes rather than represented as verbatim historical transcripts unless exact wording was available in the retained project context.

## Known prior project conversations

The accessible project context identifies at least these relevant threads:

1. **2025-12-16 — Contribution statement drafting**
2. **2025-12-16 — Context recovery analysis**
3. **2025-12-17 — Paper structure decisions**
4. **2026-03-09 — Paper Structure Expansion**
5. **2026-03-09 — LDPdM Case Study** (related case-study / reviewer-response context)
6. **2026-03-15 — Paper Review Feedback**

Their recoverable outputs are summarized in `notes/CONVERSATION_INDEX.md` and the topical notes in `notes/` and `literature/`.

## Files known to have existed but not currently retrievable

The project conversation history refers to these attachments:

- `Predictive_Maintenance_Concept-submission.pdf`
- `Predictive_Maintenance_Concept.zip`
- `outline.pdf`

In the current ChatGPT conversation, the file interface exposes no project attachments, and searches of the persistent Library did not return these files. Consequently their exact bytes could not be migrated.

Most importantly, the latest LaTeX source is **not currently available** to the migration process. The repository therefore deliberately does not contain a reconstructed substitute for the paper source.

## Required next import

Export the current Overleaf project as a ZIP (or upload the existing `Predictive_Maintenance_Concept.zip`) and provide it to the repository workflow. The import should preserve:

- every `.tex` source file;
- the canonical `.bib` file(s) and their existing keys;
- figures and diagrams in their original formats;
- custom style/class files;
- any Python/data assets already used to produce manuscript figures.

The source should be placed under `paper/` while retaining its internal structure. Once imported, the manuscript source—not the reconstructed notes—becomes authoritative wherever there is a discrepancy.

## Recovery quality

The conceptual and strategic migration is strong because the main project decisions are represented in retained conversation context. The weak point is exact-text recovery: complete historical chat transcripts, the final abstract/keyword text, the complete detailed outline, and the latest LaTeX/BibTeX source were not exposed by the currently available project/file interfaces.

No attempt was made to silently invent missing source text.
