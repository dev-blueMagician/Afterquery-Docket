# aq-00745 - document map

Written by `bundle-mapper` from `text/` (and `docs/`). Navigation only, like the form's bundle
overview: where things are, not what to ask. Questions quote the documents, never this map.
Two mapper passes share this file: pass A (earnings releases D01-D04, D07, D08, D10) and pass B
(D05, D06, D09, D11). Each pass edits only its own sections with Edit, never Write.

## Bundle

- What it is: "Abbott Quarterly Earnings and Litigation Releases" (task page AQ-00745, corporate
  filings): seven Abbott quarterly earnings releases (Q4/FY2024 through Q2 2026), the
  Abbott-Exact Sciences acquisition release, Abbott's amended and restated by-laws, a derivative
  settlement notice and a preterm infant formula litigation settlement release.
- Documents: 11; ids from `text/manifest.json`. Local Dnn = platform Doc N (both follow the file
  dates; capture headings "### Doc N · date · file" checked against the manifest at intake).
- Gaps: none since 2026-10-05. The complete capture AQ-00745_2026-10-06_0256.md ("11 of 11 captured
  in full") was re-ingested with split_capture.py --force; no gap marker remains (notes/intake.json
  keeps the clipped capture 9178797f... in its history). Before that, D01-D04, D07, D08 and D10 had
  128 clipped table ranges; passes A/B below were written on that clipped text.
- Line numbers: pass A sections for D01-D04, D07, D08 and D10 use the OLD clipped-text numbering;
  convert with notes/line-remap.md. D05, D06, D09 and D11 are byte-identical (no change).
- Table maps on current lines (pass C, 2026-10-05): notes/doc-map-tables-2025.md (D01-D04) and
  notes/doc-map-tables-2026.md (D07, D08, D10), each with read ledgers, every table, cross-release
  repeats/recasts, prose-vs-table notes, derived margins (2026 file S5) and layout notes.
- Extraction spot-checks: plain-text capture (no PDF pages). text/Dnn.txt = docs file plus a
  header line, NFKC-normalised (e.g. "…" -> "...", "™" -> "TM"); no text lost in extraction.
- Provenance: first capture AQ-00745_2026-10-05_0934.md (saved 2026-10-05 09:34, clipped tables);
  current capture AQ-00745_2026-10-06_0256.md (complete); split with tools/split_capture.py; hashes
  in notes/intake.json and text/manifest.json.

<!-- PASS A: D01 -->
## D01 - Abbott Q4 and Full-Year 2024 Earnings Release

- Source: docs/abt_ex991_2025-01-22.txt (793 lines) -> text/D01.txt (796 lines; text l.N = docs
  l.N-2). Exhibit 99.1, "abt-2024q4xexhibitx991.htm" (l.5); printed "Page 1 of 20" ... "Page 20 of 20" (l.47-795).
- Written or submitted by: Abbott ("ABBOTT PARK, Ill., Jan. 22, 2025 - Abbott today announced", l.21).
  Contacts l.347-357: Abbott Financial Michael Comilla, Tamika LeBean; Abbott Media Karen Twigg May,
  Kate Dyer. CEO quote: Robert B. Ford, "chairman and chief executive officer" (l.43).
- Type, date, edition: news release / 8-K Ex. 99.1, dated Jan. 22, 2025. Headline l.15 "Abbott Reports
  Fourth-Quarter and Full-Year 2024 Results; Issues 2025 Financial Outlook".
- Period covered: quarter "ended Dec. 31, 2024" (l.21); 4Q24 vs 4Q23 and 12M24 vs 12M23. Calendar
  fiscal year (statements "Twelve Months Ended December 31", l.443). Labels 4Q24/12M24/4Q23/12M23.
- Entities and aliases: Abbott / "Abbott Laboratories and Subsidiaries" (l.401). Segments Nutrition
  (Pediatric, Adult), Diagnostics (Core Laboratory, Molecular, Point of Care, Rapid Diagnostics),
  Established Pharmaceuticals (Key Emerging Markets, Other), Medical Devices (Rhythm Management,
  Electrophysiology, Heart Failure, Vascular, Structural Heart, Neuromodulation, Diabetes Care).
  Brands l.133 Ensure, Glucerna; l.281 FreeStyle Libre, Navitor, TriClip, Amplatzer Amulet, AVEIR.
  CSI (acquired April 27, 2023, l.101/307/661); ZonePerfect product line (discontinued, initiated
  March 2024, l.101/153/663). "S&P 500 Dividend Aristocrats Index" (l.327). EU MDR / IVDR (l.697).
- Tables ($ in millions unless noted; growth % one decimal; parentheses = negative):
  - l.57-77 total company 4Q24 sales by segment (U.S./Intl/Total; Total 10,974; Nutrition 2,129;
    Diagnostics 2,520; EPD 1,268; MD 5,052); % change rows: U.S. reported, [gap l.69], "Impact of
    COVID-19 testing sales" (1.3), "Organic (excluding COVID-19 tests)" 10.1 / U.S. 13.5 / Intl 8.1.
  - l.81-99 total company 12M24 (Total 41,950; U.S. 16,323; Intl 25,627; MD 18,986); [gap l.91];
    COVID impact (2.5); organic excl. COVID 9.6 / U.S. 10.9 / Intl 8.8.
  - Nutrition 4Q24 l.111-127 [gap l.123] and 12M24 l.137-153 [gap l.149]; rows after each gap are the
    organic U.S./Intl rows (their heading falls inside the gap).
  - Diagnostics 4Q24 l.163-179 [gap l.171] (Rapid Dx organic excl. COVID 16.4) and 12M24 l.189-207
    [gap l.201].
  - EPD 4Q24 l.217-231 [gap l.227]; 12M24 l.239-255 [gap l.251].
  - Medical Devices 4Q24 l.265-277 [gap l.273]; 12M24 l.289-305 [gap l.301] (Diabetes Care 12M24
    6,805; Vascular U.S. reported 8.0 vs organic 2.5 because of CSI).
  - Footnote-3 Diagnostics/COVID test sales tables l.363-395: all four data rows are gaps (l.371,
    379, 387, 395).
  - Statement of earnings 4Q24 l.401-419 (top rows = gap l.405; EBT 2,030 vs 1,795; taxes (7,199)
    vs 201; net earnings $9,229 vs $1,594; diluted EPS $5.27 vs $0.91; adjusted $1.34 vs $1.19,
    +12.6%; shares 1,746 vs 1,748). 12M l.443-461 (top rows = gap l.447; EBT 7,013 vs 6,664; taxes
    (6,389) vs 941; NE $13,402 vs $5,723; EPS $7.64 vs $3.26; adjusted $4.67 vs $4.44, +5.2%).
  - Non-GAAP EPS reconciliations l.487-541: only the intangible amortization row survives in each
    (465/481/1,878/1,966); remaining rows = gaps l.497, 509, 527, 539; prose under each gives
    amortization + "other net expenses" ($268m 4Q24, $159m 4Q23, $755m 12M24, $442m 12M23).
  - Tax-rate reconciliations l.547-613 (complete): 4Q24 GAAP (354.6%) / excl. specified 15.0%;
    4Q23 11.2% / 14.0%; 12M24 (91.1%) / 15.0%; 12M23 14.1% / 14.0%. Specified-items pre-tax
    733/640/2,633/2,408 (l.561/577/595/611).
  - Non-GAAP revenue reconciliation l.623-663 (complete): 4Q24/4Q23 and 12M24/12M23 reported,
    acquisition (a) and business-exit (b) adjustments, adjusted revenue, reported/adjusted/organic %
    for Total, U.S., Intl, Nutrition, Adult Nutrition, Medical Devices, Vascular (e.g. 4Q23 total
    10,241 -> adjusted 10,224; 12M23 40,109 -> 40,060).
  - Details of specified items l.669-791: body rows = gaps l.685, 715, 745, 775; surviving totals:
    4Q24 taxes 7,613, net $(6,880), EPS $(3.93); 4Q23 140/$500/$0.28; 12M24 7,835/$(5,202)/$(2.97);
    12M23 329/$2,079/$1.18.
- Lists: l.35 "more than 15 new growth opportunities" (not enumerated). Brand list l.281 (5 items).
  Contacts l.347-357 (4 people).
- Forecasts, guidance, deadlines, effective dates: 2025 guidance first issued here (headline l.19,
  bullets l.37-41, section l.313-321): FY2025 organic sales growth "7.5% to 8.5%"; FY2025 adjusted
  operating margin "23.5% to 24.0% of sales" ("increase of 150 basis points at the midpoint compared
  to 2024", l.39); FY2025 adjusted diluted EPS "$5.05 to $5.25" ("double-digit growth at the
  midpoint", l.41); "first-quarter 2025 adjusted diluted earnings per share of $1.05 to $1.09"
  (l.319). No prior range printed; no raise/narrow language (new year). l.33: FY2024 achieved "the
  upper end of the initial guidance ranges the company provided in January 2024" (the 2024 ranges
  are not printed). l.321: GAAP equivalents not provided for forward-looking non-GAAP measures.
  Dividend l.323-327: "404th CONSECUTIVE QUARTERLY DIVIDEND"; declared "Dec. 13, 2024", "$0.59 per
  share", "payable Feb. 14, 2025", record "Jan. 15, 2025"; "increased its dividend payout for 53
  consecutive years". Call: 8:30 a.m. Central time, "today" (l.335).
- Hedged claims: forward-looking caution l.345 ("may be forward-looking statements"; risks "may
  cause actual results to differ"; cites Form 10-K for year ended Dec. 31, 2023). l.321 items
  "could significantly impact" GAAP results. l.51 "Management believes" organic measures are
  appropriate. l.43 Ford: "well-positioned to deliver another year of strong growth in 2025".
- Rounded prose beside exact figures: headline/bullets "$11.0 billion" and "$42.0 billion" (l.17,
  27) vs 10,974 / 41,950 (l.63, 85) and footnotes "$10.974 billion", "$41.950 billion" (l.359,
  361). l.285 MD full-year "$19 billion and increased more than $2 billion" vs 18,986 vs 16,887
  (l.295, 657). l.283 CGM sales "$1.8 billion" (+22.7% reported, +22.8% organic) vs Diabetes Care
  column 1,863 (l.267; CGM is not a table row). COVID testing sales $176m vs $288m (l.181, 359);
  FY $747m vs $1.586 billion (l.361). Q4 organic incl. COVID 8.8% appears in prose l.23 and in the
  revenue reconciliation l.635 (the main-table row is in gap l.69).
- Notes: tax footnotes l.433/475/615: "2024 Taxes on Earnings includes $7.497 billion in non-cash
  valuation allowance adjustments resulting from the restructuring of certain foreign affiliates and
  the confirmation of certain tax filing positions." Prior-year tax item l.477/617: "2023 Taxes on
  Earnings includes the recognition of approximately $80 million of net tax expense as a result of
  the resolution of various tax positions related to prior years." Specified-items footnotes: 4Q24
  net after-tax benefits "$6.880 billion, or $3.93 per share" (l.435); 4Q23 charges "$500 million,
  or $0.28" (l.437); 12M24 benefits "$5.202 billion, or $2.97 per share" incl. "acquisitions and a
  divestiture" (l.479); 12M23 charges "$2.079 billion, or $1.18" (l.481). 12M24 specified (a)
  "Includes the loss on the sale of a non-core business" (l.753). Employees "114,000 colleagues",
  "more than 160 countries" (l.331). No litigation item and no Exact Sciences mention found.
- Operative definitions, rules and scope exceptions: organic basis "excludes the impact of foreign
  exchange and the impact of discontinuing the ZonePerfect(R) product line in the Nutrition
  business" (l.51); organic excl. COVID-19 tests reflects "underlying base business performance in
  2024" (l.51); FX method note l.53; CSI excluded from organic "from January through April 2024"
  (l.101, 307, 661). Specified-item category footnotes a)-d) l.693-699, 723-729, 753-759, 785-791
  (wording differs by period, e.g. 12M24 (c) "investment and intangible asset impairments").
- Amendments or contradictions: none internal found; four repeated tax/specified-item footnotes
  agree. Pre-tax specified items equal amortization + other net expenses (465+268=733 etc.).
- Coverage: FULL for readable text: l.1-796 read in one pass (l.1-796 inspected incl. all tables
  and footnotes). Missing source text (24 markers, 5,198 characters total): l.69, 91, 123, 149,
  171, 201, 227, 251, 273, 301 (segment sales-growth % rows between the U.S. reported row and the
  organic rows: Intl/Total reported, organic headings), l.371, 379, 387, 395 (COVID test-sales
  table rows), l.405, 447 (statement-of-earnings top rows: sales through other line items), l.497,
  509, 527, 539 (EPS reconciliation rows after amortization), l.685, 715, 745, 775 (specified-items
  detail rows). Spot-check vs docs original: line count 793 (+header), 4Q24 "Total reported 10,974
  ..." row (docs l.61 = text l.63), tax footnote "$7.497 billion" (docs l.431 = text l.433) and the
  24 markers match.

<!-- PASS A: D02 -->
## D02 - Abbott Q1 2025 Earnings Release

- Source: docs/abt_ex991_2025-04-16.txt (433 lines) -> text/D02.txt (436 lines; text l.N = docs
  l.N-2). Ex. 99.1 "abt-2025q1xexhibitx991.htm" (l.5); "Page 1 of 15" ... "Page 15 of 15" (l.39-435).
- Written or submitted by: Abbott ("ABBOTT PARK, Ill., April 16, 2025 - Abbott today announced",
  l.21). Contacts l.227-239: Abbott Financial Michael Comilla, Tamika McLoughlin (224-399-5082, the
  same number printed for "Tamika LeBean" in D01 l.351), Randy Blakley (new); Abbott Media Karen
  Twigg May, Kate Dyer. CEO quote Robert B. Ford (l.37).
- Type, date, edition: news release, April 16, 2025. Headline l.15 "Abbott Reports First-Quarter
  2025 Results and Reaffirms Full-Year Guidance".
- Period covered: "first quarter ended March 31, 2025" (l.21); 1Q25 vs 1Q24 only (no year-to-date
  columns).
- Entities and aliases: segment/sub-business names as D01. Products/programs: Volt(TM) PFA System
  (CE Mark, l.29); TECTONIC U.S. pivotal trial for "Coronary Intravascular Lithotripsy (IVL)
  System" (l.31); TRILUMINATE(TM) pivotal trial / TriClip(TM) (l.33); Ensure, Glucerna (l.103);
  FreeStyle Libre, Navitor, TriClip, Amplatzer Amulet, AVEIR (l.189). China "volume-based
  procurement programs" (l.131, 135).
- Tables ($ in millions; growth % one decimal):
  - l.49-65 total company 1Q25 (Total 10,358; U.S. 4,168; Intl 6,190; Nutrition 2,146;
    Diagnostics 2,054; EPD 1,260; MD 4,895); U.S. reported row, [gap l.61], then organic U.S. 8.8 /
    Intl 5.7 rows. No COVID-impact row survives in this table.
  - Nutrition l.79-97 [gap l.91]; Diagnostics l.111-127 [gap l.123] (Rapid Dx U.S. (16.9), Intl
    (14.6) organic); EPD l.143-159 [gap l.155]; MD l.171-183 [gap l.179] (Diabetes Care 1,827).
  - Statement of earnings l.245-271 (top rows gap l.257; EBT 1,778 vs 1,436, +23.8%; taxes 453 vs
    211; NE $1,325 vs $1,225, +8.2%; EPS $0.76 vs $0.70; adjusted $1.09 vs $0.98, +11.2%; NE excl.
    specified $1,919 vs $1,729; shares 1,747 vs 1,750).
  - Non-GAAP EPS reconciliation l.293-317: amortization rows 420 (1Q25) / 472 (1Q24); rest = gaps
    l.303, 315; prose: other net expenses $100m (1Q25), $127m (1Q24).
  - Tax-rate reconciliation l.321-357 (complete): 1Q25 GAAP 25.5%, excl. specified 16.5%
    (specified items pre-tax 520, tax (74)); 1Q24 14.7% / 15.0% (599, 95).
  - Revenue reconciliation l.361-375 (complete): 1Q24 total 9,964 less business exit (13) = 9,951;
    Nutrition, Adult Nutrition rows; no acquisition column.
  - Specified-items details l.379-433: body rows = gaps l.389, 417; totals 1Q25 tax (74), net
    $594, EPS $0.33; 1Q24 95 / $504 / $0.28.
- Lists: l.29-35 four dated/undated pipeline/investment bullets; l.187 MD growth "led by Diabetes
  Care, Structural Heart, Heart Failure and Electrophysiology"; brand list l.189 (5 items); contacts
  (5 people).
- Forecasts, guidance, deadlines, effective dates: l.27 "Abbott reaffirms all previously provided
  full-year 2025 financial guidance" (headline l.15 "Reaffirms"). Section l.195-203: FY2025 organic
  sales growth "7.5% to 8.5%"; adjusted operating margin "23.5% to 24.0% of sales"; FY2025 adjusted
  diluted EPS "$5.05 to $5.25"; "second-quarter 2025 adjusted diluted earnings per share of $1.23
  to $1.27" (l.201). Q1 actual adjusted EPS $1.09 (l.17, 269) vs D01's Q1 range $1.05-$1.09 (D01
  l.319). l.35 investments in Illinois and Texas "totaling $0.5 billion, are projected to go live
  by the end of 2025". l.29 Volt "will further expand ... throughout the second half of the year".
  Dated events: "In March" Volt CE Mark ("earlier-than-expected", l.29); "In March" TECTONIC trial
  initiation (l.31); "In March" TRILUMINATE two-year data (l.33). Dividend l.205-209: "405th";
  declared "Feb. 21, 2025", "$0.59", payable "May 15, 2025", record "April 15, 2025"; "53
  consecutive years". Call 8 a.m. Central time (l.217).
- Hedged claims: l.35 "projected to go live by the end of 2025"; forward-looking caution l.225
  (cites Form 10-K for year ended Dec. 31, 2024); l.203 "could significantly impact"; l.37 Ford
  "navigate through periods of uncertainty".
- Rounded prose beside exact figures: l.191 CGM "$1.7 billion" (+18.3% reported, +21.6% organic) vs
  Diabetes Care column 1,827 (l.173). Footnote 1 l.241 gives exact $10.358bn / $9.964bn totals,
  Diagnostics $2.054bn / $2.214bn, COVID $84m / $204m, COVID impact "decrease of 1.4 percent and
  5.4 percent", organic excl. COVID 8.3% (Abbott) and 0.5% (Diagnostics). Margins prose only
  (headline l.19): gross 52.8% reported / 57.1% adjusted (+140 bp); operating 16.3% / 21.0% (+130
  bp).
- Notes: tax footnotes l.283/355/403: "2025 Taxes on Earnings includes approximately $200 million in
  adjustments related to prior recognition of a significant non-cash deferred tax benefit."
  Prior-year item l.285/357: "2024 Taxes on Earnings includes the recognition of approximately $10
  million of net tax expense as a result of the resolution of various tax positions related to
  prior years." Specified items 1Q25 "$594 million, or $0.33 per share" incl. "charges related to
  investment impairments" (l.287); 1Q24 "$504 million, or $0.28" (l.289). Specified (a) 1Q25 adds
  "a fair value adjustment to contingent consideration related to a business acquisition" (l.397);
  (c) "investment impairment charges" (l.401). No litigation item; no Exact Sciences mention.
- Operative definitions, rules and scope exceptions: organic definition l.43 = D01 l.51 first
  sentence (FX + ZonePerfect); the D01 sentence on organic "excluding COVID-19 tests" is absent
  here, though excl.-COVID growth is still reported (l.19, 23, 71, 129, 241). FX note l.45.
  ZonePerfect footnotes l.69, 97, 375.
- Amendments or contradictions: none internal found. Guidance unchanged from D01 (stated
  "reaffirms").
- Coverage: FULL for readable text: l.1-436 read in one pass. Missing source text (10 markers,
  2,192 characters): l.61, 91, 123, 155, 179 (segment % rows after U.S. reported row), l.257
  (statement-of-earnings top rows), l.303, 315 (EPS reconciliation rows), l.389, 417 (specified
  detail rows). Spot-check vs docs: 433 lines (+header), "Total reported 10,358 ..." (docs l.53 =
  text l.55), $200 million tax footnote (docs l.281 = text l.283), 10 markers match.

<!-- PASS A: D03 -->
## D03 - Abbott Q2 2025 Earnings Release

- Source: docs/abt_ex991_2025-07-17.txt (697 lines) -> text/D03.txt (700 lines; text l.N = docs
  l.N-2). Ex. 99.1 "abt-2025q2xexhibitx991.htm" (l.5); "Page 1 of 20" ... "Page 20 of 20" (l.43-699).
- Written or submitted by: Abbott ("ABBOTT PARK, Ill., July 17, 2025 - Abbott today announced",
  l.21). Contacts l.325-337 identical to D02 (Comilla, McLoughlin, Blakley; Twigg May, Dyer). CEO
  quote Robert B. Ford (l.41).
- Type, date, edition: news release, July 17, 2025. Headline l.15 "Abbott Reports Second-Quarter
  2025 Results" (no guidance verb in headline).
- Period covered: "second quarter ended June 30, 2025" (l.21); 2Q25 vs 2Q24 and first half 1H25 vs
  1H24 (statements "First Half Ended June 30", l.395).
- Entities and aliases: segments as D01. Programs/products: FlexPulse U.S. IDE trial / TactiFlex(TM)
  Duo PFA System (l.33); AVEIR(TM) Conduction System Pacing (CSP) feasibility study (l.35);
  Tendyne(TM) TMVR system, "U.S. Food and Drug Administration (FDA)" approval (l.37); Georgia
  cardiovascular device manufacturing facility (l.39); brand list l.267 "FreeStyle Libre(R),
  Navitor(R), TriClip(R) and AVEIR(R)" (4 items; Amplatzer Amulet absent vs D01/D02).
- Tables ($ in millions; % one decimal):
  - l.53-75 total company 2Q25 (Total 11,142; U.S. 4,276; Intl 6,866; Nutrition 2,212; Diagnostics
    2,173; EPD 1,383; MD 5,369); U.S. reported, [gap l.65], "Impact of COVID-19 testing sales 1"
    (0.6)/Dx (2.2), "Organic (excluding COVID-19 tests)" 7.5 3.4 0.8 7.7 12.2, then an explicit
    "Organic" label (l.71) with U.S. 8.7 / Intl 5.8 rows.
  - l.79-99 1H25 (Total 21,500; U.S. 8,444; Intl 13,056; MD 10,264); [gap l.89]; COVID impact (1.0);
    organic excl. COVID 7.9; "Organic" U.S. 8.7 / Intl 5.8.
  - Nutrition 2Q25 l.111-127 [gap l.123], 1H25 l.135-149 [gap l.145]; Diagnostics 2Q25 l.157-169
    [gap l.165], 1H25 l.181-195 [gap l.193]; EPD 2Q25 l.203-217 [gap l.213], 1H25 l.225-241 [gap
    l.237]; MD 2Q25 l.249-261 [gap l.257] (Diabetes Care 1,981), 1H25 l.273-289 [gap l.285]
    (Diabetes Care 3,808).
  - Statement of earnings 2Q25 l.345-371 (top rows incl. net FX = gap l.357; other (income)
    expense (137) vs 10; EBT 2,150 vs 1,607; taxes 371 vs 305; NE $1,779 vs $1,302; EPS $1.01 vs
    $0.74; adjusted $1.26 vs $1.14, +10.5%; shares 1,751 / 1,751). 1H l.393-413 (gap l.401; EBT
    3,928 vs 3,043; taxes 824 vs 516; NE $3,104 vs $2,527; EPS $1.77 vs $1.44; adjusted $2.35 vs
    $2.12; NE excl. specified $4,132 vs $3,732).
  - EPS reconciliations l.435-487: amortization 420 (2Q25), 471 (2Q24), 840 (1H25), 943 (1H24);
    other rows = gaps l.445, 457, 473, 485; other net expenses $80m, $278m, $180m, $405m (prose
    l.447, 459, 475, 487).
  - Tax-rate reconciliations l.491-565 (complete): 2Q25 GAAP 17.3%, excl. specified 16.5%
    (specified 500 / 66); 2Q24 19.0% / 15.0% (749 / 48); 1H25 21.0% / 16.5% (1,020 / (8)); 1H24
    17.0% / 15.0% (1,348 / 143).
  - Revenue reconciliation l.569-583: first half only (1H24 20,341 less (13) = 20,328; Nutrition,
    Adult Nutrition). No 2Q revenue reconciliation printed.
  - Specified-items details l.587-697: body rows = gaps l.597, 625, 653, 681; totals 2Q25 tax 66,
    net $434, EPS $0.25; 2Q24 48 / $701 / $0.40; 1H25 (8) / $1,028 / $0.58; 1H24 143 / $1,205 /
    $0.68.
- Lists: dated pipeline bullets l.33-39 (April x2, May, undated Georgia plan); MD growth "led by
  double-digit growth in Diabetes Care, Heart Failure, Structural Heart and Electrophysiology"
  (l.265).
- Forecasts, guidance, deadlines, effective dates: bullets l.29-31 and section l.293-301. FY2025
  organic sales growth now stated on two bases: "excluding COVID-19 testing-related sales, to be
  7.5% to 8.0%, or 6.0% to 7.0% when including COVID-19 testing-related sales" (l.29, 295; D01/D02
  stated "7.5% to 8.5%" with no COVID basis). Adjusted operating margin "approximately 23.5% of
  sales" (l.297; D01/D02 "23.5% to 24.0%"). FY2025 adjusted diluted EPS "$5.10 to $5.20" (l.31,
  299; D01/D02 "$5.05 to $5.25"); "third-quarter 2025 adjusted diluted earnings per share of $1.28
  to $1.32" (l.299). No raise/narrow/lower/reaffirm verb and no prior range printed. Q2 actual
  adjusted EPS $1.26 (l.17) vs D02 Q2 range $1.23-$1.27 (D02 l.201). Dated events: "In April"
  FlexPulse enrollment completed "ahead of schedule" (l.33); "In April" AVEIR CSP late-breaking
  data (l.35); "In May" FDA approval of Tendyne (l.37); Georgia facility "to be completed by 2028"
  (l.39). Dividend l.303-307: "406th"; declared "June 13, 2025", "$0.59", payable "Aug. 15,
  2025", record "July 15, 2025"; "53 consecutive years". Ford l.41: "We see this momentum carrying
  into 2026."
- Hedged claims: forward-looking caution l.323 (Form 10-K for year ended Dec. 31, 2024); l.301
  "could significantly impact"; operating-margin guidance "approximately" (l.297).
- Rounded prose beside exact figures: CGM "$1.9 billion" (+21.4% reported, +19.6% organic, l.269)
  vs Diabetes Care column 1,981 (l.251). Footnotes l.339-341 exact totals: 2Q25 $11.142bn /
  Diagnostics $2.173bn / COVID $55m; 2Q24 $10.377bn / $2.195bn / $102m; 1H25 $21.500bn / $4.227bn
  / $139m; 1H24 $20.341bn / $4.409bn / $306m. Margins prose only (l.19): gross 52.7% / adjusted
  57.0% (+100 bp); operating 18.4% / adjusted 22.9% (+100 bp). First-half growth 5.7% / 6.9% /
  7.9% (l.27).
- Notes: tax footnotes 2Q (l.383, 525): "approximately $90 million of net tax benefit as a result of
  the resolution of various tax positions related to prior years" plus "approximately $100
  million in adjustments related to prior recognition of a significant non-cash deferred tax
  benefit"; 1H (l.425, 563): $90 million benefit plus "approximately $300 million" adjustments.
  Prior year: 2Q24 "approximately $25 million of net tax expense" (l.385, 527); 1H24 "approximately
  $35 million" (l.427, 565). Specified items: 2Q25 "$434 million, or $0.25 per share" (l.387); 2Q24
  "$701 million, or $0.40" incl. "acquisitions and a divestiture" (l.389); 1H25 "$1.028 billion, or
  $0.58" (l.429); 1H24 "$1.205 billion, or $0.68" (l.431). 2Q24 and 1H24 details (a): "Includes
  the loss on the sale of a non-core business" (l.633, 691). 2Q24 (c) "an intangible asset
  impairment charge" (l.637). No litigation item; no Exact Sciences mention.
- Operative definitions, rules and scope exceptions: organic definition l.47 (FX + ZonePerfect) plus
  a reinstated, reworded COVID sentence: organic "excluding COVID-19 tests is an appropriate way
  ... as the demand for COVID-19 tests has significantly declined following the transition from a
  pandemic to endemic phase" (D01 l.51 wording: "underlying base business performance in 2024";
  absent in D02). Table layout: geography rows here sit under an explicit "Organic" label (l.71,
  95), whereas D01's geography rows follow the "Organic (excluding COVID-19 tests)" row with no
  visible label (D01 l.73-77).
- Amendments or contradictions: guidance figures differ from D01/D02 (above); D03 does not label the
  change. Internal footnotes agree; quarterly items sum to first-half items (e.g. $200m + $100m =
  $300m deferred-tax adjustments; $594m + $434m = $1.028bn specified).
- Coverage: FULL for readable text: l.1-700 read in one pass. Missing source text (20 markers, 4,344
  characters): l.65, 89, 123, 145, 165, 193, 213, 237, 257, 285 (segment % rows), l.357, 401
  (statement-of-earnings top rows), l.445, 457, 473, 485 (EPS reconciliation rows), l.597, 625,
  653, 681 (specified detail rows). Spot-check vs docs: 697 lines (+header), "Total reported 11,142
  ..." (docs l.57 = text l.59), $90 million tax footnote (docs l.381 = text l.383), 20 markers
  match.

<!-- PASS A: D04 -->
## D04 - Abbott Q3 2025 Earnings Release

- Source: docs/abt_ex991_2025-10-15.txt (683 lines) -> text/D04.txt (686 lines; text l.N = docs
  l.N-2). Ex. 99.1 "abt-2025q3xexhibitx991.htm" (l.5); "Page 1 of 20" ... "Page 20 of 20" (l.41-685).
- Written or submitted by: Abbott ("ABBOTT PARK, Ill., Oct. 15, 2025 - Abbott today announced",
  l.21). Contacts l.313-325: Comilla, McLoughlin, Randy Blakley now "224-668-0036" (D02/D03:
  224-361-7966); Twigg May, Dyer. CEO quote Robert B. Ford (l.39).
- Type, date, edition: news release, Oct. 15, 2025. Headline l.15 "Abbott Reports Third-Quarter 2025
  Results and Reaffirms Full-Year Guidance".
- Period covered: "third quarter ended Sept. 30, 2025" (l.21); 3Q25 vs 3Q24 and nine months 9M25
  vs 9M24 ("Nine Months Ended September 30", l.377).
- Entities and aliases: segments as D01. Products/events: TriClip(R) approval "in Japan" (l.33);
  Navitor(R) TAVI system CE Mark expanded indication (l.35); "European Society of Cardiology (ESC)
  Congress" where "new treatment guidelines were issued" supporting MitraClip(R) and TriClip (l.37;
  the guidelines are not stated as issued by Abbott). China "challenging market conditions ...
  including the impact of volume-based procurement programs" (l.173). No brand-list sentence.
- Tables ($ in millions; % one decimal):
  - l.51-73 total company 3Q25 (Total 11,369; U.S. 4,299; Intl 7,070; Nutrition 2,153;
    Diagnostics 2,253; EPD 1,511; MD 5,448); U.S. reported, [gap l.63], COVID impact (2.0)/Dx (8.2),
    organic excl. COVID 7.5 4.0 0.4 7.1 12.5, "Organic" U.S. 2.3 / Intl 7.6.
  - l.77-97 9M25 (Total 32,869; U.S. 12,743; Intl 20,126; MD 15,712); [gap l.87]; COVID impact
    (1.3); organic excl. COVID 7.7; "Organic" U.S. 6.5 / Intl 6.4.
  - Nutrition 3Q25 l.109-125 [gap l.121] (U.S. (6.5) reported; Pediatric U.S. (8.4)), 9M25
    l.133-147 [gap l.143]; Diagnostics 3Q25 l.155-167 [gap l.163] (Rapid Dx U.S. (33.5)), 9M25
    l.177-191 [gap l.189]; EPD 3Q25 l.199-213 [gap l.209], 9M25 l.221-237 [gap l.233]; MD 3Q25
    l.245-257 [gap l.253] (Diabetes Care 2,057), 9M25 l.267-281 [gap l.277] (Diabetes Care 5,865).
  - Statement of earnings 3Q25 l.333-357 (gap l.345; EBT 2,180 vs 1,940; taxes 536 vs 294; NE
    $1,644 vs $1,646, (0.1)%; EPS $0.94 vs $0.94; adjusted $1.30 vs $1.21, +7.4%; shares 1,749 vs
    1,748). 9M l.377-393 (gap l.381; EBT 6,108 vs 4,983; taxes 1,360 vs 810; NE $4,748 vs $4,173;
    EPS $2.70 vs $2.38; adjusted $3.65 vs $3.33, +9.6%; NE excl. specified $6,410 vs $5,851).
  - EPS reconciliations l.415-467: amortization 420 (3Q25), 470 (3Q24), 1,260 (9M25), 1,413
    (9M24); other rows = gaps l.425, 437, 453, 465; other net expenses $128m, $82m, $308m, $487m.
  - Tax-rate reconciliations l.471-543 (complete): 3Q25 GAAP 24.6%, excl. specified 16.5% (548 /
    (86)); 3Q24 15.2% / 15.0% (552 / 79; no footnote); 9M25 22.3% / 16.5% (1,568 / (94)); 9M24
    16.3% / 15.0% (1,900 / 222).
  - Revenue reconciliation l.547-561: nine months only (9M24 30,976 less (13) = 30,963; Nutrition,
    Adult Nutrition).
  - Specified-items details l.565-683: body rows = gaps l.575, 603, 639, 667, except 3Q24 EBT row
    survives at l.605 ("$ 12 $ - $ 470 $ 70 552"); totals 3Q25 tax (86), net $634, EPS $0.36; 3Q24
    79 / $473 / $0.27; 9M25 (94) / $1,662 / $0.95; 9M24 222 / $1,678 / $0.95.
- Lists: dated bullets l.33-37 (July, August, August); MD growth "led by double-digit growth in
  Diabetes Care, Electrophysiology, Rhythm Management, Heart Failure and Structural Heart" (l.261).
- Forecasts, guidance, deadlines, effective dates: bullets l.29-31 and section l.285-289: "Abbott
  reaffirms previously provided full-year 2025 organic sales growth guidance of 7.5% to 8.0%,
  excluding COVID-19 testing-related sales, or 6.0% to 7.0%, when including COVID-19
  testing-related sales" (l.287; reaffirmed range printed). "Abbott also reaffirms the midpoint of
  the previously provided full-year 2025 adjusted diluted EPS guidance range and narrows the range
  to $5.12 to $5.18" (l.287; prior range not printed; D03 range $5.10-$5.20). No operating-margin
  guidance and no fourth-quarter EPS guidance printed (D01-D03 each gave a next-quarter range). Q3
  actual adjusted EPS $1.30 (l.17) vs D03 Q3 range $1.28-$1.32 (D03 l.299). Dated events: "In July"
  Japan approval for TriClip (l.33); "In August" Navitor CE Mark (l.35); "In August" ESC
  guidelines (l.37). Dividend l.291-295: "407th"; declared "Sept. 19, 2025", "$0.59", payable
  "Nov. 17, 2025", record "Oct. 15, 2025" (same day as the release); "53 consecutive years".
- Hedged claims: forward-looking caution l.311 (Form 10-K for year ended Dec. 31, 2024); l.289
  "could significantly impact".
- Rounded prose beside exact figures: CGM "$2.0 billion" (+20.5% reported, +17.2% organic, l.263)
  vs Diabetes Care 2,057 (l.247). Footnotes l.327-329: 3Q25 $11.369bn / Dx $2.253bn / COVID $69m;
  3Q24 $10.635bn / $2.412bn / $265m; 9M25 $32.869bn / $6.480bn / $208m; 9M24 $30.976bn / $6.821bn /
  $571m. Margins prose only (l.19): operating 18.1% reported / 23.0% adjusted (+40 bp); no gross
  margin bullet. YTD growth 6.1% / 6.4% / 7.7% (l.27). Adjusted EPS bullet l.25 has no growth
  claim (D02/D03 bullets said "double-digit growth"; table +7.4%, l.355).
- Notes: 3Q tax footnote l.369/505: "2025 Taxes on Earnings also includes approximately $160
  million in adjustments related to prior recognition of a significant non-cash deferred tax
  benefit" (begins "also" with no first item; no 3Q24 tax footnote). 9M l.405/541: "$90 million of
  net tax benefit" (prior-year positions) plus "approximately $460 million" adjustments; 9M24
  "$35 million of net tax expense" (l.407, 543). Specified items 3Q25 "$634 million, or $0.36 per
  share" (l.371); 3Q24 "$473 million, or $0.27" incl. "intangible impairment" and "a divestiture"
  (l.373); 9M25 "$1.662 billion, or $0.95" (l.409); 9M24 "$1.678 billion, or $0.95" (l.411). 9M24
  details (a) "Includes the loss on the sale of a non-core business" (l.677). No litigation item; no
  Exact Sciences mention.
- Operative definitions, rules and scope exceptions: organic definition l.45 verbatim as D03 l.47
  (FX + ZonePerfect; excl. COVID sentence with "pandemic to endemic phase"). FX note l.47.
  Geography rows under "Organic" label (l.69, 93).
- Amendments or contradictions: EPS guidance narrowed with midpoint reaffirmed (l.31, 287);
  quarter items sum to nine-month items ($300m + $160m = $460m adjustments; $1.028bn + $634m =
  $1.662bn; 1H24 specified pre-tax 1,348 + 552 = 1,900).
- Coverage: FULL for readable text: l.1-686 read in one pass. Missing source text (20 markers,
  4,227 characters): l.63, 87, 121, 143, 163, 189, 209, 233, 253, 277 (segment % rows), l.345, 381
  (statement-of-earnings top rows), l.425, 437, 453, 465 (EPS reconciliation rows), l.575, 603, 639,
  667 (specified detail rows). Spot-check vs docs: 683 lines (+header), "Total reported 11,369 ..."
  (docs l.55 = text l.57), $160 million tax footnote (docs l.367 = text l.369), 20 markers match.

<!-- PASS B: D05 -->
## D05 - Abbott-Exact Sciences Acquisition Press Release

- Source: text/D05.txt (docs/abt_ex991_2025-11-20.txt; 164 lines, 15,949 chars). Plain text, no
  PDF. Printed page numbers 1-7 sit alone at l.33, 53, 101, 121, 129, 139, 163 (7 pages).
- Written or submitted by: Exhibit 99.1 press release (l.3-11; tag "tm2531676d2_ex99-1.htm" l.5).
  Joint announcement: "Abbott (NYSE: ABT) and Exact Sciences (NASDAQ: EXAS) today announced a
  definitive agreement" (l.27). Contacts for both companies at l.141-155.
- Type, date, edition: deal announcement, dateline "ABBOTT PARK, Ill., and MADISON, Wis., Nov.
  20, 2025" (l.27). One edition; nothing amends it in-document.
- Period covered: announcement day; Exact Sciences revenue "this year" (l.51, undated in-line, the
  release is dated 2025); expected closing "in the second quarter of 2026" (l.49). Both companies'
  10-Ks are "for the year ended December 31, 2024"; Exact Sciences 10-Qs "for the quarterly
  periods ended March 31, 2025, June 30, 2025, and September 30, 2025" (l.135). Exact Sciences'
  2025 annual-meeting proxy "filed with the SEC on April 29, 2025" (l.127).
- Entities and aliases: "Abbott Laboratories (“Abbott”)" (l.133); "Exact Sciences Corporation
  (“Exact Sciences”)" (l.117); "the “SEC”" (l.119). People: "Robert B. Ford, chairman and chief
  executive officer, Abbott" (l.41); "Kevin Conroy, chairman and chief executive officer, Exact
  Sciences" (l.43), who "will remain with the company in an advisory role" after closing (l.57).
  "7,000 Exact Sciences’ team members" (l.43); Abbott "114,000 colleagues ... more than 160
  countries" (l.113). Exact Sciences "will maintain its presence in Madison, Wis." (l.57).
  Contacts (l.141-155): Abbott Media Scott Stoffel; Abbott Financial Michael Comilla; Exact
  Sciences Media Steph Spanos; Jim Golden and Tali Epstein, Collected Strategies. Cited source
  only: "*American Cancer Society, Global Facts & Figures, Cancer Facts & Figures." (l.157-159).
- Advisers (l.105, who advises whom as printed): "Morgan Stanley is serving as the exclusive
  financial advisor for Abbott and has provided fully committed debt financing, with Wachtell,
  Lipton, Rosen & Katz serving as legal counsel. Centerview Partners LLC and XMS Capital Partners,
  LLC are acting as financial advisors and Skadden, Arps, Slate, Meagher & Flom LLP is serving as
  legal counsel to Exact Sciences."
- Deal terms (l.27, 47): "$105 per common share in cash, at a total equity value of approximately
  $21 billion and an estimated enterprise value of $23 billion. Abbott’s financing contemplates
  absorption of Exact Sciences’ estimated $1.8 billion of net debt." No breakdown of the financing
  beyond l.47 and l.105; no termination-fee amount (only the risk at l.133).
- Tables: not applicable (none).
- Lists: 5 highlight bullets l.15-25. Product sentence l.35 names 4 (Cologuard, Oncotype DX,
  Oncodetect, Cancerguard). Product section l.69-97: "Screening" 4 bullets (Cologuard and
  Cologuard Plus l.73; Cancerguard l.75; Oncoguard Liver l.77-79; Riskguard l.81-83) and "Testing
  After Diagnosis" 3 bullets (Oncotype DX l.87-89; Oncodetect l.91-93; OncoExTra l.95-97, last).
  Cancerguard "detects 50 cancer types" naming 6 (l.75). Risk list l.133: 12 semicolon items, the
  last "the risk of litigation and/or regulatory actions related to the proposed transaction".
  Proxy headings l.127: 5 quoted headings.
- Forecasts, guidance, deadlines, effective dates: closing "expected in the second quarter of
  2026 and is subject to Exact Sciences’ shareholder approval, as well as receipt of applicable
  regulatory approvals and other customary closing conditions" (l.49); "unanimously approved by
  both companies’ boards of directors" (l.49). "Acquisition will be immediately accretive to
  Abbott’s revenue growth and gross margin" (l.23) is the only accretion statement; no EPS
  accretion/dilution wording anywhere (grep "dilut|EPS|earnings per share": none). Exact Sciences
  "projected to generate more than $3 billion in revenue this year, with a high teens organic
  sales growth rate"; after completion it "will become a subsidiary of Abbott, and Abbott’s total
  diagnostics sales will exceed $12 billion annually" (l.51). Investor call 8 a.m. CT / 9 a.m. ET
  "today" (l.25, l.61).
- Hedged claims: "approximately" attaches to the equity value (l.27, l.47); "estimated" to the
  enterprise value and to net debt (l.47); "expected" to Q2 2026 closing (l.49); "projected" to
  the >$3 billion revenue (l.51). Unhedged "will": accretion (l.23), subsidiary status and >$12
  billion diagnostics sales, conditional on "Once the transaction is completed" (l.51). Side-clause
  hedges: Oncotype DX "insights into the likely benefit from chemotherapy" (l.89, "likely" on the
  benefit); Oncodetect "traces of cancer in blood that may remain" (l.93, "may" on the traces);
  "may be deemed to be participants" (l.127). l.37 "Approximately 20 million people globally,
  including 2 million Americans" and "only expected to rise". Forward-looking caveat l.131-137.
- Rounded prose beside exact figures: every figure is rounded prose ("$60 billion U.S." segments
  l.15; $105, ~$21bn, $23bn, $1.8bn l.47; ">$3 billion", ">$12 billion" l.51); no exact table.
- Operative definitions, rules and scope exceptions: "Merger Agreement" = "the parties’ definitive
  agreement for the proposed transaction" (l.133). The transaction is described as "proposed"
  throughout l.117-137; no completion is reported in D05 (announced agreement only).
- Amendments or contradictions: none in-document. Later status of the deal is in pass A's
  earnings releases (see Shared ground).
- Notes: layout splits of single sentences at l.17/19, 39/41, 55/57, 65/67, 77/79, 81/83, 87/89,
  91/93, 95/97, 117/119, 125/127, 153/155, 157/159 (no text missing). Capture punctuation as in
  original: "(the «Merger Agreement”)" l.133, "«Risk Factors”" and "Form 10- K" l.135.
- Extraction spot-checks: docs file = text minus 2 header lines (docs l.N = text l.N+2); "™" in
  docs l.33 became "TM" (l.35); footnote "*" l.37 -> l.157-159 matches docs l.155; final page "7"
  docs l.161 = l.163. Table check not applicable.
- Coverage: full. Read l.1-164 in one chunk; no gap markers; nothing unread.

<!-- PASS B: D06 -->
## D06 - Abbott Laboratories By-Laws

- Source: text/D06.txt (docs/abt_ex991_2025-12-12.txt; 668 lines, 114,814 chars). Exhibit 99.1
  (l.3-9; tag "2 tm2533113d1_ex99-1.htm" l.5). Printed page numbers "-2-" (l.45) to "-34-"
  (l.667), continuous; page 1 unnumbered (34 pages).
- Written or submitted by: Abbott Laboratories' board: "Adopted by the Board of Directors of
  Abbott Laboratories at the Annual Meeting, April 11, 1963 / as amended and restated, effective
  December 12, 2025" (l.15-19). No signature, certificate or amendment history; nothing says which
  provisions changed in the 2025 restatement.
- Type, date, edition: by-laws, amended and restated effective December 12, 2025 (l.19); only
  by-law edition in the bundle.
- Period covered: fiscal year "shall begin on the first day of January in each year and end on
  the last day of December in each year" (Art. VII, l.611-617).
- Entities and aliases: "the Corporation" = Abbott Laboratories (l.13, l.25); "Exchange Act" =
  Securities Exchange Act of 1934 (l.39); "Commission" = Securities and Exchange Commission
  (l.145); "BCA" = "Illinois Business Corporation Act of 1983" (l.225). "Articles of
  Incorporation" throughout (l.225, 347, 355, 357, 439, 633, 651, 663-665) but "the Certificate of
  Incorporation" once (l.115). Principal office "at the intersection of State Routes 43 and 137 in
  the County of Lake" (l.27). Other instruments named: Corporate Governance Guidelines (l.345,
  347, 457), Code of Conduct (l.345), four committee charters (l.481-493), New York Stock Exchange
  (trading-day roll, l.281), Clayton Antitrust Act of 1914 s.8 (l.361), Rule 506(d) of Regulation
  D under the Securities Act of 1933 (l.361), Regulation S-K Items 404 (l.119) and 401(f) (l.347).
- Defined terms: Noticing Party (l.49); Derivative Instrument (l.59); Proposed Nominee (l.105);
  Voting Commitment (l.115); for Sections 1-2 (l.163-167): affiliate/associate per Rule 12b-2,
  beneficial owner per s.13(d), "public announcement" (press release reported by a national news
  service or a filing under s.13, 14 or 15(d)), Qualified Representative, Shareholder Associated
  Person (7 limbs, last "(VII) any Proposed Nominee" l.167); Requisite Threshold (l.177); for
  Section 15: Shareholder Nominee and Proxy Access Notice (l.287), Voting Shares (l.289-291),
  Constituent Holder (l.293-295), affiliate/associate per Rule 405 (l.297), "own" (l.301), Required
  Information (l.303-305), Permitted Number (l.315), Eligible Shareholder, Proxy Access Request
  Required Shares and Qualifying Fund (l.329), Statement (l.341); "electronic transmission" for
  Board notices (l.405).
- Numeric rules, Art. II Shareholders (what each governs; exceptions):
  - S1 annual-meeting advance notice (nominations and other business; clause (c) is "the exclusive
    means" except Rule 14a-8 proposals, l.39): received "not later than the close of business on
    the ninetieth (90th) day, or earlier than the one hundred twentieth (120th) day prior to the
    anniversary date of the preceding annual meeting"; if the meeting is "more than thirty (30)
    days prior to or more than sixty (60) days after such anniversary date", then "not earlier than
    the one hundred twentieth (120th) day prior to such annual meeting and not later than ... the
    later of (i) the ninetieth (90th) day prior ... and (ii) the tenth (10th) day following the day
    on which public announcement ... was made"; adjournment etc. starts no new period (l.41).
  - S1 updates (l.43): true as of the record date and "ten (10) business days prior to the
    meeting"; received "five (5) business days after the record date" and "seven (7) business days
    prior to the date for the meeting". Secretary supplies questionnaire and representation forms
    "within ten (10) days after receiving such request" (l.111, l.115); policies "within five (5)
    business days" (l.115); nominee cure "within ten (10) business days" (l.117); compensation
    look-back "past three (3) years" (l.119); extra information and interviews "within ten (10)
    days" (l.145); nominees "may not exceed the number of Directors to be elected" (l.149);
    inaccuracy notice "within two (2) business days" and verification "within seven (7) business
    days" (l.153); Rule 14a-19 evidence "no later than five business days prior" (l.159); delivery
    by "personal delivery, by overnight courier or by registered or certified mail" (l.171).
  - S2 special meetings: called by "the Chair of the Board, the Chief Executive Officer, any
    President, the Board of Directors or by a shareholder (or shareholders) beneficially owning not
    less than one-fifth of all the outstanding shares entitled to vote on the matter" (= Requisite
    Threshold, l.177); notice "not later than ... the ninetieth (90th) day and not earlier than the
    one hundred twentieth (120th) day prior to the date of the special meeting or, if the first
    public announcement ... is less than one hundred days prior ..., ... the tenth (10th) day
    following ..., whichever first occurs" (l.183); same 10/5/7 business-day updates (l.185);
    ownership evidence "as of the date of delivery of the special meeting request" (l.189); missing
    information = revocation (l.193); invalid requests (l.195); Board "may cancel" if unrevoked
    requests fall below "the Requisite Thresholds" (plural as printed, l.197); meeting "not be more
    than 120 days after the date on which a valid special meeting request is received" (l.203).
  - S3 remote-only meetings allowed (l.207). S4 meeting notice "not less than ten (10) nor more
    than sixty (60) days"; merger, consolidation, share exchange, dissolution or asset sale "not
    less than twenty (20) nor more than sixty (60) days" (l.211). S5 record date (meetings and
    "payment of any dividend"): "not more than sixty (60) days and, for a meeting ..., not less than
    ten (10) days", merger etc. "not less than twenty (20) days" (l.215). S6 voting list within
    "twenty (20) days after the record date ... or ten (10) days before such meeting, whichever is
    earlier", open "for a period of ten (10) days prior" (l.219).
  - S7 quorum "A majority of the outstanding shares ... entitled to vote on a matter"; vote "the
    majority of the shares represented at the meeting and entitled to vote", unless the BCA or
    Articles require more (l.225). S8 at most "two persons as proxies" (l.229); proxy void after
    "eleven (11) months" unless it provides otherwise (l.235). S9 one vote per share and cumulative
    voting in all director elections (l.239). S11 viva voce unless ballot ordered (l.257).
  - S13 written consent: notice "not less than thirty-five (35) days" before the effective date
    (l.271); consents "within sixty days of the record date" (l.275). S14 consent record date "not
    more than ten (10) days" (merger etc. "twenty (20) days") after the Board resolution; Board acts
    "no later than ten days" after a request; NYSE non-trading tenth day rolls forward (l.281).
  - S15 proxy access (l.285-371): Permitted Number "the greater of (x) one and (y) the largest whole
    number that does not exceed 20 percent of the number of Directors in office as of the last day"
    for notices (l.315), reduced by (1)-(3) (l.317-321; two-annual-term carve-outs l.319, l.321;
    clause (2) floor of one, l.319), recalculated if the Board shrinks (l.323); picks by holdings,
    largest first (l.325). Eligible Shareholder: "continuously for at least three years ... at
    least 3 percent of the aggregate voting power", aggregated holders "shall not exceed twenty",
    a Qualifying Fund counts as one (l.329). Notice timing = Art. II S1 nomination windows (l.309).
    Record-holder statements "within seven calendar days prior" to the notice; follow-up "within
    ten days after the record date" (l.333). Supplements "no later than ten days following the
    record date" and "no later than the fifth day before the annual meeting" (l.339). Statement
    "not to exceed five hundred words" (l.341). Index-fund hedge carve-out "less than 10 percent"
    (l.301). Nominee with under "25 percent" support or who withdraws: ineligible "for the next two
    annual meetings"; nominator barred for "the following annual meeting" (clause 2) and, after an
    elected nominee, "the following two annual meetings" (l.355). Exclusion grounds (1)-(7)
    (l.357-361): competitor officer/director "within the past three years" (Clayton Act s.8);
    criminal proceeding "(excluding traffic violations and other minor offenses)" or conviction
    "within the past ten years"; consequences split by clause at l.365-369 (clause (4) is assigned
    the share-exclusion consequence, l.367). "Exclusive method" except Rule 14a-19 (l.371).
  - S16 Chair of the Board chairs shareholder meetings; meeting rules (a)-(l), last (l) remote
    participation (l.375-377).
- Art. III Directors: "The number of Directors of the Corporation shall be thirteen"; one-year
  terms; no residency or shareholding requirement (l.391). Regular Board meetings "on the second
  Friday of every month at 9:00 a.m." unless changed or omitted by resolution (l.395-397).
  Special Board meetings called by "the Chair of the Board, the Chair of the Executive Committee,
  the Chief Executive Officer, any President, or of any four Directors" (l.401). Notice "at least
  one (1) day" (personal/electronic), "at least two (2) business days" (courier), "at least seven
  (7) days" (mail) (l.405). Quorum "A majority of the number of Directors fixed by these By-Laws"
  (l.409); act of majority present (l.415); unanimous written consent (l.419-423). Interim
  vacancy fills may not "exceed 33-1/3 percent of the total membership of the Board" (l.427).
  Presumption of assent (l.431). "The Audit Committee shall appoint annually a firm of
  independent public accountants as auditors" (l.435). Chair of the Board chosen from directors,
  presides at shareholder and Board meetings (l.439).
- Art. IV Committees: created by a Board majority, chair and secretary designated (l.449);
  committee quorum a majority; called by the Chair of the Board, committee chair or "any two of
  the committee’s members" (l.453). Five named committees: Executive (S3 l.455-477; majority
  independent under the Corporate Governance Guidelines; 9 prohibited acts (1)-(9), last at
  l.477; no charter named); Audit (S4 l.479-481), Compensation (S5 l.483-485), Nominations and
  Governance (S6 l.487-489), Public Policy (S7 l.491-493), each "as set forth in the ...
  Committee Charter".
- Art. V Officers (l.495-567): list at l.501 (CEO, Presidents, Executive/Group/Senior Vice
  Presidents, Vice Presidents, Treasurer, Secretary, Controller, General Counsel, assistants);
  "Any two offices may be held by the same person" (l.501); Board elects, Chair of the Board
  appoints VPs, Controller, Treasurer, Secretary and assistants (l.505); annual election at the
  first Board meeting after the annual meeting (l.507). Roles: CEO l.525; each President "the Chief
  Operating Officer of a major area" l.529; EVP/GVP/SVP l.533; VPs l.537; Treasurer l.541;
  Secretary l.545; Controller l.551; General Counsel l.555; assistants l.559-563; signing l.567.
- Other articles: lost certificates "more than 1,000 shares" vs "1,000 shares or less" approvers
  (l.603-605); Art. VIII voting shares in other corporations (l.625); Art. IX distributions
  (l.633); Art. X seal (l.643); Art. XI waiver (l.651); Art. XII "These By-Laws may be made,
  altered, amended or repealed by the shareholders or the Board of Directors." (l.657).
- Indemnification (Art. XIII, l.663-665): grants rights "to enforce the provisions of Article VI of
  the Articles of Incorporation" (the indemnification scope itself is not in the by-laws); these
  are "contract rights ... that vest at the commencement of such person’s service"; adverse
  changes "shall be prospective only"; rights continue for former directors, officers, employees
  or agents and their heirs.
- Exclusion and negative evidence: no exclusive-forum or court-selection clause and nothing on
  shareholder derivative suits ("forum": none; "court" only guardian/receiver l.249-251;
  "derivative" only Derivative Instruments l.59-81 and l.301); no majority-vote or resignation
  rule for director elections ("plurality|majority of the votes|resign": resign only l.117, 513,
  521); no lead-director role.
- Tables: not applicable. Lists: S1 notice items (1)(A)-(Q) l.51-91 plus proviso l.95-97, (2)(A)-(B)
  l.101-103, (3)(A)-(G) l.107-125 with (D)(I)-(VII) l.115-117, (4)(A)-(D) l.129-139.
- Hedged claims: not applicable (rules). Rule-strength wording differs: inaccurate information
  "shall be deemed not to have been provided" vs unverified information "may be deemed" (both
  l.153); annual-meeting Chair "shall declare" (l.149) vs special-meeting Chair "may ... declare"
  (l.191).
- Internal tensions (recorded, not resolved; no precedence stated): (a) l.169 "Subject to Rule
  14a-8 ..., nothing in these By-Laws shall be construed to permit any shareholder ... to include
  ... in the Corporation’s proxy statement any nomination of Director" vs S15 "the Corporation
  shall include in its proxy materials ... the name ... of any person nominated" (l.287, "Subject
  to the terms and conditions set forth in these By-Laws") and l.371. (b) Update regimes differ:
  S1/S2 business days (l.43, l.185) vs S15 calendar days (l.339). (c) affiliate/associate Rule
  12b-2 (l.165) vs Rule 405 (l.297). (d) Articles vs Certificate of Incorporation (l.115).
  (e) S1 window "or earlier than" (l.41) vs S2 "and not earlier than" (l.183).
- Notes: section headings split across lines (e.g. l.35/37, 173/175); "a complete an accurate"
  (l.81) and "Board of Directors.." (l.449) as printed.
- Extraction spot-checks: docs = text minus 2 header lines (docs l.641 = l.643; docs "-34-" l.665
  = l.667). Seal insignia is an empty quote pair "“”" in both docs and text (l.643): unresolved
  source glyph, no original image to inspect. Tables and footnotes: not applicable.
- Coverage: full. Ledger l.1-120, 120-199, 200-279, 279-348, 348-417, 417-486, 486-555, 556-625,
  626-668 read; nothing unread.

<!-- PASS A: D07 -->
## D07 - Abbott Q4 and Full-Year 2025 Earnings Release

- Source: docs/abt_ex991_2026-01-22.txt (703 lines) -> text/D07.txt (706 lines; text l.N = docs
  l.N-2). Ex. 99.1 "abt-2025q4xexhibitx991.htm" (l.5); "Page 1 of 20" ... "Page 20 of 20" (l.43-705).
- Written or submitted by: Abbott ("ABBOTT PARK, Ill., Jan. 22, 2026 - Abbott today announced",
  l.19). Contacts l.309-321 as D04 (Blakley 224-668-0036). CEO quote Robert B. Ford (l.41).
- Type, date, edition: news release, Jan. 22, 2026. Headline l.15 "Abbott Reports Fourth-Quarter and
  Full-Year 2025 Results; Issues 2026 Financial Outlook".
- Period covered: "fourth quarter ended Dec. 31, 2025" (l.19); 4Q25 vs 4Q24 and 12M25 vs 12M24
  ("Twelve Months Ended December 31", l.385). Calendar fiscal year.
- Entities and aliases: Exact Sciences (l.33, only mention); Volt(TM) PFA System (FDA approval,
  l.37); "TactiFlex(TM) Duo Ablation Catheter, Sensor Enabled(TM)" (CE Mark, l.39; D03 l.33 names
  "TactiFlex(TM) Duo Pulsed Field Ablation (PFA) System"); India (l.213); China volume-based
  procurement (l.169). No brand-list sentence.
- Tables ($ in millions; % one decimal):
  - l.53-75 total company 4Q25 (Total 11,459; U.S. 4,383; Intl 7,076; Nutrition 1,940; Diagnostics
    2,457; EPD 1,382; MD 5,675); U.S. reported, [gap l.65], COVID impact (0.8)/Dx (3.4), organic
    excl. COVID 3.8 (9.1) (0.2) 7.0 10.4, "Organic" U.S. 0.9 / Intl 4.3.
  - l.77-97 12M25 (Total 44,328; U.S. 17,126; Intl 27,202; Nutrition 8,451; Dx 8,937; EPD 5,536;
    MD 21,387); [gap l.87]; COVID impact (1.2); organic excl. COVID 6.7 1.2 0.4 7.4 11.9; "Organic"
    U.S. 5.0 / Intl 5.9.
  - Nutrition 4Q25 l.107-123 [gap l.119] (U.S. (13.2), Pediatric U.S. (17.7)), 12M25 l.129-143 [gap
    l.139]; Diagnostics 4Q25 l.151-163 [gap l.159], 12M25 l.173-187 [gap l.185]; EPD 4Q25 l.195-209
    [gap l.205], 12M25 l.217-233 [gap l.229]; MD 4Q25 l.241-253 [gap l.249] (Diabetes Care 2,133),
    12M25 l.263-275 [gap l.271] (Diabetes Care 7,998).
  - Statement of earnings 4Q25 l.329-359 (gap l.341; EBT 2,358 vs 2,030; taxes 582 vs (7,199); NE
    $1,776 vs $9,229; EPS $1.01 vs $5.27; adjusted $1.50 vs $1.34, +11.9%; NE excl. specified $2,630
    vs $2,349; shares 1,747 vs 1,746). 12M l.381-411 (gap l.393; EBT 8,466 vs 7,013; taxes 1,942 vs
    (6,389); NE $6,524 vs $13,402; EPS $3.72 vs $7.64; adjusted $5.15 vs $4.67, +10.3%; NE excl.
    specified $9,040 vs $8,200, +10.2%; shares 1,749 vs 1,748). The 4Q24/12M24 columns repeat D01
    l.407-461 figures.
  - EPS reconciliations l.433-485: amortization 422 (4Q25), 465 (4Q24), 1,682 (12M25), 1,878
    (12M24); other rows = gaps l.449, 459, 473, 483; other net expenses $306m, $268m, $614m, $755m.
  - Tax-rate reconciliations l.489-563 (complete): 4Q25 GAAP 24.7%, excl. specified 14.8% (728 /
    (126)); 4Q24 (354.6%) / 15.0%; 12M25 22.9% / 16.0% (2,296 / (220)); 12M24 (91.1%) / 15.0%.
  - Revenue reconciliation l.567-581: twelve months only; 12M24 base 41,950 less business exit (13)
    = 41,937 (D01 l.651 printed 12M24 business-exit impact (14) and acquisition impact (57) when
    12M24 was the current-year column).
  - Specified-items details l.585-703: body rows = gaps l.591, 623, 655, 687; totals 4Q25 tax
    (126), net $854, EPS $0.49; 4Q24 7,613 / $(6,880) / $(3.93); 12M25 (220) / $2,516 / $1.43; 12M24
    7,835 / $(5,202) / $(2.97).
- Lists: l.35-39 "two significant regulatory approvals" in Electrophysiology (December FDA Volt;
  January CE Mark TactiFlex Duo); MD growth "led by double-digit growth in Electrophysiology, Heart
  Failure, Diabetes Care, and Rhythm Management" (l.257).
- Forecasts, guidance, deadlines, effective dates: 2026 guidance first issued (headline l.15-17,
  bullets l.29-31, section l.279-285): FY2026 organic sales growth "6.5% to 7.5%"; FY2026 adjusted
  diluted EPS "$5.55 to $5.80" ("growth of 10 percent at the midpoint", l.31; "10 percent growth
  at the midpoint", l.17); "first-quarter 2026 adjusted diluted earnings per share of $1.12 to
  $1.18" (l.283). No operating-margin guidance; no COVID basis stated for 2026 organic guidance; no
  statement whether guidance includes Exact Sciences. FY2025 actuals vs 2025 guidance editions: see
  shared ground. Exact Sciences l.33: "In November, Abbott announced an agreement to acquire Exact
  Sciences ... Abbott continues to expect the transaction to close in the second quarter of 2026."
  Dated events: "In December" FDA approval of Volt PFA System (l.37); "In January" CE Mark for
  TactiFlex Duo (l.39; after the Dec. 31, 2025 quarter end). Dividend l.287-291: "408th";
  declared "Dec. 12, 2025", "$0.63 per share" (prior releases $0.59), payable "Feb. 13, 2026",
  record "Jan. 15, 2026"; "54 consecutive years" (prior releases 53). Employees "115,000" (l.295;
  prior 114,000).
- Hedged claims: l.33 "continues to expect the transaction to close in the second quarter of 2026";
  l.125 Nutrition "Abbott expects to increase volume growth with the launch of several new products
  in 2026"; l.41 Ford "well positioned for accelerating growth in 2026"; forward-looking caution
  l.307 still cites the Form 10-K "for the year ended Dec. 31, 2024".
- Rounded prose beside exact figures: l.17/23 Q4 adjusted EPS "reflects growth of 12 percent" vs
  table 11.9% (l.357); l.17/27 FY adjusted EPS "growth of 10 percent" vs 10.3% (l.409); FY sales
  "$44.3 billion" (l.25) vs 44,328 (l.81) and "$44.328 billion" (l.325). CGM "$2.0 billion" (+15.0%
  reported, +12.2% organic, l.259) vs Diabetes Care 2,133 (l.243). Footnotes l.323-325: 4Q25
  $11.459bn / Dx $2.457bn / COVID $89m; 4Q24 $10.974bn / $2.520bn / $176m; FY2025 $44.328bn /
  $8.937bn / $297m; FY2024 $41.950bn / $9.341bn / $747m. No margin bullets in this release.
- Notes: tax 4Q25 (l.371, 523): "approximately $20 million of net tax expense as a result of the
  resolution of various tax positions related to prior years" plus "approximately $150 million in
  adjustments related to prior recognition of a significant non-cash deferred tax benefit"; FY2025
  (l.423, 561): "approximately $70 million of net tax benefit" plus "approximately $610 million"
  adjustments; 2024 comparatives repeat "$7.497 billion" (l.373, 425, 525, 563). Legal item: 4Q25 and
  12M25 specified (c) "Other includes $165 million for legal reserves related to a certain
  agreed-upon settlement" (l.605, 669; settlement not named); specified-items text adds "legal
  reserves" (l.375, 427, 451, 475). Specified items 4Q25 "$854 million, or $0.49 per share" (l.375);
  FY2025 "$2.516 billion, or $1.43 per share" (l.427; D04 9M25 $0.95 + $0.49 = $1.44 per share,
  dollar amounts $1.662bn + $854m = $2.516bn). Nutrition l.123-125: Q4 Nutrition sales "decreased
  8.9 percent" reported, 9.1% organic, reflecting "lower sales volumes" and "new strategic price
  actions".
- Operative definitions, rules and scope exceptions: organic definition l.47 verbatim as D03/D04.
  Restructuring footnote (b) for 2025 periods drops "and cost reduction initiatives" (l.603, 667)
  while 2024 columns keep it (l.635, 699).
- Amendments or contradictions: 4Q24 comparative footnote wording differs from D01: D07 4Q24 (a)
  adds "as well as other costs related to business acquisitions" (l.633; D01 l.693 lacks it); D07
  4Q24 other-net-expense prose omits "intangible impairments" (l.461; D01 l.499 includes it); 12M24
  business-exit (13) vs D01 (14) (above). Page cross-references l.475 and l.485 both say "See page
  19" (12M24 details sit on page 20, l.675-705).
- Coverage: FULL for readable text: l.1-706 read in one pass. Missing source text (20 markers, 4,355
  characters): l.65, 87, 119, 139, 159, 185, 205, 229, 249, 271 (segment % rows), l.341, 393
  (statement-of-earnings top rows), l.449, 459, 473, 483 (EPS reconciliation rows), l.591, 623, 655,
  687 (specified detail rows). Spot-check vs docs: 703 lines (+header), "Total reported 11,459 ..."
  (docs l.57 = text l.59), $165 million legal-reserve footnote (docs l.603 = text l.605), 20
  markers match.

<!-- PASS A: D08 -->
## D08 - Abbott Q1 2026 Earnings Release

- Source: docs/abt_ex991_2026-04-16.txt (467 lines) -> text/D08.txt (470 lines; text l.N = docs
  l.N-2). Ex. 99.1 "abt-2026q1xexhibitx991.htm" (l.5); "Page 1 of 15" ... "Page 15 of 15" (l.41-469).
- Written or submitted by: Abbott ("ABBOTT PARK, Ill., April 16, 2026 - Abbott today announced",
  l.21). Contacts l.231-243 as D07. CEO quote Robert B. Ford (l.39).
- Type, date, edition: news release, April 16, 2026. Headline l.15 "Abbott Reports First-Quarter
  2026 Results; Updates Guidance to Reflect Acquisition of Exact Sciences".
- Period covered: "first quarter ended March 31, 2026" (l.21); 1Q26 vs 1Q25 only.
- Entities and aliases: Exact Sciences ("a cancer diagnostics company that Abbott acquired on March
  23, 2026", l.47), presented as "Abbott's Cancer Diagnostics business" (l.127); Cologuard(R),
  Cancerguard(R) ("a multi-cancer screening test that launched last year", l.137); AtaCor Medical
  (collaboration, EV-ICD, l.33); VERITAS study / "investigational Amulet 360(TM) Left Atrial
  Appendage (LAA) Occluder" (l.35); FreeDM2 trial / FreeStyle Libre (l.37); "Amplatzer Amulet Left
  Atrial Appendage Occluder" moved to Electrophysiology (l.187, 399); unnamed "competitor" paying
  Structural Heart compensation under "a multi-year agreement" (l.47, 245, 405).
- Tables ($ in millions; % one decimal):
  - l.53-67 total company 1Q26 (Total 11,164; U.S. 4,274; Intl 6,890; Nutrition 2,017; Diagnostics
    2,180; EPD 1,426; MD 5,539); U.S. reported row, [gap l.65], then comparable U.S. 2.5 / Intl 4.6
    rows (label in gap).
  - Nutrition l.77-91 [gap l.87]; EPD l.145-161 [gap l.157]; MD l.173-185 [gap l.181]
    (Electrophysiology* 788, Structural Heart* 578, Diabetes Care 2,080; U.S. Structural Heart
    reported (9.5) vs comparable (3.6)).
  - Diagnostics l.103-125 is COMPLETE (no marker): new columns Core Laboratory / Cancer Diagnostics /
    Rapid/Molecular Diagnostics; rows U.S., International, Total reported, "Total reported excl.
    foreign exchange impact", "Comparable sales growth" (1.8 total; Cancer Dx 13.4), U.S.,
    International.
  - Statement of earnings l.249-279 (gap l.261; EBT 1,449 vs 1,778, (18.5)%; taxes 372 vs 453; NE
    $1,077 vs $1,325; EPS $0.61 vs $0.76 "n/m"; adjusted $1.15 vs $1.09, +5.5%; NE excl. specified
    $2,022 vs $1,919; shares 1,747 / 1,747). 1Q25 column repeats D02 l.259-271.
  - EPS reconciliation l.301-329: amortization 422 (1Q26), 420 (1Q25); rest = gaps l.317, 327;
    other net expenses $514m (1Q26), $100m (1Q25).
  - Tax-rate reconciliation l.333-369 (complete): 1Q26 GAAP 25.6%, excl. specified 15.2% (936 /
    (9)); 1Q25 25.5% / 16.5% (repeats D02 l.333-337).
  - Revenue reconciliation l.373-405 (complete): 1Q26 reported, "Impact of acquisition (a)",
    "Impact of multi-year agreement (b)", "Foreign exchange", comparable; 1Q25 reported, (a), (b),
    comparable. Total 11,164 + 706 - 8 - 414 = 11,448; 1Q25 10,358 + 707 - 24 = 11,041; reported
    7.8%, comparable 3.7%. Rows for Total Diagnostics, Total Cancer Diagnostics (96 + 706 - 1 = 801
    vs 707; 13.4%), Total Medical Devices, Total Structural Heart (578 vs restated 1Q25 531). Layout:
    Structural Heart rows (l.395) carry an extra "-" token before each 1Q25 figure.
  - Specified-items details l.409-467: body rows = gaps l.419, 451; totals 1Q26 tax (9), net $945,
    EPS $0.54; 1Q25 (74) / $594 / $0.33.
- Lists: dated bullets l.33-37 (January, February, March) plus acquisition bullet l.27; MD growth
  "led by double-digit growth in Electrophysiology, Heart Failure and Rhythm Management" (l.193).
- Forecasts, guidance, deadlines, effective dates: headline l.15 "Updates Guidance to Reflect
  Acquisition of Exact Sciences"; bullets l.17-19, 29-31; section l.199-207: FY2026 "comparable
  sales growth of 6.5% to 7.5%" (D07 stated "organic sales growth ... 6.5% to 7.5%"); FY2026
  adjusted diluted EPS "$5.38 to $5.58, which includes $0.20 of dilution related to the
  acquisition of Exact Sciences" (D07 range $5.55-$5.80; prior range not printed here);
  "second-quarter 2026 adjusted diluted earnings per share of $1.25 to $1.31" (l.205). Q1 actual
  adjusted EPS $1.15 (l.17, 277) vs D07 Q1 range $1.12-$1.18 (D07 l.283). Exact Sciences closing:
  "On March 23, 2026, Abbott completed its acquisition of Exact Sciences" (l.27; also l.47, 127,
  137, 403); D07 l.33 had expected closing "in the second quarter of 2026". Dated events: "In
  January" AtaCor collaboration (l.33); "In February" VERITAS results (l.35); "In March" FreeDM2
  results (l.37); Amulet transfer "on Jan. 1, 2026" (l.187); multi-year agreement "final payment
  ... recognized in the first quarter of 2026" (l.47, 405). Dividend l.209-213: "409th"; declared
  "Feb. 20, 2026", "$0.63", payable "May 15, 2026", record "April 15, 2026"; "54 consecutive
  years". Employees "122,000" (l.217; D07 115,000).
- Hedged claims: l.95 pricing actions and launches "are expected to contribute to improved volume
  growth over the course of the year"; l.39 Ford "strengthening our confidence in delivering
  accelerating growth"; forward-looking caution l.229 now cites Form 10-K "for the year ended Dec.
  31, 2025".
- Rounded prose beside exact figures: l.17/25 adjusted EPS "reflects growth of 6 percent" vs table
  5.5% (l.277). CGM growth 14.2% reported / 7.6% comparable with no dollar figure (l.195). Footnote
  l.245: 2025 totals "$44.328 billion" (U.S. $17.126bn, Intl $27.202bn); Structural Heart "$89
  million of compensation payments" in 2025; Exact Sciences 2025 sales "$3.247 billion" (U.S.
  $3.145bn, international $102m). No margin bullets.
- Notes: tax l.291/367: 2026 "approximately $50 million of net tax benefit" (prior-year positions)
  plus "approximately $200 million in adjustments related to prior recognition of a significant
  non-cash deferred tax benefit"; 2025 comparative "approximately $200 million" (l.293, 369).
  Specified items 1Q26 "$945 million, or $0.54 per share, for intangible amortization, charges
  related to restructuring, acquisitions, and other net expenses" (l.295); 1Q26 (a) includes
  "stock-based compensation recognized as expense from equity awards accelerated in connection with
  the Exact Sciences acquisition" (l.429). Nutrition l.95: "strategic pricing actions implemented in
  the fourth quarter of 2025" (cf. D07 l.125). Rapid/Molecular l.135 "weaker respiratory virus
  season". No litigation or legal-reserve item in this release. No COVID-19, "organic" or
  ZonePerfect wording anywhere in D08 (keyword check).
- Operative definitions, rules and scope exceptions: "Comparable sales growth" replaces organic
  (l.45-47): "includes the prior and current year sales of Exact Sciences ... excludes the impact
  of foreign exchange and revenue in both the prior and current year related to compensation
  payments that Abbott's Structural Heart business received as part of a multi-year agreement with
  a competitor." Recasts: "Beginning in 2026, Abbott aggregated its previously reported Rapid
  Diagnostics, Molecular Diagnostics, and Point of Care businesses into the Rapid and Molecular
  Diagnostics business" (l.127); Amulet moved from Structural Heart to Electrophysiology, "$46
  million of sales in the first quarter of 2025 were moved" (l.187, 399): 1Q25 Structural Heart 531
  here (U.S. 248, Intl 283; l.395) vs 577 (U.S. 282, Intl 295) in D02 l.173. Acquisition adjustment
  (a) "includes historical sales for Exact Sciences prior to the acquisition date" (l.403).
- Amendments or contradictions: l.297 calls the 1Q25 specified items "net after-tax benefits of $594
  million, or $0.33 per share"; D02 l.287 calls the same amount "net after-tax charges"; neither
  states precedence (D08 l.273 and D02 l.265 both show NE excl. specified above GAAP NE). 1Q25
  other-net-expense wording differs slightly (l.329 vs D02 l.305).
- Coverage: FULL for readable text: l.1-470 read in one pass. Missing source text (9 markers, 2,060
  characters): l.65, 87, 157, 181 (segment % rows), l.261 (statement-of-earnings top rows), l.317,
  327 (EPS reconciliation rows), l.419, 451 (specified detail rows). Spot-check vs docs: 467 lines
  (+header), "Total reported 11,164 ..." (docs l.57 = text l.59), footnote 1 with "$3.247 billion"
  (docs l.243 = text l.245), 9 markers match.

<!-- PASS B: D09 -->
## D09 - Abbott Laboratories Derivative Settlement Notice

- Source: text/D09.txt (docs/abt_ex991_2026-04-17.txt; 272 lines, 16,828 chars). Exhibit 99.1
  (l.3-9; tag "2 tm2611915d1_ex99-1.htm" l.5). No printed page numbers; sections I-VII.
- Written or submitted by: no signatory. "THE UNITED STATES DISTRICT COURT FOR THE NORTHERN
  DISTRICT OF ILLINOIS HAS AUTHORIZED THIS NOTICE TO BE SENT TO YOU" (l.55-63); addressed "TO: ALL
  CURRENT HOLDERS OF ABBOTT LABORATORIES COMMON STOCK" (l.45-49); "THIS IS NOT A SOLICITATION"
  (l.65); "DATE: April 17, 2026" (l.271). Who prepared or filed it is not stated in the text.
- Type, date, edition: court-authorized "NOTICE OF PROPOSED SETTLEMENT OF CONSOLIDATED DERIVATIVE
  ACTION, FINAL SETTLEMENT HEARING, AND RIGHT TO APPEAR" (l.37-43), dated April 17, 2026.
- Court and case: "IN THE UNITED STATES DISTRICT COURT FOR THE NORTHERN DISTRICT OF ILLINOIS
  EASTERN DIVISION" (l.11-17); "IN RE ABBOTT LABORATORIES INFANT FORMULA SHAREHOLDER DERIVATIVE
  LITIGATION" (l.21-27); "CASE NO: 1:22-cv-5513" (l.29); caption names "Hon. Sunil R. Harjani"
  and "Hon. Laura K. McNally" (l.31-33; McNally's role is not stated); hearing "before the
  Honorable Sunil R. Harjani" (l.73).
- Parties and aliases (l.67): "derivative claims brought against certain current and former
  directors and officers (“Individual Defendants”) of Abbott Laboratories (“Abbott” or the
  “Company”) (collectively with the Individual Defendants, “Defendants”)", so Abbott is within
  "Defendants"; the action "seeks recovery on behalf of Abbott" (l.95). The phrase "nominal
  defendant" does not appear. "Court-appointed Lead Plaintiffs, International Brotherhood of
  Teamsters Local No. 710 Pension Fund and Southeastern Pennsylvania Transportation Authority"
  (l.81-83; two named). Co-Lead Counsel "Cohen Milstein Sellers & Toll PLLC and Scott+Scott
  Attorneys at Law LLP" (= "Lead Plaintiffs’ Counsel", l.95). Addresses l.145-199: Clerk of the
  Court, 219 South Dearborn Street, Chicago, IL 60604; Carol V. Gilden (Cohen Milstein, Chicago);
  Justin O. Reliford (Scott+Scott, Wilmington, DE); "Abbott’s Counsel": Eric R. Swibel, LATHAM &
  WATKINS LLP (l.177-187); "Individual Defendants’ Counsel": Brenton A. Rogers, KIRKLAND & ELLIS
  LLP (l.189-199). Phones/e-mails for Gilden and Reliford at l.243-269. Other defined terms:
  Notice, Settlement, Stipulation ("Stipulation and Agreement of Settlement"), Court (l.67);
  Settlement Hearing (l.73); Judgment ("Final Order and Judgment", l.209); "Consolidated
  Derivative Action (as defined below)" (l.67) is described at l.95 without a quoted definition;
  "SEC" used undefined (l.99). Released Claims, Released Parties, Effective Date, Unknown Claims,
  Additional Derivative Actions and Additional Shareholder Demands are "defined in the
  Stipulation" (l.71, 211-215, 223).
- Claims and alleged events: "claims of breaches of fiduciary duty and violations of federal
  securities laws" (l.95); alleges the Individual Defendants "breached their fiduciary duties by
  failing to oversee Abbott’s manufacture and sale of infant formula products in the United
  States and violated federal securities laws by causing Abbott to make material
  misrepresentations, including in certain statements filed with the SEC, regarding the same"
  (l.97-99). Events named only inside the Released Claims definition: "Abbott’s February 2022
  recall of powdered infant formula, or Abbott’s U.S. powdered infant formula manufacturing
  facilities in Sturgis, Michigan, or Casa Grande Arizona" (l.225-227). No other dates of alleged
  conduct.
- Settlement terms: "Abbott will maintain or adopt the corporate governance policies and practices
  identified in Exhibit A to the Stipulation. Abbott will commit the funds as are necessary to
  implement the corporate governance elements" (l.105-107). Exhibit A is not reproduced: no
  individual reform, timing or duration appears anywhere in D09 (grep "year|duration|charter|
  by-law|board": none). Lead Plaintiffs' characterisation: "adopting governance reforms and
  enhancing Abbott’s internal reporting and oversight framework for legal and regulatory
  compliance" (l.85). No monetary payment to Abbott is described.
- Fees and awards (l.121): "Lead Plaintiff’s Counsel may request a fee award of not more than
  $15.85 million, which includes reimbursement of their costs and expenses, including service
  awards for the Lead Plaintiffs of not more than $15,000 each, subject to Court approval";
  contingent basis, unpaid to date (l.121-123); fees not discussed until after agreement on the
  Settlement and Exhibit A provisions (l.125). Who would pay the award is not stated.
- Deadlines and hearing: Settlement Hearing "June 4, 2026, at 9:30 A.M." at "Courtroom 1925 ...
  219 South Dearborn Street, Chicago" (l.73-75, repeated l.133); four hearing purposes (i)-(iv)
  (l.75). Objections: signed writing with (i) name/address/phone, (ii) shares owned "as of the
  date of the submission" with brokerage statements, (iii) detailed grounds (l.139-143); mail to
  the Court (or file) and "mail each of the attorneys ... to arrive no later than May 18, 2026.
  YOUR OBJECTION MUST BE IN WRITING AND RECEIVED BY THIS DATE TO BE CONSIDERED" (l.143); late
  objection "the Court may deem it waived and may not consider it" (l.143). Appearance letter
  "must be received no later than May 18, 2026. by the Clerk of the Court, Lead Plaintiffs’
  Counsel, Abbott’s Counsel, and Individual Defendants’ Counsel" (l.203). Both deadlines are fixed
  calendar dates; no day-count formula is printed. "The date of the Settlement Hearing is subject
  to change without further notice" (l.203). Interim bar on Released Claims suits (l.135).
- Releases (l.211-227): Releasing Parties "Lead Plaintiffs (individually, and derivatively on
  behalf of Abbott), Abbott and all Abbott Shareholders" release Released Claims against Released
  Parties "Lead Plaintiffs, all Defendants, the Special Litigation Committee and its member, and
  any other persons that were or could have been named" (l.211-215); reverse release by
  "Defendants, the Special Litigation Committee and its member" of Lead Plaintiffs and other
  shareholders, "except for claims to enforce this Stipulation" (l.217-219). Released Claims run
  "from the beginning of time to the date of the entry of a final order and judgment in any
  forum" (l.223). No admission (l.229).
- Hedged and attributed statements: Defendants "have denied the allegations ... and continue to
  deny vigorously any wrongdoing" and support the Settlement for "time, expense, and distraction"
  (l.79, l.115). Benefit claims are attributed: Lead Plaintiffs "believe" (l.83-85); "The parties
  believe" (l.85); Lead Plaintiffs' Counsel "believes" (l.113). "Nothing in this Notice
  constitutes a finding of the Court" (l.77). "may" in "YOUR LEGAL RIGHTS MAY BE AFFECTED"
  (l.89); "is or may be deemed to be an admission" (l.229).
- Tables: not applicable. Lists: hearing purposes (i)-(iv) l.75; objection contents (i)-(iii)
  l.139-143; appearance-letter contents (i)-(ii) l.201; five address blocks l.145-199 (Clerk of
  the Court, then Gilden, Reliford, Swibel, Rogers).
- Committees and governance references: only the "Special Litigation Committee and its member"
  (singular; l.215, l.219). No by-law, charter or named board committee reference.
- Notes: layout splits at l.67/69, 73/75, 81/83, 93/95, 97/99, 105/107, 121/123, 139-143,
  211-215, 223-227 (no text missing). "May 18, 2026. by the Clerk" (l.203) and "Casa Grande
  Arizona" (no comma, l.227) as printed; "Lead Plaintiff’s Counsel" singular at l.121 and l.155.
- Extraction spot-checks: docs = text minus 2 header lines (docs l.27 case no. = l.29; docs l.141,
  201 deadline = l.143, 203; docs l.269 date = l.271). Tables, footnotes, page count: not
  applicable.
- Coverage: full. Read l.1-272 in one chunk; no gap markers; nothing unread.

<!-- PASS A: D10 -->
## D10 - Abbott Q2 2026 Earnings Release

- Source: docs/abt_ex991_2026-07-16.txt (759 lines) -> text/D10.txt (762 lines; text l.N = docs
  l.N-2). Ex. 99.1 "abt-2026q2xexhibitx991.htm" (l.5); "Page 1 of 21" ... "Page 21 of 21" (l.43-761).
- Written or submitted by: Abbott ("ABBOTT PARK, Ill., July 16, 2026 - Abbott today announced",
  l.21). Contacts l.317-329 as D07/D08. CEO quote Robert B. Ford (l.41).
- Type, date, edition: news release, July 16, 2026. Headline l.15 "Abbott Reports Second-Quarter
  2026 Results and Raises Full-Year EPS Guidance".
- Period covered: "second quarter ended June 30, 2026" (l.21); 2Q26 vs 2Q25 and first half 1H26 vs
  1H25 ("First Half Ended June 30", l.393).
- Entities and aliases: Exact Sciences / Cancer Diagnostics (l.49, 183, 593, 629); Cologuard(R),
  Cologuard Plus(R) (l.39), "precision oncology and international businesses" (l.163); TECTONIC
  U.S. pivotal trial / IVL System (l.31); "Heart Rhythm Society (HRS) conference" (l.33); Libre(R)
  Duo (l.35); Amulet(TM) 360 LAA device FDA submission (l.37); "American Cancer Society (ACS)"
  issued the updated CRC screening guidelines (l.39; issuer is ACS, not Abbott).
- Tables ($ in millions; % one decimal):
  - l.55-71 total company 2Q26 (Total 12,593; U.S. 5,216; Intl 7,377; Nutrition 2,144; Diagnostics
    3,092; EPD 1,499; MD 5,853); U.S. reported 22.0 (Dx 104.8), [gap l.67], then comparable U.S. 3.5
    / Intl 5.8 rows.
  - l.75-85 1H26 (Total 23,757; U.S. 9,490; Intl 14,267; Dx 5,272; MD 11,392); [gap l.83];
    comparable U.S. 3.0 / Intl 5.3.
  - Nutrition 2Q26 l.95-109 [gap l.105], 1H26 l.117-131 [gap l.127]; EPD 2Q26 l.193-207 [gap
    l.203], 1H26 l.215-231 [gap l.227]; MD 2Q26 l.239-251 [gap l.247] (Electrophysiology* 861,
    Structural Heart* 597, Diabetes Care 2,188), 1H26 l.261-277 [gap l.273] (Diabetes Care 4,268).
  - Diagnostics 2Q26 l.139-155 and 1H26 l.167-183 are COMPLETE (no marker): Core Laboratory / Cancer
    Diagnostics / Rapid/Molecular; rows U.S., International, Total reported, excl. FX, Comparable
    (2Q26 total 2.9, Cancer Dx 13.3; 1H26 total 2.4, Cancer Dx 13.3), U.S., International.
  - Statement of earnings 2Q26 l.335-367 (gap l.347; first visible row "Interest expense, net" 299
    vs 50; net FX 4 vs (11); EBT 1,524 vs 2,150, (29.1)%; taxes 596 vs 371; NE $928 vs $1,779,
    (47.8)%; EPS $0.53 vs $1.01; adjusted $1.31 vs $1.26, +4.0%; NE excl. specified $2,290 vs
    $2,213; shares 1,743 vs 1,751). 1H l.389-413 (gap l.401; interest expense 367 vs 99; EBT 2,973
    vs 3,928; taxes 968 vs 824; NE $2,005 vs $3,104; EPS $1.14 vs $1.77; adjusted $2.46 vs $2.35,
    +4.7%; shares 1,745 vs 1,749). 2Q25 interest-expense and net-FX rows are printed here; in D03
    the corresponding rows sit inside gap l.357.
  - EPS reconciliations l.435-483: amortization 658 (2Q26), 420 (2Q25), 1,080 (1H26), 840 (1H25);
    other rows = gaps l.443, 453, 469, 481; other net expenses $519m, $80m, $1.033bn, $180m.
  - Tax-rate reconciliations l.487-561 (complete): 2Q26 GAAP 39.1%, excl. specified 15.2% (1,177 /
    (185)); 2Q25 17.3% / 16.5%; 1H26 32.5% / 15.2% (2,113 / (194)); 1H25 21.0% / 16.5%.
  - Revenue reconciliation 2Q l.565-595 (columns: 2Q26 reported, FX, comparable; 2Q25 reported,
    acquisition (a), multi-year agreement (b), comparable): total 12,593 - 86 = 12,507 vs 11,142 +
    811 - 22 = 11,931 (13.0% / 4.8%); Diagnostics, Cancer Dx (919 vs 811; 13.3%), MD, Structural
    Heart (597 vs restated 581). 1H l.599-631: total 23,757 + 706 - 8 - 500 = 23,955 vs 21,500 +
    1,518 - 46 = 22,972 (10.5% / 4.3%); Cancer Dx 1,015 + 706 - 1 = 1,720 vs 1,518; Structural
    Heart 1,175 vs restated 1,112.
  - Specified-items details l.635-759: body rows = gaps l.647, 679, 711, 743; totals 2Q26 tax
    (185), net $1,362, EPS $0.78; 2Q25 66 / $434 / $0.25; 1H26 (194) / $2,307 / $1.32; 1H25 (8) /
    $1,028 / $0.58.
- Lists: dated bullets l.31-39 (April x2, May x3); "late-breaking data from four clinical trials"
  (l.33; trials not named); MD growth "led by low-teens growth in Electrophysiology and
  high-single-digit growth in Rhythm Management, Diabetes Care, and Heart Failure" (l.255).
- Forecasts, guidance, deadlines, effective dates: headline l.15 "Raises Full-Year EPS Guidance";
  l.19/27 "Abbott reaffirms full-year 2026 comparable sales growth guidance of 6.5% to 7.5%"; l.19/29
  "Abbott raises full-year 2026 adjusted diluted EPS guidance range to $5.45 to $5.60, compared to
  previous range of $5.38 to $5.58" (prior range printed). Section l.285-293: FY2026 comparable
  6.5%-7.5% (l.287); FY EPS $5.45-$5.60 (l.289; no Exact Sciences dilution figure restated);
  "third-quarter 2026 adjusted diluted earnings per share of $1.38 to $1.46" (l.291). Q2 actual
  adjusted EPS $1.31 (l.17, 365) vs D08 Q2 range $1.25-$1.31 (D08 l.205). l.19: "returned $2.1
  billion to shareholders in the second quarter in the form of dividends and share repurchases"
  (headline sub-bullet only). Dated events: "In April" TECTONIC enrollment completed (l.31; D02 l.31
  reported the trial's initiation "In March", no year printed, in the April 16, 2025 release); "In
  April" HRS data (l.33); "In May" CE Mark
  for Libre Duo (l.35); "In May" FDA submission for Amulet 360 (l.37; submission, not approval);
  "In May" ACS guidelines (l.39). Dividend l.295-299: "410th"; declared "June 12, 2026", "$0.63",
  payable "Aug. 17, 2026", record "July 15, 2026"; "54 consecutive years". Employees "122,000"
  (l.303).
- Hedged claims: l.41 Ford "We expect this momentum to continue and drive accelerating sales and
  earnings growth in the second half of the year"; forward-looking caution l.315 (Form 10-K for year
  ended Dec. 31, 2025); l.293 "could significantly impact".
- Rounded prose beside exact figures: l.113 "Nutrition sales increased $127 million on a sequential
  basis compared to the first quarter of 2026" (2,144 here vs D08 l.59 2,017). l.163 Cologuard
  "mid-teens growth" vs Cancer Dx comparable 13.3% (l.151). CGM growth 11.0% reported / 9.5%
  comparable, no dollar figure (l.257). Footnote 1 l.331 repeats D08 l.245 verbatim (2025 totals,
  $89m compensation payments, Exact Sciences 2025 sales $3.247bn).
- Notes: tax 2Q26 (l.379, 521): "approximately $110 million of net tax expense primarily as a result
  of the resolution of various tax positions related to prior years" plus "approximately $240
  million in adjustments related to prior recognition of a significant non-cash deferred tax
  benefit"; 1H26 (l.425, 559): "approximately $60 million of net tax expense primarily ..." plus
  "approximately $440 million"; 2025 comparatives repeat D03 ($90m benefit; $100m / $300m). Legal
  item: 2Q26 and 1H26 specified (c) "Other includes $385 million for legal reserves related to an
  agreed-in-principle settlement, subject to satisfaction of certain contingencies" (l.661, 725;
  settlement not named); "legal reserves" in specified text l.383, 429, 445, 471. Specified items
  2Q26 "$1.362 billion, or $0.78 per share" (l.383); 1H26 "$2.307 billion, or $1.32 per share"
  (l.429). Acquisition (a) adds "inventory step-up amortization" (l.657, 721) and 1H26 Exact
  Sciences accelerated equity-award expense (l.721). No COVID-19, "organic" or ZonePerfect wording
  (keyword check).
- Operative definitions, rules and scope exceptions: comparable definition l.47-49 verbatim as D08
  l.45-47. Diagnostics re-aggregation footnote l.183 = D08 l.127. Amulet transfer footnotes l.279,
  589, 625: "transferred from Structural Heart to Electrophysiology on January 1, 2026. As a result,
  $55 million of sales in the second quarter of 2025 and $101 million of sales in the first half of
  2025 were moved" (2Q25 Structural Heart 581 here, U.S. 249 / Intl 332, vs 636, U.S. 289 / Intl
  347 in D03 l.251; 1H25 1,112 vs 1,213 in D03 l.279). Multi-year agreement impact: 2Q25 (22), 1H25
  (46), none in 2Q26.
- Amendments or contradictions: guidance change stated with prior range (l.29). No internal
  conflict found; 2Q items sum with D08 1Q items to 1H (e.g. $945m + $1.362bn = $2.307bn; FX 414 +
  86 = 500; amortization 422 + 658 = 1,080).
- Coverage: FULL for readable text: l.1-762 read in one pass. Missing source text (18 markers,
  4,073 characters): l.67, 83, 105, 127, 203, 227, 247, 273 (segment % rows), l.347, 401
  (statement-of-earnings top rows above interest expense), l.443, 453, 469, 481 (EPS reconciliation
  rows), l.647, 679, 711, 743 (specified detail rows). Spot-check vs docs: 759 lines (+header),
  "Total reported 12,593 ..." (docs l.59 = text l.61), $385 million legal-reserve footnote (docs
  l.659 = text l.661), 18 markers match.

<!-- PASS B: D11 -->
## D11 - Abbott Preterm Infant Formula Litigation Settlement Press Release

- Source: text/D11.txt (docs/abt_ex991_2026-08-20.txt; 128 lines, 12,147 chars). Exhibit 99.1
  (l.3-9; tag "2 tm2623675d1_ex99-1.htm" l.5). Printed page numbers 1-5 alone at l.27, 55, 87,
  109, 127 (5 pages).
- Written or submitted by: Abbott ("ABBOTT PARK, Ill., Aug. 20, 2026 —", l.19; "About Abbott"
  l.111-115; contacts Scott Stoffel, Abbott Media, and Michael Comilla, Abbott Financial,
  l.117-123). Organisations quoted inside it are sources, not authors.
- Type, date, edition: press release dated Aug. 20, 2026 (l.19); headline "Abbott reaches
  agreements to resolve a portion of litigation involving its specialty formulas for preterm
  infants" (l.11).
- Settlement scope and amounts: "agreements with three law firms to resolve the Gill case and
  claims involving approximately 2,000 other individuals" (l.21; bullet l.13 the same); "In July
  2024, a St. Louis jury awarded the plaintiff in the Gill case $495 million in damages. Abbott
  appealed the verdict to the Missouri Court of Appeals in December 2024, but the appeal was
  denied. Rather than continuing to appeal or paying approximately $600 million, representing the
  Gill judgment plus accrued interest to date, Abbott entered into agreements to resolve the Gill
  case as well as necrotizing enterocolitis (NEC) claims asserted on behalf of approximately 2,000
  additional infants for an aggregate amount of approximately $670 million." (l.23). Qualifiers
  as printed: "$495 million" unqualified; "approximately" on $600 million, 2,000 and $670 million;
  the 2,000 are "other individuals" (l.13, l.21) and "additional infants" (l.23). Not stated: the
  judgment amount on its own, the interest amount, the appeal-denial date, the three firms' names,
  the Gill plaintiff's full name, payment timing or split of the $670 million.
- Remaining litigation (l.35): "roughly 1,700 lawsuits pending in federal and state courts
  involving claims on behalf of approximately 12,700 individual infants". The population
  "includes" 4 listed kinds (both Abbott and Mead Johnson named without identifying the formula;
  NEC diagnosed before any formula; never diagnosed with NEC; in multiple lawsuits), uncounted;
  last item "individuals who appear in multiple lawsuits in different jurisdictions".
- Court rulings (l.29-31): "victories in all three federal Multidistrict Litigation (MDL)
  bellwether cases"; "In July 2026, the U.S. Court of Appeals for the Seventh Circuit affirmed a
  pretrial judgment for Abbott in the first federal MDL bellwether case"; "In June 2026, the
  Illinois Appellate Court reversed a $60 million verdict against Mead Johnson" (learned
  intermediary doctrine; "a defense relevant in a substantial number of cases"); "In March 2026,
  a Florida state court ... also dismissed claims". FAQ l.105-107: "Watson v. Mead Johnson (Ill.
  App. Ct. 2026) and Ennix v. Abbott (Fla. Cir. Ct. 2026)" held the doctrine applies to NICU
  preterm formula. The text does not itself link these case names to the l.31 rulings. Judge
  "Rebecca R. Pallmeyer, the judge in the federal MDL" quoted (l.91). Doctrine stated at l.107.
- Dated statements (chronology as printed): NEC Society April 2024 (l.83-85); AAP July 2024
  (l.77); NEC Society July 2024 (l.79-81); AAP September 2024 (l.75); "In October 2024, the FDA,
  CDC and NIH said" (l.73); AAP "Earlier this year" (l.49, no date); brief "filed on Aug. 7, 2026,
  to the U.S. Supreme Court" (l.65 and again l.99; case not named). Undated: HHS Working Group
  report (l.47), CDC "About 1 in every 10" statistic (l.91), Pallmeyer statement (l.91).
- Abbott's own assertions vs attributed statements: Abbott asserts the agreements "are a
  compromise of disputed claims and not in any way an admission of liability" and "Abbott stands
  by the safety of these products" (l.25), "No." to formula causing NEC (l.47), "Abbott is one of
  only two companies in the U.S. providing these products" (other company unnamed) and "Abbott
  complies with all applicable FDA regulations" (l.53), and that FDA "has not asked for changes or
  additions to the ingredients or label" (l.53). Abbott's summaries of others: bullet l.17
  "Regulators and medical professionals recognize that these products are safe and necessary, and
  there is no reliable scientific evidence that they cause necrotizing enterocolitis"; l.25 list
  (Food and Drug Administration, National Institutes of Health, Centers for Disease Control and
  Prevention, American Academy of Pediatrics, NEC Society, "neonatologists and other medical
  professionals") "recognize that these products are safe and necessary"; l.71 "The FDA, CDC and
  NIH, the AAP, and the NEC Society agree". Direct quotes: FDA/CDC/NIH "There is no conclusive
  evidence that preterm infant formula causes NEC" (l.73); the "[a]vailable evidence supports the
  hypothesis that it is the absence of human milk ..." sentence is attributed to the HHS Working
  Group report at l.47 and to the FDA, CDC and NIH (October 2024) at l.73; AAP l.49, 61, 75, 77,
  91, 95; NEC Society l.61-63, 81, 85; Dr. Mark Corkins (University of Tennessee Health Science
  Center) l.49; six brief signatories l.65 and l.99 (AAP, North American Society for Pediatric
  Gastroenterology, Hepatology and Nutrition, National Association of Pediatric Nurse
  Practitioners, Perinatal Research Society, Children’s Hospitals Neonatal Consortium, March of
  Dimes, last).
- Mentioned-only organisations: St. Louis jury and Missouri Court of Appeals (l.23); Seventh
  Circuit, Illinois Appellate Court, Florida state court (l.31); Mead Johnson (l.31, 35, 105;
  defendant in the reversed verdict, co-named in claims); Department of Health and Human Services
  (organised the Working Group, l.47); U.S. Supreme Court (brief recipient, l.65, 99); three
  unnamed law firms (l.21).
- Hedged claims (claim -> hedge -> attachment): "the company believes these agreements are in its
  best long-term interest and represent a constructive step toward substantially resolving the
  overall litigation" ("believes", whole claim; "remains confident" on safety, l.33); quoted
  evidence "supports the hypothesis ... is associated with" (l.47, l.73); "no conclusive evidence"
  (l.73) vs Abbott's "no reliable scientific evidence" (l.17, l.25) and "No." (l.47); "These
  formulas can be critical" (l.73); "mothers ... may have trouble expressing a sufficient supply"
  ("may" on supply, not on formula's importance, l.63); "warned of potential impact on
  availability if manufacturers cannot continue supplying" (l.97). Count qualifiers: "roughly"
  1,700, "approximately" 12,700 (l.35).
- Definitions and aliases: "necrotizing enterocolitis (NEC)" (l.23) and "Necrotizing
  enterocolitis, or NEC, is an inflammatory intestinal disease, which typically affects premature
  infants" (l.41); "Multidistrict Litigation (MDL)" (l.29-31); "neonatal intensive care units
  (NICUs)" (l.71); preterm formulas "differ from infant formulas for full-term infants that are
  sold in stores directly to parents and caregivers" (l.53); learned intermediary doctrine
  (l.107). FDA, CDC, NIH and AAP abbreviations are used (l.49 onward) without an explicit
  expansion; the full names appear in the l.25 list. "ICU" undefined (l.85). Product named only in
  a bracketed insertion in Pallmeyer's quote: "[Similac Special Care 24]" (l.91).
- Exclusion and negative evidence: no accounting charge, reserve, EPS or earnings effect, quarter,
  insurance or prior-financial-reporting statement (grep "charge" hit is "discharge" l.85;
  "Financial" is the contact label l.121; "accru" only "accrued interest" l.23). No mention of the
  2022 recall, Sturgis, the derivative suit or Exact Sciences.
- Rounded prose beside exact figures: all figures are prose; "122,000 colleagues serve people in
  more than 160 countries" (l.113). Tables: not applicable.
- Notes: layout splits at l.29/31, 43/45, 59/61, 79/81, 83/85, 105/107 (no text missing).
- Extraction spot-checks: docs = text minus 2 header lines (docs l.17 dateline = l.19; docs l.21
  = l.23; docs l.125 "5" = l.127). Tables and footnotes: not applicable.
- Coverage: full. Read l.1-128 in one chunk; no gap markers; nothing unread.

## Shared ground (navigation only)

<!-- PASS A: shared -->
### Earnings-release series (pass A)

Locations are text/Dnn.txt lines. All seven releases are issued by Abbott; fiscal year = calendar
year in every edition. Facts only; the author owns hooks.

- Editions in date order (period; printed pages; markers): D01 2025-01-22 (4Q24/12M24; 20 pp; 24
  markers, 5,198 chars), D02 2025-04-16 (1Q25; 15 pp; 10, 2,192), D03 2025-07-17 (2Q25/1H25; 20 pp;
  20, 4,344), D04 2025-10-15 (3Q25/9M25; 20 pp; 20, 4,227), D07 2026-01-22 (4Q25/12M25; 20 pp; 20,
  4,355), D08 2026-04-16 (1Q26; 15 pp; 9, 2,060), D10 2026-07-16 (2Q26/1H26; 21 pp; 18, 4,073).
  Pass-A total 121 markers, 26,449 characters. Pass-B file dates fall between: D05 2025-11-20 and
  D06 2025-12-12 (between D04 and D07), D09 2026-04-17 (day after D08), D11 2026-08-20 (after D10).
- Headline guidance verbs: D01 l.15 "Issues 2025 Financial Outlook"; D02 l.15 "Reaffirms Full-Year
  Guidance"; D03 l.15 none; D04 l.15 "Reaffirms Full-Year Guidance" (body l.31/287 also "narrows"
  the EPS range); D07 l.15 "Issues 2026 Financial Outlook"; D08 l.15 "Updates Guidance to Reflect
  Acquisition of Exact Sciences"; D10 l.15 "Raises Full-Year EPS Guidance".
- FY2025 guidance editions: sales growth D01 l.37/315 and D02 l.197 "organic sales growth ... 7.5%
  to 8.5%" (no COVID basis); D03 l.29/295 "excluding COVID-19 testing-related sales, to be 7.5% to
  8.0%, or 6.0% to 7.0% when including"; D04 l.287 reaffirms the D03 pair. Adjusted operating margin
  D01 l.39/317, D02 l.199 "23.5% to 24.0%"; D03 l.297 "approximately 23.5%"; none in D04/D07.
  Adjusted EPS D01 l.41/319, D02 l.201 "$5.05 to $5.25"; D03 l.31/299 "$5.10 to $5.20"; D04 l.31/287
  "$5.12 to $5.18" (midpoint reaffirmed; prior range not printed). Only D10 prints a prior range.
- FY2025 actuals (D07): sales +5.7% reported, +5.5% organic, +6.7% excl. COVID (l.25; table l.91,
  revenue reconciliation l.575); adjusted EPS $5.15 (l.27, 409; +10.3%, prose "10 percent"); GAAP EPS
  $3.72. No FY2025 adjusted operating margin figure in D07 (only Ford "we expanded margins", l.41).
  Quarterly adjusted operating margin printed only for 1Q25 21.0% (D02 l.19), 2Q25 22.9% (D03 l.19),
  3Q25 23.0% (D04 l.19).
- FY2026 guidance editions: D07 l.29/281 "organic sales growth ... 6.5% to 7.5%", l.31/283 EPS
  "$5.55 to $5.80"; D08 l.29/201 "comparable sales growth of 6.5% to 7.5%", l.31/203 EPS "$5.38 to
  $5.58, which includes $0.20 of dilution related to the acquisition of Exact Sciences"; D10
  l.27/287 reaffirms comparable 6.5%-7.5%, l.29 raises EPS "to $5.45 to $5.60, compared to previous
  range of $5.38 to $5.58" (l.289 restates the range without the dilution figure). No FY2026 actual
  in the bundle's releases; 1H26 comparable growth 4.3% (D10 l.613), adjusted EPS $2.46 (D10 l.411).
- Next-quarter adjusted EPS forecast -> actual: 1Q25 $1.05-$1.09 (D01 l.319) -> $1.09 (D02 l.17,
  269); 2Q25 $1.23-$1.27 (D02 l.201) -> $1.26 (D03 l.17, 369); 3Q25 $1.28-$1.32 (D03 l.299) -> $1.30
  (D04 l.17, 355); 4Q25 no range in D04 -> $1.50 (D07 l.23, 357); 1Q26 $1.12-$1.18 (D07 l.283) ->
  $1.15 (D08 l.17, 277); 2Q26 $1.25-$1.31 (D08 l.205) -> $1.31 (D10 l.17, 365); 3Q26 $1.38-$1.46
  (D10 l.291) -> no actual in bundle.
- Exact Sciences across releases: agreement "In November" and expected close "in the second quarter
  of 2026" (D07 l.33); completed "On March 23, 2026" (D08 l.27, 47, 127, 137, 403; D10 l.49, 183,
  593, 629); presented as Cancer Diagnostics (D08 l.127; D10 l.183); 2025 Exact Sciences sales
  "$3.247 billion" (U.S. $3.145bn, international $102m) (D08 l.245 = D10 l.331); pre-acquisition
  sales in comparable bases: 1Q25 707, 1Q26 706 (D08 l.389), 2Q25 811 (D10 l.581), 1H25 1,518 and
  1H26 706 (D10 l.617); reported Cancer Dx 96 (1Q26), 919 (2Q26), 1,015 (1H26); comparable growth
  13.4% / 13.3% / 13.3%; $0.20 FY2026 EPS dilution (D08 l.19, 31, 203); accelerated equity-award
  expense (D08 l.429; D10 l.721); inventory step-up amortization (D10 l.657, 721). Intangible
  amortization 422 (1Q26, D08 l.315) -> 658 (2Q26, D10 l.441); 2Q26 "Interest expense, net" 299 vs
  50 (D10 l.349; no reason stated). D01-D04 contain no Exact Sciences mention (keyword check).
- Repeated comparatives that match the original edition: 4Q24 and FY2024 statement lines, tax rates,
  $6.880bn/$5.202bn specified items and the $7.497bn tax footnote (D01 l.407-461, 433-481, 559-597
  = D07 l.343-411, 373-429, 517-559); 4Q24 COVID $176m and Dx $2.520bn (D01 l.181, 165 = D07 l.167,
  323); FY2024 $41.950bn / Dx $9.341bn / COVID $747m (D01 l.361, 195 = D07 l.325); 1Q25 statement,
  tax rate and $200m deferred-tax item (D02 l.259-271, 283, 333-337 = D08 l.263-279, 293, 361-365);
  2Q25 and 1H25 statement lines and tax footnotes (D03 l.359-371, 383, 403-411, 425 = D10 l.353-367,
  381, 403-411, 427; D10's 2Q25 interest and net-FX rows, l.349-351, have no visible D03
  counterpart because D03 gap l.357 covers them); 2025 totals $44.328bn / U.S. $17.126bn / Intl $27.202bn (D07 l.79-81, 325 =
  D08 l.245 = D10 l.331). Prior-year quarter totals appear only as footnote comparatives: 1Q24
  $9.964bn (D02 l.241), 2Q24 $10.377bn and 1H24 $20.341bn (D03 l.339-341), 3Q24 $10.635bn and 9M24
  $30.976bn (D04 l.327-329); 4Q23 $10.241bn and FY2023 $40.109bn (D01 l.359-361).
- Changed or restated figures for the same period: (1) Structural Heart recast for the Amulet move
  "on Jan. 1, 2026": 1Q25 577 (D02 l.173) vs 531 (D08 l.395; $46m, l.187/399); 2Q25 636 (D03 l.251)
  vs 581 (D10 l.585; $55m, l.279/589); 1H25 1,213 (D03 l.279) vs 1,112 (D10 l.621; $101m, l.279/625).
  (2) Diagnostics sub-business re-aggregation "Beginning in 2026" (D08 l.127; D10 l.183) replaces the
  D01-D07 columns Core Laboratory / Molecular / Point of Care / Rapid Diagnostics. (3) FY2024
  ZonePerfect "Impact from business exit": (14) in D01 l.651-655 (4Q24 (1), l.635-639) vs (13) for
  the 12M24 base in D07 l.575-579 (1Q24, 1H24, 9M24 bases all (13): D02 l.369, D03 l.577, D04 l.555);
  no edition states precedence. (4) 1Q25 specified items "net after-tax charges of $594 million"
  (D02 l.287) vs "net after-tax benefits of $594 million" (D08 l.297). (5) 4Q24 wording: D07 l.633
  (a) adds "other costs related to business acquisitions" absent in D01 l.693; D07 l.461 omits
  "intangible impairments" present in D01 l.499. (6) Basis change of the sales-growth metric:
  organic (D01-D07) -> comparable (D08 l.45-47, D10 l.47-49).
- Per-share figures that do not sum across editions (as printed): 9M25 GAAP EPS $2.70 (D04 l.389) vs
  1H25 $1.77 (D03 l.409) + 3Q25 $0.94 (D04 l.353); FY2025 GAAP $3.72 (D07 l.407) vs 9M25 $2.70 +
  4Q25 $1.01; FY2025 specified items $1.43/share (D07 l.427) vs 9M25 $0.95 (D04 l.409) + 4Q25 $0.49
  (D07 l.375); FY2024 GAAP $7.64 (D01 l.457) vs 9M24 $2.38 (D04 l.389) + 4Q24 $5.27. Dollar amounts
  and adjusted EPS sum in each case checked (e.g. $3.65 + $1.50 = $5.15).
- Definitions by edition: organic = FX + ZonePerfect exclusion (D01 l.51, D02 l.43, D03 l.47, D04
  l.45, D07 l.47); organic-excluding-COVID rationale sentence: D01 l.51 ("underlying base business
  performance in 2024"), absent in D02, reworded in D03/D04/D07 ("pandemic to endemic phase");
  comparable (D08/D10, with Exact Sciences and multi-year-agreement terms). FX method note identical
  in all seven (D01 l.53, D02 l.45, D03 l.49, D04 l.47, D07 l.49, D08 l.49, D10 l.51). ZonePerfect
  "initiated in March 2024" footnotes in D01-D07; CSI (acquired April 27, 2023) only in D01.
  Multi-year agreement with "a competitor": impact 1Q25 (24) (D08 l.385), 2Q25 (22) and 1H25 (46)
  (D10 l.577, 613), 1Q26 (8); "$89 million" received in 2025 (D08 l.245; D10 l.331); final payment
  in 1Q26 (D08 l.47, 405; D10 l.49, 595, 631).
- Tax items per period. Prior-year tax positions: 4Q23/FY2023 ~$80m expense (D01 l.477, 617; the
  4Q23 and 12M23 tax-rate rows both carry footnote 2, l.575/609); 1Q24 ~$10m expense (D02 l.285);
  2Q24 ~$25m and 1H24/9M24 ~$35m expense (D03 l.385, 427; D04 l.407); 3Q24 none stated; 4Q24 none
  beyond the $7.497bn item, which cites "the confirmation of certain tax filing positions" (D01 l.433);
  1Q25 none; 2Q25, 1H25, 9M25 ~$90m benefit (D03 l.383, 425; D04 l.405); 3Q25 none; 4Q25 ~$20m
  expense (D07 l.371); FY2025 ~$70m benefit (D07 l.423); 1Q26 ~$50m benefit (D08 l.291); 2Q26 ~$110m
  expense "primarily" (D10 l.379); 1H26 ~$60m expense "primarily" (D10 l.425). Deferred-tax-benefit
  adjustments: 1Q25 ~$200m (D02 l.283), 2Q25 ~$100m, 1H25 ~$300m (D03 l.383, 425), 3Q25 ~$160m, 9M25
  ~$460m (D04 l.369, 405), 4Q25 ~$150m, FY2025 ~$610m (D07 l.371, 423), 1Q26 ~$200m (D08 l.291),
  2Q26 ~$240m, 1H26 ~$440m (D10 l.379, 425). 4Q24 $7.497bn valuation allowance (D01 l.433); no
  release states that the later adjustments relate to it. Adjusted tax rates: 15.0% (4Q24, FY24),
  16.5% (1Q25-3Q25), 14.8% (4Q25), 16.0% (FY25), 15.2% (1Q26, 2Q26, 1H26).
- Legal and litigation items: 4Q25/FY2025 "$165 million for legal reserves related to a certain
  agreed-upon settlement" (D07 l.605, 669); 2Q26/1H26 "$385 million for legal reserves related to an
  agreed-in-principle settlement, subject to satisfaction of certain contingencies" (D10 l.661,
  725). Neither names the matter. None in D01-D04 or D08 (keyword check; PSLRA boilerplate only).
  Pass B documents D09 (2026-04-17) and D11 (2026-08-20) concern settlements; date order only.
- Dividends (number, declared, record, payable, amount): 404th Dec. 13, 2024 / Jan. 15 / Feb. 14,
  2025 / $0.59 (D01 l.325); 405th Feb. 21 / April 15 / May 15, 2025 / $0.59 (D02 l.207); 406th June
  13 / July 15 / Aug. 15, 2025 / $0.59 (D03 l.305); 407th Sept. 19 / Oct. 15 / Nov. 17, 2025 / $0.59
  (D04 l.293); 408th Dec. 12, 2025 / Jan. 15 / Feb. 13, 2026 / $0.63 (D07 l.289); 409th Feb. 20 /
  April 15 / May 15, 2026 / $0.63 (D08 l.211); 410th June 12 / July 15 / Aug. 17, 2026 / $0.63 (D10
  l.297). "53 consecutive years" D01-D04, "54" D07-D10. No sentence describes the $0.59 -> $0.63
  change itself (each dividend paragraph gives only the amount and the consecutive-years count). D10 l.19: "$2.1 billion" returned in 2Q26 via dividends and repurchases.
- Dated events reported after the quarter end or between releases (month-only bullets print no
  year): D07 "In November" (Exact agreement), "In December" (Volt FDA), "In January" (TactiFlex Duo
  CE Mark, after the Dec. 31, 2025 quarter end) l.33-39; D08 "In January" AtaCor, "In February"
  VERITAS, "In March" FreeDM2, March 23, 2026 closing, Jan. 1, 2026 Amulet transfer (l.27-37, 187);
  D10 April/May bullets l.31-39. Each 2025 release's bullets: D02 three "In March" (l.29-33); D03
  "In April" x2, "In May" (l.33-37); D04 "In July", "In August" x2 (l.33-37).
- Program threads across editions: Volt PFA CE Mark (D02 l.29) -> FDA approval (D07 l.37); TECTONIC
  initiation (D02 l.31) -> enrollment completed (D10 l.31); TactiFlex Duo: FlexPulse IDE enrollment
  (D03 l.33, "TactiFlex(TM) Duo Pulsed Field Ablation (PFA) System") -> CE Mark (D07 l.39,
  "TactiFlex(TM) Duo Ablation Catheter, Sensor Enabled(TM)"); TriClip: TRILUMINATE data (D02 l.33)
  -> Japan approval (D04 l.33) -> ESC guidelines (D04 l.37); AVEIR CSP data (D03 l.35); HRS data for the PFA
  and CSP portfolios (D10 l.33; AVEIR not named); Amulet: Amplatzer Amulet in brand lists (D01 l.281, D02 l.189; absent D03 l.267),
  Amulet 360 VERITAS (D08 l.35) -> FDA submission (D10 l.37), Amulet moved to EP (D08 l.187, D10
  l.279); Navitor CE Mark expanded indication (D04 l.35); FreeStyle Libre FreeDM2 (D08 l.37), Libre
  Duo CE Mark (D10 l.35); Cologuard (D08 l.137 "double-digit growth"; D10 l.39 ACS, l.163 "mid-teens
  growth"); Nutrition pricing actions in 4Q25 (D07 l.125) -> effect described (D08 l.95, D10 l.113).
  No later release reports on the Illinois/Texas investments (D02 l.35) or the Georgia facility
  (D03 l.39) (keyword check).
- Item lists by edition: "Several products contributed" lists D01 l.281 and D02 l.189 (5 items),
  D03 l.267 (4 items), none later. MD growth-leader lists D02 l.187, D03 l.265, D04 l.261, D07 l.257,
  D08 l.193, D10 l.255 (members and order differ by edition). KEM drivers: D01 l.235 (therapeutic
  areas), D02 l.163 / D03 l.221 / D04 l.217 (Asia, Latin America, Middle East), D07 l.213 (India,
  Latin America, Middle East), D08 l.165 / D10 l.211 (Latin America and Asia Pacific). Counted sets:
  "more than 15" (D01 l.35), "two" investments (D02 l.35), "two significant regulatory approvals"
  (D07 l.35), "four clinical trials" (D10 l.33, unnamed).
- Issuer vs mentioned organizations: Abbott issues all seven. Mentioned: CSI, Exact Sciences, AtaCor
  Medical, an unnamed competitor, FDA, EU MDR/IVDR, European Society of Cardiology (D04 l.37,
  guidelines "were issued" at its Congress), Heart Rhythm Society (D10 l.33, conference), American
  Cancer Society (D10 l.39, "issued updated ... guidelines"), S&P 500 Dividend Aristocrats Index,
  China volume-based procurement programs (D02 l.131; D03 l.173; D04 l.173; D07 l.169).
- Actions vs mentions (as worded): approvals/marks obtained D02 l.29, D03 l.37 (Tendyne FDA), D04
  l.33, l.35, D07 l.37, l.39, D10 l.35; acquisition agreed (D07 l.33) vs completed (D08 l.27); FDA
  submission only (D10 l.37); trials/data/enrollment/plans/collaboration (D02 l.31, 33, 35; D03 l.33,
  35, 39; D08 l.33, 35, 37; D10 l.31, 33); third-party guideline actions (D04 l.37; D10 l.39).
- Hedge scope: D02 l.35 "projected to go live by the end of 2025"; D03 l.39 "to be completed by
  2028"; D07 l.33 "continues to expect the transaction to close"; D07 l.125 "expects to increase
  volume growth"; D08 l.95 "are expected to contribute"; D10 l.113 "are contributing" (unhedged);
  D07 "agreed-upon settlement" vs D10 "agreed-in-principle ... subject to satisfaction of certain
  contingencies"; D03 l.297 "approximately 23.5%". CEO outlook quotes D01 l.43, D03 l.41, D07 l.41,
  D08 l.39, D10 l.41. Forward-looking caution cites the FY2023 10-K (D01 l.345), FY2024 10-K
  (D02 l.225, D03 l.323, D04 l.311, D07 l.307) and FY2025 10-K (D08 l.229, D10 l.315).
- Exclusion and absence facts: no Q4 2025 EPS range and no operating-margin guidance in D04; no
  operating-margin guidance in D07/D08/D10; no COVID-19, "organic" or ZonePerfect wording in D08 or
  D10; no CGM dollar figure in D08 (l.195) or D10 (l.257); no statement in D07 on whether 2026
  guidance includes Exact Sciences.
- COVID-19 testing sales series (prose + footnotes): 4Q23 $288m, FY2023 $1.586bn (D01 l.181,
  359-361); 1Q24 $204m / 1Q25 $84m (D02 l.133, 241); 2Q24 $102m / 2Q25 $55m, 1H24 $306m / 1H25
  $139m (D03 l.175, 339-341); 3Q24 $265m / 3Q25 $69m, 9M24 $571m / 9M25 $208m (D04 l.171, 327-329);
  4Q24 $176m / 4Q25 $89m, FY2024 $747m / FY2025 $297m (D07 l.167, 323-325). The same "$89 million"
  is also the 2025 Structural Heart compensation-payment figure (D08 l.245).
- CGM / Diabetes Care by quarter (CGM prose; Diabetes Care table column): 4Q24 $1.8bn / 1,863 (D01
  l.283, 267); 1Q25 $1.7bn / 1,827 (D02 l.191, 173); 2Q25 $1.9bn / 1,981 (D03 l.269, 251); 3Q25
  $2.0bn / 2,057 (D04 l.263, 247); 4Q25 $2.0bn / 2,133 (D07 l.259, 243); 1Q26 growth only / 2,080
  (D08 l.195, 175); 2Q26 growth only / 2,188 (D10 l.257, 241). FY Diabetes Care 6,805 (D01 l.295),
  7,998 (D07 l.265).
- Rounded prose beside exact figures (all editions): adjusted EPS growth D02 l.25 "double-digit" vs
  11.2% (l.269); D03 l.25 "double-digit" vs 10.5% (l.369); D07 l.23 "12 percent" vs 11.9% (l.357)
  and l.27 "10 percent" vs 10.3% (l.409); D08 l.25 "6 percent" vs 5.5% (l.277); D04 and D10 bullets
  state no growth (7.4%, 4.0%). Sales in billions D01 l.17/27, D07 l.25 vs table totals. D01 l.285
  MD "$19 billion ... more than $2 billion". D10 l.163 Cologuard "mid-teens" vs Cancer Dx 13.3%.
- Narrative passages that repeat table results: opening bullets restate total sales growth and EPS
  (D01 l.23-31; D02 l.23-25; D03 l.23-27; D04 l.23-27; D07 l.21-27; D08 l.23-25; D10 l.23-25).
  Segment prose states worldwide segment growth whose table rows are clipped: D01 l.129-133, 183,
  233-235, 279-285; D02 l.99-103, 129, 135, 161-163, 185; D03 l.129-131, 171, 177, 219-221, 263; D04
  l.127-129, 169, 173, 215-217, 259; D07 l.123, 165, 169, 211-213, 255; D08 l.93, 131, 163-165, 191;
  D10 l.111, 157, 209-211, 253. Revenue reconciliations also print worldwide reported/organic or
  comparable growth for listed lines (D01 l.635-659; D02 l.369-373; D03 l.577-581; D04 l.555-559;
  D07 l.575-579; D08 l.385-395; D10 l.577-585, 613-621). D01 l.43 says fourth-quarter sales and EPS
  growth "were the highest of the year"; 2024 quarterly growth rates are not printed in these
  releases.
- Table-layout notes: rows following a marker lose their label (the "Organic"/"Comparable" heading
  sits in the gap) in the Nutrition, EPD and MD tables of all seven releases, in the Diagnostics
  tables of D02, D03, D04 and D07, in D02's total-company table and in D08 l.67 / D10 l.69, 85; their
  values match the revenue-reconciliation organic/comparable columns where both exist. D01's
  total-company and Diagnostics tables keep "Impact of COVID-19 testing sales" and "Organic
  (excluding COVID-19 tests)" labels after the gap, and their following geography rows (l.75-77,
  97-99, 177-179, 207) are excl.-COVID rows (U.S. 13.5 vs reconciliation organic 10.4, l.635). The
  total-company tables of D03, D04 and D07 also print an explicit "Organic" label (D03 l.71, 95; D04
  l.69, 93; D07 l.71, 93). Several table rows are run together on one line (e.g. D01 l.85, 165, 267; D10 l.149, 177).
  D08 l.395 Structural Heart rows carry an extra "-" before each 1Q25 figure. Diagnostics tables in
  D08 (l.103-125) and D10 (l.139-183) have no markers.
- Contacts and boilerplate: "Tamika LeBean" (D01 l.351) and "Tamika McLoughlin" (D02 l.231 onward)
  list the same 224-399-5082; Randy Blakley added in D02 (224-361-7966, D02 l.233, D03 l.331) and
  224-668-0036 from D04 (l.319). Employees 114,000 (D01-D04), 115,000 (D07 l.295), 122,000 (D08
  l.217, D10 l.303). Call 8:30 a.m. CT (D01 l.335), 8 a.m. CT thereafter.
- Pass-A gaps: all seven releases read in full (every line); only marker text is missing (lines
  listed in each document's Coverage field). No unread ranges remain.

<!-- PASS B: shared -->
### Deal, governance and litigation documents (pass B)

Locations only; pass A owns the earnings-release tables cited here.

- Acquisition timing (forecast vs actual): D05 l.49 "The closing is expected in the second quarter
  of 2026"; D07 l.33 "Abbott continues to expect the transaction to close in the second quarter
  of 2026"; completion "March 23, 2026" at D08 l.27, 47, 127, 137, 403 and D10 l.49, 183, 593,
  629. Quarter labels: D08 l.21 "first quarter ended March 31, 2026"; D10 l.21 "second quarter
  ended June 30, 2026".
- Acquisition effects: D05 l.23 "immediately accretive to Abbott’s revenue growth and gross
  margin" (D05 has no EPS statement) vs D08 l.19, 31, 203 2026 adjusted diluted EPS guidance
  "includes $0.20 of dilution related to the acquisition of Exact Sciences"; D10 l.19, 29 raise
  the range to "$5.45 to $5.60, compared to previous range of $5.38 to $5.58" without restating
  dilution ("dilution" occurs only in D08). Acquisition-cost notes: D08 l.429, D10 l.721 (D10 adds
  "inventory step-up amortization").
- Exact Sciences size: D05 l.51 "projected to generate more than $3 billion in revenue this year"
  (release of Nov. 20, 2025) vs D08 l.245 and D10 l.331 "in 2025, total worldwide sales for Exact
  Sciences were $3.247 billion, which included U.S. sales of $3.145 billion and international sales
  of $102 million" ("revenue" vs "sales" as printed). D05 l.51 "Abbott’s total diagnostics sales
  will exceed $12 billion annually" after completion; Abbott total Diagnostics sales "$8.937
  billion" (full-year 2025) and "$9.341 billion" (full year 2024) at D07 l.325; Total/Cancer
  Diagnostics rows at D08 l.387-389, D10 l.579-581 and l.615-617. Exact Sciences sales "are
  presented as Abbott's Cancer Diagnostics business" (D08 l.127, D10 l.183); comparable growth
  "includes the prior and current year sales of Exact Sciences" (D08 l.47, D10 l.49).
- Products and the American Cancer Society: Cologuard/Cologuard Plus D05 l.21, 35, 73; D08 l.137;
  D10 l.39, 163. "CancerguardTM" D05 l.35, 75 = "Cancerguard®, a multi-cancer screening test that
  launched last year" D08 l.137. American Cancer Society: source footnote for D05's cancer figures
  (l.157-159); issuer of May 2026 CRC screening guidelines, "American Cancer Society (ACS)" (D10
  l.39).
- Legal reserves vs the litigation documents (no document links them to a named matter): D07
  l.605 (Q4 2025 table, l.587) and l.669 (twelve months 2025, l.647) "$165 million for legal
  reserves related to a certain agreed-upon settlement"; D10 l.661 (Q2 2026, l.639) and l.725
  (first half 2026, l.703) "$385 million for legal reserves related to an agreed-in-principle
  settlement, subject to satisfaction of certain contingencies"; Q2 2025 note has none (D10 l.693).
  Summary mentions of "legal reserves": D07 l.375, 427, 451, 475; D10 l.383, 429, 445, 471. D11
  (Aug. 20, 2026) states "an aggregate amount of approximately $670 million" (l.23) and nothing
  on charges or reserves. D09 (April 17, 2026) states governance terms and a fee cap of "not more
  than $15.85 million" (l.121), with no settlement payment or accounting. No earnings release
  mentions NEC, preterm formula, Gill, Mead Johnson, the 2022 recall, Sturgis, the derivative
  action or its hearing (grep across D01-D04, D07, D08, D10).
- Two infant-formula matters: D09 concerns "infant formula products in the United States", the
  "February 2022 recall of powdered infant formula" and the "Sturgis, Michigan, or Casa Grande
  Arizona" facilities (l.99, l.225-227); D11 concerns NEC claims over "specialty formulas for
  preterm infants", which "differ from infant formulas for full-term infants that are sold in
  stores directly to parents and caregivers" (l.11, l.53). Neither refers to the other's matter.
  D01 l.131: U.S. Pediatric Nutrition sales "reflect continued market share gains in the infant
  formula business".
- Courts, judges, counsel (each in one document only; grep confirmed): D09 N.D. Ill. Eastern
  Division, Judges Harjani and McNally, Cohen Milstein, Scott+Scott, Latham & Watkins ("Abbott’s
  Counsel"), Kirkland & Ellis ("Individual Defendants’ Counsel"). D11 St. Louis jury and Missouri
  Court of Appeals (l.23), Seventh Circuit, Illinois Appellate Court, a Florida state court
  (l.31), U.S. Supreme Court brief (l.65, 99), Judge Rebecca R. Pallmeyer of "the federal MDL"
  (l.91), three unnamed law firms (l.21). D05 deal advisers l.105 (Morgan Stanley and Wachtell for
  Abbott; Centerview, XMS Capital and Skadden for Exact Sciences).
- People and contacts: Robert B. Ford "chairman and chief executive officer, Abbott" at D05 l.41
  and D01 l.43, D02 l.37, D03 l.41, D04 l.39, D07 l.41, D08 l.39, D10 l.41; absent from D06, D09,
  D11 (D06 names offices only: Chair of the Board l.375, 439; CEO l.501, 525). Michael Comilla
  (Abbott Financial) in every release (D05 l.147, D11 l.123; D01 l.349, D02 l.229, D03 l.327, D04
  l.315, D07 l.311, D08 l.233, D10 l.319). Scott Stoffel (Abbott Media) only D05 l.143 and D11
  l.119; earnings releases list other media contacts (e.g. D10 l.325-329). Kevin Conroy only D05.
- "About Abbott" counts: "Our 114,000 colleagues" D01 l.331, D02 l.213, D03 l.311, D04 l.299, D05
  l.113; "115,000" D07 l.295; "122,000" D08 l.217, D10 l.303, D11 l.113; all "more than 160
  countries". D05 l.43: "7,000 Exact Sciences’ team members".
- By-law rules and instances described elsewhere (located, not applied):
  - Fiscal year Jan. 1-Dec. 31 (D06 l.617); releases use calendar quarters (D08 l.21, D10 l.21)
    and full years (D07 l.325); 10-K "year ended December 31, 2024" (D05 l.135) and "Dec. 31,
    2025" (D10 l.315).
  - Dividend record dates: D06 Art. II S5 (l.215) covers "shareholders entitled to receive payment
    of any dividend", record date "not more than sixty (60) days" (the sentence ends "immediately
    preceding such meeting"). Declared / record / payable / amount: D01 l.325 Dec. 13, 2024 / Jan.
    15, 2025 / Feb. 14, 2025 / $0.59 (404th); D02 l.207 Feb. 21, 2025 / April 15, 2025 / May 15,
    2025 / $0.59 (405th); D03 l.305 June 13, 2025 / July 15, 2025 / Aug. 15, 2025 / $0.59 (406th);
    D04 l.293 Sept. 19, 2025 / Oct. 15, 2025 / Nov. 17, 2025 / $0.59 (407th); D07 l.289 Dec. 12,
    2025 / Jan. 15, 2026 / Feb. 13, 2026 / $0.63 (408th); D08 l.211 Feb. 20, 2026 / April 15, 2026
    / May 15, 2026 / $0.63 (409th); D10 l.297 June 12, 2026 / July 15, 2026 / Aug. 17, 2026 /
    $0.63 (410th). "53 consecutive years" D01 l.327, D02 l.209, D03 l.307, D04 l.295; "54" D07
    l.291, D08 l.213, D10 l.299. Related by-law text: regular Board meetings "on the second Friday
    of every month at 9:00 a.m." (D06 l.395); distributions (Art. IX l.633).
  - Same date: by-laws effective "December 12, 2025" (D06 l.19); 408th dividend declared "On Dec.
    12, 2025" (D07 l.289).
  - Committees: D06 l.449 "Each committee shall have one or more members"; five named committees
    l.455-493. D09's "Special Litigation Committee and its member" (l.215, 219) is not one of the
    five; D09 says nothing about how it was formed.
  - Indemnification: D06 Art. XIII (l.663-665) rights to enforce "Article VI of the Articles of
    Incorporation"; D09's Individual Defendants are "certain current and former directors and
    officers" (l.67); D09 mentions no indemnification or insurance; D06 has no forum or
    derivative-suit clause.
  - Listing and seat: D06 refers to the "principal U.S. exchange upon which the common shares of
    the Corporation are listed" unnamed (l.345-347, 357-359) and NYSE trading days (l.281); D05
    l.27 "Abbott (NYSE: ABT)". D06 Illinois incorporation (l.583, 643), principal office in "the
    County of Lake" (l.27); releases datelined "ABBOTT PARK, Ill." (D05 l.27, D08 l.21, D10 l.21,
    D11 l.19); D06 never names Abbott Park.
  - No Abbott annual-meeting date anywhere except the 1963 adoption meeting (D06 l.17); "thirteen"
    directors only at D06 l.391.
- Date adjacency (as printed): D08 April 16, 2026 (l.21), D09 April 17, 2026 (l.271); D09 hearing
  June 4, 2026 falls in the quarter D10 reports, and D10 does not mention it; D10 July 16, 2026
  (l.21), D11 Aug. 20, 2026 (l.19).
- Repeated passages inside pass B documents: D05 deal terms l.27 and l.47; D09 hearing l.73 and
  l.133, May 18 deadline l.143 and l.203; D11 "approximately 2,000" l.13, 21, 23; Aug. 7 brief l.65
  and l.99; "absence of human milk" quote at l.47 (HHS Working Group) and l.73 (FDA, CDC and NIH,
  October 2024); AAP "not always enough ... supply" l.75 and l.91 (bracketed "[human milk]").
- Aliases supported elsewhere: "U.S. Food and Drug Administration (FDA)" expanded at D03 l.37, D07
  l.37, D10 l.37 (D11 uses both forms unlinked, l.25, 53, 71-73); "American Cancer Society (ACS)"
  D10 l.39.
- Contradictions: none found among the facts above for the same period. Changed statements over
  time: the closing expectation (D05 l.49, D07 l.33) vs completion (D08 l.27); employee counts
  (above). D06's internal tensions are listed in its own section.
