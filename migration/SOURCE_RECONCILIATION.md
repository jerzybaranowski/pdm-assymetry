# Source reconciliation after Overleaf import

**Source import commit:** `3015f9b285d5333768cc446a04e4278fc547743c`  
**Reconciliation date:** 2026-10-19

This note records the first comparison between the reconstructed ChatGPT-project notes and the imported manuscript source. It is intended to prevent future work from reintroducing outdated terminology or overlooking issues already identified in earlier discussions.

## 1. Canonical terminology

The manuscript consistently defines the acronym as:

> **Limited-Data Predictive Maintenance (LD-PdM)**

Earlier project discussions sometimes used “low-data predictive maintenance” or “low-instrumentation PdM.” Those phrases remain accurate descriptions of the intended regime, but the canonical manuscript term is now fixed by `paper/template.tex` and should be used in manuscript-facing work unless deliberately changed.

## 2. Main source and bibliography are now available

The current manuscript is `paper/template.tex`, using `paper/extracted.bib`.

The source also contains the current TikZ/LaTeX figures for:

- asymmetric observability (`diagram.tex`);
- the station inference chain (`inferencechain.tex`);
- conceptual spatial exposure (`conceptual_heatmap.tex`);
- prioritisation output (`pioritisationoutput.tex`).

This means future manuscript edits should be made against the exact source rather than reconstructed text from conversation notes.

## 3. Previously unresolved `Cinar2020` is resolved

The canonical bibliography contains:

- Z. M. Çınar, A. A. Nuhu, Q. Zeeshan, O. Korhan, M. B. A. Asmael, and B. Safaei,
  “Machine learning in predictive maintenance towards sustainable smart manufacturing in industry 4.0,”
  *Sustainability*, 12(19), 2020,
  DOI `10.3390/su12198211`.

The key is `Cinar2020` (ASCII key, despite the accented author name).

## 4. Abstract, keywords and abbreviations are no longer missing

The imported source already contains the manuscript abstract and keyword list. The abstract explicitly states the four asymmetries:

1. limited observability of decision-relevant states;
2. sparse and biased failure evidence;
3. economic constraints on instrumentation;
4. mismatch between high asset-level uncertainty and meaningful population-level decision value.

The current abbreviation block contains PdM, LD-PdM and RUL.

Historical notes saying that these components still need to be generated should therefore be interpreted as development history, not current tasks.

## 5. The station case is illustrative, not a validated simulation

The current source contains a section titled **“Illustrative Station-Based LD-PdM Architecture”** whose opening explicitly states that it is not a fully validated predictive-maintenance model. It uses proxy information, latent-state reasoning, and decision-oriented outputs to demonstrate the conceptual framework.

This is consistent with the original high-concept-paper intention, but it creates a manuscript-level issue that should be fixed during finalization: the Introduction currently says that Sections 5 and 6 “present an illustrative simulation,” whereas the imported source describes the case itself as an illustrative architecture and conceptual decision-output demonstration. Unless numerical simulation code/results are added, the Introduction should not promise a simulation.

## 6. Companion GPECOM work is already integrated conceptually

The Conclusions cite `GPECOM2026LdPDM` as a companion conference paper containing a more technical implementation focused on railway-station doors and elevators, Bayesian proxy-flow modelling, and scheduling integration.

This supports the project decision to reuse the door/elevator context without turning the present paper into the same technical contribution. The distinction between the conceptual Symmetry paper and the technical conference implementation should remain explicit.

## 7. Li et al. (2024) remains the most important missing positioning item

The March 2026 review identified:

C. Li, S. Li, Y. Feng, K. Gryllias, F. Gu, and M. Pecht, “Small data challenges for intelligent prognostics and health management: a review,” *Artificial Intelligence Review*, 57, 214 (2024), DOI `10.1007/s10462-024-10820-4`.

A check of the imported `template.tex` and `extracted.bib` found no occurrence of this paper. This is important because the current manuscript repeatedly argues that limited data should be treated as a structural regime rather than a temporary modelling inconvenience. Li et al. are close enough to that premise that the distinction must be made explicitly.

The recommended positioning remains:

> Existing small-data PHM research primarily asks how to learn effectively from limited condition and fault data; LD-PdM addresses the complementary regime in which direct condition information is structurally limited because instrumentation itself may be unavailable or economically unjustified, so maintenance decisions must be built from uncertain proxy, contextual and historical evidence.

This should be integrated into the Introduction and bibliography before submission.

## 8. Notes that remain useful despite the source import

The Markdown material still contains research information that is not fully represented in the current manuscript:

- the broader literature-search synthesis around proxy/indirect inference across heterogeneous domains;
- the explicit distinction between sensor purchase cost and lifecycle deployment/integration cost;
- the December 2025 paragraph-level outlining discipline;
- the stronger formulation of value-of-information / sensorisation as a decision variable;
- the publication-readiness critique from the March 2026 review.

These should be treated as a source of pending improvements rather than overwritten by the present LaTeX.

## 9. Compilation status

The repository source structure appears complete enough to represent the Overleaf project, including MDPI class/style files and figures. Compilation has **not yet been independently verified in the current ChatGPT environment**. A clean compile should be part of the next repository-level validation step before substantive manuscript editing.
