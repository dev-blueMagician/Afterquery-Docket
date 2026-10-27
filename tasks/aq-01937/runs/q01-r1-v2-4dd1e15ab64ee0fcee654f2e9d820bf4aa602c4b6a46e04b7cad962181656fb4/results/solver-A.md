# q01 rev 1 solver A (fresh blind-solver, packet solver-1), 2026-10-08
tested_sha256: 4dd1e15ab64ee0fcee654f2e9d820bf4aa602c4b6a46e04b7cad962181656fb4
Transcript audit (audit_transcript.py): 19 tool calls (Glob, Grep, Read, handback), all inside the packet (clean).

answer: 22.40%
confidence: high

path:
1. "investment manager" appears only in a recurring AUM-table footnote: Alternative Investments "Includes real estate investment trusts, currency and commodities, including SPDR(R) Gold Shares and SPDR(R) Gold MiniSharesSM Trust, for which we are not the investment manager but act as the marketing agent." D10 line 189 (footnote 2), D06 line 225 (footnote 1); same wording in D02, D03, D05, D07, D08, D09. Each release quantifies the carve-out in its "About State Street" asterisk note.
2. D06 line 394: "* Assets under management as of June 30, 2025 includes approximately $116 billion of assets with respect to SPDR(R) products for which State Street Global Advisors Funds Distributors, LLC (SSGA FD) acts solely as the marketing agent."
3. D06 line 223: "Ending balance as of June 30, 2025 ... $ 5,117" (also line 47, line 241; D07 line 60/163, D08 line 200, D09 line 219, D10 lines 58 and 209 all show 5,117 for 2Q25).
4. D10 line 360: approximately $157 billion at June 30, 2026.
5. D10 line 162 "Total Assets Under Management $ 5,620 $ 114 $ 551 $ (7) $ 544 $ 6,278"; line 58 "AUM ($ billions)(2) 6,278 5,620 5,117 12 23"; line 209.
6. Originals checked (docs/stt_ex991_2025-07-15.txt lines 46, 415; docs/stt_ex991_2026-07-16.txt lines 59, 371).
Calculation: 5,117 - 116 = 5,001; 6,278 - 157 = 6,121; 1,120 / 5,001 = 0.2239552 -> 22.3955% -> 22.40%.
Rounding note: exact value 22.39552%, only 0.0005 points above the 22.395 boundary; standard rounding 22.40, truncation 22.39; inputs are printed integers so 22.40 holds with the printed figures; the two SPDR figures are "approximately", so true precision is limited.

minimal_documents: D06 and D10 (D06 only source of $116B; D10 only source of $6,278B and $157B; 5,117 also in D07-D10). No alternative set.

readings:
- Total AUM, no carve-out: 1,161 / 5,117 = 22.69% (D10 rounds to "23"); ignores "not the investment manager".
- Whole Alternative Investments line (225; 263): 6,015 / 4,892 - 1 = 22.96%; weaker (the footnote applies "not the investment manager" only to the SPDR Gold products).
- Rounded trillions ($5.1T, $6.3T): 6,143 / 4,984 - 1 = 23.25%; weak.

gaps: none missing. Read D10 lines 1-80, 145-221, 350-385; D06 lines 1-70, 120-254, 390-395; others by explicit-path searches.
contaminated: no.
