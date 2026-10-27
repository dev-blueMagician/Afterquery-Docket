# i06 strong-solver screen, solve 2 of 3 (blind-solver, fresh context; launch label "i06 blind solve 2")

Judged by the author against gold 74: RIGHT.

answer: $74 million. This is derived by subtraction; no document prints it.
confidence: high

path:
1. D03 (FCX Q1 2026 release), "Derivative Instruments", page VII, text/D03.txt lines 739–751. The table reads "Three Months Ended March 31, 2026 … Revenues | Prior Period $34 | Current Period $(55) | Total $(21)".
   - Footnote a: "Reflects adjustments to provisionally priced copper sales at December 31, 2025".
   - Footnote b: "Reflects adjustments to provisionally priced copper sales for the three months ended March 31, 2026".
   - D03 line 70 confirms the $34M ("favorable adjustments to prior period … totaling $34 million … in first-quarter 2026").
2. D04 (FCX Q2 2026 release), "Derivative Instruments", page IX, text/D04.txt lines 839–849. Q2 2026 Revenues: Prior Period $98, Current Period $40, Total $138.
   - Footnote a: "Reflects adjustments to provisionally priced copper sales at March 31, 2026".
   - Footnote b: "…during the second quarters of 2026".
3. D04 lines 851–861. Six months 2026 Revenues: Prior Period $58, Current Period $59, Total $117.
   - Footnote a: "…at December 31, 2025".
   - Footnote b: "…for the first six months of 2026".
   - D04 line 70 repeats the $98M and $58M.
4. D04 line 833 and D03 line 735 both say final pricing comes "generally one to four months from the shipment date". So sales still open at March 31, 2026 can include shipments from late 2025, and $98M is not limited to Q1 2026 sales.

Calculation (let A = Q2 2026 revenue adjustment on copper sales made in Q1 2026):
- Route 1: six-month current column 59 = Q1 sales repriced in Q1 (−55) + A + Q2 sales repriced in Q2 (40). So A = 59 − 40 + 55 = 74.
- Route 2: sales open at Dec 31, 2025 were repriced by 58 over six months and 34 in Q1, so 24 in Q2. Then A = 98 − 24 = 74.
- Checks: −21 + 138 = 117. 34 + 24 = 58. −55 + 74 + 40 = 59. 24 + 74 = 98.
- The same method on 2025 also balances: 63 − 70 = −7, 87 − 69 − 46 = −28, and −7 + (−28) = −35, which equals the printed Q2 2025 prior-period figure.

The figures are copied from the files in docs/ and match them: D04 source lines 877–899 and D03 source lines 773–781.

minimal_documents: D03 + D04. D04 alone is not enough: its equations leave one unknown, and you need either Q1's $34M or Q1's $(55)M from D03. D04 repeats no Q1 2026 provisional-pricing figures (checked by search). D01 and D02 are BHP filings and cannot replace either document.

readings:
- **$98 million:** this is the Q2 2026 "prior period" adjustment, which covers sales open at March 31, 2026. It equals the answer only if you assume every sale open at March 31 was made in Q1. The six-month table shows $24M of it applies to sales already open at December 31, 2025, so it overstates sales "made in the first quarter".
- **$19 million (−55 + 74):** the combined effect over Q1 and Q2 on Q1 sales. It is not the Q2 revenue increase.
- **$138 million:** total Q2 adjustments, including Q2's own sales. Not what was asked.
- **Net income instead of revenue:** the same method gives $23M (20 − 15 + 18; check 35 − (24 − 12) = 23). The question asks about revenue, so this does not apply.
- **South America segment row, $98M:** D04 line 1258/1280, "Other revenue adjustments, primarily for pricing on prior period open sales", Q2 2026 (91 copper + 7 other). It matches $98 only by coincidence; it is one segment and includes non-copper metals.
- **Estimate from D03's sensitivity** (136 Mlbs open at $5.58/lb, $12M per $0.05): not appropriate, because actual results are reported.

gaps:
- The answer is derived from figures rounded to millions, so a ±$1M rounding effect is possible. Both independent routes give exactly 74.
- D01 and D02 (BHP) were only searched for Freeport/FCX/provisional/repric terms; the only hits were BHP's generic provisional-pricing footnotes.
- D03 and D04 were not read end to end. I read the derivative sections, the summary footnotes, the opening narrative and the segment adjustment rows, and searched for related terms.
- The packet has text sources only (manifest method "text", pages null) and no layout or PDF files, so there were no PDF pages to inspect. The extracted tables match the source files.

contaminated: no. The caller supplied only the workspace root, packet path and question. question.txt appeared in a directory listing but I did not open it, and I read no notes or other packets.
