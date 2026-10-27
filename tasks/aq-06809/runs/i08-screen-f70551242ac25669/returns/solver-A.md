# i08 strong-solver screen, solver A (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 6). Readings raised: 0 (printed ratios, excluded by the wording), 5 (D03's
RWA in billions), 4 (AOCI-inclusive, excluded), -6 (reversed sign).

answer: 6 basis points (KeyCorp's CET1 ratio fell ≈23.76 bp vs Huntington's ≈18.12 bp; KeyCorp's decline was larger by 5.64 bp → 6 bp)

confidence: high

path:
1. KeyCorp — D05 (text/D05.txt, GAAP to Non-GAAP Reconciliations, columns 6/30/2026 | 3/31/2026 | 6/30/2025, "Page 16" follows):
   - line 783: "Common equity tier 1 (F)|$|17,016 $|17,038 $|16,775"
   - line 791: "Risk-weighted assets (H) (c)|$|152,317 $|149,338 $|143,427"
   - line 793: "Common equity tier 1 ratio (F/H) (c) 11.2 % 11.4 % 11.7 %"; footnote line 863 "(c)Amounts and ratios as of June 30, 2026 are estimated."
   - Same rows in docs/key_ex991_2026-07-21.txt lines 903, 913, 916.
2. Huntington — D04 (text/D04.txt, "Quarterly Capital Under Current Regulatory Standards (Basel III)"; header "June 30, March 31, December 31, September 30, June 30, / 2026 2026 2025 2025 2025"):
   - line 996/1015: "Common equity tier 1 (CET1) capital (A)|$|21,388 $|21,160 ..."
   - line 1006/1019: "Risk-weighted assets (RWA) (1)|$|214,192 $|208,132 ..."
   - line 1021: "CET1 ratio (A/C)|10.0 % 10.2 % ..."; line 1025 "(1)June 30, 2026 figures are estimated."
   - Same rows in docs/hban_ex992_2026-07-23.txt lines 1212, 1224, 1239, 1243.
3. Calculations (verified by cross-multiplication):
   - KeyCorp Mar 31: 17,038 / 149,338 = 11.409018%; Jun 30: 17,016 / 152,317 = 11.171439% → decline 0.237580 pp = 23.758 bp
   - Huntington Mar 31: 21,160 / 208,132 = 10.166625%; Jun 30: 21,388 / 214,192 = 9.985434% → decline 0.181191 pp = 18.119 bp
   - Difference: 23.758 − 18.119 = 5.639 bp → 6 bp
4. Sanity check: each computed ratio rounds to the bank's printed ratio (11.4→11.2; 10.2→10.0); KeyCorp's 6/30/2025 column also ties (16,775/143,427 = 11.70%).
5. Rounding robustness: result is 6 whether ratios are rounded to two decimals first (11.41−11.17 = 24 bp; 10.17−9.99 = 18 bp) or declines are rounded first (24 − 18).

minimal_documents: D04 + D05. D03 cannot substitute for D04 — its Table 12 (D03 lines 400–403) gives only ratios and RWA in billions ("Total risk-weighted assets (1) $ 214.2 $ 208.1"), no CET1 capital in dollars (searched D03 for 21,388/21,160: none). No other document carries KeyCorp's CET1 capital or RWA (D01/D02 are Fifth Third; case-sensitive search for KeyCorp/Huntington found no matches).

readings:
- Using the printed one-decimal ratios: KeyCorp 11.4→11.2 (D05 line 61 shows "(20)" bps vs 1Q26), Huntington 10.2→10.0 (D03 line 406) → 0 bp; not consistent with the question's instruction to calculate from capital and RWA.
- Mixing D04 capital with D03's rounded RWA in billions ($214.2B/$208.1B): Huntington 10.168188% → 9.985061%, decline 18.313 bp → difference 5.445 bp → 5 bp (less precise; D04 reports RWA to the million).
- Using the non-GAAP AOCI-inclusive measures (KeyCorp "Marked CET1" 14,886/149,338 → 14,862/152,317 = 21.07 bp decline; Huntington "Adjusted CET1" 19,154/208,132 → 19,347/214,192 = 17.03 bp decline) → 4.04 bp; excluded because the question specifies reported CET1 capital.
- Sign: if difference is taken as Huntington minus KeyCorp, −6 bp (magnitude unchanged).

gaps: June 30, 2026 figures are labeled estimated by both banks (scoped hedge; does not change the computation). No Q1 2026 releases in the packet to check whether March 31 figures were later restated. Read only capital sections and search hits of D03/D04/D05 (not full documents); D01/D02 checked by search, not read. Manifest shows text sources with pages null, no layout/PDF files in packet, so original pages could not be inspected; extracted table rows parsed cleanly and match the docs/ copies. Deliberately did not open question.txt in the packet folder, per instructions.

contaminated: no
