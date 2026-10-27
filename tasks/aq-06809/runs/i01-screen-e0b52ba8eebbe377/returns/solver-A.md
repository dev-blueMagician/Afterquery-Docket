# i01 strong-solver screen, solver A (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 6.5).

answer: 6.5 percentage points (Huntington ≈ 7.8 pp operating leverage minus KeyCorp ≈ 1.3 pp)
confidence: high

path:
1. Huntington FTE revenue — D03 Table 3: "Total revenue - FTE (1) $ 2,857 $ 2,592 $ 2,191 $ 2,151 $ 1,954 10 % 46 %" → Q2 2026 = 2,857; Q2 2025 = 1,954 (confirmed D04 p.10: "Total revenue FTE (1)|$|2,857 ... $|1,954").
2. Huntington noninterest expense — D03 Table 8: "Total noninterest expense|$|1,809 ... $|1,197 2 % 51 %" (same in D04 p.1).
3. Huntington itemized M&A charges — D03 Table 9: "Acquisition-related expenses included in Notable Items|$|152 $|263 $|154 $|14 $|—|" (cols 2Q26, 1Q26, 4Q25, 3Q25, 2Q25) → Q2 2026 = 152; Q2 2025 = 0. Table 2 confirms Q2 2026 "Acquisition-related expenses $(152)"; Q2 2025 notable items are non-M&A: "Staffing efficiencies expense (5)... (6)" and "FDIC Deposit Insurance Fund (DIF) special assessment... $3" ("Notable Items in the second quarter of 2025 included $6 million of expense related to staffing efficiencies, as well as a $3 million benefit..."). Under "only," these stay in expense. Q2 2025 securities loss $(58) is a repositioning, not M&A → revenue stays as reported FTE. Verified Table 9 against original docs/hban_ex991_2026-07-23.txt (lines 334, 360–361) — matches.
4. Huntington: revenue growth = 903/1,954 = 46.2129%. Expense ex-M&A: 1,809 − 152 = 1,657 vs 1,197 − 0 = 1,197 → growth 460/1,197 = 38.4294%. Operating leverage = 46.2129 − 38.4294 = 7.7835 pp.
5. KeyCorp — D05: "Total revenue (TE)|$|1,964 $|1,953 $|1,840 0.6 %|6.7 %" (p.2; also p.13/p.16); "Total noninterest expense|$|1,217 $|1,181 $|1,154 3.0 %|5.5 %". Itemized charges: Selected Items table (p.24) "Three months ended June 30, 2026 / No items" and "Three months ended June 30, 2025 / No items" (the only "merger and acquisition" text, line 423, is KeyBanc's advisory services, not a charge). Cross-check: p.16 "Adjusted operating leverage (S - T)|1.28" with S = 6.74, T = 5.46; CEO "approximately 130 basis points of operating leverage."
6. KeyCorp: revenue growth 124/1,840 = 6.7391%; expense growth 63/1,154 = 5.4593%; operating leverage = 1.2799 pp.
7. Difference: 7.7835 − 1.2799 = 6.5036 → 6.5 (using KeyCorp's printed 1.28 gives 6.5035 → 6.5; well inside 6.45–6.55).

minimal_documents: D03 + D05. D04 can substitute for Huntington revenue/expense figures but not for the $152M pre-tax acquisition charge (D04 shows only "Notable Items, after tax|116 ... 3"). D01/D02 (Fifth Third) not needed — they cover Comerica merger charges, no Huntington/KeyCorp data.

readings:
- Excluding all Huntington notable items (Table 10 adjusted expense 1,657 vs 1,194): expense growth 463/1,194 = 38.7772% → Huntington leverage 7.4357 → answer 6.2. Rejected by "only the merger and acquisition charges."
- No exclusions (GAAP): Huntington expense growth 612/1,197 = 51.1278% → leverage −4.9149 → answer −6.2.
- Removing the Q2 2025 securities loss from Huntington revenue: also excluded by "only."

gaps: D03, D04, D05 read in full; D01 and D02 (Fifth Third) searched for merger/acquisition and Huntington/KeyCorp/peer terms, not read line by line. Text-method manifest (no PDF pages), so no PDF/layout inspection possible; no extraction problems found in decisive rows.

contaminated: no
