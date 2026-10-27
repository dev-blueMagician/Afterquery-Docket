# i02 strong-solver screen: raw returns (2026-10-18)

Three fresh blind-solver contexts (claude-opus-5-5, effort max), each given only the workspace root,
the packet path runs/i02-screen-a0319ffaebc350b2/solver-1 and the exact sentence. Gold: $1,833,000.
Returns kept verbatim in substance (harness indentation removed), numbered by launch label (arrival order: 3, 2, 1).

## Solve 1: $1,833,000 (right), confidence high

answer: $1,833,000 (≈ $1.83 million per infused patient) — $71.5M of CASGEVY revenue from launch through Sept 30, 2025 ÷ 39 patients infused.

confidence: high

path:
1. Patients infused — D07 (CASGEVY highlights, L74): "Globally, since launch through September 30th, 2025, approximately 165 people with SCD or TDT have had their first cell collection for CASGEVY, including 50 people in the third quarter of 2025; and 39 people with SCD or TDT have received infusions of CASGEVY, including 10 people infused in the third quarter of 2025." → divisor 39 (165 = cell collections, not infusions, excluded).
2. 2025 revenue (9 months) — D07 (Total Revenues footnote 1, L227): "In the three and nine months ended September 30, 2025, "Other product revenues" included $16.9 million and $61.5 million from CASGEVY, respectively … In the three and nine months ended September 30, 2024, "Other product revenues" included $2.0 million from CASGEVY" → 9M 2025 = $61.5M; all of 9M 2024 = $2.0M (so nothing in H1 2024).
3. 2024 revenue — D08 (footnote 1, L272): "The three and twelve month periods ending December 31, 2024, included CASGEVY revenue of $8.0 million and $10.0 million, respectively." D09 footnote 1 (L248) repeats "$8.0 million and $10.0 million from CASGEVY" → FY2024 = $10.0M.
4. Revenue starts Q3 2024 — D06 L83: "In the third quarter of 2024, Vertex's product revenue included revenue from the first patient infused with CASGEVY." D04 L243: "In the three and six months ended June 30, 2024, there were no revenues for these products." D01 L255: "In the first quarter of 2024, there were no revenues for these products." D03's H1 2024 product revenue table (L259-264) has only TRIKAFTA/KAFTRIO and "Other CF products".
5. Cross-checks — quarter by quarter: Q3'24 $2.0M (D07) + Q4'24 $8.0M (D08/D09) + Q1'25 $14.2M (D01; D02 L224) + Q2'25 $30.4M (D04; D05 L240) + Q3'25 $16.9M (D07) = $71.5M. D09 footnote: FY2025 $115.8M − Q4'25 $54.3M = $61.5M ✓. Infusions: D04 L72 29 through June 30, 2025 + D07's 10 in Q3 = 39 ✓; D09 L83 64 in 2025 incl. 30 in Q4 → 34 in 9M 2025 → 5 infused before 2025 (39 − 34), consistent.
6. Calculation: $10.0M + $61.5M = $71.5M; $71.5M / 39 = $1,833,333.33 → $1,833,000.

minimal_documents: D07 + D08, or D07 + D09 (either supplies FY2024 $10.0M). D07 is irreplaceable (the only cumulative infusion count through Sept 30, 2025 / the Q3 2025 count of 10; D04 + D09 cannot recover it because the pre-2025/Q1 2025 split is missing elsewhere). D07 alone is insufficient: it omits Q4 2024 ($8.0M).

readings: Using D09's rounded narrative ($116M − $54M + $10M = $72M) → $72M/39 = $1,846,000 (exact footnote figures available; ranked lower). Excluding 2024 revenue ($61.5M/39) → $1,577,000 (inconsistent with "from launch"). 2025-only for both ($61.5M/34) → $1,809,000 (different window). Sensitivity: inputs rounded to $0.1M, true value could differ by roughly ±$1–3K; on reported figures $1,833,000.

gaps: No 2023 data in the packet; zero CASGEVY revenue before Q3 2024 inferred from D06's "first patient infused" and the explicit "no revenues" statements for Q1/H1 2024 (D01, D04). Text-method sources only (no PDF pages or layout files); needed tables/footnotes looked intact. D07 and D09 read in full; D01-D06 and D08 searched (CASGEVY, infusion, revenue, "since launch") and matching sections/tables read; forward-looking boilerplate not read line by line.

contaminated: no

## Solve 2: $1,833,000 (right), confidence high

answer: $1,833,000 (cumulative CASGEVY revenue of $71.5 million ÷ 39 patients infused = $1,833,333 → $1,833,000)

confidence: high

path:
1. Patients infused — D07 (Q3 2025 release) L74: "Globally, since launch through September 30th, 2025, … 39 people with SCD or TDT have received infusions of CASGEVY, including 10 people infused in the third quarter of 2025." Corroborated by D04 L72: "29 patients have received infusions of CASGEVY, including 16 infused in the second quarter of 2025" (through June 30, 2025); 29 + 10 = 39.
2. 2025 nine-month revenue — D07 footnote 1 (L227): "In the three and nine months ended September 30, 2025, 'Other product revenues' included $16.9 million and $61.5 million from CASGEVY". Same footnote gives "$2.0 million from CASGEVY" for both the three and nine months ended September 30, 2024 (so none in H1 2024). Cross-check: Q1 2025 $14.2M (D01 L255; D02 L224) + Q2 2025 $30.4M (D04 L243; D05 L240) + Q3 2025 $16.9M = $61.5M; D09 L248: FY2025 $115.8M − Q4 2025 $54.3M = $61.5M.
3. 2024 revenue — D08 L272: "The three and twelve month periods ending December 31, 2024, included CASGEVY revenue of $8.0 million and $10.0 million, respectively." D09 L248 repeats $8.0M/$10.0M. Q3 2024 $2.0M + Q4 2024 $8.0M = $10.0M.
4. Revenue start — D06 L83: "In the third quarter of 2024, Vertex's product revenue included revenue from the first patient infused with CASGEVY." D04 L243: "In the three and six months ended June 30, 2024, there were no revenues for these products." D08 attributes CASGEVY revenue only to 2024 periods (none in 2023). So since-launch revenue spans Q3 2024–Q3 2025.
5. Cumulative revenue: $10.0M + $61.5M = $71.5M (= 2.0 + 8.0 + 14.2 + 30.4 + 16.9).
6. $71,500,000 / 39 = $1,833,333.33 → nearest thousand $1,833,000 (39 × 1,833,000 = 71,487,000; 39 × 1,834,000 = 71,526,000).
7. Consistency check on patients: D09 L83 "64 patients receiving infusions of CASGEVY in 2025, including 30 people infused in the fourth quarter" → 34 in 9M 2025 → 39 − 34 = 5 infused in 2024 ($10.0M / 5 = $2.0M each, consistent with the single first patient in Q3 2024 at $2.0M).

minimal_documents: D07 + D08 (D09 substitutes for D08: L248 also gives FY2024 $10.0M). D06/D04 optional support that revenue began Q3 2024; D01, D02, D05 only repeat quarterly figures.

readings: Rounded D09 headline figures ($116M − $54M + $10M = $72M)/39 = $1,846,000 — less precise; exact footnotes give $71.5M. Wrong window, 2025 revenue only: $61.5M/39 = $1,577,000 (omits 2024 revenue). 2025-only both: $61.5M/34 = $1,809,000 (contradicts "from launch"). The primary reading ($1,833,000) is the only one consistent with the question.

gaps: No document states cumulative since-launch revenue directly (summed from periods). No explicit "$0 CASGEVY revenue in 2023" — rests on D06's "first patient infused" in Q3 2024 and D08 footnoting CASGEVY only for 2024 periods. Read in full: D07; partial: D08 L1-100, L245-280; D06 L1-90, L244-268; D09 L1-90, L225-254; D03 L250-274; D01, D02, D05 CASGEVY sections; D04 and the rest of D01-D05 by search only; docs/ originals not opened; text-only sources.

contaminated: no

## Solve 3: $1,833,000 (right), confidence high

answer: $1,833,000 per patient ($71.5 million ÷ 39 patients = $1,833,333 → nearest thousand)

confidence: high

path:
1. Patients infused from launch through 9/30/2025 — D07 (Q3 2025 release), L74: "Globally, since launch through September 30th, 2025, approximately 165 people with SCD or TDT have had their first cell collection for CASGEVY … and 39 people with SCD or TDT have received infusions of CASGEVY, including 10 people infused in the third quarter of 2025." ("approximately" applies to the 165 collections; infusions = 39.) Cross-check: D04 L72 "since launch through June 30th, 2025 … 29 patients have received infusions," and 29 + 10 = 39. D09 L83: "64 patients receiving infusions of CASGEVY in 2025, including 30 people infused in the fourth quarter" → 2025 through Q3 = 34 → 5 infused in 2024 (consistent).
2. 2025 CASGEVY revenue through Q3 — D07 L227, footnote 1: "In the three and nine months ended September 30, 2025, 'Other product revenues' included $16.9 million and $61.5 million from CASGEVY." Cross-check: D09 L248 "$54.3 million and $115.8 million from CASGEVY" (Q4/FY2025) → 115.8 − 54.3 = 61.5 ✓. Quarterly: D01 L255 Q1 2025 $14.2M; D04 L243 Q2 2025 $30.4M (H1 $44.6M); 14.2 + 30.4 + 16.9 = 61.5 ✓.
3. 2024 CASGEVY revenue — D08 L272: "The three and twelve month periods ending December 31, 2024, included CASGEVY revenue of $8.0 million and $10.0 million, respectively." (D09 L248 repeats $8.0M/$10.0M.) D07 L227: nine months ended 9/30/2024 "$2.0 million from CASGEVY" → Q3 2024 = $2.0M, Q4 = $8.0M.
4. No revenue before Q3 2024 — D06 L83: "In the third quarter of 2024, Vertex's product revenue included revenue from the first patient infused with CASGEVY." D01 L255: "In the first quarter of 2024, there were no revenues for these products." D04 L243: "In the three and six months ended June 30, 2024, there were no revenues for these products." → FY2024 $10.0M is all revenue from launch through 12/31/2024 (none in 2023).
5. Calculation — cumulative revenue = 10.0 + 61.5 = $71.5M (quarterly: 2.0 + 8.0 + 14.2 + 30.4 + 16.9 = 71.5). $71,500,000 / 39 = $1,833,333.33 → $1,833,000. (Check: 39 × 1,833,333.33 = 71,500,000.) No document states a cumulative since-launch revenue figure directly (searched "since launch", "cumulative", "to date").

minimal_documents: D07 + D08 (D09 can replace D08 — it also gives FY2024 = $10.0M — and its FY2025/Q4 2025 figures corroborate $61.5M). D07 indispensable: the only document with the since-launch infusion count through 9/30/2025 (39), not reconstructible from D04/D09 because the Q1 2025 count is missing. D06/D01/D04 only corroborate zero pre-Q3 2024 revenue.

readings: Precise footnote figures, launch through Q3 2025 → $1,833,000 (primary). Rounded D09 text figures ("$54 million", "$116 million") → 2025 through Q3 = $62M; +$10M = $72M; 72/39 = $1,846,000 (less defensible since precise $115.8M/$54.3M and $61.5M are printed). 2025-only revenue over 2025-only infusions: 61.5/34 = $1,809,000 (doesn't match "from launch"). Excluding Q4 2024, i.e. (2.0 + 61.5)/39 = $1,628,000 — not a defensible reading.

gaps: Nothing in the packet ties the 39 infusions to revenue one-for-one (e.g., whether any infusions were non-revenue such as early-access); the question says to divide regardless. Packet is text extractions only (method "text", no page markers, layouts or PDFs); decisive footnotes extracted cleanly. D02, D03, D05 checked only by searches for CASGEVY/revenue/infusion/since-launch terms, not read in full; their CASGEVY table rows (D02 L224 Q1 2025 = 14.2; D05 L240 Q2 2025 = 30.4, H1 2025 = 44.6) agree. Long forward-looking-statement lines omitted from search output (e.g., D07 L347/351) not opened.

contaminated: no
