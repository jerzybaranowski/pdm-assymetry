# Focused source checks for the Round 1 revision

**Checked:** 2026-10-26. **Scope:** direct predecessors for PdM suitability assessment, decisions under model ambiguity, and maintenance-dependent histories. This note records focused reading of original passages and access limits; it is not a systematic review or a complete methodological audit.

The [Round 1 assessment](../notes/16_round1_revision_assessment.md) identifies the relevant gaps. Four entries were added to the canonical bibliography for use in the revision; all existing keys and metadata were preserved. The [Round 0 source checks](05_round0_source_checks.md) remain the evidence record for the earlier additions. Publication years below follow the original journal issue, not the date a repository or migrated website exposed a record.

## Added sources and bounded claims

### `Tiddens2018PdMSelection`

W. W. Tiddens, A. J. J. Braaksma, and T. Tinga, *Selecting Suitable Candidates for Predictive Maintenance*, International Journal of Prognostics and Health Management 9(1), article 020 (2018), DOI `10.36001/ijphm.2018.v9i1.2699`.

**Primary sources:** [original journal PDF](https://papers.phmsociety.org/index.php/ijphm/article/download/2699/1647/7584), [journal record](https://papers.phmsociety.org/index.php/ijphm/article/view/2699), [author institution](https://research.utwente.nl/en/publications/selecting-suitable-candidates-for-predictive-maintenance/).

**Inspected:** original full-text Sections 2.1, 3.2–3.5 and 4.1–4.4, particularly the decision questions on pp. 5–7. The journal PDF and institutional record establish 2018 and article 020; the current journal landing page displays a later 2020 publication date. No later year is substituted into the entry.

**Supported claim:** PdM candidate selection already combines criticality with maintenance clustering and technical, economic, and organizational feasibility. Its screening uses Yes/No/Maybe answers followed by focused feasibility analysis. Checklist form and consequence–feasibility separation are established precedents.

**Proposed positioning:** “PdM suitability assessment already combines criticality with technical, economic, organizational, and maintenance-planning constraints. The present procedure examines an already specified maintenance choice by tracing the indirect evidence supporting its action rationale.” The second sentence describes this manuscript's organizing emphasis, not a capability absent from Tiddens et al.

### `Troffaes2007ImpreciseDecisions`

Matthias C. M. Troffaes, *Decision making under uncertainty using imprecise probabilities*, International Journal of Approximate Reasoning 45(1), 17–29 (2007), DOI `10.1016/j.ijar.2006.06.001`.

**Primary sources:** [author manuscript](https://arxiv.org/pdf/1807.03705), [institutional publication record](https://durham-repository.worktribe.com/output/1576888/decision-making-under-uncertainty-using-imprecise-probabilities).

**Inspected:** Section 1 and Eq. 2, plus Sections 3.1–3.2 in the complete accessible author manuscript. Its first page identifies the 2007 journal publication; the 2018 arXiv deposit is not a different publication year. Institutional metadata were retrieved through the search index; direct opening returned 403.

**Supported claim:** eliminating dominated decisions and then comparing criteria such as maximality and Gamma-maximin are established decision-analysis steps. The criteria can produce different choices.

**Use:** “Decision analysis under imprecise probabilities distinguishes dominance-based admissibility from the additional criterion used to select among admissible alternatives.” Here the manuscript applies dominance to model-specific expected gains. It must distinguish operational feasibility from this decision-theoretic meaning of admissibility. Troffaes is not cited as the source of the manuscript's minimax-regret formula: no regret discussion was found in the inspected manuscript. Maximizing minimum incremental gain also must not be relabelled minimizing worst-case total loss when model-dependent baseline losses are unspecified.

### `Arcieri2023RobustMaintenance`

Giacomo Arcieri, Cyprien Hoelzl, Oliver Schwery, Daniel Straub, Konstantinos G. Papakonstantinou, and Eleni Chatzi, *Bridging POMDPs and Bayesian decision making for robust maintenance planning under model uncertainty: An application to railway systems*, Reliability Engineering & System Safety 239, 109496 (2023), DOI `10.1016/j.ress.2023.109496`.

**Primary sources:** [author preprint](https://arxiv.org/pdf/2212.07933), [authors' institutional publication account](https://chatzi.ibk.ethz.ch/smm-news/2023/07/bridging-pomdps-and-bayesian-decision-making.html), [ETH publication citation](https://frs.ethz.ch/news-events/frs-news-channel/2025/04/dynamic-mobile-sensing-for-resilient-transport-infrastructure.html), [publisher record](https://www.sciencedirect.com/science/article/pii/S0951832023004106).

**Inspected:** preprint Abstract, Sections 2.2–2.3 and the application/data description. Publication metadata agree with the institutional citation. Direct publisher and institutional journal-PDF retrieval returned 403; final-version identity with the preprint was not checked or asserted.

**Supported claim:** uncertainty in transition and observation models has already been propagated into railway maintenance planning through Bayesian POMDP inference and decision analysis. The inspected formulation averages utility over parameter distributions; it is not the manuscript's unweighted comparison across routing interpretations.

**Use:** “Model uncertainty is also addressed in Bayesian POMDP maintenance planning; Arcieri et al. incorporate inferred transition and observation parameter distributions into railway maintenance decisions.” Use as a concise comparator, without transferring its data, performance results, or model assumptions to station doors.

### `CookeBedford2002ReliabilityData`

Roger Cooke and Tim Bedford, *Reliability Databases in Perspective*, IEEE Transactions on Reliability 51(3), 294–310 (2002), DOI `10.1109/TR.2002.802889`.

**Primary source:** [original published article in the TU Delft repository](https://repository.tudelft.nl/file/File_756e7c67-6012-4639-b258-d4a520d9f4f4?preview=1). The complete 17-page journal PDF was accessible; its title page, running headers, and DOI establish the metadata.

**Inspected:** Introduction, pp. 294–295; maintenance taxonomy, pp. 295–296; competing-risk discussion, Sections V–VI, pp. 300–304; and the distinction between nonidentifiability and sampling uncertainty in Section VII, pp. 304–306. Mathematical extraction omits some symbols, so no uninspected equation is imported.

**Supported claim:** maintenance histories reflect interventions as well as failures; independence between competing maintenance and failure processes requires justification. Observed failures under a maintenance policy need not identify the failure process under a changed policy.

**Use:** “Maintenance and failure can be dependent competing processes, so recorded failure histories must be interpreted together with the interventions that generated them.” This provides maintenance-specific support for the observation-history limitation. It does not supply a station likelihood, establish that every inspection process is informative, or justify a particular imperfect-repair model. A full longitudinal model remains outside the worked example.

## Existing sources and retained boundaries

- **`Enjavimadar2022`:** the [publisher-indexed original abstract and introduction](https://www.sciencedirect.com/science/article/pii/S0378779621006283) reconfirm title, authors, volume 203, article 107647, and DOI `10.1016/j.epsr.2021.107647`. The source supports maintenance-strategy optimization under budget, time, crew, and practical constraints. It is not station-specific evidence for access dependencies. Direct opening returned 403; no full-text claim is made. The Round 1 reviews report different verification access, not evidence of a false citation. No bibliography correction is required.
- **`SrinivasanParlikad2013VoCM`:** its [original publisher-indexed abstract and introduction](https://www.sciencedirect.com/science/article/pii/S0360835213001848) explicitly identify a POMDP methodology. The reviewer's inability to retrieve the abstract does not invalidate the existing characterization. The earlier access limits remain recorded.
- **`Haruehansapong2023`:** [publisher-indexed Sections 3–4](https://www.mdpi.com/2075-5309/13/1/27) describe contextual HVAC fault detection using ambient measurements and electrical-current inputs. The overlap with indirect inference should be explicit; this specific detection application does not itself validate the station evidence-to-action chain. Direct opening returned 429, so the indexed original passages, not a newly downloaded complete article, support this account.
- **`Zeng2016253`:** retains its bibliographic identity. Its general interval-censoring role is already bounded in the claim–source matrix. If the revised paragraph concerns maintenance-dependent histories rather than interval-censoring machinery, cite Cooke and Bedford and omit the unnecessary clinical-method citation from that paragraph. An unused canonical entry need not be deleted.
- **`GPECOM2026LdPDM`:** the [completed contribution-boundary check](04_gpecom_contribution_boundary.md), including the author's 2026-10-21 confirmation that the inspected preprint equals the final publication, remains authoritative. No new version-identity or metadata revision is inferred. Shared station/proxy motivation and distinct contributions must remain visible; the companion is not independent empirical validation.

No additional RCM standards, delay-time, imperfect-repair, or diagnostic-identifiability references were added. None of these checks establishes industrial performance, station prevalence, a grant number, an AI-tool version, or a submission-history declaration.

## Verification

The source task changes only the canonical bibliography and its two source-check records. Static verification found 36 unique entry keys and 35 unique DOI fields, with no duplicate keys or DOIs. All four additions have balanced braces and the required bibliographic fields. The pre-checkpoint bibliography text is unchanged, and `git diff --check` passes. These are structural checks, not a standalone BibTeX compilation; final citation integration and bibliography rendering are verified with the complete Round 1 manuscript build.
