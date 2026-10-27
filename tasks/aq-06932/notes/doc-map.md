# aq-06932 - document map

Navigation only, from `text/` (read in full, 2026-10-19). Questions quote the documents, never this map.
Line references are `text/Dnn.txt` lines (each line holds a whole page section; long).

## Bundle

- What it is: four Rio Tinto quarterly operations reviews (6-K exhibit 99.1), Q3 2025 to Q2 2026.
- Documents (local id = task-page Doc): D03 = Doc 1 Q3 2025 (14 Oct 2025); D04 = Doc 2 Q4 2025 (21 Jan 2026);
  D01 = Doc 3 Q1 2026 (21 Apr 2026); D02 = Doc 4 Q2 2026 (15 Jul 2026).
- Gaps: none. Capture "4 of 4 read in full"; page notice "Docket has been updated. Reload this page" carried from the capture.
- Extraction spot-checks: plain-text captures; each document's summary table, a detailed share table and its
  footnotes compared with the capture (identical bytes, `matches_capture: true`). Italics that mark revised
  figures ("figures in italics indicate adjustments") are lost in text: revisions show only by comparing editions.
- Provenance: notes/intake.json (capture sha256 c79efd25...); corpus sha256 99bae91d0d0f3815 (notes/mine.md).

## Each document (same layout in all four)

Sections: 1 Executive summary with headline table (L3); 2 guidance; 3 group update (exploration expense);
4 markets and index prices; 5-8 product sections (iron ore, aluminium & lithium, copper, borates/TiO2);
9-10 capital and future projects; 11 exploration; 12 releases; then "Rio Tinto share of production" tables
and "Rio Tinto operational data" (100% basis unless stated). Columns: five quarters plus YTD pairs
(D03: Q3 2024-Q3 2025, 9M 2024, 9M 2025; D04: Q4 2024-Q4 2025, FY 2024, FY 2025; D01: Q1 2025-Q1 2026;
D02: Q2 2025-Q2 2026, H1 2025, H1 2026). Q3 2024 appears only in D03; 9M 2024 only in D03; FY 2024 only in D04.

## Definition changes and restatements (locations)

- Iron ore sales/shipments: 2025 reviews print "Iron Ore Shipments" and a different "Iron Ore Sales (d) Include
  Pilbara and IOC sales adjusted for portside trading movements and third party volumes sold" (D03 L65, D04 L67).
  2026 reviews print only "Sales" with the shipments values (D01 L65 note (f), D02 L67-69 note (g)); 2025 note (c)
  "Shipments includes material shipped to our portside trading facility..." becomes "Sales includes ...".
- Simandou: D04 L43/L51 iron ore production "excludes Simandou production in 2025"; D01 L49 and D02 L51 restate
  Q4 2025 Rio Tinto iron ore production to 80,515 (D04 79,492) and global 95,670 (D04 93,399); D01 L13 "recorded
  for the first time in Q4 2025". Simandou share 45% (53% of SimFer Jersey x 85%).
- QAL alumina: 2025 at 80%; from 2026 at 100% (D04 L17 note; D01 L3 note 6, L15; D02 L3 note 6, L17). 2025 not restated.
- Bauxite third-party shipments: D02 L17/L61 restates 2025 and Q1 2026 (reclassification + 3% humidity).
- Lithium: Q1 2025 full quarter 17/17.2 kt (D03, D04, D01) vs post-acquisition 5.6 kt; D02 prints H1 2025 = 17.8
  (post-acquisition) and also "YTD: down by 7% YoY" (L21). D04 L19: "of the 57kt LCE production in 2025, 46kt was
  attributable to Rio Tinto".
- Pilbara realised price: D04 L9 H1 2025 82.5 / H2 2025 83.1 / FY 82.8 / 2024 89.6 $/wmt; D02 L9 H1 2026 85.2 /
  H1 2025 83.2, note 1 "excludes the impact of certain joint venture arrangements. Including these, ... $1.1/wmt lower
  (H1 2025, $0.7/wmt)".
- Iron ore index: 62% Fe in 2025, 61% from 2026 (D01 L9 restates Q4 2025 average 106 -> 103; D02 H1 2025 left at 62%).

## Other cross-period series

- Tariffs (RTA US-bound): D04 L19 H1/H2/FY 2025; D01 L15 adds Q4 2025 and Q1 2026; D02 L17 H1 2026.
- Exploration and evaluation expense: Q1 2025 141 (D01 L5), H1 2025 334 (D02 L5), 9M 2025 537 / 9M 2024 692 (D03 L5),
  FY 2025 795 / FY 2024 935 (D04 L5), Q1 2026 180, H1 2026 480.
- Kennecott cathode from purchased concentrate (excluded from production): Q3 2025 15.5 (34.9 YTD), Q4 2025 4 (39 FY),
  Q1 2026 7, Q2 2026 13.
- Guidance editions: 2025 (D03 L3/L5; D04 L3) and 2026 (D04 L5; D01 L3; D02 L3).
