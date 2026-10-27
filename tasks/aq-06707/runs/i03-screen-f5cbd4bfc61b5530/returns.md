# i03 strong-solver screen: raw returns (2026-10-18)

Three fresh blind-solver contexts (claude-opus-5-5, effort max), each given only the workspace root,
the packet path runs/i03-screen-f5cbd4bfc61b5530/solver-1 and the exact sentence. Gold: 11.53%.
Returns kept verbatim in substance (harness indentation removed), numbered by launch label (arrival order: 2, 3, 1).

## Solve 1: 11.53% (right), confidence high

answer: 11.53%

confidence: high

path:
1. Q3 2024 and Q3 2023 product revenue — D06 (Q3 2024 release), "Product Revenues" table, text L255–257 (= docs/ original L258–260): "|TRIKAFTA/KAFTRIO|$2,585.0|$2,274.3|…", "|Other product revenues|186.9|209.2|…", "|Product revenues, net|$2,771.9|$2,483.5|…" ($ millions; columns Q3 2024 | Q3 2023). D07 (Q3 2025 release) L220–223 repeats the same Q3 2024 figures (2,585.0 / 186.9 / 2,771.9; ALYFTREK "—").
2. Not all Q3 2024 product revenue was CF — D06 L83: "In the third quarter of 2024, Vertex's product revenue included revenue from the first patient infused with CASGEVY."
3. CASGEVY amount — D07 footnote 1, L227 (verified in docs/ original L231): "In the three and nine months ended September 30, 2024, 'Other product revenues' included $2.0 million from CASGEVY and no revenues from JOURNAVX. The remaining 'Other product revenues' are related to KALYDECO, ORKAMBI, and SYMDEKO/SYMKEVI, our other CF products."
4. Definition of CF product revenue — D05 L236–245: "Total CF product revenues, net" = TRIKAFTA/KAFTRIO + ALYFTREK + "Other CF product revenues (1)" ("Includes KALYDECO, ORKAMBI, and SYMDEKO/SYMKEVI"), with CASGEVY and JOURNAVX listed separately outside CF (check: 2,551.1 + 156.8 + 193.7 = 2,901.6).
5. Q3 2023 was entirely CF: first CASGEVY revenue was Q3 2024 ("first patient infused," D06); JOURNAVX/suzetrigine PDUFA date January 30, 2025 (D06 L93); D03 L263 labels the non-TRIKAFTA line "Other CF products"; D01 and D04 footnotes show no CASGEVY/JOURNAVX revenue in Q1/H1 2024; D08 L272 lists CASGEVY revenue only for 2024 periods. → Q3 2023 CF revenue = $2,483.5M.
6. Calculation: Q3 2024 CF revenue = 2,771.9 − 2.0 = $2,769.9M (check: 2,585.0 + (186.9 − 2.0) = 2,769.9). Growth = (2,769.9 − 2,483.5) / 2,483.5 = 286.4 / 2,483.5 = 0.1153211 → 11.53% (not near a rounding boundary).
7. Consistency: D08/D09 give Q4 2024 CASGEVY $8.0M and FY 2024 $10.0M → 9M 2024 = $2.0M, all in Q3 since none in H1 (D04) — agrees with D07. Q3 2023 total rebuilds as FY 2023 9,869.2 (D08) − Q4 2023 2,517.7 (D08) − H1 2023 4,868.0 (D03) = 2,483.5 ✓.

minimal_documents: D06 + D07. Alternatives: instead of D07, D08 (or D09) + D04 gives Q3 2024 CASGEVY = 10.0 − 8.0 − 0 = $2.0M; instead of D06, D03 + D08 (with D07) gives Q3 2023 = 9,869.2 − 2,517.7 − 4,868.0 = 2,483.5, D08's footnote showing CASGEVY only in 2024 periods (less direct).

readings: Treating total product revenue as CF (ignoring the $2.0M CASGEVY) → 288.4 / 2,483.5 = 11.61% (what D06 alone leads to; counts a non-CF product). TRIKAFTA/KAFTRIO only → 310.7 / 2,274.3 = 13.66% (too narrow; CF also covers KALYDECO, ORKAMBI, SYMDEKO/SYMKEVI). D06's "12%" headline is total product revenue, rounded.

gaps: No document breaks out Q3 2023 by product; all-CF Q3 2023 is a well-supported inference (point 5). No PDFs in the packet (manifest method "text", pages null). Fully read: D06; partially: D07 (L1–45, L175–234), D03 (252–267), D05 (226–247), D08 (260–274), D09 (230–254); D01, D02, D04 and the rest of D05/D08/D09 covered by searches across text/.

contaminated: no

## Solve 2: 11.53% (right), confidence high

answer: 11.53%

confidence: high

path:
1. D06 (Q3 2024 release), Product Revenues table, Three Months Ended September 30 ($M): "|TRIKAFTA/KAFTRIO|$2,585.0|$2,274.3|..." / "|Other product revenues|186.9|209.2|..." / "|Product revenues, net|$2,771.9|$2,483.5|" (source docs/...q3-2024...txt lines 258–259 identical).
2. D07 (Q3 2025 release), Total Revenues table, Q3 2024 column identical (TRIKAFTA/KAFTRIO $2,585.0; ALYFTREK "—"; Other product revenues 186.9). Footnote 1: "In the three and nine months ended September 30, 2024, "Other product revenues" included $2.0 million from CASGEVY and no revenues from JOURNAVX. The remaining "Other product revenues" are related to KALYDECO, ORKAMBI, and SYMDEKO/SYMKEVI, our other CF products."
3. Q3 2023 had no non-CF revenue: D06 "In the third quarter of 2024, Vertex's product revenue included revenue from the first patient infused with CASGEVY"; D06 suzetrigine (JOURNAVX) "PDUFA target action date of January 30, 2025" (not yet approved); D08 footnote counts CASGEVY only in 2024 periods ("The three and twelve month periods ending December 31, 2024, included CASGEVY revenue of $8.0 million and $10.0 million"); D03 labels the H1 2023 remainder "Other CF products" (530.9); 740.1 (D06 9M 2023) − 530.9 = 209.2 matches the Q3 2023 figure.
4. Definition check: D05 (Q2 2026) "Total CF product revenues, net" = TRIKAFTA/KAFTRIO + ALYFTREK + "Other CF product revenues (1)" ("1: Includes KALYDECO, ORKAMBI, and SYMDEKO/SYMKEVI"), CASGEVY/JOURNAVX separate; its Q2 2025 figures reconcile to D04's footnote (236.1 − 30.4 − 12.0 = 193.7).
5. Calculation: Q3 2024 CF = 2,585.0 + 0 (ALYFTREK) + (186.9 − 2.0) = 2,769.9; Q3 2023 CF = 2,274.3 + 209.2 = 2,483.5; growth = 286.4 / 2,483.5 = 0.1153211 → 11.53% (check: 2,483.5 × 1.11532 = 2,769.897).
6. Cross-checks: D08 FY2024 CASGEVY $10.0M − Q4 $8.0M = $2.0M for 9M 2024, and D04 says no CASGEVY revenue in H1 2024 ("In the three and six months ended June 30, 2024, there were no revenues for these products") → Q3 2024 = $2.0M (matches D07). D08 + D03 rebuild Q3 2023: TRIKAFTA 8,944.7 − 2,333.3 − 4,337.1 = 2,274.3; Other 924.5 − 184.4 − 530.9 = 209.2. No document prints a Q3 2024 or Q3 2023 CF total or CF growth rate directly (regex for "CF revenue", "CF product revenue", "cystic fibrosis ... revenue": "Total CF" line only in D02/D05 for 2025–26).

minimal_documents: D06 + D07. Alternatives: D06 + D09 + D04 (D09 FY2024 CASGEVY $10.0M and Q4 2024 $8.0M plus "no revenues from JOURNAVX" in 2024; D04 none in H1 2024); D06 + D08 + D04 (D06's suzetrigine PDUFA date rules out JOURNAVX). D06 replaceable for Q3 2023 by D03 + D08, but D07 or an equivalent still needed for the Q3 2024 CASGEVY amount. D06 alone insufficient.

readings: Total product revenue (keeping the $2.0M CASGEVY) → 288.4 / 2,483.5 = 11.61%. TRIKAFTA/KAFTRIO only → 310.7 / 2,274.3 = 13.66%. D06 headline (total product revenue, rounded) "a 12% increase compared to Q3 2023". The question's "cystic fibrosis product revenue" and the D05/D02 definition support 11.53%.

gaps: Text-only packet (no PDFs or layout files); docs/ originals of the decisive D06 and D07 rows match. Read in full: D06; D07 L1–60 and 185–234; others only revenue tables/footnotes (D03 250–267, D04 228–244, D05 225–249, D08 255–274, D09 230–251) plus regex hits; narratives of D01-D05, D08, D09 not fully read.

contaminated: no

## Solve 3: 11.53% (right), confidence high

answer: 11.53%

confidence: high

path:
1. D06 (Q3 2024 release), Product Revenues table, text/D06.txt L252–257 (same in docs/ q3-2024 file L258–260), columns Q3 2024 | Q3 2023: "|TRIKAFTA/KAFTRIO|$2,585.0|$2,274.3|...", "|Other product revenues|186.9|209.2|...", "|Product revenues, net|$2,771.9|$2,483.5|...".
2. D06 L83: "In the third quarter of 2024, Vertex's product revenue included revenue from the first patient infused with CASGEVY." → Q3 2024 "Other product revenues" includes non-CF revenue; as the first CASGEVY revenue, Q3 2023 had none.
3. D07 (Q3 2025 release) footnote 1, text/D07.txt L227 (docs/ L231) quantifies it: "In the three and nine months ended September 30, 2024, 'Other product revenues' included $2.0 million from CASGEVY and no revenues from JOURNAVX. The remaining 'Other product revenues' are related to KALYDECO, ORKAMBI, and SYMDEKO/SYMKEVI, our other CF products." D07 L220–223 repeats the Q3 2024 figures exactly (2,585.0 / 186.9 / 2,771.9; ALYFTREK "—"); no later document restates them.
4. CF revenue definition: D05 L236–245 "Total CF product revenues, net" = TRIKAFTA/KAFTRIO + ALYFTREK + "Other CF product revenues" ("Includes KALYDECO, ORKAMBI, and SYMDEKO/SYMKEVI"), CASGEVY and JOURNAVX separate and excluded. Check that subtraction reproduces Vertex's own figure: D04 Q2 2025 other product revenues 236.1 − 30.4 CASGEVY − 12.0 JOURNAVX = 193.7 = D05's Q2 2025 "Other CF product revenues" ✓.
5. Calculation: Q3 2024 CF = 2,585.0 + 0 + (186.9 − 2.0) = 2,769.9; Q3 2023 CF = 2,274.3 + 209.2 = 2,483.5 (all CF, no CASGEVY); growth = 286.4 / 2,483.5 = 0.115321 → 11.53% (well away from the 11.535 boundary).
6. Cross-checks: D08 L272 "The three and twelve month periods ending December 31, 2024, included CASGEVY revenue of $8.0 million and $10.0 million"; D04 L243 "In the three and six months ended June 30, 2024, there were no revenues for these products" → 10.0 − 8.0 = $2.0M in Q3 2024, consistent with D07 (D09 L248 repeats $8.0M/$10.0M). Q3 2023 by subtraction: D08 FY2023 9,869.2 − Q4 2023 2,517.7 − D03 H1 2023 4,868.0 = 2,483.5 ✓ (D03 L263 labels H1 2023 non-TRIKAFTA revenue "Other CF products").

minimal_documents: D06 + D07. Other sufficient sets: D06 + D08 + (D03 or D04), with the $2.0M CASGEVY as FY − Q4 with zero in H1 (D09 can stand in for D08); D07 + D08 + D03, deriving Q3 2023 without D06 (relying on D08 not mentioning any 2023 CASGEVY revenue rather than D06's "first patient" statement). D06 alone insufficient (does not give the CASGEVY amount).

readings: Treating all Q3 2024 product revenue as CF (ignoring the $2.0M CASGEVY): 288.4 / 2,483.5 = 11.61%. TRIKAFTA/KAFTRIO alone: 310.7 / 2,274.3 = 13.66%. D06 headline "a 12% increase" = total product revenue, rounded. Primary answer stays 11.53% (question asks for CF product revenue; Vertex's own later definition excludes CASGEVY).

gaps: No document states a Q3 2024 CF total or CF growth rate directly (searched all text/ files for CF growth percentages). Zero CASGEVY revenue in Q3 2023 inferred from D06's "first patient infused" wording, consistent with D04/D03/D08; not stated explicitly for Q3 2023. Read in full: D06; in part: D07 L1–50 plus tables and footnote, D08 L1–40 and 258–279, D09 L232–251, D03 L252–269, D04 L230–245, D05 L228–247; the rest by keyword/table-row searches. Decisive figures checked against docs/ originals; no PDFs or layouts (manifest method "text").

contaminated: no. I did not open question.txt, and nothing besides the question was provided.
