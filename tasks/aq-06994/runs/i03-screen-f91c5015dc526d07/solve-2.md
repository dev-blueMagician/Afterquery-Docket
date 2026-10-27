# i03 screen, solve 2 (blind-solver, fresh context; raw return as handed back, 2026-10-19)

I ran this solve fresh and the answer is fully supported. No filing states a thousands-level figure for Q4 FY2025, so I derived it from fiscal-year and year-to-date totals, and two separate cross-checks agree.

answer: -3,704 (thousands of dollars; Adjusted EBITDA fell from $13,310K to $9,606K)

confidence: high

path:
1. **Periods.** Comtech's fiscal year ends July 31. The quarter ended October 31, 2025 is Q1 FY2026, and the quarter ended July 31, 2025 is Q4 FY2025. D01 line 9: "first quarter ended October 31, 2025". The D01 balance sheet compares "October 31, 2025" with "July 31, 2025" (fiscal year-end).
2. **Q1 FY2026 = $9,606,000.** D01 lines 294–308, column "Three months ended October 31, 2025": "|Adjusted EBITDA|$9,606,000|$(30,766,000)|$(1,977,000)|". The reconciliation adds up: -2,757 + 1,127 + 5,044 + 3,000 + 2,441 + 751 = 9,606.
   - Cross-check: D03 line 327 gives six months ended January 31, 2026 = $18,737,000 and Q2 FY2026 = $9,131,000. 18,737 - 9,131 = 9,606.
3. **Q4 FY2025 is only printed rounded.** D01 line 54: "Adjusted EBITDA of $13.3 million in the immediately preceding quarter". D02 (10-Q) line 1596: "$13.3 million for the fourth quarter of fiscal 2025". There is no thousands-level figure in any document.
4. **Q4 FY2025 derived = $13,310,000.** D04 lines 309–323 have columns for nine months ended April 30, 2025 and Fiscal Year 2025: "|Adjusted EBITDA|$8,247,000|$12,576,000|$26,984,000|$(15,287,000)|$(1,977,000)|". Q4 = FY2025 minus nine months = -1,977 - (-15,287) = 13,310. This matches the printed $13.3 million.
   - The FY2025 total of $(1,977,000) is the same in D01 (line 308), D03 (line 327) and D04 (line 323).
   - The nine-month total ties to the quarters: Q1 FY2025 -30,766 (D01) + Q2 FY2025 2,903 (D03 line 327) + Q3 FY2025 12,576 (D04) = -15,287.
   - Line-by-line check (FY2025 minus nine months, D04 lines 313–322):
     - Operating income: -139,098 - (-140,959) = 1,861. D01 line 47 says "$1.9 million of operating income in the immediately preceding quarter".
     - Stock-based compensation: 3,120 - 2,520 = 600.
     - Amortization of intangibles: 21,723 - 16,680 = 5,043.
     - Depreciation: 11,798 - 8,400 = 3,398.
     - Restructuring: 15,585 - 14,222 = 1,363.
     - CEO transition: 2,117 - 1,072 = 1,045.
     - Impairment, cost to fulfill, proxy and strategic emerging technology: all 0.
     - Sum: 1,861 + 600 + 5,043 + 3,398 + 1,363 + 1,045 = 13,310.
5. **Change.** 9,606 - 13,310 = **-3,704** thousand (a decrease of about 27.8%).

minimal_documents:
- **{D01, D04}:** Q1 FY2026 comes from D01. Q4 FY2025 comes from FY2025 minus nine months in D04.
- **Alternative {D03, D04}:** Q1 FY2026 = D03's six-month total minus its Q2 figure. Q4 FY2025 comes from D04.
- **Not sufficient alone:**
  - D04 alone can't split the six-month FY2026 total ($18,737K) into Q1 and Q2.
  - D01, D02 and D03 without D04 only give Q4 FY2025 as the rounded $13.3 million, because Q3 FY2025 ($12,576K) appears only in D04.
  - D05–D07 (Iridium) are irrelevant: searching them for "Comtech" or "CMTL" found nothing.

readings:
- **Rounded figures from the text (D01 line 54 / D02 line 1596):** $9.6M - $13.3M = -$3.7M, written -3,700. Mixing the exact Q1 figure with the rounded Q4 gives 9,606 - 13,300 = -3,694. Both are approximations; the exact derivable answer is -3,704.
- **Segment-level (not what "Comtech's Adjusted EBITDA" means):**
  - S&S: $6.0M vs $6.3M, a change of -0.3M (D01 line 72).
  - Allerium: $11.3M vs $13.7M, a change of -2.4M (D01 line 104).
- No restatement was found. FY2025 and Q1 FY2026 figures are consistent across D01, D03 and D04.

gaps:
- No document states Q4 FY2025 Adjusted EBITDA in thousands; it has to be derived (FY minus nine months).
- **Read fully:** D01.
- **Read in part:**
  - D03: lines 300–339 plus search hits.
  - D04: lines 295–334 plus search hits.
  - D02: lines 1588–1601 and 1804–1893 plus search hits; the rest of this 244K-character 10-Q was not read.
- **Searched only, not read:** D05–D07.
- The sources are text extractions (method "text", no pages or layout files), so there was no PDF to inspect. The tables parsed cleanly.
- Packet: D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-06994\runs\i03-screen-f91c5015dc526d07\solver-1\text\ (D01.txt, D03.txt, D04.txt, D02.txt).

contaminated: no

Judgement (caller): right (gold -3,704).
