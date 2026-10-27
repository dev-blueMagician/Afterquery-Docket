# aq-02028 - document map, part A (D01, D04, D07, D14, D18)

Navigation only: where facts are, not what to ask. Group A of a parallel mapping; the caller
merges parts into `notes/doc-map.md`. Citations are line numbers in `text/Dnn.txt` ("D07 L212").
Original `docs/*.txt` line = text line - 2 (text adds a 2-line header); verified on every spot-check.

## Bundle (group A scope)

- What it is: 20 plain-text submissions to the Productivity Commission inquiry into the long-term
  productivity of Australia's maritime logistics system (early 2022). Group A = D01, D04, D07, D14, D18.
- Provenance: `notes/intake.json` lists all 20 documents as `incomplete: false`, `gap_characters: 0`,
  `matches_capture: true`. Source hashes (manifest `sha256` = intake `source_sha256`):
  D01 e6b76e530c73f887818348d2f490919d78a1441fa785690150f544a4deae3979 (sub007, 12,294 chars);
  D04 78cdee4bc2571ebeabe47fef5556ffd3617b627f1b199d2d5d4387bfdbe30749 (sub016, 9,408);
  D07 9d7abd149a388728b4110fcfc732b70040c8d56679df8dd90ba62f58b8354821 (sub023, 85,216);
  D14 eed81ecfa604e3395e8f32cc14dbd5e3df66f5b9e66552fcefc0aa3e4eab185c (sub037, 8,227);
  D18 b30734e0f0f477df3ade867daa72c7a82f6c1f1c1228c45ae2db390e46a3633a (sub043, 8,507).
  Text-file hashes were not computed here (no hashing tool);
  the caller verified text = NFKC(source).
- Extraction spot-checks (text vs `docs/` original, +2 line offset): D07 Table 3 title (orig L447 = text
  L449), Table 2 row "Yard Jump Start $100.80" (orig L441 = L443), footnote 14 "section 139A" (orig L518
  = L520), "$1.9785 per m3" (orig L119/L511 = L121/L513); U+2026 in original = 5 (orig L259, L313 x2,
  L315 x2 = text L261, L315 x2, L317 x2); text L501 "..." was already ASCII in the original. D01 "2.88
  million", "661m", knuckle lines (orig L31/66/73/78/82) match. D04 "1.9->2.0", "Min 30 days", "2Million"
  (orig L18/58/56) match. D14 "3.5 Mt", "five voyage(s)" (orig L27/32/41) match. D18 footnotes 1-2 and
  "92 per cent" (orig L46/79/23) match. Page count: not applicable (plain text; embedded page markers
  noted per document).
- Reuse binding: new map; bind to the five source hashes above.

## D01 - VICT submission (Victoria International Container Terminal Limited)

- Source: text/D01.txt (110 lines) | docs/pcau_maritime_r1_sub007_maritime_logistics.txt. Page markers
  "PAGE 2"-"PAGE 6" at L10, L28, L61, L79, L97 (cover L3-8 unnumbered).
- Written or submitted by: Victoria International Container Terminal Limited (L6-7), "VICT" (L13).
  Owner ICTSI (L19) is mentioned, not the submitter. No named individual or signatory anywhere.
- Type, date, edition: submission; "February 2022" (L8), no day. Running header L11: "Productivity
  Commission Inquiry into the Long-term Productivity of Australia's Maritime Logistics System".
- Period covered: calendar-year events (2014, March 2017, 2018, 2019, 2020, 2021, mid-2021, mid-2023);
  rates "annually" / "per annum". No fiscal years used.
- Entities and aliases: VICT = Victoria International Container Terminal (L6-7, L13); ICTSI =
  International Container Terminal Services Inc (L19); Port of Melbourne (L30, L33, L35, L84); Webb Dock,
  West Gate Bridge, East Swanson and West Swanson Dock (L35), "the Swanson Dock" (L82); vessels CMA CGM
  Ural, OOCL Beijing, Soroe Maersk (L42); Fair Work Act (L91, L102); TEU defined "Twenty-foot equivalent
  Units (TEU)" (L33) and "Twenty-Foot Equivalent Unit (TEU)" (L42); "LTI" never expanded (L53); "the
  knuckle" = outcrop at berth 4 (L68, L80, L84).
- Quantitative facts (all VICT's own statements; no third-party source cited anywhere in D01):
  - ICTSI operates 34 terminals in 20 countries, "over 33-year experience" (L19-20); Image 1.1 "34 ICTSI
    Terminals" (L22).
  - Port of Melbourne: "Australasia's largest container port and one of the top four container ports in
    the southern hemisphere"; "currently services over 2.88 million ... (TEU) annually" (L33).
  - 2014: VICT awarded concession for the "third international container terminal" at the Port of
    Melbourne, at Webb Dock (L35). Terminal completed "Within three years"; first vessel March 2017 (L40).
  - Investment "1.3billion AUD so far" (L37); "added extra capacity ... (800,000 TEU per annum)
    effectively handling a third of the market already"; "further growth potential to 1.5 million TEU per
    annum" (L37).
  - Records: largest vessel in capacity CMA CGM Ural 10,622TEU; highest TEU exchange in a single call
    OOCL Beijing 12,733 TEU; longest vessel Soroe Maersk 346.98m length overall (L42).
  - "Australia's first fully automated container terminal"; committed "$235 million over the next two
    years on critical infrastructure" (L45).
  - Safety: "nil LTI's in 2020 and 4 low severity LTI's in 2021" (L53).
  - Average Truck Turnaround Time "less than 35 minutes" (L63). "over 60 gross moves per vessel berthing
    hour", "in line with the benchmark productivity achieved in Melbourne"; intends to be first to
    "surpass 80 gross moves per hour on average" (L65).
  - Berth 4 knuckle limits quay length to 661m, "barely adequate to berth 2 vessels with a length of
    300m - the common length of 7,000 TEU vessels" (L68). Vessels of 8,000TEU and over, >300m, arrived
    in Australia in 2018 (L70). Image 1.2 caption: two 300 meter vessels vs "current 336 meter vessels
    calling at the Port of Melbourne" (L72-73).
  - Not more than 5 Quay Cranes; 20 Yard Automated Stacking Cranes (L77).
  - From 2019 vessels of 9,000 TEU called Melbourne, handled at VICT (L82); first 346.98 meter vessel
    called Melbourne in 2020 (L82); berthing conflicts "restricting the capacity of VICT to 800,000 TEU
    per annum - well short of the initially design of 1,500,000 TEU per annum" (L82).
  - Issues first arose 2018; "In mid-2021 the Port of Melbourne provided VICT with an undertaking to
    remove the knuckle and extend the quay by 71 meters by mid-2023" (L84); will allow simultaneous
    berthing of a 350 meter and a 366 meter vessel (L85).
  - First phase online "by 2023"; "8 cranes for 2 berths"; productivity "expected to exceed 80 gross
    moves per hour for the first time in Australia" (L88).
  - Workforce "some 230 individuals. 181 blue collar ... governed by an Enterprise Agreement and 49 white
    collar staff" (L89) (181 + 49 = 230).
  - Enterprise Agreement under the Fair Work Act in 2016; renegotiated in 2021 (L91).
- Tables: none. Images 1.1 (L22), 1.2 (L72-75; L75 is annotation text "Unutilised area that VICT are
  paying lease for ..."), 1.3 (L80) have no captured content.
- Lists: advantages bullets L49-59, 5 items, last "mainly powered by much 'cleaner' electrical energy"
  (L59). Three vessel records (L42).
- Forecasts, deadlines, effective dates: $235m over next two years (L45); quay extension "by mid-2023"
  (L84); first phase "by 2023" (L88); 80 gross moves target (L65, L88); growth potential 1.5m TEU (L37).
- Hedged claims: "potential for bottlenecks" (L16); "there is potential for further improvement" (L62);
  "VICT intends to become ..." (L65, intention); "is expected to exceed 80 gross moves" and "it is expected
  that the project will be able to be executed without any disruption" (L88); "virtually impossible" (L77);
  "creates potential for significant damage" (L98). Firm: "VICT is the only terminal operator to perform
  Receipt & Delivery 24/7" (L51); "VICT is the only operator capable of servicing the larger vessels now
  operating in the Port of Melbourne" (L100).
- Rounded prose beside exact figures: "a third of the market" (L37) beside 2.88 million TEU (L33) and
  800,000 TEU capacity (L37); "1.5 million TEU" (L37) vs "1,500,000 TEU" (L82); "some 230" (L89).
- Notes: actions vs statements - Port of Melbourne "provided ... an undertaking" (L84, action by the
  port owner; removal itself is future); VICT "renegotiated" its EA in 2021 (L91, action); VICT "faced
  threats of protected industrial action" (L95); VICT recommends "a reconsideration of the operation of
  the Fair Work Act" (L102) and says VICT operations should be viewed "as an essential service" (L100).
  Negative evidence: D01 contains no occurrence of "charge", "surcharge" or "fee" (whole-file search),
  i.e. no mention of VICT's own landside/infrastructure charges. Layout: heading "Labour Constraints"
  is merged onto the end of L88 (also in source).
- Operative definitions, rules and scope exceptions: none beyond the EA under the Fair Work Act (L89-91).
- Amendments or contradictions: internal figures consistent (800,000 at L37 and L82). L37 "extra
  capacity (800,000 TEU per annum)" vs L82 capacity "restricted" to 800,000 against 1,500,000 design
  (framing differs, values equal). Cross-document tensions listed under Repeats.
- Coverage: FULL. L1-110 read in one sequential chunk. Missing source material: image content only.

## D04 - The Australian Steel Association submission

- Source: text/D04.txt (78 lines) | docs/pcau_maritime_r1_sub016_maritime_logistics.txt. No page markers;
  "Contd." at L55.
- Written or submitted by: The Australian Steel Association (ASA) (L4, L8); signed "David Buchanan, CEO
  Australian Steel Association." (L71-73); website L75. FTA and APSA are organisations whose
  recommendations ASA supports (L49, L57-66), not authors. Neither acronym is expanded in D04 (expanded in
  D02 L182).
- Type, date, edition: emailed submission "By email: maritime@pc.gov.au" (L3); subject "Australia's
  Maritime Logistics System" (L5). Undated.
- Period covered: "Over the past two years of the COVID-19 pandemic" (L10); "the past 12-18months" (L43);
  "each year" (L20, L58); "coming 12 months" (L10); "5-10year horizon" (L54). No fiscal years.
- Entities and aliases: ASA (L8); Productivity Commission (L8, L11); ACCC = Australian Competition and
  Consumer Commission (L47, L49); "Department of Agriculture Water and the Environment" (L40); ADF (L52,
  unexpanded); ports: Port of Fremantle, Port of Newcastle, Port Of Melbourne, Port of Brisbane (L31);
  trading partners Japan, Vietnam, Taiwan, China, Europe, The Middle East (L20).
- Quantitative facts (ASA's own; no source cited): "Since 1980" (L13); "around 1.9->2.0 million metric
  tons of Steel Product's are imported each year to Australia" (L20); ASA members "represent almost
  2Million MT of cargo Imports each year" (L58); cargo "reportedly held at Port for 1 month plus" for
  DAWE inspection (L40); "Min 30 days' notice periods" (L60).
- Tables: none.
- Lists: member types (L11, 9 types; last "trade credit insurance providers"); products no longer made
  locally "(but not limited to: ...)" 6 items, last "Special Steel Bar" (L25); key ports 4 (L31, last Port
  of Brisbane); own recommendations a)-e), 5 items, L47-54, last e) port infrastructure review "5-10year
  horizon" (L54); supported FTA recommendations i.-vi., 6 items, L57-66, last vi. "Waterfront Industrial
  Reform" (L66). Item iv "Regulation of Terminal Access Charges" (L63); v "Regulation of Container
  Detention Practices - The ASA supports this recommendation and calls for action urgently" (L64).
- Forecasts, deadlines: "may drive inflation in the coming 12 months" (L10); 5-10 year horizon (L54).
- Hedged claims: inflation "may drive" (L10); "reportedly held" (L40); "this appears to be due to the
  COVID-19 impacts of workforce availability" (L41); "As the productivity commission may be aware" (L11).
- Rounded prose beside exact figures: "around 1.9->2.0 million metric tons" (L20) vs "almost 2Million MT"
  (L58); both rounded, scopes differ (all steel imports to Australia vs ASA members' cargo imports).
- Notes: ASA's own asks (a-e) vs endorsement of another body's recommendations (i-vi, "as detailed in
  their separate submission", L57). Demurrage charged "by the Ports operators" (L33). Break-bulk focus:
  oversized steel cannot be containerised (L29); block stacking at four ports (L31).
- Operative definitions/rules: none.
- Amendments or contradictions: none internal beyond the rounded pair above.
- Coverage: FULL. L1-78 read in one chunk.

## D07 - Federal Chamber of Automotive Industries (FCAI) submission

- Source: text/D07.txt (703 lines + blank) | docs/pcau_maritime_r1_sub023_maritime_logistics.txt.
  Structure: cover letter L3-25; Executive Summary pages i-v L27-152 (page markers L27 "i", L58 "ii", L84
  "iii", L108 "iv" inline, L134 "v"); body pages 1-19 L154-554; Bibliography L557-701 (pages 19-22;
  markers L556, L584, L634, L681). Body page markers include inline "2" (L177), "6" (L281), "7" (L302),
  "15" (L479), "16" (L503); numbers at the start of L160, L168, L256, L512, L541, L545 are footnote
  markers, not pages.
- Written or submitted by: Federal Chamber of Automotive Industries (FCAI) (L8-10, L18); cover letter
  signed "Tony McOonald, Director Industry Operations" (L24-25, name as printed). FCAI = "peak industry
  body for Australia's importers and distributors of new passenger motor vehicles, light commercials,
  motorcycles and ATVs" (L18). All other organisations are cited/quoted, not authors.
- Type, date, edition: cover letter dated 16 February 2022 (L3) to Productivity Commission, GPO Box 1428,
  Canberra City ACT 2601 (L4-6), by email maritime@pc.gov.au (L7); "Please find attached a submission"
  (L18). Letterhead OCR noise at L11, L13, L16 (also in source).
- Period covered: Australian financial years written "2019-20", "2020-21" (L125-126, L135, L488, L515,
  L518), explicitly "financial year" at L135, L190, L515; explicit calendar years at L190, L192, L194.
  Ten-year windows "2010-11 to 2019-20" (L136, L532); figure series 2010-11 to 2020-21 (L403, L529, L534).
  FY month boundaries are not defined in prose; only bibliography titles hint (Flinders "July 2021 to June
  2022" L626; NSW Ports "Dec 21 (FY22)" L663).
- Entities and aliases: ACCC (L41); CIRA = Competition and Infrastructure Reform Agreement (L60, L267);
  MIRRAT = Melbourne International RoRo & Auto Terminal Pty Ltd (L88, L192), "ultimately a wholly owned
  shipping line Wallenius Wilhelmsen" (L192) vs bibliography "a wholly owned subsidiary of Wallenius
  Wilhelmsen Logistics AS of Norway" (L574); AAT = Australian Amalgamated Terminals Pty Limited (L88,
  L184; "Pty Ltd" L567, L577); FICT = Fisherman Islands Cargo Terminal (L88, L188); Qube Ports (L197,
  L221), Qube (L379), Qube Ports Pty Ltd (L646); Linx Cargo Care Group (L197); DAWE = Commonwealth
  Department of Agriculture, Water and the Environment (L100, L412) vs cited source name "Department of
  Agriculture and Water Resources" (L103, L416, L597); Inspector-General of Biosecurity (L106, L652);
  Fremantle Ports = WA Government trading enterprise managing the Port of Fremantle (L468) - operator vs
  port; ERA = WA Economic Regulation Authority (L145, L490, L548); Flinders Ports (port operator, Port
  Adelaide; L194, L257); "Port Adelaide" and "Port of Adelaide" both used (L194); NSW Ports, Ports
  Australia, Port of Melbourne as data publishers (L190-194); PwC = PriceWaterhouseCoopers (L289, L675);
  PRC = Port Competition Review Committee (L295); QCA = Queensland Competition Authority (L302, L311);
  QCAA = Queensland Competition Authority Act 1997 (Qld) (L304); DBCT = Dalrymple Bay Coal Terminal
  (L311); COAG (L313); ACG = Allen Consulting Group (L320); ESCV = Essential Services Commission of
  Victoria (L329); PoMC (L331, unexpanded); ESCOSA = Essential Services Commission of South Australia
  (L336); SADTEI = SA Department for Transport Energy and Infrastructure (L338); MSA Act = Maritime
  Services (Access) Act 2000 (SA) (L341); EMS (L344); GHD = GHD Pty Ltd (L78, L348); OEMs (L32); PDI =
  pre-delivery inspection (L170); PCC / PCTC = Pure Car Carriers / Pure Car and Truck Carriers (L165);
  ROR = rate-of-return (L493); PAA = Port Authorities Act 1999 (WA) (L486). People: ACCC Chairman Rod
  Sims (L306-307; Sims 2012 L689, Sims 2016 L247/L691); Professor Malcolm Tull (Murdoch University) and
  Professor Fred Affleck (University of Western Australia) (L249). Shipping lines Wallenius Wilhelmsen,
  Mitsui O.S.K. Lines, Kawasaki Kisen Kaisha ("K" Line) (L160). Thai Department of Agriculture, Thai Port
  Authority (L419). Name collision: economist "Johnson" (Averch and Johnson 1962, L498, L582) vs D14's
  Marghanita Johnson.
- Quantitative facts (source attribution in brackets; "FCAI" = no citation, FCAI's own):
  - Cover/overview: "over one million new vehicles imported into Australia each year" (L20, FCAI); "In
    2021 over 1 million motor vehicles were imported and sold in Australia" (L156) [FCAI 2022 = VFACTS
    2021 media release 6 January, L622]. Last three motor vehicle producers closed 2016 and 2017 (L30,
    L156). Market has four classes (fn 1 L54 = fn 9 L171).
  - Five major automotive terminals (L36, L184): AAT "can handle in excess of 600,000 motor vehicles per
    annum from its two locations" Port Kembla Inner Harbour ("80 km south of Sydney") and FICT Brisbane
    (L184-188) [AAT 2020]; "In the 2021 calendar year just over 336,000 motor vehicles were imported
    through Port Kembla (NSW Ports, 2022), while during the 2020-21 financial year just under 250,000
    motor vehicles were imported through the Port of Brisbane (Ports Australia, 2022)" (L190); largest
    automotive terminal = Webb Dock West, MIRRAT; "In excess of 430,000 motor vehicles passed through ...
    during the 2021 calendar year (Port of Melbourne, 2022)" (L192); Flinders Ports, Outer Harbour Port
    Adelaide, "Over 57,000 motor vehicles were imported through the Port of Adelaide during the 2021
    calendar year (Ports Australia, 2022)" (L194); Fremantle Ports, two Inner Harbour locations, "able to
    process more than 100,000 motor vehicle imports per annum" (L196, fn 12 Fremantle Ports 2021).
  - Two automotive stevedores Qube Ports and Linx Cargo Care Group; Qube Ports' holding company owns AAT
    (L197); "duopoly" (L221).
  - Biosecurity: 5 per cent of each shipment inspected; after two contaminated vehicles, 20 per cent;
    after a further two, whole consignment inspected, cleaned, re-inspected (L105-108 exec = L416-417
    body) [Inspector-General of Biosecurity 2018 p. 56]. Thai New Motor Vehicle Inspection Program:
    contaminated vehicles from Thailand "reduced by more than 90 per cent"; extension considered for
    Japan and South Korea (L419-420) [IGB 2018 p. 10].
  - Price elasticity of demand for new vehicles "around -1.5 per cent"; 1 per cent price rise -> 1.5
    per cent fall in sales (L365) [Smyrk & Morris 2006].
  - ACCC undertakings: MIRRAT accepted, announced 27 March 2014 (L377) [cited "ACCC (2021a)"; media
    release ACCC 2014 L572]; AAT/Qube accepted, announced 24 November 2016, re Qube's acquisition of "the
    remaining 50 per cent shareholding in AAT" (L379) [ACCC 2021; media release ACCC 2016 L579].
  - "In 2021 the FCAI received advice that MIRRAT was intending to apply a price increase of between 2 and
    5 per cent on vehicle handling on and from 1 July 2021" (L398); Port of Melbourne new vehicle imports
    reached "a new all-time record in 2020-21" (L399-400, Figure 3).
  - Fremantle: Victoria Quay "continuous quayage 1289m long with 7 berths in commercial use" (L475)
    [Fremantle Ports 2018b p. 57]; Outer Harbour at Kwinana "20 km further south" (L470); PCCs from Asia
    handle "two-thirds of the port's motor vehicle imports" (L477) [Fremantle Ports n.d.]; stacking area
    for single shipments "up to 4,800 vehicles" (L479).
  - Fremantle Ports 2020-21 "economic rate of return of 11.4 per cent, considerably higher than its target
    rate of 8.3 per cent, based on non-current assets valued at deprival value" (L488) [Fremantle Ports
    2021]. Five WA port authorities under the PAA (L486).
  - Cargo Berth Hire: charge applies to cargo at a heavy duty berth (L118, L508); heavy duty berths = H
    berth on Victoria Quay and berths 11 and 12 at North Quay (L508); "long-standing charge imposed at
    least since 1995" (L508; fn 14 L520 cites section 139A of the former Port Authorities Regulations 2001
    under the Fremantle Port Authority Act 1902 (WA)). Until "the end of September 2021" not applied to
    empty containers, livestock, pipeline products (including bunkers), scrap metal "and new and used
    vehicles up to 25 m3" (L119-120 exec; L509-510 body; fn 3 L128 / fn 15 L522 = Fremantle Ports 2018
    p. 3). Fremantle Ports wrote to shipping lines in August 2021 that it would cease the vehicle exemption
    (L121, L512; fn 4/16 private correspondence); "now imposes ... on the importation of all motor vehicles
    at the rate of $1.9785 per m3" (L121, L513) [Fremantle Ports 2021a p. 3 = "Ship and Cargo Charges from
    1 October 2021", L641].
  - Fremantle Ports quoted "an increase in the importation of new motor vehicles during 2020-21 of 29.4
    per cent over the previous financial year of 2019-20" (L515; FCAI: "the figures quoted by Fremantle
    Ports are correct", L516; exec L135 states the 29.4 per cent without attribution).
  - Vehicle-carrier ship visits to Port of Fremantle: "only 178" in 2020-21, 186 in 2019-20, "an average
    number of visits of around 196 in the 10-year period to the end of 2019-20" (L126 exec; L518 body)
    [Figure 4, Fremantle Ports 2021 p. 133].
  - 2020-21 Fremantle new vehicle imports "not unusually high, and was surpassed in 6 out of the previous
    10 years from 2010-11 to 2019-20" (L135-136; L531-532) [Figure 5, Fremantle Ports 2021 p. 35].
  - FCAI's own estimate: Cargo Berth Hire will extract "around an additional $2 million per annum from car
    carrier shippers" (L144, L547; no citation).
  - "High and heavy" (RTM Lines 2020): length >18m, height >4.5m, width >4.5m, weight >80mt (fn 6 L147 =
    fn 10 L173 = fn 18 L550).
  - Figure 2 footnote (L361, FCAI assumptions): average new vehicle volume 15.33 cubic metres (m3) for
    Port of Melbourne, Port of Brisbane, Port Kembla and Port of Fremantle; Port Adelaide shares 15.7 per
    cent (<10 m3), 24.1 per cent (10 to <15 m3), 60.2 per cent (15 m3 and over) (sum 100.0), based on
    FCAI (2022a) VFACTS December 2021 (L624).
- Tables (all GST inclusive; Source rows and "* Rounded to the nearest whole cent."):
  - Table 1 (L424-434) MIRRAT quarantine services, Port of Melbourne [MIRRAT 2021 = "Tariff Schedule for
    Melburne July 2021", L660]: Wash - Passenger Utility and Vans $146.27 (L427); External Clean -
    Passenger, Utility and Vans $99.37 (L428); Internal Clean - same $109.42 (L429); Underbody Clean -
    same $102.80 (L430); Movement to Washing Area $74.80 (L431). 5 rows, space-separated.
  - Table 2 (L436-446) AAT, Port Kembla [AAT 2021a = Port Kembla Cargo Terminal Berths 103,105,106,107
    tariff, L565]: Wash $207.54 (L440); Internal Clean $77.09 (L441); Yard Move $51.24 (L442); Yard Jump
    Start $100.80 (L443). 4 rows, tab-separated.
  - Table 3 (L449-460) AAT, Port of Brisbane [AAT 2021 = FICT Berths 1 to 3 tariff, L562-563]: Wash -
    Passenger $133.63 (L452); Wash - Commercial $267.51 (L453); Internal Clean - Passenger $80.53 (L454);
    Internal Clean - Commercial $250.39 (L455); Yard Move $72.04 (L456); Yard Jump Starts $133.55 (L457).
    6 rows; asterisk on title rather than "Tariff" header. Row labels differ across tables (Table 1 has
    External/Underbody/Movement rows; "Yard Jump Start" vs "Yard Jump Starts").
  - Figures with NO data in the source text (captions/sources only): Figure 1 (L351-352) "Charges for
    Essential and Non-Essential Maritime Services per Port Visit for Pure Car Carriers ($000) in 2017"
    [GHD 2017 p. 25]; Figure 2 (L357-361) "Cargo Specific Charges per New Motor Vehicle ... Average Cost
    per New Motor Vehicle* ($)" [Port of Melbourne 2021; Port of Brisbane 2021; Fremantle Ports 2021a;
    Flinders Ports 2021; NSW Ports 2021]; Figure 3 (L403) New Motor Vehicle Imports at the Port of
    Melbourne 2010-11 to 2020-21; Figure 4 (L529) ship visits by car carriers, Fremantle; Figure 5 (L534)
    new vehicle imports through Fremantle 2010-11 to 2020-21.
  - Prose that restates figure results: Fig 1/2 -> L78-82 and L348-354, L363 (Fremantle and Brisbane
    highest); Fig 3 -> L399-400; Fig 4 -> L126, L518; Fig 5 -> L135-136, L531-532.
- Lists: three natural-monopoly solutions L46-50 = L240-244 (last "public ownership"); CIRA clause 4.1b
  principles L63-69 = L270-276, 4 items (last: access regimes certified under the then Trade Practices
  Act, now CCA 2010, and the Competition Principles Agreement); World Bank three types of port
  competition L206-212 (interport, intraport, intraterminal); PDI functions L199, 10 items (last
  "performing any rectification services"); undertaking provisions L380-394, 7 items, last "a non-price
  dispute process (Gilbert + Tobin, 2021)" (L394) [Gilbert + Tobin 2021 = submission by Qube Ports Pty Ltd
  to SA Productivity Commission, L646]; Cargo Berth Hire exemptions L119/L509, 5 categories, last "new and
  used vehicles up to 25 m3"; Outer Harbour commodities L472 (10 named + "other bulk commodities"); state
  CIRA reviews in order NSW L288, Queensland L294, WA L319, Victoria L328, SA L335 (last); MSA Act service
  classes L344 (Regulated Services; EMS; Pilotage Services); KPMG quoted passages L315-317 (pp. 31, 33,
  77); shipping lines L160 (3); Victoria Quay berths A-H usage L475.
- Forecasts, deadlines, effective dates: MIRRAT 2-5 per cent increase "on and from 1 July 2021" (L398);
  Fremantle exemption ended "end of September 2021" (L119, L509), charges schedule "from 1 October 2021"
  (L641); Fremantle Ports investigating moving ro-ro trades to the Outer Harbour (Statement of Corporate
  Intent 2020-21, L481-483) vs 2017 Annual Report saying Victoria Quay east end "required for the
  foreseeable future" (L481); inspection program extension "being considered" (L420); bibliography
  tariff dates: Port of Melbourne "Effective 1 July 2021" (L668), Port of Brisbane "as at 1 July 2021"
  (L665), NSW Ports Port Kembla "Effective 1 July 2021" (L662), Flinders "July 2021 to June 2022" (L626),
  Fremantle "from 1 July 2018" (L632).
- Events/actions (did) vs recommendations (proposed): did - FCAI applied to the QCA in 2009 for
  declaration of FICT's vehicle import service; "In April 2011 the QCA determined that the vehicle import
  service was not a candidate service and thus rejected the FCAI's application" (L304); FCAI received
  MIRRAT advice (L398); Fremantle Ports wrote to shipping lines (L121/L512); NSW engaged PwC (L289) and
  imposed Part 6 price monitoring (L293); Queensland established PRC (L295); KPMG engaged by COAG (L313);
  WA engaged ACG (L320); Victoria commissioned ESCV (L329) and assigned roles in 2016 (L333); SA engaged
  ESCOSA (L336), SADTEI review 2008 (L338). Proposed by FCAI - renegotiate ACCC undertaking terms so
  over-recovery is handed back (L96-97 = L408-409); quarantine services contestable (L112 = L462); WA
  Government should refer Fremantle Ports to the ERA under s. 38 (L145 = L548). Mentioned only - Shipping
  Australia (2007) suggested price monitoring (L300); QCA warned of dissatisfaction (L302).
- Hedged claims (hedge -> what it attaches to): "It is perhaps no coincidence ... also appear to levy the
  highest port charges" (L82, L363; "perhaps"/"appear" -> the link and the charge level); quarantine
  charges "appear to be excessive and exorbitant" (L110, L422); operators "seem to have leveraged their
  monopoly power" (L112, L462); CIRA clauses "would appear to impose an obligation" (L114, L464); "There is
  arguably a conflict of interest"; "it appears the WA Government has chosen to ignore" (L117, L492);
  rationale "appears disingenuous" (L124, L516); evidence "would suggest this is far from the case" (L126,
  L518); "This appears to be an exercise in the naked abuse of monopoly power ... that will extract around
  an additional $2 million" ("appears" -> characterisation; "will extract" firm; "around" -> amount)
  (L144, L547); "arguably effective competition" (L221); ROR "may not necessarily be compatible" (L493);
  vehicles "may become contaminated" (L413); ESCOSA "may have an incentive" (L219). Firm: "There is no
  doubt that major ports along with automotive terminal operators possess monopoly or market power" (L52,
  L257); "imported new motor vehicles do pose a biosecurity risk" (L101, L413); excessive charges "will
  contribute towards the slower upgrade of the motor vehicle fleet" (L85, L372).
- Rounded prose beside exact figures: "over one million" (L20, L156); "just over 336,000", "just under
  250,000", "In excess of 430,000", "Over 57,000", "more than 100,000", "in excess of 600,000"
  (L184-196); "around 196" (L126, L518) beside exact 178 and 186; "around an additional $2 million"
  (L144, L547); "more than 90 per cent" (L420); tariffs rounded to whole cents (L434, L446, L460) while
  the per-m3 rate has four decimals (L121, L513).
- Operative definitions, rules and scope exceptions: natural monopoly (Posner 1969, L226); productive
  efficiency (L231); beneficiary pays principle (fn 7 L149 = fn 19 L552); high and heavy (above);
  biosecurity inspection escalation (L105-108, L416-417); CIRA clauses 2.3, 4.1a, 4.1b, 4.2, 4.3 (L60-71,
  L267-281), clause 2 (L336), clause 4 (L338); section 87B CCA 2010 undertakings (L88, L375); s. 38 ERA
  Act 2003 (WA) lets the WA Minister refer "any matter relating to an industry that is not regulated" (fn
  8 L151-152 = fn 20 L554); ports not a "regulated industry" under the ERA Act (L325, L490); no ministerial
  approval or independent oversight of WA port charges (L325); ROR target in statement of corporate intent
  approved by WA Minister for Ports each year (L493); PAA lets port authorities set charges, WA Transport
  Minister may direct (L486); NSW Part 6 Ports and Maritime Administration Act 1995 price monitoring
  applies to all NSW ports incl. Port Kembla (L293); Queensland: only DBCT regulated by QCA (L311);
  ACCC price monitoring "only relates to container terminal operators and stevedores and does not include
  automotive terminalling and other break bulk and bulk commodities" (L291); price monitoring regimes
  operate in Victoria and South Australia (L73, L284); Pricing Order (L333); MSA Act regimes (L341-344).
- Amendments or contradictions (neutral): Executive Summary (L27-152) repeats body passages with small
  wording changes - "pure car carriers" (L78) vs "pure carriers" (L348); "new cars" (L105) vs "new motor
  vehicles" (L416); "shipping containers" (L114) vs "containers" (L464); exec omits Fremantle Ports'
  attribution of the 29.4 per cent (L135 vs L515). Victoria Quay "7 berths in commercial use" while the
  same sentence group lists berths A and B unavailable and "berths C to H" (six letters) as common user
  berths (L475). "at least since 1995" (L508) with fn citing 2001 regulations (L520). AAT "Australia's
  largest ... automotive terminal operator" (L184) vs Webb Dock West "The largest automotive terminal"
  (L192) (operator vs terminal). ACCC event dates 2014/2016 cited as ACCC (2021a)/(2021) (L377, L379).
  Bibliography entries with no in-text citation: Joskow 2007 (L653), MacroPlan 2016 (L657), Taylor &
  VanDoren 2003 (L695).
- Coverage: FULL. Sequential chunks L1-90, L91-180, L181-270, L271-350, L351-430, L431-510, L511-580,
  L581-704; nothing unread. Missing source material: data of Figures 1-5 (charts not captured in the
  source text); letterhead OCR noise L11/L13/L16.

## D14 - Australian Aluminium Council response

- Source: text/D14.txt (58 lines) | docs/pcau_maritime_r1_sub037_maritime_logistics.txt. Page markers
  "Page 1 of 3" (L3), "Page 2 of 3" (L19), "Page 3 of 3" (L45).
- Written or submitted by: Australian Aluminium Council ("the Council") (L3, L8); signed "Marghanita
  Johnson, Chief Executive Officer, Australian Aluminium Council" (L53-55). Address Level 1, 18 National
  Circuit, Barton ACT 2600; Ph 02 6267 1800 (L14-17).
- Type, date, edition: letter submission, 11 February 2022 (L6), lodged via the PC website (L5).
- Period covered: rates "per annum" / "a year" / "per year"; "since 1955" (L8); "late 2021 and early
  2022" (L24). No fiscal years.
- Entities and aliases: Council (L8); Coastal Trading Act 2012 (L29); GL = General Licence (L31-38); TL =
  Temporary Licence (L34, L43, L48); "the Minister or the Department" (L48, unnamed).
- Quantitative facts (Council's own; no sources cited): industry in Australia since 1955 (L8); "five
  large (>10 Mt per annum) bauxite mines plus several smaller mines which collectively produce over 100
  Mt per annum", world's largest bauxite producer (L8); world's largest alumina exporter, "six alumina
  refineries producing around 20 Mt per annum of alumina" (L8); sixth largest aluminium producer, four
  smelters, "more than 20 extrusion presses" (L9); directly employs "more than 17,000 people, including
  4,000 full time equivalent contractors"; indirectly supports "around 60,000 families" (L9); "annual
  intrastate shipping requirements of around 14 million tonnes and interstate coastal shipping
  requirements of approximately 3.5 million tonnes"; exports "around 55 Mt of product a year" (L11);
  "intrastate shipping requirements of approximately 3.5 Mt per year, predominantly alumina shipped from
  refineries to aluminium smelters. This is covered by the Coastal Trading Act 2012" (L29); TL rule
  "minimum of five voyages" (L34).
- Tables: none.
- Lists: market segments (L21); shortage items PPE, chemicals, specialist raw materials (L24); Coastal
  Trading Act key issues L31-34, 4 bullets (bullets 2 and 3 share L33; last L34 five-voyage minimum and
  locked loading dates/ports); solutions "in order of hierarchy" L36-48: 1) publish schedule of routes
  with no GL vessels, exempt (L38-39); 2) a) remove five voyage minimum for TL (L43), b) amend tolerance
  provisions and voyage notification (L46), c) broaden definition of "emergency" (L47), d) require
  commercial factors, safety and vessel suitability in Minister/Department decisions (L48, last).
- Forecasts, deadlines: none.
- Hedged claims: "Interstate shipping may also be the mode of transport" (L11); "There has been a
  suggestion that the development of an Australian strategic fleet would be a possible solution" (L50,
  attributed to unnamed others; the Council only "would welcome the inclusion of an assessment"); COVID
  "to an extent, expected in a black swan event" (L26). Firm: "Currently, no General Licence holder able
  to service the alumina dry bulk market" (L31); previous single GL holder -> "monopoly situation at
  substantially higher costs" (L33).
- Rounded prose: all figures approximate ("around", "approximately", "over", "more than").
- Notes: "The industry has therefore, previously raised a range of potential solutions" (L36, past action)
  vs strategic fleet suggestion by others (L50). Demurrage at ports mentioned (L26). Typos as printed:
  "COVID0-19" (L20), "productive of" (L13), "venerable supply chains" (L50).
- Operative definitions, rules and scope exceptions: TL requires minimum five voyages and locked loading
  dates and ports (L34); "emergency" definition (L47, proposed broadening).
- Amendments or contradictions: SAME LABEL, DIFFERENT VALUE - "intrastate shipping requirements" =
  "around 14 million tonnes" (L11) vs "approximately 3.5 Mt per year" (L29); L11 attaches ~3.5 million
  tonnes to "interstate coastal shipping". No document-stated precedence. Cross-document scope tension with
  D20 L81 (see Repeats).
- Coverage: FULL. L1-58 read in one chunk.

## D18 - CCIWA letter (Western Australia)

- Source: text/D18.txt (95 lines) | docs/pcau_maritime_r1_sub043_maritime_logistics.txt. Page numbers
  "2" (L32), "3" (L50), "4" (L83); "1" (L45) and "2" (L64) are displaced footnote markers.
- Written or submitted by: CCIWA, "the peak body advancing trade and commerce in Western Australia"
  (L12); the acronym is never expanded in D18. Signed "Chris Rodwell, Chief Executive Officer" (L91-92);
  signature block does not restate the organisation. Both "Yours faithfully" and "Yours sincerely" printed
  (L89-90).
- Type, date, edition: letter dated 7 February 2022 (L3) to Athena Wicks, Productivity Commission, Level
  8, Two Melbourne Quarter, 697 Collins Street, Docklands VIC 3008 (L4-9); "our initial submission";
  looks forward to engaging "once a draft report is published" (L87).
- Period covered: "over the past 6 months" (L16); survey "In December 2021" (L16); footnote 27 October
  2021 (L48); 2011 Qantas dispute (L62).
- Entities and aliases: CCIWA (L12); Westport = "WA's new metropolitan container port" (L36); Qube
  ("stevedoring company", L43); Fremantle Port / Fremantle Port Authority (L43); union unnamed in body
  ("the same union", L43), named only in footnote title "Maritime Union of Australia" (L48); FW Act = Fair
  Work Act 2009 (L51), "(Cth)" (L77); Fair Work Commission (L60); Qantas (L62-63); case "Minister for
  Tertiary Educations, Skills, Jobs and Workplace Relations [2011] FWAFB 7444" (fn 2, L81); "Bremmer, J
  (27 October 2021. Fremantle Port: Maritime Union of Australia announces new mooring bans. The West
  Australia." (fn 1, L48, as printed).
- Quantitative facts: December 2021 - "around three in five WA businesses reported that supply chain
  disruptions were a barrier to growth" (L16); "Nearly two-thirds were suffering higher costs" (L18);
  "Nearly half" delayed delivery (L20); "One third" production setbacks (L22) (base of the three bullet
  shares not stated); "Most WA businesses (92 per cent) do not expect these pressures will alleviate any
  time soon" (L25). Survey source not named; L23 "We also identified ...". Fremantle: "approximately two
  weeks after long running industrial action involving ... Qube was resolved" (L43). Qantas 2011 (quoted
  from the decision): "affected 70,000 passengers, led to the cancellation of 600 flights, the grounding of
  7 aircraft, $70 million in damage"; Qantas shut-down "costing Qantas $20 million per day" (L62-63).
- Tables: none.
- Lists: survey bullets L18-22 (3); system features L26-34, 3 items, last "Escalating fees and charges"
  (L34, after page marker L32); FW Act suspension/termination grounds L51-59, 4 items, last "significant
  economic harm to a third party" (L59); recommendations L68-85, 4 main bullets, first with 3 required
  demonstrations (L72, L74, L75), last "State and federal governments should be prepared to utilise their
  right to take steps to stop industrial action" (L85, page 4).
- Forecasts, deadlines: Westport planning commenced (L36); risks re "container trade forecasts" (L36).
- Hedged claims: "these bodies sometimes operate with unaligned objectives" (L30); "some level of increase
  ... could be justified if driven by investments" (L34); union action "would have resulted in a ban on
  the mooring and unmooring" (L43, counterfactual: notified/proposed, outcome not stated); Qantas action
  "was not considered likely to cause significant damage" (L62). Firm: "the threshold for taking lawful
  industrial action is low ... industrial action is very difficult to stop" (L51).
- Rounded prose: "around three in five", "Nearly two-thirds", "Nearly half", "One third" (L16-22);
  exact "92 per cent" labelled "Most" (L25).
- Notes: did vs proposed - the union "notified the Fremantle Port Authority of proposed industrial action"
  (L43); CCIWA's asks are recommendations (L68-85). Submission focuses on industrial relations only (L38).
- Operative definitions, rules: FW Act grounds (L51-59); FWC "very high bar" for "significant economic
  harm" (L60). Term mismatch within D18: the rule list and L60 use "significant economic harm"; the
  recommendation at L77 asks that "serious economic harm" be interpreted as "important or of consequence".
- Amendments or contradictions: none beyond the term mismatch.
- Coverage: FULL. L1-95 read in one chunk.

## Shared ground within group A (navigation only)

- Fair Work Act / enterprise bargaining: D01 L89-102 (VICT EA 2016, renegotiated 2021, threatened
  protected action, reconsider FW Act); D18 L51-85 (FW Act 2009 grounds and proposals).
- Port of Fremantle: D04 L31 (break-bulk block stacking); D07 L116-152, L196, L466-554 (Fremantle Ports
  charges, rate of return, berths); D18 L43, L48 (Qube dispute, mooring bans). D07 L123/L515 says Fremantle
  Ports cited increased trade in "new and used motor vehicles, heavy machinery, and steel" (cf. D04 steel).
- Port of Melbourne / Webb Dock: D01 L33-42, L82-85 (VICT container terminal at Webb Dock); D07 L192, L261,
  L377 (MIRRAT automotive terminal at Webb Dock West; ACCC "Port Capacity Project" quote L261).
- Port of Brisbane: D04 L31; D07 L88, L188-190, L449-458 (AAT FICT).
- Qube: D07 L197, L221, L379, L646 (automotive stevedore, AAT owner); D18 L43 (Fremantle dispute).
- ACCC: D04 L47, L49 (proposed reviewer/regulator); D07 passim.
- DAWE inspections: D04 L40 (cargo held "1 month plus"); D07 L99-108, L411-420.
- Demurrage: D04 L33; D14 L26.
- Signatories with CEO title: D04 L73, D14 L54, D18 L92; D07 signatory is a Director (L25); D01 none.
- PC contact details differ: D07 L4-6 (Canberra GPO Box) vs D18 L5-8 (Docklands); email maritime@pc.gov.au
  in D04 L3 and D07 L7.

## Repeats elsewhere in the bundle (whole-bundle Grep of text/D01-D20; inspected hits)

- Port of Melbourne container volume / status: D01 L33 "over 2.88 million ... TEU annually",
  "Australasia's largest container port". D08 L147 "approximately 3million TEU pa (1) handled through
  Melbourne" (source note L144: Dept of Transport Voluntary Performance Monitoring Framework - Q3). D11 L39
  "Australia's largest container port". D10 L39, D13 L120-121, D06 L133: World Bank/IHS Markit study ranks
  "Australia's largest container ports, Melbourne and Sydney" bottom 15% and 10% of 351 ports.
- Vessel size: D01 L42 VICT handled CMA CGM Ural 10,622TEU (largest in capacity), L70 8,000TEU+ from
  2018, L82 9,000 TEU from 2019. D13 L156: largest container ships Port of Melbourne, Port Botany and Port
  of Brisbane "can accommodate are in the range of 8,000 TEU to 10,000 TEU, fully loaded"; D13 L167 Port
  Botany "+15,000 TEU vessels" challenge.
- 24/7 operations: D01 L51 "VICT is the only terminal operator to perform Receipt & Delivery 24/7" vs
  D08 L108 "the stevedores have elected to open their operations at 24/7". Truck turnaround: D01 L63
  (<35 minutes) vs D08 L283 (monitoring of "all three container stevedores").
- Terminal access / infrastructure charges (D04 L63 asks for regulation; D01 silent): D02 L174-182 table
  "INFRASTRUCTURE SURCHARGES - AS AT 25 January 2022 per full container / excluding GST": VICT Melbourne
  $141.80 export / $141.80 import, effective 1-Jan-22 (L180); DP World Melbourne $105.90/$144.70 1-Jan-22
  (L179); Patrick Melbourne $84.90/$129.50 1-Mar-21 then 101.90/155.40 7/03/2022 (L180); "Data collated
  courtesy of" APSA, FTA and CTAA (L182). D13 L221-226: TAC "Increased 2,600% in 11 years"; quotes "VICT
  Melbourne Landside Update 30 January 2019" on the Infrastructure Surcharge. D08 L131 "Infrastructure
  Access Charge increasing from $3.57 to more than $140.00 per TEU in 3 years"; D08 L206 "up to $140.00
  per container" and "from less than $3.57 per TEU three years ago to over $140.00 per TEU today". D19 L336
  (quoted statement): Port of Melbourne access fees "$3.60 to $80.00 per container over the past 2 years",
  "over 2 000 per cent in just two years". D11 L49, L54 (Port of Melbourne TACs up over 5 years; ACCC
  report chart). Other TAC mentions: D06 L33, L137-142; D09 L38; D16 L24, L35, L152-159.
- AAT / Brisbane: D07 AAT automotive terminals Port Kembla and FICT (L88, L184-188), Table 3 quarantine
  tariffs (L449-460). D02 L176 lists "Australian Amalgamated Terminals (AAT) Brisbane $78.00 $100.00
  1-Jul-21" in the per-container infrastructure surcharge table (different charge type).
- Flinders Ports / Port Adelaide: D07 L194, L257, L336-344, L626. D02 L176 "Flinders Adelaide Container
  Terminal Adelaide $75.00 $75.00 1-Jul-21 79.50 112.50 1/04/2022". D12 L46-51 (Flinders Ports vertical
  integration, SA regime ring-fencing concerns), D12 L70 (ESCOSA 2022 review). D05 L137, L145 use
  "Flinders Port Holdings" (not equated with Flinders Ports in any text).
- Fremantle: D18 L43/L48 (Qube dispute; MUA mooring bans, 27 October 2021) and D15 L122-123 (ABCC
  inquiry into alleged picketing "during a dispute last year involving the CFMMEU's MUA division on
  Fremantle's docks"); D03 L152 (farm machinery for Fremantle diverted to Port Melbourne); D09 L64 (mining
  equipment delays); D10 L19 (ACCC monitors stevedores at Adelaide, Brisbane, Fremantle, Melbourne,
  Sydney); D02 L178-179 (DP World Fremantle $45.00/$45.00 1-Jan-21; Patrick Fremantle $26.92/$53.85
  1-Mar-21 then 28.84/57.69 7/03/2022). "Fremantle Port Authority" (D18 L43) vs "Fremantle Ports" (D07
  L468; D07 L486 calls Fremantle Ports one of five WA port authorities).
- NSW port privatisation: D07 L289 (decision to privatise Port Kembla and Port Botany; no year), L293.
  D09 L152-156 "During 2013 and 2014 the NSW Government privatised Port Botany, Port Kembla and the Port of
  Newcastle"; 50-year port commitment deeds; cap "30,000 TEUs per annum". D12 L19 Newcastle privatised
  2014. D13 L182 (Newcastle/Kembla as alternate container ports). D04 L31 Port of Newcastle (break bulk).
- Port of Melbourne lease and ESC: D07 L333 (2016 legislation to lease; ESCV monitors Pricing Order),
  L263-264 (ESCV 2020 p. 16 quote on vehicle trade not relocating to Geelong/Hastings), L618 (Market Rent
  Inquiry 2020). D19 L336 "lease of the Port of Melbourne in March 2016". D10 L68 privatisation 2016; L69
  ESC final report 28 January 2022 on pricing order compliance 1 July 2016 - 30 June 2021; L83 Market Rent
  Inquiry 14 August 2020. D11 L74-75; D06 L121 (ESCV 2020 market-power finding on land rents).
- ACCC: D07 scope statement that ACCC monitoring covers only container terminal operators/stevedores
  (L291). ACCC Container Stevedoring Monitoring Report mentions occur in D02, D05, D06, D09, D10, D13, D15,
  D16, D19 (none in group A). Rod Sims: D07 L306-309 (2012 speech), L247 (2016) vs D13 L77-125 (quotes as
  "ACCC Chair Rod Sims").
- World Bank: group A cites only "The World Bank (2007, p. 270)" Port Reform Toolkit (D07 L206, L695). The
  World Bank/IHS Markit Container Port Performance Index ranking appears in D03 L98, D06 L133, D09 L86/L98,
  D10 L39, D13 L120, D16 L112 (not in group A).
- Coastal Trading Act: D14 L28-48. D20 L27 (introduced July 2012), L56, L62-72, L76-81, L87-106 (2019
  review; CIF proposals incl. "Removal of the five-voyage minimum requirement to apply for a temporary
  licence" L90, voyage notification L94, tolerance provisions L96, "temporary licences to be issued in
  emergency situations" L98), L121-191 (TL process; "12-month period" L124). SCOPE TENSION: D14 L29 says
  intrastate alumina shipping (~3.5 Mt) "is covered by the Coastal Trading Act 2012"; D20 L81 says the Act
  "only applies to vessels that trade interstate". D19 L86 "42 vessels that hold a General Licence"
  (cf. D14 L31 no GL holder able to serve alumina dry bulk); D19 L205 January exemption after rail floods;
  D06 L40, L152, L163 section 11 exemption for container and ro-ro vessels to WA "until 31 March 2022";
  D09 L128. D20 L52 bulk coastal freight "around 50 million tonnes" over 10 years.
- Strategic fleet: D14 L49-50 (suggestion; asks for assessment); D19 L18, L274, L378-411 (proposal; L403
  "20 vessels would result in 1800 permanent jobs ... ~100 seafarers each year ... $173m in tax revenue",
  support "$140m annually").
- Fair Work Act / MUA / industrial action: D02 L158, L162; D03 L207; D05 L224; D09 L97, L103-104 (ss 172,
  194, 409); D10 L42-44 (Patrick FWC application 26 October 2021; Svitzer January 2022; in-principle
  agreement 7 February 2022); D13 L208-216; D15 L79, L113-117; D16 L30, L128 ("essential service", cf. D01
  L100). Qantas, Westport, CCIWA, Athena Wicks: D18 only.
- Biosecurity/DAWE: D04 L40, D07 L99-114/L411-420; D13 L306-324; D06 L98; D20 L30, L108; D03 L184.
- FTA / APSA: D04 L49, L57-66; D02 L182 (collated surcharge data); D16 L155 (recommendation "in line
  with" APSA's). No bundle document is authored by FTA or APSA (search of names/acronyms).
- Steel / aluminium: steel import tonnage only in D04 (L20, L58); D07 L123/L515 steel demand at Fremantle
  heavy-duty berths; D09 L51; D17 L40; D20 L49 (iron and steel, alumina and aluminium producers depend on
  coastal shipping); D07 L472 (Fremantle Outer Harbour handles alumina, bauxite).
- Demurrage/detention mentions elsewhere: D02, D05, D06, D09, D13, D20.
- Declaration/access: D07 L304-311 (FCAI-QCA 2009/2011; Sims on declaration), L679 (PC 2013 National
  Access Regime); D12 L19-34, L89 (Port of Newcastle declaration history).
- Competition and Consumer Act: D07 L69, L88, L276, L375 (s 87B); elsewhere Part X (D06 L163, D10 L29),
  ss 45E/45EA (D15). "Part X" and "seafarer" do not occur in group A.
- Same numeral, different label (no relationship stated): 430,000 (D07 L192 vehicles, Webb Dock West
  CY2021; D13 L174 Port Botany rail "430,000 pa"); 1.3 billion (D01 L37 VICT investment; D19 L226 tax
  revenue 2012-13); 250,000 (D07 L190 vehicles Brisbane FY2020-21; D19 L279 cadet training cost); 92 per
  cent (D18 L25; D16 L105 "92% of respondents" handling costs); "two-thirds" (D18 L18; D07 L477).

## Gaps

- No unread ranges in D01, D04, D07, D14, D18 (all read sequentially in full).
- Missing source material (not unread): D07 Figures 1-5 chart data (L351, L357, L403, L529, L534) - only
  captions, sources and prose summaries exist; D01 Images 1.1-1.3 (L22, L72-75, L80). The originals are
  plain text, so these cannot be recovered locally; any figure value beyond the prose is unresolved.
- Extraction noise: D07 letterhead L11, L13, L16 and signatory spelling L24 (also in source).
- Text-file sha256 not recomputed here.
