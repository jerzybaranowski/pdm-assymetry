# Source reconciliation after Overleaf import

**Source import commit:** `3015f9b285d5333768cc446a04e4278fc547743c`  
**Initial reconciliation date:** 2026-10-19

> This is a dated first-pass reconciliation record. The later full manuscript audit in [`../AUDIT.md`](../AUDIT.md) and the revised Li et al. analysis in [`../literature/02_positioning_vs_li2024.md`](../literature/02_positioning_vs_li2024.md) are the current guidance where they go beyond or correct this note.

## 1. Canonical terminology

The manuscript consistently defines the acronym as:

> **Limited-Data Predictive Maintenance (LD-PdM)**

Earlier project discussions sometimes used “low-data predictive maintenance” or “low-instrumentation PdM.” Those phrases remain descriptive, but the canonical manuscript term is fixed by `paper/template.tex` unless explicitly changed by the author.

## 2. Main source and bibliography are available

The current manuscript is `paper/template.tex`, using `paper/extracted.bib`.

The source also contains current TikZ/LaTeX figures for asymmetric observability, the station inference chain, conceptual spatial exposure, and prioritisation output.

## 3. Previously unresolved `Cinar2020` is resolved

The canonical bibliography contains Z. M. Çınar et al., “Machine learning in predictive maintenance towards sustainable smart manufacturing in industry 4.0,” *Sustainability*, 12(19), 2020, DOI `10.3390/su12198211`, key `Cinar2020`.

## 4. Abstract, keywords and abbreviations are present

The imported source already contains the manuscript abstract and keyword list. The abstract identifies four asymmetries:

1. limited observability of decision-relevant states;
2. sparse and biased failure evidence;
3. economic constraints on instrumentation;
4. mismatch between high asset-level uncertainty and meaningful population-level decision value.

The current abbreviation block contains PdM, LD-PdM and RUL.

## 5. The station case is illustrative, not yet a validated simulation

The source contains **“Illustrative Station-Based LD-PdM Architecture”** and explicitly says it is not a full validation study or detailed simulation benchmark.

This conflicts with the Introduction road map, which says Sections 5–6 present an “illustrative simulation.” The full audit now treats the decision **simulation versus explicit concept/perspective positioning** as a P0 issue.

## 6. Companion GPECOM work is integrated conceptually

The Conclusions cite `GPECOM2026LdPDM` as a companion conference paper containing a more technical implementation focused on railway-station doors and elevators, Bayesian proxy-flow modelling, and scheduling integration.

Its current bibliographic status (“Submitted for publication”) should be verified before submission.

## 7. Li et al. (2024) is the central missing positioning item

The imported manuscript does not contain Li et al. (2024), DOI `10.1007/s10462-024-10820-4`.

The initial reconciliation described Li et al. mainly through the methodological remedies they review. A later direct re-reading showed stronger overlap: Li et al. also explicitly identify heavy investment/ROI, large-scale sensor installation, incomplete and imbalanced data, complex conditions, and uncertainty under small-data PHM.

Therefore the manuscript cannot use instrumentation cost, imbalance, or uncertainty alone as novelty. The stronger distinction is **persistent weak direct observability + indirect evidence + decision-oriented maintenance reasoning**. See `../literature/02_positioning_vs_li2024.md`.

## 8. Notes remain useful despite the source import

The Markdown material preserves research information not fully represented in the manuscript, including:

- cross-domain proxy/indirect-inference synthesis;
- lifecycle deployment/integration cost logic;
- paragraph-level outlining discipline;
- value-of-information / sensing-as-decision-variable ideas;
- the quantitative station-simulation option;
- publication-readiness critique.

## 9. Compilation status

The source structure appears complete relative to the imported Overleaf project, including MDPI class/style files and figure sources. A clean compile from a fresh checkout has not yet been recorded. This remains a P2 task in `../AUDIT.md`.
