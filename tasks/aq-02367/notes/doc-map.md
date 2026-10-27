# aq-02367 - document map

Maintained by the caller from `text/`. Navigation only; questions quote the documents, never this map.

## Bundle

- What it is: four UK government papers on heat network zoning in England: the October 2021 BEIS
  consultation, its consultation-stage impact assessment (IA), the June 2022 government response, and
  a 2026 DESNZ summary of the response to the December 2023 consultation.
- Same bytes as aq-02220 (all four `docs/` and `text/` files sha256-identical, checked 2026-10-09). Its
  seven too-easy designs and twelve hooks carry over as closed families (see hooks.md). A second task on
  identical documents means the platform's Original question check can see aq-02220's drafts: reuse no
  sentence frame from tasks/aq-02220/questions or its sketches.
- Documents (local id = task-page Doc N): D03 = Doc 1 consultation 2021; D02 = Doc 2 IA; D04 = Doc 3
  government response June 2022; D01 = Doc 4 2023-consultation response summary (copyright 2026).
- Gaps: none. Capture AQ-02367_2026-10-09_0158.txt says "4 of 4 read in full (483,587 characters)";
  intake.json: all four `matches_capture: true`, `gap_characters: 0`. The page carried the "Docket has
  been updated. Reload this page" banner (navigation only; document bodies complete).
- Extraction: plain-text captures, so text/ equals docs/ apart from the `# Dnn` header. aq-02220's
  spot-checks (Table 12 pairs, Table 6 rows, Table 24 names-then-values, delivery-model prose, response
  tables) apply byte for byte. Re-read in full by the caller on 2026-10-09 (all four, every line).
- Provenance: notes/intake.json (capture sha256 263e90e5...); source sha256 D01 7f1b34a7..., D02 d1e154c1...,
  D03 21af35ab..., D04 273adfda... (identical to aq-02220).
- Reuse binding: entries below are aq-02220's map (built 2026-10-08 against the same hashes) plus the
  caller's 2026-10-09 additions marked "(add)".

## D03 (Doc 1) - Proposals for heat network zoning, consultation (BEIS)

- Written by: BEIS (foreword Lord Callanan). Issued 8 October 2021, closing 19 November 2021 (L62-65, L1591).
- England only. 60 numbered questions (in-text and list L1726-1887).
- Key numbers: CCC 18% of UK heat demand by 2050, 2% today (L23, L138, L169); over 14,000 heat networks
  "(12,000 communal and 2,000 district)", 480,000 consumers (L169); £320m HNIP (L171); GHNF £270m (L218 fn5);
  IA headline "benefits worth £560 million ... additional 31 TWh of deployment in the period to 2050 (around 7%
  of total UK heat demand)" (L155); options: £560m / £290m / net costs £110m SNPV and around 31 / 21 / 5 TWh in
  2050 (L801-808); "large" = over 100 MWh a year (L822-824); growth rate around 6% (L765); Denmark grace nine
  years, proposed 10 years (L911-914); 310 TWh/yr available heat, UK building demand "of the order of 486
  TWh/year", waste heat 14 TWh of 76 TWh DHN economic potential in England, "which is about 19% of all heat
  demand in England" (L927); CDDP six cities (L530); 50-60 towns and cities for early adopters (L1620); response
  within 12 weeks of closing (L1602); piloting nine months (L1609).
- (add) Option 3 (L795) includes "large residential buildings which already have communal heating, or are
  undergoing major refurbishment"; the IA's Option 3 omits the refurbishment group. Exec summary L144.
- (add) Low carbon requirement "from as soon as the zone is implemented" for new networks (L1076); metric gCO2
  per kWh, level not proposed (L1061-1071). Exemption criteria a-e (L873-886); triggers a-e (L901-908);
  connection cost elements a-e (L841-847); information parties (L976-982).
- Delivery models for methodology stages (L615-708): A central-government-led (CG leads identification and
  feasibility); B local-authority-led (CG leads 1a; LA leads 1b and feasibility); C private-sector-led (CG leads
  1a and 1b, "both aspects of the zone identification stage"; feasibility "likely be led by the private
  sector", fn 18). Table glyphs for lead/support lost; prose descriptions L617, L647, L672-673.
- Methodology: two stages, zone identification (1a national, 1b local) and feasibility (L574-606).
- Ownership/delivery categories 1-3 (public sector, third party/private ESCO, open market) (L1180-1232),
  referred to as "Table 4" although labelled Table 2.
- Glossary L1633-1679 (Central Authority, Zoning Coordinator, micro-business < 10 people); statutory consultee
  list L1891-1935 (17 entries). Coverage: full.

## D02 (Doc 2) - Heat Network Zoning Consultation Stage IA (BEIS035(C)-21-CH)

- Dated 27/09/21, signed 15/09/2021. Summary sheets in 2019 prices: option 1 -£110m, option 2 £270m, option 3
  £530m net benefit; option 3 total cost £9,940m, total benefit £10,470m (L20-395).
- Table 2 target buildings (heat demand 49/9/41%, buildings 41/8/51%) L829-844; (add) para 39 L791 applies the
  >100 MWh test to communally heated residential blocks too; para 50 L860 "only deduct 59%" (= 100 - 41,
  while 49 + 9 = 58). Table 3 assumptions (200 towns, 80% scaling, 4,984 kWh/yr new-build household, 14% stock
  growth, linear deployment 2025-2050 L953-955) L864-959. (add) para 17/56: 97% individual, 3% heat networks.
- Table 4 central technology mix (EfW 9, HT waste 4, LT waste 6, ASHP 14, GSHP 24, WSHP 34, back-up boilers 10;
  sums to 101) L988-1007; para 54 "19% of heat network heat demand could be met with waste heat sources" L979,
  naming "waste heat sources that require a water source heat pump"; (add) para 108 L1947 groups "EfW, High and
  Low Waste heat sources" against "heat pumps" (so whether LT waste counts as heat-pump heat is two-way).
- Table 6 designation costs L1083-1177: stage 1a national mapping £5,000 per town/city; 85% go to stage 1b;
  stage 1b local refinement £50,000 per city; 3 zones per city; feasibility £40,000 per study; concession
  £300,000; DPD £850,000 per town/city; 75% concession. Para 61-62: 200 towns and cities, costs 2024-2030.
- Table 7 coordinators (170 x 3 FTE = 510; alternative 35 x 9 = 315) L1197-1213; para 79 "510 zones in total".
  Table 17 relabels stage costs ("Stage 1" £5,000, "Stage 2" £50,000, "FTE per zone 3") L1808-1890.
- Table 9 regulator costs (Low/Medium/High by year) L1269-1310; para 70 "roughly 3,500 additional district
  heat networks by 2050" L1259. (add) Table 10 familiarisation 7.5 hours, £26/hour, "Years 2 - 6 of policy
  (2025 - 2030)"; para 81 20% of required buildings apply for exemption; Table 11 15 hours each.
- Para 89: England total heat demand 439 TWh in 2050 L1495. Table 12 deployment (TWh): Low 0.1-5.1; Medium and
  High printed as pairs per year (0.1/0.1, 4.2/6.3, 8.3/12.5, 12.5/18.8, 16.6/25.0, 20.7/31.2) L1497-1553.
- Table 13 SNPV in 2020 prices (560 / 290 / -110) L1558-1632, fn 23 on price base L1638; (add) its components do
  not sum to the SNPVs (high: 585 vs 560). Table 14 carbon by budget (garbled; two monotone parses exist, and
  neither matches the summary sheet's traded 1.8 / non-traded -11.2) L1648-1685; para 107 "£562m ... 31 TWh/yr"
  L1893; Tables 18-20 sensitivities; (add) para 110 "reduced by over 70%" vs Table 25 lower 4.7 of 31.2.
- Annex 1 Table 21 capex, Table 24 thermal efficiency L2230-2257: ASHP 321, GSHP 284, WSHP 330, WSHP low 541,
  WSHP medium 690, EfW 500, heat exchanger N/A, gas CHP 40, back-up gas boiler 85 (heat network); commercial gas
  boiler 84, domestic gas boiler 86, electric heater 100 (individual). Annex 2 Tables 23-25 sensitivity (Low and
  Medium blocks interleaved in the capture).
- Coverage: full.

## D04 (Doc 3) - Proposals for heat network zoning: government response (June 2022)

- BEIS, June 2022. 101 responses (L31, L55). Pilot in 28 towns and cities (L57, L1144). Queen's Speech "10th May"
  (no year) L48. HNIC investment potential £60-80bn by 2050 (L39).
- Per-question summaries for all 60 questions; agree/disagree tables give counts and % of non-blank responses
  (footnote 2). Q12 FTE per zone estimates 1 to 8 (L520); Q23 100 MWh threshold (Agree 14, Neither 23, Disagree
  14; (add) this table alone orders Neither before Disagree and sums to 100; 3 stakeholders proposed 50 MWh;
  9 warned communally heated/social housing could be excluded; 25-30 kWh/m2) L1237-1285; Q28 10-year grace
  period (38/21/6/0/36; (add) 19 of the 38 explicitly backed 10 years, 25 called it too long, 17 of them up to 6
  years) L1519-1566, government will shorten it L1603-1607; Q36 182 gCO2/kWh "reflecting the carbon intensity
  of gas" to 5-10 L1760; Q45 one full day (9/29/4/3/56) L2185-2227; (add) Q10 one trade association: SoS default
  coordinator above 10 GWh at full build-out, rejected L490 and L636.
- Decisions: SoS powers with DLUHC agreement; veto power; neither connection-cost option; Ofgem regulator;
  (add) pricing protections to all consumers required to connect; fines not an alternative to compliance.
- Annex A central authority / Zoning Coordinator functions L3115-3181. Coverage: full.

## D01 (Doc 4) - Heat network zoning consultation 2023: summary of government response (DESNZ)

- Copyright 2026. 2023 consultation 18 December 2023 to 26 February 2024; 156 responses (L22-24); regulations
  expected spring 2026 (L26). Warm Homes Plan target 7% (27TWh) by 2035, "a fifth of all heat by 2050" (L18).
- Renamed bodies: heat network zoning authority (was Central Authority), zone coordination bodies (was Zone
  Coordinators) L32-34. At least 10 towns and cities supported (L86). Design stage 12-18 months (L96).
- Emissions: from 2030 limit based on benchmark 85% heat from low-carbon ASHPs using electricity, 15% gas
  boilers; reviewed every 5 years; exact factors published before 2030 (L116-120). No grid carbon factor
  anywhere in the bundle (searched gCO2/kgCO2/carbon intensity/emissions factor).
- Required connections: new buildings (planning permission after designation); pre-existing communally heated
  domestic and non-domestic; pre-existing non-domestic > 100 MWh annual average with wet heating (L130-138).
  (add) Connection-charging powers await new primary legislation; caps intended: zero for pre-existing
  communally heated domestic, heat-pump-equivalent for new buildings, counterfactual for non-domestic (L142-144).
  Notice: 12-month window, minimum 6 months to agree the date (L150); temporary exemption up to 2 years (L152);
  Crown exemption (L166). Five social value outcomes (L110-112). Zone reviews only enlarge (L210).
- Penalty up to £1 million or 10% of annual turnover, whichever higher (L226); appeals 28 days (L232).
- Coverage: full.

## Shared ground (navigation only)

- CCC 18% by 2050: Doc 1 L23/L138/L169, Doc 2 L412, Doc 3 L38; Doc 4 instead "a fifth of all heat by 2050".
- 14,000 networks / 480,000 consumers: Doc 1 L169 (with communal/district split) and Doc 3 L38 (no split).
- 2021 consultation dates: Doc 1 and Doc 3. 10-year grace period: Doc 1 L914 and Doc 3 L1519/L1603.
- 100 MWh threshold: Doc 1 L822, Doc 2 L874, Doc 3 Q23, Doc 4 L136.
- IA figures repeated in Doc 1: £560m/£290m/-£110m (2020 prices, IA Table 13), 31/21/5 TWh (rounded).
- Opportunity Areas study: Doc 1 L927 (14 of 76 TWh), Doc 2 para 54 (19% waste heat) and para 89 (439 TWh).
- Delivery models A-C: Doc 1 only has roles by stage; Doc 3 L956-958 mentions LA-led and private-led models.
- (add) Current heat-network share: Doc 1/Doc 3 "2% of UK heat demand"; IA paras 17/56 "3%" of heating.
- (add) Option 3 text: Doc 1 L795 and Doc 3 L1205 (with refurbishment); IA L55-57 and L632 (without).
