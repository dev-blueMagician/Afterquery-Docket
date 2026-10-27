# aq-06007 - document map

Maintained by the caller or optional `bundle-mapper` from `text/` (and `docs/` for layout issues).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map. "L" = line number in `text/DNN.txt`
(`docs/` line = text line - 2, because text files carry a two-line header). Facts only; no hooks.

## Bundle

- What it is: 16 public submissions to the Productivity Commission study "Impacts of Heavy Vehicle
  Reform" (dated 5-19 December 2025 where a date is printed). The Commission's five reform areas /
  "information requests" recur across submissions: (1) increasing heavy vehicle road access to reduce
  emissions and increase productivity; (2) National Automated Access System (NAAS); (3) National Heavy
  Vehicle Driver Competency Framework (NHVDCF); (4) barriers to EV/HZEV truck charging infrastructure;
  (5) curfews for EV trucks / HZEVs. No Commission document itself is in the bundle.
- Documents: 16; D01-D16 from `text/manifest.json`; platform Doc N = local DNN.
- Gaps: none unread; all 16 documents read sequentially in full. Source-content gaps (image-only charts or
  tables, blank place names, flattened multi-column layouts) stay unresolved because only text captures
  exist; exact lines are under "Gaps and coverage ledger" at the end.
- Extraction spot-checks: 21 lines across all 16 documents, including table rows and footnotes, are
  identical in `docs/` and `text/` (docs line = text line - 2). Page count not applicable; see ledger.
- Provenance: `notes/intake.json` capture_sha256 8b0b66b3f297d355981537ab9e48035192693d8bdfadf289057f28c17f7952b8
  (capture AQ-06007_2026-10-16_0846.txt, "16 of 16 read in full (569,934 characters)"); every entry
  `incomplete: false`, `gap_characters: 0`, `matches_capture: true`. The capture's stale-page notice
  ("Docket has been updated. Reload this page...") concerns the page's checks, not document text.
  Extraction method "text", `pages: null` for all 16 (plain-text sources; no PDF originals in workspace).
- Reuse binding (source sha256 = extracted-text binding from manifest; no earlier map existed):

| id | source | sha256 | chars |
| --- | --- | --- | --- |
| D01 | sub003 | 92003acb5a189498fc0bd57227336da9059c75915515c24933baeb9d658992e3 | 16210 |
| D02 | sub004 | bc6f6c5ee41c69ce26d4fe33c67418d87adf496711f6592181ee0b64c235e5d8 | 82087 |
| D03 | sub006 | ee8ec121b8a84889934c5eb18c9a3bd4e63a336251276a4e2ba37d38739ec3a9 | 13046 |
| D04 | sub008 | 2569bcff2c3bbadf760fe96861e483cd5d75133eb2ff0812130347494adf092d | 40617 |
| D05 | sub010 | bf3ee231ffd7bbea7fd90ea053defa81a7ff093cc46c709b50e4e7f704b2b2cb | 31423 |
| D06 | sub012 | b0a7876f749532c278ed40a4a7f983a416b72b20d5bc07a4ad6b24eb4df0a737 | 39636 |
| D07 | sub015 | 392e6b04e9631e6d73e1380442232f0aeba7677ad7b74ae6406238ae77315897 | 25805 |
| D08 | sub016 | 8e170b40450d08677654b3f757f077adb4312ff640615c28e1e1d7ed8d93de21 | 18595 |
| D09 | sub018 | 015d3d836e39578a27c41467b70b11220a5fc794ba10a65467607b8eb861d431 | 50618 |
| D10 | sub019 | faf1bb0159f084bfa11a8b95b9b757ad4611295a3dafddba9a2b30d618297f74 | 100170 |
| D11 | sub022 | 0915e7a42d3612a5859b378780c821568bd3c66ecda1c45e4d2467f21fff0e5e | 28434 |
| D12 | sub024 | f7861ce8d9ab7c519cd0194b4db3467bfa774d12eae7dc44bf476f5f9ba3a105 | 11171 |
| D13 | sub025 | a3019397678bc63b2ebfe535dd9ae6fc6a905f4dbf98e321db016a1716437066 | 23029 |
| D14 | sub028 | 0c1a7720960b5b80f78e5b4912d59ec6c4f085d8c98af3c0c368b25b83307d1c | 49228 |
| D15 | sub029 | de5aab80787bbf33e290bf6cd2b2006d466fe7ec1d3ea8c93b201733b43582f5 | 17037 |
| D16 | sub034 | e000c19ba87802b34c79b4873a28864dffd1abc4b43ffd3f2d9dfe0bf9abbae8 | 22840 |

Source files are `docs/pcau_heavy_vehicle_reform_subNNN_heavy_vehicle_reform.txt`.

## D01 - ARTC, "Impact of Heavy Vehicle Reform" (letter submission)

- Source: sub003 | text L1-241 | no page markers.
- Written or submitted by: Australian Rail Track Corporation (ARTC), Level 15, 180 Ann Street, Brisbane
  (L3-6). Signed Jade Hooper, Group Executive Development (L235-238); contact Susan Furze, General
  Manager - Policy and Regulation (L233). Mentioned only: ONRSR (fn2 L161), NHVR (L135).
- Type, date: letter dated 12 December 2025 (L7).
- Period covered: collision data "ARTC 2021 - 2025" (fn1 L159). No fiscal convention.
- Structure: summary table "Reform Activity | ARTC Position" L33-53 (5 rows: road access; NAAS; NHVDCF;
  HZEV curfews; HZEV charging). "Responses to specific reforms" numbered 1-5 at L87, L127, L139, L163,
  L179. Cross-cutting considerations L196-221 (safety and congestion L197; pricing and competitive
  neutrality L206; evaluation and governance L218); conclusion L222-231. No numbered recommendations.
- Figures: L146 "On the ARTC network, heavy vehicles account for 30% of collisions and near hits at
  level crossings1, despite heavy vehicles making up only 2% of all vehicles on Australian roads.2";
  fn1 L159 "Data from ARTC 2021 - 2025."; fn2 L161 "Opinion: Crossing to the Same Side | ONRSR".
- Lists: ARTC network corridors L66-70 (3); interfaces L74-78 (3); safeguards L99-103 (3); NAAS
  governance sub-items L135 (3); curfew design requirements L167-171 (3); "sensible approach" L174-178
  (3, last: retain ability to reverse curfew changes); charging planning L189-195 (4).
- Positions/rules: L115 target higher masses to defined freight routes "rather than system-wide
  relaxation of limits"; L121/L184 HZEV/HPV access and charging hubs prioritised to intermodal
  terminals; L101 rail "already pays higher access charges"; L214 "PAYGO-based road funding".
- Hedged claims: L50 curfew reforms "can enable more off-peak movements ... but only where night-time
  safety, community amenity and interactions with rail are properly managed"; L164 "easing curfews could
  enable more off-peak operations"; L171 "increased night-time truck movements may heighten level-crossing
  risk, extend closure times and affect passenger rail reliability" (hedge on the rail consequence);
  L172 "A sensible approach may involve" (hedge on the proposal). Firm: L99 "higher masses and wider
  access will increase pavement and bridge wear"; L107 rail share "remains the lowest-cost
  decarbonisation option" (scoped "On many long-haul, high-volume tasks").
- Coverage: full; L1-241 read sequentially.

## D02 - NHVR, "Impacts of heavy vehicle reform" (cover letter + 25-page enclosure)

- Source: sub004 | text L1-671 | running header "NHVR submission | Consequences of remaining
  inefficiencies in our road freight system" with "N of 25" (p3 L29 ... p25 L642).
- Written or submitted by: National Heavy Vehicle Regulator (NHVR). Cover letter dated 15 December 2025
  (L3), ref "CCF/2115 DOC25/39417" (L4), signed Kelli Walker, A/ Chief of Safety and Productivity
  (L20-21); contact Brayden Soo, Manager, Freight and Supply Chains (L17). Enclosure "NHVR Response -
  Impacts of Heavy Vehicle Reform - 15 December 2025" (L22).
- Self-description: HQ Brisbane; >1,000 staff across ACT, NSW, Qld, SA, Tas, Vic (L33); established 2013;
  HVNL "applies in all Australia's states and territories except the Northern Territory and Western
  Australia" (L35). Stakeholder profile L50-56: 277,778 registered operators; 556,000+ people in road
  freight (5.3% of total employment); 6 participating jurisdictions; 468 road managers in participating
  jurisdictions. Fleet L59-69: 1,086,135 registered heavy vehicle units "(this list is not
  exhaustive)": 122,628 prime movers; 188,273 semi-trailers; 179,398 freight-carrying trucks; 119,187
  agricultural vehicles and tractors; 39,938 buses.
- Structure: L13 "focuses on Information request 1 - 3 ... with some commentary for Information request
  4 and 5, which are primarily the remit of jurisdictions and local government". Contents L73-76.
  IR1 road access L80-342 (pp5-13); IR2 NAAS L346-419 (pp14-16); IR3 NHVDCF L423-538 (pp17-21, incl.
  pilots/escorts L521-538); IR4 EV truck charging L542-603 (pp22-23; L543 NHVR "has no role in planning,
  funding or delivering charging infrastructure"); IR5 curfews L607-668 (pp24-25; L655-656 curfew
  implementation "falls outside the NHVR's remit ... the NHVR does not propose to respond directly to
  this aspect"). No numbered recommendations. Last list in document: ATAP items L664-668 (air
  pollution; noise pollution; additional costs in urban areas (barrier effects)).
- Tables:
  - Table 1 L167-178 "Comparison of average distance travelled over 5 years"; columns ABS Survey of
    Motor Vehicle Use (2020) | NHVR National Roadworthiness Survey (2024). Average annual distance (km):
    Rigid trucks 21,100 | 43,471; Articulated trucks 78,300 | 102,491; Buses 24,600 | 50,759. Relative
    Standard Error: 3.08% | 1.52%; 1.83% | 1.49%; 4.80% | 1.99%. Note L179 change "likely the result of
    a combination of sampling from both surveys, as well as increasing productivity". Prose L306: SMVU
    "last collected over 5 years ago"; NHVR data preferred.
  - Table 2 L247-289 "Summary of key issues of higher productivity vehicles and road use charges"
    (Factor | Effect | Charging Implication). Layout flattened; cells run together and split across the
    p10/p11 break (L279-285). Factor rows: longer vehicles with more trailers; fewer hauling units;
    increased trailer use; longer vehicles travel more kilometres; structural change within vehicle
    classes only; growth in PBS share ("over 20% Compound Annual Growth Rate" L275); use concentrated on
    high-productivity networks; PAYGO model is backward-looking (L287, last).
  - Table 3 L389-396 "Access permit statistics over time": Year | Industry applications | NHVR cases |
    Road manager consent requests. FY2021 69,891 | 117,886 | 195,444; FY2022 77,141 | 143,951 | 233,843;
    FY2023 81,444 | 151,380 | 249,240; FY2024 86,532 | 172,862 | 286,170; FY2025 94,088 | 196,629 |
    318,027. Rounded prose beside it: L380 "over 90,000 access permit applications submitted by industry
    every year"; fee "recovers about one-third of the administrative cost" (fn2 L401 NHVR Cost Recovery
    Study Project); per application industry ">$220", road managers ">$450" (fn3 L402: 2 hours per HVNL
    RIS 2011, ABS AWOTE, $88 permit fee); ">$180 million" over past three financial years (fn4 L403).
  - Figures with no data in text: Fig 1 L117 (Freight PASS screenshots); Fig 2 L336 "Average payload
    productivity for articulated vehicles (2014-2020)" (fn1 L340 ABS (2020) SMVU) with orphan labels
    "+4.4% +6% +16% +0.5%" L342 not attributed to jurisdictions; Fig 3 L339 "Comparison of PBS Level 2B
    networks and access permit applications across jurisdictions" (no values); Fig 4 L409 market share by
    fleet size June 2025 (fn6 L419 NEVDIS); Fig 5 L468-473 licence holders, heavy vs multi combination,
    axis 2013-2037 only (fn9 L469 BITRE (2024) Yearbook).
- Rules, limits and exceptions:
  - L83 as-of-right mass uplift "from General Mass Limits (GML) to Concessional Mass Limits (CML)" and
    as-of-right length "from 19m to 20m that will be delivered by the Heavy Vehicle National Law (HVNL)
    Amendment Act 2025"; "Network access remains a discretionary decision for road managers".
  - L88 ADR 80/04 (Euro VI) vehicles "up to 0.5t heavier"; "The increased mass limits commenced on 1
    November 2024." Exception L91: "mass concessions afforded to the prescriptive fleet do not apply to
    existing PBS approvals"; adding a Euro VI prime mover needs a new Design Approval (PBS assessor), new
    Vehicle Approval (PBS certifier), new access permit (L93-97). L98 "one jurisdiction will accept no
    more than 10 variants per application" (a 100-combination permit becomes 10 applications).
  - L109 "While axle mass limits remain unchanged" (PBS). L318 HVNL prohibits NHVR sharing TCA
    telematics data. L357 "NAAS will not provide 'automatic' access". L385 access notices "remove the
    need for individual permits". L431/L444 licensing is jurisdictional (DLAs). L529 NHVR OSOM data
    "excludes OSOM moves covered by existing access notices (i.e. permitless travel)". L653 exhaust
    braking systems "lack regulated noise limits". L656 NHVR "does not set, administer or oversee"
    curfews.
  - ADR alternative compliance L295-299: EV - ADR 109/01, UNECE R100, GTR No. 20, FMVSS No. 305;
    hydrogen - ADR 110/00, UNECE R134, GTR 13.
- Other figures (with cited sources): L106 Austroads NEF6392 modelled 2,475 pavement sections (Vic and
  Qld state networks); L113 Freight PASS public "from January 2026", >11 million configurations;
  L124-126 measures per 100t payload; L218 registration data since 2018; L275/L467 PBS growth "over 20%"
  (CAGR / "per year"); L397 largest 10 companies 2.4% market share; 93% of operators <5 hauling units
  with 54% market share; L407 ">$700 million" annually from one hour/week for operators with fewer than
  five hauling units (fn5 L418 ABS AWOTE 2024); L425 average driver age 48 (fn7 L445 BITRE (2023)); "only
  53% of truck driving vacancies are being filled" (fn8 L447 Jobs and Skills Australia (2025)); L481
  "estimated 26,000 driver positions currently unfilled" (fn10 L495 NatRoad (2024)); ~40% of businesses
  carry excess stock (fn11 L497 ABS (2022)); fn12 L498 National Truck Insurance (2024); L483/L514 4,800
  (~4,800) fewer drivers if all conventional B-doubles replaced by PBS (fn13 L500); L490-491 26,000 x
  "$184,000" GVA per driver (fn14 L501 Freight Australia (2022) dashboard, JSA (2024) ANZSCO 7331) ->
  "nearly $4.8 billion"; L493 shortfall "projected to rise to 78,000 by 2029" (fn16 L504 International
  Road Transport Union (2024) Global Truck Driver Shortage Report) -> "$14.4 billion"; "additional 12%"
  -> "just under $40 billion" (fn17 L506); L529 OSOM permit applications FY23 -> FY25: >3.5 m width
  28,368 -> 32,291 (+14%); >25 m length 27,156 -> 31,252 (+15%); both 23,369 -> 27,177 (+16%); L531 50%
  of applications become contracted moves, idle OSOM cost $5,000-$6,000/day, 10% delayed; L535 "$5.8
  million and $9.7 million" per day (fn18 L538).
- MAN noise test (cited by NHVR; NHVR "has not yet conducted its own noise testing", L611): test track in
  Munich, 20 km/h drive-past; EV "approximately 6 dB lower" (L614); diesel "as loud as four electric
  heavy vehicles combined" (L616); MAN's diesel "approximately 5 dB quieter" than literature average
  (L620); difference vs literature diesel "increased to 11 dB" -> EV "approximately half as loud" (L622);
  accelerating drive-past "12-dB reduction" (L626); EV 49 dB(A)/m vs passenger car 48 dB(A)/m, "only 1 dB
  louder" (L630); L643 "11-12 dB reduction". L634 trials: Urban Freight Trials London; Paris Silent
  Night Deliveries; Sweden updated Traffic Ordinance (municipalities may allow electric and hydrogen
  heavy trucks at night in noise-sensitive areas).
- Lists: infrastructure barriers L136-142 (4); PBS fleet-structure bullets L208-212 (3); NAAS scaling
  factors L368-372 (3); implementation bodies L442-464 (6: State/Territory DLAs; Austroads; RTOs and the
  training sector; NHVR; Australian Government (DITRDCSA); Industry and employers); IR4 regulatory
  barriers L546-556 (4), practical barriers L559-568 (5), policy issues L572-581 (4).
- Dates/forecasts: L15 supplementary insights "in early 2026"; L113 January 2026; L88 1 Nov 2024;
  L320 BITRE actuals "have fallen between the Reference Scenario and High Scenario" (NHVR considers BITRE
  "consistently conservative").
- Hedged claims: L179 "likely the result of"; L184 "is likely to exceed the shortfall identified in
  DITRDCSA's modelling"; L218 "It is likely that the number of trailers ... will continue to increase
  more than the number of hauling units" (forecast hedged; the registration-data finding is stated
  firmly); L224 "we are likely to see"; L237 "PBS is unlikely to dramatically reduce the number of vehicle
  types"; L130 "It may be worthwhile considering the broader applicability of Queensland pavement wear
  cost rates"; L161 DITRDCSA analysis "unlikely to have been updated"; L372 "In some cases, automated
  decisions may be more conservative than manual ones"; L398 small operators "may experience
  disproportionate exposure"; L407 "could unlock"; L529 "movements likely to trigger pilot or escort
  requirements"; IR4 barriers L546-556 "may slow", "could create", "could hamper", "may cause delays".
  Firm: L98 "can result in 10 (rather than one) access applications"; L104 "LZEVs will be heavier and
  will impose higher pavement wear".
- Coverage: full; L1-671 read sequentially.

## D03 - New Energy Transport (NET) submission

- Source: sub006 | text L1-175 | no page numbers; letterhead "L20 135 King St / Sydney NSW 2000" repeats
  at L3, L24, L50, L82, L120, L154 (6 pages).
- Written or submitted by: New Energy Transport (NET) / New Energy Transport Pty Ltd (L7, L170); primary
  contact Fredrik Pehrsson (L171). Date "December 2025" (L9).
- Self-description: Australian startup; "will begin operations on regional corridors between Newcastle and
  Canberra (NSW) from an initial depot near Wilton NSW" (L31, future tense).
- Structure: 1 Executive summary - 6 numbered asks L12-26 (1 fast-track strategic charging sites; 2
  co-location of charging, BESS and renewables; 3 interagency planning collaboration; 4 planning
  definition and LEP consistency; 5 curfew reform for HZEVs with safeguards; 6 transitional incentives
  and transparency, after the page break at L26). 2 Introduction L30; 3 evidence from demonstrations
  L38-52 (8 bullets); 4 support for reforms: 4.1 road access L55, 4.2 NAAS L63, 4.3 NHVDCF L72, 4.4
  charging L78; 5 curfew reform L107; 6 additional policy interventions L122; 7 economic impacts
  "(directional)" L134 (no figures); 8 requests L156-168 (7 bullets, last = transitional incentives
  L168); 9 contact L169.
- Figures: electric trucks "between three and five times more energy efficient than diesel trucks (when
  comparing the calorific content of diesel and electricity)" L33; "by a factor of three to five" L48.
  L125 "Germany's toll exemption for ZEV trucks (extended to 2031)" (no source).
- Positions: L56 supports expanded access (higher axle mass limits etc.) "where asset integrity can be
  maintained"; L19/L89-94 amend "highway service centres" to include "Facilities for servicing and
  charging electric vehicles", non-public fleet depots, on-site renewables/storage; L15/L101-104
  bidirectional ancillary use; L22/L108-118 curfew exemptions with safeguards (localised conditions;
  monitoring; NAAS rulesets); L26/L130 DNSPs/TransGrid hosting capacity maps.
- Hedged claims: L47 "Potential road safety benefits: Better grade performance could reduce risky
  overtaking from following vehicles, potentially yielding improved road safety outcomes" (hedged);
  L59 "Enhance road safety: Better grade performance by EVs reduces risky passing manoeuvres by other
  motorists" (same claim, unhedged). L152 tax-base effects "can offset transitional support".
- Notes: ligature artefacts (ffi/ff rendered as "Ư": "eƯicient", "oƯ-peak", "buƯer") at L15, L22, L33,
  L48, L104, L111, L116, L127, L138, L140, L152; readable.
- Coverage: full; L1-175.

## D04 - Team Global Express (TGE) submission

- Source: sub008 | text L1-404 | no page numbers; "OFFICIAL" markers at L9, L44, L72, L110, L143, L174,
  L201, L232, L262, L296, L330, L358, L382.
- Written or submitted by: Team Global Express (TGE), Level 3, 417 St Kilda Road, Melbourne; entity line
  "IPEC Pty Ltd ABN 15 084 157 666" (L3-7). Dated 16 December 2025 (L10). No signatory.
- Structure: 1 Introduction L11; 2 Background L14 (8 sectors L19-33; "our analysis indicates" bullets
  L38-46); 3 Increasing heavy vehicle road access and LCLFs L49; 4 NAAS L111; 5 Driver Competency
  Framework L158; 6 HZEV charging L238; 7 Curfews for HZEVs L353 (answers "information request 5", L366);
  8 Conclusions L396. No numbered recommendations.
- Lists: data/evidence list L68-104 (18 bullets: GML increases; network expansions; bridge classes;
  template approvals; pavement strengthening; bridge strengthening/retrofitting; industrial precinct
  access maps; local road exemptions; payload uplift and fleet mix shift; trip reductions and backhaul;
  emissions; critical assets; geometric design; rest areas and staging; charging sites; phasing;
  mass-distance-location charges; ADRs - last L104). NAAS items L129-153 (12). NAAS Council L129
  "chaired by the Commonwealth with entities such as the NHVR, HVNL, FIRP, HVIA, ATA and all
  state/territory road authorities". Driver framework hurdles L171-185 (8); roles L189-197 (7:
  Commonwealth (DITRDCSA); Austroads or similar; state/territory transport departments and licensing
  authorities; NHVR (where relevant); RTOs and assessors; industry; insurers and auditors); timeframes
  L202-206 (0-3, 3-6, 6-12, 12-18 months); licence classes LR/MR/HR/HC/MC L209; practical
  recommendations L227-236 (6); 12-18 month charging recommendations L344-352 (6); curfew implementation
  L380-394 (9, last = phasing L394).
- Figures/specifications: L68 model "+5% and +10% increases to axle group limits" (6x2 rigids, B-double,
  PBS A-doubles, B-triples); L203 pilots "in 3 or 4 jurisdictions (or one per state)"; L257 1-5 MW
  connections (future 10-20 MW); L275 30-40 m bays, 5 m clearance; L277 transformer lead times "can
  exceed 12 and sometimes 24 months"; L279 1-5 MWh BESS; L281 20-60 minute sessions; L282 6-12
  dispensers; L294 and L347 uptime 97-99%; L300 anchor sites 100-150 km; L345 co-fund 30-50 anchor sites,
  minimum 3-6 MW; L356 after-hours deliveries "between 5pm and 9pm"; L368 HZEV vs ICE "3-5 dB(A)
  reduction" at 0-30 km/h ("A pragmatic planning assumption shown with several OEMs"); L370 at 30-60 and
  >=60 km/h "~0-2 dB(A)"; L380 zones "between 22:00-06:00", speed <=40-50 km/h near receptors, no engine
  braking. L251 "one of the largest fleet of electric trucks anywhere in the world" (no number).
- Rules/positions: L50 extra weight "specifically over the steer axle"; L64/L108 LCLFs (renewable diesel)
  "would immediately reduce emissions whilst allowing for little if any changes to weights or road access
  networks"; L118 Tasmanian HVAMS model; L133 residual local variations (temporary works, emergencies);
  L383 councils retain local traffic powers.
- Hedged claims: L38 reforms "could contribute to GDP growth over the medium term, with the
  freight-intensive states seeing the greatest gains"; L42 "will also likely have positive benefits ...
  It is likely that employment will expand"; L46 "Net positive fiscal impacts will accrue" (unhedged);
  L60 "Road wear will increase ... but this could be managed" (wear firm, management hedged); L151 "may
  also lead to compliance risk"; L157 "would likely lead to a lowering of community complaints"; L281
  "likely to need"; L298 "will be likely to underperform"; L302 "likely to stress local networks"; L306
  "Early-phase utilisation is likely to be low"; L372 "benefits are likely to be proportional"; L374
  "are likely"; L376 "likely to reduce complaint propensity"; L378 "may still require barriers".
- Notes: typos "HVEVs" L88, "ZHEVs" L251/L370-378.
- Coverage: full; L1-404.

## D05 - Australian Logistics Council (ALC) submission

- Source: sub010 | text L1-165 | header "Impacts of Heavy Vehicle Reform , ALC, December 2025 N", pp1-7
  (L3, L20, L42, L70, L96, L118, L149).
- Written or submitted by: Australian Logistics Council (ALC) (L14). Dated "Friday,19 th December 2025"
  (L6). No signatory.
- Structure: TOC L7-13; Introduction L13-18; 1 road access and productivity L21; 2 NAAS L43; 3 driver
  competency and workforce L61; 4 HZEV infrastructure L77 (4.1 L80; 4.2 tariffs L88; 4.3 curfews L100;
  4.4 L104; 4.5 L107); 5 Strategic Implications & Policy Recommendations L120 - 9 numbered
  recommendations: 1 national multimodal freight charging framework L123; 2 electricity tariff reform
  L125; 3 regulatory reform for curfews, access, network interfaces L129; 4 data/digital L135; 5
  workforce and training L139; 6 multimodal coordination L142; 7 bridge and local road assessment L146;
  8 skilled drivers via Migration Program L150 (p7); 9 appropriate funding for NAAS L153 (p7, last);
  Conclusion L156.
- Rules and conditions: L24 HML regime - "operators must comply with National Heavy Vehicle
  Accreditation Scheme (NHVAS) Mass Management accreditation, use certified road-friendly suspension1,
  and operate only on gazetted routes2. However, many local roads remain undeclared for HML, forcing
  operators to pursue individual permits." L26 HPFVs under PBS (IAP, ABS, NHVAS). L27 Victoria PBS Class
  2 A-double: "integrated OBM (On-Board Mass) with IAP, anti-lock braking on all axles, road-friendly
  suspension, and NHVAS accreditation" (4 criteria); L28 failure -> conditional access or restricted mass
  limits. fn1 L37 VicRoads URL "victorias-hpfv-networks-for-855-tonneadoubles-master-jan-2019"; fn2 L38
  NHVR higher-mass-limits page.
- Figures with sources: L47 "By the end of October 2024, SLGAAP Phase 2 had completed 698 bridge and
  culvert assessments" (fn5 L64); L52 NAAS "in a 'proof of concept' stage8, and its introduction has been
  delayed" (fn8 L67 infrastructure.gov.au May 2025 NAAS statement); L73 "In 2024, around 28,000 truck
  driver positions remained unfilled, and 21% of current drivers are expected to retire by 2029.11" (fn11
  L92 IRU "widening-age-chasm" report URL) and "The World Road Transport Report also suggests that 47% of
  truck drivers can be characterised as being an 'older driver'"; L90 demand tariffs "amortised over a
  small number of users" (fn14 L113 Evie Networks submission to AER, NSW 2024-29 determination, May
  2023); L96 ACAPMAg (fn15), Energeia modelling for Queensland's network operator (fn16); L101 tonal
  reversing alarms (fn17 L116 EPA Victoria publication 1890).
- Tools named: Freight PASS (fn3 L39), Pavement Impact Comparison Calculator (fn4 L40), Vehicle
  Comparison Tool for Bridges L48, "Access Essentials" modules L49, HVAMS and "Victoria's HV-SAPS", NHVR
  Go L51.
- Rail-interface wording: L35, L56-57, L133, L137 (level crossings, terminal precincts, parallel road-rail
  alignments, rail access practice); compare D01 L117, L129-137, L204.
- Hedged claims: L45 NAAS "has the potential to be a strategic enabler"; L52 "there is a risk of
  duplicate processes"; L57 "could be incorporated"; L73 "expected to retire" / "also suggests"; L83
  structures "may not be rated for HZEV mass"; L90 "may draw large loads"; L105 "smaller operators may
  struggle"; L119 "Operators may also benefit from government-supported payload incentives".
- Coverage: full; L1-165.

## D06 - Crane Industry Council of Australia (CICA) submission

- Source: sub012 | text L1-349 | bare page numerals 1-22 (e.g. "10" L149, "11" L152, "22" L339).
- Written or submitted by: Crane Industry Council of Australia (CICA) (L7). Dated 5 December 2025 (L4);
  addressed to Commissioners Martin Stokie and Barry Sterland (L5). No signatory.
- Structure: Introduction L11; Issues with the Current System L24 (ROVER L27; NAAS L32; productivity
  drain L37); supports-reforms list L44-52 (5); L54 "addresses the key questions raised in the
  consultation paper". 1 ROVER and ADR compliance L56 (exhaust case study L95-123; "CICA recommends"
  L125-145: mutual recognition of Regulation (EU) 2018/858 and 2007/46/EC L127; classify cranes under EU
  N3G not NC L129; alignment with global benchmarks L133; release the ADR Harmonisation Review findings
  L144). Table 1 L150 (p10) and Figure 1 L153 (p11) - no extracted text. 2 NAAS L156 (Case Study 2
  L216-242; "CICA recommends" L244-253: HVAMS-based national system "rather than the HVSAPS model";
  collaboration; strengthened governance/whole-of-program Sponsor). 3 NHVDCF L256 (recommends L265-266).
  4 ZEV barriers L270 (recommends L299-311: funding research; increase axle limits; special dispensations
  for hybrid cranes). 5 timeframes L313-337: Immediate (0-2 years) 5 items L318-326; Medium (2-5 years) 4
  items L329-335; Long term (5-10 years) 1 item L337 (last). Conclusion L340.
- Rules/limits: L29/L129 ROVER imposes "NC Heavy Goods Vehicle classification"; L33 cranes treated as
  "oversized freight" not "essential plant"; L77 cranes are Special Purpose Vehicles; L78 ROVER (Department
  of Infrastructure portal, Road Vehicle Standards Act): Vehicle Type Approval or Concessional RAV Entry;
  L80 RAV entry prerequisite, NHVR exemptions; L96 "ADR 42 clause 24 specifies that the direction of
  exhaust discharge must not be to the left of the vehicle"; L98-99 EN 13000, UNECE 51; L112 ADR 83;
  L160 permits "up to 28 days turnaround"; L170 crane axle loads exceed prescriptive standards, more so
  for hybrid/electric; L176 first/last km restricted by local governments or "third parties (rail
  owners)"; L282 cranes classed oversize/overmass; local movement windows "typically early mornings or
  late evenings"; L284 curfews "do not differentiate between diesel and zeroemission vehicles"; L304
  proposed "nationwide harmonisation of a 12-tonne per axle limit"; L309 hybrid cranes "an additional
  2-3 tonnes (5%) on five-axle units to account for battery weight" and "a tolerance of up to 1 tonne
  (only 8%) for each axle limit".
- Figures: L17 Queensland Government "$116.8 billion, 4-year capital program" incl. 2032 Olympics (fn1
  L18 Queensland Treasury (2025) Budget Paper 3, 2025-26); other projects WestConnex (NSW), Melbourne
  Metro Rail (Vic), Torrens to Darlington (SA), Citylink/Metronet (WA) L17; L87 "35% of the all-terrain
  and hydraulic truck mobile cranes imported into Australia each year were from the used crane sector";
  L101 exhaust outlet "almost 3 meters high"; L110 "idling averages 80% of the crane's usage"; L118 UK,
  Thailand, Hong Kong data: no exhaust-fume incidents; L121 test across three models "over AUD$250, 000";
  L123 "Australia is the only country requiring this type of exhaust test"; L145 ADR review commissioned
  late 2024 by the Department (DITRDCA), "completed by Dr Warren Mundy June 2025", findings unreleased;
  L196 HVAMS proven in Tasmania (fn2 L198 Tasmanian Department of State Growth 2022 HVAMS CBA for Special
  Purpose Vehicles, 16 November; fn3 L199 HVAMS Approach and Attributes); L206 HVSAPS "being rolled out in
  Victoria and proposed for New South Wales and South Australia"; Case Study 2 (2025, NSW): bridge
  assessments "approximately $5,000", "sevenyear access issue", "more than 50 emails" (L225, L237);
  council has not updated "NSW Special Purpose Vehicle maps" (L229).
- Visual/extraction problems: Table 1 (ADR list aligned with EU 2018/858) and Figure 1 (EU certificate)
  are image-only (L150, L153). L101 cites "(Figure 2)" for the exhaust photo captioned "Figure 1" at
  L102; L141 calls the EU certificate "Figure 1" too. Case Study 2 place names are blank in the source
  (L216 "Access to", L219 "sought access ,", L225 "issue to .").
- Hedged claims: L206 HVSAPS "may offer faster processing times"; L211 "may become even more complex";
  L114 "could result in ... potential to result in catastrophic failure"; L297 "could reduce emissions";
  L311 network impact "would be negligible" (premised on "very small volume of hybrid cranes").
- Coverage: full text L1-349; image-only Table 1/Figure 1 content unresolved.

## D07 - Australian Industry Group (Ai Group) submission

- Source: sub015 | text L1-198 | header "Australian Industry Group Submission on Impacts of Heavy Vehicle
  Reform N" pp2-10 (L7, L32, L58, L77, L95, L110, L130, L151, L173).
- Written or submitted by: The Australian Industry Group ("more than 60,000 businesses", L174);
  signatories Louise McGrath, Head of Industry Development and Policy, and Aleks Mitreski, Senior
  Advisor (L190-192). Date "December 2025" (L5).
- Structure: Executive summary L8; 7 key recommendations L15-27, each repeated in the body as
  "Recommendation :" at L60 (NAAS data), L70 (council funding), L93-95 (NHVDCF/overseas drivers), L110
  (charging), L119 (green premium), L140 (curfew performance standard), L165 (council-led pilots, last).
  Sections: NAAS L32; funding certainty for local government L62; NHVDCF L77; EV charging L97; SME green
  premium L112; curfews L121; Conclusion L167; About L173. "all five focus areas" L11, L168.
- List difference: pilots list L157-163 has 4 items (acoustic measurement methods; community engagement
  approaches; night-time safety and visibility requirements; operational efficiency impacts); the
  Recommendation L165 and key recommendation L27 name 3 (acoustic measurement, community engagement,
  operational impacts).
- Figures and cited sources: L9 "BITRE freight projections indicate that road freight will grow 77%
  between 2020 and 2050" (fn1 L30 BITRE rr154 summary report); restated L33 as "projected growth in the
  national freight task of 77% between 2020 and 2050" (road freight vs national freight task); L35
  Adelaide-Sydney movement "over 16 weeks of approvals"; L37 approvals "often exceeding the claimed 30
  days timeframe and sometimes stretching beyond three months" and operation "under standard mass limits
  (CML/GML) instead of higher mass limits (HML)" (Truckvolt, fn2 L56); L49 NAAS "will be based on the
  Tasmanian Heavy Vehicle Access Management System (HVAMS)", agreed by all jurisdictions; L60 NTC (2018)
  uncertainty "single biggest barrier" to PBS take-up (fn3 L72); L63 "Local governments manage around 80%
  of Australia's road network by length" (fn4 L74 Office of Road Safety, Local Government Network Risk
  Assessment Frameworks Report 2024); ALGA: poor-condition sealed roads replacement cost $19.2bn,
  unsealed $3.9bn (fn5 L75 ALGA National State of the Assets Report 2024); L83 "projections of 70,000
  vacancies by 2030", "average driver age (53 - 56)" (no source); L92 ministers decided not to require a
  full/open car licence before heavy-vehicle licensing in the NHVDCF; L99 ARENA-funded analysis "on the
  order of 165 high-capacity heavy vehicle charging hubs" (fn6 L107 ARENA/AECOM Electrifying Road Freight
  Report); L100 hub "several megawatts", "small town"; L103 Milence (Daimler Truck, Traton Group, Volvo
  Group) ~EUR500 million, "at least 1,700" charging points by 2027 (no footnote); L105 Toll "$9.02 million
  in funding in partnership with ARENA's Driving the Nation Programme to deploy 28 heavy electric
  vehicles" (fn7 L108); L114 "Approximately 98 per cent of Australian road freight businesses are ...
  SMEs", "fewer than 20 employees"; "Over 56 per cent of trucking businesses are non-employing businesses
  (owner-drivers)" (fn8 L124-126 "ABS Data quoted by NatRoad"); L118 Truckvolt permit process "$3,000+
  exercise in the simplest applications for a basic three-day run schedule" (fn9 L128); L131 "no trucks
  after 22:00" example; Fraunhofer IML testing: electric trucks "only 1 dB 'louder' than a car" (fn10
  L149 cites "MAN, 2023" press URL); L144 COVID-19 National Cabinet removed noise curfews for 24/7
  deliveries; L146 extended relaxations "reported minimal impacts"; L148-151 ALC community sentiment
  survey: "only 1 in 7 felt transport noise increased since COVID-19, and just 2% attributed any increase
  to freight trucks" (fn11 L171 ALC, Curfews and Supply Chain Operability).
- Rules/proposals: L25/L138/L140 national "quiet freight vehicle" standard -> 24/7 access to loading docks
  and certain urban freight routes "subject to appropriate land use and amenity protections"; L136 EPA vs
  council noise thresholds.
- Hedged claims: L33 "unlikely to scale"; L64 "councils may restrict access or even remove roads"; L100
  "could require connection upgrades"; L105 "additional costs may arise"; L118 "the possibility of
  introducing a road usage tax for heavy electric vehicles"; L138 "it could be granted 24/7 access"; L83
  "This age profile implies a high retirement risk".
- Notes: spacing artefacts ("recentl y", "le vel", "operatio ns") throughout; readable.
- Coverage: full; L1-198.

## D08 - NSW Farmers submission

- Source: sub016 | text L1-158 | footer "NSW Farmers Submission ... - December 2025 / Page | N", pp1-7
  (L23-24, L45-46, L51-52, L91-92, L103-104, L129-130, L151-152).
- Written or submitted by: NSW Farmers (NSW Farmers Association), Level 4, 154 Pacific Highway, St
  Leonards NSW 2065 (L3-5); contact Samuel Miller, Principal Economist (L11). Date "December 2025" (L14).
- Scope: L30 "addresses two key elements": HVNL operation/streamlined access (particularly local roads)
  and funding for road upgrades. No sections on NAAS (except quoted NSW report L119), NHVDCF, charging or
  curfews.
- Structure: TOC L17; About L18-21; Executive summary L25; Recommendations 1-4 L32-49 (with rationale);
  Introduction L53-64 (same four, footnoted 1-5); road access L65; Recommendation 1 L109; Recommendation
  2 L121; funding L131; Recommendation 3 L147; Recommendation 4 L153 (alone on p7, last).
- Figures and sources: L19 >75,000 people in NSW and ACT, >$24 billion; L21 goal $30 billion by 2030; L26
  "over $24 billion annually"; L49/L142 Financial Assistance Grants "Prior to 1996 ... 1 percent of
  Commonwealth Tax revenue ... now fallen to 0.5 percent"; L144 returning to 1 percent "entails a $2.5
  billion commitments"; L66 Grain Growers report (fn6 L89, 2025): NSW road network carries "880,000
  trailer loads of grain per year, concentrated along six major routes": West Wyalong-Condobolin Road
  545,000; Goldfields Way 450,000; Newell Highway 450,000; Burley Griffin Way 400,000; Carnarvon Highway
  390,000; Federation Way 360,000 (tonnes per year, L68-79); L93 West Wyalong-Condobolin and Federation
  Way "remain ungazetted for PBS A-double vehicles"; L95 Moree Plains, Federation and Coonamble LGAs
  gazette entire networks for B-double access; Edward River and Wagga Wagga "extremely limited"; L99
  average receival site 418km from port, CSIRO TraNSIT average grain trailer trip 131km; L105 2 million
  tonnes, extra hour (85km), "$4 million / year" (fn8 L125 NSW Farmers 2024 submission to Freight Policy
  Reform Interim Directions Paper), full 418km "at least 5 times greater"; L138 Murray River: "Of the 30
  bridges spanning the river, 13 are restricted for PBS use, and between Eucha and Robinvale (300km)
  there are no PBS-gazetted bridges".
- Rules/schemes: Grain Harvest Management Scheme (GHMS) L37, L115-117; fn3 L86 policy 3701: remove GHMS
  requirement "to take the most practicable direct route they are authorised to travel to the first
  participating grain receiver"; fn7 L101 PBS defined under HVNL Chapter 1 Part 1.4; L119 Transport for
  NSW (2025) "Delivering freight policy reform in New South Wales" (fn9 L127, prepared for the Hon John
  Graham) recommends automating the National Service Level Standards for NSW road categorisation and
  delivering the Automated Access Assessment Program as part of NAAS; L132-136 quotes its recommendation
  "83. Review local government funding programs" (a, b). Policy footnotes fn1 L80-81 (1573 - 99AC), fn2
  L83-85 (2386 - 08EC-OCT), fn3 (3701 - 15EC-Feb), fn4 "See: 1573", fn5 L88 (4719 - 12EC-May).
- Visual: Figure 1 L97 NHVR map of LGA B-double access (green/yellow/grey) - image only.
- Notes: "Condoblin" L43 vs "Condobolin" L69/L93.
- Coverage: full; L1-158.

## D09 - Electric Vehicle Council (EVC) submission

- Source: sub018 | text L1-408 | no page numbers; no printed date.
- Written or submitted by: Electric Vehicle Council (EVC) (L3, L5; "more than 76 businesses" L8);
  contact Cameron Rimington, Senior Policy Officer - Heavy Vehicles (L18). Undated; internal references
  "As of 2025" (L30) and "As of November 2025" (fn13 L319). Anonymous "EVC Member" quotes at L101, L109,
  L118, L128, L147, L202, L206, L218, L246, L261, L289, L291, L295, L301, L317, L330.
- Scope/structure: L16 comments "confined ... to on-road freight vehicles above 4.5 tonnes" (fn1 L20:
  light commercial 4.5-8t; medium duty 8-17t GVM; heavy duty over 17t GVM); "Each of the five information
  requests are addressed chronologically": road access L22; NAAS L111; NHVDCF L140; charging L178;
  curfews L306; Further Reading L393-405 (16 entries; last Volvo Group Australia (2025) L405). No
  numbered recommendations ("The EVC recommends" L48, L147, L168).
- Rules/proposals: L24 most electric prime movers (and some heavy electric rigids) are 'Restricted Access
  Vehicles'. L48-56 reclassify heavy EVs as 'General Access Vehicles' provided they: are 100 percent
  battery electric; do not exceed 8-8.5 tonnes on the front steer axle (fn3 L63 staged); do not exceed
  18.5-19 tonnes on the rear (tandem drive) axle; otherwise comply with ADRs. L58 Austroads (2025) (fn4
  L65): even at 8.5 t Australia would remain more restrictive than most comparable markets (USA, UK).
  Chart L67-70 steer-axle tonnes for Australia (2025)*, EU, France, UK, USA, China - bar values not in
  text; chart note "*heavy vehicles complying with ADR 80/04 can qualify for an additional 0.5t of axle
  mass" L69. L79-83 international concessions: EU 4 tonne GCM; UK flat 2 tonne; USA 2,000 pound. L84-94 "a
  single electric prime mover in Australia today would need to comply with five separate state-based
  rules": NSW Towards Net Zero Emissions Freight Policy; VIC Low or Zero Emission Network Map; QLD Zero
  Emission Heavy Vehicle Network Map; SA Low and Zero Emission Heavy Vehicle Trial Scheme; Tasmania (no
  concession) - the fifth listed item is a no-concession entry. L101 member: "align across all states at
  8 tonnes (as per QLD and also NSW trials ...)". L102 concessions often "trials" or temporary. L125 LGAs
  deny general access "even where they are compliant with state-based concession schemes". L129-137
  one-touch principle (3: single window; standardised requests; deemed approval after X days). L152
  vehicles above 4.5 tonnes cannot be driven on a standard car licence; batteries add 400-700kg. L165 UK
  750kg concession; New Zealand car-licence holders may drive EVs up to 7.5 tonnes. L168 EVC recommends
  evaluating a 6-tonne car-licence limit "for electric vehicles only". fn13 L319 "As of November 2025,
  all EVs in Australia need to make an artificial noise when travelling at low speeds, consistent with
  Australian Design Rule 113/00 on Acoustic Vehicle Alerting Systems". L311-317 curfews mainly via council
  planning permits; "Several LGAs restrict loading/unloading after 6pm".
- Figures and sources: L10 road freight "over 20% of transport emissions"; L25 "$91 in compliance costs
  for a single permit for a single electric truck per delivery address; this can easily scale to $3,000
  over a basic 3-day delivery schedule" (fn2 L46 Toll Group, Lessons Learnt Report: Milestone 2, 2025,
  p.8); L30 EVC estimate "more than 550 different road access decision-makers" (as of 2025) with 7
  categories L32-44 (NHVR; all states/territories under HVNL; WA road authorities; NT road authorities;
  LGAs; rail asset owners; electrical and utility infrastructure owners - last L44); L106 LGAs manage
  "roughly half of Australia's public roads"; L107 "Australia's 530 LGAs"; L113 NAAS to "cut trucking
  permit applications by 90%"; L114 NAAS "will not actually expand access"; L119 Queensland council
  approved 7.5 t then denied the same permit at 7.1 t; another regime took one year plus a further year
  for toll roads; L121 decisions "30 days to 3 months" (fn6 L133 Toll p.7); L187 30-40% of residential
  installs stall; L193 large depot ~15-storey apartment block or 1-5 MW; L196 some grid operators (e.g.
  SA) allow one grid connection; L203 charger hardware ~$1,200/kW (2021) -> ~$200/kW; L204 site works
  70-80% of capital cost, exceeding vehicle value by up to 150%; L219 18-36-month connection delays; L221
  NSW DNSPs' Distribution System Plan; L233 10-20% of shifts need extra charging; L237 public DC chargers
  "often deliver half the rated output"; L239 ~70c/kWh; L252 ARENA and CEFC: charging "likely to be
  underutilised in the short term"; L326 a 6-hour extension raises a 12-hour window by 50%; L331-357
  formula examples: 2.5 deliveries/h (30 drops per 12-hour shift) x $100 x 12 hours (7pm-7am) = $3,000
  per operator per day; 1.25 (15 drops) x $350 x 4 hours (6pm-10pm) = $1,750; L364 payback accelerated by
  50%, halved under 24/7; L381-389 COVID precedents (NHVR; NSW SEPP - COVID Response; QLD Planning Act
  amendments; SA Development Regulations 2008 changes; VIC Amendment VC181 - last); L389 "A survey by
  the Australian Logistics Council found majority support for the continued relaxation of curfew rules;
  indeed just 6% of respondents were even aware that curfew rules had changed" (Further Reading L399:
  ALC (2022) Curfews and Supply Chain Operability); L323 Box D: a Melbourne council rejected a heavy EV as
  "too noisy"; another "unsafe" in a school zone.
- Tables/layout: "At Home | At Depot" two-column list L181-200 flattened (column of each bullet
  ambiguous; first three read as home items); formula table L331-357 flattened but values legible.
- Hedged claims: L10 road freight "may be one of the most stubborn sectors to decarbonise"; L63 "a staged
  reform may prove more practical"; L114 "Even if fully implemented, the NAAS is unlikely to improve
  national productivity in this regard"; L145 deployments "do suggest drivers will need additional
  training"; L151 "could materially cut red tape"; L167 "Anecdotally"; "potentially lower staffing
  costs"; L223 "likely to eventuate"; L248 "may prove beneficial"; L250 "may constitute a market
  failure"; L252 "likely to be underutilised" (attributed to ARENA and CEFC); L256 "could be a workable
  solution".
- Coverage: full text L1-408; chart values (L67-70) and image L267 ("NewVolt concept design") not in text.

## D10 - Australian Livestock and Rural Transporters Association (ALRTA) submission

- Source: sub019 | text L1-973 | no page numbers, letterhead or printed date; footnotes 1-93.
- Written or submitted by: Australian Livestock and Rural Transporters Association (ALRTA) (L4); "six state
  member associations", "around 700 operators" (L5). No signatory. Undated; latest dated item cited is MLA
  news of 9 December 2025 (fn75 L625); many sources "viewed 4 December 2025". (D11 L18 lists ALRTA as an
  ATA member association.)
- Structure: Executive Summary L3-23 (7 bullets L9-21). Reform 1 access/mass/HPVs L25-174 ("Good access"
  1-3 L64-68; package (a)-(d) L127-149; fairness bullets L158-172). Reform 2 NAAS L176-344 (Recommendations
  1-6 L320-343). Reform 3 NHVDCF L345-454 ("four implementation priorities" L384; summary 1-4 L444-452).
  Reform 4 charging L456-608 (recommendations 1-4 L592-606). Reform 5 curfews L610-726 ("Five practical
  questions" 1-5 L659-709; Issues and options 5 bullets L716-724). Data and evidence L728-853 (summary 1-5
  L844-852). Summary of Recommendations L855-970: Overall 1-6 (L857-880); Reform 1 = 11-14 (L882-894);
  Reform 2 = 15-18 (L898-912); Reform 3 = 19-23 (L915-929); Reform 4 = 24-28 (L932-949); Reform 5 = 29-33
  (L952-970). Numbering skips 7-10; last item 33 "Pilot, prove, then scale" L968-970.
- Outside sources with figures (period; cited source):
  - L26 ABARES: ~70% of agriculture/fisheries/forestry output exported, $75.6 billion in 2023-24 (fn1);
    production forecast $99.5 billion in 2025-26, >$106.4 billion incl. fisheries and forestry (fn2, 2
    December 2025); ~255,500 employed, ~1.8% of workforce (fn3).
  - L29 since January 2022: 23 flood events, 429 disaster declarations across 277 LGAs, >82,000 km of roads
    closed (fn4 ALGA 2023 Rural Road Alliance release).
  - NTC HVNL C-RIS (fn5/fn15, NTC 2023, October 2023, ch. 7, Table 23): GML raised to CML, Options 4a/4b:
    road wear ~$48.7 million (4a) and $71.3 million (4b) vs productivity benefits ~$553.7 million and
    $1,107.4 million (L54-56); restated L155 as "$553.7 million to $1,107.4 million per year" vs
    "$48.7 million to $71.3 million per year (2023 dollars)"; RIS "does not calculate headline NPV/BCR
    figures" (L155); assumes no benefit where movements already run at higher mass; ~40% of NHVAS
    operators held the mass management module only (~3,500 in March 2023); CML vs HML split not extractable
    (L156, fn18).
  - L74 Austroads 2014 AP-R465-14: HPV initiative $12.6 billion real benefits by 2030 (fn6).
  - L79 NTC PBS review 2014-16 (fn7 NTC 2017): 24.8% average productivity gain; 6.2% saving in gross
    tonne-km in 2016; >440 million truck-km avoided 2014-16; at least four lives; ~$65 million maintenance.
  - L81 "reporting attributed to NHVR's Heavy Vehicle Productivity Plan 2020-2025" (fn8 NHVR 2022 submission
    to the PC ports inquiry, 19 October 2022, p.6): 2007-2019 PBS cut truck travel >1.6 billion km, fuel
    >800 million litres, CO2 >2.2 billion kg.
  - L99 "The consultation proposes increasing the general vehicle height limit from 4.3 m to 4.6 m" (fn9
    NTC C-RIS); notices already allow livestock trucks, car carriers, some cubic-freight and hay vehicles
    to 4.6 m (fn10-12); Victoria's "Height Clearance on Roads" (fn13).
  - L182 NatRoad (fn20 NatRoad 2025, Road to 2028): "NHVR access permits have more than doubled in the past
    decade, from about 78,500 permits in 2014-15 to over 172,000 in 2023-24"; 11.5 days average
    processing; "almost two million days of regulatory delay each year" (fn21); HVIA (fn22, 2023 PBS 2.0
    submission pp.7-9): HVNL requires road managers to respond to NHVR consent requests within 28 days
    "unless an extension is agreed".
  - L203 TASSIC 2021 case study (fn23-24): HVAMS gives 24/7 permit-free access for ~80% of OSOM and 95% of
    SPV activity; SPV permit applications ~700 -> ~30 per year; May 2025 ministerial statement (fn25): "95%
    reduction in permit applications for mobile cranes".
  - L219 May 2025 NAAS statement (fn26): NAAS to "replace around 90% of current access permit requests";
    early releases for PBS, OSOM and SPV in testing in Queensland and Tasmania.
  - L220-226 "the 2022 Kanofski recommendations, as summarised by NatRoad" (fn27): NAAS within three years;
    50% permit reduction within three years; 90% within five years; NatRoad urges eliminating at least 90%
    of access permits by 2028 (fn28). Restated in recommendation 1 L320 and recommendation 16 L902 ("around
    half within three years and around 90% within five").
  - L246 AS 5100.7; L248 nationally consistent live-load factor of 1.6 for assured-mass freight tasks (fn31
    NTC Review of quad-axle groups).
  - L252 councils "own and manage around 678,000 km of sealed and unsealed roads - about 77% of Australia's
    road network", collect ~3.5% of national taxation revenue (fn32 ALGA 2022 Pre-Budget Submission
    2022-23); L259-263 "ALGA's 2021 State of the Assets-backed analysis": ~8% of sealed and 14% of unsealed
    local roads in poor condition; replacement cost $17.8 billion (fn33 Ibid.).
  - L272 SLGAAP funded "$8.0 million in 2019-20 and a further $12 million in 2021-22" (fn34 DITRDCA 2023).
  - L303 NatRoad citing Deloitte 2019: access reforms could save the average consumer $452 per year (fn36).
  - L348/L363 NHVDCF "scheduled to start rolling out in 2026" (fn38/fn45 Austroads webpage updated 31 March
    2025); elements L364-368 (minimum course lengths and behind-the-wheel time; experience-based
    progression; training governance).
  - L352 JSA 2024 Occupation Shortage - Drivers report: Truck Drivers ~161,582 workers (fn40 Table 3).
  - L360 NatRoad "drawing on the 2024 Global Truck Driver Shortage Report by the International Road
    Transport Union (IRU)": in Australia 47% of drivers in 2024 were 55 or older, 5.4% under 25, ~28,000
    unfilled positions, "projected to rise to over 78,000 by 2029 as more than 50,000 drivers retire";
    "Road freight volumes are projected to grow by 77% by 2050" (fn41 Clark, W 2025, 'A ticking time
    bomb', NatRoad, 14 August 2025; fn42 Ibid.).
  - L361 NTARC Major Incident Investigation Report 2025 via AfMA (fn43-44): heavy vehicles not at fault in
    ~86% of truck-car crashes.
  - L416 Victoria's Heavy Vehicle Training Program, funded since 2016, with the Victorian Transport
    Association: nearly 400 drivers trained and placed (fn49, additional $1 million).
  - L463 Climate Change Authority 2024 Sector Pathways Review (fn51): heavy road vehicles ~22 Mt CO2-e a
    year, ~24% of transport emissions.
  - L469 "Electric Vehicle Council data, cited by the ACCC and AER": mid-2024 1,059 high-power public charging
    locations, 1,849 high-power chargers, ~90% more locations than a year earlier (fn52 ACCC December
    quarter 2024 report; fn53 AER 2025). EVC is D09's author.
  - L487 "ARENA-commissioned analysis ... would likely need on the order of hundreds of high-capacity freight
    charging hubs" - its superscript 55 points to fn55 L511, which is RACE for 2030 CRC 2021 (not an ARENA
    report); RACE for 2030 bullets L489-495.
  - L522 Viva Energy Geelong hydrogen station, 2.5 MW electrolyser, ARENA-backed (fn58 2022). L533 $1.1
    billion Cleaner Fuels Program over 10 years (fn59). L534 Cleanaway HVO100 cuts GHG 91% (fn60-61).
  - L538 2022-23 automotive diesel sales 32,109.8 ML (~32.1 billion litres) (fn62 BITRE Yearbook 2024 Table
    11.1); "A 10% substitution target therefore implies roughly 3.2 billion litres". L539 2022-23 canola 4.4
    million ha, 8.9 million t (fn64 ABS). L553 Victorian grains farms ~3.5 million ha 2021-22 (fn66);
    Argus: ~100,000 t/yr used cooking oil (fn67); 517,364 t tallow exported Jan-Nov 2024, >90% to Singapore
    or the US (fn68); ACAPMA: renewable diesel premium $1.20-$1.40 per litre wholesale (fn69, 17 Jul 2024);
    BDO 2025: imported HVO almost $5/L vs fossil diesel just under $2/L (fn70).
  - L615-617 "Controlled tests of a 40-tonne MAN eTruck ... found noise levels around 6-12 dB(A) lower than
    a diesel equivalent at typical urban speeds - perceived as 'about half as loud'" (fn72 Wirtz 2023,
    Truck Pages); hydrogen trucks comparable at low speed (fn73 Hydrogen Central 2023: KEYOU, Fraunhofer
    IML results).
  - L634-638 "A survey of 1,205 Australians for the Australian Logistics Council (ALC)": 71% supported
    permanently removing curfews preventing overnight deliveries to supermarkets/retail; 67% supported
    ports and warehouses operating at night (fn79 L645 ALC 2020 media release, 2 July 2020, Newgate
    Research).
  - L654 EPA Victoria Noise Control Guidelines 1254.2 (fn74/fn83): deliveries "inaudible inside dwellings
    outside 7 am-10 pm (9 am-10 pm Sundays and public holidays)".
  - L733 BITRE 2023 Economics of Road Maintenance RR156 (fn84-85): local roads ~39% of Australia's paved
    public road length.
  - L782 IRU 2024 "as summarised in Perdaman Global Services 2025" (fn89): >28,000 unfilled truck-driver
    positions "today", 78,000 by 2029 "if current trends persist". L783 BITRE 2019 (fn90): 28.3% of truck
    drivers aged 55 and over in 2016.
  - L803-804 AECOM 2025 Electrifying Road Freight for ARENA (fn91-93): road freight 8.6% of GDP; ~223
    billion tonne-km a year; ~80% of freight emissions, ~36 Mt CO2 a year; "the freight task could grow by
    77% by 2050"; "up to 165 potential heavy-vehicle charging hubs"; relies on discontinued ABS SMVU 2020.
- Rules/proposals: L135 link higher GML and height limits to PBS performance, braking/stability and Euro VI
  ("Euro VI vehicles otherwise risk losing payload due to higher tare weights", fn14); L686 curfew relief
  "for any vehicle (including modern diesel or renewable-diesel trucks) that meets the same low-noise
  standards"; L716 performance-based night access; L656-657 Commission to focus on how changes would be
  designed "if governments decide to proceed".
- Same-document variants: hubs "on the order of hundreds" (L487) vs "up to 165" (L804); heavy road vehicles
  ~22 Mt CO2-e (L463, CCA) vs road freight ~36 Mt CO2 (L803, AECOM); 77% by 2050 attributed to IRU via
  NatRoad (L360, fn41) and to AECOM (L803); driver figures from IRU via NatRoad (L360) and via Perdaman
  (L782).
- Hedged claims: L56 RIS "cautions that these are network-wide averages"; L156 "part of the 'reform
  dividend' may be genuine payload uplift"; "there may be greater variability in loading practices ...
  which could increase pavement wear" (hedge on the RIS's distributional risk); L280 "there is a real risk
  that NAAS will replicate existing inequalities"; L487 "would likely need"; L514 hydrogen "likely to be
  important" (CCA); L553 cost pass-through "would likely be passed through" (ACAPMA), pressures "likely to
  intensify"; L638 "communities may be willing"; L654 performance-based approach "more likely to align";
  L782 "if current trends persist"; L804 "energy generation is unlikely to be the main constraint".
- Coverage: full; L1-973.

## D11 - Australian Trucking Association (ATA) submission

- Source: sub022 | text L1-307 | "Page N of 12" (L4 ... L302); numbered paragraphs 1-60.
- Written or submitted by: Australian Trucking Association (ATA) (L5), a company limited by guarantee
  (L13). Dated 19 December 2025 (L6). No signatory. Members are listed, not co-authors: 11 industry
  associations L16-36 (Australian Furniture Removers Association; Australian Livestock and Rural
  Transporters Association; National Road Transport Association; NT Road Transport Association;
  Queensland Trucking Association; Road Freight NSW; South Australian Road Transport Association; Tasmanian
  Transport Association; Transport Women Australia Limited; Victorian Transport Association; Western Roads
  Federation - last); 7 corporate members L39-51 (Australia Post; Camlin Transport and Rural Trading; DGL;
  John West Logistics PTY LTD; K&S Corporation Limited; Mainfreight; Multiquip - last); 9 associate members
  (L52). L52 "We represent the 60,000 businesses and 200,000 people who make up the Australian trucking
  industry."
- Structure: Introduction paras 1-2; About 3-7; road access 8-16 (L58); productivity and decarbonisation 17
  (L86); vehicle standards 18-19 (L96); NAAS 20-37 (L104-170); NHVDCF 38-48 (L172-200); EV charging 49-55
  (L204-222); curfews 56-60 (L226-304). Last paragraph 60 (L281); last bullet L304. No recommendation list.
- Rules/limits: para 8 L59 "The HVNL applies in every state except Western Australia and the NT."; para 10
  L63 access decisions rest with "the 6 states and two territories, 537 local councils, utility owners and
  private land holders"; para 11 L64 "As ATA understands it, state authorities can if they choose, override
  road access decisions of local councils"; para 13 L68-74 three HVNL-review general access reforms (GML to
  CML; general access length 20 metres; height 4.3 to 4.6 metres); para 14 L76 "The first two reforms
  above were agreed and are being implemented. More needs to be done on the height increase."; para 15
  L78 GML to CML "will allow an additional 5 per cent payload on all movements, without the need for
  permits or accreditation"; para 18 L97 "ADR109/00 Electric powertrain safety and ADR110/00 Hydrogen
  fuelled vehicle safety ... harmonised with UNECE R100 and UNECE R134"; para 44 L193 split the MC class
  at 37 metres, existing holders with >6 months' experience upgraded; para 46 L197 overseas credentials
  above a car licence not recognised; para 47 L199 South Australia's MC Licence Program; SA "has ceased
  recognising overseas truck driving experience (except from New Zealand)"; para 48 L200 adopt it
  nationally as an interim measure; para 59 L251 "ADR108/00 - reversing alarms" mandated; L269 "ADR113/00
  will implement artificial sound generators at low speeds"; L273 "SURP (ADR106/00) is mandatory for NB2 and
  NC vehicles where the width is greater than 2.5m" (ATA proposes SURP on all EV heavy vehicles used for
  curfew-exempt night work).
- NAAS history quotes: para 23 L113 Review of the National Freight and Supply Chain Strategy, May 2024
  (DITRDCA): all governments committed to a NAAS "by 2026", based on Tasmanian HVAMS; para 24 L115-119
  statement on the 17 February 2025 HVNL Reform Implementation Steering Committee meeting (published 10
  April 2025): Technical Advisory Group chaired by Michael Bushby; workshop in Melbourne 13-14 February;
  para 25 L120-121 "Updated: 2 June 2025"; para 26 L122-123 statement of 5 November 2025: "On October 17,
  2025, the plan and budget for Phase 2 of the NAAS was approved by the Infrastructure and Transport Senior
  Officer's Committee"; Phase 1 releases continue in Queensland and Tasmania, hosting moving from Tasmania
  to Queensland.
- Figures (no source cited unless stated): para 20 L106 NAAS "independently assessed Benefit Cost Ratio
  (BCR) of an astounding 30:1" (repeated L148, L157); para 27 L124 "although ITMM set the target of 50%
  permit reduction in three years and 95% in five years, three years in, the activity has not delivered
  against the goal of reduced permit applications (with 196,629 in 2024-25, 172,000 in 2023/24, 151,000
  in 2022/23, and 143,000 in 2021/22)"; ADF functionality delayed; para 39 L184 "Almost ten years after
  industry first called for change following a 2016 safety incident"; para 17 L87-94 ATA's August 2025
  submission to the PC energy inquiry (voucher program; low carbon fuel standard; regtech/infrastructure/
  access), "now been endorsed as a National Competition Policy priority"; para 53 L213 California LCFS
  replaced "nearly 7.5 gigalitres (2 billion gallons)" of diesel in 2022; para 55 L222 ATA modelling: 5 per
  cent renewable diesel saves 6.9 Mt CO2-e "from 2026- 2050"; para 57 L232 "Typical ICE trucks generate
  70-90 dB under load, while EV trucks often operate at 55-65 dB".
- Lists: engagement mechanisms L136-142 (4); para 35 L157-165 (5); NHVDCF concerns L175-179 (3); LCFS design
  L216-220 (3); curfew considerations L249-255 (4); safety concerns L263-265 (2); mitigations L269-277 (5);
  quantification L283-304 (10).
- Hedged claims: para 12 L66 "perhaps determined and imposed at Ministerial level"; para 20 "has the
  potential"; para 32 L146 program "may fail to deliver"; para 56 L227 "has the potential to be able to
  mitigate"; para 59 L249 curfews "may need revision"; L263 "may increase collision risk".
- Coverage: full; L1-307.

## D12 - The Australia Institute submission

- Source: sub024 | text L1-88 | header "Heavy Vehicle PC submission N", pp1-5 (L3, L18, L36, L54, L73).
- Written or submitted by: The Australia Institute (L9). Date "December 2025" (L7). No signatory. Cites its
  own research: Campbell et al (2024) (fn2, fn8), Denniss, Quicke and Parrott (2023) (fn12-13), Denniss
  (2023) (fn14).
- Scope: two "elephants" - the Fuel Tax Credit Scheme (FTCS) (L12) and buses (L22). Sections: Introduction
  L8; fuel tax credits L23; electric buses L60; Conclusion L80. No NAAS, NHVDCF, charging or curfew
  sections; no numbered recommendations.
- Figures and sources: L24 FTCS "reduces government revenue by over $10 billion per year" (fn4 Budget
  2025-26 BP1), "costs more than either the operation of the army or the air force"; FTCS refunds excise
  "either in part (on road) or in full (offroad, particularly for mining)"; L28 Fortescue: heavy mobile
  equipment >50 per cent of some miners' scope 1 emissions (fn5); L38 Parliamentary Budget Office:
  "Australia has the 12th lowest level of fuel tax out of 44 countries for fuel used on road and is ninth
  lowest for fuel used for non-road purposes" (fn6 PBO 2022); L62 "as of late 2022, merely 0.2% of
  Australia's registered buses were electric" (fn12); L66 electric buses "up to 20 dB(A) quieter than
  diesel buses"; L75 buses "just 0.5% of Australia's registered vehicles, but account for up to 6% of key
  air pollutants and produce roughly 1.4m tonnes of CO2 equivalent pollution each year - equivalent to the
  ACT's total annual emissions" (Australia Institute (2023), fn13).
- People: PC Chair Danielle Wood (L13-14, L55; fn3 Grattan 2023; fn9 AFR 2025); Commissioner Barry
  Sterland quote L45 (fn7 Hansard, Senate Economics Legislation Committee Estimates, 10 October 2025);
  Senator Barbara Pocock L57; Climate Change Authority Chair Matt Kean calls the FTCS "insane" (fn11 Cropp
  2025). L20 FTCS "not mentioned in the call for submissions document"; L22 buses "a word that appears just
  once in the call for submissions document" (fn1 PC call for submissions).
- Hedged claims: L20 "The FTCS is possibly the biggest barrier"; L43 "there is likely to be a strong link
  between on-road and off-road heavy electric vehicles. All such vehicles are likely to share related
  battery technology"; L77 "likely to increase public transport use"; L22 buses "may be fewer in number".
- Coverage: full; L1-88.

## D13 - ARENA, "Impacts of Heavy Vehicle Reform: ARENA Response"

- Source: sub025 | text L1-265 | "Page N of 11" (L3 ... L247).
- Written or submitted by: Australian Renewable Energy Agency (ARENA) (L15); dated 19 December 2025 (L4);
  offices and ABN 35 931 927 899 (L248-262). No signatory.
- Self-description: established 1 July 2012 (L15); since 2012 >800 projects, >$3 billion grants, almost $15
  billion total investment (L20); since 2017 >$300 million for transport decarbonisation (L31); Driving the
  Nation Program focus areas as of December 2025 (3, L34-45). ARENA-supported projects L49-67 (10): Team
  Global Express, Depot of the Future Vehicle Electrification Project (TGE = D04's author); Tropic Wings;
  Patrick Terminals (Fremantle Port); Centurion; ANC; Zenobe; Wyndham City Council; Linfox; Toll Group,
  Project Truckvolt; Mondo Power, Melbourne Electrified Freight Hub (last).
- Structure: TOC L10; Executive Summary L13; five insights listed L84-88 (wording differs from headings: L85
  "Weight limits should be reconsidered" vs heading L131 "Weight limits and licencing requirements";
  L88 "revised in their application" vs heading L189 "refreshed"). Key Message 1 L90 (recommendations 1-2
  L120-124); Key Message 2 L131 (A HML: recommendations 1-3 L143-145; B licensing: one recommendation L151);
  Key Message 3 L162 (recommendations 1-2 L173-175); Key Message 4 L177-180 (recommendation L180); Key
  Message 5 L189 (recommendations 1-3 L196-200); Appendix table "Information Request | ARENA Response"
  L204-245.
- Appendix layout: each response is printed at the start of the line after its sub-question (L209 "See Key
  Insights 1-5" answers the L208 item). Read that way: IR1 (6 sub-questions): reforms to assess - KI 1-5;
  road-wear cost - N/A; infrastructure barriers - KI 2; cost apportionment - N/A; imported vehicles - N/A;
  data - N/A. IR2 (5): coordination - KI 3; eligible roads - N/A; scaling Tasmania's model - N/A; permit
  system costs/benefits - KI 2-3; data - N/A. IR3 (5): all N/A. IR4 (3): all KI 1. IR5 (4): noise levels -
  KI 4; noise effect - KI 4; implementation - N/A; quantification - N/A.
- Figures and sources: L21 transport ~23% of national emissions in the year to June 2025 (fn1 DCCEEW June
  2025 inventory update p.18); L25-26 "Road freight activity is projected to grow by approximately 35%
  between 2025 and 2040, leading to a 10% (or 2 Mt CO2-e) increase in truck emissions by 2040"; truck
  emissions rise through 2035 then flatten, marginal decline by 2040 (fn2-3 DCCEEW Australia's emissions
  projections 2025, November 2025).
- Rules/limits: L135 "Conventional steer axle High Mass Limits (HML) of 7 tonnes do not account for the
  heavier battery packs" (fn11 Change Management Report, TGE (2025), p.15); "companies like Toll have had
  to comply with ... ICE weight thresholds" (fn12 "Ibid.", i.e. the TGE report); L139 WA: "a NHVR
  weighbridge recorded a HZEV with axle weight over 7 tonne as being non-compliant, even though it had a
  HML exemption permit"; L147-148 licences based on GVM; progression "typically requires holding a
  lower-class license for 1-2 years" (fn13 AECOM 2025 p.12); L165 Queensland requires operators to apply to
  TMR for HML vehicle approvals; "operators in New South Wales and Victoria can run HZEV fleets with HML on
  the NHVR network without needing additional state permits"; WA and other states interpret
  independently; L168 NHVR exemptions for heavier axle weights on approved networks in NSW and QLD; "one
  council rejected 8t steer axles entirely" (fn14 "Lessons Learnt Report: Milestone 2, TGE (2025), p. 8");
  L177 "HZEVs are quieter and yet ICE truck curfews apply equally" (fn15 AECOM p.11; fn16 "'Electric
  Trucks: Keeping shelves stocked in a net zero world', EVC (2022), p. 5" - EVC is D09's author);
  L189-191 HZEVs not approved for dangerous goods beyond Class 2 packaged DG under the ADG Code; for
  flammable gases by tank vehicle the code "does not mandate that an electric drive train cannot be used"
  but requires AS 2809 4.4.2.3.2, so "A HZEV would therefore be out of scope" (fn17 TGE (2025) p.10); L196
  "UNECE ADR 2025" (dangerous-goods agreement) and R105.
- Other: L124 charging phased - capital-city freight precincts near ports first, then national highway
  corridors (fn9 AECOM); L116 CEFC finance to OEMs (fn6 Volvo) and hub operators (fn7 Zenobe/Woolworths);
  fn8 NSW EV Fleets Incentive Kick-start FY26.
- Hedged claims: L91-101 "we expect that over time" (vehicle costs fall; TCO parity "in many use cases");
  L134 OEM products "may align with existing limits"; L137 "battery packs may increase"; L139 "may be
  needed"/"may be required"; L180 quieter trucks "could extend their hours ... could deliver significant
  financial and efficiency benefits"; recommendations under Key Messages 2-4 open with "Consider" (L143-145,
  L151, L173-175, L180); Key Messages 1 and 5 recommendations are unhedged (L122-124, L196-200).
- Coverage: full; L1-265.

## D14 - Victorian Government submission

- Source: sub028 | text L1-402 | "OFFICIAL" markers; front matter i-ii (L30, L54); body pages 1-18 (L62 "1"
  ... L390 "18").
- Written or submitted by: Victorian Government (L8), published via the Department of Treasury and Finance
  (L11-18); body cites Department of Transport and Planning (DTP) work (L185, L209). Cover "NOVEMBER 2025:"
  (L4) but "(c) State of Victoria 2026" (L23); printer fields "XXXXXXXXXXX" (L19-20). No signatory.
- Structure: Contents L30-60; 1 Executive Summary L64 (section guide L73-81; three asks L83-88); 2 Background
  L93; 3 road access L107 (3.2 L108, 3.1 L111 - out of order in extraction, 3.3 L134, 3.4 L144, 3.5 L156,
  3.6 L166, 3.7 L168); 4 NAAS L180 (4.2 L182, 4.1 L193, 4.3 L208, 4.4 L212, 4.5 L216, 4.6 L224, 4.7 L231); 5
  NHVDCF L238 (5.2 L240, 5.1 L252, 5.3 L278, 5.4 L307, 5.5 L318, 5.6 L322); 6 charging L328 (6.2 L329, 6.3
  L335, 6.1 L340, 6.4 L355); 7 curfews L367 (7.2 L368, 7.3 L371, 7.4 L373, 7.1 L379). Each section reprints
  the Commission's sub-questions: IR1 L112-124 (6), IR2 L194-204 (5), IR3 L253-263 (5), IR4 L341-347 (3),
  IR5 L380-388 (4). No numbered recommendations.
- Figures and sources: L67 freight and logistics >=$36 billion (~6 per cent of Victorian GSP), ~240,000 FTE
  (fn1 Victorian Freight Plan 2025-30; URL reads "2025-29"); logistics TFP +1 per cent -> +$2 billion GDP
  nationally (fn2 Moving More with Less 2021); L96 HPFV network >40 per cent of arterial roads; "In 2015,
  there were 17 HPFVs operating on Victorian roads. By 2025, this number had increased to more than 5,200";
  L109 "from less than 20 to more than 5,200" over the past decade, "without additional Commonwealth
  funding" (Chart 1 L111, no values in text); L98 net zero by 2045; transport and logistics 25 per cent of
  emissions; road freight ~a third of transport emissions, ~8 per cent of Victoria's total (fn3); L128 late
  1990s B-double access on >90 per cent of arterial roads; L153 ~3000 bridges and ~6000 road carrying
  structures, many pre-1950; L185 since 2021 "a 400 per cent increase in Class 1 and Class 2 permit
  applications requiring a bridge assessment"; L187 >70 maps on NHVR National Network Maps; L213 HVSAPS can
  assess 6,000 structures for Class 1 and Class 2; 20 minutes to an hour each; L218-219 LGAs: Tasmania 29
  ("able to bring all 29 LGAs on board" for early HVAMS crane releases), Victoria 79, NSW 128, Queensland
  77; L241 heavy vehicles <4 per cent of Victorian traffic, 15 per cent of road fatalities (fn7 BITRE 2025;
  fn8 TAC 2025); "Victoria's road freight task projected to grow 75 per cent by 2040" (fn9 BITRE (2022)
  road freight forecasts 2022 update, rr155) "with an increased demand for more than 21,000 additional
  drivers by 2034" (fn10 Victorian Government 2025); L272 drivers with recent licence bans have crash rates
  50-157 per cent higher (fn12 MUARC 2023); L275 Victorian courses: licence attainment 40-60 hours vs
  certificate course >400 hours; fn4 L172 PC 2024 NCP modelling p.79.
- Rules and schemes: L171 legislated Principal Freight Network; L183 NAAS written as "National Automated
  Assessment System", "introduced at the Infrastructure and Transport Ministers Meeting (ITMM) in 2022";
  Victoria funded Phases 1 and 2 (L184). HVSAPS = "Heavy Vehicle Structural Assessment Permit System" (L75,
  L140, L167, L185): rollout "in the second week of January 2026" (L185), "when launched in January 2026"
  (L189, L234); integration with NAAS "toward the end of 2026" (L209); recognised by the Commonwealth and
  ITSOC as a future NAAS module; some operators may get greater approved mass limits than manual
  assessments allow (L189). fn5 L191-192 "As per the Heavy Vehicle National Law, Class 1 vehicles are large
  mobile cranes, low loaders and platform trailers. Class 2 vehicles are larger freight combinations like
  A-Doubles and B-Triples." L217 HVAMS written as "Heavy Vehicle Assessment Management System", "now forms
  the backbone of NAAS"; Queensland TMR adopted HVAMS for oversize vehicles (due 2026); earlier HVAMS
  "vehicle matching" did not meet Victoria's needs. fn6 L220 "SLGAAP, at least in Victoria, only collects
  structural data, not geometric data." L226 "The National Heavy Vehicle Law sets a 28-day limit for a
  permit to be issued." L228 one PBS permit application "can have 500 combination variants". L136/L233
  smart OBM and regulated telematics required on HPFVs.
- NHVDCF proposal vs endorsement: L243 DRIS (fn11 Frontier Economics 2023) presented Option 1 Competency
  Refresh (L244) and Option 2 Eligibility Criteria: 2a "Requiring an open licence before a driver is
  eligible for a Medium Rigid or above licence" (L246); 2b excluding drivers with a licence suspension or
  disqualification in the past two years (L267). L269 "transport ministers provided in-principle
  endorsement of Options 1 and 2b in December 2023 based on the D-RIS" (2a not among those endorsed). L243
  "agreed-in-principle at the Infrastructure Transport Ministers' Meeting (ITTM) in December 2023". L320
  "Austroads has committed to delivering core national work packages by June 2026, with a two-year period
  for jurisdictions to adopt and implement." L324 Victorian RIS being drafted. Stages 1-3 L311-317.
- Curfews: L369 DTP "has no specific data available about the difference in noise levels"; L372 a new ADR
  requires AVAS ("Acoustic Vehicle Altering System") on new electric, hybrid and hydrogen fuel cell cars,
  trucks and buses "from November 2025" - "This may negate some of the noise reduction benefits"; L373 truck
  curfews on certain Victorian roads "generally do not affect last kilometre delivery"; council planning
  permits are the binding restriction; L375 Local Government Bulletin asks councils to allow supermarket
  deliveries "two hours before and after current restriction times" - "not a mandate"; barriers list
  starts L377 and resumes L393-397 after the IR5 box (layout split).
- Charging: L331 Victorian Acceleration of Zero Emissions Vehicle Adoption program; Commonwealth "Driving
  the Nation Fund"; National Electric Vehicle Strategy; L351 Net Zero Transport Sector Plan quote;
  L358-360 ARENA-commissioned AECOM study (fn14); L361 charging at Heavy Vehicle Rest Areas or bus depots.
- Hedged claims: L83/L85 costs "likely to be"/"likely to change"; L100 "potentially helping reduce operating
  costs"; L153 "may see the introduction of stricter load limits"; L155 "Austroads may be able to provide
  further context" (unhedged in the same paragraph: greater LZEHV uptake "will create permanent and
  compounding cost pressures"); L219 "would likely require significant additional time"; L275 providers
  "may shorten training"; L297 "Jurisdictions (especially smaller jurisdictions) may struggle"; L303 new
  pathways "may also create new compliance ... challenges such as potentially opening the door to fraud";
  L372 "may negate"; L377 barriers "may include".
- Coverage: full; L1-402; Chart 1 values absent.

## D15 - Australian Retailers Association + National Retail Association (joint submission)

- Source: sub029 | text L1-90 | no page numbers.
- Written or submitted by: jointly the Australian Retailers Association (ARA) and the National Retail
  Association (NRA), "the Associations", "amalgamating to form the Australian Retail Council (ARC)"
  (L6-8). Date "DECEMBER 2025" (L5). Contact `policy@retail.org.au` (L87). No signatory.
- Self-description L8-10: $444 billion sector; 1.4 million employees (one in ten workers); 16 percent of
  GDP; 95% of membership small/independent; >155,000 retail outlets.
- Structure: Executive Summary L13-22; Body L24; 1 road access and road user charging L28; 2 NAAS L38; 3
  NHVDCF L49; 4 ZEHV charging L57; 5 curfews L71 (L77 "support the progressive removal of curfews for
  zero-emission heavy vehicles in appropriate locations"); Conclusion L79. No numbered recommendations.
- Figures and sources: L29 "road freight performance has increased by only 5 percent since 1998, while rail
  has lifted just 8 percent" (fn1 National Freight and Supply Chain Strategy (2019) 8); L31 cost reduction
  top priority (fn2 AFGC and Argon & Co 2025); L39 "a single freight route can require approval from dozens
  of local councils"; L40 "NAAS is expected to replace around 90 percent of existing heavy vehicle access
  permit requests" (fn3 Infrastructure and Transport Ministers, "Update on NAAS" (May 2025) 1); L50 "around
  28,000 heavy-vehicle driver positions currently unfilled" (fn4 NatRoad, Global Driver Shortage Report
  2024 (2024) 1); "could increase to approximately 78,000 vacancies by 2029" (fn5 NatRoad, A Ticking Time
  Bomb (2024), citing IRU); L51 "47 percent of drivers are aged over 55, while only 5 to 6 percent are under
  25" (fn6 NatRoad, A Ticking Time Bomb (2025)); L60 "around 165 dedicated heavy-duty charging hubs" (fn7
  ARENA/AECOM 2025); L61 electricity demand "expected to outstrip current national projections" (unsourced
  "Sector analysis").
- Note: L14 calls it "the Productivity Commission's proposed Heavy Vehicle Productivity Reform Package"
  (D02 L10: package "proposed by the Treasurer").
- Hedged claims: L50 "could increase"; L61 "expected to outstrip"; L74 blanket curfews "risks limiting".
- Coverage: full; L1-90.

## D16 - Tasmanian Government (Department of State Growth) submission

- Source: sub034 | text L1-198 | "OFFICIAL"; footer "Tasmanian Government Submission: Impacts of Heavy Vehicle
  Reform N" pp1-6 (L14, L37, L58, L85, L131, L157); back page also labelled "1" (L188).
- Written or submitted by: Tasmanian Government, Department of State Growth (Tas) (L3, L6, L190-195, 4
  Salamanca Place, Hobart). Date "December 2025" (L7). No signatory.
- Structure: Contents L12; Executive Summary L16-31; IR1 L32-62; IR2 L64-80; IR3 L87-138; IR4 L140-145; IR5
  L147-178; Conclusion L179-186. No numbered recommendations.
- IR1 facts: L39 axle loading vs pavement wear "exponential, not linear"; L41 Austroads NEF6392 "Future
  freight vehicles and buses - implications for road managers ... understood to be nearing completion" and
  "expected to provide" data; L43 Austroads NEF6394, report AP-R745-52 "published in December 2025"; L49
  "With the road freight task projected to increase by 77 per cent between 2022 and 2050" (fn1 L56 DITRDCA
  Australian aggregate freight forecasts); L51 some PBS vehicles not paying registration commensurate with
  pavement wear; L60 "Through ITMM, Transport Ministers have asked the National Transport Commission to
  consult on a forward-looking cost base (FLCB) as an alternative to the current pay-as-you-go model ...
  Consultation is expected to commence in early 2026" (fn2 NTC 2025); L62 "To date, Department of State
  Growth has not received requests from the road freight industry to operate LZEVs above existing axle mass
  limits. There are some LZEV buses in operation, however these have not sought to operate with masses
  higher than existing limits." L26 LZEV uptake should shift from heavy vehicles, not rail; Transport
  Emissions Reduction and Resilience Plan 2024-29.
- IR2: L65 HVAMS "in operation and ongoing development since 2016"; L67 benefits (fn3 L83 "HoustonKemp
  Economists 2022, Cost benefit analysis of extending the Heavy Vehicle Access Management System to Special
  Purpose Vehicles", URL ...HVAMS_CBA_Final_Report_16_Nov_22.pdf); L69 "The NAAS intends to create a single,
  seamless, national access assessment system that removes the need for 90 per cent or more of heavy vehicle
  permit requests."; L73 vehicle parameters saved as a unique code; L75 NAAS accommodates each road
  manager's assessment methods; L77-78 state-local cooperation and funding were key to HVAMS.
- IR3: L89 DRIS "approved by Ministers at the ... (ITMM) in December 2023"; L98-102 two Progression
  Pathways (Driving Experience Pathway; Supervision Program Pathway) "recommended to ITMM to be implemented
  in addition to existing tenure-based licence progression pathways" (L104); March 2025 Implementation
  Group meeting created the Alternative Progression Pathways Working Group, chaired by Austroads; L106
  Tasmanian regulatory work from Q1 2026, ~18 months; challenges L110-114 (3); other bodies L118-128 (6:
  NTC; Registration and Licensing Taskforce; Austroads; ITSOC; ITMM; all other licensing jurisdictions -
  last); L134 some jurisdictions incl. Tasmania cannot commit to the Learning Management System without
  cost-recovery transparency; L138 Tasmanian implementation "anticipated for the 2027-28 period".
- IR4: L141 "There are no known regulatory barriers preventing the installation of charging
  infrastructure."; L143 "In November 2025, Tas Petroleum opened a new site at Legana including charging
  infrastructure for heavy vehicles."; L145 other issues: low demand, network capacity, installation cost.
- IR5: L148 "Department of State Growth does not currently impose any noise related travel restrictions on
  heavy vehicles. Additionally, State Growth is not aware of local government imposing such restrictions in
  Tasmania."; L163-170 Tasmanian time-of-travel restrictions (3): OSOM wider than 3.5m kept outside peaks
  on several state roads in greater Hobart, Launceston and Burnie; >30m HPFVs through Launceston (no access
  through Hobart or over the Tasman Bridge); school-bus times on narrow routes (last); L172 "These
  restrictions would not be mitigated by a change to a quieter vehicle such as a LZEV because they do not
  relate to noise."; L174 complaints about engine compression brakes; L184 Tasmania's "net-zero by 2030
  target".
- Hedged claims: L22 road user charging reform "has the potential"; L35 "likely to result in more road wear"; L39
  small increases "may result in dramatically reducing pavement life"; L41 "expected to provide"; L49 "it is
  likely that there will be more heavy vehicles movements"; L106 "anticipated to require approximately 18
  months"; L138 "anticipated for the 2027-28 period"; L145 "may delay"; L150 "may arise"; L178 "may also
  offer the potential". Firm: L33 access "certainly boosts productivity"; L141 "no known regulatory
  barriers".
- Coverage: full; L1-198.

## Shared ground (navigation only)

### (a) Access-permit counts by year, their labels, and permit-reduction targets

- D02 Table 3 L389-396 (NHVR's own data, no footnote), FY2021-FY2025. Columns "Industry applications" |
  "NHVR cases" | "Road manager consent requests": FY2021 69,891 | 117,886 | 195,444; FY2022 77,141 |
  143,951 | 233,843; FY2023 81,444 | 151,380 | 249,240; FY2024 86,532 | 172,862 | 286,170; FY2025 94,088 |
  196,629 | 318,027. Prose L380 "over 90,000 access permit applications submitted by industry every year".
- D10 L182 (NatRoad 2025, fn20): "NHVR access permits ... from about 78,500 permits in 2014-15 to over
  172,000 in 2023-24"; 11.5 days average; "almost two million days".
- D11 para 27 L124 (no source): "permit applications": "196,629 in 2024-25, 172,000 in 2023/24, 151,000 in
  2022/23, and 143,000 in 2021/22".
- Label/value relationship (location facts only): D11's four values and D10's 2023-24 value sit at the
  magnitude of D02's "NHVR cases" column (FY2025 196,629 identical; FY2024 172,862; FY2023 151,380; FY2022
  143,951), not D02's "Industry applications" column (FY2025 94,088). Year labels differ: D02 "FY2025", D11
  "2024-25", D10 "2023-24".
- Other permit counts: D02 L529 OSOM applications FY23 -> FY25 (>3.5 m wide 28,368 -> 32,291; >25 m long
  27,156 -> 31,252; both 23,369 -> 27,177); D10 L203 Tasmania SPV ~700 -> ~30 a year; D14 L185 Victorian
  Class 1 and 2 bridge-assessment permit applications +400 per cent since 2021; variants per application:
  D02 L98 one jurisdiction caps at 10 vs D14 L228 up to 500.
- Targets: D10 L220-226 Kanofski 2022 (via NatRoad): NAAS within three years, 50% reduction within three
  years, 90% within five; NatRoad: at least 90% eliminated by 2028 (restated L320, L902). D10 L219 May 2025
  ministers' statement: NAAS to replace ~90% of permit requests; L203 95% reduction for mobile cranes
  (Tasmania). D11 L124 "ITMM set the target of 50% permit reduction in three years and 95% in five years".
  D15 L40 ~90% (May 2025 ITM update). D16 L69 "90 per cent or more". D09 L113 "cut trucking permit
  applications by 90%" (no period). Five-year figure: 90% (D10, Kanofski) vs 95% (D11, ITMM); neither
  document states precedence.
- NAAS timing: D14 L183 NAAS introduced at ITMM in 2022; D11 L113 "by 2026" (May 2024 review); D05 L52
  "'proof of concept' stage ... delayed" (May 2025 statement); D10 L219 and D11 L123 Phase 1 releases in
  Queensland and Tasmania; D11 L122 Phase 2 approved 17 October 2025; D14 L184 Victoria funded Phases 1-2.
- NAAS benefit-cost ratio: only D11 (30:1, L106/L148/L157, source not named). D10 L155: the HVNL C-RIS (a
  different reform) "does not calculate headline NPV/BCR figures".

### (b) Councils, LGAs and road managers; council-managed share of roads

- Counts: D02 L56 "468 road managers in participating jurisdictions" (6 participating jurisdictions L54;
  HVNL excludes NT and WA L35); D09 L30 ">550 different road access decision-makers" (EVC estimate "As of
  2025", 7 categories incl. WA/NT authorities, rail and utility owners) and L107 "Australia's 530 LGAs"; D11
  L63 "the 6 states and two territories, 537 local councils, utility owners and private land holders"; D14
  L218-219 Tasmania 29, Victoria 79, NSW 128, Queensland 77 LGAs; D15 L39 "dozens of local councils" on one
  route; D10 L29 277 LGAs under flood disaster declarations since January 2022.
- Shares: D07 L63 "around 80% of Australia's road network by length" (fn4 Office of Road Safety 2024); D09
  L106 "roughly half of Australia's public roads" (no source); D10 L252 "around 678,000 km ... about 77% of
  Australia's road network" (fn32 ALGA 2022); D10 L733 local roads "around 39% of Australia's paved public
  road length" (BITRE 2023). The measures differ (network length, public roads, paved length).
- Related editions: ALGA local-road condition - D10 L259-263 "ALGA's 2021 State of the Assets" analysis:
  8% sealed / 14% unsealed poor, $17.8 billion; D07 L63 ALGA National State of the Assets Report 2024:
  $19.2bn sealed + $3.9bn unsealed (poor condition). Council funding: D08 L49/L142 FAGs 1% -> 0.5% of
  Commonwealth tax revenue, L144 $2.5 billion to restore; D10 L252 councils collect ~3.5% of tax revenue.
  SLGAAP: D02 L351-353; D05 L47 (Phase 2, 698 assessments by end October 2024); D10 L272 ($8.0m 2019-20,
  $12m 2021-22); D14 L214, fn6 L220.

### (c) Driver-shortage and workforce figures

| Doc/line | Figure | Source cited (year) |
| --- | --- | --- |
| D02 L425 | average driver age 48; "only 53% of truck driving vacancies are being filled" | BITRE (2023); Jobs and Skills Australia (2025) |
| D02 L481, L490 | ~26,000 driver positions unfilled (x $184,000 GVA -> "nearly $4.8 billion") | NatRoad (2024) "Truck driver shortage: Australia in the global context" |
| D02 L493 | 78,000 by 2029 (-> $14.4 billion) | IRU (2024) Global Truck Driver Shortage Report |
| D02 L483, L514 | 4,800 fewer drivers if all conventional B-doubles became PBS | NHVR estimate (fn13) |
| D05 L73 | "In 2024, around 28,000 ... unfilled"; "21% of current drivers are expected to retire by 2029"; 47% "older driver" | IRU report URL (fn11); "World Road Transport Report" |
| D07 L83 | "70,000 vacancies by 2030"; average age "53 - 56" | none |
| D10 L352 | 161,582 truck drivers employed | JSA 2024 Occupation Shortage - Drivers |
| D10 L360 | 47% aged 55 or older (2024); 5.4% under 25; ~28,000 unfilled; >78,000 by 2029; >50,000 retiring | IRU 2024 via NatRoad (Clark, 14 August 2025) |
| D10 L782 | >28,000 unfilled "today"; 78,000 by 2029 "if current trends persist" | IRU 2024 via Perdaman (2025) |
| D10 L783 | 28.3% aged 55 and over in 2016 | BITRE 2019 Information Sheet 104 |
| D14 L241 | Victoria: >21,000 additional drivers by 2034 | Victorian Government (2025) |
| D15 L50-51 | ~28,000 unfilled; ~78,000 by 2029; 47% "aged over 55"; "5 to 6 percent" under 25 | NatRoad Global Driver Shortage Report 2024; NatRoad "A Ticking Time Bomb" (2024, citing IRU) and (2025) |

- Differences: current unfilled 26,000 (D02) vs ~28,000 (D05, D10, D15); 78,000 by 2029 (D02, D10, D15) vs
  70,000 by 2030 (D07); average age 48 (D02) vs 53-56 (D07); 47% described as "older driver" (D05), "55 or
  older" (D10), "over 55" (D15); under-25 share 5.4% (D10) vs 5-6% (D15). Shortage mentioned without
  figures: D01 L46/L143, D04 L159-161, D06 L263, D09 L176.

### (d) Steer-axle, ZEV and other mass limits and concessions

- D02 L83 GML -> CML as of right and 19 m -> 20 m (HVNL Amendment Act 2025); L88 Euro VI (ADR 80/04) "up to
  0.5t heavier", increased mass limits from 1 November 2024; L91 concession does not apply to existing PBS
  approvals. D09 L69 chart note: ADR 80/04 vehicles "can qualify for an additional 0.5t of axle mass".
- D09 (proposal, national): L52-54 battery-electric General Access Vehicles <=8-8.5 t front steer axle and
  <=18.5-19 t rear tandem drive axle; L58 Austroads (2025): 8.5 t still more restrictive than USA/UK; L79-83
  EU 4 tonne GCM, UK flat 2 tonne, USA 2,000 pound concessions; L84-94 state schemes NSW, VIC, QLD, SA,
  "Tasmania (no concession)"; L101 member: "8 tonnes (as per QLD and also NSW trials ...)"; L119 Queensland
  council approved 7.5 t, refused 7.1 t (axle unstated); licence masses L152 4.5 t car-licence limit, L165
  UK 750kg, New Zealand up to 7.5 t on a car licence, L168 proposed 6 t for EVs only.
- D13 L135 "Conventional steer axle High Mass Limits (HML) of 7 tonnes"; L139 WA NHVR weighbridge flagged
  >7 t axle despite HML exemption permit; L165 Queensland TMR HML approvals; NSW and Victoria HZEV HML on
  the NHVR network without extra state permits; L168 NSW/QLD NHVR exemptions; one council rejected 8t steer
  axles.
- D06 (cranes): L304 proposed nationwide 12-tonne per axle limit; L309 hybrid cranes +2-3 tonnes (5%) on
  five-axle units and up to 1 tonne (8%) per-axle tolerance; L170 crane axle loads exceed prescriptive
  standards.
- Others: D11 L78 GML -> CML = +5 per cent payload; D04 L68 model +5% and +10% axle-group limits; D10
  L52-56/L155 C-RIS Options 4a/4b; D05 L24 HML conditions and L27 Victorian PBS Class 2 A-double criteria;
  D07 L37 operators stay at CML/GML rather than HML; D14 L189 HVSAPS may allow higher mass than manual
  assessment, fn5 L191 Class 1/2 definitions; D16 L62 no Tasmanian requests to exceed axle limits with
  LZEVs; heavy vehicle threshold "above 4.5 tonnes" GVM (D11 L8; D09 L16).

### (e) ALC curfew survey reports

- D07 L148-151: "The Australian Logistics Council conducted a community sentiment survey. Once curfews were
  reinstated, only 1 in 7 felt transport noise increased since COVID-19, and just 2% attributed any increase
  to freight trucks" (fn11 L171 ALC, "Curfews and Supply Chain Operability", undated).
- D09 L389: "A survey by the Australian Logistics Council found majority support for the continued
  relaxation of curfew rules; indeed just 6% of respondents were even aware that curfew rules had changed"
  (no footnote; Further Reading L399 "Australian Logistics Council (2022), Curfews and Supply Chain
  Operability").
- D10 L634-638: survey "of 1,205 Australians for the ALC": 71% for permanently removing curfews on overnight
  supermarket/retail deliveries; 67% for ports and warehouses operating at night (fn79 L645 ALC media
  release, 2 July 2020, Newgate Research); L707 surveys "modelled on the ALC/Newgate research".
- D05 (ALC's own submission) reports no survey (curfews L100-102; recommendation 3 L129-133).

### (f) Freight-growth projections

| Doc/line | Projection | Base-end years | Source cited |
| --- | --- | --- | --- |
| D07 L9 | "road freight will grow 77%" | 2020-2050 | BITRE freight projections (fn1 rr154 summary) |
| D07 L33 | "national freight task of 77%" | 2020-2050 | same passage restated |
| D10 L360 | "Road freight volumes ... grow by 77% by 2050" | to 2050, no base | fn42 Ibid. -> fn41 NatRoad (Clark 2025) summarising IRU 2024 |
| D10 L803 | "the freight task could grow by 77% by 2050" | to 2050, no base | AECOM 2025 for ARENA (fn91) |
| D13 L25 | road freight activity "approximately 35%" (truck emissions +10% / 2 Mt CO2-e) | 2025-2040 | DCCEEW emissions projections 2025 (fn2-3) |
| D14 L241 | Victoria's road freight task "75 per cent" | to 2040, no base | BITRE (2022) road freight forecasts 2022 update (rr155) |
| D16 L49 | road freight task "77 per cent" | 2022-2050 | DITRDCA Australian aggregate freight forecasts (fn1) |

- Related: D02 L320 BITRE actuals "between the Reference Scenario and High Scenario"; D15 L29 retrospective
  (road freight performance +5% since 1998, rail +8%).

### Issuer vs mentioned organisations (submitters named in other documents)

- TGE (D04): D13 L49 ARENA-funded "Depot of the Future" project; D13 fn10/fn11 "Change Management Report,
  TGE (2024)/(2025), p.15"; fn14/fn17 "Lessons Learnt Report: Milestone 2, TGE (2025)" pp.8, 10.
- EVC (D09): D10 L469/fn52 EVC charger data via ACCC/AER; D13 fn16 L186 EVC (2022) report.
- ALC (D05): survey in D07 L148, D09 L389, D10 L634 (see (e)).
- ALRTA (D10): D11 L18 ATA member association. ATA (D11): D04 L129 named for a proposed NAAS Council.
- Tasmanian Department of State Growth (D16): D06 fn2-3 L198-199 cites it as author of the 2022 HVAMS CBA;
  D16 fn3 L83 cites the same URL as "HoustonKemp Economists 2022".
- NHVR (D02) figures in other documents: D05 L47 SLGAAP 698 assessments; D10 L81 NHVR plan PBS savings,
  L182 NHVR permits via NatRoad; D11 L124 permit series; D14 L187 >70 NHVR maps; D13 L139/L168 NHVR
  weighbridge/exemptions.
- ARENA (D13) work cited elsewhere: D07 L99 (165 hubs), L105 (Toll $9.02 million, 28 heavy EVs, "Driving the
  Nation Programme"); D09 L252 (ARENA and CEFC); D10 L487, L522, L803-804; D14 L331 ("Driving the Nation
  Fund"), L358-360; D15 L60.
- Not named outside their own document (search of names): ARTC (D01), NET (D03), CICA (D06), Ai Group (D07),
  NSW Farmers (D08), The Australia Institute (D12), ARA/NRA (D15). NatRoad (quoted in D02, D07 fn8, D10,
  D15) is an ATA member (D11 L20) but not a submitter here.

### Jurisdiction figures appearing outside that jurisdiction's own submission

- Victoria (D14's issuer): D05 L27 Victorian PBS Class 2 A-double criteria, L51 "Victoria's HV-SAPS"; D06
  L206 HVSAPS "being rolled out in Victoria and proposed for New South Wales and South Australia"; D02 L106
  pavement sections from Victorian and Queensland networks; D09 L88 VIC network map, L323 Melbourne council
  refusal, L389 VC181; D10 L416 Victorian training program (~400 drivers), L553 Victorian grains area,
  L654 EPA Victoria hours; D13 L165 Victoria HML on NHVR network.
- Tasmania (D16's issuer): D09 L94 "Tasmania (no concession)"; D10 L203 HVAMS outcomes (80% OSOM, 95% SPV,
  ~700 -> ~30 SPV permits, 95% crane permit reduction), L219; D11 L123; D14 L217-218 (29 LGAs); D06
  L196-199; D04 L118; D07 L49; D02 L366.
- Queensland: D06 L17 ($116.8 billion 4-year capital program); D02 L130 TMR pavement wear rates; D09 L90,
  L101, L119, L385; D13 L165, L168; D14 L217, L219 (77 LGAs); D05 L96 Energeia for Queensland's network.
- NSW: D02 L304, L325; D06 L206, L229; D09 L86, L221, L383; D13 L165, L168, fn8; D14 L219 (128 LGAs).
- SA: D06 L206; D07 L58; D09 L92, L196, L387; D10 L407; D11 L199 (MC program; overseas experience except NZ).
- WA/NT: D02 L35 and D11 L59 (HVNL not in WA, NT); D09 L36-38; D13 L139, L165.

### Other repeated facts and relationships

- Aliases and similar names: NAAS = "National Automated Access System" everywhere except D14 L183
  "National Automated Assessment System"; HVAMS "Heavy Vehicle Access Management System" (D06 L196, D07 L49,
  D10 L202, D11 L106, D16 L47) vs "Heavy Vehicle Assessment Management System" (D14 L217); HVSAPS "Heavy
  Vehicle Structural Assessment Permit System" (D14) vs "Heavy Vehicle Structural Assessment Program" (D06
  L206) vs "HV-SAPS" (D05 L51); NHVDCF vs "HVDCF" (D16 L28); Driving the Nation "Program" (D13 L32),
  "Programme" (D07 L105), "Fund" (D14 L331); ACAPMAg (D05 L96, fn15) and ACAPMA (D10 fn69) - no stated link;
  "ADR" = Australian Design Rule vs "UNECE ADR 2025" dangerous-goods agreement (D13 L196); "ITTM" (D14
  L243) for ITMM; "Lessons Learnt Report: Milestone 2" attributed to Toll Group (D07 fn2/fn7/fn9; D09
  fn2/fn6 and L403-405) and to TGE (D13 fn14 p.8, fn17 p.10).
- ADR versions/dates: ADR 109/01 (D02 L296) vs ADR109/00 (D11 L97); AVAS/ADR 113/00: D09 fn13 L319 "As of
  November 2025, all EVs ... need to make an artificial noise", D11 L269 "will implement", D14 L372 new
  vehicles "from November 2025".
- Noise figures: D02 L611-643 (MAN Munich test: ~6 dB at 20 km/h; 11 dB vs literature diesel; 12 dB
  accelerating; EV 49 vs car 48 dB(A)/m; NHVR has no own testing); D04 L368-370 (3-5 dB(A) at 0-30 km/h,
  ~0-2 dB(A) above 30 km/h; OEM planning assumption); D07 L131 (Fraunhofer IML: "only 1 dB 'louder' than a
  car", footnoted to MAN 2023); D10 L615-622 (MAN 40-tonne eTruck 6-12 dB(A); KEYOU/Fraunhofer IML
  hydrogen); D11 L232 (ICE 70-90 dB, EV 55-65 dB); D12 L66 (e-buses up to 20 dB(A)); D14 L369 (no data).
- Charging hubs: D07 L99 "on the order of 165" (ARENA); D10 L487 "hundreds" (fn55 = RACE for 2030) and L804
  "up to 165" (AECOM); D15 L60 "around 165" (ARENA/AECOM).
- Permit time/cost and the 28-day rule: D02 L380 (>$220 industry, >$450 road managers, $88 fee); D07 L118
  and D09 L25 (Truckvolt: $3,000(+) for a basic three-day schedule; D09 adds $91 per permit per delivery
  address); D07 L37 and D09 L121 (30 days to three months); D06 L160 (up to 28 days); D07 L35 (16 weeks
  Adelaide-Sydney); D10 L182 (HVIA: road managers must answer NHVR consent requests within 28 days "unless
  an extension is agreed"); D14 L226 ("28-day limit for a permit to be issued").
- Emissions shares: D09 L10 road freight >20% of transport emissions; D10 L463 ~24%/~22 Mt (CCA); D10 L803
  ~80% of freight emissions/~36 Mt (AECOM); D13 L21 transport ~23% of national emissions; D14 L98 Victoria
  road freight ~8% of state emissions. Net-zero targets: D09 L10 national 2050; D14 L98 Victoria 2045; D16
  L184 Tasmania 2030.
- NHVDCF proposal vs outcome: D14 L243-269 options 1, 2a, 2b; endorsed 1 and 2b (December 2023); D07 L92
  ministers "decided not to proceed with requiring a full/open car licence before entering heavy-vehicle
  licensing"; D16 L89 DRIS "approved" December 2023, L104 pathways added "in addition to existing
  tenure-based" pathways; dates: D14 L320 (June 2026 + two years), D10 L348/L363 (2026 start), D16 L106/L138
  (Tasmania from Q1 2026; 2027-28), D11 L184 (no practical reform in almost ten years).
- Overseas drivers: D07 L87-95 (competency pathway, no tenure or car-licence prerequisite) vs D11 L197 (no
  recognition above a car licence) and L199 (SA: no overseas experience recognised except New Zealand); D05
  L150-151 (Migration Program pathway); D10 L436-440 (migration complementary, same NHVDCF standard). SA MC
  program: D10 L407; D11 L198-200.
- HVNL review reforms: D02 L83 (GML -> CML and 19 -> 20 m to be delivered by the HVNL Amendment Act 2025);
  D11 L68-76 (GML/CML and 20 m agreed and being implemented; 4.6 m height not yet); D10 L99 (4.6 m
  "proposed" in the consultation).
- Austroads NEF6392: D02 L106 (2,475 sections modelled; results available) vs D16 L41 ("nearing
  completion"); D14 L155 Austroads-commissioned LZEHV maintenance research "still in draft stage".
- Curfew hours: D04 L356 (5pm-9pm), L380 (22:00-06:00); D07 L131 (after 22:00); D09 L317 (after 6pm), L344
  (7pm-7am), L356 (6pm-10pm); D10 L654 (EPA Vic 7 am-10 pm; Sundays/public holidays 9 am-10 pm); D14 L375
  (two hours either side); D16 L166 (outside AM/PM peaks). Negative/scope evidence: D16 L148 (no
  noise-related restrictions known in Tasmania), L172 (Tasmanian restrictions not noise-based); D14 L373
  (road curfews rarely affect last km; planning permits do); D09 L311 (road-specific curfews "relatively
  rare"); D02 L656 (NHVR does not set curfews); D05 L101 and D06 L284 (curfews do not distinguish diesel
  and ZEVs); D13 L177 (ICE curfews apply equally).
- Charging barriers: D16 L141 "no known regulatory barriers" vs barrier lists in D02 L544-581, D04 L253-324,
  D07 L97-119, D09 L178-304, D10 L487-509; D02 L543 NHVR has no charging role.
- COVID curfew relaxation: D07 L144-146; D09 L377-391 (5 instruments; last VIC VC181); D10 L634; D14 L375.
- Rail interface: D01 throughout; D05 L35, L56-57, L133, L137 (parallel wording, no citation of ARTC); D14
  L210; D06 L176; D09 L42; D15 L37; D16 L26; D08 L99-105.
- Road user charging: D01 L61, L214; D02 L152-245 (MDL instead of PAYGO), L287; D04 L102; D05 L33-34, L59,
  L128; D07 L17; D14 L88 (Treasurers' joint statement), L163; D15 L16, L33; D16 L20-22, L51-54, L60 (FLCB).
- Overviews repeating tables or other passages: D02 L380 prose vs Table 3; D02 L306 vs Table 1; D14
  L96/L109 vs Chart 1; D10 L155 restates L52-56 with "per year (2023 dollars)"; D10 Summary L855-970
  restates sectional recommendations; D07 key recommendations L15-27 restated at L60-L165; D08
  recommendations at L33-49, L56-62 and L109-155; D13 insight list L84-88 vs headings.
- Late or last list members: D02 implementation bodies (last "Industry and employers" L463); D09
  decision-makers (last utility owners L44), state rules (last "Tasmania (no concession)" L94), COVID
  precedents (last VC181 L389); D11 member associations (last Western Roads Federation L36); D13 projects
  (last Mondo Power L67); D16 bodies (last "All other Australian licensing jurisdictions" L128); D04 data
  list (last ADRs L104); D05 recommendation 9 (L153, p7); D08 Recommendation 4 (L153, p7); D07 last
  recommendation L165; D10 item 33 (L968); D03 ask 6 (L26) and last request (L168).

## Gaps and coverage ledger

- Read ledger (all sequential, all complete; nothing unread): D01 L1-241; D02 L1-671; D03 L1-175; D04
  L1-404; D05 L1-165; D06 L1-349; D07 L1-198; D08 L1-158; D09 L1-408; D10 L1-973; D11 L1-307; D12 L1-88; D13
  L1-265; D14 L1-402; D15 L1-90; D16 L1-198.
- Missing or visually unresolved source content (the captures are text only; no PDF pages exist to inspect):
  D02 Figures 1-5 (L117; L336-342 incl. unattributed labels "+4.4% +6% +16% +0.5%"; L339; L409; L468-473) and
  Table 2 cell boundaries (L247-289); D06 Table 1 (L150) and Figure 1 (L153) image-only, figure numbering
  clash (L101-102, L141), blank place names in Case Study 2 (L216, L219, L225); D08 Figure 1 map (L97); D09
  steer-axle chart values (L67-70), "At Home | At Depot" column membership (L181-200), image L267; D13
  appendix answer alignment (L204-245, read by line position); D14 Chart 1 values (L111), headings out of
  order and the barrier list split around the IR5 box (L377/L393).
- Citation facts that are not extraction gaps: D10 L487 superscript 55 -> RACE for 2030 footnote (L511);
  D13 fn12 "Ibid." (TGE report) for a Toll statement (L135); D14 fn1 title "2025-30" vs URL "2025-29".
- Extraction spot-checks: text = docs minus a two-line header (docs line = text line - 2). Lines checked
  identical: D01 fn1 L159; D02 Table 1 row L171 and Table 3 FY2025 row L396; D03 L33; D04 L68, L277; D05
  L47; D06 L96; D07 L99; D08
  L75, L138, fn8 L125; D09 L119; D10 L54, L182; D11 L124; D12 L24; D13 L135; D14 L219; D15 L50; D16 L49.
  Page count not applicable (method "text", pages null); printed page labels are noted per document.
