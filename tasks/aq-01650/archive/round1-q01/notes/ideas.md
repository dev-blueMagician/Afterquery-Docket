# aq-01650 - lean candidate sketches

Current target: medium (user, 2026-10-08: "there is no slot for Easy Tier for this bundle, we should
target medium and high"; page: Hard 0/2, Medium 0/3, Easy 0/1 with "In review: Easy 1"); measured
platform success pending.
Choose hooks from notes/hooks.md and draft from shorthand facts, then reopen sources to verify
premises, exact names, terms, periods and units. A sketch needs question, provisional short gold,
essential inputs/locations, mechanism, source risk and preliminary decision. Full components,
submission reasoning, membership proof and independent checks follow promotion.

Round 1 (2026-10-08): caller sketches S1-S3 (origin claude) and independent question-author sketches
i01-i04 (origin claude; raw return runs/sketch-r1/author-A.md). Golds recomputed by the caller's scripts.
Ids: local Dnn (page Doc N).

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | hooks h1: hidden complete-case scope in D01 (Doc 5) + D03 (Doc 2) 2015 mean | "On each survey's own literacy test, how many percentage points higher was the average share of questions answered correctly by non-student respondents to Japan's 2016 Financial Literacy Survey than by households in the 2015 China Household Finance Survey? Give one decimal place." Gold 9.2 | D01 L69, L208, L365, L397; D03 L102, L106, L108 | Calculate across documents; State the rounding; decoys 13.7 (complete-case 15.2), 9.3 (unweighted), 9.4 (complete-case weights) | instruments differ (defined in the question); FL observed for all non-students | sketch blind solve match 9.2 (medium-high, named 13.7 and rejected it); closed-book miss (~26). PROMOTED to q01 rev 0. Caller tier estimate: Too easy ~15%, Easy ~45%, Medium ~30%, Hard/Too hard ~10%. Platform 2026-10-08: rev 0 blocked "too vague" by the form (both form solvers 13.7); a user-edited firmer wording (version 1923ac) ran the difficulty check: "Answer not supported", Low 3/5, high model 13.7 in 3 of 3 (never consulted the decomposition table). DROPPED for Medium (q01 rev 2, status dropped). |
| S2 | h2: share-of-takers vs rate-within-group, D04 (Doc 3) T4 + D05 (Doc 4) T4 | Women's share of 40-64 non-mandatory check-up takers minus their share of 40+ respondents with any non-breast, non-uterine cancer screening, pp one decimal. Gold +14.5 | D04 T4 418/701; D05 T4 women 1,347 with 723 zero, 1,382 screened | Look-alike measure; decoy -9.3 (within-women rates, sign flips) | analogous-figure comparison; two age scopes in wording | quick-test candidate (Easy-leaning) |
| S3 | h3: education group bridge D04 -> D05 T4 mean | Mean number of counted cancer screenings (40+) in the education group less likely to take non-mandatory check-ups (40-64). Gold 1.36 (902/665) | D04 L243 (28.89 vs 32.76); D05 T4 above-university column | Who belongs where; decoys 1.15 (printed overall mean), 1.08 (guessed group) | one-sentence prose bridge (measured too-easy risk) | quick-test candidate (Easy-leaning) |
| i01 | author h2: D05 (Doc 4) T6 score >= 0.5 = 2+ of 3 correct + D03 (Doc 2) T1 | Osaka 40+ share with at least two of three correct minus 2015 CHFS share, pp one decimal. Gold 24.7 (67.03 - 42.32) | D05 L56, T6 L134-147; D03 T1 L100-106 | Calculate across documents; unit/basis (average-score threshold); decoy 19.7 (0.62 read as a share) | shares D03 Table 1 with S1 (different cells) | quick-test candidate (author: Medium ~12%) |
| i02 | author h1: direction reversals D04 T4-5 x D05 T4-5 | Which of graduates, the unemployed, smokers, drinkers, frequent gamblers reverse direction between check-up and screening rates. Gold: university graduates, the unemployed, drinkers | D04 T4-5; D05 T4-5 | Scatter the pieces; decoys smokers, gamblers; prose narrows drinkers and unemployed | 58 words, near-rulebook; gives away i04 | quick-test candidate (author: Medium ~15%) |
| i03 | author h3: CHFS zero-correct vs UK all-wrong | Gold +0.7 (11.67 - 11) | D03 T1; D06 (Doc 1) L31 | look-alike measure; decoys -4.5, -9.8 | overview exposes both inputs | hold (author: Too easy ~55%) |
| i04 | author h4: definitions applied to a hypothetical respondent | Gold "1 screening, no health check-up" | D05 L51-52; D04 L77-78 | definition applied to a case | one-sentence exclusions (measured Too easy pattern); rule-10 risk | hold (author: Too easy ~50%) |
| h4/h7 | caller holds (tiers on CHFS; same-direction covariates) | - | hooks.md | - | Too easy risk / ambiguity | hold |

Round 2 (2026-10-08): a second independent question-author searched for untied hidden-scope traps and
3+-step cross-document derived numerics outside q01's family and returned no sketches (raw:
runs/sketch-r1/author-B.md; eleven families R2-a to R2-k rejected with recomputed reasons). Both authors,
both q01 reviews and the caller agree: q01 is the only Medium-plausible design; Hard is unsupported here.
Round 3 not run: every text is fully read and the cross-document relationships are exhausted.
Quick-test batch for the user: notes/quicktest-batch.md (q01, i01, i02, S2, S3).
2026-10-08 after the platform result: q01 dropped; the batch is now i01, i02, S2, S3. All four read descriptive
tables (Doc 2 Table 1; Doc 3/Doc 4 Tables 4-6), not a decomposition or regression table, so their risk is Too easy
or Easy rather than "Answer not supported". Medium for any of them needs the low model to miss 5 of 5; quick-test
first and write up only a survivor.

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.
Require decoys for which-items; use wrong-route calculations for selected rounding/exclusion
levers. Other hooks may be not applicable. Ordinary valid cross-document reasoning remains eligible.
Preserve failed screens and whether revisions change the actual evidence/mechanism.
