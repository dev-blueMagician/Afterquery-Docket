# i11 sketch blind solve (fresh blind-solver, packet sk1-a4/solver-1), 2026-10-08

Question given: Using the definition under which State Street's foreign exchange trading services revenue was $393 million in the second quarter of 2025, by what percentage did that revenue grow from the fourth quarter of 2025 to the second quarter of 2026? Round to the nearest whole percent.
Transcript audit (audit_transcript2.py): 16 tool calls (Grep, Read, handback), all inside the packet (clean).

answer: 41%
confidence: high

path:
1. The $393M definition is the restated basis introduced in 1Q26: D10 line 221 "Foreign exchange trading services 494 435 393 13.6 25.7" (2Q26, 1Q26, 2Q25); footnote lines 93/255 "GAAP FX trading services revenue of $393 million in 2Q25"; the same quarter first reported as $431M in D06 line 255; difference explained by D09 lines 99/245 (distribution and marketing revenue reclassified from FX trading services to Management fees; prior periods reclassified).
2. 4Q25 on that basis: D09 line 231 (docs line 238) "Foreign exchange trading services(1) 435 350 337 24.3 29.1" -> 4Q25 = $350M (the 4Q25 release, D08 line 213, showed the old-basis $405M).
3. 2Q26 = $494M (D10 line 221).
4. (494 - 350) / 350 = 144 / 350 = 0.41143 -> 41%.
Checks: printed percentages match (435/350 - 1 = 24.29%; 494/393 - 1 = 25.70%); fee lines sum to totals (D09 4Q25 2,862; D10 2Q26 3,188; D10 2Q25 2,719); reclassification nets to zero against Management fees (2Q25 +38/-38; 4Q25 +55/-55).

minimal_documents: D09 + D10 (D09 only document with restated 4Q25 FX; D10 only source of 2Q26 and of the $393M definition); D06/D08 context only.
readings: ex-notables 41% (only FX notable is 2Q25's $3M recovery); mixed basis (D08's $405M) 89/405 = 21.98% -> 22%, ruled out by the stipulated definition.
gaps: none affecting the answer; D01-D07 by targeted search; D08 revenue rows and notable items; D10 through line 300.
contaminated: no

Caller note: match (gold 41%). Fair for a strong solver; the pin by number makes the decoy (22%) excluded by the wording. The chained printed QoQ rates (24.3% x 13.6% -> 41.2%) reach the gold without the decoy (author A's note), a difficulty risk.
