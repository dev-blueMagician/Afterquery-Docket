# i01 strong-solver screen, solver B (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 6.5).

answer: 6.5 percentage points (Huntington ≈ 7.78 pp operating leverage minus KeyCorp ≈ 1.28 pp)

confidence: high

path:
1. Huntington FTE revenue — D03 Table 3: "Total revenue - FTE (1) $ 2,857 $ 2,592 $ 2,191 $ 2,151 $ 1,954" (cols Q2'26, Q1'26, Q4'25, Q3'25, Q2'25). Same in D04 p.10 "Total revenue FTE (1)|$|2,857 … $|1,954".
2. Huntington noninterest expense — D03 Table 8: "Total noninterest expense|$|1,809 $|1,774 $|1,420 $|1,246 $|1,197" (same D04 p.1/p.10).
3. Huntington M&A charges — D03 Table 9: "Acquisition-related expenses included in Notable Items|$|152 $|263 $|154 $|14 $|—|" → Q2'26 = 152, Q2'25 = 0. Table 2 confirms Q2'26 only "Acquisition-related expenses $(152)"; Q2'25 items were "FDIC Deposit Insurance Fund (DIF) special assessment $3" and "Staffing efficiencies expense (6)" — not M&A, so under "only" they stay in expense (Q2'25 base = 1,197, not Table 10's adjusted 1,194).
4. KeyCorp — D05 p.16: "Total taxable-equivalent revenue (non-GAAP) (A+K) = (Q)|$|1,964 $|1,953 $|1,840" (Q2'26, Q1'26, Q2'25); "Noninterest expense (GAAP) (M)|$|1,217 $|1,181 $|1,154". TE uses "statutory federal income tax rate of 21%" (D05 p.19) — same basis as Huntington's FTE.
5. KeyCorp itemized M&A charges — D05 p.24 "Selected Items Impact on Earnings": "Three months ended June 30, 2026 … No items"; "Three months ended June 30, 2025 … No items" (only items anywhere are FDIC special assessments in Q3'25/Q4'25). So KeyCorp exclusion = 0. (The only "merger" text in D05, line 423, is KeyBanc's "merger and acquisition advice" service — not a charge.)
6. Huntington: revenue growth = 2,857/1,954 − 1 = 46.2129%; expense growth ex-M&A = (1,809−152)/(1,197−0) − 1 = 1,657/1,197 − 1 = 38.4294%; operating leverage = 7.7835 pp.
7. KeyCorp: revenue growth = 1,964/1,840 − 1 = 6.7391%; expense growth = 1,217/1,154 − 1 = 5.4593%; operating leverage = 1.2799 pp — matches D05's own "Adjusted operating leverage (S - T)|1.28" and CEO's "approximately 130 basis points of operating leverage."
8. 7.7835 − 1.2799 = 6.5036 → 6.5 (using KeyCorp's printed 1.28: 6.5035 → 6.5). Decisive rows cross-checked against raw docs/hban_ex991 and docs/key_ex991 — identical.

minimal_documents: D03 + D05. (D04 duplicates D03's revenue/expense totals but cannot replace D03 for the $152M pre-tax acquisition-related figure — D04 only shows after-tax total Notable Items 116 / 3. D01/D02 are Fifth Third documents, not needed.)

readings:
- Excluding all Huntington Notable Items (Table 10 adjusted expense 1,657 vs 1,194): expense growth 38.7772% → HBAN OL 7.4357 → answer 6.2 (contradicts "only the merger and acquisition charges").
- No exclusions (GAAP): HBAN expense growth 51.1278% → OL −4.9149 → answer −6.2.
- Also removing Huntington's $58M Q2'25 securities loss from revenue (D04 efficiency table 2,855 vs 2,012) → ≈2.2; ruled out by "only" (not an M&A charge).
- Rounding growth rates to 1 decimal first (46.2−38.4=7.8; 6.7−5.5=1.2) → 6.6; unrounded/2-decimal intermediates give 6.5.

gaps: Read D03, D04, D05 in full. D01/D02 (Fifth Third) not read in full — only searched for Huntington/KeyCorp/"operating leverage"/merger terms; they mention neither bank ("Key" hits are "Key statistics"/"Key Messages"; their "Merger-related charges" rows, e.g., $203M, are Fifth Third's own). All documents are text extractions (no PDF pages/layout files); raw-file rows match extraction. No missing facts.

contaminated: no (did not open the packet-root question.txt; used only the question as given)
