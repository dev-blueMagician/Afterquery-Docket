# aq-01650 - cross-document hooks

Find facts that combine into a world answer before drafting wording. Record sources/locations,
input quantities and units/periods, the relationship, a possible ask and one or two selected levers.
Explore forecast/actual, proposal/final dates, changed/conflicting tables, amendments, hedge scope,
mentions/actions, entity/edition joins, ordered/late items, exclusions and ordinary cross-document
calculations. Find more viable hooks than questions requested without inventing a quota.

Bundle character (caller, 2026-10-08, after reading all seven texts in full): seven academic papers on
financial literacy with no cross-citations and no forecasts, editions, amendments or dated events.
Clusters: China Household Finance Survey (Doc 1 = D06, 2017/2019; Doc 2 = D03, 2015/2017; Doc 6 = D02,
2011-2019), Osaka Preference Parameters Study 2010/2011 (Doc 3 = D04, ages 40-64; Doc 4 = D05, 40+),
Bank of Japan Financial Literacy Survey 2016 (Doc 5 = D01), Saudi survey (Doc 7 = D07). Per the
calibration lesson for unrelated-paper bundles, the Medium mechanism has to come from one paper's
internals (a same-label figure whose scope differs), joined to a second paper's indispensable input.
The task page's suggested "period identified by a fact" shape is unsupported: 2016 appears in Doc 1 and
Doc 7 only as citation years.

Ids below: local Dnn (page Doc N). Lines are text/Dnn.txt line numbers.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D01 (Doc 5) L208 students excluded 1,212, "remaining 23,788"; complete cases 15,228; L216 Table 2 "Financial literacy 15,228 15.2" (complete cases); L365 decomposition "Men: 14.719 ... Women: 13.480", L397 N "23,788 (Men: 11,658, Women: 12,130)"; L69 literacy = correct answers of 25. D03 (Doc 2) L102/L108 2015 CHFS mean correct 1.414 of 3. | Japan non-student average share correct minus China 2015 average share correct: 14.0872/25 = 56.35% vs 47.13% -> +9.2 pp | Part vs total (complete-case subset vs all non-students); figure that must be computed (weighted mean); unit normalisation (25 vs 3 questions) | complete-case 15.2 -> 13.7; unweighted 14.0995 -> 9.3; complete-case weights -> 9.4; men only 11.7; women only 6.8 | FL observed for all non-students (imputation only for covariates; SEs fit n of 11-12k); different instruments, metric defined in the question | sketch S1 (primary) |
| h2 | D04 (Doc 3) Table 4 L209-218: women 418 of 701 check-up takers (column % 36.99 is within women); D05 (Doc 4) Table 4 L84-99: women 1,347 with 723 zero screenings; all 1,311 zero of 2,693 | Women's share of non-mandatory check-up takers (40-64) minus their share of people with at least one counted cancer screening (40+): 59.63 - 45.15 = +14.5 pp | Look-alike measure (share of takers who are women vs share of women who take); calculate across documents | within-women rates 36.99 - 46.33 = -9.3 (sign flips); mixed 13.3 / -8.2 | different age scopes must be stated; analogous-figure comparison | sketch S2 |
| h3 | D04 (Doc 3) L243 above-university check-up rate 28.89% < below 32.76% (counterintuitive); D05 (Doc 4) Table 4 above-university column 268/98/119/154/26 (n 665); L65 overall mean 1.1508 | Mean number of counted cancer screenings in the education group less likely to take non-mandatory check-ups: 902/665 = 1.36 | Who belongs where (group identified in one paper, statistic in the other); figure that must be computed | overall printed mean 1.15; below-university 1.08 (the guess without Doc 3) | bridge stated plainly in one prose sentence (one-sentence bridge risk) | sketch S3 |
| h4 | D02 (Doc 6) L310 three tiers: low = unable to answer or zero correct, high = all correct, intermediate between; D03 (Doc 2) Table 1 L100-106 2015 distribution | Intermediate share 46.01 + 31.55 = 77.56%; low 11.67% (all-"unknown" 6.50% is inside zero-correct) | Definition applied to an instance | double-counting unknowns gives low 18.17%, intermediate 71.06% | "unable to answer" wording admits a second reading; short path | hold (Too easy risk, ambiguity) |
| h5 | D04 (Doc 3) L72 2011 wave 4,934, 2,208 = 44.75%; D05 (Doc 4) L47 2011 wave "4943", 2,693 = 54.58% (consistent only with 4,934) | Reconcile the wave total | Reconcile documents that disagree | 4,943 typo route | document-error decoy on an input; rule 10 if asked about the disagreement | reject (two defensible answers) |
| h6 | D01 (Doc 5) Table 5 L359-370: university endowment 0.676 = 85.1% of endowments (0.794); total gap 1.240 | Share of the whole gender gap from university attainment: 54.5% | Part vs total | prose 85.1% | single document; "attributable" admits three readings | reject as a question (single-doc); note for set |
| h7 | D04 (Doc 3) Tables 6-7, L362-369 significant covariates; D05 (Doc 4) L186 significant covariates; Doc 3 abstract L15 lists only male/age/married/smoking | Characteristics significant in the same direction in both studies: age, household assets, happiness, smoking | Match then exclude (male opposite signs); bury late items (assets, happiness absent from Doc 3 abstract) | male; married; children/income; unemployment (either opposite or not significant) | per-item direction words printed in prose (keyword-filter risk); Doc 4 tables 7-8 absent | hold (Too easy risk) |
| h8 | D01 (Doc 5) Table 3 N men 11,658 of 23,788 = 49.01%, Table 2 male 0.529 (complete cases); D04 (Doc 3) L144-146 census men 48.7% | Male share of non-student respondents minus census share: +0.31 pp | Part vs total | complete-case 52.9 -> 4.2 | same trap family as h1 (sibling) | alternative to S1 only |
| h9 | D05 (Doc 4) L78 prose "Of those who did not undergo cancer screening, more than half (51.43%) obtained lower than university qualifications" vs Table 4 1,043 of 1,311 = 79.56% | Share of non-screened below university | Look-alike measure | prose 51.43% | document misstatement on the asked fact | reject (document-error decoy) |

Independent author inventory (question-author, round 1, 2026-10-08; full table in
runs/sketch-r1/author-A.md, hooks h1-h17). Agreements and differences with the table above:
- Same rejections: the 2011-wave total conflict (4,934 vs "4943"), the 51.43% misreading, the
  financial-education school-level conflict, Doc 1's sample-size conflicts, the 85.1% single-document
  endowment trap, regression-significance lists (Doc 4 Tables 7-9 absent), the task page's suggested shapes.
- Author h7 is this table's h1. The author rejected it because it paired the Doc 5 non-student mean with the
  Osaka panel's three-question mean (0.62 prose vs 0.6185 table), where the gold flips with the chosen figure.
  The caller pairs it with Doc 2's 2015 CHFS mean of 1.414, which is printed identically in prose and table;
  every stated input form gives 9.2 (q01).
- Author additions sketched: i01 (Doc 4 Table 6 threshold mapping x Doc 2 Table 1), i02 (direction reversals
  across Doc 3/Doc 4 Tables 4-5), i03 (CHFS zero-correct vs UK all-wrong), i04 (definitions applied to a
  hypothetical respondent). Others rejected: income/asset unit conversions (two lookups plus one operation),
  attention-coding comparisons (ambiguous mapping), overconfidence typology applied to Doc 5's self-rating
  (two readings), CHFS coverage counts (different scopes).
- Mapper (notes/doc-map.md, complete, no unread ranges) located the same conflicts and adds table-layout
  defects (Doc 5 shifted standard-error rows, Doc 6 t-values without parentheses, Doc 2 Table 3 Panel B rows
  swapped) that no candidate depends on.

Round 2 (second independent question-author, 2026-10-08; raw: runs/sketch-r1/author-B.md, rows R2-a to R2-k,
all reject): carving the over-64 group from the two Osaka samples fails (pools differ: 3,420 vs 3,403, so 502 vs
485); Doc 4's rounded prose against its own table counts is the measured no-trap; hidden scopes whose true quantity
no document prints (any-screening incl. breast/uterine, any check-up incl. mandatory, narrow risky assets) leave the
gold unsupported; Doc 1's "Age 60 and over" household criterion is single-document with three denominators; Doc 5's
other complete-case rows are q01's mechanism; the 85.1% endowment share is single-document; Doc 5's decomposition is
internally inconsistent when inverted; CHFS cross-paper joins hit undefined scopes or document errors; no method
transfers to another paper's data except those already used; qualitative levers are guessable, close to rule 10 or
rest on document errors. Conclusion shared by both authors and both reviews: q01 is the only Medium-plausible design;
Hard is unsupported on this document set.

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.
