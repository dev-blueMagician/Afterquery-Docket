# aq-01650 quick-test batch (round 1, 2026-10-08)

For the task page's "Question drafts" panel: paste each question and its short answer, then quick-test
them all at once (0 of 10 quick tests used). A quick test runs only the easier (low) model, never sets a
tier and never affects pay. For a Medium placement the low model must miss all five attempts in the
difficulty check, so "Too easy - solver got it" on a quick test means the sketch cannot reach Medium.
"Survived" is necessary, not sufficient. Every gold below was recomputed by script.

Origin of every sketch: claude (S1/S2/S3 by the caller, i01/i02 by the independent question-author).
Ids: local Dnn (page Doc N): D01 = Doc 5, D03 = Doc 2, D04 = Doc 3, D05 = Doc 4.

## 1. q01 (S1) - DROPPED 2026-10-08 (do not test)

A platform difficulty check on version 1923ac (rev 1 plus ", including those with missing background
information,") ended "Answer not supported", Low 3/5: the high model never consulted the decomposition table
holding the gold's input and answered 13.7 three times. A pointer to that table would make it Easy or Too easy
(Easy is full). Kept below only as a record.

Rev 0 (without "all") was blocked by the form's free "One defensible answer" check on 2026-10-08: both
form solvers answered 13.7. Rev 1 added "all"; rev 2 also names both surveys more precisely (the user's
request after the form's "Narrow the description" advisories). Screen it in the form's free check first.

Question:
On each survey's own literacy test, how many percentage points higher was the average share of questions answered correctly by all non-student respondents to the Central Council for Financial Services Information's Financial Literacy Survey 2016 in Japan than by households in the China Household Finance Survey's 2015 wave? Give one decimal place.

Answer: 9.2 percentage points

Mechanism: Doc 5 prints its only overall literacy mean (15.2) for the 15,228 complete cases; the
23,788 non-students' mean must be rebuilt from the decomposition table's sex-specific means and counts
(14.0872 of 25 = 56.349%), then set against Doc 2's 2015 mean (1.414 of 3 = 47.133%). Wrong routes:
13.7 (complete cases), 9.3 (unweighted), 9.4 (complete-case weights). Independent review: Too easy 15%,
Easy 45%, Medium 22%, Between levels 10%, Hard/Too hard 3%, Answer not supported 5%.

## 2. i01 - sketch (independent author)

Question:
Osaka University's Preference Parameters Study panel (respondents aged 40 or over, matched across its 2010 and 2011 waves) and China's 2015 Household Finance Survey each posed three basic financial-literacy questions. What was the panel's share answering at least two correctly minus the Chinese survey's share, in percentage points to one decimal?

Answer: 24.7 percentage points

Mechanism: Doc 4's Table 6 splits respondents at an average score of 0.5, which on three questions means
two or three correct (1,805 of 2,693 = 67.03%); Doc 2's 2015 distribution gives 31.55 + 10.77 = 42.32%.
Wrong route: Doc 4's "Average financial literacy was 0.62" read as a share gives 19.7. Author's estimate:
Too easy ~45%, Easy ~40%, Medium ~12%. Shares Doc 2's Table 1 with q01 (different cells).

## 3. i02 - sketch (independent author)

Question:
In the 2011 wave of the Preference Parameters Study panel, which of university graduates, the unemployed, smokers, drinkers and frequent gamblers had a higher raw past-year rate than their counterparts for one of these but lower for the other: a non-mandatory health check-up (ages 40–64), or a non-breast, non-uterine cancer screening (ages 40+)? List in the order given.

Answer: University graduates, the unemployed, drinkers

Mechanism: Doc 3 Tables 4-5 (check-up rates) against Doc 4 Tables 4-5 (any-screening rates, from the
zero rows); smokers and frequent gamblers are lower on both. Author's estimate: Too easy ~40%, Easy ~40%,
Medium ~15%. 58 words.

## 4. S2 - sketch (caller)

Question:
In the 2011 wave of Osaka University's Preference Parameters Study, what was women's share of 40-to-64-year-olds who had a non-mandatory health check-up in the past year, minus women's share of respondents aged 40 or older who had any cancer screening other than breast or uterine? Answer in percentage points to one decimal place.

Answer: 14.5 percentage points

Mechanism: the tables print rates within each sex (women 36.99% had a check-up; 53.67% had no screening);
the asked shares run the other way: 418 / 701 = 59.63% and 624 / 1,382 = 45.15%. Using the printed
within-sex rates gives -9.3 (sign flips). Caller's estimate: Easy-leaning, Medium ~10%.

## 5. S3 - sketch (caller)

Question:
In Osaka University's 2011 Preference Parameters Study data, 40-to-64-year-olds in one education group (university degree or not) were less likely to have had a non-mandatory health check-up. On average, how many types of cancer screening other than breast or uterine did respondents aged 40 or older in that group take? Two decimal places.

Answer: 1.36

Mechanism: Doc 3 shows degree holders were less likely to take the check-up (28.89% vs 32.76%), the
opposite of the usual expectation; Doc 4's degree-holder column gives 902 screenings over 665 people.
Wrong routes: the printed overall mean 1.15; the other group's 1.08. Caller's estimate: Easy-leaning,
Medium ~10%.

## Held, not proposed

- i03 (CHFS none-correct 11.67% minus the UK 11% all-wrong figure, +0.7): both inputs are in the bundle
  overview; Too easy ~55%.
- i04 (coding a hypothetical respondent under both Osaka papers' definitions): one-sentence exclusions,
  the measured Too easy pattern, and a rule-10 risk.

## Set notes

i02, S2 and S3 all read Doc 3/Doc 4 Tables 4-5; q01 and i01 both read Doc 2's Table 1. Fine for a quick
test; submit at most one per family.
