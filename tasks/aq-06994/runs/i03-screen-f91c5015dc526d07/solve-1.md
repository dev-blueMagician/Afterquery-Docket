# i03 screen, solve 1 (blind-solver, fresh context; raw return as handed back, 2026-10-19)

answer: -3,704 (thousands of dollars). Adjusted EBITDA fell from $13,310 thousand in the quarter ended July 31, 2025 to $9,606 thousand in the quarter ended October 31, 2025.

confidence: high

path:
Comtech's fiscal year ends July 31. The quarter ended July 31, 2025 is Q4 FY2025 and the quarter ended October 31, 2025 is Q1 FY2026. The documents give the Q4 FY2025 consolidated figure only rounded to $13.3 million, so the exact figure has to be derived.

1. Q1 FY2026: D01 (Q1 FY2026 earnings release), line 308, in the "Reconciliation of GAAP Operating loss to Adjusted EBITDA" table, column "Three months ended October 31, 2025". It reads: "|Adjusted EBITDA|$9,606,000|$(30,766,000)|$(1,977,000)|". The columns are Q1 FY2026, Q1 FY2025 and Fiscal Year 2025.
   - Footing check: -2,757 + 1,127 + 5,044 + 3,000 + 2,441 + 751 = 9,606.
2. FY2025: $(1,977,000). This appears in D01 line 308, D03 line 327 and D04 line 323.
   - Footing check: -139,098 + 3,120 + 21,723 + 79,555 + 11,798 + 261 + 15,585 + 280 + 2,682 + 2,117 = -1,977.
3. Nine months ended April 30, 2025: D04 (Q3 FY2026 release), line 323. The column headers are Q3'26, Q3'25, 9M'26, 9M'25 and FY2025. The row reads: "|Adjusted EBITDA|$8,247,000|$12,576,000|$26,984,000|$(15,287,000)|$(1,977,000)|".
   - Footing check: -140,959 + 2,520 + 16,680 + 79,555 + 261 + 8,400 + 14,222 + 1,072 + 2,682 + 280 = -15,287.
   - Cross-check by quarter: Q1'25 -30,766 (D01) + Q2'25 2,903 (D03 line 327) + Q3'25 12,576 (D04) = -15,287. This also matches the D03 six-month figure of -27,863 plus 12,576.
4. Q4 FY2025 = -1,977 - (-15,287) = 13,310.
   - Built up line by line: operating income 1,861, SBC 600, amortization of intangibles 5,043, depreciation 3,398, restructuring 1,363, CEO transition 1,045. These sum to 13,310.
   - This agrees with D01 line 54 ("Adjusted EBITDA of $13.3 million in the immediately preceding quarter") and D02 line 1596 ("$13.3 million for the fourth quarter of fiscal 2025"). It also agrees with D01 line 47 ("$1.9 million of operating income in the immediately preceding quarter").
5. Change = 9,606 - 13,310 = -3,704 thousand (about -27.8%).

The FY2025 reconciling items and total are the same in D01, D03 and D04. The definition is in D02 line 1883. I found no restatement or change of definition.

minimal_documents:
- Main set: D01 + D04. D01 gives Q1 FY2026 exactly; D04 gives the FY2025 and nine-month FY2025 figures.
- Alternative: D03 + D04. In this case Q1 FY2026 = D03's six-month FY2026 figure of 18,737 minus Q2 FY2026 of 9,131 = 9,606.
- D04 is needed in every exact solution. It is the only document with Q3 or nine-month FY2025 Adjusted EBITDA.
- D02 alone, or D01 alone, gives only the rounded $13.3M.
- I did not check whether the exact GAAP statements in D02 could replace D01.

readings:
- Using only the rounded figures (D01 or D02 alone): 9.6 - 13.3 = -3.7 million, which is -3,700 thousand. This is inferior at the requested precision.
- Mixing exact and rounded figures: 9,606 - 13,300 = -3,694. Not defensible.
- Segment-level figures (S&S: 6.3 to 6.0; Allerium: 13.7 to 11.3) don't fit "Comtech's Adjusted EBITDA", which means the consolidated figure.

gaps:
- No document states the exact Q4 FY2025 figure or the change directly. I searched for "13,310", "3,704" and "13.31" and found nothing.
- The sources are .txt files (manifest method "text", pages null), so there was no PDF to inspect. The tables foot exactly.
- What I read:
  - D01: all of it.
  - D03: lines 305–384 plus grep hits.
  - D04: lines 1–130 and 300–379.
  - D02: grep hits plus lines 1804–1893.
  - D05–D07 (Iridium): not read. A grep found no Comtech or CMTL mention in them.
- Not read: the rest of the D02 10-Q, the D03 narrative and D04 lines 131–299 (financial statements).

contaminated: no

Judgement (caller): right (gold -3,704).
