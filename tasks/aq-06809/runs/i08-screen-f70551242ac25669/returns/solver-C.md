# i08 strong-solver screen, solver C (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 6). Readings raised: 0 (printed ratios, ruled out by the wording),
4 (AOCI-inclusive, not regulatory), -6 (reversed sign).

answer: 6 basis points (KeyCorp's CET1 ratio fell ≈23.76 bp vs. Huntington's ≈18.12 bp; KeyCorp's decline was larger by 5.64 bp → 6 bp)

confidence: high

path:
1. KeyCorp — D05 (key_ex991_2026-07-21, "GAAP to Non-GAAP Reconciliations," page 15 block, text/D05.txt lines 752, 783-793; column header "6/30/2026 | 3/31/2026 | 6/30/2025"):
   - L783 "Common equity tier 1 (F) | $17,016 | $17,038 | $16,775"
   - L791 "Risk-weighted assets (H) (c) | $152,317 | $149,338 | $143,427"
   - L793 "Common equity tier 1 ratio (F/H) (c) 11.2 % 11.4 % 11.7 %"; L863 "(c)Amounts and ratios as of June 30, 2026 are estimated."
2. Huntington — D04 (hban_ex992_2026-07-23, Quarterly Financial Supplement, "Quarterly Capital Under Current Regulatory Standards (Basel III)," text/D04.txt lines 983-1025; header "June 30, March 31, December 31, September 30, June 30" / "2026 2026 2025 2025 2025"):
   - L996 "Common equity tier 1 capital | 21,388 21,160 17,286 15,924 15,539"
   - L1006 "Risk-weighted assets (RWA) (1) | $214,192 $208,132 $166,684 $150,222 $148,602"
   - L1007 "Common equity tier 1 risk-based capital ratio (1) | 10.0 % 10.2 % …" (same figures restated L1015-1021 as "CET1 ratio (A/C)"); L1025 "(1)June 30, 2026 figures are estimated."
3. Calculations:
   - KeyCorp 3/31: 17,038 / 149,338 = 11.409018%; 6/30: 17,016 / 152,317 = 11.171439% → decline 0.237580 pp = 23.758 bp.
   - Huntington 3/31: 21,160 / 208,132 = 10.166625%; 6/30: 21,388 / 214,192 = 9.985434% → decline 0.181191 pp = 18.119 bp.
   - Difference = 23.758 − 18.119 = 5.639 bp → 6 bp.
4. Verification by cross-multiplication: KeyCorp (17,038×152,317 − 17,016×149,338)/(149,338×152,317) = 54,041,638 / 22,746,716,146 = 0.0023758; Huntington (21,160×214,192 − 21,388×208,132)/(208,132×214,192) = 80,775,504 / 44,580,209,344 = 0.0018119.
5. Alignment checks: each computed ratio rounds to the printed one (11.2/11.4 KeyCorp; 10.0/10.2 Huntington); Huntington's other ratios tie to the same RWA (e.g., 24,279/214,192 = 11.3% Tier 1; 29,076/214,192 = 13.6% total); KeyCorp's 6/30/2025 column ties (16,775/143,427 = 11.7%).

minimal_documents: D04 + D05 (no substitute for D04: D03 — Huntington release — gives RWA only in billions "$ 214.2 $ 208.1" (line 403) and no CET1 capital dollar amount (searched "CET1 capital", "tier 1 capital", 21,388, 21,160: none); no substitute for D05: KeyCorp CET1 dollars and RWA appear only there; D01/D02 (Fifth Third) contain no KeyCorp/Huntington references — searched case-sensitive KeyCorp, Huntington, HBAN, \bKEY\b: none relevant).

readings:
- Using printed rounded ratios (KeyCorp 11.4→11.2, reported change "(20)" bps at D05 L61; Huntington 10.2→10.0, D03 L45) → 20 − 20 = 0 bp; ruled out by the question's requirement to compute ratios from CET1 capital and RWA.
- Rounding each computed ratio to 2 decimals first (11.41−11.17 = 24; 10.17−9.99 = 18) → 6 bp, same.
- Using non-GAAP measures instead (KeyCorp "Marked CET1" 14,886/149,338 → 14,862/152,317 = 21.07 bp decline; Huntington "Adjusted CET1" 19,154/208,132 → 19,347/214,192 = 17.03 bp decline) → ≈4 bp; not regulatory CET1, so inconsistent with the question.
- Expressed as Huntington minus KeyCorp → −6 bp.

gaps: June 30, 2026 amounts are labelled estimates in both releases; no revision notes for March 31. Sources are text/HTML extractions (no PDFs) so no page images to check; table alignment confirmed via printed-ratio reconciliation. Unread coverage: read D05 lines 1-90, 195-244, 580-639, 730-868; D04 lines 1-12, 225-254, 975-1044; D03 lines 30-109, 385-409; all five documents searched for CET1/common equity tier 1/risk-weighted/RWA/entity names/key figures; D01/D02 checked only by search, not read in full.

contaminated: no (received only workspace root, packet path and question; read nothing outside the packet's text/ and docs/)
