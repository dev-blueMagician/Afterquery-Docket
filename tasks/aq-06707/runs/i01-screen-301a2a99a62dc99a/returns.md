# i01 strong-solver screen: raw returns (2026-10-18)

Three fresh blind-solver contexts (claude-opus-5-5, effort max), each given only the workspace root,
the packet path runs/i01-screen-301a2a99a62dc99a/solver-1 and the exact sentence. Gold: $35,000.
Returns kept verbatim in substance (harness indentation removed), numbered by launch label (arrival order: 2, 3, 1).

## Solve 1: $35,000 (right), confidence high

answer: $35,000 (Q1 2025, the fewest infusions: ~$1,775,000 per patient infused vs. Q4 2025, the most infusions: ~$1,810,000)

confidence: high

path:
1. Q4 2025 infusions — D09 L83: "This reflects 64 patients receiving infusions of CASGEVY in 2025, including 30 people infused in the fourth quarter of 2025."
2. Q2 2025 infusions — D04 L72: "since launch through June 30th, 2025, ... 29 patients have received infusions of CASGEVY, including 16 infused in the second quarter of 2025."
3. Q3 2025 infusions — D07 L74: "39 people with SCD or TDT have received infusions of CASGEVY, including 10 people infused in the third quarter of 2025." (Cumulative check: 29 + 10 = 39 ✓.)
4. Q1 2025 infusions are not stated anywhere (searched "infus" across all text/ files and "first quarter ... infus/patients" in docs/). Derived: Q1 = 64 − 16 − 10 − 30 = 8. Cross-check: cumulative through 3/31/25 = 29 − 16 = 13; cumulative through 12/31/25 = 39 + 30 = 69; pre-2025 infusions = 69 − 64 = 5; Q1 = 13 − 5 = 8 ✓. Infusions: Q1 = 8 (fewest), Q2 = 16, Q3 = 10, Q4 = 30 (most).
5. CASGEVY revenue: Q1 2025 = $14.2M — D01 L255 "In the first quarter of 2025, "Other product revenues" included $14.2 million from CASGEVY"; also D02 L224 "|CASGEVY|42.9|14.2|" (2025 column). Q2 2025 = $30.4M, H1 = $44.6M — D04 L243 "$30.4 million and $44.6 million from CASGEVY" (D05 L240 same); 44.6 − 30.4 = 14.2 ✓. Q3 2025 = $16.9M (9M $61.5M) — D07 L227 "$16.9 million and $61.5 million from CASGEVY". Q4 2025 = $54.3M (FY $115.8M) — D09 L248 "In the three and twelve months ended December 31, 2025, "Other product revenues" included $54.3 million and $115.8 million from CASGEVY" (headline D09 L83 rounds to "$54 million"). Check: 14.2 + 30.4 + 16.9 + 54.3 = 115.8 ✓.
6. Revenue per infused patient: Q1 14.2/8 = $1,775,000; Q2 30.4/16 = $1,900,000; Q3 16.9/10 = $1,690,000; Q4 54.3/30 = $1,810,000.
7. Fewest-infusion quarter (Q1) vs most-infusion quarter (Q4): 1,810,000 − 1,775,000 = $35,000 lower.

minimal_documents: D04, D07, D09. D04: Q2 count (16, unique) and Q1 revenue by H1 − Q2 (44.6 − 30.4). D07: Q3 count (10, unique), needed to derive Q1's count and to show Q3 isn't the fewest. D09: full-year count 64, Q4 count 30, Q4 revenue $54.3M. Alternatives: Q1 revenue can come from D01, D02 or D05 instead of D04's subtraction, but D04 is still needed for the Q2 count. Without D04 or D07, only Q1+Q2 (24) or Q1+Q3 (18) is determinable, not Q1 alone.

readings: (a) Using D09's rounded headline "$54 million" for Q4: 54/30 = $1,800,000 → difference $25,000; rejected because the footnote gives the more precise $54.3M and the answer is requested to the nearest thousand. (b) Ignoring Q1 because its count isn't printed and treating Q3 (10) as fewest: 1,810,000 − 1,690,000 = $120,000; rejected because Q1's 8 follows directly from D09's full-year total, confirmed by the cumulative figures. Rounding sensitivity: revenue printed to $0.1M means the true difference could range roughly $27K–$43K; at printed precision the answer is $35,000.

gaps: Q1 2025 infusions not stated directly (derived, confirmed two ways). D03 and D06 checked only via search hits; D06 L83 notes the first infused patient in Q3 2024. D08 reports only cell collections. All sources are text (method "text", no PDF pages); no extraction problems.

contaminated: no

## Solve 2: $35,000 (right), confidence high

answer: $35,000 — CASGEVY revenue per patient infused was about $1,775,000 in Q1 2025 (fewest infusions) vs. about $1,810,000 in Q4 2025 (most infusions), so Q1 was $35,000 lower.

confidence: high

path:
1. Q1 2025 revenue $14.2M — D01 footnote 1 (L255): "In the first quarter of 2025, "Other product revenues" included $14.2 million from CASGEVY"; D02 revenue table (L224) "|CASGEVY|42.9|14.2|" (Q1'26, Q1'25).
2. Q2 2025 revenue $30.4M and 16 infusions — D04 footnote 1 (L243): "In the three and six months ended June 30, 2025, … included $30.4 million and $44.6 million from CASGEVY" (44.6 − 30.4 = 14.2, matches fact 1); D05 table (L240) repeats 30.4. D04 L72: "since launch through June 30th, 2025, … 29 patients have received infusions of CASGEVY, including 16 infused in the second quarter of 2025."
3. Q3 2025 revenue $16.9M and 10 infusions — D07 footnote 1 (L227): "$16.9 million and $61.5 million from CASGEVY"; D07 L74: "39 people with SCD or TDT have received infusions of CASGEVY, including 10 people infused in the third quarter of 2025."
4. Q4 2025 revenue $54.3M, 30 infusions, 64 in 2025 — D09 footnote 1 (L248): "$54.3 million and $115.8 million from CASGEVY" (reconciles: 14.2+30.4+16.9+54.3 = 115.8; 61.5+54.3 = 115.8). D09 L83: "Vertex recorded fourth quarter 2025 CASGEVY revenue of $54 million and full year 2025 revenue of $116 million. This reflects 64 patients receiving infusions of CASGEVY in 2025, including 30 people infused in the fourth quarter of 2025."
5. Q1 2025 infusions (not stated in any document; D01 does not mention them) derived two ways: 64 − 16 − 10 − 30 = 8; cumulative: 29 − 16 = 13 through Mar 31, 2025 (since launch); 39 + 30 = 69 through year-end; 69 − 64 = 5 infused in 2024; Q1 2025 = 13 − 5 = 8. Both give 8.
6. Infusions: Q1 8, Q2 16, Q3 10, Q4 30 → fewest Q1, most Q4.
7. Revenue per patient: Q1 14.2/8 = $1.775M; Q2 30.4/16 = $1.900M; Q3 16.9/10 = $1.690M; Q4 54.3/30 = $1.810M.
8. Difference: 1.810 − 1.775 = $0.035M = $35,000.

minimal_documents: D04, D07, D09 (D04 Q1 revenue via 44.6 − 30.4, Q2 revenue and count; D07 Q3 count and revenue; D09 Q4 revenue/count and the 2025 total). D07 irreplaceable. D01 or D02 can substitute for D04 as the Q1 revenue source; D05 for D04's Q2 revenue; D04 still needed for the Q2 count and the 29 cumulative.

readings: (a) D09's rounded "$54 million" for Q4 → 54/30 = $1.800M → $25,000; footnote's $54.3M is more precise, so prefer $35,000. (b) Misreading the 13 cumulative infusions through Q1 as Q1-only gives Q1 = 14.2/13 ≈ $1.092M, making Q3 the fewest → 1.81 − 1.69 = $120,000; not defensible because D04 explicitly says "since launch" (includes 2024). (c) Deriving Q4 as full-year $116M minus nine-month $61.5M = $54.5M → difference ≈ $42,000; mixes rounded and exact figures, not preferred.

gaps: Q1 2025 infusions derived (8), not stated. Text extractions only. Read coverage: D01 full; D04 L1–130 + hits; D07 L1–80 + hits; D09 L1–95, L215–254; D02 L1–85, L212–231; D05 L1–80, L228–249; D03, D06, D08 search only. Some long forward-looking-statement lines unread. question.txt not opened.

contaminated: no

## Solve 3: $35,000 (right), confidence high

answer: $35,000 (Q1 2025, 8 infusions = fewest: ~$1,775,000 per infused patient; Q4 2025, 30 infusions = most: ~$1,810,000 per infused patient)

confidence: high

path:
1. Q2 2025 infusions = 16 — D04 L72: "29 patients have received infusions of CASGEVY, including 16 infused in the second quarter of 2025."
2. Q3 2025 infusions = 10 — D07 L74: "39 people with SCD or TDT have received infusions of CASGEVY, including 10 people infused in the third quarter of 2025."
3. Q4 2025 and full-year infusions = 30 and 64 — D09 L83: "This reflects 64 patients receiving infusions of CASGEVY in 2025, including 30 people infused in the fourth quarter of 2025."
4. Q1 2025 infusions not stated in any document (searched "infus", "dosed", "treated", "cell collection", "first quarter of 2025" across all nine; D01 L76 gives only first cell collections, "approximately 90 patients have had their first cell collection"). Derived: 64 − 16 − 10 − 30 = 8. Cross-check: 29 (to Jun 30) + 10 = 39 (to Sep 30); 39 + 30 = 69 since launch → 69 − 64 = 5 pre-2025; cumulative to Mar 31 = 29 − 16 = 13 = 5 + 8 ✓. Ranking: Q1 = 8 (fewest), Q3 = 10, Q2 = 16, Q4 = 30 (most).
5. Quarterly CASGEVY revenue ($M, footnotes): Q1 = 14.2 (D01 L255; D02 L224 prior-year comparative); Q2 = 30.4 (D04 L243 three/six months 30.4/44.6, giving Q1 = 44.6 − 30.4 = 14.2; D05 L240 repeats); Q3 = 16.9 (D07 L227, 16.9/61.5); Q4 = 54.3 (D09 L248 "$54.3 million and $115.8 million from CASGEVY"; headline D09 L83 rounds to "$54 million"/"$116 million"). Check: 14.2+30.4+16.9+54.3 = 115.8 ✓.
6. Q1: 14.2M / 8 = $1,775,000. Q4: 54.3M / 30 = $1,810,000. Difference: $35,000 lower. Decisive figures also verified in the original docs/ files.

minimal_documents: D04, D07, D09 (Q1 revenue from D04 by subtraction; D01 or D02 can substitute as a direct Q1 revenue source; D05 can replace D04 for Q2/H1 revenue but not the Q2 count). None of D03, D06, D08 needed.

readings: (a) Using only directly reported quarters (Q2–Q4), treating Q3 as fewest → 1,810,000 − 1,690,000 = $120,000; misses the Q1 figure derivable from D09's 64-patient total. (b) Using the rounded headline Q4 revenue of $54M → $25,000 (or $110,000 combined with (a)); inferior because the footnote prints $54.3M and the question asks the nearest thousand. Precision caveat: Q1 revenue printed only to $0.1M, so the true Q1 per-patient value is known only within about ±$6,250; with printed figures the answer is $35,000.

gaps: Q1 2025 infusions derived (8); no 2024 infusion count printed (D06 L83 "the first patient infused" in Q3 2024; D08 cell collections only). Coverage: CASGEVY sections and revenue tables of D01, D02, D04, D05, D07, D09 and D08's CASGEVY section read in full; D03 and D06 by keyword search; not every line of every document read. Text extractions only; no extraction problems seen.

contaminated: no
