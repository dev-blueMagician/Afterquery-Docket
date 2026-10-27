# aq-01937 - document map

Written once by `bundle-mapper` from `text/` (and `docs/` for flattened tables and scans).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

Line refs "Dnn Lx" are lines of `text/Dnn.txt`. The text adds a 2-line header and collapses some
blank lines, so `docs/` line numbers differ by a varying offset (D01 +2 throughout; D02 +1 to +17).
Text files carry no page markers (method text, `pages: null`); releases print their own page
numbers as bare lines ("1" ... "14").

## Bundle

- What it is: ten State Street Corporation (NYSE: STT) Form 8-K Exhibit 99.1 documents, Feb 2024 -
  Jul 2026: two investor presentations (D01 UBS conference deck, D04 Global Advisors strategic
  overview) and eight quarterly earnings releases (D02 3Q24, D03 4Q24, D05 1Q25, D06 2Q25,
  D07 3Q25, D08 4Q25, D09 1Q26, D10 2Q26).
- Documents: 10; D01-D10 from `text/manifest.json`; local ids equal task page Doc 1-Doc 10.
- Coverage ledger (all FULL, nothing remaining): D01 L1-L42; D02 L1-L446; D03 L1-L453; D04
  L1-L32; D05 L1-L435; D06 L1-L453; D07 L1-L398; D08 L1-L404; D09 L1-L423; D10 L1-L417.
- Gaps: no capture gaps (intake gap_characters 0; every text file read in full). Visual
  (flattened-chart) gaps, unresolved because the originals are themselves plain text: D01 L17
  servicing-wins product-mix percentages; D01 L23 expense-waterfall label pairing; D04 L13 "As a %
  of STT" series; D04 L15 industry AUM / 5-year CAGR bars; D04 L17 asset-class percentage pairing;
  D04 L19 partnership heading assignment and any partner logos. Referenced but not in any captured
  exhibit: the non-GAAP "Addendum" cited by every release. Not stated anywhere in the bundle:
  medium-term target values (D10 L26), the post-increase 3Q26 dividend amount (D10 L25), any
  full-year 2024/2025 income-statement totals, 1Q24/2Q24 servicing fee revenue wins.
- Extraction spot-checks: originals are plain-text captures (pages not applicable). For every
  document one table row, one footnote/endnote and the last printed page number (or last slide)
  were string-matched between `text/` and `docs/` (details in each Coverage line). Doubled "%"
  signs (D08) and zero-width-space lines (D09, D10) exist in the originals.
- Provenance: notes/intake.json schema 1, capture AQ-01937_2026-10-08_0303.txt sha256 e694687a...;
  all 10 documents incomplete=false, gap_characters 0, matches_capture true; manifest sha256 equal
  intake source_sha256 for D01-D10. No recovered-source history.

## D01 - UBS Financial Services Conference presentation (February 27, 2024)

- Source: docs/stt_ex991_2024-02-27.txt (32,877 chars); text/D01.txt L1-L42; slide numbers 1-17
  begin each paragraph (slide 10 is an empty line, L27).
- Written or submitted by: State Street (8-K Exhibit 99.1, "sttubsfinancialservicesc.htm", L4).
  Presenters L9: Ronald P. O'Hanley, Chairman and Chief Executive Officer; Eric Aboaf, Vice
  Chairman and Chief Financial Officer. Slide 11 "Fireside chat" (L29) names O'Hanley, Aboaf and
  Brennan Hawken (role not stated).
- Type, date, edition: conference slide deck, dated February 27, 2024 (L9).
- Period covered: FY2023 actuals and FY2024 projections; FY = full-year (calendar labels "2023",
  "FY2024", "4Q23"). Historical chart series 2020-2023 plus 2024E (L17).
- Entities and aliases: segments Investment Servicing (= Asset Services + Markets and Financing)
  and Investment Management (= Global Advisors) (L15); "Markets & Financing" (L13); State Street
  Alpha(R), Private Markets ("a subset of Alternatives", endnote 9 L33); CF Global Trading
  acquisition "Closed" (L19); Currenex, Fund Connect, FX Connect (L19); SPY = SPDR S&P 500 ETF
  Trust (L41); operations joint ventures in India (L25, L35, L37).
- Tables/charts (flattened):
  - L15 rankings: #2 Custodian globally(1), #1 ETF servicer(2), #1 FX provider to asset
    managers(3), #3 Agency securities lender(4), #4 Asset manager globally(5), #4 in US Defined
    Contribution(6); sources/as-of dates in endnotes 1-6 (L33; 5 and 6 are as of Dec 31, 2022).
  - L17 "Servicing fee rev. wins by product ($M)": 2020 $140, 2021 $253, 2022 $259, 2023 $301,
    2024E $350-400; segment shares (Middle Office / Alternatives / Back Office ex-Alts) appear as
    an unordered run "60% 62% 47% 29% 19% 35% 19% 18% ... 11% ... 43% 36% 21%" - year/segment
    mapping NOT recoverable from text (visual gap).
  - L23 FY2024 expense outlook waterfall (ex-notables, non-GAAP): FY2023 $8,963M; labels
    ~(5-6)% Productivity savings, ~0.5% Currency translation, ~1-2% Merit, ~1%, ~4-5% Incremental
    investments, Variable costs, "+~2.5%" FY2024E, "~$500M ~$400M ~1.7x vs. FY2023" - bar-to-label
    pairing ambiguous after flattening (visual gap).
  - L23 footnote (exact): "FY2023 non-GAAP expenses of $8,963M is FY2023 GAAP expenses of $9,583M
    excluding notable items of $(620)M consisting of the FDIC special assessment of $(387)M, net
    repositioning charges of $(203)M, other notable items (net) of $(45)M, and an accrual release
    in acquisition and restructuring costs of $15M."
- Lists: priorities 1-4 (L13); Asset Services 2024 outcomes 4 items (L17); Markets and Financing
  4 items (L19); Investment Management 4 targets (L21); FY2023 achievements 6 and FY2024 focus
  areas 6 (L25); endnotes 1-22 (L33) and 23-26 (L35, last list items); definitions (L41).
- Forecasts, guidance, deadlines (all FY2024 unless stated; footnote A L13/L15/L23 "Financial
  metrics presented as part of our outlook exclude notable items and are non-GAAP measures"):
  - L13 "Deliver full-year fee revenue growth of ~3-4%"; L15 "Projected ~3-4% YoY fee revenue
    growth and positive fee operating leverage in FY2024".
  - L17 servicing fee revenue wins $350-400M ("~$50-100M YoY increase ... in 2024"); revenue
    retention rate 97% (endnote 11 excludes a previously disclosed significant client transition
    of ETF assets; 2020-2023 average 97% vs 96% 2019-2022); Private Markets YoY servicing fee
    growth 15%+; reduce avg. Alpha implementation time ~2-3 months (endnote 10: historical
    ~24-36 months); "+6-8 new Alpha mandates targeted in 2024".
  - L19 client FX volumes +2-3%; FX revenue growth from new products +1-2% (endnote 14: "1-2%
    point", FX Sales and Trading only); Agency Lending market share "Top 2: +1 Position"; average
    loan balances ~+10% (endnote 16: FY2024 vs FY2023, excludes overdrafts).
  - L21 US Low-Cost ETF AUM market share to 5% (baseline 4.6% 4Q23, endnote 18); US DC AUM
    market share +0.5% (endnote 20: 6.0% as of Dec 31, 2022); Institutional MMF rank #8 -> #7;
    organic AUM growth >2% (endnote 22: FY2024 net new assets / total AUM at Dec 31, 2023).
  - L23 expenses ex-notables FY2024E (+~2.5% per waterfall label; see visual gap).
  - L25 FY2024: consolidate second operations JV in India (endnote 23: "expected to be completed
    in 2Q24"); reduce additional 5% legacy applications (endnote 24: ~2,000-application 2019
    baseline; ~40% total reduction expected by end of 2024); eliminate 10% bespoke processes
    (endnote 25: baseline Dec 31, 2023); >10 AI savings initiatives; span of control ~1:5 -> ~1:8;
    3-4% net IT vendor productivity savings.
- 2023 actuals stated: servicing fee revenue wins $301M, $270M to be installed at YE2023 (L17,
  endnote 8); 18 live Alpha clients YE2023; 7 new Alpha mandates in 2023; record ETF AUM $1.27T;
  SPY and Low-Cost ETF inflows $52B and $33B; Institutional AUM $2.39T YE2023; record Cash inflows
  $76B (prior record $42B FY2009, endnote 21); Cash AUM $467B YE2023; record 4Q23 total net inflows
  $103B (L21); 35% legacy applications rationalized; bespoke processes -7%; ~85% bank loan
  settlements automated; 4% net IT vendor savings (L25).
- Hedged claims: FLS L11/L37 (generic). Endnote 13 L33 "may be subject to completion of
  definitive agreements..." attaches to new servicing mandates incl. announced Alpha clients.
- Rounded prose beside exact figures: none within D01 beyond the $8,963M reconciliation.
- Operative definitions (L41 unless noted): "Fee operating leverage: Rate of growth of total fee
  revenue less the rate of growth of total expenses, relative to the successive prior year
  period, as applicable"; "Through-the-cycle: Approximately 3 years"; NII; YoY; non-GAAP/notable
  items and constant currency ("applying prior period weighted average foreign currency exchange
  rates to current period results") at L39; servicing fee revenue wins/backlog endnote 7 (L33).
- Amendments or contradictions: none internal.
- Coverage: FULL - L1-L42 read; original spot-check: docs line 21 "$8,963M is FY2023 GAAP
  expenses", line 25 slide "10" empty, line 33 endnotes 23-26 match text L23/L27/L35. Not
  applicable: pages, footnote-vs-page check. Visual gaps: L17 product-mix percentages, L23
  waterfall pairings.

## D02 - 3Q24 earnings news release (October 15, 2024)

- Source: docs/stt_ex991_2024-10-15.txt (46,375 chars; "a3q24earningspressrelease.htm"); text
  L1-L446; printed pages 1-14 (page numbers at L54, 81, 115, 179, 246, 288, 331, 342, 374, 388, 398,
  418, 432, 445).
- Written or submitted by: State Street Corporation, One Congress Street, Boston (L10-L16).
  Quotes Ron O'Hanley, Chairman and CEO (L27-L31). Contacts L52: Elizabeth Lynn (investor),
  Carolyn Cichon (media). Euromoney named as award giver (L65, L78).
- Type, date, edition: quarterly earnings news release, "Boston, MA... October 15, 2024" (L16).
  Call Tuesday October 15, 2024 12:00 p.m. ET (L377).
- Period covered: 3Q24 (quarter ended September 30, 2024; L220, L385); calendar quarters labelled
  "3Q24". Comparative columns: most tables 3Q24 | 2Q24 | 3Q23 (+% QoQ, % YoY); industry flows and
  AUM roll-forward 5 quarters 3Q24-3Q23. No YTD or full-year columns.
- Entities and aliases: segments called "Investment Servicing" (L60, L181) and "Investment
  Management" (L60, L204), but CEO says "Within Investment Services" (L29) and "Global Advisors"
  (L22, L29); "Markets & Financing" (L65); CRD = Charles River Development; FIX = The Charles River
  Network's FIX Network Service (CRN) (L410); SSGA FD (L386); SSC vs SSBT (State Street Bank and
  Trust) for LCR (L403).
- Headline (L18-L25): "RECORD EPS OF $2.26"; AUC/A wins $466B; "RECORD GLOBAL ADVISORS NET
  INFLOWS OF $100 BILLION"; revenue up 21%, up 9% ex-notables; fee revenue up 11%, up 7%
  ex-notables; NII up 16%; positive fee and total operating leverage; ROE of 12%.
- Tables (USD millions unless noted):
  - L34-L46 Financial highlights 3Q24/2Q24/3Q23: fee revenue 2,616/2,456/2,361 (7%, 11%); NII
    723/735/624; other income (80)/—/(294); total revenue 3,259/3,191/2,691; provision 26/10/—;
    total expenses 2,308/2,269/2,180; net income 730/711/422; diluted EPS $2.26/$2.15/$1.25;
    ROE 12.0/11.9/7.3%; pre-tax margin 28.4/28.6/19.0%; AUC/A ($B) 46,759/44,312/40,017; AUM ($B)
    4,732/4,369/3,672.
  - L94-L106 Notable items 3Q24/2Q24/3Q23: investment portfolio repositioning (81)/—/(294); gain
    on sale of an equity investment 66/—/—; revenue-related recovery 15/—/—; "Total notable items
    (pre-tax) $ — $ — $ (294)"; tax impact —/—/(79); EPS impact —/—/$(0.68). L108: $81M loss in
    Other income; $66M gain in Other fee revenue; $15M recovery from "a 2018 FX benchmark
    litigation resolution" in FX trading services.
  - L120-L153 Market data (indices, VIX 17.1/14.0/15.0, specials volumes, EUR 1.099, GBP 1.301);
    footnote (1) AUC $33,667B/$32,161B/$29,113B.
  - L158-L177 Industry flows ($B) 3Q24/2Q24/1Q24/4Q23/3Q23: N. America total 444/157/219/212/131;
    EMEA total 266/148/83/115/38. Footnote (2) 3Q24 N. America = July-August actuals plus
    Morningstar estimates for September 2024; (4) EMEA rolling June-August 2024.
  - L184-L202 AUC/A by product and asset class ($B; 3 columns).
  - L207-L224 3Q24 AUM roll-forward by product (Equity/Fixed-Income/Cash/Multi-Asset Class
    Solutions/Alternative Investments/Total): begin 2,759/583/483/349/195/4,369; total flows
    34/7/54/2/3/100; end Sep 30, 2024 2,977/623/543/375/214/4,732. Footnote (2): "AUM for passive
    alternative investments has been revised from prior presentations."
  - L226-L244 5-quarter AUM roll-forward ($B) 3Q24/2Q24/1Q24/4Q23/3Q23 (prior four marked (1)
    revised): total flows 100/(6)/(14)/95/10; cash fund 54/(4)/9/29/41; ETF 37/6/1/68/(1); LT
    institutional 9/(8)/(24)/(2)/(30); ending 4,732/4,369/4,299/4,102/3,672.
  - L250-L273 Revenue with % to one decimal: back office 1,167/1,146/1,138; middle office
    99/93/96; servicing fees 1,266/1,239/1,234 (2.2%, 2.6%); management fees 527/511/479 (3.1,
    10.0); FX trading 374/336/313 (11.3, 19.5); securities finance 116/108/103; front office
    software and data 146/152/130; lending related and other fees 62/62/58; software and
    processing fees 208/214/188; other fee revenue 125/48/44; total fee revenue (6.5%, 10.8%);
    NII (1.6)%/15.9%; total revenue ex-notables 3,259/3,191/2,985 (2.1%, 9.2%); NIM (FTE)
    1.07/1.13/1.12%.
  - L298-L305 Allowance for credit losses: begin 145/146/136; provision 26/10/—; charge-offs
    —/(11)/(2); end 171/145/134.
  - L311-L321 Expenses: comp 1,134/1,099/1,082; info systems 463/454/411; transaction processing
    255/250/241; occupancy 105/106/101; amortization of other intangible assets 56/60/60; other
    295/300/285; total 2,308/2,269/2,180 (1.7%, 5.9%); ETR 21.1/22.1/17.4%. No acquisition and
    restructuring line.
  - L347-L366 Capital (preliminary): Std CET1 11.6/11.2/11.0; Tier 1 13.9/13.3/12.7; total
    15.6/15.0/14.0; Adv CET1 12.5/12.0/12.2; Tier 1 leverage 5.5/5.3/5.8; SLR 6.4/6.3/6.3; LCR
    107/106/109%; SSBT LCR 129/134/120%. Standardized binding all periods.
- Forecasts/outlook: L31 "we remain focused on delivering full-year positive fee and total
  operating leverage". No numeric guidance in D02. L383: 3Q24 regulatory disclosure updates by "on
  or about November 9, 2024" (LCR "on or about November 14, 2024").
- Events/actions: 3Q24 repurchases $450M; total capital return $674M = $450M buybacks + $224M
  dividends ($0.76/share), ~100% of net income available to common (L111); Alpha: "2 new mandate
  wins in 3Q24, for a total of 5 mandate wins year-to-date" (L65); servicing fee revenue wins $84M;
  to be installed $288M and AUC/A $2.4T (L64-L65); front office ARR $356M up 19% (ARR 3Q23 $299M,
  2Q24 $345M, L400); India JVs "consolidated in 4Q23 and 2Q24" (footnote L329); 4% YoY headcount
  reduction pro-forma (L323); record Cash inflows $54B (L65).
- Rounded prose beside exact figures: highlights bullets L69-L74 (servicing +3%, mgmt +10%, FX
  +19%, sec finance +13%, S&P +11%) vs table L252-L263 (2.6, 10.0, 19.5, 12.6, 10.6); highlights
  fee revenue % QoQ "7 %" (L35) vs 6.5% (L263); $15M recovery "approximately 4% points" of FX
  growth (L279); AUC/A "$46.8 trillion", AUM "$4.7 trillion" (L60, L385).
- Definitions (L391-L416): servicing fee revenue wins/backlog (adds "may include anticipated
  servicing-related revenues associated with acquisitions or structured transactions", not in D01
  endnote 7); front office ARR (L396-L400); ROE (L405); "Operating leverage ... total revenue less
  ... total expenses, relative to the corresponding prior year period" (L407); "Fee operating
  leverage ... relative to the successive prior year period" (L408); NIM = FTE NII / average total
  interest-earning assets (L412); AUM boilerplate includes ~$83B SPDR products where SSGA FD is
  solely marketing agent (L386); Alternative Investments include SPDR Gold products where "we are
  not the investment manager but act as the marketing agent" (L222).
- Hedged claims: L394 mandates "may be subject to completion of definitive agreements...".
- Amendments or contradictions: L223/L243 revision of passive alternatives AUM in prior quarters.
- Coverage: FULL - L1-L446 read. Spot-check vs original: notable-items total row (docs L103),
  footnote "(2) AUM for passive alternative..." (docs L232, L253), page "14" (docs L462) match.
  The referenced "Addendum" (non-GAAP reconciliation) is not part of the captured exhibit.

## D03 - 4Q24 earnings news release (January 17, 2025)

- Source: docs/stt_ex991_2025-01-17.txt (47,888 chars; "a4q24earningspressrelease.htm"); text
  L1-L453; printed pages 1-15 (L58, 84, 114, 119, 183, 250, 291, 331, 348, 380, 394, 404, 424,
  439, 452).
- Written or submitted by: State Street Corporation (L10-L16); quotes Ron O'Hanley, Chairman and
  CEO (L26-L30); contacts Elizabeth Lynn, Carolyn Cichon (L56).
- Type, date, edition: quarterly earnings release, "Boston, MA... January 17, 2025" (L16); call
  Friday January 17, 2025, 11:00 a.m. ET, ID 30802 (L383).
- Period covered: 4Q24 (quarter ended December 31, 2024; L224). Columns: 4Q24 | 3Q24 | 4Q23 (+%
  QoQ, % YoY); flows/AUM roll-forward 4Q24-4Q23 (5 quarters). NO full-year 2024 columns anywhere.
- Entities and aliases: "Investment Servicing" (L64, L185), "Investment Management" (L64, L208),
  CEO "Within Investment Services ... At Global Advisors" (L28); "APAC Asset Owner" (L68).
- Headline (L18-L24): "FOURTH QUARTER 2024 EPS OF $2.46; $2.60 EXCLUDING NOTABLE ITEMS"; total
  revenue up 12%; fee revenue up 13%; NII up 10%; positive fee and total operating leverage;
  "PRE-TAX MARGIN OF 28%; 30% EX-NOTABLES"; "ROE OF 12.7%; 13.5% EX-NOTABLES".
- Results vs prior outlook (CEO): L26 2024 "positive fee and total operating leverage supported by
  record NII, and overall, exceeded the financial outlook we provided at the outset of 2024"; L28
  "we met our full-year Servicing fee revenue wins goal of $350-400 million, supported by a
  transformative mandate in the quarter"; "new AUC/A wins exceeded $1 trillion"; Global Advisors
  "record Management fees and $64 billion of quarterly net inflows". L30 "foundation and momentum
  for 2025". No numeric 2025 guidance in D03.
- Tables (USD millions unless noted):
  - L33-L50 highlights 4Q24/3Q24/4Q23: fee revenue 2,662/2,616/2,365 (2%, 13%); NII 749/723/678;
    other income 1/(80)/—; total revenue 3,412/3,259/3,043 (5, 12); provision 12/26/20; total
    expenses 2,440/2,308/2,822 (6, (14)); net income 783/730/210; EPS $2.46/$2.26/$0.55; ROE
    12.7/12.0/3.1%; pre-tax margin 28.1/28.4/6.6%; AUC/A ($B) 46,557/46,759/41,810; AUM ($B)
    4,715/4,732/4,102.
  - L93-L105 Notable items 4Q24/3Q24/4Q23: "Deferred compensation expense acceleration" (79)/—/—;
    "FDIC special assessment" 31/—/(387); "Repositioning charges and other notable items (net)"
    (10)/—/(233); total (58)/—/(620); tax (17)/—/(156); EPS (0.14)/—/(1.49). L107: $79M related
    to prior-period awards "to align State Street's deferred pay mix with peers"; $31M FDIC
    release in Other expenses. L108: 4Q24 (10) = $13M Occupancy + $12M Other charges less $15M
    Compensation release. Footnote (c) L112: 4Q23 $233M = $182M comp + $21M occupancy + $41M info
    systems + $4M other, less $15M Acquisition and restructuring benefit; 3Q24 "$0" = $81M loss
    less $66M gain less $15M recovery (D02 listed these as three separate rows).
  - L124-L157 Market data; AUC footnote $33,805B/$33,667B/$30,615B.
  - L162-L181 Industry flows ($B) 4Q24/3Q24/2Q24/1Q24/4Q23: N. America total 651/401/157/219/212;
    EMEA total 244/255/148/83/115. Footnote (2) 4Q24 N. America Oct-Nov actuals + December
    estimates; (4) EMEA rolling Sep-Nov 2024.
  - L188-L206 AUC/A by product/asset class (3 columns; 3Q24 equals D02).
  - L211-L228 4Q24 AUM roll-forward by product: begin 2,977/623/543/375/214/4,732; LT
    institutional 2/13/—/10/1/26; ETF 54/11/—/—/—/65; cash (27); total flows 56/24/(27)/10/1/64;
    end Dec 31, 2024 3,007/616/518/374/200/4,715; footnote (2) passive alternatives revised.
  - L230-L248 5-quarter AUM ($B) 4Q24/3Q24/2Q24/1Q24/4Q23: total flows 64/100/(6)/(14)/95; cash
    (27)/54/(4)/9/29; ETF 65/37/6/1/68; ending 4,715/4,732/4,369/4,299/4,102 (same as D02 for
    overlapping quarters).
  - L254-L274 Revenue: back office 1,184/1,167/1,128; middle office 99/99/84; servicing fees
    1,283/1,266/1,212 (1.3%, 5.9%); management fees 576/527/479 (9.3, 20.3); FX trading 360/374/307
    ((3.7), 17.3); securities finance 118/116/97 (1.7, 21.6); front office software and data
    197/146/179; lending related 62/62/58; software and processing 259/208/237 (24.5, 9.3); other
    fee revenue 66/125/33; total fee revenue (1.8%, 12.6%); NII (3.6%, 10.5%); total revenue
    (4.7%, 12.1%); NIM 1.07/1.07/1.16%. No "total revenue excluding notable items" row.
  - L299-L306 Allowance: begin 171/145/134; provision 12/26/20; charge-offs —/—/(4); end
    183/171/150.
  - L312-L325 Expenses: comp 1,212/1,134/1,247; info systems 480/463/473; transaction processing
    245/255/242; occupancy 123/105/128; "Acquisition and restructuring costs" —/—/(15) (row absent
    in D02); amortization 54/56/59; other 326/295/688; total 2,440/2,308/2,822 (5.7%, (13.5)%);
    "Total expenses, excluding notable items" 2,382/2,308/2,202 (3.2%, 8.2%); ETR
    18.4/21.1/(4.4)%.
  - L353-L372 Capital: Std CET1 10.9/11.6/11.6; Tier 1 13.2/13.9/13.4; total 14.8/15.6/15.2; Adv
    CET1 12.0/12.5/12.1; Tier 1 leverage 5.2/5.5/5.5; SLR 6.2/6.4/6.2; LCR 107/107/106; SSBT LCR
    134/129/122 (3Q24 column equals D02).
- Events/actions: 4Q24 servicing fee revenue wins $154M "mainly driven by a large, multiregional
  win with an APAC Asset Owner"; AUC/A wins $1.1 trillion (L68); to be installed $346M and AUC/A
  $3.0T (L70); "State Street Alpha: Reported 2 new mandate wins in 4Q24, for a total of 7 mandate
  wins in 2024" (L70); ARR up 19% ($315M 4Q23, $356M 3Q24, $375M 4Q24, L406); 4Q24 capital return
  $770M = $550M repurchases + $220M dividends ($0.76/share), 106% of net income available to
  common (L117); disclosure updates "on or about March 1, 2025" (L389).
- Rounded prose beside exact figures: highlight bullets L74-L79 (servicing +6%, mgmt +20%, FX
  +17%, sec finance +22%, S&P +9%) vs table 5.9/20.3/17.3/21.6/9.3; headline "PRE-TAX MARGIN OF
  28%" vs 28.1 (L46); "exceeded $1 trillion" (L28) vs "$1.1 trillion" (L68); highlights provision
  "(54)" vs (53.8) (L303); expense bullets L87-L89 vs table L313-L322.
- Definitions changed vs D02: L414 "Fee operating leverage ... relative to the corresponding prior
  year period" (D01 L41, D02 L408 say "successive"); L399 restores "No servicing fees are
  recognized until..."; L400 adds "or other conditions", "servicing assets/fees", "publicly
  disclose or anonymously disclose"; L401 adds "Levels of AUC/A ... are always presented as of the
  end of the relevant period". L392 AUM includes ~$82B SPDR products (SSGA FD marketing agent).
- Other notes: Other fee revenue +$33M YoY includes "absence of the impact of the Argentine peso
  devaluation in the prior year period" (L287); FLS cites 2023 Form 10-K (L450).
- Coverage: FULL - L1-L453 read. Spot-check vs original: notable-items row (docs L94), footnote
  (c) (docs L113), fee operating leverage definition (docs L427-L428), page "15" (docs L466) match.
  Referenced Addendum not in captured exhibit.

## D04 - State Street Global Advisors strategic overview presentation (March 5, 2025)

- Source: docs/stt_ex991_2025-03-05.txt (15,722 chars; "ssgarbccapitalmarketsglo.htm", L4);
  text L1-L32; slides 1-12 each one paragraph (offset +2 vs docs).
- Written or submitted by: State Street (8-K Exhibit 99.1). Presenters L9: Yie-Hsin Hung, "Chief
  Executive Officer, State Street Global Advisors"; Mark Keating, "Interim Chief Financial
  Officer, State Street Corporation". Slide 8 (L23) names Hung, Keating and Gerard Cassidy (role
  not stated). Event/conference name not stated in the text (only the file name).
- Type, date, edition: segment strategy slide deck dated March 5, 2025 (L9).
- Period covered: calendar 2022-2024 actuals (slide 3), 2024 AUM by focus area, combined 2023 &
  2024 net new assets (slide 5); industry estimates 2023-2028 (McKinsey, endnote 8).
- Entities and aliases: SSGA = State Street Global Advisors (L31) = "Global Advisors"; franchises
  named "Global Advisors", "Global Markets", "Investment Services" and "One State Street" (L11);
  State Street Global Markets securities lending program (L11); McKinsey Global Growth Cube,
  Pensions & Investments, Bloomberg, iMoneyNet as sources (L27).
- Tables/charts (flattened):
  - L11 rankings: "#4 global asset manager with $4.7T in AUM"(1), "#3 global index manager"(2),
    "#3 ETF manager worldwide with $1.6T in AUM"(3), "#4 U.S. retirement manager"(4) (endnote 4:
    U.S. DC + U.S. DB AUM), "Top 10 institutional money market provider"(5) (exact rank not
    printed). Synergies: "State Street Alpha client"; "Manages ~$400B of State Street-sourced
    cash balances"; "~$1.4T of SSGA funds participate in State Street Global Markets securities
    lending program".
  - L13 slide 3 (SSGA, $): Total revenue ($B) 2022 $2.0, 2023 $2.1, 2024 $2.3, "+9%" CAGR; AUM
    ($T) $3.5, $4.1, $4.7, "+16%" CAGR; Pre-tax margin 29.7%, 25.9%, 29.4% with "(3.8)% pts" and
    "+3.5% pts"; Net new assets ($B) $(37), $117, $144; Organic growth "(0.9)% +3.4% +3.5%";
    "16% 18%17%" beside "As a % of STT" - which metric and year order not recoverable (visual
    gap).
  - L15 slide 4 "Key focus area by" category: ETFs ~$1.6T +24%; Non-U.S. ~$1.2T +16%; Wealth ~$1.2T
    +23%; Fixed income ~$600B +5% (SSGA 2024 AUM and 2022-2024 CAGR); industry AUM "~$11T ~$60T
    ~$52T ~$34T" and 5-year CAGR bars (Est. 2023-2028) - per-category pairing and bar values not
    recoverable (visual gap).
  - L17 slide 5 "2023 & 2024 organic net new assets by focus area": Region 36%/64% (Non-U.S./
    Americas); channel 54%/46% (Wealth/Institutional); asset class "18% 20% 21% 41%" with labels
    "Solutions/Other Equity Fixed income Cash" (pairing ambiguous); product 25%/75% (Other/ETFs);
    callouts "$47B Fixed income", "$197B 72% Wealth & 28% Institutional", "$93B Non-U.S.", "$141B
    Wealth". Endnote 10 (L27): NNA 2023 $117B and 2024 $144B.
- Lists: slide 6 (L19) partnership areas, two headings ("New product partnerships", "Strategic
  wealth partnerships") then 8 items in one run: Private Markets, Digital Assets, Global Defined
  Contribution, U.S. Wealth, Liquid Alternatives, Personalized Retirement Income, Australian
  Wealth, European Wealth - item-to-heading assignment and any partner names/logos not in text
  (visual gap). Endnotes 1-11 (L27).
- Forecasts/targets: none numeric for SSGA; McKinsey 5-year industry CAGR estimates 2023-2028
  (values not in text). L27: P&I 2024 rankings "will not be available until Summer 2025".
- Rounded prose: slide 3 rounded $B/$T vs release tables (e.g. 2024 AUM $4.7T vs D03 L224 4,715;
  2023 AUM $4.1T vs D03 L245 4Q23 4,102).
- Operative definitions (L31): "Net new assets: Inflows net of outflows, excluding market/foreign
  exchange impact"; "Organic growth: Net new assets divided by prior period assets under
  management"; "Pre-tax margin: Income before income tax expense divided by total revenue";
  CAGR; FY. Endnote 11: "Higher revenue, AUM growth and pre-tax margin expansion represents 2024
  compared to 2023". Endnote 7 defines McKinsey Non-U.S. (98% of global AUM ex-U.S.), Fixed
  income, Wealth, ETFs; endnote 9 Non-U.S. = Europe/Middle East/Africa and Asia/Pacific.
- Hedged claims: FLS L29 only; cites "2024 Annual Report on Form 10-K".
- Amendments or contradictions: none internal.
- Coverage: FULL - L1-L32 read. Spot-check vs original: docs L11 "$(37) $117 $144", L21 slide 8,
  L25 endnote 10 match. Visual gaps: slide 3 "As a % of STT" series, slide 4 industry bars,
  slide 5 asset-class pairing, slide 6 partner layout.

## D05 - 1Q25 earnings news release (April 17, 2025)

- Source: docs/stt_ex991_2025-04-17.txt (47,081 chars; "a1q25earningspressrelease.htm"); text
  L1-L435; printed pages 1-13 (L58, 86, 113, 177, 243, 284, 329, 364, 378, 387, 407, 422, 434).
- Written or submitted by: State Street Corporation (L10-L16); quotes Ron O'Hanley, Chairman and
  CEO (L26-L30); contacts Elizabeth Lynn, Carolyn Cichon (L56).
- Type, date, edition: quarterly earnings release, "Boston, MA... April 17, 2025" (L16); call
  Thursday April 17, 2025 11:00 a.m. ET, (805) 309-0220, passcode 5051317# (L367; new dial-in).
- Period covered: 1Q25 (quarter ended March 31, 2025; L218). Columns 1Q25 | 4Q24 | 1Q24 (+% QoQ,
  % YoY); flows/AUM roll-forward 1Q25-1Q24. No full-year columns.
- Headline (L18-L24): "FIRST QUARTER 2025 EPS OF $2.04"; total revenue up 5%; fee revenue up 6%;
  servicing fees up 4%; management fees up 10%; front office software and data up 10%; "EXPENSES
  DOWN 3%; UP 3% EX-NOTABLES"; positive fee and total operating leverage; "EPS OF $2.04, INCREASED
  49%; UP 21% EX-NOTABLES".
- Outlook/prose: CEO L26 "solid start to the year"; L28 "geopolitical and government policy
  uncertainty around trade, deficits, tax, and deregulation"; L30 "prepared for a wide range of
  scenarios". No numeric guidance.
- Tables (USD millions unless noted):
  - L33-L50 highlights 1Q25/4Q24/1Q24: fee revenue 2,570/2,662/2,422 ((3)%, 6%); NII 714/749/716;
    total revenue 3,284/3,412/3,138; provision 12/12/27; total expenses 2,450/2,440/2,513 (0,
    (3)); net income 644/783/463; EPS $2.04/$2.46/$1.37; ROE 10.6/12.7/7.7%; pre-tax margin
    25.0/28.1/19.1%; AUC/A ($B) 46,733/46,557/43,912; AUM ($B) 4,665/4,715/4,299. First release
    in bundle printing 1Q24 income-statement figures.
  - L94-L102 Notable items 1Q25/4Q24/1Q24: deferred comp acceleration —/(79)/—; "FDIC special
    assessment" —/31/(130); repositioning and other (net) —/(10)/—; total —/(58)/(130); tax
    —/(17)/(31); EPS —/(0.14)/(0.32). 1Q25 has no notable items. Footnotes L108-L111: 1Q24 FDIC
    $130M in Other expenses; 1Q25 Other expenses $276M vs 1Q24 adjusted $288M (down 4%); L327
    4Q24 adjusted Other expenses $345M (FDIC $31M reduction, $12M operating model charges).
  - L118-L152 Market data (new footnote (1) "Historical financial information may not be
    indicative of future financial information"); AUC footnote $33,837B/$33,805B/$32,159B; 4Q24
    column equals D03.
  - L156-L175 Industry flows ($B) 1Q25/4Q24/3Q24/2Q24/1Q24: N. America total 221/673/401/157/219
    (MM 79/376/230/62/31); EMEA total 260/265/255/148/83. Row label now "Long-term Funds".
  - L182-L200 AUC/A by product/asset class: collective funds 15,430/15,266/14,694; mutual funds
    12,143/12,301/11,552; pension 9,377/9,386/8,800; insurance and other 9,783/9,604/8,866;
    equities 27,508/27,535/25,909; fixed-income 11,900/11,933/11,368; short-term 7,325/7,089/6,635.
  - L205-L221 1Q25 AUM roll-forward by product: begin 3,007/616/518/374/200/4,715; LT
    institutional (21)/(7)/—/13/—/(15); ETF (16)/9/—/—/8/1; cash 1; total flows
    (37)/2/1/13/8/(13); market (84)/8/(2)/(1)/14/(65); FX 15/7/1/4/1/28; end Mar 31, 2025
    2,901/633/518/390/223/4,665. No "revised" footnote on this table.
  - L223-L241 5-quarter AUM ($B) 1Q25/4Q24/3Q24/2Q24/1Q24 (3Q24-1Q24 marked (1) revised): total
    flows (13)/64/100/(6)/(14); ending 4,665/4,715/4,732/4,369/4,299.
  - L247-L265 Revenue: "Servicing fees" 1,275/1,283/1,228 (no back office / middle office rows,
    unlike D02 L252-L254 and D03 L256-L258); management fees 562/576/510 (10.2%); FX trading
    362/360/331 (9.4); securities finance 114/118/96 (18.8); front office software and data
    158/197/144 (9.7); lending related 67/62/63; software and processing 225/259/207 (8.7);
    other fee revenue 32/66/50 ((36.0)); total fee revenue (3.5)%/6.1%; NII (4.7)%/(0.3)%; total
    revenue 3,284/3,412/3,138 ((3.8)%, 4.7%); NIM 1.00/1.07/1.13%.
  - L288-L295 Allowance: begin 183/171/150; provision 12/12/27; charge-offs (9)/—/(31); end
    186/183/146.
  - L300-L312 Expenses: comp 1,262/1,212/1,252; info systems 497/480/432 (15.0%); transaction
    processing 258/245/248; occupancy 103/123/103; amortization 54/54/60; other 276/326/418
    ((34.0)); total 2,450/2,440/2,513 (0.4%, (2.5)%); ex-notables 2,450/2,382/2,383 (2.9%, 2.8%);
    ETR 21.7/18.4/22.5%. No acquisition and restructuring row.
  - L337-L356 Capital: Std CET1 11.0/10.9/11.1; Tier 1 13.8/13.2/13.2; total 15.3/14.8/14.9; Adv
    CET1 12.5/12.0/11.7; Tier 1 leverage 5.5/5.2/5.4; SLR 6.5/6.2/6.5; LCR 106/107/107; SSBT LCR
    139/134/130 (4Q24 column equals D03).
- Events/actions: servicing fee revenue wins $55M (majority back office); AUC/A wins $182B, ~$86B
  "driven by State Street Alpha" (L68-L69); to be installed $356M and AUC/A $3.1T (L70); "State
  Street Alpha: Reported 1 new mandate win in 1Q25" (L70); ARR "increased approximately 15%"
  (L71) with ARR $326M 1Q24, $375M 4Q24, $373M 1Q25 (L389; 373/326 computes to 14.4%); Global
  Advisors "key partnerships and product launches", "market share gains in U.S. Low Cost ETF
  suite" (L71, no names); 1Q25 capital return $320M = $100M repurchases + $220M dividends
  ($0.76/share) (L105); disclosure updates "on or about May 10, 2025" and May 15 for LCR (L373).
- Rounded prose beside exact figures: headline/bullets (servicing +4%, mgmt +10%, FX +9%, sec
  finance +19%, S&P +9%, other -36%, expenses down 3%/up 3% ex-notables) vs table 3.8, 10.2, 9.4,
  18.8, 8.7, (36.0), (2.5), 2.8; ARR "approximately 15%" vs L389 values; highlights total
  expenses % QoQ "0" vs 0.4.
- Definitions: L383 adds "(i.e., "to be installed")" and "Both AUC/A and servicing fee revenue,
  when presented on a "backlog" or "to be installed" basis, are presented as of period-end"; L385
  drops "Consistent with past practice,"; L397 fee operating leverage "corresponding prior year
  period" (as D03); L376 AUM includes ~$106B SPDR products (SSGA FD marketing agent).
- Other notes: management fees down QoQ "driven by the absence of performance fees and day
  count" (L269); Other expenses ex-notables down 4% YoY "mainly due to the timing of foundation
  funding" (L323); FLS adds "changes in U.S. trade policy" (L414), cites 2024 Form 10-K (L432).
- Coverage: FULL - L1-L435 read. Spot-check vs original: notable row "FDIC special
  assessment(d)" (docs L99), footnote (b) (docs L109, L346), ARR sentence (docs L409), page "13"
  (docs L454) match. Referenced Addendum not in captured exhibit.

## D06 - 2Q25 earnings news release (July 15, 2025)

- Source: docs/stt_ex991_2025-07-15.txt (54,641 chars; "a2q25earningspressrelease.htm"); text
  L1-L453; printed pages 1-15 (L54, 79, 114, 119, 182, 246, 286, 309, 345, 382, 396, 405, 425,
  439, 452).
- Written or submitted by: State Street Corporation (L10-L16); quotes Ron O'Hanley (L28-L30);
  contacts Lynn, Cichon (L52).
- Type, date, edition: quarterly earnings release, "Boston, MA... July 15, 2025" (L16); call
  Tuesday July 15, 2025 12:00 p.m. ET, passcode 1408453# (L385).
- Period covered: 2Q25 (quarter ended June 30, 2025; L223). Columns 2Q25 | 1Q25 | 2Q24 (+% QoQ,
  % YoY); flows/AUM 2Q25-2Q24. No YTD/full-year columns. Note (a) L50: percentages "reflect
  year-over-year 2Q comparisons"; AUC/A, AUM "as of quarter end".
- Entities and aliases: RENAMING - CEO L29 "surpassed $5 trillion in AUM at State Street
  Investment Management"; L394 "SSGA FD and State Street Investment Management are affiliated"
  (D05 L376: "...and State Street Global Advisors are affiliated"); tables still "Investment
  Servicing AUC/A" / "Investment Management AUM" (L60, L184, L207); "Markets: Record quarterly FX
  trading volumes, up 17%" (L66); "Investment Services" (L29).
- Headline (L18-L26): "SECOND QUARTER 2025 EPS OF $2.17; $2.53 EXCLUDING NOTABLE ITEMS"; "RECORD
  $49 TRILLION OF AUC/A AND RECORD $5 TRILLION OF AUM"; AUC/A wins $1.1T; IM net inflows $82B;
  "TOTAL OPERATING LEVERAGE (341) BPS; 241 BPS, EX-NOTABLES"; "FEE OPERATING LEVERAGE (75) BPS;
  526 BPS, EX-NOTABLES"; "PRE-TAX MARGIN OF 26%; 30%, EX-NOTABLES" (first release stating
  operating leverage in bps).
- Outlook/prose: L28 fee revenue "up 11% ... and up 12%, excluding notable items"; L29 "sixth
  straight quarter of positive year-over-year total operating leverage, excluding notable items",
  "near-record sales in Investment Services", "record FX trading client volumes"; L30 "results of
  the Federal Reserve's stress test reaffirm our financial strength", "planned 11% increase in our
  per share quarterly common stock dividend", "we expect this momentum will continue". L117: "In
  July 2025, State Street announced a planned 11% increase to its quarterly common stock dividend
  to $0.84 per share in 3Q25, subject to approval by the Board of Directors".
- Tables (USD millions unless noted):
  - L33-L49 highlights 2Q25/1Q25/2Q24: fee revenue 2,719/2,570/2,456 (6%, 11%); NII 729/714/735;
    total revenue 3,448/3,284/3,191 (5, 8); provision 30/12/10; total expenses 2,529/2,450/2,269
    (3, 11); net income 693/644/711; EPS $2.17/$2.04/$2.15; ROE 10.8/10.6/11.9%; pre-tax margin
    25.8/25.0/28.6%; AUC/A ($B) 49,000/46,733/44,312; AUM ($B) 5,117/4,665/4,369. No "Other
    income" row (present D02-D05).
  - L88-L102 Notable items 2Q25/1Q25/2Q24: "Repositioning charge" (100)/—/—; "Client rescoping"
    "Revenue impact" (24) and "Expense impact" (18); "Other notable items" 4; total (138)/—/—; tax
    (35); EPS (0.36). L104-L107: $100M in comp "primarily from workforce rationalization"; $24M
    "Alpha-related client rescoping" in Front office software and data (Professional services);
    $18M in Information systems and communications; other $4M = $3M FX benchmark litigation
    recovery (2018) + $1M release of prior-period notable item in Other expenses.
  - Adjusted-line footnotes (L76-L77, L110-L112, repeated L305-L307, L341-L343): FX $431M ->
    adjusted $428M (+27% vs $336M, +18% vs $362M); software and processing $230M -> $254M (+19%,
    +13%); front office software and data $169M -> $193M (+27% vs $152M, +22% vs $158M); comp
    $1,280M -> $1,180M (+7% vs $1,099M, -6% vs $1,262M); info systems $523M -> $505M (+11%, +2%);
    other $305M -> $306M (+2% vs $300M, +11% vs $276M).
  - L124-L157 Market data: indices, VIX 23.6/18.5/14.0, EUR 1.135, GBP 1.336; AUC $35,548B/
    $33,837B/$32,161B. "Specials Volumes" rows dropped (present D02-D05).
  - L161-L180 Industry flows ($B) 2Q25/1Q25/4Q24/3Q24/2Q24: N. America total 54/243/673/401/157
    (MM (14)/100/376/230/62); EMEA total 183/224/265/255/148.
  - L187-L205 AUC/A: collective funds 16,728/15,430/14,573; mutual 12,641/12,143/11,645; pension
    9,679/9,377/8,916; insurance 9,952/9,783/9,178; equities 29,311/27,508/26,291; fixed-income
    12,122/11,900/11,303; short-term 7,567/7,325/6,718.
  - L210-L226 2Q25 AUM roll-forward by product: begin 2,901/633/518/390/223/4,665; LT
    institutional 6/48/—/25/(11)/68; ETF 8/3/—/—/4/15; "Cash" (row renamed from "Cash fund")
    (1); total flows 14/51/(1)/25/(7)/82; market 273/7/6/27/5/318; FX 30/9/2/7/4/52; end June 30,
    2025 3,218/700/525/449/225/5,117.
  - L228-L244 5-quarter AUM 2Q25/1Q25/4Q24/3Q24(1)/2Q24(1): total flows 82/(13)/64/100/(6);
    ending 5,117/4,665/4,715/4,732/4,369.
  - L250-L271 Revenue: servicing fees 1,304/1,275/1,239 (2.3%, 5.2%); management fees 562/562/511
    (—, 10.0); FX trading 431/362/336 (19.1, 28.3); securities finance 126/114/108 (10.5, 16.7);
    front office software and data 169/158/152; lending related 61/67/62; software and processing
    230/225/214 (2.2, 7.5); other fee revenue 66/32/48; total fee revenue (5.8%, 10.7%); NII
    729/714/735 (2.1%, (0.8)%); total revenue (5.0%, 8.1%); "Total revenue, excluding notable
    items" 3,469/3,284/3,191 (5.6%, 8.7%); NIM 0.96/1.00/1.13%. No "Other income" row.
  - L294-L301 Allowance: begin 186/183/146; provision 30/12/10; charge-offs (24)/(9)/(11); end
    192/186/145.
  - L313-L325 Expenses: comp 1,280/1,262/1,099 (16.5% YoY); info systems 523/497/454; transaction
    processing 260/258/250; occupancy 105/103/106; amortization 56/54/60; other 305/276/300;
    total 2,529/2,450/2,269 (3.2%, 11.5%); ex-notables 2,412/2,450/2,269 ((1.6)%, 6.3%); ETR
    22.0/21.7/22.1%; L348 ETR ex-notables 22.5%.
  - L353-L372 Capital: Std CET1 10.7/11.0/11.2; Tier 1 13.3/13.8/13.3; total 14.8/15.3/15.0; Adv
    CET1 12.5/12.6/12.0 (1Q25 printed 12.5 in D05 L345); Adv Tier 1 15.5/15.7/14.2; Tier 1
    leverage 5.3/5.5/5.3; SLR 6.3/6.5/6.3; LCR 107/106/106; SSBT LCR 136/139/134.
- Events/actions: servicing fee revenue wins $145M "primarily related to back office"; AUC/A wins
  $1.1T, ~$380B "driven by State Street Alpha" (L64); to be installed $444M and AUC/A $4.0T (L65);
  "State Street Alpha: Reported 2 new mandates in 2Q25; 3 Alpha clients went live in 2Q25,
  resulting in a total of 28 live clients to-date" (L66); ARR ~10% ($345M 2Q24, $373M 1Q25, $379M
  2Q25, L407); 2Q25 capital return $517M = $300M repurchases + $217M dividends ($0.76) (L117);
  employees "approximately 52,000" (L393; 53,000 in D02-D05); SPDR marketing-agent AUM ~$116B
  (L394); disclosure updates "on or about August 9, 2025" / August 14 (L391).
- Rounded prose beside exact figures: headline pre-tax margin 26% vs 25.8; bullets (servicing +5%,
  FX +28%, sec finance +17%, S&P +7%, total expenses +11%, comp +16%) vs table 5.2, 28.3, 16.7,
  7.5, 11.5, 16.5; "$49 TRILLION" vs 49,000; "$5 TRILLION" vs 5,117.
- Definitions: L415 fee operating leverage "corresponding prior year period"; L401-L403 same as
  D05. FLS L432 adds "potential for retaliatory actions by governments"; L435 adds "timing of new
  business onboarding"; cites 2024 Form 10-K (L450).
- Coverage: FULL - L1-L453 read. Spot-check vs original: notable row "Expense impact" (docs L98),
  footnote (d) (docs L323), Advanced CET1 row "12.5 12.6 12.0" (docs L381; D05 docs L364 "12.5
  12.0 11.7"), affiliate sentence (docs L415), page "15" (docs L473) match. Addendum not captured.

## D07 - 3Q25 earnings news release (October 17, 2025)

- Source: docs/stt_ex991_2025-10-17.txt (49,769 chars; "a3q25earningspressrelease.htm"); text
  L1-L398; printed pages 1-13 (L66, 96, 133, 195, 237, 260, 295, 330, 344, 352, 370, 384, 397).
- Written or submitted by: State Street Corporation (L9-L12); quotes "RON O'HANLEY CHAIRMAN AND
  CHIEF EXECUTIVE OFFICER" (L19-L27). Contacts L64: Elizabeth Lynn (investor), Mark LaVoie (media;
  Carolyn Cichon in D02-D06). Apex Fintech Solutions named as partner (L26, L79); Euromoney (L79).
- Type, date, edition: quarterly earnings release dated "October 17, 2025" (L13; new front-page
  layout with KPI tiles); call Friday October 17, 2025 11:00 a.m. ET, passcode 2389583# (L333).
- Period covered: 3Q25 (quarter ended September 30, 2025; L174). Columns 3Q25 | 2Q25 | 3Q24;
  AUM roll-forward 3Q25-3Q24. No YTD/full-year columns.
- Headline/tiles (L15-L39): "THIRD QUARTER 2025 EPS OF $2.78"; "$51.7T RECORD AUC/A"; "$5.4T
  RECORD AUM"; "$3.5B TOTAL REVENUE, up 9% YoY"; "332BPS TOTAL OPERATING LEVERAGE"; "31.1%
  PRE-TAX MARGIN"; "13.4% ROE"; "20.9% ROTCE(a)" (ROTCE first appears; non-GAAP per L63).
- Outlook/prose (CEO): L25 "seventh consecutive quarter of positive operating leverage, excluding
  notable items"; L26 "recently announced partnership with Apex Fintech Solutions" (Wealth
  Services strategy), "record quarter of Management fee revenue", Investment Management
  "launching 39 new products"; L27 returned $637M; "As previously announced, we were pleased to
  increase State Street's quarterly per share common stock dividend by 11% to $0.84"; "position us
  well to sustain momentum". No numeric guidance.
- Tables (USD millions unless noted):
  - L43-L62 highlights 3Q25/2Q25/3Q24: fee revenue 2,829/2,719/2,616 (4%, 8%); NII 715/729/723;
    other income 1/—/(80) (row restored); total revenue 3,545/3,448/3,259 (3, 9); provision
    9/30/26; total expenses 2,434/2,529/2,308 ((4), 5); net income 861/693/730; EPS
    $2.78/$2.17/$2.26 (28%, 23%); ROE 13.4/10.8/12.0%; pre-tax margin 31.1/25.8/28.4%; AUC/A ($B)
    51,664/49,000/46,759; AUM ($B) 5,446/5,117/4,732.
  - L109-L123 Notable items 3Q25/2Q25/3Q24: repositioning charge —/(100)/—; client rescoping
    revenue impact —/(24)/—, expense impact —/(18)/—; "Other notable items (net)" —/4/—; total
    —/(138)/—; EPS —/(0.36)/—. 3Q25 has none. Footnote (d) L131 nets 3Q24 $81M loss / $66M gain /
    $15M recovery to $0 under this row name (D03 used "Repositioning charges and other notable
    items (net)").
  - Adjusted-figure footnotes: L93/L255 3Q24 FX $374M less $15M = $359M (3Q25 $416M +16%); 2Q25
    adjusted FX $428M (3Q25 -3%); L94/L258 3Q24 Other fee revenue $125M less $66M = $59M (3Q25
    $79M, +$20M); L256 2Q25 adjusted software and processing $254M (3Q25 $227M, -11%); L257 2Q25
    adjusted front office $193M (3Q25 $167M, -13%); L291-L293 2Q25 adjusted comp $1,180M, info
    systems $505M, other $306M.
  - NO "MARKET DATA" or "INDUSTRY FLOW DATA" tables (present D02-D06); Morningstar notes also gone.
  - L138-L156 AUC/A: collective funds 17,795/16,728/15,253; mutual 13,209/12,641/12,223; pension
    10,321/9,679/9,339; insurance 10,339/9,952/9,944; equities 31,124/29,311/27,715; fixed-income
    12,874/12,122/12,027; short-term 7,666/7,567/7,017.
  - L161-L177 3Q25 AUM roll-forward by product: begin 3,218/700/525/449/225/5,117; LT
    institutional (21)/12/—/6/(18)/(21); ETF 26/1/—/—/10/37; cash 10; total flows
    5/13/10/6/(8)/26; market 244/10/5/24/27/310; FX (2)/(3)/—/(2)/—/(7); end Sep 30, 2025
    3,465/720/540/477/244/5,446.
  - L179-L193 5-quarter AUM 3Q25/2Q25/1Q25/4Q24/3Q24: total flows 26/82/(13)/64/100; ending
    5,446/5,117/4,665/4,715/4,732. "Revised" footnote no longer attached to 3Q24.
  - L199-L221 Revenue: servicing fees 1,357/1,304/1,266 (4.1%, 7.2%); management fees
    612/562/527 (8.9, 16.1); FX trading 416/431/374 ((3.5), 11.2); securities finance 138/126/116
    (9.5, 19.0); front office software and data 167/169/146 ((1.2), 14.4); lending related
    60/61/62; software and processing 227/230/208 ((1.3), 9.1); other fee revenue 79/66/125; total
    fee revenue (4.0%, 8.1%); NII (1.9)%/(1.1)%; other income 1/—/(80); total revenue (2.8%,
    8.8%); ex-notables 3,545/3,469/3,259 (2.2%, 8.8%); NIM 0.96/0.96/1.07% (change in "bps").
  - L245-L252 Allowance: begin 192/186/145; provision 9/30/26; charge-offs —/(24)/—; end
    201/192/171.
  - L264-L276 Expenses: comp 1,162/1,280/1,134; info systems 517/523/463; transaction processing
    276/260/255; occupancy 106/105/105; amortization 56/56/56; other 317/305/295; total
    2,434/2,529/2,308 ((3.8)%, 5.5%); ex-notables 2,434/2,412/2,308 (0.9%, 5.5%); ETR
    21.9/22.0/21.1%.
  - L303-L322 Capital: Std CET1 11.3/10.7/11.6; Tier 1 13.9/13.3/13.9; total 15.5/14.8/15.6; Adv
    CET1 13.1/12.5/12.5; Adv Tier 1 16.2/15.5/15.0; total 17.8/17.0/16.6; Tier 1 leverage
    5.6/5.3/5.5; SLR 6.4/6.3/6.4; LCR 106/107/107; SSBT LCR 142/136/129.
- Events/actions: servicing fee revenue wins $47M "primarily driven by back office, including a
  strong contribution from private markets"; AUC/A wins $361B (L76); to be installed $401M and
  AUC/A $3.6T (L77); "State Street Alpha: 1 new mandate win and 1 go-live in 3Q25, with 4 mandate
  wins year-to-date" (L78; no live-client total printed); Apex partnership "to deliver a
  differentiated, fully digital, globally scalable, custody and clearing solution for wealth
  advisors and self-directed wealth platforms" (L79); ARR ~13% ($356M 3Q24, $379M 2Q25, $402M
  3Q25, L356); "Winner of 8 categories in the Euromoney 2025 FX Awards" (L79); 3Q25 capital
  return $637M = $400M repurchases + $237M dividends ($0.84/share) (L126); SPDR marketing-agent
  AUM ~$145B, ~52,000 employees (L341-L342); disclosure updates "on or about November 9, 2025" /
  November 14 (L339).
- Rounded prose beside exact figures: tiles "$3.5B" vs 3,545; "up 9%" vs 8.8; bullets (servicing
  +7%, mgmt +16%, FX +11%, sec finance +19%, S&P +9%, expenses +5%) vs 7.2, 16.1, 11.2, 19.0,
  9.1, 5.5; "$51.7T"/"$5.4T" vs 51,664/5,446.
- Definitions: L347 new non-GAAP bullet incl. ROTCE ("tangible common equity ... reflects a
  reduction (net of deferred taxes) for goodwill and other intangible assets") and constant
  currency; Addendum location "Filings & Reports - Quarterly Results"; L364 fee operating leverage
  "corresponding". FLS L377 adds "the pending shutdown of the U.S. federal government" and AI
  adoption; cites 2024 Form 10-K (L395).
- Coverage: FULL - L1-L398 read. Spot-check vs original: tile "332BPS" (docs L30), notable row
  "Other notable items (net)(d)" (docs L120), page "13" (docs L409) match; original contains no
  "MARKET DATA", "INDUSTRY FLOW" or "Morningstar" text (absence confirmed). Addendum not captured.

## D08 - 4Q25 earnings news release (January 16, 2026)

- Source: docs/stt_ex991_2026-01-16.txt (51,824 chars; "a4q25earningspressrelease.htm"); text
  L1-L404; printed pages 1-14 (L77, 101, 137, 142, 204, 246, 260, 295, 334, 348, 356, 374, 391,
  403). Capture artifact (also in original): doubled percent signs (e.g. "1 % % 8 % %", tab-separated) in tables.
- Written or submitted by: State Street Corporation (L9-L12); quotes Ron O'Hanley (L19-L28);
  contacts Lynn, Mark LaVoie (L75). Partners/investees named: Apex Fintech Solutions (L26, L86),
  Coller Capital (L87), "Groww AMC, the asset management arm of an India-based digital investment
  platform" = "Groww Asset Management Limited" (L87, L99).
- Type, date, edition: quarterly earnings release dated "January 16, 2026" (L13); call Friday
  January 16, 2026 11:00 a.m. ET, passcode 5068204# (L337).
- Period covered: 4Q25 (quarter ended December 31, 2025; L183). Columns 4Q25 | 3Q25 | 4Q24; AUM
  roll-forward 4Q25-4Q24 (= all four 2025 quarters + 4Q24). NO full-year 2025 columns.
- Headline/tiles (L15-L47): "FOURTH QUARTER 2025 EPS OF $2.42; $2.97 EXCLUDING NOTABLE ITEMS";
  "$3.7B TOTAL REVENUE, up 7% YoY"; "(487)BPS TOTAL OPERATING LEVERAGE"; "25.0% PRE-TAX MARGIN";
  "11.3% ROE"; "17.5% ROTCE"; "Ex-notables": "105BPS TOTAL OPERATING LEVERAGE", "30.7% PRE-TAX
  MARGIN", "13.9% ROE", "21.5% ROTCE". (Table figures 3,667/3,412 and 2,741/2,440 compute to about
  (486) bps; ex-notables 2,535/2,382 to 105 bps.)
- Outlook/prose (CEO): L26 "2025 ... achieving positive operating leverage, expanding pre-tax
  margin, and generating higher returns", "expanding Wealth Services through our partnership with
  Apex Fintech Solutions"; L27 4Q25 "record fee and total revenue"; L28 "As we enter 2026, we will
  execute against our strategic priorities, including further embedding technology and
  artificial intelligence". No numeric 2026 guidance; no FY2025 figures printed.
- Tables (USD millions unless noted):
  - L51-L74 highlights 4Q25/3Q25/4Q24: fee revenue 2,862/2,829/2,662 (1%, 8%); NII 802/715/749
    (12, 7); other income 3/1/1; total revenue 3,667/3,545/3,412 (3, 7); provision 8/9/12; total
    expenses 2,741/2,434/2,440 (13, 12); net income 747/861/783; EPS $2.42/$2.78/$2.46 ((13)%,
    (2)%); ROE 11.3/13.4/12.7%; NEW row "Return on average tangible common equity (ROTCE)"
    17.5/20.9/20.3; pre-tax margin 25.0/31.1/28.1%; AUC/A ($B) 53,800/51,664/46,557; AUM ($B)
    5,665/5,446/4,715.
  - L112-L124 Notable items 4Q25/3Q25/4Q24: "Repositioning charges (net)" (226)/—/2; "Other
    notable items (net)" 20/—/19; "Deferred compensation expense acceleration" —/—/(79); total
    (206)/—/(58); tax (49)/—/(17); EPS (0.55)/—/(0.14). L126: 4Q25 repositioning $226M = $111M
    comp (workforce rationalization) + $69M occupancy (real estate footprint optimization) + $24M
    info systems + $22M other (operating model changes); other notable $20M = $60M FDIC special
    assessment release less $40M "Legal and related costs". Footnotes (f)-(h) L133-L135 RECAST
    4Q24: repositioning (net) +$2M = $15M comp release less $13M occupancy charge; other (net)
    +$19M = $31M FDIC release less $12M operating-model charge (D03 L95-L99 showed 4Q24 rows FDIC
    31 and "Repositioning charges and other notable items (net)" (10); same total (58)).
  - Adjusted-line footnotes (L129-L132, repeated L290-L293): comp $1,331M -> $1,220M vs adjusted
    4Q24 $1,148M (+6%); info systems $557M -> $533M vs $480M (+11%); occupancy $173M -> $104M vs
    adjusted 4Q24 $110M (-5%); other $424M -> $422M vs adjusted 4Q24 $399M (+6%) and vs 3Q25 GAAP
    $373M (+13%).
  - L147-L165 AUC/A: collective funds 17,997/17,795/15,266; mutual 13,518/13,209/12,301; pension
    10,452/10,321/9,386; insurance and other 11,833/10,339/9,604 (14%, 23%); equities
    31,879/31,124/27,535; fixed-income 13,830/12,874/11,933; short-term 8,091/7,666/7,089.
  - L170-L186 4Q25 AUM roll-forward by product: begin 3,465/720/540/477/244/5,446; LT
    institutional (10)/8/—/12/—/10; ETF 38/3/—/—/10/51; cash 24; total flows 28/11/24/12/10/85;
    market 102/11/6/12/17/148; FX (6)/(8)/—/—/—/(14); end Dec 31, 2025 3,589/734/570/501/271/5,665.
  - L188-L202 5-quarter AUM 4Q25/3Q25/2Q25/1Q25/4Q24: total flows 85/26/82/(13)/64; ending
    5,665/5,446/5,117/4,665/4,715.
  - L208-L227 Revenue: servicing fees 1,388/1,357/1,283 (2.3%, 8.2%); management fees 662/612/576
    (8.2, 14.9); FX trading 405/416/360 ((2.6), 12.5); securities finance 127/138/118 ((8.0),
    7.6); front office software and data 163/167/197 ((2.4), (17.3)); lending related 58/60/62;
    software and processing 221/227/259 ((2.6), (14.7)); other fee revenue 59/79/66; total fee
    revenue (1.2%, 7.5%); NII 802/715/749 (12.2%, 7.1%); other income 3/1/1; total revenue (3.4%,
    7.5%); NIM 1.10/0.96/1.07% (14 bps, 3 bps). No ex-notables revenue row.
  - L250-L257 Allowance: begin 201/192/171; provision 8/9/12; charge-offs (6)/—/—; end 203/201/183.
  - L264-L275 Expenses: comp 1,331/1,162/1,212; info systems 557/517/480; transaction processing
    256/276/245; occupancy 173/106/123; "Other" 424/373/380 - NO amortization row (D07 L270-L271:
    3Q25 amortization 56 + other 317 = 373; D03 L318-L319: 4Q24 54 + 326 = 380); total
    2,741/2,434/2,440 (12.6%, 12.3%); ex-notables 2,535/2,434/2,382 (4.1%, 6.4%); ETR
    18.6/21.9/18.4%; L298 ETR ex-notables 19.6% (4Q25) vs 18.9% (4Q24).
  - L303-L322 Capital: Std CET1 11.7/11.3/10.9; Tier 1 14.4/13.9/13.2; total 16.1/15.5/14.8; Adv
    CET1 13.0/13.1/12.0; Adv Tier 1 16.1/16.2/14.5; total 17.7/17.8/16.1; Tier 1 leverage
    5.5/5.6/5.2; "Supplementary leverage ratio (SLR)" 6.5/6.4/6.2; LCR 106/106/107; SSBT LCR
    143/142/134. New SLR narrative L328.
- Events/actions: servicing fee revenue wins $87M (back office, private markets); AUC/A wins
  $484B "majority from Insurance and Asset Managers" (L84); to be installed $320M and AUC/A $2.5T
  (L85); "Launched State Street's Digital Asset Platform" (L86) - footnote (b) L99 "launched on
  January 15, 2026"; Groww partnership incl. "a minority investment by State Street Investment
  Management, announced on January 14, 2026" (L99); Coller Capital "Strategic investment and
  partnership ... private markets secondaries" (L87); "37 new products launched in 4Q25, and 134
  new products launched in 2025" (L87); ARR ~11% ($375M 4Q24, $402M 3Q25, $418M 4Q25, L360); NO
  State Street Alpha bullet (present D02-D07); 4Q25 capital return $635M = $400M repurchases +
  $235M dividends ($0.84) (L140); SPDR marketing-agent AUM ~$173B, ~52,000 employees (L345-L346);
  disclosure updates "on or about March 1, 2026" (L343).
- Rounded prose beside exact figures: "$3.7B" vs 3,667; fee revenue "8%" vs 7.5 (2,862/2,662) and
  total revenue "7%" vs 7.5 (3,667/3,412); bullets (servicing +8%, mgmt +15%, FX +13%, sec
  finance +8%, S&P -15%, occupancy +41%) vs 8.2, 14.9, 12.5, 7.6, (14.7), 40.7.
- Definitions: L353-L359 "asset servicing" wording changed to "investment servicing" ("new
  investment servicing wins", "New investment servicing mandates", "investment servicing and
  investment management mandates"); L368 fee operating leverage "corresponding". FLS L389 changes
  ESG bullet to "investment management, stewardship and sustainable investment strategies"; drops
  the federal-shutdown clause and the "significant operations and clients in many markets"
  bullet; still cites 2024 Form 10-K (L401).
- Coverage: FULL - L1-L404 read. Spot-check vs original: highlights row with doubled "%" (docs L50),
  footnote (b) launch date (docs L100), notable row (docs L116), expense row "Other 424 373 380"
  (docs L282), page "14" (docs L417) match; original has no amortization row. Addendum not
  captured.

## D09 - 1Q26 earnings news release (April 17, 2026)

- Source: docs/stt_ex991_2026-04-17.txt (51,675 chars; "a1q26earningspressrelease.htm"); text
  L1-L423; printed pages 1-14 (L72, 101, 134, 202, 222, 264, 278, 313, 355, 369, 377, 395, 409,
  422). Zero-width-space lines at L237, L332, L336 (capture artifacts).
- Written or submitted by: State Street Corporation (L9-L12); quotes Ron O'Hanley (L19-L28);
  contacts Lynn, LaVoie (L70).
- Type, date, edition: quarterly earnings release dated "April 17, 2026" (L13); call Friday April
  17, 2026 11:00 a.m. ET, passcode 68683# (L358).
- Period covered: 1Q26 (quarter ended March 31, 2026; L162). Columns 1Q26 | 4Q25 | 1Q25; AUM
  5-quarter 1Q26-1Q25. No full-year columns.
- Headline/tiles (L15-L47): "FIRST QUARTER 2026 EPS OF $2.49; $2.84 EXCLUDING NOTABLE ITEMS";
  "$3.8B TOTAL REVENUE, up 16% YoY"; "86BPS TOTAL OPERATING LEVERAGE"; "25.5% PRE-TAX MARGIN";
  "11.6% ROE"; "17.6% ROTCE"; ex-notables "616BPS", "29.0%", "13.3%", "20.1%".
- Outlook/prose (CEO): L26 "strong start to 2026"; L27 "record quarterly fee revenue, net
  interest income, and total revenue"; L28 "Looking ahead, how the macro and geopolitical
  environment will evolve is uncertain" (hedge attaches to the environment), "confident in our
  ability to continue to grow and deliver even more as we move through the year". No numeric
  guidance.
- RECLASSIFICATION (footnote (b) L99 = footnote (1) L245): "In the first quarter of 2026, revenue
  related to distribution and marketing activities was reclassified from Foreign exchange trading
  services to Management fees. Additionally, Lending related and other fees, previously recognized
  within Software and processing fees, was reclassified to Other fee revenue, and the Software and
  processing fees caption has been changed to Software services. Prior-period amounts have been
  reclassified ... no impact on Total fee revenue, Total revenue or Net income".
- Tables (USD millions unless noted):
  - L51-L69 highlights 1Q26/4Q25/1Q25: fee revenue 2,960/2,862/2,570 (3%, 15%); NII 835/802/714;
    other income 1/3/—; total revenue 3,796/3,667/3,284 (4, 16); provision 16/8/12; total
    expenses 2,811/2,741/2,450 (3, 15); net income 764/747/644; EPS $2.49/$2.42/$2.04 (3%, 22%);
    ROE 11.6/11.3/10.6%; ROTCE 17.6/17.5/16.4; pre-tax margin 25.5/25.0/25.0%; AUC/A ($B)
    54,515/53,800/46,733; AUM ($B) 5,620/5,665/4,665.
  - L109-L121 Notable items 1Q26/4Q25/1Q25: "Repositioning charges" (89)/(226)/—; "Client
    rescoping" (41)/—/—; "Other notable items (net)" —/20/—; total (130)/(206)/—; tax
    (32)/(49)/—; EPS (0.35)/(0.55)/—. L123: $89M = $79M comp (workforce rationalization) + $1M
    occupancy (footprint) + $9M info systems (operating model); client rescoping $41M in info
    systems (not described as Alpha-related here). Footnotes (e)/(f) L131-L132 repeat 4Q25
    components. Adjusted lines L128-L130/L308-L311: comp $1,441M -> $1,362M (+8% vs $1,262M;
    +12% vs adjusted 4Q25 $1,220M); info systems $637M -> $587M (notables $50M; +18% vs $497M,
    +10% vs $533M); occupancy $101M -> $100M; 1Q26 Other $349M -17% vs adjusted 4Q25 $422M.
  - L139-L157 AUC/A: collective funds 18,338/17,997/15,430; mutual 13,309/13,518/12,143; pension
    10,912/10,452/9,377; insurance 11,956/11,833/9,783; equities 32,243/31,879/27,508;
    fixed-income 14,030/13,830/11,900; short-term 8,242/8,091/7,325.
  - L160-L200 RESTRUCTURED AUM tables (footnote (1) L197: disclosures "now organized around
    Index; Active, Alternatives and Other Strategies; and Cash"; asset class and geography
    retained as supplemental views). Columns: Dec 31, 2025 balance | net flows | market | FX |
    total market+FX | Mar 31, 2026 balance.
    - By asset class: Equity 3,589/2/(94)/(1)/(95)/3,496; Fixed-Income 734/28/.../756; Cash
      570/8/3/—/3/581; "Multi-Asset" 501/12/(6)/(4)/(10)/503; Alternative 271/(1)/14/—/14/284;
      total 5,665/49/(86)/(8)/(94)/5,620.
    - By geography (footnote (4) client or fund management location): Americas
      4,155/10/(56)/(1)/(57)/4,108; label printed "Europe/Middle East/Asia" 841/29/(15)/(10)/(25)/
      845; Asia-Pacific 669/10/(15)/3/(12)/667.
    - By vehicle: ETF 1,951/25/(36)/—/(36)/1,940; Separately Managed Accounts 2,127/30/.../2,120;
      Other Commingled Funds 1,587/(6)/.../1,560.
    - By strategy: Index - ETFs 1,936/25/(35)/—/(35)/1,926; Other Index 2,986/13/(53)/(8)/(61)/
      2,938; Total Index 4,922/38/.../4,864; Active, Alternatives and Other 173/3/(1)/—/(1)/175;
      Cash 570/8/.../581. (ETF by vehicle 1,951 vs Index ETFs 1,936.)
  - L204-L220 5-quarter AUM 1Q26/4Q25/3Q25/2Q25/1Q25 recast by strategy: Index ETFs
    25/51/38/15/—; Other Index 13/14/(7)/81/(12); total Index 38/65/31/96/(12); Active,
    Alternatives and Other 3/(4)/(15)/(13)/(2); Cash 8/24/10/(1)/1; total flows 49/85/26/82/(13);
    ending 5,620/5,665/5,446/5,117/4,665; "Memo: ETF Total Flows, net" 25/51/37/15/1.
  - L226-L246 Revenue (recast): servicing fees 1,409/1,388/1,275 (1.5%, 10.5%); "Management
    fees(1)" 724/717/587 (1.0, 23.3); "Foreign exchange trading services(1)" 435/350/337 (24.3,
    29.1); securities finance 116/127/114 ((8.7), 1.8); "Software services(1)" 169/163/158 (3.7,
    7.0); "Other fee revenue(1)" 107/117/99 ((8.5), 8.1); total fee revenue 2,960/2,862/2,570
    (3.4%, 15.2%); NII 835/802/714 (4.1%, 16.9%); other income 1/3/— ((66.7)%); total revenue
    3,796/3,667/3,284 (3.5%, 15.6%); NIM 1.16/1.10/1.00% (6 bps, 16 bps). No front office or
    lending-related rows.
  - L268-L275 Allowance: begin 203/201/183; provision 16/8/12; charge-offs (40)/(6)/(9); end
    179/203/186.
  - L282-L293 Expenses: comp 1,441/1,331/1,262 (14.2% YoY); info systems 637/557/497 (28.2);
    transaction processing 283/256/258; occupancy 101/173/103; "Other" 349/424/330 (1Q25 Other
    330 = D05 L306-L307 amortization 54 + other 276); total 2,811/2,741/2,450 (2.6%, 14.7%);
    ex-notables 2,681/2,535/2,450 (5.8%, 9.4%); ETR 21.2/18.6/21.7%; L316 ETR ex-notables 21.6%
    (1Q26) vs 21.7% (1Q25), 19.6% (4Q25).
  - L321-L343 Capital: Std CET1 10.6/11.6/11.0 (4Q25 printed 11.7 in D08 L305; docs checked);
    Tier 1 13.1/14.4/13.8; total 14.5/16.1/15.3; Adv CET1 12.5/13.0/12.6; Adv Tier 1
    15.5/16.1/15.7; total 17.0/17.7/17.3; Tier 1 leverage 5.4/5.5/5.5; SLR 6.3/6.5/6.5; LCR
    106/106/106; SSBT LCR 139/143/139. L125/L345 CET1 "decreased 1.0% point compared to 4Q25,
    primarily due to a normalization in RWA from episodically low levels in the prior quarter".
- Events/actions: servicing fee revenue wins $56M "primarily driven by back office and
  Alternatives, which includes private markets and hedge funds"; AUC/A wins $365B (majority Asset
  Managers) (L79); to be installed $315M and AUC/A $2.7T (L80); "State Street Alpha: 1 new mandate
  win" (L81); "Software services" ARR ~12% ($373M 1Q25, $418M 4Q25, $418M 1Q26, L381); "Record
  quarterly SPYM ETF inflows: #1 asset gathering ETF globally"; "57 new products and solutions";
  "4 awards at the 2026 ETF.com Awards for ALLW and PRIV" (L83-L85); "Record FX trading volumes up
  25%, average securities on loan up 20%" (L86); 1Q26 capital return $633M = $400M repurchases +
  $233M dividends ($0.84) (L125); ~51,000 employees, SPDR marketing-agent AUM ~$184B (L366-L367);
  disclosure updates "on or about May 10, 2026" / May 15 (L364).
- Rounded prose beside exact figures: "$3.8B" vs 3,796; "up 16%" vs 15.6; bullets (servicing
  +11%, mgmt +23%, FX +29%, sec finance +2%, software services +7%, other +8%) vs 10.5, 23.3, 29.1,
  1.8, 7.0, 8.1; expenses +15% vs 14.7; ex-notables +9% vs 9.4.
- Definitions: L374 "Servicing fee revenue wins (i.e., "sales") and backlog (i.e., "to be
  installed")"; L381 "Software services ARR" ("software and data revenue" replaces
  "software-enabled revenue"); L389 fee operating leverage "corresponding". FLS L402 "the recent
  shutdown of the U.S. federal government"; L406 new capital-return bullet; cites "2025 Annual
  Report on Form 10-K" (L420; first in bundle).
- Coverage: FULL - L1-L423 read. Spot-check vs original: reclass footnote (docs L100, L254),
  "Europe/Middle East/Asia" (docs L179), memo ETF row (docs L226), management fees row (docs
  L237), expense row "Other 349 424 330" (docs L301), CET1 row "10.6 % 11.6 % 11.0 %" (docs
  L337; D08 docs L318 "11.7"), page "14" (docs L436) match. Addendum not captured.

## D10 - 2Q26 earnings news release (July 16, 2026)

- Source: docs/stt_ex991_2026-07-16.txt (52,997 chars; "a2q26earningspressrelease.htm"); text
  L1-L417; printed pages 1-14 (L65, 96, 126, 192, 212, 258, 272, 306, 348, 362, 370, 388, 403,
  416). Zero-width-space lines L227, L325, L329.
- Written or submitted by: State Street Corporation (L9-L12); quotes Ron O'Hanley (L19-L26);
  contacts Lynn, LaVoie (L63). Mentioned (not authors): U.S. Department of the Treasury (L91),
  Federal Reserve stress test (L25).
- Type, date, edition: quarterly earnings release dated "July 16, 2026" (L13); call Thursday July
  16, 2026 11:00 a.m. ET, passcode 93090# (L351). Latest document in bundle.
- Period covered: 2Q26 (quarter ended June 30, 2026; L154). Columns 2Q26 | 1Q26 | 2Q25; AUM
  5-quarter 2Q26-2Q25. No YTD/full-year columns.
- Headline/tiles (L15-L40): "SECOND QUARTER 2026 EPS OF $3.65" (no ex-notables EPS; 2Q26 has no
  notable items); "$4.0B TOTAL REVENUE, up 17%"; "1,226BPS TOTAL OPERATING LEVERAGE"; "34.3%
  PRE-TAX MARGIN"; "16.7% ROE"; "25.5% ROTCE"; "Ex-notables: 645BPS TOTAL OPERATING LEVERAGE".
- Outlook/prose (CEO): L24 "record total revenues, along with record AUC/A and AUM", "a tenth
  consecutive quarter of positive operating leverage excluding notable items"; L25 "Following the
  release of the Federal Reserve's stress test results, we recently declared a 10% per share
  increase to our third quarter common stock dividend" (new per-share amount NOT printed); L26
  "we are entering our next phase of growth, defined by new medium-term financial targets. We are
  confident in our ability to deliver on these goals" - the target values are NOT stated in D10
  or anywhere in the bundle (grep "medium-term" hits only D10 L26, L391). FLS L391 adds terms
  "medium-term", "assumption", "illustrative", "framework".
- Tables (USD millions unless noted):
  - L44-L61 highlights 2Q26/1Q26/2Q25: fee revenue 3,188/2,960/2,719 (8%, 17%); NII 860/835/729;
    other income —/1/—; total revenue 4,048/3,796/3,448 (7, 17); provision —/16/30; total
    expenses 2,659/2,811/2,529 ((5), 5); net income 1,084/764/693 (42, 56); EPS
    $3.65/$2.49/$2.17 (47%, 68%); ROE 16.7/11.6/10.8%; ROTCE 25.5/17.6/16.7; pre-tax margin
    34.3/25.5/25.8%; AUC/A ($B) 57,858/54,515/49,000; AUM ($B) 6,278/5,620/5,117.
  - L105-L112 Notable items 2Q26/1Q26/2Q25: "Repositioning charges" —/(89)/(100); "Client
    rescoping" —/(41)/(42) (2Q25 single row = D06's revenue (24) + expense (18)); "Other notable
    items" —/—/4; total —/(130)/(138); tax —/(32)/(35); EPS —/(0.35)/(0.36). Footnotes L122-L124;
    (f) L123 places 2Q25 $24M revenue impact in "Software services" and $18M in info systems (no
    "Alpha-related" wording).
  - Adjusted-figure footnotes: L93/L255 2Q25 FX "$393 million" incl. $3M -> adjusted $390M (2Q26
    $494M +27%); L94/L256 2Q25 software services $169M -> $193M (2Q26 $166M -14%); L119-L121 and
    L301-L304: comp 2Q26 $1,292M +9% vs adjusted 2Q25 $1,180M, -5% vs adjusted 1Q26 $1,362M; info
    systems $589M +17% vs $505M, flat vs $587M; occupancy $96M -4% vs adjusted 1Q26 $100M; other
    $402M +11% vs adjusted 2Q25 "$362 million" (2Q25 GAAP Other "$361 million").
  - L131-L149 AUC/A: collective funds 20,055/18,338/16,728; mutual 14,353/13,309/12,641; pension
    11,219/10,912/9,679; insurance 12,231/11,956/9,952; equities 34,670/32,243/29,311;
    fixed-income 14,160/14,030/12,122; short-term 9,028/8,242/7,567.
  - L152-L190 AUM 2Q26 (Mar 31, 2026 balance | flows | market | FX | total | Jun 30, 2026):
    - Asset class: Equity 3,496/60/499/(4)/495/4,051; Fixed-Income 756/12/11/(3)/8/776; Cash
      581/35/5/—/5/621; Multi-Asset 503/13/51/—/51/567; Alternative 284/(6)/(15)/—/(15)/263; total
      5,620/114/551/(7)/544/6,278.
    - Geography: Americas 4,108/75/391/(1)/390/4,573; "Europe/Middle East/Africa"
      845/18/94/(1)/93/956 (D09 L176 labelled this row "Europe/Middle East/Asia"); Asia-Pacific
      667/21/66/(5)/61/749.
    - Vehicle: ETF 1,940/68/196/—/196/2,204; Separately Managed Accounts 2,120/9/218/(7)/211/2,340;
      Other Commingled Funds 1,560/37/137/—/137/1,734.
    - Strategy: Index ETFs 1,926/66/196/—/196/2,188; Other Index 2,938/15/333/(7)/326/3,279;
      Total Index 4,864/81/529/(7)/522/5,467; Active, Alternatives and Other 175/(2)/17/—/17/190;
      Cash 581/35/5/—/5/621. D09's restructuring footnote is not repeated.
  - L194-L210 5-quarter AUM 2Q26/1Q26/4Q25/3Q25/2Q25: Index ETFs 66/25/51/38/15; Other Index
    15/13/14/(7)/81; Active/Alt/Other (2)/3/(4)/(15)/(13); Cash 35/8/24/10/(1); total flows
    114/49/85/26/82; ending 6,278/5,620/5,665/5,446/5,117; memo ETF total flows 68/25/51/37/15.
  - L216-L237 Revenue (reclassified basis, no reclass footnote in D10): servicing fees
    1,468/1,409/1,304 (4.2%, 12.6%); management fees 772/724/600 (6.6, 28.7); FX trading
    494/435/393 (13.6, 25.7); securities finance 150/116/126 (29.3, 19.0); software services
    166/169/169 ((1.8), (1.8)); other fee revenue 138/107/127 (29.0, 8.7); total fee revenue
    3,188/2,960/2,719 (7.7%, 17.2%); NII 860/835/729 (3.0%, 18.0%); total revenue
    4,048/3,796/3,448 (6.6%, 17.4%); ex-notables 4,048/3,796/3,469 (6.6, 16.7); NIM
    1.13/1.16/0.96% ((3) bps, 17 bps).
  - L262-L269 Allowance: begin 179/203/186; provision —/16/30; charge-offs (4)/(40)/(24); end
    175/179/192 (L270 reserve release from commercial loan sales/repayments offset by CRE).
  - L276-L287 Expenses: comp 1,292/1,441/1,280; info systems 589/637/523; transaction processing
    280/283/260; occupancy 96/101/105; "Other" 402/349/361 (2Q25 361 = D06 L319-L320 amortization
    56 + other 305); total 2,659/2,811/2,529 ((5.4)%, 5.1%); ex-notables 2,659/2,681/2,412
    ((0.8), 10.2); ETR 21.9/21.2/22.0% (L309 ex-notables vs 22.5% 2Q25, 21.6% 1Q26).
  - L314-L336 Capital: Std CET1 10.8/10.6/10.7; Tier 1 13.2/13.1/13.3; total 14.5/14.5/14.8; Adv
    CET1 13.2/12.5/12.5; Adv Tier 1 16.3/15.5/15.5; total 17.8/17.0/17.0; Tier 1 leverage
    5.3/5.4/5.3; SLR 6.2/6.3/6.3; LCR 107/106/107; SSBT LCR 136/139/136. LCR described "at
    quarter-end" (L115, L344) while L376 still says LCR "is a preliminary estimate based on a
    quarterly daily average".
- Events/actions: servicing fee revenue wins $87M (back office and Alternatives); AUC/A wins $384B
  (majority Asset Managers and Alternatives) (L72); to be installed $335M and AUC/A $2.9T (L73);
  "Digital Assets: Announced tokenized fund servicing capability in Luxembourg" with footnote (b)
  L90 "Delivery of the capability remains subject to applicable regulatory approvals and
  operational readiness milestones" (announcement, not delivery); "38 newly launched products and
  solutions" (L76); "SPYM ETF selected as exclusive default investment for Trump Accounts" -
  footnote (c) L91 "State Street Investment Management announced on July 1, 2026, that SPYM was
  selected by the U.S. Department of the Treasury as the exclusive default ETF for Trump
  Accounts"; "record FX client trading volumes up 25%, average securities on loan up 24%" (L79);
  no State Street Alpha bullet; 2Q26 capital return $631M = $400M repurchases + $231M dividends
  ($0.84) (L116); ~51,000 employees; SPDR marketing-agent AUM ~$157B (L359-L360); disclosure
  updates "on or about August 9, 2026" / August 14 (L357).
- ARR DEFINITION CHANGE (L374): now "annualizing the revenue from the last month of the relevant
  quarter" (previously the quarter's revenue); "Prior period amounts have been recast"; Software
  services ARR $381M (2Q25), $427M (1Q26), $433M (2Q26) - vs D06 L407 2Q25 $379M and D09 L381
  1Q26 $418M under the old method. Highlights L75 "increased approximately 14%".
- Rounded prose beside exact figures: "$4.0B" vs 4,048; "up 17%" vs 17.4; bullets (servicing
  +13%, mgmt +29%, FX +26%, sec finance +19%, software services -2%, other +9%, expenses +5%) vs
  12.6, 28.7, 25.7, 19.0, (1.8), 8.7, 5.1; ex-notables fee revenue +16% (L82).
- Definitions: L367 wins "(i.e., "sales")"/backlog; L382 fee operating leverage "corresponding";
  FLS L411 adds AI-enabled attacks; cites 2025 Form 10-K (L414).
- Coverage: FULL - L1-L417 read. Spot-check vs original: "medium-term financial targets" (docs
  L24), tile (docs L26), notable row (docs L111), "Europe/Middle East/Africa" (docs L171),
  management fees row (docs L225), expense row "Other 402 349 361" (docs L292), ARR method (docs
  L385), page "14" (docs L427) match. Addendum not captured.

## Shared ground (navigation only)

Facts and locations only; the author turns relationships into hooks in notes/hooks.md.

### Entities and aliases in more than one document

- Issuer: every document is a State Street Corporation (NYSE: STT) Form 8-K Exhibit 99.1; no
  bundle document is written by another organization. Releases D02-D10 open with State Street
  Corporation, One Congress Street, Boston; decks D01 and D04 carry State Street presenters.
- People: Ron(ald P.) O'Hanley, Chairman and CEO - D01 L9/L29; quoted in D02 L27, D03 L26, D05
  L26, D06 L28, D07 L19, D08 L19, D09 L19, D10 L19. Eric Aboaf (Vice Chairman and CFO) D01 only;
  Mark Keating (Interim CFO) and Yie-Hsin Hung (CEO, State Street Global Advisors) D04 only;
  Brennan Hawken (D01 L29) and Gerard Cassidy (D04 L23) named without roles. Contacts: Elizabeth
  Lynn D02-D10; Carolyn Cichon D02-D06; Mark LaVoie D07-D10.
- Investment-management business: "Global Advisors" (D01 L15, D02 L22/L29, D03 L28, D05 L71);
  "State Street Global Advisors"/"SSGA" (D04 L9, L31; affiliate sentence D02 L386, D03 L392, D05
  L376); "State Street Investment Management" (D06 L29/L394, D07 L342, D08 L99/L346, D09 L367,
  D10 L91/L360). Table caption "Investment Management" in all releases. The entity "State Street
  Global Advisors Funds Distributors, LLC (SSGA FD)" keeps its name in D06-D10.
- Servicing business: "Investment Servicing" (D01 L15; release table captions); "Investment
  Services" (D02 L29, D03 L28, D04 L11, D06 L29, D07 L79, D08 L27, D09 L27).
- Markets business: "Markets and Financing"/"Markets & Financing" (D01 L13/L19, D02 L65); "Global
  Markets" (D01 endnote 3 L33, D02 L29, D04 L11); "Markets" (D06 L66, D07 L79, D08 L87, D09 L86,
  D10 L79).
- Software line: "Front office software and data" (D02-D08; within "Software and processing
  fees") -> "Software services" (D09 L99/L233, D10 L223). CRD = Charles River Development
  (definitions D02-D10).
- State Street Alpha: D01 L15/L17, D02 L65, D03 L70, D04 L11 (SSGA is an Alpha client), D05
  L69-L70, D06 L64/L66/L104-L106, D07 L78, D09 L81; no Alpha bullet in D08 or D10 highlights.
- Mentioned (non-issuer) organizations: Euromoney (D02 L65/L78, D07 L79); Apex Fintech Solutions
  (D07 L26/L79, D08 L26/L86); Coller Capital and Groww AMC = Groww Asset Management Limited (D08
  L87/L99); U.S. Department of the Treasury (D10 L91); Federal Reserve stress test (D06 L30, D10
  L25); CF Global Trading (D01 L19); ETF.com (D09 L85); data sources Morningstar (D02-D06), S&P
  Global Market Intelligence (D01 endnotes 4/15; D02-D05), Pensions & Investments, Bloomberg,
  iMoneyNet (D01 L33; D04 L27), McKinsey (D04 L27), Global Custodian (D01 L33).
- Products: SPY (D01 L21/L41, D06 L66, D08 L87); SPYM (D09 L83, D10 L77/L91); ALLW, PRIV (D09
  L85); SPDR Gold Shares / Gold MiniShares (AUM table footnotes D02-D10).

### Periods covered by more than one document

- Quarter columns (current | prior quarter | year-ago): 3Q23 D02; 4Q23 D03; 1Q24 D05; 2Q24 D02,
  D06; 3Q24 D02, D03, D07; 4Q24 D03, D05, D08; 1Q25 D05, D06, D09; 2Q25 D06, D07, D10; 3Q25 D07,
  D08; 4Q25 D08, D09; 1Q26 D09, D10; 2Q26 D10 only. AUM 5-quarter roll-forwards: D02 3Q23-3Q24,
  D03 4Q23-4Q24, D05 1Q24-1Q25, D06 2Q24-2Q25, D07 3Q24-3Q25, D08 4Q24-4Q25, D09 1Q25-1Q26, D10
  2Q25-2Q26. Industry flows (5 quarters): D02, D03, D05, D06 only.
- Annual figures exist only in D01 (FY2023 expenses, FY2024 outlook, 2020-2024E wins chart) and
  D04 (SSGA calendar 2022-2024). No release prints full-year columns. All periods are calendar
  quarters (AUM captions use Mar 31 / Jun 30 / Sep 30 / Dec 31).
- Overlapping quarter values checked identical across editions (highlights, pre-reclass revenue,
  pre-merge expenses, AUC/A, allowance, market data, capital ratios) except the differences listed
  under "Same-period values that differ".

### Repeated per-quarter series (locations)

- Servicing fee revenue wins / to be installed / AUC/A wins / AUC/A to be installed: 3Q24
  $84M/$288M/$466B/$2.4T (D02 L64-L65); 4Q24 $154M/$346M/$1.1T/$3.0T (D03 L68-L70); 1Q25
  $55M/$356M/$182B/$3.1T (D05 L68-L70); 2Q25 $145M/$444M/$1.1T/$4.0T (D06 L64-L65); 3Q25
  $47M/$401M/$361B/$3.6T (D07 L76-L77); 4Q25 $87M/$320M/$484B/$2.5T (D08 L84-L85); 1Q26
  $56M/$315M/$365B/$2.7T (D09 L79-L80); 2Q26 $87M/$335M/$384B/$2.9T (D10 L72-L73). 2023: $301M
  wins, $270M to be installed at year-end 2023 (D01 L17, endnote 8).
- Alpha: 2023 7 mandates, 18 live clients YE2023 (D01 L17); 3Q24 2, YTD 5 (D02 L65); 4Q24 2, 2024
  total 7 (D03 L70); 1Q25 1 (D05 L70); 2Q25 2, 3 go-lives, 28 live (D06 L66); 3Q25 1 + 1 go-live,
  4 YTD (D07 L78); 1Q26 1 (D09 L81).
- Capital return total / buybacks / dividends / per share ($M): 3Q24 674/450/224/$0.76 (D02
  L111); 4Q24 770/550/220/$0.76 (D03 L117); 1Q25 320/100/220/$0.76 (D05 L105); 2Q25
  517/300/217/$0.76 (D06 L117); 3Q25 637/400/237/$0.84 (D07 L126); 4Q25 635/400/235/$0.84 (D08
  L140); 1Q26 633/400/233/$0.84 (D09 L125); 2Q26 631/400/231/$0.84 (D10 L116).
- Notable items pre-tax total / EPS impact: 3Q23 (294)/(0.68) D02; 4Q23 (620)/(1.49) D03; 1Q24
  (130)/(0.32) D05; 2Q24 none (D02, D06); 3Q24 net nil of (81)/66/15 (D02, D03, D07); 4Q24
  (58)/(0.14) (D03, D05, D08); 1Q25 none (D05, D06, D09); 2Q25 (138)/(0.36) (D06, D07, D10); 3Q25
  none (D07, D08); 4Q25 (206)/(0.55) (D08, D09); 1Q26 (130)/(0.35) (D09, D10); 2Q26 none (D10).
- Diluted EPS: 3Q23 $1.25, 2Q24 $2.15, 3Q24 $2.26 (D02 L40); 4Q23 $0.55, 4Q24 $2.46 (D03 L44);
  1Q24 $1.37, 1Q25 $2.04 (D05 L44); 2Q25 $2.17 (D06 L41); 3Q25 $2.78 (D07 L54); 4Q25 $2.42 (D08
  L62); 1Q26 $2.49 (D09 L57); 2Q26 $3.65 (D10 L50). Ex-notables EPS printed only in headlines:
  4Q24 $2.60 (D03 L18), 2Q25 $2.53 (D06 L18), 4Q25 $2.97 (D08 L15), 1Q26 $2.84 (D09 L15).
- ROTCE: 4Q24 20.3 (D08 L65); 1Q25 16.4 (D09 L60); 2Q25 16.7 (D10 L53); 3Q25 20.9 (D07 L38, D08
  L65); 4Q25 17.5 (D08, D09); 1Q26 17.6 (D09, D10); 2Q26 25.5 (D10).
- SPDR marketing-agent AUM inside reported AUM: ~$83B (D02 L386), ~$82B (D03 L392), ~$106B (D05
  L376), ~$116B (D06 L394), ~$145B (D07 L342), ~$173B (D08 L346), ~$184B (D09 L367), ~$157B (D10
  L360).
- New IM products: 39 in 3Q25 (D07 L26); 37 in 4Q25 and 134 in 2025 (D08 L87); 57 "products and
  solutions" 1Q26 (D09 L84); 38 "newly launched products and solutions" 2Q26 (D10 L76).
- "Record" claims: 3Q24 EPS, Global Advisors net inflows $100B, Cash inflows $54B (D02 L18, L22,
  L65); 4Q24 management fees (D03 L28); 2Q25 AUC/A $49T, AUM $5T, FX volumes (D06 L21, L29, L66);
  3Q25 AUC/A, AUM, management fees (D07 L22-L26); 4Q25 fee and total revenue (D08 L27); 1Q26 fee
  revenue, NII, total revenue, SPYM inflows, FX volumes (D09 L27, L83, L86); 2Q26 total revenues,
  AUC/A, AUM, FX client volumes (D10 L24, L70, L79). D01 L21 calls 4Q23 $103B a record.

### References back and amendment order

- No document names another bundle document. Back-references: D03 L26 "exceeded the financial
  outlook we provided at the outset of 2024"; D03 L28 servicing-wins goal of $350-400 million
  (goal in D01 L17); D07 L27 "As previously announced" (dividend; D06 L117); passive-alternatives
  revision footnotes (D02 L223/L243, D03 L227/L247, D05 L240, D06 L243); D09 L99/L245 "Prior-period
  amounts have been reclassified"; D09 L197 AUM disclosure update; D10 L374 ARR "Prior period
  amounts have been recast".
- Presentation changes in order: D03 fee operating leverage "successive" -> "corresponding",
  3Q24 notable rows netted; D05 back/middle office rows dropped, "Long-term Funds" label; D06
  SSGA -> State Street Investment Management, "Specials Volumes" and "Other income" rows dropped,
  "Cash fund" -> "Cash", leverage in bps; D07 market data and industry flows dropped, ROTCE tile,
  new non-GAAP bullet; D08 amortization merged into "Other", 4Q24 notable rows recast, "asset
  servicing" -> "investment servicing", ROTCE table row; D09 revenue reclassification, "Software
  services", AUM by strategy/vehicle/geography, 2025 Form 10-K; D10 ARR last-month method, single
  "Client rescoping" row for 2Q25, "Europe/Middle East/Africa" label.

### Forecast/target vs later actual; proposal vs action

- D01 FY2024 outlook (fee revenue ~3-4%, positive fee operating leverage; L13, L15, L23) vs D03
  L26 "exceeded the financial outlook" - no FY2024 figures anywhere in the bundle.
- D01 L17 servicing fee revenue wins $350-400M (2024) vs D03 L28 goal met (quarterly 3Q24 $84M,
  4Q24 $154M only).
- D01 L17 "+6-8 new Alpha mandates targeted in 2024" vs D03 L70 "7 mandate wins in 2024".
- D01 L21 organic AUM growth >2% (endnote 22) vs D04 L13 2024 "+3.5%".
- D01 endnote 23 L35 second India JV consolidation "expected to be completed in 2Q24" vs D02 L329
  JVs "consolidated in 4Q23 and 2Q24".
- D01 L21 Institutional MMF rank #8 -> #7 target vs D04 L11 "Top 10" (rank not stated).
- D01 L21 U.S. Low-Cost ETF share to 5% vs later "market share gains" without figures (D05 L71,
  D06 L66, D07 L79, D08 L87, D09 L86).
- D01 L19 average loan balances ~+10% (FY2024 vs FY2023, ex-overdrafts, endnote 16) vs D03 L80
  "double-digit loan growth" (stated as a 4Q24 YoY NII driver; different measure).
- D01 L25/L35 legacy-application, bespoke-process, AI-initiative, span-of-control goals: no later
  outcome stated.
- D06 L30/L117 planned 11% dividend increase to $0.84 "subject to approval by the Board" -> D07
  L27/L126 increased, $0.84 declared. D10 L25 "recently declared a 10% per share increase to our
  third quarter common stock dividend" (amount not printed).
- D10 L26 "new medium-term financial targets" (values not printed).
- Announced/launched with dates: D08 L99 Groww partnership "announced on January 14, 2026",
  Digital Asset Platform "launched on January 15, 2026" (both after the 4Q25 quarter-end); D10 L91
  SPYM selection announced July 1, 2026; D10 L74/L90 Luxembourg tokenized fund servicing
  "Announced", delivery "remains subject to applicable regulatory approvals and operational
  readiness milestones". D01 L19 "Closed CF Global Trading acquisition"; D01 L25 "Announced plans
  to streamline and delayer our staff functions".

### Same-period values that differ between editions (both locations)

- 4Q23 IM total net flows: D01 L21 $103B ("record") vs D02 L237/D03 L241 95 (revised footnote).
- Industry flows: 3Q24 D02 vs D03; 4Q24 D03 vs D05; 1Q25 D05 vs D06 (first-edition quarters use
  Morningstar estimates for the final month).
- Capital: 1Q25 Advanced CET1 12.5 (D05 L345) vs 12.6 (D06 L361, D09 L329); 4Q25 Standardized
  CET1 11.7 (D08 L305) vs 11.6 (D09 L323).
- Revenue reclassification: 1Q25 (D05 vs D09), 2Q25 (D06 vs D10), 4Q25 (D08 vs D09) management,
  FX, software and other fee lines; 2Q25 adjusted FX $428M (D06 L76) vs $390M (D10 L93).
- Expense "Other" incl. amortization: 4Q24 326 vs 380, 3Q25 317 vs 373, 1Q25 276 vs 330, 2Q25 305
  vs 361; adjusted Other 4Q24 $345M (D05 L327) vs $399M (D08 L132); 2Q25 $306M (D06 L112) vs $362M
  (D10 L121).
- ARR: 2Q25 $379M (D06 L407) vs $381M (D10 L374); 1Q26 $418M (D09 L381) vs $427M (D10 L374).
- Notable-item row allocation (totals equal): 3Q24 (D02 vs D03/D07), 4Q24 (D03/D05 vs D08), 2Q25
  client rescoping (D06/D07 vs D10).
- Label: Mar 31, 2026 geography row 845 "Europe/Middle East/Asia" (D09 L176) vs
  "Europe/Middle East/Africa" (D10 L167).

### Scope, exclusion and hedge locations

- AUM includes SPDR products where SSGA FD "acts solely as the marketing agent" (boilerplate
  footnote, every release) and Alternative Investments include SPDR Gold products "for which we
  are not the investment manager" (AUM footnotes D02-D10).
- Exclusions: long-term institutional flows exclude ETFs (D02-D08); net new assets exclude
  market/FX impact (D04 L31); D01 endnotes 11 (retention excludes an ETF client transition), 13
  (undisclosed contracted business excluded), 14 (FX new products within FX Sales and Trading
  only), 16 (loans ex-overdrafts); ARR excludes brokerage, affiliate and licensing revenue (all
  release definitions); industry data "not intended to reflect State Street or its clients'
  activity" (D02-D06); D09 reclassification "no impact on Total fee revenue, Total revenue or Net
  income"; capital ratios are State Street Corporation, not SSBT, unless noted (all releases).
- Hedge/condition attachments: D05 L28 uncertainty "around trade, deficits, tax, and
  deregulation" (global environment); D09 L28 "is uncertain" (macro and geopolitical
  environment); D06 L117 "subject to approval by the Board of Directors" (planned dividend); D10
  L90 "remains subject to applicable regulatory approvals" (Luxembourg capability); mandate
  conditions "may be subject to completion of definitive agreements" (D01 endnote 13; release
  definitions); confidence statements D09 L28, D10 L26.

### Narrative/overview passages repeating table results

- Every release: headline/tiles and the FINANCIAL HIGHLIGHTS table repeat the REVENUE/EXPENSES
  tables; "Highlights" bullets round one-decimal table changes to whole percents (see each
  document's "Rounded prose" line); boilerplate paragraphs repeat AUC/A and AUM rounded (D02 L385,
  D03 L391, D05 L375, D06 L393, D07 L341, D08 L345, D09 L366, D10 L359). D04 slide 3 repeats SSGA
  year-end AUM that also appears in D02/D03 AUM tables.

### Items found in only one document

- D10: medium-term targets mention; 10% 3Q26 dividend increase; SPYM Trump Accounts (Treasury,
  July 1, 2026); Luxembourg tokenized fund servicing; ARR last-month method; 2Q26 figures.
- D09: reclassification note; AUM restructure note; SPYM "#1 asset gathering ETF globally";
  ETF.com awards for ALLW and PRIV; 57 products and solutions.
- D08: Coller Capital; Groww; Digital Asset Platform launch; 134 products in 2025; 4Q24 ROTCE.
- D07: Euromoney 2025 8 categories; 39 products; Apex "recently announced".
- D06: planned 11% dividend; 28 Alpha live clients; fee operating leverage in bps; "sixth
  straight quarter".
- D05: 1Q24 columns (FDIC $130M notable, EPS $1.37); ~$86B Alpha-driven AUC/A wins.
- D04: SSGA revenue, pre-tax margin, NNA, organic growth 2022-2024; focus-area AUM/CAGRs;
  partnership areas; Interim CFO.
- D03: 4Q23 columns; 2024 Alpha total; wins goal met; deferred comp acceleration; acquisition and
  restructuring row.
- D02: 3Q23 columns; Euromoney 2024 4 awards; India JV consolidation quarters; 4% pro-forma
  headcount reduction.
- D01: FY2024 outlook and 2024 targets; FY2023 notable-item breakdown; 2020-2024E wins chart.

### Absent from the bundle (negative evidence, from full reading plus searches)

- No release (D02-D10) prints full-year 2024 or 2025 totals or any numeric guidance; D10 L26
  refers to medium-term targets without values; D10 L25 gives the 10% dividend increase without
  the new per-share amount.
- Not in bundle: 1Q24/2Q24 servicing fee revenue wins; any 1Q23/2Q23 data; 2024 FX volume growth,
  2024 revenue retention, Private Markets servicing fee growth or Alpha implementation-time
  outcomes (D01 L17/L19 targets); Institutional MMF exact rank after 2023 (D04 L11 "Top 10").
- Alpha: no bullet in D08 or D10; no live-client total after 2Q25 (D07 L78 gives "1 go-live").
- CFO named only in decks (D01 Aboaf, D04 Keating); releases quote only the CEO.
- D04 does not name the conference/event (file name only, L4).
- Market data and industry flow tables absent D07-D10; Addendum absent from every release.

### Detailed cross-edition log (chronological, as mapped; locations only)

  - 4Q23 Investment Management total net flows: D01 L21 "record total quarterly net inflows in
    4Q23 of $103B" vs D02 L237 4Q23 "Total flows, net $ 95" (column marked (1) "AUM for passive
    alternative investments has been revised from prior presentations", L243). D02 L22/L65 calls
    3Q24 $100B a "record".
  - India operations JVs: D01 L25 "Consolidated first operations joint venture in India" (FY2023)
    and endnote 23 L35 second consolidation "expected to be completed in 2Q24"; D02 L329 JVs
    "consolidated in 4Q23 and 2Q24".
  - Alpha mandates: D01 L17 "+6-8 new Alpha mandates targeted in 2024", "7 new Alpha mandates in
    2023"; D02 L65 "2 new mandate wins in 3Q24, for a total of 5 mandate wins year-to-date".
  - Servicing fee revenue wins: D01 L17 2023 $301M, 2024 target $350-400M; D02 L64 3Q24 $84M.
  - Fee operating leverage definition: D01 L41 and D02 L408 identical wording ("successive prior
    year period"); D03 L414 changes to "corresponding prior year period"; operating leverage
    (total revenue) defined D02 L407 / D03 L413 ("corresponding").
  - Alpha 2024: D01 L17 target "+6-8"; D03 L70 "total of 7 mandate wins in 2024".
  - Servicing fee revenue wins 2024: D01 L17 goal $350-400M; D02 L64 3Q24 $84M; D03 L68 4Q24
    $154M; D03 L28 "met our full-year ... goal of $350-400 million" (1Q24, 2Q24 amounts and the
    FY2024 total are not printed in D02/D03).
  - FY2024 outlook vs outcome: D01 L13/L15/L23 (fee revenue ~3-4%, positive fee operating
    leverage, expenses ex-notables) vs D03 L26 "exceeded the financial outlook we provided at the
    outset of 2024"; D03 prints no FY2024 columns.
  - 4Q23 notable items: D01 L23 FY2023 notable items $(620)M = FDIC $(387)M + net repositioning
    $(203)M + other (net) $(45)M + $15M acquisition/restructuring release; D03 L95-L112 4Q23 total
    (620) = FDIC (387) + "Repositioning charges and other notable items (net)" (233).
  - 3Q24 notable items presentation: D02 L96-L102 three rows (81)/66/15, total —; D03 L93-L101
    3Q24 column all "—" with footnote (c) L112 netting them to $0.
  - 3Q24 industry flows revised between editions: D02 L162-L172 (N. America LT (121), MM 278, ETF
    288, total 444; EMEA LT 76, MM 127, ETF 63, total 266; September estimated) vs D03 L166-L176
    (N. America (117)/230/288/401; EMEA 82/107/66/255). 2Q24, 1Q24, 4Q23 columns identical.
  - Same-period exact matches D02 vs D03 (3Q24): highlights, revenue, expenses, AUC/A, AUM,
    market data, capital ratios.
  - SSGA 2024 net new assets: D04 L13/L27 $144B; quarterly total flows 1Q24 (14), 2Q24 (6), 3Q24
    100 (D02 L237, D03 L241), 4Q24 64 (D03 L241). 2023 NNA $117B (D04); 4Q23 95, 3Q23 10 (D02
    L237); 1Q23-2Q23 not in bundle.
  - Organic AUM growth: D01 L21 FY2024 target ">2%" (endnote 22 L33: FY2024 NNA / total AUM at
    Dec 31, 2023) vs D04 L13 2024 organic growth "+3.5%" (definition L31).
  - Rankings across decks: D01 L15 "#4 Asset manager globally" (P&I Dec 31, 2022), "#4 in US
    Defined Contribution", Institutional MMF rank #8 with #7 target (L21, endnote 21) vs D04 L11
    "#4 global asset manager" (P&I Dec 31, 2023), "#4 U.S. retirement manager" (DC + DB), "Top 10
    institutional money market provider" (Dec 31, 2024). D01 "#1 ETF servicer" (servicing) vs D04
    "#3 ETF manager worldwide with $1.6T".
  - CFO naming: D01 L9 Eric Aboaf "Vice Chairman and Chief Financial Officer"; D04 L9 Mark Keating
    "Interim Chief Financial Officer".
  - Business naming: D01 "Investment Servicing" (Asset Services; Markets and Financing) and
    "Investment Management" (Global Advisors); D02/D03 tables "Investment Servicing"/"Investment
    Management", CEO prose "Investment Services"/"Global Advisors"/"Global Markets franchise";
    D04 L11 "Global Advisors", "Global Markets", "Investment Services".
  - AUM year-ends: D04 L13 $3.5T/$4.1T/$4.7T (2022-2024) vs D02/D03 4Q23 ending 4,102 and 4Q24
    4,715.
  - 4Q24 industry flows revised between editions: D03 L166-L176 (N. America LT (131), MM 355, ETF
    427, total 651; EMEA 92/71/81/244; December estimated) vs D05 L160-L170 (N. America
    (129)/376/427/673; EMEA 108/73/85/265). 3Q24 in D05 equals D03's revised values.
  - Revenue table structure: back office / middle office services rows printed only in D02 (L252,
    L254) and D03 (L256, L258) (bundle-wide search); D05-D10 print "Servicing fees" only.
  - Expense table "Acquisition and restructuring costs" row: D03 L317 only (bundle-wide search).
  - 1Q24 notable item FDIC special assessment $(130)M first appears in D05 L98 (1Q24 column).
  - Alpha mandate counts: 3Q24 2 (YTD 5) D02 L65; 4Q24 2 (2024 total 7) D03 L70; 1Q25 1 D05 L70.
  - Servicing fee revenue wins by quarter: 3Q24 $84M (D02 L64), 4Q24 $154M (D03 L68), 1Q25 $55M
    (D05 L68); to be installed $288M / $346M / $356M; AUC/A to be installed $2.4T / $3.0T / $3.1T.
  - Front office ARR series: 3Q23 $299M, 2Q24 $345M, 3Q24 $356M (D02 L400); 4Q23 $315M, 4Q24
    $375M (D03 L406); 1Q24 $326M, 1Q25 $373M (D05 L389).
  - Capital return by quarter: 3Q24 $674M ($450M buybacks) D02 L111; 4Q24 $770M ($550M) D03 L117;
    1Q25 $320M ($100M) D05 L105; 2Q25 $517M ($300M) D06 L117; dividends $0.76/share each quarter
    through 2Q25; D06 L117 planned increase to $0.84 in 3Q25 "subject to approval by the Board".
  - 1Q25 Advanced Approaches CET1: D05 L345 12.5 vs D06 L361 12.6 (both originals checked); other
    1Q25 capital ratios identical across D05/D06.
  - 1Q25 industry flows revised: D05 L160-L170 (N. America (149)/79/291/221; EMEA 96/70/94/260;
    March estimated) vs D06 L165-L175 (N. America (148)/100/291/243; EMEA 75/58/92/224).
  - Renaming: "State Street Global Advisors" (D02-D05 boilerplate) -> "State Street Investment
    Management" (D06 L29, L394); market-data "Specials Volumes" rows and highlights/revenue "Other
    income" row absent from D06; AUM flow row "Cash fund" -> "Cash" (D06 L217, L236).
  - Alpha live clients: D01 L17 "18 live clients at year-end 2023"; D06 L66 "total of 28 live
    clients to-date" (2Q25, 3 went live in 2Q25). Alpha mandates 2Q25: 2 (D06 L66).
  - FX benchmark litigation recoveries (2018 resolution): $15M 3Q24 (D02 L108), $3M 2Q25 (D06
    L107).
  - Employees: ~53,000 (D02 L385, D03 L391, D05 L375) -> ~52,000 (D06 L393, D07 L341).
  - Dividend proposal -> action: D06 L30/L117 planned 11% increase to $0.84 in 3Q25 "subject to
    approval by the Board of Directors" -> D07 L27 "As previously announced, we were pleased to
    increase ... by 11% to $0.84"; D07 L126 3Q25 declared dividends $237M ($0.84 per share).
  - Positive operating leverage streak (ex-notables): D06 L29 "sixth straight quarter of positive
    year-over-year total operating leverage"; D07 L25 "seventh consecutive quarter of positive
    operating leverage".
  - Alpha 2025: 1Q25 1 (D05 L70), 2Q25 2 (D06 L66), 3Q25 1 win + 1 go-live, "4 mandate wins
    year-to-date" (D07 L78).
  - Euromoney FX Awards: 2024 four categories (D02 L65, L78); 2025 "8 categories" (D07 L79).
  - Market data and industry flow tables: D02-D06 only; absent D07-D10 (searched).
  - Operating leverage stated in bps: D06 L24-L25 (YoY: total (341)/241 ex-notables; fee (75)/526
    ex-notables); D07 L32 total 332 bps; D08 L25/L40 total (487) bps, 105 bps ex-notables.
  - 4Q24 notable items recast: D03 L95-L101 rows deferred comp (79) / FDIC 31 / "Repositioning
    charges and other notable items (net)" (10) vs D08 L114-L120 repositioning (net) 2 / other
    notable (net) 19 / deferred comp (79); total (58) in both; components D03 L107-L108, D08
    L133-L135.
  - Expense line re-presentation: "Amortization of other intangible assets" row in D02-D07; folded
    into "Other" in D08 (4Q24 Other 326 in D03 L319 vs 380 in D08 L270; 3Q25 Other 317 in D07 L271
    vs 373 in D08 L270). 4Q24 adjusted Other expenses: D05 L327 "$345M" vs D08 L132 "$399
    million" (difference = 4Q24 amortization 54, D03 L318).
  - 2025 Investment Management new products: 3Q25 39 (D07 L26); 4Q25 37, 2025 total 134 (D08 L87).
  - Post-quarter events dated in D08 (4Q25 release): Groww partnership announced January 14, 2026;
    Digital Asset Platform launched January 15, 2026 (D08 L99).
  - ROTCE: tile only in D07 (20.9% 3Q25, L38); table row from D08 L65 (4Q25 17.5, 3Q25 20.9, 4Q24
    20.3).
  - Alpha bullet absent from D08 highlights (last count D07 L78: 4 mandate wins YTD 3Q25).
  - Apex Fintech Solutions: "recently announced partnership" (D07 L26, L79); "Strategic investment
    and partnership" (D08 L86).
  - 2025 quarterly IM total net flows (D08 L196): 1Q25 (13), 2Q25 82, 3Q25 26, 4Q25 85 (same in
    D09 L215).
  - 4Q25 Standardized CET1: D08 L305 (and L140, L324) 11.7% vs D09 L323 11.6% (D09 L125/L345
    "decreased 1.0% point compared to 4Q25" from 10.6). Both originals checked; other 4Q25 capital
    ratios identical.
  - 1Q26 revenue reclassification (D09 L99/L245) changes prior-period lines: 4Q25 management fees
    662 (D08 L212) -> 717 (D09 L230); FX 405 -> 350; software and processing 221 -> "Software
    services" 163 (= D08 front office software and data 163); other fee revenue 59 -> 117 (= 59 +
    lending related 58). 1Q25: management 562 (D05 L251) -> 587; FX 362 -> 337; software and
    processing 225 -> software services 158 (= D05 front office 158); other fee revenue 32 -> 99
    (= 32 + lending 67). Totals unchanged (2,862; 2,570).
  - 1Q25 expense "Other": D05 L307 276 (+ amortization 54, L306) vs D09 L288 330.
  - AUM disclosure restructured in D09 (strategy/vehicle/geography views; "Multi-Asset" label);
    earlier releases D02-D08 use product categories Equity/Fixed-Income/Cash/Multi-Asset Class
    Solutions/Alternative Investments and flow rows LT institutional/ETF/Cash (fund).
  - ETF flows by quarter: D07/D08 3Q25 ETF 37 vs D09 L210 Index ETFs 38 and memo ETF total 37;
    1Q25 ETF 1 (D05 L232) vs D09 Index ETFs — and memo 1.
  - Software ARR series continues: 4Q25 $418M (D08 L360, D09 L381), 1Q26 $418M (D09 L381);
    caption "Front office software and data" (D02-D08) -> "Software services" (D09).
  - Alpha bullet returns in D09 L81 ("1 new mandate win"); absent D08.
  - Employees ~51,000 (D09 L366).
  - Form 10-K cited in FLS: 2023 (D01-D03), 2024 (D04-D08), 2025 (D09, D10).
  - 2Q25 revenue lines across editions: D06 L254-L259 management 562, FX 431, software and
    processing 230 (front office 169 + lending 61), other fee revenue 66 vs D10 L220-L224
    management 600, FX 393, software services 169, other 127; total 2,719 both. 2Q25 adjusted FX:
    D06 L76 "$428 million" vs D10 L93 "$390 million".
  - 2Q25 client rescoping: D06 L92-L95 two rows (revenue (24), expense (18)) vs D10 L108 one row
    (42); D06 L105-L106/L77 "Alpha-related" vs D10 L120/L123 without "Alpha-related".
  - 2Q25 Other expenses: D06 L320 305 (+ amortization 56, L319) vs D10 L282 361; adjusted D06 L112
    "$306 million" vs D10 L121 "$362 million".
  - ARR recast (D10 L374 method change): 2Q25 $379M (D06 L407) -> $381M; 1Q26 $418M (D09 L381) ->
    $427M.
  - Geography label for the 845 row: D09 L176 "Europe/Middle East/Asia" vs D10 L167
    "Europe/Middle East/Africa" (same Mar 31, 2026 balance 845).
  - Operating leverage streak ex-notables: sixth (2Q25, D06 L29), seventh (3Q25, D07 L25), tenth
    (2Q26, D10 L24); D08/D09 give no count.
  - Dividend increases: 2025 "planned 11%" to $0.84 (D06) -> declared (D07); 2026 "recently
    declared a 10% per share increase to our third quarter common stock dividend" (D10 L25; amount
    not printed). Both tied in the text to Federal Reserve stress test results (D06 L30, D10 L25).
  - Medium-term targets referenced but not stated: D10 L26.
