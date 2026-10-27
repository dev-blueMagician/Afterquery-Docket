# i06 strong-solver screen, solver B (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 6). Confidence "high (medium on which reading is meant)"; readings raised:
printed ratios give 0 (named weaker), AOCI-inclusive ratios give 4.

answer: 6 basis points (KeyCorp's CET1 ratio fell ≈23.76 bp vs. Huntington's ≈18.12 bp; difference 5.64 bp → 6 bp)
confidence: high (medium on which reading is intended — see readings)

path:
1. KeyCorp — D05 (D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-06809\runs\i06-screen-2cfcfa4976a8bfe0\solver-1\text\D05.txt), "GAAP to Non-GAAP Reconciliations," columns 6/30/2026 | 3/31/2026 | 6/30/2025: line 783 "Common equity tier 1 (F)|$|17,016 $|17,038 $|16,775|"; line 791 "Risk-weighted assets (H) (c)|$|152,317 $|149,338 $|143,427|"; line 793 "Common equity tier 1 ratio (F/H) (c) 11.2 % 11.4 % 11.7 %"; line 863 "(c)Amounts and ratios as of June 30, 2026 are estimated." Confirmed identical in raw source docs\key_ex991_2026-07-21.txt (lines 903, 913). 17,038/149,338 = 11.40902%; 17,016/152,317 = 11.17144% → decline 0.23758 pp = 23.76 bp.
2. Huntington — D04 (text\D04.txt), "Quarterly Capital Under Current Regulatory Standards (Basel III)," columns June 30 2026 | March 31 2026 | Dec 31 2025 | …: line 996 "Common equity tier 1 capital|21,388 21,160 17,286 15,924 15,539"; line 1006 "Risk-weighted assets (RWA) (1)|$|214,192 $|208,132 $|166,684 …"; line 1007 "Common equity tier 1 risk-based capital ratio (1)|10.0 % 10.2 % 10.4 % 10.6 % 10.5 %"; repeated as (A), (C), A/C at lines 1015/1019/1021; footnote line 1025 "(1)June 30, 2026 figures are estimated." Confirmed in raw docs\hban_ex992_2026-07-23.txt (lines 1212, 1224, 1235, 1239). 21,160/208,132 = 10.16663%; 21,388/214,192 = 9.98543% → decline 0.18119 pp = 18.12 bp.
3. Sanity check: every computed ratio rounds to the printed one-decimal ratio for all periods of both banks (e.g., 16,775/143,427 = 11.70%; 17,286/166,684 = 10.37%), confirming column alignment.
4. Difference: 23.758 − 18.119 = 5.639 → 6 bp (rounding each decline first, 24 − 18, also gives 6; not near a rounding boundary).
5. Direct-answer search: neither bank prints CET1 ratios to more than one decimal (KeyCorp D05 line 61 "Common Equity Tier 1 ratio (b)|11.2 11.4 11.7 (20) (50)" — printed change 20 bp; Huntington D03 line 45 "CET1 … was 10.0%, at June 30, 2026, compared to 10.2% at the prior quarter end"; D03 Table 12, line 403, gives RWA only in billions "$ 214.2 / $ 208.1" and no CET1 capital dollars). Those printed ratios cannot support a nearest-basis-point answer, so the dollar components were required.

minimal_documents: D04 + D05 (neither replaceable: D05 is the only KeyCorp document; D03 lacks Huntington CET1 capital dollars; Fifth Third docs D01/D02 have no KeyCorp/Huntington data).

readings:
- Printed rounded ratios: KeyCorp 11.4% → 11.2% (20 bp decline, also printed as "(20)"); Huntington 10.2% → 10.0% (20 bp) → difference 0 bp. Weaker because inputs are only precise to 10 bp while the question asks nearest basis point.
- Non-GAAP AOCI-inclusive measures (unlikely, since question says "common equity tier 1 ratios"): KeyCorp marked CET1 (D05 line 787, G/H) 14,886/149,338 = 9.968% → 14,862/152,317 = 9.757% (21.07 bp decline); Huntington adjusted CET1 (D04 line 1018, B/C) 19,154/208,132 = 9.203% → 19,347/214,192 = 9.033% (17.03 bp decline) → difference ≈ 4 bp.

gaps: June 30, 2026 figures are estimates for both banks (footnotes). Sources are plain .txt (no PDFs/page markers/layout files) — no original pages to inspect; table rows parsed consistently. Coverage: read D05 lines 1–120, 200–249, 590–629, 735–869; D04 lines 150–259, 960–1039; D03 lines 1–110, 385–409; did not read D01 or D02 in full (searched only for CET1/KeyCorp/Huntington/"Key"/"peer" — matches were Fifth Third's own figures, generic "Key statistics/Key Messages," and peer-median fee/NDFI exposure comparisons with no other banks' CET1 data). All five text files searched for the decisive dollar figures — found only in D04/D05.

contaminated: no (nothing leaked; did not open the packet's question.txt; used only the question as given)
