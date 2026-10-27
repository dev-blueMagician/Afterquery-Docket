# i08 strong-solver screen, solver B (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 6). Readings raised: 0 (printed ratios, ruled out by the wording),
5 (D03's RWA in billions, weaker).

answer: 6 basis points (KeyCorp's CET1 ratio fell ≈23.76 bp, Huntington's ≈18.12 bp; KeyCorp's decline was larger by 5.64 bp → 6)
confidence: high

path:
1. KeyCorp — D05 (key_ex991_2026-07-21, "GAAP to Non-GAAP Reconciliations," release Page 15; D05.txt lines 752, 783, 791, 793; original docs/key_ex991_2026-07-21.txt lines 903, 913, 916), columns "6/30/2026|3/31/2026|6/30/2025": "Common equity tier 1 (F) $ 17,016 $ 17,038 $ 16,775"; "Risk-weighted assets (H) (c) $ 152,317 $ 149,338 $ 143,427"; "Common equity tier 1 ratio (F/H) (c) 11.2 % 11.4 % 11.7 %". Footnote (c), line 863: "Amounts and ratios as of June 30, 2026 are estimated."
2. Huntington — D04 (hban_ex992_2026-07-23, "Quarterly Capital Under Current Regulatory Standards (Basel III)," supplement p.16; D04.txt lines 983-1007 and 1015-1021; original docs lines 1212, 1224, 1235, 1239), columns June 30 2026, March 31 2026, Dec 31 2025, …: "Common equity tier 1 capital 21,388 21,160 17,286 15,924 15,539"; "Risk-weighted assets (RWA) (1) $ 214,192 $ 208,132 …"; "CET1 ratio (A/C) 10.0 % 10.2 % …". Footnote (1): "June 30, 2026 figures are estimated." Cross-check of CET1 build-up: 32,624 − 2,891 + 2,208 − 10,126 − 427 = 21,388 (June); 32,535 − 2,891 + 2,055 − 10,180 − 359 = 21,160 (March) — ties.
3. Calculations (each verified by back-multiplication):
   - KeyCorp Mar 31: 17,038 / 149,338 = 11.409018%; Jun 30: 17,016 / 152,317 = 11.171439% → decline 0.237580 pp = 23.758 bp
   - Huntington Mar 31: 21,160 / 208,132 = 10.166625%; Jun 30: 21,388 / 214,192 = 9.985434% → decline 0.181191 pp = 18.119 bp
   - Difference: 23.758 − 18.119 = 5.639 bp → 6 bp
   - All calculated ratios round to the printed one-decimal ratios (11.4/11.2; 10.2/10.0), confirming input consistency.
4. Robust to rounding order: rounding ratios to 0.01% first gives (11.41 − 11.17) − (10.17 − 9.99) = 24 − 18 = 6; rounding each decline to whole bp first also gives 24 − 18 = 6.

minimal_documents: D04 and D05 (no substitute in the packet: D03, the Huntington earnings release Table 12 line 403, gives RWA only in billions "$ 214.2 $ 208.1" and no CET1 capital dollars, so cannot replace D04; D05 is the only KeyCorp document; D01/D02 are Fifth Third and unneeded).

readings:
- Using printed rounded ratios (KeyCorp "11.2 11.4 … (20)" bp, D05 line 61; Huntington 10.2% → 10.0%, D03 line 406 / D04 line 235): both declines 20 bp → difference 0 bp. Ruled out by the question's instruction to calculate the ratios from CET1 capital and RWA.
- Using D03's billion-rounded Huntington RWA (214.2/208.1) with D04's CET1 capital: 9.98506% and 10.16819% → decline 18.31 bp → difference 5.45 bp → 5 bp. Weaker, since D04 reports the exact RWA in millions.
- Direction unambiguous (KeyCorp's decline was the larger).
- No bank-level (subsidiary) or restated March 31 figures appear in the packet; consolidated holding-company figures from the Q2 releases used.

gaps: June 30, 2026 amounts are labelled estimated by both banks (does not affect the calculation). Sources are .txt (manifest "method": "text", "pages": null; no layout files/PDFs), so no original pages to inspect — decisive rows verified against the original docs/ text instead. Coverage: searched all of D01–D05 for CET1/common equity tier 1/risk-weighted/RWA; read the relevant sections of D03, D04, D05; did not fully read D01/D02 (Fifth Third) or non-capital sections of D03–D05.

contaminated: no
