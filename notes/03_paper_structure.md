# Recovered manuscript structure and outlining rules

This note preserves the part of the manuscript structure that is explicitly recoverable from retained project context. The complete detailed outline existed previously, but its exact text is not available in the current migration environment.

## Recovered Introduction structure

### 1. Introduction

#### 1.1. PdM as decision-making under uncertainty

Intended message: predictive maintenance is not merely a signal-processing/classification task. It is a decision problem involving uncertain condition, uncertain future evolution and asymmetric consequences of action or inaction.

#### 1.2. Identification of LD-PdM as a distinct data regime

Intended message: there exists a practically important class of assets for which maintenance decisions matter but direct condition data are structurally weak, sparse, indirect or absent. The regime is linked to sensor economics, legacy infrastructure, scale and rare fault information.

#### 1.3. Motivation for Bayesian framing in LD-PdM

Intended message: when condition must be inferred from proxies, contextual variables, histories and prior engineering knowledge, uncertainty should be propagated explicitly. Bayesian/probabilistic modelling is therefore a natural language for the problem.

#### 1.4. Contribution statement

This subsection was considered effectively locked during the detailed-outline phase. The contribution logic is preserved in `notes/02_contribution_statement.md`.

## Paragraph-level outlining convention

The project adopted a strict detailed-outline format:

- each bullet represents one future paragraph;
- each paragraph introduces one coherent message;
- a paragraph should not combine multiple independent claims merely to shorten the outline;
- references are attached to the bullet/message they support;
- required figures/tables are represented as separate bullets rather than hidden inside prose bullets.

This is intended to make the transition from outline to LaTeX prose mechanical and to expose argumentative gaps before writing.

## Introduction citation rule

During the 2025-12-17 restructuring discussion, the user decided that references in the Introduction should be concentrated in Sections 1.1–1.3. Section 1.4 was not considered a good location for introducing new literature and was left essentially unchanged.

A previous request also specified that a detailed LaTeX outline should end each subsection with a bulk citation containing all references used in that subsection. When the exact LaTeX source is imported, check whether that convention survived into the manuscript or was only an outlining device.

## Figures in the Introduction

Figures in the Introduction were allowed only if absolutely necessary to establish a conceptual point. The default was to reserve figures for later sections.

## What is not safely recoverable

The complete headings and paragraph bullets for the remainder of the paper are not available in retained context. They should **not** be reconstructed from memory and silently presented as the original outline.

Once the Overleaf source or `outline.pdf` is imported, this file should be expanded with the exact structure and then marked as verified.
