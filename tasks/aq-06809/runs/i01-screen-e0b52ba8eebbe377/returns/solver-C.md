# i01 strong-solver screen, solver C (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 6.5).

answer: 6.5 percentage points (Huntington ≈ 7.78 pp minus KeyCorp ≈ 1.28 pp; unrounded 6.504)

confidence: high

path:
1. Huntington FTE revenue — D03 Table 3: "Total revenue - FTE (1) $ 2,857 $ 2,592 $ 2,191 $ 2,151 $ 1,954" (columns 2Q26 … 2Q25) → 2Q26 = 2,857; 2Q25 = 1,954. Confirmed D04 p.10: "Total revenue FTE (1)|$|2,857 … $|1,954|". Growth = 903/1954 = 46.2129%.
2. Huntington noninterest expense — D03 Table 8: "Total noninterest expense|$|1,809 $|1,774 $|1,420 $|1,246 $|1,197" (also D04 L188, L704).
3. Huntington itemized M&A charges — D03 Table 2, 2Q26: "Acquisition-related expenses|$|(152) (116) (0.06)" (the only 2Q26 Notable Item); D03 Table 9: "Acquisition-related expenses included in Notable Items|$|152 $|263 $|154 $|14 $|—|" → 2Q26 = 152, 2Q25 = 0. The 2Q25 Notable Items are an FDIC DIF special assessment benefit ($3) and "Staffing efficiencies expense" ($(6)) — not M&A, so not excluded. Adjusted expense: 2Q26 = 1,809 − 152 = 1,657; 2Q25 = 1,197. Growth = 460/1197 = 38.4294%. Huntington OL = 46.2129 − 38.4294 = 7.7835 pp.
4. KeyCorp TE revenue/expense — D05 Financial Highlights: "Total revenue (TE)|1,964 1,953 1,840" and "Noninterest expense|1,217 1,181 1,154" (same in income statement and GAAP/non-GAAP table).
5. KeyCorp itemized charges — D05 p.24 Selected Items Impact on Earnings: "Three months ended June 30, 2026 … No items"; "Three months ended June 30, 2025 … No items"; reconciliation "Plus: Selected items (d) (O)|— — — — —". So nothing excluded. (Only other "merger" hit in D05, L423, is "merger and acquisition advice" — a product, not a charge.)
6. KeyCorp OL = 124/1840 (6.7391%) − 63/1154 (5.4593%) = 1.2799 pp; matches D05's printed "Adjusted operating leverage (S - T)|1.28" (6.74 − 5.46) and the CEO's "approximately 130 basis points of operating leverage."
7. Result: 7.7835 − 1.2799 = 6.5036 → 6.5 pp. Arithmetic re-verified by multiplying back each division.

minimal_documents: D03, D05. (D04 duplicates D03's revenue/expense totals but does not itemize acquisition-related expenses — searched; only allowance-at-acquisition credit lines — so D03 is irreplaceable; D05 is the only KeyCorp source. D01/D02 are Fifth Third and do not mention Huntington or KeyCorp.)

readings:
- Using all Huntington Notable Items (Table 10 adjusted expense 1,657 vs 1,194): expense growth 463/1194 = 38.7772%, Huntington OL 7.4357 → answer 6.2. Contradicts "only the merger and acquisition charges" (2Q25's $3 net is staffing/FDIC).
- GAAP with no exclusions: Huntington expense growth 612/1197 = 51.1278%, OL −4.9149 → answer −6.2.
- Also stripping Huntington securities gains/losses from revenue (efficiency-ratio basis, 2,855 vs 2,012): answer ≈ 2.2 — not called for by the question.
- One-decimal intermediate rounding (46.2−38.4 = 7.8; 6.7−5.5 = 1.2) could give 6.6; unrounded result 6.504 → 6.5.

gaps: No PDF pages (all manifest entries text-method; no layout files to verify). Read D03 and D05 in full; D04 front matter, key statistics (L160–279), p.10 income statement data (L680–749) and ROTCE/efficiency reconciliation (L1090–1134), plus targeted searches (merger/acquisition/notable/revenue/expense). D01/D02 not read beyond searches for Huntington/KeyCorp/HBAN/Key. Decisive Table 9 row confirmed in original docs file (hban_ex991, L361).

contaminated: no
