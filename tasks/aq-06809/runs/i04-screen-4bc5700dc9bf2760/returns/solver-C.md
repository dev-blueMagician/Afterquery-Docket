# i04 strong-solver screen, solver C (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold Fifth Third, KeyCorp, Huntington). Reading raised: dollar interest expense
(K, F, H), called weaker by the solver.

answer: Fifth Third (1.54%) < KeyCorp (1.63%) < Huntington (1.88%)
confidence: high

path:
1. Quantity: each bank's total cost of deposits for 2Q26 (quarter ended June 30, 2026) — interest paid on deposits divided by all average deposits (incl. noninterest-bearing), not the interest-bearing-only rate. Rank lowest → highest.
2. Fifth Third — D02 (2Q26 earnings presentation, slide 9; text line 25): "1.80% 1.81% 1.71% 1.58% 1.54% Fed Funds Rate Total Cost of Deposits 2Q25 3Q25 4Q25 1Q26 2Q26" → 2Q26 total cost of deposits = 1.54% (same slide gives "Total interest-bearing deposit costs" 2.13% for 2Q26, a different measure). Cross-check from D01 (earnings release): "Interest on deposits|891" (line 761) and "Total average deposits $231,506" (line 341) → 891 × 365/91 ÷ 231,506 = 1.544%. Also "Total interest-bearing deposits|167,530|2.13%" (line 1096) → 167,530 × 2.13% ÷ 231,506 = 1.541%. (Same method on 1Q26: 813 × 365/90 ÷ 209,352 = 1.575% ≈ chart's 1.58%, confirming the chart reading.)
3. KeyCorp — D05 (earnings release p.4; line 172): "Cost of total deposits 1.63 % 1.65 % 1.99 %" (2Q26, 1Q26, 2Q25) → 1.63%; line 176: "the overall cost of deposits declined by 2 basis points to 1.63%." Cross-check from average balance sheet (line 1071/1078): interest-bearing deposits 120,011 with interest 600 (2.01%) + noninterest-bearing 27,566 = 147,577 total → 600 × 365/91 ÷ 147,577 = 1.631%.
4. Huntington — D04 (quarterly financial supplement p.9; line 655): "Total cost of deposits (4) 1.88 % 1.82 % 1.88 % 2.00 % 2.02 %" with column order (line 592) "June 30, March 31, December 31, September 30, June 30, 2026 2026 2025 2025 2025" → 2Q26 = 1.88%; footnote (4): "Includes noninterest-bearing and interest-bearing deposit balances." Cross-check: interest on interest-bearing deposits 1,048 (line 576) ÷ average total deposits 223,403 (line 450) × 365/91 = 1.882%. Also derivable from D03 alone: interest-bearing deposit rate 2.29% (line 165) × (223.4 − 40.0 noninterest-bearing demand)/223.4 ($B, lines 221/227) = 1.880%.
5. Gaps: 9 bp (Fifth Third vs KeyCorp) and 25 bp (KeyCorp vs Huntington) — robust to any rounding in source figures.

minimal_documents: D02, D04, D05 — or D01 in place of D02 (Fifth Third derived ≈1.54%) and/or D03 in place of D04 (Huntington derived ≈1.88%); KeyCorp figure only in D05 (no substitute). Smallest set using directly stated figures: {D02, D04, D05}; using derivations: {D01, D03, D05}.

readings:
- Interest-bearing deposit cost only (misreading, since each bank separately reports a total figure): KeyCorp 2.01% (D05 line 1071) < Fifth Third 2.13% (D01 line 24) < Huntington 2.29% (D03 line 165) → KeyCorp, Fifth Third, Huntington.
- "Total cost" as dollar deposit interest expense: KeyCorp $600M < Fifth Third $891M < Huntington $1,048M → KeyCorp, Fifth Third, Huntington (weaker reading; all three banks present "cost of deposits" as a rate).
- Huntington year-to-date (1.85%, six months, D04 line 1363) instead of quarter: order unchanged (Fifth Third, KeyCorp, Huntington).

gaps: None material. Packet contains only text extractions (manifest method "text", no PDFs/layout files), so original pages could not be inspected; Fifth Third's slide-9 chart was flattened text but its 2Q26/1Q26 values were independently confirmed from D01's balance-sheet figures. Not every line of every document was read: regex searches for cost/deposit/spot/beta/funding-cost terms across all five documents; read in full the relevant sections (D01 lines 1–60, 150–169, 318–347, 1060–1129; D02 lines 1–40; D03 lines 140–244; D04 lines 560–669; D05 lines 75–184, 1050–1094). No spot (period-end) or adjusted deposit-cost figure found for any bank. Did not read question.txt, as instructed.

contaminated: no
