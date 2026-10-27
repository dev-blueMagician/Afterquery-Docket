# aq-06634 - document map

Maintained by the caller or optional `bundle-mapper` from `text/` (and `docs/` for layout issues).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

Mapped 2026-10-18 by bundle-mapper (full map requested). `l.` = line in `text/Dnn.txt`. Figures are
$ millions unless stated. "(derived)" marks mapper arithmetic done by hand (no script tool was
available to the mapper in this pass). It is not a document statement, so recheck it before use.

## Bundle

- What it is: six Paychex, Inc. (Nasdaq: PAYX) filings, an earnings release and a Form 10-Q for each
  of fiscal Q2 FY2026 (quarter ended Nov 30, 2025), Q3 FY2026 (Feb 28, 2026) and Q1 FY2027
  (Aug 31, 2026). Fiscal year ends May 31 ("fiscal 2026" = year ending May 31, 2026; "fiscal 2027" =
  year ending May 31, 2027). Quarters: Q1 Jun-Aug, Q2 Sep-Nov, Q3 Dec-Feb, Q4 Mar-May.
- Documents: 6 (ids from `text/manifest.json`; platform Doc numbers from notes/intake.json)

| Local | Platform | Type / title | Period | Dated or signed | Lines |
|---|---|---|---|---|---|
| D01 | Doc 2 | Release "Paychex Reports First Quarter Fiscal 2027 Results" | 3M ended Aug 31, 2026 | Sept 23, 2026 (l.18) | 344 |
| D02 | Doc 1 | Form 10-Q | quarter ended Aug 31, 2026 | signed Sept 24, 2026 (l.1437) | 1449 |
| D03 | Doc 6 | Release "Paychex Reports Second Quarter Results" | 3M and 6M ended Nov 30, 2025 | Dec 19, 2025 (l.18) | 347 |
| D04 | Doc 5 | Form 10-Q | quarter ended Nov 30, 2025 | signed Dec 22, 2025 (l.1528) | 1540 |
| D05 | Doc 4 | Release "Paychex Reports Third Quarter Results" | 3M and 9M ended Feb 28, 2026 | Mar 25, 2026 (l.18) | 378 |
| D06 | Doc 3 | Form 10-Q | quarter ended Feb 28, 2026 | signed Mar 26, 2026 (l.1560) | 1572 |

- Gaps: no unread ranges (see ledger). There is no missing extracted text. The source captures themselves
  lack text in one place. In all six, the risk-factor bullet list has no forward-looking-statement lead-in
  and starts partway through: D01 l.102-144 (22 items), D03 l.201 (1 item), D05 l.207-229 (12 items),
  D02 l.824-828 (3), D04 l.930-936 (4), D06 l.954-958 (3). The same truncation appears in the
  `docs/` originals (checked by searching the originals for "forward-looking", "safe harbor" and "negative publicity"), so it comes from
  the capture, not the extraction. It affects risk-list wording only, and no figures. Not in the bundle:
  any Q1 FY2026 or Q4 FY2026 release or 10-Q, the FY2025 and FY2026 10-Ks, the earlier FY2026/FY2027
  outlook releases that "previously" refers to, the Jan 26, 2026 8-K and the credit agreements.
  No PDFs, charts or scans, so page/visual checks are not applicable.
- Extraction spot-checks (method "text", pages null, so page counts are not applicable). The text files add
  a 2-line header and collapse double blank lines, which shifts line numbers against `docs/`.
  - D01: original l.1-30, 96-107 and 276-345 match the highlights table, About, the cash-flow
    reconciliation ("-" cell for funds-held restricted cash at Aug 31, 2026), the non-GAAP table and
    footnote (1).
  - D02: original l.1016 footnote ($151.2M at Sept 23, 2026) and l.1485-1488 repurchase table ($675.6)
    match text l.952 and l.1404-1407.
  - D03: original l.79 prose "$77.0 million" and l.135/140 table "77.1" match text l.79, 134, 139.
  - D04: original l.583 ($161.0M), l.620 (goodwill $2,594.1) and l.1285 (PNC row 18.2/231.8) match
    text l.547, 583, 1206.
  - D05: original l.73 ("$71.0 million"), l.129/134 (71.2) and l.168 ($13.2M footnote) match text
    l.73, 128, 133, 166.
  - D06: original l.586 ($232.1M), l.623 ($2,591.1) and l.1616-1617 (repurchase table) match text
    l.550, 586, 1527-1528.
  - Funds-held restricted cash row checked in all six originals.
- Provenance: notes/intake.json capture sha256 56b6664efcfd3f7e1afd89186259143a631a1eada1d82c0902eaddc6ff04411c.
  All six records match the capture, none incomplete, gap_characters 0. There is no recovered-source history.
- Reuse binding (source sha256 from manifest; text corpus sha256 prefix 09e5f180ed2e7fdf from
  notes/mine.md; per-file text hashes were not computed in this pass)
  - D01 97e638df621b38b0cce411b06624e58b29124a560bb6804b86f213a0cdbb2d43
  - D02 279224ceebd0dfd118543486f3830a95b9b985b248b1841c4b1588688f7a47d2
  - D03 9f5426ed29d8354c7f9aff8a75608010eb4ad1fd6c203329ef90bdfc3ad9d599
  - D04 314cfe99f761c80663a25b5458acec17a92ea33620212cef5a0fc13f27247adb
  - D05 67765ef6c0d8d2502ee3c0da932ddb40eefb41c963db9f8f668728ed93e2e87c
  - D06 f11e1e514d2362dd28d21bdacf9aef1942ec91d709bbfcc785ccf153f3b97ad9
  - Reuse the entries below while these hashes are unchanged. Re-map any document whose hash changes,
    together with the Shared-ground rows that cite it.

### Read ledger

| Doc | Chunks read (text lines) | Unread | Status |
|---|---|---|---|
| D01 | 1-344 | none | complete |
| D02 | 1-230, 230-449, 449-648, 648-847, 847-1046, 1046-1245, 1245-1449 | none | complete |
| D03 | 1-347 | none | complete |
| D04 | 1-280, 280-519, 519-758, 758-997, 997-1236, 1236-1495, 1495-1540 | none | complete |
| D05 | 1-378 | none | complete |
| D06 | 1-60, 60-289, 289-538, 538-787, 787-1026, 1026-1265, 1265-1534, 1534-1572 | none | complete |

## D01 - Paychex Reports First Quarter Fiscal 2027 Results (release; platform Doc 2)

- Source: docs/Paychex-Q1-FY2027-Earnings-Release.txt | plain text | text/D01.txt l.1-344
- Written or submitted by: Paychex, Inc. news release (Rochester, N.Y.). John Gibson (President and CEO)
  is quoted at l.30 and l.32. Contacts at l.91-96: Rachel White (Head of Investor Relations, investors@paychex.com)
  and Tracy Volkmann (Manager, Public Relations, public_relations@paychex.com).
- Type, date, edition: earnings release dated September 23, 2026 (l.18).
- Period covered: "fiscal quarter ended August 31, 2026 (the "first quarter") of the fiscal year ending
  May 31, 2027 ("fiscal 2027")" (l.18). The comparatives are the 3M ended Aug 31, 2025. The balance sheet
  compares Aug 31, 2026 with May 31, 2026. "Unless otherwise noted, all growth rates refer to the current
  period versus the comparable prior-year period" (l.18).
- Entities and aliases: Paychex; Paycor HCM, Inc. ("Paycor") at l.329; PEO = Professional Employer Organization
  (l.43); WISE engine and WISE Hire (l.16, 32, 100); Microsoft business applications are mentioned at l.32.
  About (l.100) says "approximately 840,000 customers" and "1 in 11 U.S. private sector workers".
- Tables
  - l.20-28: highlights, 3M Aug 31, 2026 vs 2025 with a Change column. Total revenue 1,630.5/1,540.0 (6%);
    operating income 619.2/541.9 (14%); adjusted operating income 684.7/626.7 (9%); diluted EPS $1.21/$1.06
    (14%); adjusted diluted EPS $1.34/$1.22 (10%).
  - l.146-175: income statement, 3M plus Change; footnote (1) at l.177-178 (see Shared ground).
  - l.180-230: balance sheet Aug 31, 2026 vs May 31, 2026. It has no short-term borrowings line and no
    current-portion-of-debt line.
  - l.232-283: cash flows, 3M only. Funds-held restricted cash equivalents are "-" at Aug 31, 2026 and 775.2 at Aug 31, 2025 (l.282).
  - l.285-323: non-GAAP reconciliation, 3M; footnotes (1)-(3) at l.325-341.
  - l.81-89: fiscal 2027 outlook table.
- Lists: the outlook has 7 rows, the last being adjusted diluted EPS growth (l.89). The footnote (1) bullets
  are 3 (l.328-335). The risk list (l.102-144) has 22 items and starts mid-list.
- Forecasts and guidance: see Shared ground K. The lead-in at l.79 says "Forward-looking adjusted operating margin
  and adjusted diluted earnings per share exclude acquisition-related costs."
- Hedged claims: "Changes in the macroeconomic environment could alter our guidance" (l.79; "could" applies to
  the guidance). The CEO says "we believe these innovations strengthen our competitive position..." (l.32, a belief).
- Rounded prose next to exact figures: l.37 "$1.6 billion" (1,630.5); l.40 Management Solutions "4% to $1.2
  billion" (1,213.1); l.64 "Cash, restricted cash, and total corporate investments of $1.0 billion"
  (600.9+55.0+333.3=989.2, derived); l.67 "Long-term borrowings ... $4.6 billion" (4,558.0); l.52 margins
  38.0%/35.2% and 42.0%/40.7%; l.75 "Paid dividends of $1.19 per share totaling $424.1 million". There is no
  repurchase bullet (Q1 FY27 repurchases "—", l.272).
- Operative definitions: l.57 "Operating margin and adjusted operating margin are calculated as a percentage of
  total revenue." Footnote (3) at l.340-341 says the per-share impact "is performed on each line independently.
  The table may not add down by +/- $0.01 due to rounding." Footnote (2) at l.337-338 reads "Net tax windfall
  related to stock-based compensation payments ... will vary based on option holder decisions related to
  exercising stock options..."
- Features absent from D01, though D03 and D05 have them: the "Percentage changes are calculated based on
  unrounded numbers" footnote; the paragraph defining the non-GAAP measures; the paragraph about the 10-Q filing.
- Coverage: full.

## D02 - Form 10-Q for the quarter ended August 31, 2026 (platform Doc 1)

- Source: docs/Paychex-Q1-FY2027-Quarterly-Report.txt | text/D02.txt l.1-1449
- Written or submitted by: Paychex, Inc. It is signed Sept 24, 2026 by John B. Gibson (President, CEO and Director),
  Robert L. Schrader (SVP and CFO) and Christopher Simmons (VP, Controller and Treasurer) (l.1437-1446).
- Period covered: 3M ended Aug 31, 2026 ("first quarter") and 3M ended Aug 31, 2025 ("prior year
  period") (l.817). The cover (l.62) gives 355,980,473 shares outstanding as of Aug 31, 2026. The filing is to be
  read with the "Form 10-K for the fiscal year ended May 31, 2026" (l.305 and l.820), which was "filed with the SEC
  on July 17, 2026" (l.1353).
- Entities and aliases: Note A (l.299) says the Company "also has operations in Canada, India, and Israel" and
  "reports as one segment", with segment reporting in Note J. Platforms are SurePayroll®, Paychex Flex® and
  Paycor® (l.836). Bank names: "JPMorgan Chase Bank, N.A. ("JPM")" (l.747) and "2019 JP Morgan Chase Bank, N.A.
  ("JPM") Credit Facility" (l.1108); "PNC Bank, N.A. ("PNC")" (l.749); "2020 PNC Credit Facility"
  (l.1116, 1124). Other names: Paychex Insurance Agency, Inc. (l.416); "Coronavirus Aid, Relief, and Economic
  Security Act" (l.1205, 1216); "One Big Beautiful Bill Act" (l.782).
- Tables (all 3M Aug 31, 2026 vs 2025 unless a balance date is given)
  - l.94-125: income statement and comprehensive income, with OCI (31.4)/28.7 and comprehensive income
    398.3/412.5 (l.120-121).
  - l.133-182: balance sheet Aug 31, 2026 / May 31, 2026; no short-term borrowings line; contingencies under Note H (l.175).
  - l.190-222: stockholders' equity for Q1 FY27 and Q1 FY26; footnote (1) at l.224-225 covers reclassification;
    footnote (2) at l.227-228 covers the repurchase program.
  - l.236-285: cash flows, 3M.
  - l.310-319: accounts receivable. l.329-337: allowance roll-forward. l.406-414: PEO pass-through costs.
  - l.426-445: material-rights deferred revenue roll-forward and expected recognition. l.455-475: costs to
    obtain and costs to fulfill contracts.
  - l.479-497: EPS (Note C). l.501-511: other income (Note D: interest income on corporate investments 10.2/18.7, other 0.7/5.1).
  - Note E (l.515-634): investments at Aug 31, 2026 and May 31, 2026; classification (l.562-569);
    unrealized-loss tables (l.575-601); realized gains and losses (l.611-619); maturities (l.621-632).
  - Note F (l.663-706): fair-value hierarchy. l.719-729: long-term borrowings at amortized cost and fair value.
  - Note J (l.784-811): segment table.
  - MD&A tables: highlights (l.852-864, including dividends paid 424.1/389.1); summary (l.878-896, with ETR
    24.0%/22.9%); investment balances and rates (l.927-939); market table (l.943-950, footnotes l.952-956);
    expenses (l.962-973); margins (l.1013-1018); non-GAAP (l.1033-1063, footnotes l.1065-1083); credit
    facilities (l.1103-1110); borrowings (l.1122-1129); long-term financing (l.1139-1145); cash-flow summary
    (l.1179-1187); maturities (l.1291-1300); Part II repurchases (l.1402-1407).
- Lists: critical accounting estimates, 8 items ending "income taxes" (l.1355-1370); interest-rate factors, 7
  items (l.1308-1320); captive-insurance risks, 6 (l.1159 and l.768); exhibits 31.1-104 (l.1417-1425), with
  no 10.x exhibits; accounting standards updates covered: 2025-05 (adopted, l.367), 2024-03 (l.369),
  2025-06 (l.377), 2025-08 (l.379).
- Forecasts: "total investment portfolio ... is expected to average approximately $7.0 billion for the fiscal year
  ending May 31, 2027", with about 35% short-term and VRDNs and 65% AFS (l.1324). A 25-basis-point
  short-term rate change is put at "approximately $4.5 million to $5.0 million, after taxes, for a twelve-month
  period" (l.1322). A 25-basis-point fall in longer-term rates would raise fair value by about $30.0M to
  $35.0M (l.1331).
- Hedged claims: the market-risk impact "would be approximately"; "Such a basis point change may or may not be
  tied to changes in the Federal Funds rate" (l.1322; "may or may not" applies to the tie). The impairment
  assessment "could change in the future" (l.607, l.1345). The liquidity outlook says the Company "currently
  anticipate[s] ... will support ... share repurchases, dividend payments, and debt service"; this list has
  no "acquisitions" (l.1093).
- Rounded prose: l.902 "$1.6 billion"; l.905 "$1.2 billion"; l.960 "relatively unchanged at $1.0 billion";
  l.1093 "$1.0 billion", "Long-term borrowings of $4.6 billion", "$2.0 billion" and "$413.5 million"; l.1137
  "$0.4 billion" of Senior Notes and "$4.2 billion" of bonds; l.1328 "$4.6 billion and $4.5 billion" in AFS.
- Notes and events: Series A repaid ("During fiscal 2026 ... $400.0 million, which matured on March 13, 2026",
  l.758 and l.1147). No short-term borrowings outstanding at Aug 31, 2026 or May 31, 2026 (l.743). Credit
  facility amendments effective Jan 23, 2026 (l.747-750 and l.1114-1117). Borrowings after Aug 31, 2026: "13 times on
  an overnight basis, $523.8 million, on a weighted-average basis" (l.1133). Federal Funds rate raised to
  3.75%-4.00% effective Sept 17, 2026 (l.954, l.1304). Net unrealized loss about $151.2M at Sept 23, 2026
  (l.952, l.1326); during Q1 it ranged from $93.0M to $51.8M (l.1326). Seven limited partnerships, $40.5M
  maximum, about $35.1M contributed (l.1153). Capital-asset commitments $9.7M (Aug 31, 2026) and $13.5M
  (May 31, 2026) (l.762). Letters of credit $173.0M and $176.5M, expiring between Sept 01, 2026 and Dec 24, 2027 (l.754).
- Coverage: full.

## D03 - Paychex Reports Second Quarter Results (release; platform Doc 6)

- Source: docs/Paychex-Q2-FY2026-Earnings-Release.txt | text/D03.txt l.1-347
- Written or submitted by: Paychex, Inc. The issuer is defined as "the "Company," "Paychex," "we," "our," or "us""
  (l.18). Gibson is quoted (l.36, 38). Contacts: Rachel White; Tracy Volkmann, tvolkmann@paychex.com (l.190-195).
- Type, date, edition: release dated December 19, 2025 (l.18). It says the 10-Q will be filed "within the
  next couple of business days" (l.188).
- Period covered: fiscal quarter ended Nov 30, 2025 ("second quarter") of fiscal 2026, plus the six months
  ended Nov 30, 2025 ("six months", l.91). The comparatives are 2024. Balance sheet Nov 30, 2025 vs May 31, 2025.
- Entities and aliases: HCM = human capital management (l.18); HR = Human Resources (l.48); PEO (l.54); Paycor
  "acquired in April 2025" (l.45); U.S. and GAAP defined at l.31; SEC at l.169. About (l.199): "one out of every 11
  American private sector workers" and "approximately 800,000 customers in the U.S. and Europe".
- Tables
  - l.20-28: highlights, 3M and 6M with Change(2). Footnote (2) at l.33-34: "Percentage changes are calculated
    based on unrounded numbers."
  - l.128-158: non-GAAP, 3M and 6M; footnotes (1)-(3) at l.160-167. The definitions paragraph is at l.169-171.
  - l.203-232: income statement, 3M and 6M; footnotes at l.234-238 ("n/m — not meaningful").
  - l.240-292: balance sheet Nov 30, 2025 / May 31, 2025. Line labels include "Short-term borrowings" 18.2/18.6 (l.272)
    and "Long-term borrowings, net, current portion" 399.9/399.8 (l.274).
  - l.294-344: cash flows, six months only. There is no three-month cash flow.
- Forecasts and guidance: fiscal 2026 outlook at l.173-184 (see Shared ground K). The headline bullet reads "Raises Full Year
  Earnings Outlook" (l.16).
- Rounded prose: l.42 "$1.6 billion"; l.45 "$1.2 billion"; l.79 "excludes $77.0 million of Paycor
  acquisition-related costs", while the table at l.134 and the footnote sum give 77.1; l.94 "$3.1 billion"; l.97 "3% to
  $1.1 billion" and "18% to $1.3 billion"; l.112 "$1.6 billion" (1,485.6+50.7+37.6=1,573.9, derived); l.115
  "Short-term and long-term borrowings ... $5.0 billion" (18.2+399.9+4,552.2=4,970.3, derived); l.118 "$1.2
  billion" (1,163.3); l.123 "$2.16 per share totaling $777.0 million"; l.126 "Repurchased 2.1 million shares ...
  for $286.6 million". l.103 reads "Adjusted diluted earnings per share(1) increased to 8% to $2.48 per share".
- Narrative reasons: Q2 interest on funds held rose 51% "due to" higher average balances from Paycor and
  "Higher realized gains due to strategic repositioning of our investment portfolio" (l.63-69). Interest expense
  "increased $59.0 million to $68.5 million" (l.81). The ETR was "24.0% for the second quarter and the prior year
  period" (l.83).
- Coverage: full.

## D04 - Form 10-Q for the quarter ended November 30, 2025 (platform Doc 5)

- Source: docs/Paychex-Q2-FY2026-Quarterly-Report.txt | text/D04.txt l.1-1540
- Written or submitted by: Paychex, Inc. Same three signers, dated Dec 22, 2025 (l.1528-1537).
- Period covered: 3M ended Nov 30, 2025 ("second quarter"), 6M ended Nov 30, 2025 ("six months") and the 2024 prior-year periods (l.923).
  The cover (l.62) gives 358,967,450 shares as of Nov 30, 2025. It is to be read with the FY2025 10-K (l.344, l.926),
  "filed with the SEC on July 11, 2025" (l.1444).
- Entities and aliases: Note A (l.338) says "The Company also has operations in India"; segment reporting is in
  Note K. Credit-facility rows are labelled "JP Morgan Chase Bank, N.A. ("JPM")", "JPM" and "PNC Bank, National
  Association ("PNC")" (l.1204-1206). Platforms are listed at l.946. "Paycor, a leading provider of HCM, payroll and talent software" (l.956).
- Tables
  - l.96-125: income statement and comprehensive income, 3M and 6M. OCI 7.4/(11.6)/36.1/53.2.
  - l.133-184: balance sheet Nov 30, 2025 / May 31, 2025, with "Long-term debt, net, current portion" at l.165.
  - Stockholders' equity: 6M FY26 (l.196-209), Q2 FY26 (l.211-224), 6M FY25 (l.234-247) and Q2 FY25
    (l.249-262), with footnotes at l.226-230 and l.264-268.
  - l.280-324: cash flows, six months only.
  - Note A: accounts receivable (l.351-360), allowance (l.370-378, 3M and 6M).
  - Note B: pass-through costs (l.444-452), material rights (l.462-483), contract costs (l.495-513).
  - Note C: EPS (l.519-535).
  - Note D: Paycor purchase price allocation table (l.559-583) and pro forma (l.593-597).
  - Note E: other income (l.609-617; interest income on corporate investments 16.5/15.8/35.2/35.7; other 0.3/(0.7)/5.4/(0.6)).
  - Note F: investments (l.623-655), classification (l.667-674), unrealized-loss tables (l.684-708),
    realized gains and losses (l.721-729), maturities (l.733-742).
  - Note G: fair value (l.771-818); borrowings at amortized cost and fair value (l.831-842).
  - Note K: segment (l.890-917).
  - MD&A tables: highlights (l.964-976, dividends paid 387.9/352.8/777.0/706.2); summary (l.990-1008);
    investments and rates (l.1047-1059); market (l.1063-1076); expenses (l.1082-1093); margins (l.1120-1125);
    non-GAAP (l.1138-1168, footnotes l.1170-1179); credit facilities (l.1197-1207); borrowings (l.1213-1223);
    long-term financing (l.1233-1239); cash-flow summary (l.1271-1279); maturities (l.1380-1389); Part II
    repurchases (l.1493-1498).
- Lists: accounting standards updates covered are 2023-09, 2024-03, 2025-05 (being evaluated), 2025-06 and
  2025-08 (l.404-424). Critical accounting estimates: 8 items (l.1446-1461). Interest-rate factors: 7 (l.1399-1411).
  Exhibits: 31.1-104, no 10.x.
- Forecasts and expectations: "expected to average approximately $7.4 billion for the fiscal year ending May 31,
  2026", with about 40% short-term and VRDNs and 60% AFS (l.1415). The 25-basis-point short-term impact is
  "approximately $5.5 million to $6.0 million" (l.1413). The purchase price allocation "is subject to change ...
  These adjustments will be finalized no later than one year from the acquisition date" (l.553). The One Big
  Beautiful Bill Act: "deferred tax liabilities will be impacted in fiscal 2026 ... The Act is not expected to
  have a material impact" (l.888).
- Hedged claims: expectation wording on the Act (l.888); "may or may not be tied" (l.1413); "it is not
  more-than-likely that we would be required to sell" (l.1191) against "not more-likely-than-not that we will be
  required to sell" (l.714, l.1433). The liquidity outlook list includes "acquisitions" (l.1189).
- Rounded prose: l.1014 "$1.6 billion ... $3.1 billion"; l.1019 "$1.2 billion ... $2.3 billion"; l.1080 "28% to
  $2.0 billion"; l.1102 "$1.1 billion"; l.1116 "3% to $1.1 billion", "18% to $1.3 billion"; l.1189 "$1.6 billion",
  "Short-term borrowings of $18.2 million and long-term borrowings of $5.0 billion", "approximately $2.0 billion"
  and "$1.2 billion"; l.1231 "$0.8 billion" of Senior Notes; l.1419 "$4.5 billion and $3.8 billion".
- Notes and events: "Reclassifications: Certain prior year amounts have been reclassified to conform to the
  current period presentation. These reclassifications had no effect on reported consolidated earnings." (l.347;
  no lines are named). PNC: "Amounts outstanding under the PNC credit facility as of November 30, 2025 remain
  outstanding as of the date of this report" (l.1211). Borrowings after Nov 30, 2025: "one time on an
  overnight basis, $595.0 million under our PNC and JPM credit facilities" (l.1227). Federal Funds rate cut to
  3.50%-3.75% effective Dec 11, 2025 (l.1074, l.1393). Net unrealized loss about $15.8M at Dec 17, 2025
  (l.1072, l.1417); the six-month range was a net unrealized gain of $2.3M to a net unrealized loss of $63.8M (l.1417).
  A lease not yet commenced runs 7.58 years for about $14.5M (l.854). Six limited partnerships, $37.5M maximum,
  $32.1M contributed (l.1243).
- Coverage: full.

## D05 - Paychex Reports Third Quarter Results (release; platform Doc 4)

- Source: docs/Paychex-Q3-FY2026-Earnings-Release.txt | text/D05.txt l.1-378
- Written or submitted by: Paychex, Inc. Gibson is quoted (l.36, 38). Contacts at l.194-201 (the table header row is split
  from its body in the source layout; tvolkmann@paychex.com).
- Type, date, edition: release dated March 25, 2026 (l.18). The 10-Q is to follow "within the next couple of business days" (l.192).
- Period covered: quarter ended Feb 28, 2026 ("third quarter") and nine months ended Feb 28, 2026 ("nine months",
  l.85). The comparatives are 2025. Balance sheet Feb 28, 2026 vs May 31, 2025.
- Entities and aliases: as D03. About (l.205) is identical to D03's (about 800,000 customers).
- Tables
  - l.20-28: highlights, 3M and 9M with Change(2).
  - l.122-152: non-GAAP; footnotes at l.154-172, including the interest-expense paragraph at l.166. Definitions at l.174-178.
  - l.231-260: income statement, 3M and 9M; footnotes at l.262-266.
  - l.268-320: balance sheet. Short-term borrowings "—"/18.6 (l.300); "Long-term borrowings, net, current
    portion" 400.0/399.8 (l.302).
  - l.322-375: cash flows, nine months only. This is the only release cash flow with "Premiums paid on cash flow hedges —/(19.2)",
    "Net change in short-term borrowings (18.8)/—" and "Debt issuance fees —/(11.4)" (l.342, 362, 365).
- Forecasts and guidance: fiscal 2026 outlook at l.180-188 (see Shared ground K).
- Claims without a figure: the headline "Accelerated Organic Revenue Growth" (l.13) and the CEO's "accelerated our organic revenue
  growth" (l.36). No organic growth figure appears anywhere in the bundle (searched "organic").
- Rounded prose: l.16 "Returned Over $1.5 Billion to Shareholders Fiscal Year to Date" and l.38 "The $1.5 billion
  returned". No sum is printed; dividends 1,165.0 plus repurchases 361.6 = 1,526.6 (derived). Further: l.42 "$1.8
  billion"; l.45 "$1.4 billion"; l.65 "Total expenses increased 24% to $1.0 billion"; l.73 "excludes $71.0 million
  of Paycor acquisition-related costs", while the table at l.128 and the footnote sum give 71.2; l.88 "$4.9 billion"; l.91 "$1.9
  billion" and "$2.1 billion"; l.106 "$1.8 billion" (1,742.5+49.8+38.1=1,830.4, derived); l.109 "$5.0 billion"
  (0+400.0+4,554.1=4,954.1, derived); l.112 "$2.0 billion" (1,975.8); l.117 "$3.24 per share totaling $1.2 billion"
  (1,165.0); l.120 "2.9 million shares ... for $361.6 million"; l.97 "increased to 11% to $4.19".
- Narrative reasons: Q3 interest on funds held "increased 33% to $56.8 million for the third quarter due to higher
  average investment balances resulting from the acquisition of Paycor" (l.63). Only one reason is given here; D06
  l.1059-1065 gives two for Q3 and the nine months together. Interest expense "increased $45.5 million to $68.1
  million" (l.75). ETR 24.2% vs 24.3% (l.77).
- Coverage: full.

## D06 - Form 10-Q for the quarter ended February 28, 2026 (platform Doc 3)

- Source: docs/Paychex-Q3-FY2026-Quarterly-Report.txt | text/D06.txt l.1-1572
- Written or submitted by: Paychex, Inc. Same signers, dated Mar 26, 2026 (l.1560-1569).
- Period covered: 3M ended Feb 28, 2026 ("third quarter"), 9M ended Feb 28, 2026 ("nine months") and the 2025 prior-year periods (l.947).
  The cover (l.62) gives 358,290,881 shares as of Feb 28, 2026. It is to be read with the FY2025 10-K (l.347, l.950; filed July 11, 2025, l.1474).
- Entities and aliases: Note A (l.341) says "operations in India". Subsidiaries: Paychex of New York LLC ("PoNY") (l.872); "Paychex
  of New York, LLC" (l.1276); "Paychex Advance, LLC" (l.874); "Paychex of New York" (exhibits l.1540-1541). Banks: "JPMorgan
  Chase Bank, N.A. ("JPM")" (l.872, 1540-1541) and "JP Morgan Chase Bank, N.A. ("JPM")" (l.1239); "PNC Bank, N.A." and
  "2020 PNC Credit Facility" (l.874-875, 1243, 1249). The Current Report on Form 8-K was filed Jan 26, 2026 (l.1243, 1540-1541).
- Tables
  - l.96-125: income statement and comprehensive income, 3M and 9M. OCI 14.9/2.3/51.0/55.5.
  - l.133-184: balance sheet Feb 28, 2026 / May 31, 2025 ("Long-term debt, net, current portion" 400.0/399.8, l.165).
  - Equity: 9M FY26 (l.196-209), Q3 FY26 (l.211-224), 9M FY25 (l.234-247) and Q3 FY25 (l.249-262). A "Cash flow hedges"
    column appears in D06 only. Footnotes at l.226-230 and l.264-268.
  - l.280-327: cash flows, nine months only.
  - Note A: AR (l.354-363), allowance (l.375-381).
  - Note B: pass-through (l.449-455), material rights (l.469-486), contract costs (l.498-516).
  - Note C: EPS (l.522-538).
  - Note D: purchase price allocation (l.562-586) and pro forma (l.596-600).
  - Note E: other income (l.614-620; interest income on corporate investments 15.2/16.6/50.4/52.3; other (0.1)/(0.0)/5.3/(0.6)).
  - Note F: investments (l.626-659), classification (l.673-678), unrealized-loss tables (l.688-712), realized (l.727-733),
    maturities (l.737-746).
  - Note G: fair value (l.777-827); borrowings (l.840-849).
  - Note K: segment (l.917-941).
  - MD&A tables: highlights (l.984-996, dividends paid 388.0/353.0/1,165.0/1,059.2); summary (l.1010-1028); investments
    (l.1069-1081); market (l.1085-1098); expenses (l.1104-1115); margins (l.1142-1147); non-GAAP (l.1160-1190,
    footnotes l.1192-1212); credit facilities (l.1234-1241); borrowings (l.1247-1254); long-term financing
    (l.1264-1270); cash-flow summary (l.1306-1314); maturities (l.1412-1421); Part II repurchases (l.1523-1528).
- Lists: the exhibits include 10.1 (2017 Credit Agreement dated Aug 17, 2017, through Amendment No. 6 dated Jan 23, 2026)
  and 10.2 (2019 Credit Agreement dated July 31, 2019, through Amendment No. 4 dated Jan 23, 2026) (l.1540-1541).
  D02 and D04 have no 10.x exhibits. The critical-estimates list ends with "income taxes" after a page break (l.1493).
- Forecasts: $7.4B average portfolio for FY ending May 31, 2026, 40%/60% (l.1445). The 25-basis-point impact is
  "approximately $5.0 million to $5.5 million" (l.1443). The One Big Beautiful Bill Act is "not expected to have a material impact" (l.911).
- Notes and events: the Series A repayment comes "Subsequent to February 28, 2026" (l.883, l.1272). Bridge loan commitment
  (Jan 7, 2025; JPM; 364-day facility up to $3.5B; $11.4M fees in 3M ended Feb 28, 2025; expired when the bonds were
  issued) at l.887 and l.1276. Swaptions (Jan 31, 2025; three; $3.0B notional; $19.2M premiums; expired
  unexercised) at l.889 and l.1278. Net unrealized loss about $55.3M at Mar 24, 2026 (l.1094, l.1449); the nine-month range was a
  gain of $7.3M to a loss of $63.8M (l.1449). Capital commitments $10.7M (l.893). Six limited partnerships, $37.5M and $32.1M,
  unchanged from D04 (l.1280). Reclassifications paragraph at l.350 (no lines named). l.1387 states the fiscal 2025
  repurchase "during the six months" inside a nine-month comparison.
- Coverage: full.

## Shared ground (navigation only)

### A. Which document prints which period

| Statement | 3M Q2 FY25 (Nov 30, 2024) | 6M FY25 | 3M Q3 FY25 (Feb 28, 2025) | 9M FY25 | 3M Q1 FY26 (Aug 31, 2025) | 3M Q2 FY26 | 6M FY26 | 3M Q3 FY26 | 9M FY26 | 3M Q4 FY26 (May 31, 2026) | 3M Q1 FY27 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Income statement | D03, D04 | D03, D04 | D05, D06 | D05, D06 | D01, D02 (comparative) | D03, D04 | D03, D04 | D05, D06 | D05, D06 | none | D01, D02 |
| Non-GAAP reconciliation | D03, D04 | D03, D04 | D05, D06 | D05, D06 | D01, D02 | D03, D04 | D03, D04 | D05, D06 | D05, D06 | none | D01, D02 |
| Cash flows | none | D03, D04 | none | D05, D06 | D01, D02 | none | D03, D04 | none | D05, D06 | none | D01, D02 |
| Equity statement | D04 | D04 | D06 | D06 | D02 | D04 | D04 | D06 | D06 | none | D02 |
| Segment / expense table | D04 | D04 | D06 | D06 | D02 | D04 | D04 | D06 | D06 | none | D02 |

- Cash flows for the second and third quarters of each year appear only cumulatively (6M and 9M). The Q1 FY26 cash flow
  appears only as the comparative column of D01/D02.
- Q1 FY26 (quarter ended Aug 31, 2025) has no document of its own. It is printed directly as the D01/D02 comparative, and the
  six-month figures less Q2 in D03/D04 reproduce it (check in section I).
- Q4 FY26 (quarter ended May 31, 2026) has no three-month or full-year income-statement or cash-flow figure in any document.
  The "12 months" hits in D02/D04/D06 are cover boilerplate (l.47, 49) and the "twelve months" are headers of the
  unrealized-loss tables. The only figures for Q4 are endpoints: balance sheets at Feb 28, 2026 (D05, D06) and May 31, 2026 (D01, D02);
  the D02 roll-forwards' opening balances; the repurchase authorization left ($925.0 at Feb 28, 2026 in D06 l.1528;
  $675.6 at June 30, 2026 and after in D02 l.1404); and Series A repaid on Mar 13, 2026.
- Balance-sheet dates printed: May 31, 2025 (D03, D04, D05, D06); Nov 30, 2025 (D03, D04); Feb 28, 2026 (D05, D06); May 31, 2026
  (D01, D02); Aug 31, 2026 (D01, D02). No balance sheet is printed for Aug 31, 2025, Nov 30, 2024 or Feb 28, 2025. Only the
  cash-flow reconciliations (cash 809.0/1,202.1/1,563.8; restricted 50.4/63.1/49.1; funds-held restricted cash equivalents
  775.2/393.8/780.4) and equity balances are given for those dates.

### B. Income statement by period (identical in each release / 10-Q pair)

| Line | Q2 FY25 | 6M FY25 | Q3 FY25 | 9M FY25 | Q1 FY26 | Q2 FY26 | 6M FY26 | Q3 FY26 | 9M FY26 | Q1 FY27 |
|---|---|---|---|---|---|---|---|---|---|---|
| Management Solutions | 962.9 | 1,924.6 | 1,100.7 | 3,025.3 | 1,163.3 | 1,166.4 | 2,329.7 | 1,354.6 | 3,684.3 | 1,213.1 |
| PEO and Insurance Solutions | 317.9 | 637.2 | 365.4 | 1,002.6 | 329.1 | 336.9 | 666.0 | 397.5 | 1,063.5 | 367.6 |
| Total service revenue | 1,280.8 | 2,561.8 | 1,466.1 | 4,027.9 | 1,492.4 | 1,503.3 | 2,995.7 | 1,752.1 | 4,747.8 | 1,580.7 |
| Interest on funds held for clients | 36.1 | 73.6 | 42.9 | 116.5 | 47.6 | 54.3 | 101.9 | 56.8 | 158.7 | 49.8 |
| Total revenue | 1,316.9 | 2,635.4 | 1,509.0 | 4,144.4 | 1,540.0 | 1,557.6 | 3,097.6 | 1,808.9 | 4,906.5 | 1,630.5 |
| Cost of service revenue | 379.1 | 759.1 | 387.4 | 1,146.5 | 413.8 | 412.2 | 826.0 | 431.2 | 1,257.2 | 430.1 |
| SG&A | 399.7 | 791.5 | 429.8 | 1,221.3 | 584.3 | 573.5 | 1,157.8 | 585.7 | 1,743.5 | 581.2 |
| Total expenses | 778.8 | 1,550.6 | 817.2 | 2,367.8 | 998.1 | 985.7 | 1,983.8 | 1,016.9 | 3,000.7 | 1,011.3 |
| Operating income | 538.1 | 1,084.8 | 691.8 | 1,776.6 | 541.9 | 571.9 | 1,113.8 | 792.0 | 1,905.8 | 619.2 |
| Interest expense | (9.5) | (19.1) | (22.6) | (41.7) | (68.2) | (68.5) | (136.7) | (68.1) | (204.8) | (65.1) |
| Other income, net | 15.1 | 35.1 | 16.6 | 51.7 | 23.8 | 16.8 | 40.6 | 15.1 | 55.7 | 10.9 |
| Income before taxes | 543.7 | 1,100.8 | 685.8 | 1,786.6 | 497.5 | 520.2 | 1,017.7 | 739.0 | 1,756.7 | 565.0 |
| Income taxes | 130.3 | 260.0 | 166.5 | 426.5 | 113.7 | 124.8 | 238.5 | 178.7 | 417.2 | 135.3 |
| Net income | 413.4 | 840.8 | 519.3 | 1,360.1 | 383.8 | 395.4 | 779.2 | 560.3 | 1,339.5 | 429.7 |
| OCI, net of tax (10-Qs only) | (11.6) | 53.2 | 2.3 | 55.5 | 28.7 | 7.4 | 36.1 | 14.9 | 51.0 | (31.4) |
| Comprehensive income (10-Qs only) | 401.8 | 894.0 | 521.6 | 1,415.6 | 412.5 | 402.8 | 815.3 | 575.2 | 1,390.5 | 398.3 |
| Basic / diluted EPS ($) | 1.15/1.14 | 2.34/2.32 | 1.44/1.43 | 3.78/3.76 | 1.07/1.06 | 1.10/1.10 | 2.17/2.16 | 1.56/1.56 | 3.73/3.71 | 1.21/1.21 |
| Wtd shares basic / diluted | 360.0/361.7 | 360.1/361.8 | 360.1/362.0 | 360.1/361.9 | 360.1/361.9 | 359.4/360.4 | 359.7/361.1 | 358.7/359.5 | 359.4/360.6 | 355.8/356.6 |
| ETR (10-Q text/tables) | 24.0% | 23.6% | 24.3% | 23.9% | 22.9% | 24.0% | 23.4% | 24.2% | 23.7% | 24.0% |

Locations: D03 l.209-232 and D04 l.100-125 (Q2/6M); D05 l.237-260 and D06 l.100-125 (Q3/9M); D01 l.152-175 and D02 l.100-125
(Q1 FY27 / Q1 FY26). ETRs are at D02 l.780 and 894; D04 l.886 and 1006; D06 l.907 and 1026. The releases show Change columns; the
10-Qs show changes only in the MD&A tables. Per-share figures do not add across periods: 9M FY26 diluted 3.71 less 6M 2.16 = 1.55
against Q3 1.56; 9M FY25 3.76 less 2.32 = 1.44 against Q3 FY25 1.43 (derived).

Segment and expense table (D02 l.788-805 and l.962-973; D04 l.894-911 and l.1082-1093; D06 l.917-935 and l.1104-1115). The 10-Q notes
label the line "Other segment items" and the MD&A labels it "Other expenses".

| Line | Q2 FY25 | 6M FY25 | Q3 FY25 | 9M FY25 | Q1 FY26 | Q2 FY26 | 6M FY26 | Q3 FY26 | 9M FY26 | Q1 FY27 |
|---|---|---|---|---|---|---|---|---|---|---|
| Compensation-related | 454.4 | 905.7 | 455.7 | 1,361.4 | 530.0 | 525.5 | 1,055.5 | 530.9 | 1,586.4 | 526.8 |
| PEO direct insurance costs | 130.8 | 261.1 | 127.7 | 388.8 | 138.6 | 137.0 | 275.6 | 139.7 | 415.3 | 152.9 |
| Depreciation and amortization (core) | 41.7 | 80.7 | 43.1 | 123.8 | 48.2 | 49.1 | 97.3 | 50.6 | 147.9 | 52.9 |
| Other segment items / other expenses | 151.9 | 303.1 | 174.0 | 477.1 | 196.5 | 197.0 | 393.5 | 224.5 | 618.0 | 213.2 |
| Acquisition-related costs (non-core) | — | — | 16.7 | 16.7 | 84.8 | 77.1 | 161.9 | 71.2 | 233.1 | 65.5 |

D06 (l.930-931) alone splits interest expense into "Interest expense, excluding Paycor acquisition-related costs"
(68.1/9.4/204.8/28.5) and "Acquisition-related costs" (—/(13.2)/—/(13.2)). Segment footnote (1) wording differs: D02 l.808
"expenses related to professional services, marketing and advertising, technology and general overhead"; D04 l.914 and D06 l.938
"professional service expense, marketing and advertising expenses, and other overhead expenses".

### C. Non-GAAP reconciliations: lines, figures, definitions

Every reconciliation has four blocks: operating income to adjusted operating income (plus adjusted operating margin); net income
to adjusted net income; diluted EPS to adjusted diluted EPS; net income to EBITDA to adjusted EBITDA. Locations: D01 l.293-323;
D02 l.1033-1063; D03 l.128-158; D04 l.1138-1168; D05 l.122-152; D06 l.1160-1190.

| Line | Q2 FY25 | 6M FY25 | Q3 FY25 | 9M FY25 | Q1 FY26 | Q2 FY26 | 6M FY26 | Q3 FY26 | 9M FY26 | Q1 FY27 |
|---|---|---|---|---|---|---|---|---|---|---|
| Acq.-related costs (operating income block) | — | — | 16.7 | 16.7 | 84.8 | 77.1 | 161.9 | 71.2 | 233.1 | 65.5 |
| Adjusted operating income | 538.1 | 1,084.8 | 708.5 | 1,793.3 | 626.7 | 649.0 | 1,275.7 | 863.2 | 2,138.9 | 684.7 |
| Adjusted operating margin | 40.9% | 41.2% | 46.9% | 43.3% | 40.7% | 41.7% | 41.2% | 47.7% | 43.6% | 42.0% |
| Acq.-related costs (net income block) | — | — | 29.9 | 29.9 | 84.8 | 77.1 | 161.9 | 71.2 | 233.1 | 65.5 |
| Income tax benefit for acq.-related costs | — | — | (7.3) | (7.3) | (20.6) | (18.4) | (39.0) | (17.1) | (56.1) | (15.7) |
| Discrete tax shortfall/(windfall) | (2.4) | (8.6) | (0.8) | (9.4) | (7.2) | 0.5 | (6.7) | 0.5 | (6.2) | (0.3) |
| Adjusted net income | 411.0 | 832.2 | 541.1 | 1,373.3 | 440.8 | 454.6 | 895.4 | 614.9 | 1,510.3 | 479.2 |
| EPS: acq. costs / tax benefit / discrete ($) | —/—/(0.01) | —/—/(0.02) | 0.08/(0.02)/(0.00) | 0.08/(0.02)/(0.03) | 0.23/(0.06)/(0.02) | 0.21/(0.05)/0.00 | 0.45/(0.11)/(0.02) | 0.20/(0.05)/0.00 | 0.65/(0.16)/(0.02) | 0.18/(0.04)/(0.00) |
| Adjusted diluted EPS ($) | 1.14 | 2.30 | 1.49 | 3.79 | 1.22 | 1.26 | 2.48 | 1.71 | 4.19 | 1.34 |
| EBITDA add-backs: interest exp / corporate interest income / income taxes / D&A | 9.5/(15.8)/130.3/41.7 | 19.1/(35.7)/260.0/80.7 | 22.6/(16.6)/166.5/43.1 | 41.7/(52.3)/426.5/123.8 | 68.2/(18.7)/113.7/109.3 | 68.5/(16.5)/124.8/109.1 | 136.7/(35.2)/238.5/218.4 | 68.1/(15.2)/178.7/111.0 | 204.8/(50.4)/417.2/329.4 | 65.1/(10.2)/135.3/109.8 |
| EBITDA | 579.1 | 1,164.9 | 734.9 | 1,899.8 | 656.3 | 681.3 | 1,337.6 | 902.9 | 2,240.5 | 729.7 |
| Acq.-related costs (EBITDA block) | — | — | 16.7 | 16.7 | 23.7 | 17.1 | 40.9 | 10.7 | 51.6 | 8.6 |
| Adjusted EBITDA | 579.1 | 1,164.9 | 751.6 | 1,916.5 | 680.0 | 698.4 | 1,378.5 | 913.6 | 2,292.1 | 738.3 |

- Footnote components of acquisition-related costs "included in selling, general and administrative expenses":

| Period | Amortization of Paycor intangibles | Compensation (integration, replacement awards, severance, retention) | Other acquisition-related costs | Interest-expense item | Source |
|---|---|---|---|---|---|
| Q1 FY26 | 61.1 | 18.7 | 5.0 | — | D01 l.329-335; D02 l.1069-1075 (prior-year figures) |
| Q2 FY26 / 6M FY26 | 60.0 / 121.0 | 13.2 / 31.9 | 3.9 / 9.0 | — | D03 l.161; D04 l.1171 |
| Q3 FY26 / 9M FY26 | 60.5 / 181.5 | 9.8 / 41.7 | 0.9 / 9.9 | — | D05 l.158-164; D06 l.1196-1204 |
| Q3 FY25 / 9M FY25 | — | — | 16.7 / 16.7 | 13.2 / 13.2 | D05 l.164-166; D06 l.1204-1206 |
| Q1 FY27 | 56.9 | 8.5 | 0.1 | — | D01 l.329-335; D02 l.1069-1075 |

- In each period the EBITDA-block figure equals the total less the amortization component (65.5-56.9=8.6; 77.1-60.0=17.1;
  84.8-61.1=23.7; derived). D&A is added back in full in the EBITDA block. No document states this relationship.
- What "acquisition-related costs" covers, by passage:
  - D01 l.326 and D02 l.1066 list three bullets. The "other acquisition-related costs" bullet has no qualifier (D01 l.335).
  - D03 l.161 and D04 l.1171 add "(iii) ... other acquisition-related costs, primarily reflecting professional service fees".
  - D05 l.164 and D06 l.1204 have the same qualifier. They also say "In addition, acquisition-related costs for the three and nine months ended
    February 28, 2025 include $13.2 million, reflecting the amortization of financing fees related to debt instruments ... and the
    excluded component of the initial fair value of the interest rate swaption contracts that are included in Interest expense"
    (D05 l.166; D06 l.1206 adds a reference to Note H).
  - Segment footnotes: D02 l.811 has "other acquisition-related costs" with no qualifier; D04 l.917 and D06 l.941 add "primarily reflecting third-party
    professional service fees". D06 l.941 adds that "acquisition-related costs included in interest expense for fiscal 2025 include
    the amortization of financing fees ... and the excluded components" (plural; D05 l.166 has "component", singular).
  - MD&A: D02 l.1007, D04 l.1114 and D06 l.1136 say "primarily reflecting third-party professional service fees".
  - Business-combination notes: D04 l.547 "Acquisition related costs consist of miscellaneous professional service fees and expenses for our recent
    acquisitions. The Company recognized $161.0 million of acquisition-related costs, including $121.0 million related to
    amortization for step-up basis intangible assets" (6M). D06 l.550 gives "$232.1 million ... including $181.5 million" (9M), with "the
    Company's recent acquisitions".
  - The release prose says "Adjusted operating income ... which excludes $X million of Paycor acquisition-related costs included in
    selling, general and administrative expenses" (D03 l.79 $77.0M; D05 l.73 $71.0M). D02 l.1009, D04 l.1116 and D06 l.1138 give no amount.
- Tax-item label and definition: D01 and D02 use "Discrete tax windfall related to employee stock-based compensation payments". The footnote reads
  "Net tax windfall related to stock-based compensation payments ... option holder decisions related to exercising stock options"
  (D01 l.338) or "option-holder decisions relating to" (D02 l.1080). D03-D06 use "Discrete tax shortfall/(windfall) ...". Their footnote reads "Net
  tax shortfall/(windfall) related to employee stock-based compensation payments ... employee decisions on exercising employee
  stock options" (D03 l.164; D04 l.1176; D05 l.169; D06 l.1209).
- Requested labels that do not occur in the bundle: "excess tax benefit" and "net gain/loss on ... investments" (searched all six). The nearest
  lines are "Net realized (gains)/losses on sales of AFS securities" in the cash flows and Notes E/F, and the realized-gain tables.
- Footnote (3), on per-line EPS computation and ±$0.01, appears in all six (D01 l.341; D02 l.1083; D03 l.167; D04 l.1179; D05 l.172; D06 l.1212).
- Measures-definition paragraph ("In addition to reporting operating income...") appears in D02 l.1085-1089, D03 l.169-171, D04 l.1181-1185,
  D05 l.174-178 and D06 l.1214-1218. It is absent from D01.

### D. Balance sheets by date

| Line | May 31, 2025 | Nov 30, 2025 | Feb 28, 2026 | May 31, 2026 | Aug 31, 2026 |
|---|---|---|---|---|---|
| Cash and cash equivalents | 1,628.6 | 1,485.6 | 1,742.5 | 1,088.2 | 600.9 |
| Restricted cash | 47.9 | 50.7 | 49.8 | 52.8 | 55.0 |
| Corporate investments | 34.5 | 37.6 | 38.1 | 36.3 | 333.3 |
| Interest receivable | 27.9 | 35.0 | 37.0 | 36.1 | 39.2 |
| Accounts receivable, net | 1,330.5 | 1,355.5 | 1,435.0 | 1,507.6 | 1,615.9 |
| PEO unbilled receivables, net | 616.6 | 640.0 | 598.8 | 664.2 | 680.2 |
| Prepaid income taxes | 38.9 | 56.8 | 37.7 | 11.2 | 11.5 |
| Prepaid expenses and other current | 378.3 | 372.5 | 378.2 | 384.7 | 409.2 |
| Current assets before funds held | 4,103.2 | 4,033.7 | 4,317.1 | 3,781.1 | 3,745.2 |
| Funds held for clients | 4,813.3 | 4,875.7 | 5,610.9 | 4,832.2 | 4,348.4 |
| Total current assets | 8,916.5 | 8,909.4 | 9,928.0 | 8,613.3 | 8,093.6 |
| Property and equipment, net | 511.5 | 551.2 | 569.2 | 588.9 | 614.6 |
| Operating lease ROU assets | 63.8 | 80.1 | 69.8 | 63.9 | 75.8 |
| Intangible assets, net | 1,947.3 | 1,812.3 | 1,748.2 | 1,684.0 | 1,626.2 |
| Goodwill | 4,514.1 | 4,527.3 | 4,526.6 | 4,527.4 | 4,534.1 |
| Long-term deferred costs | 482.4 | 504.1 | 530.0 | 555.8 | 571.0 |
| Other long-term assets | 128.5 | 134.5 | 139.6 | 141.2 | 145.4 |
| Total assets | 16,564.1 | 16,518.9 | 17,511.4 | 16,174.5 | 15,660.7 |
| Accounts payable | 129.8 | 137.6 | 132.4 | 154.8 | 141.4 |
| Accrued corporate compensation | 183.9 | 147.1 | 176.7 | 162.1 | 132.5 |
| Accrued worksite employee compensation | 735.8 | 807.2 | 824.6 | 844.8 | 824.7 |
| Short-term borrowings | 18.6 | 18.2 | — | (no line) | (no line) |
| Accrued income taxes (current) | — | 44.4 | 62.5 | 87.8 | 81.1 |
| Long-term debt/borrowings, current portion | 399.8 | 399.9 | 400.0 | (no line) | (no line) |
| Deferred revenue | 69.4 | 70.5 | 70.3 | 69.4 | 70.8 |
| Other current liabilities | 552.0 | 531.5 | 609.0 | 637.1 | 648.8 |
| Current liabilities before client fund obligations | 2,089.3 | 2,156.4 | 2,275.5 | 1,956.0 | 1,899.3 |
| Client fund obligations | 4,867.0 | 4,884.7 | 5,603.6 | 4,884.6 | 4,440.7 |
| Total current liabilities | 6,956.3 | 7,041.1 | 7,879.1 | 6,840.6 | 6,340.0 |
| Accrued income taxes (long-term) | 119.0 | 130.5 | 136.6 | 140.5 | 145.5 |
| Deferred income taxes | 444.7 | 531.9 | 553.5 | 543.3 | 537.6 |
| Long-term borrowings, net | 4,548.4 | 4,552.2 | 4,554.1 | 4,556.1 | 4,558.0 |
| Operating lease liabilities | 55.5 | 66.6 | 59.3 | 52.2 | 62.9 |
| Other long-term liabilities | 312.2 | 316.5 | 315.2 | 306.7 | 311.2 |
| Total liabilities | 12,436.1 | 12,638.8 | 13,497.8 | 12,439.4 | 11,955.2 |
| Shares issued and outstanding (millions) | 360.5 | 359.0 | 358.3 | 355.6 | 356.0 |
| Common stock / APIC | 3.6 / 1,901.1 | 3.6 / 1,944.1 | 3.6 / 1,965.4 | 3.6 / 1,975.6 | 3.6 / 1,994.8 |
| Retained earnings | 2,277.0 | 1,950.0 | 2,047.3 | 1,805.8 | 1,788.4 |
| Accumulated other comprehensive loss | (53.7) | (17.6) | (2.7) | (49.9) | (81.3) |
| Total stockholders' equity | 4,128.0 | 3,880.1 | 4,013.6 | 3,735.1 | 3,705.5 |

- Locations: May 31, 2025 at D03 l.246-292, D04 l.137-184, D05 l.274-320 and D06 l.137-184, identical in all four. Nov 30, 2025 at D03 and D04. Feb 28, 2026
  at D05 and D06. May 31 and Aug 31, 2026 at D01 l.186-230 and D02 l.137-182. Pairs are identical apart from labels. The current-debt line is
  "Long-term borrowings, net, current portion" in the releases (D03 l.274; D05 l.302) and "Long-term debt, net, current portion"
  in the 10-Qs (D04 l.165; D06 l.165).
- AOCL split (equity statements): AFS / cash-flow hedges / foreign currency. May 31, 2024 (120.7)/—/(24.4); Aug 31, 2024
  (58.9)/(21.4); Nov 30, 2024 (63.1)/—/(28.8); Feb 28, 2025 (49.5)/(8.6)/(31.5); May 31, 2025 (38.5)/—/(15.2); Aug 31, 2025
  (14.2)/(10.8); Nov 30, 2025 (5.3)/—/(12.3); Feb 28, 2026 7.0/—/(9.7); May 31, 2026 (37.8)/(12.1); Aug 31, 2026 (68.1)/(13.2).
- Cover-page share counts (exact): 358,967,450 (Nov 30, 2025, D04 l.62); 358,290,881 (Feb 28, 2026, D06 l.62); 355,980,473
  (Aug 31, 2026, D02 l.62). The par value prints as "$.01" in D04/D06 and "$0.01" in D02.

### E. Cash flows (cumulative periods only)

| Line | Q1 FY26 | Q1 FY27 | 6M FY25 | 6M FY26 | 9M FY25 | 9M FY26 |
|---|---|---|---|---|---|---|
| Net income | 383.8 | 429.7 | 840.8 | 779.2 | 1,360.1 | 1,339.5 |
| Depreciation and amortization | 109.3 | 109.8 | 80.7 | 218.4 | 123.8 | 329.4 |
| Amortization of premiums/discounts, net | (2.1) | (2.2) | (5.6) | (4.1) | 5.1 | (5.7) |
| Amortization of deferred contract costs | 60.4 | 66.0 | 117.3 | 121.8 | 176.6 | 184.6 |
| Stock-based compensation | 26.8 | 19.3 | 32.9 | 52.3 | 50.5 | 75.4 |
| Deferred income taxes provision/(benefit) | 66.0 | 9.3 | (9.5) | 77.2 | (16.1) | 99.0 |
| Provision for credit losses | 7.7 | 8.6 | 12.4 | 12.2 | 17.6 | 29.1 |
| Net realized (gains)/losses on AFS | 0.0 | (0.0) | (0.0) | (7.1) | 0.4 | (7.4) |
| Premiums paid on cash flow hedges | — | — | — | — | (19.2) | — |
| Net cash from operating activities | 718.4 | 413.5 | 841.1 | 1,163.3 | 1,557.1 | 1,975.8 |
| Purchases of AFS securities | (3,731.9) | (5,072.2) | (5,168.5) | (6,527.9) | (8,473.2) | (10,699.4) |
| Proceeds from sales/maturities of AFS | 2,547.3 | 4,880.7 | 5,163.6 | 5,804.5 | 8,500.4 | 10,054.1 |
| Net purchases of short-term receivables | (47.0) | (63.2) | (200.1) | (65.2) | (153.3) | (85.3) |
| Purchases of property and equipment | (55.9) | (56.1) | (82.6) | (118.0) | (131.3) | (169.0) |
| Acquisition of businesses, net | (0.2) | (18.1) | — | (0.3) | — | (0.4) |
| Purchases of other assets, net | (15.0) | (6.9) | (15.1) | (19.5) | (24.3) | (25.0) |
| Net cash used in investing | (1,302.7) | (335.8) | (302.7) | (926.4) | (281.7) | (925.0) |
| Net change in client fund obligations | 81.4 | (443.9) | 26.3 | 17.7 | 383.1 | 736.6 |
| Net change in short-term borrowings | — | — | — | — | — | (18.8) |
| Dividends paid | (389.1) | (424.1) | (706.2) | (777.0) | (1,059.2) | (1,165.0) |
| Repurchases of common shares | (160.1) | — | (104.5) | (286.6) | (104.5) | (361.6) |
| Contingent consideration paid | — | (15.0) | — | — | — | — |
| Debt issuance fees | — | — | — | — | (11.4) | — |
| Equity-based plans | (47.6) | (23.6) | 8.0 | (51.9) | 12.9 | (53.7) |
| Net cash used in financing | (515.4) | (906.6) | (776.4) | (1,097.8) | (779.1) | (862.5) |
| Net change in cash, restricted cash and equivalents | (1,099.7) | (828.9) | (238.0) | (860.9) | 496.3 | 188.3 |
| Beginning / end of period | 2,734.3 / 1,634.6 | 1,484.8 / 655.9 | 1,897.0 / 1,659.0 | 2,734.3 / 1,873.4 | 1,897.0 / 2,393.3 | 2,734.3 / 2,922.6 |
| End: cash / restricted / in funds held | 809.0/50.4/775.2 | 600.9/55.0/— | 1,202.1/63.1/393.8 | 1,485.6/50.7/337.1 | 1,563.8/49.1/780.4 | 1,742.5/49.8/1,130.3 |

- Locations: D01 l.238-283 and D02 l.240-285; D03 l.300-344 and D04 l.280-324; D05 l.328-375 and D06 l.280-327. Each pair is identical.
  The MD&A summaries (D02 l.1179-1187; D04 l.1271-1279; D06 l.1306-1314) repeat the three subtotals with a $ change column and give "Cash
  dividends per common share" ($1.19/$1.08; $2.16/$1.96; $3.24/$2.94). The D02 summary header reads "In millions, except per share
  amounts"; the D04/D06 headers read "In millions".
- The May 31, 2026 funds-held restricted cash equivalents (343.8) are printed only in D02 Note E (l.542). The total 1,484.8 at l.279 equals
  1,088.2+52.8+343.8 (derived).
- MD&A driver headings use fiscal-year labels for the interim periods: "Fiscal 2027"/"Fiscal 2026" = 3M (D02 l.1193-1269);
  "Fiscal 2026"/"Fiscal 2025" = 6M (D04 l.1287-1360) and 9M (D06 l.1320-1390).

### F. Equity, dividends and repurchases

- Dividends declared (equity statements) and paid:

| Period | Declared per share | Declared $ | Paid $ | Locations |
|---|---|---|---|---|
| Q2 FY25 | $0.98 | 352.9 | 352.8 | D04 l.257, l.976 |
| 6M FY25 | $1.96 | 705.7 | 706.2 | D04 l.242, l.313; D03 l.333 |
| Q3 FY25 | $0.98 | 353.2 | 353.0 | D06 l.257, l.996 |
| 9M FY25 | $2.94 | 1,058.9 | 1,059.2 | D06 l.242, l.315; D05 l.363 |
| Q1 FY26 | $1.08 | 389.0 | 389.1 | D02 l.217, l.273, l.864; D01 l.271 |
| Q2 FY26 | $1.08 | 388.0 | 387.9 | D04 l.219, l.976 |
| 6M FY26 | $2.16 | 777.0 | 777.0 | D04 l.204, l.313; D03 l.123, l.333 |
| Q3 FY26 | $1.08 | 388.0 | 388.0 | D06 l.219, l.996 |
| 9M FY26 | $3.24 | 1,165.0 | 1,165.0 | D06 l.204, l.315; D05 l.117, l.363 |
| Q4 FY26 | not printed | not printed | not printed | — |
| Q1 FY27 | $1.19 | 423.6 | 424.1 | D02 l.202, l.273, l.864; D01 l.75, l.271 |

- Repurchases:

| Period | Shares (M) | $ | Average price | Locations |
|---|---|---|---|---|
| 6M FY25 (9M FY25 is the same amount) | 0.8 | 104.5 incl. $0.5 excise | $125.50 | D04 l.243, l.1357; 9M FY25 row D06 l.243; D06 l.1387 |
| Q2 FY25 | — | 0.5 (excise only) | — | D04 l.258 |
| Q3 FY25 | — | — (excise $0.0) | — | D06 l.258 |
| Q1 FY26 | 1.1 | 160.1 | $145.59 | D02 l.218, l.1269; D01 l.272 |
| Q2 FY26 (Oct 2025 only; Sept and Nov none) | 1.0 | 126.5 | $122.54 | D04 l.220, l.1495-1498 |
| 6M FY26 | 2.1 | 286.6 | $134.43 | D04 l.205, l.1347; D03 l.126 |
| Q3 FY26 (Jan 0.5M at $102.59 = 50.0; Feb 0.3M at $92.65 = 25.0; Dec none) | 0.8 | 75.0 | $99.05 | D06 l.220, l.1525-1528 |
| 9M FY26 | 2.9 | 361.6 | $125.16 | D06 l.205, l.1376; D05 l.120 |
| Q4 FY26 | not printed | not printed | not printed | — |
| Q1 FY27 | — | — | — | D02 l.203, l.1404-1407; D01 l.272 |

- Remaining authorization ("Approximate dollar value of shares that may yet be purchased"): $135.9 after Sept 2025 and $9.4 after Oct and Nov 2025 (D04
  l.1495-1498); $9.4 after Dec 2025, $950.0 after Jan 2026 and $925.0 after Feb 2026 (D06 l.1525-1528); $675.6 after June, July and Aug 2026 (D02
  l.1404-1407). (Derived) the remaining amount fell by 249.4 between the Feb 2026 row (925.0) and the June 2026 row (675.6, with June
  purchases "—"). No document prints repurchases for Mar-May 2026 (Q4 FY26).
- Program descriptions, as printed:
  - D04 equity footnote (2), l.230 and l.268: "The Company maintains a program to repurchase $400.0 million of its common stock, with
    authorization expiring May 31, 2027." No "up to".
  - D04 Part II, l.1491: "...program to repurchase up to $400.0 million ... with authorization that expires on May 31, 2027."
  - D06 l.230, 268 and 1521, and D02 l.228 and 1400: "maintained a program to repurchase up to $400.0 million ... with authorization that expired on
    January 16, 2026, at which time $9.4 million of unused repurchase authorization expired. On January 16, 2026, the Company's Board
    approved a program to repurchase up to an additional $1.0 billion of its common stock with no expiration date."
  - All three 10-Qs: "The purpose of this program is to manage common stock dilution. All shares ... repurchased were retired."

### G. Debt and credit facilities

- Long-term borrowings, amortized cost / fair value:

| Instrument | Terms | May 31, 2025 | Nov 30, 2025 | Feb 28, 2026 | May 31, 2026 | Aug 31, 2026 |
|---|---|---|---|---|---|---|
| Senior Notes, Series A | $0.4B, 4.07%, due Mar 13, 2026 | 399.8 / 398.3 | 399.9 / 399.9 | 400.0 / 400.0 | (repaid) | (repaid) |
| Senior Notes, Series B | $0.4B, 4.25%, due Mar 13, 2029 | 399.3 / 395.5 | 399.4 / 402.3 | 399.4 / 403.1 | 399.5 / 397.4 | 399.5 / 394.3 |
| 5-year bonds | $1.5B, 5.10%, Apr 15, 2030 | 1,484.8 / 1,505.1 | 1,486.3 / 1,528.5 | 1,487.1 / 1,519.0 | 1,487.9 / 1,504.9 | 1,488.7 / 1,489.3 |
| 7-year bonds | $1.5B, 5.35%, Apr 15, 2032 | 1,482.7 / 1,504.9 | 1,483.9 / 1,544.1 | 1,484.6 / 1,522.6 | 1,485.2 / 1,504.3 | 1,485.8 / 1,485.4 |
| 10-year bonds | $1.2B, 5.60%, Apr 15, 2035 | 1,181.6 / 1,201.9 | 1,182.6 / 1,243.1 | 1,183.0 / 1,212.7 | 1,183.5 / 1,194.2 | 1,184.0 / 1,175.5 |
| Total | | 4,948.2 / 5,005.7 | 4,952.1 / 5,118.0 | 4,954.1 / 5,057.4 | 4,556.1 / 4,600.8 | 4,558.0 / 4,544.5 |

- Locations: D04 l.833-842; D06 l.840-849; D02 l.721-729. Terms are at D04 l.1233-1239, D06 l.1264-1270 and D02 l.1139-1145. Series A/B interest is paid March
  and September; bonds April and October. Labels differ: "5-Year Fixed Rate Corporate Bonds" (D04, D06) and "5-Year Fixed Rate Bonds" (D02). Prose totals:
  "$0.8 billion" of Senior Notes (D04 l.1231; D06 l.1262) and "$0.4 billion" (D02 l.1137); "$4.2 billion" of Corporate Bonds in all three.
- Series A repayment: D06 l.883 and l.1272 say "Subsequent to February 28, 2026, the Company repaid ... $400.0 million, which matured on March 13, 2026". D02 l.758 and
  l.1147 say "During fiscal 2026". D04 l.866 says "no material changes ... subsequent to May 31, 2025"; D06 l.881 "during the nine months"; D02 l.756
  "during the three months ended August 31, 2026".
- Credit facilities:

| Facility | As of Nov 30, 2025 (D04 l.1199-1207) | As of Feb 28, 2026 (D06 l.1234-1241) | As of Aug 31, 2026 (D02 l.1103-1110) |
|---|---|---|---|
| 2019 JPM | $1,000.0, expires Apr 12, 2029; nothing outstanding | same | same |
| 2017 JPM | $750.0, expires Sept 17, 2026 | $1,000.0, expires Jan 23, 2031 | same as Feb 28, 2026 |
| PNC (D02/D06 call it the "2020 PNC Credit Facility") | $250.0, expires Feb 6, 2026; 18.2 outstanding; 231.8 available | terminated | terminated |
| Total outstanding / available | 18.2 / 1,981.8 | — / 2,000.0 | — / 2,000.0 |

- The amendment took effect Jan 23, 2026 (D06 l.872-875 and l.1243; D02 l.747-750 and l.1114-1117). At its termination, "no outstanding loans under" the
  PNC facility. The unused amount is "approximately $2.0 billion" at every date (D04 l.860; D06 l.870; D02 l.743). The weighted-average rate on
  outstanding borrowings was 3.53% at Nov 30, 2025 and 3.87% at May 31, 2025 (D04 l.860; D06 l.870 gives the May 31, 2025 rate only).
- Borrowing activity in each quarter (days / maximum / weighted-average amount / rate):
  - Q2 FY26 (D04 l.1215-1223): $1B JPM 3 / $210.0 / 159.2 / 7.05%; $750M JPM —; PNC 91 / $243.4 / 31.3 / 4.48%.
  - Q3 FY26 (D06 l.1247-1254): 2019 facility 1 / $370.0 / 370.0 / 7.00%; 2017 facility —; 2020 PNC 28 / $243.3 / 26.5 / 4.16%.
  - Q1 FY27 (D02 l.1122-1129): 2019 facility 22 / $1,000.0 / 483.5 / 4.51%; 2017 facility 1 / $200.0 / 200.0 / 4.50%; 2020 PNC — (the column is still
    printed).
- Financing tied to the Paycor acquisition: $4.2B of bonds issued to finance it (D04 l.545; D06 l.548). Bridge loan and swaptions: D06 l.887-889 and
  l.1276-1278 only. The 9M FY25 cash flow shows premiums (19.2) and debt issuance fees (11.4) (D05 l.342 and l.365; D06 l.294 and l.317).
- Letters of credit: $165.0M at May 31, 2025; $172.9M at Nov 30, 2025, expiring Dec 01, 2025 to Feb 28, 2027 (D04 l.864, 1229); $179.1M at Feb 28, 2026,
  expiring Mar 03, 2026 to Feb 28, 2027 (D06 l.879, 1258); $176.5M at May 31, 2026; $173.0M at Aug 31, 2026, expiring Sept 01, 2026 to Dec 24, 2027 (D02
  l.754, 1135). None were drawn.

### H. Funds held for clients, investments and interest

- Average balances and rates (10-Q MD&A only: D04 l.1047-1059; D06 l.1069-1081; D02 l.927-939). Rates are "exclusive of net realized
  (losses)/gains".

| Period | Funds held avg | Corporate avg | Total avg | Rate funds / corporate / combined | Net realized gains/(losses) |
|---|---|---|---|---|---|
| Q2 FY25 | 4,252.3 | 1,471.4 | 5,723.7 | 3.4% / 4.3% / 3.6% | 0.0 |
| 6M FY25 | 4,269.2 | 1,545.6 | 5,814.8 | 3.4% / 4.6% / 3.8% | (0.0) |
| Q3 FY25 | 5,116.8 | 1,541.4 | 6,658.2 | 3.4% / 4.3% / 3.6% | (0.4) |
| 9M FY25 | 4,551.7 | 1,544.3 | 6,096.0 | 3.4% / 4.5% / 3.7% | (0.4) |
| Q1 FY26 | 5,400.0 | 1,776.9 | 7,176.9 | 3.5% / 4.2% / 3.7% | (0.0) |
| Q2 FY26 | 5,353.2 | 1,683.1 | 7,036.3 | 3.5% / 3.9% / 3.6% | 7.1 |
| 6M FY26 | 5,376.6 | 1,730.0 | 7,106.6 | 3.5% / 4.1% / 3.7% | 7.1 |
| Q3 FY26 | 6,464.8 | 1,765.9 | 8,230.7 | 3.5% / 3.4% / 3.5% | 0.3 |
| 9M FY26 | 5,739.3 | 1,742.0 | 7,481.3 | 3.5% / 3.9% / 3.6% | 7.4 |
| Q1 FY27 | 5,401.6 | 1,240.9 | 6,642.5 | 3.7% / 3.3% / 3.6% | 0.0 |

- Market tables, at May 31, 2025 / Nov 30, 2025 / Feb 28, 2026 / May 31, 2026 / Aug 31, 2026:
  - Net unrealized gains/(losses) on AFS: (53.6) / (9.0) / 7.2 / (52.5) / (92.4).
  - Federal Funds rate as printed: 4.50% / 4.00% / 3.75% / 3.75% / 3.75%. Footnotes give the ranges 4.25-4.50%, 3.75-4.00%, 3.50-3.75%,
    3.50-3.75% and 3.50-3.75%; the table prints the upper bound.
  - AFS fair value: 3,755.5 / 4,538.6 / 4,480.8 / 4,488.4 / 4,644.1.
  - Duration (years): 2.2 / 3.0 / 3.0 / 3.1 / 3.1. Yield to maturity: 3.3% / 3.6% / 3.6% / 3.7% / 3.8%. Both exclude VRDNs.
  - Locations: D04 l.1063-1076; D06 l.1085-1098; D02 l.943-956.
- AFS securities in an unrealized loss position: 600 (about 50%) at May 31, 2025; 489 (41%) at Nov 30, 2025; 415 (37%) at Feb 28, 2026; 664 (60%) at May 31, 2026;
  821 (77%) at Aug 31, 2026 (D04 l.678; D06 l.682; D02 l.573). Gross unrealized losses: 68.0, 42.1, 31.4, 59.8 and 94.2. The fair value below amortized cost is
  "$1.9 billion" (D04 l.1431), "$1.6 billion" (D06 l.1463) and "$3.8 billion" (D02 l.1342).
- Investment tables: D04 l.623-655 (Nov 30, 2025 and May 31, 2025); D06 l.626-659 (Feb 28, 2026 and May 31, 2025, identical to D04's May 31, 2025);
  D02 l.519-550 (Aug 31, 2026 and May 31, 2026). Funds-held money market securities and other restricted cash equivalents: 1,057.8 / 337.1 /
  1,130.3 / 343.8 / $— (Aug 31, 2026). VRDN rows: 0.2 (Feb 28, 2026) and 204.3 (Aug 31, 2026); no row at the other dates. The composition of
  restricted cash equivalents is described at D04 l.657 (commercial paper, U.S. government agency and treasury, money market funds) and D06 l.661 (adds corporate
  and municipal bonds). The fair-value tables print "Total restricted and unrestricted cash equivalents" of 663.4 (May 31, 2025), 833.2, 1,357.4, 25.3
  (May 31, 2026) and $— (Aug 31, 2026) (D04 l.785, 809; D06 l.791; D02 l.675, 697). The scope differs from the Note E/F money-market line, and
  the documents do not reconcile the two.
- Classification: total funds held and corporate investments 4,847.8 / 4,913.3 / 5,649.0 / 4,868.5 / 4,681.7 (D04 l.669-674; D06 l.673-678; D02
  l.564-569).
- Client fund obligations: 4,867.0 / 4,884.7 / 5,603.6 / 4,884.6 / 4,440.7 (balance sheets, section D). Collections are "typically remitted from one to
  30 days after receipt, with some items extending to 90 days" (D02 l.1173; D04 l.1267; D06 l.1302).
- Subsequent-date unrealized loss: about $15.8M at Dec 17, 2025 (D04 l.1072); $55.3M at Mar 24, 2026 (D06 l.1094); $151.2M at Sept 23, 2026 (D02 l.952).
- Federal Funds rate events: cut to 3.50-3.75% effective Dec 11, 2025 (D04 l.1074, 1393); raised to 3.75-4.00% effective Sept 17, 2026 (D02
  l.954, 1304). D06 l.1096 and l.1425 give no change.

### I. Same-period figures in more than one document

- The release/10-Q pairs (D01/D02, D03/D04, D05/D06) print identical income statements, balance sheets, cash flows and non-GAAP
  reconciliations. Differences are in labels and columns only:
  - D01 titles the statement "CONSOLIDATED STATEMENTS OF INCOME" with Change columns; D02 adds "AND COMPREHENSIVE INCOME" and the OCI lines.
  - The current-debt label differs, as noted in D.
  - The 10-Q highlights tables add "Total service revenue", "Adjusted net income" and "Dividends paid to stockholders" rows (D02 l.856-864; D04 l.968-976;
    D06 l.988-996).
- May 31, 2025 balance sheet (D03, D04, D05, D06) and investment tables (D04, D06): identical.
- Equity balances repeated across editions: Aug 31, 2025 (D02 l.222 end of period = D04 l.215 start, 3,970.6); Nov 30, 2025 (D04 l.209/224 = D06 l.215,
  3,880.1); Nov 30, 2024 (D04 l.247/262 = D06 l.253, 3,925.7); May 31, 2024 (D04 l.238 = D06 l.238, 3,801.0). All match.
- Q1 FY26 printed in D01/D02 against D03/D04 six months less Q2 (derived):
  - Every GAAP income-statement line matches, as do OCI 28.7 and comprehensive income 412.5.
  - Non-GAAP lines that match: acquisition costs 84.8, adjusted operating income 626.7, tax benefit (20.6), discrete item (7.2),
    adjusted net income 440.8, adjusted EPS 1.22, interest expense 68.2, corporate interest income (18.7), D&A 109.3 and EBITDA 656.3.
  - The note roll-forwards also match: allowance, material rights, contract costs, pass-through costs, other income, SBC 26.8, depreciation
    34.5 and amortization 74.8.
  - Differences:

| Item | D01/D02 print for Q1 FY26 | D03/D04 6M less Q2 |
|---|---|---|
| Amortization of Paycor intangibles | 61.1 | 121.0-60.0 = 61.0 |
| Other acquisition-related costs | 5.0 | 9.0-3.9 = 5.1 |
| EBITDA-block acquisition costs | 23.7 | 40.9-17.1 = 23.8 |
| Adjusted EBITDA | 680.0 | 1,378.5-698.4 = 680.1 |
| EPS acquisition-cost line | 0.23 | 0.45-0.21 = 0.24 (footnote (3) says lines are computed independently) |

- Q3 FY26 (D05/D06) against nine months less six months (D03/D04), derived: every non-GAAP and GAAP amount matches (for example amortization
  181.5-121.0 = 60.5, other costs 9.9-9.0 = 0.9, adjusted EBITDA 913.6). Diluted EPS is the exception (1.55 against 1.56, noted in B).
- Segment D&A in the 10-Qs against the footnote amortization, derived:
  - Q1 FY26: 109.3-48.2 = 61.1, consistent with D01/D02.
  - Q2 FY26: 109.1-49.1 = 60.0.
  - 6M FY26: 218.4-97.3 = 121.1, against the D03/D04 footnote's 121.0.
  - Q3 FY26: 111.0-50.6 = 60.4, against the D05/D06 footnote's 60.5.
  - 9M FY26: 329.4-147.9 = 181.5, consistent.
  - Q1 FY27: 109.8-52.9 = 56.9, consistent.
- Totals for the same period within one document:
  - D04: Note D l.547 gives "$161.0 million" for the six months; MD&A l.1114, segment l.905 and non-GAAP l.1144 give 161.9.
  - D06: Note D l.550 gives "$232.1 million" for nine months; segment l.928 and MD&A l.1114, 1136 and 1166 give 233.1.
  - D03: prose l.79 gives $77.0M; table l.134 gives 77.1. D05: prose l.73 gives $71.0M; table l.128 gives 71.2.
  - No document states which figure takes precedence.
- Values that recur at different dates (no conflict): deferred revenue 69.4 at both May 31, 2025 and May 31, 2026. Client fund obligations are 4,884.7
  (Nov 30, 2025) and 4,884.6 (May 31, 2026). Total intangible amortization is 74.8 in both Q1 FY26 (D02 l.741) and Q3 FY26 (D06 l.865). The interest-on-funds
  guidance range is $200-210 million for both FY2026 (D05 l.185) and FY2027 (D01 l.86).
- Mine entry D04 l.643-649 against D06 l.628-634 (1,057.8 against 1,130.3) compares May 31, 2025 with Feb 28, 2026, so these are different dates, not a
  changed figure. D06 l.651 repeats 1,057.8 for May 31, 2025.

### J. Paycor acquisition and purchase-accounting editions

- Facts common to D04 l.543-549 and D06 l.546-552: acquisition completed April 14, 2025; total consideration "approximately $4.1 billion, of which $4.06
  billion was paid in cash and $25.1 million ... in the form of replacement awards"; $4.2B of bonds issued to finance it; Paycor is a SaaS HCM provider "across all 50 states
  within the U.S."; "Paycor's fiscal year end was June 30" (D04 l.605; D06 l.608). The allocation "will be finalized no later than one year from the
  acquisition date" (D04 l.553; D06 l.556). D02 has no business-combination note.
- Purchase price allocation table, D04 edition (l.559-583) against D06 edition (l.562-586). Unchanged: total price 4,085.7; cash 168.8; restricted 0.0; interest
  receivable 0.7; AR 26.5; prepaid income taxes 1.0; funds held 1,288.2; P&E 27.6; ROU 9.1; intangibles 1,776.5; other LT assets 1.9; client funds obligation
  1,288.9; other LT liabilities 69.7. Changed:

| Line | D04 (as of Nov 30, 2025) | D06 (as of Feb 28, 2026) |
|---|---|---|
| Prepaid expenses and other current assets | 29.1 | 28.7 |
| Total assets | 3,329.4 | 3,329.0 |
| Current liabilities | 136.8 | 137.3 |
| Deferred income taxes | 342.4 | 338.5 |
| Total liabilities | 1,837.8 | 1,834.4 |
| Net assets | 1,491.6 | 1,494.6 |
| Goodwill | 2,594.1 | 2,591.1 |

- Goodwill-change text:
  - D04 l.557 and l.858, six months: "increased goodwill $6.5 million, primarily resulting from the write-down of a building by $4.9 million, net of deferred taxes of
    $1.9 million".
  - D06 l.560 and l.866, nine months: "increased goodwill $3.4 million ... offset by a reduction due to a change in deferred tax liability of $3.9 million related
    to return-to-provision adjustments from the predecessor's final tax return". l.866 calls it "a further reduction".
  - Both say "The impact of these changes on previously reported earnings was not material."
  - (Derived) the text implies a Q3 change of 3.4-6.5 = -3.1; the tables give 2,591.1-2,594.1 = -3.0.
  - D02 l.741: Q1 FY27 goodwill was "impacted by an immaterial acquisition and immaterial foreign currency translation".
- Pro forma (as if acquired June 1, 2023): Q2 FY25 revenues 1,485.8 and net income 332.7; 6M FY25 2,971.8 and 678.3 (D04 l.596-597); Q3 FY25 1,720.4 and 467.4;
  9M FY25 4,692.2 and 1,145.7 (D06 l.599-600).
- Paycor's contribution to Management Solutions revenue growth: "approximately 17%" for Q2 FY26 (D03 l.45; D04 l.1019 "for the second quarter and six
  months"); about 19% for Q3 FY26 (D05 l.45; D06 l.1037); about 18% for 9M FY26 (D06 l.1037). D01 and D02 give no figure.

### K. Guidance, outlook and forecast/actual pairs

- Fiscal 2026 outlook:
  - D03 l.175-184: the lead-in says it "excludes acquisition-related costs"; "Adjusted diluted earnings per share ... is now anticipated to grow in the range of 10% to 11%";
    "Other aspects of our guidance for fiscal 2026 remain unchanged from what we provided previously". The earlier values are not printed.
  - D05 l.182-188: the lead-in says "excluding acquisition-related costs"; "Interest on funds held for clients is now anticipated to be in the range of $200 million to
    $210 million"; "All other aspects of our fiscal 2026 guidance remain consistent with our prior outlook". The earlier range is not printed.
  - No full outlook table for fiscal 2026 is printed anywhere.
  - Full-year FY2026 actuals are not printed. The latest cumulative actuals are the 9M FY26 figures: interest on funds held 158.7; adjusted diluted EPS 4.19.
  - The base for growth (FY2025 adjusted diluted EPS) is not printed; only 6M FY25 2.30 and 9M FY25 3.79 are.
- Fiscal 2027 outlook (D01 l.79-89), with Updates column:
  - Total revenue growth 5% to 6%, no change.
  - Management Solutions growth 5% to 6%, no change.
  - PEO and Insurance Solutions growth 7% to 8%, previously 6% to 7%.
  - Interest on funds held $200 million to $210 million, previously $195 million to $205 million.
  - Adjusted operating margin ~44%, no change. Effective tax rate ~24%, no change.
  - Adjusted diluted EPS growth 7% to 9%, no change.
  - The "previously" values come from an outlook outside the bundle. FY2026 base values are not printed. Q1 FY27 actuals for comparison: Management Solutions
    +4%, PEO +12%, interest on funds held 49.8, adjusted operating margin 42.0%, ETR 24.0%, adjusted diluted EPS +10% (D01 l.37-55).
- Expectations in the 10-Qs and what happened later:
  - Average portfolio: about $7.4B expected for FY2026 (D04 l.1415; D06 l.1445); 6M FY26 actual 7,106.6 and 9M FY26 7,481.3; the full-year figure is not printed.
    About $7.0B expected for FY2027 (D02 l.1324); Q1 FY27 actual 6,642.5. The expected allocations are 40/60 (FY2026) and 35/65 (FY2027).
  - Series A, due Mar 13, 2026 (D04 l.1237; D06 l.1268), was repaid at maturity (D06 l.883; D02 l.758).
  - The PNC facility, shown expiring Feb 6, 2026 (D04 l.1206), was terminated Jan 23, 2026. The 2017 JPM facility, shown expiring Sept 17, 2026 (D04 l.1205), was extended to Jan 23, 2031 and
    increased to $1.0B.
  - The $400M program, shown expiring May 31, 2027 (D04), "expired on January 16, 2026" (D06, D02).
  - D04 l.1211 says the PNC amount "remain[s] outstanding as of the date of this report". At Feb 28, 2026 short-term borrowings were "—" and there were "no outstanding loans" at
    termination (D06 l.875).
  - One Big Beautiful Bill Act: "will be impacted in fiscal 2026 ... not expected to have a material impact" (D04 l.888; D06 l.911); later "were impacted in
    fiscal 2026 ... did not have a material impact" (D02 l.782).
  - ASU 2025-05: "applicable to the Company's fiscal year beginning June 1, 2026 ... currently evaluating" (D04 l.414; D06 l.417); later "adopted ... and elected
    the practical expedient ... did not have a material impact" (D02 l.367).
  - The 25-basis-point earnings sensitivity changes by edition: $5.5-6.0M (D04 l.1413), $5.0-5.5M (D06 l.1443), $4.5-5.0M (D02 l.1322). The fair-value sensitivity
    is $30.0-35.0M in all three.

### L. Headline prose that rounds or summarises table figures

- Revenue, segment and expense totals in billions (each document's entry above), with exact figures in the tables. D04 l.1014 "$3.1 billion" for the six
  months is the rounded form of 3,097.6.
- Amounts excluded from adjusted operating income: "$77.0 million" (D03 l.79) against 77.1, and "$71.0 million" (D05 l.73) against 71.2.
- Returned to shareholders: "Over $1.5 Billion" and "$1.5 billion" (D05 l.16, 38), with no sum printed. Liquidity totals: D01 l.64, D03 l.112 and D05 l.106 (sums derived
  above). Borrowings: "$5.0 billion" in D03 l.115 and D05 l.109 includes short-term and current portions; D04 l.1189 and D06 l.1222 say "long-term borrowings of $5.0
  billion".
- Margin prose matches the tables: D01 l.52; D03 l.79 and 100; D05 l.73 and 94; D02 l.1017-1018; D04 l.1124-1125; D06 l.1146-1147. D03 l.100 says "41.2% for both" six-month periods.
- Percent changes rest on unrounded numbers: D03 l.34; D05 l.34; D02 l.870 and 898; D04 l.982 and 1010; D06 l.1002 and 1030. D01 has no such footnote.

### M. Footnotes and notes that change how a line is read

- Releases' footnote (1) on "Interest on funds held for clients" and "Other income, net" points to the 10-Q/10-K MD&A for further information (D01 l.177-178; D03
  l.234; D05 l.262).
- "n/m — not meaningful" applies to the interest-expense change (D03 l.238; D05 l.266; D04 l.1012; D06 l.1032).
- Equity footnote (1): reclassification adjustments for AFS sales "are reflected in interest on funds held for clients and other income, net" (D02 l.225; D04 l.227,
  265; D06 l.227, 265). Realized gains from the funds-held portfolio go to interest on funds held; those from the corporate portfolio go to other income (D02 l.609;
  D04 l.717; D06 l.723).
- "Certain disclosures are reported as zero balances due to rounding" (D02 l.303; D04 l.342; D06 l.345).
- The Reclassifications paragraph is in D04 l.347 and D06 l.350 and absent from D02. No reclassified lines are identified.
- Market-table footnotes: the subsequent-date unrealized loss, Federal Funds ranges, and the VRDN exclusion from duration and yield (D02 l.952-956; D04 l.1072-1076; D06 l.1094-1098).
- The 6M FY25 repurchase line includes $0.5 million of excise taxes (D04 l.243; D06 l.243).
- PEO revenue is "reported net of certain pass-through costs" (D02 l.404; D04 l.442; D06 l.445). Pass-through tables: Q1 FY26 7,356.1/23.7/175.5; Q1 FY27 8,713.5/27.7/214.4
  (D02 l.412-414); Q2 FY26 7,694.6/22.4/177.9; Q2 FY25 7,172.0/23.4/167.5; 6M FY26 15,050.7/46.1/353.4; 6M FY25 14,053.6/46.4/333.3 (D04 l.450-452); Q3 FY26
  8,587.8/88.6/193.8; Q3 FY25 7,783.0/81.5/172.6; 9M FY26 23,638.5/134.7/547.2; 9M FY25 21,836.6/127.9/505.9 (D06 l.453-455). Columns are payroll wages and taxes /
  state unemployment insurance (included in wages) / guaranteed cost benefit plans.
- Average rates exclude net realized gains and losses (D02 l.935; D04 l.1055; D06 l.1077).
- PEO workers' compensation structure:
  - D04 l.384 and D06 l.387: "For fiscal 2026 and fiscal 2025 ... aggregate maximum liability of $1.0 million for claims exceeding $1.0 million, and once met, the
    maximum individual claims liability is $1.0 million".
  - D02 l.343: "For fiscal 2027, the Company has a maximum individual claims liability of $1.0 million. For fiscal 2026, ... aggregate ...".
  - Reserves, current / long-term: 80.4/156.4 (May 31, 2025); 88.4/158.2 (Nov 30, 2025); 86.3/155.8 (Feb 28, 2026); 80.7/157.0 (May 31, 2026); 88.8/160.5 (Aug 31, 2026).
  - The health individual claims limit is $0.5M (D02 l.350; D04 l.388; D06 l.391). Health reserve amounts (67.0/64.3) are printed only in D02 l.351.

### N. Wording differences between parallel passages (mine checklist, confirmed)

- Impairment assessment:
  - Notes say "could change in the future due to new developments or changes in the Company's strategies" (D02 l.607; D04 l.715; D06 l.721).
  - Market risk in each 10-Q says "due to new developments, including changes in our strategies" (D02 l.1345; D04 l.1434; D06 l.1466).
- Rating sentence in market risk: "Most of the AFS securities in an unrealized loss position ... had an AA rating or better" (D02 l.1343) against "A substantial portion"
  (D04 l.1432; D06 l.1464). The notes say "A substantial portion" in all three (D02 l.603; D04 l.713; D06 l.719).
- Sale intent:
  - Liquidity section: "not more-than-likely that we would be required to sell" (D02 l.1095; D04 l.1191; D06 l.1224).
  - Notes and market risk: "not more-likely-than-not that it/we will be required to sell" (D02 l.607 and 1344; D04 l.714 and 1433; D06 l.720 and 1465).
- Tax-rate sentence: "both periods" (D02 l.1027) against "all periods" (D04 l.1134; D06 l.1156). Notes I/J say "Both periods were impacted" in all three (D02 l.780; D04 l.886;
  D06 l.907).
- Self-insurance:
  - "health and medical benefit plans" (D04 l.874 and 1251; D06 l.897 and 1284).
  - "health benefit plans, including medical, dental, vision, life insurance, and disability plans" (D02 l.766 and 1157).
- Captive insurance wording: D04 l.876 and 1253 and D06 l.899 and 1286 describe "gap coverage ... capacity for deductibles and self-insured retention(s)". D02 l.768 and
  1159 describe coverage "where commercial coverage is limited, unavailable, or not economically practical". The same six risk types appear in each.
- Operations and geography: D04 l.338 and D06 l.341 say "operations in India"; D02 l.299 says "operations in Canada, India, and Israel".
- Uses of cash and the liquidity outlook: D04 l.1189 and 1257 and D06 l.1222 and 1292 include "acquisitions"; D02 l.1093 and 1163 do not.
- Short-term investment vehicles: "U.S. government agency discount notes and bank demand deposit accounts" (D04 l.1374; D06 l.1406); D02 l.1283 adds VRDNs. Rate direction
  is described as "falling" in D04 l.1376 and D06 l.1408, and as "rising" in D02 l.1285.
- Contract termination notice: "30-day notice" (D04 l.428; D06 l.431); "30 days notice" (D02 l.390).
- Insurance offerings: D04 l.454 and D06 l.457 list "health, dental, vision, life and disability"; D02 l.416 lists "medical, dental, vision, life insurance, and disability plans".
- Business description: D04 l.338 and D06 l.341 say "advisory services ... payroll processing for businesses"; D02 l.299 says "advisory solutions ... payroll for customers". The D02 notes use "customers"
  where D04 and D06 use "clients" (for example D02 l.321 against D04 l.362).
- Releases: EPS-sentence footnotes say "are non-GAAP measures" (D01 l.57) against "are not U.S. GAAP measures" (D03 l.87 and 105; D05 l.81 and 99). The 10-Q highlight footnotes use
  "not U.S. generally accepted accounting principle ("GAAP") measures" (D02 l.867; D04 l.979; D06 l.999).
- Credit-facility reference: "Note M ... Form 10-K for fiscal 2026 ... as of May 31, 2026" (D02 l.1099); "fiscal 2025" (D04 l.1195; D06 l.1230 "as of May 31, 2025").
- Senior Notes fair-value sentence: Series A and B (D04 l.844; D06 l.851); Series B only (D02 l.731).

### O. Entities, aliases, people and outside organisations

- Issuer of all six: Paychex, Inc. (Delaware, formed 1979; 911 Panorama Trail South, Rochester, NY; Commission file 0-11330; IRS no. 16-1124166). The
  aliases "the Company", "Paychex", "we", "our" and "us" are defined in D03 l.18, D05 l.18 and the 10-Q MD&A intros.
- People: John Gibson or John B. Gibson (President and CEO; quoted in D01, D03 and D05; signs D02, D04 and D06); Robert L. Schrader (SVP and CFO, signer); Christopher Simmons
  (VP, Controller and Treasurer, signer); Rachel White (Head of IR); Tracy Volkmann (Manager, Public Relations).
- Subsidiaries: Paychex Insurance Agency, Inc. (D02 l.416; D04 l.454; D06 l.457); Paychex of New York LLC, "PoNY" (D06 l.872, 887, 1276, 1540-1541); Paychex Advance,
  LLC (D06 l.874).
- Outside organisations mentioned with figures, with period and the source cited:
  - Paycor HCM, Inc.: acquired company; consideration, allocation, pro forma and contribution percentages (sections J and C). The source is the issuer's own figures.
  - JPMorgan Chase Bank, N.A.: administrative agent and counterparty. Facilities in G; bridge loan up to $3.5B (Jan 7, 2025); swaptions with $3.0B notional (Jan 31, 2025);
    D06 l.887-889. No outside source is cited.
  - PNC Bank, N.A.: $250M facility (D04 l.1206; terminated Jan 23, 2026).
  - Federal Reserve: Federal Funds ranges and change dates (H). No source is cited.
  - FASB: ASU issue and effective dates (D02 l.367-386; D04 l.400-424; D06 l.403-427).
  - SEC: 10-K filing dates (July 11, 2025 in D04 l.1444 and D06 l.1474; July 17, 2026 in D02 l.1353) and the 8-K filed Jan 26, 2026 (D06 l.1243).
  - Legislation: the One Big Beautiful Bill Act, enacted July 4, 2025, and the CARES Act (D02 l.1205, 1216).
  - Mentioned without figures: Nasdaq; Microsoft (D01 l.32); "the U.S. President, the Federal Reserve and other government agencies" (market-risk sentences).
- Name variants: "JP Morgan Chase Bank" (D02 l.1108; D04 l.1204; D06 l.1239) against "JPMorgan Chase Bank" (D02 l.747; D06 l.872, 1540-1541). "PNC Bank, National Association"
  (D04 l.1206) against "PNC Bank, N.A." (D02 l.749, 1116; D06 l.874-875, 1243) and "2020 PNC Credit Facility" (D02 l.1116; D06 l.1243). "Paycor HCM, Inc." against "Paycor".
  "Corporate Bonds" against "Fixed Rate Bonds" (D02 l.726-728). Customer counts: about 800,000 (D03 l.199; D05 l.205) and about 840,000 (D01 l.100).

### P. Cross-references between documents and to outside filings

- Each release is paired with the 10-Q for the same quarter. D03 l.186-188 and D05 l.190-192 say the 10-Q will be filed within a couple of business days and the release "should be read in
  conjunction with" it. D01 has no such paragraph.
- The 10-Qs cite the 10-K for fiscal 2025 (D04, D06) or fiscal 2026 (D02); Note M (credit facilities); Note N (long-term financing; D02 l.1151; D04 l.1241; D06 l.1274);
  and the 10-K's Part I, Item 1 "Our Solutions" (D02 l.838; D04 l.948; D06 l.968).
- Internal note letters shift by edition, because D02 has no business-combination note. Segment reporting is Note J in D02 and Note K in D04 and D06. Commitments are Note H in D02 and Note I in D04 and D06.
  Supplemental information is Note G in D02 and Note H in D04 and D06.

### Q. Narrative passages that repeat table results

- D01 l.34-55 and l.59-75; D02 l.902-923, 960-1029 and 1093; D03 l.40-126; D04 l.1014-1134 and 1189; D05 l.40-120; D06 l.1034-1156 and 1222. Each restates (often
  rounded) figures from the statements and reconciliations above. Reasons for changes appear only in this prose: for example interest on funds held "due to higher
  average interest rates" (D01 l.46; D02 l.923); Q1 FY27 operating income growth "primarily reflecting revenue growth and lower acquisition-related costs" (D01 l.49);
  Q1 FY27 interest expense "decreased by $3.1 million ... reflecting lower outstanding debt balances" (D02 l.1023).

### R. Mine checklist disposition (notes/mine.md, corpus 09e5f180ed2e7fdf)

- §1 parallel-passage edits are confirmed in N; the release EPS sentences are identified in L. Pairs that differ only by period are not same-period changes. These are D01 l.55-57 against D03/D05; D05 l.257-260
  against D06 l.122-125 (Change column only); D04 l.643-649 against D06 l.628-634 (different dates); and D04 l.1304 against D06 l.1323 (FY2025 and FY2026 driver bullets).
- §2 restatements: confirmed in F (repurchase program), N and G (letters of credit at different dates).
- §3: the "Reclassification adjustment" rows are AOCI reclassifications, not restatements. The "Reclassifications:" paragraphs are D04 l.347 and D06 l.350. The "previously reported
  earnings" sentences are D04 l.557 and D06 l.560 (section J). No other restated same-period figure was found beyond I and J.
- §4: Q2 and Q3 cash flows are cumulative only (confirmed). The mine's "12 months in D02, D04, D06" did not hold up: no 12-month figures exist (section A).
- §5: every pair compares different periods (for example D01 Q1 FY27 against D03 Q2 FY26). None is a restatement.
- §6: name variants are in O. HR, SEC and U.S. are defined in D03 and D02 and used undefined in D01.
- §7: rounded prose is in L and the document entries. §8: release footnote (1) is in M. §9: "all 50 states" (D04 l.545; D06 l.548) has no enumeration in the bundle.
  §10: D04 "$3.1 billion" (L).
