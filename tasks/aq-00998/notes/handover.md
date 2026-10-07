# aq-00998 hand-over (generated from questions/q05.md, q06.md; never submitted)

Platform numbering: local D01-D12 = task page Doc 1-12. Origin of every question here: claude
(Claude Code, Opus 5.5). The form's "I wrote this question myself." cannot be ticked truthfully
for this content; that decision and the AI-use terms are the user's. Value quotes taken from
tables contain tab characters in the source: check them with Save passage before relying on
the form's verbatim check. q05's two "ROCE earnings" quotes (Doc 10 and Doc 12) exist only as
Markdown pipe rows in the capture ("| ROCE earnings | ... |"); the platform page likely shows
them without pipes, so take those two quotes from Save passage on the platform page. Quick
tests and difficulty checks need no evidence; changing a quote is a new revision with new checks.
q05's last decoy line cites Doc 9 and Doc 11 to show the rounded-ROCE route; they are not necessary
documents. If Derive the rest proposes them, keep only Doc 10 and Doc 12 marked necessary.

## q05 (status ready, rev 4, tested_sha256 17565b4d9669...)

### Question

Using the same method Chevron applies to its full-year return on capital employed, what was Chevron's ROCE for the twelve months ended June 30, 2026? Give the percentage to three decimal places.

### Number of asks

1

### Gold answer

10.869%

### Step-by-step reasoning

Step 1. Doc 10: Chevron's full-year ROCE divides ROCE earnings (reported earnings plus noncontrolling interest plus after-tax interest expense) by average capital employed; for 2025 the table shows ROCE earnings of 13,581, average capital employed of 205,316 and ROCE of 6.6%. Its footnote defines capital employed as stockholders' equity plus total debt plus noncontrolling interest and says average capital employed "is computed by averaging the sum of capital employed at the beginning and the end of the period".

Step 2. Doc 10 and Doc 12: ROCE earnings for the twelve months ended June 30, 2026 are full-year 2025 (Doc 10) minus the first half of 2025 plus the first half of 2026 (Doc 12): 13,581 - 6,469 + 15,135 = 22,247 ($ millions).

Step 3. Doc 10: capital employed at December 31, 2024 is stockholders' equity plus total debt plus noncontrolling interests: 152,318 + 24,541 + 839 = 177,698.

Step 4. Doc 10 and Doc 12: Doc 12's average capital employed for the first half of 2025 is 177,212, the average of capital employed at December 31, 2024 and at the end of that half-year, so capital employed at the end of the first half of 2025 is 2 x 177,212 - (152,318 + 24,541 + 839) = 176,726.

Step 5. Doc 12: capital employed at June 30, 2026 is stockholders' equity plus total debt plus noncontrolling interests: 189,883 + 37,075 + 5,675 = 232,633.

Step 6. Doc 10 and Doc 12: average capital employed for the twelve months is (2 x 177,212 - (152,318 + 24,541 + 839) + 189,883 + 37,075 + 5,675) / 2 = 204,679.5.

Step 7. Doc 10 and Doc 12: ROCE for the twelve months is (13,581 - 6,469 + 15,135) / ((2 x 177,212 - (152,318 + 24,541 + 839) + 189,883 + 37,075 + 5,675) / 2) = 10.869% (to three decimal places).

Decoy check. Doc 12 prints ROCE of 21.4% for the second quarter of 2026 and 13.0% for the first half of 2026, and Doc 10 prints 6.6% for 2025; none covers the twelve months ended June 30, 2026.

Decoy check. Doc 10 and Doc 12: reusing Doc 10's printed full-year average capital employed gives (13,581 - 6,469 + 15,135) / 205,316 = 10.835%.

Decoy check. Doc 10 and Doc 12: dividing by Doc 12's printed six-month 2026 average capital employed gives (13,581 - 6,469 + 15,135) / 232,784 = 9.557%.

Decoy check. Doc 9, Doc 11 and Doc 12: taking Doc 11's rounded fourth-quarter 2025 ROCE of 5.4% at face value in place of the fourth-quarter ROCE earnings gives (3,942 + 5.4% x (189,843 + 41,544 + 5,757 + 186,450 + 40,758 + 5,726) / 8 + 2,603 + 12,532) / ((2 x 177,212 - (152,318 + 24,541 + 839) + 189,883 + 37,075 + 5,675) / 2) = 10.871%.

### Components (check what the form derives)

- c1: 10.869%

### Evidence (local ids; form uses Doc N)

- D10 (l.394, Attachment 2 ROCE header) [c1]: "RETURN ON CAPITAL EMPLOYED (ROCE) Three Months Ended December 31, Year Ended"
- D10 (l.405, Attachment 2) [c1]: "| ROCE earnings | 3,170 | 3,440 | 13,581 | 18,288 |"
- D10 (l.408, Attachment 2) [c1]: "Average capital employed (1) 235,039 180,285 205,316 180,232"
- D10 (l.412, Attachment 2 footnote) [c1]: "Average capital employed is computed by averaging the sum of capital employed at the beginning and the end of the period"
- D10 (l.359, Attachment 2 header) [c1]: "SELECTED BALANCE SHEET ACCOUNT DATA (Preliminary) December 31, 2025 December 31,"
- D10 (l.370, Attachment 2) [c1]: "Total debt $ 40,758 $ 24,541"
- D10 (l.371, Attachment 2) [c1]: "equity $ 186,450 $ 152,318"
- D10 (l.372, Attachment 2) [c1]: "Noncontrolling interests $ 5,726 $ 839"
- D12 (l.378, Attachment 2 ROCE header) [c1]: "RETURN ON CAPITAL EMPLOYED (ROCE) Three Months Ended June 30, Six Months Ended"
- D12 (l.389, Attachment 2) [c1]: "| ROCE earnings | 12,532 | 2,765 | 15,135 | 6,469 |"
- D12 (l.392, Attachment 2) [c1]: "Average capital employed (1) 233,716 178,243 232,784 177,212"
- D12 (l.341, Attachment 2 header) [c1]: "SELECTED BALANCE SHEET ACCOUNT DATA (Preliminary) June 30, 2026 December 31,"
- D12 (l.352, Attachment 2) [c1]: "Total debt $ 37,075 $ 40,758"
- D12 (l.353, Attachment 2) [c1]: "equity $ 189,883 $ 186,450"
- D12 (l.354, Attachment 2) [c1]: "Noncontrolling interests $ 5,675 $ 5,726"

### Documents and tags

Documents: D10, D12 (Doc numbers identical).  Tags: Temporal alignment; Cross-document join; Aggregation.  Levers: Calculate across documents; Exact table vs rounded prose.

## q06 (status checked, rev 1, tested_sha256 29d185e75de6...)

### Question

From 1Q 2024 through 2Q 2026, in which quarters, if any, did Chevron's total debt fall while its net debt (total debt minus cash, cash equivalents, time deposits and marketable securities) rose, compared with the previous quarter-end? List them in date order.

### Number of asks

1

### Gold answer

2Q 2025, 4Q 2025

### Step-by-step reasoning

Step 1. Doc 8, Doc 9, Doc 11 and Doc 12 label the measure "Net debt (Total debt less cash and cash equivalents, time deposits and marketable securities)"; Doc 4 and Doc 6 print the same definition under "Adjusted debt". Each release's balance sheet compares its own quarter-end with the previous December 31, so the previous quarter-end usually comes from the prior release.

Step 2. Doc 2: total debt was 20,836 at December 31, 2023 and 21,835 at March 31, 2024.

Step 3. Doc 3: total debt was 23,184 at June 30, 2024.

Step 4. Doc 4: at September 30, 2024, total debt was 25,841 and adjusted debt was 21,138.

Step 5. Doc 6: total debt was 24,541 at December 31, 2024 and 29,681 at March 31, 2025; adjusted debt was 17,756 and 25,038 at the same dates.

Step 6. Doc 8: at June 30, 2025, total debt was 29,467 and net debt was 25,401.

Step 7. Doc 9: at September 30, 2025, total debt was 41,544 and net debt was 33,817.

Step 8. Doc 11: total debt was 40,758 at December 31, 2025 and 45,428 at March 31, 2026; net debt was 34,461 and 40,101 at the same dates.

Step 9. Doc 12: at June 30, 2026, total debt was 37,075 and net debt was 28,545.

Step 10. Total debt rose from the previous quarter-end in 1Q 2024 (20,836 to 21,835), 2Q 2024 (21,835 to 23,184), 3Q 2024 (23,184 to 25,841), 1Q 2025 (24,541 to 29,681), 3Q 2025 (29,467 to 41,544) and 1Q 2026 (40,758 to 45,428), so none of these quarters qualifies.

Step 11. Total debt fell in 4Q 2024 (25,841 to 24,541) and in 2Q 2026 (45,428 to 37,075), but net debt also fell (21,138 to 17,756, and 40,101 to 28,545), so neither quarter qualifies.

Step 12. In 2Q 2025 total debt fell (29,681 to 29,467) while net debt rose (25,038 to 25,401), and in 4Q 2025 total debt fell (41,544 to 40,758) while net debt rose (33,817 to 34,461). The qualifying quarters in date order are 2Q 2025 and 4Q 2025.

### Components (check what the form derives)

- c1: 2Q 2025
- c2: 4Q 2025

### Evidence (local ids; form uses Doc N)

- D02 (l.325, Attachment 2 header) [c1, c2]: "SELECTED BALANCE SHEET ACCOUNT DATA (Preliminary) March 31, 2024 December 31,"
- D02 (l.334, Attachment 2) [c1, c2]: "Total debt $ 21,835 $ 20,836"
- D03 (l.337, Attachment 2 header) [c1, c2]: "SELECTED BALANCE SHEET ACCOUNT DATA (Preliminary) June 30, 2024 December 31,"
- D03 (l.346, Attachment 2) [c1, c2]: "Total debt $ 23,184 $ 20,836"
- D04 (l.341, Attachment 2 header) [c1, c2]: "SELECTED BALANCE SHEET ACCOUNT DATA (Preliminary) September 30, 2024 December 31,"
- D04 (l.350, Attachment 2) [c1, c2]: "Total debt $ 25,841 $ 20,836"
- D04 (l.362, Attachment 2) [c1, c2]: "Adjusted debt (Total debt less cash and cash equivalents, time deposits and marketable securities) $ 21,138 $ 12,613"
- D06 (l.321, Attachment 2 header) [c1]: "SELECTED BALANCE SHEET ACCOUNT DATA (Preliminary) March 31, 2025 December 31,"
- D06 (l.332, Attachment 2) [c1]: "Total debt $ 29,681 $ 24,541"
- D06 (l.344, Attachment 2) [c1]: "Adjusted debt (Total debt less cash and cash equivalents, time deposits and marketable securities) $ 25,038 $ 17,756"
- D08 (l.347, Attachment 2 header) [c1]: "SELECTED BALANCE SHEET ACCOUNT DATA (Preliminary) June 30, 2025 December 31,"
- D08 (l.358, Attachment 2) [c1]: "Total debt $ 29,467 $ 24,541"
- D08 (l.370, Attachment 2) [c1]: "Net debt (Total debt less cash and cash equivalents, time deposits and marketable securities) $ 25,401 $ 17,756"
- D09 (l.332, Attachment 2 header) [c2]: "SELECTED BALANCE SHEET ACCOUNT DATA (Preliminary) September 30, 2025 December 31,"
- D09 (l.343, Attachment 2) [c2]: "Total debt $ 41,544 $ 24,541"
- D09 (l.355, Attachment 2) [c2]: "Net debt (Total debt less cash and cash equivalents, time deposits and marketable securities) $ 33,817 $ 17,756"
- D11 (l.333, Attachment 2 header) [c2]: "SELECTED BALANCE SHEET ACCOUNT DATA (Preliminary) March 31, 2026 December 31,"
- D11 (l.344, Attachment 2) [c2]: "Total debt $ 45,428 $ 40,758"
- D11 (l.356, Attachment 2) [c2]: "Net debt (Total debt less cash and cash equivalents, time deposits and marketable securities) $ 40,101 $ 34,461"
- D12 (l.341, Attachment 2 header) [c1, c2]: "SELECTED BALANCE SHEET ACCOUNT DATA (Preliminary) June 30, 2026 December 31,"
- D12 (l.352, Attachment 2) [c1, c2]: "Total debt $ 37,075 $ 40,758"
- D12 (l.364, Attachment 2) [c1, c2]: "Net debt (Total debt less cash and cash equivalents, time deposits and marketable securities) $ 28,545 $ 34,461"

### Documents and tags

Documents: D02, D03, D04, D06, D08, D09, D11, D12 (Doc numbers identical).  Tags: Conditional filter; Temporal alignment; Cross-document join.  Levers: Match, then exclude; Scatter the pieces.
