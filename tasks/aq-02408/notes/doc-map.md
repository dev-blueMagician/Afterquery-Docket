# aq-02408 - document map

Maintained by the caller from `text/`. Navigation only, like the form's bundle overview; questions
quote the documents, never this map. Line numbers are `text/Dnn.txt` lines.

## Bundle

- What it is: six unrelated Federal Register documents on grid reliability/interconnection,
  Mar 2024 - Feb 2026 (FERC NOPR, DOE NOI, WAPA rate order, EPA proposed rule, DOJ antitrust
  notice, FERC order). No editions of one series; no proposal/final pair inside the bundle.
- Documents: 6; local D01-D06 = page Doc 1-6 (alphabetical file order matches page order).
- Gaps: none. Capture "6 of 6 read in full (461,743 characters)"; splitter: every source
  `matches_capture`, `incomplete: false`, gap_characters 0. All six texts read in full by the
  caller on 2026-10-09 (D01 L1-723, D02 L1-257, D03 L1-323, D04 L1-378, D05 L1-733, D06 L1-424).
- Extraction spot-checks: plain-text sources (method `text`), extraction = capture body minus a
  header line (char counts within 4-13 of the capture). Tables are FR fixed-width text flattened
  to dot-leader lines (D01 L573-581 burden table; D02 L26-33 meeting table, L208-219 permits;
  D06 L305-380 burden tables). No pipe tables. Footnotes inline (`\N\`).
- Provenance: notes/intake.json (capture sha c1c2cf71...), manifest hashes D01 b9a1eb44,
  D02 fd7cbee2, D03 133135e4, D04 e98a1b87, D05 44f0dbfa, D06 ac2b4026. No other bundle holds
  these files.

## D01 - FERC NOPR, Compensation for Reactive Power Within the Standard Power Factor Range (Doc 1)

- Docket RM22-2-000; FR 2024-06556, 89 FR 21454, published Thu Mar 28, 2024; issued Mar 21, 2024
  (L640, "Debbie-Anne A. Reese, Acting Secretary"). Comments May 28, 2024; replies June 26, 2024 (L29).
- Rule: standard power factor range 0.95 leading to 0.95 lagging (L99, L175); power factor = real /
  apparent power (L167, fn22 L170); small generating facility = no more than 20 MW (Order 2006, L199).
- Six Commission-jurisdictional RTOs/ISOs; only PJM (AEP Methodology), ISO-NE, NYISO pay in-range;
  CAISO, SPP, MISO do not (L234-242). SPP pays outside the dead band (fn78 L354).
- PJM numbers: capacity rules assume $2,546 per MW-year; revenue requirements ~$1,000-$13,000 per
  MW-year (L419); total PJM reactive compensation ~$384 million as of Dec 2023 (fn104 L439).
  Panda Stonewall ~$6.2M filed vs ~$2M set, ~$17M overcollection (fn90 L403-404); fn74 $2,051,894 /
  $10,018 heating losses (L346).
- Queues as of Feb 21, 2024 (fn113 L478): CAISO 453 facilities (440 non-synchronous), 122,885 MW
  (120,043 MW); SPP 947 (770), 175,243 MW (141,879 MW).
- NOI Nov 18, 2021; 37 initial + 10 reply comments (L259, L266); Appendix A commenter list L646-719.
- Info collection (L567-581): $100/hour from FY2024 average cost $207,786/year (fn124 L571); 516H 40
  TPs, 516 and 516A 43 TPs, 4 hrs/$400 each; totals 504 hrs, $50,400. 43 TPs affected, 6 small
  (~14%) (L607); SBA threshold 950 employees in body (L597-598) vs 500 in fn129 (L602): internal conflict.
- Compliance: filing within 60 days of final rule's effective date; 90 days to implement (L535).
- Typos: Order No. 827 cited "(June 23, 2006)" (L204, really 2016); "Docket No. RM22-13-000" (fn124).

## D02 - DOE GDO NOI, North Plains Connector EIS (Doc 2)

- FR 2024-24879, 89 FR 85182, published Fri Oct 25, 2024; signed Oct 21 (Maria D. Robinson), Oct 22.
- Scoping comments by Dec 9, 2024; five meetings Nov 6 (Mandan, CT), Nov 7 (Dickinson), Nov 12
  (Miles City), Nov 13 (Colstrip), Nov 19 (virtual) 2024 (L24-33).
- Project (L66-81): ~420 total miles; Rosebud 500-kV AC, two parallel circuits each ~3 mi, ROW ~320 ft;
  HVDC up to 525 kV ~341 mi, 200-ft ROW (MT ~172 mi Rosebud/Custer/Fallon; ND ~169 mi); Oliver 345-kV
  AC ~51 mi to Oliver County Substation (MISO interconnection, eastern grid); Morton 345-kV AC ~22 mi
  to Morton County Switchyard (SPP interconnection, eastern grid); Colstrip Substation = WECC point.
  (2x3 + 341 + 51 + 22 = 420.) BLM purpose statement says "approximately 400 miles" (L105).
- Federal land (L51, L105-119): BLM MCFO ~10 mi (~240 ac) MT; USFS DPG ~10 mi (~250 ac; 10.3 mi =
  3.1 Golden Valley + 7.2 Slope) ND; ARS Fort Keogh ~8 mi (~200 ac) MT. BLM MCFO and ARS Fort Keogh
  both "Miles City, MT" in SUMMARY (L21).
- Route alternatives (L149-179): Northern 8.5 mi shorter; Southern ~25 shorter; Tongue River almost
  30 shorter; Broadview endpoint +~100 mi (L187). NREL Seam Study B/C up to 2.89, NPV savings up to
  $28.8B (L93). Draft EIS Fall 2025, Final EIS Fall 2026; 45-day draft comment; objections within 45
  days; BLM/ARS/DEQ decisions no sooner than 30 days after Final EIS (L224-228).

## D03 - WAPA Rate Order No. WAPA-218 (Doc 3)

- FR 2025-12990, 90 FR 30910, published Fri Jul 11, 2025; signed Jul 7 (Tracey A. LeBeau), Jul 9.
- Provisional formula rates (WAUGP-ATRR, WAUGP-DCTIE-IMEU, WAUGP-AS1) effective first day of first
  full billing period beginning upon the later of UGP's expanded SPP participation in the WI or SPP
  RTO West go-live (scheduled Apr 1, 2026); through Mar 31, 2031 (L25, L112).
- History: WAPA-188 FERC-approved Sep 28, 2020 through Sep 30, 2025; WAPA-217 (notice Dec 20, 2024,
  89 FR 104143) extends through Sep 30, 2030; Proposed FRN Dec 30, 2024 (89 FR 106476); 90-day period
  ended Mar 31, 2025; forums Feb 19, 2025; no comments received (L29-40, L116-122).
- Definitions (L77-108): FY Oct 1-Sep 30; Eastern Interconnection tied to WI by six HVDC DC Ties;
  West DC Ties = Miles City, Stegall, Sidney; WI states list (portions of MT, SD, NE, NM, TX).
- UGP facilities in both interconnections separated by Miles City DC Tie and Fort Peck substation;
  WAUW BAA to merge into SPP West BAA (L147); Zone 19 = Upper Missouri Zone (L143).
- Formulas: ATRR = A+...+G (L242-244); IMEU Share = (E-C)*A, C = 1/B, E = 1/(B*(1-D)) (L312-317).
- SPP RTO West: WAPA FR notice Apr 28, 2023; SPP filing Jun 4, 2024; FERC accepted Mar 20, 2025 (L136).

## D04 - EPA proposed rule, CCR alternative closure deadline extension (Doc 4)

- FR 2025-21597, 90 FR 54611, published Fri Nov 28, 2025; Docket EPA-HQ-OLEM-2025-2864; Zeldin.
  Comments by Jan 7, 2026; virtual hearing Jan 6, 2026 9:00 a.m.-1:00 p.m. ET, 5 min per speaker
  (may be cut to no shorter than 3); pre-register by Jan 2, 2026; accommodations by Dec 17, 2025.
- Rule: >40-acre unlined impoundments under 257.103(f)(2): Oct 17, 2028 -> Oct 17, 2031 (L25-27,
  L374); <=40 acres Oct 17, 2023 (L121). 23 complete requests by Nov 30, 2020: 7 small, 16 large; 11
  still operating; completeness letters Jan 11, 2022 (L123-126). 13 units at 11 facilities (L287).
- Plants by market (L131-203): MISO - Baldwin IL 1,185 MW (Dynegy Midwest Generation; cease Dec 31,
  2025 -> Dec 31, 2027 per Apr 2, 2025 update), Big Cajun II LA Unit 1 580 MW (consent decree, no coal
  after Apr 1, 2025; Unit 3 coal, capacity not given), Brame LA Rodemacher 2 523 MW, Newton IL 615 MW
  (Jul 17 -> Sep 1, 2027 per Oct 22, 2025 update), RM Schahfer IN two boilers 847 MW; PJM - Kincaid
  IL 1,108 MW, Miami Fort OH 1,100 MW (Dynegy Miami Fort); ERCOT - Coleto Creek TX 650 MW (to gas
  after 2027); SPP - Welsh, Pittsburgh TX, 1,056 MW; Southwest - Intermountain UT 1,900 MW; Northwest
  - Naughton WY ~380 MW.
- NERC: six regional entities (fn12 L210); 2024 LTRA: 8 of 11 elevated-risk (MISO 5, PJM 2, SPP 1),
  3 normal (L219-224). DOE July 2025 report: 104 GW firm retirements by 2030 (L232).
- EPA estimates (L254-263): MISO ~3,200 MW online, nearly 10% of 32,345 MW MISO retirements by 2030;
  SPP 1,056 MW, about 14% (fn19 mislabels the 7,318 MW as MISO); PJM ~2,200 MW, about 13% of 16,706.
  (1,185+523+615+847 = 3,170 without Big Cajun II; 1,108+1,100 = 2,208.)
- Cost savings $7-12M/yr at 3%, $17-27M/yr at 7% (L109, L295). CWA action 90 FR 47693, Oct 2, 2025.

## D05 - DOJ, U.S. et al. v. Constellation Energy Corp. et al.: Proposed Final Judgment and CIS (Doc 5)

- FR 2025-23298, 90 FR 59205, published Thu Dec 18, 2025; complaint Dec 5, 2025; CIS Dec 12, 2025;
  60-day comment period (from notice, L29; CIS L667 "or ... newspaper ... whichever is later").
- Deal: announced Jan 10, 2025, $26.6B net (L56, L558). Constellation ERCOT ~5,000 MW (3,500 gas +
  44% of ~2,600 nuclear + ~170 wind; L64, L141-142), PJM >20,000 MW (25 plants + 3 partial);
  Calpine ERCOT ~9,000 MW (13 CC + 1 CT, 28% interest in another, L68), PJM >5,000 MW (14 plants).
  Post-deal ERCOT nearly 14,000 MW, >12% of ERCOT capacity, >20% of gas (L140-143).
- Relevant markets: ERCOT (>27M Texans, ~90% of demand, $14.4B 2024, peak >85,000 MW, ~1,200 MW
  imports via Mexico and SPP; L124-125, L599) and PJM Coastal Mid-Atlantic (SE PA, NJ, DE, eastern
  shores of MD and VA; ~$4B, >10M people; Nottingham constraint; L129-131). PJM serves 13 states + DC
  (L57, L97), >67M people, >$25B/yr.
- Divestitures (CIS L632-637): Jack A. Fusco 557 MW CC (Richmond TX); Gregory 365 MW CC, Calpine owns
  ~28.5% (complaint says 28%); Bethlehem 1,134 MW (2003); York 1 569 MW (2011); York 2 828 MW (2019);
  Hay Road 1,136 MW dual-fuel CC (1989); Edge Moor 707 MW simple cycle (1965). PJM sum 4,374 MW.
- Final Judgment: definitive contract within 240 days of consummation, up to two 30-day extensions;
  regulatory approvals within 5 days; divest within 30 days of last approval (+15); expires 10 years
  from entry (terminable after 5) (L382, L496). "Good Utility Practice" names "North American Electric
  Reliability Council" and "Mid-Atlantic Area Council" (L341). "One MW serves 800 to 1,000 homes" (L65).

## D06 - FERC order approving IBR/generator modeling Reliability Standards (Doc 6)

- Dockets RD26-1/2/3-000; FR 2026-03659, 91 FR 8864, published Tue Feb 24, 2026; issued Feb 19, 2026.
  Commissioners Swett (Chairman), Rosner, See, Chang, LaCerte (L17).
- NERC petitions Nov 4, 2025 (second tranche of Order No. 901): DER definition, MOD-032-2, IRO-010-6,
  TOP-003-8; MOD-033-3 (validation at least once every 24 calendar months, L190); MOD-026-2
  (consolidates MOD-026-1/MOD-027-1; R3 EMT models for FACTS, HVDC systems, registered IBRs; legacy
  facilities without OEM EMT support excluded; legacy = COD before MOD-026-2's effective date).
- Notice "90 FR 53320 (Nov. 25, 2026)" [sic] with comments/interventions due Dec 8, 2025; Calpine
  Corporation moved to intervene in all three dockets; ERCOT, ISO-NE, MISO, "New York System Operator
  Inc." [sic], PJM and SPP ("the ISOs") commented in RD26-3; NERC reply Dec 19, 2025 (L230-231).
- Category 2 GO/GOP: non-BES IBRs >= 20 MVA aggregate at >= 60 kV (fn15 L73-74); 491 cat-2 GOs, 310
  cat-2 GOPs (L297); GO 1,343 + 491 = 1,834; GOP 1,023 + 310 = 1,333 (fn65, fn68).
- Burden: $63.52/hour (= $53.39 + $10.13 from BLS $71.19 x .75 and $40.51 x .25; fn64 L302). Table
  cells print per-response cost with "/hr" labels ($508.16 for 8 hrs, $1016.32 16 hrs, $762.24 12 hrs,
  $635.20 10 hrs; one GOP row "$565.36/hr" inconsistent, L344). Totals: MOD-032-2 26,704 hrs
  $1,696,238.08; IRO-010-6 32,688 hrs $2,076,341.76; TOP-003-8 32,592 hrs $2,070,243.84; MOD-033-3
  1,952 hrs $123,991.04; MOD-026-2 27,312 hrs $1,734,858.24. Registry Dec 3, 2025: BA 97, DP 299,
  PC 62, RP 157, TO 341, TP 208, TSP 70, RC 12, TOP 170.

## Shared ground (navigation only)

- SPP in all six (D01 L242/L354/L478; D02 L81; D03 throughout; D04 L192-193, L224, L254; D05 L125;
  D06 L230). PJM in D01, D04, D05, D06. MISO in D01, D02 (L79), D04, D06. ERCOT in D04, D05, D06.
  CAISO only D01. NERC in D01 (registry), D04, D06; D05 uses the old name "Council".
- Calpine: D05 (party) and D06 (intervenor, L230, L258). Dynegy: D01 (Vistra Corp. and Dynegy
  Marketing and Trade, commenter; fn28 cites Dynegy Midwest Generation, Inc. (2008)) and D04 (Dynegy
  Midwest Generation LLC = Baldwin; Dynegy Miami Fort, LLC).
- Miles City: D02 (BLM MCFO, ARS Fort Keogh, scoping meeting) and D03 (Miles City DC Tie).
- HVDC between the eastern and western grids: D02 (proposed NPC) and D03 (six existing DC Ties).
- FERC hourly burden cost: D01 $100/hour (FY2024) vs D06 $63.52/hour (BLS).
- No document cites, amends or responds to another bundle document.
