# aq-01650 round-1 author return (question-author subagent, origin claude, 2026-10-08)

Raw hand-back, verbatim as delivered to the caller (harness indentation removed).

## aq-01650, round-1 sketches (writer origin: claude)

**I found no fair design that uses a mechanism the platform has measured at Medium. There is no fair Hard design either.** All four sketches below are fair, cross-document and Easy-leaning. My Medium estimate is 15% or less for each. The task page shows the Easy slot full (one question in review), so an Easy result cannot be accepted here. The platform's quick tests cost nothing ("Quick tests used: 0 of 10"). I suggest quick-testing i02, i01 and i04 before spending any difficulty run, and telling the user early that Medium is unlikely on this document set.

How I read the bundle:
- I read all seven texts in full (`D:\Agents\Docket\tasks\aq-01650\text\D01.txt` … `D07.txt`).
- `notes/doc-map.md` was still the empty template when I read it, so every fact below comes from the texts.
- I also read the capture's bundle overview (`D:\Agents\Docket\AQ-01650_2026-10-08_0005.txt`, lines 26–79) only to check which facts it exposes.
- Document numbers: D01=Doc 5, D02=Doc 6, D03=Doc 2, D04=Doc 3, D05=Doc 4, D06=Doc 1, D07=Doc 7.

---

### i02 (ranked first)
- **id:** i02
- **difficulty_target:** medium. Honest estimate: Too easy ~40%, Easy ~40%, Medium ~15%, Answer not supported ~5%.
- **question (58 words):** In the 2011 wave of the Preference Parameters Study panel, which of university graduates, the unemployed, smokers, drinkers and frequent gamblers had a higher raw past-year rate than their counterparts for one of these but lower for the other: a non-mandatory health check-up (ages 40–64), or a non-breast, non-uterine cancer screening (ages 40+)? List in the order given.
- **answer:** University graduates, the unemployed, drinkers
- **facts:**
  - D04/Doc 3 Table 4 (L209–218) gives health check-up rates:
    - below a university degree 534/1630 = 32.76%; above 167/578 = 28.89%
    - not unemployed 680/2156 = 31.54%; unemployed 21/52 = 40.38%
  - D04/Doc 3 Table 5 (L226–235):
    - non-smokers 594/1692 = 35.11%; smokers 107/516 = 20.74%
    - non-drinkers 387/1134 = 34.13%; drinkers 314/1074 = 29.24%
    - non-gamblers 643/1974 = 32.57%; gamblers 58/234 = 24.79%
  - D04 scope (L77): "excluding health check-ups organized by employers and schools".
  - D05/Doc 4 Tables 4–5 (L84–99, L109–124) give the 0-screening row; at least one screening = complement:
    - below a degree 48.57%; above 59.70%
    - not unemployed 51.63%; unemployed 36.36%
    - non-smokers 53.51%; smokers 43.40%
    - non-drinkers 49.22%; drinkers 53.62%
    - non-gamblers 51.42%; gamblers 50.38%
  - D05 scope (L52): "other than breast and uterine cancers, which were excluded".
- **documents:** D04/Doc 3, D05/Doc 4
- **dependency:** Each document is the only source of one outcome's direction. No other document cross-tabulates either outcome by these groups. Removing either leaves the reversal undetermined. I left sex out of the list on purpose: it reverses too (women 36.99% vs men 26.25% for check-ups; men 56.32% vs women 46.33% for screening) but is the most guessable without the documents.
- **selected_levers:** Scatter the pieces; Calculate across documents (complement rates).
- **lever_checks:**
  - Decoys that fail the test:
    - Smokers are lower in both (20.74 vs 35.11; 43.40 vs 53.51).
    - Frequent gamblers are lower in both (24.79 vs 32.57; 50.38 vs 51.42). D05's prose (L103) says it "did not find a sizeable disparity" for gamblers.
  - Recomputed wrong lists:
    - Dropping drinkers, because D05's prose limits drinkers' higher screening to "those taking more than two cancer tests", gives "university graduates, the unemployed".
    - Dropping the unemployed, because D04 (L243) calls that gap "insignificant" and D05 (L78) says only "A similar and significant difference was observed in the unemployment variable", gives "university graduates, drinkers".
    - Using D05's 4-test row (gamblers 4.17% vs 3.13%) adds gamblers.
  - Robustness: the directions are identical using mean screening counts (graduates 1.356 vs 1.083; unemployed 0.709 vs 1.160; drinkers 1.244 vs 1.066; smokers 0.940 vs 1.209; gamblers 1.080 vs 1.159).
- **arithmetic_check:** Python, all rates from counts; every D04 rate matches its printed %. "Rate" means the share with at least one qualifying event in the past 12 months.
- **shortcut_search:** I searched check-up, screening, unemploy, drink, gambl, university, and the overview. No passage lists any reversal.
  - D04's prose (L243–245) states every D04 direction.
  - D05's prose gives education (L78), smoking and drinking (L103, narrowed for drinkers) and gambling (no disparity). The direction for the unemployed is only in D05's table.
  - Strongest surviving route: read both papers' Tables 4–5, about ten comparisons. This is a keyword-filter risk (aq-00745 q01 pattern).
- **tags:** Cross-document join, Conditional filter
- **completeness:** Uses only D04 Tables 4–5 and D05 Tables 4–5 plus prose, all present. D05's missing Tables 1–3 and 7–9 and D04's missing Appendix are irrelevant here.
- **portfolio:** Osaka-panel family. **Gives away i04:** the phrase "non-breast, non-uterine" reveals i04's key exclusion, so do not pair i02 with i04.
- **unresolved:**
  - D04 itself is inconsistent about whether municipal (government) check-ups count (L77 vs L79/L418). The table values are unaffected; "non-mandatory" is D04's own term.
  - A reviewer may want "raw" explained.

### i01 (ranked second)
- **id:** i01
- **difficulty_target:** medium. Honest estimate: Too easy ~45%, Easy ~40%, Medium ~12%.
- **question (~50 words):** Osaka University's Preference Parameters Study panel (respondents aged 40 or over, matched across its 2010 and 2011 waves) and China's 2015 Household Finance Survey each posed three basic financial-literacy questions. What was the panel's share answering at least two correctly minus the Chinese survey's share, in percentage points to one decimal?
- **answer:** 24.7 percentage points
- **facts:**
  - D05/Doc 4 L56: "we adopted 1 as the score for every correct answer and 0 for an incorrect answer and averaged scores of the total 3 responses". The possible scores are 0, 1/3, 2/3 and 1, so a score of at least 0.5 means two or three correct.
  - D05 Table 6 (L134–147): "Score < 0.5" 888; "Score ≥ 0.5" 1805; total 2693.
  - D05 sample (L47): 3403 matched, 710 under 40 excluded, 2693 remain.
  - D03/Doc 2 Table 1 (L100–106), "Correctly" row: 0 = 11.67%, 1 = 46.01%, 2 = 31.55%, 3 = 10.77%. Note: "Calculated by the data of Chinese Household Financial Survey in 2015."
- **documents:** D05/Doc 4, D03/Doc 2
- **dependency:**
  - The panel's distribution exists only in D05 Table 6. D04/Doc 3 gives only a mean (0.6185, for ages 40–64).
  - The 2015 CHFS distribution exists only in D03 Table 1.
  - Neither mean (0.62 / 0.6185) can stand in for the at-least-two share.
- **selected_levers:** Calculate across documents; Unit or basis (an averaged-score threshold converted to a count of correct answers).
- **lever_checks:** Recomputed decoys:
  - Reading "Average financial literacy was 0.62" (D05 L66; also D04 L150 and the overview) as a share gives 62 − 42.32 = 19.7.
  - D04's 0.6185 (wrong sample) gives 19.5.
  - Using only CHFS all-three-correct gives 67.03 − 10.77 = 56.3.
  - Mistaking 888 for the at-least-two group gives 32.97 − 42.32 = −9.4.
- **arithmetic_check:** 1805/2693 = 67.0256%; 31.55 + 10.77 = 42.32%; difference 24.7056. The complement route (100 − 32.97) − (100 − 57.68) gives the same. Every rounding route gives 24.7.
- **shortcut_search:** "At least two" is printed nowhere. D05's prose says only "scores greater than 0.5" (L128). D03's prose gives only the all-three figure and the mean of 1.414 (L108). The overview exposes the 0.62 decoy and the 10.77% figure, not the gold. Strongest route: two labelled tables, one threshold mapping, one subtraction.
- **tags:** Cross-document join, Unit normalization, Aggregation
- **completeness:** D05 Tables 1–2 and D03 Supplementary Table 1 are absent; not used.
- **portfolio:** CHFS-literacy family. Shares D03 Table 1 with i03 (different cells); no answer giveaway.
- **unresolved:** A closed-book "about 25 points" guess is possible but unlikely at one decimal.

### i03 (ranked third)
- **id:** i03
- **difficulty_target:** medium. Honest estimate: Too easy ~55%, Easy ~35%, Medium ~8%.
- **question (48 words):** What was the share of 2015 China Household Finance Survey respondents answering none of its three financial-literacy questions correctly, minus the share of UK household-survey respondents reported as getting every answer wrong on a three-question interest and repayment quiz? Give percentage points with sign, to one decimal.
- **answer:** +0.7 percentage points
- **facts:**
  - D03/Doc 2 Table 1: "Correctly" 0 = 11.67%.
  - Look-alikes in D03: "Unknown" 3 = 6.50%; "Incorrectly" 3 = 1.16%; prose (L108) "Nearly 6.50% of the households knew nothing about these three questions."
  - D06/Doc 1 L31: "11% of the respondents got all the answers wrong" (three questions on simple interest, compound interest and minimum repayment).
- **documents:** D03/Doc 2, D06/Doc 1
- **dependency:** The UK figure exists only in D06 L31; the CHFS zero-correct share only in D03 Table 1.
- **selected_levers:** Calculate across documents; look-alike measure ("knew nothing" or all answers incorrect, vs none correct).
- **lever_checks:** Recomputed decoys:
  - 6.50 − 11 = −4.5
  - 1.16 − 11 = −9.8
  - 10.77 − 11 = −0.2
  - 11.67 − 30 (the UK all-right figure) = −18.3
- **arithmetic_check:** 11.67 − 11 = 0.67, so +0.7. The UK 11% is taken as printed; the answer is given to one decimal for that reason.
- **shortcut_search:** The overview's figure lines expose both the UK 11% (Doc 1) and the CHFS 10.77% (Doc 2). The 6.50% decoy is defused by Table 1's labelled "Correctly 0" cell.
- **tags:** Cross-document join, Conditional filter (the second tag is weak).
- **completeness:** Fully present.
- **portfolio:** Shares D03 Table 1 with i01.
- **unresolved:** Whether the UK "all wrong" counts "don't know" answers. This does not matter because the figure is taken as stated.

### i04 (ranked fourth; a practitioner scenario, which the task page lists as "short of")
- **id:** i04
- **difficulty_target:** medium. Honest estimate: Too easy ~50%, Easy ~35%, Medium ~10%.
- **question (~52 words):** Coding a 58-year-old woman in the 2011 Preference Parameters Study panel whose past-year examinations were stomach and breast cancer screenings plus a health check run by her employer's labor union, how many cancer screenings does she count for, and does she count as having had a health check-up, under the published panel analyses' definitions?
- **answer:** 1 screening, no health check-up (written without a semicolon, as the form requires)
- **facts:**
  - D05 L51–52: the cancer item lists stomach, lung, uterine, breast, colon and other examinations; the count excludes breast and uterine.
  - D04 L77: the check-up variable excludes check-ups "organized by employers and schools".
  - D04 L78: option 2 is "Health check organized by your employee or labor union of your employee". The check-up question itself excludes "cancer examination".
- **documents:** D05/Doc 4, D04/Doc 3
- **dependency:**
  - Without D05, a solver would likely count 2 screenings.
  - Without D04, a solver would likely say "yes" to a check-up.
  - Closed-book, a solver would likely answer 2 and yes.
- **selected_levers:** Definition applied to a case; Scatter the pieces.
- **lever_checks:** Recomputed wrong answers:
  - 2 screenings, no (breast counted)
  - 1 screening, yes (employer check counted)
  - 2 screenings, yes (both rules missed)
  - 0 screenings (D04's employer exclusion wrongly applied to screening)
- **arithmetic_check:** Not applicable.
- **shortcut_search:** Searching "breast" and "employer" lands on the two exclusion sentences. This is the aq-01432 pattern (a one-sentence exception), measured Too easy.
- **tags:** Cross-document join, Conditional filter
- **completeness:** Present.
- **portfolio:** i02's wording gives this question away (see i02).
- **unresolved:** Rule-10 risk: the answer concerns how two analyses code a respondent.

---

### Hook inventory (for notes/hooks.md)
| Hook | Inputs | Decision |
| --- | --- | --- |
| h1 | D04 T4–5 × D05 T4–5: group-wise direction reversals | sketch i02 |
| h2 | D05 T6 (≥0.5 = 2+ correct) × D03 T1 | sketch i01 |
| h3 | D03 T1 (0 correct 11.67; unknown×3 6.50; incorrect×3 1.16) × D06 L31 (UK 11%) | sketch i03 (overview-exposed) |
| h4 | D04 L77–78 exclusions × D05 L52 exclusion (hypothetical) | sketch i04 |
| h5 | 2011 wave: D04 L72 says 4,934; D05 L47 says "4943", but its 54.58% equals 2693/4934 | rejected: a document error on the fact any use depends on; golds split (2,241 vs 2,250; 9.83 vs 9.73) |
| h6 | D01 T5: university endowment 0.676 is 85.1% of endowments but 0.676/1.240 = 54.5% of the total gap | rejected: the bundle's strongest hidden-scope trap, but single-document (no partner anywhere) |
| h7 | D01 T2 complete-case 15.2 (n=15,228) vs T5 non-student means (14.719 × 11,658 + 13.480 × 12,130)/23,788 = 14.087 | rejected: the only partner (PPS share correct) is a different instrument; the gold is fragile (5.49–5.65 at one decimal or whole number) |
| h8 | Income/assets: D01 in 10,000 JPY (515.293; 744.065) vs D04 6,888,813 / 13,500,000 vs D05 6,523,023 / 14,500,000 | rejected: two lookups, a unit conversion and one operation (measured Too easy) |
| h9 | D02 L310 literacy tiers × D03 T1 (middle tier 77.56%; double-count decoy 71.06%) | rejected: the tiers are guessable without D02 (removal test); the question would have to cite "a study" |
| h10 | Concern/attention coding: D03 L112 (only "very" = 1; four categories) vs D06 L205/L215 (five options; "generally" = 1) vs D02 L179 (1–5 scale) | rejected: ambiguous mapping ("extremely" is absent from D03) |
| h11 | D07 L127 overestimation vs overplacement × D01 L127 self-rating "compared with others" | rejected: two defensible readings |
| h12 | D05 L78 "51.43%" is the row share 1043/2028; the true share of non-screened is 1043/1311 = 79.56% | rejected: a document error on the asked fact |
| h13 | CHFS coverage: D02 L164 "355 counties" (pooled 2011–2019) vs D06 L162 "345 cities/counties in 2019" | rejected: lookups with different scopes |
| h14 | D06 sample size: 8,735 (L164) vs 10,846 (tables) vs subgroup sums 10,876 (T8, T10, T11) | rejected: the paper contradicts itself |
| h15 | Financial-education question wording: D04 L83 "elementary" vs D05 L58 "high school" (but D05 L66/L128 say "primary") | rejected: a document error |
| h16 | Regression significance compared across D04 and D05 | rejected: D05 Tables 7–9 are missing; D04's prose (L367–368) misstates significance levels; D03's long-term prose (L171, L293) contradicts Tables 3–4 |
| h17 | The task page's suggested shapes ("Doc 7 ties 2016 to an event", "Marriage in Doc 1 and Doc 2") | not supported: 2016 appears only as citation years; the "Marriage" figures are unrelated coefficients and means |

The number 1,212 appears in both D01 (students excluded) and D04 (ages outside 40–64 removed). The value is the same, so it cannot change any answer.

### Mechanisms tried that produced no fair Medium
- **Edition or forecast traps:** none exist; there are no editions or outlooks.
- **A printed grouped figure split in another document:** none exists. D05's "Score ≥ 0.5" and D04's 1,212 grouping have no valid split, because the two papers' merged pools differ (3,420 vs 3,403).
- **A stated aggregate with hidden scope:** only D01's 85.1% qualifies, and it has no cross-document partner.
- **The two Osaka-panel papers' conflicts** are document errors that would give two defensible answers.
- **Hedge and mentions-vs-does:** no world-framed list that can be proved; for example, the papers do not show that the CHFS lacks a financial-education item.

Further rounds are unlikely to change this: all seven documents are fully read and 17 hooks have been screened.

**Gaps:** None of the four sketches relies on missing material (D05 Tables 1–3 and 7–9; D04 Appendix; D03 Supplementary Table 1). Those gaps only blocked the rejected hooks h16 and some regression-based ideas.
