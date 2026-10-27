# i05 strong-solver screen, solver A (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 9.0). Reading raised: rounding each share to one decimal first gives 8.9
(the gold is one rounding step from it; the sentence has no "do not round" instruction).

answer: 9.0 percentage points (Fifth Third ≈ 27.63% vs KeyCorp ≈ 18.68% noninterest-bearing share of Q2 2026 average total deposits)

confidence: high

path:
1. Fifth Third (D01, Q2 2026 earnings release, "Average Deposits" table ~lines 320-341, three-month columns June 2026 / March 2026 / June 2025): "Demand|$63,976 $55,770 $40,885" and "Total average deposits $231,506 $209,352 $163,575".
2. Confirmed demand deposits are the noninterest-bearing balance: D01's three-month average balance sheet (~lines 1089-1104) lists "Total interest-bearing deposits|167,530" and, separately after "Total interest-bearing liabilities", "Demand deposits|63,976"; 167,530 + 63,976 = 231,506. D02 (slide deck, slide 9) also labels the $64.0B series "Non Interest-Bearing $".
3. KeyCorp (D05, Q2 2026 earnings release): average balance sheet p.19 (header "Second Quarter 2026 First Quarter 2026 Second Quarter 2025", line 1019): "Total interest-bearing deposits|120,011" (line 1071) and "Noninterest-bearing deposits|27,566 26,934 27,473" (line 1078); Average Deposits table (line 170): "Total deposits|$|147,577 $|147,299 $|147,446". Check: 120,011 + 27,566 = 147,577. (KeyCorp's "Demand deposits" line items, 61,013, are inside interest-bearing deposits, so not counted.)
4. Fifth Third share = 63,976 / 231,506 = 0.276347 → 27.6347%; KeyCorp share = 27,566 / 147,577 = 0.186791 → 18.6791%; difference = 27.6347 − 18.6791 = 8.9556 pp → 9.0 (both divisions checked by reciprocal verification).

minimal_documents: D01 + D05. (D02 can substitute for D01 using its rounded figures: average total deposits "$231.5" and non-interest-bearing "$64.0" ($B, 2Q26) → 64.0/231.5 = 27.646% → 27.646 − 18.679 = 8.97 → still 9.0. D05 is the only KeyCorp document in the packet, so no substitute. D03/D04 are Huntington and not needed.)

readings (alternatives a solver could slip into, all different quantities from the one asked):
- Core deposits instead of total: D02's "Core deposit trends (average)" chart shows "Non Interest-Bearing %" 28.0% for 2Q26 (= 64.0/228.5, share of core deposits, not total) → 28.0 − 18.68 = 9.3. The deposit-mix pie ("Demand, 28% … $232B Average Deposits") is whole-number rounding and would also give ≈9.3.
- Rounding each share first (27.6 − 18.7) → 8.9; unrounded inputs give 9.0.
- Period-end balances: Fifth Third 63,928/234,141 = 27.30%; KeyCorp 30,893/153,089 = 20.18% (D05 lines 899-902) → 7.1 (question asks average).
- Six-month averages: Fifth Third 59,896/(160,594+59,896) = 27.17%; KeyCorp 27,251/(120,187+27,251) = 18.48% → 8.7 (not Q2 alone).
- KeyCorp segment figure (Consumer Bank noninterest-bearing 14,082 of 87,399 = 16.1%) — wrong scope.

gaps: Sources are already text files (manifest method "text", no PDF pages/layout files), so no original-page check was possible; tables used reconcile by addition. Coverage: D01 read lines 300-359 and 1036-1199 (rest searched only); D02 read lines 23-26 and 73 (rest searched); D05 read lines 60-99, 150-199, 1012-1189 (rest searched for deposit/noninterest-bearing terms); D03/D04 only search hits, not read. KeyCorp's release provides no noninterest-bearing percentage of its own, so its share had to be computed.

contaminated: no (did not open question.txt or any notes; worked only from the provided question and the packet's text/ files)
