# i07 strong-solver screen, solver B (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 9.0). Named 8.9 (shares rounded first) as ruled out by the question.

answer: 9.0 percentage points (Fifth Third ≈27.6347% − KeyCorp ≈18.6791% = 8.9556 pp)
confidence: high

path:
1. Fifth Third 2Q26 average total deposits — D01 (FITB EX-99.1, 2Q26 release), Average Deposits table (text/D01.txt lines 324-341): "Demand|$63,976 $55,770 $40,885" and "Total average deposits $231,506 $209,352 $163,575" (columns June 2026 / March 2026 / June 2025, three months). Also Key Financial Data box (line 64): "Average deposits|231,506 209,352 163,575".
2. Fifth Third's noninterest-bearing deposits are labeled "Demand": D01 average balance sheet (lines 1048-1104, "For the Three Months Ended June 2026") lists "Total interest-bearing deposits|167,530" (interest checking 70,507 + savings 18,430 + money market 63,200 + CDs ≤$250K 12,403 + CDs >$250K 2,990), then "Demand deposits|63,976" placed below "Total interest-bearing liabilities" (outside the interest-bearing group); 167,530 + 63,976 = 231,506. D02 (presentation slide 9, line 25) states it directly: "$40.9 $41.2 $41.8 $55.8 $64.0 ... Interest-Bearing $ Non Interest-Bearing $".
3. KeyCorp — D05 (KEY EX-99.1) Consolidated Average Balance Sheet, "Second Quarter 2026" column (lines 1019-1078): "Total interest-bearing deposits|120,011" and "Noninterest-bearing deposits|27,566 26,934 27,473"; KeyCorp's "Demand deposits" (61,013, 1.84% rate) are interest-bearing, so excluded. Average Deposits table (line 170): "Total deposits|$|147,577 $|147,299 $|147,446" (= 120,011 + 27,566); narrative line 174 "Average deposits totaled $147.6 billion".
4. Calculation: Fifth Third 63,976 / 231,506 = 0.2763470 → 27.63470% (check 231,506 × 0.276347 = 63,975.99); KeyCorp 27,566 / 147,577 = 0.1867906 → 18.67906% (check 147,577 × 0.18679 = 27,565.91); difference 27.63470 − 18.67906 = 8.95564 pp → 9.0 (only 0.0056 pp above the 8.95 rounding point).
5. Key rows cross-checked in docs/ source files (fitb_ex991 lines 375, 395, 1289, 1297; key_ex991 lines 191, 1247, 1256).

minimal_documents: D01 + D05. (Alternative: D02 + D05 — D02 slide 9 gives Fifth Third only in rounded billions, $64.0B noninterest-bearing / $231.5B total → 27.6458% − 18.6791% = 8.967 → still 9.0, but less precise inputs. D03/D04 (Huntington) not needed — searched, no Fifth Third/KeyCorp data.)

readings:
- Rounding each share first (27.6% − 18.7%) → 8.9; ruled out by the question.
- Using Fifth Third's reported "Non Interest-Bearing %" of 28.0% (D02 slide 9) — that is a share of core deposits ($228.5B), not total deposits; using it (or 63,976/228,516 = 27.9963%) gives 9.3172 → 9.3. Doesn't match "average total deposits."
- Period-end instead of average: Fifth Third 63,928/234,141 = 27.303% (D01 line 908); KeyCorp 30,893/153,089 = 20.180% (D05 line 901) → ≈7.1. Question asks for averages.
- Six-month YTD averages: Fifth Third 59,896/220,490 = 27.165%; KeyCorp 27,251/147,438 = 18.483% → ≈8.7. Question asks for 2Q only.
- Counting KeyCorp's "Demand deposits" (61,013) as noninterest-bearing would be wrong (KeyCorp reports a separate noninterest-bearing line; demand deposits there pay interest).
- KeyCorp Consumer Bank segment only (14,082/87,399 = 16.11%, D05 line 328) — not consolidated.

gaps: No extraction difficulty — all text sources; decisive rows match docs/ originals. Not read in full: D01 and D05 (read deposit, highlight, average balance sheet and period-end balance sheet sections plus full-document searches for deposit terms); D02 (read lines 1-49, rest searched); D03/D04 (searched only).

contaminated: no
