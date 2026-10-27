# aq-06835 - document map

Maintained by the caller from `text/` (and `docs/` for layout issues).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

## Bundle

- What it is: nine Form 8-K Ex. 99.1 earnings releases, three per company: Stryker, Zimmer Biomet (ZB),
  Edwards Lifesciences, each for 4Q/FY 2025, 1Q 2026 and 2Q 2026. All three companies report on calendar years.
- Documents: 9; local ids are alphabetical by filename (text/manifest.json), not the task page's Doc numbers:
  D01 Edwards 1Q26 (page Doc 8), D02 Edwards 2Q26 (Doc 9), D03 Edwards 4Q/FY25 (Doc 7), D04 Stryker 1Q26
  (Doc 2), D05 Stryker 2Q26 (Doc 3), D06 Stryker 4Q/FY25 (Doc 1), D07 ZB 1Q26 (Doc 5), D08 ZB 2Q26 (Doc 6),
  D09 ZB 4Q/FY25 (Doc 4).
- Gaps: none. Plain-text capture, "9 of 9 read in full (310,707 characters)"; every document read in full by
  the caller on 2026-10-18. Page note at capture: "Docket has been updated. Reload this page..."
- Extraction spot-checks: text/ equals docs/ apart from the header line (plain text in, plain text out);
  tables are pipe tables. Checked: D06 segment table and supplemental tables, D05 note under the sales table,
  D08 six-month statements against D07 + D08 quarters (sums agree to 0.1), D03 special-item prose.
- Provenance: notes/intake.json (capture AQ-06835_2026-10-18_1759.txt, every source matches the capture).
- Reuse binding: miner corpus sha256 aabcf00c51945bb1 (notes/mine.md).

## Stryker (D06 FY25, D04 1Q26, D05 2Q26) - $ millions, integers

- D06: Q4 and FY 2025 (and 2024) statements; FY-only cash flow (no Q4 cash flow); segment table (MedSurg and
  Neurotechnology 4,562 / 15,647; Orthopaedics 2,609 / 9,469) and supplemental product lines on the 2025
  structure: Instruments 925 / 3,183, Endoscopy, Medical, Vascular, Neuro Cranial 669 / 2,485; Knees, Hips,
  Trauma and Extremities, Other 267 / 815, subtotal, Spinal Implants 8 / 185. Non-GAAP reconciliations Q4 and FY.
  2026 outlook: organic growth 8.0%-9.5%, adjusted EPS $14.90-$15.10.
- D04: Q1 2026 and Q1 2025. l.32 announces the Ortho Tech reorganization and "Prior period segment information
  has been recast"; l.205 note gives the bridge for Q1 2026 / Q1 2025: Orthopaedic Instruments 489 / 484 and
  Other Orthopaedics 157 / 133 inside Ortho Tech; Neuro Cranial 606 / 563 and Enabling Technologies 26 / 29 inside
  Instruments. Cyber incident first reported March 11, 2026.
- D05: Q2 and six months 2026 / 2025; cash flow six months only. Sales table by business with US/International;
  l.222 note: three-month and six-month bridge (OI 523 / 501 and 1,012 / 985; OO 194 / 148 and 351 / 281;
  NC 681 / 616 and 1,287 / 1,179; ET 28 / 34 and 54 / 63). New reconciliation row "Reversal of 2025 tariffs"
  (gross profit (158)). Q2 2025 "Adjusted percent net sales" gross profit printed 65.4% although 3,934 / 6,022 is
  65.3%. Outlook narrowed: organic 8.3%-9.3%, adjusted EPS $14.95-$15.10.

## Zimmer Biomet (D09 FY25, D07 1Q26, D08 2Q26) - $ millions, one decimal

- Sales tables print current-period sales and % changes only; prior-year category sales are not printed
  (only consolidated prior-year figures in the statements).
- D09: Q4 and FY statements; FY cash flow; Q4 and FY free cash flow, gross profit and operating profit
  reconciliations (adjusted gross margin 72.4% Q4, 72.2% FY; operating profit margin 6.9% Q4). Note (1): E&O
  inventory charges on lines to be discontinued $159.2M Q4, $162.1M FY. Note (4): contingent-consideration gains
  $14.3M Q4, $77.1M FY. Guidance (Feb): reported revenue change 2.5%-4.5%, FX +0.50%, CC 2.0%-4.0%, organic
  1.0%-3.0%, adjusted EPS $8.30-$8.45. $250M buyback in Q4; new $1.5B authorization from Feb 9, 2026.
- D07: Q1 2026 / Q1 2025 statements and reconciliations; l.202 goodwill-impairment caveat (initial assessment of
  no Q1 charge; D08's six-month figures equal Q1 + Q2, so none was added). Guidance (Apr): EPS raised to
  $8.40-$8.55, revenue lines unchanged.
- D08: Q2 and six months 2026 / 2025 statements; cash flow six months only; FCF Q2 and six months. Note (1): E&O
  "impacts" income $3.9M Q2 2026, expense $3.0M Q2 2025; six months income $2.6M / expense $5.6M (wording changed
  from "charges on" to "impacts to"). Guidance (Aug): reported 3.9%-4.9%, CC 3.4%-4.4%, organic 2.25%-3.25%
  (Paragon 28 about 110bps), adjusted EPS $8.47-$8.59; buyback expectation up to $1B for 2026.

## Edwards (D03 FY25, D01 1Q26, D02 2Q26) - $ millions, one decimal

- No cash flow statement in any release; cash and debt only as "approximately" prose.
- D03: Q4 and FY 2025 statements (lines "Intellectual property agreement and certain litigation expenses",
  "Intangible assets impairment charges" 40.0 FY, "Loss on impairment" 99.8 Q4 / 146.9 FY); special items by
  quarter in prose l.177-197 (litigation 10.9/15.5/90.4/208.6; intangible impairment $40.0M Q3 2025; loss on
  impairment $47.1M Q2 2025 and $99.8M Q4 2025, JenaValve; contingent-consideration gain $12.5M Q3 2025). Sales by
  product group and region, Q4 and YTD; IHFM note (A). Q1 2026 projection: sales $1.55-$1.63B, adjusted EPS
  $0.70-$0.76. Tax effects "based upon the items' actual effect" (D01/D02 say "forecasted").
- D01: Q1 2026 / Q1 2025; loss on impairment $123.6M (VIE investment), remeasurement gain $65.2M; TMTT headline
  $173M excludes $2.0M IHFM (table 175.1); Surgical includes $3.0M TSA revenue. Outlook: CC growth 9%-11%, total
  sales $6.5-$6.9B, TAVR $4.7-$5.0B; Q2 projection $1.66-$1.74B, adjusted EPS $0.70-$0.76. $500M ASR.
- D02: Q2 and six months; loss on impairment $40.0M Q2 (option on a VIE not exercised), remeasurement gain $19.9M,
  $188.2M California R&D-credit valuation allowance (Q2 GAAP tax rate 53.6%). Outlook: CC growth 10%-11%, total
  sales $6.6-$6.9B, TAVR $4.75-$5.0B, TMTT $760-$780M; Q3 projection $1.63-$1.71B, adjusted EPS $0.71-$0.77.

## Shared ground (navigation only)

- Third quarter 2025 is printed in no release for any company: FY (D06/D09/D03) less Q4 (same) less six months
  2025 (D05/D08/D02).
- Stryker's 2025 product lines appear on two structures: D06 (2025 structure) and D04/D05 (recast); only the
  D04/D05 notes bridge them, for Q1, Q2 and six months.
- Guidance editions: three per company (Jan/Feb, Apr, Jul/Aug 2026). Edwards prints quarterly sales projections
  (Q1 in D03, Q2 in D01, Q3 in D02); actuals follow in the next release.
