# aq-05049 - document map

Maintained by the caller from `text/` (and `docs/` for layout issues).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

## Bundle

- What it is: two unrelated companies' quarterly filings. Docusign, Inc.: three earnings releases
  (Q3 FY2025, Q4/FY2025, Q1 FY2026) and the Q3 FY2025 Form 10-Q. Paylocity Holding Corporation:
  three earnings releases (Q1, Q2, Q3 FY2025). Page label "Corporate filings · Easy or Hard only".
- Documents: 7. Local ids are alphabetical by file name and differ from the page's Doc numbers:

| local | page | document |
| --- | --- | --- |
| D01 | Doc 1 | Docusign Q1 FY2026 release (qtr ended Apr 30, 2025; dated June 5, 2025) |
| D02 | Doc 3 | Docusign Q3 FY2025 release (qtr ended Oct 31, 2024; dated Dec 5, 2024) |
| D03 | Doc 4 | Docusign Q3 FY2025 Form 10-Q (qtr ended Oct 31, 2024; signed Dec 6, 2024) |
| D04 | Doc 2 | Docusign Q4 and FY2025 release (qtr and year ended Jan 31, 2025; dated Mar 13, 2025) |
| D05 | Doc 7 | Paylocity Q1 FY2025 release (qtr ended Sep 30, 2024; dated Oct 30, 2024) |
| D06 | Doc 6 | Paylocity Q2 FY2025 release (qtr ended Dec 31, 2024; dated Feb 6, 2025) |
| D07 | Doc 5 | Paylocity Q3 FY2025 release (qtr ended Mar 31, 2025; dated May 1, 2025) |

- Gaps: none. Capture "7 of 7 read in full"; `notes/intake.json` shows every document complete,
  `matches_capture: true`. Some release pages are blank in the capture (D04 "| 5 |", D01 has no
  definitions section, D05 has no definitions section); D03 MD&A pages 36-37 carry only the tables.
- Extraction spot-checks (2026-10-14, caller): plain-text captures, so extraction = capture body
  minus 2 trailing characters each. Checked D04 income statement and billings table, D03 Part II
  repurchase table and Note 13, D07 FCF table and footnotes (1)-(6): rows, units and labels intact.
- Provenance: `notes/intake.json` (capture sha256 fca2ee09...7d88); per-document hashes there.
- Coverage: the caller read D01, D02, D04-D07 in full and D03 lines 1-1413 and 2420-2516 in full;
  D03 lines 1414-2428 (legal proceedings, risk factors) were swept for figures (only the 10% and 6%
  workforce reductions, 26/25/23% international revenue, 36% employees abroad, 12 countries).

## Docusign (D01-D04)

- Fiscal year ends January 31 ("fiscal 2025" = year ended Jan 31, 2025). Columns newest first.
  Units: $ thousands except per-share; guidance in $ millions.
- Income statement, balance sheet, cash flow, non-GAAP reconciliations, FCF and billings tables in
  each release: D01 lines 141-405 (Q1 FY26 and Q1 FY25 only); D02 127-410 (Q3 and 9M, FY25 and
  FY24); D04 171-466 (Q4 and FY, FY25 and FY24). D03: statements 105-341, equity statement 207-266
  (Q3 roll from July 31, 2024 and 9M roll from Jan 31, 2024; no Q1 or Q2 roll), notes 369-901, MD&A
  905-1365 (non-GAAP tables 1273-1364), Part II repurchase table 2429-2452.
- No document prints the quarter ended July 31, 2024 (Q2 FY2025) by itself. Q1 FY2025 appears
  only as D01's comparative column. Verified: FY (D04) = 9M (D02/D03) + Q4 (D04) on every line.
- Guidance: D02 lines 61-83 (Q4 FY25, FY25); D04 93-119 (Q1 FY26, FY26, FX footnotes: revenue +0.7
  pts, billings +1.0 pts ex-FX); D01 85-111 (Q2 FY26, FY26; FX: revenue neutral, billings ~0.7
  points lower ex-FX).
- Definitions (D02 111-121, D04 153-163): non-GAAP measures exclude SBC, employer payroll tax on
  stock transactions, acquisition-related intangibles amortization, acquisition-related expenses,
  restructuring, etc.; fixed 20% non-GAAP tax rate "For fiscal 2024 and fiscal 2025" (D02) / "For
  each of the years ended January 31, 2025 and 2024" (D04). FCF = operating cash flow less purchases
  of property and equipment. Billings = revenue plus change in contract liabilities and refund
  liability less contract assets and unbilled receivables (text silent on acquisitions).
- Billings tables carry "contributed by acquisitions" lines in the 9M (D02 408-409, D03 1362-1363)
  and FY (D04 464-465) columns: (5,071) contract liabilities, +53 contract assets. D03 Note 5
  (lines 539-591): Lexion acquired May 31, 2024 for $154,020K; contract liabilities - current
  (5,071); escrow $17.4M; deferred compensation $19.1M; RSUs $34.8M; acquisition expenses $4.3M.
- Reconciliation "Add: Stock-based compensation" excludes SBC inside restructuring (D01 Q1 FY25
  137,876 vs cash-flow 142,504; restructuring SBC 4,628; 9M restructuring SBC 4,836).
- Tax: D03 Note 13 (lines 887-901): "$837.7 million, recorded as a discrete tax benefit during the
  three months ended July 31, 2024"; MD&A (1028, 1190) "$831.4 million". Two figures, same event.
- Repurchases: program $200.0M (Mar 2022) + $300.0M (Sep 2023) + $1.0B (May 2024) (D03 824, 2442-
  2444); D01 line 79: further $1.0B, "As of June 5, 2025 ... up to $1.4 billion". D03 Note 10 and
  equity statement amounts include the 1% excise tax ($523.7M 9M; $172.9M Q3); cash flow and Part II
  table exclude it (Part II: remaining $942,306K Aug 31, $834,762K Sep 30, $769,641K Oct 31, 2024;
  Q3 usage equals Q3 cash 172,665). Q4 FY25 cash 161,725 (D04); Q1 FY26 183,431 (D01).
- Customers: "Over 1.6 million" (D02, D03 Oct 31, 2024: ~256,000 enterprise and commercial; 1,075
  with ACV > $300,000), "Nearly 1.7 million" (D04 boilerplate), "Over 1.7 million" (D01).
  RPO $2.3B at Oct 31, 2024, 56% within 12 months (D03 442). International 28% (D03 974).
- Rounded prose beside exact tables: highlights (e.g., "$1.1 billion" cash and investments each
  quarter; growth rates to whole percent).

## Paylocity (D05-D07)

- Fiscal year ends June 30 ("fiscal year 2025" = year ending June 30, 2025). Columns OLDEST first
  (2023 then 2024). Units: $ thousands; guidance in $ millions.
- Tables: D05 85-327 (Q1 only); D06 79-327 (Q2 and 6M; cash flow 6M only); D07 79-328 (Q3 and 9M;
  cash flow 9M only). Footnotes (1)-(6) on "Other items": D05 329-335, D06 329-339, D07 330-340.
- Definitions only in D06 341-375 and D07 342-376: Adjusted EBITDA margin over total revenues; the
  "excluding interest income on funds held for clients" margins over recurring and other revenue;
  the adjusted FCF margin sentence says "dividing free cash flow by total revenues" (slip).
- FCF measure change: D05 lines 321-327 "Free cash flow excluding interest income on funds held for
  clients" (Q1 FY25 44,066 = 73,917 - 29,851). D06 316-327 and D07 317-328 print "Adjusted free cash
  flow" (= FCF + "Cash paid for other items (6)": 6M 5,073, 9M 6,723) and its ex-interest version
  (6M 56,702; 9M 192,624). No Q1 cash paid for other items is printed.
- Guidance: D05 53-75 (Q2, FY), D06 49-71 (Q3, FY), D07 49-71 (Q4, FY). Interest income on funds
  held for clients is never guided directly; implied as total minus recurring (= Adjusted EBITDA
  minus ex-interest): Q2 26.5, FY 108 (D05); Q3 29.0, FY 113 (D06); Q4 27.4, FY 120 (D07).
- Airbase acquired Oct 1, 2024 (D05 13, 18, 47); $325.0M drawn on the credit facility in Q1 (D05
  211); $81.25M repaid in Q3 (D07 43, 207); debt $243,750K at Mar 31, 2025. Acquisitions cash
  (278,001) 6M, (277,851) 9M; liabilities assumed 55,730.
- Repurchases: none in Q1; (8,395) 6M; (91,080) 9M. D07 line 15 (CEO): "$150 million or
  approximately 800,000 shares repurchased through April of this fiscal year". Retained earnings
  move only by net income. D06 line 15: max PEPY $600.

## Shared ground (navigation only)

- Entities in more than one document: Docusign (D01-D04), Lexion (D02, D03), Paylocity (D05-D07),
  Airbase (D05-D07). The two companies never mention each other.
- Periods covered by more than one document: Docusign Q3 FY25 and 9M (D02 = D03 tables); FY25 vs
  9M + Q4 (D04 vs D02/D03); Q1 FY25 (D01 comparative only); balances Jan 31, 2025 (D04, D01).
  Paylocity Q1 (D05) inside 6M (D06) inside 9M (D07); June 30, 2024 balance sheet in all three.
- Citing/amending relationships: none between documents; guidance editions supersede each other
  (Docusign FY26 guidance D04 -> D01; Paylocity FY25 guidance D05 -> D06 -> D07).
- Forecast/actual pairs: Docusign Q4 FY25 and FY25 guidance (D02) vs actuals (D04); Q1 FY26
  guidance (D04) vs actual (D01, billings 739.6 below the 741-751 range). Paylocity Q2 guidance
  (D05) vs actual (D06); Q3 guidance (D06) vs actual (D07).
