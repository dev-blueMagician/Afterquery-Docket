# i06 strong-solver screen, solver C (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 6). Readings raised: printed ratios give 0 ("the main risk", named less
likely intended), non-regulatory adjusted measures give 4.

answer: 6 basis points (from March 31 to June 30, 2026, KeyCorp's CET1 ratio fell ≈23.8 bps and Huntington's fell ≈18.1 bps; Key's decline was ≈5.6 bps larger, rounding to 6)

confidence: high (arithmetic certain; main risk is the 0 bps reading noted under readings)

path:
1. Both banks report CET1 only to one decimal, so exact ratios were computed from CET1 capital and risk-weighted assets.
2. KeyCorp — D05 (key_ex991_2026-07-21), "GAAP to Non-GAAP Reconciliations," page 15, columns "6/30/2026 | 3/31/2026 | 6/30/2025" (line 752): line 783 "Common equity tier 1 (F) $ 17,016 $ 17,038 $ 16,775"; line 791 "Risk-weighted assets (H) (c) $ 152,317 $ 149,338 $ 143,427"; line 793 "Common equity tier 1 ratio (F/H) (c) 11.2 % 11.4 % 11.7 %"; footnote (c), line 863: "Amounts and ratios as of June 30, 2026 are estimated." (Same 11.2/11.4 at lines 61 — with change "(20)" — 216, 608.)
3. Huntington — D04 (hban_ex992 financial supplement), "Quarterly Capital Under Current Regulatory Standards (Basel III)," page 16, columns June 30 2026, March 31 2026, Dec 31 2025, Sep 30 2025, June 30 2025 (lines 983–985): line 996 "Common equity tier 1 capital 21,388 21,160 …"; line 1006 "Risk-weighted assets (RWA) (1) $ 214,192 $ 208,132 …"; line 1007 ratio "10.0 % 10.2 % …"; same A/C reconciliation lines 1015/1019/1021; footnote (1), line 1025: "June 30, 2026 figures are estimated." (Press release D03 agrees: line 406 "CET1 … was 10.0% at June 30, 2026, compared to 10.2% at March 31, 2026"; RWA "$ 214.2 $ 208.1" billions at line 403.)
4. Calculations:
   - Key: 17,038 / 149,338 = 11.40902% (Mar 31); 17,016 / 152,317 = 11.17144% (Jun 30) → decline 0.23758 pp = 23.758 bps
   - Huntington: 21,160 / 208,132 = 10.16663% (Mar 31); 21,388 / 214,192 = 9.98543% (Jun 30) → decline 0.18119 pp = 18.119 bps
   - Difference: 23.758 − 18.119 = 5.639 → 6 bps. (Rounding ratios to two decimals first gives the same: Key 11.41 → 11.17 = 24 bps; Huntington 10.17 → 9.99 = 18 bps; difference 6.)
   - Cross-check: each computed ratio reproduces the printed one-decimal figure (Key 11.4/11.2; Huntington 10.2/10.0; also Key June 2025 16,775/143,427 = 11.70%, Huntington Dec 2025 17,286/166,684 = 10.37%).

minimal_documents: D04 and D05 (D03 cannot substitute for D04 under the main reading — it lacks CET1 capital dollars, giving only ratios and RWA in billions; D01/D02 are Fifth Third, not needed).

readings:
- Using printed one-decimal ratios: Key 11.4% → 11.2% (D05 line 61 shows "(20)") and Huntington 10.2% → 10.0% are both 20 bps declines → difference 0 bps (needs only D05 plus D03 or D04). I judge this less likely intended, since "to the nearest basis point" points to the precise calculation.
- Using non-regulatory adjusted measures instead (weak reading): Key "Marked CET1" 14,886/149,338 = 9.968% → 14,862/152,317 = 9.757% (21.07 bps decline); Huntington "Adjusted CET1" 19,154/208,132 = 9.203% → 19,347/214,192 = 9.033% (17.03 bps decline) → difference ≈4 bps.

gaps: June 30, 2026 figures are labelled estimated by both banks. Did not read any document in full — searched all five for CET1/common equity tier 1/risk-weighted/RWA/KeyCorp/Huntington and read the capital sections of D03, D04, D05 and D05's footnotes; D01/D02 contain no KeyCorp/Huntington mentions (only generic "Key Highlights/Key Messages/Key statistics"). Sources are .txt filings (no PDFs), so no page images to verify, but extracted table rows are clean and mutually consistent across tables. Did not read question.txt in the packet root, per instructions.

contaminated: no
