# i06 strong-solver screen, solver A (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 6). Readings raised: printed one-decimal ratios give 0 (named weaker);
AOCI-inclusive ratios give 4; relative declines 30 (stretched).

answer: 6 basis points (Key's CET1 ratio fell ≈23.8 bps vs Huntington's ≈18.1 bps; Key's decline was ≈5.6 bps larger → 6 bps)

confidence: high (arithmetic solid; only real alternative is the rounded-headline reading noted under readings)

path:
1. KeyCorp — D05 (docs/key_ex991_2026-07-21.txt), "GAAP to Non-GAAP Reconciliations" table (release Page 15), columns "6/30/2026 | 3/31/2026 | 6/30/2025" (D05 line 752):
   - line 783: "Common equity tier 1 (F) | $ 17,016 $ 17,038 $ 16,775"
   - line 791: "Risk-weighted assets (H) (c) | $ 152,317 $ 149,338 $ 143,427"
   - line 793: "Common equity tier 1 ratio (F/H) (c) 11.2 % 11.4 % 11.7 %"; line 863: "(c)Amounts and ratios as of June 30, 2026 are estimated." (Same figures in raw source, docs lines 903/913; headline table line 61 "Common Equity Tier 1 ratio (b) 11.2 11.4 11.7 (20) (50)".)
2. Huntington — D04 (docs/hban_ex992_2026-07-23.txt), "Quarterly Capital Under Current Regulatory Standards (Basel III)" (supplement page 16), columns June 30 2026, Mar 31 2026, Dec 31 2025, Sep 30 2025, Jun 30 2025:
   - lines 996/1015: "Common equity tier 1 (CET1) capital (A) | $ 21,388 $ 21,160 $ 17,286 …"
   - lines 1006/1019: "Risk-weighted assets (RWA) (C) 214,192 208,132 166,684 …"
   - line 1021: "CET1 ratio (A/C) 10.0 % 10.2 % 10.4 % 10.6 % 10.5 %"; line 1025: "(1)June 30, 2026 figures are estimated." (Raw source matches, docs lines 1212/1224/1235/1239; D03 line 45 text: "CET1 … ratio was 10.0%, at June 30, 2026, compared to 10.2% at the prior quarter end.")
3. Unrounded ratios (each verified by multiplying back; all reproduce the printed rounded ratios, incl. other periods):
   - Key 6/30: 17,016 / 152,317 = 11.17144%; Key 3/31: 17,038 / 149,338 = 11.40902% → decline 0.23758 pp = 23.76 bps
   - Huntington 6/30: 21,388 / 214,192 = 9.98543%; 3/31: 21,160 / 208,132 = 10.16663% → decline 0.18119 pp = 18.12 bps
   - Difference = 23.758 − 18.119 = 5.64 bps → 6 bps (rounding each decline first, 24 − 18, also gives 6). Rounding sensitivity: inputs are $ millions, so each ratio can move only ~±0.03 bps — result stays 6.

minimal_documents: D04 + D05 (no other packet document gives Key's CET1 capital/RWA, so D05 required; D03 cannot replace D04 for the bp calculation — it has only rounded ratios 10.0/10.2 and RWA in billions "$ 214.2 $ 208.1" (line 403), no CET1 capital amounts. For the rounded-headline reading below, D03 or D04 plus D05 suffices. D01/D02 are Fifth Third — irrelevant; "Key…" hits in D02 are slide titles like "Key Messages", not KeyCorp.)

readings:
- Printed one-decimal ratios: Key 11.4 → 11.2 (−20 bps, printed "(20)"), Huntington 10.2 → 10.0 (−20 bps) → difference 0 bps. The headline ratios are only precise to 10 bps, so the requested basis-point precision points to the component computation (6).
- Non-regulatory ratios (not asked): Key marked CET1 (14,862/152,317 vs 14,886/149,338) declined ≈21.07 bps; Huntington adjusted CET1 (19,347/214,192 vs 19,154/208,132) declined ≈17.0 bps → difference ≈4 bps.
- Relative (percentage) declines (stretched reading): Key 2.08% vs Huntington 1.78% → ≈0.30 pp = 30 "bps".

gaps: Both companies' June 30, 2026 figures are labeled estimated. No layout files/PDF page images (sources are HTML-derived text); extracted rows verified against raw docs. Unread coverage: D01/D02 checked only by targeted searches (CET1, KeyCorp, Huntington, Key, peer); D03/D04/D05 read in opening pages and capital sections, rest only via those searches. question.txt not read.

contaminated: no
