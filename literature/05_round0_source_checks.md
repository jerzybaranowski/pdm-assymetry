# Focused source checks for the Round 0 revision

**Checked:** 2026-10-23. **Scope:** comparison with small-data PHM, usage/load-based maintenance, soft sensing, and probabilistic inspection planning; disputed references and companion-paper provenance. This is a targeted claim check, not a systematic review or a claim that every cited paper has been read in full.

The starting records are [`02_positioning_vs_li2024.md`](02_positioning_vs_li2024.md), [`03_claim_source_matrix.md`](03_claim_source_matrix.md), and [`04_gpecom_contribution_boundary.md`](04_gpecom_contribution_boundary.md). Existing BibTeX keys remain authoritative. A publisher-indexed passage is identified as such below: successful retrieval of an abstract or preview does not count as access to the whole article.

## Recommended manuscript treatment

Add two focused references, Tinga and Kadlec et al., for the previously missing usage/load and soft-sensor comparisons. Keep the existing condition-monitoring and value-of-information references. These establish the relevant overlap without expanding the paper into a general maintenance review. The manuscript's contribution must be its particular checklist, evidence assessment procedure, and worked decision comparison; none of the source checks establishes that established methods cannot address those questions.

Replace the paragraph listing pulp control, engine pressure reconstruction, bridge response, and tram vibration with a concise account of usage/load-based maintenance and soft sensing. Remove `Buznikov20181216` from its separate representative role. This is a relevance decision, not a finding that those records are false. Retain unused imported bibliography entries and their established keys; no record needs deletion merely because it is no longer cited.

## Four-way comparison: bounded wording

The final column describes this manuscript's proposed use of established work. It is an editorial synthesis, not a finding of exclusive capability.

| Approach and citation | Safe account of its question and evidence | Role in the LD-PdM procedure |
|---|---|---|
| Small-data PHM: `Li2024SmallDataPHM` | Data-efficient PHM under limited quantity or quality; includes operational/economic causes, uncertainty, maintenance records, fleet information, and physical knowledge. | Assess whether the problem is sample limitation, weak condition information, or both, before selecting learning methods. |
| Usage/load-based maintenance: `Tinga2010UsageLoad` | Uses service usage/load observations with physical failure models to assess condition and plan maintenance intervals. | Check the usage-to-load/condition relationship, and identify where usage itself is only indirectly known. |
| Soft sensing: `Kadlec2009SoftSensors` | Estimates process quantities using other measured variables and a model; model development, validation, and changing operating conditions matter. | Identify which quantity an indirect estimate supports and what evidence supports its transfer to the maintenance mechanism. |
| POMDP/information-value maintenance: `SrinivasanParlikad2013VoCM`, `MemarzadehPozzi2016VoI` | Connects uncertain observations, maintenance actions, information acquisition, and costs; includes component inspection and system scheduling. | Supply the established decision reasoning after specifying admissible actions, observation quality, consequences, and resource limits. |

## Passage-level evidence and limits

### Li et al. (2024): retain the broad overlap

**Primary source:** [Springer full text](https://link.springer.com/article/10.1007/s10462-024-10820-4).

Rechecked Introduction, Sections 2.1–2.3, 4.3.2.2, and 6.2–6.3. These passages cover maintenance execution; limited quantity/quality; investment, access and operational constraints; uncertainty; maintenance records and fleet information; and physical/domain knowledge. The abstract and Section 3 identify augmentation, transfer learning, and few-shot learning as the principal method families reviewed. No full audit of the review's cited studies was performed.

**Safe manuscript sentence:** “Small-data PHM already addresses economic and operational constraints, uncertainty, and the use of records and physical knowledge; the present procedure begins with the maintenance choice and examines whether its available evidence supports a differentiated action.”

Replace the manuscript's detailed internal section-number citations with this substantive comparison. Keep the existing bibliography entry unchanged.

### Tinga (2010): add usage/load-based maintenance

**Primary sources:** [publisher preview](https://www.sciencedirect.com/science/article/abs/pii/S0951832010001006), [author institution record](https://research.utwente.nl/en/publications/application-of-physical-failure-models-to-enable-usage-and-load-b/).

Inspected the original abstract, Introduction, and publisher-indexed section openings, especially “Physical models and uncertainty” and “Discussion”. The latter explicitly identifies quantitative usage–load–life-consumption relationships as central. Metadata agree across publisher and institution. The full paper was not accessible; direct publisher opening returned 403. Do not attribute detailed derivations, performance gains, or station applicability from these passages.

**Safe manuscript sentence:** “Usage- and load-based maintenance connects operating information to condition and maintenance intervals through physical failure models.”

For the comparison, refer to this representative formulation rather than asserting that all usage-based policies require a detailed physics model. Do not claim that LD-PdM introduces usage-informed maintenance.

### Kadlec, Gabrys, and Strandt (2009): add representative soft sensing

**Primary sources:** [publisher preview](https://www.sciencedirect.com/science/article/pii/S0098135409000076), [author institution record](https://eprints.bournemouth.ac.uk/8498/), [institutional accepted manuscript](https://eprints.bournemouth.ac.uk/8498/1/CACE_KadlecGabrysStrandt_2008.pdf).

Inspected the original publisher-indexed Introduction and section openings. The Introduction distinguishes model-driven and data-driven approaches, describes online prediction of variables measured infrequently or offline, and discusses historical measurements, noise, missingness and process change. The institutional PDF link was confirmed but timed out; its complete text was not inspected. Bibliographic metadata were checked against both publisher and institution.

**Safe manuscript sentence:** “Soft sensors estimate process quantities from other measurements using model-driven or data-driven relationships; their usefulness depends on the data, validation, and the stability of those relationships.”

This is a methodological precedent. It neither supplies a station-device model nor establishes uncertainty calibration. Avoid implying that soft sensing means inference without physical measurements.

### Existing information-value sources: retain and use explicitly

**Primary sources:** [Srinivasan and Parlikad publisher preview](https://www.sciencedirect.com/science/article/pii/S0360835213001848), [Memarzadeh and Pozzi publisher preview](https://www.sciencedirect.com/science/article/pii/S0951832016300771).

Inspected original abstracts, highlights and publisher-indexed Introduction passages. Srinivasan and Parlikad explicitly connect monitoring accuracy, cost and maintenance policy through a POMDP. Memarzadeh and Pozzi explicitly include partial/noisy observations, observation-dependent decisions, permanent monitoring, and component-level information value used for system inspection scheduling. Full methodological papers were not retrieved in this pass. Existing bibliography metadata agree with the publisher records.

**Safe manuscript sentence:** “POMDP and value-of-information analyses already connect uncertain condition observations to maintenance policies and inspection allocation.”

These sources support the decision comparison and the statement that inspection must be evaluated with the possible subsequent actions. They do not justify any particular probabilities, utilities, effectiveness values, or cost assumptions in a new example. Keep both existing keys and entries unchanged.

### Additional POMDP lead: checked, not necessary to add

[Papakonstantinou and Shinozuka, Part I (2014), publisher preview](https://www.sciencedirect.com/science/article/pii/S0951832014000672) and [Penn State record](https://pure.psu.edu/en/publications/planning-structural-inspection-and-maintenance-policies-via-dynam/) confirm *Reliability Engineering & System Safety*, 130, 202–213, DOI `10.1016/j.ress.2014.04.005`. Original indexed Introduction and institutional abstract inspected; full text not checked. They explicitly discuss uncertain inspections, belief updating, maintenance effects and minimum-lifecycle-cost policies. This supports the reviewer's overlap concern; the two existing information-value references are sufficient for the narrow revised comparison. Do not add this entry unless the manuscript needs a more detailed POMDP discussion.

## New entries ready for insertion only when cited

The entries below preserve the verified publication metadata without importing abstracts or unverified claims. No canonical bibliography changes were made by this source-check task.

```bibtex
@article{Tinga2010UsageLoad,
  author = {Tinga, Tiedo},
  title = {Application of physical failure models to enable usage and load based maintenance},
  journal = {Reliability Engineering \& System Safety},
  year = {2010},
  volume = {95},
  number = {10},
  pages = {1061--1075},
  doi = {10.1016/j.ress.2010.04.015},
  url = {https://doi.org/10.1016/j.ress.2010.04.015},
}

@article{Kadlec2009SoftSensors,
  author = {Kadlec, Petr and Gabrys, Bogdan and Strandt, Sibylle},
  title = {Data-driven Soft Sensors in the process industry},
  journal = {Computers \& Chemical Engineering},
  year = {2009},
  volume = {33},
  number = {4},
  pages = {795--814},
  doi = {10.1016/j.compchemeng.2008.12.012},
  url = {https://doi.org/10.1016/j.compchemeng.2008.12.012},
}
```

## Disputed references and provenance

| Review concern | Check and proportionate disposition |
|---|---|
| `Xin2026` cannot be located | Reconfirmed the original [Elsevier record](https://www.sciencedirect.com/science/article/abs/pii/S0263224125023589): Gou et al.; *Measurement* 257, article 118999 (2026), DOI `10.1016/j.measurement.2025.118999`. The [coauthor's professional-society profile](https://huiyuan.csice.org.cn/member/senior/1158.html) confirms name ordering. Original abstract inspected; full text not read. The bibliographic record is supported. Its removal from the comparison is for relevance; retain the key and corrected metadata. |
| GPECOM is only a submitted preprint | The [AGH institutional publication record](https://badap.agh.edu.pl/publikacja/169113) again supplies the IEEE publication DOI `10.1109/GPECOM70462.2026.11578618`; the publisher itself was not independently opened. Retain the earlier full-text/version-identity check rather than claim it was repeated. The [public text](https://arxiv.org/html/2603.14384v1) remains the reviewer-accessible version identified in the contribution-boundary note. |
| `Ren2018261` and `Buznikov20181216` are weak representatives | Their metadata and narrow abstract-level use were already recorded in the source matrix. The standard soft-sensor review now serves the general claim. No statement about publisher/indexing misconduct has been verified or is needed. |
| Every reference was read in full | Do not make this declaration. The evidence record explicitly distinguishes original full-text passages, publisher previews, abstracts, and metadata. It supports claims only at the level actually checked. |

The revised manuscript should state the concrete relationship to GPECOM: shared station/proxy motivation; GPECOM supplies a particular flow, service-condition and scheduling model; the present work supplies the applicability and evidence assessment procedure and its own hypothetical inspection example. Any new synthetic probabilities must be identified as assumptions of that example, not results imported from GPECOM. The existing author confirmation of preprint/final identity remains sufficient; no new confirmation is required.

## Limits of this review

Additional review suggestions (general CBM reviews, broad maintenance-optimization reviews, and covariate/use-rate models) remain search leads. Adding them solely to increase reference count is unnecessary. No source inspected here establishes station-specific sensor return on investment, population prevalence of the proposed regime, calibrated failure probability, or industrial savings. No access restriction was bypassed, and no packages were installed.
