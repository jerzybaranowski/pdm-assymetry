# Manuscript components from the finishing stage

During the 2026-03-09 manuscript-finishing conversation, work was performed on the abstract, keywords, abbreviation list, and candidate citations. The current Overleaf source has now been imported, so the exact manuscript state can be read directly from `../paper/template.tex`.

## Abstract

The canonical abstract is present in `paper/template.tex`. It defines **Limited-Data Predictive Maintenance (LD-PdM)** and explicitly identifies four asymmetries:

1. limited observability of decision-relevant states;
2. sparse and biased failure evidence;
3. economic constraints on instrumentation;
4. mismatch between high asset-level uncertainty and meaningful population-level decision value.

It also states that the paper’s contribution is conceptual and structural rather than algorithmic.

## Current keyword list

The imported manuscript uses:

- predictive maintenance;
- Bayesian methods;
- uncertainty quantification;
- proxy data;
- indirect measurement;
- digital twins;
- risk-based maintenance;
- infrastructure maintenance;
- railway stations;
- decision support.

## Current abbreviation list

The imported manuscript currently contains:

- PdM — Predictive maintenance;
- LD-PdM — Limited-Data Predictive Maintenance;
- RUL — Remaining useful life.

Earlier project notes mentioned PHM, CBM and DT as possible abbreviations, but they are not currently included in the manuscript abbreviation block.

## Known candidate self-citation

The March 2026 conversation explicitly supplied:

```bibtex
@ARTICLE{Bauer2025,
    author = {Bauer, Waldemar and Baranowski, Jerzy},
    title = {A Comparison of Deep Recurrent Neural Networks and Bayesian Neural Networks for Detecting Electric Motor Damage Through Sound Signal Analysis},
    year = {2025},
    journal = {Energies},
    volume = {18},
    number = {18},
    pages = {},
    doi = {10.3390/en18184997}
}
```

A reconciliation check found that `Bauer2025` is **not currently present** in `paper/extracted.bib`. It should only be added if it supports a specific manuscript statement; it should not be introduced merely as a self-citation.

## Historical versus current state

This file now records the verified current manuscript state. For exact wording, always use `paper/template.tex`; this note exists only to preserve the relationship between the March 2026 finishing work and the imported source.
