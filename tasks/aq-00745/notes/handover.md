# aq-00745 hand-over: form fields (complete capture; updated 2026-10-06 for the Medium target)

Platform Doc N = local Dnn for every document in this bundle. Origin of all content: claude
(Claude Code, Opus 5.5). The form's "I wrote this question myself." cannot be ticked truthfully
for this content; that decision and the AI-use terms are yours. No platform test has been run by
this workspace; the form showed "Quick tests used: 3 of 10" in the capture, results not supplied.

The bundle was re-ingested from AQ-00745_2026-10-06_0256.md (11 of 11 documents in full). q01 and
q03 keep exactly the same form fields as before; only their local checks were re-run on the
complete documents (rev 1). Line numbers below are for orientation only; quotes are what the form
checks.

## q09 (rev 1, tested_sha256 a33b813ef217...) — MEDIUM candidate, use this one

Platform: user reports "passed as a High tier" (2026-10-06).

Replaces q08 (and q01) on the platform form; do not keep both. Local status checked (review ready,
difficulty medium, marginal). Built from the measured runs: the low model reliably took the
release's own later range for an event it reported; the medium/high models saw through it when the
release tied its guidance change to that event ("Updates Guidance to Reflect Acquisition"). Here the
event (FreeDM2 trial results, March) has no such tie, as in the aq-00964 Medium pass. Paste the
question exactly as written: last time a rewording created the ambiguity the Coach flagged.

### Question

By what percentage did the midpoint of Abbott's full-year 2026 adjusted diluted EPS guidance change from the range in force when it announced results from the FreeDM2 trial to the range it issued in July 2026? Give the sign, to one decimal place.

### Number of asks

1

### Gold answer

-2.6%

### Step-by-step reasoning

Step 1. Doc 8: "In March, Abbott announced results from the FreeDM2 randomized controlled trial". Doc 8 is dated April 16, 2026, so those results were announced in March 2026, and the full-year range Doc 8 itself gives ($5.38 to $5.58) was only issued on April 16, 2026.

Step 2. Doc 7: the range issued on Jan. 22, 2026, the latest full-year 2026 range issued before Doc 8's, is $5.55 to $5.80, so it was the range in force in March 2026, with a midpoint of (5.55 + 5.80) / 2 = 5.675.

Step 3. Doc 10: the range issued on July 16, 2026 is $5.45 to $5.60, with a midpoint of (5.45 + 5.60) / 2 = 5.525.

Step 4. Doc 7 and Doc 10: percentage change of the midpoint = ((5.45 + 5.60) - (5.55 + 5.80)) / (5.55 + 5.80) = -2.6% (to one decimal place).

Conclusion: the midpoint changed by -2.6%.

Decoy (Doc 8 and Doc 10): taking Doc 8's own range as the one in force when the FreeDM2 results were announced gives ((5.45 + 5.60) - (5.38 + 5.58)) / (5.38 + 5.58) = +0.8%, the same figure Doc 10's own comparison with its "previous range of $5.38 to $5.58" gives.

### Answer components

- -2.6%

### Necessary documents

Doc 7, Doc 8, Doc 10 (mark all three; Doc 8 is the only source of the FreeDM2 date)

### Reasoning tags

Temporal alignment; Cross-document join

### Evidence passages (document, then exact quote)

- Doc 8 [c1] (l.37, Q1 2026 highlights): "In March, Abbott announced results from the FreeDM2 randomized controlled trial"
- Doc 8 [c1] (l.21, dateline): "ABBOTT PARK, Ill., April 16, 2026"
- Doc 8 [c1] (l.223, financial guidance; decoy): "Abbott projects full-year 2026 adjusted diluted earnings per share of $5.38 to $5.58"
- Doc 7 [c1] (l.19, dateline): "ABBOTT PARK, Ill., Jan. 22, 2026"
- Doc 7 [c1] (l.335, financial guidance): "Abbott projects full-year 2026 adjusted diluted earnings per share of $5.55 to $5.80"
- Doc 10 [c1] (l.21, dateline): "ABBOTT PARK, Ill., July 16, 2026"
- Doc 10 [c1] (l.329, financial guidance): "Abbott projects full-year 2026 adjusted diluted earnings per share of $5.45 to $5.60"
- Doc 10 [c1] (l.29, highlights; decoy): "compared to previous range of $5.38 to $5.58"

### Local evidence summary

Two fresh blind solves matched (-2.6%, high confidence); closed-book answered "unknown"; shortcut audit clear (Doc 7, 8 and 10 each hold a fact nothing else supplies); review ready, difficulty medium (marginal). Rev 0 (the same question as a low-end change, -$0.10) was dropped because a closed-book estimate reached it.

### Watch on the form

- Expected placement: Medium if the low model takes Doc 8's range on all attempts and the medium model sometimes sees through it. Risks: Easy if one low attempt is right (q01's layout drew Low 1/5); too hard if the medium model never sees through it.
- Expect advisories: "may be too vague" (solvers agreeing on +0.8%) and "No single passage gives the answer" (Doc 10's previous-vs-new sentence gives +0.8%). Neither states -2.6%.
- If the form's reasoning check flags Step 2 ("March 2026" is not printed in Doc 7), change only that step to "...so it was the range in force in March, with a midpoint..." — reasoning edits do not need a new difficulty run; tell me so I can record it.

## q01 (rev 1, tested_sha256 dbae27b24ec2...)

Primary candidate. Local status checked (review ready, difficulty easy, marginal). Same
mechanism as the aq-00964 q01 platform pass (event in a later release whose own range postdates it).

### Question

By how much, in dollars to the nearest cent, did the midpoint of Abbott's full-year 2026 adjusted diluted EPS guidance change from the range in force when it completed its acquisition of Exact Sciences to the range it issued in July 2026? Give the sign.

### Number of asks

1

### Gold answer

-$0.15

### Step-by-step reasoning

Step 1. Doc 8: "On March 23, 2026, Abbott completed its acquisition of Exact Sciences". Doc 8 itself is dated April 16, 2026, so the full-year 2026 range it gives ($5.38 to $5.58, which it says includes the acquisition's dilution) was issued after the closing and was not yet in force on March 23, 2026.

Step 2. Doc 7: the range issued on Jan. 22, 2026, the latest full-year 2026 range before the closing, is adjusted diluted earnings per share of $5.55 to $5.80, a midpoint of (5.55 + 5.80) / 2 = 5.675.

Step 3. Doc 10: the range issued on July 16, 2026 is $5.45 to $5.60, a midpoint of (5.45 + 5.60) / 2 = 5.525.

Step 4. Doc 7 and Doc 10: change in the midpoint = (5.45 + 5.60) / 2 - (5.55 + 5.80) / 2 = -0.15.

Conclusion: the midpoint changed by -$0.15.

Decoy: Doc 10 describes its range as a raise "compared to previous range of $5.38 to $5.58", which is Doc 8's April range. Treating that range as the one in force at the closing gives (5.45 + 5.60) / 2 - (5.38 + 5.58) / 2 = 0.045.

### Answer components

- -$0.15

### Necessary documents

Doc 7, Doc 8, Doc 10

### Reasoning tags

Temporal alignment; Cross-document join

### Evidence passages (document, then exact quote)

- Doc 8 [c1] (l.27, Q1 2026 highlights): "On March 23, 2026, Abbott completed its acquisition of Exact Sciences"
- Doc 8 [c1] (l.21, dateline): "ABBOTT PARK, Ill., April 16, 2026"
- Doc 8 [c1] (l.223, financial guidance): "adjusted diluted earnings per share of $5.38 to $5.58, which includes $0.20 of dilution related to the acquisition of Exact Sciences"
- Doc 7 [c1] (l.19, dateline): "ABBOTT PARK, Ill., Jan. 22, 2026"
- Doc 7 [c1] (l.335, financial guidance): "Abbott projects full-year 2026 adjusted diluted earnings per share of $5.55 to $5.80"
- Doc 10 [c1] (l.21, dateline): "ABBOTT PARK, Ill., July 16, 2026"
- Doc 10 [c1] (l.329, financial guidance): "Abbott projects full-year 2026 adjusted diluted earnings per share of $5.45 to $5.60"
- Doc 10 [c1] (l.29, highlights; decoy source): "compared to previous range of $5.38 to $5.58"

### Local evidence summary

Two fresh blind solves matched (-$0.15, high confidence); closed-book missed (-$0.20 guess); shortcut audit clear; review ready, easy (marginal). Risks the review named: the correct base is also the first 2026 range; the bridge facts are plain sentences; the page's bundle overview prints every input (but no midpoint or change); the January range is recallable without the documents.

### Watch on the form

- Step 4 cites Doc 7 and Doc 10 together; the form's reaction to a two-document step is not yet observed.
- The Doc 10 'previous range' quote supports ruling out the decoy; the evidence advisory may flag it.

## q03 (rev 1, tested_sha256 885ef14edf5c...)

Second candidate. Local status checked (review ready, difficulty easy, marginal; too-easy risk moderate to high).

### Question

Using the business structure Abbott adopted in 2026, by how much did reported sales of its Rapid and Molecular Diagnostics business change from the second half of 2025 to the first half of 2026? Answer in millions of dollars, with the sign.

### Number of asks

1

### Gold answer

-$318 million

### Step-by-step reasoning

Step 1. Doc 10: "Beginning in 2026, Abbott aggregated its previously reported Rapid Diagnostics, Molecular Diagnostics, and Point of Care businesses into the Rapid and Molecular Diagnostics business." Its first-half 2026 Diagnostics table reports Rapid/Molecular Diagnostics sales of 1,567 ($ in millions).

Step 2. Doc 4: third-quarter 2025 sales were Molecular 131, Point of Care 158 and Rapid Diagnostics 600 ($ in millions), so the combined business had 131 + 158 + 600 = 889.

Step 3. Doc 7: fourth-quarter 2025 sales were Molecular 141, Point of Care 158 and Rapid Diagnostics 697, so the combined business had 141 + 158 + 697 = 996.

Step 4. Doc 4, Doc 7 and Doc 10: change from the second half of 2025 to the first half of 2026 = 1,567 - (131 + 158 + 600) - (141 + 158 + 697) = -318.

Conclusion: reported sales of the business fell by $318 million, a change of -$318 million.

Decoy: leaving out Point of Care, whose name the new business does not carry, gives 1,567 - (131 + 600) - (141 + 697) = -2 (Doc 4, Doc 7 and Doc 10 figures), an apparently flat business.

### Answer components

- -$318 million

### Necessary documents

Doc 7, Doc 10

### Reasoning tags

Entity resolution; Cross-document join; Aggregation; Temporal alignment

### Evidence passages (document, then exact quote)

- Doc 10 [c1] (l.203, Diagnostics table footnote): "Abbott aggregated its previously reported Rapid Diagnostics, Molecular Diagnostics, and Point of Care businesses into the Rapid and Molecular Diagnostics business"
- Doc 10 [c1] (l.187, 1H26 Diagnostics table header): "Total Core Laboratory Cancer Diagnostics Rapid/Molecular Diagnostics"
- Doc 10 [c1] (l.191, 1H26 Diagnostics table, total reported row): "5,272 2,690 1,015 1,567"
- Doc 7 [c1] (l.173, 4Q25 Diagnostics table header): "Total Core Laboratory Molecular Point of Care Rapid Diagnostics"
- Doc 7 [c1] (l.175, 4Q25 Diagnostics table, total reported row): "2,457 1,461 141 158 697"
- Doc 4 [c1] (l.177, 3Q25 Diagnostics table header; unlisted source): "Total Core Laboratory Molecular Point of Care Rapid Diagnostics"
- Doc 4 [c1] (l.179, 3Q25 Diagnostics table, total reported row; unlisted source): "2,253 1,364 131 158 600"

### Local evidence summary

Two fresh blind solves matched (-$318 million, high confidence); closed-book answered "unknown"; shortcut audit clear; review ready, easy (marginal). The complete tables confirm the regrouping is a pure sum (the 2026 releases' recast growth rates reproduce exactly from the old three lines).

### Watch on the form

- Step 2 and Step 4 cite Doc 4, which is deliberately not marked necessary: Doc 3 can replace it (full year minus first half). If the form's derive step proposes Doc 4, keep only Doc 7 and Doc 10 as necessary; if the form objects, tell me and I will re-run checks on a revision that lists it.
- Step 4 and the decoy line cite three documents together; the form's reaction is not yet observed.

## q05 (rev 0, tested_sha256 b5701f231afc...)

Third candidate, new this round and only possible with the complete tables. Local status checked
(review ready, difficulty easy, marginal; too-easy risk high). Read the two risks under "Watch on
the form" before using it.

### Question

By how many percentage points did Abbott's full-year 2025 adjusted operating margin differ from the figure in its most recent outlook for that margin? Give the sign, to one decimal place.

### Number of asks

1

### Gold answer

-0.3 percentage points

### Step-by-step reasoning

Step 1. Doc 1 (Jan. 22, 2025) projected a full-year 2025 adjusted operating margin of 23.5% to 24.0% of sales, and Doc 2 (April 16, 2025) repeated that range.

Step 2. Doc 3 (July 17, 2025) changed the projection to approximately 23.5% of sales. Doc 4 (Oct. 15, 2025) reaffirmed only its sales growth and adjusted EPS guidance and gave no margin figure, so Doc 3's figure is the most recent outlook for that margin.

Step 3. Doc 7: full-year 2025 net sales were 44,328, and the full-year reconciliation gives adjusted gross margin 25,151, adjusted R&D 2,830 and adjusted SG&A 12,020 ($ in millions), so the adjusted operating margin = (25,151 - 2,830 - 12,020) / 44,328 = 23.24%.

Step 4. Doc 3 and Doc 7: difference = (25,151 - 2,830 - 12,020) / 44,328 - 23.5% = -0.3 percentage points (to one decimal place).

Conclusion: Abbott's full-year 2025 adjusted operating margin came in below the figure in its most recent outlook, a difference of -0.3 percentage points.

Decoy (Doc 1 and Doc 7): taking the midpoint of the January 2025 range instead gives (25,151 - 2,830 - 12,020) / 44,328 - (23.5 + 24.0) / 2 = -0.5. Decoy (Doc 3 and Doc 7): using adjusted earnings before taxes in place of operating earnings gives 10,762 / 44,328 - 23.5% = +0.8, the wrong sign.

### Answer components

- -0.3 percentage points

### Necessary documents

Doc 3, Doc 7

### Reasoning tags

Cross-document join; Temporal alignment

### Evidence passages (document, then exact quote)

- Doc 3 [c1] (l.349, financial guidance): "Abbott projects full-year 2025 adjusted operating margin to be approximately 23.5% of sales"
- Doc 3 [c1] (l.21, dateline): "ABBOTT PARK, Ill., July 17, 2025"
- Doc 7 [c1] (l.377, footnote 2): "In the full-year 2025, total worldwide sales were $44.328 billion"
- Doc 7 [c1] (l.553, reconciliation title): "Non-GAAP Reconciliation of Financial Information Twelve Months Ended December 31, 2025"
- Doc 7 [c1] (l.557, reconciliation column header): "As Reported (GAAP) Specified Items As Adjusted"
- Doc 7 [c1] (l.563, 12M25 reconciliation; see the format note below): "| Gross Margin | 23,327 | 1,824 | 25,151 |"
- Doc 7 [c1] (l.564, 12M25 reconciliation; see the format note below): "| R&D | 2,942 | (112) | 2,830 |"
- Doc 7 [c1] (l.565, 12M25 reconciliation; see the format note below): "| SG&A | 12,332 | (312) | 12,020 |"
- Doc 4 [c1] (l.339, guidance with no margin figure; not marked necessary): "Abbott reaffirms previously provided full-year 2025 organic sales growth guidance of 7.5% to 8.0%"
- Doc 1 [c1] (l.372, earlier range, decoy source; not marked necessary): "Abbott projects full-year 2025 adjusted operating margin to be 23.5% to 24.0% of sales"

### Local evidence summary

Two fresh blind solves matched (-0.3, high confidence; both reproduced Abbott's printed quarterly margins with the same method). Two closed-book runs gave the wrong sign (+0.2 at sketch stage, +0.1 on the frozen wording). Shortcut audit clear. Review ready, easy (marginal), too-easy risk high.

### Watch on the form

- Quote format: the three Doc 7 table rows above are rows this capture shows as Markdown pipe tables (they were the hidden blocks in the first capture). The platform's own messages show such rows without pipes (on aq-00949 it quoted "Other International (C) - - - - - - - 4 1"). If the form says these quotes are not found, select the rows on the platform page and use Save passage to copy them in the platform's own form, then tell me the exact text: changing the evidence makes a new revision, which I then re-check. No other passage carries these three figures.
- One clear answer: Doc 7's highlight says "$44.3 billion" (its footnote 2 gives $44.328 billion). A solver using the rounded headline gets -0.2 instead of -0.3, because the exact result (-0.262) sits 0.012 points from the rounding boundary. If the platform returns "answered inconsistently", this is the cause.
- Quick test first: the platform's quick test needs only the question and the short answer, so neither risk above affects it.

## q02 (rev 1; records bound to the clipped capture)

Local status checked on the clipped capture only (rev 1 review: ready, easy, marginal, high too-easy risk). Not re-run on the complete documents.

### Question

During calendar 2025 and the first half of calendar 2026, in which quarters, if any, did Abbott's adjusted diluted EPS equal the top of the range it had projected for that quarter? List them in chronological order.

### Number of asks

1

### Gold answer

Q1 2025 and Q2 2026

### Step-by-step reasoning

Step 1. Doc 1: Abbott projected first-quarter 2025 adjusted diluted EPS of $1.05 to $1.09.

Step 2. Doc 2: first-quarter 2025 adjusted diluted EPS was $1.09, the top of the Step 1 range. Doc 2 also projected second-quarter 2025 adjusted diluted EPS of $1.23 to $1.27.

Step 3. Doc 3: second-quarter 2025 adjusted diluted EPS was $1.26, below the top of the Step 2 range. Doc 3 also projected third-quarter 2025 adjusted diluted EPS of $1.28 to $1.32.

Step 4. Doc 4: third-quarter 2025 adjusted diluted EPS was $1.30, below the top of the Step 3 range. Doc 4's guidance gives only a full-year 2025 range of $5.12 to $5.18 and no fourth-quarter range.

Step 5. Doc 7: fourth-quarter 2025 adjusted diluted EPS was $1.50, with no quarterly range to meet. Doc 7 also projected first-quarter 2026 adjusted diluted EPS of $1.12 to $1.18.

Step 6. Doc 8: first-quarter 2026 adjusted diluted EPS was $1.15, below the top of the Step 5 range. Doc 8 also projected second-quarter 2026 adjusted diluted EPS of $1.25 to $1.31.

Step 7. Doc 10: second-quarter 2026 adjusted diluted EPS was $1.31, the top of the Step 6 range.

Conclusion: in chronological order, Q1 2025 and Q2 2026.

Decoy: Q2 2025 beat the midpoint of its range but stopped one cent short of the top ($1.26 against $1.27).

### Answer components

- Q1 2025
- Q2 2026

### Necessary documents

Doc 1, Doc 2, Doc 3, Doc 4, Doc 7, Doc 8, Doc 10

### Reasoning tags

Cross-document join; Temporal alignment; Conditional filter

### Evidence passages (document, then exact quote)

- Doc 1 [c1] (l.319, financial guidance; old line numbering): "first-quarter 2025 adjusted diluted earnings per share of $1.05 to $1.09"
- Doc 2 [c1] (l.17, highlights; old line numbering): "First-quarter GAAP diluted EPS of $0.76; adjusted diluted EPS of $1.09"
- Doc 2 [c1, c2] (l.201, financial guidance; old line numbering): "second-quarter 2025 adjusted diluted earnings per share of $1.23 to $1.27"
- Doc 3 [c1, c2] (l.17, highlights; old line numbering): "Second-quarter GAAP diluted EPS of $1.01; adjusted diluted EPS of $1.26"
- Doc 3 [c1, c2] (l.299, financial guidance; old line numbering): "third-quarter 2025 adjusted diluted earnings per share of $1.28 to $1.32"
- Doc 4 [c1, c2] (l.17, highlights; old line numbering): "Third-quarter GAAP diluted EPS of $0.94; adjusted diluted EPS of $1.30"
- Doc 4 [c1, c2] (l.287, financial guidance; old line numbering): "narrows the range to $5.12 to $5.18"
- Doc 7 [c1, c2] (l.17, highlights; old line numbering): "Fourth-quarter GAAP diluted EPS of $1.01; adjusted diluted EPS of $1.50"
- Doc 7 [c1, c2] (l.283, financial guidance; old line numbering): "first-quarter 2026 adjusted diluted earnings per share of $1.12 to $1.18"
- Doc 8 [c1, c2] (l.17, highlights; old line numbering): "First-quarter GAAP diluted EPS of $0.61; adjusted diluted EPS of $1.15"
- Doc 8 [c2] (l.205, financial guidance; old line numbering): "second-quarter 2026 adjusted diluted earnings per share of $1.25 to $1.31"
- Doc 10 [c2] (l.17, highlights; old line numbering): "Second-quarter GAAP diluted EPS of $0.53; adjusted diluted EPS of $1.31"

## q04 (rev 0; records bound to the clipped capture)

Local status checked on the clipped capture only (rev 0 review: revise; per-item printed status, evidence quotes stop before "Duo"). Optional quick test only; not re-run.

### Question

Between January and June 2026, which Abbott products did the company announce had received a regulatory approval or CE Mark? List them in date order, or say none.

### Number of asks

1

### Gold answer

TactiFlex Duo ablation catheter and Libre Duo sensor

### Step-by-step reasoning

Step 1. Doc 7 is dated Jan. 22, 2026: "In January, Abbott announced the company obtained CE Mark for its TactiFlex Duo Ablation Catheter", so that announcement came in January 2026. The same release's other approval, "In December, Abbott announced U.S. Food and Drug Administration (FDA) approval for its Volt PFA System", was announced in December 2025, before the period.

Step 2. Doc 8 is dated April 16, 2026: its January, February and March 2026 items are a collaboration with AtaCor Medical, early results from the VERITAS study and results from the FreeDM2 trial, none of them an approval.

Step 3. Doc 10 is dated July 16, 2026: "In May, Abbott announced it secured CE Mark for Libre Duo". Its other May items are a "submission to the U.S. Food and Drug Administration (FDA) seeking approval" for the Amulet 360 device, which is a request rather than an approval, and American Cancer Society screening guidelines, which are not a regulatory approval; its April items are trial enrollment and conference data.

Conclusion: in date order, the TactiFlex Duo ablation catheter (January 2026) and the Libre Duo sensor (May 2026).

Decoy: Doc 7 introduces Volt and TactiFlex Duo together as "two significant regulatory approvals", but only the January announcement falls in 2026.

### Answer components

- TactiFlex Duo ablation catheter
- Libre Duo sensor

### Necessary documents

Doc 7, Doc 10

### Reasoning tags

Temporal alignment; Conditional filter; Cross-document join

### Evidence passages (document, then exact quote)

- Doc 7 [c1] (l.19, dateline; old line numbering): "ABBOTT PARK, Ill., Jan. 22, 2026"
- Doc 7 [c1] (l.39, highlights; old line numbering): "In January, Abbott announced the company obtained CE Mark for its TactiFlex"
- Doc 7 [c1] (l.37, highlights; excluded item; old line numbering): "In December, Abbott announced U.S. Food and Drug Administration (FDA) approval for its Volt"
- Doc 10 [c2] (l.21, dateline; old line numbering): "ABBOTT PARK, Ill., July 16, 2026"
- Doc 10 [c2] (l.35, highlights; old line numbering): "In May, Abbott announced it secured CE Mark for Libre"
- Doc 10 [c2] (l.37, highlights; excluded item; old line numbering): "completed its submission to the U.S. Food and Drug Administration (FDA) seeking approval"
- Doc 8 [c1, c2] (l.21, dateline; unlisted completeness source; old line numbering): "ABBOTT PARK, Ill., April 16, 2026"
- Doc 8 [c1, c2] (l.33, highlights; unlisted completeness source; old line numbering): "In January, Abbott announced a collaboration with AtaCor Medical"
