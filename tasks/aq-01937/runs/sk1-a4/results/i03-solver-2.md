# i03 sketch blind solve (fresh blind-solver, packet sk1-a4/solver-2), 2026-10-08

Question given: How much revenue from distribution and marketing activities did State Street include in its foreign exchange trading services revenue for the first half of 2025, in millions of dollars?

answer: $63 million (1Q25: $25M + 2Q25: $38M)
confidence: high

path:
1. D09 line 245 (also line 99): "In the first quarter of 2026, revenue related to distribution and marketing activities was reclassified from Foreign exchange trading services to Management fees. Additionally, Lending related and other fees, previously recognized within Software and processing fees, was reclassified to Other fee revenue ... Prior-period amounts have been reclassified to conform to the current presentation. These reclassifications had no impact on Total fee revenue..." The second reclassification does not touch FX trading or Management fees.
2. Originally reported 1Q25 and 2Q25, D06 lines 254-255 (2Q25 | 1Q25 | 2Q24): "Management fees 562 562 511"; "Foreign exchange trading services 431 362 336". Same 1Q25 in D05 lines 251-252; same 2Q25 in D07 lines 203-204.
3. Reclassified 1Q25, D09 lines 230-231 (1Q26 | 4Q25 | 1Q25): "Management fees(1) 724 717 587"; "Foreign exchange trading services(1) 435 350 337".
4. Reclassified 2Q25, D10 lines 220-221 (2Q26 | 1Q26 | 2Q25): "Management fees 772 724 600"; "Foreign exchange trading services 494 435 393". D10 has no reclassification footnote; its 1Q26 figures (724, 435) match D09's new-basis figures.
5. 1Q25: 362 - 337 = 25 (management 587 - 562 = 25). 2Q25: 431 - 393 = 38 (600 - 562 = 38). First half: 25 + 38 = 63 (793 - 730 = 63).
6. Checks: Other fee revenue 32 + 67 = 99 (D09) and 66 + 61 = 127 (D10); Software services 158 and 169; total fee revenue unchanged (2,570; 2,719). The $3M 2Q25 FX notable item sits inside both 431 (D06) and 393 (D10). Printed YoY rates match reclassified figures (435/337 - 1 = 29.1%; 494/393 - 1 = 25.7%). 4Q25 sanity check: D08 662/405 vs D09 717/350, shift 55 both ways. Decisive rows re-checked against docs\.

minimal_documents: D06, D09, D10 (alternative: D05 + D07 instead of D06). D09 irreplaceable (only document naming the reclassification and the only source of reclassified 1Q25); D10 irreplaceable (only source of reclassified 2Q25).

readings: one quarter only gives 25 or 38; total H1 FX revenue would be 793 (original) or 730 (reclassified) - not the asked portion.

gaps: no document states the amount directly; attribution of the whole FX difference rests on D09's note naming that as the only FX change (matching management-fee offset supports it); D10 repeats no note; no six-month table. Read revenue and highlights of D05-D10 in full; searched all documents for distribution, marketing, foreign exchange trading, reclassify/recast, half-year/six months; D01-D04 not read in full.

contaminated: no
