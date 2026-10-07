# aq-docket-trial-01 - cross-document hooks

Find facts that combine into a world answer before drafting wording. Record sources/locations,
input quantities and units/periods, the relationship, a possible ask and one or two selected levers.
Explore forecast/actual, proposal/final dates, changed/conflicting tables, amendments, hedge scope,
mentions/actions, entity/edition joins, ordered/late items, exclusions and ordinary cross-document
calculations. Find more viable hooks than questions requested without inventing a quota.

Bundle character (caller read of all six texts, 2026-10-06; map confirms): six unrelated statistics
preprints. No document cites, amends or responds to another; no shared dataset, author, funder or
reference work. Cross-document reasoning is therefore limited to comparisons/arithmetic over
analogous quantities (iterations, gene counts, cluster counts, tuning values). Difficulty must come
from close reading inside each paper (a deciding fact away from a same-label decoy), per the
2026-10-04 platform verdict on the earlier trial-01 q01 ("too easy: it can be answered without
careful work across the documents").

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D01 Fig. 5 runtime "Sparse DPMM: 65" (413) + "∼ 5.91 seconds per iteration" (403) -> about 11 iterations (not printed); D04 RIGLS "converged after just 2-iterations" (379, 385) | iterations: leukemia benchmark run minus battery full-model identification = 9 | Scatter the pieces; facts put together from two passages; calculate across documents | D04 "In our experience convergence occurs after roughly 3-5 iterations" (351) gives 6-8; D01 slice sampler "1000 MCMC iterations" (263) gives 998 | "∼" approximate: 65/5.91 = 10.998, only integer 11; runtime may include several random initializations (total still 11) | sketch i01 |
| h2 | D02 raw 9,671 genes (431); Appendix A "top 3000 genes ranked by MAD were retained" (723); main text "979 highly variable genes" (439), Table 4 "MAD-based model ... 979" (585); D05 33,538 genes, "top 3,000 HVGs" (783) | share of measured genes kept by each study's top-variability cut: 31.0% vs 8.9%, difference 22.1 pp | Bury one item late; calculate across documents; state the rounding | 979 (post-module set, labelled "highly variable genes") gives 10.1% and 1.2 pp | 979 also called "pre-selected genes" in 5.5 (577): wording must point at the ranking cut, not the final set | sketch i02 |
| h3 | D04 Fig. 7 caption "At convergence λ = 0.0002" for the full model (385); BIC tunes λ (121); D02 BIC minimum at K = 9, q = 8 (447) | values each BIC-tuned study reports: λ 0.0002 and 9 clusters | Who belongs where (same label, different scope); scatter the pieces | D04 Results text "The value of the hyper-parameter at convergence is λ = 0.00067" (367, cell 8 level-1 fit), 0.00048 (383, cell 3); D02 WGCNA K = 4 (579) | two parallel asks joined only by the shared criterion (weak combination) | sketch i03 |
| h4 | D01 benchmark uses "empirical Bayes hyper-parameters" (403); EB estimate a0 = b0 = 28.9076 with "strong" prior Kpost = 3 (273); weaker a0 = b0 = 10 gives Kpost = 4 (297), the abstract/intro highlight the extra sub-cluster (13, 37); D02 K = 9 (447) | clusters each model settled on: 3 and 9 | Same series, right configuration; scatter the pieces | weak prior 4 (headline sub-cluster); D02 WGCNA K = 4 | Fig. 5b benchmark cluster count is figure-only; inference that the benchmark run equals the EB run | sketch i04 |
| h5 | D05 "40-year" benchmark = 984 bi-weekly observations, 01/08/1982-12/24/2022 = 41 calendar years (887) | single-document only | exact vs rounded prose | 40 vs 41 | no cross-document partner; paper itself says 40 | rejected (one document) |
| h6 | D04 abstract "10 cells" vs cell 5 excluded, "all 9 cells" (21, 291, 377) | cells in final model | edition-style scope | 10 | abstract's "training data comprised ... 10 cells" makes 10 defensible | rejected (ambiguity) |
| h7 | D03 stated bound 0 <= W*d <= 1 (427, 689) vs Table 3 left-censoring W*d 1.884, 2.970, 1.642 (755-759) | single-document only | hedge/claim vs data | 0 | no partner | rejected (one document) |
| h8 | D05 Algorithm 1: 8 sills + 4x4 length-scale pairs = 24 SOFM fits (741-747, 815-817) | single-document only | procedure applied to configuration | 12, 26 | final refit unstated; no partner | rejected |

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.
