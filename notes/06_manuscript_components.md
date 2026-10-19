# Manuscript components from the finishing stage

During the 2026-03-09 manuscript-finishing conversation, work was performed on the abstract, keywords, abbreviation list, and candidate citations. The source was subsequently imported and revised on 2026-10-19. Current wording is in `../paper/template.tex`; the implementation report is `08_manuscript_revision_report.md`.

## Abstract

The canonical abstract is present in `paper/template.tex`. It defines **Limited-Data Predictive Maintenance (LD-PdM)** and explicitly identifies four asymmetries:

1. limited observability of decision-relevant states;
2. sparse and biased failure evidence;
3. economic constraints on instrumentation;
4. mismatch between high asset-level uncertainty and meaningful population-level decision value.

It also states the operational characterization and synthesis contribution, the worked qualitative station example, overlap with existing approaches, and the absence of an empirical performance claim. The MDPI front-matter declaration has been repaired so that the abstract and keywords render correctly.

## Current keyword list

The revised manuscript uses:

- predictive maintenance;
- limited data;
- partial observability;
- proxy information;
- Bayesian inference;
- uncertainty;
- risk-based maintenance;
- railway stations;
- inspection planning;
- decision support.

## Current abbreviation list

The revised manuscript contains:

- PdM — Predictive maintenance;
- LD-PdM — Limited-Data Predictive Maintenance;
- PHM — Prognostics and health management;
- RUL — Remaining useful life;
- POMDP — Partially observable Markov decision process.

CBM and DT are not used as manuscript abbreviations in this revision.

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
