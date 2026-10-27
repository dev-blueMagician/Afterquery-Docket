# i05 strong-solver screen, solver C (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 9.0). Readings raised: 9.3 (core basis / pie), 8.9 (rounding shares first),
7.1 (period-end); noted D02 alone bounds the gap at 8.94-8.99 from its rounded billions.

answer: 9.0 percentage points (Fifth Third ≈27.63% vs KeyCorp ≈18.68% noninterest-bearing share; gap 8.956 → 9.0)
confidence: high

path:
1. Fifth Third — Q2 2026 average demand (noninterest-bearing) deposits $63,976M: D01 "Average Deposits" table, line 326: "Demand|$63,976 $55,770 $40,885"; D01 average balance sheet, line 1104: "Demand deposits|63,976" (listed after "Total interest-bearing liabilities", no rate → outside the interest-bearing group). D02 slide 9 (line 25) labels the same series "Non Interest-Bearing $ … $64.0".
2. Fifth Third — Q2 2026 total average deposits $231,506M: D01 line 341 "Total average deposits $231,506 $209,352 $163,575"; also D01 line 64 "Average deposits|231,506". Check: total interest-bearing deposits 167,530 (line 1096) + 63,976 = 231,506.
3. KeyCorp — Q2 2026 average noninterest-bearing deposits $27,566M: D05 average balance sheet, line 1078: "Noninterest-bearing deposits|27,566 26,934 27,473" (column header line 1019: "Second Quarter 2026 First Quarter 2026 Second Quarter 2025").
4. KeyCorp — Q2 2026 total average deposits $147,577M: D05 line 170 "Total deposits|$|147,577"; line 174 "Average deposits totaled $147.6 billion for the second quarter of 2026". Check: total interest-bearing deposits 120,011 (line 1071) + 27,566 = 147,577.
5. Calculation: Fifth Third 63,976 / 231,506 = 0.276347 → 27.6347%; KeyCorp 27,566 / 147,577 = 0.186791 → 18.6791%; difference = 8.9556 pp → 9.0 (verified both divisions by long multiplication).

Classification notes: KeyCorp's "Demand deposits" row (61,013, line 1066) is interest-bearing (1.84% rate, included in total interest-bearing deposits) — not noninterest-bearing. D02 slide 9 prints a Fifth Third "Non Interest-Bearing %" of 28.0% for 2Q26 — that is noninterest-bearing ÷ average core deposits (63,976 / 228,516 = 27.996%; core defined in D01 line 604/footnote (c) as excluding CDs over $250,000; the same series' 25.3% for 2Q25 matches 40,885/161,375). The question says "average total deposits," so the 231,506 denominator is used. The D02 pie ("Demand, 28% … $232B Average Deposits") is the total-deposit share rounded to a whole percent.

minimal_documents: D01 + D05. (Partial substitute for D01: D02's rounded figures, $64.0B / $231.5B = 27.65% → 8.97 pp, also 9.0 — but rounding uncertainty allows ≈8.94–8.99, so D02 alone doesn't settle the one-decimal answer as cleanly. No substitute for D05 (KeyCorp figures appear nowhere else). D03/D04 (Huntington) not needed and don't mention Fifth Third/KeyCorp.)

readings:
- Using Fifth Third's printed 28.0% "Non Interest-Bearing %" (core-deposit basis): 28.0 − 18.68 = 9.32 → 9.3 — doesn't match "total deposits" wording.
- Using the 28% pie chart: ≈9.3 — same issue.
- Rounding each share to one decimal before subtracting: 27.6 − 18.7 = 8.9 — the unrounded difference (8.956) makes 9.0 the correct one-decimal result.
- Period-end instead of average balances: Fifth Third 63,928/234,141 = 27.30% (D01 lines 908, 914); KeyCorp 30,893/153,089 = 20.18% (D05 lines 901–902) → 7.1 — not the question's average basis.
- Six-month YTD averages — not the question's period.

gaps: No missing facts. Manifest lists all five sources as "text" with no PDF pages or layout files, so no original pages to inspect; slide chart extraction (D02) was coherent and consistent with D01. D03/D04 not read beyond keyword searches; D01, D02, D05 not read in full — covered via keyword searches plus reading the deposit, highlights, and average-balance-sheet sections.

contaminated: no
