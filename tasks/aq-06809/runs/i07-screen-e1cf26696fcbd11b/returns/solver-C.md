# i07 strong-solver screen, solver C (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 9.0). Named 8.9 (shares rounded first) as "not allowed by the question".

answer: 9.0 percentage points (Fifth Third 27.6347% − KeyCorp 18.6791% = 8.9556 pp)
confidence: high

path:
1. Fifth Third — D01 (FITB Q2 2026 Exhibit 99.1), page-7 "Average Deposits" table (text/D01.txt l.324-341; docs/fitb_ex991_2026-07-17.txt l.375, 395), column order June 2026 / March 2026 / June 2025: "Demand|$63,976 $55,770 $40,885" and "Total average deposits $231,506 $209,352 $163,575".
2. Confirmed Demand = noninterest-bearing: D01 three-month average balance sheet (l.1088-1104; docs l.1289, 1297) lists "Demand deposits|63,976" below "Total interest-bearing liabilities|190,452" (i.e., outside the interest-bearing group), with "Total interest-bearing deposits|167,530"; check 167,530 + 63,976 = 231,506 = total. Corroborated by D02 slide 9 (text/D02.txt l.25): "Non Interest-Bearing $ ... $64.0" for 2Q26.
3. KeyCorp — D05 (KEY Q2 2026 Exhibit 99.1), average balance sheet three months ended 6/30/2026 (l.1065-1078; docs/key_ex991_2026-07-21.txt l.1247, 1256): "Total interest-bearing deposits|120,011 600 2.01" and "Noninterest-bearing deposits|27,566 26,934 27,473"; page-4 Average Deposits table (l.170; docs l.191): "Total deposits|$|147,577 $|147,299 $|147,446". Check: 120,011 + 27,566 = 147,577; also 42,843 + 61,013 + 4,406 + 27,566 = 135,828 = reported "Non-time deposits", + 11,749 time = 147,577. (KeyCorp's "Demand deposits 61,013 280 1.84" are interest-bearing — carry a 1.84% rate and sit within interest-bearing deposits — so excluded.)
4. Calculation (unrounded shares): Fifth Third 63,976 / 231,506 = 0.27634705 → 27.63470%; KeyCorp 27,566 / 147,577 = 0.18679063 → 18.67906%; difference 27.63470 − 18.67906 = 8.95564 pp → 9.0 (≈0.006 above the 8.95 rounding boundary; arithmetic double-checked).

minimal_documents: D01 + D05 (D02 can replace D01 using its rounded figures $64.0B / $231.5B = 27.6458% → 8.9667 → still 9.0, though D02's inputs are rounded to $0.1B; nothing else in the packet replaces D05; D03/D04 Huntington not needed).

readings:
- Rounding shares first (not allowed by the question): 27.6 − 18.7 = 8.9.
- Using D02's printed "Non Interest-Bearing %" of 28.0% for 2Q26 → 9.3; but that figure is on a core-deposit base (63,976 / 228,516 = 27.996% → 9.317), not total deposits. D02's pie "Demand, 28%" of "$232B Average Deposits" is a rounded share → also ~9.3. Neither fits "average total deposits, unrounded."
- Treating KeyCorp's interest-bearing "Demand deposits" (61,013) as noninterest-bearing is not defensible from the labels (would give a negative difference, ≈ −13.7).
- Period-end balances are not what was asked (KEY period-end 30,893 / 153,089 = 20.18%, D05 l.899-902; FITB period-end not computed).

gaps: None in extraction — sources are text-method (no PDFs/layout files in the packet); decisive rows verified against docs/ originals. Unread coverage: D01, D02, D05 read only in targeted sections located via searches for noninterest-bearing/demand/deposits terms; D03/D04 (Huntington) only seen via search hits.

contaminated: no
