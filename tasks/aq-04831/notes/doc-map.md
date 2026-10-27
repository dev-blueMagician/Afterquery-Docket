# aq-04831 - document map

Navigation only (locations are line numbers in `text/Dnn.txt`). Questions quote the documents, never this map.

## Bundle

- What it is: "Industry research", eight loosely related public papers: APRA's CPG 229 guide, four RBA Bulletin
  articles (climate risk to banks 2021, physical risk in repo-eligible RMBS 2024, sovereign green debt Jan 2025,
  Australian coal 2019, commodity-price drivers 2019), Treasury's PRRT gas transfer pricing review (May 2023) and a
  Stats NZ environmental account (April 2017).
- Documents: 8. Local ids are alphabetical and differ from the page: D07 = Doc 1, D04 = Doc 2, D01 = Doc 3,
  D03 = Doc 4, D08 = Doc 5, D05 = Doc 6, D06 = Doc 7, D02 = Doc 8 (notes/intake.json).
- Gaps: none in the capture (8 of 8 read in full; every doc matches the capture). Graph bodies are not text: graph
  axis labels and data labels are scattered (D01 Graphs 1-6, D04 Graphs 1-8, D03 Graphs 1-5, D08 Graphs 1-17, D05
  Graphs 1-8, D06 Chart 8.1). D02 Tables 1-2 and D01 Table 2 are flattened out of column order (see notes below);
  D06 Table 8.1's low-price row is split ("200", "300" after the footnotes).
- Extraction spot-checks: all eight texts read in full by the caller 2026-10-14 against the capture; table
  reconstruction checked by arithmetic (D02 Table 1 rows sum to the renewables totals; D02 net generation values
  average 42,487 GWh as the text says; D01 Table 2 deal counts 106 + 94 + 64 = 264, not the text's 283 deals).
- Provenance: notes/intake.json (capture AQ-04831_2026-10-14_1113.txt, sha 6ef19d2a...), all `matches_capture: true`.
- Repeat check: no document shared with any bundle in 10.6, 10.7, 10.8 or docket-capture (file names and five
  distinctive phrases searched 2026-10-14; AQ-04830 only mentions Green Treasury Bonds in a budget paper).

## D07 = Doc 1 - APRA CPG 229 Climate Change Financial Risks (November 2021)

- Definitions (l.83-91): "climate risks" = physical, transition and liability risks; "APRA-regulated institution"
  = ADI, RSE licensee, general insurer, life company (incl. friendly societies), private health insurer, NOHC,
  Level 2/3 groups. Physical risk chronic vs acute (l.134). Risk channels a-f (l.150-174). Sector criteria a-f
  (l.295-321). Mitigation a-c (l.376-388).
- Scenario guidance (l.425-449): 3 deg C or more by 2100 vs well below 2 deg C; orderly vs disorderly. Footnote 8
  (l.469): pathways relative to 1850-1900; "APRA does not expect entities to conduct long-term assessments out to 2100."
- Footnote 5 (l.341): Scope 1/2/3 (GHG-protocol style; scope 3 upstream and downstream).
- Few figures. Coverage: full.

## D04 = Doc 2 - Climate Change Risks to Australian Banks (Bellrose, Norman, Royters; RBA Bulletin Sept 2021)

- VaR = technical insurance premium / replacement cost; "a VaR of 0.5 per cent is equivalent to an annual premium of
  $2,500 on a building that would cost $500,000 to replace" (l.33). High risk = VaR > 1% (FEMA) (l.33-34).
- 3 1/2% of dwellings currently VaR > 1%, 8% "over the next 80 years" (l.35). Change in VaR measured "from 2021" (l.36).
- User cost: 0.4 ppt VaR change ~ 10% price fall (l.36); fn 4 starting rental yield 4% (l.326-328).
- By 2050 ~1 1/2% of properties >=10% fall; 9% by 2100, "of which 3 per cent" up to 20% (VaR change >= 1 ppt) (l.37-43).
- 254 suburbs (2050) / 1,438 (2100) with VaR increase > 0.4 ppt (l.45). Suburb aggregation for VaR (l.27).
- HRP check at postcode level: ~0.5% (74,000) properties move into high risk by 2050 (l.106).
- 40,000 more loans (2 1/4% of all loans) LVR > 80%; about half > 90% (l.117). Postcode matching (l.116).
- Five hazards (l.26): riverine flooding, coastal inundation, forest wildfires, wind storms (other than cyclones),
  ground subsidence in drought. RCP 8.5 "Hot House World"; fn 2: about 4.3 deg C by 2100 (l.323). TIP in 2020 dollars (fn 3).
- Business lending: 114 sub-industries (l.140); scope 1/2/3 defined its own way (l.141-149, scope 2 = direct
  suppliers' emissions added; scope 3 upstream only); ~20% of business loans to top-quartile scope-1 industries
  (l.163); Graph 6 top-20 list (l.165-184); fn 9 coal not on the list (l.347); fn 10 FY2020 major banks' coal
  mining ~$2.3bn, oil & gas ~$25bn (l.348). Mortgages ~2/3 of major banks' portfolios (l.22). Cites CPG 229 as
  the April 2021 draft (l.306, l.352). Data from "four major banks" (l.321); CVA with "five largest banks" (l.8).
- Coverage: full.

## D01 = Doc 3 - Assessing Physical Climate Risk in Repo-eligible RMBS (McCarthy, Reid; RBA 2024)

- Builds on D04's method (l.87-94). Seven hazards (fn 5, l.642): coastal inundation, cyclone wind, extreme wind,
  forest fire, riverine flooding, soil subsidence, surface (flash) flooding.
- 2020 Australia-wide average VaR 0.22% = $1,075 on a $500,000 rebuild (l.95; $1,075/500,000 = 0.215%); fn 6
  2,639 postcodes, property-weighted. ~4% of dwellings HRP in 2020 (l.95).
- 2.5 million securitised mortgages, ~2/3 of public RMBS market, ~1/3 of mortgages by value (l.101).
- 283 repo-eligible deals at 31 Dec 2023 (l.103); average VaR index 0.2% (l.109); highest ~3x average, "over
  $3,000" (l.113); small-bank HRP 4%; most at-risk HRP > 15% (l.165).
- 2050: +25% VaR, ~0.05 ppt (l.213-214); HRP +1.25 ppt average, 1.5-2 ppt for a few; seven highest unchanged
  (l.262); price falls 1.25% average, 2% largest (l.308); high-LVR share +2.75 ppt average, +15 ppt one RMBS (l.309).
- Table 1 (l.361-388): All RMBS VaR 0.20%, HRP 3.55%, repo collateral $129b, face value $613b, non-metro 27.2%,
  LMI 30.0%; 'High-risk' RMBS 0.40%, 10.25%, $0.25b, $2b, 72.9%, 11.8%. Small-bank deals ~20% by number (l.357).
- Table 2 (l.402-458), flattened: VaR/HRP 0.209/4.00 (small banks per text), 0.196/3.46, 0.193/3.39; three
  columns of other metrics ending in deal counts 106, 94, 64 (column mapping inferred: non-banks, large, small).
- Issuer definitions fn 10 (l.654): large banks = ADIs under LCR; small = ADIs under MLH; non-banks not
  deposit-taking. Regression 232 obs (l.595); 2018 first green RMBS (l.542, l.601).
- Coverage: full.

## D03 = Doc 4 - Australia's Sovereign 'Green' Labelled Debt (Alexander, Jayawardhana; RBA Bulletin Jan 2025)

- June 2024 inaugural 10-year Green Treasury Bond $7bn, about half a typical syndication (l.152); 105 investors,
  17 new (l.227); greenium ~2 bps = $11 million saving (l.246); < 1 bp by Aug 2024, higher yield than conventional
  by Oct 2024 when $300m more issued; Dec 2024 another $300m (l.340). Closest comparator May 2034 bond (fn 3).
- Semis labelled since 2016, Victoria first (l.41); labelled semis at a premium 2017-2021 (l.345).
- Graph 3 coverage ratios 4.36, 3.03, 2.51, 3.27 (labels scrambled). Graph 4 peers (scrambled: Germany, Canada,
  Denmark, Switzerland, Australia). Coverage: full.

## D08 = Doc 5 - The Changing Global Market for Australian Coal (Cunningham, Van Uffelen, Chambers; RBA 2019)

- 510 Mt produced 2017/18, ~75% (380 Mt) exported, 55% in 1990/91 (l.13); coal ~1/4 of resource exports and 14%
  of total exports since 2015 (l.14-16); 2018 exports $67bn = 3 1/2% of nominal GDP (l.16); domestic use ~122 Mt (l.26).
- Thermal ~3/4 of global consumption; met 13% (l.127-128); 2018 global generation 26,600 TWh, coal ~10,000 TWh
  (l.130); coal share 41% (2007) to 38% (2018) (l.191-192); China ~3,200 Mt thermal (l.190).
- Australia and Indonesia ~30% each of export volumes 2018 (l.428); Australia ~half of met seaborne, ~20% thermal
  (l.429); Japan ~40% of thermal exports 2018 (l.548-549); China <2% (2008) to ~1/4 thermal; India, China, Japan
  ~2/3 of met (l.550-607); China ~1/4 of met (l.1023); fn 4 44% / 24% of Chinese imports from Australia (l.1048).
- Debbie April 2017: met exports -50% (l.679); -1/2 ppt GDP growth year to June qtr 2017 (l.977).
- Newcastle 6,000 vs 5,500 kcal/kg premium > US$50/t mid 2018 vs ~US$17/t long run (l.788). Fn 3 met coal
  includes coking and PCI coal (l.1047). IEA NPS 37% (2017), ~30% (2030), 26% (2040) (l.1066); SDS ~40% to ~5% (l.895-896).
- Coverage: full.

## D05 = Doc 6 - Exploring the Supply and Demand Drivers of Commodity Prices (Cunningham, Smith; RBA 2019)

- Commodities two-thirds of exports (l.15); 43 commodities (l.45); Table A1 series counts (l.154-207): 43; Energy 6
  (oil 3, gas 3); Food & beverages 22 (food 18, beverages 4); Industrial inputs 12 (agriculture 5, base metals 5);
  Bulks 3.
- Oil > US$110 to US$28 (Jan 2016), more than tripled by mid 2018; inventories +~20% (l.78-85); ~half global,
  ~half block (l.87).
- 2009-2011: global factor ~1/3 iron ore, 1/4 coking coal, ~1/2 thermal; block ~half coal, ~1/4 iron ore;
  commodity-specific ~40% iron ore (l.98-102).
- Bowen Basin ~1/3 of Australia's coal exports; coking coal exports -50% April 2017 (l.108); beef +35% since
  Oct 2018 lows (l.129). Coverage: full.

## D06 = Doc 7 - PRRT: Review of Gas Transfer Pricing Arrangements (Treasury, final report May 2023)

- Timeline (l.71-92, 142-147): 2 Nov 2018 response; 5 Apr 2019 tasking; Jan 2019 roundtable; Apr 2019 paper (21
  submissions incl. 4 confidential); paused Apr 2020; resumed Dec 2022. Regulation sunsets 1 Apr 2026 (l.140,
  312); remade 2015 before 1 Apr 2016 sunset (l.311); introduced 2005; PRRT 1987.
- Recommendations 1a/1b/1c (l.104-112): netback only (LTBR+7, plus LTBR+7 on opex); 80:20 split; deductions cap
  90% of assessable receipts, 7 years after first production, exclusions (closing-down, starting base, resource tax).
  Cap = PRRT of 4% of receipts (10% x 40%) (l.856). Cap start "1 July 2023 or 7 years after the year of first
  production, whichever is later" (l.1051). Change start ideally 1 July 2024 (l.1042). Combined marginal rate 58% (l.765).
- 2020-21: 33 PRRT projects, 10 entities paid for 6 projects (l.156). Net PRRT gap 2019-20 $13m (1.3%) (fn 71).
- LNG: 2021-22 83.2 Mt, 21% of trade, $70bn, second largest commodity export after iron ore; >$90bn forecast
  2022-23, ~81 Mt (l.336); 10 facilities ~88 mtpa; $230bn boom 2007-2012, eight FIDs (l.329-330); ~3/4 oil-linked
  (l.345). Project dates (l.348-349); five PRRT LNG projects: Pluto, Gorgon, Wheatstone, Ichthys, Prelude (l.366);
  WA DMO 15% (fn 16, l.373); Gorgon US$37bn (2009) -> US$54bn (2013) -> US$60bn (2017 WoodMac) (l.350).
- Employment 12,000 (2007-08) -> 28,000 (2014-15) -> 22,000 (2021-22) (l.407-408). LNG netback $7.91/GJ (2016-20)
  -> $29.08/GJ (2021-22) (l.411). Callaghan baseline US$65 WTI (l.411) but "US$65 per barrel Brent" (l.1401).
- Modelling (l.1385-1514): central US$72.70 WTI, high US$92, low US$62 (CPI-indexed beyond 2026-27). Baseline central
  ~$5bn to 2033-34, ~$53bn to 2049-50; low <$1bn / ~$20bn; high ~$18bn / ~$99bn. Netback +3.9 / +16.3 (central),
  +21.9 / +48 (high), ~+0.2 / +3.3 (low); modified RPM +2.4 / +10.2, +13.3 / +26.4, ~+0.3 / +6.2; cap +7.0 / +3.7,
  +5.6 / +3.8, +8.1 / +3.0 ($bn; to 2033-34 / to 2049-50). Exec summary rounds: ~$4bn/$16bn, >$2bn/$10bn, ~$7bn/~$3 1/2bn.
  Callaghan: $12bn 10 yrs to 2027, $106bn to 2050; netback +$89bn 2023-2050, +$68bn 2027-2039 (l.1401, 1485).
  LTBR+5 = 6-10% since 2011; LTBR+7 = 8-12% (l.1477); minimum returns 7-8% upstream, 9-10% downstream (l.1497).
- Coverage: full.

## D02 = Doc 8 - Asset value of water and other renewables for electricity generation: 2007-15 (Stats NZ, Apr 2017)

- March years; NZ$. 2015: renewables asset $13.8bn, water $9.8bn; rent renewables $829m, hydro $586m (l.114-122);
  hydro 56% (23,728 of 42,362 GWh); renewables 79% of generation; geothermal 17% (7,091 GWh) (l.124-132).
- Rent share renewables 68% (2007) -> 79% (2015); geothermal rent $76m -> $175m (11%/yr); wind $14m -> $53m (6.4%);
  average net generation 42,487 GWh (l.136-155). Total rent "$1 billion in 2015" (l.365).
- Asset value = rent / 6% discount rate, infinite life (l.868); real return 4% (l.858, 874); previous report 8%
  return and 4% discount rate (l.960, 966). Geothermal asset $1.3bn -> $2.9bn; wind $238m -> $884m; fuelwood,
  biogas, solar rents $8.6m, $5.7m, $0.5m and assets $143m, $95.3m, $8.5m (l.393-449). 1 GWh = 0.0036 PJ (l.1055).
- Table 1 (l.211-351) flattened by column; Table 2 (l.475-751) regional water and generation, flattened.
- Population 4,219,400 (Mar 2007) -> 4,580,000 (+9%); net generation +0.6% or 270 GWh (l.462). Coverage: full.

## Shared ground (navigation only)

- D04 -> D01: D01 reuses D04's VaR, HRP threshold, 0.4 ppt ~ 10% mapping and 4% yield (D01 l.87-94, 308, fn 11);
  hazards 5 (D04) vs 7 (D01); current HRP share 3 1/2% "currently" (D04) vs 4% "in 2020" (D01); base year 2021 vs 2020;
  suburb vs postcode aggregation; banks only vs banks and non-banks; loans counted (D04 2 1/4% of loans) vs by
  value (D01 high-LVR share of pool value).
- D07 definitions -> D04/D01 practice: scope definitions differ (D07 fn 5 vs D04 l.141-149); liability risk only in
  D07; D04 cites the April 2021 draft of D07.
- D08 <-> D05: same lead author; Debbie April 2017 (-50% met/coking); seaborne met/coking "over/more than half";
  D08 fn 3 met = coking + PCI; Bowen Basin 1/3 of coal exports only in D05.
- D06 <-> D05: oil (D05 Brent episode 2016-18; D06 WTI scenarios, Brent premium fn 81). D06 <-> D02: "resource
  rent" concept (D02 Table 3 derivation; D06 rent tax). D03 <-> D01: green issuance (semis 2016, green RMBS 2018,
  Green Treasury Bond June 2024).
- No document amends, answers or completes another's figures; no forecast/actual pair across documents.
