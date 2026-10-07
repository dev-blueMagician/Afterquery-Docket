# aq-00964 - document map

Written once by `bundle-mapper` from `text/` (and `docs/` for flattened tables and scans).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

## Bundle

- What it is: seven American Tower Corporation (NYSE: AMT) Exhibit 99.1 press releases: one
  2021-11-15 joint AMT/CoreSite acquisition announcement (D01) and six quarterly earnings
  releases covering Q1 2025, Q2 2025, Q3 2025, Q4/FY 2025, Q1 2026 and Q2 2026 (D02-D07).
- Documents: 7; ids D01-D07 from `text/manifest.json`; local Dnn = platform Doc N (Doc 1-7).
- Gaps: no pages/scans (all plain-text captures). D02-D07 contain 145 capture-gap markers
  "[... N characters not shown on the page ...]" (D02 23, D03 23, D04 23, D05 31, D06 22, D07 23);
  the originals in `docs/` carry the identical markers (grep count 2026-10-05), so the cut
  content is not recoverable locally. Every gap falls inside the financial-statement /
  reconciliation tables (balance sheet, statement of operations, cash flows, segment tables,
  Adjusted EBITDA / FFO / AFFO reconciliations, segment gross margin reconciliations); no
  narrative, outlook or definition section is cut. Per-gap lists are under each document.
- Provenance: `notes/intake.json` (schema 1; capture_sha256 9ab6d4ec...7638). Every source
  sha256 matches the capture. D01 complete; D02-D07 flagged incomplete (D02 56,573 of 64,381
  chars on page; D03 55,986/64,067; D04 56,214/64,678; D05 60,861/71,882; D06 45,569/52,981;
  D07 47,774/55,849). No recovered-source history.

## D01 - "AMERICAN TOWER TO ACQUIRE CORESITE" (Exhibit 99.1)

- Source: `docs/amt_ex991_2021-11-15.txt` | text, 109 lines; filing file "d245474dex991.htm"
  (l.5); page footers "Page 2 of 4" (l.79), "Page 3 of 4" (l.101), "Page 4 of 4" (l.109).
- Written or submitted by: joint release of American Tower Corporation and CoreSite Realty
  Corporation, dateline "Boston, Massachusetts and Denver, Colorado - November 15, 2021"
  (l.27). Contacts: "ATC Contact: Adam Smith, Vice President, Investor Relations" (l.13-15);
  "CoreSite Contact: Kate Ruppe, Manager, Investor Relations" (l.19-21).
- Type, date, edition: transaction announcement (not an earnings release), 2021-11-15.
- Period covered: CoreSite metrics "as of Q3 2021" / "in Q3 2021" (l.33); risk factors cite
  Forms 10-K "for the year ended December 31, 2020" (l.91).
- Entities and aliases: American Tower Corporation (NYSE: AMT) "American Tower" (l.27-29),
  "ATC" (contact label l.13); CoreSite Realty Corporation (NYSE: COR) "CoreSite" (l.29);
  Appleseed Merger Sub LLC and Appleseed Holdco LLC (l.97, tender filers); people: Tom
  Bartlett, American Tower CEO (l.39-41); Paul Szurek, CoreSite CEO (l.43-45). Advisers
  (l.49): J.P. Morgan (committed financing; lead financial advisor to American Tower); CDX
  Advisors (also advising American Tower); Cleary Gottlieb Steen & Hamilton LLP (principal legal
  advisor to American Tower); Evercore (sole financial advisor to CoreSite); Wachtell, Lipton,
  Rosen & Katz (CoreSite's principal legal advisor). SEC, Schedule TO, Schedule 14D-9 (l.91, 97).
- Key terms and figures: "$170.00 per share in cash" (l.29); total consideration "including the
  assumption and/or repayment of CoreSite's existing debt at closing, is approximately $10.1
  billion" (l.31); "unanimously approved by the boards of directors of both companies" (l.31).
  CoreSite "as of Q3 2021 consisted of 25 data centers, 21 cloud on-ramps and over 32,000
  interconnections in eight major U.S. markets", "annualized revenue and Adjusted EBITDA of $655
  million and $343 million, respectively, in Q3 2021"; "averaged double-digit annual revenue
  growth over the past five years" (l.33). About CoreSite (l.83): "eight key North American
  markets", "More than 1,370" customers, "480+ dedicated employees". About American Tower (l.77):
  "approximately 219,000 communications sites" (compare D02-D07 boilerplate below).
- Structure: tender offer by a wholly owned subsidiary for all CoreSite common shares, then a
  merger for untendered shares at the same price; tender subject to at least a majority of
  outstanding shares and customary conditions (l.47). CoreSite plans to declare and pay its Q4
  dividend during Q4 2021 "and no later than the close of the transaction" (l.47). Financing
  "consistent with maintaining its investment grade credit rating"; committed financing from
  J.P. Morgan (l.49). Tender "has not yet commenced" (l.97).
- Forecasts / expected timing: "expected to close by the end of 2021, or shortly thereafter";
  "anticipated to be modestly accretive to American Tower's AFFO per Share initially, and
  increasingly accretive over time" (l.47). Conference call "today at 8:00 a.m. ET"; replay
  until "11:59 p.m. ET on November 29, 2021"; passcodes 8072944 / 6561145 (l.51-73).
- Hedged claims: "is expected to create a differentiated ... platform" (l.31); "expected to be
  transformative for American Tower's mobile edge compute business" (l.35); "expects to leverage
  its strong financial position ... while also evaluating the potential for international
  expansion in the data center space" (l.33); CEO quotes use "expect", "anticipate" (l.41, 45).
  Forward-looking word list and risks (l.89-93).
- Tables: none. Lists: advisers (5 firms, l.49); forward-looking verbs (l.91).
- Operative definitions / amendments: none. Contradictions: "eight major U.S. markets" (l.33) vs
  "eight key North American markets" (l.83) - wording difference only, stated as is.
- Coverage: FULL - lines 1-109 read.

## D02 - "AMERICAN TOWER CORPORATION REPORTS FIRST QUARTER 2025 FINANCIAL RESULTS"

- Source: `docs/amt_ex991_2025-04-29.txt` | text, 824 lines; file "pressreleaseq12025.htm" (l.5);
  release page numbers 1-17 appear as bare lines (e.g. "1" l.97, "17" l.823).
- Written by: American Tower Corporation; dateline "Boston, Massachusetts - April 29, 2025"
  (l.45). Contact Adam Smith, "Senior Vice President, Investor Relations and FP&A" (l.15). CEO
  quote: Steven Vondran (l.47-49).
- Type, date, edition: Q1 2025 earnings release, 2025-04-29; outlook "as of April 29, 2025".
- Period covered: "quarter ended March 31, 2025", comparatives vs "quarter ended March 31, 2024"
  (l.53). Calendar quarters; balance sheet columns March 31, 2025 / December 31, 2024 (l.443).
  All statement columns are "Three Months Ended March 31" (l.469, 535, 707, 727, 783).
- Headlines (l.19-45): total revenue +2.0% to $2,563M; total property revenue +0.2% to $2,488M;
  net income -45.9% to $499M "primarily due to foreign currency gains and (losses)"; Adjusted
  EBITDA +1.9% to $1,744M; NI attributable -46.7% to $489M; AFFO attributable -1.0% to $1,290M;
  AFFO attributable, as adjusted +7.1% to $1,290M.
- CEO prose (l.47): "highest quarter of services revenue since 2021"; "Attributable AFFO per
  Share growth, on an as adjusted basis, of 6.6%"; "resuming mid-single digit dividend per share
  growth".
- Operating results table (l.55-93; $M except per share; Q1 2025 value, growth): total revenue
  2,563 2.0%; total property revenue 2,488 0.2%; Total Tenant Billings Growth $97 5.2%; Organic
  TBG $87 4.7%; Property Gross Margin 1,889 0.6%; Property Gross Margin % 75.9%; net income 499
  (45.9)%; NI attributable 489 (46.7)%; per diluted share 1.04 (46.9)%; Adjusted EBITDA 1,744 1.9%;
  Adj. EBITDA Margin 68.1%; Nareit FFO attributable 816 (39.3)%; AFFO attributable 1,290 (1.0)%;
  AFFO/Share 2.75 (1.4)%; AFFO as adjusted 1,290 7.1%; AFFO/Share as adjusted 2.75 6.6%; cash
  from operations 1,295 0.9%; cash capex 340 (15.4)%; Free Cash Flow 955 8.3%.
- Headline footnotes (l.99-113): (1) ATC TIPL sale completed "September 12, 2024" to "Data
  Infrastructure Trust, an Infrastructure Investment Trust sponsored by an affiliate of Brookfield
  Asset Management" ("ATC TIPL Transaction"); discontinued operations; results formerly "within
  the Asia-Pacific property segment" (l.99). (2) which metrics exclude vs include discontinued
  operations (l.101). (3) straight-line revenue $17.1M vs $79.1M. (4) FX losses ~$(345.7)M vs
  gains ~$127.7M. (5) gain on sale of South Africa Fiber $53.6M, completed March 6, 2025.
  (6) straight-line revenue net of straight-line expense $8.0M vs $68.4M. (7) "as adjusted" =
  continuing-ops AFFO adjusted for a full period of interest savings from ~$2.0B of ATC TIPL
  proceeds used on the 2021 Multicurrency Credit Facility; ~$120M India Term Loan repayment
  needs no adjustment (India Term Loan "as amended in January 2024"). (8) capex includes $8.9M
  finance lease and perpetual land easement payments.
- Capital allocation (l.117-141): distribution $1.70/share, aggregate $795.8M, YoY per-share
  growth 4.9% (declared March 6, 2025, paid April 28, 2025, record April 11, 2025; l.133). Capex
  ~$340M, of which $38M non-discretionary capital improvements and corporate (l.135).
  Acquisitions ~$148M for 242 sites (145 U.S., 97 Europe) (l.137). April 1, 2025: acquired
  multi-tenant data center in Denver, Colorado, previously leased ("DE1") (l.139). March 6, 2025:
  through ATC South Africa Wireless Infrastructure Proprietary Limited sold "South Africa Fiber"
  for 2.5 billion South African Rand (~$137.7M at closing), gain ~$53.6M in Other operating
  income; formerly in "the Africa & APAC property segment" (l.141).
- Leverage (l.145-161): Net Leverage Ratio 5.0x; total debt $36,862M; cash $2,104M; net debt
  $34,759M; Q1 annualized Adjusted EBITDA $6,977M ("Q1 2025 Adjusted EBITDA multiplied by four").
- Liquidity/financing (l.163-169): ~$11.7B liquidity (~$2.1B cash + ~$9.6B revolver capacity).
  Jan 14, 2025 repaid $650.0M 2.950% notes due 2025; Mar 14, 2025 repaid $750.0M 2.400% notes
  due 2025 ("2.400% Notes"). Jan 28, 2025 amended the $6.0B "2021 Multicurrency Credit
  Facility", $4.0B "2021 Credit Facility" and $1.0B term loan ("Loans") to extend maturities and
  update Applicable Margins. Mar 14, 2025 issued $650.0M 4.900% notes due 2030 and $350.0M
  5.350% notes due 2035; proceeds to repay the 2.400% Notes, the 2021 Multicurrency Credit
  Facility and general purposes.
- Outlook FY2025 (l.171-341): FX rates for April 29-December 31, 2025, 17 currencies (a)-(q)
  (l.175). FX vs prior outlook: +~$50M property revenue, +$30M Adj. EBITDA, +$20M AFFO, +$0.04/
  share (l.177); midpoints raised by those amounts; net income and NI attributable midpoints
  reduced by $185M and $180M "primarily due to unrealized foreign currency losses" (l.181). 2024
  base on continuing-ops basis except NI, NI attributable, AFFO and AFFO/Share (l.179).
  Table (l.187-199; range, midpoint growth, as-adjusted growth): total property revenue
  $9,970-$10,120, 1.1%, N/A; net income 2,740-2,840, 22.4%; NI attributable 2,775-2,875, 25.3%;
  Adjusted EBITDA 6,885-6,955, 1.6%; AFFO attributable 4,850-4,940, (0.8)%, 5.0%; AFFO/Share
  $10.35-$10.54, (0.9)%, 4.8%. Footnote (1) (l.201): U.S. & Canada property $5,190-$5,250M,
  international $3,755-$3,825M, Data Centers $1,025-$1,045M; midpoint growth (0.5)%, 0.8%, 11.9%;
  U.S. & Canada includes ~4% negative straight-line impact; international "nearly 5%" negative
  FX. (2) ~2% straight-line drag on property revenue; (3) ~3% on Adj. EBITDA.
  Components (l.207-217): international pass-through $1,034M; straight-line 28/23/10, total 61.
  TBG outlook (l.229-235; U.S.&C / Intl / Total): organic >=4.3% / ~6% / ~5%; new site ~0% / ~1%
  / ~0.5%; total >=4.3% / ~7% / ~5.5%. Capex (l.243-263): discretionary $880-$910 (1,950-2,550
  sites; $610M Data Centers development), ground lease 190-210, start-up 50-70, redevelopment
  360-390, capital improvement 145-155, corporate 10; total $1,635-$1,745. Reconciliations
  (l.267-341): interest expense 1,370-1,350; D&A 2,000-2,010; tax 375-365; SBC 170; other
  230-220; diluted shares 468,700 thousand; cash interest (1,320)-(1,300); interest income 105;
  cash taxes (270)-(260); NCI adjustments (373).
- Conference call (l.345-355): 8:30 a.m. ET; text says "quarter and full year ended March 31,
  2025" (l.347, as printed).
- About American Tower (l.359): "over 149,000 communications sites and a highly interconnected
  footprint of U.S. data center facilities".
- Defined measures (l.361-429): list of non-GAAP measures (l.363; Segment Gross Margin, Segment
  Operating Profit, Segment Operating Profit Margin, Adjusted EBITDA, Adj. EBITDA Margin, Nareit
  FFO, AFFO, AFFO as adjusted, AFFO/Share, AFFO/Share as adjusted, Free Cash Flow, Net Debt, Net
  Leverage Ratio; plus Tenant Billings, TBG, Organic TBG, New Site TBG). "Property Gross Margin"
  (headline table l.65) is not in that list. Revenue components, 8 items (i)-(viii) (l.371);
  definitions: Tenant Billings 4 aspects (l.373), New Site (l.375), Organic (l.377), pass-through
  (l.379), straight-line (l.383), pre-paid amortization (l.385), FX (l.387), Other revenue
  "customer settlements, fiber solutions revenue and data centers revenue" (l.389). Adjusted
  EBITDA (l.393), Margin (l.395), AFFO (l.397, mentions "minority interests in its Europe business
  and its U.S. data center business"), as adjusted (l.399), per Share (l.401-403), Free Cash Flow
  (l.405), Nareit FFO (l.407-411), Net Debt (l.413), Net Leverage Ratio (l.415), New Site TBG
  (l.417), Organic TBG (l.419), Segment Gross Margin (l.421), Segment Operating Profit (l.423-425),
  SOP Margin (l.427), TBG "adjusted for foreign currency exchange rate fluctuations" (l.429).
- Risk factors: 21 numbered items (1)-(21) in one paragraph (l.435).
- Statement of operations visible rows (l.465-527; $M, Q1 2025 / Q1 2024): interest income
  26.9/31.0; interest expense (325.3)/(363.8); other (expense) income (338.2)/113.1 incl. FX
  (345.7)/127.7; NI from continuing ops 498.6/830.0; discontinued —/91.7; NI 498.6/921.7; NCI
  (9.9)/(4.3); NI attributable 488.7/917.4; diluted EPS 1.04/1.96 (continuing 1.04/1.77); basic
  1.05/1.97; shares basic 467,640/466,519, diluted 468,519/467,660 (thousands); SBC in SG&A
  $53.4M/$62.8M.
- Cash flow visible rows (l.531-573): NI 498.6/921.7; repayments (1,840.7)/(3,568.4); FX on cash
  29.9/(34.0); cash taxes 32.9/66.5; cash interest 370.1/442.3; finance lease payments
  $0.7M/$1.1M; perpetual land easement $8.2M/$8.6M; Q1 2024 Singapore withholding tax $11.8M "as a
  result of the ATC TIPL Transaction".
- Segment tables: Q1 2025 (l.577-633) and Q1 2024 (l.637-697); 9 columns U.S. & Canada | Latin
  America | Africa & APAC | Europe | Total International | Data Centers | Total Property |
  Services | Total. Q1 2025: SOP Margin 81/64/64/57/62/50/71/45/70%; Revenue Growth
  (0.9)/(10.4)/12.3/4.2/(0.1)/8.7/0.2/147.0/2.0%; Total TBG 3.7/3.1/16.6/7.1/8.1/N/A/5.2%;
  Organic TBG 3.6/3.0/13.2/5.4/6.7/N/A/4.7%; Prior-Year TB 1,212/312/201/139/652/—/1,864;
  Organic TB 1,255/322/227/147/696/—/1,951; New Site TB 1/0/7/2/9/—/10; Total TB
  1,256/322/234/149/705/—/1,961; FX (0)/(42)/(6)/(5)/(53)/—/(53); Total TB (Current Period)
  1,256/280/228/144/652/—/1,908. Q1 2024: SOP Margin 82/62/63/56/61/51/71/38/71%; Revenue Growth
  1.8/(4.0)/(7.5)/6.7/(3.1)/10.6/0.6/(42.7)/(0.3)%; Total TBG 4.5/2.9/21.9/6.8/9.9/N/A/6.4%;
  Organic TBG 4.6/2.8/14.5/5.5/7.2/N/A/5.5%; Prior-Year TB 1,159/285/201/129/615/—/1,775; Organic
  TB 1,213/293/230/136/659/—/1,872; New Site (1)/0/15/2/17/—/16; Total TB 1,212/294/245/138/676/—/
  1,888; FX 0/19/(44)/2/(24)/—/(24); Current Period 1,212/312/201/139/652/—/1,864. Footnotes:
  Total International "excluding Canada"; Africa & APAC (Q1 2024) "Excludes the operating results
  of ATC TIPL"; components at prior-period FX.
- Selected info (l.701-793): Adj. EBITDA 1,744.2/1,712.2; total revenue 2,562.8/2,512.6; margin
  68%/68% (l.713-717; footnote: all lines except NI and discontinued income exclude discontinued
  ops). Nareit/AFFO (l.725-779): NI 498.6/921.7; real-estate D&A 457.3/470.0; (gain) losses on
  real estate (49.1)/2.9; deferred financing amortization 13.8/13.0; "As Adjusted": AFFO from
  discontinued —/131.3; AFFO from continuing 1,290.2/1,171.8; interest-savings adjustment —/32.9;
  AFFO as adjusted 1,290.2/1,204.8; per Share as adjusted 2.75/2.58. Footnotes: (2) no material
  impairments; South Africa Fiber gain $53.6M; (3) distributions on "mandatorily convertible
  preferred equity" with "investment vehicles affiliated with Stonepeak Partners LP"; (4) Q1 2024
  discontinued RE D&A $38.9M, gains $1.6M; (5) Singapore WHT $11.8M "nonrecurring"; (6) FX
  $345.7M / ($127.7)M; (7) acquisition, integration and disposition costs. EBITDA-to-AFFO
  (l.781-793): AFFO per Share 2.75/2.79; as adjusted 1,290.2/1,204.8 and 2.75/2.58.
- Capture gaps (23; line, chars, location):
  1. l.449 (516) balance sheet: all asset rows after "CURRENT ASSETS:" (l.447), before "LIABILITIES".
  2. l.455 (576) all liability rows after "CURRENT LIABILITIES:", before "COMMITMENTS AND CONTINGENCIES".
  3. l.461 (380) all equity rows/totals after "EQUITY:". Balance sheet has no visible figures.
  4. l.473 (92) statement of operations revenue rows after "REVENUES:" (l.471).
  5. l.479 (282) cost/expense rows, D&A, SG&A (footnote 1 marker), operating income, after "Costs of operations..." (l.477), before "OTHER INCOME (EXPENSE):".
  6. l.489 (143) rows between "Other (expense) income..." (l.487) and "NET INCOME FROM CONTINUING OPERATIONS" (l.491) (pre-tax income/tax rows not visible).
  7. l.545 (461) cash-flow operating adjustments and operating total, before "CASH FLOWS FROM INVESTING ACTIVITIES:".
  8. l.549 (328) all investing rows.
  9. l.553 (206) financing rows before "Repayments of notes payable..." (l.555).
  10. l.557 (346) financing rows after repayments (incl. the footnote-2 easement row), before FX on cash (l.559).
  11. l.561 (244) net change / beginning / end cash rows, before "CASH PAID FOR INCOME TAXES" (l.563).
  12. l.591 (348) Q1 2025 segment table: revenue, opex, gross margin, SG&A(3), Segment Operating Profit rows before "Segment Operating Profit Margin" (l.593).
  13. l.607 (148) Q1 2025 Tenant Billings bridge rows between "Prior-Year Tenant Billings" (l.605) and "Organic Tenant Billings" (l.609).
  14. l.619 (335) Q1 2025 rows after "Total Tenant Billings (Current Period)" (l.617): remaining revenue components incl. the footnote-(6) FX row and property revenue total.
  15. l.653 (349) Q1 2024 segment table rows before SOP Margin (l.655).
  16. l.669 (149) Q1 2024 Tenant Billings bridge rows (l.667-671).
  17. l.681 (333) Q1 2024 rows after Current Period TB (l.679).
  18. l.711 (357) Adjusted EBITDA reconciliation: every reconciling row; only Adj. EBITDA, total revenue, margin visible (l.713-717).
  19. l.737 (494) Nareit/AFFO table rows between real-estate gains (l.735) and deferred financing amortization (l.739) - Nareit FFO total row not visible here.
  20. l.741 (558) rows after deferred financing amortization to "As Adjusted:" (l.743) - total AFFO attributable, share count and AFFO/Share rows not visible here.
  21. l.787 (568) EBITDA-to-AFFO reconciliation: all rows before "AFFO Attributable to Common Stockholders per Share" (l.789).
  22. l.801 (297) Q1 2025 segment gross margin reconciliation: all rows (header l.797-799).
  23. l.815 (298) Q1 2024 segment gross margin reconciliation: all rows (header l.807-813).
- Hedged claims: outlook "based on a number of assumptions" (l.173); FX net-income impact "not
  provided ... without unreasonable effort" (l.177); headline NI decline "primarily due to"
  FX (l.33, 41); NI midpoint cut "primarily due to unrealized foreign currency losses" (l.181).
- Rounded prose beside exact figures: headline $M rounded (l.25-45) vs statements in $0.1M
  (e.g. revenue 2,562.8 l.715; NI 498.6 l.495); CEO "6.6%" equals table l.87.
- Coverage: FULL - lines 1-824 read; 23 capture gaps listed above remain unresolvable.

## D03 - "AMERICAN TOWER CORPORATION REPORTS SECOND QUARTER 2025 FINANCIAL RESULTS"

- Source: `docs/amt_ex991_2025-07-29.txt` | text, 818 lines; file "pressreleaseq22025.htm" (l.5).
- Written by: American Tower Corporation; dateline "Boston, Massachusetts - July 29, 2025" (l.47).
  Contact changed: "Kate Reeb, Senior Director, Investor Relations", (617) 375-7565 (l.13-17).
  CEO Steven Vondran quote (l.49-51).
- Type, date, edition: Q2 2025 earnings release; outlook "as of July 29, 2025" (l.173).
- Period: "quarter ended June 30, 2025" vs "quarter ended June 30, 2024" (l.55). Statement of
  operations has Three Months and Six Months Ended June 30, 2025/2024 columns (l.469); cash flow
  is Six Months only (l.531); segment and reconciliation tables are three months (l.577, 637, 703,
  723, 777); balance sheet June 30, 2025 / December 31, 2024 (l.443).
- Headlines (l.21-47): total revenue +3.2% to $2,627M; property revenue +1.2% to $2,527M; NI
  -58.1% to $381M "primarily due to foreign currency losses in the current period"; Adj. EBITDA
  +1.8% to $1,752M; NI attributable -59.3% to $367M; AFFO attributable -6.7% to $1,218M; as
  adjusted +2.6% to $1,218M.
- CEO prose (l.49): "one of the highest quarters of U.S. Services revenue contributions on
  record"; "AI-ready interconnection solutions fueled double-digit growth at CoreSite"; "continue
  to manage through certain customer events, particularly in Latin America".
- Operating results table (l.57-95; Q2 2025, growth): revenue 2,627 3.2%; property revenue 2,527
  1.2%; Total TBG $97 5.2%; Organic TBG $87 4.7% (same $97/5.2% and $87/4.7% as D02 Q1 2025
  l.61-63; the D03 segment table l.595-597 also shows 5.2%/4.7%); Property Gross Margin 1,887
  0.9%; PGM% 74.7%; NI 381 (58.1)%; NI attributable 367 (59.3)%; diluted EPS 0.78 (59.4)%; Adj.
  EBITDA 1,752 1.8%; margin 66.7%; Nareit FFO 765 (43.4)%; AFFO 1,218 (6.7)%; AFFO/Share 2.60
  (6.8)%; AFFO as adjusted 1,218 2.6%; AFFO/Share as adjusted 2.60 2.4%; cash from operations
  1,282 (4.3)%; cash capex 313 (4.6)%; FCF 969 (4.1)%.
- Headline footnotes (l.99-115): (1) ATC TIPL text as D02 but alias "ATC India" dropped (only
  "ATC TIPL"), still "Asia-Pacific property segment"; (3) straight-line revenue ~$28.2M vs
  ~$74.1M; (4) FX losses ~$(484.0)M vs losses ~$(21.7)M; (5) straight-line net ~$18.8M vs
  ~$63.3M; (6) as-adjusted text as D02; (7) capex includes $8.3M finance lease/easement payments.
- Capital allocation (l.119-139): distribution $1.70, aggregate $796.0M, growth 4.9% (declared May
  15, 2025, paid July 11, 2025, record June 13, 2025; l.135). Capex ~$313M, $40M non-discretionary
  (l.137). Acquisitions ~$185M "primarily driven by" the DE1 Denver data center acquisition
  (l.139; no completion date given here - D02 l.139 gives April 1, 2025).
- Leverage (l.143-159): 5.1x; total debt $37,485M; cash $2,076M; net debt $35,409M; Q2 annualized
  Adj. EBITDA $7,007M.
- Liquidity/financing (l.161-169): ~$10.5B (~$2.1B cash + ~$8.4B revolvers). April 3, 2025 repaid
  EUR 500.0M 1.375% notes due April 4, 2025; May 30, 2025 repaid $750.0M 4.000% notes due June 1,
  2025; May 30, 2025 issued EUR 500.0M (~$567.4M) 3.625% notes due 2032 (proceeds to 2021
  Multicurrency Credit Facility and general purposes); June 16, 2025 repaid $525.0M Secured Tower
  Revenue Notes, Series 2015-2, Class A ("2015 Securitization"), after which "no notes were
  outstanding under the 2015 Securitization".
- Outlook FY2025 (l.171-341): FX rates for July 29-December 31, 2025, 17 currencies (l.175). FX vs
  prior outlook +~$130M property revenue, $80M Adj. EBITDA, $55M AFFO, $0.12/share (l.177).
  Midpoints raised by $165M, $120M, $55M, $0.12 "As a result of the estimated positive foreign
  currency exchange rate fluctuations described above, and core outperformance as it relates to
  property revenue and Adjusted EBITDA"; NI and NI attributable midpoints cut by $400M and $475M
  "primarily due to unrealized foreign currency losses" (l.181). Table (l.187-199): property
  revenue $10,135-$10,285, 2.8%; NI 2,340-2,440, 4.8%; NI attributable 2,300-2,400, 4.2%; Adj.
  EBITDA 7,005-7,075, 3.3%; AFFO 4,905-4,995, 0.3%, as adjusted 6.2%; AFFO/Share $10.46-$10.65,
  0.2%, 6.0%. Footnote (1) (l.201): U.S. & Canada $5,200-$5,260M, international $3,900-$3,970M,
  Data Centers $1,035-$1,055M; midpoint growth (0.3)%, 4.6%, 13.0%; U.S. & Canada ~3% straight-line
  drag; international ~1% FX drag. (2) ~2%, (3) ~3% straight-line. Components (l.215-217):
  pass-through $1,061M; straight-line 48/32/7, total 87. TBG outlook (l.231-235): organic ~4.3% /
  >6% / ~5%; new site ~0% / ~1% / ~0.5%; total ~4.3% / >7% / ~5.5%. Capex (l.243-263):
  discretionary $865-$895 (1,850-2,450 sites; $600M Data Centers), ground lease 200-220, start-up
  65-85, redevelopment 320-350, capital improvement 155-165, corporate 10; total $1,615-$1,725.
  Reconciliations (l.267-341): interest 1,385-1,365; D&A 2,040-2,050; tax 435-425; SBC 170; other
  635-625; straight-line revenue (87), expense 36; deferred tax 156; other 804-794; NCI (389);
  diluted shares 468,900 thousand; cash interest (1,326)-(1,306); interest income 110; cash taxes
  (279)-(269).
- Conference call 8:30 a.m. ET, "quarter ended June 30, 2025" (l.347). About (l.359): "nearly
  150,000 communications sites".
- Definitions (l.361-429): same list and texts as D02; Nareit FFO wording differs slightly
  ("accretion, and including adjustments" l.409 vs D02 "accretion including adjustments" l.407).
  Risk factors 21 items, same text (l.435).
- Statement of operations (l.465-523; 3M 2025 / 3M 2024 / 6M 2025 / 6M 2024): interest income
  30.6/34.4/57.5/65.4; interest expense (342.6)/(362.7)/(667.9)/(726.5); other (expense) income
  (373.9)/19.4/(712.1)/132.5 "including unrealized foreign currency (losses) gains of $(484.0),
  $(21.7), $(829.7) and $106.0" (l.487; "unrealized" not in D02's label); NI continuing
  380.5/769.9/879.1/1,599.9; discontinued —/138.5/—/230.2; NI 380.5/908.4/879.1/1,830.1; NCI
  (13.7)/(8.1)/(23.6)/(12.4); NI attributable 366.8/900.3/855.5/1,817.7; continuing attributable
  366.8/761.8/855.5/1,587.5; basic EPS 0.78/1.93/1.83/3.89; diluted 0.78/1.92/1.83/3.89 (diluted
  continuing 0.78/1.63/1.83/3.39); shares basic 468,178/467,038/467,909/466,778, diluted
  468,791/467,781/468,717/467,793; SBC $47.3M (Q2'25), $100.7M (6M'25), $44.3M (Q2'24), $107.1M
  (6M'24).
- Cash flow (six months, l.527-569): NI 879.1/1,830.1; repayments (5,318.2)/(7,189.7); FX on cash
  116.6/(153.5); cash taxes 131.4/179.2; cash interest 684.2/803.1; finance lease $1.7M/$2.2M;
  easements $15.5M/$16.2M; footnote (3): 6M 2025 "taxes paid in South Africa of $19.6 million"
  from the South Africa Fiber sale; 6M 2024 Singapore withholding taxes $33.5M (ATC TIPL).
- Segment tables (same 9 columns as D02). Q2 2025 (l.573-629): SOP Margin 80/61/63/57/61/53/70/45/
  69%; Revenue Growth (0.6)/(13.2)/12.4/14.5/0.8/13.5/1.2/109.9/3.2%; Total TBG 3.8/3.0/15.8/7.1/
  7.9/N/A/5.2%; Organic TBG 3.7/2.9/13.0/5.1/6.5/N/A/4.7%; Prior-Year TB 1,215/305/204/140/649/—/
  1,864; Organic TB 1,260/314/231/147/691/—/1,951; New Site 2/0/6/3/9/—/10; Total TB 1,261/314/
  236/149/700/—/1,961; FX (0)/(26)/6/7/(13)/—/(13); Current Period 1,261/288/242/157/687/—/1,948.
  (The Total Property Prior-Year 1,864 / Organic 1,951 / Total 1,961 coincide with D02's Q1 2025
  totals although segment values differ.) Q2 2024 (l.633-693): SOP Margin 80/65/61/56/62/49/70/44/
  70%; Revenue Growth 0.9/2.1/(8.2)/2.5/(1.3)/12.6/1.0/10.0/1.2%; Total TBG 5.0/2.4/19.9/7.2/9.0/
  N/A/6.4%; Organic TBG 5.1/2.2/13.1/5.7/6.4/N/A/5.6%; Prior-Year TB 1,157/299/205/131/636/—/1,793;
  Organic 1,216/306/232/139/677/—/1,893; New Site (1)/1/14/2/17/—/16; Total 1,215/306/246/141/693/
  —/1,909; FX (0)/(1)/(42)/(1)/(45)/—/(45); Current Period 1,215/305/204/140/649/—/1,864.
- Selected info (l.697-787): Adj. EBITDA 1,751.8/1,721.4; total revenue 2,626.9/2,544.7; margin
  67%/68% (l.709-713). Nareit/AFFO: NI 380.5/908.4; RE D&A 475.4/482.6; "Losses from sale or
  disposal of real estate..." 9.1/10.4 (label lacks D02's "(Gain)"); deferred financing 13.7/13.3;
  AFFO discontinued —/150.8; AFFO continuing 1,218.3/1,155.0; interest savings —/32.9; AFFO as
  adjusted 1,218.3/1,188.0; per Share as adjusted 2.60/2.54. Footnotes: (2) no material
  impairments; (3) Stonepeak Partners LP preferred equity; (4) Q2 2024 discontinued RE D&A $39.3M,
  gains $1.4M; (5) Q2 2025 South Africa taxes $19.6M; Q2 2024 Singapore WHT $21.7M; "these
  withholding tax payments are nonrecurring"; (6) FX losses $484.0M and $21.7M (note Q2 2024 FX
  loss and Q2 2024 Singapore WHT are both $21.7M). EBITDA-to-AFFO (l.775-787): AFFO/Share
  2.60/2.79; as adjusted 1,218.3/1,188.0, 2.60/2.54.
- Capture gaps (23): l.449 (516) BS assets; l.455 (576) BS liabilities; l.461 (381) BS equity -
  balance sheet has no visible figures; l.473 (139) SoO revenue rows (4 columns); l.479 (388)
  opex through operating income; l.489 (193) rows between "Other (expense) income" (l.487) and NI
  from continuing ops (l.491); l.541 (470) CF operating adjustments/total; l.545 (329) investing;
  l.549 (210) financing rows before repayments (l.551); l.553 (390) financing rows after
  repayments; l.557 (244) cash roll-forward before cash taxes (l.559); l.587 (351) Q2 2025 segment
  revenue/opex/gross margin/SG&A/SOP rows; l.603 (148) Q2 2025 TB bridge rows (l.601-605); l.615
  (332) Q2 2025 rows after Current Period TB; l.649 (349) Q2 2024 segment rows; l.665 (150) Q2 2024
  TB bridge; l.677 (338) Q2 2024 rows after Current Period TB; l.707 (364) Adj. EBITDA
  reconciling rows; l.733 (494) Nareit rows incl. Nareit FFO total; l.737 (558) AFFO total/shares/
  per-Share rows; l.781 (568) EBITDA-to-AFFO rows before AFFO/Share (l.783); l.795 (295) Q2 2025
  segment gross margin reconciliation; l.809 (298) Q2 2024 segment gross margin reconciliation.
- Coverage: FULL - lines 1-818 read; 23 gaps unresolvable.

## D04 - "AMERICAN TOWER CORPORATION REPORTS THIRD QUARTER 2025 FINANCIAL RESULTS"

- Source: `docs/amt_ex991_2025-10-28.txt` | text, 820 lines; file "pressreleaseq32025.htm" (l.5).
- Written by: American Tower Corporation; dateline "Boston, Massachusetts - October 28, 2025"
  (l.51). Contact changed: "Spencer Kurn, Senior Vice President, Investor Relations", (617)
  375-7517 (l.13-17). CEO Steven Vondran quote (l.53-55).
- Type, date, edition: Q3 2025 earnings release; outlook "as of October 28, 2025" (l.175).
- Period: "quarter ended September 30, 2025" vs "quarter ended September 30, 2024" (l.59). SoO has
  Three and Nine Months Ended September 30 columns (l.471); cash flow Nine Months (l.529); segment
  and reconciliation tables three months; balance sheet September 30, 2025 / December 31, 2024.
- Headlines (l.21-51): revenue +7.7% to $2,717M; property revenue +5.9% to $2,616M; NI +216.9% to
  $913M "primarily due to foreign currency losses in the prior year period"; Adj. EBITDA +7.6% to
  $1,816M; NI attributable +207.7% to $853M (same reason); AFFO attributable +5.3% to $1,303M; as
  adjusted +10.4% to $1,303M.
- CEO prose (l.53): "mid-to-high single-digit growth in revenue and Adjusted EBITDA, and
  double-digit growth in AFFO per Share, as adjusted"; data centers: "strong hybrid-cloud demand,
  favorable pricing, and rising AI-related workloads drove a strong quarter, including a record
  quarter of signed retail new leasing".
- Operating results table (l.61-99): revenue 2,717 7.7%; property revenue 2,616 5.9%; Total TBG
  $102 5.5%; Organic TBG $92 5.0%; Property Gross Margin 1,959 6.3%; PGM% 74.9%; NI 913 216.9%;
  NI attributable 853 207.7%; diluted EPS 1.82 207.7% (same % as NI attributable, as printed);
  Adj. EBITDA 1,816 7.6%; margin 66.8%; Nareit FFO 1,262 47.2%; AFFO 1,303 5.3%; AFFO/Share 2.78
  5.3%; AFFO as adjusted 1,303 10.4%; AFFO/Share as adjusted 2.78 10.3%; cash from operations
  1,460 (0.6)%; cash capex 476 10.0%; FCF 984 (5.1)%.
- Headline footnotes (l.103-121): (1) ATC TIPL as D03; (3) straight-line ~$27.7M vs ~$68.5M;
  (4) FX gains ~$18.0M vs losses ~$(337.4)M; (5) straight-line net ~$18.3M vs ~$51.2M; (6) NEW:
  prior-year "loss on the sale of ATC TIPL of $1.2 billion ... primarily included the
  reclassification of the Company's cumulative translation adjustment in India upon exiting the
  market of $1.1 billion", included in Loss from discontinued operations (l.117); (7) as adjusted,
  now naming "the Company's $6.0 billion senior unsecured multicurrency revolving credit
  facility" instead of the defined term (l.119); (8) capex includes $10.4M finance lease/easement.
- Capital allocation (l.125-143): distribution $1.70, aggregate $796.1M, growth 4.9% (declared
  September 18, 2025, paid October 20, 2025, record September 30, 2025; l.141). Capex ~$476M,
  $54M non-discretionary (l.143). No "Acquisitions" or "Other Events" paragraph in this edition.
- Leverage (l.147-163): 4.9x; total debt $37,239M; cash $1,951M; net debt $35,288M; Q3
  annualized Adj. EBITDA $7,262M.
- Liquidity/financing/buybacks (l.165-171): ~$10.7B (~$2.0B cash + ~$8.7B revolvers). Sept 12,
  2025 repaid $500.0M 1.300% notes due September 15, 2025. Sept 16, 2025 issued $575.0M senior
  unsecured notes (no coupon/maturity stated in this capture); proceeds to repay the $4.0B senior
  unsecured revolving credit facility and general purposes. "During the third quarter of 2025,
  there were no repurchases under either of the Company's buyback programs. Subsequent to
  September 30, 2025, through October 21, 2025, the Company repurchased approximately 151,000
  shares ... for an aggregate of approximately $28.0 million, including commissions and fees.
  There are no amounts remaining under the Company's 2011 buyback program." Expects to manage
  pacing of "the remaining approximately $2.0 billion under the Company's 2017 buyback program"
  (l.171).
- Outlook FY2025 (l.173-343): FX rates October 28-December 31, 2025, 17 currencies (l.177). FX vs
  prior outlook +~$50M property revenue, $30M Adj. EBITDA, $20M AFFO, $0.04/share (l.179; same
  four values as D02 l.177). Midpoints raised by $40M, $45M, $50M, $0.10 "primarily as a result
  of estimated positive foreign currency exchange rate fluctuations"; NI and NI attributable
  midpoints INCREASED by $95M and $40M "primarily due to unrealized foreign currency gains"; the
  NI attributable increase "is partially offset by increased minority interests as a result of a
  recent tax law change in Europe" (l.183). Table (l.189-201): property revenue $10,210-$10,290,
  3.2%; NI 2,458-2,513, 9.0%; NI attributable 2,363-2,418, 6.0%; Adj. EBITDA 7,058-7,113, 4.0%;
  AFFO 4,973-5,028, 1.3%, as adjusted 7.3%; AFFO/Share $10.60-$10.72, 1.1%, 7.0%. Footnote (1)
  (l.203): U.S. & Canada $5,230-$5,240M, international $3,940-$4,000M, Data Centers $1,040-$1,050M;
  midpoint growth (0.2)%, 5.6%, 13.0%; U.S. & Canada "over 3%" straight-line drag; no FX sentence
  for international in this edition. (2) ~2% straight-line; (3) ~3% "net straight-line" (wording
  change). Components (l.217-219): pass-through $1,080M; straight-line 48/32/7, total 87. TBG
  outlook (l.233-237): identical to D03. Capex (l.245-265): discretionary $865-$895 (1,850-2,450
  sites; $600M Data Centers), ground lease 200-220, start-up 65-85, redevelopment 320-350, capital
  improvement 160-170, corporate 10; total $1,620-$1,730. Reconciliations (l.269-343): interest
  1,370-1,360; D&A 2,035-2,045; tax 425; SBC 175; other 595; deferred tax 149; other 768;
  capital improvement (160)-(170); NCI (391); shares 468,900; cash interest (1,317)-(1,307);
  interest income 120; cash taxes (276).
- Conference call 8:30 a.m. ET (l.349). About (l.361): "over 149,000 communications sites".
- Definitions (l.363-431): same list/texts as D03 (incl. Nareit "accretion, and including"); the
  as-adjusted definition (l.401) and footnote (10) (l.771) still use "2021 Multicurrency Credit
  Facility". Risk factors 21 items, same text (l.437).
- Statement of operations (l.467-521; 3M 2025 / 3M 2024 / 9M 2025 / 9M 2024): interest income
  36.1/37.7/93.6/103.1; interest expense (347.1)/(356.8)/(1,015.0)/(1,083.3); other income
  (expense) 27.7/(269.6)/(684.4)/(137.1) incl. unrealized FX 18.0/(337.4)/(811.7)/(231.4) (l.489).
  NI, NI from continuing ops, discontinued ops and NCI rows are inside gap l.491 (not visible).
  NI (loss) attributable 853.3/(792.3)/1,708.8/1,025.4; continuing attributable 853.3/416.2/
  1,708.8/2,003.7; net loss from discontinued attributable —/(1,208.5)/—/(978.3); basic EPS
  1.82/(1.70)/3.65/2.20 (continuing 1.82/0.89/3.65/4.29; discontinued —/(2.59)/—/(2.10)); diluted
  1.82/(1.69)/3.64/2.19 (continuing 1.82/0.89/3.64/4.28; discontinued —/(2.58)/—/(2.09)); shares
  basic 468,287/467,196/468,036/466,919, diluted 469,039/468,261/468,856/468,001; SBC $41.9M
  (Q3'25), $142.6M (9M'25), $43.7M (Q3'24), $150.8M (9M'24).
- Cash flow (nine months, l.525-569): NI 1,791.7/1,049.7; repayments (7,800.4)/(10,435.8); FX on
  cash 112.5/(130.1); cash taxes 171.8/224.4; cash interest 1,105.2/1,216.7. Footnotes: (1) 9M
  2025 includes $137.7M from the South Africa Fiber sale; 9M 2024 includes $238.0M "from the sale
  of the optionally convertible debentures issued by one of the Company's customers in India,
  Vodafone Idea Limited ("VIL") and associated shares of equity of VIL" (l.563; the row it
  annotates is in cut gap l.543); (2) finance leases $3.5M/$3.9M; (3) easements $24.1M/$24.0M;
  (4) 9M 2025 South Africa taxes $19.6M and Singapore taxes $0.3M; 9M 2024 Singapore WHT $36.4M.
- Segment tables (9 columns as D02). Q3 2025 (l.573-629): SOP Margin 80/61/64/56/61/53/70/41/69%;
  Revenue Growth 0.1/3.4/22.5/14.5/12.3/14.1/5.9/92.9/7.7%; Total TBG 4.1/3.2/16.0/6.9/8.2/N/A/
  5.5%; Organic TBG 3.9/3.2/13.5/4.9/6.9/N/A/5.0%; Prior-Year TB 1,226/287/207/144/638/—/1,863;
  Organic TB 1,274/296/236/151/682/—/1,956; New Site 2/0/5/3/8/—/10; Total TB 1,275/296/241/154/
  690/—/1,966; FX (0)/4/16/10/31/—/31; Current Period 1,275/300/257/164/721/—/1,996. Q3 2024
  (l.633-693): SOP Margin 80/61/63/56/61/48/70/43/69%; Revenue Growth (0.5)/(12.4)/1.4/6.2/(4.2)/
  10.3/(1.0)/100.0/0.0%; Total TBG 4.9/1.9/16.9/7.9/7.7/N/A/5.9%; Organic TBG 5.0/1.7/11.5/6.3/5.7/
  N/A/5.2%; Prior-Year TB 1,169/310/197/132/639/—/1,808; Organic 1,227/315/220/141/676/—/1,902;
  New Site (1)/0/11/2/13/—/12; Total 1,226/315/231/143/689/—/1,914; FX (0)/(29)/(23)/1/(51)/—/
  (51); Current Period 1,226/287/207/144/638/—/1,863.
- Selected info (l.697-789): Adj. EBITDA 1,815.5/1,686.5; total revenue 2,717.4/2,522.3; margin
  67%/67% (l.709-713; footnote now "Net income (loss) and Loss from discontinued operations").
  Nareit/AFFO: NI (loss) 912.6/(780.4); RE D&A 486.0/461.5; losses on real estate 11.4/9.6;
  deferred financing 13.5/13.7; AFFO discontinued —/83.1; AFFO continuing 1,303.1/1,154.3;
  interest savings —/26.4; AFFO as adjusted 1,303.1/1,180.7; per Share as adjusted 2.78/2.52.
  Footnotes: (1) Q3 2024 loss from discontinued ops $1.2B; (4) Q3 2024 discontinued RE D&A $13.1M
  and real-estate losses for discontinued ops $1.2B, "includes a loss on the sale of ATC TIPL of
  $1.2 billion"; (5) "For the three ended September 30, 2025" (sic) Singapore taxes $0.3M; Q3 2024
  Singapore WHT $2.9M; "these tax payments are nonrecurring"; (6) FX (gains) losses $(18.0)M and
  $337.4M. EBITDA-to-AFFO (l.777-789): AFFO/Share 2.78/2.64; as adjusted 1,303.1/1,180.7,
  2.78/2.52.
- Capture gaps (23): l.451 (516) BS assets; l.457 (576) BS liabilities; l.463 (381) BS equity -
  no visible balance-sheet figures; l.475 (141) SoO revenue rows; l.481 (385) opex through
  operating income; l.491 (465) rows between "Other income (expense)" (l.489) and NI attributable
  (l.493) - includes NI, continuing, discontinued and NCI rows; l.539 (502) CF operating
  adjustments; l.543 (400) investing rows (incl. footnote-1 sale-proceeds row); l.547 (210)
  financing rows before repayments (l.549); l.551 (392) financing rows after repayments (incl.
  footnote-3 row); l.555 (255) cash roll-forward; l.587 (353) Q3 2025 segment revenue/opex/GM/SG&A/
  SOP rows; l.603 (146) Q3 2025 TB bridge; l.615 (323) Q3 2025 rows after Current Period TB; l.649
  (350) Q3 2024 segment rows; l.665 (150) Q3 2024 TB bridge; l.677 (336) Q3 2024 rows after Current
  Period TB; l.707 (361) Adj. EBITDA reconciling rows; l.733 (499) Nareit rows incl. Nareit FFO
  total; l.737 (563) AFFO total/shares/per-Share rows; l.783 (568) EBITDA-to-AFFO rows before
  AFFO/Share (l.785); l.797 (295) Q3 2025 segment GM reconciliation; l.811 (297) Q3 2024 segment
  GM reconciliation.
- Coverage: FULL - lines 1-820 read; 23 gaps unresolvable.

## D05 - "AMERICAN TOWER CORPORATION REPORTS FOURTH QUARTER AND FULL YEAR 2025 FINANCIAL RESULTS"

- Source: `docs/amt_ex991_2026-02-24.txt` | text, 920 lines; file "pressreleaseq42025.htm" (l.5).
- Written by: American Tower Corporation; dateline "Boston, Massachusetts - February 24, 2026"
  (l.53). Contact Spencer Kurn, SVP Investor Relations, (617) 375-7517 (l.13-17). CEO Steven
  Vondran quote (l.55-57).
- Type, date, edition: Q4 and full-year 2025 earnings release; first FULL YEAR 2026 outlook "as
  of February 24, 2026" (l.171-173).
- Period: "quarter and full year ended December 31, 2025" vs 2024 (l.61). SoO, Adj. EBITDA,
  Nareit/AFFO and EBITDA-to-AFFO tables have Three Months and Twelve Months Ended December 31
  columns (l.459, 795, 813-815, 867-869); cash flow Twelve Months (l.517); four segment tables
  (Q4 2025 l.561, Q4 2024 l.617, FY 2025 l.673, FY 2024 l.729); balance sheet December 31, 2025 /
  December 31, 2024 (l.433).
- Headlines (l.21-53; Q4 2025 | FY 2025): revenue +7.5% to $2,738M | +5.1% to $10,645M; property
  revenue +7.6% to $2,673M | +3.7% to $10,305M; NI -32.0% to $837M | +15.3% to $2,629M; Adj.
  EBITDA +7.5% to $1,819M | +4.7% to $7,130M; NI attributable -33.3% to $821M | +12.2% to $2,530M;
  AFFO attributable +13.1% to $1,230M | +2.2% to $5,042M; as adjusted +13.1% to $1,230M | +8.2% to
  $5,042M. No headline reason phrase for the NI moves in this edition.
- CEO prose (l.55-57): "high-single-digit growth in AFFO per Share, as adjusted"; "improve
  financial flexibility by returning to our target leverage range"; 2026 focus on "durable revenue
  growth, advancing our new cost efficiency initiatives, and disciplined capital allocation".
- Operating results table (l.63-101; Q4 value, growth | FY value, growth): revenue 2,738 7.5% |
  10,645 5.1%; property revenue 2,673 7.6% | 10,305 3.7%; Total TBG $119 6.5% | $416 5.6%; Organic
  TBG $109 5.9% | $375 5.1%; Property Gross Margin 1,996 7.2% | 7,731 3.7%; PGM% 74.7% | 75.0%; NI
  837 (32.0)% | 2,629 15.3%; NI attributable 821 (33.3)% | 2,530 12.2%; diluted EPS 1.75 (33.2)% |
  5.40 12.0%; Adj. EBITDA 1,819 7.5% | 7,130 4.7%; margin 66.4% | 67.0%; Nareit FFO 1,318 (21.6)% |
  4,161 (20.5)%; AFFO 1,230 13.1% | 5,042 2.2%; AFFO/Share 2.63 13.4% | 10.76 2.1%; AFFO as
  adjusted 1,230 13.1% | 5,042 8.2%; AFFO/Share as adjusted 2.63 13.4% | 10.76 8.0%; cash from
  operations 1,428 19.1% | 5,464 3.3%; cash capex 592 30.7% | 1,721 6.5%; FCF 836 12.0% | 3,743 1.9%.
- Headline footnotes (l.107-121): (1) ATC TIPL as D03; (3) straight-line ~$28.0M (Q4) and $101.0M
  (FY) vs ~$55.9M and $277.6M; (4) FX gains (losses) ~$2.3M and $(809.4)M vs gains ~$539.7M and
  $308.3M; (5) straight-line net ~$19.7M and $64.8M vs ~$47.9M and $230.8M; (6) FY: prior-year
  $1.2B loss on sale of ATC TIPL incl. $1.1B CTA reclassification; (7) as adjusted, defined term
  "2021 Multicurrency Credit Facility" restored (l.119); (8) capex includes $12.7M (Q4) and $40.3M
  (FY) finance lease/easement payments.
- Capital allocation (l.125-145): distributions Q4 $1.70 | FY $6.80; aggregate $792.9M | $3,180.8M;
  growth 4.9% | 4.9% (Q4 declared December 4, 2025, paid February 2, 2026, record December 29,
  2025; l.141). Stock repurchases (l.143): Q4 2025 "approximately 2 million shares ... approximately
  $365 million"; after quarter-end "through February 17, 2026" ~312 thousand shares for ~$53M;
  "remaining approximately $1.6 billion under its buyback program" (singular; compare D04 l.171
  2011/2017 programs); funding via cash on hand, operations and credit-facility borrowings. Capex
  Q4 ~$592M ($63M non-discretionary); FY ~$1.7B ($196M non-discretionary) (l.145). No
  Acquisitions or Other Events paragraph.
- Leverage (l.149-165): 4.9x; total debt $37,220M; cash $1,475M; net debt $35,746M; Q4 annualized
  Adj. EBITDA $7,274M. Liquidity (l.167): ~$11.1B (~$1.5B cash + ~$9.6B revolvers). December 5,
  2025 issued $850.0M 4.700% notes due 2032; proceeds repaid the $4.0B revolving credit facility
  (l.169).
- Outlook FY2026 (l.171-331): FX rates February 24-December 31, 2026, 17 currencies (l.175). FX
  impact now stated "relative to the Company's 2025 results" (not prior outlook): +~$87M property
  revenue, $57M Adj. EBITDA, $44M AFFO, $0.09/share (l.177). No "as adjusted" column; table header
  "Midpoint Growth Rates vs. Prior Year" only (l.181). Table (l.183-193): property revenue
  $10,440-$10,590, 2.0%; NI 2,945-3,025, 14.1%; NI attributable 2,980-3,060, 24.1%; Adj. EBITDA
  7,090-7,160, (0.1)%; AFFO 5,035-5,115, 0.7%; AFFO/Share $10.78-$10.95, 1.0%. PRESENTATION CHANGE:
  footnote (1) (l.195) now gives five segments instead of "international": U.S. & Canada
  $5,060-$5,120M, Latin America $1,645-$1,665M, Africa & APAC $1,535-$1,555M, Europe
  $1,025-$1,055M, Data Centers $1,175-$1,195M; midpoint growth (3.0)%, 0.8%, 8.6%, 10.9%, 12.5%;
  U.S. & Canada "over 3%" straight-line drag. (2) ~2% "associated with a decrease in straight-line
  revenue recognition"; (3) Adj. EBITDA "over 2%" net straight-line drag. Components (l.203-211;
  US&C / LatAm / Afr&APAC / Europe / DC / Total): pass-through N/A / $485 / $382 / $213 / N/A /
  $1,080; straight-line (124) / (34) / 67 / 3 / 18 / (70). TBG outlook by segment (l.221-227;
  US&C / LatAm / Afr&APAC / Europe / Total): organic ~0.5% / (~3%) / ~8.5% / ~4% / ~1%; new site
  ~0% / ~0% / ~3.5% / ~9% / ~1%; total ~0.5% / (~3%) / ~12% / ~13% / ~2%. Capex (l.233-253):
  discretionary $1,050-$1,080 (1,700-2,300 sites; $695M Data Centers), ground lease 200-220,
  start-up 35-55, redevelopment 335-365, capital improvement 160-170, corporate 15; total
  $1,795-$1,905. Reconciliations (l.255-331): interest 1,415-1,395; D&A 2,060-2,070; tax 440; SBC
  140; other 90; straight-line revenue +70; straight-line expense 36; deferred tax 128; other 268;
  capital improvement (160)-(170); corporate (15); NCI (437); diluted shares 467,000 thousand; cash
  interest (1,362)-(1,342); interest income 125; cash taxes (312).
- Conference call 8:30 a.m. ET, "quarter and full year ended December 31, 2025 and its outlook for
  2026" (l.337). About (l.349): "nearly 150,000 communications sites".
- Definitions (l.351-419): same as D04 except "Foreign currency exchange impact" now reads "The
  majority of the Company's Latin America, Africa & APAC and Europe revenue and operating expenses"
  (l.377; earlier editions "international revenue"). Risk factors expanded to 26 items (l.425):
  new/changed include (2) "disputes with our customers"; (8) "divestitures" (partnerships split
  out); (9) "joint ventures and strategic partnerships"; (10) "leverage, debt service obligations
  and repurchase activity"; (11) "increased inflation and interest rates"; (12) "securitization
  transaction" (singular); (20) data center segment operational differences; (22) data governance;
  (23) "transformation initiatives"; (24) "expansion initiatives"; (25) adds "public perception of
  health risks"; refers to "our upcoming annual report on Form 10-K" (D02-D04: "most recent").
- Statement of operations (l.455-509; Q4 2025 / Q4 2024 / FY 2025 / FY 2024): interest income
  40.4/32.1/134.0/135.2; interest expense (344.4)/(321.2)/(1,359.4)/(1,404.5); other income
  (expense) 108.2/514.7/(576.2)/377.6 incl. unrealized FX 2.3/539.7/(809.4)/308.3 (l.477). NI,
  continuing, discontinued and NCI rows in gap l.479. NI attributable 820.7/1,229.6/2,529.5/2,255.0;
  continuing attributable 820.7/1,229.6/2,529.5/3,233.3; discontinued —/—/—/(978.3); basic EPS
  1.76/2.63/5.41/4.83 (continuing 1.76/2.63/5.41/6.92); diluted 1.75/2.62/5.40/4.82 (continuing
  1.75/2.62/5.40/6.91; discontinued FY24 (2.09)); shares basic 467,586/467,337/467,922/467,011,
  diluted 468,429/468,418/468,757/468,120; SBC $31.6M (Q4'25), $174.2M (FY25), $41.9M (Q4'24),
  $192.7M (FY24).
- Cash flow (twelve months, l.513-557): NI 2,628.5/2,280.2; repayments (9,450.1)/(12,429.6); FX on
  cash 101.3/(233.9); cash taxes 328.7/350.8; cash interest 1,287.4/1,424.3. Footnotes: (1) FY 2025
  "$159.6 million from the sale of equity securities in the U.S." and $137.7M South Africa Fiber;
  FY 2024 $238.0M VIL debentures/shares (row itself in gap l.531); (2) finance leases $4.3M/$4.7M;
  (3) easements $36.0M/$32.7M; (4) FY 2025 taxes: (i) $0.3M Singapore "related to the ATC TIPL
  Transaction", (ii) $25.8M South Africa (South Africa Fiber), (iii) $30.4M "related to the sale of
  equity securities in the U.S.", (iv) $6.5M other tax adjustments; FY 2024 Singapore WHT $36.4M.
- Segment tables - PRESENTATION CHANGE: "Total International" column dropped; 8 columns U.S. &
  Canada | Latin America | Africa & APAC | Europe | Data Centers | Total Property | Services | Total;
  TBG/TB rows have 6 values (US&C, LatAm, Afr&APAC, Europe, DC, Total Property). Q4 2025 (l.561-613):
  SOP Margin 79/64/61/54/57/70/29/69%; Revenue Growth 1.6/3.9/23.6/16.0/19.0/7.6/1.1/7.5%; Total TBG
  5.8/3.1/14.7/7.1/N/A/6.5%; Organic 5.6/3.1/12.0/5.0/N/A/5.9%; Prior-Year TB 1,212/273/212/142/—/
  1,838; Organic TB 1,280/282/237/149/—/1,948; New Site 2/(0)/6/3/—/10; Total TB 1,282/281/243/152/—/
  1,958; FX 0/24/19/13/—/56; Current Period 1,282/305/262/165/—/2,014. Q4 2024 (l.617-669; no ATC
  TIPL footnote on this table): SOP Margin 80/62/65/52/49/70/40/69%; Revenue Growth 0.2/(3.3)/3.4/
  15.6/9.7/2.0/203.3/3.7%; Total TBG 4.2/2.6/18.3/7.3/N/A/5.7%; Organic 4.2/2.5/13.3/5.7/N/A/5.0%;
  Prior-Year TB 1,163/300/197/133/—/1,793; Organic 1,212/307/223/140/—/1,882; New Site 0/0/10/2/—/
  12; Total 1,212/308/233/142/—/1,895; FX (0)/(35)/(21)/(1)/—/(56); Current Period 1,212/273/212/
  142/—/1,838. FY 2025 (l.673-725): SOP Margin 80/63/63/56/53/70/41/69%; Revenue Growth 0.0/(4.4)/
  17.8/12.3/13.9/3.7/75.3/5.1%; Total TBG 4.3/3.1/15.7/7.1/N/A/5.6%; Organic 4.2/3.0/12.9/5.1/N/A/
  5.1%; Prior-Year TB 4,865/1,177/824/564/—/7,430; Organic 5,069/1,213/931/593/—/7,806; New Site
  6/1/23/11/—/40; Total 5,075/1,214/954/604/—/7,846; FX (0)/(40)/35/26/—/20; Current Period 5,074/
  1,173/989/630/—/7,867. FY 2024 (l.729-785; Africa & APAC footnote "Excludes the operating results
  of ATC TIPL"): SOP Margin 80/63/63/55/49/70/41/70%; Revenue Growth 0.6/(4.5)/(2.9)/7.6/10.8/0.7/
  35.5/1.1%; Total TBG 4.7/2.4/19.3/7.3/N/A/6.1%; Organic 4.7/2.3/13.1/5.8/N/A/5.3%; Prior-Year TB
  4,649/1,194/800/525/—/7,168; Organic 4,867/1,221/905/556/—/7,549; New Site (2)/2/49/8/—/57; Total
  4,865/1,223/955/564/—/7,606; FX (0)/(46)/(131)/1/—/(176); Current Period 4,865/1,177/824/564/—/
  7,430.
- Selected info (l.789-877): Adj. EBITDA 1,818.5/1,692.0/7,130.0/6,812.1; total revenue 2,737.5/
  2,547.6/10,644.6/10,127.2; margin 66/66/67/67% (l.799-803). Nareit/AFFO (l.811-863): NI 836.8/
  1,230.5/2,628.5/2,280.2; RE D&A 480.9/465.5/1,899.6/1,879.6; losses on real estate incl.
  impairments 112.1/68.7/83.5/91.6; deferred financing 13.1/14.1/54.1/54.1; AFFO discontinued
  —/—/—/365.2; AFFO continuing 1,230.0/1,087.8/5,041.6/4,568.9; interest savings —/—/—/92.2; AFFO
  as adjusted 1,230.0/1,087.8/5,041.6/4,661.1; per Share as adjusted 2.63/2.32/10.76/9.96.
  Footnotes: (1) FY 2024 loss from discontinued ops $978.3M; (2) impairment charges ~$100.2M (Q4
  2025), $68.6M (Q4 2024), $100.7M (FY 2025), $68.6M (FY 2024); FY 2025 South Africa Fiber gain
  $53.6M; (4) FY 2024 discontinued RE D&A $91.3M, $1.2B real-estate losses, $1.2B loss on sale of
  ATC TIPL; (5) Q4 2025 tax adjustments $6.2M South Africa, $30.4M U.S. equity securities sale,
  $6.5M other; FY 2025 $0.3M Singapore, $25.8M South Africa, $30.4M, $6.5M; the "nonrecurring"
  sentence of D02-D04 is absent (footnote goes straight to "Accordingly, we believe ..."); (6) FX
  $2.3M, $539.7M, $(809.4)M, $308.3M. EBITDA-to-AFFO (l.865-877): AFFO/Share 2.63/2.32/10.76/10.54;
  as adjusted 1,230.0/1,087.8/5,041.6/4,661.1 and 2.63/2.32/10.76/9.96.
- Capture gaps (31): l.439 (516) BS assets; l.445 (574) BS liabilities; l.451 (381) BS equity - no
  visible balance-sheet figures; l.463 (143) SoO revenue rows (4 columns); l.469 (377) opex
  through operating income; l.479 (458) NI / continuing / discontinued / NCI rows between "Other
  income (expense)" (l.477) and NI attributable (l.481); l.527 (506) CF operating adjustments;
  l.531 (400) investing rows (incl. footnote-1 proceeds row); l.535 (161) financing rows before
  repayments (l.537); l.539 (428) financing rows after repayments (incl. footnote-3 row) before FX
  (l.541); l.543 (256) cash roll-forward; l.573 (324) Q4 2025 segment revenue/opex/GM/SG&A/SOP rows;
  l.589 (135) Q4 2025 TB bridge; l.601 (306) Q4 2025 rows after Current Period TB; l.629 (324) Q4
  2024 segment rows; l.645 (135) Q4 2024 TB bridge; l.657 (314) Q4 2024 rows after Current Period
  TB; l.685 (350) FY 2025 segment rows; l.701 (144) FY 2025 TB bridge; l.713 (329) FY 2025 rows
  after Current Period TB; l.743 (344) FY 2024 segment rows; l.759 (146) FY 2024 TB bridge; l.771
  (332) FY 2024 rows after Current Period TB; l.797 (477) Adj. EBITDA reconciling rows (4 columns);
  l.823 (602) Nareit rows incl. Nareit FFO total; l.827 (688) AFFO total/shares/per-Share rows;
  l.871 (746) EBITDA-to-AFFO rows before AFFO/Share (l.873); l.887 (274) Q4 2025 segment GM recon;
  l.895 (275) Q4 2024 segment GM recon; l.905 (287) FY 2025 segment GM recon; l.913 (289) FY 2024
  segment GM recon.
- Coverage: FULL - lines 1-920 read; 31 gaps unresolvable.

## D06 - "AMERICAN TOWER CORPORATION REPORTS FIRST QUARTER 2026 FINANCIAL RESULTS"

- Source: `docs/amt_ex991_2026-04-28.txt` | text, 712 lines; file "pressreleaseq12026.htm" (l.5).
- Written by: American Tower Corporation; dateline "Boston, Massachusetts - April 28, 2026" (l.41).
  Contact Spencer Kurn, SVP Investor Relations (l.13-17). CEO quote attributed to "Steve Vondran"
  (l.43; D02-D05 and D07 use "Steven Vondran").
- Type, date, edition: Q1 2026 earnings release; outlook "as of April 28, 2026" (l.149).
- Period: "quarter ended March 31, 2026" vs "quarter ended March 31, 2025" (l.49). All tables three
  months; balance sheet March 31, 2026 / December 31, 2025 (l.409).
- PRESENTATION CHANGES vs D02-D05: "CONSOLIDATED HIGHLIGHTS" and overview carry no (1)(2) ATC
  TIPL/discontinued-operations footnotes; no "as adjusted" AFFO lines anywhere (headline, table,
  definitions list l.331, definitions l.367-369, AFFO reconciliation); no "As Adjusted:" block;
  segment tables keep D05's 8-column layout (no Total International).
- Headlines (l.21-41): revenue +6.8% to $2,738M; property revenue +7.3% to $2,670M; NI +76.2% to
  $879M; Adj. EBITDA +5.2% to $1,835M; NI attributable +75.9% to $860M; AFFO attributable +2.6% to
  $1,324M.
- CEO prose (l.43-45): "excellent start to 2026"; "strongest strategic position in more than a
  decade" (stated as "I believe").
- Operating results table (l.51-85): revenue 2,738 6.8%; property revenue 2,670 7.3%; Total TBG $44
  2.3%; Organic TBG $32 1.7%; Property Gross Margin 2,005 6.2%; PGM% 75.1%; NI 879 76.2%; NI
  attributable 860 75.9%; diluted EPS 1.84 76.9%; Adj. EBITDA 1,835 5.2%; margin 67.0%; Nareit FFO
  1,279 56.7%; AFFO 1,324 2.6%; AFFO/Share 2.84 3.3%; cash from operations 1,401 8.2%; cash capex
  460 35.3%; FCF 941 (1.5)%.
- Footnotes (l.89-93): (1) FX gains ~$68.1M vs losses $(345.7)M; (2) "an increase in other
  operating expenses, primarily due to the gain on the sale of our fiber assets in South Africa
  ("South Africa Fiber") of $53.6 million in the prior-year period" (D02 l.107 described the same
  gain as "an increase in other operating income"); (3) capex includes $10.4M finance lease/
  easement payments.
- Capital allocation (l.99-119): distribution $1.79, aggregate $833.9M, growth 5.3% (declared March
  5, 2026, "will be paid on April 28, 2026", record April 14, 2026; l.115). "Stock Repurchase
  Program" (l.117): Q1 2026 ~1.1 million shares for ~$184M; after quarter-end "through April 21,
  2026" ~0.1 million shares for ~$19M (no remaining-authorization figure stated). Capex ~$460M,
  $48M non-discretionary (l.119).
- Leverage (l.121-137): 4.9x; total debt $37,322M; cash $1,609M; net debt $35,713M; Q1 annualized
  Adj. EBITDA $7,341M. Liquidity (l.139): ~$10.4B (~$1.6B cash + ~$8.8B revolvers). Feb 13, 2026
  repaid $500.0M 4.400% notes due February 15, 2026; April 14, 2026 repaid $700.0M 1.600% notes due
  April 15, 2026 (l.141-143). No new issuance stated.
- Outlook FY2026 revision (l.147-309): FX rates April 28-December 31, 2026, 17 currencies (l.151).
  FX vs "prior 2026 outlook": +~$107M property revenue, $67M Adj. EBITDA, $55M AFFO, $0.12/share
  (l.153). Midpoints raised by $145M, $105M, $55M, $0.12 "As a result of the estimated positive
  foreign currency exchange rate fluctuations described above and accelerating straight-line
  revenue in Latin America"; NI and NI attributable midpoints increased by $70M and $85M
  "primarily due to unrealized foreign currency gains" (l.155). Table (l.159-171): property
  revenue $10,585-$10,735, 3.4%; NI 3,015-3,095, 16.2%; NI attributable 2,965-3,045, 18.8%; Adj.
  EBITDA 7,195-7,265, 1.4%; AFFO 5,090-5,170, 1.8%; AFFO/Share $10.90-$11.07, 2.1%. Footnote (1)
  (l.173): U.S. & Canada $5,060-$5,120M, Latin America $1,730-$1,750M, Africa & APAC
  $1,595-$1,615M, Europe $1,025-$1,055M, Data Centers $1,175-$1,195M; growth (3.0)%, 5.9%, 12.8%,
  10.9%, 12.5%; (2) ~1% straight-line drag (D05: ~2%); (3) ~2% (D05: over 2%). Components
  (l.185-187): pass-through N/A / $497 / $403 / $212 / N/A / $1,112; straight-line (124) / 6 / 70
  / 3 / 18 / (27). TBG outlook (l.199-203): identical to D05. Capex (l.211-231): discretionary
  $1,050-$1,080 (1,700-2,300 sites; $695M Data Centers), ground lease 200-220, start-up 35-55,
  redevelopment 335-365, capital improvement 165-175, corporate 15; total $1,800-$1,910.
  Reconciliations (l.233-309): interest 1,430-1,410; D&A 2,135-2,145; tax 470; SBC 145; other —
  (zero); straight-line revenue 27; expense 36; deferred tax 152; other 197; capital improvement
  (165)-(175); corporate (15); NCI (437); shares 467,000; cash interest (1,362)-(1,342); interest
  income 129; cash taxes (318).
- Conference call 8:30 a.m. ET (l.315). About (l.327): "nearly 150,000 communications sites".
- Definitions (l.329-395): as D05 minus the two "as adjusted" definitions; FX-impact wording as D05
  (l.357). Risk factors 26 items as D05 (l.401); example list adds "our expectations regarding our
  stock repurchase program"; refers to "our most recent annual report on Form 10-K".
- Statement of operations (l.431-471; Q1 2026 / Q1 2025): interest income 36.0/26.9; interest
  expense (347.3)/(325.3); other income (expense) 90.2/(338.2) incl. unrealized FX 68.1/(345.7)
  (l.453); NI/NCI/NI attributable rows in gap l.455; basic EPS 1.84/1.05; diluted 1.84/1.04 (no
  continuing/discontinued split); shares basic 466,202/467,640, diluted 466,833/468,519; SBC
  $58.4M/$53.4M. Q1 2025 comparatives equal D02's values.
- Cash flow (l.475-519): NI 878.5/498.6; "Repayments of notes payable, credit facilities, senior
  notes, secured debt and finance leases(1)" (label drops "term loans") (1,226.1)/(1,840.7); FX on
  cash 36.8/29.9; VISIBLE here (cut in D02): net increase in cash 132.7/131.0; beginning cash
  1,605.2/2,108.2; ending cash 1,737.9/2,239.2 (l.505-509); cash taxes 44.3/32.9; cash interest
  434.8/370.1; finance leases $0.8M/$0.7M; easements $9.6M/$8.2M.
- Segment tables (8 columns). Q1 2026 (l.523-573): SOP Margin 81/66/63/58/53/70/35/69%; Revenue
  Growth (2.8)/20.3/13.5/22.4/18.4/7.3/(9.4)/6.8%; Total TBG 0.7/(2.1)/13.9/6.0/N/A/2.3%; Organic
  0.6/(2.0)/10.5/3.9/N/A/1.7%; Prior-Year TB 1,256/280/228/144/—/1,908; Organic TB 1,264/274/252/
  150/—/1,941; New Site 1/(0)/8/3/—/12; Total TB 1,265/274/260/153/—/1,952; FX 0/35/21/18/—/74;
  Current Period 1,265/309/281/171/—/2,026. Q1 2025 recast (l.577-629): SOP Margin 81/64/64/57/50/
  71/45/70%; Revenue Growth (0.9)/(10.4)/12.3/4.2/8.7/0.2/147.0/2.0%; TB rows identical to D02's
  Q1 2025 table with the Total International column removed (D02 l.593-617).
- Selected info (l.633-691): Adj. EBITDA 1,835.2/1,744.2; total revenue 2,737.5/2,562.8; margin
  67%/68% (l.645-649). Nareit/AFFO: NI 878.5/498.6; RE D&A 483.6/457.3; "Losses (gains) from sale or
  disposal..." 24.2/(49.1); deferred financing 13.0/13.8. Footnotes: (1) Q1 2025 South Africa Fiber
  gain $53.6M; (2) Stonepeak preferred equity; (3) "refunds in Germany of $0.5 million. We believe
  that these tax payments are nonrecurring"; (4) FX (gains) losses $(68.1)M and $345.7M; (5)
  acquisition/integration/disposition costs; (6) NCI adjustments.
- Capture gaps (22): l.415 (516) BS assets; l.421 (572) BS liabilities; l.427 (382) BS equity - no
  visible balance-sheet figures; l.439 (92) SoO revenue rows; l.445 (291) opex through operating
  income; l.455 (329) rows between "Other income (expense)" (l.453) and per-share block (l.457) -
  pre-tax, tax, NI, NCI and NI attributable rows not visible; l.489 (461) CF operating adjustments;
  l.493 (325) investing rows; l.497 (142) financing rows before repayments (l.499); l.501 (379)
  financing rows after repayments (incl. footnote-2 easement row); l.533 (325) Q1 2026 segment
  revenue/opex/GM/SG&A/SOP rows; l.549 (135) Q1 2026 TB bridge; l.561 (311) Q1 2026 rows after
  Current Period TB; l.589 (324) Q1 2025 segment rows; l.605 (135) Q1 2025 TB bridge; l.617 (312)
  Q1 2025 rows after Current Period TB; l.643 (297) Adj. EBITDA reconciling rows; l.663 (443)
  Nareit rows incl. Nareit FFO total; l.667 (507) AFFO total/shares/AFFO-per-Share rows; l.691 (585)
  the ENTIRE EBITDA-to-AFFO reconciliation (no row visible); l.701 (274) Q1 2026 segment GM recon;
  l.709 (275) Q1 2025 segment GM recon.
- Coverage: FULL - lines 1-712 read; 22 gaps unresolvable.

## D07 - "AMERICAN TOWER CORPORATION REPORTS SECOND QUARTER 2026 FINANCIAL RESULTS"

- Source: `docs/amt_ex991_2026-07-28.txt` | text, 716 lines; file "pressreleaseq22026.htm" (l.5).
- Written by: American Tower Corporation; dateline "Boston, Massachusetts - July 28, 2026" (l.39).
  Contact Spencer Kurn, SVP Investor Relations (l.13-17). CEO quote "Steve Vondran" (l.41-45).
- Type, date, edition: Q2 2026 earnings release; outlook "as of July 28, 2026" (l.153). Latest
  edition in the bundle.
- Period: "quarter ended June 30, 2026" vs "quarter ended June 30, 2025" (l.49). SoO has Three and
  Six Months Ended June 30 columns (l.439); cash flow Six Months (l.477); segment/reconciliation
  tables three months; balance sheet June 30, 2026 / December 31, 2025 (l.413). Presentation as D06
  (no ATC TIPL footnotes, no "as adjusted", 8-column segment tables).
- Headlines (l.21-39): revenue +4.7% to $2,749M; property revenue +6.3% to $2,688M; NI +133.2% to
  $888M; Adj. EBITDA +3.2% to $1,808M; NI attributable +136.5% to $868M; AFFO attributable +3.8% to
  $1,264M.
- CEO prose (l.41-45): "record leasing activity at CoreSite"; "mid-single-digit AFFO per share
  growth, normalized for one-time DISH churn" (only DISH mention in the bundle); "raise our
  full-year outlook for the second time this year"; "We believe these powerful secular trends are
  creating a multi-year demand cycle" (l.43); "we believe we are well positioned" (l.45).
- Operating results table (l.51-85): revenue 2,749 4.7%; property revenue 2,688 6.3%; Total TBG $46
  2.4%; Organic TBG $34 1.7%; Property Gross Margin 1,980 4.9%; PGM% 73.7%; NI 888 133.2%; NI
  attributable 868 136.5%; diluted EPS 1.86 138.5%; Adj. EBITDA 1,808 3.2%; margin 65.8%; Nareit FFO
  1,249 63.4%; AFFO 1,264 3.8%; AFFO/Share 2.71 4.2%; cash from operations 1,487 16.0%; cash capex
  329 5.1%; FCF 1,158 19.6%. Footnotes (l.89-91): (1) FX gains ~$42.1M vs losses $(484.0)M; (2)
  capex includes $7.9M finance lease/easement payments.
- Capital allocation (l.97-119): distribution $1.79, aggregate $834.1M, growth 5.3% (declared May
  21, 2026, paid July 13, 2026, record June 12, 2026; l.113). Stock Repurchase Program (l.115): Q2
  2026 ~0.1 million shares for ~$19M (same size/amount as D06's post-quarter figure "through April
  21, 2026", D06 l.117). Divestitures (l.117): "On June 15, 2026, the Company completed the sale of
  its subsidiary in the Philippines ("ATC Philippines") for a total consideration of $75.6 million
  at the date of closing. On June 29, 2026, the Company completed the sale of its controlling
  interest in Kirtonkhola Tower Bangladesh Limited ("KTBL") for total consideration of $6.9 million
  at the date of closing." Capex ~$329M, $47M non-discretionary (l.119).
- Leverage (l.121-137): 4.9x; total debt $37,190M; cash $1,763M; net debt $35,427M; Q2 annualized
  Adj. EBITDA $7,233M. Liquidity (l.139): "approximately $9.9 billion" (~$1.8B cash + ~$8.2B
  revolvers, as printed).
- Financing (l.141-147): April 14, 2026 repaid $700.0M 1.600% notes due April 15, 2026 (also in
  D06 l.143). May 7, 2026 amended the $6.0B 2021 Multicurrency Credit Facility, $4.0B revolver and
  $1.0B term loan ("Loans") to extend maturities "and to include limited conditionality provisions
  in the 2021 Multicurrency Credit Facility, permitting the Company to borrow up to $5.0 billion in
  connection with certain acquisitions" (l.143). May 21, 2026 repaid EUR 500.0M 1.950% notes due
  May 22, 2026. May 27, 2026 issued EUR 750.0M (~$872.0M) 4.000% notes due 2033; proceeds to repay
  the 2021 Multicurrency Credit Facility and partially redeem the 4.125% Notes. June 18, 2026
  redeemed EUR 250.0M of 4.125% notes due May 16, 2027 ("4.125% Notes"); EUR 350.0M remain
  outstanding (l.147).
- Outlook FY2026 second revision (l.151-313): FX rates July 28-December 31, 2026 now 15 currencies
  (a)-(o) - Bangladeshi Taka and Philippine Pesos no longer listed (l.155; all earlier lists had 17).
  FX vs "prior 2026 outlook": +~$35M property revenue, $22M Adj. EBITDA, $29M AFFO, $0.06/share
  (l.157). Midpoints raised by $110M, $45M, $45M, $0.09 "As a result of the estimated positive
  foreign currency exchange rate fluctuations described above, Data Center outperformance and
  one-time expense benefits"; NI and NI attributable midpoints increased by $255M and $235M
  "primarily due to unrealized foreign currency gains" (l.159). Table (l.163-175): property revenue
  $10,695-$10,845, 4.5%; NI 3,270-3,350, 25.9%; NI attributable 3,200-3,280, 28.1%; Adj. EBITDA
  7,240-7,310, 2.0%; AFFO 5,135-5,215, 2.7%; AFFO/Share $11.00-$11.17, 3.0%. Footnote (1) (l.177):
  U.S. & Canada $5,060-$5,120M, Latin America $1,790-$1,810M, Africa & APAC $1,620-$1,640M, Europe
  $1,025-$1,055M, Data Centers $1,200-$1,220M; growth (3.0)%, 9.6%, 14.6%, 10.9%, 14.9%; (2) ~2%
  straight-line drag; (3) ~2%. Components (l.189-191): pass-through N/A / $516 / $478 / $230 / N/A
  / $1,224; straight-line (124) / 3 / 33 / 3 / 19 / (66). TBG outlook (l.203-207): organic as D05/
  D06; new site Europe ~6% (D05/D06 ~9%); total Europe ~10% (D05/D06 ~13%); other cells unchanged.
  Capex (l.215-235): as D06 except capital improvement 170-180; total $1,805-$1,915.
  Reconciliations (l.237-313): interest 1,450-1,430; D&A 2,055-2,065; tax 490; SBC 145; other (170);
  straight-line revenue 66; expense 34; deferred tax 151; other 34; capital improvement
  (170)-(180); corporate (15); NCI (435); shares 467,000; cash interest (1,400)-(1,380); interest
  income 154; cash taxes (339).
- Conference call 8:30 a.m. ET (l.319). About (l.331): "over 148,000 communications sites".
- Definitions (l.333-399) and 26 risk factors (l.405): same as D06.
- Statement of operations (l.435-469; Q2 2026 / Q2 2025 / 6M 2026 / 6M 2025): interest income and
  interest expense rows are CUT (gap l.453); other income (expense) 53.8/(373.9)/144.0/(712.1) incl.
  unrealized FX 42.1/(484.0)/110.2/(829.7) (l.455); NI/NCI/NI attributable rows cut (gap l.457);
  basic EPS 1.86/0.78/3.71/1.83; diluted 1.86/0.78/3.70/1.83; shares basic 465,938/468,178/466,068/
  467,909, diluted 466,265/468,791/466,578/468,717; SBC $34.2M (Q2'26), $92.6M (6M'26), $47.3M
  (Q2'25), $100.7M (6M'25).
- Cash flow (six months, l.473-517): NI 1,766.0/879.1; repayments (4,274.1)/(5,318.2); FX on cash
  36.4/116.6; net increase 287.4/101.4; beginning 1,605.2/2,108.2; ending 1,892.6/2,209.6; cash
  taxes 163.2/131.4; cash interest 789.4/684.2; finance leases $1.6M/$1.7M; easements $16.7M/$15.5M.
- Segment tables (8 columns). Q2 2026 (l.521-577): Africa & APAC footnote (1) "Includes results of
  Bangladesh and the Philippines through dates of sale" (l.567); SOP Margin 79/65/59/57/53/69/36/68%;
  Revenue Growth (2.5)/13.4/23.5/11.5/13.4/6.3/(38.4)/4.7%; Total TBG 0.7/(2.4)/14.5/6.0/N/A/2.4%;
  Organic 0.7/(2.4)/10.6/4.1/N/A/1.7%; Prior-Year TB 1,261/288/242/157/—/1,948; Organic TB 1,270/281/
  268/163/—/1,982; New Site 0/(0)/9/3/—/13; Total TB 1,270/281/277/166/—/1,994; FX 0/32/10/5/—/46;
  Current Period 1,270/313/287/171/—/2,041. Q2 2025 recast (l.581-633): SOP Margin 80/61/63/57/53/70/
  45/69%; Revenue Growth (0.6)/(13.2)/12.4/14.5/13.5/1.2/109.9/3.2%; TB rows identical to D03's Q2
  2025 table minus Total International (D03 l.589-613).
- Selected info (l.637-695): Adj. EBITDA 1,808.2/1,751.8; total revenue 2,749.1/2,626.9; margin
  66%/67% (l.649-653). Nareit/AFFO: NI 887.5/380.5; RE D&A 480.4/475.4; "(Gains) losses from sale or
  disposal..." (8.2)/9.1; deferred financing 13.0/13.7. Footnotes: (1) Q2 2026 "net gain on the
  sales of ATC Philippines and the controlling interest in KTBL of $20.4 million"; "For the three
  months ended June 30, 2025, includes a gain on the sale of our fiber assets in South Africa
  ("South Africa Fiber") of $53.6 million" (l.675 - see Contradictions in Shared ground); (2)
  Stonepeak; (3) Q2 2025 South Africa taxes $19.6M, "these tax payments are nonrecurring"; (4) FX
  (gains) losses $(42.1)M and $484.0M; (5) acquisition/integration/disposition costs; (6) NCI.
- Capture gaps (23): l.419 (518) BS assets; l.425 (572) BS liabilities; l.431 (382) BS equity - no
  visible balance-sheet figures; l.443 (140) SoO revenue rows (4 columns); l.449 (389) opex through
  operating income; l.453 (149) first OTHER INCOME (EXPENSE) rows - interest income and interest
  expense not visible; l.457 (426) pre-tax/tax/NI/NCI/NI attributable rows before per-share block
  (l.459); l.487 (518) CF operating adjustments; l.491 (330) investing rows (divestiture proceeds,
  if any, not visible); l.495 (150) financing rows before repayments (l.497); l.499 (487) financing
  rows after repayments (incl. footnote-2 easement row); l.535 (325) Q2 2026 segment revenue/opex/
  GM/SG&A/SOP rows; l.551 (133) Q2 2026 TB bridge; l.563 (312) Q2 2026 rows after Current Period TB;
  l.593 (327) Q2 2025 segment rows; l.609 (135) Q2 2025 TB bridge; l.621 (309) Q2 2025 rows after
  Current Period TB; l.647 (348) Adj. EBITDA reconciling rows; l.667 (441) Nareit rows incl. Nareit
  FFO total; l.671 (555) AFFO total/shares/AFFO-per-Share rows; l.695 (582) the ENTIRE EBITDA-to-AFFO
  reconciliation; l.705 (274) Q2 2026 segment GM recon; l.713 (273) Q2 2025 segment GM recon.
- Coverage: FULL - lines 1-716 read; 23 gaps unresolvable.

## Shared ground (navigation only)

### Entities and aliases across documents

- American Tower Corporation: all seven ("American Tower", "the Company"; "ATC" only as D01's
  contact label l.13; "AMT" inside metric names D02-D07).
- CoreSite / CoreSite Realty Corporation: D01 throughout; afterwards only in CEO quotes - D02 l.47
  ("favorable leasing and pricing trends at CoreSite"), D03 l.49 ("double-digit growth at
  CoreSite"), D07 l.41 ("record leasing activity at CoreSite"). D02-D07 never state the CoreSite
  closing date, final price or that "Data Centers" equals CoreSite; the Data Centers segment is
  defined as "the Company's data center facilities and related assets" (D02 l.201/227, D03
  l.201/227, D04 l.203/229, D05 l.195/219, D06 l.173/195, D07 l.177/199). AFFO definition cites
  "minority interests in its Europe business and its U.S. data center business" (D02 l.397, D03
  l.399, D04 l.399, D05 l.387, D06 l.367, D07 l.371).
- People: Adam Smith - "Vice President, Investor Relations" (D01 l.13-15) vs "Senior Vice
  President, Investor Relations and FP&A" (D02 l.13-15); Kate Reeb (D03 l.13); Spencer Kurn
  (D04-D07 l.13). CEO: Tom Bartlett (D01 l.39, 2021); "Steven Vondran" (D02 l.47, D03 l.49, D04
  l.53, D05 l.55) = "Steve Vondran" (D06 l.43, D07 l.41), both titled American Tower's CEO. Paul
  Szurek and Kate Ruppe only D01.
- ATC TIPL (alias "ATC India" only D02 l.99) / Data Infrastructure Trust / Brookfield Asset
  Management: headline footnote (1) D02 l.99, D03 l.99, D04 l.103, D05 l.107; $1.2B loss on sale
  incl. $1.1B CTA: D04 l.117, l.759; D05 l.117, l.849. Absent from D06/D07 (only generic
  "discontinued operations" wording inside definitions, D06 l.363-373, D07 l.367-377). Former
  segment named "Asia-Pacific property segment" in footnote (1) while tables use "Africa & APAC"
  with "Excludes the operating results of ATC TIPL" (D02 l.685/821; D03 l.681/815; D04 l.681/817;
  D05 l.775/917 FY 2024 tables only).
- India Term Loan (~$120M repaid) and ~$2.0B proceeds used on the 2021 Multicurrency Credit
  Facility ("as adjusted" basis): D02 l.111/399/775; D03 l.113/401/771; D04 l.119/401/771; D05
  l.119/389/863. Interest-savings adjustment amounts: Q1 2024 32.9 (D02 l.749), Q2 2024 32.9 (D03
  l.745), Q3 2024 26.4 (D04 l.745), FY 2024 92.2 (D05 l.835).
- South Africa Fiber (sold March 6, 2025 for ZAR 2.5B, ~$137.7M; gain $53.6M): D02 l.107/141/759;
  D03 l.569/761 (taxes $19.6M); D04 l.563 (proceeds $137.7M in 9M 2025 investing) and l.569 (taxes
  $19.6M); D05 l.551 (proceeds), l.557/851 (taxes $25.8M FY; $6.2M Q4), l.845 (FY gain); D06 l.91,
  l.671; D07 l.675, l.681.
- Stonepeak Partners LP (mandatorily convertible preferred equity distributions): D02 l.761, D03
  l.757, D04 l.757, D05 l.847, D06 l.673, D07 l.677.
- Vodafone Idea Limited ("VIL") debenture/share sale proceeds $238.0M (9M/FY 2024): D04 l.563, D05
  l.551.
- Other one-document entities: DE1 Denver data center (D02 l.139 completed April 1, 2025; D03
  l.139 Q2 acquisitions "primarily driven by" DE1); ATC South Africa Wireless Infrastructure
  Proprietary Limited (D02 l.141); 2015 Securitization (D03 l.169); U.S. equity securities sale
  (D05 l.551/557/851); Germany refunds $0.5M (D06 l.675); Europe tax law change (D04 l.183); ATC
  Philippines and Kirtonkhola Tower Bangladesh Limited "KTBL" (D07 l.117/567/675); DISH (D07 l.41);
  Latin America "customer events" (D03 l.49) and "accelerating straight-line revenue in Latin
  America" (D06 l.155).
- Credit facilities: $6.0B "2021 Multicurrency Credit Facility" defined D02 l.167, D03 l.167, D05
  l.119, D07 l.143; long-form name without defined term D04 l.119 while D04 l.401/l.771 use the
  defined term (not defined anywhere in D04). $4.0B revolver ("2021 Credit Facility" D02 l.167;
  unnamed D04 l.169, D05 l.169, D07 l.143). $1.0B term loan (D02 l.167, D07 l.143). Amendments:
  January 28, 2025 (D02 l.167; extend maturities, Applicable Margins) and May 7, 2026 (D07 l.143;
  extend maturities, up-to-$5.0B acquisition borrowing with limited conditionality).
- Notes repaid / issued (date; doc line): repaid $650.0M 2.950% (Jan 14, 2025; D02 l.165), $750.0M
  2.400% (Mar 14, 2025; D02 l.165), EUR 500.0M 1.375% (Apr 3, 2025; D03 l.163), $750.0M 4.000% (May
  30, 2025; D03 l.165), $525.0M Series 2015-2 Class A (Jun 16, 2025; D03 l.169), $500.0M 1.300% (Sep
  12, 2025; D04 l.167), $500.0M 4.400% (Feb 13, 2026; D06 l.141), $700.0M 1.600% (Apr 14, 2026; D06
  l.143 AND D07 l.141 - duplicated), EUR 500.0M 1.950% (May 21, 2026; D07 l.145), EUR 250.0M of
  4.125% notes due May 16, 2027 redeemed (Jun 18, 2026; D07 l.147). Issued $650.0M 4.900% 2030 +
  $350.0M 5.350% 2035 (Mar 14, 2025; D02 l.169), EUR 500.0M 3.625% 2032 (May 30, 2025; D03 l.167),
  $575.0M (Sep 16, 2025; D04 l.169; terms not stated), $850.0M 4.700% 2032 (Dec 5, 2025; D05 l.169),
  EUR 750.0M 4.000% 2033 (May 27, 2026; D07 l.147).
- Buybacks: D04 l.171 (none in Q3 2025; ~151,000 shares/~$28.0M Oct 1-21, 2025; 2011 program
  exhausted; ~$2.0B left under 2017 program); D05 l.143 (Q4 2025 ~2M shares/~$365M; ~312K/~$53M
  through Feb 17, 2026; ~$1.6B remaining); D06 l.117 (Q1 2026 ~1.1M/~$184M; ~0.1M/~$19M through Apr
  21, 2026); D07 l.115 (Q2 2026 ~0.1M/~$19M). D02/D03 have no buyback paragraph.
- Distributions per share / aggregate / declared: D02 l.125-133 $1.70/$795.8M/Mar 6, 2025; D03
  l.127-135 $1.70/$796.0M/May 15, 2025; D04 l.133-141 $1.70/$796.1M/Sep 18, 2025; D05 l.133-141
  $1.70 ($6.80 FY)/$792.9M ($3,180.8M FY)/Dec 4, 2025; D06 l.107-115 $1.79/$833.9M/Mar 5, 2026;
  D07 l.105-113 $1.79/$834.1M/May 21, 2026. YoY growth 4.9% (D02-D05), 5.3% (D06-D07).
- Net Leverage Ratio / liquidity: D02 5.0x/~$11.7B; D03 5.1x/~$10.5B; D04 4.9x/~$10.7B; D05 4.9x/
  ~$11.1B; D06 4.9x/~$10.4B; D07 4.9x/~$9.9B (calculation tables at D02 l.149, D03 l.147, D04
  l.151, D05 l.153, D06 l.125, D07 l.125).
- "About American Tower" site counts: D01 l.77 ~219,000; D02 l.359 over 149,000; D03 l.359 nearly
  150,000; D04 l.361 over 149,000; D05 l.349 nearly 150,000; D06 l.327 nearly 150,000; D07 l.331
  over 148,000.
- Outlook FX currency lists: 17 currencies D02 l.175, D03 l.175, D04 l.177, D05 l.175, D06 l.151;
  15 in D07 l.155 (no Bangladeshi Taka, no Philippine Pesos).

### Periods and series covered by more than one document

- Q1 2025: primary D02; recast comparative D06 (SoO l.449-467, cash flow l.485-513, segment l.577-
  629, Adj. EBITDA l.645-649, Nareit l.657-665); inside D03 six-month columns. Q2 2025: primary
  D03; comparative D07 (segment l.581-633, Adj. EBITDA l.649-653, Nareit l.661-669); 6M 2025 in
  D03 and D07. Q3 2025: D04 only (9M in D04; FY in D05). Q4 2025 / FY 2025: D05 only.
- 2024 comparatives: Q1 2024 D02; Q2 2024 + 6M D03; Q3 2024 + 9M D04; Q4 2024 + FY 2024 D05.
- Q1 2026: D06; 6M 2026 in D07. Q2 2026: D07.
- FY 2025 outlook editions: D02 (Apr 29, 2025), D03 (Jul 29), D04 (Oct 28); FY 2025 actuals D05.
  The "prior 2025 outlook" revised by D02 (l.177) is not in the bundle.
- FY 2026 outlook editions: D05 initial (Feb 24, 2026; FX vs "2025 results" l.177), D06 revision
  (Apr 28; vs "prior 2026 outlook" l.153), D07 revision (Jul 28; l.157; CEO "second time this year"
  l.41).
- Stated outlook-change drivers: D02 l.181 FX (NI cut: unrealized FX losses); D03 l.181 FX + "core
  outperformance" in property revenue and Adj. EBITDA (NI cut: unrealized FX losses); D04 l.183
  primarily FX (NI raised: unrealized FX gains; NI attributable partly offset by Europe tax-law
  minority interests); D06 l.155 FX + Latin America straight-line (NI raised: FX gains); D07 l.159
  FX + Data Center outperformance + one-time expense benefits (NI raised: FX gains).
- Balance-sheet dates December 31, 2024 (D02-D05) and December 31, 2025 (D05-D07): all rows cut in
  every edition.

### Edition and presentation relationships

- D02-D05: ATC TIPL discontinued-operations footnotes, "as adjusted" AFFO metrics and "As
  Adjusted:" blocks. D06-D07: none of these (headline footnotes renumbered; definitions list drops
  the two "as adjusted" measures, D06 l.331, D07 l.335).
- Segment tables: 9 columns incl. "Total International" (defined "international operations
  excluding Canada") in D02-D04; 8 columns without it from D05 (incl. recast Q1/Q2 2025 tables in
  D06/D07). Outlook property revenue: "international" aggregate (D02 l.201, D03 l.201, D04 l.203)
  vs per-segment Latin America / Africa & APAC / Europe (D05 l.195, D06 l.173, D07 l.177).
- Definitions: same core texts D02-D07; Nareit FFO "accretion, and including" from D03 (D02
  l.407 lacks "and"); FX-impact sentence "international revenue" (D02-D04) vs "Latin America, Africa
  & APAC and Europe revenue" (D05 l.377, D06 l.357, D07 l.361). Risk-factor list 21 items (D02 l.435,
  D03 l.435, D04 l.437) vs 26 items (D05 l.425, D06 l.401, D07 l.405).
- Statement-of-operations "Other (expense) income" label: "foreign currency (losses) gains" (D02
  l.487) vs "unrealized foreign currency" (D03 l.487 onward).
- Repeated identical values across editions (not conflicts, but duplicates that can be mistaken
  for each other): D02 Q1 2025 and D03 Q2 2025 headline TBG "$97 5.2%" and Organic "$87 4.7%" and
  Total Property TB 1,864/1,951/1,961 (D02 l.61-63, l.605-613; D03 l.63-65, l.601-609); total
  revenue 2,737.5 / "$2,738 million" for Q4 2025 (D05 l.27, l.801) and Q1 2026 (D06 l.25, l.647);
  AFFO/Share 2.79 for Q1 2024 (D02 l.789) and Q2 2024 (D03 l.783); Q2 2024 FX loss $21.7M and Q2
  2024 Singapore WHT $21.7M (D03 l.763, l.761); FX impacts vs prior outlook $50M/$30M/$20M/$0.04
  in both D02 l.177 and D04 l.179; ~0.1M shares/~$19M buyback in D06 l.117 (post-Q1) and D07 l.115
  (Q2 2026); FY 2024 AFFO/Share $10.54 (D05 l.873) and the top of D02's 2025 AFFO/Share range
  $10.54 (D02 l.199).

### Defined terms, rules, scope exceptions and enumerated sets (D02 lines; same text in D03-D07 unless noted)

- Tenant Billings Growth: vs "corresponding prior-year period, in each case adjusted for foreign
  currency exchange rate fluctuations" (D02 l.429; D07 l.399). Organic Tenant Billings: sites
  "owned since the beginning of the prior-year period" plus later activity on new sites (D02
  l.377). New Site Tenant Billings: "Day-one Tenant Billings" on sites built/acquired since the
  beginning of the prior-year period; later colocations/escalations/cancellations excluded; "In
  certain cases, this could also include the net impact of certain divestitures" (D02 l.375).
  Tenant Billings has 4 aspects (colocations/amendments, escalations, cancellations, new sites;
  D02 l.373). Revenue components list has 8 items (i)-(viii) (D02 l.371). "Other revenue" can
  include customer settlements, fiber solutions revenue and data centers revenue (D02 l.389).
- Scope rules: "Tenant Billings Growth is not applicable to the Data Centers segment" (outlook
  footnotes, e.g. D02 l.239, D05 l.231, D07 l.211); "Total International reflects the Company's
  international operations excluding Canada" (D02-D04 segment footnotes, e.g. D02 l.623); U.S. &
  Canada property revenue covers all U.S. and Canada assets "other than data center facilities and
  related assets" (D02 l.223, D05 l.217, D07 l.197); actual-results revenue components "translated
  at prior-period foreign currency exchange rates" except current-period lines (D02 l.629).
- Adjusted EBITDA: net income before 10 listed items incl. discontinued operations and "Other
  operating income (expense), including Goodwill impairment" (D02 l.393; D07 l.367). Margin =
  Adjusted EBITDA / total revenue (D02 l.395). AFFO: Nareit FFO before items (i)-(viii), less
  capital-improvement and corporate capex, incl. NCI and discontinued-ops adjustments (D02 l.397;
  D07 l.371). AFFO per Share = AFFO / diluted weighted average shares (D02 l.403). Free Cash Flow =
  cash from operations less total cash capex "including the impacts associated with discontinued
  operations and payments on finance leases and perpetual land easements" (D02 l.405). Net Debt
  and Net Leverage Ratio: include finance lease liabilities "for periods beginning in the first
  quarter of 2019"; ratio uses "the quarter's Adjusted EBITDA multiplied by four" (D02 l.413-415;
  each calculation table instead labels the numerator "Total debt" and the prose says "total debt
  less cash and cash equivalents", e.g. D02 l.147-151). Segment Gross Margin / Operating Profit /
  SOP Margin (D02 l.421-427). As-adjusted AFFO (D02 l.399-401; D03-D05 only; dropped in D06/D07).
- Headline footnote (2) rule (D02 l.101, D03 l.105, D04 l.109, D05 l.109): growth rates for
  revenue, property revenue, TBG, Organic TBG, Property Gross Margin, Adjusted EBITDA and the two
  as-adjusted AFFO metrics EXCLUDE discontinued operations; NI, NI attributable, EPS, Nareit FFO,
  AFFO, AFFO/Share, cash from operations, cash capex and FCF INCLUDE them. Outlook 2024 base on
  continuing-ops basis except NI, NI attributable, AFFO, AFFO/Share (D02 l.179, D03 l.179, D04
  l.181; absent from D05-D07 outlooks).
- Non-recurring tax adjustments excluded from AFFO (Nareit footnote (5)/(3)): Singapore WHT (D02
  l.765, D03 l.761, D04 l.761), South Africa taxes (D03 l.761, D05 l.851, D07 l.681), U.S. equity
  securities sale taxes and "other tax adjustments" (D05 l.851), Germany refunds (D06 l.675).

### Contradictions and inconsistencies (recorded neutrally; no document states precedence)

1. South Africa Fiber gain period: D02 l.107 ("completed on March 6, 2025"), l.141, l.759 ("For
   the three months ended March 31, 2025, includes a gain on the sale of South Africa Fiber of
   $53.6 million") and D06 l.671 (same, three months ended March 31, 2025) vs D07 l.675 ("For the
   three months ended June 30, 2025, includes a gain on the sale of our fiber assets in South
   Africa ... of $53.6 million"). D03 (Q2 2025 release) l.755 mentions no gain; the Q2 2025
   real-estate line is a 9.1 loss in both D03 l.731 and D07 l.665.
2. Same gain's direction wording: D02 l.107 "an increase in other operating income, primarily due
   to the gain" vs D06 l.91 "an increase in other operating expenses, primarily due to the gain".
3. ATC TIPL's former segment: "Asia-Pacific property segment" (D02 l.99 etc.) vs tables "Africa &
   APAC" with ATC TIPL exclusion footnote (D02 l.685).
4. D04 uses the defined term "2021 Multicurrency Credit Facility" (l.401, l.771) without defining
   it (l.119 uses the long-form name).
5. Wording oddities as printed: D02 l.347 "quarter and full year ended March 31, 2025"; D04 l.761
   "For the three ended September 30, 2025"; D05 l.851 "Accordingly, we believe..." with the
   preceding "nonrecurring" sentence absent; D07 l.139 "approximately $9.9 billion" beside ~$1.8B +
   ~$8.2B; D01 l.33 "eight major U.S. markets" vs l.83 "eight key North American markets".

### Narrative passages that repeat table results

- Each release's headline bullets repeat the operating-results table in rounded $M (D02 l.19-45 vs
  l.55-93; D03 l.21-47 vs l.57-95; D04 l.21-49 vs l.61-99; D05 l.21-53 vs l.63-101; D06 l.21-39 vs
  l.51-85; D07 l.21-39 vs l.51-85); the table values are themselves rounded relative to the
  $0.1M statements (e.g., revenue, Adj. EBITDA, AFFO rows in the selected-information sections).
- CEO growth statements tied to table rows: D02 l.47 "6.6%" (table l.87); D04 l.53 "double-digit
  growth in AFFO per Share, as adjusted" (l.93 10.3%); D05 l.55 "high-single-digit growth in AFFO
  per Share, as adjusted" (l.95 FY 8.0%); D07 l.41 "mid-single-digit AFFO per share growth,
  normalized for one-time DISH churn" (table l.79 shows 4.2% unnormalized; no normalized figure is
  printed).
- Capex narrative "approximately" totals vs table "total cash capital expenditures" (D02 l.135/l.91;
  D03 l.137/l.93; D04 l.143/l.97; D05 l.145 "approximately $1.7 billion" FY / l.99 1,721; D06
  l.119/l.83; D07 l.119/l.83).
- FX amounts appear three times per release: headline footnote, SoO "Other income (expense)" label,
  Nareit footnote (e.g., D03 l.109, l.487, l.763).
- Outlook narrative midpoint changes (D02 l.181, D03 l.181, D04 l.183, D06 l.155, D07 l.159) sit
  beside the outlook tables; the prior-edition tables in the bundle give the earlier ranges.

### Documents that cite, amend or respond to another document in the bundle

- No release cites another release by name or date. Later outlooks revise earlier ones by
  reference ("prior 2025 outlook", "prior 2026 outlook"). D02 l.139 (DE1 completed April 1, 2025)
  is followed up in D03 l.139; D02's South Africa Fiber sale is carried into D03-D07 footnotes; D04
  l.171 buyback programs are followed by D05 l.143 single "buyback program" with ~$1.6B remaining.
  D01's CoreSite acquisition expectations (close "by the end of 2021, or shortly thereafter")
  are not updated by any later document.

### Coverage summary and gaps

- All seven documents read in full, in chunks: D01 l.1-109; D02 l.1-824; D03 l.1-818; D04
  l.1-820; D05 l.1-920; D06 l.1-712; D07 l.1-716. No unread line ranges.
- Unresolvable gaps: 145 capture-gap markers (listed per document above), all inside financial
  tables; originals in `docs/` are identical captures. No visible figures for any balance sheet;
  revenue/expense rows of every statement of operations; segment revenue/opex/gross margin/
  operating-profit dollar rows; Tenant Billings bridge rows (colocations, escalations,
  cancellations etc.); non-TB revenue components (straight-line, pass-through, FX on other
  revenue) in actual-results tables; Adjusted EBITDA reconciling rows; Nareit FFO totals inside the
  reconciliations; total AFFO rows inside every Nareit/AFFO reconciliation (D02-D05 show only the
  "As Adjusted:" block - discontinued AFFO, continuing AFFO, interest-savings adjustment, as-adjusted
  AFFO and per Share; D06/D07 show no AFFO row at all; headline tables still give AFFO);
  EBITDA-to-AFFO reconciliations show only the per-Share/as-adjusted tail in D02-D05 and nothing in
  D06/D07; all segment gross-margin reconciliations. Net-income rows of the SoO: visible in D02/D03;
  NI, continuing, discontinued and NCI rows hidden in D04/D05 (NI attributable visible); NI, NCI and
  NI attributable rows all hidden in D06/D07 (only EPS visible); D07 also hides interest income/
  expense rows. Net income itself remains visible at the top of each cash-flow statement and
  Nareit reconciliation.
- A fresh full capture of D02-D07 would be needed to resolve any of the above; the extraction
  tool cannot recover it.
