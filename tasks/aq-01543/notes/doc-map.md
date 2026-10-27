# aq-01543 - document map

Written by four parallel `bundle-mapper` runs (D01-D05, D06-D10, D11-D15, D16-D20) from `text/`
and compared with `docs/`; merged by the caller 2026-10-07. Navigation only, like the form's bundle
overview: where things are, not what to ask. Questions quote the documents, never this map.
Arithmetic marked as the mapper's own is a check, not document text.

## Bundle

- What it is: twenty U.S. International Trade Administration Country Commercial Guide energy (and
  environmental technology) chapters, one per country, last published 2023-11-03 to 2026-06-26.
- Documents: 20; ids from `text/manifest.json` (alphabetical by file name). Page Doc N:
  D01 Angola=7, D02 Bulgaria=1, D03 Chile=6, D04 China=10, D05 Finland=18, D06 Germany=9,
  D07 Indonesia=19, D08 Israel=5, D09 Mauritius=8, D10 Mexico=13, D11 Poland=2, D12 Portugal=16,
  D13 Romania=20, D14 South Africa=12, D15 South Korea=4, D16 Spain=17, D17 UAE=11, D18 UK=14,
  D19 Uruguay=15, D20 Vietnam=3.
- Gaps: none in the capture (all 20 match_capture, no clipped ranges). All sources are text captures;
  charts referenced in the text (D02 L44 production chart, D15 L324 LNG chart) are absent from the
  source itself. D05 L11 is cut at "updated in Septe" in the source; D03 L81 starts mid-name.
- Extraction spot-checks: text line = original line + 2 (header); only trailing spaces in flattened
  table cells and one blank line differ. Tables checked per part (see each section).
- Provenance: notes/intake.json (capture AQ-01543_2026-10-07_0302.txt, sha256 41394e0a...).


<!-- merged from doc-map-a.md -->

# aq-01543 - document map, part A (D01-D05)

Part A of a split map: D01 Angola, D02 Bulgaria, D03 Chile, D04 China, D05 Finland. The caller
merges the parts into notes/doc-map.md. Navigation only: where things are, not what to ask.
Questions quote the documents, never this map.

Conventions used below:

- Line numbers are those of `text/Dnn.txt`. Each text file starts with a 2-line header
  ("# Dnn | docs/..." plus a blank line). The `docs/` originals are plain .txt files whose line
  numbers differ (about text line minus 2 near the top, drifting further because extraction
  collapses runs of blank lines and strips trailing spaces). Content was compared and is identical.
- Tables are flattened: " | " separates cells; many rows wrap with one cell per line, and pipes
  are sometimes missing. Values below are copied verbatim (decimal commas and odd spacing kept).
- Pages: not applicable (manifest `pages: null`, method text). There is no visual original to
  inspect beyond the .txt; any layout ambiguity present in the .txt is recorded as unresolved.
- Platform Doc numbers (notes/intake.json): D01 Angola = Doc 7; D02 Bulgaria = Doc 1;
  D03 Chile = Doc 6; D04 China = Doc 10; D05 Finland = Doc 18.

## D01 - Angola: Energy (Angola Country Commercial Guide)

- Source: text/D01.txt lines 1-136; manifest docs/ccg_energy_cleantech_sectors_angola.txt, method
  text, pages null, 23,040 chars, sha256 98c914ef...4055. Platform Doc 7.
- Written or submitted by: U.S. International Trade Administration (line 3: "Angola Country
  Commercial Guide (U.S. International Trade Administration)"). Contact block lines 128-133: "Mauro
  Fonseca, Commercial Assistant / U.S. Commercial Service Angola / `Mauro.fonseca@trade.gov` / Tel:
  (+244) 222 641 253 / Mob: (+244) 929 667 036". Line 60 says "please contact CS Angola" (CS not
  expanded in the document).
- Type, date, edition: Country Commercial Guide chapter headed "## Energy" (line 5). "Last
  published: 2024-02-01" (line 6). `Source: https://www.trade.gov/country-commercial-guides/angola-energy`
  (line 7). No edition or version number.
- Headings in order: Overview (9); Table 1 title (20); Table 2 title (34); run-in "Power Africa:"
  paragraph (63); run-in "Support to Angola:" paragraph (64); Table 3 title (67); Leading Sub-Sectors
  (84) with Generation (85), Transmission (91), Distribution (95), Services (fused onto the end of
  line 98); Opportunities (101) with Generation (103), Transmission (110), Distribution (116);
  Resources (118); "For information contact:" (128); closing rule "-----" (135).
- Period covered: calendar years only; no fiscal convention stated. Table 3 columns 2018-2022;
  budget 2022 vs 2023 (102); dated events 2015-2023; targets "by 2025" (10, 15, 19, 65, 104, 106,
  107) and Power Africa goals "by 2030" (63). Table 1 tariffs carry no date or base period.
- Entities and aliases:
  - MINEA = Ministry of Energy and Water (11 "the Ministry of Energy and Water (MINEA)"; 13, 104;
    Resources 119 "Ministry of Energy and Water (MINEA) -").
  - Three public utilities under MINEA (18): PRODEL "(Empresa Pública de Produção de Electricidade),
    the national production company"; RNT "(Empresa Rede Nacional de Transporte de Electricidade),
    the national transmission company" (also 111); ENDE "(Empresa Nacional de Distribuição de
    Electricidade), the national distribution company" (also 33, 117).
  - GAMEK "(Gabinete de Aproveitamento do Médio Kwanza)", hydro utility on the Kwanza River whose
    purview "was expanded to include oversight of the development and construction of most major
    power projects" (18); Resources 121 "Medio Kwanza Exploitation Office - (GAMEK)".
  - Regulator IRSEA "(Instituto Regulador dos Serviços de Electricidade e Águas)" (19); Resources
    120 lists "Regulatory Institute of Electricity Sector (IRSE)" - different abbreviation.
  - African Development Bank: "(AfDB)" (65), "(AFDB)" (115), spelled out (117, 124).
  - Power Africa (17, 63-66, 123); its Southern African Energy Program "(SAEP)" (64).
  - Southern African Power Pool (17, 112); Central Africa Power Pool (112).
  - "GRA" (66) not expanded; "Government of Angola" (65). "PTSE" = "Electricity Sector
    Transformation Program" (122 only).
  - U.S.-named companies: GE, Cummins, Caterpillar, Westinghouse Turbines "among others" (61); GE
    "supplied the turbines" for Soyo I (105); "U.S. companies Itron and Landis & Gyre" (117); an
    unnamed "U.S. company" developing a 380 MW solar project (106).
  - Other firms: Odebrecht ("The Brazilian firm", 41, 104); China Machinery Engineering Corporation
    (CMEC) (46, 105); Sun Africa (51, 56); China Gezhouba Group Corporation (CGGC) / Niara Holding
    (60); ENI ("The Italian company", 106); Solenova ("a joint venture between ENI and Angolan
    state-owned oil producer Sonangol", 106); "German Conjucta GmbH and Gauff GmbH & Co company"
    (106); consortium "Total Eren and Angola Environment Technology, Limited" (106); Biocom (107);
    ZTE (China) and Energitec (India) (117); EXIM Bank (57); World Bank (117).
  - U.S. bodies: U.S. Trade and Development Agency (111); U.S. Department of State (111); U.S.
    Congress / Electrify Africa Act (63); United States International Trade Commission (83, 125);
    Global Trade Atlas (83, 126).
  - Spelling variants inside the document: Kwanza Norte / Cuanza Norte, Kwanza Sul / Cuanza Sul,
    Malange / Malanje, Uige / Uíge, Bie / Bié, Huila / Huíla, Laúca / Lauca (11, 14-16, 37, 104, 106,
    115, 117).
  - Plan names (the document never states whether these are one plan): "2025 Government Energy Plan"
    (60), "2025 Angola Energy Strategy" (104), "Angola 2025 Plan" (106), "the 2025 plan" (107);
    "National Development Plan 2018-2022" (106).
- Tables:
  - Table 1, lines 20-30. Fused title: "Price per kilowatt for various types of clientsTable 1:Price
    per kilowatt for various types of clients". Columns: [client class] | Price (KWh) | % increased.
    Units Kz/KWh with decimal commas ("Kz" not expanded). No date, no base for "% increased", no
    source line. Rows verbatim:
    - 22 "Low Voltage | Price (KWh) | % increased" (group header)
    - 23 "Industry | 12,82 Kz/KWh | 81%"
    - 24 "Domestic Clients | 6,41 Kz/KWh | 113%"
    - 25 "Domestic Clients (Low Income) | 2,46 Kz/KWh | No change"
    - 26 "Medium Voltage (< 30KV) | Price (KWh) | % increased" (group header)
    - 27 "Industry | 9,61 Kz/KWh | 87.2%"
    - 28 "Commerce and Services | 11,54 Kz/KWh | 96.2%"
    - 29 "High Voltage (> 30Kv) | Price (KWh) | % increased" (group header)
    - 30 "Large Industry | 7,31 Kz/KWh | 55.5%"
    - Two rows are labelled "Industry" (low voltage 23, medium voltage 27).
  - Table 2, lines 34-60. Fused title: "Current and future major power projects:Table 2: Current and
    future major power projects:". Header (36): "Project | Estimated Installed Capacity | Estimated
    Completion Date and Contractor". Five project rows, cells wrapped one per line:
    1. 37-41 "Laúca Hydroelectric Dam and transmission lines (supplies Luanda, Huambo, Huíla, Malange,
       and Kwanza Norte)" | "2070 MW" | "2022 – currently operating at 95 percent the last generator
       is still under construction (completion December 2022)." / "Contractor: Odebrecht".
    2. 43-46 "Soyo Combined Cycle (Phase 1) and high voltage power lines" | "750 MW" | "2020" /
       "Contractor: China Machinery Engineering Corporation (CMEC)".
    3. 48-52 "Solar Power Plants" | "370 MW" | "2022" / "Contractor: Sun Africa" / "Contractor already
       delivered two sites in July2022."
    4. 54-57 "Solar Power Plants" | "TBD" | "Contractor: Sun Africa" / "EXIM Bank approved US$900
       million". Only one value (TBD) covers the capacity and completion columns; whether TBD is the
       capacity or the date is unresolved (the original .txt has the same layout).
    5. 58-60 "Caculo Cabaça Hydroelectric" | "2171 MW" | "TBD – 12.5 percent of total execution" /
       "US$ 4.7 billion financed by a Chinese government loan and US$ 1.4 billion by Germany for
       electromechanical equipment. Contractor: China Gezhouba Group Corporation (CGGC) / Niara
       Holding". Line 60 runs straight on into prose: "For more information on projects in the 2025
       Government Energy Plan please contact CS Angola."
    - No units footnote or source line. Cambambe (700 MW, prose 104) and Capanda (15) are not rows.
  - Table 3, lines 67-83, "Table 3: Energy equipment and technologies". Header (69): " | Energy
    equipment and technologies | 2018 | 2019 2020 | 2021 | 2022" - 2019 and 2020 share one cell
    (missing pipe; same in original). Five values per data row. "Units: US$ millions" (82). Rows
    verbatim (2018 | 2019 | 2020 | 2021 | 2022):
    - 70 "Total Local Production | N/A | N/A | N/A | N/A | N/A"
    - 71 "Total Exports | N/A | N/A | N/A | N/A | N/A"
    - 73-74 "Total Imports (based on HS codes , 8411, 8503 and 8537)" / "230 | 196 | 115 | 192 | 258"
    - 76-78 "Imports from the US (based on HS codes 8411, , 8503 and 8537)" / "40 | 40.1 | 29.1 | 24.4 | 19.3"
    - 79 "Total Market Size | 230 | 196 | 115 | 192 | 258"
    - 80 "Exchange Rates | 245 | 365 | 520 | 625 | 460" (currency pair/unit not stated)
    - 82 "(total market size = (total local production + imports) – exports) Units: US$ millions";
      83 "Source: United States International Trade Commission and Global Trade Atlas."
    - Total Market Size equals Total Imports in every year. No (estimated)/(forecast) labels.
    - Related prose 62: "Electric power-related equipment (HTS 8411) exported to Angola in 2022, was
      valued at US$ 14.8 million." (HTS 8411 only; exporting country not stated) - differs in scope
      from Table 3's 2022 "Imports from the US" 19.3 (HS 8411, 8503, 8537).
- Lists:
  - Provinces on the interconnected northern-central backbone (16), "10 of the 18 provinces":
    Luanda, Bengo, Uíge, Cuanza Norte, Cuanza Sul, Benguela, Huambo, Bié, Malanje, Zaire (10; last Zaire).
  - Northern grid provinces (14): Luanda, Uige, Bengo, Zaire, Malange, Kwanza Norte, Kwanza Sul (7).
    Central network: "220kV lines from Benguela to Huambo and Bie" (14). Southern grid "serves Huila
    and Namibe" (15).
  - "four main power production plants - Lauca, Capanda, Cambambe and Soyo combined cycle" (15).
  - SAEP "five key constraints on investment" numbered 1-5 (64); last "5. weak institutional and
    human resource capacity for energy sector management".
  - Leading Sub-Sectors (84-100), 13 items: Generation 5 (86-90: small-scale hydro equipment; diesel
    and gas turbine generators; "Renewable energy solutions: solar; biomass; wind; small hydro";
    utility scale central dispatch center; minigrids complete solutions); Transmission 3 (92-94);
    Distribution 3 (96-98, last ends "...(SCADA)"); Services 2 (99 EPC services; 100 "Maintenance,
    repair and operation services" = last item).
  - "the government approved three solar projects" (106) - the three are not enumerated. Named
    nearby: 380 MW (U.S. company), ENI 50 MW Namibe (concession agreement), Total Eren consortium
    30-100 MW PV Lubango (MOU for a feasibility study).
  - AfDB line-of-credit components (115): 343 km transmission line; new "400/220/60 kV- 2 x 450 MVA
    substation in Lubango, Huila Province"; upgrades to an existing substation in Huambo; SCADA
    control system.
  - ENDE 2022 public tenders (117): two, both AfDB-financed: "deliver 1.2 million pre-paid meters";
    "consultancy and supervision for the 1.2 million smart meters".
  - World Bank densification provinces (117): Luanda, Benguela, Huila, Huambo (4).
  - Resources (119-126): 8 entries; last "Global Trade Atlas".
- Quantitative prose figures (line: figure - what it measures):
  - 10: targeted 8.9 GW installed generation capacity and 60 percent electrification rate by 2025.
  - 11: current installed capacity estimated 5.7 GW, "only 70 percent is in use"; "current energy
    mix" 61.8 percent hydropower, 37.6 percent other fossil fuels, 0.6 percent hybrid (solar/fossil
    fuel) - sums to 100.0; base (capacity or generation) not stated; MINEA expects 6.3 GW generation
    capacity once Soyo (750 MW) and Laúca (2.1 GW) are fully online.
  - 12: electrification "43 percent in most cities and less than 10 percent in rural areas".
  - 13: MINEA mapping potential 16.3 GW solar, 3.9 GW wind, 18 GW hydropower.
  - 15: grid expansion "from 3,354 km to 16,350 km by 2025".
  - 17: Baynes Dam 600 MW installed capacity, "300 MW for each country".
  - 19: June 2019 subsidies cut by 85 percent leading to retail rate hikes of 77 percent.
  - 62: HTS 8411 equipment exported to Angola in 2022: US$ 14.8 million.
  - 63: Power Africa goals "to add 30,000 MW of generation capacity, and to expand electricity access
    to 60 million people in sub-Saharan Africa by 2030"; "more than 150" partners.
  - 65: US$ 530 million AfDB program (2020); 343-kilometer line; 1.2 million prepaid meters; access
    "from its current estimated 42 percent in most cities and less than 10 percent in rural areas to
    50 percent by 2025".
  - 102: budget for electricity production, transmission and distribution "increased to US$ 817.2
    million in 2023 from US$490 million in 2022"; "national budget for electricity assessment
    allocated is around US$ 249.4 million" (no year).
  - 104: Cambambe expansion 700 MW and Lauca 2070 MW; generation began 2017 (Cambambe) and 2018
    (Lauca); "100 locations suitable to produce 600 MW from mini hydro"; Matala mini hydro expansion
    "from 27 MW to 40.8 MW".
  - 105: Soyo I 750 MW "currently generating 500MW"; second Soyo plant 500 MW planned.
  - 106: 380 MW solar ("over the next four years"); ENI 50 MW solar (Namibe); 30 - 100 MW PV (Lubango).
  - 107: biomass goal 500 MW; Biocom 100 MW toward 2025 target; renewables excluding large hydro
    "about 8 percent of total installed capacity by 2025"; "at least 42 biomass projects that can
    reach 3.4 GW".
  - 115: US$ 530 million line of credit; tender open until November 21st, 2023.
  - 117: losses "as high as 35 percent"; "approximately 80 percent of electricity customers are
    un-metered"; 2015 pilot 1,500 smart meters; planned program 1.5 million units; World Bank target
    196,500 new connections; "The budgeted amount of US$250 million."
- Forecasts, guidance, deadlines, effective dates:
  - 2025 targets: 8.9 GW and 60 percent electrification (10); grid 16,350 km (15); progress toward
    cost-reflective tariffs (19); AfDB program access 50 percent (65); mini hydro 600 MW at 100
    locations in the "2025 Angola Energy Strategy" (104); renewables 200 -> 700 MW -> 1 GW under
    consideration (106); biomass 500 MW (107); renewables ex-large hydro about 8 percent (107).
  - Target revision (106), verbatim: "Although the government committed to the production of 200 MW
    of renewable energies in the Angola 2025 Plan, the National Development Plan 2018-2022, raised
    the renewable production goal to 700 MW, and there is consideration of updating the goal to 1 GW."
  - Power Africa (63): "established two goals that have been subsequently updated: to add 30,000 MW
    ... and to expand electricity access to 60 million people ... by 2030" - the document does not
    say whether these figures are the original or the updated goals.
  - Tenders "through 2024" (66); AfDB tender "open until November 21st, 2023" (115).
- Dated events: December 2015 General Electricity Law approved (32); "A 2015 feasibility study
  financed by the U.S. Trade and Development Agency" (111) and ENDE 1,500-meter pilot (117); 2016 Electrify Africa Act (63); 2017/2018 generation
  began at Cambambe/Lauca (104); May 2018 Natural Gas Commercialization Law passed (105); June 2019
  subsidy cut (19); 2020 Power Africa began assisting AfDB program (65); late June 2020 GRA released
  first tender (66); Soyo Phase 1 completion "2020" (45); July 2022 Sun Africa delivered two sites
  (52); December 2022 Laúca last generator completion (40); 2022 Sonangol green-hydrogen partnership
  announced (106); 2022 ENDE two tenders (117); November 21st, 2023 tender close (115).
- Hedged claims (hedge -> what it attaches to):
  - 11 "MINEA expects to reach 6.3 GW" (capacity once Soyo/Laúca fully online); "expected to come
    online over the next two to five years" (several hydro and solar projects).
  - 12 "are expected to create demand for alternative energy solutions" (higher prices after
    subsidy reductions).
  - 17 "would be shared" (Baynes output); "is also being considered" (DRC connection via Inga).
  - 19 "should improve government utility financial viability" (rate increases); "is expected to
    make progress toward achieving cost-reflective tariffs" (government, by 2025).
  - 66 "could present new opportunities for U.S. companies" (the tenders).
  - 105 "hopes that the Natural Gas Commercialization Law ... will attract private investment";
    "should encourage a shift towards energy production equipment for natural gas".
  - 106 "expected to become one of the largest in the region" (one approved solar project);
    "expected to be completed over the next four years" (380 MW project); "there is consideration
    of updating the goal to 1 GW".
  - 107 "are expected to represent about 8 percent" (renewables ex-large hydro); "would contribute
    100 MW" (Biocom).
  - 109 "this trend is likely to continue" (power equipment among top U.S. export categories - the
    ranking itself is stated firmly); "may also be an opportunity" attaches to procurement of
    maintenance equipment and services and is conditioned on "Assuming government prioritization of
    appropriate budget and financing resources for maintenance". Same paragraph states firmly "there
    is a high demand for related equipment and services".
  - 111 "will likely consist of 400kV transmission lines" (the backbone) vs 113 unhedged "the
    interconnection will be in 400Kv".
- Rounded prose beside exact figures: Laúca "2.1 GW" (11) vs "2070 MW" (39, 104); Soyo 750 MW
  consistent (11, 44, 105); electrification 43 percent (12) vs 42 percent (65) for "most cities";
  Table 2 solar 370 MW (Sun Africa) vs prose "380 MW solar project developed by a U.S. company" (106) -
  the document does not link them.
- Operative definitions, rules and scope exceptions:
  - "mini hydro (<10 MW)" (104); the next sentence calls Matala a "mini hydro plant" expanding from
    27 MW to 40.8 MW.
  - Market size formula (82); HS-code scope 8411, 8503, 8537 (73, 76) vs HTS 8411 only (62).
  - "Renewables, excluding large hydro" (107) - share scope.
  - Voltage classes "Medium Voltage (< 30KV)", "High Voltage (> 30Kv)" (26, 29); low-income domestic
    tariff "No change" (25).
  - "Power Purchase Agreements (PPAs or “off-take agreements”)" (108).
  - IPPs "essentially non-existent in Angola" (32); "Angola has no major import or export capability
    for electricity" (112); Angola "is currently a non-operating member of the Southern African Power
    Pool" (17).
- Amendments or contradictions (neutral; the document states no precedence for any):
  - Renewable goal raised 200 MW -> 700 MW, 1 GW considered (106); biomass goal 500 MW in "the 2025
    plan" (107) and 600 MW mini hydro in the "2025 Angola Energy Strategy" (104) sit beside the 200 MW
    renewable commitment of the "Angola 2025 Plan" (106).
  - Grid count: "three separate major grid systems (northern, central, and southern), in addition to
    isolated grids in the east" (14), "three regional power grids" (65) vs "the four major energy
    systems, namely the north, south, east and center" (113).
  - Electrification 43 vs 42 percent "in most cities" (12 vs 65); 2025 targets 60 percent
    electrification rate (10) vs 50 percent access goal of the AfDB program (65).
  - Capacity: 5.7 GW current and 6.3 GW expected once Soyo (750 MW) and Laúca (2.1 GW) are fully
    online (11) - the document does not state what 5.7 GW includes. Soyo completion "2020" (45) vs
    "currently generating 500MW" of 750 MW (105).
  - Laúca: Table 2 "currently operating at 95 percent ... (completion December 2022)" (40) vs prose
    "largely completed", generation began 2018 (104).
  - Regulator abbreviation IRSEA (19) vs IRSE (120).
  - Prose retail rate hikes 77 percent (19) vs Table 1 increases 81%, 113%, No change, 87.2%, 96.2%,
    55.5% (no table value is 77%).
  - Meters: tender 1 "1.2 million pre-paid meters", tender 2 "the 1.2 million smart meters" (117);
    AfDB program "1.2 million prepaid meters" (65); planned smart meter program "1.5 million units" (117).
  - AfDB US$ 530 million called "power sector finance program" (65) and "line of credit for energy
    infrastructure" (115).
- Coverage: full. Ledger: text lines 1-136 read (one chunk; all readable text). Spot-checks against
  docs original: Table 2 and Table 3 (original lines 30-84) identical in content (text collapses
  double blank lines, strips trailing spaces); "2019 2020" merged header cell and second-solar-row
  layout present in the original. Page count: not applicable. Footnote spot-check: Table 3
  formula/units/source lines identical. Unread ranges: none.

## D02 - Bulgaria: Energy and Environmental Technologies (Bulgaria Country Commercial Guide)

- Source: text/D02.txt lines 1-214; manifest docs/ccg_energy_cleantech_sectors_bulgaria.txt, method
  text, pages null, 36,074 chars, sha256 cd0e3cf1...b396c0. Platform Doc 1.
- Written or submitted by: U.S. International Trade Administration (line 3: "Bulgaria Country
  Commercial Guide (U.S. International Trade Administration)"). Energy contact 147-151: "U.S.
  Commercial Service Sofia Contact Information / Name: Emily Taneva / Position: Commercial Specialist
  / Email: `emily.taneva@trade.gov` / Phone: +359-2-939-5770". Environmental Technologies contact
  206-211: "U.S. Commercial Service Sofia / Name: Stanislava Dimitrova / Position: Senior Commercial
  Specialist / Email: `stanislava.dimitrova@trade.gov` / Phone: +359-2-939-5740".
- Type, date, edition: two CCG chapters with different dates. "## Energy" (5), "Last published:
  2026-03-31" (6), `Source: https://www.trade.gov/country-commercial-guides/bulgaria-energy` (7).
  "## Environmental Technologies" (153), "Last published: 2026-04-01" (154),
  `Source: https://www.trade.gov/country-commercial-guides/bulgaria-environmental-technologies` (155).
- Headings in order: Energy chapter: untitled overview (9-41); "Bulgaria’s electricity production"
  (42); priorities list (45); "Sub-sector Best Prospects" (52); Natural Gas (53); Coal (69); Oil
  (72); Smart Grids (82); Nuclear Energy (93); Renewables (116); Energy Efficiency (132); "Web
  Resources" (run-in, 137-145); contact (147). Environmental Technologies chapter: Overview (157);
  "Environmental Opportunities for U.S. Companies" (160); "Sub-sector Prospects" (189); Air Pollution
  Control (190); Drinking Water and Wastewater Management (196); Waste Management (199); Web
  Resources (202); Contact Information (206); closing rule "-----" (213).
- Period covered: calendar years; no fiscal convention. Mostly 2020-2025 data; a 12-month window
  "From September 2024 to August 2025" (18); monthly 2024 production (43). Target years 2026 (16,
  55, 95), 2027 (87), 2030 (119), 2038 (16), 2050 (133, 194); programmes 2021-2027 (134, 187;
  "valid through 2029", 187).
- Entities and aliases:
  - BEH = Bulgarian Energy Holding (22, 71). NEK = National Electric Company (26, 28, 30, 122, 138).
  - KNPP = "Kozloduy Nuclear Power Plant (KNPP)" (24, 39); "Kozloduy NPP" (40, 103, 139); "Kozloduy
    Nuclear Power Plant (NPP)" (96); "Kozloduy" (97).
  - ESO: "ESO, the country’s transmission system operator" (14); "Electricity System Operator (ESO)."
    (32). "the TSO" (120) is not expanded there. "Transmission System Operators (TSOs)" (56) are the
    gas TSOs of seven Vertical Gas Corridor countries - same abbreviation, different bodies.
  - Bulgargaz (34, 57); Bulgartransgaz (36, 137).
  - Maritza East name variants: "Maritza East 2 Thermal Power Plant (TPP), part of the Maritza East
    Complex" (28); "Maritsa East 2 plant" (19); "Maritza East Mining Complex" (40); "Martiza East
    complex" (70). Plants (40): "Maritza East 1 (ME-1), a 686-MW U.S.-built plant, owned and operated by
    AES Corporation"; "Maritza East 2 (ME-2), a 1,610-MW state-owned plant"; "Maritza East (ME-3), a
    908-MW plant owned by the U.S. company Contour Global"; "Maritza East 3 TPP" (28, 41).
  - Contour Global (28, 40, 41) also misspelled "Countour Global" (41). AES Corporation (40, 121).
  - IAEA = International Atomic Energy Agency (13). RRP = "recovery and resilience plan (RRP)" (15;
    "Recovery and Resilience Plan" 14, 85); RRF = Recovery and Resilience Facility (15, 16). European
    Commission (16, 85, 87); Council of the European Union (85); Bulgarian Parliament (16).
  - Gas: Gazprom (54); Vertical Gas Corridor (55-56); "floating storage and regasification unit
    (FSRU) in Alexandroupolis" (55); IGB = Interconnector Greece-Bulgaria (55); IBS = "The Serbo-
    Bulgarian gas link, formally known as the Interconnector Bulgaria-Serbia (IBS)" (64); Bulgaria-
    Romania interconnector (65); Chiren underground gas storage (57).
  - Upstream: "Shell Exploration and Production, a subsidiary of Shell plc" (66), "Block 1-26 Khan
    Tervel field"; "OMV Petrom, a Romanian oil and gas company, and NewMed Energy Balkan, a subsidiary
    of Israel-based NewMed Energy" (68), Han Asparuh block, Noble Corporation, drillship Globetrotter
    I, Halliburton, SLB (68).
  - UND = University of North Dakota (71). Lukoil / "Lukoil Neftochim" (73-74, 81); INSA (77);
    Bulgarian Petroleum Refinery (79).
  - EBRD = European Bank for Reconstruction and Development (83); EDG West = Electrodistribution Grid
    West (83). ADD Bulgaria and ZTE (87); Electrohold, EVN, Energo-pro (90-92).
  - Nuclear: IGA = intergovernmental agreement (95); "Departments of State, Energy and Commerce and the
    U.S. Nuclear Regulatory Commission" (95); "Westinghouse Electric Company" (95), "Westinghouse
    Electric" (97), "WEC fuel assemblies" (97), "Westinghouse AP1000" (95); RWFA = Robust Westinghouse
    Fuel Assembly (97); BNRA = Bulgarian Nuclear Regulatory Agency (97); Atomstroyexport (96);
    U.S.-based NuScale Power, X-Energy, Fluor Corporation, Holtec International (98).
  - Plans/funds: "The National Energy and Climate Plan" (133; the document gives no abbreviation -
    "NECP" in this map is shorthand); Cohesion Policy (134); JTF = Just
    Transition Fund (134); National Energy Savings Plan (136); "Operational Program on the
    Environment 2021-2027" (187, 192) = "Environmental Operational Program 2021-2027" (205, link
    eufunds.bg); "European Green Deal" (133) / "EU Green Deal" (194).
  - Resources bodies: Ministry of Energy (140); Energy and Water Regulatory Commission (141); Energy
    Efficiency and Renewable Sources Fund (142); Bulgarian Wind Energy Association (143); Ministry of
    Environment and Water (203); Ministry of Regional Development and Public Works (204).
- Tables: none. The only "|" in text/D02.txt is the file header. Tab-separated list 88-92:
  "Deployed smart meters in Bulgaria (in percentage to the number of end-customers in the region)
  are as follows:" / "- Electrohold – 15%" / "- EVN – 66%" / "- Energo-pro – 10%".
  Chart: line 44 "View Bulgaria’s Electricity Production from Jan 2024 to Dec 2024 in the chart:" -
  the chart is absent in both text and original (original line 42 is followed directly by the
  priorities list). Only prose values survive (43).
- Lists:
  - State-owned entities (20-36), 8 bullets: BEH; KNPP "with two operating units"; NEK; Maritza East
    2 TPP (bullet also says "Contour Global owns 73% of Maritza East 3 TPP, with the NEK holding the
    remaining 27%."); "31 hydropower plants and pumped-storage hydropower plants owned by NEK, with
    total installed capacities of 2737 MW"; ESO; "Bulgargaz; and"; Bulgartransgaz (last, 36).
  - Energy sector priorities (45-50), 5 numbered; last "5. Renovation of the building stock".
  - Russian-gas transit neighbours (54): Hungary, Greece, North Macedonia, Serbia.
  - Vertical Gas Corridor TSO countries (56): Greece, Bulgaria, Romania, Hungary, Slovakia, Moldova,
    Ukraine (7; last Ukraine).
  - "Potential gas project opportunities" (59-63): 2 bullets (LNG technologies/liquefaction
    know-how; drilling equipment, seismic, offshore platforms, upstream equipment and services). A
    separate stand-alone bullet at 68 (OMV Petrom/NewMed) follows the Shell paragraph.
  - "There are three refineries in Bulgaria" (75-81): INSA's facility Belozem; Bulgarian Petroleum
    Refinery in Dolni Dabnik; Lukoil Neftochim Refinery in Burgas port (last, 81).
  - Smart meter deployment (88-92): 3 entries.
  - SMR MoU partners (98): 4 named, last Holtec International.
  - Nuclear "Project opportunities" (99-115): 8 bullets; last "Working with Bulgaria’s universities on
    training and educating nuclear engineers" (115).
  - Four large hydro cascades (123-131): "Belmeken - Sestrimo - Chaira Hydro Power Complex"; Batak
    Cascade; Dospat-Vacha Cascade; Arda Cascade (last).
  - Energy Web Resources (137-145): S&P Global URL, Bulgartransgaz, National Electric Company,
    Kozloduy NPP, Ministry of Energy, Energy and Water Regulatory Commission, Energy Efficiency and
    Renewable Sources Fund, Bulgarian Wind Energy Association, Global Data, Statista, then two bare
    URLs (gem.wiki Gas_Interconnector_Bulgaria-Romania; lowcarbonpower.org) on line 145.
  - "Environmental Opportunities for U.S. Companies" (160-186): 13 bullets; last "Water loss
    detection equipment" (186).
  - Operational Program on the Environment expected outcomes (187): 6; last "2.8 million people
    benefiting from flood protection and reduced risk of landslides".
  - Air-pollution municipalities (192): Burgas, Montana, Sofia, Smolian.
  - Environmental Web Resources (203-205): 3.
- Quantitative prose figures (line: figure - what it measures):
  - 10: electricity production "decreased by 4.98% year-on-year, to some 37,963 GWh in 2024";
    consumption "increased slightly by 0.97%".
  - 11: net electricity exports 2024 "dropped to 1.02TWh, a 69.9 % decline compared to the previous
    year"; baseload (coal, nuclear) "generated a total of 28,46TWh of electricity in 2024, which is
    10.7 % less than 2023"; "The share of electricity produced from RES, linked to the transmission
    network, increased by 32.21%, reaching 3,3264 GWh." (number format as printed; magnitude
    ambiguous).
  - 12: renewable capacity (mostly solar PV) +938 MW in 2024 vs "over 1.2 GW in photovoltaics in
    2023"; "At the start of 2025, projects for a total of 4.1 GW were lined up for grid connections";
    "Around 500 MW of battery energy storage systems (BESS), with a storage capacity of some 1,300
    MWh" installed by mid-2025; projection +7,000-7,500 MW battery storage in next 12-18 months,
    "capable of meeting 10%-15% of daily demand".
  - 13: nuclear "approximately 41.6% of Bulgaria’s total electricity generation" in 2024 (per IAEA).
  - 14: ESO "more than EUR 25 million in digitalization of the grid".
  - 15: RRP minimum 1.4 GW renewables with storage; EUR 342 million RRF + EUR 684 million private.
  - 16: "tripling power generation from renewables by 2026"; coal fleet online until 2038; risk of
    losing "almost EUR 1 billion".
  - 17: "uses only one-third of its large, pumped-storage hydro power plants (HPPs)".
  - 18 (September 2024 - August 2025): clean sources "more than two-thirds, or 67.27%"; nuclear "about
    40.38%"; solar 16.52%; wind 3.44%; hydropower 6.47%; fossil "about 32.73%"; coal 27.6%; natural
    gas 5.13%. Listed clean components sum to 66.81 (not 67.27); fossil components sum to 32.73;
    67.27 + 32.73 = 100.00. Bases vary in wording (consumption, supply, generation, energy mix).
  - 39: KNPP launched 1974; "six units were completed"; "3,000MW installed capacity"; Belene
    equipment: two reactor vessels, two pressure compensators, 24 hydraulic accumulators.
  - 40-41: ME-1 686 MW; ME-2 1,610 MW; ME-3 908 MW; Varna TPP 1,260 MW ("the largest among" other TPPs).
  - 43: "3,821 GWh in Dec 2024, compared with 3,008 GWh in the previous month"; "record low of 2,463
    GWh in June 2024".
  - 54-55: domestic gas market "more than 3 billion cubic meters (bcm) per year, a third of which is
    from Azerbaijan"; transits "five times as much Russian gas"; industry "almost two-thirds",
    residential heating "one-third"; "moves 16 bcma of Russian gas"; "20-percent owner" of the FSRU.
  - 57: Chiren "from 550 million cubic meters to 1 billion cubic meters"; above-ground stage "increase
    capacity by about 20%"; "650 million cubic meters of storage capacity" this autumn-winter.
  - 64: IBS "62-km", completed 2023. 66: exploration area "more than 4,000 sq. km". 68: two wells;
    "Total drilling budget is expected at approximately EUR170 million".
  - 70 (repeated at 135): coal share of electricity "from 35 percent in 2020 to 27 percent in 2025";
    70 only: Maritza East complex "generates around 40 percent of all coal-powered electricity".
  - 73: 70 percent of oil to transport, industry 9 percent; refinery "over 75% of fuel for the local
    market". 74: Lukoil granted "EUR11.6 million" (2024); Lukoil Neftochim loss "USD125.6 million
    (EUR107 million) for 2024".
  - 83: EBRD "$56.2 million (EUR50 million)". 84: "up to 194GWh of energy savings annually".
  - 85-86: "EUR 590 million" (end of 2024); "at least three gigawatt-hours" of storage; funds "should
    be available by December 31, 2025".
  - 87: "$230.14 million (EUR 196) million" for "four plans"; smart meter deadline 2027; "over 1.5
    million smart meters" installed by 2024.
  - 94: "two nuclear reactors, generating more than one-third of its electricity".
  - 95: "$100 million Westinghouse Electric Company fuel contract for its Unit 5 reactor".
  - 96: "EUR 600 million (USD 642 million)" to Atomstroyexport, December 2016.
  - 97: Unit 5 "1,000 MW Russian-built"; "another 42 Robust Westinghouse Fuel Assembly (RWFA) fuel
    assemblies" loaded May 2025.
  - 118: renewables "27 percent in 2025" of electricity generated; of that "53 percent comes from
    solar, 30 percent from hydropower, 15 percent from wind, and two percent from biomass" (sums 100).
  - 119: "its 3,200 MW renewable energy target for 2030, with over 3,000 MW of total installed
    capacity, predominantly from photovoltaic (PV) solar power"; PV "from just over 1 GW in 2020 to
    triple that amount in about three years".
  - 120: TSO-confirmed RES applications 40,000 MW (2023), "reduced to 35,000 MW" (2024).
  - 121: AES "operates 52 wind turbines". 122: NEK "31 hydropower plants, with a total capacity of
    2.74 GW"; Chaira pumped storage (864 MW): "only one of the four units ... was repaired since it
    shut down in 2022". 123: Belmeken "375 MW in generation mode and a pumping system of 104 MW";
    "14 facilities are under 10 MW".
  - 133: "3.5 times more energy resources per unit of its GDP than the EU average"; energy sector "70
    percent of total greenhouse gases". 134: "EUR 5.3 billion" 2021-2027; "3,800 homes and 180,000
    square meters of public buildings".
  - 187: "USD 1.77 billion in EU funds"; outcomes 1.5 million / 200,000 people / 285,000 tons / 1.3
    million / 4.4 million hectares / 2.8 million.
  - 197: "688 rivers, 43 lakes, 13 coastal waterways, and 177 groundwater bodies/aquifers".
  - 200: recycling "increased to 35 percent" vs EU average 46 percent; landfill rate 62 percent vs EU
    average 24 percent.
  - 201: full implementation of waste legislation "could create more than 14,000 jobs" and "USD 1.6
    billion" turnover; "Waste legislation and policies could create an additional 16,500 jobs" and
    "USD 2.1 billion".
- Forecasts, guidance, deadlines, effective dates:
  - RRP: minimum 1.4 GW renewables with storage (15); tripling renewables generation by 2026 and a
    coal phase-out framework (16). Vertical Gas Corridor "expected to conclude in 2026" (55). Storage
    scheme funds by December 31, 2025 (86). Smart meter "deadline for the full implementation" 2027
    (87). FID on AP1000 Units 7 & 8 "by early 2026" (95). Renewable target "3,200 MW ... for 2030"
    which Bulgaria "will soon exceed" (119). NECP: decarbonize "by 2050" and keep lignite reliance
    "to 2050 and beyond" (133). EU Green Deal carbon neutrality by 2050 (194).
- Dated events: 1974 KNPP launched (39); 1980s Belene approved (39); units 1-2 shut 2002, units 3-4
  shut 2006 (96) ("early 2000s" / "2007 agreement", 39); December 2016 Atomstroyexport compensation
  (96); 2020 derogation request for National Energy Savings Plan (136); 2022 Gazprom halted flows
  (54); 2022 Chaira shut down (122); end of 2022 Westinghouse fuel deal (97); 2022-early 2024 Russian
  crude under EU exception, derogation expired early 2024 (74); January 2023 Parliament vote (16);
  2023 IBS completed (64); 2024 U.S.-Bulgaria IGA (95); mid-2024 new fuel loaded (97); June 2024
  record-low month (43); end of 2024 EC approved EUR 590 million (85); March 2025 ME-3 set to stop,
  later reversed (41); May 2025 42 RWFA loaded (97); June 2025 OMV Petrom/NewMed rig contract (68);
  mid-2025 BESS (12); August 2025 Alexandroupolis renewed operations (55); September 2025 Chiren first
  stage completed (57) and UND-BEH MOU (71).
- Hedged claims (hedge -> what it attaches to):
  - 9 "nuclear is expected to retain its large share of generation capacities".
  - 12 "The projections are that ... Bulgaria will add 7,000-7,500 MW of battery storage".
  - 54 "imported gas from Turkiye is likely a Russian-Turkish blend" (the blend composition only;
    "Bulgaria no longer directly imports gas from Russia" is firm).
  - 55 "the project is expected to conclude in 2026" (Vertical Gas Corridor).
  - 57 "When completed, the expansion is expected to increase the storage capacity" (the 1 bcm
    end-state); the completed first stage and the 650 million m3 are stated firmly.
  - 68 "Total drilling budget is expected at approximately EUR170 million".
  - 71 "Initial analyses suggest" (lignite analogous to North Dakota coal).
  - 74 "has reportedly been importing crude from Kazakhstan, Iraq, and Tunisia" (post-2024 sources only).
  - 84 "are expected to contribute to climate change mitigation efforts and result in up to 194GWh".
  - 86 "The funds should be available by December 31, 2025."
  - 95 "aims to reach a final investment decision"; "will present many additional opportunities" (firm).
  - 119 "will soon exceed" (firm future, no hedge word).
  - 133 "That may not sound alarming" (rhetorical, attaches to the 3.5x figure).
  - 134 "is expected to benefit 3,800 homes"; "could help Bulgaria support sustainable energy solutions" (JTF).
  - 197 "it is estimated that most ... reach a good or high ecological status".
  - 198 "U.S. firms may participate with a Bulgarian partner or representative" (permission).
  - 201 "It is estimated that ... could create more than 14,000 jobs"; "could create an additional 16,500 jobs".
- Rounded prose beside exact figures: NEK hydro "2737 MW" (30) vs "2.74 GW" (122) (30 counts
  "hydropower plants and pumped-storage hydropower plants", 122 says "31 hydropower plants"); clean
  share "more than two-thirds, or 67.27%" (18); nuclear "more than one-third" (94) vs 41.6% (2024,
  13) vs 40.38% (Sep 2024-Aug 2025, 18); coal 27 percent 2025 (70, 135) vs 27.6% (18); Chiren
  "about 20%" (57) beside 550 -> 650 million m3.
- Operative definitions, rules and scope exceptions:
  - Smart meter shares are "in percentage to the number of end-customers in the region" (88).
  - "Baseload power plants (coal, nuclear)" (11); "RES, linked to the transmission network" (11).
  - The "clean energy sources" category includes nuclear (18).
  - Storage aid is "non-repayable aid and will be accessible to all storage technologies" (86).
  - Population thresholds: plants needed "for communities of fewer than 10,000 inhabitants" (159);
    "Urban wastewater treatment plants are planned for hundreds of cities and towns with less than
    10,000 residents"; "Wastewater treatment plants in towns with more than 10,000 inhabitants have
    already been constructed" (197). Exactly 10,000 is covered by neither wording.
  - "14 facilities are under 10 MW" (123).
  - EU Russian-crude prohibition: refinery used "an exception"; "This derogation expired in early
    2024" (74).
  - "only one licensed supplier in each geographical region" (38).
  - "the energy efficiency obligation scheme is implemented through a combination of individual
    energy savings targets for energy traders and alternative measures" (136).
- Amendments or contradictions (neutral; no document-stated precedence):
  - Coal: RRP "framework for a coal phase-out" (16) -> "in January 2023, the Bulgarian Parliament
    voted to scrap interim coal-reduction commitments from the RRP and keep its entire coal fleet
    online until 2038" and "The RRF is being renegotiated" (16); NECP keeps lignite "to 2050 and
    beyond" (133); "Bulgaria’s commitment to phase out the use of coal" (134).
  - ME-3: "set to stop generating power" as of March 2025, then "the Bulgarian government reversed
    this decision" (41). Ownership "Contour Global owns 73% ... NEK holding the remaining 27%" (28) vs
    "owned by the U.S. company Contour Global" (40). Complex "a state-owned enterprise" (70) vs ME-1
    AES-owned and ME-3 Contour Global-owned (40).
  - Energy intensity "among the highest in the EU" (38) vs "the most energy-intensive economy in the
    EU by a wide margin" (133).
  - Refining "dominated by one refinery" (73) beside "There are three refineries in Bulgaria" (75).
  - KNPP "Bulgaria’s first nuclear power plant" (39) vs "Bulgaria’s only nuclear power plant" (96);
    closures "early 2000s ... prerequisite for EU accession" and "part of the 2007 agreement" (39) vs
    "units 1 and 2 in 2002 and units 3 and 4 in 2006" (96); "a new KNPP unit (Unit 7)" (39) vs "two new
    reactors (Units 7 & 8)" (95); Belene "approved for construction" (39) vs "planned ... but
    subsequently opted not to do so" (96).
  - RES applications 40,000 MW (2023) "reduced to 35,000 MW" (2024) (120).
  - Waste: "a decrease in recycling" vs "Recycling of municipal waste (including composting)
    increased to 35 percent" (both 200).
  - Clean components 66.81 vs stated 67.27 (18). Number formats "28,46TWh", "3,3264 GWh" (11) and
    "$230.14 million (EUR 196) million" (87) as printed.
  - Near-duplicate coal paragraphs at 70 and 135.
- Coverage: full. Ledger: text lines 1-80, 80-139, 139-214 read (all readable text, both chapters).
  Spot-checks vs original: chart area (original 38-45) confirms the chart is not in the source text;
  smart meter tab list (original 89-91) identical. Page count: not applicable. Table spot-check: not
  applicable (no tables). Footnote: not applicable (none). Gap: the Jan-Dec 2024 production chart
  (44) is missing source material.

## D03 - Chile: Energy and Environmental Technologies (Chile Country Commercial Guide)

- Source: text/D03.txt lines 1-162; manifest docs/ccg_energy_cleantech_sectors_chile.txt, method
  text, pages null, 22,581 chars, sha256 480201f3...bfcee87. Platform Doc 6.
- Written or submitted by: U.S. International Trade Administration (line 3: "Chile Country
  Commercial Guide (U.S. International Trade Administration)"). Energy contact (95): "For more
  information about the energy sector contact U.S. Commercial Service Industry Specialist: Marcelo
  Orellana". Environmental contact (159): "contact U.S. Commercial Service Chile Commercial
  Specialist Felipe Bascuñan."
- Type, date, edition: two CCG chapters with different dates. "## Energy" (5), "Last published:
  2026-02-23" (6), `Source: https://www.trade.gov/country-commercial-guides/chile-energy` (7).
  "## Environmental Technologies" (97), "Last published: 2025-11-24" (98),
  `Source: https://www.trade.gov/country-commercial-guides/chile-environmental-technologies` (99).
- Headings in order: Energy: Overview (9); Traditional Energy Sources (12); New Energy Technologies
  (14); Advanced Nuclear (20); Conclusion (22); table (24-57); "Leading sectors include:" (fused onto
  the end of 57); Opportunities (70); Trade Shows (72); Resources (78); contact (95). Environmental
  Technologies: Overview (101); run-in "Atmospheric contamination:" (105), "Water resources scarcity
  and pollution:" (106), "Solid waste management and recycling:" (109), "Soil loss, deterioration,
  and pollution:" (111); table (112-144); "Leading Sub-sectors" (fused onto the end of 144);
  Opportunities (148) with run-ins "Desalination Plants:" (149), "Rural Potable Water:" (150),
  "Reservoir Construction:" (151); Resources (152); contact (159); closing rule (161).
- Period covered: calendar years; no fiscal convention. Both tables 2022-2025 with 2025 estimated.
  CEN capacity "As of December 2024" (15); marginal cost November 2024 (15). Target years 2025 (19),
  2030 (15), 2040 (10, 19), 2050 (10, 21, 102); trade shows 2026 (75, 77).
- Entities and aliases:
  - Ministry of Energy (15, 79, 81, 83).
  - CEN: "Chile’s Independent System Operator (Coordinador Eléctrico Nacional or CEN)" (15);
    "Coordinador Eléctrico Nacional (National Electric Coordinator or CEN), Chile’s Independent System
    Operator (ISO)" (93).
  - ACERA: "Chilean Association for Renewable Energy (ACERA)" (15); Resources 85 "Chilean Association
    for Renewable Energies, a 140-member association" (plural, no abbreviation).
  - EIU = Economist Intelligence Unit; "EIU Energy Reports" cited at 10, 13, 15.
  - Resources entry 81 begins "National Energy Commission), a technical organization, under the
    Ministry of Energy..." - the Spanish name/abbreviation before ")" is missing in the source itself.
  - SEC = "Superintendencia de Electricidad y Combustibles (Fuel and Electricity Superintendent, SEC)",
    "an office of the Ministry of Energy" (83).
  - Chilean Nuclear Energy Commission (21). SEIA = "Chile’s Environmental Impact Assessment Service
    (SEIA)" (71); PV Magazine LATAM and New Energy Events (71, cited sources).
  - Other associations (87-91): Chilean Association of Solar Energy; Chilean Association of Power
    Generation companies; Chilean Association of Energy Transmission.
  - Laws: "Framework Law on Climate Change" announced 2022 (10) / "the 2022 Climate Change Framework
    Law" (102); "Energy Transition Law" (15); "Chilean Law 20.571" (15); "The Extended Producer
    Responsibility Law (Law 20.920, or Ley REP)" (110) / "The new Extended Product Responsibility Law"
    (147); Water Code (108); Paris Agreement (102).
  - Environmental bodies: "Ministry of the Environment" (103, 110) / "Ministry of Environment" (103,
    146) / "Ministerio del Medio Ambiente (Ministry of Environment, MMA)" (154); "Superintendency of the
    Environment" (103) / "Superintendencia del Medio Ambiente (Superintendency of the Environment,
    SMA)" (155); "The Environmental Evaluation Agency" (103); "General Directorate of Waters" (108);
    MOP = "Ministerio de Obras Públicas (Ministry of Public Works, MOP)" (149-151, 153); CRHIAM and
    "Consejo Minero (Mining Council)" (156); "ACADES (Chilean association for desalination and
    wastewater reuse)" (157); Fundación Chile (109); "The 2024 World Air Quality Report" (105).
  - PPDA = "Prevention and/or Atmospheric Decontamination Plans (PPDA)" (105; "PPDAs" 103). APR =
    "rural potable water systems (APR)" (150). Net-Zero Nature-Positive Accelerator Program, Climate
    Governance Framework, Long-Term Climate Strategy (102).
  - Trade shows: EXPOENERGÍA (73), EXPONOR (75), RE+ Cono Sur (77). No energy or environmental company
    is named anywhere in D03 (only "U.S. companies" generically, 11, 71, and "The U.S Pavilion", 75);
    named non-government sources are EIU Energy Reports, PV Magazine LATAM, New Energy Events and
    Fundación Chile.
- Tables:
  - Energy table, lines 24-57: "Table: Sample Market Size for Chile Electrical Equipment (US$
    Millions)". Column headers 26-29: "2022 |", "2023 |", "2024 |", "2025 est.". Rows verbatim
    (2022 | 2023 | 2024 | 2025 est.):
    - 30-34 "Total Exports": 132.3 | 130.5 | 143.1 | 175.7
    - 36-40 "Total Imports": 3,922 | 3,957 | 3,574 | 3,886
    - 41-45 "Imports from the U.S.": 280 | 279 | 277 | 356
    - 46-50 "U.S. Trade Surplus (Deficit)": 260 | 265 | 257 | 341
    - 51-55 "U.S. Share of Imports": 7% | 7% | 8% | 10%
    - 56 "Units: US$ million, 2025 estimate based on first six months of 2025"
    - 57 "Source: Global Trade Atlas (HTS 7413, 7414, 8406, 8410, 8411, 841912, 8501, 8502, 8503, 8504,
      8506, 8507, 8532-37, 8541-44, 8546-48, 8574)" with "Leading sectors include:" fused on.
    - No Total Local Production, Total Market Size or exchange-rate row despite the title. The basis
      of "U.S. Trade Surplus (Deficit)" is not explained. Arithmetic check: Imports from the U.S. /
      Total Imports = 7.1%, 7.1%, 7.8%, 9.2%; the printed 2025 est. share "10%" does not match 356 /
      3,886. Prose 23: "The U.S. supplies, on average, over 8 percent of parts and equipment to
      Chile’s energy sector."
  - Environmental table, lines 112-144: "Table: Chile Environmental Technologies (US$ Millions)".
    Headers 114-117: "2022 |", "2023 |", "2024 |", "2025 estimate". Rows verbatim:
    - 118-122 "Total Exports": 29 | 33 | 35 | 41
    - 123-127 "Total Imports": 561 | 639 | 752 | 696
    - 128-132 "Imports from the US": 116 | 113 | 109 | 113
    - 133-137 "U.S. Trade Surplus (Deficit)": 114 | 108 | 103 | 111
    - 138-142 "U.S. Share of Imports": 21% | 18% | 15% | 16%
    - 143 "Units: $ millions"; 144 "Source: Global Trade Atlas (HTS 841960, 842121, 842129, 842139,
      842199, 847410, 847989, 902519, 902610, 902710, 902820, 847982)" with "Leading Sub-sectors"
      fused on. No basis stated for the 2025 estimate. Check: 116/561 = 20.7%, 113/639 = 17.7%,
      109/752 = 14.5% (printed 15%), 113/696 = 16.2%.
  - The two tables share the same row labels and years but different HS scopes and units lines.
- Lists:
  - Energy "Leading sectors include:" (57-69): 12 items; first "Transmission line monitoring
    equipment" (58); last "Personal safety equipment" (69).
  - Trade Shows (73-77): 3 - "EXPOENERGÍA, Santiago" (no date); "EXPONOR, June 8-11, 2026,
    Antofagasta: Chile’s second largest mining trade show also features an energy pavilion. The show
    takes place every two years. The U.S Pavilion expects over 30 exhibitors."; "RE+ Cono Sur, March
    25-26, 2026, Santiago" (last).
  - Energy Resources (79-93): 8 - Ministry of Energy; National Energy Commission; SEC; Chilean
    Association for Renewable Energies; Chilean Association of Solar Energy; Chilean Association of
    Power Generation companies; Chilean Association of Energy Transmission; Coordinador Eléctrico
    Nacional (last, 93).
  - Project pipelines: solar PV (16) "44 solar PV projects under evaluation, 86 in the approval
    process, 318 approved, and 212 in construction", plus "one solar thermal energy project that has
    been approved"; wind (17) "five wind projects under evaluation, 26 in the approval process, 33
    approved, and 13 in construction"; hydro (18) "six hydro projects under evaluation, two approved,
    and nine in construction" (no approval-process count).
  - Ley REP six products (110): oil & lubricants, electronic devices, industrial/vehicle batteries,
    packaging materials and containers, tires, small batteries (last).
  - Main air pollutants (146): PM2.5, PM10, CO, NO2, O3.
  - Environmental Resources (153-157): MOP; MMA; SMA; CRHIAM and Consejo Minero on one line (156);
    ACADES (last, 157) - 6 bodies on 5 lines.
  - Reservoirs (151): "two mayor reservoirs in the BioBio and Ñuble regions, along with five medium
    size reservoirs for the Maule and Aconcagua regions".
- Quantitative prose figures (line: figure - what it measures):
  - 13: traditional sources "installed capacity of 11.9 GW is produced by coal (3.5 GW), petroleum
    (3.1 GW), and natural gas (5.3 GW)" (parts sum to 11.9).
  - 15: target "70 percent of energy consumption from renewable power sources" by 2030, "an increase
    from the current 41 percent"; ACERA: "between the years 2022 and 2025, 5.8 gigawatts (GW) of
    renewable energy were added to the total installed capacity, meeting projected energy goals";
    Law 20.571 "installed capacity of up to 100 kilowatts (KW)"; CEN "installed power capacity of
    36,778 megawatts (MW), a 7.2 percent increase from the previous year" (as of December 2024);
    solar "8,459 MW ... (up 23 percent from 2023)"; wind "5,149 MW ... (up approximately 7 percent
    from 2023)"; Quillota 220 kV node marginal cost "$33 per megawatt hour (MWh)" (November 2024).
  - 16: "In 2024 alone, solar power plants in Chile delivered 18.6 giga watts hours (GWh) of energy";
    solar approved + under construction "approximately 20.5 GW".
  - 17: "In 2024, wind power plants delivered 11.1 GWh of energy"; wind approved + under construction
    "approximately 13.53 GW". (16-17 generation units are printed as GWh; record as printed.)
  - 18: hydro approved + under construction "approximately 121.46 megawatts (MW)".
  - 19: "six hydrogen projects with a cumulative electrolyser capacity of 396 MW are in construction".
  - 21: "the country has 2 nuclear reactors" used "only ... for medicinal purposes and research".
  - 71: six solar and battery projects submitted to SEIA: "total investment of $879.16 million",
    "155.34 MW of solar capacity and over 1 GW of battery storage (BESS)".
  - 102: "$5.3 million", four-year initiative.
  - 105: "ranks Chile as 62 of 138 most air polluted country, improving 19 positions compared with 2022".
  - 106: "After 14 years of drought"; 2024 "national deficit of 12 percent"; "11 desalination plants
    in operation, exclusively for the mining industry".
  - 107: consumptive water: agriculture 73%, drinking water 12%, industrial 7%, mining 4%, "remaining
    four percent" livestock and electricity generation (sums 100); mining's "eleven water desalination
    plants and three seawater impulse systems ... represent 25 percent of the fresh, non-recirculated
    water for their operations".
  - 108: "Approximately 95 percent of the water utility system is urban and privatized"; "100 percent
    treatment of sewage water in ten years".
  - 109: "More than 19.6 million tons of waste ... each year, 53 percent ... industrial production, 42
    percent ... municipal waste, two percent ... water treatment plants, and three percent ...
    hazardous products" (sums 100); "almost 1.2 kilograms" per capita per day; "Approximately 95
    percent of solid waste ends up in garbage dumps"; "up to 290 tons of plastics each year".
  - 110: "33 percent of Chile’s waste is recyclable, but only ten percent is recycled"; "twelve waste
    collection and recovery goals that took effect in September 2023"; "a goal of 30 percent recycled
    waste in five years".
  - 147: recycled shares: tires five percent, batteries seven percent, appliances "less than two
    percent", computer equipment 17 percent.
  - 149: Coquimbo desalination tender (2025) "$318 million"; Rancagua tender expected 2026, "around
    100 kilometers to the south of Santiago", "$186 million".
  - 150: "$63 million in rural potable water systems (APR), for the years 2025 and 2026"; 2025
    "projected investments of $25 million": expansion/improvement 76%, new services plus maintenance
    "together account for 11%", remainder exploratory wells (percentage not printed).
  - 151: Ñuble reservoir "estimated at $350 million".
- Forecasts, guidance, deadlines, effective dates: carbon neutrality by 2050 (10) / net-zero by 2050
  (102); generators "formally committed to retiring thermal power plants by 2040" (10); 70 percent
  renewable consumption by 2030 (15); hydrogen: "become a top world exporter of hydrogen by the year
  2040" and electrolysers "projected to be fully functional by 2025" (19); "Chile’s energy plan for
  2050 does not include nuclear energy as a short-term option" (21); Ley REP goals effective
  September 2023 and "30 percent recycled waste in five years" (110); Rancagua tender "expected to be
  in 2026" (149).
- Dated events: 2022 Framework Law on Climate Change announced (10); December 2024 Energy Transition
  Law passed (15); 2023 wetter winter (106); September 2023 Ley REP goals took effect (110); 2025 MOP
  Coquimbo desalination tender (149); RE+ Cono Sur March 25-26, 2026 (77); EXPONOR June 8-11, 2026 (75).
- Hedged claims (hedge -> what it attaches to):
  - 15 "the government aims to have 70 percent" (2030 target).
  - 16-18 "The estimated combined total power capacity ... is approximately" (pipeline capacity).
  - 19 "are projected to be fully functional by 2025" (the six hydrogen projects).
  - 21 "nuclear power may play a role in providing reliable energy to sectors such as mining"; "This
    characteristic may make advanced nuclear power critical"; "Demand for nuclear power is expected to
    increase in energy-intensive sectors". Firm in the same paragraph: "Nuclear power has yet to be
    developed or considered in Chile’s electricity matrix"; "there are no regulatory barriers to
    nuclear installation" (attributed to the Chilean Nuclear Energy Commission); "neither are used to
    produce electricity".
  - 71 "would add 155.34 MW of solar capacity and over 1 GW of battery storage" (submitted projects).
  - 75 "The U.S Pavilion expects over 30 exhibitors".
  - 106 "it cannot yet be stated that the drought has come to an end".
  - 149 "is expected to be in 2026" (next tender); "estimated investment of $186 million".
  - 150 "projected investments of $25 million"; 151 "estimated at $350 million".
- Rounded prose beside exact figures: "on average, over 8 percent" (23) vs table shares 7%, 7%, 8%,
  10% (51-55); "100 percent" sewage treatment (108) and "100 percent coverage" (145); "11" (106) and
  "eleven" (107) desalination plants.
- Operative definitions, rules and scope exceptions:
  - Law 20.571 covers "power generation by residential owners with installed capacity of up to 100
    kilowatts (KW)" (15).
  - Ley REP "mandates that manufacturers and importers recycle six products" (110); "either directly
    or through outsourcing services" (147).
  - Generation, transmission and distribution: "Each is operated entirely by private companies" (10).
  - Water: "legally a national asset and property of the Chilean state"; "Water property is separate
    from land property"; water rights "legal transferable property" (108).
  - Desalination plants "exclusively for the mining industry" (106).
  - Nuclear development condition: regulators must be "effectively independent" with "functional
    separation" (21). Exclusion: Chile's 2 reactors are "only used for medicinal purposes and
    research, neither are used to produce electricity" (21); "Chile is not committed to a nuclear
    energy program" (21).
  - Energy-table 2025 basis: "2025 estimate based on first six months of 2025" (56).
- Amendments or contradictions (neutral; no document-stated precedence):
  - Climate law: "carbon neutrality by 2050" (10) vs "net-zero emissions by 2050" (102); name order
    differs ("Framework Law on Climate Change" / "Climate Change Framework Law").
  - Prices: "the highest energy prices in the Americas" (13, per EIU) vs "energy costs in Chile are
    among the highest in Latin America" (146).
  - Printed shares vs row ratios: Energy 2025 est. 10% vs 356/3,886; Environmental 2024 15% vs 109/752.
  - REP law name: "Extended Producer Responsibility Law" (110) vs "new Extended Product Responsibility
    Law" (147).
  - The Energy chapter's SEIA (71) and the Environmental chapter's "Environmental Evaluation Agency"
    (103) are not linked by the document.
- Coverage: full. Ledger: text lines 1-90 and 90-162 read (all readable text, both chapters).
  Spot-checks vs original: energy table header/units lines (original 21-54) and environmental table
  (original 114-141) identical; "National Energy Commission)" clipping is present in the original
  (source defect, not extraction). Page count: not applicable. Unread ranges: none.

## D04 - China: Energy and Environmental Technology (China Country Commercial Guide)

- Source: text/D04.txt lines 1-54; manifest docs/ccg_energy_cleantech_sectors_china.txt, method
  text, pages null, 17,559 chars, sha256 e7ab0ff3...b928226. Platform Doc 10.
- Written or submitted by: U.S. International Trade Administration (line 3: "China Country Commercial
  Guide (U.S. International Trade Administration)"). No contact person or office block anywhere in
  D04 (checked against original). Line 45 refers readers to "the International Trade Administration
  Top Markets Environmental Technologies Report at `www.trade.gov`".
- Type, date, edition: two CCG chapters, same date. "## Energy" (5), "Last published: 2025-09-25" (6),
  `Source: https://www.trade.gov/country-commercial-guides/china-energy` (7). "## Environmental
  Technology" (26, singular), "Last published: 2025-09-25" (27),
  `Source: https://www.trade.gov/country-commercial-guides/china-environmental-technology` (28).
- Headings in order: Energy: untitled overview (9); Leading Sub-sectors (10); Oil & Gas (11); Silica
  & Quartz Sands (13); Distribution & Transmission (15); Energy Storage (17); Resources (19, events
  20-24). Environmental Technology: untitled overview (30); Leading Sub-sectors (31); Air Pollution
  Monitoring & Control (32); Water (35) with run-ins "Wastewater Treatment:" (37), "Sludge Treatment:"
  (38), "Water Reuse:" (39); Solid Waste (40) with run-ins "Municipal Solid Waste:" (42), "Ordinary
  Industrial Waste:" (43), "Hazardous Waste:" (44); referral line (45); Resources (46, events 47-51);
  closing rule (53).
- Period covered: calendar years; no fiscal convention. Data 2017-2024; targets 2025, 2027, 2030;
  events April 2025 - March 2026.
- Entities and aliases:
  - "China’s state-owned Sinopec oil company" (12). "Zhang Zongliang, an academician with the Chinese
    Academy of Engineering" (18, source of the pumped-hydro figure).
  - "the Chinese government" (9, 18) / "the PRC" (34) (PRC not expanded).
  - "Ministry of Ecology and Environment" (33, 37, 38); "World Health Organization" (33).
  - "China’s State Council" (36) / "the State Council" (41) / "the China State Council’s 2025 Report
    on the Work of the Government to the National People’s Congress" (42).
  - NDRC = "National Development and Reform Commission (NDRC)" (37; also 38, 39); MOHURD = "Ministry
    of Housing and Urban-Rural Development (MOHURD)" (37, 38); "Ministry of Water Resources" (39).
  - Plans and laws: "City and Township Sewage Treatment and Resource Utilization Development Plan"
    (37); "A January 2024 guideline from the plan" (37); "The most recent implementation plan,
    released in 2022" (sludge, 38); "14th Five-Year Plan" (39) / "The 14th Five-Year Plan (2021-2025)"
    (41); "China’s Action Plan for Reaching Carbon Dioxide Peak Before 2030" (41, 2021); "the Solid
    Waste Law" revised 2020 (44).
  - Countries named as suppliers/competitors: Russia, Saudi Arabia, Iraq (crude, 12); Australia,
    Qatar, Russia (LNG competition, 12); United States, Australia, Indonesia (silica sand sources, 14).
  - Provinces/cities: Shaanxi, Tianjin, Shandong (oilfield activity, 12); Harbin, Yinchuan, Beijing,
    Changsha (PM2.5, 33); Shanxi, Inner Mongolia, Hebei, Liaoning, Shandong (industrial waste, 43);
    Shandong, Jiangsu, Zhejiang (hazardous waste production centres) and Xinjiang, Qinghai, Sichuan
    (disposal gaps) (44). Shandong recurs at 12, 43 and 44.
  - Event abbreviations: ESIE (20), WGC2025 (21), EP Shanghai (23), NIC (24), WieTeC (49), IE Expo (47,
    50, 51). No company other than Sinopec is named; U.S. firms appear only generically.
- Tables: none (the only "|" is the file header). Not applicable.
- Lists:
  - Energy Resources events (20-24), 5 items: "Energy Storage Conference & Expo 2025 (ESIE) – Beijing,
    April 10-12, 2025"; "29th World Gas Conference (WGC2025) – Beijing, May 19-23, 2025"; "2025 Central
    China Petrochemical High-Quality Development Conference & Exhibition – Zhengzhou, Henan, June 17-19,
    2025"; "International Exhibition of Electric Power Equipment and Technology (EP Shanghai) – November
    18-20, 2025"; "Nuclear Industry China (NIC) – Beijing, March 19-22, 2026" (last).
  - Environmental Resources events (47-51), 5 items: "IE Expo China – Shanghai, April 21-23, 2025";
    "The China International Environmental Protection Exhibition & Conference – Beijing, April 10-12,
    2025"; "WieTeC – Shanghai, June 3-5, 2025"; "IE Expo Chengdu – Chengdu, June 25-27, 2025"; "IE Expo
    Guangzhou – Guangzhou, September 17-19, 2025" (last). Not in date order (47 is later than 48).
    ESIE (20) and the 48 conference share Beijing and April 10-12, 2025.
  - PV supply chain stages (14): "wafer, cell, and module production".
  - Provincial capitals with PM2.5 increases (33): Harbin (72 percent), Yinchuan (56 percent), Beijing
    (46 percent), Changsha (44 percent) - 4, last Changsha.
  - Water-reuse pilot sectors (39): "six industrial sectors, including petrochemical, iron and steel,
    nonferrous metals, papermaking, textiles, and food" (6, last food).
  - Leading solid-waste regions (41): Southwest, South, East, Central China.
  - Five industrial-waste provinces (43): Shanxi, Inner Mongolia, Hebei, Liaoning, Shandong (last).
- Quantitative prose figures (line: figure - what it measures):
  - 12: "largest oil importer since 2017, importing over 70 percent of the 75 million tons it consumed
    in 2024" (as printed); Sinopec "peak oil" by 2027; 2024 LNG imports "fell approximately 2 percent";
    "15 percent additional tariffs on U.S. LNG announced by China in February 2025".
  - 14: U.S. exported "$882.1 million worth of silica sands and quartz sands in 2024, with $403.2.
    million sold to China—a 45.1-percent year-on-year increase"; China's share of U.S. silica/quartz
    exports "grown from 16.1 percent to 45.7 percent" "Since 2020" (403.2/882.1 = 45.7%, consistent);
    China controls "over 80 percent of each major stage of the supply chain".
  - 16: "a record 373.6 GW of new installations in 2023 alone, primarily in solar and wind"; "total
    renewable energy capacity to 1,827.3 GW, already exceeding its target of 1,200 GW of installed wind
    and solar by 2030" (total-renewable figure compared with a wind-and-solar target as printed);
    renewables "just 35 percent of electricity generation".
  - 18: pumped hydro storage "reaching 58.69 million kW by the end of 2024" (kW scale); BESS "total
    storage capacity quadrupling to 31.4 GW in 2023" (GW scale; different year; whether 31.4 GW is BESS
    only or all storage is not explicit).
  - 30: environmental technology market "average annual rate of 12.8 percent from 2017 to 2021"; 2022
    industry "$329 billion in operating income, accounting for 1.8 percent of GDP and employing over
    3.2 million people".
  - 33: air pollution "contributing to over 2 million deaths annually"; 2024 annual mean PM2.5
    "approximately 29.3 μg/m3"; WHO guideline "should not exceed 5 μg/m3"; "more than 30 percent of
    Chinese cities failing to meet national air quality standards for PM2.5".
  - 36: population "about 18 percent of the world’s total", water resources "only 6 percent"; 2023
    rural residential sewage treatment rate "exceeded 40 percent".
  - 37: "100 low-carbon treatment plants set to be built by 2025"; "expanding and renovating 45,000
    kilometers of sewage collection networks and increasing sewage treatment capacity by 12 million
    cubic meters daily".
  - 38: sludge production "exceeded 70 million tons" (as of 2024); "additional 20,000 tons per day of
    sludge treatment capacity by the end of 2025"; treatment rate "above 95 percent".
  - 39: "add 15 million cubic meters per day of reclaimed water capacity by 2025"; water reuse market
    "$2.07 billion" (2023), "projected to reach $4.06 billion by 2030"; "sponge city" projects "in 90
    cities".
  - 41: resource recycling industry "projected to reach $697 billion by 2025".
  - 42: "As of 2023, China treated 254 million metric tons of municipal waste"; "927 incineration plants
    and over 300 waste-to-energy facilities"; sorting efficiency "from 75 percent to 98 percent";
    possible mandate "30 percent of materials in government projects to be certified recycled".
  - 43: ordinary industrial waste "about four-fifths of China’s solid waste"; "4.11 billion tons" (2022)
    "up from 3.97 billion tons in 2021"; five provinces "45 percent of the total in 2021".
  - 44: hazardous waste "projected to reach 200 million tons by 2030, growing at a 3 percent annual
    rate"; "hazardous waste utilization rate of around 47 percent".
- Forecasts, guidance, deadlines, effective dates:
  - Peak oil by 2027 (Sinopec anticipation, 12); wind+solar target 1,200 GW by 2030, stated as already
    exceeded (16); carbon peak by 2030 (41); waste recycling system by 2025, "full development by 2030"
    (41); water/sewage 2025 targets (36-39); hazardous waste 200 million tons by 2030 (44); water reuse
    market $4.06 billion by 2030 (39); recycling industry $697 billion by 2025 (41).
  - 2025 water targets, three wordings: State Council "over 95 percent in county-level areas" and
    recycled water "more than 25 percent in water-scarce cities at the prefecture level and above" (36);
    development plan "over 95 percent in county-level cities" and "over 25 percent in water-scarce
    prefecture-level cities" (37); Ministry of Water Resources and NDRC "above 25 percent in
    water-scarce cities" (39); sludge "above 95 percent in county-level and larger cities" (38).
- Dated events: 2017 China becomes largest oil importer (12); 2020 Solid Waste Law revised (44); 2021
  carbon-peak action plan (41); 2022 sludge implementation plan released (38); January 2024 guideline
  (37); February 2025 15 percent LNG tariff announced (12); March 2025 storage mandates cancelled (18);
  events April 10-12, 2025 through March 19-22, 2026 (20-24, 47-51).
- Hedged claims (hedge -> what it attaches to):
  - 12 Sinopec "anticipates China will reach “peak oil” by 2027".
  - 14 "anecdotal and trade source reporting suggests that China has steadily increased its downstream
    processing capabilities" (preceded by "While global market data ... is limited").
  - 34 "will be well-positioned" (U.S. sensor/monitoring firms).
  - 36 "the country aims to achieve" (State Council 2025 targets) vs 37 "China will achieve" (same
    targets stated firmly under the development plan).
  - 39 "is projected to reach $4.06 billion by 2030"; 41 "is projected to reach $697 billion by 2025";
    41 "will likely find growing demand" (U.S. waste-solution providers).
  - 42 "considering a mandate requiring 30 percent" (proposal) vs "China is introducing a certification
    system for recycled products" (action under way); "Several large-scale waste treatment facilities
    are also planned".
  - 44 "is projected to reach 200 million tons by 2030".
- Rounded prose beside exact figures: none paired with a table. Shares 45.7 percent (14) vs
  403.2/882.1 consistent.
- Operative definitions, rules and scope exceptions:
  - March 2025 action: "the government cancelled policy mandates requiring solar and wind energy
    projects to include energy storage systems" (18).
  - Silica/quartz described as "the primary minerals used for solar generation" (14).
  - WHO PM2.5 guideline threshold 5 μg/m3 (33).
  - Scope words for 2025 water targets differ (county-level areas vs county-level cities; prefecture
    level and above vs prefecture-level) - see Forecasts.
- Amendments or contradictions (neutral; no document-stated precedence):
  - Storage mandates for solar and wind projects cancelled March 2025 (18) - an actual policy change
    (prior mandate described as "an important factor in driving storage capacity demand").
  - Capacity vs target scope: 1,827.3 GW "total renewable energy capacity" said to exceed a "1,200 GW of
    installed wind and solar" target (16).
  - Unit scales differ inside one paragraph: "58.69 million kW" (end-2024 pumped hydro) vs "31.4 GW"
    (2023 storage) (18).
  - Event lists: energy ESIE and environmental exhibition both "Beijing, April 10-12, 2025" (20, 48).
- Coverage: full. Ledger: text lines 1-54 read (one chunk; all readable text, both chapters).
  Spot-check: original has 46 non-empty lines, matching the text's 46 content lines; no tables or
  footnotes (not applicable). Page count: not applicable. Unread ranges: none.

## D05 - Finland: Energy (Finland Country Commercial Guide)

- Source: text/D05.txt lines 1-73; manifest docs/ccg_energy_cleantech_sectors_finland.txt, method
  text, pages null, 15,544 chars, sha256 afd71281...be12. Platform Doc 18.
- Written or submitted by: U.S. International Trade Administration (line 3: "Finland Country
  Commercial Guide (U.S. International Trade Administration)"). Contact (69-70): "Information /
  Interested parties may contact Commercial Specialist Tiina Ketelä-Juvonen, `tiina.ketela@trade.gov`".
- Type, date, edition: single CCG chapter "## Energy" (5), "Last published: 2025-09-29" (6),
  `Source: https://www.trade.gov/country-commercial-guides/finland-energy` (7). No Environmental
  Technologies chapter.
- Headings in order: Overview (9); bare Reuters URL line (15); Leading Sub-Sectors (16); Nuclear (17);
  Critical Minerals (23); Renewable Energy (30) with run-ins "Wood-based fuels:" (35), "Hydropower:"
  (37), "Wind power:" (38), "Geothermal energy:" (mid-line 38), "Solar:" (39); Opportunities (41);
  Associations (42); Events (51); Resources (60); Information (69); closing rule (72).
- Period covered: calendar years; no fiscal convention. Data 2022-2024 (2024 energy totals are
  "Statistics Finland’s preliminary data", 31). Targets 2030, 2035, 2040, 2050; events February 2025 -
  October 2026.
- Entities and aliases:
  - "The Government of Finland" (11); "the Climate Change Act from 2015" (11); "Finland’s Annual
    Climate Report" (11); "Finland’s Climate and Energy Strategy and Medium-term Climate Change Policy
    Plan" (11).
  - Fortum: "Finnish energy company Fortum" (13); "Fortum Oyj, a Finnish state-owned energy company and
    operator of the Loviisa NPP" (18). "U.S.-based Westinghouse Electric" (13). TVEL (13; nationality
    and role not stated beyond "Fortum’s existing contracts with TVEL").
  - "TVO Oyj (Teollisuuden Voima Oyj), operating the Olkiluoto NPP (OL1, OL2 and OL3)" (18).
  - "STUK, the Nuclear Safety Authority, which is the regulatory body in charge of supervising
    radiation and nuclear safety in Finland" (18) - listed inside the sentence "Finland’s nuclear power
    operators are:".
  - Reactor designs (19): OL1 and OL2 "ASEA-Atom, Boiling Water Reactors"; OL3 "an AREVA NP, Siemens
    AG, European Pressurized Water Reactor (ERP." (as printed); Loviisa "VVER-440 V213 (Western I&C
    system and containment) Pressurized Water Reactors".
  - Hanhikivi: "the Hanhikivi 1 NPP project in northern Finland" / "the Hanhikivi NPP" (20); Fennovoima
    "a consortium of 67 companies and co-owned by RAOS Voima, a subsidiary of Russian Rosatom" (RAOS
    Voima also "RAOS"); "The Municipality of Pyhäjoki" (20).
  - "EcoSMR HUB" (22) / "EcoSMR: Internationally networked Finnish system dedicated to the development
    of small modular reactors (SMRs)" (46).
  - UNFC = "United Nations Framework Classification for Resources (UNFC)" (25); GTK = "Geological
    Survey of Finland (GTK)" (25); MSP = "Minerals Security Partnership (MSP), a U.S. U.S. initiative
    established in 2022" (26, doubled "U.S." as printed).
  - Laws (29): "the Land Extraction Act (555/1981, Since January 1, 1982) and the Mining Act (621/2011,
    Since July 1, 2011)".
  - Statistics Finland (31, 62, 64); "EU Renewable Energy Directive" (31); Sweden (31, comparison).
  - "Fingrid, Finland’s grid transmission system operator" (34).
  - Associations (44-50): "Finnish Wind Power Association/ Renewables Finland Association"; EcoSMR;
    "Finnuclear Association, 2023 Directory"; "TED (Tenders Electronic Daily)". "State Treasury Republic
    of Finland" (68). Reuters (URL at 15, dated 2024-09-02 in the slug).
- Tables: none (no "|" in the original). Resources line 66 names an external table, "Total energy
  consumption by energy source (all categories), 1970-2023*"; the asterisk has no note in the document.
- Lists:
  - Fossil fuels Finland lacks (11): "coal, oil, or natural gas"; it has "wood-based fuels, rich
    reserves of peat, and extensive wood resources".
  - Climate Change Act targets vs 1990 (11): 2030 "down by 60 percent", 2040 "down by 80 percent",
    2050 "down by 90 percent, but aiming at a cut of 95 percent".
  - Nuclear entities (18): Fortum Oyj; TVO Oyj; STUK (last; the regulator).
  - Reactors (19): OL1, OL2, OL3 at Olkiluoto; two VVER-440 units at Loviisa (5 total).
  - Finland-US MoU topics (21): nuclear energy technologies; nuclear waste management and final
    disposal of radioactive waste; new reactor types such as SMRs; nuclear safety; nuclear fuels.
  - Mineral-supplier strengths (28): 4; last "a highly educated and competent workforce".
  - "most important forms of renewable energy" (33): bioenergy; forest-industry side-stream fuels and
    other wood-based fuels; hydropower; wind power; air and ground-source heat pumps.
  - Associations (44-50): 4; last TED.
  - Events (53-59), 4, not in date order: "Wind Finland, September 30, 2025, in Helsinki" ("more than
    500 participants from more than 12 countries"); "Energia, October 20-22, 2026, in Tampere" ("the
    largest biennial energy industry trade event"); "Nordic Hydrogen Week, February 10-14, 2025, in
    Oulu" ("will showcase TOP-10 hydrogen projects", future tense); "EnergyWeek, March 17-20, 2025, in
    Vaasa" (last).
  - Resources (62-68): 4; last "State Treasury Republic of Finland".
- Quantitative prose figures (line: figure - what it measures):
  - 11: carbon-neutral by 2035, "carbon-negative soon after"; emission cuts above.
  - 13: TVEL contracts "go on until 2027 and 2030".
  - 14: "Consumption of fossil fuels decreased by 10 percent in 2023 and was 30 percent of total energy
    consumption in 2023. The share of oil was 19 percent and coal five percent." (remaining fossil
    share not itemized).
  - 19: "The reactors provided 41.1 percent (32.75 TWh) of the total electricity generated in the
    country in 2023"; "The share of total energy consumption was 27 percent in 2023, which was an
    increase of 35 percent compared to 2022" (base of the 35 percent not explicit).
  - 20: "consortium of 67 companies"; "existing permits for the construction of two conventional
    reactors" (municipality's claim).
  - 24: "more than 40 mining clusters"; lithium deposits "first identified in the late 1950s".
  - 27: "As of January 1, 2024, the mining tax is $0.6 per cent of the average market value of the
    previous calendar year for metallic minerals and $0.2 per ton for other minerals." (symbols as
    printed).
  - 31: 2024 total energy consumption "1.29 million terajoules (TJ), and renewable 562 thousand
    terajoules"; renewables "43 percent of energy end-consumption in 2024"; target "51 percent for the
    share of renewable energy (gross final consumption)"; share "second highest in the European Union
    after Sweden". (562 / 1,290 thousand TJ = 43.6%; the printed 43 percent is on an
    "end-consumption" base.)
  - 35: wood fuels "around one-fourth of Finland’s total energy consumption" (recent years).
  - 36: "In 2024, wood fuels covered 28 percent of total energy consumption".
  - 37: hydropower "4.0 percent of the total energy consumption in 2024"; "The installed hydropower
    capacity currently is 13.3 TWh" (capacity printed in an energy unit).
  - 38: wind "more than 19.8 TWh of electricity, accounting for 24 percent of total electricity
    consumption" (2024).
  - 39: "The share of solar power capacity in Finland grew by 61 percent in 2024"; solar "covering only
    one percent of the electricity consumption".
- Forecasts, guidance, deadlines, effective dates: carbon-neutral by 2035 (11); 2030/2040/2050 cuts
  (11); renewable target 51 percent "currently set" (31); EU climate neutrality by 2050, "binding for
  Finland" (32); "Lithium production also will commence in Finland over the next few years" (24);
  mining tax rates effective January 1, 2024 (27).
- Amendments: "The Act was updated in 2022 and sets new emission reduction targets" and "The scope of
  the Act has been extended to cover the land use sector" (11). "Finland’s Climate and Energy Strategy
  and Medium-term Climate Change Policy Plan was also updated in Septe On an international scale..."
  (11) - sentence clipped in the source; the update month/year is missing source text.
- Dated events: late 1950s lithium identified (24); January 1, 1982 and July 1, 2011 laws in force
  (29); 2015 Climate Change Act (11); February 2022 invasion of Ukraine (13); May 2022 Russian
  electricity and pipeline-gas imports ceased (13); spring and summer 2022 Russian crude stopped (13);
  May 2022 Fennovoima terminated the RAOS contract and withdrew the construction licence application
  (20); 2022 Act updated (11); 2022 MSP established (26); April 2023 Finland-US MoU (21); September
  2024 Fortum announced Westinghouse fuel at Loviisa (13); events February 10-14, 2025; March 17-20,
  2025; September 30, 2025; October 20-22, 2026 (53-59).
- Hedged claims (hedge -> what it attaches to):
  - 11 "but aiming at a cut of 95 percent" (2050 aspiration beyond the 90 percent target); "additional
    measures are needed" (per the Annual Climate Report).
  - 20 "It would have been operated by Fennovoima" (counterfactual); the municipality "claims"
    Hanhikivi "offers the quickest pathway" (attributed claim).
  - 22 "Finland sees SMRs as a strong potential option".
  - 24 "Lithium production also will commence" (firm "will", no hedge).
  - 37 "with no significant change foreseen" (hydro capacity).
  - 38 "Geo-energy is expected to take an even greater share".
  - 39 "roughly as much sunshine as countries such as Germany and Denmark".
- Rounded prose beside exact figures: wood fuels "around one-fourth" (35) vs "28 percent" in 2024
  (36); renewables "43 percent" vs 562 / 1,290 thousand TJ (31).
- Operative definitions, rules and scope exceptions:
  - "There are no inactive reactors in Finland." (19) - exclusion statement.
  - Peat and wood are listed as what Finland "does have", contrasted with fossil fuels (11).
  - Mining tax bases: metallic minerals on "the average market value of the previous calendar year";
    other minerals "per ton" (27).
  - Renewable target base "(gross final consumption)" vs actual share on "energy end-consumption" (31).
  - "the only EU member state with its own cobalt production" (24).
  - "Finnish energy companies use open tenders as required by European Union (EU) regulations" (50).
  - Aliases defined: "Geothermal energy (or geo-energy as it often called in Finland)"; "Ground Source
    Heat Pumps (GSHPs)" (38).
- Amendments or contradictions (neutral; no document-stated precedence):
  - Finland "has ceased all imports and consumption of Russian energy resources" (13) beside "Fortum’s
    existing contracts with TVEL go on until 2027 and 2030" (13).
  - "five operating nuclear reactors in two power plants" (19) vs "A sixth nuclear power plant, the
    Hanhikivi 1 NPP project" (20).
  - STUK, the regulator, listed under "nuclear power operators" (18).
  - Hydropower "capacity" given as 13.3 TWh (37).
  - Nordic Hydrogen Week (February 2025) described in future tense in a chapter published 2025-09-29 (57).
- Coverage: full. Ledger: text lines 1-73 read (one chunk; all readable text). Spot-checks vs
  original: no "|" (no tables; table/footnote checks not applicable); "updated in Septe On an
  international scale" clipping, "(ERP.", "U.S. U.S." and "$0.6 per cent" all present in the original
  (source defects). Page count: not applicable. Gap: the clipped update date in line 11 is missing
  source text.

## Shared ground within this part (navigation only)

- Authorship and editions: all five are U.S. International Trade Administration Country Commercial
  Guide chapters (line 3 of each). Chapters and "Last published" dates: D01 Energy 2024-02-01 (6);
  D02 Energy 2026-03-31 (6) and Environmental Technologies 2026-04-01 (154); D03 Energy 2026-02-23 (6)
  and Environmental Technologies 2025-11-24 (98); D04 Energy 2025-09-25 (6) and Environmental
  Technology 2025-09-25 (27); D05 Energy 2025-09-29 (6). Each country appears once; no document in
  D01-D05 cites, amends or responds to another.
- Contacts (issuer staff, not mentioned organizations): D01 Mauro Fonseca, U.S. Commercial Service
  Angola (128-133); D02 Emily Taneva (147-151) and Stanislava Dimitrova (206-211), U.S. Commercial
  Service Sofia; D03 Marcelo Orellana (95) and Felipe Bascuñan (159); D04 none; D05 Tiina
  Ketelä-Juvonen (70).
- Market-data tables: only D01 (Table 3, 67-83: 2018-2022, "Units: US$ millions", Local Production,
  Exports, Imports, Imports from the US, Total Market Size, Exchange Rates) and D03 (energy 24-57 and
  environmental 112-144: 2022-2025 est., Exports, Imports, Imports from the U.S., U.S. Trade Surplus
  (Deficit), U.S. Share of Imports). 2022 is the only year present in both D01 and D03 tables. Global
  Trade Atlas is the source in D01 (83, with the "United States International Trade Commission") and
  D03 (57, 144). HS 8411 and 8503 appear in
  both D01 (73, 76) and D03 (57); D03's "8532-37" range spans D01's 8537. D02, D04, D05 have no tables.
- Prose that repeats or sits beside table results: D01 62 (HTS 8411 US$ 14.8 million, 2022) beside
  Table 3; D03 23 ("on average, over 8 percent") beside the U.S. Share of Imports row (51-55).
- Westinghouse: D01 "Westinghouse Turbines" among U.S.-based companies (61); D02 Westinghouse Electric
  Company / Westinghouse Electric / WEC / AP1000 / RWFA (95, 97); D05 "U.S.-based Westinghouse
  Electric" fuel at Loviisa, September 2024 (13).
- VVER and Russian nuclear entities: D02 "Russia-designed VVER-1000" (97) and Atomstroyexport (96);
  D05 "VVER-440 V213" (19), "RAOS Voima, a subsidiary of Russian Rosatom" (20), TVEL (13).
- ZTE: D01 117 ("ZTE (China)", meter supplier considered, project on hold) and D02 87 (installed smart
  meters with ADD Bulgaria).
- Nuclear electricity shares: D02 "approximately 41.6%" of generation 2024 per IAEA (13) and "about
  40.38%" for September 2024 - August 2025 (18); D05 "41.1 percent (32.75 TWh)" of electricity
  generated in 2023 (19). D03 states its 2 reactors are not used for electricity (21). D01 and D04
  give no nuclear generation figure (D04 lists only a Nuclear Industry China event, 24).
- SMRs and U.S. nuclear cooperation: D02 2024 IGA (95) and MoUs with NuScale, X-Energy, Fluor,
  Holtec (98); D05 April 2023 Finland-US MoU (21), EcoSMR (22, 46); D03 "advanced nuclear" (20-21).
- Russian supply cut-offs after the invasion of Ukraine: D02 (54 Gazprom halted 2022; 74 crude
  derogation expired early 2024; 117); D05 (13 May 2022 and spring/summer 2022; 20 May 2022 Hanhikivi
  contract termination).
- Battery storage figures: D02 (12 BESS ~500 MW / ~1,300 MWh by mid-2025; 86 at least 3 GWh target);
  D03 (71 over 1 GW BESS in submitted projects); D04 (18 "total storage capacity quadrupling to 31.4
  GW in 2023" in a BESS sentence, scope not explicit; storage mandates cancelled March 2025).
- Green hydrogen: D01 (106 Sonangol 2022 partnership), D02 (47 priority), D03 (19 396 MW electrolysers,
  2040 exporter goal), D05 (57 Nordic Hydrogen Week).
- Smart meters: D01 (65, 117), D02 (83-92), D05 (12).
- Target years shared: 2050 climate neutrality/net-zero in D02 (133 NECP; 194 EU Green Deal), D03 (10,
  102), D05 (32 EU); D05 national carbon neutrality 2035 (11). 2030 targets in D01 (63 Power Africa),
  D02 (119 3,200 MW), D03 (15 70 percent), D04 (16 1,200 GW wind+solar; 41 carbon peak), D05 (11 -60
  percent). 2025 targets in D01 (10, 15, 65, 104, 106-107), D03 (19), D04 (36-41).
- Wind/solar figures on different bases and units: D02 wind 3.44% and solar 16.52% (18), 15 and 53
  percent of renewables (118); D03 wind 5,149 MW / 11.1 GWh and solar 8,459 MW / 18.6 GWh (15-17); D05
  wind 19.8 TWh = 24 percent of electricity consumption, solar one percent (38-39).
- Trade-event lists: D03 (73-77, 2026 dates), D04 (20-24 and 47-51, 2025-2026), D05 (53-59, 2025-2026).
- Abbreviation reuse within this part: "TSO/TSOs" (D02 56 gas TSOs of seven countries; D02 120 "the
  TSO"; D02 14 ESO described as transmission system operator); D05 Fingrid "grid transmission system
  operator" (34); D03 CEN as "Independent System Operator (ISO)" (93); "MOU/MoU" (D01 106, D02 71/98,
  D05 21); "BESS" (D02 12, D03 71, D04 18); "NPP" (D02, D05); "AfDB/AFDB" (D01 65/115).
- Source defects (not extraction): D01 Table 2 row 4 "TBD" placement and Table 3 "2019 2020" merged
  header (54-57, 69); D02 missing chart (44); D03 clipped "National Energy Commission)" (81); D05
  clipped "updated in Septe" (11).


<!-- merged from doc-map-b.md -->

# aq-01543 - document map, part B (D06-D10)

Written by `bundle-mapper` (part B of five parallel parts; the caller merges the parts into
`notes/doc-map.md`). It is for navigation: where things are, not what to ask. Questions quote
the documents, never this map.

Conventions:
- `Lnn` = line number in `text/Dxx.txt`. Body lines map to the `docs/` original as
  original line = text line - 2 (the text adds a two-line `# Dxx | docs/...` header). The closing
  `-----` separator alone sits at text = original + 1 (the text collapses the double blank line
  before it).
- "Computed" marks the mapper's own arithmetic on stated figures (re-checked by hand). These
  results are not stated in the documents.
- Quoted strings are verbatim (curly quotes, dashes and typos kept).

## Part B bundle notes

- What it is: five U.S. International Trade Administration (ITA) Country Commercial Guide sector
  chapters (energy, environmental technology, power sector, renewable energy). The countries are
  Germany, Indonesia, Israel, Mauritius and Mexico. All are plain-text captures with no page images.
- Documents: D06 Germany, D07 Indonesia, D08 Israel, D09 Mauritius, D10 Mexico (ids from
  `text/manifest.json`).
- Gaps: none in this part. Every line of all five texts was read, so no range is unread. No source
  text is missing (`notes/intake.json`: `incomplete: false`, `gap_characters: 0`,
  `matches_capture: true` for all five). No line reaches 2,000 characters. The only line over
  1,800 characters is D09 L74, and it displayed through its true end "solar farm in Amaury.",
  so no display was truncated. Visual/page inspection does not apply: the sources are .txt captures
  and the manifest gives `pages: null`.
- Extraction spot-checks (text against the `docs/` original):
  - Page count: not applicable for all five (text sources).
  - Tables: in D07, table 1 (text L10-66 = original L8-64) and table 2 (text L103-115 = original
    L101-113) are identical except that the trailing space after each "|" is stripped. The D10 table
    (text L30-38 = original L28-36) is identical. D06, D08 and D09 have no tables (not applicable).
  - Footnote: the D09 anchor "Key Statistics*" (L15) and "*Source: Statistics Mauritius, January 2025
    CareEdge Ratings Report" (L23) are identical to original L13/L21. D06, D07, D08 and D10 have no
    footnotes (not applicable). The data-source lines under the tables (D07 L66 and L115, D10 L38)
    are identical.
  - Other compared ranges (text -> original): D06 L54-67 -> L52-66; D07 L3-72, L97-121 and L130-144
    -> L1-70, L95-119 and L128-143; D08 L35-87 -> L33-86; D09 L12-26 and L117-124 -> L10-24 and
    L115-123; D10 L27-56 and L76-104 -> L25-54 and L74-103. All are identical apart from the
    trailing-space and final-blank-line differences noted above.
- Provenance: the platform's capture numbering (in `notes/intake.json`) differs from the D-ids:
  D06 = capture doc 9, D07 = doc 19, D08 = doc 5, D09 = doc 8, D10 = doc 13. For each document,
  `source_sha256` = `captured_sha256` = the manifest sha256 (D06 44852689..., D07 122bcda5...,
  D08 d6233beb..., D09 ced21501..., D10 9aae3651...).

---

## D06 - Germany Country Commercial Guide: Energy

- Source: `text/D06.txt` (67 lines; 23,033 chars) from `docs/ccg_energy_cleantech_sectors_germany.txt`. No pages.
- Written or submitted by: U.S. International Trade Administration (L3 "Germany Country Commercial Guide (U.S. International Trade Administration)"). There is no commercial-specialist contact line. Bodies cited for figures, which are not authors: Federal Network Agency (L44); National Hydrogen Council (L52); "The German government" (L52); economy-ministry name variants (L32, L34, L54).
- Type, date, edition: one chapter, "## Energy" (L5); "Last published: 2025-08-01" (L6); "Source: https://www.trade.gov/country-commercial-guides/germany-energy" (L7). The bundle holds one edition.
- Period covered: actuals are mainly 2023 and 2024. 2024 covers the energy mix, electricity, gas, crude and LNG. 2023 covers domestic production, storage installations, residential PV and carbon intensity. Status points: "As of May 2025" (L24), "As of 2025" (L33), "As of early 2025" (L44), industrial output "in 2025" (L10). Targets run 2027-2050. Fiscal/calendar convention: not stated; years are unlabelled.
- Section headings in order: "Overview" L9; "Energy consumption and generation" L16 (run-in labels "Energy consumption:" L17, "Energy production:" L18, "Electricity generation:" L19, "Energy costs:" L20); "Energy imports" L21 ("Natural Gas:" L22, "Crude Oil:" L23, "Liquified Natural Gas (LNG):" L24); "Energy policy" L25; "Opportunities" L35; "Energy infrastructure" L38; "Investment in High Voltage Lines and Grid Expansion" L43; "Energy Storage" L47; "Hydrogen" L51; "Resources" L55; "Trade Events" L56; "Government Links" L62; separator L67.
- Entities and aliases:
  - Economy ministry name variants: "The Federal Ministry for Economic Affairs and Energy (BMWE)" L26 (oversees energy policy and supervises the energy sector) and "BMWE - Federal Ministry for Economic Affairs and Energy" L63; "the Ministry of Economy" L32 (2045 hydrogen demand); "the Federal Ministry of Economy and Energy" L34 (LNG terminals); "the Federal Ministry of Economics" L54 (green ammonia). The text does not explicitly equate the variants.
  - "The Federal Ministry for the Environment, Climate Action, Nature Conservation, and Nuclear Safety (BMUKN)" L26 (environmental protection, nature conservation, climate action).
  - Regulator: "The “Federal Network Agency” (Bundesnetzagentur)" L36 = "BNetzA - Federal Network Agency" L65; also cited at L44. It is the "regulatory office for electricity, gas, telecommunications, post, and railway markets" (L36).
  - "DENA - German Energy Agency" L64 (link list only).
  - Laws: "Renewable Energy Source Act (EEG)" and "Renewable Energies Heat Act (EEWärmeG)" L28; "The European Climate Law" L30.
  - Hydrogen: "The National Hydrogen Council" ("government advisory board") L52; "H2Global" / "The H2Global Foundation" / "its H2Global foundation" L54; "the European Commission" (state-aid approval) L54; "the European Hydrogen Bank" L54.
  - Transmission system operators (TSOs), four at L46: "50 Hertz Transmission, Amprion, TenneT TSO, and TransnetBW".
  - LNG: terminal locations at L37 ("such as those in Wilhelmshaven, Brunsbüttel, and Mukran"); "Floating Storage and Regasification Units (FSRUs)" L33.
  - Countries: France and Italy (energy consumers after Germany, L10); France at 56 gCO2/kWh (L12); Norway 48% and the Netherlands 25% of 2024 gas imports (L22); Belgium and the Netherlands (connected terminals, L33); Russia (L20, L24, L29, L33, L34); United States (price comparison L20, LNG L24, hydrogen L53); "Canada, the UAE, Australia, and the United States" (potential hydrogen suppliers, L53).
  - Places: Lusatia region, "Eastern Germany’s historic lignite mining belt" (L50). Trade-event cities: Essen, Hannover, Munich, Hamburg, Bilbao (L57-61).
  - Terms: "Energiewende" (L11, L27, L28), glossed as "energy transition" (L27).
  - Governments: "the new coalition agreement" (L17); "The previous government" (L34).
- Tables: none (not applicable). All figures are in prose.
- Quantitative figures in prose (unit, period, what is measured):
  - L10: industrial output for energy-intensive goods "in 2025 remaining roughly 17 percent lower than pre-2022 levels"; production has declined "almost continuously since the beginning of 2022".
  - L12: target "80 percent of its electricity supply to come from renewables by 2030 and achieved 59 percent in 2024"; GHG "reduce ... by 65 percent from 1990 levels by 2030"; carbon neutrality by 2045; 2024 CO2 emissions at their "lowest level ... since the 1950s"; "sixth most carbon-intensive electricity in Europe at 381 gCO2/kWh compared to just 56 gCO2/kWh in France in 2023".
  - L17 (2024 primary energy consumption): "10,478 Petajoules"; "more than 77 percent coming from fossil sources"; "20 percent from renewables"; oil "36.1 percent"; natural gas "25.9 percent"; "Hard Coal accounted for 7.3 percent and lignite for 7.6 percent"; "Of the 20 percent renewable energy production, on- and off-shore wind accounted for 48.8 percent"; hydro output "increased by 11.6 percent year-over-year ... making up 4.5 percent of all gross electricity generation"; "wind energy accounted for 27.9 percent of electricity generation and for PV systems 14.9 percent, a year-over-year increase of 16.1 percent".
  - L18 (domestic energy production, 2023 against 2022): net imports "roughly 70 percent of total energy supply in 2023"; "biofuels and recovered waste energy" "39.1 percent of domestic energy production, a decrease of 2.1 percent"; coal "26.9 percent, a considerable year-over-year decline of 21.8 percent"; renewables "22.5 percent" ("third largest domestic source"); "Renewables grew 8 percent from 2022 to 2023"; other sources "only to the low single digits".
  - L19 (2024 electricity): generation "decreased by 4.2 percent year-over-year in 2024 and totaled to 431.7TWh"; renewables "59 percent of total electricity production, an increase from 56 percent in 2023"; hard coal "fell 31.2 percent"; lignite "dropped 8.8 percent"; "Gas-fired power plant’s share of electricity generation grew 8.9 percent to 56.9 TWh"; wind "about 137.6 TWh", "a share of 31.8 percent of total generation", "again the most important source"; PV "about 63.3 TWh electricity, a 13.6 percent increase from 2023"; "Biomass generated 36.0 TWh"; "hydropower accounted for the vast majority of the remaining 17.2 TWh contributed by renewable sources"; renewables total "about 254.7 TWh in 2024".
  - L20: industrial electricity "around 0.19 USD/kWh in 2024 compared to just 0.08 USD/kWh in the United States in March 2024"; subsidy plans of "around USD 11.3 billion by 2030".
  - L22 (2024 gas): imports "fell to 865 TWh"; "Norway (48 percent) and the Netherlands (25 percent)"; imports "down 11 percent in 2024"; industrial gas consumption "almost 514 TWh, which is 61 percent of total consumption".
  - L23: crude imports "increased from 73 to 78.4 million tons in 2024, a 7 percent year-over-year increase".
  - L24: "In 2024, Germany imported 69TWh of LNG, accounting for about 8 percent of total German gas imports in 2024"; "U.S. LNG now accounts for approximately 90 percent of German LNG imports, the highest share of any European country’s imports"; "As of May 2025, there are four active temporary LNG terminals supplying between 5-12 percent of gas consumed in Germany".
  - L28 (by 2030): renewables "80 percent of electricity production"; onshore wind "planned to double to up to 110 GW"; offshore wind "should reach 30 GW - the capacity of 10 nuclear plants"; solar "planned to triple to 200 GW".
  - L32: by 2045, hydrogen demand "between 360 and 500 TWh, with an additional 200 TWh for hydrogen derivatives".
  - L34: terminals have "a capacity to cover around 17 percent of Germany’s gas needs"; land-based terminals are "planned for 2028"; the economy ministry "expects to cover about half of Russia’s gas imports in 2021"; the core hydrogen network "would modify half of the existing 9700 km gas pipelines".
  - L36: "annual power generation of about 430 TWh and a capacity of about 270 GW"; "More than one thousand market participants".
  - L37: "commitment to build up to 20 GW of new gas-fired power plants by 2030"; "all landing slots at key terminals already booked for 2025".
  - L44: transmission grid "about 37,000 kilometers"; "maximum voltage of 220 kilovolts (kV) or 380 kV"; north-south HVDC lines "planned to be completed by 2027"; "around 14,000 km of new power lines are needed"; "As of early 2025, about 2,200 km of new transmission lines have been approved, of which 1,800 km have been constructed. 1,700 km of lines are expected to be approved in 2025."
  - L45: "an estimated USD 737 billion cost to expand its power grids by 2045".
  - L48 (2023): "Total energy storage capacity installations jumped to 17.7 GWh in 2023, reflecting a 39 percent increase from the previous year"; battery storage "reached 12.1 GWh, a 40 percent increase, accounting for 30 percent of the total installed capacity".
  - L49: PV systems "reached 4.8 million"; cumulative PV "approximately 100 gigawatts in 2024, a year-over-year increase of 15.5 gigawatts"; "Half of the newly installed solar power capacity in 2023 came from the residential segment, marking a 135 percent increase compared to 2022"; "In 2023, every second newly installed residential PV-system is combined with an energy storage system"; "Only 8 percent of rooftop PV systems in Germany are equipped with a battery today – by 2030 it could be well over 80 percent."
  - L50: "The 1.000 MWh project involves building a USD USD 220 million facility" (verbatim: a period as thousands separator and "USD" repeated).
  - L52: "around 94 to 125 TWh of hydrogen will be needed by 2030" (National Hydrogen Council); "50 percent to 70 percent of the required supply will be imported" (German government); 2050 forecasts "between 400 TWh and 800 TWh"; imports "up-to two-thirds of its consumption".
  - L54: "Between 2027 and 2033, the Federal Ministry of Economics expects Germany to import at least 259,000 tons of green ammonia through the H2Global Foundation program."
- Lists:
  - Trade Events, L57-61, 5 items in this order: "E-world energy and water – energy and water industry, Essen, February 10-12, 2026"; "Hannover Messe – industrial, Hannover, April 20 - April 24, 2026"; "The Smarter E Europe and Intersolar – energy transition, Munich, June 23-25, 2026"; "Hydrogen Technology Expo – hydrogen technology, Hamburg, October 21-23, 2025"; last "Enlit Europe – power and energy, Bilbao, November 18-20, 2025". The order is not chronological (the 2026 items come first).
  - Government Links, L63-65, 3 items: BMWE, DENA, last BNetzA.
  - TSOs, L46: 4 items (last TransnetBW).
  - Hydrogen demand drivers, L32: "the steel industry, basic materials, petrochemicals, mobility, logistics, and the power sector" (6 items).
  - Industries the hydrogen strategy aims to decarbonize, L31: "steel, cement, and chemicals".
  - Potential hydrogen suppliers, L53: 4 items.
  - Energiewende tools, L27: expansion of renewable energies, reduction of energy consumption, cessation of fossil fuels. "The two pillars", L28: renewable energy sources and energy efficiency.
  - Pilot grid technologies, L40 ("for example"): superconductors, high-temperature lines, local power transformers.
- Forecasts, guidance, deadlines, effective dates:
  - 80% renewable electricity by 2030. The base wording differs: "electricity supply" (L12), "electricity production" (L28), "electricity consumption" (L45).
  - GHG -65% vs 1990 by 2030 (L12). Neutrality by 2045, against the EU's net zero by 2050 (L12, L30).
  - Coal phase-out by 2038: "planned coal phase-outs in 2038" (L14); "legally mandated by 2038, with this deadline being supported in the new coalition agreement" (L17); "planned by 2038 the latest" (L27); "plans to phase out coal-fired power plants by 2038" (L29).
  - 2030 capacity goals: onshore 110 GW, offshore 30 GW, solar 200 GW (L28).
  - Up to 20 GW of new gas plants by 2030 (L37); HVDC lines by 2027 and 1,700 km of approvals expected in 2025 (L44); grid cost to 2045 (L45).
  - Land-based LNG terminals in 2028 (L34).
  - Hydrogen demand ranges for 2030 and 2050 (L52) and 2045 (L32); H2Global ammonia imports 2027-2033 (L54).
  - Battery-equipped rooftop PV share by 2030 (L49); USD 11.3 billion subsidy by 2030 (L20).
- Dated events; actions vs plans:
  - Actions: the last nuclear plants shut "in April 2023" (L17; "As of April 2023" L27; "The nuclear phase out in 2023" L14; "the shutdown of the last nuclear power plants in 2023" L29). First hydrogen strategy "in 2020, which was updated in July 2023" (L31). European Commission state-aid approval for H2Global "In January 2022" (L54). "In May 2023, Germany agreed to link its H2Global foundation to the European Hydrogen Bank" (L54). Four temporary FSRU terminals operating (L24, L33). 2,200 km of lines approved and 1,800 km built as of early 2025 (L44). "no longer importing any Russian gas directly" (L29).
  - Plans and proposals: coal exit by 2038; land-based terminals in 2028; core hydrogen network ("The previous government also started plans", L34); largest battery park ("there are plans to build", L50); subsidy ("revealed plans to set aside around USD 11.3 billion", L20); blue hydrogen ("“low-carbon” blue hydrogen is planned to be included", L32); "Efforts are underway to secure long-term LNG contracts" (L37).
- Hedged claims (hedge word -> what it attaches to):
  - L14: "two potential sources of instability". "potential" qualifies the instability; "These dependencies have generated" is stated as fact.
  - L14: "are set to increase the country’s reliance on natural gas" (forward-looking, on reliance).
  - L18: "preliminary data from 2024 shows their share continuing to grow quickly". "preliminary" attaches only to the 2024 data; the 2023 shares are firm.
  - L32: "Hydrogen demand is expected to be driven primarily by ..." and "the Ministry of Economy expects hydrogen demand to reach between 360 and 500 TWh" (an attributed expectation). The next sentence, "However, several large energy intensive companies have significantly reduced their production in Germany", is stated as fact.
  - L34: "expects to cover about half of Russia’s gas imports in 2021" (attributed; "about").
  - L40: "Hydrogen is expected to play an important role".
  - L44: "1,700 km of lines are expected to be approved in 2025"; the approved and built counts are firm.
  - L45: "an estimated USD 737 billion cost".
  - L49: "Retrofit storage installations are expected to be a major driver". "by 2030 it could be well over 80 percent": "could" attaches to the 2030 share, while "Only 8 percent ... today" is firm.
  - L52: "expects that around 94 to 125 TWh"; "estimates that 50 percent to 70 percent"; "According to these estimates, Germany’s hydrogen imports will account for up-to two-thirds" (the "will" sits under the attribution).
  - L54: "expects Germany to import at least 259,000 tons".
  - Firm forward statements with no hedge word: L13 "will be necessary" and "energy efficiency will play a key role"; L22 "natural gas will continue to be relevant"; L24 "additional U.S. export capacity will come online"; L37 "will sustain demand for LNG in the medium term". In the same L37 paragraph, "lower-than-expected utilization at some terminals" uses "expected" descriptively.
- Rounded prose beside exact figures:
  - "about 430 TWh" (L36) vs 431.7 TWh (L19).
  - Crude growth "7 percent" (L23) vs 7.4% computed from 73 to 78.4.
  - LNG "about 8 percent" of gas imports (L24) vs 8.0% computed (69/865).
  - "59 percent" (L12, L19) vs 59.0% computed (254.7/431.7).
  - Wind "31.8 percent" (L19) vs 31.9% computed (137.6/431.7).
  - "approximately 90 percent" U.S. LNG share (L24) has no exact counterpart.
- Operative definitions, rules and scope exceptions:
  - L32: the updated hydrogen strategy "includes subsidies for the use, though not the production, of blue hydrogen. The focus will remain on green hydrogen produced from renewables."
  - L36: the Federal Network Agency is "responsible for ensuring non-discriminatory third-party access to the power network". New market actors are those "who do not own power plants or supplier networks".
  - L46: "Demand for control energy is created when the sum of power generated varies from the actual load."
  - L41: smart grids allow "a shift from “consumption-oriented generation” to “generation-optimized consumption.”"
  - L28: the EEG "regulates the renewable electricity sector"; the EEWärmeG "promotes the increase of heat generated from renewable energy in new buildings".
  - L30: the European Climate Law "sets a legally binding target of net zero greenhouse gas emissions by 2050"; "EU Institutions and member states are bound to take the necessary measures".
  - L54: "Initially, H2Global aimed to promote the development of green hydrogen production plants in sunny non-EU countries". The May 2023 link opened "the funding model to all EU member states".
  - L34: the planned terminals "will be ‘hydrogen-ready’ facilities".
- Negative and exclusion statements: "no remarkable incidents of power interruptions thus far" (L15); "no longer importing any Russian gas directly" (L29); "no longer producing any electricity from nuclear power plants" as of April 2023 (L27); non-coal fossil fuels "almost exclusively imported" (L14); blue-hydrogen production excluded from the subsidies (L32); "Germany’s geography limits the development of new pumped storage capacity" (L48).
- Amendments or contradictions (stated neutrally; the document states no precedence):
  - Wind share of 2024 electricity: "27.9 percent of electricity generation" (L17) vs "31.8 percent of total generation" (L19).
  - PV year-over-year growth: "16.1 percent" (L17) vs "a 13.6 percent increase from 2023" (L19). PV share: "14.9 percent" (L17) vs 14.7% computed from 63.3/431.7 (L19).
  - Hydro: "4.5 percent of all gross electricity generation" (L17) vs hydro as "the vast majority of the remaining 17.2 TWh" (L19; 17.2/431.7 = 4.0% computed). L17 says "gross" and L19 says "total".
  - Renewable generation parts (L19): 137.6 + 63.3 + 36.0 + 17.2 = 254.1 TWh computed, vs the stated total "about 254.7 TWh".
  - Fossil share (L17): 36.1 + 25.9 + 7.3 + 7.6 = 76.9% computed, vs "more than 77 percent".
  - Battery storage (L48): 12.1 GWh of 17.7 GWh is 68.4% computed, vs "accounting for 30 percent of the total installed capacity".
  - LNG measures differ: terminals "supplying between 5-12 percent of gas consumed" as of May 2025 (L24); "capacity to cover around 17 percent of Germany’s gas needs" (L34); 2024 LNG at "about 8 percent of total German gas imports" (L24). These are a supply share, a capacity share and an import share.
  - Solar: "planned to triple to 200 GW" by 2030 (L28) vs cumulative PV of "approximately 100 gigawatts in 2024" (L49). The base for "triple" is not stated.
  - Hydrogen sequence: strategy adopted 2020 and updated July 2023 (L31); the H2Global/European Hydrogen Bank link came in May 2023 (L54), before that update.
- Notes: "Germany is Europe’s largest electricity market" (L36); "the largest energy consumer in the European Union followed by France and Italy" (L10); "a global leader in energy storage technology" and "the European lead target market" (L48); "one of the lowest power interruption rates worldwide" (L15). Verbatim typos: "higher in prices" (L20), "Liquified" (L24), "an import role" (L50).
- Coverage: full. Read ledger: L1-67 in one chunk (offset 1), with the tail L64-67 re-read. Unread: none. Missing text: none.

---

## D07 - Indonesia Country Commercial Guide: Energy; Environmental Technology

- Source: `text/D07.txt` (144 lines; 13,208 chars) from `docs/ccg_energy_cleantech_sectors_indonesia.txt`. No pages.
- Written or submitted by: ITA (L3 "Indonesia Country Commercial Guide (U.S. International Trade Administration)"). Contacts: "Commercial Specialist Ari Febriana at Ari.Febriana@trade.gov" (Energy, L96) and "Commercial Specialist Trianie Ananda at Trianie.Ananda@trade.gov" (Environmental Technology, L142). Named data sources, which are not authors: Global Trade Atlas and the World Bank (exchange rate) at L66, L103 and L115; a Ministry of Environment estimate at L124.
- Type, date, edition: two chapters:
  - "## Energy" (L5); "Last published: 2025-11-17" (L6); "Source: https://www.trade.gov/country-commercial-guides/indonesia-energy" (L7).
  - "## Environmental Technology" (L98); "Last published: 2025-11-17" (L99); "Source: https://www.trade.gov/country-commercial-guides/indonesia-environmental-technology" (L100).
- Period covered: the tables give 2020-2024 actuals plus "2025 (est.)". Prose covers 2022-2025 (end-2024 capacity, 2024 waste, the 2024 and 2025 block rounds). Targets run 2027-2060. Fiscal/calendar convention: not stated.
- Section headings in order:
  - Energy: "Overview" L9; table L10-66; "Indonesia’s Energy Sector" L68; "Leading Sub-sectors" L80; "Opportunities" L86; "Resources" L92.
  - Environmental Technology: "Overview" L102; table L103-115; "Indonesia’s Environmental Sector" L117; "Leading Sub-sectors" L120; "Opportunities" L129; "Events" L133; "Resources" L139; separator L144.
- Tables:
  - **Table 1, L10-66** (Energy). Title: "Table: total Market Size for Energy, Unit: USD Millions" (L10). Column header L12-17: "2020 |", "2021 |", "2022 |", "2023 |", "2024 |", "2025 (est.)". Layout: a row-label line, then one value per line in year order. Values are whole numbers with thousands commas. Columns are 2020 | 2021 | 2022 | 2023 | 2024 | 2025 (est.):
    - "Total Exports" (label L19, values L20-25): 30,062 | 50,860 | 82,216 | 68,298 | 68,768 | 64,500
    - "Total Imports" (L27; L28-33): 23,860 | 40,613 | 55,854 | 49,817 | 49,646 | 55,800
    - "Export to U.S." (L35; L36-41): 329 | 377 | 388 | 279 | 471 | 435
    - "Imports from the U.S." (L43; L44-49): 1,398 | 2,872 | 2,788 | 2,647 | 3,338 | 3,820
    - "Trade Surplus/Deficit" (L51; L52-57): (1,069) | (2,495) | (2,400) | (2,368) | (2,867) | (3,385)
    - "Exchange Rate" (L59; L60-65): 14,582 | 14,308 | 14,850 | 15,237 | 15,855 | N/A
    - Source line L66: "Data Sources: Global Trade Atlas. Average exchange rate of Indonesian rupiah to U.S. dollars from the World Bank."
    - Table notes: despite the title there is no "Total Local Production" or "Total Market Size" row. Parentheses mark negatives. No HS code or product scope is stated. Per the source line, the exchange-rate row is rupiah per U.S. dollar, unscaled.
    - Computed: every "Trade Surplus/Deficit" value equals "Export to U.S." minus "Imports from the U.S." for the same year (2024: 471 - 3,338 = -2,867; 2025 est.: 435 - 3,820 = -3,385). It does not equal Total Exports minus Total Imports (2024: +19,122 computed).
  - **Table 2, L103-115** (Environmental Technology). Title line as extracted: "Table: Average exchange rate of Indonesian Rupiahs to U.S. dollars from the World Bank, Unit: USD millions 2020 2021 2022 |" (L103). The header continues "2023" (L104), "2024 |" (L105), "2025 (est.)" (L106). Rows are in pipe form with six values each, in the order 2020 | 2021 | 2022 | 2023 | 2024 | 2025 (est.):
    - "Total Exports" L108: 1,139 | 1,383 | 1,170 | 1,556 | 1,700 | 1,810
    - "Total Imports" L109: 5,083 | 6,035 | 7,776 | 7,448 | 8,236 | 8,700
    - "Export to the U.S." L110: 124 | 177 | 207 | 202 | 276 | 300
    - "Imports from the U.S." L111: 357 | 369 | 450 | 457 | 494 | 520
    - "Trade Surplus/Deficit" L112: (233) | (192) | (243) | (255) | (218) | (220)
    - "Exchange Rate" L113: 14,582 | 14,308 | 14,850 | 15,237 | 15,855 | N/A
    - Source line L115: "Source: Global Trade Atlas (GTA)".
    - Table notes: the title line is the exchange-rate source caption, not a sector title. The sector is given only by the section heading (L98). The year header is split over L103-106 (the original is laid out the same way), but each row has six values, matching the six year labels in order.
    - Computed: "Trade Surplus/Deficit" = "Export to the U.S." minus "Imports from the U.S." in all six columns (2024: 276 - 494 = -218).
    - The Exchange Rate row is identical to Table 1's. The row labels differ: "Export to the U.S." (Table 2) vs "Export to U.S." (Table 1).
  - No prose restates any table value.
- Quantitative figures in prose:
  - L69: coal is "accounting for approximately 61% of the national energy mix", in a sentence framing it as "the dominant source for electricity generation". Natural gas is "approximately 20%"; "the remaining share comes from renewable energy sources" (no figure given).
  - L70: "As of the end of 2024, Indonesia’s total installed power generation capacity reached approximately 101 GW", with coal "contributing the majority share".
  - L71: "the United States supplies around 60 percent of Indonesia’s LPG".
  - L72: U.S. crude imports "presently constitute about 4% of Indonesia’s total oil and gas imports".
  - L73: Pertamina "covers approximately 55–60% of Indonesia’s total energy supply", "manages over 90% of fuel distribution and has a near-monopoly on LPG and fuel importation".
  - L74: "auctioned 11 oil and gas blocks in 2024 and launched an additional 3 blocks in 2025, with a total potential of 2.2 billion barrels of oil equivalent (BOE) from the 2025 blocks alone"; "plan to offer 60 blocks between 2024-2028"; "boosting production from 600,000 BOE/day to 1 million BOE/day by 2030"; "reactivate over 4,000 identified idle wells".
  - L76: carbon market regulations planned for 2025; "Implementation is expected to begin in 2027"; "15 potential CCS/CCUS projects have already been identified".
  - L78: "geothermal energy potential of 23 GW, but as of 2024, only 2,597 MW (11%) has been developed".
  - L79: nuclear "by 2032, starting with up to two 250 MW plants"; the RUPTL covers "2024-2035".
  - L88: "The government’s plan to add 35 GW of new power generation capacity" (no target year).
  - L118: the 2022 NDC update commits to "reduce greenhouse gas emissions by 32 percent by 2030 and to achieve net-zero emissions by 2060" (no base year stated).
  - L119: "ranks among the top 20 most polluted globally".
  - L122: "In 2024, Indonesia generated approximately 34.2 million tons of waste across 317 districts and cities"; food waste "about 39.26%"; goal of "100% waste management by 2029".
  - L124: "transportation contributes 44% and industry 31% of Jakarta’s pollution" (Ministry of Environment estimate).
  - L126: "In 2023, the country hosted its inaugural International Battery Summit, which has since become an annual event".
  - L128: "More than 80% of the population lacks access to piped water".
- Lists:
  - Energy "Leading Sub-sectors", L82-85, 4 items: Power Generation Equipment; Transmission and Distribution; Smart Grid Solutions; last "Oil, Gas and Geothermal Infrastructure".
  - Energy "Opportunities", L88-91, 4 items: Infrastructure Development; Oil and Gas Exploration; Energy Equipment Imports; last "Technical Training and Services".
  - Sectors targeted by the carbon market, L76, 6 items: cement, steel, textiles, food and beverages, chemicals, fertilizers.
  - Underexplored gas regions, L74: "Sulawesi, Maluku, and Jayapura region".
  - Energy "Resources", L93-95, run together (the item split below is the mapper's parse):
    1. Ministry of Energy and Mineral Resources ESDM
    2. Directorate General of Electricity (ESDM-Electricity Directorate)
    3. Directorate General of New & Renewable and Energy Conservation (ESDM-New Renewable Energy Directorate)
    4. Special Task Force for Upstream Oil and Gas Business Activities (SKK Migas)
    5. PLN
    6. APLSI (Indonesia Independent Power Producer Association)
    7. Indonesia Petroleum Association Convention and Exhibition
    8. Global Hydrogen Ecosystem Summit & Exhibition 2025
    9. Last: "11th IndoGAS Conference & Exhibition" (L95)
  - Environmental "Leading Sub-sectors", L122-128, 4 items: Waste Management; Air and Industrial Pollution; Sustainable Batteries and Recycling; last "Water and Sanitation".
  - Environmental "Opportunities", L131-132, run together (the mapper's parse gives 6): Smart, modular, or off-grid water purification and recycling systems; Waste sorting and composting technologies; Battery recycling systems and lithium recovery technologies; Emission control and real-time environmental monitoring solutions; Air-to-water generators and eco-friendly chemicals for water treatment; last "AI or Satellite fire detector technology".
  - "Events", L134-138, 5 items: WEFTEC The Water Quality Event 2025; ENLIT Asia 2025; International Battery Summit 2025; Plastic Recycling World North America; last "Water Quality Technology Conference".
  - Environmental "Resources", L140-141, run together: U.S. Commercial Service - Indonesia (CS Indonesia); Industry and Analysis, Office of Supply Chain, Professional & Business Services ("US Trade"); Indonesia Chamber of Commerce / KADIN (Kamar Dagang Indonesia); last Ministry of Environment.
  - Other short lists:
    - Air-pollution opportunities, L124 (5): emission monitoring systems, industrial dust control, desulfurization technologies, air pollution control technologies, IoT-based pollution and fire sensors.
    - Water demand, L128 (4): decentralized water treatment, filtration systems, sludge removal, solar-powered atmospheric water generation.
    - Establishments required to run waste programs, L122: "malls, hotels, and restaurants".
- Entities and aliases:
  - "PT Perusahaan Listrik Negara (PLN)", "The state-owned electricity company" (L70); "State-owned electric company - PT Perusahaan Listrik Negara PLN" (L94).
  - "Pertamina, Indonesia’s state-owned oil and gas company" (L73).
  - The Ministry of Energy and Mineral Resources is abbreviated two ways: "(EMR)" at L77, and "ESDM" at L78 ("Ministerial Regulation ESDM No. 11/2024"), L93 and L94. Its minister is "Bahlil Lahadalia" (L72).
  - "The Ministry of Industry" (L76; carbon market regulations) is a different ministry from EMR/ESDM.
  - "Ministry of Environment" (L124, L141).
  - "Special Task Force for Upstream Oil and Gas Business Activities (SKK Migas)" and "APLSI (Indonesia Independent Power Producer Association)" (L94).
  - "KADIN (Kamar Dagang Indonesia)" = Indonesia Chamber of Commerce (L141).
  - "2024-2035 National’s Electricity Supply Business Plan (RUPTL)" (L79).
  - Regulations: "Ministry of Energy and Mineral Resources (EMR) Regulation No. 16/2024" and "Presidential Regulation No. 14/2024" (L77); "Ministerial Regulation ESDM No. 11/2024" (L78), which mandates "TKDN compliance" (TKDN is not expanded).
  - Abbreviations: NRE "new and renewable energy" (L73); BOE (L74); EOR (L74); CCS/CCUS (L76, L77, L90); LPG (L71); NDC (L118).
  - Places: "Aceh Island to Sumatra and Java" (pipeline network, L75); Sulawesi, Maluku, Jayapura (L74); Sumatra and Kalimantan (forest fires, L119); Jakarta (L122, L124).
  - Events: International Battery Summit (L126, L136); ENLIT Asia 2025 (L135); WEFTEC (L134).
- Forecasts, guidance, deadlines, effective dates:
  - Oil and gas: 60 blocks offered 2024-2028; 1 million BOE/day by 2030, a target Indonesia "has long articulated" (L74).
  - Carbon market: regulations to be released in 2025, with "Implementation ... expected to begin in 2027" (L76).
  - Power: nuclear in the energy mix by 2032 (L79); 35 GW of new capacity, no year (L88).
  - Environment: GHG -32% by 2030 and net zero by 2060 (L118); 100% waste management by 2029 (L122).
  - Tables: "2025 (est.)" columns.
- Dated events; actions vs plans:
  - Actions: 11 blocks auctioned in 2024 and 3 launched in 2025 (L74). EMR Regulation No. 16/2024 and Presidential Regulation No. 14/2024 "have been issued" (L77); ESDM No. 11/2024 was "issued" (L78). Nuclear "officially included" in the 2024-2035 RUPTL (L79). NDC "updated" in 2022 (L118). Inaugural battery summit in 2023 (L126). "the first privately owned large-scale waste-to-energy plant is under construction" (L122).
  - Plans and intent: "expressed its intent to increase imports of U.S. energy commodities" (L71; restated at L90 as "Indonesia plans to increase imports of U.S. energy commodities"). "highlighted plans to boost the proportion of U.S. crude oil imports" (L72). "aims to enhance its integrated gas infrastructure by developing a pipeline network" (L75). The Ministry of Industry "plans to release carbon market regulations in 2025" (L76).
- Hedged claims:
  - "approximately" on the coal and gas shares (L69) and on capacity (L70).
  - L76: "Implementation is expected to begin in 2027". "expected" attaches to the start date; "This regulatory shift will drive demand for Carbon Capture and Storage (CCS) technologies" is firm.
  - L79: "aims to integrate nuclear ... by 2032".
  - "potential" in "total potential of 2.2 billion barrels" (L74) describes the resource. In "15 potential CCS/CCUS projects" (L76) it describes the projects.
  - Firm statements: L90 "will play a critical role"; L119 "Although Indonesia’s ranking fluctuates, it remains high".
- Rounded prose beside exact figures: "2,597 MW (11%)" of 23 GW (L78) vs 11.3% computed. No prose duplicates a table value.
- Operative definitions, rules and scope exceptions:
  - L77: the regulations "govern the implementation of carbon storage activities within licensed carbon storage areas", "enable private sector participation in carbon capture and storage (CCS) projects and allow them to propose designated CCS areas".
  - L78: TKDN compliance is mandated "for all new geothermal and other electricity infrastructure projects".
  - L122: "Regulatory frameworks require commercial establishments—such as malls, hotels, and restaurants—to implement waste management programs".
- Negative and exclusion statements: "Tap water is not safe to drink and water recycling is not yet regulated" (L128); the 2025 exchange rate is "N/A" in both tables (L65, L113).
- Amendments or contradictions (no precedence stated):
  - One ministry name carries two abbreviations: EMR (L77) and ESDM (L78, L93-94).
  - Table 2's title line is the exchange-rate caption (L103).
  - The "Trade Surplus/Deficit" rows behave as a bilateral U.S. balance (computed), not a total balance.
  - L69: "approximately 61% of the national energy mix" sits in a sentence about electricity generation, so the base is ambiguous.
  - L118: the NDC was "updated" in 2022; the earlier values are not stated.
  - L78: the TKDN mandate is framed as both "To attract more foreign investment in the sector" and "to stimulate local industry and retain economic benefits within Indonesia".
- Notes: verbatim phrasings: "pipeline network connecting Aceh Island to Sumatra and Java" (L75); "horizontal drilling (fracking)" (L74).
- Coverage: full. Read ledger: L1-144 in one chunk (offset 1), with the tail L140-144 re-read. Unread: none. Missing text: none.

---

## D08 - Israel Country Commercial Guide: Energy; Environmental Technologies

- Source: `text/D08.txt` (87 lines; 22,522 chars) from `docs/ccg_energy_cleantech_sectors_israel.txt`. No pages.
- Written or submitted by: ITA (L3). Contacts: "Commercial Specialist Naama Myers-Altman at Naama.Altman@trade.gov" (Energy, L47) and "Commercial Assistant Alla Polotsky at Alla.Polotsky@trade.gov" (Environmental Technologies, L85). Bodies cited, which are not authors:
  - Electricity Authority (L14)
  - the energy ministry and minister (L16, L18, L29)
  - MOEP (L55, L56, L71, L72)
  - Water Authority (L62)
  - Israeli government decisions (L20, L32, L56)
- Type, date, edition:
  - "## Energy" (L5); "Last published: 2026-03-17" (L6); "Source: https://www.trade.gov/country-commercial-guides/israel-energy" (L7).
  - "## Environmental Technologies" (L49); "Last published: 2026-03-11" (L50); "Source: https://www.trade.gov/country-commercial-guides/israel-environmental-technologies" (L51).
  - The two chapters of this one document carry different publish dates.
- Period covered: actuals span 2000-2025 (2023 capacity, gas and renewables; 2024 exports; March 2025 Sorek B; August 2025 Leviathan deal). Targets run 2026-2075. Fiscal/calendar convention: not stated. "Q4 2025" quarter labels (L37, L38, L40) are not defined.
  - Forward-looking items dated before the publish dates, with no later status given: "PQ anticipated in Q4 2025" (L37, L38, L40); "expected to be brought forward for approval later in 2025" (L62); "pre-qualification phase expected to open later in 2025" (L65); "pre-qualification phase anticipated in 2025–2026" (L73).
- Section headings in order:
  - Energy: "Overview" L9; "Electricity Infrastructure" L11; "Natural Gas" L15; "Renewable Energy" L19; "Leading Sub-sectors" L21; "Opportunities" L23, with sub-headings "Electricity Infrastructure" L24, "Natural Gas" L28 and "Renewable Energy" L31; "Energy Infrastructure Projects" L35; "Resources" L41.
  - Environmental Technologies: "Overview" L53; "Leading Sub-sectors" L57; "Opportunities" L60, with "Water" L61 and "Recycling" L70; "Environmental Infrastructure Projects" L74; "R&D" L76; "Resources" L78; separator L87.
- Tables: none (not applicable).
- Quantitative figures in prose:
  - L10: "In 2040, 13.2 million people are expected to live in Israel (in comparison to 9.8 million in 2023) and electricity demand will double".
  - L12: demand "has grown by an average of 3% annually between 2010-2020".
  - L14: "Overall installed capacity in 2023 totaled 23.7 GW, with parastatal company Israel Electric Corporation (IEC) accounting for 56% of production". Per the Electricity Authority, "installed capacity will reach 39.6 GW in 2030 (67% increase)". The reform dates from "June 2018" and runs "over the course of 8 years (2018-2026)".
  - L16: coal "accounted for only 17% of Israel’s power in 2023 compared with 52% in 2013". The 2030 goal is "70% use of natural gas and 30% renewables". The gasoline-car import ban starts "in 2030". Gas consumption "has reached 13.1 billion cubic meters (bcm) in 2023 (a 3.5% increase from 2022.)"; the electricity sector accounts for "79% (10.4 bcm) of generation sources".
  - L17: Tamar was discovered in 2009. Leviathan "started production in late 2019" with "contingent resources totaling 605 bcm" ("almost double the size of Tamar and approximately two thirds of the gas discovered to date offshore Israel"). "In 2021, Leviathan surpassed Tamar and provided more than 50% of Israel’s natural gas". Karish began production "in October 2022"; "block D (awarded in 2019)"; blocks A and C were awarded "in 2019".
  - L18: "In 2024, it represented 49% of total consumption, an all-time record" ("it" = the gas export market). Exports in 2024 "increased by 13.2% compared to 2023"; exports to Egypt "grew by 16%" and "to/via Jordan grew by 6%". Planned: "increase gas exports from the Tamar field to Egypt by 60% starting in 2026". "In August 2025", Leviathan signed an export agreement "worth up to $35 billion".
  - L20 (with a near-duplicate at L32):
    - Renewables were "only 12.5%" of electricity in 2023.
    - July 2021 GHG update: "27% decrease ... by 2030, using 2015 as the base year". Emissions from electricity generation are to fall "by 30%" on the same base.
    - Renewable energy targets: "30% of electricity ... by 2030". Solar is "approximately 90%" of the renewable electricity; "wind, water and biomass will provide the remaining 10%".
    - Solar capacity must reach "17.1 GW (almost 3.5 times of its capacity in 2022– 4.7 GW)".
    - Storage must rise "by 10 times from 300 MW in 2020 to approximately 3,000 MW in 2030".
  - L25: IEC is "the second largest procurement organization in Israel, with 5,000 active suppliers worldwide".
  - L26: "IEC’s five-year (2022-2026) procurement plan totals more than $2.5b".
  - L29: "It is anticipated that by 2040, Israel will need to construct at least 13 new gas-based power plants."
  - L30: "The fourth offshore bid round concluded in July 2023. A fifth offshore bid round is planned but no date has been announced."
  - L37-40: projects (see Lists).
  - L54: desalination provides "approximately 80% of its water consumption"; wastewater reclaimed "about 90%".
  - L55 (restated at L71): "approximately 80% of its waste being sent to landfill, and only 20% to recycling". 2030 goals: "recycle 54% of the waste (compared to 20% in 2020)", sorting facilities "that will process 100% of the waste", and "reducing landfill disposal to 20% (from 80% in 2020)". Circular economy "by 2050". The MOEP announced the plan "in 2021".
  - L56: solid-waste GHG "by 47% until 2030, and by 92% until 2050, using 2015 as the base year"; "reduction of 71% in municipal solid waste sent to landfill by 2030, compared to 2018".
  - L62: Water Authority plan released "In February 2025"; "currently pending government approval".
  - L63: the plan builds on "the 2018 national strategic water plan, which was developed in response to a five-year drought".
  - L65, desalination:
    - Emek Hefer "is expected to add 400 million cubic meters (MCM) of capacity"; the Ashkelon expansion adds "another 220 MCM".
    - Total annual capacity will rise "from 587 MCM in 2023 to more than 1200 MCM".
    - Required desalinated water: "2,000 MCM" by 2050 and "3,200 MCM" by 2075.
    - Sorek B "(awarded in 2020) began operations in March 2025, adding 200 MCM"; Western Galilee is "expected to begin operations in early 2027, contributing an additional 100 MCM".
  - L66: projects connecting the Western Galilee plant are "valued at $144-300 million".
  - L67: "Approximately 400 wells are planned by 2050, with a total estimated value of $797 million."
  - L72: "7-10 new sorting facilities" are needed for dry recyclable waste ("about 39% of total waste"), in addition to "the five facilities already operating, and the six facilities that are under development". Organic waste "constitutes 43% of total waste".
  - L73: Neot Hovav "began construction in 2025 and is expected to process 300,000 tons of waste annually, with the option to expand capacity to 500,000 tons". Two more facilities, in Jerusalem and southern Israel, are planned, "each designed to treat 650,000 tons of waste per year".
  - L75: Infrastructure for Growth covers projects "valued at more than 100 million shekels (~$30 million)". "The 2025 workplan includes 270 projects, valued at $151 billion in total".
- Lists:
  - "Energy Infrastructure Projects", L37-40, 4 items (intro L36: "Some of the notable energy infrastructure projects in the pipeline include:"):
    1. "“Yavor” LPG Storage facility of 20,000-ton capacity. PQ anticipated in Q4 2025."
    2. "The Jerusalem Region Waste-to-Energy facility of 650k tons annually. PQ anticipated in Q4 2025."
    3. "The Tamar Region Waste-to-Energy facility of 650k tons annually. PQ anticipated in 2026."
    4. Last: "The Emek Hefer Desalination facility of 400 MCM per annum, with an adjacent CCGT power plant of 300 MW. PQ anticipated in Q4 2025."
  - IEC procurement categories, L26 (8 named): transformers, switchgear, protection systems, zero-point earthing equipment, D.C. equipment, power cables, towers, insulators "and more".
  - Energy leading sub-sectors, L22: "Electricity Infrastructure, Natural Gas, and Renewable Energy (including Energy Storage)".
  - Renewable opportunities, L33: (a) suppliers of PV, wind and storage; (b) suppliers of transmission and distribution equipment; (c) IPPs.
  - Factors "often cited" for the renewables shortfall, L20 (4): "Bureaucratic bottlenecks, limited land resources, underdeveloped transmission infrastructure from remote generation sites, and recent discoveries of offshore gas that can produce electricity at a lower cost than solar".
  - Dual-use solar projects, L32: "rooftops, water reservoirs, agrovoltaic, and more".
  - Energy "Resources", L42-45, 4 items: Israel Electric Corp.; Ministry of Energy and Infrastructure; Israel Natural Gas Lines; last BIRD Foundation.
  - Environmental leading sub-sectors, L58 (3): "Water Infrastructure, Groundwater Treatment, and Waste Treatment and Recycling". L59 lists 4 services.
  - Water-sector components, L65-69, 5 items: Desalination; Connecting to the national water conduit system; Turnkey well-drilling projects; Domestic and regional water infrastructure upgrades; last "Other opportunities".
  - Environmental "Resources", L79-84, 6 items: Ministry of Energy - Water; Water Authority; Mekorot; Ministry of Environmental Protection; Infrastructure for Growth 2025; last BIRD Foundation.
  - Desalination plants named at L65:
    - Emek Hefer: planned, 400 MCM
    - Ashkelon: expansion, 220 MCM
    - Sorek B: operating since March 2025, 200 MCM
    - Western Galilee: under construction, 100 MCM
    - L68 adds an unnamed "large desalination plant on the Mediterranean coast".
  - Gas fields and blocks, L17: Tamar, Leviathan, Karish, Tanin, block D, Katlan (Olympus), blocks A and C.
- Entities and aliases:
  - "Israel Electric Corporation (IEC)": "parastatal company" and "the sole vertically integrated electric utility company in Israel" (L14); "Israel’s state-owned electricity utility company" (L25); "Israel Electric Corp." (L42).
  - Energy-ministry name variants: "The Israeli Ministry of Energy’s 2030 goal" (L16); "the Minister of Energy" (L18); "the Ministry of Energy" (L29); "Ministry of Energy and Infrastructure" (L43); "Ministry of Energy - Water" (L79).
  - Other bodies:
    - "the Electricity Authority" (L14)
    - "the Israeli Ministry of Finance" (leads the PPP projects, L36)
    - "Ministry of Environmental Protection (MOEP)" (L55, L71, L82)
    - "Israel’s Water Authority" (L62, L68, L80)
    - "Mekorot" (L81)
    - "Israel Natural Gas Lines" (L44)
    - "The BIRD Foundation" (L34, L45, L77, L84)
  - Companies: "U.S. company Noble Energy (acquired by Chevron in 2020)"; Chevron; "Greek company Energean"; "British companies Cairn and Pharos" (all L17).
  - "the Katlan deposit (also known as Olympus)" (L17).
  - "Tamar" names two different things: the gas field (L17, L18) and "The Tamar Region Waste-to-Energy facility" (L39).
  - Waste-to-energy plant naming differs between chapters. The Energy chapter has "Jerusalem Region" and "Tamar Region" plants (L38-39). The Environmental chapter has "one in Jerusalem and another in southern Israel" (L73). The text does not explicitly link "Tamar Region" with "southern Israel".
  - Regional links: "Cyprus and Greece (The Great Sea Interconnector)" (L13); "Jordanian/Palestinian/Israeli cooperation to create a water and renewable energy exchange (Project Prosperity)" (L13); "the “Project Prosperity” agreement" for water sales to Jordan (L68).
  - "the multi-year Infrastructure for Growth workplan" (L75) / "Infrastructure for Growth 2025" (L83).
  - Abbreviations:
    - OECD (L10)
    - IPPs (L14, L22, L26, L33)
    - "IOC’s" (L17)
    - bcm (L16); MCM (L65)
    - PQ (not expanded; the pre-qualification wording appears at L27 "pre-qualify", L65 and L73)
    - CCGT (L40, not expanded)
    - PPP (L36, L75)
    - WTO/GPA (L27); GHG (L20)
- Forecasts, guidance, deadlines, effective dates:
  - Demand and capacity: 2040 population and the doubling of electricity demand (L10); 39.6 GW in 2030 (L14); the 2018-2026 reform (L14, L26).
  - Electricity mix: 2030 goal of 70% gas and 30% renewables with coal plants shut (L16); renewables 30%, 17.1 GW solar and about 3,000 MW storage by 2030 (L20, L32); at least 13 gas plants by 2040 (L29).
  - Gas and transport: Tamar-to-Egypt exports +60% from 2026 (L18); gasoline-car import ban from 2030 (L16).
  - Emissions and waste: GHG -27% by 2030 (L20, L56) and electricity GHG -30% (L20); waste targets for 2030 and 2050 (L55, L56, L71).
  - Infrastructure: PQ dates (L37-40); desalination milestones in 2027, 2050 and 2075 (L65); wells by 2050 (L67).
- Dated events; actions vs plans:
  - Actions:
    - First commercial gas discovery in 2000 (L16); Tamar found in 2009 (L17).
    - Block D and blocks A and C awarded in 2019; Leviathan production from late 2019 (L17).
    - Noble acquired by Chevron in 2020; Leviathan overtook Tamar in 2021; Karish production from October 2022 (L17).
    - June 2018 electricity reform: "approved" (L14), "initiated" (L26).
    - Renewable energy decision of October 2020 (L32; "from 2020" at L20).
    - July 2021 GHG update (L20, L56); MOEP plan in 2021 (L55).
    - Fourth bid round concluded in July 2023 (L30).
    - Water Authority plan released in February 2025 (L62).
    - Sorek B, awarded in 2020, operating from March 2025 (L65); Neot Hovav construction began in 2025 (L73).
    - Leviathan export agreement in August 2025 (L18).
  - Plans: fifth bid round (no date, L30); Tamar export increase from 2026 (announced, L18); Water Authority plan pending approval (L62); pre-qualifications for the waste-to-energy and desalination projects.
- Hedged claims:
  - L10: "13.2 million people are expected to live in Israel". "expected" governs the population; "electricity demand will double" uses an unhedged "will".
  - L12: "is expected to face significant challenges".
  - L14: "According to the Electricity Authority, installed capacity will reach 39.6 GW in 2030" (attribution).
  - L20: the factors "are often cited as factors explaining the lower-than-expected use of renewable energy". "often cited" attaches to the causal explanation; the shortfall and the 12.5% are firm.
  - L29: "It is anticipated that by 2040".
  - L37-40: "PQ anticipated".
  - L55: "the Ministry of Environmental Protection (MOEP) cautions that Israel is quickly approaching full capacity of its current landfills".
  - L62: "is expected to be brought forward for approval later in 2025".
  - L65: "is expected to add 400 million cubic meters"; "is projected to reach"; "is expected to begin operations in early 2027".
  - L72: "MOEP estimates that 7-10 new sorting facilities will be required".
  - L73: "is expected to process 300,000 tons".
- Rounded prose beside exact figures:
  - "39.6 GW in 2030 (67% increase)" vs 67.1% computed from 23.7 GW.
  - "79% (10.4 bcm)" vs 79.4% computed (10.4/13.1).
  - "almost 3.5 times" vs 3.64 computed (17.1/4.7).
  - "more than 1200 MCM" vs 1,207 computed (587 + 400 + 220).
  - "650k tons" (L38-39) vs "650,000 tons" (L73).
  - "100 million shekels (~$30 million)" (L75).
- Operative definitions, rules and scope exceptions:
  - L27: IEC "is bound by Israel’s WTO/GPA agreement concerning public tender procedures. While some projects are tendered out in open tender procedures, in most cases, a selective tendering process requires potential suppliers to pre-qualify to be included in IEC’s approved suppliers’ list."
  - L16: all coal plants are to shut "while ... retaining some generation capabilities for events of emergency".
  - L14 and L26: IEC "will retain a monopoly" / "retains a monopoly in the transmission and distribution segments".
  - L75: the workplan covers "all projects valued at more than 100 million shekels (~$30 million) that are either in progress, budgeted or approved by the government".
  - L29: "the Ministry of Energy is issuing licenses for small scale, gas-based generation sites for industrial plants".
  - L72: dry waste that cannot be recycled "will be transferred to energy recovery facilities where possible, or otherwise landfilled".
- Negative and exclusion statements: the grid "is not connected to the systems of neighboring countries" (L12); "no date has been announced" for the fifth bid round (L30); the water plan is "currently pending government approval" (L62); waste treatment is "a situation that has seen little improvement over the past two decades" (L55).
- Amendments or contradictions (no precedence stated):
  - The June 2018 reform is "approved" (L14) vs "initiated" (L26). L14 says "8 years (2018-2026)"; L26 says "planned to be concluded in 2026".
  - L20 has "An earlier government decision from 2020" and "To reach this new goal"; L32 has "A Government of Israel decision from October 2020" and "To reach this goal". The figures are otherwise the same.
  - BIRD "publishes new calls for proposals regularly" (L34) vs "normally publishes new calls for proposals annually" (L77).
  - The July 2021 update of the 2015 GHG goal (L20, L56) does not state the earlier value.
  - Emek Hefer: "PQ anticipated in Q4 2025" (L40) vs "pre-qualification phase expected to open later in 2025" (L65).
  - Waste-to-energy pre-qualification: Jerusalem in Q4 2025 and Tamar Region in 2026 (L38-39), vs both "anticipated in 2025–2026" (L73).
  - The landfill targets use different bases: a share, "to 20% (from 80% in 2020)" (L55, L71), vs a volume reduction, "reduction of 71% in municipal solid waste sent to landfill by 2030, compared to 2018" (L56).
  - Desalination totals: 587 + 400 + 220 = 1,207 MCM computed, vs "more than 1200 MCM". Sorek B (200 MCM, from March 2025) and Western Galilee (100 MCM, from 2027) are stated separately; the text does not say whether they are in the 1200 figure.
- Notes: L14 places IEC's "56% of production" in a sentence about installed capacity. L18 "it" refers back to "the export market for natural gas produced in Israel". Verbatim typo: "draught" (L54).
- Coverage: full. Read ledger: L1-87 in one chunk (offset 1), with the tail L84-87 re-read. Unread: none. Missing text: none.

---

## D09 - Mauritius Country Commercial Guide: Energy

- Source: `text/D09.txt` (124 lines; 23,215 chars) from `docs/ccg_energy_cleantech_sectors_mauritius.txt`. No pages.
- Written or submitted by: ITA (L3). There is no commercial-specialist contact. Statistics are attributed to "the CareEdge Ratings Africa Report" (L15) and "*Source: Statistics Mauritius, January 2025 CareEdge Ratings Report" (L23). The Resources preface is written in the first person: "While I cannot provide hyperlinks directly, I can guide you to the official websites or organizations where you can find relevant information" (L93). It is recorded here as document text (data).
- Type, date, edition: one chapter, "## Energy" (L5); "Last published: 2026-02-19" (L6); "Source: https://www.trade.gov/country-commercial-guides/mauritius-energy" (L7).
- Period covered:
  - Actuals span 2013-2025: 2023 and 2024 energy statistics, October 2024 vehicle registrations, and 2025 budget, tenders and construction starts. Targets run 2026-2030.
  - Budget labels: "2025-2026" (L13, L87) and "2023/2024" (L87); "over three years (2024-2027)" (L72).
  - Seasons: summer peak "from December to February" (L12); sugarcane harvest "from June to November", with imported coal "from December to May" (L11).
  - Forward-looking items dated before the publish date, with no later status given: "100 MW of capacity by January 2026" (L14); Stor'Sun 3 and 4 "set to commence in August and September 2025" (L74); LNG feasibility "by 2025" (L79).
- Section headings in order:
  - "Overview" L9.
  - "Key Statistics* per the CareEdge Ratings Africa Report:" L15, with run-in labels "Import Dependency:" L16, "Energy Consumption:" L18, "Electricity Generation:" L20 and "Transport Sector Energy Use:" L22; footnote L23.
  - "Highlights of the Renewable Energy Strategic Plan (RESP) 2025–2030" L24 (pillars at L26, L31, L35, L40).
  - "Leading Sub-sectors" L43 (groups at L44, L51, L55, L59, L63, L66).
  - "Market Opportunities for U.S. Companies" L70: "Renewable Energy Projects" L71; "Solar Technology" L73; "Waste-to-Energy" L75; "Liquefied Natural Gas (LNG)" L78; "Electric Mobility" L86; "Battery Storage" L88.
  - "Resources" L92; "Mauritius Energy Sector Resources" L94; separator L124.
- Tables: none (not applicable). The statistics are in prose, in toe and GWh.
- Quantitative figures in prose:
  - L10: "90.9 percent of the primary energy requirement sourced from imports in 2024, including petroleum products (61.1 percent) and coal (29.8 percent)"; target "60 percent renewable energy in electricity generation by 2030".
  - L11: the CEB "usually generates around 40 percent of Mauritius’s electricity through its four thermal power stations and ten hydroelectric plants", while "the remaining 60 percent" comes from IPPs. "In 2024, the IPPs produced 53 percent of the total electricity generated and the CEB produced the remaining 47 percent." The CEB was established by "the CEB Act of 1963".
  - L12: demand "was expected to exceed its daily 626 megawatts power generation capacity"; the power-barge tender was "to boost electricity output by up to 100 megawatts per day".
  - L13: the 2025-2026 budget (June 2025) includes "a $662 million (Rs 30 billion) investment in solar energy and biomass projects, aiming to boost renewable energy to over 35 percent of the electricity mix by 2028"; "a 15 MW floating photovoltaic system at Tamarin Falls".
  - L14: "plans to add 100 MW of capacity by January 2026".
  - L16: imports "made up 90.9 percent (1,467,806 toe) of the total primary energy requirement in 2024"; local sources "9.1 percent (147,066 toe)". 2023 imported petroleum products: "fuel oil (44 percent), diesel (21 percent), aviation fuel(16 percent), gasolene (12 percent) and LPG (6 percent)". "In 2024, $32 million worth of the LPG imported was sourced from the United States via the UAE."
  - L18: total primary energy requirement in 2024 "was 1,614,872 tons of oil equivalent (toe), up by 5.0 percent from 1,537,622 toe in 2023".
  - L20: "electricity generation increased by 4.7 percent from 3,265.5 GWh (280,780 toe) in 2023 to 3,417.6 GWh (293,864 toe), of which 81.8 percent (2,796.6 GWh) was generated from non-renewable sources and 18.2 percent (621.0 GWh) from renewable sources".
  - L22 (2023 end use): transport "52 percent", manufacturing "20 percent", households "16 percent".
  - RESP figures:
    - L28: "Achieving 538 GWh from biomass and 98 GWh from WtE by 2030".
    - L29: "a target of 300,000 systems installed by 2027".
    - L30: "a goal of 50 MW installed capacity by 2030" (ocean energy).
    - L32: "Integrating 500 MW of Battery Energy Storage Systems (BESS) by 2030".
    - L41: "to train 500+ workers".
  - L72: "$213 million (Rs 19 billion) for energy self-sufficiency projects over three years (2024-2027)".
  - L74, solar:
    - Radiation of "some 6 kWh/m2/day"; MARENA targets (see Lists).
    - GreenYellow operates "a 14MWac solar farm at Arsenal and another 16MWac solar farm in Solitude"; its pipeline "aggregates to some 13 solar projects totaling over 37 MWac".
    - Qair has been in Mauritius "since 2008". It is "investing approximately Rs. 6.7 billion" in "four STOR’SUN hybrid renewable energy projects", which "will contribute 60 MWac to the grid, increasing renewable energy by 6%".
    - SeaBrew plans "a 15 MW solar farm in Amaury" (April 2025).
  - L76: "over 400,000 tonnes of municipal solid waste annually". The waste-to-energy plan is: "(1) setting up of a 3.45 MW WtE pilot plant by 2027, and two additional plants by 2029, with a target of 15 MW capacity by 2030 (2) development of a sustainable and diversified biomass energy sector capable of generating 538 GW by 2030".
  - L79: "the target of a 1050 GW generation from LNG by 2030".
  - L87, electric mobility:
    - "1,263 electric cars ... as at October 2024, compared to only 10 in 2016".
    - Land-transport energy "rising by 27 percent from 310.1 Ktoe in 2013 to 393.8 Ktoe in 2023".
    - "As at October 31, 2024, 705,103 vehicles were registered", against the 2023 figure of "676,441".
    - Budget 2023/2024: "a 30 percent subsidy up to a maximum of Rs 3.5 million on the purchase of electric buses by bus companies".
    - 2025-2026 budget: "the renewal of the Negative Excise Duty of Rs 200,000 for purchase of electric vehicles up to June 2025".
  - L89: the CEB "has already installed 40 MW of BESS spread over 6 sub-stations". Targets: "500 MW of BESS by 2030"; "training 100 technicians by 2026"; "at least two agreements signed by 2028"; "100 percent SSDG/MSDG interconnection and 60 percent grid responsiveness to variable renewable energy by 2030".
- Lists:
  - RESP highlights, L26-42, 4 numbered pillars:
    1. "Renewable Energy Expansion:" (4 bullets, L27-30)
    2. "Grid Modernization and Energy Storage:" (3 bullets, L32-34)
    3. "Policy and Investment Frameworks:" (3 bullets, L36-38)
    4. "Capacity Building and Innovation:" (2 bullets, L41-42). The last bullet is "Promoting youth entrepreneurship through CleanTech incubators and fostering local manufacturing of renewable energy components".
  - Leading Sub-sectors, L44-68: 6 groups with 19 items in total:
    - "Renewable Energy Projects:" (6): PV cells and technology; solar water heaters; wind turbines; waste-to-energy plants; bioenergy; "Liquefied Natural Gas (LNG) projects" (L50). LNG projects sit inside this group (L44-50).
    - "Electric Mobility" (3, L52-54)
    - "Energy Efficiency Solutions" (3, L56-58)
    - "Public-Private Partnerships" (3, L60-62)
    - "Capacity Building and Training:" (2, L64-65)
    - "Innovation and R&D:" (2, L67-68). The last item is "Research partnerships to advance smart grids and energy efficiency technologies".
  - MARENA solar targets, L74, 6 numbered items:
    1. "Installation of 300,000 rooftop solar systems by 2027"
    2. "150 MW in agro-industrial solar systems by 2028"
    3. "operationalization of 3 pilot floating solar energy production site by 2028"
    4. "Deployment of 30 hybrid PV-BESS systems by 2029"
    5. "launching 3 pilot agri-photovoltaic projects by 2027"
    6. Last: "Deployment 5 solar-powered desalisation units in water distressed areas by 2030"
  - Local solar players, L74 (6): Cluny Solar Ltd, IBL Energy, Terragen, Ominicane, SeaBrew Solar Ltd, last Alteo. Waste-to-energy players, L76 (3): Alteo, Omnicane, Terragen.
  - Qair STOR'SUN projects, L74: 4 (Stor’Sun 1-4).
  - LNG areas of interest, L81-85 (intro L80: "While there is no visibility on actual upcoming tenders, key areas of interest for the future include:"), 6 items: Feasibility Studies and Environmental Impact Assessments; Combined Cycle Gas Turbine (CCGT) Technology; LNG Infrastructure Development; Power Barges and Floating LNG Solutions; Regional LNG Hub Development; last "Financing and Project Development" (runs on at L85).
  - Local energy sources, L16 (6): "bagasse, hydro, wind, landfill gas, photovoltaic and fuelwood".
  - Budget key measures, L13 (3): support for private solar producers; a second BESS; electric buses.
  - RESP key initiatives, L13 (4): National Biomass Framework; 15 MW floating PV at Tamarin Falls; agri-solar and hybrid solar projects; wind farm at Plaine des Roches.
  - REIF support, L14 (3): sovereign guarantees; blended finance instruments; a digital one-stop-shop.
  - Resources, L95-122, 9 entries:
    1. MEPU (L95-97)
    2. CEB (L98-102)
    3. MARENA (L103-105)
    4. MRIC (L106-108)
    5. MCCI (L109-110; no website line)
    6. Statistics Mauritius (L111-113)
    7. EEMO (L114-116)
    8. UNDP Mauritius (L117-119)
    9. Last: "Government of Mauritius e-Procurement System" (L120-122)
- Entities and aliases:
  - "The Central Electricity Board (CEB), a government-owned entity in Mauritius under the Ministry of Energy and Public Utilities, established by the CEB Act of 1963" (L11); also L89 and L98-102.
  - "Ministry of Energy and Public Utilities (MEPU)" (L11, L95).
  - "Mauritius Renewable Energy Agency (MARENA)" (L13); "MARENA" (L74, L89, L103); "the MARENA" (L79).
  - "The Renewable Energy Strategic Plan (RESP) 2025–2030" (L13, L24, L89, L91); also "its strategic plan for 2025-2030" (L79) and "the 2025-2030 plan" (L81).
  - "The Renewable Energy Investment Facility (REIF)" (L14, L36, L61).
  - IPPs: "various Independent Power Producers (IPPs), mainly private generators from the sugarcane industry" (L11); "the procurement arm of the three IPPs" (L11).
  - International: IRENA and the World Bank (L13); "the World Bank published a sugarcane sector review competitiveness analysis" in 2020 (L76); "PricewaterhouseCoopers India" (L79); Madagascar (L79); South Africa (coal source, L11); the United States and the UAE (LPG route, L16); UNDP (L117).
  - Companies: "French company GreenYellow" (L74). "French company Qair" (L74), credited with "establishing the country’s first wind energy facility". Local players at L74 and L76; the name is spelled "Ominicane" (L74) and "Omnicane" (L76).
  - Places and sites: Tamarin Falls and Plaine des Roches (L13); Arsenal, Solitude, Amaury (L74); "the Mare Chicose landfill" (L76).
  - Others: CareEdge Ratings (L15, L23); Statistics Mauritius (L23, L111); "the National Land Transport Authority" (L87); MRIC, MCCI, EEMO (L106-116); the e-Procurement System (L120).
  - Abbreviations:
    - toe/Ktoe (L16-20, L87); MWac (L74)
    - BESS (L13, L32, L89); WtE/WTE (L27-28, L48, L75-76); OTEC (L30); VRE (L33)
    - PPAs (L13); PPPs (L89); RFI (L79)
    - SSDG/MSDG (L89; not expanded)
    - CCGT (L79, L82). L79 spells it "Combine Cycle Gas Turbine" once.
- Forecasts, guidance, deadlines, effective dates:
  - Renewable share: 60% of electricity generation by 2030 (L10, L74); over 35% of the electricity mix by 2028 (L13).
  - Capacity: 100 MW added by January 2026 (L14).
  - RESP and MARENA: RESP targets for 2027-2030 (L28-32, L41); MARENA solar targets (L74).
  - Waste and biomass: a 3.45 MW waste-to-energy pilot by 2027, two more plants by 2029 and 15 MW by 2030 (L76); biomass "538 GWh" (L28) or "538 GW" (L76) by 2030; waste-to-energy 98 GWh by 2030 (L28).
  - Ocean energy: 50 MW by 2030 (L30).
  - BESS: 500 MW by 2030 (L32, L89, L91); 100 technicians by 2026 and two PPP agreements by 2028 (L89).
  - LNG: feasibility "by 2025" and "1050 GW generation from LNG by 2030" (L79).
- Dated events; actions vs plans:
  - Actions:
    - CEB Act of 1963 (L11); Qair present since 2008 (L74); 2020 World Bank review (L76).
    - LNG history (L79): 2017 feasibility study; the 2018 CCGT tender "stalled due to financing issues"; 2019 talks with Madagascar, alongside a government announcement of a regional LNG value chain and partial CCGT financing; 2021 PwC India study; 2022 RFI.
    - Budget 2023/2024 electric-bus subsidy (L87).
    - Early-2025 peak shortfall. "the CEB released a tender in June" (2025 by the paragraph's context) for power barges; then "government backed down on this project" (L12).
    - April 2025: SeaBrew announced plans (L74).
    - June 2025: budget (L13); coal tender extended to U.S. companies "for the first time" (L11); construction of Stor’Sun 1 and 2 began (L74).
    - August 2025: MARENA strategic-plan announcement. "As of September 2025, no further progress has been reported" on LNG (L79).
    - 40 MW of BESS installed by the CEB (L89).
  - Plans: RESP items; Stor’Sun 3 and 4 "set to commence in August and September 2025, respectively" (L74); "Establishing a comprehensive Renewable Energy law" and "operationalizing a Renewable Energy Investment Facility" (L36).
- Hedged claims:
  - L11: "usually generates around 40 percent". "usually" and "around" attach to the typical CEB share; the 2024 split of 47/53 is firm.
  - L12: "energy demand was expected to exceed its daily 626 megawatts".
  - L79: "the project appears to be shelved". "appears" attaches to "shelved"; "no further progress has been reported" is firm.
  - L80: "While there is no visibility on actual upcoming tenders, key areas of interest for the future include". The areas listed are not stated to be tenders.
  - L74: "Once operational, these projects will contribute 60 MWac" (conditional); "some 6 kWh/m2/day"; "some 13 solar projects".
  - L87: "which will further incentivize potential car owners" (firm).
- Rounded prose beside exact figures (computed checks):
  - 1,467,806/1,614,872 = 90.9% (matches); 61.1 + 29.8 = 90.9 (matches); 1,467,806 + 147,066 = 1,614,872 (matches L18).
  - 1,614,872/1,537,622 = +5.0% (matches); 3,417.6/3,265.5 = +4.66% ("4.7 percent").
  - 2,796.6 + 621.0 = 3,417.6 (matches); 621.0/3,417.6 = 18.2% (matches).
  - 393.8/310.1 = +27.0% (matches).
  - The 2023 petroleum-product shares sum to 99%. The 2023 end-use shares listed sum to 88%; the remainder is not stated.
  - GreenYellow's two farms total 14 + 16 = 30 MWac, within "over 37 MWac".
- Operative definitions, rules and scope exceptions:
  - L18: the total primary energy requirement is "sum of imported and locally available fuels less re-exports and bunkering after adjusting for stock changes".
  - L22: the transport sector "includes land, air and sea transport modes".
  - L87: the subsidy applies to "the purchase of electric buses by bus companies" at "30 percent ... up to a maximum of Rs 3.5 million". The Negative Excise Duty is "Rs 200,000 for purchase of electric vehicles up to June 2025".
  - L11: IPPs burn bagasse "during the sugarcane harvesting season from June to November and imported coal outside of the harvesting season from December to May".
- Negative and exclusion statements: the power-barge project was withdrawn ("government backed down on this project", L12); LNG has "no further progress has been reported" and "appears to be shelved" (L79); "no visibility on actual upcoming tenders" (L80); the MCCI entry has no website line (L109-110); "While I cannot provide hyperlinks directly" (L93).
- Amendments or contradictions (no precedence stated):
  - Biomass by 2030: "538 GWh from biomass" (L28) vs "capable of generating 538 GW by 2030" (L76).
  - Waste-to-energy by 2030: "98 GWh from WtE" (L28, energy) vs "a target of 15 MW capacity by 2030" (L76, capacity). These are different measures.
  - LNG chronology: "As of September 2025, no further progress has been reported, and the project appears to be shelved. However, more recently in August 2025, the MARENA announced ..." (L79). August precedes September. The LNG target is stated in the unit "1050 GW generation".
  - Renewable targets by year: over 35% of the electricity mix by 2028 (L13) and 60% by 2030 (L10, L74); the 2024 actual was 18.2% of generation (L20).
  - CEB share: "usually ... around 40 percent" vs "47 percent" in 2024 (both L11).
  - Currency conversions (computed): "$662 million (Rs 30 billion)" (L13) implies about 45.3 Rs/USD; "$213 million (Rs 19 billion)" (L72) implies about 89.2 Rs/USD. No exchange rate is stated.
  - Training: "train 500+ workers" (L41, RESP pillar 4) vs "training 100 technicians by 2026" (L89, BESS plan). These have different scopes.
  - BESS: the budget's "introduction of a second Battery Energy Storage System (BESS)" (L13) vs the CEB having "already installed 40 MW of BESS spread over 6 sub-stations" (L89).
  - IPP count: "various Independent Power Producers (IPPs)" vs "the procurement arm of the three IPPs" (both L11).
  - The 2025-2026 budget, announced in June 2025 (L13), "saw the renewal of the Negative Excise Duty ... up to June 2025" (L87).
  - Source attribution: the heading names "the CareEdge Ratings Africa Report" (L15); the footnote names "Statistics Mauritius, January 2025 CareEdge Ratings Report" (L23), and that source carries 2024 data.
  - Name spellings: "Ominicane" (L74) vs "Omnicane" (L76); "Combine Cycle Gas Turbine" vs "combined cycle gas turbine" (both L79; also L82).
- Notes: L87 describes electric cars as "slowly but steadily increasing, since 2019" while comparing with 2016. Verbatim spellings: "desalisation" (L74), "gasolene" (L16).
- Coverage: full. Read ledger: L1-124 in one chunk (offset 1), with the tail L120-124 re-read. L74, the longest line, was checked to its true end. Unread: none. Missing text: none.

---

## D10 - Mexico Country Commercial Guide: Power Sector: Electricity Infrastructure and Smart Grid; Renewable Energy

- Source: `text/D10.txt` (104 lines; 15,891 chars) from `docs/ccg_energy_cleantech_sectors_mexico.txt`. No pages.
- Written or submitted by: ITA (L3). Both chapters name the same contact, "Claudia Salgado (Claudia.Salgado@trade.gov)" (L51, L102), labelled "Commercial Specialist" (end of L50; L101). Bodies cited, which are not authors: PRODESEN (L11, L59); the International Energy Agency (L12); the table sources "INEGI, U.S. International Trade Administration, Global Trade Atlas" (L38). ITA is both the issuer and a named table source.
- Type, date, edition: two chapters:
  - "## Power Sector: Electricity Infrastructure and Smart Grid" (L5); "Last published: 2026-02-12" (L6); "Source: https://www.trade.gov/country-commercial-guides/mexico-power-sector-electricity-infrastructure-and-smart-grid" (L7).
  - "## Renewable Energy" (L53); "Last published: 2026-02-12" (L54); "Source: https://www.trade.gov/country-commercial-guides/mexico-renewable-energy" (L55).
- Period covered: actuals span 2022-2025 (2023 PRODESEN system data; the table's 2022-2024 plus "2025 (est.)"). Reforms: 2014, the October 2024 constitutional reform, and the laws of March 18, 2025. Projections run to 2027, 2030, 2038 and 2050. Fiscal/calendar convention: not stated. Two announcement dates have no year: "On August 21" (L28) and "On February 5" (L79).
- Section headings in order:
  - Chapter 1: "Overview" L9; "Trade Statistics" L29; "Leading Sub-sectors" (run into the end of source line L38); "Opportunities" (run into the end of L39); "Resources" L41; "Events" (run into the end of L48); "Commercial Specialist" (run into the end of L50).
  - Chapter 2: "Overview" L57; "Leading Sub-sectors" (run into the end of L68); "Opportunities" L74; "Industrial and Commercial Sectors" L75; "Working with States" L77; "Strengthening and Expansion of the National Electrical System 2025-2030" (run-in at the start of L79); "Geothermal" L80; "Solar Thermal" L82; "Resources" L84; "Events" (run into the end of L96); "Commercial Specialist" L101; separator L104.
- Tables:
  - **L30-38.** Title: "Table: Mexico Power Generation Equipment Market Size (USD Billions)" (L30). Header L32: "2022 | 2023 | 2024 | 2025 (est.)". Values have two decimals. Rows:
    - "Total Exports" L33: 4.58 | 5.72 | 5.48 | 5.79
    - "Total Imports" L34: 4.13 | 4.94 | 4.44 | 2.90
    - "Imports from the United States" L35: 1.09 | 1.22 | 1.07 | 0.97
    - "Exchange Rates" L36: 20.13 | 17.76 | 18.30 | 19.81
    - Source line L38: "Source: INEGI, U.S. International Trade Administration, Global Trade Atlas (HS Codes 8501, 8502, 8503)". The heading "Leading Sub-sectors" follows on the same line.
    - Table notes: despite the title there is no "Total Local Production", "Total Market Size" or exports-to-U.S. row. "Exchange Rates" has no currency or unit label. The 2025 column is an estimate. Product scope is HS codes 8501, 8502 and 8503. No prose restates a table value.
- Quantitative figures in prose:
  - L10: the SEN supplies "more than 129 million inhabitants" and "encompasses nine regions plus a binational electricity system in Baja California".
  - L11 (PRODESEN, 2023):
    - Consumption "was 298,599 GWh in 2023, which represented an increase of 3.4 percent in comparison to 2022", "attributed to six sectors: residential, commercial, services, agricultural, and medium and large enterprises".
    - Generation was "351,695 GWh, from which 58.46 percent corresponded to combined cycle". "In 2023, there were 12.2 percent total losses in comparison to 2022."
    - Total installed capacity in 2023 "reached 93,788 MW".
  - L12: population "expected to grow to over 150 million by 2050" (IEA); "The industrial and commercial sectors account for 72 percent of electricity demand". Consumption is estimated to rise "2.8 percent annually on average between 2024 and 2038". Capacity is expected to "increase 23,992 MW between 2024-2027, 58,736 MW between 2028-2038, and 82,728 MW between 2024-2038, to reach a total of 176,516 MW by 2038".
  - L14 (repeated at L60): the package includes "eight new secondary laws and amendments to three existing laws".
  - L15 (repeated at L60): "at least 54 percent of the electricity dispatched to the national grid must come from Federal Electricity Commission (CFE) plants, leaving up to 46 percent for private sector producers".
  - L16: Plan México "aims to add 22 gigawatts of new power generation capacity by 2030, deliver a portfolio of 100 transmission and distribution projects, and ensure the CFE holds at least 54 percent market share in electricity generation".
  - L20-25 (repeated at L63-68): pathway thresholds "up to 0.7 MW", "between 0.7-20 MW", "larger than 0.7 MW", and "a minimum 54 percent ownership stake".
  - L27: CFE is "comprised of 10 subsidiaries, five affiliated companies, and four business units". Power generation runs "through six companies"; "Another three subsidiaries oversee transmission, distribution, and supply of electricity."
  - L28: "invest over 8.1 billion dollars to strengthen the transmission network in the benefit of 50 million users"; "275 new transmission lines and 524 electrical substations". "generation capacity will increase by 29,074 MW", with CFE "22,674 MW" and the private sector "6,400 MW".
  - L59: 2023 total "351,695 GWh, from which 24.32 percent corresponded to clean energy sources", with "75 percent" from fossil fuels. Clean installed capacity "is projected to increase to 62.4 percent by 2038". The 2038 scenario has "approximately 6.4 million electric vehicles, which would represent 35.1 percent of the motor vehicles sold in 2038".
  - L76: "more than 30 percent of the industrial sector has begun to take voluntary steps to decarbonize".
  - L79: "CFE generates 22,674 MW with an estimated investment of over 22 billion dollars, while private investment generates 6,400 MW"; "seven wind farms, nine photovoltaic plants, five combined-cycle plants".
  - L83: "two thermal solar projects in Baja California".
- Lists:
  - Six pathways for private participation, at Chapter 1 L20-25 and repeated with identical wording at Chapter 2 L63-68:
    1. "On-site distributed generation up to 0.7 MW, exempt from permit requirements"
    2. "Self-generation systems between 0.7-20 MW, not connected to the national grid"
    3. "Self-generation systems between 0.7-20 MW with grid connection, where surplus power must be sold exclusively to the CFE"
    4. "Open competition for projects larger than 0.7 MW participating in Mexico’s wholesale electricity market"
    5. "Utility-scale projects developed privately, with electricity sold exclusively to the CFE and possible asset transfer"
    6. Last: "Joint ventures with the CFE, in which the CFE holds a minimum 54 percent ownership stake"
  - Chapter 1 "Leading Sub-sectors", L39 (inline, 5): power generation, energy efficiency, distributed generation, energy storage technologies, small-scale renewable energy projects.
  - Chapter 1 "Resources", L42-48, 8 items: SENER; CENACE; CFE; CNE; INEEL and FIDE (same line, L46); CONUEE; last CONAMER.
  - Chapter 1 events, L49-50, 3 items: "Power-Gen International, January 20-22, 2026. San Antonio, TX"; "Distributech International, February 2-5, 2026. San Diego, CA."; last "Expo Eléctrica Internacional, May 26-28, 2026. Mexico City".
  - Chapter 2 "Leading Sub-sectors", L69-73, 5 items: Small-scale distributed generation; On-site distributed generation; Energy storage; Solar heating; last Geothermal.
  - Chapter 2 "Resources", L85-96, 13 items: SENER; CFE; CNE; CENACE; INEEL and FIDE (same line, L89); AMDEE; ANES; ASOLMEX; AGM; Mexican Hydrogen Association; AMEXHIDRO; last CONUEE.
  - Chapter 2 events, L97-100, 4 items: "The Green Expo: 2026 TBC. Mexico City."; "RE+: November 16-19, 2026. Las Vegas."; "Distributech International: February 2-5, 2026. San Diego, CA."; last "Expo Eléctrica Internacional: May 26-28, 2026. Mexico City."
  - Contents of the plan, L79: seven wind farms; nine PV plants; five natural-gas combined-cycle plants (including "the replacement of the Tula fuel oil plant with a combined-cycle plant"); internal combustion plants; "batteries that accompany renewable energy"; cogeneration.
  - Generation sources, L11: combined cycle "and the rest to gas, coal, internal combustion, hydro, wind, solar nuclear, geothermal and efficient cogeneration" (verbatim; there is no comma between "solar" and "nuclear").
- Entities and aliases:
  - The national system is named "National Power System (Sistema Eléctrico Nacional or SEN)" (L10), "National Electricity System" (L11), "National Electrical System (Sistema Eléctrico Nacional or SEN)" (L59) and "National Electrical System" (L79).
  - "National Interconnected System (Sistema Interconectado Nacional or SIN)" and "Western Electricity Coordinating Council (WECC)" (L10).
  - "National Power System Development Program (Programa de Desarrollo del Sistema Eléctrico Nacional or PRODESEN)" (L11, L59); "the 2024-2038 PRODESEN" (L59).
  - "Federal Electricity Commission (Comisión Federal de Electricidad or CFE)" (L11); "a State Productive Enterprise" (L27).
  - "Government of Mexico (GOM)" (L13); "President Claudia Sheinbaum" (L14, L16, L28, L60, L79, L83).
  - Regulators: the reforms dissolve "the National Hydrocarbons Commission (CNH) and the Energy Regulatory Commission (CRE)", "replacing them with a centralized National Energy Commission (CNE) reporting directly to the executive branch" (L15). CNE also appears at L45 and L87.
  - Plans: "Plan México" (L16) / "Plan Mexico 2025-2030" (L83); "CFE’s Strengthening and Expansion Plan 2025-2030" (L28); the run-in heading "Strengthening and Expansion of the National Electrical System 2025-2030" and the body's "the Plan to Strengthen and Expand the National Electrical System 2025-2038" (L79).
  - Expansions differ between the two Resources lists:
    - SENER: "Mexican Secretariat of Energy" (L42) / "Secretariat of Energy" (L85)
    - CENACE: "National Control Center for Energy" (L43) / "National Energy Control Center" (L88)
    - INEEL: "National Institute of Electricity and Clean Energy" (L46) / "National Institute for Electricity and Clean Energy" (L89)
    - FIDE: "Trust for Electric Energy Saving" (L46) / "Fund for Energy Saving" (L89)
    - CONUEE: "National Commission for Energy Efficiency" (L47) / "National Commission for the Efficient Use of Energy" (L96)
    - CONAMER: "Federal Commission for Regulatory Improvement" (L48 only)
  - Others: International Energy Agency (L12); Pemex and the Tula fuel oil plant (L79); INEGI (L38, not expanded); "a new Geothermal Energy Law" (L81); Baja California (L10, L28, L83).
- Forecasts, guidance, deadlines, effective dates:
  - Demand: consumption +2.8% a year over 2024-2038 (L12); population by 2050 (L12).
  - Capacity: the path to 176,516 MW by 2038 (L12); Plan México's 22 GW by 2030 and 100 transmission/distribution projects, with CFE at 54% or more (L16); the CFE plan for 2025-2030, with 275 lines, 524 substations and +29,074 MW (L28).
  - 2038 projections: clean capacity at 62.4% and 6.4 million EVs (L59).
  - Table: "2025 (est.)".
- Dated events:
  - Reforms: the 2014 energy reform and the "October 2024 constitutional reform" (L14, L60); "On March 18, 2025, President Claudia Sheinbaum enacted a sweeping energy reform package" (L14, L60).
  - Laws: "On March 18, 2025, Mexico published a new Geothermal Energy Law" (L81).
  - Announcements: "On August 21", the CFE plan (L28, no year); "On February 5", the national-system plan (L79, no year); "On August 26, 2025", two thermal solar projects (L83).
  - Trade events: dates in 2026 (L49-50, L97-100).
- Hedged claims:
  - L12: "It is estimated that consumption will increase"; "It is expected that the installed capacity will increase"; "According to the International Energy Agency, Mexico’s population is expected to grow".
  - L16: "While the government frames these reforms around goals of sustainability and energy security, the shift raises concerns among private and foreign stakeholders about regulatory transparency, investment risk, and market competition". "frames" attributes the goals to the government; the concerns are stated as fact.
  - L58: "with the right technologies and expertise, the country could increase energy storage and green hydrogen projects"; "Harnessing this potential could help to diversify the energy supply" (a conditional "could").
  - L59: "is projected to increase to 62.4 percent by 2038"; "estimating that ... will reach approximately 6.4 million electric vehicles, which would represent 35.1 percent".
  - L79: "an estimated investment of over 22 billion dollars"; "The plan also projects that Pemex will generate electricity primarily in its refineries and petrochemical plants".
- Rounded prose beside exact figures: Plan México's "22 gigawatts ... by 2030" (L16) sits alongside CFE's "22,674 MW" (L28, L79); also "more than 129 million" (L10) and "over 150 million" (L12). Computed checks: 23,992 + 58,736 = 82,728 (matches); 93,788 + 82,728 = 176,516 (matches); 22,674 + 6,400 = 29,074 (matches); 54 + 46 = 100.
- Operative definitions, rules and scope exceptions:
  - The dispatch rule: at least 54% from CFE and up to 46% private (L15, L60).
  - The six pathways, with their thresholds and exclusivity terms (L20-25, L63-68).
  - L59 defines "clean energy sources" as "(renewable such as solar, wind, and hydro, and non-renewable such as nuclear and efficient cogeneration)" and fossil fuels as "(combined cycle, conventional thermal, coal fired, gas fired, and internal combustion)".
  - L11: installed capacity covers "power generation plants from the Federal Electricity Commission ... and from private companies, interconnected and from distributed generation".
  - L10: the SEN's scope is nine regions plus the Baja California binational system; "The Baja California system operates in the Western Interconnection of the United States".
  - L38: the table covers HS 8501-8503.
  - L81: the Geothermal Energy Law's purpose covers "generating electricity or for divers uses such as water hear, industrial or agricultural uses" (verbatim).
- Negative and exclusion statements: pathway 2 is "not connected to the national grid"; pathway 1 is "exempt from permit requirements"; the reforms are "significantly restricting private-sector participation" (L14; "private sector" at L60); CNH and CRE are dissolved (L15); "The Green Expo: 2026 TBC" (L97).
- Amendments or contradictions (no precedence stated):
  - The CFE expansion plan is described twice:
    - L28: "On August 21, President Claudia Sheinbaum announced CFE’s Strengthening and Expansion Plan 2025-2030 to invest over 8.1 billion dollars to strengthen the transmission network".
    - L79: the heading "Strengthening and Expansion of the National Electrical System 2025-2030" and the body "On February 5, President Claudia Sheinbaum announced the Plan to Strengthen and Expand the National Electrical System 2025-2038. The objective is that CFE generates 22,674 MW with an estimated investment of over 22 billion dollars".
    - The announcement dates, the plan horizon (2030 vs 2038) and the investment figures differ. The MW split (22,674 CFE and 6,400 private) agrees. Neither date has a year.
  - Plan México's "22 gigawatts ... by 2030" (L16) vs the CFE plan's total of "+29,074 MW" (L28).
  - 2023 generation shares: clean 24.32% + fossil 75% = 99.32% (L59). Combined cycle at 58.46% (L11) falls within the fossil share.
  - L59 switches basis from a generation share (24.32% of GWh) to "This installed capacity from clean energy plants ... 62.4 percent by 2038".
  - L11 announces "six sectors" and then gives five comma-separated entries, the last being "medium and large enterprises".
  - CFE has "10 subsidiaries" (L27), but the text describes six generation companies and "Another three subsidiaries", which is 9.
  - Amendment order: the 2025 package "largely reverse[s] the liberalization introduced in Mexico’s 2014 energy reform" and implements the "October 2024 constitutional reform" (L14, L60). The order is 2014, then October 2024, then March 18, 2025.
- Notes: Chapter 1 L13-17 and Chapter 2 L60-61 repeat the reform text nearly verbatim. L11 and L59 both give 351,695 GWh for 2023.
- Coverage: full. Read ledger: L1-104 in one chunk (offset 1), with the tail L100-104 re-read. Unread: none. Missing text: none.

---

## Shared ground within this part (navigation only)

- Issuer and edition: all five are ITA Country Commercial Guide chapters (L3 of each; trade.gov source URLs). Publish dates:
  - D06: 2025-08-01 (L6)
  - D07: 2025-11-17 (L6, L99)
  - D08: 2026-03-17 (L6) and 2026-03-11 (L50)
  - D09: 2026-02-19 (L6)
  - D10: 2026-02-12 (L6, L54)

  Each country appears once (one edition each). None of these five cites another bundle document.
- Market-data tables: only D07 and D10 have them.
  - D07 has two tables in USD millions, covering 2020-2024 plus 2025 (est.), sourced from Global Trade Atlas and the World Bank (L10-66, L103-115). Its row label is "Imports from the U.S.".
  - D10 has one table in USD billions, covering 2022-2024 plus 2025 (est.), sourced from INEGI, ITA and GTA, scope HS 8501-8503 (L30-38). Its row label is "Imports from the United States".
  - Neither has a local-production or market-size row. D06, D08 and D09 have no tables.
- Renewable electricity targets and actuals (the bases differ):
  - D06: 80% by 2030 (L12, L28, L45); 59% in 2024 (L12, L19).
  - D08: 30% by 2030 (L16, L20, L32); 12.5% in 2023 (L20).
  - D09: 60% of electricity generation by 2030 (L10, L74); over 35% of the electricity mix by 2028 (L13); 18.2% of 2024 generation (L20).
  - D10: clean energy at 24.32% of 2023 generation, including nuclear and efficient cogeneration (L59); clean installed capacity at 62.4% by 2038 (L59).
  - D07: renewables appear only as "the remaining share" after coal (about 61%) and gas (about 20%) (L69). No renewable target was found.
- Emissions targets:
  - D06: -65% vs 1990 by 2030; neutrality by 2045; EU net zero by 2050 (L12, L30).
  - D07: -32% by 2030 and net zero by 2060 (2022 NDC, L118).
  - D08: -27% vs 2015 by 2030 (July 2021; L20, L56); electricity -30% (L20); solid waste -47% by 2030 and -92% by 2050 (L56).
  - The Paris Agreement appears in D07 L118, D08 L20 and L56, and D09 L14.
- Installed capacity and generation scale (units differ):
  - D06: about 270 GW and about 430 TWh (L36); 431.7 TWh in 2024 (L19).
  - D07: about 101 GW at end-2024 (L70).
  - D08: 23.7 GW in 2023, rising to 39.6 GW in 2030 (L14).
  - D09: 626 MW daily capacity (L12); 3,417.6 GWh in 2024 (L20).
  - D10: 93,788 MW in 2023, rising to 176,516 MW in 2038 (L11-12); 351,695 GWh in 2023 (L11, L59).
- State utilities, oil companies and market-share rules:
  - D07: PLN (L70); Pertamina (L73).
  - D08: IEC, the 2018-2026 reform and IEC's transmission/distribution monopoly (L14, L25-27).
  - D09: the CEB produced 47% of 2024 generation, against a usual ~40% (L11).
  - D10: CFE at 54% or more of dispatch, market share and JV stakes (L15, L16, L25, L60, L68).
- The United States as supplier:
  - D06: U.S. LNG is about 90% of German LNG imports (L24).
  - D07: the U.S. supplies about 60% of Indonesia's LPG (L71); U.S. crude is about 4% of oil and gas imports (L72); the tables have U.S. trade rows.
  - D09: $32 million of LPG from the U.S. via the UAE in 2024 (L16); a coal tender opened to U.S. companies in June 2025 (L11).
  - D10: the table row "Imports from the United States" (L35).
  - U.S. companies named: Noble Energy and Chevron (D08 L17).
  - The UAE appears in D06 L53 (potential hydrogen supplier) and D09 L16 (LPG route).
- International bodies: the World Bank appears in D07 L66 and L103 (exchange-rate source) and in D09 L13 (partner) and L76 (2020 sugarcane review). IRENA: D09 L13. IEA: D10 L12. OECD: D08 L10.
- Coal:
  - D06: phase-out by 2038 (L14, L17, L27, L29).
  - D07: coal is about 61% (L69).
  - D08: 17% in 2023, with all coal plants to shut under the 2030 goal (L16).
  - D09: 29.8% of the primary energy requirement, imported from South Africa (L10-11, L16).
  - D10: coal appears in the generation lists (L11, L59).
- Nuclear: D06 phase-out in April 2023 (L14, L17, L27, L29); D07 nuclear by 2032 with up to two 250 MW plants (L79); D10 counts nuclear as clean energy (L59).
- LNG and gas:
  - D06: FSRU terminals (L24, L33-34, L37).
  - D07: LNG opportunities (L74, L89).
  - D08: gas fields and exports (L16-18); the "Yavor" LPG storage project (L37).
  - D09: LNG history and the 2030 target (L78-85).
  - D10: combined cycle at 58.46% (L11); five combined-cycle plants in the plan (L79).
- Storage and BESS:
  - D06: 17.7 GWh total and 12.1 GWh battery storage in 2023 (L48); the 1.000 MWh battery park (L50).
  - D08: 300 MW in 2020, rising to about 3,000 MW in 2030 (L20, L32).
  - D09: 40 MW installed; 500 MW by 2030 (L32, L89).
  - D10: storage as a sub-sector (L39, L71); batteries in the plan (L79).
- Hydrogen: D06 L31-34, L51-54 and L60; D07 L76 and L94 (summit); D10 L58 (green hydrogen) and L94 (Mexican Hydrogen Association).
- Waste-to-energy:
  - D07: the first privately owned large-scale plant is under construction (L122).
  - D08: Neot Hovav, plus the Jerusalem, Tamar Region and southern Israel plants (L38-39, L73).
  - D09: the pilot plant and targets (L27-28, L48, L75-77).
- Desalination: D08 L40, L54 and L65-68; D09 solar-powered desalination units by 2030 (L74).
- Geothermal: D07 has 23 GW potential with 2,597 MW developed (L78) and lists geothermal as a sub-sector (L85). D10 has the Geothermal Energy Law of March 18, 2025 (L81) and lists geothermal as a sub-sector (L73).
- Interconnection status: D08 is an "electricity island" (L12) with the planned Great Sea Interconnector (L13). In D10, Baja California is in the U.S. Western Interconnection (L10), and the plan would interconnect the peninsula (L28).
- Similar names:
  - "Enlit Europe" (Bilbao, D06 L61) vs "ENLIT Asia 2025" (D07 L135).
  - The "Tamar" gas field (D08 L17-18) vs the "Tamar Region Waste-to-Energy facility" (D08 L39) vs "Tamarin Falls" (D09 L13).
  - "Project Prosperity" (D08 L13, L68).
  - "Distributech International" and "Expo Eléctrica Internacional" appear in both D10 event lists (L49-50, L99-100).
  - International Battery Summit (D07 L126, L136).
- Ministry abbreviation and alias variants:
  - D06: BMWE vs "Ministry of Economy", "Federal Ministry of Economy and Energy" and "Federal Ministry of Economics" (L26, L32, L34, L54, L63).
  - D07: EMR vs ESDM (L77, L78, L93-94).
  - D08: Ministry of Energy vs Ministry of Energy and Infrastructure (L16, L29, L43, L79).
  - D10: the expansions of CENACE, FIDE, INEEL, CONUEE and SENER differ between chapters (L42-48 vs L85-96).
- Forecasts and later actuals: no later edition exists in this part. Forward-looking statements dated before their own publish date, with no outcome stated:
  - D08: the pre-qualification timings (L37-40, L62, L65, L73).
  - D09: 100 MW by January 2026 (L14); Stor’Sun 3 and 4 (L74); LNG feasibility by 2025 (L79).
  - D06: 1,700 km of approvals expected in 2025 (L44; published 2025-08-01).
  - D07: carbon-market regulations planned for 2025 (L76; published 2025-11-17).
  - The D07 and D10 tables carry "2025 (est.)" columns.
- Proposed vs final; amendment order:
  - D10: 2014 reform, then the October 2024 constitutional reform, then the laws of March 18, 2025 (L14, L60).
  - D06: hydrogen strategy in 2020, updated July 2023 (L31). H2Global approval in January 2022, then the European Hydrogen Bank link in May 2023 (L54).
  - D08: the 2015 GHG goal, updated July 2021 (L20, L56); the October 2020 renewable energy decision (L32); the February 2025 Water Authority plan, pending approval (L62).
  - D07: NDC updated in 2022 (L118); carbon-market regulations planned for 2025, with implementation expected in 2027 (L76).
  - D09: the power-barge tender (June) was withdrawn (L12); LNG steps from 2017 to 2022, then "appears to be shelved" (L79).
- Same-period conflicts within documents (located in the sections above):
  - D06: L17 vs L19 (wind share, PV growth and share, hydro); L48 (battery share).
  - D08: L14 vs L26 (reform verb); L34 vs L77 (BIRD cadence).
  - D09: L28 vs L76 (538 GWh vs GW); L79 (August/September 2025 order).
  - D10: L28 vs L79 (plan date, horizon and investment).
- Issuer vs mentioned organizations: ITA is the author throughout. Data-source bodies are mentioned, not authors:
  - D07: Global Trade Atlas and the World Bank.
  - D09: Statistics Mauritius and CareEdge.
  - D10: INEGI, ITA and GTA; PRODESEN; IEA.
  - D08: the Electricity Authority, MOEP and the Water Authority.
  - D06: the Federal Network Agency and the National Hydrogen Council.
  - D06 and D09 carry no ITA contact; D07, D08 and D10 name ITA staff.


<!-- merged from doc-map-c.md -->

# aq-01543 - document map, part C (D11-D15)

Part file for the caller to merge into `notes/doc-map.md`. It is navigation only: it records where facts are, not what to ask.
Line numbers (`l.N`) are `text/Dnn.txt` lines. A text line equals the `docs/` original line + 2, because extraction adds a
two-line `# Dnn | ...` header. Facts are recorded as printed. "(computed)" marks arithmetic the mapper did by hand,
because no script runtime was available to this mapper. Re-run those figures with a script before relying on them.

## Part scope, provenance and read ledger

- Ids mapped: D11 Poland, D12 Portugal, D13 Romania, D14 South Africa, D15 South Korea. All have `method: text` and
  `pages: null`, so page counts do not apply.
- For all five, the manifest sha256 matches `notes/intake.json` `captured_sha256` and `source_sha256`. Intake also records
  `incomplete: false`, `gap_characters: 0` and `matches_capture: true`. Platform capture numbering differs from the D ids:
  D11 = capture doc 2, D15 = capture doc 4, D14 = capture doc 12, D12 = capture doc 16, D13 = capture doc 20.
- `docs/` holds only `.txt` captures (no HTML, PDF or images). Visual layout, such as merged table cells or the LNG chart
  that D15 l.324 mentions, cannot be inspected. These are recorded as unresolved, not as missing text.
- Read ledger: every line of every document was read in chunks.

| id | text lines | chunks read | original (`docs/`) lines compared | coverage |
|---|---|---|---|---|
| D11 | 1-234 | 1-150, 150-234, end check 230-234 | 1-25, 184-233 | full |
| D12 | 1-65 | 1-65, end check 60-65 | 14-19, 54-63 | full |
| D13 | 1-71 | 1-71, end check 66-71 | 20-25, 48-70 | full |
| D14 | 1-114 | 1-114, end check 108-114 | 10-12, 54-65 | full |
| D15 | 1-442 | 1-120, 120-199, 199-348, 348-442 | 1-40, 66-155, 155-214, 213-284, 284-323, 323-374, 374-441 | full |

- Table detection: a grep for `|` finds no table cells in D11, D13 or D14 (only the header line). In D12 it finds only
  link titles in Resources (l.58-60). D15 has two flattened tables (l.15-160 and l.167-318).
- Extraction spot-checks: the originals match the text apart from the 2-line header and trailing spaces stripped after `|`
  cells in D15.
  - D15 generation-mix table: the header and the 2022 TWh row were compared (original l.13-40), as were the 2024, 2025,
    2030 and 2038 rows (original l.69-156). The 2022 % tail and the 2023 TWh row (original l.41-65) were not compared
    against the original, but they were read in the text.
  - D15 Table 2: all 32 rows and the footer were compared (original l.165-316).
  - The D15 table note (l.159) and source lines (l.160, l.318) are in the original.
  - D11-D14 have no footnotes (not applicable).

## D11 - Poland CCG: "Energy Sector" and "Environmental Technologies"

- Source: `text/D11.txt` (234 lines, 34,111 chars), from `docs/ccg_energy_cleantech_sectors_poland.txt`; capture doc 2.
- Written or submitted by: U.S. International Trade Administration (l.3 "Poland Country Commercial Guide (U.S.
  International Trade Administration)"). Contact for both chapters: U.S. Commercial Service Poland, Commercial
  Specialist Katarzyna Szyndel (l.65-67, l.231). The chapter cites these sources but they are not its authors: Forum
  Energii "Yearbook - Energy Data" (l.25), the Renewable Energy Institute report (l.28), a PSEW estimate (l.33), GUS
  (l.74), EU Environmental Implementation Review 2022 (l.78, l.185), Institute for Environmental Economics (l.101) and
  Ministry of Climate and Environment forecasts (l.182).
- Type, date, edition: two web chapters.
  - `## Energy Sector` (l.5): "Last published: 2026-04-02" (l.6); "Source:
    https://www.trade.gov/country-commercial-guides/poland-energy-sector" (l.7).
  - `## Environmental Technologies` (l.69): "Last published: 2026-04-06" (l.70); "Source:
    https://www.trade.gov/country-commercial-guides/poland-environmental-technologies" (l.71).
  - No edition number.
- Period covered: calendar years, no fiscal convention.
  - Actuals: 2024 power (l.13-18), end-Q1 2025 PV (l.28), 2024 gas (l.41), 2025 licences (l.44).
  - EU budget 2021-2027 (l.21). Targets run 2025-2050.
- Headings in order:
  - Energy chapter: intro (l.9-10, no heading), Leading Sub-sectors l.11, Power Generation l.12, European Union Green Deal
    and FIT for 55 Package l.20, Nuclear Energy l.22, Renewable energy l.24, Photovoltaics l.27, Wind: Onshore and Offshore
    l.31, Energy Storage l.34, Hydrogen l.37, Natural Gas l.40, Web Resources l.45, contact l.64-67.
  - Environmental chapter: Overview l.73, State of the Environmental Regime l.76, Market Barriers l.79 (sub-heads l.81,
    l.83, l.85, l.87, l.89), Leading Sub-sectors l.91, Air Pollution Control l.92, Water and Wastewater Treatment l.132,
    Industrial Process and Wastewater l.155, Waste Management and Circular Economy l.181, Environmental Permitting l.205,
    Trade Shows l.209, Resources l.216, contact l.231.
- Entities and aliases:
  - Agencies and plans:
    - Ministry of Climate and Environment = "(MoCE)" (l.77); it also appears at l.47, l.182, l.189 ("Ministries of Climate
      and Environment and State Assets"), l.206 and l.218.
    - Polish Wind Energy Association = "(PSEW)" (l.33; listed at l.57).
    - National Energy Network = "(KSE)" (l.36).
    - Gaz-System manages the gas transmission pipelines (l.41).
    - Polish Statistics Office = "GUS" (l.74).
    - Polish Center for Research and Certification = "(PCBC)", "the national testing and certification office" (l.82,
      l.228).
    - Polish Geological Institute (l.44).
    - Małopolska Sejmik (l.99).
    - "National Plan for Energy and Climate" (l.26).
  - Variant names for environmental bodies. The document never says whether the inspectorate names refer to one body.
    - "the Main Inspectorate of Environmental Protection" (l.206).
    - "The General Inspectorate of Environmental Protection supervises compliance" (l.206).
    - "The Chief Inspectorate of Environmental Protection (GIOS)" (l.220).
    - "General Directorate of Environmental Protection" issues EIAs (l.206). The Resources list spells it "The General
      Directorate for Environmental Protection" (l.222).
  - One abbreviation for two names: "National Program of Municipal Wastewater Treatment (NPMWT)" (l.133) and "National Plan
    for Municipal Wastewater Management, (NPMWT)" (l.134).
  - EU court naming: "Court of Justice of the European Union (CJEU)" (l.97), "the EU Court" (l.95), "Court of Justice of
    the EU" (l.185).
  - "Renewable Energy Institute" (report source, l.28) versus the web resource "Institute for Renewable Energy" (l.63).
    The document does not equate them.
  - Abbreviations:
    - RES (renewable energy sources, l.14)
    - SMRs (Small Modular Reactors, l.23)
    - FSRU (Floating Storage Regasification Unit, l.43)
    - bcm (billion cubic meters, l.41)
    - BAT ("Best Available Technique", l.95)
    - PSD (EU Priority Substance Directive, l.158)
    - PPP (Public-Private Partnership, l.188)
    - EPC (engineering, procurement, and construction, l.189)
    - EIAs (Environmental Impact Assessments, l.206)
    - ISO, ITU ("International Telecommunications Union"), IEC (l.82)
    - Not expanded: CHPs (l.17), p.p. (l.13), VAT expanded only as "value added tax" (l.30).
  - Companies:
    - POSCO E&C, "the South Korean company" chosen by Warsaw for its waste-to-energy (WtE) plant (l.188).
    - An unnamed "Canadian company" that discovered an oil field (l.44).
  - Plants and sites:
    - Coal: Kozienice, Opole, Jaworzno, Turów (l.19).
    - Gas: Dolna Odra, Ostrołęka (l.19); new gas units in Gryfino (l.15).
    - Pumped storage: Porąbka-Żar (l.16).
    - Electrolysis plants: Konin, Oława (l.39). Konin is also a WtE city (l.188).
    - Gas infrastructure: Swinoujście gas port / LNG terminal (l.41, l.44), Baltic Pipe (l.41-42), FSRU in the Bay of
      Gdansk (l.43).
    - Gas deposits: Bronsko, Przemysl (l.44).
  - Programmes and laws:
    - "My Electricity" (l.28); "Clean Air" (l.99, l.101).
    - Polish Hydrogen Strategy (l.38); "Hydrogen Law" (l.39).
    - 2001 Environmental Protection Act (l.77); 2015 "anti-smog" law (l.94).
    - National Plan for Waste Management (l.160); National Development Plan (l.186).
    - The Act on Disclosing Information about the Environment ... of October 3, 2008 (l.208).
  - EU instruments:
    - European Green Deal (l.21); Renewable Energy Directive EU/2023/2413 (l.25).
    - Regulation (EU) No. 1025/2012 (l.82); Industrial Emissions Directive (l.95); Air Quality Directive 2008/50/EC (l.96).
    - Cohesion Policy funds, Social Climate Fund, Just Transition Fund (l.21); Modernization Fund (l.36).
    - Trans-European Networks for Energy (l.42); EU Circular Economy policy (l.187).
  - Countries:
    - United States: Intergovernmental Agreement on nuclear in 2020 (l.23); LNG supplier (l.41).
    - Qatar: LNG supplier (l.41). Norway: Baltic Pipe gas source (l.42). Russia: main pre-2022 gas supplier (l.41).
    - Germany and Sweden: import sources. Czech Republic and Slovakia: export destinations (l.18).
- Tables: none (not applicable).
- Quantitative figures, Energy chapter:
  - l.10: green-transformation spending "around 700-800 billion PLN by 2030, meaning each year 120-150 billion PLN".
  - l.13 (2024):
    - Coal share of electricity generation 56.2%, "down from 70.7% in 2022 and 4.3 p.p. less than in 2023". The 2023
      value is not printed (computed 60.5%).
    - Coal production -5.4 TWh (-5.4% y/y): hard coal -6.7 TWh (-10.2%), lignite +1.3 TWh (+3.6 %). Computed check:
      -6.7 + 1.3 = -5.4.
  - l.14: RES production 29.4%, "2.3 p.p. more than in 2023". RES production a record 49.8 TWh; lignite 36 TWh.
  - l.15: wind 24.5 TWh (14.5% of electricity generation). Gas +3.9 TWh to a record 20.6 TWh (12.2%).
  - l.16:
    - PV +34.4% y/y; wind +5.5% y/y.
    - Shares of RES generation: wind "almost half ... (49.1%)", PV 30.6%, biomass 10.8%. The three sum to 90.5% and the
      rest is not itemized (computed).
    - Pumped storage output 23.9% lower than in 2023.
  - l.17: 2024 consumption 171.3 TWh; 85.1% end-user; 14.9% own consumption and losses. Industry is the largest end user.
  - l.18:
    - "exported 13.25 GWh ... and imported 15.21 TWh" (units mixed as printed).
    - Peak demand 28.5 GW, "a 1.2 GW increase from 2023".
    - Prosumers produced 4.7% of national electricity; self-consumption is "roughly" 1.5% of national consumption.
  - l.19: last coal plants Kozienice 1,000 MW, Opole 2x900 MW, Jaworzno 910 MW, Turów 450 MW ("commissioned in the early
    2020s"). Gas plants: Dolna Odra 2 x 700 MW and Ostrołęka 750 MW.
  - l.21:
    - GHG -55% by 2030 against 1990; climate neutrality by 2050.
    - EU 2021-2027: €137 billion ($161 billion) in subsidies plus €34.2 billion ($40.2 billion) in repayable aid. This
      makes Poland "the biggest net EU beneficiary".
    - Cohesion funds: €17.9 billion ($21 billion) for RES and circular economy; €20 billion ($ 23.5 billion) for transport
      decarbonization.
    - Social Climate Fund €11.4 billion ($ 13.4 billion); Just Transition Fund about €3.85 billion ($ 4.5 billion).
    - The transformation requires "about $250 billion".
    - "By 2030, Poland's energy mix is to decrease to at least 56 percent reliance on coal."
    - No EUR/USD rate is stated; the implied ratios are about 1.17-1.18 (computed).
  - l.23: two nuclear power plants (six reactors), 6-9 GW in total. First reactor 2036, "the remaining five units coming
    online every two years until the project is completed in 2043".
  - l.25: EU 2030 binding target "at least 42.5%". In 2024 renewables reached "a record 29.4% of the mix", with installed
    capacity of 28.6 GW.
  - l.26: NECP forecast of RES capacity "from 28 GW in 2025 to 50 GW in 2030". "By 2027, Poland expects 6 GW" of offshore
    wind.
  - l.28 (PV):
    - 21.8 GW installed at the end of Q1 2025. Microgeneration 59%; "PV farms and small systems" 41%.
    - Farms above 1 MW supply "half of new capacity".
    - PV is "64% of Poland's RES capacity"; its "share of RES power generation rose to 31.5%".
    - Ranked "5th in 2024" in the EU for PV capacity increase.
    - In 2024, 141,500 new microgeneration units (1.43 GW) were connected; "My Electricity" supported 53,500 installations.
  - l.30: VAT cut from 23% to 8% for solar systems under 50 kW.
  - l.32 (wind):
    - More than 1,200 installations, "over 7,185 MW, which is about 65% of installed capacity in all types of renewable
      energy installations".
    - Nearly 160 under construction, about 2,500 MW.
  - l.33: "goal of 21% of RES by 2030". Phase II offshore support auction "scheduled for December 17th, 2025", up to 4 GW.
    PSEW: 1,000 MW of new wind needed each year.
  - l.35: storage contracted 9.5 GW (power-market auctions 2021-2028 plus supplementary auctions 2021-2025). The December
    2024 auction alone contracted a record 2.5 GW.
  - l.36: $1.09 billion storage co-financing programme (spring 2025), "over 5 GWh ... by 2028"; minimum project size
    2 MW/4 MWh.
  - l.39: Poland "produces 1/3 of a total amount of hydrogen produced in Europe".
  - l.41: "nearly 17 billion cubic meters" transmitted in 2024. Storage 3.33 bcm at end-2024; consumption about 20 bcm a
    year. Swinoujście plus Baltic Pipe can cover "about 40%" of demand; the first LNG terminal opened in 2015.
  - l.42: Baltic Pipe, September 2022, "up to 10bcm" a year from Norway.
  - l.43: FSRU contracted in 2024, operational early 2028, 12 bcm of LNG a year.
  - l.44:
    - Domestic production covers "approximately 20%" of demand.
    - Six wells completed by June 2025, with five more under way.
    - In 2025, 44 exploration licences were issued; there are 182 active production licences.
    - Deposits: Bronsko 10.8 bcm, Przemysl 8.7 bcm.
- Quantitative figures, Environmental chapter:
  - l.74: "approximately 3.2% of its GDP ($26 billion or 16%)" (GUS, data from end-2022).
  - l.75: since 2004, more than 1,000 new water treatment plants; CO2 down by more than 30%.
  - l.93: "Fossil fuels made up 70% of Poland's energy sources in 2024"; coal "expected to remain ... primary energy source
    until 2049".
  - l.95: BAT adopted July 2017; implementation "not later than August 18, 2021".
  - l.98: CJEU verdict covered 2007-2015. June 2018: "over $28 billion" for thermo-modernization.
  - l.99: Clean Air runs 2018-2032, with "almost 450,000 applications". The Kraków rule applies from September 1, 2019.
  - l.100: "approximately 285 heating sources located in 220 buildings, or approximately 0.17% of all facilities".
  - l.101: 3-4 million solid-fuel boilers, 3 million stove-fired; Clean Air contracts with "more than 370 thousand
    beneficiaries".
  - l.133: 73% of facilities under the national programme in 2020; "over 1,000 agglomerations" lack collection.
  - l.134: nitrogen and phosphorus to be cut by 75%; "$7 billion between 2017 and 2020" for 1,578 agglomerations.
  - l.156: 1,450-1,600 m3 of water per capita a year; industry uses 70%. l.157: industry use 2-3 times other EU nations.
  - l.159: over 700,000 tons of sludge a year. l.160: "60% of sludge ... incineration, a 25% increase from current levels".
  - l.182: investment "over $7 million by 2034"; recycling 55% by 2025 and 65% by 2035.
  - l.183: 38% in 2020. About $14 billion of EU money for 2021-2027, with more than $9.9 billion allocated by November
    2023.
  - l.184: over 60% of waste goes to 800 landfills; more than 1,000 non-compliant organizations; landfill must fall by 50%.
  - l.185: $6.9 billion needed for the remaining agglomerations.
  - l.188: "Eleven waste-to-energy facilities with a capacity of 200,000 tons each are slated ..., and seven have been
    already completed". Eight cities are named, "valued at a combined $1 billion".
  - l.189: almost 13 million tons of waste a year, growing by about 1 million tons a year; over 376 kg per person.
- Lists (count, with the last item):
  - Last coal plants (l.19): 4, last Turów. Gas plants: 2, last Ostrołęka.
  - Hydrogen Strategy areas (l.38): 3 (industry, the power generating sector, transport).
  - Web Resources (l.46-63): 18, from "Energy Information Administration" (l.46) to "Institute for Renewable Energy"
    (l.63).
  - Market Barriers sub-heads (l.81-90): 5, last "Slow implementation of EU environmental rules" (l.89).
  - Standards bodies recognized (l.82): 3.
  - Air-pollution technologies (l.104-130): 14, last "Small capacity energy storage" (l.130).
  - Water and wastewater technologies (l.137-153): 9, last "Testing equipment" (l.153).
  - Industrial wastewater technologies (l.163-179): 9. The items repeat the water list, but l.169 spells
    "Waste-to-energy technology" where l.143 has "Waste to energy technology". Last item "Testing equipment" (l.179).
  - WtE cities (l.188): 8 (Bialystok, Bydgoszcz, Torun, Konin, Krakow, Poznan, Gdansk, Szczecin). Warsaw is separate.
    Poznan was the first PPP; Gdansk followed.
  - Possible further WtE locations (l.189): 8, last "the Lublin region".
  - Waste technologies (l.192-204): 7, last "Recycling process expertise" (l.204).
  - Permitting regulators (l.206): 3.
  - Trade Shows (l.211-215): 3.
    - "POLECO Poznan, October 14-16.10.2025"
    - "GREENPOWER Poznan, 22-26.03.2026"
    - "Waste Management SOS Expo, Hotel Novotel Warszawa Airport, Warsaw, 2026 TBD"
  - Environmental Resources (l.218-230): 7, last "EU Environmental Implementation Review 2025" (l.230).
- Forecasts, guidance, deadlines, effective dates:
  - Targets and plans:
    - 700-800 billion PLN by 2030 (l.10).
    - GHG -55% by 2030 and neutrality by 2050 (l.21); coal "at least 56 percent" by 2030 (l.21).
    - Nuclear 2036 to 2043 (l.23).
    - 2030 renewables: EU 42.5% (l.25), NECP 50 GW (l.26) and the "21% of RES" goal (l.33).
    - Offshore wind 6 GW by 2027 (l.26); storage over 5 GWh by 2028 (l.36).
    - Hydrogen Strategy to 2030 with an outlook to 2040 (l.38).
    - Coal primary until 2049 (l.93); Clean Air until 2032 (l.99); recycling 2025/2035 (l.182).
  - Scheduled dates that fall before the April 2026 publication dates, with no outcome reported:
    - Phase II offshore wind auction on December 17, 2025 (l.33).
    - Warsaw WtE modernization "will be finished by 2025" (l.188).
    - The 55% recycling level "by 2025" (l.182).
    - POLECO show, October 2025 (l.211).
  - The FSRU is "to be operational early 2028" (l.43).
- Dated events:
  - 2001 Environmental Protection Act (l.77).
  - 2004 EU accession (l.75, l.77, l.93).
  - October 3, 2008 EIA Act (l.208).
  - 2015: LNG terminal opened (l.41) and anti-smog law passed (l.94).
  - July 2017: BAT standards adopted (l.95).
  - May 2018 CJEU judgment (l.97); June 2018 $28 billion allocation (l.98); Clean Air launched 2018 (l.99).
  - September 1, 2019: Kraków fuel rule (l.99).
  - 2020 US-Poland nuclear Intergovernmental Agreement (l.23).
  - "At the beginning of 2021" the EU Court declared the BAT conclusions invalid (l.95). Hydrogen Strategy adopted 2021
    (l.38). BAT deadline August 18, 2021 (l.95).
  - September 2022: Baltic Pipe inaugurated (l.42).
  - November 2023: more than $9.9 billion allocated (l.183).
  - 2024: FSRU contracted (l.43). December 2024: power-market auction contracted 2.5 GW of storage (l.35).
  - January 2025: Hydrogen Law in force (l.39). Spring 2025: storage programme (l.36).
  - By June 2025: wells completed (l.44). July 2025: oil discovery (l.44).
- Hedged claims (hedge word and what it attaches to):
  - l.16: the pumped-storage drop is "most likely due to" the Porąbka-Żar shutdown. The hedge covers the cause, not the
    23.9% figure.
  - l.23: "Poland is also considering how SMRs can be deployed"; companies "are considering investments in SMRs". These
    are considerations, set against the firm "plans to build" and the "scheduled" first reactor.
  - l.26: "forecasts"; "Poland expects 6 GW".
  - l.33: "PSEW estimates"; the auction "is scheduled".
  - l.43: FSRU "is to be operational"; "with plans for possible expansion"; the tanker "would also enable" bunkering.
  - l.93: coal "is expected to remain" primary until 2049.
  - l.95: "Virtually all Polish coal power plants do not comply".
  - l.100: "Officials estimate that the resolution was successfully implemented".
  - l.158: PSD "already formally in force ... but its impact ... is limited".
  - l.160: "There is also a proposal to use treated sludge as a biomass fuel" (a proposal only).
  - l.189: PPPs "could yield opportunities"; "More waste-to-energy facilities could be built".
- Rounded prose beside exact figures: there are no tables. Figures stated twice:
  - RES 29.4% at l.14 and l.25 (agree).
  - PV share of RES generation: 30.6% at l.16 versus 31.5% at l.28.
  - Rounded wording: "almost half (49.1%)" (l.16); "about 65%" (l.32); "nearly 17", "about 20", "about 40%" (l.41).
- Operative definitions, rules and scope exceptions:
  - l.29: curtailment "mainly affects non-micro-PV installations (those are curtailed by over-voltage automation)". It
    happens around noon, "initially on holidays ... now also on weekdays".
  - l.30: the VAT cut covers "Solar power systems with less than 50 kW". PV costs "can also offset income"; auctions fund
    large-scale plants.
  - l.36: storage eligibility is "at least 2 MW/4 MWh, connected to the distribution and transmission network at all
    voltage levels".
  - l.82: Regulation 1025/2012 "only recognizes standards from three international bodies"; "In Poland, the CE mark is
    required."
  - l.84: US performance-based standards versus EU design-based standards. l.86: precautionary versus risk-based approach.
  - l.94: the anti-smog law lets local authorities ban burning coal in private homes.
  - l.99: Kraków allows "only gaseous fuels or light fuel oil". Clean Air "targets individual homeowners".
  - l.184: landfill waste to be cut by 50%.
  - l.186: municipal and regional governments are responsible for waste; "cities or voivodships will issue future
    contracts".
  - l.187: EU policy ranks incineration "on the penultimate place".
  - l.207: integrated permits are "required when activities could cause harm to the environment in general" and "renewed
    every five years". Single/separate permits cover activities that "may affect an aspect of the environment ... such as
    air and water" and are "valid for a maximum of 10 years" (l.208).
  - l.208: an EIA is required where a project "may have a serious impact on the environment or a Natura 2000 area".
    Natura 2000 is defined as "an area that is protected because of its environmental significance".
- Amendments or contradictions (recorded neutrally; the document states no precedence):
  - Stated amendments:
    - The Hydrogen Law is "An amendment to the Energy Law" in force from January 2025 (l.39).
    - The Environmental Protection Law amendment responds to the May 2018 CJEU judgment (l.97).
    - The BAT conclusions were declared invalid in early 2021, "and after amendment has accepted the new BAT conclusions"
      (l.95).
    - "the amendment to the act on water law" (l.185).
    - EIR 2022 led to an infringement case before the Court of Justice of the EU (l.185).
  - Internal inconsistencies:
    - Nuclear timing (l.23): a first unit in 2036 plus five more "every two years" ends in 2046 (computed), against
      "completed in 2043".
    - Shares of RES capacity: PV "64% of Poland's RES capacity" (l.28) versus wind "about 65% of installed capacity in
      all types of renewable energy installations" (l.32). Together they exceed 100%.
    - Capacities: PV 21.8 GW (end-Q1 2025, l.28) plus wind 7,185 MW (l.32) is about 29.0 GW (computed). That exceeds the
      2024 RES capacity of 28.6 GW (l.25), and the NECP's 2025 figure is 28 GW (l.26).
    - Wind share of RES generation: 24.5/49.8 = 49.2% (computed) versus the printed 49.1% (l.16).
    - Electricity trade: exports in GWh versus imports in TWh (l.18).
    - Three 2030 renewables measures are not reconciled: ≥42.5% (l.25), 21% (l.33) and 50 GW (l.26).
    - Coal measures use different bases: "at least 56 percent reliance on coal" by 2030 (energy mix, l.21), 56.2% of
      2024 electricity generation (l.13), and "Fossil fuels made up 70% of Poland's energy sources in 2024" (l.93).
    - WtE counts: 11 slated, 7 completed, 8 cities named (l.188).
    - "$7 million by 2034" (l.182) sits beside billion-scale figures (l.183, l.185).
    - Unexplained figures: "($26 billion or 16%)" (l.74); "a 25% increase" with no percent-or-points convention (l.160).
    - Clean Air counts different things: "almost 450,000 applications" (l.99) versus contracts with "more than 370
      thousand beneficiaries" (l.101).
    - Review editions: text cites EIR 2022 (l.78, l.185), Resources lists EIR 2025 (l.230).
    - Coal dependence wording: "one of the most coal-dependent countries in the EU" (l.9) versus "the most fossil
      fuel-reliant economy in the EU" (l.93).
- Notes:
  - l.19 has an unclosed parenthesis: "Opole (2x900 MW, Jaworzno (910 MW)".
  - l.74 has an unclosed parenthesis: "(GUS-last data from the end of 2022,".
  - l.16 typo: "Wind power for responsible for".
  - The Kraków anti-smog resolution was adopted by the Małopolska Sejmik (l.99).
- Coverage: full (l.1-234). No gaps.

## D12 - Portugal CCG: "Energy"

- Source: `text/D12.txt` (65 lines, 18,870 chars), from `docs/ccg_energy_cleantech_sectors_portugal.txt`; capture
  doc 16.
- Written or submitted by: U.S. International Trade Administration (l.3). The chapter names no specialist and has no
  contact block; l.49 refers only to "the U.S. Commercial Service in Portugal". Cited sources: Eurostat (l.11), APREN
  (l.17-19), "Portugal 2021 Energy Policy Review" and NECP (l.20), "the government" (l.25), U.S. Department of Energy
  data (l.33), DGEG (l.37), LNEG (l.43).
- Type, date, edition: one chapter, `## Energy` (l.5). "Last published: 2026-04-16" (l.6); "Source:
  https://www.trade.gov/country-commercial-guides/portugal-energy" (l.7). No Environmental Technologies chapter.
- Period covered: calendar years.
  - 2024: Eurostat data (l.11), EV record in December 2024 (l.39).
  - "between January 1 and November 30, 2025" for Mainland Portugal (l.17); November 2025 alone (l.18).
  - 2022 mining data (l.37); 2019 baseline and 2030 targets (l.20); 2050 goals (l.10, l.13).
- Headings in order: Overview l.9, Leading Sub-sectors l.15, Renewable Energy l.16, Green Hydrogen l.23, Natural Gas
  l.28, Mining l.35, Opportunities l.44, Key Government Regulatory Agencies l.50, Resources l.56.
- Entities and aliases:
  - APREN: "Portuguese Association of Renewable Energy (APREN)" (l.17); listed as "Portuguese Association for Renewable
    Energy" (l.53).
  - RNC2050 = "Roadmap for Carbon Neutrality 2050" (l.10).
  - NECP: "Integrated National Energy and Climate Plan (NECP)" (l.20); "National Energy and Climate Plan for 2030"
    (l.12). The text does not explicitly equate the two.
  - PNI 2030 = "National Investment Program 2030", approved 2023 (l.14).
  - EN-H2 = "National Strategy for Hydrogen" (l.24); l.54 "National Strategy for Hydrogen – Public Consultation".
  - DGEG = Directorate-General for Energy and Geology (l.37, l.52). LNEG = National Laboratory of Energy and Geology
    (l.43).
  - Other bodies: National Energy Poverty Observatory (l.13); International Offshore Energy Testing Center and the
    Recovery and Resilience Program (l.14); Ministry of Environment and Climate Change (l.51); Portuguese Association for
    the Extractive and Manufacturing Industry (l.55); INEGI (l.62).
  - Resource publishers: European Commission, Energy Global, Pordata, Energy Institute, IEA (l.57-61).
  - Places:
    - Sines: coal plant closed 2021, port, LNG terminal, hydrogen and ammonia projects (l.13, l.27, l.29-34, l.47-48).
    - Pego: coal plant closed 2021 (l.13).
    - Madeira: served by the "virtual LNG pipeline" (l.31).
    - "Mainland Portugal" (l.17).
  - Countries: Spain (marginal pipeline inflows, l.30; lithium cooperation, l.42); Russia (reliance "minimal", l.33); US.
- Tables: none (not applicable).
- Quantitative figures:
  - l.10: "ranking 11th among EU member states" for energy-import dependence. Fossil-fuel dependence "projected to decline
    to roughly 65 percent" by 2030. RNC2050: energy import dependence "below 19 percent by mid-century".
  - l.11:
    - Installed capacity: "approximately 8 GW of hydropower, more than 5 GW of onshore wind, and nearly 4 GW of solar".
    - "95 percent of its electricity demand with renewable sources during several periods in 2024".
    - Eurostat: "ranked second in the EU in 2024, with approximately 87.5 percent of net electricity generation" from
      renewables.
  - l.12: "at least 80 percent renewable electricity generation" (NECP 2030 and the carbon-neutrality roadmap).
  - l.17: "44 303 GWh" generated January 1 to November 30, 2025, in Mainland Portugal; "75.1 %" renewable.
  - l.18: November 2025: "74.3 %" renewable, "approximately 3 081 GWh ... out of 4 147 GWh". Computed check: 3,081/4,147
    = 74.3%.
  - l.19: in some months, wind "around 25 %–26 %" and solar "up to 20 %".
  - l.20: renewable installed capacity "from 14.1 GW in 2019 to around 24.7 GW by 2030". EIA exemption planned for solar
    "below 50 MW".
  - l.22: "three-quarters or more of total generation through most of 2025".
  - l.25: hydrogen viability benchmark "around or below 25 €/MWh".
  - l.33: "the first European country to receive U.S. LNG in 2016".
  - l.37: mining and quarrying production of "approximately €1.3 billion in 2022", with exports "at a similar level";
    "close to 9,000 workers".
  - l.38: lithium "around 60,000 metric tons"; "largest identified lithium reserves in Europe"; "top ten globally".
  - l.39: December 2024: "more than 10,000 electric vehicles registered in a single month".
- Lists (count, with the last item):
  - Installed-renewables trio (l.11).
  - Energy Poverty Strategy means (l.13): 4, plus the Observatory.
  - Principal renewable sources (l.20): 4 (hydro, wind, solar, biomass).
  - Minerals (l.36): metallic copper, tin, lithium, tungsten; stones marble, limestone, granite. Portugal is among the
    EU's most significant producers of copper, tin and tungsten.
  - Lithium best practices (l.43): 3.
  - Opportunities paragraphs (l.45-49): 4 areas (renewables l.46, green hydrogen l.47, LNG l.48, mining l.49). Mining
    (lithium, copper, tungsten) comes last.
  - Renewables products (l.46): 10, last "engineered components".
  - Hydrogen sourcing (l.47): 5, last "engineering services".
  - LNG opportunities (l.48): 6, last "logistics services".
  - "Key Government Regulatory Agencies" (l.51-55): 5, last "Portuguese Association for the Extractive and Manufacturing
    Industry". The list includes trade associations and a public-consultation page.
  - Resources (l.57-62): 6, last "INEGI – Institute of Science and Innovation in Mechanical and Industrial Engineering".
- Forecasts, guidance, deadlines, effective dates:
  - About 65% fossil dependence by 2030; import dependence under 19% by 2050; at least 80% renewable electricity by 2030.
  - Hydrogen strategy to lower gas dependence by 2030 (l.13). Energy poverty to be eliminated by 2050 (l.13).
  - Offshore testing centre "by 2026" (l.14); 24.7 GW by 2030 (l.20).
  - "Portugal must significantly increase installed capacity in solar, wind, and hydropower by 2030" (l.46).
- Dated events:
  - 2016: first US LNG cargo (l.33).
  - 2021: coal exit, closing Sines and Pego (l.13).
  - Since 2022: gas demand reduced (l.32).
  - 2023: PNI 2030 approved (l.14).
  - January 2024: National Long-Term Energy Poverty Mitigation Strategy (2023–2050) approved (l.13).
  - December 2024: EV record (l.39).
- Hedged claims:
  - l.10: "is projected to decline".
  - l.19: the breakdown "isn't fully published yet".
  - l.20: "has also planned to streamline permitting, including stopping environmental impact assessments for solar
    projects with capacities below 50 MW". This is a plan, not an enacted rule.
  - l.21: "decision-making tends to be bureaucratic"; "Most major projects will likely involve joint ventures". "likely"
    attaches to joint-venture involvement.
  - l.25: the threshold is "often discussed ... around or below 25 €/MWh ... it should be understood as an indicative
    benchmark rather than a formal government target". This is an explicit scope limit.
  - l.30: Sines "has the potential to function as an Atlantic LNG service station".
  - l.31: "can be replicated"; "Scaling this concept would open".
  - l.37: "medium-term projections indicate continued growth"; 2023-2024 figures "still being released".
  - l.43: LNEG "indicate that modern lithium mining can be conducted with limited environmental risk when best practices
    are applied". The condition is the "when" clause; the next sentence adds "Nevertheless ... remains subject to public
    scrutiny".
- Rounded prose beside exact figures: there are no tables. "three-quarters or more ... through most of 2025" (l.22)
  stands beside 75.1% for January-November (l.17) and 74.3% for November (l.18).
- Operative definitions, rules and scope exceptions:
  - Green hydrogen: produced by electrolysis using renewable electricity (l.26).
  - l.41: lithium "should be processed domestically rather than exported in raw form".
  - l.42: tender specifications "typically mandate social benefit plans" and EIA compliance.
  - l.20: the planned EIA exemption covers solar under 50 MW.
- Amendments or contradictions:
  - Different scope and period: 87.5% of national net generation in 2024 (Eurostat, l.11) versus 75.1% for Mainland
    Portugal, January-November 2025 (APREN, l.17).
  - "three-quarters or more ... through most of 2025" (l.22) versus November at 74.3% (l.18).
  - Two different measures: "fossil fuel dependence" of 65% by 2030 versus "energy import dependence" under 19% (l.10).
  - Installed capacity of about 17 GW (computed from l.11) sits beside the NECP figures of 14.1 GW in 2019 and 24.7 GW
    by 2030 (l.20).
  - "Portugal no longer relies on coal" (l.19) is consistent with the 2021 exit (l.13).
- Notes: the document uses spaces as thousands separators ("44 303 GWh") and a space before "%".
- Coverage: full (l.1-65). No gaps.

## D13 - Romania CCG: "Energy"

- Source: `text/D13.txt` (71 lines, 13,196 chars), from `docs/ccg_energy_cleantech_sectors_romania.txt`; capture doc 20.
- Written or submitted by: U.S. International Trade Administration (l.3). Contact: "Maria Petrescu, Commercial
  Specialist" (l.66-68). Cited sources: Romanian Energy Ministry (l.12), International Renewable Energy Agency (l.44),
  ANRE (l.61), Transgaz development plan (l.54).
- Type, date, edition: one chapter, `## Energy` (l.5). "Last published: 2026-06-02" (l.6); "Source:
  https://www.trade.gov/country-commercial-guides/romania-energy" (l.7).
- Period covered: calendar years. April 2025 electricity (l.24); "as of May 2025" capacity shares (l.52); the
  Transgaz plan for 2024-2033 (l.54); "In 2025" items (l.56, l.61, l.64); targets 2025-2050; Caragele to 2097.
- Headings in order: Overview l.9, Leading Sub-sectors l.25, Nuclear Sector l.26, Oil and Gas l.33, LNG at the Black Sea
  l.38, Coal Sector l.41, Renewable Energy l.43, Opportunities l.45, Nuclear l.46, Power Production and Distribution
  l.51, Oil and Gas l.53 (the heading repeats), Renewables l.55, Wind Energy l.57, PV Energy l.60, Biomass Energy l.63,
  contact l.66.
- Entities and aliases:
  - One abbreviation for two names in the same line (l.22): "Romanian Resilience and Recovery Plan (PNRR)" and "National
    Recovery and Resilience Plan (PNRR)".
  - Romgaz: "Romanian state-owned Romgaz" (l.35); "majority-owned by the Romanian Government" (l.39).
  - OMV Petrom: "majority-owned by Austria's OMV" (l.35). Neptun Deep is "a joint venture between OMV Petrom ... and
    Romgaz".
  - BSOG = "Black Sea Oil & Gas" (l.37).
  - BRUA = Bulgaria-Romania-Hungary-Austria pipeline (l.40, l.54). T1 = Transbalkan pipeline (l.40).
  - Transgaz: "the national transport system operator, hereinafter "SNT"" (l.54). SNT is then used for the system
    itself ("Transgaz SNT pipelines").
  - CE Oltenia = Complexul Energetic Oltenia (l.42).
  - ANRE = "National Regulatory Authority" (l.61).
  - Other abbreviations: CfD = Contracts for Difference (l.59); SMRs = small modular reactors (l.27); CANDU = "Canadian
    Deuterium Uranium" (l.28).
  - Companies: Monsson (PV developer) and Dama Solar (l.62). Programme: Casa Verde Fotovoltaice ("Green PV Home", l.44).
  - Spelling variants: "Cernavodă" (l.23, l.28, l.30, l.31, l.48, l.49) and "Cernavoda" (l.47).
  - Places:
    - 2025 projects: Mintia, Iernut, Navodari, Răstolița (l.15-21).
    - Nuclear: Doicești (l.27, l.32, l.50).
    - Gas: Caragele (l.36), Midia (l.37), Port of Constanta (l.39), Tuzla-Podisor (l.40), Isaccea and Negru Voda (l.54).
    - Coal-to-gas sites: Ișalnița and Turceni (l.42).
    - PV project: Arad County (l.62).
  - Countries:
    - Electricity trade partners: Hungary, Bulgaria, Serbia, Ukraine, Moldova (l.23).
    - Turkey, via Istanbul and the Bosphorus (l.39); Austria, through OMV (l.35).
    - US: Intergovernmental Cooperation Agreement (l.47); "re-gasified U.S. LNG" via BRUA (l.40).
- Tables: none (not applicable).
- Quantitative figures:
  - l.11: GHG "by 78% by 2030"; climate neutrality 2050.
  - l.12: "expects around 2.5 GW of new power capacity to be commissioned" (2025), following "1.2 GW ... put into
    operation in 2024".
  - l.15-21: 2025 projects: Mintia gas plant 1 GW ("expected at the end of 2025"), Iernut gas plant 430 MW, Navodari gas
    CHP 80 MW, Răstolița hydro 30 MW. Computed sum: 1,540 MW.
  - l.22: PNRR projects to bring 1.2-1.5 GW of renewables; battery storage "to double its capacity, reaching 400-500 MWh";
    "at least 2.5 GW of new capacity ... including at least 600 MW of base-load production".
  - l.24, verbatim: "In April 2025, Romania's electricity production value amounted to 3.734 TWh, out of which the energy
    output consisted of 31.9 TWh, while imports amounted to 30.14 TWh. Romania's own electricity output and imports
    totaled 11.791 TWh combined in the review period, up 0.5% year-on-year. Domestic electricity production alone
    dropped by 16.6% to 8.714 TWh." The same line gives "approximately 50%" renewable: "hydropower at around 30%, wind at
    11%, photo-voltaic at 13%, and biomass at 0.1%".
  - l.27: Doicești "462 MWe" SMR by 2030; "a total of 2,480 MWe/2.48 GWe by 2040". This is repeated at l.50.
  - l.28: Units 1 and 2 are CANDU-6 pressurized heavy water reactors, "individually produce 650 MWe". Units 3 and 4 "will
    individually produce 700 MWe" and are due by 2032.
  - l.35: Neptun Deep: about 8 bcm, production 2027. Drilling of the "first of ten wells began in March 2025".
    Investment "up to EUR 4 bln".
  - l.36: Caragele "recovered 26.71% of its total recoverable reserves", peak production 2021, economic limit in 2097,
    "approximately 4% of the country's daily output".
  - l.39: Constanta LNG terminal "€ 900 million", "completion deadline of 2026".
  - l.40: "308.3-kilometre Tuzla-Podisor pipeline, expected to be completed in 2025".
  - l.42: "Active coal plants had an overall 1.9 GW in April 2024, compared to 5.3 GW in 2012."
  - l.44: "2030 renewables target of 34% (previously set to 30.7%)"; "another 2 GW" (1 GW large-scale, 1 GW
    self-consumption); IRENA: "4.7 GW of installed solar capacity at the end of 2024".
  - l.52, "as of May 2025": "30.36% Hydro; 11.47% Coal; 18.85% Hydrocarb; 25.3% Nuclear; 13.2% Solar; 0.8% Biomass".
    Computed sum 99.98%. There is no wind category.
  - l.58: wind "projected to reach 3.47 GW in 2025 ... compared to the 3 GW capacity over the past five years"; "at least
    3 GW of additional renewable capacity by 2026".
  - l.59: CfD round 2: "3,472 MW, financed with €3 billion from the Modernization Fund"; "1,472 MW of solar and 2,000 MW of
    onshore wind"; "completed by the third quarter of 2025". Computed check: 1,472 + 2,000 = 3,472.
  - l.61: ANRE: "in 2025, Romania currently has a total of 5 GW installed solar capacity", plus "an additional 2 GW"
    (1+1).
  - l.62: Monsson PV "for 1.04 GW", "final approvals in December 2024", "total estimated value of 1 billion with Dama Solar
    valued at 800 million € and an additional 200 million € to be spent on batteries"; "over 1,000 local individuals".
  - l.64: biomass in 2025: "50-80 million MWh, corresponding to 21.5 to 35.8 million tons". The NECP 2021-2030 includes "a
    total of 2.5 GW of new power capacity".
- Lists (count, with the last item):
  - 2025 projects (l.15-21): 4, last "Răstolița hydropower plant - 30 MW".
  - Electricity trade partners (l.23): 5, last Moldova.
  - Civil nuclear efforts (l.30-32): numbered 1-3, last "Doicești – Building Romania's First Small Modular Reactor".
  - Opportunities for US companies (l.48-49): 2 bullets marked "·", last "Refurbishing Units 1 ...".
  - SMR opportunity areas (l.50): 6, last "manufacturing".
  - BRUA gas sources (l.40): 3.
  - Installed-power shares (l.52): 6 categories.
  - Transgaz plan projects (l.54): 5, last "modernization of stations Isaccea and Negru Voda".
  - Biomass regions (l.65): "eight", matching 8 items, last "South Plain".
- Forecasts, guidance, deadlines, effective dates:
  - Energy Strategy 2025-2035, "launched in 2024" (l.10).
  - Coal: 2026 deadline and exit (l.42); official coal phase-out 2032 (l.42).
  - Nuclear: SMR by 2030 (l.27, l.50); Cernavodă Units 3-4 by 2032 (l.28); 2,480 MWe by 2040 (l.27, l.50).
  - Neptun Deep 2027 (l.35); Constanta LNG terminal 2026 (l.39); renewables 34% by 2030 (l.44); 3 GW more by 2026 (l.58).
  - Scheduled dates before the June 2026 publication date, with no outcome reported:
    - Mintia "expected at the end of 2025" (l.15).
    - Tuzla-Podisor 2025 (l.40).
    - CfD "by the third quarter of 2025" (l.59).
    - Wind "projected" at 3.47 GW in 2025 (l.58).
    - About 2.5 GW commissioned in 2025 (l.12).
- Dated events:
  - 2012: 5.3 GW of coal capacity (l.42).
  - Since 2020: BRUA prioritized (l.40).
  - 2021: Caragele peak (l.36). July 28, 2021: US-Romania Intergovernmental Cooperation Agreement entered into force
    (l.47).
  - 2024: Energy Strategy launched (l.10); 1.2 GW commissioned (l.12). April 2024: coal capacity 1.9 GW (l.42).
  - December 2024: Monsson final approvals (l.62).
  - March 2025: Neptun Deep drilling began (l.35).
- Hedged claims:
  - l.12: "expects around 2.5 GW".
  - l.22: "are expected to bring"; "is expected to double"; "will add at least 2.5 GW".
  - l.35: "on track for production in 2027"; "expected to double Romania's gas production and potentially make it a net
    exporter". "potentially" attaches only to net-exporter status.
  - l.36: "Based on economic assumptions, production will continue until ... 2097".
  - l.42: "is expected to decrease".
  - l.58: "is projected to reach".
  - l.59: "is expected to be completed".
  - l.62: "on its way to have the biggest PV project in Europe".
- Rounded prose beside exact figures: there are no tables. Figures stated more than once:
  - "approximately 50%" renewable, beside shares that sum to 54.1% (computed, l.24).
  - 2,480 MWe (l.27 and l.50).
  - "2 GW" in two contexts: the 34% target (l.44) and ANRE 2025 (l.61).
  - "2.5 GW" in three framings: the Energy Ministry's 2025 figure (l.12), "at least 2.5 GW" from the PNRR investments
    (l.22), and the NECP 2021-2030 total (l.64).
- Operative definitions, rules and scope exceptions:
  - Units 1-2: "pressurized heavy water reactors that use Canadian Deuterium Uranium technology (3rd generation, CANDU-6
    technology)" (l.28). The SMR is also called "3rd generation technology" (l.27, l.50).
  - Casa Verde Fotovoltaice covers residential solar "under the national net metering regime" (l.44).
  - CfD is "to provide revenue stability" (l.59).
  - Neptun Deep is "the first deepwater offshore project in Romania" (l.35).
  - Constanta rationale: the Black Sea lacks an LNG terminal, which gave Turkey leverage over tankers (l.39).
- Amendments or contradictions (neutral):
  - Revision stated by the document: the 2030 renewables target is "34% (previously set to 30.7%)" (l.44).
  - Coal dates in one paragraph (l.42): "strict deadline to phase out coal by 2026", "its 2026 exit", CE Oltenia
    replacement "by 2026", and "officially planning to complete its coal phaseout by 2032".
  - April 2025 figures (l.24): the parts (31.9 TWh output, 30.14 TWh imports) exceed the stated whole (3.734 TWh).
    Output plus imports is given as 11.791 TWh and production as 8.714 TWh (computed difference 3.077).
  - Nuclear total of 2,480 MWe by 2040 (l.27, l.50) versus the stated unit sizes 2×650 + 2×700 + 462 = 3,162 MWe
    (computed).
  - Refurbishment scope: "Refurbishing Units 1 & 2" (l.30) versus the agreement's "refurbishing Unit 1" (l.47) and the
    bullet "Refurbishing Units 1" (l.49).
  - Constanta LNG terminal: "currently in the process of building" versus "is a proposal by Romgaz" (l.39). The Transgaz
    plan lists "a future LNG terminal" (l.54).
  - Solar: 4.7 GW at end-2024 (IRENA, l.44) versus 5 GW in 2025 (ANRE, l.61).
  - The May 2025 capacity shares have no wind category (l.52), while wind is put at 3.47 GW (l.58).
  - Biomass energy per ton differs between the ends of the range: about 2.33 MWh/t versus about 2.23 MWh/t (computed,
    l.64).
  - The Monsson value of "1 billion" has no currency in that clause; 800 + 200 million € = 1,000 million € (computed).
- Notes: "European Green Pact" (l.34). Wind and PV each have a "hub" aim (l.61).
- Coverage: full (l.1-71). No gaps.

## D14 - South Africa CCG: "Energy" and "Environmental Technology"

- Source: `text/D14.txt` (114 lines, 17,280 chars), from `docs/ccg_energy_cleantech_sectors_south_africa.txt`; capture
  doc 12.
- Written or submitted by: U.S. International Trade Administration (l.3).
  - Energy contact: "Contact in Johannesburg, South Africa: Mpilo.Mahlangu@trade.gov", "Phone: +27-11- 290-3120" (l.56-60).
  - Environmental contact: "Commercial Specialist for the Envirotech Sector in Cape Town ... Felicity.Nagel@trade.gov",
    "+27 21 702 7363" (l.108-111).
  - Cited sources: Eskom estimates (l.22), "World Wild Fund for Nature 2025" (as printed, l.67), SAICE and the 2030 Water
    Resources Group (l.68), the DWS Blue Drop report (l.69), Johannesburg Water (l.70).
- Type, date, edition: two chapters.
  - `## Energy` (l.5): "Last published: 2026-06-01" (l.6); "Source:
    https://www.trade.gov/country-commercial-guides/south-africa-energy" (l.7).
  - `## Environmental Technology` (l.62): "Last published: 2026-06-01" (l.63); "Source:
    https://www.trade.gov/country-commercial-guides/south-africa-environmental-technology" (l.64).
- Period covered: calendar years.
  - Prices 2008-2023 (l.10); events through September 2025 (l.17).
  - Some dates have no year: "as of February" (l.11); "draft regulations in April", "pre-qualification tender in July"
    (l.26).
  - "2023/2024 audit cycle" (l.69); the 2025 SONA (l.68).
- Headings in order:
  - Energy chapter: Overview l.9, "State Owned Utility" (fused into the start of l.11), Market Reforms l.12, "REIPPPP:"
    (inline at l.14), Advanced Gas Turbine Engine Technologies and LNG Imports l.15, Advanced Nuclear Energy Technologies
    l.19, Energy Services l.21, Electricity Transmission and Distribution l.24, Sub-Sector Best Prospects l.27, Major Shows:
    l.47, Resources: l.51, For More Information: l.56.
  - Environmental chapter: Overview l.66. Several heads are fused into paragraph starts: "Water Scarcity" (l.67),
    "Statistics" (l.68), "Water and Wastewater Management" (l.71), "Solid Waste Management" (l.72), "Limpopo" (l.74).
    Then Opportunities l.73, Resources l.101, Key Contacts l.103, For More Information l.108.
- Entities and aliases:
  - Eskom: "state-owned utility Eskom" (l.10), "Eskom Holdings" (l.13), "Eskom Holdings Limited" (l.53).
  - Market reforms:
    - NTCSA = National Transmission Company of South Africa (l.13, l.26).
    - ERA Act = "Electricity Regulation Amendment (ERA) Act" (l.13).
    - TSO = independent transmission system operator (l.13).
  - REIPPPP = "Renewable Energy Independent Power Producer Procurement Programme" (l.14). It is spelled "Program" at l.30.
  - Gas and LNG:
    - OCGT = open cycle gas turbine (l.16).
    - TNPA = Transnet National Ports Authority (l.17).
    - Vopak, "Dutch terminal operator", and Transnet Pipelines (l.17).
    - Supreme Court of Appeal (l.17).
  - Nuclear:
    - NNR = National Nuclear Regulator (l.20).
    - Necsa = Nuclear Energy Corporation of South Africa (l.20).
    - SAFARI-1 research reactor at Pelindaba (l.20); Koeberg plant near Cape Town (l.20).
  - Other abbreviations: C&I = commercial and industrial (l.22); DSM = Demand-Side Management (l.34); SMRs (l.20, l.46).
  - Transmission programme bodies:
    - "the Department of Electricity and Energy" (l.26) = "Department of Electricity and Energy (DEE)" (l.52).
    - National Treasury (l.26); IFC = "the World Bank's International Finance Corporation" (l.26).
    - CGV = credit guarantee vehicle (l.26); ITPO = Independent Transmission Projects Office (l.26); BOOT =
      Build-Own-Operate-Transfer (l.26).
  - Resources and events: Fitch Solutions and Horizon Grand View Research (l.54-55); CTICC (not expanded, l.50).
  - People:
    - President Ramaphosa (l.13, l.68).
    - "Minister of Electricity and Energy Kgosientsho Ramokgopa" (l.16).
    - "Minister of Mineral and Petroleum Resources Gwede Mantashe" (l.18).
  - Environmental chapter:
    - "2025 State of the Union Address (SONA)" (as printed, l.68).
    - SAICE = "South African Institute for Civil Engineering" (l.68).
    - One abbreviation for two names: "Department of Water and Sanitation (DWS)" (l.69) and "Department of Human
      Settlement, Water, and Sanitation (DWS)" (l.104).
    - Blue Drop report (l.69); Johannesburg Water (l.70).
    - Mokolo Crocodile Water Augmentation Project (Phase 2A); Medupi and Matimba Power Stations; Lephalale Municipality
      (l.74).
    - Water Research Commission; WISA = Water Institute of Southern Africa; Rand Water (l.105-107).
  - Places: Richards Bay; Port of Ngqura in the Eastern Cape Province (l.17); Karoo Basin (l.18); the Northern, Western
    and Eastern Cape provinces (l.25); Johannesburg (l.70); "Kwa-Zulu Natal area" (l.67); Limpopo and Lephalale (l.74).
- Tables: none (not applicable).
- Quantitative figures:
  - l.10:
    - Coal provides "approximately 80 percent" of electricity.
    - "Behind-the-meter private solar installations totaled more than 7 GW, exceeding the installed capacity of
      utility-scale projects".
    - Peak demand is "currently less than 32 GW".
    - "Between 2008 and 2023, electricity prices rose by 720 percent".
  - l.11: municipal debt to Eskom "more than $6 billion (R107 billion) as of February".
  - l.13: ERA Act signed August 2024; TSO "within five years"; NTCSA began operations July 2024.
  - l.14 (REIPPPP):
    - "over 6,280MW of generation capacity" built.
    - "Since the program's 2011 inception, 93 wind and solar projects generating more than 6 GW of electricity are
      operational, with an additional 2 GW ... under construction".
    - "$15 billion (R272.5 billion)" invested; "88 percent decrease in solar tariffs and a 70 percent decrease in wind
      tariffs".
  - l.16: the country "could commit to 300 petajoules of gas demand per year"; industrial users "facing a gas supply
    shortage in 2030".
  - l.17 (Richards Bay):
    - Phase 1: "two million tons of LNG per year", operational date 2028; "five million tons per year by the second
      quarter of 2030".
    - Vopak final investment decision targeted for 2026.
    - Eskom "3 GW gas-to-power plant", "targeting 2030".
  - l.20 (nuclear):
    - Nuclear is "just over 6 percent" of output.
    - Koeberg: two reactors, "combined generating capacity of 1,830 MW". Unit 1 extended 20 years to July 2044.
    - Plans for "10 GW of new nuclear ... over the next decade". Necsa to break ground in 2026.
  - l.22: rooftop PV embedded generation "now totaling 7.3 GW, registering a 215 percent increase since Eskom first
    published its estimates in August 2022".
  - l.23: storage market "expected to grow to $1,461 million by 2030".
  - l.25: "more than 14,000 km of transmission lines over the next 10 years, equivalent to a 325 percent increase in the
    current build rate"; cost "more than $13 billion (R250 billion)".
  - l.26: "tenders for seven corridors by the end of 2025".
  - l.67: rainfall "around half of the global average".
  - l.68: "R23 billion (USD1.2 billion)" for water projects; "an additional R1 trillion (USD55 billion)"; "17 percent more
    water by 2030".
  - l.69:
    - December 5, 2023 Blue Drop report.
    - "Around 46 percent of drinking water was microbiologically unsafe at the time of sampling in 2022".
    - "47 percent of tap water is considered non-revenue".
  - l.70: "42 of their reservoirs are leaking (half of their existing fleet)"; leak loss "25 percent"; budget covers
    "around 495 miles of the city's estimated 7,456 miles".
  - l.71: "approximately 1,050 wastewater treatment works".
  - l.72: "more than 6 million tons of general waste"; "Around 30 percent is recycled"; "One in ten households".
  - l.74: Mokolo Phase 2A "R12.4 billion (USD 720 million)", investment period "five years", "completed by May 2026".
  - No exchange rate is stated. The implied R per USD varies by line (computed): about 17.8 (l.11), 18.2 (l.14),
    19.2 (l.25), 19.2 (l.68), 18.2 (l.68) and 17.2 (l.74).
- Lists (count, with the last item):
  - ERA Act reforms (l.13): 4, last "imposing penalties for damage to and sabotage of electricity infrastructure".
  - Transmission programme bodies (l.26): 4.
  - Sub-Sector Best Prospects (l.30-46): 9, last "Nuclear, including small modular reactors (SMRs) and radioisotope
    production" (l.46).
  - Major Shows (l.48-50): "Enlit Africa 2026" / "Power and Energy" / "May 19-21, 2026, Cape Town, CTICC". The text does
    not show whether "Power and Energy" is a second show or a descriptor.
  - Energy Resources (l.52-55): 4, last "Horizon Grand View Research".
  - Water treatment equipment types (l.71): 4.
  - "Other areas of opportunity" (l.77-91): 8, last "Household organic waste composters" (l.91).
  - "Other sub-sector prospects in the EnviroTech sector" (l.94-100): 4, last "Solid waste management" (l.100).
  - Key Contacts (l.104-107): 4, last "Rand Water - South Africa".
- Forecasts, guidance, deadlines, effective dates:
  - Coal remains the majority source "for the next decade" (l.10).
  - Independent TSO "within five years", one of the ERA Act's reforms; the Act was signed in August 2024. The document
    does not say when the five years start (l.13).
  - Richards Bay: 2028 operation; Q2 2030 ramp-up; final investment decision 2026 (l.17).
  - Eskom gas plant 2030 (l.17); Koeberg Unit 1 to July 2044 (l.20); 10 GW of nuclear within a decade (l.20); Necsa 2026
    (l.20).
  - Storage $1,461 million by 2030 (l.23); 14,000 km of lines over 10 years (l.25).
  - 17% more water by 2030 (l.68); Mokolo by May 2026 (l.74).
  - Dates before the June 2026 publication date, with no outcome reported:
    - Seven-corridor tenders by end-2025 (l.26).
    - Karoo surveys in 2025 (l.18).
    - Next Blue Drop report at end-2025 (l.69).
- Dated events:
  - 2011: REIPPPP inception (l.14).
  - August 2022: Eskom's first rooftop estimate (l.22).
  - December 5, 2023: Blue Drop report (l.69).
  - January 2024: TNPA appointed Vopak and Transnet Pipelines (l.17).
  - July 2024: NTCSA began operations (l.13). August 2024: ERA Act signed (l.13).
  - September 2024: TNPA tender for an EIA on the Ngqura terminal (l.17).
  - September 2025, verbatim: "environmental groups won a legal challenge in September 2025 to dismiss the project's
    environmental authorization, with the Supreme Court of Appeal ruling the public consultation process for the project
    was flawed and ordering Eskom to undertake a more robust public participation process as part of a new environmental
    impact assessment" (l.17).
  - May 19-21, 2026: Enlit Africa (l.50).
- Hedged claims:
  - l.16: the Minister "has suggested the country could commit to 300 petajoules". This is a suggestion, not a commitment.
  - l.17: "is aiming for an operational date of 2028". Vopak's decision is "contingent on securing customer commitments".
    Eskom "plans" the plant and "is targeting 2030", but environmental groups "won a legal challenge in September 2025 to
    dismiss the project's environmental authorization".
  - l.18: Karoo extraction "would likely face resistance from environmental groups"; "likely" attaches to future
    extraction. The same line says the matter is "controversial however".
  - l.20: "has announced plans to procure 10 GW"; Necsa "plans to break ground"; the NNR "is still reviewing" Unit 2.
  - l.23: "is expected to grow".
  - l.26: "aims to issue tenders".
  - l.69: potable water in major cities "is still considered safe"; DWS "plans to release".
  - l.70: "there is concern that the system is close to collapse".
  - l.71: filtration "is deemed the most cost-effective".
  - l.74: "proposed investment value"; "aims to be completed".
- Rounded prose beside exact figures: there are no tables. "more than 7 GW" (l.10) versus "7.3 GW" (l.22). "over
  6,280MW" built versus "more than 6 GW ... operational" (l.14).
- Operative definitions, rules and scope exceptions:
  - l.10: load shedding is defined as "nationwide scheduled rolling blackouts, known as load shedding".
  - l.14: REIPPPP is "for utility-scale transactions".
  - l.16: the gas demand covers "new gas-to-power plants and retrofitting of Eskom's current diesel-run open cycle gas
    turbine (OCGT) peaking plants – and industrial users".
  - l.26: ITPO's mandate is to "issue tenders for private sector funded transmission projects under the
    Build-Own-Operate-Transfer (BOOT) model". The CGV is "to de-risk the program ... given the government's lack of fiscal
    space to provide sovereign guarantees".
  - l.69: the stated causes of non-revenue water.
  - l.92: water projects "would require a tender process".
- Amendments or contradictions:
  - The ERA Act is the amending law (l.13).
  - Eskom's Richards Bay gas plant (l.17): a plan with a 2030 target, set against the September 2025 legal challenge
    "to dismiss the project's environmental authorization" and the order for a new public participation process.
  - REIPPPP is spelled "Programme" (l.14) and "Program" (l.30).
  - DWS stands for two department names (l.69, l.104).
  - Prices rose "far outpacing inflation", but no inflation figure is given (l.10).
- Notes: the two chapters have separate contacts and cities (Johannesburg for energy, Cape Town for environmental
  technology).
- Coverage: full (l.1-114). No gaps.

## D15 - South Korea CCG: "Energy"

- Source: `text/D15.txt` (442 lines, 19,437 chars), from `docs/ccg_energy_cleantech_sectors_south_korea.txt`; capture
  doc 4.
- Written or submitted by: U.S. International Trade Administration (l.3). Contact: "Local Contact U.S. Commercial Service
  Korea U.S. Embassy Seoul", "188 Sejong-daero, Jongro-gu Seoul 03141, Korea Tel: 82-2-397-4535 office.seoul@trade.gov"
  (l.438-439). No named specialist.
  - Data sources: "Korean government (MOTIR/KEEI/KESIS) data" (l.9); the U.S. EIA (l.165).
  - Table 1 source: "the 11th Basic Plan for Electricity Supply and Demand, Ministry of Trade, Industry and Resources
    (MOTIR)" (l.160).
  - Table 2 source: "Nuclear Safety and Security Commission (NSSC) and Korea Hydro & Nuclear Power Co., Ltd. (KHNP)"
    (l.318).
- Type, date, edition: one chapter, `## Energy` (l.5). "Last published: 2026-06-26 Source:
  https://www.trade.gov/country-commercial-guides/south-korea-energy" (both on l.6).
- Period covered: calendar years.
  - Actuals 2022-2024; "provisional January-November 2025" (l.10, l.159, l.165).
  - 11th BPESD covers 2024-2038 (l.11).
  - LNG plan 2023-2036 (l.325). Table 2 data "as of September 25, 2025" (l.318).
- Headings in order:
  - l.8: "Energy: Power Generation Mix, LNG and Commercial Nuclear Power Overview".
  - l.15: unnumbered "Table:".
  - "Electricity Market and Governance": fused after the Source on l.160.
  - l.164: Nuclear; l.167: "Table 2: List of nuclear power plants in Korea".
  - "Liquified Natural Gas (LNG)": fused at the start of l.321.
  - "Best Prospects": fused at l.328. "Opportunities": fused inside the last bullet at l.340.
  - l.341: "The six GENCOs are:". IPP heading fused at l.353.
  - "Direct Importers of LNG" (l.380), with sub-heads fused into item lines: "Importers within SK Group" (l.380), "within
    GS Group" (l.396), "within POSCO Group" (l.404), "Others" (l.408).
  - "Key Organizations": fused at l.424. "Local Contact": fused at l.438.
- Entities and aliases:
  - MOTIR is first used unexpanded (l.9) and later expanded as "Ministry of Trade, Industry and Resources (MOTIR)"
    (l.160, l.428).
  - MCEE: "Ministry of Climate, Energy and Environment (MCEE)" (l.13); "Ministry of Climate, Energy, and Environment
    (MCEE)" (l.162, l.426).
  - Nuclear oversight: MSIT = Ministry of Science and ICT; NSSC = Nuclear Safety and Security Commission; KINS = Korea
    Institute of Nuclear Safety (all l.13).
  - KHNP: "Korea Hydro & Nuclear Power Co., Ltd. (KHNP)" (l.318) and "Korea Hydro and Nuclear Power (KHNP)" (l.343).
  - Utilities and market bodies:
    - KEPCO = Korea Electric Power Corporation, "state-owned" (l.161, l.430).
    - GENCOs = "power generation companies" (l.161) and "KEPCO's six generation subsidiaries" (l.340).
    - IPPs = Independent Power Producers (l.161, l.340, l.353).
    - KPX = Korea Power Exchange (l.161, l.434).
    - KOGAS = Korea Gas Corporation (l.432).
  - Agencies: KEA = Korea Energy Agency (l.436); KEEI = Korea Energy Economics Institute (l.438). KESIS is not expanded.
  - Terms:
    - BPESD = Basic Plan for Electricity Supply and Demand (l.9, l.15).
    - CFE = "Carbon Free Energy" (l.23, l.159).
    - SPAs = "sales and purchase agreements" (l.327).
    - EIA = U.S. Energy Information Administration (l.165).
    - "gigawatts electric (GW(e))" (l.165).
    - Not expanded: PWR, PHWR, IGCC, CTL, CTG, SMR, EPC, IAEA.
  - People: "The Lee Jae Myung administration, which took office in June 2025" (l.12); "The Lee administration" (l.166).
  - Policies and plans: "Energy Highway" policy (l.14); Special Act on Activation of Distributed Energy (l.160); 15th
    Long-Term Natural Gas Supply and Demand Plan (l.325); 2026 edition of Korea Electric Power Statistics (l.10, l.159).
  - Reactor aliases: Saeul-3 is "Former Shin-Kori-5" (l.208); Saeul-4 is "Former Shin-Kori-6" (l.213).
  - Location spellings: "Jangan-eup, Kijang-Geun, Busan" (Kori-2, l.175) versus "Gijang-gun, Busan" (Kori-1, l.311).
  - Countries:
    - Nuclear capacity ranking: US, France, China, Russia (l.165).
    - LNG suppliers: "Australia, Qatar, the United States, Malaysia, Indonesia, Russia, and Oman", the same 7 in the same
      order at l.323 and l.324.
  - Companies: SK, GS and POSCO conglomerates (l.326); SK E&S and POSCO International upstream (l.327); the list names
    under Lists below.
- Table 1, generation mix (l.15-160):
  - Title (l.15): "Table: Korea's Power Generation Mix according to the 11th Basic Plan for Electricity Supply and Demand
    (BPESD) (unit: TWh and mix ratio in%)".
  - Header cells (l.17-23): Nuclear | Coal | LNG | Renewable | New | Clean hydrogen and ammonia | Others | Total |, then
    a sub-row. In the sub-row, "PV, bio, hydro, wind, tidal, waste power" describes Renewable and "Fuel cells, IGCC, CTL,
    CTG" describes New. Two further columns follow: "Carbon Energy" and "Carbon Free Energy (CFE)".
  - Layout: one block per year. Each block has 10 TWh cells followed by 10 % cells.
  - Year labels as printed: "2022", "2023", "2024", "2025 (Jan.-Nov. est.)", "2030 (target)", "2038 (target)". The table
    has six years, including the 2025 partial-year row.
  - Note (l.159): "CFE = nuclear + renewable + clean hydrogen and ammonia. 2025 figures are provisional Jan.–Nov. estimates
    from KESIS/KEEI and should be updated once MOTIR and KEPCO publish the 2026 edition of Korea Electric Power Statistics
    with finalized 2025 annual data."
  - Source (l.160): "Source: the 11th Basic Plan for Electricity Supply and Demand, Ministry of Trade, Industry and
    Resources (MOTIR)". The next section's heading and text run on in the same line.

  TWh values. Each year's block covers these text lines: 2022 l.25-35, 2023 l.48-58, 2024 l.71-81,
  2025 l.94-103, 2030 l.116-125, 2038 l.138-147.

  | TWh | 2022 | 2023 | 2024 | 2025 (Jan.-Nov. est.) | 2030 (target) | 2038 (target) |
  |---|---|---|---|---|---|---|
  | Nuclear | 176.1 | 180.5 | 188.8 | 169.3 | 204.2 | 248.3 |
  | Coal | 193.2 | 184.9 | 167.2 | 157.9 | 110.5 | 70.9 |
  | LNG | 163.6 | 157.7 | 167.2 | 148.5 | 161 | 74.3 |
  | Renewable | 53.2 | 49.4 | 63.2 | 57.6 | 120.9 | 205.7 |
  | New | 0.9 | 7.2 | 7.3 | 7.7 | 18.7 | 26.4 |
  | Clean hydrogen and ammonia | 0 | 0 | 0.8 | 0.3 | 15.5 | 43.9 |
  | Others | 8.4 | 8.3 | 4.5 | 2.3 | 11.8 | 34.9 |
  | Total | 595.3 | 588 | 595.6 | 543.6 | 642.6 | 704.4 |
  | Carbon Energy | 366.0 | 358.1 | 342.85 | 316.4 | 302.0 | 206.5 |
  | CFE | 229.3 | 229.9 | 252.8 | 227.2 | 340.6 | 497.9 |

  Mix-ratio values. Each year's block covers these text lines: 2022 l.37-46, 2023 l.60-69, 2024 l.83-92,
  2025 l.105-114, 2030 l.127-136, 2038 l.149-158.

  | % | 2022 | 2023 | 2024 | 2025 (Jan.-Nov. est.) | 2030 (target) | 2038 (target) |
  |---|---|---|---|---|---|---|
  | Nuclear | 29.6% | 30.7% | 31.7% | 31.1% | 31.8% | 35.2% |
  | Coal | 32.5% | 31.4% | 28.1% | 29.0% | 17.2% | 10.1% |
  | LNG | 27.5% | 26.8% | 28.1% | 27.3% | 25.1% | 10.5% |
  | Renewable | 8.9% | 8.4% | 10.6% | 10.6% | 18.8% | 29.2% |
  | New | 0.1% | 1.2% | 1.2% | 1.4% | 2.9% | 3.7% |
  | Clean hydrogen and ammonia | 0.0% | 0.0% | 0.1% | 0.1% | 2.4% | 6.2% |
  | Others | 1.4% | 1.4% | 0.8% | 0.4% | 1.8% | 5.0% |
  | Total | 100% | 100% | 100.0% | 100.0% | 100% | 100% |
  | Carbon Energy | 61.5% | 60.9% | 57.6% | 58.2% | 47.0% | 29.3% |
  | CFE | 38.5% | 39.1% | 42.4% | 41.8% | 53.0% | 70.7% |

  - Precision: one decimal, except "588" (2023 total), "161" (2030 LNG), "0" (Clean H2 in 2022 and 2023) and "342.85"
    (2024 Carbon Energy, the only two-decimal cell). Totals print as "100%" or "100.0%".
  - Internal checks (computed):
    - The seven components sum to the Total in 2023, 2025, 2030 and 2038. 2022 sums to 595.4 against 595.3.
    - **2024 components sum to 599.0 TWh against the printed Total of 595.6 (a 3.4 TWh gap).**
    - The seven 2024 % cells sum to 100.6%. The other years sum to 99.9-100.0%.
    - Every printed 2024 share equals its TWh value divided by 595.6 (for example, 188.8/595.6 = 31.7%).
    - CFE equals nuclear + renewable + clean H2 in every year.
    - Carbon Energy equals Total minus CFE in every year (2024: 595.6 - 252.8 = 342.8, printed 342.85). In 2024,
      coal + LNG + New + Others = 346.2.
    - 2024/2023 total = 595.6/588, about +1.3%, which matches "up 1.3%" (l.9).
  - Prose beside the table:
    - l.9-10 (2024 and January-November 2025) and l.11 (the 2030 and 2038 shares) agree with the table.
    - The nuclear targets at l.166 (204.2 and 248.3 TWh; 31.8% and 35.2%) agree.
    - The LNG targets at l.322 (161 TWh / 25.1% in 2030; 74.3 TWh / 10.5% in 2038) agree.
    - l.327 (LNG share from 28.1% in 2024 to 10.5% in 2038) agrees.
    - Rounded prose: l.325 "53% (340TWh) by 2030" versus table 53.0% / 340.6; "70.7% (497.9TWh) by 2038" matches.
    - l.325 "from 167TWh in 2024" versus table 167.2.

- Table 2, nuclear plants (l.167-318):
  - Headers (l.169-172): "NAME |", "LOCATION |", "TYPE |", "Capa. (MWe) | Ground-breaking | Operation date | Status".
  - Footer (l.318): "(Data as of September 25, 2025) Source: Nuclear Safety and Security Commission (NSSC) and Korea Hydro
    & Nuclear Power Co., Ltd. (KHNP)".
  - Dates are MM/DD/YY, or MM/YYYY for some ground-breakings.
  - Location cells are printed only on 8 rows. Most rows have no location cell, which suggests merged cells. Kori-3 and
    Kori-4 have no status cell. Neither can be resolved visually (only the `.txt` capture exists).

  | # | Name | Location (as printed) | Type | MWe | Ground-breaking | Operation date | Status (as printed) | lines |
  |---|---|---|---|---|---|---|---|---|
  | 1 | Kori-2 | Jangan-eup, Kijang-Geun, Busan | PWR | 650 | 12/04/77 | 07/25/83 | Taken offline on 3/8/23, 9/28/24, and 8/6/25 and waits for a decision on its operation license renewal | 174-177 |
  | 2 | Kori-3 | (none) | PWR | 950 | 10/01/79 | 09/30/85 | (none) | 179-182 |
  | 3 | Kori-4 | (none) | PWR | 950 | 04/01/80 | 04/29/86 | (none) | 184-187 |
  | 4 | Shin-Kori-1 | (none) | PWR | 1,000 | 01/17/05 | 02/28/11 | in operation | 189-191 |
  | 5 | Shin-Kori-2 | (none) | PWR | 1,000 | 01/17/05 | 07/20/12 | in operation | 193-195 |
  | 6 | Saeul-1 | Ulju-gun, Ulsan | PWR | 1,400 | 12/2015 | 12/20/16 | in operation | 197-199 |
  | 7 | Saeul-2 | (none) | PWR | 1,400 | 12/2015 | 08/29/19 | in operation | 201-203 |
  | 8 | Saeul-3 | Ulju-gun, Ulsan | PWR | 1,400 | 06/2016 | n/a | Former Shin-Kori-5 Expected to be in operation in the first half of 2026. | 205-208 |
  | 9 | Saeul-4 | (none) | PWR | 1,400 | 06/2016 | n/a | Former Shin-Kori-6 Expected to be in operation in 2027. | 210-213 |
  | 10 | Wolsong-2 | Gyeongju-si, Gyeongsangbuk-do | PHWR | 700 | 06/22/92 | 07/01/97 | in operation | 215-218 |
  | 11 | Wolsong-3 | (none) | PHWR | 700 | 03/17/94 | 07/01/98 | in operation | 220-223 |
  | 12 | Wolsong-4 | (none) | PHWR | 700 | 07/22/94 | 10/01/99 | in operation | 225-228 |
  | 13 | Shin-Wolsong-1 (name and type in one cell) | (none) | PWR | 1,000 | 10/01/05 | 07/31/12 | in operation | 230-232 |
  | 14 | Shin-Wolsong-2 (name and type in one cell) | (none) | PWR | 1,000 | 10/01/05 | 07/24/15 | in operation | 234-236 |
  | 15 | Hanbit-1 | Yeonggwang-gun, Jeollanam-do | PWR | 950 | 06/04/81 | 08/25/86 | in operation | 238-240 |
  | 16 | Hanbit-2 | (none) | PWR | 950 | 12/01/81 | 06/10/87 | in operation | 242-244 |
  | 17 | Hanbit-3 | (none) | PWR | 1,000 | 12/23/89 | 03/31/95 | in operation | 246-248 |
  | 18 | Hanbit-4 | (none) | PWR | 1,000 | 05/26/90 | 01/01/96 | in operation | 250-252 |
  | 19 | Hanbit-5 | (none) | PWR | 1,000 | 06/29/97 | 05/21/02 | in operation | 254-256 |
  | 20 | Hanbit-6 | (none) | PWR | 1,000 | 11/20/97 | 12/24/02 | in operation | 258-260 |
  | 21 | Hanul-1 | Uljin-gun, Gyeongsangbuk-do | PWR | 950 | 01/26/83 | 09/10/88 | in operation | 262-264 |
  | 22 | Hanul-2 | (none) | PWR | 950 | 07/05/83 | 09/30/89 | in operation | 266-268 |
  | 23 | Hanul-3 | (none) | PWR | 1,000 | 07/21/93 | 08/11/98 | in operation | 270-272 |
  | 24 | Hanul-4 | (none) | PWR | 1,000 | 11/01/93 | 12/31/99 | in operation | 274-276 |
  | 25 | Hanul-5 | (none) | PWR | 1,000 | 10/01/99 | 07/29/04 | in operation | 278-280 |
  | 26 | Hanul-6 | (none) | PWR | 1,000 | 09/29/00 | 04/22/05 | in operation | 282-284 |
  | 27 | Shin-Hanul-1 | (none) | PWR | 1,400 | 04/30/10 | 12/07/22 | in operation | 286-288 |
  | 28 | Shin-Hanul-2 | (none) | PWR | 1,400 | 04/30/10 | 04/05/24 | in operation | 290-294 |
  | 29 | Shin-Hanul-3 | (none) | PWR | 1,400 | 09/13/24 | n/a | Expected to be in operation by Oct. 2033 | 296-301 |
  | 30 | Shin-Hanul-4 | (none) | PWR | 1,400 | 09/13/24 | n/a | Expected to be in operation by Oct. 2033 | 303-308 |
  | 31 | Kori-1 | Gijang-gun, Busan | PWR | 587 | 04/27/72 | 04/29/78 | Permanently shut down on 6/18/17 | 310-313 |
  | 32 | Wolsong-1 | Gyeongju-si, Gyeongsangbuk-do | PHWR | 679 | 10/30/77 | 04/22/83 | Permanently shut down on 12/24/19 | 315-318 |

  - Counts (computed):
    - 32 rows: 28 PWR and 4 PHWR (Wolsong-1 to Wolsong-4).
    - 23 rows read "in operation", totalling 23,500 MWe.
    - Kori-2 is offline awaiting renewal; Kori-3 and Kori-4 have a blank status. These 3 rows total 2,550 MWe. With the
      23 operating rows they make 26 rows and 26,050 MWe.
    - 4 rows have operation date "n/a" (Saeul-3, Saeul-4, Shin-Hanul-3, Shin-Hanul-4), 1,400 MWe each (5,600 MWe).
    - 2 rows are permanently shut down (587 + 679 = 1,266 MWe).
  - Prose beside the table: l.165 says "26 nuclear reactors, 23 of which are currently in operation ... approximately 26
    gigawatts electric". The counts fit the 23 "in operation" rows plus Kori-2, Kori-3 and Kori-4.
  - l.166: "two large nuclear reactors and one SMR by 2038" do not appear in Table 2.

- Quantitative figures in prose (not counting repeats of table values):
  - l.9: 2024 generation 595.6 TWh, "up 1.3%"; nuclear became the "largest single power source in 18 years".
  - l.165: nuclear capacity of the US, France, China and Russia: "approximately 97GWe, 63GWe, 55GWe, and 27GWe".
  - l.324 (2024 LNG):
    - "KOGAS imported approximately 34.1mil. tons, down 2.2%".
    - Private direct importers "approximately 12.2 mil. tons, up 32.2%". "Private direct imports accounted for
      approximately 26.4% of Korea's total LNG imports".
    - Total LNG imports "increased by approximately 5% year-on-year".
  - l.325: LNG demand "decline by an average of 1.38% per year from 45.09mil. tons in 2023 to 37.66mil. tons in 2036"
    (computed CAGR about -1.376%/yr, consistent).
  - l.326:
    - "There are 18 private direct importers of LNG". Direct import has been allowed "since 1997".
    - Private direct imports "supplying 26.1% of the total import volume of 46.33mil. tons ... as of 2024".
    - "large conglomerates including SK, GS, POSCO, and GENCOs account for about 26.4% of Korea's total direct import
      volume".
  - l.327: KOGAS "secures 80-85% through long-term ... SPAs, with the remaining 15-20% ... spot"; "only about 35% of global
    LNG is traded on the spot market".
- Lists (count, with the last item):
  - 11th BPESD mixes for 2030 and 2038 (l.11): 7 categories each.
  - Nuclear governance split (l.13, l.320): MOTIR (industry, exports); MSIT (R&D); NSSC/KINS (safety and licensing); MCEE
    (climate and energy role).
  - Coordination topics (l.162): 9.
  - LNG suppliers (l.323, repeated at l.324): 7, last Oman.
  - LNG value-chain segments (l.326): 3.
  - Best Prospects (l.330-340): 6, last "Power equipment and clean firm power solutions for data centers, semiconductors,
    and advanced industrial demand" (l.340; the "Opportunities" paragraph is fused onto it).
  - Six GENCOs (l.343-353): KHNP, KOEN (Korea South-East Power), KOWEPO (Korea Western Power), KOMIPO (Korea Midland
    Power), KOSPO (Korea Southern Power), EWP (Korea East-West Power Company), the last at l.353.
  - IPPs, "include, but are not limited to" (l.355-379): 13. POSCO International, GS EPS, Pyeongtaek Energy Service,
    S-Power Co., Ltd., Paju Energy Service Co., Ltd., GS Power, Goseong Green Power Co., Ltd., Gangneung Eco Power (GEP),
    SC bluepower, Donghae IPP Power, Pocheon Power, CGN Yulchon, SK E&S (last, l.379).
  - Direct Importers of LNG (l.380-420): 20 names by count (computed).
    - SK Group, 8: SK E&S, SK Hynix, SK Energy, Narae Energy Service Co., Ltd., Paju Energy Service Co., Ltd., Yeoju
      Energy Service, Ulsan GPS, SK Incheon Petrochemical (l.396).
    - GS Group, 4: GS EPS, GS Caltex, GS Power, "SPPC Co., Ltd.," (l.404).
    - POSCO Group, 2: POSCO, POSCO International (l.408).
    - Others, 6: S-Oil, Korea Zinc, Hanwha Solution, HD Hyundai Chemical, Tongyeong Eco Power, Lotte Ineos Resources
      (last, l.420).
  - Two unheaded event items follow the importer list in the same bullet run: "Korea Energy Show, Busan" (l.422) and
    "International Ministerial Conference on Nuclear Power IAEA, Songdo, Incheon" (l.424). Neither the text nor the
    original has an events heading; this is unresolved.
  - Key Organizations (l.426-438): 7, last "Korea Energy Economics Institute (KEEI)".
  - Overlaps (computed): the IPP list and the importer list share 5 names (POSCO International, GS EPS, Paju Energy
    Service Co., Ltd., GS Power, SK E&S). The upstream companies (l.327) are KOGAS, SK E&S and POSCO International. No
    GENCO appears in the importer list, although l.326 names GENCOs among LNG-importing groups.
- Forecasts, guidance, deadlines, effective dates:
  - 11th BPESD "finalized in February 2025 and covers the 2024-2038 period" (l.11). Targets for 2030 and 2038 (l.11, l.166,
    l.322, l.325, l.327).
  - The new administration "is developing a new BPESD framework" (l.12).
  - 2025 provisional data to be updated once the 2026 Korea Electric Power Statistics are published (l.10, l.159).
  - Saeul-3 in the first half of 2026; Saeul-4 in 2027; Shin-Hanul-3 and -4 by October 2033 (Table 2).
  - Two large reactors and one SMR by 2038, "subject to future siting, licensing, policy, and project development
    processes" (l.166).
  - LNG demand to 2036 (l.325).
- Dated events:
  - 1997: direct LNG import allowed (l.326).
  - Kori-1 shut 6/18/17; Wolsong-1 shut 12/24/19 (Table 2).
  - April 27, 2023: MOTIR announced the 15th Long-Term Natural Gas Supply and Demand Plan (l.325).
  - 2023: the US's "first full-year top position" as LNG exporter; the US was also the largest exporter in 2024 (l.323).
  - June 2024: Special Act on Activation of Distributed Energy "implemented" (l.160).
  - February 2025: 11th BPESD finalized (l.11). June 2025: Lee Jae Myung administration took office (l.12).
  - Kori-2 taken offline on 3/8/23, 9/28/24 and 8/6/25 (l.177).
  - Table 2 data as of September 25, 2025 (l.318).
- Hedged claims:
  - l.10 and l.159: provisional figures "should be updated".
  - l.12: the administration "is expected to continue supporting civil nuclear exports while placing greater emphasis on
    renewable energy".
  - l.161: legislation "expected to gradually change" the market structure.
  - l.162 and l.320: MCEE's role "may influence how nuclear power is evaluated". "may" attaches to MCEE's influence. In
    l.320, MOTIR "is expected to remain important", while MSIT "retains" and NSSC/KINS "remain central" are stated firmly.
  - l.163: "the new administration is likely to pursue a more balanced energy policy".
  - l.165: further nuclear increases "will depend on" grid capacity and other factors.
  - l.166: the reactors are "subject to future siting, licensing, policy, and project development processes".
  - l.322: LNG's long-term share "is expected to decline sharply".
  - l.323: "LNG-fired generation appears to have remained under pressure"; the strategy "is therefore likely to continue
    balancing".
  - l.327: LNG "is still expected to play a flexible balancing role".
  - l.328: companies "should have opportunities".
- Rounded prose beside exact figures: see the Table 1 notes (l.325: 167 against 167.2, and 340 against 340.6). l.165:
  "approximately 26 gigawatts electric" against the Table 2 MWe values (computed 26,050 for the 26 rows that are not shut
  and have an operation date).
- Operative definitions, rules and scope exceptions:
  - CFE (l.159). Renewable and New components (l.23).
  - Special Act (l.160): "allows eligible smaller generation facilities and integrated energy systems to sell power within
    defined regions, while wholesale electricity prices are also calculated separately by region".
  - Direct LNG import is allowed "under the limited conditions of corporate self-consumption" (l.326).
  - Direct importers "are also mandated to participate in power exchange tenders due to supply obligations necessitating
    the procurement of minimum volumes through long-term SPAs" (l.327).
  - IPP list is "include, but are not limited to" (l.353), so it is non-exhaustive.
- Amendments or contradictions (neutral; none resolved by the document):
  - Table 1, 2024 column: component sum 599.0 versus Total 595.6; % sum 100.6; Carbon Energy 342.85 versus a component
    sum of 346.2 (computed).
  - Private direct LNG share for 2024: "approximately 26.4%" (l.324) versus "26.1% of the total import volume of
    46.33mil. tons" (l.326). l.326 reuses "about 26.4%" for the conglomerates' share of "total direct import volume".
    Computed: 12.2/46.33 is about 26.3%; 34.1 + 12.2 = 46.3 against 46.33.
  - "There are 18 private direct importers of LNG" (l.326) versus 20 names in l.380-420.
  - IPP definition:
    - l.340: "The Independent Power Producers (IPPs) consist of KEPCO's six generation subsidiaries, known as GENCOs, as
      well as private power producers".
    - l.161 lists "KEPCO, its power generation companies (GENCOs), and Independent Power Producers (IPPs)" as separate,
      and l.340 also says "GENCOs and IPPs".
    - The IPP list (l.355-379) contains no GENCO.
  - KOGAS "monopolizes imports and supply in the midstream and downstream sectors" (l.327) versus private direct imports
    of 12.2 Mt (l.324) and "KOGAS remained the dominant importer" (l.323).
  - Publisher of the 2026 Korea Electric Power Statistics: "once KEPCO publishes" (l.10) versus "once MOTIR and KEPCO
    publish" (l.159).
  - The Table 1 title attributes the table to the 11th BPESD, but the 2025 row comes from KESIS/KEEI provisional
    estimates (l.159).
  - The 2025 column covers 11 months, unlike the full-year columns. l.10 says renewables "remained at 57.6TWh, or 10.6%".
  - Only "Table:" (unnumbered) and "Table 2:" appear; there is no "Table 1" label.
- Gaps:
  - l.324: "The chart below shows Korea's LNG import trends". Neither the text nor the original capture contains any
    chart data, so the chart's values are missing. Only the prose figures on l.324 survive.
  - Table 2's location and status cells for unmarked rows cannot be resolved visually.
  - The heading for l.422-424 is absent.
- Coverage: full (l.1-442). No unread text.

## Shared ground within this part (navigation only; facts and locations)

- Entities in more than one document:
  - POSCO: D11 l.188 names POSCO E&C as "the South Korean company" for the Warsaw WtE plant. D15 names the POSCO group
    (l.326), POSCO and POSCO International (l.327, l.355, l.404-408). No document links POSCO E&C to the D15 entities.
  - United States as an LNG source:
    - D11 l.41 (long-term contracts).
    - D12 l.29, l.33 (first European receipt in 2016), l.48.
    - D13 l.40 ("re-gasified U.S. LNG" via BRUA).
    - D15 l.321, l.323 (largest exporter in 2024), l.324.
  - Qatar as an LNG source: D11 l.41; D15 l.323-324.
  - Russia:
    - Gas: D11 l.41 (main supplier before 2022); D12 l.33 (reliance "minimal"); D13 l.35 ("shift away from Russian gas").
    - D15 l.165 (27 GWe of nuclear) and l.323-324 (LNG supplier).
  - US nuclear agreements: D11 l.23 (2020 Intergovernmental Agreement); D13 l.47 (in force July 28, 2021).
  - EU Modernization Fund: D11 l.36 (storage co-financing programme); D13 l.59 (€3 billion for CfD round 2).
  - Recovery and resilience plans: D12 l.14 ("Portugal's Recovery and Resilience Program"; no funder stated). D13 l.22
    (PNRR, under two names, one of them "the government's EU-aided National Recovery and Resilience Plan").
  - National energy and climate plans:
    - D11 l.26: "National Plan for Energy and Climate".
    - D12 l.12 and l.20: "National Energy and Climate Plan for 2030" and "Integrated National Energy and Climate Plan
      (NECP)".
    - D13 l.64: "Integrated National Plan for Energy and Climate Change 2021-2030".
  - SMRs: D11 l.23; D13 l.27, l.32, l.50; D14 l.20, l.46; D15 l.166, l.332.
  - Reactor-type terms: D13 l.28 calls Cernavodă Units 1-2 "pressurized heavy water reactors" (CANDU-6). D15 Table 2
    gives type "PHWR" for Wolsong-1 to Wolsong-4 and "PWR" for the rest, and never expands either. No document defines
    PHWR, so the bundle does not itself link the two terms.
  - Coal positions:
    - D11 l.19 (last plants), l.21 (at least 56% by 2030), l.93 (primary until 2049).
    - D12 l.13 (exit in 2021).
    - D13 l.42 (2026 deadline versus 2032).
    - D14 l.10 (about 80%).
    - D15 Table 1 (coal 2022-2038).
  - Hydrogen: D11 l.38-39; D12 l.13, l.24-27, l.47; D15 l.11, l.14 and the Table 1 column "Clean hydrogen and ammonia".
  - Energy storage: D11 l.35-36; D13 l.22; D14 l.23.
  - Grid, pipeline and market bodies, as each document describes them:
    - D11 l.41: Gaz-System manages "the transmission system pipelines".
    - D13 l.54: Transgaz is "the national transport system operator" (SNT).
    - D14 l.13 and l.26: NTCSA, and the planned independent TSO under the ERA Act.
    - D15 l.161: KEPCO and its GENCOs, with "Korea Power Exchange (KPX) administered wholesale transactions".
  - LNG terminals: D11 l.41-43 (Swinoujście; FSRU in the Bay of Gdansk); D12 l.29-34 (Sines); D13 l.39 (Constanta);
    D14 l.17 (Richards Bay; Ngqura).
  - External data bodies:
    - Eurostat (D12 l.11); International Renewable Energy Agency (D13 l.44).
    - D11 l.46 lists the web resource "Energy Information Administration" with no country; D15 l.165 cites "the U.S.
      Energy Information Administration (EIA)". The documents do not equate them.
    - IEA (D12 l.61); IAEA (D15 l.424); IFC/World Bank (D14 l.26).
  - "First" and ranking claims:
    - D11 l.41: Swinoujście is the "first onshore regasification facility in the Baltic Sea region". D11 l.28: Poland
      ranked 5th in the EU for PV increase in 2024.
    - D12 l.33: first European country to receive US LNG. D12 l.10: 11th for import dependence. D12 l.11: second in the
      EU for renewables share in 2024.
    - D13 l.27 and l.50: "first European market to deploy an SMR". D13 l.62: "biggest PV project in Europe".
    - D15 l.165: Korea is behind the US, France, China and Russia in nuclear capacity.
- Shared periods and series:
  - Calendar-2024 electricity actuals: D11 l.13-18; D12 l.11; D13 l.12 and l.44 (end-2024 solar); D15 l.9 and the 2024
    Table 1 column.
  - Two January-November 2025 partial-year windows:
    - D12 l.17: APREN, Mainland Portugal, January 1 to November 30, 2025.
    - D15 l.10 and the Table 1 "2025 (Jan.-Nov. est.)" row: KESIS/KEEI provisional.
  - Single-month figures:
    - D12: November 2025 (l.18); December 2024 EV registrations (l.39).
    - D13: April 2025 electricity (l.24); "as of May 2025" capacity shares (l.52).
    - D11: December 2024 storage auction (l.35).
  - Planning horizons:
    - D15: 11th BPESD 2024-2038.
    - D13: Energy Strategy 2025-2035; Transgaz plan 2024-2033; NECP 2021-2030.
    - D11: Hydrogen Strategy to 2030 with an outlook to 2040; EU budget 2021-2027.
    - D12: Energy Poverty Strategy 2023-2050.
  - Publication dates: D11 2026-04-02 (Energy) and 2026-04-06 (Environmental); D12 2026-04-16; D14 2026-06-01 (both
    chapters); D13 2026-06-02; D15 2026-06-26.
  - Forward dates that fall before each document's publication date, with no outcome reported:
    - D11 l.33 (December 17, 2025 auction), l.188 (Warsaw WtE by 2025).
    - D13 l.12, l.15, l.40, l.58, l.59 (2025 items).
    - D14 l.18, l.26, l.69 (2025 items).
    - D15: Saeul-3 in the first half of 2026 (Table 2 data as of September 25, 2025).
- Units and scale:
  - Capacity: MW and GW in D11-D14. Electrical units "MWe"/"GWe" appear in D13 l.27-28 and D15 (Table 2 "Capa. (MWe)";
    l.165 "GWe" and "GW(e)").
  - Generation: TWh in D11, D13 and D15; GWh in D12 l.17-18 and D11 l.18 (exports).
  - Storage: MWh (D13 l.22) and GWh (D11 l.36).
  - Gas: bcm (D11, D13 l.35); million tons of LNG (D14 l.17, D15 l.324-326); petajoules (D14 l.16).
  - Currency:
    - D11: PLN (l.10); EUR with USD in parentheses (l.21); USD alone (l.21 "$250 billion", l.36, and throughout the
      Environmental chapter).
    - D12 and D13: EUR. D14: rand ("R") with USD in parentheses.
    - D15: no currency figures.
    - No document states an exchange rate.
  - Thresholds of "50" in different units: D11 l.30 VAT cut for solar "less than 50 kW"; D12 l.20 EIA exemption planned
    for solar "below 50 MW".
- Cross-references: none of D11-D15 cites, amends or responds to another bundle document. Each is a separate ITA country
  chapter. Within-document repeats are listed under each document (D11 RES 29.4%; D13 2,480 MWe, 2 GW and 2.5 GW; D14
  7 GW against 7.3 GW; D15 prose against Table 1).
- Revisions stated by a document:
  - D13 l.44: renewables target "34% (previously set to 30.7%)".
  - D15 l.12: the new administration "is developing a new BPESD framework". The document does not say what it changes
    in the 11th BPESD.
  - D15 l.10 and l.159: 2025 provisional figures are pending finalization.
  - D11 l.95: BAT conclusions were declared invalid, then new ones accepted.


<!-- merged from doc-map-d.md -->

# aq-01543 - document map, part D (D16-D20)

Part D of the bundle map, written for the caller to merge into `notes/doc-map.md`. It is for navigation only: where things are, not what to ask.
`Lnn` = line nn of `text/Dnn.txt`. For every content line, the `docs/` original line is Lnn-2. The text file adds a 2-line `# Dnn | docs/...` header. The original's double blank line before the closing `-----` is collapsed to one blank line, which is a whitespace-only difference.
"(map arithmetic)" marks the mapper's own recomputation. It is not document text.

## Part header

- Documents: D16 Spain, D17 United Arab Emirates, D18 United Kingdom, D19 Uruguay, D20 Vietnam. All are U.S. International Trade Administration (ITA) Country Commercial Guide chapters. Manifest values: method `text`, pages `null`. Chars: D16 15,531; D17 17,137; D18 17,940; D19 17,164; D20 34,431. sha256 prefixes: D16 3c8f8cb8, D17 7c13c26e, D18 d58be9f0, D19 9d7b0660, D20 ca33498a.
- Coverage: all readable text of all five documents was read in full, in line chunks. Each section has its own ledger. No unread ranges remain.
- Extraction spot-checks:
  - Page count: not applicable (these are text captures).
  - Tables: D16 L13-31 matches original L11-29 exactly. D20 L138-145 matches original L136-143 exactly, including the missing separators and "iltration".
  - Footnotes: not applicable, because none of the five has footnotes.
  - Anomalies confirmed to be in the originals (not caused by extraction): D16 "only 2.8%" (orig L9); D17 ADSW dates (orig L54/L121) and "Samrt" (orig L102); D18 "Great Britian", "many100" and the two NESO expansions (orig L25-27, L52); D19 "2.026 GWh" and "570 MV" (orig L14/L16).
- Market-data tables: none in D16-D20. The search terms were "market size", "exchange rate", "local production", "imports from" and "|". The only pipe-cell table in this part is D20 L140-145.
- Missing or unresolved, by type:
  - Hyperlink targets were not captured. These are "(PDF)" markers, "available here", and resource names without URLs; locations are given per document.
  - The trade.gov web pages are not available, so any images or charts on them cannot be checked. Because of this, the cell boundaries in D20's table are unresolved.

## D16 - Spain: "Energy" chapter

- Source: `text/D16.txt` (74 lines), from `docs/ccg_energy_cleantech_sectors_spain.txt` | pages: not applicable
- Written or submitted by: U.S. ITA, "Spain Country Commercial Guide (U.S. International Trade Administration)" (L3). The contact block is "U.S. Commercial Service Spain / Energy Sector Specialist: Carmen Adrada", with tel and e-mail at L69-71.
  - Cited as sources, not authors: Red Electrica (L31), EY's RECAI (L33), International Energy Agency (L38), European Commission (L38, L43), "industry analysts" (L49), Emergency Capital Investment Program (ECINP) (L51).
- Type, date, edition: one chapter, `## Energy` (L5).
  - L6: "Last published: 2024-07-31".
  - L7: "Source: https://www.trade.gov/country-commercial-guides/spain-energy".
  - No edition or version label.
- Headings in order: Overview L9; Leading Sub-Sectors L41; "Renewable Energy (Offshore wind and PV self-production and self-consumption)" L42; Energy Storage and Efficiency L44; Green Hydrogen L48; Opportunities L50; Resources L53; Stakeholders L54; "In renewable energy, the main trade associations include:" L64; U.S. Commercial Service Spain L69; end marker `-----` L73.
  - The L42 sub-heading names offshore wind and self-consumption, but the L43 paragraph under it gives no offshore-wind or self-consumption figures.
- Period covered:
  - Capacity snapshot "as of December 31, 2022" (L13). Changes during 2022 (L10-12, L35). "first quarter of 2023" (L32). June 2023 (L33).
  - October 2023 (L43) is the latest dated past event.
  - Forecast windows: 2022-2027 (L38-39) and 2023-2028 (L34). Target years: 2023, 2027, 2030, 2050.
  - No fiscal-year convention is stated.
  - Money is given as USD with EUR in parentheses. No exchange rate is stated; the pairs imply about 1.07-1.08 USD per EUR (map arithmetic).
- Entities and aliases:
  - Red Electrica (L31 source line) = Red Eléctrica de España (REE) (L57). REE is "partially owned by the government" and the "sole transmission agent and system operator (TSO)" (L57). It is the exception in "all operators are private (except for the 20% stake held by the state in REE)" (L59).
  - Ministry for Ecological Transition (MITECO) (L55). Also "the Ministry of Ecological Transition's Secretary of State of Energy" (L60).
  - CNMC has two English expansions: "National Commission for Markets and Competition (CNMC)" (L56) and "National Commission of Markets and Competition (Comisión Nacional de los Mercados y la Competencia - CNMC)" (L59).
  - OMIE = "OMI-Polo Español SA (OMIE)". It is the electricity market operator and manages the wholesale market "for the Iberian Peninsula (Spain and Portugal)" (L58).
  - OMIP = "Iberian Energy Market Operator (OMIP) (Portuguese Division), SGMR, S.A.", the futures market (L58). L58 also says "OMIE belongs to the Iberian Market Operator business group".
  - IDAE = Institute for Diversification and Energy Saving (L60).
  - aelec = Asociación de Empresas de Energía Eléctrica (L61). ENERCLUB = El Club Español de la Energía (L62).
  - APPA = Renewable Energy Companies Association; UNEF = PV Energy Companies Association; AEE = Spanish Wind Energy Association (L65-67).
  - Companies (all at L59 only): Endesa, Iberdrola, EDP, Naturgy, Cepsa Gas, Repsol, Cepsa, BP, Galp, Disa.
  - Plans and laws: 2021 Climate Change and Energy Transition law and Just Transition Strategy (L36); Energy Storage Strategy (L37); REPowerEU (L38, L43); revised National Recovery and Resilience Plan (L43); "COVID-19 recovery plan" (L49); Hydrogen Roadmap / "green hydrogen roadmap" (L49, L51); Long-Term Decarbonization Plan (L49); EU Hydrogen Strategy (L49); NextGenerationEU (NGEU) (L51).
  - Countries:
    - Portugal (L10, L58).
    - France: energy partnership and reduced nuclear capacity (L32); also in the PPA-index list (L33).
    - PPA index (L33): Germany, "the United Sates" [sic], UK, France, Australia.
    - Gas-supply countries (L35): U.S., Algeria, Nigeria, Norway, Russia, Qatar.
    - Germany (L39). Russia (L34, L38, L43).
  - Abbreviations: PV (L11); PPA (L33, L40); RECAI (L33); CAGR (L34); LNG (L35); MT = "million metric ton equivalent" (L36); IEA (L38); NGEU (L51); TSO (L57); MWh (L58).
- Tables:
  - L13-31 is a list-form table with no `|` cells. Its title is "Installed power capacity on the Iberian Peninsula as of December 31, 2022:". Unit MW, whole numbers. Source line L31: "Source: Red Electrica".
  - Rows verbatim: Wind: 29,994 MW (L14); Combined cycle: 26,250 MW (L15); Solar PV: 19,785 MW (L16); Hydro: 17,094 MW (L17); Nuclear: 7,117 MW (L18); Cogeneration: 5,643 MW (L19); Coal: 3,464 MW (L20); Pumped storage: 3,331 MW (L21); Fuel and gas: 2,408 MW (L22); Solar Thermal: 2,304 MW (L23); Other renewables: 1,093 MW (L24); Non-renewable waste: 426 MW (L25); Renewable waste: 170 MW (L26); Hydro-wind: 11 MW (L27); Total Renewable: 70,452 MW (L28); Total Non-renewable: 48,639 MW (L29); Total: 119,091 MW (L30).
  - Rows are sorted by size. No row is flagged renewable or non-renewable.
  - Map arithmetic:
    - The 14 component rows sum to 119,090 MW, 1 MW below the stated Total.
    - Total Renewable + Total Non-renewable = 119,091.
    - Combined cycle + Nuclear + Cogeneration + Coal + Pumped storage + Fuel and gas + Non-renewable waste = 48,639 exactly. The document never says pumped storage is non-renewable.
    - The other seven rows sum to 70,451.
    - Shares of the 119,091 MW total: non-renewable 40.8%, renewable 59.2%, coal 2.9%.
- Lists:
  - L14-27: 14 technology rows, followed by 3 total rows. The last component row is "Hydro-wind: 11 MW" (L27).
  - L33: five countries ahead of Spain on the PPA index. L35: four "Other countries exporting LNG to Spain" (Nigeria, Norway, Russia, Qatar).
  - L52: four partnering regions (Europe, Latin America, the Middle East, Africa).
  - L59 operator sets, in order:
    1. "dominant operators, those whose market share exceeds 10%, include Endesa, Iberdrola, EDP, and Naturgy" (4). That sentence does not name the sector.
    2. Gas: "Naturgy remains the main market operator, followed by Endesa, Iberdrola, and Cepsa Gas" (4).
    3. "main operators in the fuel sector are Repsol, Cepsa, BP, Galp, and Disa" (5).
    4. LPG "leaders are Repsol, Cepsa, BP, Naturgy and Disa" (5).
    5. "In natural gas, there are only two dominant operators, whose market shares exceed 10%, which are Naturgy and Endesa" (2).
    6. Last sentence: "Repsol and Cepsa are the dominant operators in the sectors of fuels and liquefied petroleum gases" (2).
  - L65-67: three renewable trade associations; the last is AEE.
  - Leading Sub-Sectors headings: 3 (L42, L44, L48).
- Quantitative figures in prose:
  - L10: "Spain's total installed energy capacity increased by 4.9% in 2022, reaching 119 GW". Renewable installed capacity +9.1% "across the Iberian Peninsula (including Portugal)".
  - L11, 2022:
    - PV "growing over 22% (4.4 GW)", making it "the third leading generation capacity after wind and combined cycle".
    - Wind "adding 4.9% capacity". Non-renewable power -0.8%. Coal -8.5%, plus "decommissioning of a major coal plant" (not named).
    - "By the end of the year, non-renewable capacity made up only 2.8% of the Iberian Peninsula's total generation capacity."
  - L12: "non-peninsular" systems (Balearic Islands (Mallorca and Ibiza), Canary Islands): installed capacity +2.2% in 2022; solar PV +31.4%; wind +2.4%. No MW values are given.
  - L32: electricity demand of energy-heavy industries (steel, chemical, paper, food) -7.7% in the first quarter of 2023.
  - L33: Spain is "8th most attractive market" in EY's biannual RECAI (June 2023). PPA index: "at the top ... behind" five countries.
  - L34: power-market CAGR "expected to increase more than 2.8% between 2023 and 2028".
  - L35:
    - Natural gas exports "increased 24.6% compared to May 2022 and stand at 9,683 GWh". The period of the 9,683 GWh is not stated.
    - 75.7% of exports go by pipeline and 24.3% as LNG.
    - In 2022, U.S. LNG was "29% of the total natural gas imports volume", followed by Algeria at "almost 25% through the Mediterranean pipeline".
  - L36: CO2 falls from "334 million metric ton equivalent (MT) emitted in 2018 to a maximum of 29 MT in 2050"; 100% renewable electricity system by 2050.
  - L37:
    - Energy Storage Strategy (March 2022): 20 GW of storage by 2030 and 30 GW by 2050.
    - 2021 EV plan: "$4.6 billion (€4.3 billion) by 2023", expected to attract "an additional $21.2 billion (€19.7 billion)" from the private sector.
  - L38:
    - IEA: Europe's renewable capacity "forecast to expand by 45%" over 2022-2027.
    - REPowerEU (May 2022): end reliance on Russian fossil fuels "by 2027"; renewables share of final energy consumption 45% by 2030, "exceeding the 40% previously under negotiation".
  - L39: Europe's planned renewable electricity expansion "doubles over the 2022-2027 period". The EU forecast was "revised upward significantly (by 30%) from last year's goal, led by Germany (50% higher) and Spain (60% higher)".
  - L43:
    - Rankings: third highest renewable generation capacity in Europe; 11th lowest CO2 per inhabitant; "Globally, Spain is the 14th most sustainable country".
    - The revised National Recovery and Resilience Plan is "Valued at nearly $178 billion (€165.5 billion)", with a goal of "before 2030".
    - "In October 2023, 40% of funds ($4.58 billion/€4.26 billion) were allocated to climate-related objectives". The base of "funds" is not stated. Map arithmetic: 4.58/0.40 = $11.45 billion, while 40% of $178 billion = $71.2 billion.
  - L49:
    - "$70 billion (€65.1 billion) COVID-19 recovery plan". Hydrogen Roadmap "approved in 2021".
    - Long-Term Decarbonization Plan: GHG "-90% in 2050 compared to 1990 levels". EU Hydrogen Strategy "approved in July 2021" (as printed).
    - "$9.6 billion (€8.9 billion) Hydrogen Roadmap". Carbon neutrality by 2050.
    - "4GW of renewable hydrogen electrolyzers by 2030, representing 10% of the European Union's 40 GW target".
    - GHG -4.6 million tons CO2 equivalent "in the next ten years" (start date not stated). The roadmap is reviewed "every three years".
  - L51:
    - ECINP "investment need of $263.5 billion (€245 billion) through 2030 (pre-COVID)", "only 20%" public.
    - Green hydrogen roadmap investment "will reach almost $11 billion (€10.3 billion)".
    - "target is to install 11GWof [sic] hydrogen electrolysis capacity by 2030".
    - "$19.5 billion (€18.1 billion) to produce and distribute hydrogen derived from renewable energy sources".
  - L52: the government is exploring ways to get the private sector to invest "$118 billion (€110 billion)" through 2030.
  - L55: the MITECO authorization threshold is "more than 50MW". L59: the state holds 20% of REE; "five largest shares"; "exceeds 10%".
- Forecasts, targets, deadlines:
  - 2027: EU ends reliance on Russian fossil fuels (L38, REPowerEU "proposes").
  - 2030: 20 GW storage (L37); renewables 45% of final energy consumption (EU, L38); 4 GW electrolyzers (L49) and 11 GW electrolysis (L51); ECINP need and $118 billion private investment "through 2030" (L51, L52); recovery-plan goal "before 2030" (L43).
  - 2050: 100% renewable electricity and CO2 at most 29 MT (L36); 30 GW storage (L37); -90% GHG vs 1990 and carbon neutrality (L49).
  - Other: EV investment "by 2023" (L37); CAGR window 2023-2028 (L34); IEA window 2022-2027 (L38-39).
- Dated events: 2018 emissions baseline (L36); 2021 law (L36); 2021 EV plan (L37); 2021 Hydrogen Roadmap approval and "July 2021" EU Hydrogen Strategy (L49); March 2022 Energy Storage Strategy (L37); May 2022 REPowerEU release (L38); Dec 31, 2022 capacity snapshot (L13); Q1 2023 demand (L32); June 2023 RECAI (L33); October 2023 fund allocation (L43).
- Hedged claims:
  - L32: "Climate change is expected to increase the prospect of drought". The hedge attaches to the future drought prospect. The demand drop itself is stated as fact, and its reason is given as "The most apparent reason being...".
  - L34: "estimated ... is expected to increase more than 2.8%" (the CAGR).
  - L38: "forecast to expand by 45%" (IEA); REPowerEU "proposes".
  - L40: "Corporations are expected to further drive this growth through PPAs".
  - L45: "would greatly reduce Spain's dependency" (conditional on storage).
  - L49: "According to industry analysts, Spain has the ideal conditions to become Europe's green hydrogen hub". The attribution covers the hub claim only.
  - L51: "It is expected that ... roadmap investment will reach almost $11 billion"; research investment "will increase considerably".
  - L52: "is exploring ways to persuade". This is not a commitment.
- Rounded prose beside exact figures:
  - L10 "119 GW" vs table Total 119,091 MW (L30).
  - L11 PV "+4.4 GW" / "over 22%" vs table Solar PV 19,785 MW at end-2022 (L16). Map arithmetic: a 4.4 GW addition onto 15,385 MW is +28.6%; 22% growth to 19,785 MW would be about +3.57 GW. The table gives no start-of-year values.
  - L11 rank "third ... after wind and combined cycle" agrees with table order L14-16.
  - L49: 4 GW / 40 GW = 10% (consistent).
- Notes:
  - Scope varies: L10 calls 119 GW "Spain's total", the table header (L13) says "Iberian Peninsula", the L10 renewable growth is "across the Iberian Peninsula (including Portugal)", and L12 covers non-peninsular systems separately.
  - Text glitches: "United Sates" (L33); "remains is essential" (L40); "11GWof" (L51).
  - Missing link targets: "(PDF)" markers at L36 (twice) and L37.
- Operative definitions, rules and scope exceptions:
  - L55, MITECO authorizes facilities "with an installed capacity of more than 50MW when they affect the territorial scope of more than one autonomous community or are offshore in the territorial sea".
  - L55, autonomous communities grant authorizations "when the electric infrastructure solely affects their territory unless such authorizations are expressly reserved for the MITECO". Town councils grant "works and activity licenses".
  - L59, principal operators: "those that hold one of the five largest shares of the market or sector" (CNMC annual list). Dominant: "those whose market share exceeds 10%".
  - L36: the 2021 law "prohibits new hydrocarbon exploration and extraction projects".
  - L49: "Unlike the EU Hydrogen Strategy..., Spain's Hydrogen Roadmap excludes the role low-carbon hydrogen could play".
  - L57: REE is the "sole transmission agent and system operator (TSO)".
  - L47: the "efficiency first" principle.
- Amendments or contradictions (both locations; none has a document-stated precedence):
  - L11 "non-renewable capacity made up only 2.8%" vs table L29-30: 48,639 of 119,091 MW, which is 40.8%.
  - L49 "4GW of renewable hydrogen electrolyzers by 2030" vs L51 "11GW ... electrolysis capacity by 2030".
  - Hydrogen money: L49 "$9.6 billion (€8.9 billion) Hydrogen Roadmap"; L51 "almost $11 billion (€10.3 billion)" expected; L51 "$19.5 billion (€18.1 billion)" hydrogen initiative.
  - Recovery plan value: L49 "$70 billion (€65.1 billion) COVID-19 recovery plan" vs L43 revised plan "nearly $178 billion (€165.5 billion)".
  - Emissions baselines: L36 uses 2018 (334 MT to at most 29 MT, -91.3% by map arithmetic). L49 uses -90% vs 1990.
  - Stated target change: L38 EU renewables share 45%, "exceeding the 40% previously under negotiation". Stated forecast revision: L39 "+30%" vs last year's goal.
- Coverage: full. Ledger: L1-74 read in one chunk; L70-74 re-read to confirm end of file. Remaining unread: none. Missing source text: only the link targets listed above.

## D17 - United Arab Emirates: two chapters

- Source: `text/D17.txt` (130 lines), from `docs/ccg_energy_cleantech_sectors_united_arab_emirates.txt` | pages: not applicable
- Written or submitted by: U.S. ITA, "United Arab Emirates Country Commercial Guide" (L3). No named contact; "Please contact us" appears at L51 and L118.
  - Attribution phrases: "According to the announcement" (L36, Helios); "said to be" (L24); "purported" (L44).
- Type, date, edition:
  - Chapter 1, `## Renewable Energy and Clean Energy` (L5). L6 "Last published: 2025-08-25". L7 "Source: https://www.trade.gov/country-commercial-guides/united-arab-emirates-renewable-energy-and-clean-energy-0".
  - Chapter 2, `## Clean Tech and Environmental Technologies` (L65). L66 "Last published: 2025-08-25". L67 "Source: https://www.trade.gov/country-commercial-guides/united-arab-emirates-clean-tech-and-environmental-technologies".
- Headings in order:
  - Chapter 1: Overview L9; "Milestones include:" L12; Leading Sub-Sectors L25; Opportunities L27; Solar L29; Hydrogen L31; Chemicals and Derivatives L39; Waste-to-Energy L43; inline "Waste-to-Solar:" L48; Resources L49; Trade Shows & Exhibitions L50.
  - Chapter 2: Overview L69; Leading Sub-Sectors L82; Water and Wastewater Treatment L83; Waste Management and Recycling L91; Air Pollution Mitigation L95; Opportunities L99; Resources L116; Trade Shows and Exhibitions L117; `-----` L129.
- Period covered: milestones 2006-2023 (L13-20); events through January 2025 (L48, latest past event); trade shows September 2025 - May 2026; target years 2030, 2031, 2035, 2036, 2050. No fiscal-year convention. USD only.
- Entities and aliases:
  - Masdar:
    - "Abu Dhabi Future Energy Company (Masdar)", established 2006. Masdar City is a separate item, "the first carbon-neutral zero waste city" (L13); IRENA is located on the "edge of the Masdar City campus" (L15).
    - Hydrogen: Project Green Falcon, and a "$5 billion strategic alliance" with Engie (L32).
    - Emirates Waste to Energy Company, a JV of BEEAH and Masdar (L48).
  - Emirates Nuclear Energy Corporation (L14); International Renewable Energy Agency (IRENA) (L15); COP 28 (L19).
  - Mohammed bin Rashid Al Maktoum (MBR) solar facility / "MBR plant" (L24); Al Dhafra; Abu Dhabi PV3 (L24).
  - Green Falcon partners (L32): Siemens Energy, TotalEnergies, Marubeni Corporation, Abu Dhabi Department of Energy, Etihad Airways, Lufthansa Group, Khalifa University.
  - The Department of Energy is written "Abu Dhabi Department of Energy" (L32) and "Abu Dhabi's Department of Energy" (L84).
  - Dubai Electricity and Water Authority (DEWA) (L34).
  - "The UAE company Helios Industry" / "Helios"; Khalifa Industrial Zone Abu Dhabi (KIZAD); Thyssenkrupp (L36).
  - Ruwais Derivatives Park / "Ruwais Park". "Ta'ziz company, ADNOC's 60/40 joint venture with Abu Dhabi's industrial holding company ADQ" (L42). ADNOC is not expanded.
  - Dubai energy-from-waste consortium (L44): Dubai Holding (lead), Dubal Holding, Itochu Corporation, Hitachi Zosen Inova, Besix Group, Tech Group.
  - "Emirates Water and Electricity Company" (L46) = "Emirates Water and Electricity Company (EWEC)" (L84).
  - "Abu Dhabi Waste Management Company (Tadweer)" (L46) = "Tadweer" (L94).
  - Sharjah Waste to Energy Facility (L48); Alterra climate fund (L72); Ministry of Climate Change and Environment (MoCCAE) (L94, L96, L98); Abu Dhabi's Sewerage and Services Company and its Strategic Tunnel Enhancement Program (L90).
  - Venues and events: ADNEC = Abu Dhabi National Exhibition Center (L54); ADIPEC = Abu Dhabi International Petroleum Exhibition and Conference (L52); ADSW = Abu Dhabi Sustainability Week (L55, L122); WFES = World Future Energy Summit (L58, L125); WETEX = Water Energy Technology Environment Exhibition (L119); "Make it in the UAE" (L61).
- Tables: none (no `|` rows). Trade shows are given as name / "Date:" / "Venue:" triplets.
- Lists:
  - Milestones L13-20: 8 items. The last item (L20) is "Net Zero 2050 target. In July 2023, the UAE announced a strategy to invest $54 billion in renewables by 2030...".
  - Four solar projects (L24): Al Dhafra (2 GW), Abu Dhabi PV3 (1.5 GW), MBR fourth phase (950 MW), MBR fifth phase (900 MW). Sum 5,350 MW (map arithmetic).
  - Leading sub-sectors (L26), 5 items: "solar power, chemicals and derivatives, hydrogen, waste-to-energy, and waste-to-solar".
  - Green Falcon partners (L32): 7; the last is Khalifa University.
  - Dubai WtE consortium (L44): leader plus 5; the last is Tech Group.
  - Chapter 1 trade shows (L52-63), 4, all at ADNEC: ADIPEC Nov 3-6, 2025; ADSW Jan 12-18, 2026; WFES Jan 13-15, 2026; Make it in the UAE May 4-7, 2026.
  - Vision 2021 aims (L75-79): 5; the last is "Implement standards in the construction and management of buildings."
  - Dubai Law No. 18 of 2024 scope (L94), 8 activities: separation, collection, transport, storage, reuse, recycling, treatment, disposal.
  - Chapter 2 opportunity lists:
    - Water L102-105: 4 items; the last is "Underground water storage."; L104 reads "Samrt water monitoring systems."
    - Waste L107-110: 4 items; the last is "Waste-to-energy".
    - Air L112-115: 4 items; the last is "Analytical and laboratory testing equipment."
  - Chapter 2 trade shows (L119-127), 3: WETEX Sept 30 - Oct 2, 2025, Dubai; ADSW Jan 11-17, 2026, venue "Abu Dhabi, UAE"; WFES Jan 13-15, 2026, ADNEC.
- Quantitative figures in prose:
  - L10: "invest over $163 billion by 2050".
  - L20: July 2023, "$54 billion in renewables by 2030".
  - L22, Energy Strategy 2050 (launched January 2017): "increase the contribution of clean energy in the total energy mix from 25% to 50% by 2050"; reduce the carbon footprint of power generation by 70%; increase the consumption efficiency of individuals and corporates by 40%.
  - L24: "Among the seven emirates". MBR "planned total capacity of 5GW when fully operational by 2030".
  - L32: by 2050, "14 to 22 million tons of hydrogen and hydrogen derivates annually". Masdar "up to one million tons of green hydrogen by 2030". Masdar-Engie "$5 billion" alliance for a "200-megawatt green hydrogen plant to produce green ammonia".
  - L36: Helios "almost $1 billion", "two phases". At peak, "about 200,000 tons of green ammonia from 40,000 tons of green hydrogen". "800-MW" solar facility.
  - L42: Ta'ziz "60/40" joint venture.
  - L44: Dubai "$1 billion energy-from-waste project"; first phase "inaugurated in July 2023"; "200-megawatt facility"; "fully operational since September 2024".
  - L46: May 2023; "expected annual processing capacity of 900,000 tons of waste"; "expected carbon emissions reduction of 1.1 million tons per year"; "up to 52,500 households".
  - L48: Sharjah facility "completed in 2022", "300,000 metric tons of non-recyclable waste", "30 megawatts". Landfill to become a "120-megawatt solar energy farm" once zero-waste targets are achieved. "Phase 2 was announced in January 2025."
  - L72: net zero by 2050; interim "32% renewable energy share by 2030" and "47% reduction in emissions by 2035". Alterra: "initial commitment of $30 billion in December 2023".
  - L94: Green Growth Strategy "75% recovery rate of processed municipal solid waste".
- Forecasts, targets, deadlines:
  - 2030: $54 billion (L20); MBR at 5 GW (L24); Masdar at 1 Mt hydrogen (L32); 32% renewable share (L72).
  - 2031: National Air Quality Agenda 2031 (L98).
  - 2035: -47% emissions (L72).
  - 2036: Water Security Strategy 2036 (L86).
  - 2050: $163 billion (L10); net zero (L20, L72); clean energy at 50% of the energy mix (L22); hydrogen 14-22 Mt (L32).
  - Policy frameworks: Vision 2021 "Green Economy for Sustainable Development" (L74); Green Growth Strategy (L94); "updated National Net Zero Pathway and Energy Strategy 2050" (L72).
- Dated events:
  - 2006 Masdar (L13). 2009 ENEC (L14). 2009 IRENA HQ designation and 2015 relocation (L15). 2016 Paris ratification (L16).
  - Jan 2017 Energy Strategy 2050 (L22). 2019 first National Air Emissions Inventory Report (L98). Expo Oct 2021 - Mar 2022 (L17). 2022 Sharjah facility completed (L48). Sept 2022 Air Quality Agenda (L98).
  - 2023 Hydrogen Strategy (L32). "2023 and 2024" Year of Sustainability (L18). May 2023 WtE proposals received (L46). July 2023 $54 billion strategy (L20) and Dubai WtE first phase (L44). COP 28 Nov 30 - Dec 12, 2023 (L19). Dec 2023 Alterra (L72).
  - 2024 Climate Change Law (L72). Dubai Law No. 18 of 2024 (L94). Sept 2024 Dubai WtE fully operational (L44). Jan 2025 Phase 2 (L48).
- Hedged claims:
  - L24: "is said to be the world's largest single-site solar installation". The hedge attaches to the superlative only.
  - L24: "Four solar projects ... are expected to drive this growth".
  - L36: "is expected to utilize Thyssenkrupp technologies"; "According to the announcement, this will be the first commercial plant to produce carbon dioxide-free green ammonia ... in the UAE".
  - L42: "is targeted to become the world's largest integrated refinery and petrochemicals complex".
  - L44: "purported to be the biggest and most efficient in the world". The same line states "fully operational since September 2024" without a hedge.
  - L46: "Set to be one of the region's largest"; "expected" processing, emissions and households figures.
  - L88: wastewater reuse "is expected to expand".
- Rounded prose beside exact figures: not applicable (no tables).
- Notes:
  - Repeated figures attached to different projects: "200-megawatt" is the Masdar-Engie hydrogen plant (L32) and also the Dubai energy-from-waste facility (L44). About $1 billion is Helios ("almost", L36) and also Dubai energy-from-waste (L44).
  - L30: concentrated solar "constitute the second-largest technology by installed capacity". The base is not scoped.
  - L94: "emirates.Tadweer" is missing a space.
  - Missing link targets: none of the resources have URLs.
- Operative definitions, rules and scope exceptions:
  - L42: "'plug-and-play' concept, meaning that new projects can be plugged into the existing park infrastructure".
  - L88 and L92: wastewater and waste are "managed and coordinated through individual local authorities and municipalities in each emirate".
  - L84: "regulations restrict groundwater use".
  - L40: "SMEs are advised to partner with major U.S. industry players as suppliers or subcontractors".
- Amendments or contradictions:
  - ADSW 2026 dates: L56 "January 12-18, 2026" (ADNEC) vs L123 "January 11-17, 2026" ("Abu Dhabi, UAE"). Both chapters are dated 2025-08-25 and no precedence is stated. Confirmed in the original (L54/L121).
  - Energy Strategy 2050: launched January 2017 with a 25% to 50% clean-energy target by 2050 (L22). L72 refers to an "updated ... Energy Strategy 2050" carrying a 32% renewable share by 2030 and -47% emissions by 2035. The update date is not stated, and the metrics differ (clean energy in the total energy mix vs renewable energy share).
- Coverage: full. Ledger: L1-130 read in one chunk. Remaining unread: none.

## D18 - United Kingdom: "Energy" chapter

- Source: `text/D18.txt` (83 lines), from `docs/ccg_energy_cleantech_sectors_united_kingdom.txt` | pages: not applicable
- Written or submitted by: U.S. ITA, "United Kingdom Country Commercial Guide" (L3). Contact: "Leah Kollhoff, Commercial Specialist, U.S. Commercial Service, Tel: +44 (0)20 7891 3459" (L80). Data attribution: "According to the International Energy Agency" (L10).
- Type, date, edition: one chapter, `## Energy` (L5).
  - L6: "Last published: 2023-11-03".
  - L7: "Source: https://www.trade.gov/country-commercial-guides/united-kingdom-energy".
  - The body describes events after the stated publication date: Dec 2024 (L15), July 2024 (L25), Oct 2024 (L54), Feb 2025 (L23, L33), June 2025 (L24), "As of 2025" (L29), and 2026 events (L64-67). This is a source fact; no revision note appears.
- Headings in order:
  - Overview L9.
  - Leading Sub-Sectors L20, with inline labels "Nuclear:" L21; "Renewables: Wind, Solar, Biomass, Tidal, and Waste:" L25; "Pricing and Distribution - Smart Grids/Energy Storage:" L27.
  - Opportunities L30; Nuclear L31, with inline labels "Existing plant's life extension & New Build:" L32 and "Decommissioning:" L34.
  - Wind L37; Smart Grids L40; Energy Storage L57.
  - Resources L62: "Industry Events:" L63; "Trade Associations:" L68; "Government Departments:" L73; contact L79-80; `-----` L82.
- Period covered: IEA energy supply "in 2023" (L10); 2024 generation mix (L12); "Currently" (L13); EDF spending 2025-2027 (L32); decommissioning spending 2024-2025 (L35); target years 2029, 2030, 2035, 2050. No fiscal-year convention. USD, with one GBP pair (L14: $9 billion = £7.3 billion; about 1.23 USD per GBP, map arithmetic).
- Entities and aliases:
  - NESO has two expansions: "National Grid Electricity System Operator (NESO)" (L28, which paid the 2024 constraint payments) and "National Energy System Operator (NESO): Established as an independent public body in October 2024" (L54).
  - GBE-N = "Great British Energy-Nuclear (GBE-N), a publicly owned energy company headquartered in Aberdeen, Scotland focused on clean energy projects" (L14). It is the SMR partner at L24. The Resources list has "Great British Nuclear" (L75).
  - EDF forms:
    - "EDF Energy, a wholly owned subsidiary of the EDF Group (headquartered in France)" (L32). L32 also has "EDF" (committed investment, Sizewell C JV) and "Areva (France)" EPRs.
    - "EdF Energy" in the Big 6 (L51); "EDF" as a storage developer (L60).
  - HMG (L23, L32) is not expanded. "UK Labour government" (L24). "Rolls-Royce SMR" (L24).
  - National Grid compounds:
    - "National Grid Electricity Transmission (NGET)" and "National Gas Transmission (formerly part of National Grid)" (L52).
    - "National Grid Electricity Distribution (formerly Western Power Distribution)" (L53).
    - "National Grid" (L60).
  - NIE = Northern Ireland Electricity, in both the transmission list (L52) and the distribution list (L53).
  - Nuclear bodies and terms: Nuclear Decommissioning Authority (NDA) (L34, L76); advanced gas-cooled reactor (AGR) (L34); "National Policy Statement (NPS) for Nuclear Power Generation (EN-6)" (L33); Regulated Asset Base (RAB) (L32).
  - The Crown Estate (L39); Energy Networks Association Smart Networks Portal (L55); Distribution Network Operators (DNOs) (L60).
  - U.S. engineering companies: Bechtel, Amentum, "GE through Alstom acquisition" (L32); Bechtel, Amentum, AECOM, Fluor (L35).
  - Siemens Gamesa (L38).
  - Projects: Hinkley Point C (Somerset), Sizewell C (Suffolk) (L32); Hornsea One, Hornsea Two, Seagreen Wind Farm, "Dogger Bank A, B, and C (and potentially D)" (L38).
  - Abbreviations: CCUS (L15); SMR (L24, L33); AMR (L33, not expanded); BESS, GW, GWh (L29); TWh (L28); O&M (L39); ICT (L27).
- Tables: none (no `|` rows). Percentage mixes appear in prose at L10 and L12.
- Lists:
  - L14: four steps (halting new North Sea licenses; loosening nuclear site restrictions; GBE-N; National Wealth Fund). National Wealth Fund areas: ports, gigafactories, clean steel, carbon capture and storage, green hydrogen (5).
  - L23: eight former approved nuclear sites: "Bradwell, Hartlepool, Heysham, Hinkley Point, Moorside/Sellafield, Oldbury, Sizewell, and Wylfa". The last is Wylfa.
  - L43-49: seven smart-grid target sectors; the last is "Consumer engagement platforms and services".
  - L51: "Big 6": British Gas, E.ON, OVO Energy, EdF Energy, Octopus Energy, Scottish Power.
  - L52: transmission network operators (4): NGET (England and Wales); Scottish Power Transmission (southern and central Scotland); Scottish Hydro Electric Transmission (northern Scotland); NIE (Northern Ireland, transmission and distribution).
  - L52: gas transmission and distribution (2): National Gas Transmission (Great Britain); Cadent Gas ("four of the eight regional gas distribution networks").
  - L53: distribution network operators (7): Electricity North West, Northern PowerGrid, SP Energy Networks, SSE Power Distribution, UK Power Networks, National Grid Electricity Distribution, Northern Ireland Electricity (last).
  - L60: six storage developers: Anesco, EDF, Pivot Power, Statera, RES, Zenobe.
  - L64-67: four industry events: International Energy Week 2026 (Feb 10-12, 2026, London); Smart Energy Conference (RenewableNI) (March 26, 2026, Belfast Northern Ireland); Global Offshore Wind 2026 (June 16, 2026, Manchester Central); World Nuclear Symposium (Sept 9-11, 2026, London).
  - L69-72: four trade associations: Nuclear Industry Association, Energy Networks Association, Energy UK, Renewable UK.
  - L74-78: five government departments: Department of Energy Security and Net Zero, Great British Nuclear, Nuclear Decommissioning Authority, North Sea Transition Authority, Office of Nuclear Regulation (last).
- Quantitative figures in prose:
  - L10, IEA, "in 2023": natural gas 38% of total energy supply, oil 36%, renewables/nuclear 25%, coal 1% (sums to 100). "The UK imported 44.3% of its total energy supply", with Norway and the United States "the principal sources of UK's imported energy in 2024". The year of the 44.3% is not explicit.
  - L12, 2024 electricity generation: "26% gas, 35% wind and solar, 14% nuclear, 16% other renewable, 1% coal and 8% other" (sums to 100). "In 2024, the UK imported more power than it exported."
  - L13: 95% "clean" power grid by 2030 ("one of its five manifesto pledges"). "over 750,000 jobs"; "$189 billion" to the economy; "Approximately 120,000 jobs" in oil and gas, concentrated in Northeast Scotland.
  - L14: National Wealth Fund "$9 billion (£7.3 billion)".
  - L22: "nine civil nuclear reactors currently in operation, with two reactors under construction. All but one of the current operating reactors ... scheduled to be shut down by 2030."
  - L25:
    - "14.7 GW of offshore wind operating capacity", described as "the largest installed capacity in Europe". Targets "43-50 GW by 2030".
    - "In 2024, wind farms contributed a record 30% of the country's electricity".
    - "up to 50GW of offshore wind by 2030"; "five-fold by 2035" (the base is not stated); Scotland "11GW installed offshore wind capacity by 2030".
  - L26: "eight regional offshore clusters".
  - L28: in 2024, NESO "paid approximately $500 million in constraint payments to wind farms to curtail 8.3 terawatt-hours (TWh)".
  - L29, "As of 2025": "over 6 gigawatts (GW) of operational grid-scale" BESS; "energy capacity exceeding 8 gigawatt-hours (GWh)"; "20GW additional capacity approved in planning"; pipeline "approximately 127 GW"; "many100 MW and larger" [sic].
  - L32:
    - EDF "an additional $1.6 billion ... over the next three years (2025-2027)"; "averages approximately $550 million per year". Map arithmetic: 1.6/3 = $533 million.
    - Hinkley Point construction "started in 2018"; first new reactor to the grid "by 2029". Sizewell C is a "50-50 joint venture between HMG and EDF".
  - L33: "eight specific sites identified in the National Policy Statement (NPS) ... (EN-6)".
  - L34: NDA "owns 17 nuclear sites"; "seven advanced gas-cooled reactor (AGR) stations".
  - L35: "plans to shut down eight reactors by 2030"; "approximately $5.5 billion in 2024-2025 on decommissioning programs".
  - L38:
    - Hornsea One: completed 2020, "1.2 GW", "174 Siemens Gamesa turbines, each with a capacity of 7 MW" (map arithmetic: 1,218 MW).
    - Hornsea Two: operational "August 2022", "1.4 GW", "165 turbines".
    - Seagreen: "completed in June 2023", "1,075MW", "Scotland's largest offshore fixed wind farm".
    - Dogger Bank: "When the three phases are completed in 2026", "3.6GW", "5% of total UK demand".
  - L52: Cadent operates "four of the eight regional gas distribution networks".
- Forecasts, targets, deadlines:
  - 2026: Dogger Bank completion (L38).
  - 2029: first Hinkley Point C reactor connected (L32).
  - 2030: 95% clean power (L13); eight reactor shutdowns (L22, L35); offshore wind 43-50 GW / "up to 50GW" (L25); Scotland 11 GW (L25).
  - 2035: offshore wind five-fold (L25).
  - 2050: Net Zero (L33).
  - Spending windows: 2025-2027 EDF (L32); 2024-2025 decommissioning (L35).
- Dated events: 2018 Hinkley construction start (L32); 2020 Hornsea One; Aug 2022 Hornsea Two; June 2023 Seagreen (L38); July 2024 onshore wind de facto ban lifted (L25); Oct 2024 NESO established (L54); Dec 2024 updated "Powering Up Britain" (L15); Feb 2025 nuclear planning reforms (L23, L33); June 2025 SMR competition result (L24).
- Hedged claims:
  - L24: Rolls-Royce SMR is "chosen as the preferred bidder ... subject to final government approvals". The hedge attaches to the selection.
  - L23: "the government will define specific criteria that nuclear developers could use".
  - L32: "EDF plans to connect ... by 2029". U.S. companies "are involved ... even though their scope is limited".
  - L35: "currently plans to spend approximately $5.5 billion".
  - L38: "(and potentially D)". The hedge attaches only to phase D; the 2026 completion and "will be the world's largest wind farm" are stated firmly.
  - L21: "Robust foreign competition and financing are the chief obstacles".
- Rounded prose beside exact figures: L32 "$1.6 billion" over 3 years vs "approximately $550 million per year"; L38 "1.2 GW" vs 174 x 7 MW.
- Notes:
  - Text glitches: "Great Britian" (L27); "many100" (L29); "from design and planning though construction" (L39); "U.S exporters" (L42).
  - Missing source text: no URLs for any resource (L64-78).
- Operative definitions, rules and scope exceptions:
  - L10: overall energy supply is "(energy used for electricity generation, transportation, heating etc.)". Total energy supply is "(all energy produced in the UK or imported, minus that which is exported or stored)".
  - L23 exception: "(Note: In Scotland, the UK government does not have authority over local energy planning. Currently, the Scottish government has a ban on new nuclear development)". The reform covers "anywhere in England and Wales". Developers submit an application to HMG showing how their site meets the criteria.
  - L32, RAB: "consumers pay levies on their energy bills before the plant generates electricity". Sizewell C is "the first nuclear project eligible".
  - L50: the market is "unbundled (non-vertically integrated)". L51 defines the "Big 6" as controlling "the majority of the energy retail market".
- Amendments or contradictions (both locations; no precedence stated):
  - Offshore wind rank: L25 "largest installed capacity in Europe" vs L59 "largest installed capacity of offshore wind in the world".
  - NESO: two expansions (L28 vs L54). L28 attributes 2024 payments to NESO; L54 says NESO was established in Oct 2024.
  - Coal: L10 "has now been phased out" vs L12 2024 mix "1% coal".
  - Wind share in 2024: L12 "35% wind and solar" vs L25 wind "30%". These measure different scopes and are not necessarily a conflict.
  - Reactors under construction: L22 "two reactors under construction". L32 says EDF "is building two ... EPRs at Hinkley Point C ... and Sizewell C" and also that Sizewell C "will follow the same design as Hinkley Point once construction begins".
  - Shutdown count: L22 "All but one" of nine (= 8) is consistent with L35 "eight reactors by 2030".
  - Feb 2025 change, two descriptions: L23 (nuclear plants "anywhere in England and Wales", replacing the eight-site list) and L33 ("free up additional sites for Small Modular Reactor (SMR) development", replacing the EN-6 eight sites). Amendment order: EN-6 eight sites ("Previously", L23, L33), then the Feb 2025 reforms.
  - Publication date (2023-11-03) vs content dated up to June 2025 and 2026 events.
- Coverage: full. Ledger: L1-83 read in one chunk. Remaining unread: none.

## D19 - Uruguay: "Energy" chapter

- Source: `text/D19.txt` (69 lines), from `docs/ccg_energy_cleantech_sectors_uruguay.txt` | pages: not applicable
- Written or submitted by: U.S. ITA, "Uruguay Country Commercial Guide" (L3). Embassy contact "Office.Montevideo@trade.gov" (L61).
  - Data attributed to: MIEM (L12, twice); UTE ("officially reported", L16); "the government estimates" (L33); "preliminary reports" and "Reports suggest" (L43); Uruguay XXI (L59).
- Type, date, edition: one chapter, `## Energy` (L5).
  - L6: "Last published: 2025-08-15".
  - L7: "Source: https://www.trade.gov/country-commercial-guides/uruguay-energy".
- Headings in order: Overview L9; Opportunities L21; Leading Sub-Sectors L29; Oil & Gas L30; Hydrogen L32; E-fuels L38; Hydroelectric L44; Wind L47; Solar L51; Biomass L56; Resources L60; `-----` L68. In this document, Opportunities comes before Leading Sub-Sectors.
- Period covered: "In 2024" data (L12, L16, L57, L59); 2023 comparisons (L12, L20, L52); May and June 2025 (L26, L28, L41; latest dated events); target years 2025, 2026, 2027, 2032, 2040, 2049, 2050. No fiscal-year convention. USD only.
- Entities and aliases:
  - MIEM = "Ministry of Industry, Energy, and Mining" (L12, expanded twice with different comma use). "Ministry of Industry, Energy and Mining" appears again in Resources (L62).
  - ANCAP = "Administración Nacional de Combustibles, Alcohol y Portland" (L14). Descriptions: "State-owned ANCAP" (L14); "The state-owned energy company ANCAP" (L31); "the Uruguayan state-owned oil refinery, ANCAP" (L49). ANCAP operates the La Teja refinery in Montevideo (L14).
  - UTE descriptions: "the state-owned company in charge of managing Uruguay's electrical grid" (L16); "the state-owned energy company UTE" (L49); "Uruguay's state-owned electricity company UTE" (L52); "National Electricity Utility - UTE" (L64). L31 and L49 use "state-owned energy company" for ANCAP and UTE respectively.
  - Other acronyms: SIN = National Interconnected System (L20); GOU = Government of Uruguay (L33); ANII = "national research and innovation agency" (L33); IDB (L46), UNIT (L26) and URSEA (L65) are not expanded; Mercosur (L24).
  - Hydrogen projects: Khairos project / Ventus / Montes del Plata (L35); H24U consortium of Saceem, CIR and Air Liquide (L37); HIF Global (L39); "Texas-based Syzygy Plasmonics", "NovaSAF 1" and Estancias del Lago (L41); Tambor Green Hydrogen Hub, "the German company Enertrag" and SEG Ingeniería (L43); ANCAP "H2U Offshore" (L49).
  - "H2U Offshore" (ANCAP, 2021, L49) and "H24U" (pilot consortium, L37) are similar names for different projects.
  - Places: Melo, Rivera (L18); Salto Grande (L18, L45, L46); Fray Bentos (L35); Paysandú (L39); Durazno (L41, also in L45 plant locations); Punta del Tigre (L52); Namibia (L14, L31).
- Tables: none.
- Lists:
  - L12, 2024 electricity sources: hydropower 42, wind 28, biomass 26, solar 3, fossil 1 (percent).
  - L14: import sources "such as Nigeria, the United States, and Argentina".
  - L45, four hydro plants: "Salto Grande (Salto), Palmar/Constitución (Rio Negro/Soriano), Rincón del Bonete (Tacuarembó/Durazno) and Baygorria (Rio Negro/Durazno)". The last is Baygorria.
  - L48: wind leaders "alongside Denmark, Ireland, and Germany".
  - L37: H24U uses of the $43.5 million (4): solar PV plant; electrolyzer; hydrogen refueling station; truck procurement and fuel-cell conversion.
  - L50: concession includes "the platform, the hydrolyzer, and green ammonia plant" (3).
  - L54: self-generation sites: remote schools, hospitals, hotels, sports clubs, new public buildings (5).
  - L61-66: Resources, 6 items. The last is "Balance Energético Nacional", with no URL.
- Quantitative figures in prose:
  - L12:
    - 2024: "99 percent of its electricity from renewable sources" (hydro 42, wind 28, biomass 26; solar 3, fossil 1), per MIEM.
    - Preliminary 2024 MIEM data: "national energy production reached 17,202 GWh", "a rebound from the downward trend observed in 2023". "15,175.8 GWh was used to meet domestic demand, while 2,026.2 GWh was exported" (sum 17,202.0, map arithmetic).
  - L14: La Teja "around 50,000 barrels per day".
  - L16: in 2024 UTE "officially reported exporting 2.026 GWh for approximately $104 million". The "2.026" is printed this way.
  - L18: Brazil connections "currently 570 MV from Melo and 70 MV from Rivera". The unit "MV" is printed this way.
  - L20: SIN CO2 emission factor "7 tons of CO2 per GWh"; "88% reduction compared to 2023"; "lowest level recorded in the past decade". The year of the 7 t value is not stated.
  - L24: "an average of 14 percent duty applies to conventional equipment that are not products of Mercosur countries".
  - L26: "In May 2025, there were more than 300 charging stations distributed in every department". Standards "UNIT - IEC 61851-1:2017 and UNIT - 1234:2016".
  - L28: Montevideo goal "150 electric taxis by 2025"; national goal "300 electric buses in operation by 2025".
  - L31:
    - Namibia discovery "early 2022". ANCAP "awarded seven contracts" covering "all 120,000 square kilometers" of offshore waters, "generating over $200 million in investments".
    - Seismic work "commenced in 2025"; drilling "planned for 2026". Exploration "expected to span four years and could be extended by an additional two or four years".
  - L33: 2021 National Green Hydrogen Strategy; "could generate $2.1 billion per year by 2040".
  - L35: Khairos: "Scheduled to begin operations in 2026"; "2 MW electrolyzer powered by a 4.8 MW solar farm - comprising 8,000 solar panels"; "reduce CO2 emissions by 870 tons annually".
  - L37: H24U "$10 million grant"; "total estimated investment of $43.5 million".
  - L39: 2022 HIF Global "$6 billion project" in Paysandú; "approximately 256 million liters of e-fuels per year".
  - L41: June 2025 NovaSAF 1; "expected to be fully operational in early 2027"; "nearly 100% renewable energy grid"; "emissions more than 80% lower than conventional Jet-A fuels".
  - L43: Tambor "13,000 tons of hydrogen or 70,000 tons of e-methanol per year".
  - L45: "1,500 megawatts (MW) from four hydroelectric plants". Baygorria and Salto Grande were built "in 1960 and 1979, respectively".
  - L46: Salto Grande renovation "started in 2019 and will last until 2049"; "first stage of modernization will be concluded by 2024"; IDB credit line "of up to $800 million".
  - L48: "generating 31 percent of its total power from wind" (no year); "more than 1,525 MW of installed wind capacity"; wind speeds "6 to 9 meters/second" at "90 meters".
  - L49: UTE new wind investments "in 2032 via modules of 50MW"; "60 wind modules before 2049" (60 x 50 MW = 3,000 MW, map arithmetic; not stated); 2021 "H2U Offshore"; carbon neutrality "by 2050".
  - L50:
    - "between 8 and 16 blocks".
    - First block "more than 10 km" from the coast at a depth "between 10 and 30 meters". Second block "more than 100 km" out, "maximum depth of 50 meters".
    - Concession "term of 25 years"; bidding "from 8 months to a maximum of 2 years"; cost "between $1 and 3 billion".
  - L52:
    - Solar legislative support "since 2013"; "distributed solar generation reached 301 MW in 2023"; "1,700 KW per square meter of sunlight a year" (unit as printed).
    - 2024 Punta del Tigre park, part of a plan to "add 900 MW of solar capacity through 100 MW modules".
    - "$27 million in negotiable bonds in December 2024"; "expects to build 18 solar photovoltaics modules by 2049".
  - L57: "In 2024, biomass represented 46 percent of the total energy supply", while oil and derivatives were "responsible for 39 percent".
  - L59: biomass investment "increased considerably in 2013, reaching more than 400 MW", and "has not increased since then". Per Uruguay XXI, "in 2024 biomass represented 8 percent of the total amount of electric generation".
- Forecasts, targets, deadlines:
  - 2025: 150 e-taxis and 300 e-buses (L28). Status of the taxi goal at L28: "As of June 2025, there is no official confirmation on whether this target has been achieved". The bus target has no status line.
  - 2026: drilling (L31); Khairos operations (L35).
  - Early 2027: NovaSAF 1 (L41).
  - 2032: wind investment start (L49).
  - 2040: $2.1 billion per year (L33).
  - 2049: Salto Grande renovation end (L46); 60 wind modules (L49); 18 PV modules (L52).
  - 2050: carbon neutrality (L49).
  - "First stage ... by 2024" (L46) is written in the future tense in a 2025 publication; no actual is reported.
- Dated events: 2005 shift to renewables (L12); 2013 solar legislation and biomass build-out (L52, L59); 2019 Salto Grande renovation start (L46); 2021 National Green Hydrogen Strategy (L33) and H2U Offshore (L49); early 2022 Namibia discovery (L31); 2022 HIF Global announcement (L39); 2024 Punta del Tigre inauguration (L52); Dec 2024 UTE bonds (L52); 2025 seismic work start (L31); May 2025 charging-station count (L26); June 2025 NovaSAF 1 announcement (L41).
- Hedged claims:
  - L45: "Hydroelectric capacity is unlikely to grow given that the country is already producing an electricity surplus". The same line states the modernization as fact.
  - L43: "According to preliminary reports" covers the output figures; "Reports suggest that these outputs will largely be exported".
  - L33: "The government estimates ... could generate $2.1 billion".
  - L35: "is set to become Uruguay's first green hydrogen plant"; CO2 cut "is expected". Financial closure is stated as fact ("Notably, Khairos is the first project ... to have reached financial closure").
  - L39: "Uruguay is expected to become a leading country in the region in the development of e-fuels".
  - L41: "expected to be fully operational in early 2027".
  - L31: "expected to span four years and could be extended".
  - L12: "preliminary 2024 data".
- Rounded prose beside exact figures:
  - L12 "2,026.2 GWh" vs L16 "2.026 GWh".
  - L41 "nearly 100% renewable" vs L12 "99 percent".
- Notes:
  - L26 has two near-duplicate sentences about incentives for electric taxis and buses.
  - L55 "Information on the government's solar plan is available here." The link target is not captured.
- Operative definitions, rules and scope exceptions:
  - L39: e-fuels are "synthetic fuels that are produced using renewable energy".
  - L35: financial closure means "all necessary funding and investment agreements are in place to proceed with development and construction".
  - L24: "electric vehicles, renewable-energy generators and capital equipment can be imported into Uruguay duty free"; "an average of 14 percent duty applies to conventional equipment that are not products of Mercosur countries".
  - L26: "Type 2 connectors according to UNIT standards".
  - L50, ANCAP offshore-wind tender: "Companies must present a scope of work, that includes ANCAP participation". A tender is released "When ANCAP believes it has enough interested parties". Concession term 25 years.
  - L14: "the country does not produce hydrocarbons domestically and relies entirely on imports".
- Amendments or contradictions (both locations; no precedence stated):
  - Biomass share of 2024 electricity: L12 26% (MIEM) vs L59 8% (Uruguay XXI). L57 gives 46% on a different base (total energy supply).
  - Wind share: L12 28% (2024) vs L48 31% (no year).
  - 2024 exports: L12 "2,026.2 GWh" vs L16 "2.026 GWh".
  - Solar modules: L52 "900 MW ... through 100 MW modules" (map arithmetic: 9 modules) vs "18 solar photovoltaics modules by 2049" in the same line. The module size for the 18 is not stated.
  - CO2 factor: L20 attributes the fall to "increased biomass energy production following the startup of new pulp mill operations". L59 says biomass installed power "has not increased since" 2013. The two lines measure production and installed capacity respectively.
- Coverage: full. Ledger: L1-69 read in one chunk. Remaining unread: none. Missing source text: L55 link; Resources item without URL (L66).

## D20 - Vietnam: two chapters

- Source: `text/D20.txt` (169 lines), from `docs/ccg_energy_cleantech_sectors_vietnam.txt` | pages: not applicable
- Written or submitted by: U.S. ITA, "Vietnam Country Commercial Guide" (L3).
  - Contacts in both chapters: "Nam Tran, Commercial Specialist, U.S. Consulate General in HCMC, Nam.Tran@trade.gov" and "Janice Tran, Commercial Specialist, U.S. Embassy in Hanoi, E-mail: Bich.Tran@trade.gov" (L74-79, L163-166).
  - Attributions: "According to BMI Research" (L23), "According to the World Bank" (L88), "industry experts" (L35).
- Type, date, edition:
  - Chapter 1, `## Power Generation, Transmission, and Distribution` (L5). L6 "Last published: 2026-03-31". L7 "Source: https://www.trade.gov/country-commercial-guides/vietnam-power-generation-transmission-and-distribution".
  - Chapter 2, `## Environmental Technology` (L81). L82 "Last published: 2026-03-31". L83 "Source: https://www.trade.gov/country-commercial-guides/vietnam-environmental-technology".
- Headings in order:
  - Chapter 1: Overview L9; Regulatory Framework L10; Power Consumption L22; Power Generation L31; Transmission and Distribution L37; Leading Sub-sectors L45; Nuclear Power L46; "Liquified Natural Gas (LNG)-to-Power" L50; Renewable Energy L54; Opportunities L56; Resources L63; contact L73.
  - Chapter 2:
    - Overview L85; Institutional Framework and Policies L91; Leading Sub-sectors L99; Environmental Technologies Sector L100; "Key trends:" L103.
    - Industry Structure L108; Water Supply Infrastructure L113; "Wastewater Treatment: Market Dynamics" L117; Urban Wastewater Treatment L118; Industrial Wastewater Treatment L121; Outlook for U.S. Companies L124.
    - Air Pollution L130; Product Preferences and Challenges L135; Key Technologies in Demand L137; What You Need to Know L146; "Historical reliance on Official Development Assistance (ODA)." L151; Resources L155; contact L162; `-----` L168.
- Period covered: events June 2019 - March 2025; data "As of 2024" (L39, L116, L119, L122); forecast and target years 2025, 2030, 2032, 2034, 2035, 2045, 2050; PDP8R "framework ... from 2021 to 2030" (L20). No fiscal-year convention. USD only. The word "hydrogen" does not appear in D20.
- Entities and aliases:
  - Ministry of Industry and Trade (MOIT) (L11, L41, L48, L94; Resources L65).
  - Three MOIT-affiliated agencies (L11-13): Electricity Authority of Vietnam (EAV); Department of Electricity and Renewable Energy (run together with the EAV sentence at L12); Department of Energy Efficiency and Sustainable Development.
  - EVN has three expansions: "Vietnam Electricity (EVN)" (L15); "Electricity Vietnam (EVN)" (L38); "Electricity of Vietnam Group (EVN)" (L66 and again at L72).
  - The transmission company has four forms: "The National Power Transmission Corporation" (L18); "EVNNPT" (L38-44); "NPT" ("EVN/NPT-funded", L62); "Vietnam National Power Transmission Corporation (NPT)" (L67).
  - NSMO = "National Electricity System and Market Operation Company Limited", formerly under EVN as the "National Load Dispatch Center (NLDC)" (L19).
  - PDP8R = "Revised 8th Power Development Plan" (L19, L20, L41, L53, L55). Also "revised PDP8" (L47); "the initial plan" / "original" (L55).
  - "Deputy Prime Minister Son" (L20).
  - PetroVietnam (L47) vs "PetroVietnam Power Corporation (PV Power)" (L68). VINACOMIN = "Vietnam National Coal - Mineral Industries Holding Corporation Limited" (L69).
  - Nuclear institutions: MST, VARANS, VINATOM, IAEA (L48-49).
  - Environment ministries: MONRE, MARD, and the new MAE (L87); VEA (L92, L158); MOC (L93); MPS (L94); "Departments of Agriculture and Environment" (L95).
  - "GOVN" (L97) is not expanded; elsewhere the text says "Government of Vietnam". "HCMC" (L75, L163) = "Ho Chi Minh City" (L17, L41, L131).
  - Plants: Ninh Thuan 1 and Ninh Thuan 2 (L47); Nhon Trach 4 (L51).
  - Other organisations: BMI Research (L23); FitchSolutions (L70); Vietnam Energy Association (L71); World Bank (L88, L153, L159); Asian Development Bank (L153, L160); USAID (L161).
  - PPP has two law names: "updated Public-Private Partnership (PPP) Law" (L44) and "Law on Public-Private Partnerships (PPPs), effective from January 1, 2021" (L93).
  - The power law appears as "Electricity Law 2024" (L36) and "amended Electricity Law" (L44).
- Tables:
  - L138-145. Title L138: "Table: Priority Technology Segments for U.S. Companies". L139 is blank.
  - Header row L140: " | Segment Key Opportunities for U.S. Firms". The intended columns are Segment | Key Opportunities for U.S. Firms.
  - Rows verbatim:
    - L141 "Wastewater Treatment Advanced treatment systems, EPC, monitoring"
    - L142 "Air Pollution Control | Emissions monitoring, scrubbers, catalytic reduction, sensors"
    - L143 "Solid Waste & Waste-to-Energy Sorting, incineration, landfill design"
    - L144 "Drinking & Process Water iltration, membrane, reuse technologies"
    - L145 "Environmental Consulting | Filtration, membrane, reuse technologies"
  - No units, source line or notes.
  - Problems: the separator between the two cells is missing at L140, L141, L143 and L144. L144's second cell begins "iltration". L145's opportunity text repeats L144's.
  - The text matches the original (orig L136-143), so these problems are source-level. The web page is not available, so cell boundaries and the content of the L145 row are unresolved.
- Lists:
  - L15-18: EVN's "nine main subsidiaries" are Genco 1-3 (L16) + 5 power corporations (L17: Northern, Central, Southern, Hanoi, Ho Chi Minh City) + National Power Transmission Corporation (L18). 3 + 5 + 1 = 9 (map arithmetic).
  - L26-30: three demand drivers; the last is "Digital Transformation and High-Tech Industries".
  - L33: imports from "Laos and China"; exports to "countries like Cambodia, Singapore, and Malaysia".
  - L41: source regions Central Highlands, South Central Coast and North Central; demand hubs HCMC and the Red River Delta.
  - L48: five nuclear institutions; the last is MOIT.
  - L57: five generation segments, numbered (1)-(5). The last is IPP investment via BOT, BT, BTO and JV, all expanded.
  - L58: four transmission and distribution areas, numbered (1)-(4).
  - L59: further areas: offshore E&P, engineering steel fabrication, LNG supplies and infrastructure, petrochemicals. L60-62: three bullet opportunities.
  - L65-72: eight Resources entries. EVN is listed twice (L66 with URL, L72 without); L72 is last. URLs are given only at L66, L67 and L69.
  - L88: GHG sources: energy sector ("more than half"), then agriculture, industrial processes, waste.
  - L90: National action plan areas: air quality, water conservation, plastic waste pollution.
  - L104-107: four key trends; the last is "Decentralized and Modular Systems".
  - L125-127 plus L129: Outlook statements.
  - L132: air pollution sources: transportation, industry, construction, waste burning.
  - L136: preferred origins: United States, Europe, Japan, Australia.
  - L147-150: four "What You Need to Know" statements.
  - L153: donors "Japan, Germany, France, and other countries".
  - L157-161: five Resources entries; the last is "United States Agency for International Development". L157 still lists "Ministry of Natural Resources and Environment (MONRE)". No URLs.
- Quantitative figures in prose:
  - Chapter 1, L13-35:
    - L13: Vietnam Scaling Up Energy Efficiency Project launched June 2019.
    - L20: PDP8R "approved on April 15, 2025, by Deputy Prime Minister Son (Decision 768/QD-TTg)"; framework "from 2021 to 2030"; plans "map out ... ten years out".
    - L23: BMI Research: demand "growing at an annual average rate of 7.2% through 2034".
    - L32: Resolution No. 55-NQ/TW "dated 11 February 2020": "installed capacity by 2030 is expected to be 125-130GW, a doubling of capacity in 10 years".
    - L33, PDP8R: nuclear "operational between 2030 and 2035"; imports "9.4-12.1 GW ... by 2030"; exports "5-10 GW ... by 2035"; "By 2030 to 2035 ... 6-17 GW of offshore wind power and 4-6.4 GW of nuclear power".
    - L34: total power capacity "approximately 146,000 MW by 2030 and over 416,000 MW by 2045".
    - L35: combustible fuels "projected to account for 57% of power generation in 2034, up from an estimated 55% in 2025". Wind, solar, hydropower and biomass "48% of Vietnam's installed capacity by 2030", "at least 63% by 2050".
  - Chapter 1, L36-55:
    - L36: Decree No. 58/2025/ND-CP, enacted March 2025.
    - L39: "As of 2024": "about 28,600 km of transmission lines (10,053 km of 500 kV and 18,559 km of 220 kV)" (sum 28,612, map arithmetic); "176 substations (34 at 500 kV and 142 at 220 kV)"; "around 115,650 megavolt-amperes (MVA)"; "Over 90% of its business processes are digitalized".
    - L40: "99.7% of communes and nearly 99% of rural households".
    - L43: "approximately $62 billion ... through 2050", with "around $18 billion targeted for the 2026-2030 period".
    - L47: target "4-6.4 GW by 2030-35"; Ninh Thuan tasking in February 2025.
    - L49: 123 Agreement "signed in 2014".
    - L53:
      - LNG thermal capacity goal for 2030 "22,524 MW, accounting for 9.5-12.3% of the country's energy mix". The base of the percentage is not stated (22,524/146,000 = 15.4%, map arithmetic).
      - "In 2050 ... as high as nearly 50,000 MW". Gas/LNG demand "rise by an average of 12% per year", with "could experience a threefold increase by the mid-2030s".
    - L55, revised targets (old to new): renewable energy excluding hydropower "36% in 2030, compared to 30% in the initial plan"; onshore/nearshore wind "26,066-38,029 MW by 2030, up from the original 21,880 MW"; offshore wind "from 6,000 MW to 17,032 MW"; battery storage "10,000-16,300 MW from the previously planned 300 MW".
  - Chapter 2:
    - L87: merger effective "March 1, 2025".
    - L88: GHG emissions "multiplied fivefold in the last 20 years".
    - L89: waste "expected to double in less than 15 years"; "Ninety percent of global marine plastic pollution is estimated to come from just ten inland rivers"; Vietnam is "among the ten countries most affected by air pollution".
    - L90: COP26 "November 2021".
    - L93: PPP law "effective from January 1, 2021"; "MOC's 2021 draft bill".
    - L95: Revised LEP "passed ... in May 2021", "went into effect in January 2022", replacing "the 2014 version".
    - L96: "Decree 06 on January 7, 2022"; National Methane Emissions Inventory 2020.
    - L97: "April 2022 ... Decision 450/QD-TTg ... to 2030, vision to 2050".
    - L98: Solid waste strategy "by 2025, vision to 2050".
    - L104: water purifier market "expected to double by 2032".
    - L111: "By 2024 ... about 12.2 million cubic meters per day, up from 11.5 million cubic meters in 2022-an average annual growth rate of 6%".
    - L115: water loss "projected to decline to 15.8% by 2025, from 17.5% in 2022".
    - L116: "As of 2024 ... more than 780 operating water plants"; household consumption "+4.8% year-on-year"; industrial "+8.2%"; tariffs "averaging 3%".
    - L119: "only an estimated 16% of urban wastewater collected and treated as of 2024".
    - L122: "As of 2024, over 55 wastewater treatment plants ... combined capacity exceeding 2 million cubic meters per day"; "about 80% of plants use activated sludge".
    - L133: "20% reduction in ... NOx, SOx, and particulate emissions from heavy industries by 2025".
- Forecasts, targets, deadlines:
  - Nuclear 2030-2035 (L33, L47); imports by 2030; exports by 2035 (L33); 146,000 MW by 2030 and 416,000 MW by 2045 (L34); 48% by 2030 and 63% by 2050 (L35); LNG 22,524 MW in 2030 and about 50,000 MW in 2050 (L53); L55 revised targets; transmission funding $62 billion through 2050 and $18 billion in 2026-2030 (L43).
  - Net zero / carbon neutral 2050 (L32, L55, L90, L95).
  - Targets dated 2025, before the publication date: water loss 15.8% (L115); 20% emissions cut (L133); solid-waste strategy (L98). No 2025 actuals are reported.
- Dated events: June 2019 EE project (L13); 11 Feb 2020 Resolution 55 (L32); Jan 1, 2021 PPP law in effect (L93); May 2021 Revised LEP passed (L95); Nov 2021 COP26 (L32, L90, L95); Jan 2022 LEP in effect (L95); Jan 7, 2022 Decree 06 (L96); April 2022 Decision 450 (L97); July 2024 DPPA approved (L21); Aug 2024 NSMO starts as operator (L19); Feb 2025 Ninh Thuan tasking (L47); March 1, 2025 MAE merger (L87); March 2025 Decree 58 (L36); April 15, 2025 PDP8R (L20, L53). The Nhon Trach 4 synchronization (L51) is undated.
- Hedged claims:
  - L23: inside the BMI paragraph, "we expect the recent liberalization ... to boost private investment". L35 repeats the sentence with "industry experts expect".
  - L32: "is expected to be 125-130GW".
  - L33: nuclear "expected to be operational ... with potential for earlier deployment if conditions permit".
  - L35: "projected ... 57%" and "an estimated 55%".
  - L47: "EVN would invest ... PetroVietnam would fund" is conditional. The February 2025 tasking is stated as fact. "traditional large-scale reactors are being considered".
  - L53: "is projected to rise as high as nearly 50,000 MW"; "could experience a threefold increase".
  - L44: implementation guidelines "are still under development"; opportunities "are expected to grow".
  - L89: "expected to double"; "is estimated to come from just ten inland rivers".
  - L104, L115 and L119 use "expected", "projected" and "estimated" respectively.
- Rounded prose beside exact figures: L39 "about 28,600 km" vs the components (sum 28,612). L111 "6%" average annual vs the two-year change from 11.5 to 12.2 (+6.1% over 2022-2024; compound about 3.0% per year, map arithmetic).
- Notes:
  - Same-line run-together at L12.
  - The contact name "Janice Tran" sits beside the e-mail "Bich.Tran@trade.gov" (L77-79, L165-166).
  - L94 refers to "the three ministries" without naming them. The paragraphs around it name MAE (L92), MOC (L93), MPS and MOIT (L94).
- Operative definitions, rules and scope exceptions:
  - L21, DPPA: "enables renewable energy producers to supply electricity directly to consumers, bypassing traditional utility intermediaries".
  - L32: "PDP8R is required to comply with the policies stated in Resolution No. 55". L32 calls the Central Committee of the Politburo "the highest body of the Communist Party of Vietnam".
  - L36, Decree 58: "prioritizing grid access for storage-equipped systems during peak demand hours".
  - L15: EVN "holds a monopoly on transmission and distribution". L18: NPT "is the only company in the transmission sector". L38: "EVNNPT still operates the entire high-voltage grid". L44: the "government now permits non-state ownership of transmission and substation assets", with guidelines still under development.
  - L49: "123 Agreement" = "Agreement for Cooperation Concerning Peaceful Uses of Nuclear Energy".
  - L95: Revised LEP requires "factory operators to use the best available technologies".
  - L109: water utilities "hold exclusive rights to distribute water locally".
  - L133: "New regulations require continuous emission monitoring for major emitters".
- Amendments or contradictions (both locations; no precedence stated unless noted):
  - 2030 capacity: L32 (Resolution 55) 125-130 GW vs L34 (PDP8R) about 146,000 MW. L32 states that PDP8R must comply with Resolution 55.
  - Offshore wind: L33 "6-17 GW" by 2030-2035 vs L55 "from 6,000 MW to 17,032 MW". The low end of L33's range equals L55's old value.
  - Renewable share by 2030: L35 48% (wind, solar, hydro and biomass, installed capacity) vs L55 36% (renewables excluding hydro). The bases differ.
  - COP26 pledge: "net-zero emissions by 2050" (L32); "carbon-neutral economy by 2050" (L90); "net-zero carbon emissions (GHG) by 2050" (L95).
  - Ministry: L87 says MONRE was merged into MAE on March 1, 2025; Resources L157 still lists MONRE.
  - Amendment order, power planning: Resolution 55 (11 Feb 2020) -> initial PDP8 (date not stated; "original"/"initial plan", L55) -> PDP8R (approved/issued April 15, 2025, Decision 768/QD-TTg; L20, L41, L53).
  - Amendment order, environmental law: 2014 LEP -> Revised LEP (passed May 2021, effective January 2022) (L95).
  - Amendment order, Water Supply and Sewerage law: MOC is drafting it ("The proposed law", "2021 draft bill", L93). It is not enacted in the text.
- Coverage: full. Ledger: L1-120 read; L120-169 read (two chunks, overlapping at L120). Remaining unread: none. Missing source text: URLs for most Resources entries.

## Shared ground within this part (navigation only)

- Issuer and editions:
  - All five are U.S. ITA Country Commercial Guide chapters (L3 in each). No document in D16-D20 cites, amends or responds to another bundle document.
  - "Last published" dates: D18 2023-11-03, D16 2024-07-31, D19 2025-08-15, D17 2025-08-25 (L6, L66), D20 2026-03-31 (L6, L82). D18's body runs past its stated date (to June 2025 and 2026 events).
  - Two-chapter documents: D17 (L5/L65) and D20 (L5/L81).
- Organisations quoted as data sources, separate from the issuer: D16 Red Electrica (L31), EY (L33), IEA (L38), European Commission (L38); D18 IEA (L10); D19 MIEM (L12), UTE (L16), Uruguay XXI (L59); D20 BMI Research (L23), World Bank (L88).
- 2050 net zero / carbon neutrality: D16 L36, L49; D17 L20, L72; D18 L33; D19 L49; D20 L32, L55, L90, L95.
- 2030 targets by document:
  - D16: storage 20 GW (L37); electrolysis 4 GW (L49) / 11 GW (L51); EU 45% (L38).
  - D17: $54 billion (L20); MBR 5 GW (L24); Masdar 1 Mt hydrogen (L32); 32% renewable share (L72).
  - D18: 95% clean power (L13); offshore wind 43-50 GW (L25); 8 reactor closures (L22, L35).
  - D20: 125-130 GW (L32) vs about 146,000 MW (L34); 48% (L35); 36% (L55); LNG 22,524 MW (L53); wind and storage ranges (L55).
- Hydrogen: D16 L43, L48, L49, L51 (Hydrogen Roadmap 2021); D17 L26, L31, L32, L34, L36, L72 (National Hydrogen Strategy 2050, unveiled 2023); D18 L14, L15 (mentions only); D19 L10, L22, L32-43, L49-50 (2021 National Green Hydrogen Strategy, projects). D20 has none (zero hits).
  - Electrolyzer figures: D16 L49/L51; D17 L36 ("multi-megawatt"); D19 L35 (2 MW), L37, L43, L50 ("hydrolyzer").
  - Green ammonia: D17 L32, L36; D19 L50. Aviation fuel: D17 L32 (Green Falcon); D19 L41 (NovaSAF 1).
- Storage: D16 L37, L44-47; D18 L27-29, L57-60; D19 L22, L54; D20 L33, L36, L55.
- Nuclear: D16 L18 (7,117 MW row), L32 (France); D17 L14, L24, L72; D18 L21-24, L31-35; D20 L33, L47-49. SMRs: D18 L24, L33; D20 L47. U.S.-linked nuclear facts: D18 L32, L35 (U.S. engineering firms); D20 L49 (123 Agreement, 2014).
- Offshore wind: D16 L42 (heading only); D18 L25-26, L38-39, L59; D19 L49-50; D20 L33, L55.
- Waste-to-energy, water and air: waste-to-energy D17 L26, L44-48, L76, L110 and D20 L143. Desalination D17 L38, L70, L77, L84, L103 and D20 L114. Wastewater D17 L83-90, L102 and D20 L117-129, L141. Air quality D17 L95-98, L111-115 and D20 L130-134, L142.
- U.S. as a supply source: D16 L35 (U.S. LNG 29% of 2022 gas imports); D18 L10 (principal source of UK imported energy, 2024); D19 L14 (crude/refined imports); D20 L51 (U.S. LNG suppliers "well-positioned").
- Cross-border power: D16 L32 (France), L58 (Iberian market with Portugal); D18 L12 (2024 net importer); D19 L16-18 (Argentina, Brazil); D20 L33 (Laos/China imports; Cambodia/Singapore/Malaysia exports). Grid constraints: D18 L18 (connection wait times), D20 L40. Curtailment: D18 L28 (8.3 TWh, 2024); D20 L40-42.
- Abbreviation and alias collisions:
  - "PV" means photovoltaic in D16 and D19; it is part of the project name "Abu Dhabi PV3" in D17 L24; it means PetroVietnam Power Corporation in D20 L68.
  - NESO has two expansions within D18 (L28, L54).
  - EVN has three expansions within D20.
  - Distinct agreement terms: PPA (D16 L33, L40); DPPA (D20 L21); PPP (D20 L44, L93).
  - "state-owned energy company" is used for ANCAP (D19 L31) and for UTE (D19 L49).
  - Similar project names in D19: H2U Offshore (L49) vs H24U (L37).
- Forecast/actual and status pairs:
  - D17 L44: first phase July 2023, then "fully operational since September 2024".
  - D17 L48: completed 2022, then Phase 2 announced January 2025.
  - D17 L46: proposals received May 2023; no award stated.
  - D19 L28: 2025 e-taxi goal, status unconfirmed as of June 2025.
  - D19 L46: "first stage ... will be concluded by 2024"; no actual.
  - D20 L115 and L133: 2025 targets; no actuals.
  - D16 L37: EV investment "by 2023"; no actual.
  - D18 L38: Dogger Bank 2026. D18 L32: Hinkley Point C 2029.
- Proposed vs final rules:
  - D16 L38: REPowerEU "proposes"; 45% vs 40% "previously under negotiation".
  - D18 L23/L33: Feb 2025 reform replaces the EN-6 eight sites. D18 L24: SMR choice "subject to final government approvals".
  - D20 L93: water law is a draft while the PPP law is in force (Jan 1, 2021). D20 L95: LEP 2014 -> 2021/2022. D20 L55: PDP8 initial -> PDP8R.
  - D17 L22/L72: Energy Strategy 2050, original vs "updated".
- Same-document conflicts:
  - D16: L11 vs L28-30; L49 vs L51.
  - D17: L56 vs L123.
  - D18: L25 vs L59; L10 vs L12; L28 vs L54.
  - D19: L12 vs L59; L12 vs L48; L12 vs L16; L52 (900 MW vs 18 modules).
  - D20: L32 vs L34; L87 vs L157.
- Exclusion and negative facts:
  - D16: L36 (hydrocarbon prohibition); L49 (roadmap excludes low-carbon hydrogen); L59 (only Naturgy and Endesa are dominant in natural gas; REE 20% is the state exception).
  - D18: L22 ("All but one"); L23 (Scotland excluded from the reform).
  - D19: L14 (no domestic hydrocarbons); L24 (14% duty only on non-Mercosur conventional equipment); L45 ("unlikely to grow"); L49 (no short-term UTE wind investment); L59 (biomass capacity not increased since 2013).
  - D20: L18/L38 vs L44 (transmission exclusivity vs new non-state ownership).
- Late list members: D16 L59 natural-gas and fuels/LPG "dominant" sentences come after the broader operator lists; D17 L20 (last milestone); D17 L32 (Khalifa University); D18 L53 (NIE repeated as last DNO); D19 L66 (Balance Energético Nacional); D20 L72 (EVN repeated as last Resources entry); D20 L161 (USAID).
- Cross-part pointers (grep hits only, not mapped here; the owning mappers cover these documents):
  - Spain at D12 L30, L42.
  - UAE at D06 L53 and D09 L16; IRENA at D09 L13.
  - Fitch at D14 L54; Fluor at D02 L98.
  - COP, SMR, IEA and Paris-agreement terms appear in 15 documents (count search only).
