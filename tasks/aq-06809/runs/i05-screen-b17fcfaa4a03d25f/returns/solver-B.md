# i05 strong-solver screen, solver B (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 9.0). Raised the rounding edge: 8.9556 is about 0.006 above 8.95, and
rounding each share first gives 8.9 (wording defect: the sentence does not say not to round the shares first).

answer: 9.0 percentage points (Fifth Third's noninterest-bearing share of average total deposits ≈ 27.63% vs KeyCorp's ≈ 18.68%; difference 8.9556 → 9.0)
confidence: high (note: result 8.9556 sits ~0.006 above the 8.95 rounding boundary; rounding each share before subtracting would give 8.9 — see readings)

path:
1. Fifth Third noninterest-bearing deposits = its demand deposits. D01 (fitb_ex991) average balance sheet, three months ended June 2026: "Total interest-bearing deposits|167,530" (line 1096) comprises interest checking, savings, money market, CDs; "Demand deposits|63,976 55,770 40,885" is listed after "Total interest-bearing liabilities" (line 1104). D02 slide 9 confirms the label: "Non Interest-Bearing $" series "$40.9 $41.2 $41.8 $55.8 $64.0" matches demand amounts.
2. Fifth Third Q2 2026 averages — D01 Average Deposits table: "|Demand|$63,976 $55,770 $40,885" (line 326) and "Total average deposits $231,506 $209,352 $163,575" (line 341; also highlights "Average deposits|231,506", line 64). Cross-check: 167,530 + 63,976 = 231,506.
3. KeyCorp Q2 2026 averages — D05 (key_ex991) average balance sheet: "Noninterest-bearing deposits|27,566 26,934 27,473" (line 1078); "Total interest-bearing deposits|120,011" (line 1071); Average Deposits table "Total deposits|$|147,577 $|147,299 $|147,446" (line 170). Cross-check: 120,011 + 27,566 = 147,577. (KeyCorp's "Demand deposits 61,013 … 1.84" at line 1066 are interest-bearing — rate 1.84% — so excluded.)
4. Calculations: Fifth Third 63,976 / 231,506 = 0.276347 → 27.6347%; KeyCorp 27,566 / 147,577 = 0.186791 → 18.6791%; difference 27.6347 − 18.6791 = 8.9556 pp → 9.0 (verified both divisions by multiplying back).

minimal_documents: D01 + D05. (KeyCorp: D05 is the only KeyCorp source. Fifth Third: D02 is not a full substitute — its rounded figures ($64.0B of $231.5B average deposits) give 27.646% and a 8.97 difference (→9.0), but the rounding range of those figures spans differences of about 8.94–8.99, straddling 8.95, so D01's exact millions are needed. D03/D04 are Huntington — no Fifth Third/KeyCorp data — not needed.)

readings:
- Rounding each share to one decimal first: 27.6 − 18.7 = 8.9 (not the right method — keep shares unrounded and round only the result → 9.0).
- D02 slide 9 prints a ready-made "Non Interest-Bearing %" of 28.0% for 2Q26, but it is a share of core deposits ($64.0B/$228.5B; D01: 63,976/228,516 = 27.996%), not total deposits → would give 28.0 − 18.68 = 9.3. The same slide's pie ("Demand, 28% … $232B Average Deposits") is rounded to whole percent and would also give ≈9.3. Neither matches "average total deposits."
- Period-end balances instead of averages: Fifth Third 63,928 / 234,141 = 27.30% (D01 lines 908, 914), KeyCorp 30,893 / 153,089 = 20.18% (D05 lines 901–902) → 7.1 — not applicable (question says average).
- Six-month (YTD) averages: Fifth Third 59,896 / 220,490 = 27.17%, KeyCorp 27,251 / 147,438 = 18.48% → 8.7 — not applicable (Q2).

gaps: No PDFs in packet (manifest method "text", no pages) — no page-image check possible; D02 slide 9 was extracted as a flat text run, but its series labels/values reconcile to D01. Coverage: D01 read lines 1–100, 300–380, 585–634, 900–920, 1040–1220; D02 lines 1–72; D05 lines 1–200, 300–349, 880–909, 1020–1189; D03/D04 checked by search only; all five files searched for noninterest-bearing/demand/deposit terms; remainder of each file not read line by line.

contaminated: no
