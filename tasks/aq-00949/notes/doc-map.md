# aq-00949 - document map

Written once by `bundle-mapper` from `text/` (and `docs/` for flattened tables and scans).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

Re-mapped 2026-10-05 after the complete re-ingest (capture c0774ce9..., "7 of 7 captured in full")
and the splitter fix that removed a stray metadata first line from D06/D07. Every line of
text/D02, D04, D05, D06 and D07 was read; D01 and D03 are byte-identical to the first map and were
spot-checked. All line numbers are current text/Dnn.txt line numbers (D06/D07 after the fix).
Values are copied as printed; parentheses = negative, "—" = printed dash. "a / b" separates
columns as noted. This file holds facts and locations only: no questions, answers, decoys or
difficulty claims.

## Bundle

- What it is: seven EX-99.1 exhibits of EOG Resources, Inc. Two press releases: D01 (March 16,
  2020, 2020 capital-plan cut) and D03 (May 30, 2025, Encino acquisition agreement + dividend
  declaration). Five editions of the quarterly "Supplemental Financial and Operating Data": D02
  1Q 2025, D04 2Q 2025, D05 3Q 2025, D06 1Q 2026, D07 2Q 2026. Quarterly columns span 1Q 2024 -
  2Q 2026; balance-sheet dates Mar 31 2024 - Jun 30 2026; annual columns FY 2021 - FY 2025. D01
  adds December 31, 2019 balance figures and the 2020 plan.
- Documents: 7, D01-D07 from text/manifest.json. Local ids equal platform Doc 1-7 per the
  extraction report (intake.json numbers 1-7 map to the same file names); not re-checked against
  the capture's "### Doc N" headings here.
- Gaps (no gap remains inside the readable source text):
  - Hidden-text markers: none. Grep for "characters not shown" returns 0 hits in text/ and docs/
    (hits exist only in old runs/ packets copied from the clipped capture; see Provenance). The
    old map's hidden-marker table is withdrawn.
  - Each series file starts at its Table of Contents (printed page 12, 12, 11, 9, 9). The
    earnings-release pages before it are not in any file. G&A "Certain Items" labels cite
    earnings-release endnotes (D04 881, D05 904, D06 875, D07 877) that are absent. No narrative
    results, guidance tables or closing announcements are in the series files.
  - No 4Q 2024 or 4Q 2025 edition is in the bundle; those quarters appear only as comparative
    columns (4Q24 in D02/D04/D05; 4Q25 in D06/D07).
  - No 2019 or 2020 actual operating or financial results anywhere. Earliest actual columns:
    FY 2021 (D06/D07 annual CFO/FCF, per-Boe and AKFI tables) and 1Q 2024 (D02 quarterly). D01
    gives Dec 31, 2019 balances only.
  - No pages, scans or charts: all seven sources are .txt (method "text", pages null). Visual
    checks: not applicable. Tables are flattened markdown with blank header rows; column
    assignment follows the preceding text headers (documented per section) and ties
    arithmetically.
  - Not opened by the mapper: the capture files D:\Dev\Docket\AQ-00949_2026-10-06_0251.md
    (current) and AQ-00949_2026-10-05_2020.md (old), including any bundle-overview text they
    hold. Overview exposure remains a sketch-time check.
- Extraction spot-checks (re-ingested corpus):
  - Page count: not applicable (text sources). Printed page markers run in sequence with no
    missing number in every series file (D02 12-35, D04 12-37, D05 11-36, D06 9-29, D07 9-29;
    locations in each section).
  - One table row and one footnote per document, text/ versus docs/ original (text line = docs
    line + 2 because of the "# Dnn | path" header): D02 765 / 224 = docs 763 / 222; D04 282 / 354
    = docs 280 / 352; D05 280 / 165 = docs 278 / 163; D06 286 / 236 = docs 284 / 234; D07 762 / 166
    = docs 760 / 164; D01 table values 21,641 and (2,028 at text 163 / 171 = docs 161 / 169. D01
    and D03 footnotes: not applicable (no footnotes). D03 table: not applicable.
  - The docs/ originals of D06 and D07 contain no "tokens ·" / "quotes found" metadata line.
- Provenance: notes/intake.json schema 1; capture sha256
  c0774ce9149c2a43628de606ecaddf2d4fbdeb9b1f9ed97bdc98a9b9b2beac7c ("7 of 7 captured in full").
  All 7 documents incomplete = false, gap_characters = 0, matches_capture = true, and
  captured_sha256 = source_sha256 = manifest sha256. Current hashes: D01 7b2406b8..., D02
  5bc99544..., D03 21b89e5d..., D04 68f243ce..., D05 c591c318..., D06 9327b6cd... (59,242
  chars), D07 5f6c76d4... (60,423 chars).
  - History (two prior entries): (1) c669ef05... clipped capture: D02/D04/D05/D06/D07 incomplete
    with 13,732 / 14,927 / 14,811 / 13,638 / 14,191 gap characters; (2) c0774ce9... first split of
    the complete capture, where D06 (83e1b3e3...) and D07 (d0d94cc3...) still began with a stray
    page-metadata line ("17,678 tokens · 53,814 characters · 2/2 quotes found" / "18,184 tokens ·
    54,668 characters · 4/4 quotes found"). The splitter fix removed that line and re-split
    D06/D07, lowering every D06/D07 line number by 2. D01 and D03 hashes are identical in all
    three entries.
  - Old run packets runs/q01-r0-*, runs/q01-r1-* and runs/q02-r0-* still hold the clipped texts
    (marker hits per packet copy: 37/42/40/38/38); they predate the re-ingest.

## Mapping ledger (final)

| Doc | Lines (current file) | Read | Remaining |
|---|---|---|---|
| D01 | 1-201 | 1-201 (first map; byte-identical; references spot-checked 2026-10-05) | none |
| D02 | 1-1067 | 1-260, 261-520, 521-800, 801-1067 | none |
| D03 | 1-213 | 1-213 (first map; byte-identical; references spot-checked 2026-10-05) | none |
| D04 | 1-1193 | 1-300, 301-600, 601-900, 901-1193 | none |
| D05 | 1-1216 | 1-310, 311-610, 611-910, 911-1216 | none |
| D06 | 1-1205 (after splitter fix) | 1-320, 321-620, 621-920, 921-1205 | none |
| D07 | 1-1207 (after splitter fix) | 1-320, 321-620, 621-920, 921-1207 | none |

Coverage is complete for every readable line. No continuation chunk is pending.

## Series layout shared by D02, D04, D05, D06, D07

Common header: "EX-99.1", file name, "EXHIBIT 99.1", then the "Table of Contents" for the
"<Nth> Quarter <YYYY> Supplemental Financial and Operating Data". Issuer: EOG Resources, Inc.;
no person is named and no issue date is printed (the date comes only from the file name). Fiscal
year = calendar year ("twelve months ended December 31, 2024", D02 545; 10-K "fiscal year ended
December 31", D01 113 / D03 203). Labels: statement tables "1st Qtr ... 4th Qtr, Year"; Adjusted
NI and bridges "1Q 2025", "FY 2024"; balance sheets "MAR JUN SEP DEC"; net debt "March 31, 2025";
AKFI "2024 Actual". Each edition's current-year "Year" column holds year-to-date values (D02 1Q;
D04 H1; D05 9M; D06 FY 2025 plus 2026 Q1; D07 H1 2026).

Section line ranges (current files):

| Section | D02 | D04 | D05 | D06 | D07 |
|---|---|---|---|---|---|
| Table of Contents | 13-41 | 11-41 | 13-43 | 13-43 | 13-43 |
| Income Statements | 43-89 | 43-89 | 45-91 | 45-91 | 45-91 |
| Volumes and Prices | 91-160 | 91-160 | 93-169 | 93-174 | 93-172 |
| Balance Sheets | 162-226 | 162-226 | 171-235 | 176-240 | 174-238 |
| Cash Flow Statements | 228-293 | 228-294 | 237-304 | 242-310 | 240-308 |
| Non-GAAP Financial Measures + Direct ATROR | 295-313 | 296-314 | 306-324 | 312-330 | 310-328 |
| Adjusted Net Income | 315-582 | 316-586 | 326-599 | 332-590 | 330-590 |
| Net Income Per Share (bridge) | 584-649 | 588-653 | 601-666 | 592-651 | 592-649 |
| Adjusted Net Income Per Share (bridge) | 651-717 | 655-721 | 668-735 | 653-712 | 651-710 |
| Cash Flow from Operations and Free Cash Flow | 719-816 | 723-825 | 737-848 | 714-819 | 712-821 |
| Net Debt-to-Total Capitalization Ratio | 818-839 | 827-848 | 850-871 | 821-842 | 823-844 |
| Revenues, Costs and Margins Per Boe | 841-1067 | 850-1083 | 873-1106 | 844-1080 | 846-1082 |
| Additional Key Financial Information (AKFI) | absent | 1085-1193 | 1108-1216 | 1082-1205 | 1084-1207 |

Table rows present in every edition (values per document section): income-statement revenue
and expense lines through Net Income, "Dividends Declared per Common Share", EPS and share
counts; crude, NGL and natural-gas volumes and prices, crude oil equivalent volumes (MBoed) and
Total MMBoe; every balance-sheet row; cash-flow statement rows (non-cash items, working capital,
investing, financing, cash roll-forward); complete Adjusted NI tables with totals for every
period; complete bridges (prices, volumes, certain operating costs per Boe, MTM or settlements,
Other); CFO/FCF with working-capital and capex reconciling rows; net-debt components; per-Boe
volume (a), (b)-(d), revenue by product, cost lines and all ratios; AKFI volumes, prices,
differentials, realizations, unit costs, expenses, TOTI and tax rows.

Per-Boe composition (row letters as printed; sums verified on the printed figures): (a) Volume
MMBoe; (b) Total Operating Revenues and Other; (c) Total Operating Expenses; (d) Operating
Income; (e) total revenues from sales of crude oil and condensate, NGLs and natural gas. The cost
lines listed under "Operating Costs" (Lease and Well, GP&T, G&A, TOTI and Interest Expense, Net)
sum to (f) GAAP / (g) Non-GAAP (e.g. D02 868-883: 401 + 440 + 171 + 341 + 47 = 1,400); (h)/(i) add
DD&A; (j)/(k) add Total Exploration Costs (Exploration + Dry Hole + Impairments; Non-GAAP less
Certain Impairments). Ratios divide by (a); margins equal (e)/(a) minus the cost per Boe.

Standing definitions repeated in all five editions (locations):
- BOE ratio "1.0 barrel of crude oil and condensate or NGLs to 6.0 thousand cubic feet of natural
  gas" and the MMBoe method (D02 158, D04 158, D05 167, D06 172, D07 170).
- Free Cash Flow = CFO before changes in working capital (D02 723) or Adjusted CFO (D04 727, D05
  741, D06 718, D07 716) less Total Capital Expenditures (Non-GAAP).
- Net debt "(b) / [(a) + (b)]" and "(c) / [(a) + (c)]"; "A portion of the cash is associated with
  international subsidiaries; tax considerations may impact debt paydown" (D02 822, D04 831, D05
  854, D06 825, D07 827).
- Adjusted NI method (D02 319, D04 320, D05 330, D06 336, D07 334): reflects net cash from
  derivative settlements, removes unrealized MTM and asset-disposition gains/losses, adds back
  certain impairments; D05+ add "to add back costs associated with the Encino acquisition".
- Impairment exclusion (i) commodity-price declines, (ii) property sales, (iii) other events or
  decisions: "from total exploration costs" in per-Boe footnotes (D02 1061, D04 1075, D05 1104,
  D06 1078, D07 1080); "from total impairment costs" in AKFI endnotes (D04 1191, D05 1214, D06
  1201, D07 1203).
- GP&T combined "Effective January 1, 2024 ... no impact on previously reported Net Income" (D02
  1059; D04 1073, 1187; D05 1096, 1210; D06 1070, 1197; D07 1072, 1199).
- Direct ATROR short form (D02 311, D04 312, D05 322, D06 328, D07 326).
- Bridges impute income tax "based on 22%".

## D01 - EOG Resources Updates 2020 Capital Plan; Premium Strategy Proves Resilient at Low Oil Prices

- Source: docs/eog_ex991_2020-03-16.txt | text, no pages. text/D01.txt has 201 lines and 16,784 chars;
  "EX-99.1", file "exh99-1031620.htm" (line 5), "PRESS RELEASE OF EOG RESOURCES, INC." (7).
  Byte-identical across the 2026-10-05 re-ingest; line references below were spot-checked
  against the current file (13, 19, 33-49, 53, 59, 83, 91, 145-201).
- Written or submitted by: EOG Resources, Inc. (HOUSTON dateline, line 33).
- Type, date, edition: press release, Exhibit 99.1, dated "March 16, 2020" (13); headline 15.
- Period covered: full-year 2020 plan; balance data "At December 31, 2019" (155-157). Production
  is compared with "full-year 2019 levels" (35). 10-K "for the fiscal year ended December 31, 2019"
  (113, 119): fiscal year = calendar year.
- Entities and aliases: EOG Resources, Inc. = "EOG" (33) = "NYSE: EOG" (49). William R. "Bill"
  Thomas, Chairman and Chief Executive Officer (39; "said Thomas" 43). Investor Contacts: David
  Streit 713-571-4902, Neel Panchal 713-571-4884. "Media and Investor Contact": Kimberly Ehmer
  713-571-4676 (51-59). Other names: SEC (117); Delaware Basin and South Texas Eagle Ford (37).
  Proved reserves are "in the United States, Trinidad, and China" (49).
- Tables: "Reconciliation of Net Debt and Total Capitalization" 145-201 ("Unaudited; in millions,
  except ratio data", at December 31, 2019; each label line is followed by its value line).
  Total Stockholders' Equity (a) $21,641 (159/163); Current and Long-Term Debt (GAAP) (b) 5,175
  (165/167); Less: Cash (2,028) (169/171); Net Debt (Non-GAAP) (c) 3,147 (175/177); Total
  Capitalization (GAAP) $26,816 (179/183); Total Capitalization (Non-GAAP) $24,788 (185/189);
  Debt-to-Total Capitalization (GAAP) 19% (191/193); Net Debt-to-Total Capitalization (Non-GAAP)
  13% (197/199). ATROR graphic text 121-143 (non-numeric box).
- Lists: 4 headline bullets (17-31). 24 risk-factor bullets (63-113), the last being Item 1A
  "on pages 13 through 23" of the 10-K for FY 2019. 14 forward-looking cue words (61): "expect" ...
  "believe". The ATROR box (127-143) lists 2 included cost bases and 2 excluded indirect-capital
  items.
- Forecasts, guidance, deadlines, effective dates:
  - 2020 exploration and development expenditures "now expected to range from $4.3 billion to
    $4.7 billion". They include "facilities and gathering, processing and other expenditures" and
    exclude "acquisitions and non-cash exchanges" (35).
  - Headline: "Reduces 2020 Capital Plan 31% to $4.3 to $4.7 Billion and Targets Flat YoY Crude Oil
    Production Volumes" (19). The pre-cut plan amount is not stated anywhere in the bundle.
  - Full-year 2020 crude oil production of "446,000 to 466,000 barrels of oil per day,
    approximately flat compared to full-year 2019 levels" (35). The 2019 level is not stated.
  - Net cash from operating activities "is expected to fund both capital expenditures and
    dividend payments assuming mid-$30 oil prices for the remainder of 2020" (35).
  - "With oil around $30 our 2020 premium drilling program is expected to generate more than 30%
    direct after-tax rate of return" (39).
  - A fuller update is planned "with the release of its first quarter 2020 results" (45); that
    release is not in the bundle.
- Hedged claims:
  - Line 35: "expected to range" attaches to the capex range. "is expected to fund ... assuming
    mid-$30 oil prices" attaches to the funding claim and adds a price condition. "supports ...
    approximately flat" attaches to the production comparison.
  - Line 39: "is expected to generate more than 30%" attaches to the ATROR claim.
  - Headline bullets 19-31 state the same items without hedge words ("Revised Plan Generates
    Strong Returns at $30 Oil Price"; "Funded with Net Cash from Operating Activities at Mid-$30
    Oil Prices").
  - Line 153: "tax considerations may impact debt paydown" ("may" attaches to the effect of tax on
    paydown). "EOG believes this presentation may be useful".
- Rounded prose beside exact figures: line 41 says total debt "$5.2 billion" (table 5,175), cash
  "$2.0 billion" (table 2,028), "19 percent" and "13 percent" (table 19% and 13%, whole percents).
- Notes:
  - Actual actions versus plans: "EOG has elected to reduce activity across its operating areas"
    (37, decision taken); "The company plans to focus its drilling operations in the Delaware
    Basin and South Texas Eagle Ford" (37, plan).
  - The printed text says "fourth-party-operated" (83) and "(by EOG or fourth parties)" (91),
    where D03 prints "third-party-operated" (151) and "third parties" (167).
  - Safe harbor cites "Section 27A of the Securities Act of 1933" and "Section 21E of the Securities
    Exchange Act of 1934" (61). Line 61 names forward-looking non-GAAP measures "such as free cash
    flow or discretionary cash flow".
- Operative definitions, rules and scope exceptions:
  - Direct ATROR long form (123-125): "based on the estimated recoverable reserves ("net" to EOG's
    interest) for all wells in such play or such well ..., the estimated net present value (NPV)
    ... and our direct net costs incurred in drilling or acquiring ... cannot be calculated from
    our consolidated financial statements".
  - ATROR box (127-143): "Based on Cash Flow and Time Value of Money"; "Excludes Indirect Capital
    - Gathering and Processing and other Midstream - Land, Seismic, Geological and Geophysical";
    "Payback ~12 Months on 100% Direct ATROR Wells"; "First Five Years ~1/2 Estimated Ultimate
    Recovery Produced but ~3/4 of NPV Captured".
  - Net debt formulas 191, 197. Capex scope 35 (see Forecasts).
  - SEC reserve categories "proved", "probable" and "possible" are defined (117).
- Amendments or contradictions: D01 revises an earlier 2020 capital plan that is not in the bundle.
  The "About EOG" reserve countries (US, Trinidad, China; 49) differ from D03 63 (US and Trinidad).
  The two documents carry different dates, and no document states a change.
- Coverage: full; lines 1-201 read (first map); byte-identical file, references spot-checked after
  the re-ingest. No hidden markers in either capture.

## D02 - First Quarter 2025 Supplemental Financial and Operating Data

- Source: docs/eog_ex991_2025-05-01.txt | text, no pages. text/D02.txt has 1,067 lines and 48,738
  chars (manifest). "EX-99.1" (3), "2 exh99-1050125.htm" (5), "PRESS RELEASE OF EOG RESOURCES,
  INC." (7), "EXHIBIT 99.1" (11). Printed page numbers 12-35 run in sequence (12 at 41, 13 at 89,
  14 at 160, 15 at 226, 16 at 293, 17 at 313, 18-24 at 351/390/431/470/509/547/582, 25 at 625,
  26 at 649, 27 at 690, 28 at 717, 29 at 769, 30 at 816, 31 at 839, 32 at 903, 33 at 949, 34 at
  1013, 35 at 1067).
- Written or submitted by: EOG Resources, Inc. No person is named.
- Type, date, edition: series edition "First Quarter 2025 Supplemental Financial and Operating
  Data" (15); no printed issue date (file name 2025-05-01). TOC 13-39 has 11 entries (Income
  Statements 13 ... Revenues, Costs and Margins Per Barrel of Oil Equivalent 32); no AKFI.
- Period covered and column convention:
  - Statement tables print text headers "2024 2025" and "1st Qtr 2nd Qtr 3rd Qtr 4th Qtr Year 1st
    Qtr ... Year" (45-47, 95-97, 232-234, 725-727, 754-756); the markdown tables below them have an
    empty header row and 7 value columns = 2024 Q1, Q2, Q3, Q4, 2024 Year, 2025 Q1, 2025 Year (the
    empty 2025 Q2-Q4 columns are omitted; 2025 Year = 1Q25). Balance sheet: header "MAR JUN SEP DEC
    MAR JUN SEP DEC" (168) over 5 value columns = Mar 2024, Jun 2024, Sep 2024, Dec 2024, Mar 2025.
    Column assignment is inferred from these headers; quarter sums tie to the Year column (e.g.
    NI 1,789+1,690+1,673+1,251 = 6,403).
  - Adjusted NI tables: 1Q25, 4Q24, 3Q24, 2Q24, 1Q24, FY24, FY23. Bridges 4Q24 -> 1Q25. Annual
    CFO/FCF: FY2023, FY2022. Net debt: Mar 31 2025, Dec 31 2024, Sep 30 2024, Jun 30 2024, Mar 31
    2024. Per-Boe quarterly 1Q25, 4Q24, 3Q24, 2Q24, 1Q24; annual 2024, 2023, 2022.
  - Fiscal year = calendar year ("twelve months ended December 31, 2024", 545). Price footnote
    cites Note 10 of the 10-Q "for the quarterly period ended March 31, 2025" (156).
- Entities and aliases: EOG. Geographies: United States and Trinidad only (no Other International
  rows). Non-GAAP names (297): "Adjusted Net Income (Loss), Cash Flow from Operations Before
  Changes in Working Capital, Free Cash Flow, Net Debt and related statistics". No mention of
  Encino.
- Tables (USD millions unless stated; columns per the convention above):
  - Income Statements 43-87 ("In millions of USD, except share data (in millions) and per share
    data (Unaudited)", 45):
    - Operating Revenues and Other (49-60): Crude Oil and Condensate 3,480 3,692 3,488 3,261 /
      13,921 / 3,293 (53); Natural Gas Liquids 513 515 524 554 / 2,106 / 572 (54); Natural Gas 382
      303 372 494 / 1,551 / 637 (55); Gains (Losses) on Mark-to-Market Financial Commodity and
      Other Derivative Contracts, Net 237 (47) 79 (65) / 204 / (191) (56); Gathering, Processing
      and Marketing 1,459 1,519 1,481 1,341 / 5,800 / 1,340 (57); Gains (Losses) on Asset
      Dispositions, Net 26 20 (7) (23) / 16 / (1) (58); Other, Net 26 23 28 23 / 100 / 19 (59);
      Total 6,123 6,025 5,965 5,585 / 23,698 / 5,669 (60).
    - Operating Expenses (62-75): Lease and Well 396 390 392 394 / 1,572 / 401 (66); Gathering,
      Processing and Transportation Costs 413 423 445 441 / 1,722 / 440 (67); Exploration Costs 45
      34 43 52 / 174 / 41 (68); Dry Hole Costs 1 5 — 8 / 14 / 34 (69); Impairments 19 81 15 276 /
      391 / 44 (70); Marketing Costs 1,404 1,490 1,500 1,323 / 5,717 / 1,325 (71); Depreciation,
      Depletion and Amortization 1,074 984 1,031 1,019 / 4,108 / 1,013 (72); General and
      Administrative 162 151 167 189 / 669 / 171 (73); Taxes Other Than Income 338 337 283 291 /
      1,249 / 341 (74); Total 3,852 3,895 3,876 3,993 / 15,616 / 3,810 (75).
    - Operating Income 2,271 2,130 2,089 1,592 / 8,082 / 1,859 (76); Other Income, Net 62 66 76
      70 / 274 / 65 (77); Income Before Interest Expense and Income Taxes 2,333 2,196 2,165 1,662 /
      8,356 / 1,924 (78); Interest Expense, Net 33 36 31 38 / 138 / 47 (79); Income Before Income
      Taxes 2,300 2,160 2,134 1,624 / 8,218 / 1,877 (80); Income Tax Provision 511 470 461 373 /
      1,815 / 414 (81); Net Income 1,789 1,690 1,673 1,251 / 6,403 / 1,463 (82).
    - "Dividends Declared per Common Share" 0.9100 0.9100 0.9100 0.9750 / 3.7050 / 0.9750 (83;
      dollars, four decimals).
    - Line 87 (one flattened line): EPS Basic 3.11 2.97 2.97 2.25 / 11.31 / 2.66; Diluted 3.10
      2.95 2.95 2.23 / 11.25 / 2.65; Average shares Basic 575 569 564 557 / 566 / 550; Diluted 577
      572 568 561 / 569 / 553.
  - Volumes and Prices 91-158 ("(Unaudited)"; units in footnote (A) 154: MBbld or MMcfd; (B) 156:
    $/Bbl or $/Mcf, excluding derivatives):
    - Crude volumes (MBbld) (99-106): US 486.8 490.1 491.8 493.5 / 490.6 / 500.9 (102); Trinidad
      0.6 0.6 1.2 1.1 / 0.8 / 1.2 (103); Total 487.4 490.7 493.0 494.6 / 491.4 / 502.1 (106).
    - Crude prices (108-113): US 78.46 82.71 76.95 71.68 / 77.42 / 72.90; Trinidad 67.50 70.75
      63.15 60.47 / 64.43 / 61.12; Composite 78.45 82.69 76.92 71.66 / 77.40 / 72.87.
    - NGL volumes (116-120): US = Total 231.7 244.8 254.3 252.5 / 245.9 / 241.7. NGL prices
      (122-126): US = Composite 24.32 23.11 22.42 23.85 / 23.40 / 26.29.
    - Natural Gas Volumes (MMcfd) (129-135): US 1,658 1,668 1,745 1,840 / 1,728 / 1,834 (133);
      Trinidad 200 204 225 252 / 220 / 246 (134); Total 1,858 1,872 1,970 2,092 / 1,948 / 2,080
      (135).
    - Gas prices (137-142): US 2.10 1.57 1.84 2.39 / 1.99 / 3.36; Trinidad 3.54 3.48 3.68 3.86 /
      3.65 / 3.78; Composite 2.26 1.78 2.05 2.57 / 2.17 / 3.41.
    - Crude Oil Equivalent Volumes (MBoed) (C) (145-152): US 994.7 1,013.0 1,037.1 1,052.7 /
      1,024.5 / 1,048.3 (149); Trinidad 34.1 34.5 38.6 43.0 / 37.6 / 42.1 (150); Total 1,028.8
      1,047.5 1,075.7 1,095.7 / 1,062.1 / 1,090.4 (151); "Total MMBoe (C)" 93.6 95.3 99.0 100.8 /
      388.7 / 98.1 (152).
    - Footnote (C) 158: BOE ratio 1.0 barrel to 6.0 Mcf; "MMBoe is calculated by multiplying the
      MBoed amount by the number of days in the period and then dividing that amount by one
      thousand".
  - Balance Sheets 162-224 ("In millions of USD (Unaudited)"; Mar24 Jun24 Sep24 Dec24 Mar25):
    - Current Assets (170-179): Cash and Cash Equivalents 5,292 5,431 6,122 7,092 6,599 (174);
      Accounts Receivable, Net 2,688 2,657 2,545 2,650 2,621 (175); Inventories 1,154 1,069 1,038
      985 897 (176); Assets from Price Risk Management Activities 110 4 — — — (177); Other (A) 684
      642 460 503 563 (178); Total 9,928 9,803 10,165 11,230 10,680 (179).
    - Property, Plant and Equipment (181-192): Oil and Gas Properties (Successful Efforts Method)
      73,356 74,615 75,887 77,091 78,432 (185); Other PP&E 5,768 6,078 6,314 6,418 6,510 (186);
      Total PP&E 79,124 80,693 82,201 83,509 84,942 (187); Less: Accumulated DD&A (46,047)
      (47,049) (48,075) (49,297) (50,310) (188); Total PP&E, Net 33,077 33,644 34,126 34,212
      34,632 (189); Deferred Income Taxes 38 44 42 39 44 (190); Other Assets 1,753 1,733 1,818
      1,705 1,626 (191); Total Assets 44,796 45,224 46,151 47,186 46,982 (192).
    - Current Liabilities (194-205): Accounts Payable 2,389 2,436 2,290 2,464 2,353 (198);
      Accrued Taxes Payable 786 600 855 1,007 668 (199); Dividends Payable 523 516 513 539 534
      (200); Liabilities from Price Risk Management Activities — 8 32 116 276 (201); Current
      Portion of Long-Term Debt 34 534 34 532 1,280 (202); Current Portion of Operating Lease
      Liabilities 318 303 338 315 318 (203); Other 223 231 344 381 290 (204); Total 4,273 4,628
      4,406 5,354 5,719 (205).
    - Long-Term Debt 3,757 3,250 3,742 4,220 3,464 (206); Other Liabilities 2,533 2,456 2,480
      2,395 2,368 (207); Deferred Income Taxes 5,597 5,731 5,949 5,866 5,915 (208).
      "Commitments and Contingencies" (210) carries no footnote letter here.
    - Stockholders' Equity (212-222): Common Stock, $0.01 Par 206 (all five, 216); Additional
      Paid in Capital 6,188 6,219 6,058 6,090 6,095 (217); Accumulated Other Comprehensive Loss
      (8) (8) (9) (4) (4) (218); Retained Earnings 23,897 25,071 26,231 26,941 27,869 (219); Common
      Stock Held in Treasury (1,647) (2,329) (2,912) (3,882) (4,650) (220); Total Stockholders'
      Equity 28,636 29,159 29,574 29,351 29,516 (221); Total Liabilities and Stockholders' Equity
      44,796 45,224 46,151 47,186 46,982 (222).
    - Footnote (A) 224: "Effective October 1, 2024, EOG combined Income Taxes Receivable into the
      Other line item. This presentation has been conformed for all periods presented and had no
      impact on previously reported Total Assets."
  - Cash Flow Statements 228-291 ("In millions of USD (Unaudited)"):
    - Line 240 (flattened): Net Income 1,789 1,690 1,673 1,251 / 6,403 / 1,463.
    - Items Not Requiring (Providing) Cash (242-252): DD&A 1,074 984 1,031 1,019 / 4,108 / 1,013
      (244); Impairments 19 81 15 276 / 391 / 44 (245); Stock-Based Compensation Expenses 45 45 58
      51 / 199 / 50 (246); Deferred Income Taxes 199 128 220 (80) / 467 / 44 (247); (Gains) Losses
      on Asset Dispositions, Net (26) (20) 7 23 / (16) / 1 (248); Other, Net 9 3 2 3 / 17 / 11
      (249); Dry Hole Costs 1 5 — 8 / 14 / 34 (250); Mark-to-Market ... (Gains) Losses, Net (237)
      47 (79) 65 / (204) / 191 (251); Net Cash Received from (Payments for) Settlements of
      Financial Commodity Derivative Contracts 55 79 61 19 / 214 / (38) (252).
    - Changes in Components of Working Capital and Other Assets and Liabilities (254-264):
      Accounts Receivable 58 33 109 (99) / 101 / 48 (258); Inventories 117 75 30 37 / 259 / 76
      (259); Accounts Payable (58) 29 (159) 152 / (36) / (129) (260); Accrued Taxes Payable 319
      (185) 256 151 / 541 / (339) (261); Other Assets (161) 42 197 (34) / 44 / (43) (262); Other
      Liabilities (71) (20) 108 6 / 23 / (96) (263); Changes in Components of Working Capital
      Associated with Investing Activities (229) (127) 59 (85) / (382) / (41) (264).
    - Net Cash Provided by Operating Activities 2,903 2,889 3,588 2,763 / 12,143 / 2,289 (265).
    - Investing Cash Flows (267-275): Additions to Oil and Gas Properties (1,485) (1,357) (1,263)
      (1,248) / (5,353) / (1,381) (271); Additions to Other Property, Plant and Equipment (350)
      (313) (239) (117) / (1,019) / (102) (272); Proceeds from Sales of Assets 9 10 — 4 / 23 / 12
      (273); Changes in Components of Working Capital Associated with Investing Activities 229 127
      (59) 85 / 382 / 41 (274); Net Cash Used in Investing Activities (1,597) (1,533) (1,561)
      (1,276) / (5,967) / (1,430) (275). No acquisition row in D02.
    - Financing Cash Flows (277-287): Long-Term Debt Borrowings — — — 985 / 985 / — (281);
      Dividends Paid (525) (520) (533) (509) / (2,087) / (538) (282); Treasury Stock Purchased
      (759) (699) (795) (993) / (3,246) / (806) (283); Proceeds from Stock Options Exercised and
      Employee Stock Purchase Plan — 11 — 11 / 22 / — (284); Debt Issuance Costs — — — (2) / (2) /
      — (285); Repayment of Finance Lease Liabilities (8) (9) (8) (8) / (33) / (8) (286); Net Cash
      Used in Financing Activities (1,292) (1,217) (1,336) (516) / (4,361) / (1,352) (287). No
      debt-repayment row in D02.
    - Effect of Exchange Rate Changes on Cash — – – (1) / (1) / — (288; the 2Q24 and 3Q24 cells
      print an en dash "–", the others an em dash "—"); Increase (Decrease) in Cash 14 139 691 970
      / 1,814 / (493) (289); Cash at Beginning of Period 5,278 5,292 5,431 6,122 / 5,278 / 7,092
      (290); Cash at End of Period 5,292 5,431 6,122 7,092 / 7,092 / 6,599 (291).
  - Non-GAAP Financial Measures 295-311 (boilerplate; Direct ATROR short form 309-311).
  - Adjusted Net Income 315-580. Columns: Before Tax / Income Tax Impact / After Tax / Diluted
    Earnings per Share. Method paragraph 319. Each table ends with average shares and footnote (1)
    restating the before-tax settlement amount. All seven tables are complete:
    - 1Q25 (321-349): Reported 1,877 (414) 1,463 2.65 (329); "Losses on Mark-to-Market ..." 191
      (41) 150 0.26 (333); "Net Cash Payments for Settlements ..." (38) 8 (30) (0.05) (335); "Add:
      Losses on Asset Dispositions, Net" 1 2 3 0.01 (339; tax impact printed as positive 2);
      Adjustments to Net Income 154 (31) 123 0.22 (340); Adjusted Net Income (Non-GAAP) 2,031 (445)
      1,586 2.87 (341); shares 550/553 (345/347); "$38 million" (349).
    - 4Q24 (359-388): Reported 1,624 (373) 1,251 2.23; Losses MTM 65 (14) 51 0.10; Net Cash
      Received 19 (4) 15 0.03; Add: Losses on Asset Dispositions 23 (4) 19 0.03 (377); Add:
      Certain Impairments 254 (55) 199 0.35 (378); Adjustments 361 (77) 284 0.51 (379); Adjusted NI
      1,985 (450) 1,535 2.74 (380); 557/561; "$19 million" (388).
    - 3Q24 (398-429): Reported 2,134 (461) 1,673 2.95; Gains MTM (79) 17 (62) (0.11); Received 61
      (13) 48 0.08; Add: Losses on Asset Dispositions 7 (2) 5 0.01 (416); "Less: Severance Tax
      Refund" (31) 7 (24) (0.04) (417); "Add: Severance Tax Consulting Fees" 10 (2) 8 0.01 (418);
      "Less: Interest on Severance Tax Refund" (5) 1 (4) (0.01) (419); Adjustments (37) 8 (29)
      (0.06) (420); Adjusted NI 2,097 (453) 1,644 2.89 (421); 564/568; "$61 million" (429).
    - 2Q24 (439-468): Reported 2,160 (470) 1,690 2.95; Losses MTM 47 (10) 37 0.07; Received 79 (17)
      62 0.11; "Less: Gains on Asset Dispositions, Net" (20) 5 (15) (0.03) (457); Add: Certain
      Impairments 35 (2) 33 0.06 (458); Adjustments 141 (24) 117 0.21 (459); Adjusted NI 2,301
      (494) 1,807 3.16 (460); 569/572; "$79 million" (468).
    - 1Q24 (478-507): Reported 2,300 (511) 1,789 3.10; Gains MTM (237) 51 (186) (0.31); Received
      55 (12) 43 0.07; Less: Gains on Asset Dispositions (26) 4 (22) (0.04) (496); Add: Certain
      Impairments 2 — 2 — (497); Adjustments (206) 43 (163) (0.28) (498); Adjusted NI 2,094 (468)
      1,626 2.82 (499); 575/577; "$55 million" (507).
    - FY24 (515-545): Reported 8,218 (1,815) 6,403 11.25 (523); Gains MTM (204) 44 (160) (0.28);
      Received 214 (46) 168 0.30; Less: Gains on Asset Dispositions (16) 3 (13) (0.02) (531); Add:
      Certain Impairments 291 (57) 234 0.41 (532); Less: Severance Tax Refund (31) 7 (24) (0.04)
      (533); Add: Severance Tax Consulting Fees 10 (2) 8 0.01 (534); Less: Interest on Severance
      Tax Refund (5) 1 (4) (0.01) (535); Adjustments 259 (50) 209 0.37 (536); Adjusted NI 8,477
      (1,865) 6,612 11.62 (537); 566/569; "$214 million" (545).
    - FY23 (553-580): Reported 9,689 (2,095) 7,594 13.00 (561); "Gains on Mark-to-Market Financial
      Commodity Derivative Contracts, Net" (no "and Other") (818) 176 (642) (1.09) (563); Net Cash
      Payments (112) 24 (88) (0.15) (565); Less: Gains on Asset Dispositions (95) 20 (75) (0.13)
      (569); Add: Certain Impairments 42 (6) 36 0.06 (570); Adjustments (983) 214 (769) (1.31)
      (571); Adjusted NI 8,706 (1,881) 6,825 11.69 (572); 581/584; "$112 million" (580).
  - Net Income per Share bridge 584-647 (4Q24 -> 1Q25): start 2.23 (588). Prices 45.88 less
    (42.74) = 3.14 x 98.1 = 308; tax (68); NI 240; EPS 0.43 (592-598). Volumes 98.1 less (100.8) =
    (2.7) x GAAP margin 20.09 = (54); tax 12; NI (42); EPS (0.08) (602-610). Certain Operating
    Costs per Boe: "4Q 2024 Total Cash Operating Costs (GAAP) and Total DD&A per Boe 20.26" (614);
    less 1Q25 (20.63); subtotal (0.37) x 98.1 = (36); tax 8; NI (28); EPS (0.05) (616-623). MTM 1Q25
    (191)/41/(150) less 4Q24 (65)/14/(51); change (99); EPS (0.18) (633-639). Other (1) 0.30 (641);
    1Q25 diluted 2.65 (643); 553 shares (645). Footnote (1) 647 lists "gains (losses) on asset
    dispositions" among the Other items.
  - Adjusted NI per Share bridge 651-715: start 4Q24 adjusted 2.74 (655). Prices and volumes as
    above (Non-GAAP margin 20.09, 671). Costs: "4Q 2024 Total Cash Operating Costs (Non-GAAP) and
    Total DD&A per Boe 20.26" (679), less (20.63), (0.37), (36), 8, (28), (0.05) (681-688).
    Settlements 1Q25 (38)/8/(30) less 4Q24 19/(4)/15; change (45); EPS (0.08) (698-707). Other (1)
    (0.09) (709); "1Q 2025 Adjusted Net Income per Share (Non-GAAP) 2.87" (711). Footnote 715 omits
    asset dispositions.
  - Cash Flow from Operations and Free Cash Flow 719-814:
    - Paragraph 723: reconciles NCFO (GAAP) to "Cash Flow from Operations Before Changes in Working
      Capital (Non-GAAP)"; FCF = that measure "less the Total Capital Expenditures (Non-GAAP)".
    - NCFO 2,903 2,889 3,588 2,763 / 12,143 / 2,289 (729). Working-capital adjustments (735-743):
      AR (58) (33) (109) 99 / (101) / (48); Inventories (117) (75) (30) (37) / (259) / (76); AP 58
      (29) 159 (152) / 36 / 129; Accrued Taxes Payable (319) 185 (256) (151) / (541) / 339; Other
      Assets 161 (42) (197) 34 / (44) / 43; Other Liabilities 71 20 (108) (6) / (23) / 96; WC
      associated with investing 229 127 (59) 85 / 382 / 41.
    - "Cash Flow from Operations Before Changes in Working Capital (Non-GAAP)" 2,928 3,042 2,988
      2,635 / 11,593 / 2,813 (744). Total Capital Expenditures (Non-GAAP) (1,703) (1,668) (1,497)
      (1,358) / (6,226) / (1,484) (748). Free Cash Flow 1,225 1,374 1,491 1,277 / 5,367 / 1,329
      (750).
    - Reconciliation (752-767): Total Expenditures (GAAP) 1,952 1,682 1,573 1,446 / 6,653 / 1,546
      (758); Asset Retirement Costs (21) 60 (11) (26) / 2 / (13) (762); "Non-Cash Acquisition
      Costs of Unproved Properties" (31) (34) (17) (3) / (85) / (9) (763); "Acquisition Costs of
      Proved Properties" (21) (5) — (7) / (33) / 1 (764); "Acquisition Costs of Other Property,
      Plant and Equipment" (131) (1) (5) — / (137) / — (765); Exploration Costs (45) (34) (43) (52)
      / (174) / (41) (766); Total Capital Expenditures (Non-GAAP) 1,703 1,668 1,497 1,358 / 6,226 /
      1,484 (767).
    - FY2023 / FY2022 (771-814): NCFO 11,340 / 11,093 (777); AR 38 / 347; Inventories 231 / 534;
      AP 119 / (90); Accrued Taxes Payable (61) / 113; Other Assets (39) / 364; Other Liabilities
      (184) / 266; WC investing (295) / (375) (785-791); CFO Before Changes in WC 11,149 / 12,252
      (792); capex (6,041) / (4,607) (796); FCF 5,108 / 7,645 (798); Total Expenditures 6,818 /
      5,610 (802); ARC (257) / (298); Non-Cash Development Drilling (90) / —; Non-Cash Acquisition
      Costs of Unproved Properties (99) / (127); Acquisition Costs of Proved Properties (16) /
      (419); Acquisition Costs of Other PP&E (134) / —; Exploration Costs (181) / (159); Total
      Capex 6,041 / 4,607 (808-814).
  - Net Debt-to-Total Capitalization 818-837 (dates Mar 31 2025, Dec 31 2024, Sep 30 2024, Jun 30
    2024, Mar 31 2024; 824): Total Stockholders' Equity (a) 29,516 29,351 29,574 29,159 28,636
    (828); Current and Long-Term Debt (GAAP) (b) 4,744 4,752 3,776 3,784 3,791 (829); Less: Cash
    (6,599) (7,092) (6,122) (5,431) (5,292) (830); Net Debt (c) (1,855) (2,340) (2,346) (1,647)
    (1,501) (831); Total Capitalization (GAAP) 34,260 34,103 33,350 32,943 32,427 (832); Total
    Capitalization (Non-GAAP) 27,661 27,011 27,228 27,512 27,135 (833); Debt-to-Total Cap (GAAP)
    13.8% 13.9% 11.3% 11.5% 11.7% (835); Net Debt-to-Total Cap (Non-GAAP) -6.7% -8.7% -8.6% -6.0%
    -5.5% (837). Debt (b) equals balance-sheet current portion + long-term debt (202 + 206).
  - Revenues, Costs and Margins Per Boe, quarterly 841-947 (1Q25 4Q24 3Q24 2Q24 1Q24; "In millions
    of USD, except Boe and per Boe amounts", 843):
    - Volume MMBoe (a) 98.1 100.8 99.0 95.3 93.6 (851); Total Operating Revenues and Other (b)
      5,669 5,585 5,965 6,025 6,123 (852); Total Operating Expenses (c) 3,810 3,993 3,876 3,895
      3,852 (853); Operating Income (d) 1,859 1,592 2,089 2,130 2,271 (854).
    - Revenues by product (858-862): Crude 3,293 3,261 3,488 3,692 3,480; NGLs 572 554 524 515
      513; Natural Gas 637 494 372 303 382. (e) 4,502 4,309 4,384 4,510 4,375 (864).
    - Lease and Well 401 394 392 390 396 (868); GP&T (1) 440 441 445 423 413 (870); G&A (GAAP) 171
      189 167 151 162 and "Less: Severance Tax Consulting Fees" — — (10) — — (872); G&A (Non-GAAP)
      (3) 171 189 157 151 162 (874); TOTI (GAAP) 341 291 283 337 338 and "Add: Severance Tax
      Refund" — — 31 — — (876); TOTI (Non-GAAP) (4) 341 291 314 337 338 (878).
    - Interest Expense, Net 47 38 31 36 33 (882; included in (f)); (f) 1,400 1,353 1,318 1,337
      1,342 (883); (g) 1,400 1,353 1,339 1,337 1,342 (884); DD&A 1,013 1,019 1,031 984 1,074 (885);
      (h) 2,413 2,372 2,349 2,321 2,416 (886); (i) 2,413 2,372 2,370 2,321 2,416 (887);
      Exploration Costs 41 52 43 34 45; Dry Hole 34 8 — 5 1; Impairments 44 276 15 81 19; Total
      Exploration Costs (GAAP) 119 336 58 120 65 (888-891); "Less: Certain Impairments (2)" —
      (254) — (35) (2) (893); Total Exploration Costs (Non-GAAP) 119 82 58 85 63 (897); (j) 2,532
      2,708 2,407 2,441 2,481 (898); (k) 2,532 2,454 2,428 2,406 2,479 (899).
    - Revenues less cost incl. exploration (901): GAAP 1,970 1,601 1,977 2,069 1,894; Non-GAAP
      1,970 1,855 1,956 2,104 1,896.
    - Per Boe GAAP (913-933): (b)/(a) 57.79 55.41 60.25 63.22 65.42; (c)/(a) 38.84 39.62 39.15
      40.87 41.16; (d)/(a) 18.95 15.79 21.10 22.35 24.26; (e)/(a) 45.88 42.74 44.31 47.31 46.73;
      (f)/(a) 14.26 13.42 13.32 14.03 14.33; margin 31.62 29.32 30.99 33.28 32.40; (h)/(a) 24.58
      23.53 23.74 24.35 25.80; margin 21.30 19.21 20.57 22.96 20.93; (j)/(a) 25.79 26.86 24.33
      25.61 26.49; margin 20.09 15.88 19.98 21.70 20.24.
    - Per Boe Non-GAAP (935-947): (g)/(a) 14.26 13.42 13.53 14.03 14.33; margin 31.62 29.32 30.78
      33.28 32.40; (i)/(a) 24.58 23.53 23.95 24.35 25.80; margin 21.30 19.21 20.36 22.96 20.93;
      (k)/(a) 25.79 24.34 24.54 25.24 26.47; margin 20.09 18.40 19.77 22.07 20.26.
  - Per Boe annual 951-1065 (2024 2023 2022):
    - (a) 388.7 359.4 331.5 (961); (b) 23,698 24,186 25,702; (c) 15,616 14,583 15,736; Operating
      Income (Loss) (d) 8,082 9,603 9,966 (962-964).
    - Crude 13,921 13,748 16,367; NGLs 2,106 1,884 2,648; Natural Gas 1,551 1,744 3,781 (970-972);
      (e) 17,578 17,376 22,796 (974).
    - L&W 1,572 1,454 1,331; GP&T 1,722 1,620 1,587; G&A 669 640 570 with "Less: Severance Tax
      Consulting Fees" (10) — (16) (982); G&A (Non-GAAP) 659 640 554; TOTI 1,249 1,284 1,585 with
      "Add: Severance Tax Refund" 31 — 115 (986); TOTI (Non-GAAP) 1,280 1,284 1,700 (978-988).
    - Interest Expense, Net 138 148 179 (992); (f) 5,350 5,146 5,252; (g) 5,371 5,146 5,351; DD&A
      4,108 3,492 3,542; (h) 9,458 8,638 8,794; (i) 9,479 8,638 8,893; Exploration 174 181 159; Dry
      Hole 14 1 45; Impairments 391 202 382; Total Exploration Costs (GAAP) 579 384 586
      (993-1001); Less: Certain Impairments (291) (42) (113) (1003); Total Exploration Costs
      (Non-GAAP) 288 342 473; (j) 10,037 9,022 9,380; (k) 9,767 8,980 9,366 (1007-1009).
    - Revenues less cost (1011): GAAP 7,541 8,354 13,416; Non-GAAP 7,811 8,396 13,430.
    - Per Boe GAAP (1027-1043): (b)/(a) 60.97 67.30 77.53; (c)/(a) 40.18 40.58 47.47; (d)/(a)
      20.79 26.72 30.06; (e)/(a) 45.22 48.34 68.77; (f) 13.76 14.31 15.84; margin 31.46 34.03
      52.93; (h) 24.33 24.03 26.53; margin 20.89 24.31 42.24; (j) 25.82 25.10 28.30; margin 19.40
      23.24 40.47.
    - Per Boe Non-GAAP (1047-1057): (g) 13.82 14.31 16.14; margin 31.40 34.03 52.63; (i) 24.39
      24.03 26.83; margin 20.83 24.31 41.94; (k) 25.13 24.98 28.26; margin 20.09 23.36 40.51.
    - Footnotes 1059-1065: (1) GP&T combination effective Jan 1, 2024; (2) impairment exclusion
      "from total exploration costs"; (3) G&A items non-recurring; (4) TOTI items non-recurring.
- Lists: 11 TOC entries. 7 Adjusted NI tables (last, FY23, 553-580). Adjustment-row sets as listed
  above (1Q25: MTM, settlements, asset dispositions; 4Q24 adds impairments; 3Q24 has three
  severance-tax rows). Bridge "Other (1)" footnotes 647 (GAAP, with asset dispositions) and 715
  (Non-GAAP, without).
- Forecasts, guidance, deadlines, effective dates: none forward-looking. Effective dates: Oct 1,
  2024 Income Taxes Receivable into Other (224); Jan 1, 2024 GP&T combination (1059).
- Hedged claims: boilerplate only: "may be useful" (301, 319, 723, 822, 845); "tax considerations
  may impact debt paydown" (822); "may include, but are not limited to" (297); "EOG may also change
  the calculation" (307).
- Rounded prose beside exact figures: none; no narrative results text. Adjusted NI footnotes (1)
  restate each settlement amount in dollars ("$38 million" etc.).
- Notes:
  - Settlement-row label and sign by period: "Net Cash Payments" 1Q25 and FY23 (footnote
    "subtracts ... total net cash paid"); "Net Cash Received" 1Q24-4Q24 and FY24 ("adds ... total
    net cash received").
  - MTM label: "Losses" 1Q25, 4Q24, 2Q24; "Gains" 3Q24, 1Q24, FY24, FY23.
  - The severance-tax items appear as three Adjusted NI rows (refund (31), consulting fees 10,
    interest on refund (5)) in 3Q24 and FY24, but only as two per-Boe rows (TOTI refund 31, G&A
    fees (10)); interest on the refund has no per-Boe row.
  - Asset-disposition sign pattern: income statement 26 20 (7) (23) / 16 (58) versus Adjusted NI
    "Less: Gains" 1Q24/2Q24/FY24 and "Add: Losses" 3Q24/4Q24/1Q25.
- Operative definitions: FCF (723); BOE conversion and MMBoe (158); per-Boe impairment exclusion
  (1061); G&A and TOTI items "non-recurring" (1063, 1065); Direct ATROR (311); net-debt formulas
  (829-837).
- Amendments or contradictions: two presentation changes, each "conformed for all periods
  presented" (224, 1059). No internal numeric conflict found: statement totals tie, balance-sheet
  debt and cash tie to the net-debt table, and per-Boe (a) equals the volume table's Total MMBoe.
- Coverage: full; every line 1-1067 read in four chunks (1-260, 261-520, 521-800, 801-1067). No
  hidden markers.

## D03 - EOG Resources to Acquire Encino Acquisition Partners from CPP Investments and Encino Energy, Strengthening Premier Utica Asset; Increases Regular Dividend 5%

- Source: docs/eog_ex991_2025-05-30.txt | text, no pages. text/D03.txt has 213 lines and 17,492 chars;
  file "d904377dex991.htm" (5); "Exhibit 99.1" (11). Byte-identical across the 2026-10-05
  re-ingest; line references below were spot-checked against the current file (19-75, 151, 167,
  203, 211).
- Written or submitted by: EOG Resources, Inc. (HOUSTON dateline 19). Quoted speaker: Ezra Y. Yacob,
  Chairman and Chief Executive Officer (21; "continued Yacob" 23).
- Type, date, edition: acquisition and dividend press release dated "May 30, 2025" (13); headline
  15-17 (the line break splits "EOG" / "Resources").
- Period covered: announcement date May 30, 2025. Later dates and periods referenced: 2025 EBITDA,
  CFO and FCF accretion; first-year synergies; dividend dates in October 2025; closing "in the
  second half of 2025"; the 10-K for the fiscal year ended December 31, 2024 (203, 211).
- Entities and aliases:
  - Encino Acquisition Partners = "EAP or Encino" (19); "the Transaction" = "the proposed
    acquisition of Encino/EAP" (77).
  - Sellers: Canada Pension Plan Investment Board = "CPP" (19) = "CPP Investments" (headline 17);
    and Encino Energy (separate seller; 17, 19).
  - Advisors (59): Goldman Sachs & Co. LLC ("exclusive financial advisor"); its affiliate Goldman
    Sachs Bank USA ("sole provider of fully committed financing"); Wachtell, Lipton, Rosen & Katz
    ("lead legal advisor"); Akin Gump Strauss Hauer & Feld LLP ("also serving as legal counsel").
  - Investor Contacts: Pearce Hammond 713-571-4684, Neel Panchal 713-571-4884, Shelby O'Connor
    713-571-4560. Media Contact: Kimberly Ehmer 713-571-4676 (65-75).
  - Plays: Utica, Delaware Basin, Eagle Ford (21). Hart-Scott-Rodino Act (49, 89). Proved
    reserves "in the United States and Trinidad" (63).
- Tables: none.
- Lists: 5 "Transaction Highlights" bullets (29-47). 30 risk-factor bullets (83-203); the first
  four are transaction-specific (85-97), and the last is Item 1A of the 10-K FY2024. 17
  forward-looking cue words (77) add "ambition", "initiative" and "focused on" to D01's set.
  4 advisor entities (59). Contacts: 3 investor + 1 media.
- Forecasts, guidance, deadlines, effective dates:
  - Price "$5.6 billion, inclusive of EAP's net debt"; "currently expects to fund the
    acquisition through $3.5 billion of debt and $2.1 billion of cash on hand" (19).
  - "accretive on an annualized basis to 2025 EBITDA by 10%, and cash flow from operations and
    free cash flow by 9%" (35).
  - "more than $150 million of synergies in the first year driven by lower capital, operating,
    and debt financing costs" (43).
  - Dividend: Board "today declared a dividend of $1.02 per share", "payable October 31, 2025, to
    stockholders of record as of October 17, 2025", "indicated annual rate is $4.08"; headline
    "Increases Regular Dividend 5%" (17, 47). D03 does not state the prior dividend amount (see
    Shared ground for the series' "Dividends Declared per Common Share" rows).
  - "long-term target of less than one times total debt-to-EBITDA ratio at bottom cycle prices of
    $45 WTI oil" (47).
  - Capital and volume guidance effects "will be provided after closing, which is expected to
    occur in the second half of 2025"; "subject to clearance under the Hart-Scott-Rodino Act and
    other customary closing conditions" (49).
  - Conference call "8 a.m. Central time (9 a.m. Eastern time) on Friday, May 30, 2025"; replay
    available "for one year" (55).
- Hedged claims:
  - "currently expects to fund" (19); "expects to generate more than $150 million" (43); "expects
    the acquisition will have no material impact" on the leverage target (47); "closing, which is
    expected to occur" (49). "will be a textbook example" (25) is a future-tense claim.
  - Stated without hedge words: "is immediately accretive to EOG's net asset value as well as all
    per-share financial metrics" (35, also 23); "Pro forma production totals 275,000 barrels of oil
    equivalent per day" (31); the acreage facts (31, 39).
  - Line 77 brands all transaction rationale and benefit statements as forward-looking.
- Rounded prose beside exact figures: "$5.6 billion" equals the "$3.5 billion" debt plus "$2.1 billion"
  cash (19). Approximate figures: "more than 12 billion barrels of oil equivalent net resource" (21);
  "more than two billion barrels oil equivalent of undeveloped net resource" (31); "more than 20%"
  working-interest increase (39); "averages 65% liquids production" (39).
- Notes (acreage item set, as stated):
  - "Encino's 675,000 net core acres" bring the Utica position "to a combined 1,100,000 net acres"
    (31).
  - Volatile oil window: "by 235,000 net acres for a combined contiguous position of 485,000 net
    acres" (39).
  - Natural gas window: "adds 330,000 net acres" (39).
  - Northern acreage: "increases its existing average working interest by more than 20%" (39); no
    acreage figure.
  - EOG's pre-deal Utica acreage is not stated directly.
  - Proposal versus action: the acquisition is a signed "definitive agreement" that is still
    pending (conditions at 49). The dividend is an actual board action ("today declared").
- Operative definitions: "the Transaction" (77). SEC reserve categories (211).
- Amendments or contradictions: none internal. The "About EOG" country list differs from D01 49
  (see D01).
- Coverage: full; lines 1-213 read (first map); byte-identical file, references spot-checked after
  the re-ingest. No hidden markers in either capture.

## D04 - Second Quarter 2025 Supplemental Financial and Operating Data

- Source: docs/eog_ex991_2025-08-07.txt | text, no pages. text/D04.txt has 1,193 lines and 56,141
  chars (manifest). "EX-99.1" (3), "2 exh99-1080725.htm EX-99.1" (5), "Document" (7), "EXHIBIT
  99.1" (9). Unlike D02/D05-D07 there is no "PRESS RELEASE OF EOG RESOURCES, INC." line. Printed
  page numbers 12-37 run in sequence (12 at 41, 13 at 89, 14 at 160, 15 at 226, 16 at 294, 17 at
  314, 18-24 at 356/394/433/474/513/551/586, 25 at 629, 26 at 653, 27 at 694, 28 at 721, 29 at
  778, 30 at 825, 31 at 848, 32 at 917, 33 at 963, 34 at 1027, 35 at 1083, 36 at 1171, 37 at
  1193).
- Written or submitted by: EOG Resources, Inc. No person is named.
- Type, date, edition: series edition "Second Quarter 2025 Supplemental Financial and Operating
  Data" (13); no printed issue date (file name 2025-08-07). TOC 11-39 has 12 entries and adds
  "Additional Key Financial Information 36" (39).
- Period covered and column convention: statement tables have 8 value columns = 2024 Q1-Q4, 2024
  Year, 2025 Q1, Q2, 2025 Year (first-half YTD; e.g. NI 1,463 + 1,345 = 2,808). Balance sheet 6
  value columns = Mar, Jun, Sep, Dec 2024, Mar, Jun 2025. Adjusted NI tables 2Q25, 1Q25, 4Q24,
  3Q24, 2Q24, FY24, FY23 (D02's 1Q24 table dropped). Bridges 1Q25 -> 2Q25. Annual CFO/FCF FY2023,
  FY2022. Net debt Jun 30 2025, Mar 31 2025, Dec 31 2024, Sep 30 2024, Jun 30 2024. Per-Boe
  quarterly 2Q25 1Q25 4Q24 3Q24 2Q24; annual 2024 2023 2022. AKFI "2024 Actual 2023 Actual 2022
  Actual" (1089). Price footnote: Note 10 of the 10-Q for the quarter ended June 30, 2025 (156).
- Entities and aliases: first series mention of "Encino" (354, 759). National Gas Company of
  Trinidad and Tobago Limited (1183). WTI "at Cushing, Oklahoma" (1179); Henry Hub, Louisiana,
  NYMEX Last Day Settle (1181). Non-GAAP names (298) now list "Adjusted Cash Flow from Operations".
- Tables (new columns; every overlapping 2024/1Q25 cell was compared with D02 and is identical
  unless noted):
  - Income Statements 43-87, 2Q25 / 2025 Year (H1):
    - Revenues (53-60): Crude Oil and Condensate 2,974 / 6,267; NGLs 534 / 1,106; Natural Gas 600
      / 1,237; MTM gains (losses) 107 / (84); Gathering, Processing and Marketing 1,247 / 2,587;
      Gains (Losses) on Asset Dispositions — / (1); Other, Net 16 / 35; Total 5,478 / 11,147.
    - Expenses (66-75): Lease and Well 396 / 797; GP&T 455 / 895; Exploration Costs 74 / 115; Dry
      Hole Costs 11 / 45; Impairments 39 / 83; Marketing Costs 1,216 / 2,541; DD&A 1,053 / 2,066;
      G&A 186 / 357; Taxes Other Than Income 301 / 642; Total 3,731 / 7,541.
    - Operating Income 1,747 / 3,606 (76); Other Income, Net 55 / 120; Income Before Interest
      Expense and Income Taxes 1,802 / 3,726; Interest Expense, Net 51 / 98 (79); Income Before
      Income Taxes 1,751 / 3,628; Income Tax Provision 406 / 820; Net Income 1,345 / 2,808 (82).
    - "Dividends Declared per Common Share" 2Q25 1.9950 / 2025 Year 2.9700 (83); 2024 and 1Q25 as
      in D02 (0.9100 x3, 0.9750, 3.7050, 0.9750).
    - Line 87: EPS Basic 2.48 / 5.13; Diluted 2.46 / 5.11; shares Basic 543 / 547, Diluted 546 /
      549.
  - Volumes and Prices 91-158, 2Q25 / H1: crude US 503.1 / 502.0, Trinidad 1.1 / 1.1, Total 504.2
    / 503.1 (102-106); crude price US 64.84 / 68.84, Trinidad 54.50 / 57.84, Composite 64.82 /
    68.81 (111-113); NGLs 258.4 / 250.1 (118-120), NGL price 22.70 / 24.42 (125-126); Natural Gas
    Volumes US 1,977 / 1,906, Trinidad 252 / 249, Total 2,229 / 2,155 (133-135); gas price US 2.87
    / 3.10, Trinidad 3.65 / 3.71, Composite 2.96 / 3.17 (140-142); COE Volumes US 1,090.9 /
    1,069.7, Trinidad 43.2 / 42.7, Total 1,134.1 / 1,112.4, Total MMBoe 103.2 / 201.3 (149-152).
  - Balance Sheets 162-224, Jun 30 2025 column (6th value): Cash and Cash Equivalents 5,216 (174);
    AR 2,504; Inventories 934; PRM assets —; Other (A) 591; Total current assets 9,245 (179); Oil
    and Gas Properties 80,139; Other PP&E 6,616; Total PP&E 86,755; Accumulated DD&A (51,394); Net
    PP&E 35,361; Deferred Income Taxes 39; Other Assets 1,639; Total Assets 46,284 (185-192);
    Accounts Payable 2,266; Accrued Taxes Payable 348; Dividends Payable 1,081 (200); PRM
    liabilities 85; Current Portion of Long-Term Debt 778 (202); Current Portion of Operating Lease
    Liabilities 360; Other 257; Total current liabilities 5,175 (205); Long-Term Debt 3,458 (206);
    Other Liabilities 2,398; Deferred Income Taxes 6,015; Common Stock 206; APIC 6,153; AOCL (7);
    Retained Earnings 28,131; Treasury (5,245); Total Stockholders' Equity 29,238 (221); Total L&SE
    46,284 (222). Footnote (A) 224 as in D02.
  - Cash Flow Statements 228-292, 2Q25 / H1:
    - Net Income 1,345 / 2,808 (240). Non-cash items (244-252): DD&A 1,053 / 2,066; Impairments 39
      / 83; Stock-Based Compensation 53 / 103; Deferred Income Taxes 105 / 149; asset dispositions
      — / 1; Other, Net 11 / 22; Dry Hole 11 / 45; MTM (107) / 84; settlements (24) / (62).
    - Working capital (258-264): AR 122 / 170; Inventories (45) / 31; AP (107) / (236); Accrued
      Taxes Payable (321) / (660); Other Assets (43) / (86); Other Liabilities (52) / (148); WC
      associated with investing (8) / (49). NCFO 2,032 / 4,321 (265).
    - Investing (271-275): Additions to Oil and Gas Properties (1,699) / (3,080); Additions to
      Other PP&E (94) / (196); Proceeds from Sales of Assets 4 / 16; WC investing 8 / 49; Net Cash
      Used in Investing (1,781) / (3,211).
    - Financing (281-288): Long-Term Debt Borrowings — / — (281); new row "Long-Term Debt
      Repayments" — (all 2024 and 1Q25) and (500) / (500) (282); Dividends Paid (528) / (1,066)
      (283); Treasury Stock Purchased (602) / (1,408) (284); stock options/ESPP 11 / 11; "Debt
      Issuance and Other Financing Costs" (renamed from D02's "Debt Issuance Costs"; same 2024
      values) (7) / (7) (286); finance leases (9) / (17); Net Cash Used in Financing (1,635) /
      (2,987) (288).
    - Effect of exchange rate 1 / 1 (289); Increase (Decrease) in Cash (1,383) / (1,876) (290);
      Beginning 6,599 / 7,092 (291); End 5,216 / 5,216 (292).
  - Non-GAAP Financial Measures 296-312 (Direct ATROR 310-312).
  - Adjusted Net Income 316-584 (method 320):
    - 2Q25 (322-354), lines are text, not a markdown table: Reported 1,751 (406) 1,345 2.46 (330);
      "Gains on Mark-to-Market ..." (107) 23 (84) (0.16) (334); "Net Cash Payments ..." (24) 5
      (19) (0.03) (336); "Add: Certain Impairments" 11 — 11 0.02 (338); "Add: Acquisition-related
      costs (2)" 18 (3) 15 0.03 (340); Adjustments (102) 25 (77) (0.14) (342); Adjusted NI 1,649
      (381) 1,268 2.32 (344); shares 543/546 (348/350); footnote (1) "$24 million" (352); footnote
      (2) "Consists of Encino acquisition-related G&A costs ($12 million) and financing commitment
      costs ($6 million)." (354).
    - 1Q25 (364-392), 4Q24 (402-431), 3Q24 (441-472), 2Q24 (482-511), FY24 (519-549), FY23
      (557-584): every row identical to D02.
  - NI per Share bridge 588-651 (1Q25 -> 2Q25): start 2.65 (592). Prices 39.80 less (45.88) =
    (6.08) x 103.2 = (627); tax 138; NI (489); EPS (0.90) (596-602). Volumes 103.2 less (98.1) = 5.1
    x GAAP margin 14.94 = 76; tax (17); NI 59; EPS 0.11 (606-614). Costs: "1Q 2025 Total Cash
    Operating Costs (GAAP) and Total DD&A per Boe 20.63" (618) less 2Q25 (20.25) = 0.38 x 103.2 =
    39; tax (9); NI 30; EPS 0.05 (620-627). MTM 2Q25 107/(23)/84 less 1Q25 (191)/41/(150); change
    234; EPS 0.43 (637-643). Other (1) 0.12 (645); 2Q25 diluted 2.46 (647); 546 (649). Footnote 651
    adds "(for GAAP earnings per share only)", "exploration costs, dry hole costs" and "the impact
    of share repurchases on diluted shares".
  - Adjusted NI per Share bridge 655-719: start 2.87 (659). Prices as above (663-669). Volumes x
    Non-GAAP margin 15.21 = 78; tax (17); NI 61; EPS 0.11 (673-679). Costs: 1Q25 (Non-GAAP) 20.63
    (683) less 2Q25 (20.14) = 0.49 x 103.2 = 51; tax (11); NI 40; EPS 0.07 (685-692). Settlements
    2Q25 (24)/5/(19) less 1Q25 (38)/8/(30); change 11; EPS 0.02 (702-711). Other (1) 0.15 (713);
    "2Q 2025 Adjusted Net Income per Share (Non-GAAP) 2.32" (715); footnote 719.
  - CFO and FCF 723-823:
    - Paragraph 727: NCFO reconciled to "Adjusted Cash Flow from Operations (Non-GAAP)"; adds
      "(or Investing and Financing Activities, as applicable)"; EOG is "(1) ... adjusting Net Cash
      Provided by Operating Activities (GAAP) to add back certain non-recurring acquisition-related
      costs incurred during the second quarter 2025 and (2) now presenting such adjusted measure as
      'Adjusted Cash Flow from Operations (Non-GAAP)' (instead of 'Cash Flow from Operations Before
      Changes in Working Capital (Non-GAAP)' as reported in prior periods); the presentation below
      with respect to the second quarter 2025 and the prior periods shown has been conformed".
    - NCFO 2,903 2,889 3,588 2,763 / 12,143 / 2,289 2,032 / 4,321 (733). WC rows (741-747), 2Q25
      / H1: AR (122) / (170); Inventories 45 / (31); AP 107 / 236; Accrued Taxes Payable 321 / 660;
      Other Assets 43 / 86; Other Liabilities 52 / 148; WC investing 8 / 49.
    - "Add: Acquisition-Related Costs (1), Net of Tax" — x6, 10 / 10 (751). "Adjusted Cash Flow
      from Operations (Non-GAAP)" 2,928 3,042 2,988 2,635 / 11,593 / 2,813 2,496 / 5,309 (753).
      Capex (2) (1,703) (1,668) (1,497) (1,358) / (6,226) / (1,484) (1,523) / (3,007) (755). FCF
      1,225 1,374 1,491 1,277 / 5,367 / 1,329 973 / 2,302 (757). Footnote (1) 759: "Consists of
      Encino acquisition-related G&A costs of $12 million (before tax) for the three months ended
      June 30, 2025."
    - Reconciliation (767-776): Total Expenditures (GAAP) ... 1,546 1,883 / 3,429 (767); ARC (13)
      (14) / (27); "Non-Cash Acquisition Costs of Unproved Properties" (9) (2) / (11); "Acquisition
      Costs of Proved Properties" 1 (270) / (269) (773); "Acquisition Costs of Other Property,
      Plant and Equipment" — — / — (774); Exploration Costs (41) (74) / (115); Total Capex 1,484
      1,523 / 3,007 (776). 2024 values as in D02.
    - FY2023 / FY2022 table 780-823 (title without "(Continued)"): same values as D02, but row 801
      is now "Adjusted Cash Flow from Operations (Non-GAAP)" 11,149 / 12,252 (D02 792 "Cash Flow
      from Operations Before Changes in Working Capital" 11,149 / 12,252). Reconciling rows
      817-823 keep D02's labels and values.
  - Net Debt 827-846 (833 dates): Jun 30 2025 column: equity 29,238; debt 4,236 (= 778 + 3,458);
    cash (5,216); Net Debt (980); Total Cap (GAAP) 33,474; Total Cap (Non-GAAP) 28,258 (837-842);
    12.7% (844); -3.5% (846). Other dates as D02.
  - Per-Boe quarterly 850-961 (856 columns 2Q25 1Q25 4Q24 3Q24 2Q24), 2Q25 column:
    - (a) 103.2; (b) 5,478; (c) 3,731; (d) 1,747 (860-863); Crude 2,974; NGLs 534; Gas 600
      (869-871); (e) 4,108 (873); L&W 396 (877); GP&T 455 (879).
    - G&A (GAAP) 186 with "Less: Certain Items (see Endnotes 2 & 3 to 2Q 2025 earnings release)"
      (12) — — (10) — (881); G&A (Non-GAAP) 174 171 189 157 151 (883).
    - TOTI 301, refund — (885); TOTI (Non-GAAP) 301 (887).
    - Interest now a text row: "Interest Expense, Net" 51 47 38 31 36 (889); "Less:
      Acquisition-Related Financing Commitment Costs" (6) — — — — (891); "Interest Expense, Net
      (Non-GAAP) (5)" 45 47 38 31 36 (893).
    - (f) 1,389; (g) 1,371; DD&A 1,053; (h) 2,442; (i) 2,424; Exploration 74; Dry Hole 11;
      Impairments 39; Total Exploration (GAAP) 124 (897-905); Less: Certain Impairments (2) (11) —
      (254) — (35) (907); Total Exploration (Non-GAAP) 113; (j) 2,566; (k) 2,537 (911-913).
    - Revenues less cost (915): GAAP 1,542; Non-GAAP 1,571.
    - Per Boe GAAP (931-947): (b)/(a) 53.08; (c)/(a) 36.15; (d)/(a) 16.93; (e)/(a) 39.80; (f) 13.46;
      26.34; (h) 23.66; 16.14; (j) 24.86; 14.94. Non-GAAP (951-961): (g) 13.30; 26.50; (i) 23.50;
      16.30; (k) 24.59; 15.21.
  - Per-Boe annual 965-1081: every value identical to D02 (971-1071); the G&A row keeps "Less:
    Severance Tax Consulting Fees" (996). Footnotes (1)-(5) 1073-1081; (5) is new (Interest Expense
    items non-recurring).
  - Additional Key Financial Information 1085-1191 ("(Unaudited)"; 2024 / 2023 / 2022 Actual):
    - "Crude Oil and Condensate Volumes (MBod)" US 490.6 / 475.2 / 460.7; Trinidad 0.8 / 0.6 / 0.6;
      Total 491.4 / 475.8 / 461.3 (1095-1097).
    - Line 1099: NGL Volumes (MBbld) Total 245.9 / 223.8 / 197.7. Natural Gas Volumes (MMcfd) US
      1,728 / 1,551 / 1,315; Trinidad 220 / 160 / 180; Total 1,948 / 1,711 / 1,495 (1103-1105).
    - COE Volumes (MBoed) US 1,024.5 / 957.5 / 877.5; Trinidad 37.6 / 27.3 / 30.7; Total 1,062.1 /
      984.8 / 908.2 (1111-1113).
    - Benchmark (1117): Oil (WTI) ($/Bbl) 75.72 / 77.61 / 94.23; Natural Gas (HH) ($/Mcf) 2.27 /
      2.74 / 6.64.
    - Crude above (below) WTI (endnote 1): US 1.70 / 1.57 / 2.99; Trinidad (11.29) / (9.03) /
      (8.07) (1121). NGL realizations as % of WTI 30.9% / 29.7% / 39.0% (1123). Gas above (below)
      Henry Hub (endnote 2), US (0.28) / (0.04) / 0.63 (1127).
    - Table 1131-1135 combines "Natural Gas Realizations3 ($/Mcf)" Trinidad 3.65 / 3.65 / 4.43
      (1133) with Total Expenditures (GAAP) ($MM) 6,653 / 6,818 / 5,610 (1134) and Capital
      Expenditures4 (non-GAAP) ($MM) 6,226 / 6,041 / 4,607 (1135).
    - Operating Unit Costs ($/Boe) (1141-1147): Lease and Well 4.04 / 4.05 / 4.02; GP&T5 4.43 /
      4.50 / 4.78; G&A (GAAP) 1.72 / 1.78 / 1.72; G&A (non-GAAP)6 1.70 / 1.78 / 1.67; Cash Operating
      Costs (GAAP) 10.19 / 10.33 / 10.52; Cash Operating Costs (non-GAAP)6 10.17 / 10.33 / 10.47;
      DD&A 10.57 / 9.72 / 10.69.
    - Expenses ($MM) (1153-1157): Exploration and Dry Hole 188 / 182 / 204; Impairment (GAAP) 391
      / 202 / 382; "Impairment (excluding certain impairments (non-GAAP))7" 100 / 160 / 269;
      Capitalized Interest 45 / 33 / 36; Net Interest 138 / 148 / 179.
    - TOTI % of revenues: GAAP 7.1 / 7.4 / 7.0 (1161); non-GAAP6 7.3 / 7.4 / 7.5 (1163). Effective
      Rate 22.1 / 21.6 / 21.7% (1167); Current Tax Expense ($MM) 1,348 / 1,415 / 2,208 (1169).
    - Continuation page titled "Additional Key Information (Continued)" (1173-1175). Endnotes
      1177-1191: 1) WTI differential basis (1179); 2) Henry Hub basis (1181); 3) Trinidad 2022
      one-time $0.76/Mcf adjustment (1183); 4) Capital Expenditures scope (1185); 5) GP&T
      combination (1187); 6) Cash Operating Costs and severance items, per-Boe impact "$(0.02) and
      $(0.05)" for FY2024 and FY2022 (1189); 7) impairment exclusion "from total impairment costs"
      (1191).
- Lists: 12 TOC entries. 7 Adjusted NI tables. 2Q25 adjustment rows: MTM, settlements, certain
  impairments, acquisition-related costs (no asset-disposition row; the income statement shows
  asset dispositions "—" for 2Q25, line 58). AKFI endnotes 1-7.
- Forecasts, guidance, deadlines, effective dates: none forward-looking. Effective dates: Oct 1,
  2024 (224); Jan 1, 2024 (1073, 1187).
- Hedged claims: boilerplate ("may be useful" 302, 320, 727, 831, 854; "may impact debt paydown"
  831).
- Rounded prose beside exact figures: none. Endnote 6 (1189) gives per-Boe consulting-fee impacts
  printed nowhere else.
- Notes:
  - 2Q25 impairment add-back 11 has no income-tax impact ("—", 338). Income-statement Impairments
    2Q25 = 39 (70); per-Boe Certain Impairments (11) (907).
  - Acquisition-related costs: Adjusted NI 18 before tax = G&A 12 + financing commitment 6 (340,
    354); CFO add-back 10 net of tax covers G&A only (751, 759); per-Boe G&A Certain Items (12)
    (881) and interest financing commitment (6) (891).
- Operative definitions, rules and scope exceptions: FCF now "Adjusted Cash Flow from Operations
  (Non-GAAP) ... less the Total Capital Expenditures (Non-GAAP)" (727). AKFI endnotes 1-7
  (1179-1191) as listed; endnote 4: Capital Expenditures include "Exploration and Development
  Drilling, Facilities, Leasehold Acquisitions, Capitalized Interest, Dry Hole Costs and Other
  Property, Plant and Equipment" and exclude "Property Acquisitions, Asset Retirement Costs,
  Non-Cash Exchanges and Transactions and exploration costs incurred as operating expenses".
- Amendments or contradictions (versus D02; values unchanged in every case):
  - Measure renamed: D02 744/792 "Cash Flow from Operations Before Changes in Working Capital
    (Non-GAAP)" -> D04 753/801 "Adjusted Cash Flow from Operations (Non-GAAP)"; prior periods
    "conformed" (727); 2024, 1Q25, FY23 and FY22 values identical.
  - Financing row "Debt Issuance Costs" (D02 285) -> "Debt Issuance and Other Financing Costs"
    (D04 286); new "Long-Term Debt Repayments" row (282).
  - Quarterly per-Boe G&A label "Severance Tax Consulting Fees" (D02 872) -> "Certain Items (see
    Endnotes 2 & 3 to 2Q 2025 earnings release)" (D04 881); the 3Q24 amount stays (10).
  - Per-Boe interest row moves out of the (f) table into text with a Non-GAAP variant (889-893).
- Coverage: full; every line 1-1193 read in four chunks (1-300, 301-600, 601-900, 901-1193). No
  hidden markers.

## D05 - Third Quarter 2025 Supplemental Financial and Operating Data

- Source: docs/eog_ex991_2025-11-06.txt | text, no pages. text/D05.txt has 1,216 lines and 57,956
  chars (manifest). "EX-99.1" (3), "2 exh99-1110625.htm" (5), "PRESS RELEASE OF EOG RESOURCES,
  INC." (7), "EXHIBIT 99.1" (11). Printed page numbers 11-36 run in sequence (11 at 43, 12 at 91,
  13 at 169, 14 at 235, 15 at 304, 16 at 324, 17-23 at 366/408/446/485/526/564/599, 24 at 642,
  25 at 666, 26 at 707, 27 at 735, 28 at 795, 29 at 848, 30 at 871, 31 at 940, 32 at 986, 33 at
  1050, 34 at 1106, 35 at 1194, 36 at 1216).
- Written or submitted by: EOG Resources, Inc. No person is named.
- Type, date, edition: series edition "Third Quarter 2025 Supplemental Financial and Operating
  Data" (15); no printed issue date (file name 2025-11-06). TOC 13-43 (entries 17-41): 12 entries,
  page numbers one lower than D04 (AKFI 35).
- Period covered and column convention: statement tables 9 value columns = 2024 Q1-Q4, 2024 Year,
  2025 Q1, Q2, Q3, 2025 Year (nine-month YTD; NI 1,463 + 1,345 + 1,471 = 4,279). Balance sheet 7
  value columns = Mar, Jun, Sep, Dec 2024, Mar, Jun, Sep 2025. Adjusted NI tables 3Q25, 2Q25,
  1Q25, 4Q24, 3Q24, FY24, FY23 (2Q24 dropped). Bridges 2Q25 -> 3Q25. Annual CFO/FCF FY2023,
  FY2022. Net debt Sep 30 2025, Jun 30 2025, Mar 31 2025, Dec 31 2024, Sep 30 2024. Per-Boe
  quarterly 3Q25 2Q25 1Q25 4Q24 3Q24; annual 2024 2023 2022. AKFI 2024/2023/2022 Actual. Price
  footnote: Note 10 of the 10-Q for the quarter ended September 30, 2025 (163).
- Entities and aliases:
  - "Encino Acquisition Partners, LLC" (cash-flow row, 280): the only series use of the full
    name; D03 19 has "Encino Acquisition Partners (EAP or Encino)". Short "Encino" at 330, 364,
    406, 773.
  - New "Other International (C)" rows for gas volumes (137) and gas price (147); BOE "Other
    International" (157, no letter). Footnote (C) 165: "Other International represents EOG's
    Kingdom of Bahrain operations. Realized price represents contract price less Bapco's
    processing and distribution costs." Bapco appears only here. No crude Other International
    row in D05.
- Tables (new columns; every overlapping cell was compared with D04 and D02 and is identical
  unless noted):
  - Income Statements 45-89, 3Q25 / 2025 Year (9M):
    - Revenues (55-62): Crude 3,243 / 9,510; NGLs 604 / 1,710; Natural Gas 707 / 1,944; MTM 116 /
      32; Gathering, Processing and Marketing 1,178 / 3,765; Gains (Losses) on Asset Dispositions
      (18) / (19); Other, Net 17 / 52; Total 5,847 / 16,994.
    - Expenses (68-77): L&W 431 / 1,228; GP&T 587 / 1,482; Exploration 71 / 186; Dry Hole — / 45;
      Impairments 71 / 154; Marketing 1,134 / 3,675; DD&A 1,169 / 3,235; G&A 239 / 596; TOTI 309
      / 951; Total 4,011 / 11,552.
    - Operating Income 1,836 / 5,442; Other Income 59 / 179; Income Before Interest and Taxes
      1,895 / 5,621; Interest Expense, Net 71 / 169 (81); Income Before Income Taxes 1,824 /
      5,452; Income Tax Provision 353 / 1,173; Net Income 1,471 / 4,279 (84).
    - "Dividends Declared per Common Share" 3Q25 "—" / 2025 Year 2.9700 (85); 2Q25 1.9950.
    - Line 89: EPS Basic 2.72 / 7.85; Diluted 2.70 / 7.81; shares Basic 541 / 545; Diluted 544 /
      548.
  - Volumes and Prices 93-167, 3Q25 / 9M: crude US 532.9 / 512.4, Trinidad 1.6 / 1.3, Total 534.5
    / 513.7 (104-108); crude price US 65.97 / 67.83, Trinidad 57.74 / 57.80, Composite 65.95 /
    67.81 (113-115); NGLs 309.3 / 270.0 (120-122); NGL price 21.25 / 23.20 (127-128); Natural Gas
    Volumes US 2,511 / 2,110, Trinidad 230 / 243, Other International 4 / 1 (earlier columns
    "—"), Total 2,745 / 2,354 (135-138); gas price US 2.71 / 2.94, Trinidad 3.80 / 3.74 (143-144),
    Other International 3.27 / 3.27 (147), Composite 2.80 / 3.03 (149); COE Volumes US 1,260.7 /
    1,134.1, Trinidad 39.8 / 41.7, Other International 0.7 / 0.2, Total 1,301.2 / 1,176.0, Total
    MMBoe 119.7 / 321.0 (155-159). BOE footnote relettered (D) (167).
  - Balance Sheets 171-233, Sep 30 2025 column (7th value): Cash 3,530 (183); AR 2,680;
    Inventories 945; PRM assets 19; Other 646; Total current assets 7,820 (188); Oil and Gas
    Properties 88,301 (194); Other PP&E 6,772; Total PP&E 95,073; Accumulated DD&A (52,488); Net
    PP&E 42,585 (198); Deferred Income Taxes 37; Other Assets 1,757; Total Assets 52,199 (201);
    Accounts Payable 2,944; Accrued Taxes Payable 392; Dividends Payable 550 (209); PRM
    liabilities 17; Current Portion of Long-Term Debt 27 (211); Current Portion of Operating Lease
    Liabilities 433; Other 452; Total current liabilities 4,815 (214); Long-Term Debt 7,667 (215);
    Other Liabilities 2,496; Deferred Income Taxes 6,936 (217); Common Stock 206; APIC 5,978;
    AOCL (5); Retained Earnings 29,603; Treasury (5,497); Total Stockholders' Equity 30,285
    (230); Total L&SE 52,199 (231). Footnote (A) 233.
  - Cash Flow Statements 237-302, 3Q25 / 9M:
    - Net Income 1,471 / 4,279 (249). Non-cash (253-261): DD&A 1,169 / 3,235; Impairments 71 /
      154; Stock-Based Compensation 53 / 156; Deferred Income Taxes 278 / 427; asset dispositions
      18 / 19; Other 2 / 24; Dry Hole — / 45; MTM (116) / (32); settlements 27 / (35).
    - Working capital (267-273): AR 133 / 303; Inventories 4 / 35; AP 5 / (231); Accrued Taxes
      Payable 28 / (632); Other Assets (28) / (114); Other Liabilities 155 / 7; WC investing (159)
      / (208). NCFO 3,111 / 7,432 (274).
    - Investing (280-285): new first row "Acquisition of Encino Acquisition Partners, LLC, Net of
      Cash Acquired" — in every 2024, 1Q25 and 2Q25 column; (4,464) 3Q25 / (4,464) 9M (280).
      Additions to Oil and Gas Properties (1,492) / (4,572); Additions to Other PP&E (171) /
      (367); Proceeds from Sales of Assets 5 / 21; WC investing 159 / 208; Net Cash Used in
      Investing (5,963) / (9,174) (285).
    - Financing (291-298): Long-Term Debt Borrowings 3,472 / 3,472 (291); Long-Term Debt
      Repayments (1,266) / (1,766) (292); Dividends Paid (545) / (1,611) (293); Treasury Stock
      Purchased (479) / (1,887) (294); stock options/ESPP — / 11; Debt Issuance and Other
      Financing Costs (7) / (14); finance leases (8) / (25); Net Cash Provided by (Used in)
      Financing 1,167 / (1,820) (298; label still "Net Cash Used in Financing Activities").
    - Effect of exchange rate (1) / — (299); Increase (Decrease) in Cash (1,686) / (3,562) (300);
      Beginning 5,216 / 7,092 (301); End 3,530 / 3,530 (302).
  - Non-GAAP Financial Measures 306-322.
  - Adjusted Net Income 326-597. Method paragraph 330 adds "to add back costs associated with the
    Encino acquisition".
    - 3Q25 (332-364; text lines): Reported 1,824 (353) 1,471 2.70 (340); "Gains on
      Mark-to-Market ..." (116) 25 (91) (0.16) (344); "Net Cash Received ..." 27 (5) 22 0.04
      (346); "Add: Losses on Asset Dispositions, Net" 18 (6) 12 0.02 (348); "Add:
      Acquisition-related costs (2)" 68 (10) 58 0.11 (350); Adjustments (3) 4 1 0.01 (352);
      Adjusted NI 1,821 (349) 1,472 2.71 (354); shares 541/544 (358/360); footnote (1) "$27
      million" (362); footnote (2) "Consists of Encino acquisition-related G&A costs ($68
      million)." (364).
    - 2Q25 (374-406), 1Q25 (416-444), 4Q24 (454-483), 3Q24 (493-524), FY24 (532-562), FY23
      (570-597): identical to D04/D02.
  - NI per Share bridge 601-664 (2Q25 -> 3Q25): start 2.46 (605). Prices 38.05 less (39.80) =
    (1.75) x 119.7 = (209); tax 46; NI (163); EPS (0.30) (609-615). Volumes 119.7 less (103.2) =
    16.5 x GAAP margin 13.42 = 221; tax (49); NI 172; EPS 0.32 (619-627). Costs: "2Q 2025 Total
    Cash Operating Costs (GAAP) and Total DD&A per Boe 20.25" (631) less 3Q25 (20.27) = (0.02) x
    119.7 = (2); tax 1; NI (1); EPS 0.00 (633-640). MTM 3Q25 116/(25)/91 less 2Q25 107/(23)/84;
    change 7; EPS 0.01 (650-656). Other (1) 0.21 (658); 3Q25 diluted 2.70 (660); 544 (662).
    Footnote 664 ("impairments, marketing costs").
  - Adjusted NI per Share bridge 668-733: start 2.32 (672). Prices as above. Volumes x Non-GAAP
    margin 13.99 = 231; tax (51); NI 180; EPS 0.33 (686-692). Costs: 2Q25 (Non-GAAP) 20.14 (696)
    less 3Q25 (19.70) = 0.44 x 119.7 = 53; tax (12); NI 41; EPS 0.08 (698-705). Settlements 3Q25
    27/(5)/22 less 2Q25 (24)/5/(19); change 41; EPS 0.08 (715-725). Other (1) 0.20 (727); 3Q25
    adjusted 2.71 (729); footnote 733.
  - CFO and FCF 737-846:
    - Paragraph 741: add-back of acquisition-related costs "incurred during the second and third
      quarters of 2025"; prior periods conformed.
    - NCFO ... | 2,289 2,032 3,111 / 7,432 (747). WC rows (755-761), 3Q25 / 9M: AR (133) / (303);
      Inventories (4) / (35); AP (5) / 231; Accrued Taxes Payable (28) / 632; Other Assets 28 /
      114; Other Liabilities (155) / (7); WC investing 159 / 208.
    - "Acquisition-Related Costs (1), Net of Tax" — x6, 10 58 / 68 (765). Adjusted CFO ... | 2,813
      2,496 3,031 / 8,340 (767). Capex ... | (1,484) (1,523) (1,648) / (4,655) (769). FCF ... |
      1,329 973 1,383 / 3,685 (771). Footnote (1) 773: "Encino acquisition-related G&A costs of
      $12 million and $68 million (each before tax)" for the quarters ended June 30 and September
      30, 2025.
    - Reconciliation (781-793), 2024 Q1-Q4 / Year | 2025 Q1 Q2 Q3 / 9M: Total Expenditures (GAAP)
      1,952 1,682 1,573 1,446 / 6,653 | 1,546 1,883 8,544 / 11,973 (781); Asset Retirement Costs
      (21) 60 (11) (26) / 2 | (13) (14) (86) / (113) (783); "Non-Cash Leasehold Acquisition Costs
      (3)" (31) (34) (17) (3) / (85) | (9) (2) (3) / (14) (785); "Acquisition Costs of Properties
      (3)" (21) (5) — (7) / (33) | 1 (270) (6,736) / (7,005) (787); "Acquisition Costs of Other
      Property, Plant and Equipment" (131) (1) (5) — / (137) | — — — / — (791); Exploration Costs
      (45) (34) (43) (52) / (174) | (41) (74) (71) / (186) (792); Total Capex 1,703 1,668 1,497
      1,358 / 6,226 | 1,484 1,523 1,648 / 4,655 (793).
    - FY2023 / FY2022 table 797-846 ("(Continued)"): NCFO 11,340 / 11,093; WC rows as D02;
      Adjusted CFO 11,149 / 12,252 (818); capex (6,041) / (4,607); FCF 5,108 / 7,645; Total
      Expenditures 6,818 / 5,610 (828); ARC (257) / (298); Non-Cash Development Drilling (90) / —;
      Non-Cash Leasehold Acquisition Costs (3) (99) / (127) (836); Acquisition Costs of Properties
      (3) (16) / (419) (838); Acquisition Costs of Other PP&E (134) / — (842); Exploration (181) /
      (159); Total Capex 6,041 / 4,607 (832-844).
    - Footnote (3) 846: "Line item descriptions revised (from descriptions shown in EOG's
      previously published tables) to more accurately describe the costs reflected therein;
      previously reported cost amounts not impacted by such changes in presentation."
  - Net Debt 850-869 (856 dates), Sep 30 2025 column: equity 30,285; debt 7,694 (= 27 + 7,667);
    cash (3,530); Net Debt 4,164; Total Cap (GAAP) 37,979; Total Cap (Non-GAAP) 34,449 (860-865);
    20.3% (867); 12.1% (869). Other dates as D04.
  - Per-Boe quarterly 873-984 (879 columns 3Q25 2Q25 1Q25 4Q24 3Q24), 3Q25 column:
    - (a) 119.7; (b) 5,847; (c) 4,011; (d) 1,836 (883-886); Crude 3,243; NGLs 604; Gas 707
      (892-894); (e) 4,554 (896); L&W 431 (900); GP&T 587 (902).
    - G&A (GAAP) 239 with "Less: Certain Items (see Endnotes 2 & 3 to 3Q 2025 earnings release)"
      (68) (12) — — (10) (904); "General and Administrative (Non-GAAP) (2)" 171 174 171 189 157
      (906).
    - TOTI 309; refund — — — — 31 (908); TOTI (Non-GAAP) (3) 309 301 341 291 314 (910).
    - Interest 71 51 47 38 31 (912); financing commitment — (6) — — — (914); Interest (Non-GAAP)
      (4) 71 45 47 38 31 (916).
    - (f) 1,637; (g) 1,569; DD&A 1,169; (h) 2,806; (i) 2,738; Exploration 71; Dry Hole —;
      Impairments 71; Total Exploration (GAAP) 142 (920-928); "Less: Certain Impairments (5)" —
      (11) — (254) — (930); Total Exploration (Non-GAAP) 142; (j) 2,948; (k) 2,880 (934-936).
    - Revenues less cost (938): GAAP 1,606; Non-GAAP 1,674.
    - Per Boe GAAP (954-970): (b)/(a) 48.85; (c)/(a) 33.51; (d)/(a) 15.34; (e)/(a) 38.05; (f) 13.67;
      24.38; (h) 23.44; 14.61; (j) 24.63; 13.42. Non-GAAP (974-984): (g) 13.10; 24.95; (i) 22.87;
      15.18; (k) 24.06; 13.99.
  - Per-Boe annual 988-1104: values identical to D02/D04; G&A row keeps "Less: Severance Tax
    Consulting Fees" (1019). Footnotes renumbered (1096-1104): (1) GP&T, (2) G&A, (3) TOTI, (4)
    Interest, (5) impairments.
  - AKFI 1108-1214: every value and endnote identical to D04 (crude volumes 1118-1120; NGL and
    gas volumes 1122-1128; COE 1134-1136; benchmarks 1140; differentials 1144-1150; Trinidad gas
    realization and expenditures 1156-1158; unit costs 1164-1170; expenses 1176-1180; TOTI
    1184-1186; tax 1190-1192; endnotes 1-7 at 1202-1214). Continuation title "Additional Key
    Information (Continued)" (1196-1198).
- Lists: 12 TOC entries. 7 Adjusted NI tables. 3Q25 adjustment rows: MTM, settlements, losses on
  asset dispositions, acquisition-related costs (no impairment row although income-statement
  Impairments 3Q25 = 71, line 72; per-Boe Certain Impairments 3Q25 "—", 930).
- Forecasts, guidance, deadlines, effective dates: none forward-looking. Effective dates Oct 1,
  2024 (233); Jan 1, 2024 (1096, 1210).
- Hedged claims: boilerplate only.
- Rounded prose beside exact figures: none.
- Notes:
  - No text states that the Encino acquisition closed or gives a closing date; the acquisition
    cash-flow row is populated only in the 3Q25 column (280).
  - 3Q25 acquisition-related costs are G&A only ($68 million; 364, 773; per-Boe (68), 904).
- Operative definitions, rules and scope exceptions: as D04; footnote (C) defines Other
  International (165).
- Amendments or contradictions:
  - Reconciling-row relabels with unchanged amounts (footnote (3), 846): D02 763 / D04 772
    "Non-Cash Acquisition Costs of Unproved Properties" -> D05 785 "Non-Cash Leasehold Acquisition
    Costs"; D02 764 / D04 773 "Acquisition Costs of Proved Properties" -> D05 787 "Acquisition
    Costs of Properties". Same for the FY23/FY22 rows (D02 810-811, D04 819-820 -> D05 836-838).
  - CFO paragraph (741) now says "second and third quarters of 2025"; Adjusted NI method (330)
    adds the Encino add-back.
  - Quarterly per-Boe footnote numbers change (G&A (2), TOTI (3), Interest (4), impairments (5)).
- Coverage: full; every line 1-1216 read in four chunks (1-310, 311-610, 611-910, 911-1216). No
  hidden markers.

## D06 - First Quarter 2026 Supplemental Financial and Operating Data

- Source: docs/eog_ex991_2026-05-05.txt | text, no pages. Current text/D06.txt (re-extracted
  2026-10-05 after the splitter fix; the stray page-metadata first line is gone) has 1,205 lines
  and starts "# D06 | ...", blank, "EX-99.1". "2 exh99-1050526.htm" (5), "PRESS RELEASE OF EOG
  RESOURCES, INC." (7), "EXHIBIT 99.1" (11). Printed page numbers 9-29 run in sequence (9 at 43,
  10 at 91, 11 at 174, 12 at 240, 13 at 310, 14 at 330, 15 at 368, 16 at 444, 17 at 512, 18 at
  590, 19 at 651, 20 at 712, 21 at 768, 22 at 819, 23 at 842, 24 at 911, 25 at 957, 26 at 1024,
  27 at 1080, 28 at 1179, 29 at 1205). All line numbers below are for the current file.
- Written or submitted by: EOG Resources, Inc. No person is named.
- Type, date, edition: series edition "First Quarter 2026 Supplemental Financial and Operating
  Data" (15); no printed issue date (file name 2026-05-05). TOC 13-43 (entries 17-41): 12 entries
  (Income Statements 10 ... Adjusted NI 15, NI Per Share 19, Adjusted NI Per Share 20, CFO/FCF 21,
  Net Debt 23, Per-Boe 24, AKFI 28).
- Period covered and column convention: statement tables 7 value columns = 2025 Q1, Q2, Q3, Q4,
  2025 Year (full FY 2025), 2026 Q1, 2026 Year (= Q1). Balance sheet 5 value columns = Mar, Jun,
  Sep, Dec 2025, Mar 2026. Adjusted NI tables 1Q26, 4Q25, 3Q25, 2Q25, 1Q25, FY25, FY24 (4Q24,
  3Q24, FY23 dropped). Bridges 4Q25 -> 1Q26. Annual CFO/FCF FY2024, FY2023, FY2022, FY2021. Net
  debt Mar 31 2026, Dec 31 2025, Sep 30 2025, Jun 30 2025, Mar 31 2025. Per-Boe quarterly 1Q26
  4Q25 3Q25 2Q25 1Q25; annual 2025-2021. AKFI 2025-2021 "Actual". First appearance in the bundle
  of 4Q25, FY25 and FY21 figures. Price footnote: Note 9 of the 10-Q for the quarter ended March
  31, 2026 (170); balance-sheet footnote (B): Note 5 (238).
- Entities and aliases:
  - "Other International (B)" rows for crude volume (108), crude price (119), gas volume (142),
    gas price (152) and BOE (162). Footnote (B) 168: "Production volumes from Bahrain operations;
    natural gas realized price represents contract price less partner's processing and
    distribution costs." (D05 165 said "Bapco's"; no document states that Bapco is the
    "partner".)
  - "Encino Acquisition Partners, LLC" (286); "Encino" at 336, 410, 442, 482, 552, 750, 1199,
    1203. Plays in impairment footnotes: "Barnett Shale and Woodford Oil Window" (408, 550, 1201);
    "Rocky Mountain area" (588, 1201).
- Tables (new columns; every overlapping cell was compared with D05/D04 and is identical unless
  noted under Amendments):
  - Income Statements 45-89, 4Q25 / FY25 / 1Q26:
    - Revenues (55-62): Crude 2,991 / 12,501 / 3,577; NGLs 666 / 2,376 / 664; Natural Gas 847 /
      2,791 / 1,021; MTM (19) / 13 / 113; Gathering, Processing and Marketing 1,149 / 4,914 /
      1,496; Gains (Losses) on Asset Dispositions (16) / (35) / 31; Other, Net 20 / 72 / 19; Total
      5,638 / 22,632 / 6,921.
    - Expenses (68-77): L&W 447 / 1,675 / 462; GP&T 652 / 2,134 / 654; Exploration 50 / 236 / 45;
      Dry Hole 4 / 49 / 23; Impairments 689 / 843 / 39 (72); Marketing 1,120 / 4,795 / 1,384; DD&A
      1,226 / 4,461 / 1,193; G&A 224 / 820 / 185; TOTI 283 / 1,234 / 338; Total 4,695 / 16,247 /
      4,323.
    - Operating Income 943 / 6,385 / 2,598 (78); Other Income 33 / 212 / 23; Income Before
      Interest and Taxes 976 / 6,597 / 2,621; Interest Expense, Net 66 / 235 / 66 (81); Income
      Before Income Taxes 910 / 6,362 / 2,555; Income Tax Provision 209 / 1,382 / 575; Net Income
      701 / 4,980 / 1,980 (84).
    - "Dividends Declared per Common Share" 2025: 0.9750 1.9950 — 1.0200 / Year 3.9900; 2026 Q1
      1.0200 / Year 1.0200 (85).
    - Line 89: EPS Basic 1.31 / 9.17 / 3.72; Diluted 1.30 / 9.12 / 3.70; shares Basic 537 / 543 /
      532; Diluted 539 / 546 / 535.
  - Volumes and Prices 93-172 (4Q25 / FY25 / 1Q26):
    - Crude (MBbld): US 544.5 / 520.5 / 546.5; Trinidad 1.5 / 1.4 / 1.9; Other International (B)
      2025 "— — — 0.1", FY "—", 1Q26 0.1 (108); Total 546.1 / 521.9 / 548.5 (110).
    - Crude price: US 59.54 / 65.65 / 72.48; Trinidad 57.07 / 57.59 / 68.91; Other International
      "— — —" 63.98 / "—" / 89.12 (119); Composite 59.54 / 65.63 / 72.47 (121).
    - NGLs 342.1 / 288.2 / 332.1 (125-127); NGL price 21.15 / 22.58 / 22.20 (132-133).
    - Natural Gas Volumes (MMcfd): US 2,859 / 2,299 / 2,769; Trinidad 195 / 230 / 239; Other
      International "— — 4" 11 / 4 / 12; Total 3,065 / 2,533 / 3,020 (140-143).
    - Gas price: US 2.94 / 2.94 / 3.75; Trinidad 3.94 / 3.78 / 3.91 (148-149); Other International
      "— — 3.27" 3.29 / 3.28 / 3.26 (152); Composite 3.00 / 3.02 / 3.76 (154).
    - COE Volumes (MBoed): US 1,363.0 / 1,191.8 / 1,340.1; Trinidad 34.2 / 39.8 / 41.7; Other
      International (B) "— — 0.7" 1.8 / 0.6 / 2.0; Total 1,399.0 / 1,232.2 / 1,383.8; Total MMBoe
      128.7 / 449.8 / 124.5 (160-164).
  - Balance Sheets 176-238 (Mar25 Jun25 Sep25 Dec25 Mar26):
    - Current Assets (188-192): Cash 6,599 5,216 3,530 3,396 3,849; AR 2,621 2,504 2,680 2,681
      3,597; Inventories 897 934 945 1,014 955; Other (A) 563 591 665 565 562; Total 10,680 9,245
      7,820 7,656 8,963. No "Assets from Price Risk Management Activities" row.
    - PP&E (198-205): Oil and Gas Properties 78,432 80,139 88,301 89,857 90,786; Other PP&E 6,510
      6,616 6,772 6,832 6,942; Total PP&E 84,942 86,755 95,073 96,689 97,728; Accumulated DD&A
      (50,310) (51,394) (52,488) (54,348) (55,054); Net 34,632 35,361 42,585 42,341 42,674;
      Deferred Income Taxes 44 39 37 39 30; Other Assets 1,626 1,639 1,757 1,763 1,711; Total
      Assets 46,982 46,284 52,199 51,799 53,378.
    - Current Liabilities (211-217): AP 2,353 2,266 2,944 2,904 3,186; Accrued Taxes Payable 668
      348 392 299 766; Dividends Payable 534 1,081 550 544 541 (213); Current Portion of Long-Term
      Debt 1,280 778 27 27 27 (214); Current Portion of Operating Lease Liabilities 318 360 433 472
      375; Other (A) 566 342 469 445 329 (216); Total 5,719 5,175 4,815 4,691 5,224. No "Liabilities
      from Price Risk Management Activities" row.
    - Long-Term Debt 3,464 3,458 7,667 7,909 7,904 (218); Other Liabilities 2,368 2,398 2,496 2,512
      2,476; Deferred Income Taxes 5,915 6,015 6,936 6,854 6,866 (220). "Commitments and
      Contingencies (B)" (222).
    - Equity (228-234): Common Stock 206 (all); APIC 6,095 6,153 5,978 6,027 6,026; AOCL (4) (7)
      (5) (7) (6); Retained Earnings 27,869 28,131 29,603 29,765 31,200; Treasury (4,650) (5,245)
      (5,497) (6,158) (6,518); Total Stockholders' Equity 29,516 29,238 30,285 29,833 30,908; Total
      L&SE 46,982 46,284 52,199 51,799 53,378.
    - Footnote (A) 236: "Effective January 1, 2026, EOG combined Price Risk Management Activities
      into the Other line item. This presentation has been conformed for all periods presented and
      had no impact on previously reported Total Assets and Total Liabilities and Stockholders's
      Equity" (sic). Footnote (B) 238: Note 5 of the 10-Q.
  - Cash Flow Statements 242-308 (2025 Q1-Q4 / Year | 2026 Q1 / Year):
    - Net Income 1,463 1,345 1,471 701 / 4,980 | 1,980 (254).
    - Non-cash (258-267): DD&A ... 1,226 / 4,461 | 1,193; Impairments ... 689 / 843 | 39; Stock-Based
      Compensation 50 53 53 60 / 216 | 58; Deferred Income Taxes 44 105 278 (84) / 343 | 18; asset
      dispositions 1 — 18 16 / 35 | (31); Other, Net 11 11 2 3 / 27 | 15 (263); Dry Hole 34 11 — 4
      / 49 | 23; MTM 191 (107) (116) 19 / (13) | (113); settlements (38) (24) 27 (21) / (56) |
      (53); a second "Other, Net" row — — — (1) / (1) | — (267; new in D06).
    - Working capital (273-279): AR 48 122 133 (3) / 300 | (907); Inventories 76 (45) 4 (84) /
      (49) | 21; AP (129) (107) 5 (40) / (271) | 279; Accrued Taxes Payable (339) (321) 28 (103) /
      (735) | 467; Other Assets (43) (43) (28) 97 / (17) | 55; Other Liabilities (96) (52) 155 10 /
      17 | (123); WC investing (41) (8) (159) 123 / (85) | 45. NCFO 2,289 2,032 3,111 2,612 /
      10,044 | 2,966 (280).
    - Investing (286-291): "Acquisition of Encino Acquisition Partners, LLC, Net of Cash
      Acquired" — — (4,464) 13 / (4,451) | — (286); Additions to Oil and Gas Properties (1,381)
      (1,699) (1,492) (1,543) / (6,115) | (1,491); Additions to Other PP&E (102) (94) (171) (112) /
      (479) | (153); Proceeds from Sales of Assets 12 4 5 3 / 24 | 144 (289); WC investing 41 8 159
      (123) / 85 | (45); Net Cash Used in Investing (1,430) (1,781) (5,963) (1,762) / (10,936) |
      (1,545) (291).
    - Financing (297-304): Long-Term Debt Borrowings — — 3,472 999 / 4,471 | — (297); Long-Term
      Debt Repayments — (500) (1,266) (750) / (2,516) | — (298); Dividends Paid (538) (528) (545)
      (550) / (2,161) | (544) (299); Treasury Stock Purchased (806) (602) (479) (677) / (2,564) |
      (418) (300); stock options/ESPP — 11 — 12 / 23 | 1; Debt Issuance and Other Financing Costs
      — (7) (7) (11) / (25) | —; finance leases (8) (9) (8) (7) / (32) | (7); Net Cash Used in
      Financing (1,352) (1,635) 1,167 (984) / (2,804) | (968) (304).
    - Effect of exchange rate — 1 (1) – / — | — (305); Increase (Decrease) in Cash (493) (1,383)
      (1,686) (134) / (3,696) | 453 (306); Beginning 7,092 6,599 5,216 3,530 / 7,092 | 3,396 (307);
      End 6,599 5,216 3,530 3,396 / 3,396 | 3,849 (308).
  - Non-GAAP Financial Measures 312-328 ("accompanying earnings presentation slides", 314).
  - Adjusted Net Income 332-588 (method 336 includes the Encino add-back):
    - 1Q26 (338-366): Reported 2,555 (575) 1,980 3.70 (346); Gains MTM (113) 24 (89) (0.17) (350);
      Net Cash Payments (53) 11 (42) (0.08) (352); "Less: Gains on Asset Dispositions, Net" (31) 7
      (24) (0.04) (356); Adjustments (197) 42 (155) (0.29) (357); Adjusted NI 2,358 (533) 1,825
      3.41 (358); shares 532/535; "$53 million" (366). Complete.
    - 4Q25 (376-410): Reported 910 (209) 701 1.30 (384); Losses MTM 19 (4) 15 0.03 (386); Net Cash
      Payments (21) 4 (17) (0.03) (388); Add: Losses on Asset Dispositions 16 (4) 12 0.02 (390);
      "Add: Certain Impairments (2)" 646 (140) 506 0.94 (392); "Add: Acquisition-Related Costs
      (3)" 8 (3) 5 0.01 (394); Adjustments 668 (147) 521 0.97 (396); Adjusted NI 1,578 (356) 1,222
      2.27 (398); 537/539; footnotes (1) "$21 million" (406), (2) "Impairments primarily
      associated with the write-down to fair value of natural gas and crude oil assets in the
      Barnett Shale and Woodford Oil Window (mainly driven by play-specific economics and resource
      allocation)" (408), (3) "Consists of Encino acquisition-related G&A costs ($8 million)"
      (410).
    - 3Q25 (412-442), 2Q25 (452-482), 1Q25 (484-510): identical values to D05/D04/D02; label now
      "Acquisition-Related Costs" (428, 468).
    - FY25 (518-552): Reported 6,362 (1,382) 4,980 9.12 (526); Gains MTM (13) 3 (10) (0.02);
      Payments (56) 12 (44) (0.08); Add: Losses on Asset Dispositions 35 (8) 27 0.05 (532); Add:
      Certain Impairments (2) 657 (140) 517 0.95 (534); Add: Acquisition-Related Costs (3) 94 (16)
      78 0.14 (536); Adjustments 717 (149) 568 1.04 (538); Adjusted NI 7,079 (1,531) 5,548 10.16
      (540); 543/546; footnotes "$56 million" (548), Barnett/Woodford (550), "Encino
      acquisition-related G&A costs ($88 million) and financing commitment costs ($6 million)"
      (552). Quarterly rows sum to FY25: asset dispositions 1 + 0 + 18 + 16 = 35; impairments 11 +
      646 = 657; acquisition costs 18 + 68 + 8 = 94.
    - FY24 (554-588): identical values to D02/D04/D05 (Adjusted NI 8,477 (1,865) 6,612 11.62,
      578); new footnote (2) on Certain Impairments: "write-down to fair value of natural gas and
      crude oil assets in the Rocky Mountain area" (588).
  - NI per Share bridge 592-649 (4Q25 -> 1Q26): start 1.30 (596). Prices 42.24 less (34.99) =
    7.25 x 124.5 = 903; tax (199); NI 704; EPS 1.32 (600-606). Volumes 124.5 less (128.7) = (4.2) x
    GAAP margin 18.11 = (76); tax 17; NI (59); EPS (0.11) (610-618). Costs: "4Q 2025 Total Cash
    Operating Costs (GAAP) and Total DD&A per Boe 19.81" (622) less 1Q26 (20.03) = (0.22) x 124.5
    = (27); tax 6; NI (21); EPS (0.04) (624-631). MTM 1Q26 113/(24)/89 less 4Q25 (19)/4/(15);
    change 104; EPS 0.19 (633-641). Other (1) 1.04 (643); 1Q26 diluted 3.70 (645); 535 (647).
    Footnote 649.
  - Adjusted NI per Share bridge 653-710: start 4Q25 adjusted 2.27 (657). Prices as above.
    Volumes x Non-GAAP margin 18.11 = (76); tax 17; NI (59); EPS (0.11) (671-677). Costs: 4Q25
    (Non-GAAP) 19.75 (681) less 1Q26 (20.03) = (0.28) x 124.5 = (35); tax 8; NI (27); EPS (0.05)
    (683-690). Settlements 1Q26 (53)/11/(42) less 4Q25 (21)/4/(17); change (25); EPS (0.05)
    (692-702). Other (1) 0.03 (704); "1Q 2026 Adjusted Net Income per Share (Non-GAAP) 3.41" (706).
  - CFO and FCF 714-817:
    - Paragraph 718: add-back covers "the second, third and fourth quarters of 2025".
    - NCFO 2,289 2,032 3,111 2,612 / 10,044 | 2,966 (724). WC rows (732-738): AR (48) (122) (133) 3
      / (300) | 907; Inventories (76) 45 (4) 84 / 49 | (21); AP 129 107 (5) 40 / 271 | (279);
      Accrued Taxes Payable 339 321 (28) 103 / 735 | (467); Other Assets 43 43 28 (97) / 17 |
      (55); Other Liabilities 96 52 (155) (10) / (17) | 123; WC investing 41 8 159 (123) / 85 |
      (45).
    - "Acquisition-Related Costs (1), Net of Tax" — 10 58 5 / 73 | — (742). Adjusted CFO 2,813
      2,496 3,031 2,617 / 10,957 | 3,129 (744). Capex (2) (1,484) (1,523) (1,648) (1,639) /
      (6,294) | (1,636) (746). FCF 1,329 973 1,383 978 / 4,663 | 1,493 (748). Footnote (1) 750:
      "$12 million, $68 million and $8 million (each before tax)" for the quarters ended June 30,
      September 30 and December 31, 2025.
    - Reconciliation (758-766): Total Expenditures (GAAP) 1,546 1,883 8,544 1,730 / 13,703 |
      1,768 (758); ARC (13) (14) (86) (33) / (146) | (12) (760); Non-Cash Leasehold Acquisition
      Costs (3) (9) (2) (3) (10) / (24) | (52) (762); Acquisition Costs of Properties (3) 1 (270)
      (6,736) 2 / (7,003) | (23) (764); Exploration Costs (41) (74) (71) (50) / (236) | (45) and
      Total Capital Expenditures (Non-GAAP) 1,484 1,523 1,648 1,639 / 6,294 | 1,636 (766, one
      flattened line). The "Acquisition Costs of Other PP&E" row is not printed for 2025-2026.
    - Annual table 770-817 (FY2024 / FY2023 / FY2022 / FY2021): NCFO 12,143 / 11,340 / 11,093 /
      8,791 (776); AR (101) / 38 / 347 / 821; Inventories (259) / 231 / 534 / 13; AP 36 / 119 /
      (90) / (456); Accrued Taxes Payable (541) / (61) / 113 / (312); Other Assets (44) / (39) /
      364 / 136; Other Liabilities (23) / (184) / 266 / 116; WC investing 382 / (295) / (375) /
      200 (784-790); Adjusted CFO 11,593 / 11,149 / 12,252 / 9,309 (791); capex (6,226) / (6,041)
      / (4,607) / (3,755) (795); FCF 5,367 / 5,108 / 7,645 / 5,554 (797); Total Expenditures 6,653
      / 6,818 / 5,610 / 4,255 (801); ARC 2 / (257) / (298) / (127) and Non-Cash Development
      Drilling — / (90) / — / — (803); Non-Cash Leasehold Acquisition Costs (3) (85) / (99) /
      (127) / (45) (805); "Non-Cash Finance Leases" — / — / — / (74) (807); Acquisition Costs of
      Properties (3) (33) / (16) / (419) / (100) (809); Acquisition Costs of Other PP&E (137) /
      (134) / — / — (813); Exploration Costs (174) / (181) / (159) / (154) (814); Total Capex 6,226
      / 6,041 / 4,607 / 3,755 (815). Footnote (3) 817 (revised descriptions).
  - Net Debt 821-840 (827 dates Mar 31 2026, Dec 31 2025, Sep 30 2025, Jun 30 2025, Mar 31 2025):
    equity 30,908 29,833 30,285 29,238 29,516 (831); debt 7,931 7,936 7,694 4,236 4,744 (832);
    cash (3,849) (3,396) (3,530) (5,216) (6,599) (833); Net Debt 4,082 4,540 4,164 (980) (1,855)
    (834); Total Cap (GAAP) 38,839 37,769 37,979 33,474 34,260 (835); Total Cap (Non-GAAP) 34,990
    34,373 34,449 28,258 27,661 (836); 20.4% 21.0% 20.3% 12.7% 13.8% (838); 11.7% 13.2% 12.1%
    -3.5% -6.7% (840). Debt equals balance-sheet 214 + 218 (Dec 31 2025: 27 + 7,909).
  - Per-Boe quarterly 844-955 (850 columns 1Q26 4Q25 3Q25 2Q25 1Q25), 1Q26 / 4Q25 columns:
    - (a) 124.5 / 128.7; (b) 6,921 / 5,638; (c) 4,323 / 4,695; (d) 2,598 / 943 (854-857); Crude
      3,577 / 2,991; NGLs 664 / 666; Gas 1,021 / 847 (863-865); (e) 5,262 / 4,504 (867).
    - L&W 462 / 447 (871); GP&T 654 / 652 (873); G&A (GAAP) 185 / 224 with "Less: Certain Items
      (see Endnote 2 to 1Q 2026 earnings release)" — (8) (68) (12) — (875); G&A (Non-GAAP) (2) 185
      216 171 174 171 (877); TOTI 338 / 283, refund all "—" (879); TOTI (Non-GAAP) (3) 338 283 309
      301 341 (881); Interest 66 66 71 51 47 (883); financing commitment — — — (6) — (885); Interest
      (Non-GAAP) (4) 66 66 71 45 47 (887).
    - (f) 1,705 1,672 1,637 1,389 1,400 (891); (g) 1,705 1,664 1,569 1,371 1,400 (892); DD&A 1,193
      1,226 1,169 1,053 1,013 (893); (h) 2,898 2,898 2,806 2,442 2,413 (894); (i) 2,898 2,890 2,738
      2,424 2,413 (895); Exploration 45 50 71 74 41; Dry Hole 23 4 — 11 34; Impairments 39 689 71 39
      44; Total Exploration (GAAP) 107 743 142 124 119 (896-899); "Less: Certain Impairments (5)" —
      (646) — (11) — (901); Total Exploration (Non-GAAP) 107 97 142 113 119 (905); (j) 3,005 3,641
      2,948 2,566 2,532 (906); (k) 3,005 2,987 2,880 2,537 2,532 (907).
    - Revenues less cost (909): GAAP 2,257 863 1,606 1,542 1,970; Non-GAAP 2,257 1,517 1,674 1,571
      1,970.
    - Per Boe GAAP (925-941): (b)/(a) 55.59 43.81 48.85 53.08 57.79; (c)/(a) 34.72 36.48 33.51
      36.15 38.84; (d)/(a) 20.87 7.33 15.34 16.93 18.95; (e)/(a) 42.24 34.99 38.05 39.80 45.88; (f)
      13.69 12.99 13.67 13.46 14.26; margin 28.55 22.00 24.38 26.34 31.62; (h) 23.27 22.52 23.44
      23.66 24.58; margin 18.97 12.47 14.61 16.14 21.30; (j) 24.13 28.29 24.63 24.86 25.79; margin
      18.11 6.70 13.42 14.94 20.09.
    - Per Boe Non-GAAP (945-955): (g) 13.69 12.93 13.10 13.30 14.26; margin 28.55 22.06 24.95 26.50
      31.62; (i) 23.27 22.46 22.87 23.50 24.58; margin 18.97 12.53 15.18 16.30 21.30; (k) 24.13
      23.21 24.06 24.59 25.79; margin 18.11 11.78 13.99 15.21 20.09.
  - Per-Boe annual 959-1078 (965 columns 2025 2024 2023 2022 2021):
    - (a) 449.8 388.7 359.4 331.5 302.5 (969); (b) 22,632 23,698 24,186 25,702 18,642; (c) 16,247
      15,616 14,583 15,736 12,540; (d) 6,385 8,082 9,603 9,966 6,102 (970-972).
    - Crude 12,501 13,921 13,748 16,367 11,125; NGLs 2,376 2,106 1,884 2,648 1,812; Gas 2,791 1,551
      1,744 3,781 2,444 (978-980); (e) 17,668 17,578 17,376 22,796 15,381 (982).
    - L&W 1,675 1,572 1,454 1,331 1,135 (986); GP&T 2,134 1,722 1,620 1,587 1,422 (988); G&A 820
      669 640 570 511 with "Less: Certain Items (see Endnote 7 to Additional Key Financial
      Information below)" (88) (10) — (16) — (990); G&A (Non-GAAP) (2) 732 659 640 554 511 (992);
      TOTI 1,234 1,249 1,284 1,585 1,047 with refund — 31 — 115 — (994); TOTI (Non-GAAP) (3) 1,234
      1,280 1,284 1,700 1,047 (996); Interest 235 138 148 179 178 with "Less: Acquisition-Related
      Financing Commitment Costs" (6) — — — — (998); Interest (Non-GAAP) (4) 229 138 148 179 178
      (1000).
    - (f) 6,098 5,350 5,146 5,252 4,293; (g) 6,004 5,371 5,146 5,351 4,293; DD&A 4,461 4,108 3,492
      3,542 3,651; (h) 10,559 9,458 8,638 8,794 7,944; (i) 10,465 9,479 8,638 8,893 7,944;
      Exploration 236 174 181 159 154; Dry Hole 49 14 1 45 71; Impairments 843 391 202 382 376;
      Total Exploration (GAAP) 1,128 579 384 586 601 (1004-1012); Less: Certain Impairments (5)
      (657) (291) (42) (113) (15) (1014); Total Exploration (Non-GAAP) 471 288 342 473 586; (j)
      11,687 10,037 9,022 9,380 8,545; (k) 10,936 9,767 8,980 9,366 8,530 (1018-1020).
    - Revenues less cost (1022): GAAP 5,981 7,541 8,354 13,416 6,836; Non-GAAP 6,732 7,811 8,396
      13,430 6,851.
    - Per Boe GAAP (1038-1054): (b)/(a) 50.32 60.97 67.30 77.53 61.63; (c)/(a) 36.12 40.18 40.58
      47.47 41.46; (d)/(a) 14.20 20.79 26.72 30.06 20.17; (e)/(a) 39.28 45.22 48.34 68.77 50.84;
      (f) 13.54 13.76 14.31 15.84 14.19; margin 25.74 31.46 34.03 52.93 36.65; (h) 23.46 24.33
      24.03 26.53 26.26; margin 15.82 20.89 24.31 42.24 24.58; (j) 25.97 25.82 25.10 28.30 28.25;
      margin 13.31 19.40 23.24 40.47 22.59.
    - Per Boe Non-GAAP (1058-1068): (g) 13.34 13.82 14.31 16.14 14.19; margin 25.94 31.40 34.03
      52.63 36.65; (i) 23.26 24.39 24.03 26.83 26.26; margin 16.02 20.83 24.31 41.94 24.58; (k)
      24.31 25.13 24.98 28.26 28.20; margin 14.97 20.09 23.36 40.51 22.64.
    - Footnotes (1)-(5) 1070-1078 (numbering as D05).
  - AKFI 1082-1203 (1086 columns 2025 2024 2023 2022 2021 Actual):
    - Crude Oil and Condensate Volumes (MBod): US 520.5 490.6 475.2 460.7 443.4; Trinidad 1.4 0.8
      0.6 0.6 1.5; Other International — — — — 0.1; Total 521.9 491.4 475.8 461.3 445.0
      (1092-1095).
    - NGL Total 288.2 245.9 223.8 197.7 144.5 (1097). Natural Gas Volumes (MMcfd): US 2,299 1,728
      1,551 1,315 1,210; Trinidad 230 220 160 180 217; "Other International1" 4 — — — 9; Total
      2,533 1,948 1,711 1,495 1,436 (1101-1104).
    - COE Volumes (MBoed): US 1,191.8 1,024.5 957.5 877.5 789.6; Trinidad 39.8 37.6 27.3 30.7
      37.7; Other International1 0.6 — — — 1.6; Total 1,232.2 1,062.1 984.8 908.2 828.9
      (1110-1113).
    - Benchmark (1117): WTI 64.78 75.72 77.61 94.23 67.96; HH 3.43 2.27 2.74 6.64 3.85.
    - Crude above (below) WTI2 (1121-1125): US 0.87 1.70 1.57 2.99 0.58; Trinidad (7.19) (11.29)
      (9.03) (8.07) (11.70); Other International1 0.36 — — — —.
    - NGL % of WTI 34.9 30.9 29.7 39.0 50.5% (1129). Gas above (below) HH3, US (0.49) (0.28)
      (0.04) 0.63 1.03 (1133).
    - Table 1137-1142: Natural Gas Realizations4 Trinidad 3.78 3.65 3.65 4.43 3.40; Other
      International1 3.28 — — — —; Total Expenditures (GAAP) ($MM) 13,703 6,653 6,818 5,610 4,255;
      Capital Expenditures5 (Non-GAAP) ($MM) 6,294 6,226 6,041 4,607 3,755.
    - Operating Unit Costs ($/Boe) (1148-1154): L&W 3.72 4.04 4.05 4.02 3.75; GP&T6 4.74 4.43 4.50
      4.78 4.70; G&A (GAAP) 1.82 1.72 1.78 1.72 1.69; G&A (Non-GAAP)7 1.63 1.70 1.78 1.67 1.69;
      Cash Operating Costs (GAAP) 10.28 10.19 10.33 10.52 10.14; (Non-GAAP)7 10.09 10.17 10.33
      10.47 10.14; DD&A 9.92 10.57 9.72 10.69 12.07.
    - Expenses ($MM) (1160-1165): Exploration and Dry Hole 285 188 182 204 225; Impairment (GAAP)
      843 391 202 382 376; Impairment (excluding certain impairments (Non-GAAP))8 186 100 160 269
      361; Capitalized Interest 86 45 33 36 33; Net Interest 235 138 148 179 178; "Net Interest
      (Non-GAAP)9" 229 — — — — (1165; new row).
    - TOTI %: GAAP 7.0 7.1 7.4 7.0 6.8 (1169); Non-GAAP7 7.0 7.3 7.4 7.5 6.8 (1171). Effective
      Rate 21.7 22.1 21.6 21.7 21.4% (1175); Current Tax Expense ($MM) 1,039 1,348 1,415 2,208
      1,393 (1177).
    - Continuation page titled "Additional Key Financial Information (Continued)" (1181-1183;
      D04/D05 used "Additional Key Information"). Endnotes 1185-1203: 1) "2025 production volumes
      are from Bahrain operations; natural gas realized price represents contract price less
      partner's processing and distribution costs." (1187); 2) WTI basis "simple average of the
      daily settlement prices for the prompt-month NYMEX futures contract for each of the
      applicable calendar months" (1189); 3) Henry Hub (1191); 4) Trinidad 2022 $0.76/Mcf (1193);
      5) Capital Expenditures scope (1195); 6) GP&T (1197); 7) Cash Operating Costs; "G&A
      (Non-GAAP) for fiscal year 2025 excludes costs related to the Encino acquisition"; per-Boe
      impacts "$(0.19), $(0.02) and $(0.05)" for FY2025, 2024 and 2022 (1199); 8) impairment
      exclusion, "$657 million" FY2025 (Barnett Shale and Woodford Oil Window) and "$291 million"
      FY2024 (Rocky Mountain area) (1201); 9) "Net Interest for fiscal year 2025 excludes
      financing commitment costs related to the Encino acquisition"; per-Boe "$(0.01)" (1203).
- Lists: 12 TOC entries. 7 Adjusted NI tables. Adjustment-row sets: 1Q26 MTM, settlements, gains
  on asset dispositions; 4Q25 and FY25 all five types (MTM, settlements, asset dispositions,
  certain impairments, acquisition-related costs). AKFI endnotes 1-9.
- Forecasts, guidance, deadlines, effective dates: none forward-looking. New effective date Jan
  1, 2026 (236). The Oct 1, 2024 Income Taxes Receivable footnote is not carried.
- Hedged claims: boilerplate; "accompanying earnings presentation slides" (314).
- Rounded prose beside exact figures: endnotes restate table amounts exactly ("$657 million",
  "$291 million" at 1201; per-Boe impacts at 1199, 1203).
- Notes:
  - Other International FY25 crude volume and price print "—" (108, 119; AKFI 1094) although 4Q25
    prints 0.1 and 63.98; the AKFI FY25 Other International crude differential prints 0.36
    (1125). No note explains this. AKFI 2021 prints Other International crude 0.1, gas 9, BOE 1.6
    (1094, 1103, 1112); endnote 1 describes only 2025 volumes.
  - Income-statement Impairments 4Q25 689 / FY25 843 (72) versus Certain Impairments 646 / 657
    (392, 534, 901, 1014) and AKFI Impairment (Non-GAAP) 186 (1162).
  - The Encino acquisition row prints +13 in 4Q25 (286); FY25 (4,451). No text explains the 13.
- Operative definitions, rules and scope exceptions: endnotes 1-9 as listed; footnote (B) 168.
- Amendments or contradictions (same-period differences against earlier editions, located):
  - Balance-sheet recast (footnote (A) 236): current-asset "Other" Sep 30 2025 = 665 (D06 191)
    versus D05 187 Other 646 plus D05 186 PRM assets 19; current-liability "Other" Mar/Jun/Sep 30
    2025 = 566 / 342 / 469 (D06 216) versus D05 213 Other 290 / 257 / 452 plus D05 210 PRM
    liabilities 276 / 85 / 17 (same in D04 204/201 for Mar/Jun). Totals unchanged.
  - Measure labels: "Acquisition-related costs" (D04 340, D05 350) -> "Acquisition-Related Costs"
    (D06 394, 428, 468); same amounts.
  - G&A labels now cite "Endnote 2 to 1Q 2026 earnings release" (quarterly, 875) and "Endnote 7
    to Additional Key Financial Information below" (annual, 990); the annual 2024 (10) and 2022
    (16) amounts are unchanged from D02 982 / D04 996 / D05 1019 "Severance Tax Consulting Fees".
  - WTI differential basis wording changed (endnote 2, 1189) versus D04 1179 / D05 1202 endnote 1;
    the 2024-2022 differential values are unchanged (D06 1123-1124 versus D04 1121, D05 1144).
  - FY24 Adjusted NI gains a Rocky Mountain impairment footnote (588) absent from D02 532 / D04
    536 / D05 549.
  - No numeric conflict found in any other shared cell (2025 Q1-Q3 income statement, volumes,
    cash flow, Adjusted NI, CFO/FCF, net debt and per-Boe; FY2024-FY2022 annual tables and AKFI).
- Coverage: full; every line 1-1205 of the current file read in four chunks (1-320, 321-620,
  621-920, 921-1205). No hidden markers.

## D07 - Second Quarter 2026 Supplemental Financial and Operating Data

- Source: docs/eog_ex991_2026-08-04.txt | text, no pages. Current text/D07.txt (re-extracted
  2026-10-05 after the splitter fix; the stray page-metadata first line is gone) has 1,207 lines
  and starts "# D07 | ...", blank, "EX-99.1". "2 exh99-1080426.htm" (5), "PRESS RELEASE OF EOG
  RESOURCES, INC." (7), "EXHIBIT 99.1" (11). Printed page numbers 9-29 run in sequence (9 at 43,
  10 at 91, 11 at 172, 12 at 238, 13 at 308, 14 at 328, 15 at 366, 16 at 440, 17 at 512, 18 at
  590, 19 at 649, 20 at 710, 21 at 768, 22 at 821, 23 at 844, 24 at 913, 25 at 959, 26 at 1026,
  27 at 1082, 28 at 1181, 29 at 1207). All line numbers below are for the current file.
- Written or submitted by: EOG Resources, Inc. No person is named.
- Type, date, edition: series edition "Second Quarter 2026 Supplemental Financial and Operating
  Data" (15); no printed issue date (file name 2026-08-04). TOC 13-43 (entries 17-41); page
  numbers equal D06's.
- Period covered and column convention: statement tables 8 value columns = 2025 Q1-Q4, 2025 Year,
  2026 Q1, Q2, 2026 Year (first-half YTD; NI 1,980 + 2,724 = 4,704). Balance sheet 6 value columns
  = Mar, Jun, Sep, Dec 2025, Mar, Jun 2026. Adjusted NI tables 2Q26, 1Q26, 4Q25, 3Q25, 2Q25, FY25,
  FY24 (1Q25 dropped). Bridges 1Q26 -> 2Q26. Annual CFO/FCF FY2024-FY2021. Net debt Jun 30 2026,
  Mar 31 2026, Dec 31 2025, Sep 30 2025, Jun 30 2025. Per-Boe quarterly 2Q26 1Q26 4Q25 3Q25 2Q25;
  annual 2025-2021. AKFI 2025-2021 Actual. Price footnote: Note 9 of the 10-Q for the quarter
  ended June 30, 2026 (168); balance-sheet footnote (B): Note 5 (236).
- Entities and aliases:
  - Footnote (B) 166: "Crude oil and condensate volumes are from UAE and Bahrain operations.
    Natural gas volumes are from Bahrain operations; natural gas realized price represents
    contract price less partner's processing and distribution costs." UAE appears only here.
    Rows labelled "Other International (B)": crude volume 108, gas volume 140, gas price 150; the
    crude-price row (119) and BOE row (160) print "Other International" without "(B)".
  - "Encino Acquisition Partners, LLC" (284); "Encino" at 334, 438, 478, 510, 552, 748, 1201,
    1205. Barnett Shale and Woodford Oil Window (436, 550, 1203); Rocky Mountain area (588, 1203).
- Tables (new columns; every overlapping cell was compared with D06 and is identical):
  - Income Statements 45-89, 2Q26 / 2026 Year (H1):
    - Revenues (55-62): Crude 4,901 / 8,478; NGLs 770 / 1,434; Natural Gas 812 / 1,833; MTM 40 /
      153; Gathering, Processing and Marketing 2,011 / 3,507; Gains (Losses) on Asset Dispositions
      58 / 89; Other, Net 28 / 47; Total 8,620 / 15,541.
    - Expenses (68-77): L&W 467 / 929; GP&T 676 / 1,330; Exploration 47 / 92; Dry Hole 30 / 53;
      Impairments 19 / 58; Marketing 1,950 / 3,334; DD&A 1,259 / 2,452; G&A 213 / 398; TOTI 431 /
      769; Total 5,092 / 9,415.
    - Operating Income 3,528 / 6,126; Other Income 38 / 61; Income Before Interest and Taxes
      3,566 / 6,187; Interest Expense, Net 67 / 133 (81); Income Before Income Taxes 3,499 /
      6,054; Income Tax Provision 775 / 1,350; Net Income 2,724 / 4,704 (84).
    - "Dividends Declared per Common Share" 2Q26 1.0200 / 2026 Year 2.0400 (85); 2025 columns as
      D06.
    - Line 89: EPS Basic 5.18 / 8.89; Diluted 5.15 / 8.84; shares Basic 526 / 529; Diluted 529 /
      532.
  - Volumes and Prices 93-170, 2Q26 / H1: crude US 546.2 / 546.3, Trinidad 2.1 / 2.0, Other
    International 0.5 / 0.3 (108), Total 548.8 / 548.6 (110); crude price US 98.18 / 85.40,
    Trinidad 88.87 / 79.20, Other International 103.40 / 101.81 (119), Composite 98.15 / 85.38
    (121); NGLs 346.8 / 339.5 (125, US and Total on one line); NGL price 24.41 / 23.34 (130-131);
    Natural Gas Volumes US 2,784 / 2,777, Trinidad 293 / 266, Other International 12 / 12, Total
    3,089 / 3,055 (138-141); gas price US 2.77 / 3.25, Trinidad 3.99 / 3.95 (146-147), Other
    International 3.27 / 3.27 (150), Composite 2.89 / 3.32 (152); COE Volumes US 1,357.1 /
    1,348.6, Trinidad 50.9 / 46.4, Other International 2.4 / 2.2, Total 1,410.4 / 1,397.2, Total
    MMBoe 128.3 / 252.9 (158-162).
  - Balance Sheets 174-236, Jun 30 2026 column (6th value): Cash 4,907 (186); AR 3,529;
    Inventories 930; Other (A) 511; Total current assets 9,877 (190); Oil and Gas Properties
    92,454; Other PP&E 7,064; Total PP&E 99,518; Accumulated DD&A (56,278); Net PP&E 43,240;
    Deferred Income Taxes 35; Other Assets 1,631; Total Assets 54,783 (196-203); Accounts Payable
    3,374; Accrued Taxes Payable 697; Dividends Payable 531 (211); Current Portion of Long-Term
    Debt 27 (212); Current Portion of Operating Lease Liabilities 324; Other (A) 382; Total current
    liabilities 5,335 (215); Long-Term Debt 7,899 (216); Other Liabilities 2,468; Deferred Income
    Taxes 7,217; Common Stock 206; APIC 6,072; AOCL (5); Retained Earnings 33,390; Treasury
    (7,799) (230); Total Stockholders' Equity 31,864 (231); Total L&SE 54,783 (232). Footnotes (A)
    234 (Jan 1, 2026 Price Risk Management change, repeated) and (B) 236.
  - Cash Flow Statements 240-306, 2Q26 / H1:
    - Net Income 2,724 / 4,704 (252). Non-cash (256-265): DD&A 1,259 / 2,452; Impairments 19 / 58;
      Stock-Based Compensation 60 / 118; Deferred Income Taxes 346 / 364; asset dispositions (58)
      / (89); Other, Net 2 / 17; Dry Hole 30 / 53; MTM (40) / (153); settlements 45 / (8); second
      "Other, Net" (1) / (1) (265).
    - Working capital (271-277): AR 60 / (847); Inventories 26 / 47; AP 176 / 455; Accrued Taxes
      Payable (69) / 398; Other Assets 47 / 102; Other Liabilities 37 / (86); WC investing 6 / 51.
      NCFO 4,669 / 7,635 (278).
    - Investing (284-289): Encino acquisition row — / — (284; 2025 columns as D06); Additions to
      Oil and Gas Properties (1,638) / (3,129); Additions to Other PP&E (144) / (297); Proceeds
      from Sales of Assets 7 / 151; WC investing (6) / (51); Net Cash Used in Investing (1,781) /
      (3,326).
    - Financing (295-302): Long-Term Debt Borrowings — / —; Long-Term Debt Repayments — / —;
      Dividends Paid (540) / (1,084) (297); Treasury Stock Purchased (1,299) / (1,717) (298);
      stock options/ESPP 15 / 16; Debt Issuance and Other Financing Costs — / —; finance leases
      (6) / (13); Net Cash Used in Financing (1,830) / (2,798) (302).
    - Effect of exchange rate – / — (303); Increase (Decrease) in Cash 1,058 / 1,511 (304);
      Beginning 3,849 / 3,396 (305); End 4,907 / 4,907 (306).
  - Non-GAAP Financial Measures 310-326.
  - Adjusted Net Income 330-588 (method 334 includes the Encino add-back):
    - 2Q26 (336-364): Reported 3,499 (775) 2,724 5.15 (344); Gains MTM (40) 9 (31) (0.06) (348);
      "Net Cash Received ..." 45 (9) 36 0.07 (350); "Less: Gains on Asset Dispositions, Net" (58)
      12 (46) (0.09) (354); Adjustments (53) 12 (41) (0.08) (355); Adjusted NI 3,446 (763) 2,683
      5.07 (356); shares 526/529 (360/362); "$45 million" (364). Complete.
    - 1Q26 (374-402), 4Q25 (404-438), 3Q25 (448-478), 2Q25 (480-510), FY25 (518-552), FY24
      (554-588): identical to D06, footnotes included.
  - NI per Share bridge 592-647 (1Q26 -> 2Q26): start 3.70 (596). Prices 50.52 less (42.24) =
    8.28 x 128.3 = 1,062; tax (234); NI 828; EPS 1.57 (600-606). Volumes 128.3 less (124.5) = 3.8
    x GAAP margin 25.51 = 97; tax (21); NI 76; EPS 0.14 (610-618). Costs: "1Q 2026 Total Cash
    Operating Costs (GAAP) and Total DD&A per Boe 20.03" (622) less 2Q26 (20.38) = (0.35) x 128.3
    = (45); tax 10; NI (35); EPS (0.07) (624-631). MTM 2Q26 40/(9)/31 less 1Q26 113/(24)/89; change
    (58); EPS (0.11) (633-639). Other (1) (0.08) (641); 2Q26 diluted 5.15 (643); 529 (645).
  - Adjusted NI per Share bridge 651-708: start 3.41 (655). Prices as above. Volumes x Non-GAAP
    margin 25.51 = 97; tax (21); NI 76; EPS 0.14 (669-675). Costs: 1Q26 (Non-GAAP) 20.03 (679)
    less 2Q26 (20.38) = (0.35); (45); 10; (35); (0.07) (681-688). Settlements 2Q26 45/(9)/36 less
    1Q26 (53)/11/(42); change 78; EPS 0.15 (690-700). Other (1) (0.13) (702); "2Q 2026 Adjusted
    Net Income per Share (Non-GAAP) 5.07" (704).
  - CFO and FCF 712-819:
    - Paragraph 716 identical to D06 718 ("second, third and fourth quarters of 2025").
    - NCFO ... | 2,966 4,669 / 7,635 (722). WC rows (730-736), 2Q26 / H1: AR (60) / 847;
      Inventories (26) / (47); AP (176) / (455); Accrued Taxes Payable 69 / (398); Other Assets
      (47) / (102); Other Liabilities (37) / 86; WC investing (6) / (51).
    - Acquisition-Related Costs, Net of Tax: 2026 "— — —" (740). Adjusted CFO ... | 3,129 4,386 /
      7,515 (742). Capex ... | (1,636) (1,587) / (3,223) (744). FCF ... | 1,493 2,799 / 4,292
      (746). Footnote (1) 748 as D06 750.
    - Reconciliation (756-766), 2026 Q1 Q2 / H1: Total Expenditures 1,768 1,919 / 3,687 (756);
      ARC (12) (37) / (49) (758); Non-Cash Leasehold Acquisition Costs (3) (52) (53) / (105)
      (760); new row "Non-Cash Property Acquisition Costs" — (all 2025 and 1Q26) (2) / (2) (762);
      Acquisition Costs of Properties (3) (23) (193) / (216) (764); Exploration Costs (45) (47) /
      (92) and Total Capex 1,636 1,587 / 3,223 (766). 2025 columns as D06.
    - Annual FY2024-FY2021 table 770-819: identical to D06 (title split "Cash Flow from
      Operations and Free Cash Flow" / "(Continued)", 770-772).
  - Net Debt 823-842 (829 dates): Jun 30 2026 column: equity 31,864; debt 7,926 (= 27 + 7,899);
    cash (4,907); Net Debt 3,019; Total Cap (GAAP) 39,790; Total Cap (Non-GAAP) 34,883 (833-838);
    19.9% (840); 8.7% (842). Other four dates as D06.
  - Per-Boe quarterly 846-957 (852 columns 2Q26 1Q26 4Q25 3Q25 2Q25), 2Q26 column:
    - (a) 128.3; (b) 8,620; (c) 5,092; (d) 3,528 (856-859); Crude 4,901; NGLs 770; Gas 812
      (865-867); (e) 6,483 (869); L&W 467; GP&T 676 (873-875).
    - G&A (GAAP) 213 with "Less: Certain Items (see Endnote 2 to 2Q 2026 earnings release)" — —
      (8) (68) (12) (877); G&A (Non-GAAP) (2) 213 185 216 171 174 (879); TOTI 431, refund all "—"
      (881); TOTI (Non-GAAP) (3) 431 (883); Interest 67 66 66 71 51 (885); financing commitment —
      — — — (6) (887); Interest (Non-GAAP) (4) 67 66 66 71 45 (889).
    - (f) 1,854; (g) 1,854; DD&A 1,259; (h) 3,113; (i) 3,113; Exploration 47; Dry Hole 30;
      Impairments 19; Total Exploration (GAAP) 96 (893-901); Less: Certain Impairments (5) — —
      (646) — (11) (903); Total Exploration (Non-GAAP) 96; (j) 3,209; (k) 3,209 (907-909).
    - Revenues less cost (911): GAAP 3,274 2,257 863 1,606 1,542; Non-GAAP 3,274 2,257 1,517
      1,674 1,571.
    - Per Boe 2Q26 (927-957): (b)/(a) 67.19; (c)/(a) 39.69; (d)/(a) 27.50; (e)/(a) 50.52; GAAP =
      Non-GAAP: (f)/(g) 14.45; margin 36.07; (h)/(i) 24.26; margin 26.26; (j)/(k) 25.01; margin
      25.51.
  - Per-Boe annual 961-1080: every value identical to D06 (969-1070); footnotes 1072-1080.
  - AKFI 1084-1205: every value identical to D06 (crude 1094-1097; NGL and gas 1099-1106; COE
    1112-1115; benchmarks 1119; differentials 1121-1127; NGL % 1131; HH 1135; realizations and
    expenditures 1141-1144; unit costs 1150-1156; expenses 1162-1167; TOTI 1171-1173; tax
    1177-1179). The BOE (1114) and crude-differential (1127) "Other International" rows print no
    endnote "1" (D06 1112, 1125 print "Other International1"). Continuation title "Additional Key
    Financial Information (Continued)" (1183-1185). Endnotes 1187-1205.
- Lists: 12 TOC entries. 7 Adjusted NI tables. 2Q26 adjustment rows: MTM, settlements, gains on
  asset dispositions (no impairment row; income-statement Impairments 2Q26 = 19, per-Boe Certain
  Impairments "—"). The 2026 capex reconciliation has five reconciling rows plus the total. AKFI
  endnotes 1-9.
- Forecasts, guidance, deadlines, effective dates: none forward-looking. Balance-sheet footnote
  (A) 234 repeats the Jan 1, 2026 change.
- Hedged claims: boilerplate.
- Rounded prose beside exact figures: none beyond the endnote restatements repeated from D06.
- Notes: 2Q 2026 and Jun 30 2026 values appear only in D07 (no second edition).
- Operative definitions, rules and scope exceptions (endnote wording changes versus D06):
  - Endnote 1 (1189): "2025 volumes are from Bahrain operations" (D06 1187: "2025 production
    volumes").
  - Endnote 2 (1191): "United States, Trinidad and Other International crude oil and condensate
    price differentials" (D06 1189: "United States and Trinidad").
  - Endnote 5 (1197): "Capital Expenditures include ... Capital Expenditures exclude ..." (D06
    1195: "includes ... excludes").
  - Endnotes 7-9 (1201-1205) match D06 1199-1203.
- Amendments or contradictions: no new effective-date change. The geographic footnote broadens
  from Bahrain (D06 168) to "UAE and Bahrain" for crude volumes (D07 166). No numeric conflict with
  D06 in any shared cell (2025 quarters and FY, 1Q26, Mar 2025-Mar 2026 balances, Adjusted NI,
  bridges' shared values, CFO/FCF, net debt, per-Boe, annual tables, AKFI).
- Coverage: full; every line 1-1207 of the current file read in four chunks (1-320, 321-620,
  621-920, 921-1207). No hidden markers.

## Shared ground (navigation only)

Facts and locations only. The series never cites D01 or D03; every relationship below is a
location pairing, not a document-stated link, unless a quoted label names it.

### Entities that appear in more than one document, and where

- EOG Resources, Inc.: issuer of all seven documents. No other issuer.
- Encino:
  - D03: "Encino Acquisition Partners (EAP or Encino)" (19); sellers "Canada Pension Plan
    Investment Board (CPP)" / "CPP Investments" and "Encino Energy" (17, 19); "the Transaction"
    = "the proposed acquisition of Encino/EAP" (77).
  - Series: the full name "Encino Acquisition Partners, LLC" appears only in the cash-flow row
    (D05 280, D06 286, D07 284). "Encino" / "the Encino acquisition": D04 354, 759; D05 330, 364,
    406, 773; D06 336, 410, 442, 482, 552, 750, 1199, 1203; D07 334, 438, 478, 510, 552, 748,
    1201, 1205.
  - Not in any series edition (grep-checked): "EAP", CPP, Encino Energy, Goldman Sachs or the
    other advisors, Hart-Scott-Rodino, "Utica", "synergies", "EBITDA", "pro forma", any closing
    statement or closing date.
- Trinidad: reserve countries D01 49 and D03 63; volume and price rows in all series editions;
  the 2022 Trinidad gas-price endnote naming "National Gas Company of Trinidad and Tobago
  Limited" (D04 1183, D05 1206, D06 1193, D07 1195).
- Other International / Bahrain / UAE / China:
  - D05 footnote (C) 165 ("Kingdom of Bahrain", "Bapco's"); rows 137, 147, 157.
  - D06 footnote (B) 168 ("Bahrain", "partner's"); rows 108, 119, 142, 152, 162; AKFI endnote 1
    (1187) and rows 1094, 1103, 1112, 1125, 1140.
  - D07 footnote (B) 166 ("UAE and Bahrain" crude; "Bahrain" gas); rows 108, 119, 140, 150, 160;
    AKFI endnote 1 (1189) and rows 1096, 1105, 1114, 1127, 1142.
  - China: D01 49 only. UAE: D07 166 only. Bapco: D05 165 only.
  - AKFI FY2021 prints Other International crude 0.1 MBod, gas 9 MMcfd and BOE 1.6 MBoed (D06
    1094/1103/1112; D07 1096/1105/1114). No document names the 2021 country.
- Plays: Delaware Basin and Eagle Ford (D01 37 "South Texas Eagle Ford"; D03 21). Utica: D03
  only (21, 31, 39). Barnett Shale and Woodford Oil Window: D06 408, 550, 1201; D07 436, 550,
  1203. Rocky Mountain area: D06 588, 1201; D07 588, 1203.
- People: Neel Panchal (D01 55, D03 69; same number 713-571-4884); Kimberly Ehmer (D01 59 "Media
  and Investor Contact"; D03 75 "Media Contact"; 713-571-4676); "Chairman and Chief Executive
  Officer": William R. "Bill" Thomas (D01 39) and Ezra Y. Yacob (D03 21). D01 only: David Streit.
  D03 only: Pearce Hammond, Shelby O'Connor. No person is named in the series.
- Filings, regulators and market terms: SEC reserve passage (D01 117, D03 211); 10-K risk
  factors (D01 113 FY2019; D03 203 FY2024); 10-Q Note 10 (D02 156, D04 156, D05 163), Note 9 (D06
  170, D07 168), Note 5 (D06 238, D07 236). WTI: D03 47 ("$45 WTI") and AKFI benchmarks (D04 1117,
  D05 1140, D06 1117, D07 1119). NYMEX and Henry Hub: AKFI endnotes.
- Issuer versus mentioned organizations: EOG wrote every document. Mentioned only: CPP, Encino
  Energy, EAP, Goldman Sachs & Co. LLC, Goldman Sachs Bank USA, Wachtell, Lipton, Rosen & Katz,
  Akin Gump Strauss Hauer & Feld LLP (D03 17-19, 59); SEC (D01, D03); National Gas Company of
  Trinidad and Tobago Limited (AKFI); Bapco (D05 165); the unnamed "partner" (D06 168, D07 166).

### Periods or series that more than one document covers, and where

| Period | Statement columns (income, volumes, cash flow, CFO/FCF) | Balance-sheet date | Adjusted NI table | Net-debt date | Per-Boe column | Bridge / AKFI |
|---|---|---|---|---|---|---|
| 1Q24 | D02 D04 D05 | Mar 31 2024: D02 D04 D05 | D02 | D02 | D02 | — |
| 2Q24 | D02 D04 D05 | Jun 30 2024: D02 D04 D05 | D02 D04 | D02 D04 | D02 D04 | — |
| 3Q24 | D02 D04 D05 | Sep 30 2024: D02 D04 D05 | D02 D04 D05 | D02 D04 D05 | D02 D04 D05 | — |
| 4Q24 | D02 D04 D05 | Dec 31 2024: D02 D04 D05 | D02 D04 D05 | D02 D04 D05 | D02 D04 D05 | bridge start D02 |
| FY24 | Year column D02 D04 D05; annual CFO/FCF D06 D07 | — | all five | — | annual, all five | AKFI D04-D07 |
| FY23, FY22 | annual CFO/FCF, all five | — | FY23: D02 D04 D05 | — | annual, all five | AKFI D04-D07 |
| FY21 | annual CFO/FCF D06 D07 | — | — | — | D06 D07 | AKFI D06 D07 |
| 1Q25 | all five | Mar 31 2025: all five | D02 D04 D05 D06 | D02 D04 D05 D06 | D02 D04 D05 D06 | end D02, start D04 |
| 2Q25 | D04 D05 D06 D07 | Jun 30 2025: D04 D05 D06 D07 | D04 D05 D06 D07 | D04 D05 D06 D07 | D04 D05 D06 D07 | end D04, start D05 |
| 3Q25 | D05 D06 D07 | Sep 30 2025: D05 D06 D07 | D05 D06 D07 | D05 D06 D07 | D05 D06 D07 | end D05 |
| 4Q25 | D06 D07 | Dec 31 2025: D06 D07 | D06 D07 | D06 D07 | D06 D07 | start D06 |
| FY25 | D06 D07 | — | D06 D07 | — | D06 D07 | AKFI D06 D07 |
| 1Q26 | D06 D07 | Mar 31 2026: D06 D07 | D06 D07 | D06 D07 | D06 D07 | end D06, start D07 |
| 2Q26 | D07 | Jun 30 2026: D07 | D07 | D07 | D07 | end D07 |

Year-to-date columns printed once each: H1 2025 (D04), 9M 2025 (D05), H1 2026 (D07). Dec 31,
2019 balances and the 2020 plan: D01 only. The Encino agreement, the dividend declaration and the
acreage: D03 only.

### Same-period consistency across editions

- Every overlapping cell was compared (income statements, volumes, balance sheets, cash-flow
  statements, Adjusted NI tables, bridge values that recur, CFO/FCF and capex reconciliations, net
  debt, quarterly and annual per-Boe, AKFI). No same-labelled figure is restated in a later
  edition.
- Same-period figures that differ only through a presentation recast or relabel (both
  locations):
  1. Balance-sheet "Other" after the Jan 1, 2026 Price Risk Management fold-in (D06 236, D07 234):
     current-asset Other Sep 30 2025 = 665 (D06 191, D07 189) versus D05 187 Other 646 plus D05
     186 PRM assets 19; Mar/Jun 2025 563/591 unchanged (PRM assets "—"). Current-liability Other
     Mar/Jun/Sep 30 2025 = 566/342/469 (D06 216, D07 214) versus 290/257/452 (D05 213; D04 204 for
     Mar/Jun; D02 204 for Mar) plus PRM liabilities 276/85/17 (D05 210; D04 201; D02 201). Totals
     unchanged. 2024 PRM rows (assets 110/4/—/—, liabilities —/8/32/116; D02 177, 201) are not
     reprinted after the recast.
  2. "Cash Flow from Operations Before Changes in Working Capital (Non-GAAP)" (D02 744, 792) ->
     "Adjusted Cash Flow from Operations (Non-GAAP)" (D04 753, 801; D05 767, 818; D06 744, 791;
     D07 742, 793). Values identical: 2024 quarters 2,928 3,042 2,988 2,635, FY24 11,593, 1Q25
     2,813, FY23 11,149, FY22 12,252.
  3. Capex reconciling rows relabelled (footnote (3): D05 846, D06 817, D07 819): "Non-Cash
     Acquisition Costs of Unproved Properties" (D02 763, 810; D04 772, 819) -> "Non-Cash Leasehold
     Acquisition Costs" (D05 785, 836; D06 762, 805; D07 760, 807); "Acquisition Costs of Proved
     Properties" (D02 764, 811; D04 773, 820) -> "Acquisition Costs of Properties" (D05 787, 838;
     D06 764, 809; D07 764, 811). Amounts identical (e.g. 2Q25 (270): D04 773, D05 787, D06 764,
     D07 764).
  4. Financing row "Debt Issuance Costs" (D02 285) -> "Debt Issuance and Other Financing Costs"
     (D04 286 onward); 4Q24 (2) unchanged.
  5. G&A adjustment label "Severance Tax Consulting Fees" (quarterly D02 872; annual D02 982, D04
     996, D05 1019) -> "Certain Items" citing earnings-release endnotes (quarterly D04 881, D05
     904, D06 875, D07 877) or "Endnote 7 to Additional Key Financial Information below" (annual
     D06 990, D07 992). 3Q24 (10), FY24 (10) and FY22 (16) unchanged.
  6. "Acquisition-related costs" (D04 340; D05 350, 392) -> "Acquisition-Related Costs" (D06 394,
     428, 468; D07 422, 464, 496); amounts unchanged.
  7. Per-Boe interest: inside the cost table in D02 (882 quarterly, 992 annual) -> separate GAAP
     and Non-GAAP rows (quarterly from D04 889-893; annual from D06 998-1000).
  8. FY24 Certain Impairments row gains a Rocky Mountain footnote (D06 588, D07 588); D02 532, D04
     536, D05 549 print it without a footnote. Amount 291 unchanged.
  9. WTI-differential basis wording (D04 1179, D05 1202 -> D06 1189, D07 1191); 2024-2022
     differential values unchanged (D04 1121, D05 1144, D06 1123-1124, D07 1125-1126).
- Arithmetic ties (navigation aids): quarterly Adjusted NI rows sum to FY rows (FY24 impairments 2
  + 35 + 254 = 291; asset dispositions (26) + (20) + 7 + 23 = (16); FY25 asset dispositions 1 + 18
  + 16 = 35; impairments 11 + 646 = 657; acquisition costs 18 + 68 + 8 = 94). Net-debt (b) equals
  balance-sheet current portion plus long-term debt in every edition. Per-Boe (a) equals the
  volume table's Total MMBoe.

### Edition relationships and amendment order (located)

1. Jan 1, 2024 GP&T combination: all five editions (Series layout).
2. Oct 1, 2024 Income Taxes Receivable into Other: D02 224, D04 224, D05 233; not carried in
   D06/D07.
3. 2Q 2025 edition: CFO measure renamed and acquisition-cost add-back begins (D04 727); add-back
   quarters "second and third" (D05 741) and "second, third and fourth quarters of 2025" (D06 718,
   D07 716).
4. 3Q 2025 edition: reconciling-row descriptions revised (D05 846; repeated D06 817, D07 819).
5. Jan 1, 2026 Price Risk Management Activities into Other (D06 236, D07 234).
6. Bridge "Other (1)" footnote: D02 647/715 -> D04 651/719 add "(for GAAP earnings per share
   only)", "exploration costs, dry hole costs" and "the impact of share repurchases on diluted
   shares" -> D05 664/733, D06 649/710, D07 647/708 read "impairments, marketing costs".
7. Other International footnote: D05 165 (Kingdom of Bahrain; Bapco) -> D06 168 (Bahrain;
   partner) -> D07 166 (UAE and Bahrain crude; Bahrain gas).
8. 10-Q note in price footnote: Note 10 (D02/D04/D05) -> Note 9 (D06/D07). "Commitments and
   Contingencies (B)" with Note 5 from D06 (222/238; D07 220/236).
9. "investor presentation slides" (D02 297, D04 298, D05 308) -> "earnings presentation slides"
   (D06 314, D07 312).
10. AKFI from D04 on (absent in D02); endnotes 7 (D04/D05) -> 9 (D06/D07); continuation title
    "Additional Key Information (Continued)" (D04 1173, D05 1196) -> "Additional Key Financial
    Information (Continued)" (D06 1181, D07 1183).
11. Rows appearing late: "Long-Term Debt Repayments" (from D04 282); "Acquisition of Encino
    Acquisition Partners, LLC, Net of Cash Acquired" (from D05 280); Other International gas rows
    (from D05 137/147) and crude rows (from D06 108/119); a second cash-flow "Other, Net" row (D06
    267, D07 265); "Non-Cash Finance Leases" FY2021 (D06 807, D07 809); AKFI "Net Interest
    (Non-GAAP)" (D06 1165, D07 1167); "Non-Cash Property Acquisition Costs" (D07 762 only).
12. Rows dropped: PRM asset/liability rows (after D05); "Acquisition Costs of Other Property,
    Plant and Equipment" in the 2025-2026 quarterly reconciliation (dashes for 2025 in D05 791;
    absent in D06/D07); each edition drops the oldest Adjusted NI table and net-debt date.
13. Annual CFO/FCF, per-Boe and AKFI tables gain FY2021 and FY2025 columns in D06.

### D03 (May 30, 2025 Encino agreement and dividend) and series rows reporting corresponding actual figures

- Price and funding (D03 19: "$5.6 billion, inclusive of EAP's net debt"; "currently expects to
  fund the acquisition through $3.5 billion of debt and $2.1 billion of cash on hand"):
  - "Acquisition of Encino Acquisition Partners, LLC, Net of Cash Acquired": 3Q25 (4,464), 9M
    (4,464) (D05 280); 3Q25 (4,464), 4Q25 13, FY25 (4,451) (D06 286, D07 284). All earlier
    columns "—"; 1H 2026 "—" (D07 284).
  - Capex reconciliation "Acquisition Costs of Properties": 3Q25 (6,736), 9M (7,005) (D05 787);
    FY25 (7,003) (D06 764, D07 764). Total Expenditures (GAAP): 3Q25 8,544, 9M 11,973 (D05 781);
    FY25 13,703 (D06 758, D07 756; AKFI D06 1141, D07 1143). AKFI endnote 4/5 excludes "Property
    Acquisitions" from Capital Expenditures (D04 1185, D05 1208, D06 1195, D07 1197).
  - Long-Term Debt Borrowings: 3Q25 3,472 (D05 291; D06 297; D07 295); 4Q25 999; FY25 4,471 (D06
    297; D07 295). Earlier: 4Q24 985 (D02 281; D04 281; D05 291).
  - Long-Term Debt Repayments: 2Q25 (500) (D04 282); 3Q25 (1,266) (D05 292); 4Q25 (750); FY25
    (2,516) (D06 298; D07 296). None in 1H 2026 (D07 296).
  - Debt Issuance and Other Financing Costs: 2Q25 (7), 3Q25 (7), 4Q25 (11), FY25 (25) (D06 302;
    D07 300).
  - Debt balances (Current Portion of LTD / Long-Term Debt): Jun 30 2025 778 / 3,458 (D04
    202/206); Sep 30 2025 27 / 7,667 (D05 211/215); Dec 31 2025 27 / 7,909; Mar 31 2026 27 / 7,904
    (D06 214/218); Jun 30 2026 27 / 7,899 (D07 212/216). Net-debt table (b): 4,236 (D04 838);
    7,694 (D05 861); 7,936 and 7,931 (D06 832); 7,926 (D07 834).
  - Cash and Cash Equivalents: Mar 31 2025 6,599; Jun 30 2025 5,216 (D04 174, 292); Sep 30 2025
    3,530 (D05 183, 302); Dec 31 2025 3,396 (D06 188, 308); Mar 31 2026 3,849; Jun 30 2026 4,907
    (D07 186, 306). 3Q25 Increase (Decrease) in Cash (1,686) (D05 300).
  - Net Debt (c) and ratios: Jun 30 2025 (980), 12.7% / -3.5% (D04 840-846); Sep 30 2025 4,164,
    20.3% / 12.1% (D05 863-869); Dec 31 2025 4,540, 21.0% / 13.2% (D06 834-840); Jun 30 2026 3,019,
    19.9% / 8.7% (D07 836-842).
  - Balance sheet Jun 30 -> Sep 30 2025: Oil and Gas Properties 80,139 -> 88,301 (D05 194);
    Deferred Income Taxes (liability) 6,015 -> 6,936 (D05 217); Total Assets 46,284 -> 52,199 (D05
    201).
  - No series row is labelled as debt assumed. No series text states EAP's net debt, the $5.6
    billion price or a debt/cash funding split.
  - Pre-closing 2Q25 "Acquisition Costs of Proved Properties" (270) (D04 773; later "Acquisition
    Costs of Properties", D05 787) carries no Encino label.
- Financing commitment (D03 59: Goldman Sachs Bank USA "is the sole provider of fully committed
  financing"): "financing commitment costs ($6 million)" for 2Q25 (D04 354; D05 406; D06 482,
  552; D07 510, 552); per-Boe "Less: Acquisition-Related Financing Commitment Costs" (6) at 2Q25
  (D04 891, D05 914, D06 885, D07 887) and FY25 (D06 998, D07 1000); AKFI "Net Interest
  (Non-GAAP)" 229 versus Net Interest 235 (D06 1164-1165, D07 1166-1167); endnote 9 (D06 1203, D07
  1205). The series does not name the lender.
- Acquisition-related G&A: 2Q25 $12 million (D04 354, 759); 3Q25 $68 million (D05 364, 773); 4Q25
  $8 million (D06 410, 750); FY25 $88 million (D06 552; per-Boe annual G&A Certain Items (88), D06
  990, D07 992; AKFI endnote 7, D06 1199, D07 1201). Adjusted NI before tax 18 / 68 / 8 / FY 94
  (D04 340; D05 350; D06 394, 536). CFO add-back net of tax 10 / 58 / 5 / FY 73 (D04 751; D05 765;
  D06 742; D07 740); 2026 "—" (D07 740).
- Expected closing (D03 49: "expected to occur in the second half of 2025"; Hart-Scott-Rodino
  clearance and customary conditions): the acquisition cash-flow row is first populated in the
  3Q25 column (D05 280). No series text states that the acquisition closed or gives a date.
- Dividend (D03 17 "Increases Regular Dividend 5%"; D03 47 "today declared a dividend of $1.02 per
  share", "payable October 31, 2025, to stockholders of record as of October 17, 2025", "indicated
  annual rate is $4.08"):
  - "Dividends Declared per Common Share": 2024 0.9100 0.9100 0.9100 0.9750 / FY 3.7050 and 1Q25
    0.9750 (D02 83); 2Q25 1.9950, H1 2.9700 (D04 83); 3Q25 "—", 9M 2.9700 (D05 85); 4Q25 1.0200,
    FY25 3.9900 (D06 85, D07 85); 1Q26 1.0200 (D06 85); 2Q26 1.0200, H1 2026 2.0400 (D07 85).
  - Dividends Payable: 2024 523 516 513 539 (D02 200); Mar 31 2025 534; Jun 30 2025 1,081 (D04
    200); Sep 30 2025 550 (D05 209); Dec 31 2025 544; Mar 31 2026 541 (D06 213); Jun 30 2026 531
    (D07 211).
  - Dividends Paid: 2024 (525) (520) (533) (509) / (2,087) (D02 282); 2025 (538) (528) (545) (550) /
    (2,161) (D06 299); 2026 (544) (540) / (1,084) (D07 297).
  - The series prints no declaration, record or payment date and does not link any dividend row
    to the May 30, 2025 declaration.
- Production (D03 31: "Pro forma production totals 275,000 barrels of oil equivalent per day
  creating a leading producer in the Utica shale play"; acreage 31, 39): no Utica, Encino or
  acquired-asset production line exists in the series. Company totals, MBoed (US / Total): 2Q25
  1,090.9 / 1,134.1 (D04 149, 151); 3Q25 1,260.7 / 1,301.2 (D05 155, 158); 4Q25 1,363.0 / 1,399.0;
  FY25 1,191.8 / 1,232.2 (D06 160, 163; AKFI D06 1110, 1113); 1Q26 1,340.1 / 1,383.8 (D06 160,
  163); 2Q26 1,357.1 / 1,410.4 (D07 158, 161). US natural gas MMcfd 1,977 (2Q25), 2,511 (3Q25),
  2,859 (4Q25) (D06 140); US NGLs MBbld 258.4, 309.3, 342.1 (D06 125); US crude MBbld 503.1, 532.9,
  544.5 (D06 104).
- Accretion, synergies, leverage target (D03 35, 43, 47): no EBITDA, synergy or debt-to-EBITDA
  figure in any series edition. Related series measures: FY25 NCFO 10,044, Adjusted CFO 10,957,
  FCF 4,663 (D06 724, 744, 748); FY24 12,143 / 11,593 / 5,367 (D06 776, 791, 797).
- Guidance (D03 49: capital and volume guidance "will be provided after closing"): no guidance in
  the series files.
- Reserve countries (D03 63 "United States and Trinidad"; D01 49 "United States, Trinidad, and
  China"): the series adds Other International production (Bahrain from 3Q25, D05 165; "UAE and
  Bahrain" crude, D07 166).

### D01 (March 16, 2020 plan; Dec 31, 2019 capitalization) and the series

- 2020 capex "$4.3 billion to $4.7 billion", including "facilities and gathering, processing and
  other expenditures" and "excluding acquisitions and non-cash exchanges" (D01 35; headline 19).
  No 2020 actual exists in the bundle. Series Capital Expenditures scope (AKFI endnote 4/5:
  excludes "Property Acquisitions, Asset Retirement Costs, Non-Cash Exchanges and Transactions and
  exploration costs incurred as operating expenses"; D04 1185, D05 1208, D06 1195, D07 1197).
  Earliest series Total Capital Expenditures (Non-GAAP): FY2021 3,755; FY2022 4,607; FY2023 6,041;
  FY2024 6,226; FY2025 6,294 (D06 795/815, 1142; D07 797/817, 1144). Total Expenditures (GAAP)
  FY2021 4,255 (D06 801; D07 803).
- 2020 crude production "446,000 to 466,000 barrels of oil per day, approximately flat compared to
  full-year 2019 levels" (D01 35). No 2019 or 2020 volume in the bundle. Earliest series annual
  crude (MBod): FY2021 total 445.0 (US 443.4, Trinidad 1.5, Other International 0.1) (D06
  1092-1095; D07 1094-1097); FY2022 461.3 and FY2023 475.8 (D04 1097; D05 1120); FY2024 491.4;
  FY2025 521.9 (D06 1095).
- Funding claim (D01 35, CFO "is expected to fund both capital expenditures and dividend payments
  assuming mid-$30 oil prices for the remainder of 2020"): no 2020 actuals. FY2021 WTI 67.96 (D06
  1117); FY2021 NCFO 8,791 and FCF 5,554 (D06 776, 797).
- Dec 31, 2019 net debt table (D01 145-201): equity 21,641; debt 5,175; cash (2,028); net debt
  3,147; Total Capitalization 26,816 / 24,788; 19% / 13% (whole percents), with rounded prose
  "$5.2 billion", "$2.0 billion", "19 percent", "13 percent" (D01 41). Series net-debt tables
  repeat the formula labels and the international-cash sentence (D01 153; D02 822; D04 831; D05
  854; D06 825; D07 827) with one-decimal percents for Mar 31, 2024 - Jun 30, 2026. No balance
  between Dec 31, 2019 and Mar 31, 2024 is printed.
- D01 61 names forward-looking non-GAAP measures "such as free cash flow or discretionary cash
  flow"; series FCF definitions are located in Series layout. D01 ATROR long form and box
  (123-143) versus the series short form (Series layout).

### Narrative, footnote or overview passages that repeat table results

- D01 41 restates the D01 net-debt table in rounded form.
- Adjusted NI footnote (1) restates each table's before-tax settlement amount ("$38 million",
  etc.).
- Acquisition-cost footnotes restate the Adjusted NI, CFO add-back and per-Boe amounts (locations
  above).
- AKFI endnotes 6/7 (per-Boe consulting-fee and acquisition-cost impacts: D04 1189, D05 1212, D06
  1199, D07 1201), 8 ("$657 million" / "$291 million": D06 1201, D07 1203) and 9 ("$(0.01)": D06
  1203, D07 1205).
- AKFI rows repeat other tables: Total Expenditures and Capital Expenditures = CFO/FCF
  reconciliation totals; Net Interest = per-Boe annual interest; Impairment (GAAP) =
  income-statement Impairments; Exploration and Dry Hole = Exploration Costs + Dry Hole Costs
  (FY25 236 + 49 = 285, D06 1160); AKFI volumes = the Volumes and Prices "Year" columns (FY25 crude
  521.9: D06 110 and 1095).
- Bridges repeat per-Boe revenue and margins, prior and current MMBoe and prior adjusted EPS.
- Captured platform overviews: not opened; navigation only, never evidence.

### Item sets, located

- Adjusted NI adjustment types by period (before-tax amounts):
  - 1Q24: Gains MTM (237), settlements 55, gains on asset dispositions (26), Certain Impairments 2
    (D02 490-497).
  - 2Q24: Losses MTM 47, settlements 79, gains on asset dispositions (20), Certain Impairments 35
    (D02 451-458; D04 494-501).
  - 3Q24: Gains MTM (79), settlements 61, losses on asset dispositions 7, Severance Tax Refund (31),
    Severance Tax Consulting Fees 10, Interest on Severance Tax Refund (5) (D02 410-419; D04
    453-462; D05 505-514).
  - 4Q24: Losses MTM 65, settlements 19, losses on asset dispositions 23, Certain Impairments 254
    (D02 371-378; D04 414-421; D05 466-473).
  - FY24: (204), 214, (16), 291, (31), 10, (5) (D02 525-535; D04 529-539; D05 542-552; D06 564-576;
    D07 564-576).
  - FY23: (818), (112), (95), 42 (D02 563-570; D04 567-574; D05 580-587).
  - 1Q25: Losses MTM 191, settlements (38), losses on asset dispositions 1 (D02 333-339; D04
    376-382; D05 428-434; D06 494-500).
  - 2Q25: Gains MTM (107), settlements (24), Certain Impairments 11, acquisition-related 18 (D04
    334-340; D05 386-392; D06 462-468; D07 490-496).
  - 3Q25: Gains MTM (116), settlements 27, losses on asset dispositions 18, acquisition-related 68
    (D05 344-350; D06 422-428; D07 458-464).
  - 4Q25: Losses MTM 19, settlements (21), losses on asset dispositions 16, Certain Impairments
    646, acquisition-related 8 (D06 386-394; D07 414-422).
  - FY25: (13), (56), 35, 657, 94 (D06 528-536; D07 528-536).
  - 1Q26: Gains MTM (113), settlements (53), gains on asset dispositions (31) (D06 350-356; D07
    386-392).
  - 2Q26: Gains MTM (40), settlements 45, gains on asset dispositions (58) (D07 348-354).
- Adjusted Net Income (Non-GAAP) after tax / adjusted diluted EPS: 1Q24 1,626 / 2.82; 2Q24 1,807
  / 3.16; 3Q24 1,644 / 2.89; 4Q24 1,535 / 2.74; FY24 6,612 / 11.62; FY23 6,825 / 11.69; 1Q25 1,586
  / 2.87; 2Q25 1,268 / 2.32; 3Q25 1,472 / 2.71; 4Q25 1,222 / 2.27; FY25 5,548 / 10.16; 1Q26 1,825 /
  3.41; 2Q26 2,683 / 5.07 (lines in each document section).
- Income-statement Impairments / Certain Impairments: 1Q24 19 / 2; 2Q24 81 / 35; 3Q24 15 / —; 4Q24
  276 / 254; FY24 391 / 291; 1Q25 44 / —; 2Q25 39 / 11; 3Q25 71 / —; 4Q25 689 / 646; FY25 843 / 657;
  1Q26 39 / —; 2Q26 19 / —; FY21 376 / 15; FY22 382 / 113; FY23 202 / 42 (D02 70, 890-893,
  1000-1003; D04 70, 904-907; D05 72, 927-930; D06 72, 898-901, 1011-1014; D07 72, 900-903).
- Severance-tax items: TOTI refund 31 and G&A consulting fees (10) in 3Q24 and FY24; interest on
  the refund (5) only in Adjusted NI; FY22 refund 115 and fees (16) only in the per-Boe annual
  tables and AKFI endnote 6/7.
- Settlements (before tax): 1Q24 55, 2Q24 79, 3Q24 61, 4Q24 19, FY24 214, FY23 (112), 1Q25 (38),
  2Q25 (24), 3Q25 27, 4Q25 (21), FY25 (56), 1Q26 (53), 2Q26 45.
- MMBoe: 1Q24 93.6, 2Q24 95.3, 3Q24 99.0, 4Q24 100.8, FY24 388.7 (D02 152); 1Q25 98.1, 2Q25 103.2,
  H1 2025 201.3 (D04 152); 3Q25 119.7, 9M 2025 321.0 (D05 159); 4Q25 128.7, FY25 449.8, 1Q26 124.5
  (D06 164); 2Q26 128.3, H1 2026 252.9 (D07 162); FY21 302.5, FY22 331.5, FY23 359.4 (per-Boe
  annual (a), D06 969).
- "Total Cash Operating Costs and Total DD&A per Boe" (GAAP / Non-GAAP), printed only in
  bridges: 4Q24 20.26 / 20.26 (D02 614, 679); 1Q25 20.63 / 20.63 (D02 616, 681; D04 618, 683); 2Q25
  20.25 / 20.14 (D04 620, 685; D05 631, 696); 3Q25 20.27 / 19.70 (D05 633, 698); 4Q25 19.81 / 19.75
  (D06 622, 681); 1Q26 20.03 / 20.03 (D06 624, 683; D07 622, 679); 2Q26 20.38 / 20.38 (D07 624,
  681). Not printed for 1Q24-3Q24.
- Treasury Stock Purchased: 2024 (759) (699) (795) (993) / (3,246) (D02 283); 2025 (806) (602)
  (479) (677) / (2,564) (D06 300); 2026 (418) (1,299) / (1,717) (D07 298). Treasury balance Jun 30
  2026 (7,799) (D07 230).
- Debt flows: borrowings 4Q24 985, 3Q25 3,472, 4Q25 999; repayments 2Q25 (500), 3Q25 (1,266), 4Q25
  (750) (locations above).

### External references (not in the bundle)

- 10-K Item 1A (D01 113, D03 203); 10-Q notes (series price footnotes; Note 5).
- EOG website "Reconciliations & Guidance" (D02 299, D04 300, D05 310, D06 316, D07 314).
- Earnings-release endnotes (D04 881, D05 904, D06 875, D07 877).
- D01 45 (first quarter 2020 results release); D03 55 (webcast and presentation materials).

### Documents that cite, amend or respond to another bundle document

- None cites another bundle document by name or date. Links are topical: D03 announces the
  pending Encino agreement and the dividend; D05-D07 report the Encino acquisition cash outflow
  and D04-D07 the Encino acquisition-related costs; series editions repeat earlier editions'
  comparatives. D01's 2020 plan has no matching actuals in the bundle.
