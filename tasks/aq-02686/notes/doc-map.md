# aq-02686 - document map

Maintained by the caller or optional `bundle-mapper` from `text/` (and `docs/` for layout issues).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

Conventions used below: `Lnn` = line number in `text/Dnn.txt` as shown by a numbered read (1-based).
The matching line in the `docs/` original is `Lnn - 2` (text/ adds one header line and one blank line;
checked on D01 L82, D05 L154, D07 L70 and L249). Quoted strings are verbatim anchors from the text files.
"Mapper arithmetic" marks a calculation made while mapping; it is not a document statement.

## Bundle

- What it is: seven Federal Register texts, 2022-2026, issued by four bodies (EPA x3, DOE x2, TVA x1,
  Treasury x1). They share a battery / critical-mineral / recycling topic; only some are formally linked
  (see Shared ground). Publication order equals id order: D01 June 9, 2022; D02 December 4, 2023;
  D03 April 8, 2024; D04 May 6, 2024; D05 August 16, 2024; D06 December 23, 2024; D07 April 24, 2026.
- Documents: 7; ids from `text/manifest.json` (D01-D07 = task page Doc 1-7 per `notes/intake.json`).
- Mapped (2026-10-10): D01, D03, D05, D06, D07 by the bundle-mapper, each read in full; D02 and D04 by
  the caller, each read in full (see their section). The caller also read D01, D05 and D07 in full and
  D06 L20-242 first-hand; D03 is known to the caller through this map only (no candidate uses it).
- Gaps: none (every line of all seven read). No scans, charts or images: all seven sources are plain text. Tables
  cited by D03 and D06 (Final EIS table 2.2-1, table 3.824; TSD tables 4-8 and 5-2) are in external
  documents that are not in the bundle - missing source material, not unread text.
- Extraction spot-checks (originals are `.txt`, so no page count applies):
  - Page markers `[[Page N]]` counted in docs/ and text/ for all seven files: identical
    (D01 6, D02 7, D03 8, D04 12, D05 8, D06 7, D07 8).
  - Table: D05 index row "197......................." present in docs/fr_2024_16461.txt L152 = text L154.
  - Footnote: D01 footnote "\4\ Strategic and critical minerals" present in docs/fr_2022_12459.txt L80 = text L82.
  - Oddities confirmed to be in the originals, not extraction artefacts: D07 "$14,967" (docs L247),
    "Metal cobalt" (docs L333), "Subtitles C" (docs L323, L352), "whichpersons" / "Forpurposes" / "thedocket"
    (docs L310, L312, L316, L175, L198); D06 "February 2024" (docs L122); D03 "85 FR 31780" (docs L113),
    "89 FR 6108" (docs L55), "ENTG" (docs L88).
- Provenance: `notes/intake.json` records all seven as `incomplete: false`, `gap_characters: 0`,
  `matches_capture: true`; capture sha256 110862be...477ee0.
- Reuse binding (source sha256 and char count from `text/manifest.json`, read 2026-10-10; the previous
  map was the unfilled template, so nothing was reused):
  - D01 1a214892198f2eeaf86e32d0e22267dee01cc76708f8c8d120eb8ece79fbcc86 | 42,284 chars | 225 lines
  - D03 1a800e21470b080f40920f7f59c583e73f49a058b2636110badebff656c04dad | 58,260 chars | 231 lines
  - D05 a59b9eb90eda0142ae547b688f148b6a297227226e868550e9a5ec33474d4611 | 40,006 chars | 556 lines
  - D06 78d5a021c4f04fec711a680ee02312bd99e752f75be6ea38a399121645dd076f | 53,457 chars | 242 lines
  - D07 93c061d238a7d62a111088e48e600d8bad50113eeec13291823feedfdfd40e53 | 56,912 chars | 366 lines
  - D02 7943dee0c...6871ede | 48,395 chars | 240 lines and D04 ff080d73e...0535e9 | 85,760 chars | 355 lines
    (caller's section).

## D01 - EPA, Development of Best Practices for Collection of Batteries To Be Recycled and Voluntary Battery Labeling Guidelines; Request for Information

- Source: text/D01.txt (docs/fr_2022_12459.txt) | FR pages 35202-35208 (L6; markers 35203-35208).
- Written or submitted by: Environmental Protection Agency (L11, L17); the requesting office is "the Office
  of Resource Conservation and Recovery (ORCR) within the Environmental Protection Agency" (L23). Signer
  "Carolyn Hoskinson, Director, Office of Resource Conservation and Recovery." (L221-222). Contact Rita Chow,
  "Resource Conservation and Sustainability Division", "(202) 566-0227" (L39).
- Type, date, edition: Notices section; "ACTION: Request for Information (RFI)." (L19). Published
  "Thursday, June 9, 2022" (L3, L5); 87 FR, Number 111; "FR Doc No: 2022-12459" (L7);
  "[EPA-HQ-OLEM-2022-0340, FRL-9842-01-OLEM]" (L13); "Dated: June 3, 2022." (L220);
  "Filed 6-8-22; 8:45 am" (L223); "BILLING CODE 6560-50-P" (L224). No RIN is printed. Single edition.
- Period covered: not a periodic report. Forward-looking ("Over the course of 2022, ORCR will be hosting
  virtual meetings" L95).
- Deadlines and dates:
  - Comment deadline: "must be received on or before July 11, 2022" (L25).
  - Feedback-session dates are not printed: "The dates and times for those feedback sessions will be posted on" (L25).
  - Background dates: "In 2019, the U.S. Department of Commerce issued a Federal Strategy" (L71);
    "In February 2021, President Biden signed Executive Order 14017" (L71); "In June 2021, the White House
    released" (L71); "released a report in July 2021" (L105); "In October 2021, EPA held a two-day virtual
    stakeholder workshop" (L105); "Argus. (2017)" (fn 5, L83); "U.S. Geological Survey 2022 List of
    Critical Minerals" (fn 12, L127); "Infrastructure Investment and Jobs Act of 2021" (L23).
- Quantities (all in L91 unless noted; none is stated twice, none has a second value):
  - "it provided more than $7 billion investment in the supply chain for batteries" - for DOE; firm,
    lower-bound wording ("more than"); scope "including investments in the end-of-life infrastructure
    for batteries from the collection, safe storage and transportation, recycling, and second-use".
  - "it provided $10 million in funding for EPA to develop battery collection best practices" - firm.
  - "It also provided $15 million in funding for EPA to establish a program to develop voluntary
    labeling guidelines for batteries and other forms of communication materials" - firm.
  - "up to 40% of critical materials in batteries may be supplied from recycled batteries according to
    the U.S. Department of Energy (DOE).\6\" (L79) - forecast, attributed to DOE, hedged (see below).
  - Submission format: "1-inch margins" (L49); "Times New Roman and 12-point font" (L50); "Two clearly
    delineated sections" (L48). Docket Center "8:30 ... a.m.-4:30 p.m., Monday-Friday" (L31-35).
- Statutes and authorities: "Infrastructure Investment and Jobs Act (Pub. L. 117-58), also known as the
  Bipartisan Infrastructure Law" (L57). D01 cites NO section number of that Act (searched "section",
  "sec.", "U.S.C.", "CFR": only L37, L48, L57 hit; none is a statutory section). "FAR 15.202(3)" (L51).
  "Executive Order 14017" (L71).
- Entities and aliases: EPA / "the Agency"; ORCR; "U.S. Department of Energy" = DOE (L62, L79, L91);
  U.S. Department of Commerce (L71); White House (L71); U.S. Geological Survey (fn 12); Argus (fn 5);
  "Rechargeable Battery Recycling Corporation (RBRC)" (L200), "RBRC's Call2recycle.org" (L209);
  Earth911 (L209); Minnesota, "Larimer County, Colorado" (L199). "Bipartisan Infrastructure Law" is the
  alias used after L57 (L62, L71, L91, L95, L105, L114, L174, L196); "BIL" is never used in D01.
  "single-use batteries, also known as primary batteries, and rechargeable batteries, also known as
  secondary batteries" (L23, L60).
- Tables: none.
- Lists:
  - Critical minerals used in batteries, 6 items: "antimony, cobalt, graphite, lithium, manganese, and nickel" (L79).
  - Battery chemistries named: "lithium based, nickel-metal hydride, and other battery chemistries"
    (L23, L60, L122) - an open list ("including but not limited to" L60, L122). Also "lithium-ion"
    (L70, L79, L105), "lead-acid" and "small, sealed lead acid batteries" (L122).
  - Battery types: "small consumer batteries, large format batteries (including electric vehicles and
    grid energy storage), and industrial batteries used in manufacturing, commercial businesses, and
    healthcare operations" (L23, L60); short form "small format, large format, and industrial" (L59, L117).
  - Vehicle management chain, 7 items: "dealerships, repair shops, auction houses, dismantlers, entities
    that repurpose electric vehicle batteries, refurbishers, and scrap yards" (L23; repeated L180).
  - Two programs covered by the RFI (L58, L59). Best-practice criteria, 3: "technically and economically
    feasible; environmentally sound and safe for waste management workers; and optimize the value and
    use of material derived from recycling of batteries" (L58). Labeling-program purposes, 3: "identifying
    battery collection locations and increasing accessibility to those locations; promoting consumer
    education about battery collection and recycling; and reducing safety concerns relating to the
    improper disposal of batteries" (L59).
  - Related RFIs named (L62): "Solid Waste Infrastructure for Recycling Grant Program and the Recycling
    Education and Outreach--Grant Program and Model Recycling Program Toolkit".
  - Four "key information categories" (L115-117; bullets lost, items run together): scope and
    prioritization; understanding the collection and recycling system; labeling guidelines; reuse and
    recycling communication materials. They correspond to sections IV.A (L120), IV.B (L155), IV.C (L172), IV.D (L194).
  - Suggested questions are NOT numbered in the text. Counts by extracted paragraph (a counting
    convention, not a document statement; many paragraphs hold several question sentences; 46 lines
    of D01 contain "?"):
    - A (L123-153): one "Please share any existing studies and reports" lead-in (L123) with four [cir]
      sub-items (L124, L130, L131, L132), then 13 question paragraphs (L133, L134, L135, L136, L137,
      L138-143, L144-145, L146-147, L148, L149, L150-151, L152, L153).
    - B (L158-170): 13 paragraphs, one per line.
    - C (L179-192): "Scope of Voluntary Labeling Guidelines" (L179) with 4 paragraphs (L180-183);
      "Knowledge of Existing Battery Labeling Guidelines" (heading fused into L184) with 8 paragraphs
      (L184, L185, L186-187, L188, L189, L190, L191, L192).
    - D (L197-213): 5 paragraphs (L197, L198, L199-200, L208, L209-213).
  - Named existing communication materials, 3 (L199-200): "Minnesota--Be Our Battery Hero" (fn 13 URL
    reads "Be-A-Battery-Hero"), "Larimer County, Colorado--Be Alert! Divert Hidden Batteries",
    "Rechargeable Battery Recycling Corporation (RBRC)--Avoid the Spark". Websites named, 2: "Earth911
    and RBRC's Call2recycle.org" (L209).
  - Footnotes: 15 (\1\-\15\) at L74-76, L82-85, L98, L108-111, L127, L203-205. Sections I-V (L44, L53, L64, L93, L215).
- Forecasts, guidance, future actions: "the U.S. Department of Energy will be issuing future information
  requests ... which includes several grant programs to support battery collection, safe storage and
  transportation, recycling, and second-use" (L62) - a mention of DOE's plans, not an EPA action.
  "EPA is intending to develop a strategy to increase the circularity of electronics, including
  batteries" (L95). "the demand for these batteries are expected to continue rising at an exponential rate" (L79).
- Hedged claims:
  - "up to 40% ... may be supplied from recycled batteries" (L79): "In the future", "up to", "may" all
    attach to the supply share itself; attributed to DOE.
  - "lead-acid batteries may not need to be considered in the battery collection best practices" (L122):
    "may not" attaches to the scope decision. Followed by "However, EPA is interested in information on
    other lead-acid batteries such as small, sealed lead acid batteries that may not be recycled at a
    high rate" - here "may not" attaches to the recycling rate of the small sealed type.
  - Firm in the same sentence: lead-acid batteries "are manufactured with antimony, a critical mineral,
    and are currently recycled at a high rate especially from vehicles" (L122).
- Rounded prose beside exact figures: none (no tables; dollar figures appear once each).
- Operative definitions, rules and scope exceptions:
  - fn 4 (L82): "Strategic and critical minerals are any materials that are needed to supply the military,
    industrial, and essential civilian needs of the United States during a national emergency, and that
    are not found or produced in the U.S. in sufficient quantities to meet such need."
  - "critical materials" and "critical minerals" are both used (both in L79); "critical materials" is not defined.
  - Not a solicitation: "does not constitute a Request for Proposals (RFP) or a Request for Applications
    (RFA)" (L217); "does not represent any award commitment" (L218); "Response to this RFI is voluntary" (L46).
  - No CBI: L36, L51.
- Amendments or contradictions: none found inside D01.
- Notes / passages not fully interpretable: the last sentence of the SUMMARY (L23, "Information from a
  wide range of stakeholders ... and international organizations.") has no verb. L115-117 category
  bullets are fused. Question bullets carry no markers, so question boundaries rest on line breaks only.
- Coverage: FULL. Read L1-225 in one pass (every line). Nothing remains unread.

## D02 / D04 - DOE "Interpretation of Foreign Entity of Concern" (proposed, then final)

Mapped by the caller (Claude Code, claude-opus-5-5), 2026-10-10. Coverage: FULL for both, read in one
pass each (D02 L1-240, D04 L1-355). Reuse binding: D02 7943dee0c...6871ede, 48,395 chars; D04
ff080d73e...0535e9, 85,760 chars (text/manifest.json).

- D02: DOE Office of Manufacturing and Energy Supply Chains (MESC), "Notification of proposed interpretive
  rule; request for comments" (L22); published Monday, December 4, 2023 (L3), 88 FR pages 84082-84089 (L6),
  RIN 1901-ZA02 (L15); comments "no later than January 3, 2024" (L28); signed November 28, 2023 by Giulia
  Siccardo (L233); contact Mallory Clites (L37). Sections A-G; operative proposal in Section B (L75-123),
  explanation in Section C (L125-205), further requests in Section D (L207-211).
- D04: same office and RIN, "Notification of final interpretive rule" (L22); published Monday, May 6, 2024
  (L3), 89 FR pages 37079-37091 (L6); "effective May 6, 2024" (L28); signed April 18, 2024 (L344), liaison
  April 22, 2024 (L350); contact Widad Whitman (L31). Sections I-VI: comments and responses II (L79-194),
  explanation of changes III (L196-276), regulatory review IV (L278-284), operative text V (L286-336).
- Statute (both): BIL section 40207 "$6 billion" (D02 L64, D04 L63); priorities for applicants that will
  not use FEOC battery material and "recycling applicants who will not export recovered critical materials
  to a FEOC" (D02 L65, D04 L68); five FEOC grounds (A)-(E), covered nations PRC, Russia, North Korea, Iran
  (D02 L65, D04 L69-70); 30D(d)(7) dates after December 31, 2024 (critical minerals) and after December 31,
  2023 (components) (D02 L68-69, D04 L72).
- Operative tests, same in both unless noted (D02 Section B / D04 Section V):
  - Foreign entity (i)-(iv) (D02 L86-90; D04 L299-303).
  - Government of a foreign country (i)-(iv), including "subnational government", instrumentalities, ruling
    party, "current or former senior foreign political figure" with immediate family "(spouse, parent,
    sibling, child, or a spouse's parent and sibling)" (D02 L94-99; D04 L307-312, restructured (a)-(c)).
  - Subject to the jurisdiction (i) incorporated, domiciled or principal place of business in a covered
    nation; (ii) activity-specific production in a covered nation (D02 L103-105; D04 L316-318).
  - Control: "25% or more of the entity's board seats, voting rights, or equity interest" cumulatively held,
    directly or indirectly (D02 L110); D04 L323 adds "with each metric evaluated independently". Contract
    "effective control" (D02 L111, L117; D04 L324, L330 limits it to a "FEOC contractor, whether the entity
    is a FEOC via 25% control or via jurisdiction"). Five reserved rights (D02 L118-123; D04 L331-336; the
    fifth right reworded, D04 L160).
  - Tiers: a parent holding "50% or more" is treated as equivalent, holdings "fully attributed"; below 50%
    "attributed proportionately" (D02 L114-115; D04 L327-328). Scenarios 1-3, "(25% x 40% = 10%)"
    (D02 L191-196; D04 L259-268, voting rights only).
  - Jurisdiction-only FEOCs: subsidiaries "not automatically" FEOCs (D02 L166, L173-175; D04 L236); their
    holdings are not factored into the 25% test (D02 L189; D04 L257).
- Only in D04 (clarifications in comment responses and section III):
  - 84 comment submissions, "Forty-two--half" anonymous; meetings with Korea, Chile, Australia (L83-84).
  - U.S.-headquartered company operating in a covered nation: not a foreign entity unless organized there;
    such operations are a FEOC that does not "flow back" (L94-95).
  - National plus local SOE holdings combine toward 25% (L110).
  - PRC senior-figure categories (a)-(d): current and former members of the Central Committee, Politburo
    Standing Committee, Politburo, National People's Congress, Provincial Party Congresses and the national
    CPPCC; "current but not former members of local or provincial CPPCCs" (L116, L219). D02 L149 lists
    "current members of Chinese People's Political Consultative Conference" and current and former members
    of four bodies including the "National Party Congress".
  - Metrics not combined: 20% voting, 10% equity, 15% board seats gives 20%, "not ... 45%" (L131, L245).
  - Voting rights mean owners' voting rights; "the value of a board seat to equal the value of its voting
    power on the board"; equity includes contingent interests (L134-138, L255).
  - 50-50 joint venture with a FEOC member "would be considered to be a FEOC"; below 25% only a contract
    giving effective control counts (L150). Read beside scenario 3 this is the one internal tension found:
    a FEOC holding 40% of an entity is not enough in scenario 3 (L263-268).
  - Declined: FEOC list (L170-171), pre-review of contracts (L173), all subsidiaries as FEOCs (L123-124),
    investment-based control (L126, L243). Treasury's final 30D regulations "published elsewhere in this
    issue" (L107); Treasury "has incorporated DOE's FEOC guidance into its 30D rule" (L186).
  - Determination authority: D02 "DOE intends to promulgate separate regulations" (L70, L209) vs D04 "DOE may
    decide to initiate a separate rulemaking" and "has not exercised this authority, as of this date" (L71, L74).
- No "30%" is printed in D04; "25%" first at character 16,753 of the docs/ file, "20%" at 23,629, "40%" at
  70,277. D02 has no statement on valuing board seats or on combining metrics.

## D03 - TVA, Kingston Fossil Plant Retirement Environmental Impact Statement; Record of decision

- Source: text/D03.txt (docs/fr_2024_07411.txt) | FR pages 24557-24565 (L6; markers 24558-24565).
- Written or submitted by: Tennessee Valley Authority (L11, L15). Signer "Jeff Lyash, President & Chief
  Executive Officer, Tennessee Valley Authority." (L227-228). Contact Brittany Kunkle, "NEPA Compliance
  Specialist", "865-632-6470" (L28). EPA, FERC, FWS, ETNG and others are named, not authors.
- Type, date, edition: Notices section; "ACTION: Record of decision." (L17). Published "Monday, April 8,
  2024" (L3, L5); 89 FR, Number 68; "FR Doc No: 2024-07411" (L7); "Dated: April 2, 2024." (L226);
  "Filed 4-5-24; 8:45 am" (L229); "BILLING CODE 8120-08-P" (L230); "Authority: 40 CFR 1505.2." (L224).
  No docket number or RIN printed.
- Period covered: planning horizon. KIF retirement "by the end of 2027" (L26, L35, L38, L39, L45, L50,
  L58, L65, L66, L72, L73, L75, L131); "by 2027" (L75, L104, L111); "in 2027" (L61).
- Entities and aliases: Kingston Fossil Plant = "KIF" (L21) = "the KIF Plant" (L38); "Kingston
  Reservation" (L35); "CC/aero CT Plant" defined L26 ("a single natural gas-fired combined cycle (CC)
  plant, 16 dual-fuel aeroderivative combustion turbines (aero CTs) and a new switchyard (hereafter the
  CC/aero CT Plant)"); "East Tennessee Natural Gas, LLC (ETNG)" (L26) - printed once as "ENTG" (L90);
  "Ridgeline Expansion Project" (L26); BESS = "battery energy storage system" (L26); FERC (L56);
  "U.S. Fish and Wildlife Service (FWS)" (L90); "U.S. Environmental Protection Agency (EPA)" (L92);
  SHPO (L93); TDEC (L135); NRHP (L93); IRP (L34); ELGs (L37); EJ (L52); SC-GHG (L91); NOA (L24);
  NOI (L57); Sierra Club, Energy Alabama (L115); National Park Service (L116); "2023 Solar Energy
  Industries Association" (L68); Council on Environmental Quality (L30, L91).
- Tables: none in the document. It refers to external "table 2.2-1" (L79) and "table 3.824" (L90) of the Final EIS.
- Capacity, energy and size figures:
  - "summer net generating capacity of 1,298 MW" vs "design capacity (1,700 MW)" (L36) - actual / design.
  - "nine coal-fired units" (L26, L35 and throughout); "built between 1951 and 1955" (L34).
  - Replacement requirement "at least 1,500 MW of firm, dispatchable power" (L39; also L50, L53, L58, L73,
    L131 with "at least"); stated without "at least" as "1,500 MW" at L72, L104, L111.
  - Alternative A components: "16 dual-fuel aeroderivative combustion turbines" (L26) / "16 dual-fueled
    aero CTs" (L53) / "16 dual-fired aeroderivative CTs" (L131); "a 3 to 4 megawatt (MW) solar site"
    (L26; L53, L131, L223) / "3-4 MW of solar" (L74); "a 100 MW lithium-ion battery energy storage system
    (BESS)" (L26; "100 MW BESS" L53, L131; "100 MW of battery storage" L74; "100 MW lithium-ion BESS" L223);
    "a new 161-kilovolt switchyard" (L53; "161-kilovolt system" L39).
  - Alternative B: "1,500 MW of utility-scale solar and 2,200 MW of BESS facilities" (L59); "approximately
    10,950 acres for the solar facilities and up to ... 825 acres for the BESS facilities" (L59-60);
    "multiple (15+) solar generating locations" (L60); "approximately 3.8 million panels, based on the
    projected 10,950 acres required to generate 1,500 MW" (L66); "approximately 5.4 years or greater"
    for a solar interconnection (L61); "approximately 8.4 years" to bring Alternative B resources online
    in the Knoxville area (L61); domestic solar supply chain "3 to ... 5 years" to mature (L67-68).
  - System-wide: "up to 10,000 MW of solar by 2035" (L26, L75); interconnection queue "close to 30,000 MW",
    "Over 15,000 MW of that is solar or solar and storage" (L40).
  - Pipeline: "a new 122-mile natural gas pipeline" (L26) / "approximately 122 miles of new 30-inch
    natural gas pipeline, a 14,600- horsepower electric motor drive compressor station" (L56) /
    "122-mile natural gas pipeline" (L138); adjacent to "line number 3100" (L56).
  - Land: "2,254-acre Kingston Reservation" (L35); Alternative A components "approximately 505 acres" (L54).
  - TVA facts: "153 local power companies serving approximately 10 million people", "an 80,000-square-mile
    region" (L30); IRP "20-year planning period" (L34); "past 10 to 15 years" (L36).
  - Hydrogen: "initially capable of blending 5 percent hydrogen", "at least 30 percent hydrogen by volume" (L223).
  - Carbon goals: "70 percent carbon reduction by 2030", "80 percent reduction by 2035", "net-zero carbon
    reduction by 2050" (L91).
- Dollar figures (all estimates):
  - Alternative A vs No Action, life cycle social cost of GHG, "net savings/benefit, ranges from
    approximately $398 million to $4.34 billion in nominal dollars" (L91) - a range, system-wide basis.
  - "Alternative B reflects an estimated $2.26 billion of SC-GHG savings relative to the No Action
    Alternative, approximately $417 million ... more savings than Alternative A" (L100-104).
    No single-point Alternative A SC-GHG savings figure is printed; only the L91 range and the L100 difference.
  - "Alternative B is estimated to cost approximately $1 billion more than Alternative A in project costs,
    which include capital, transmission, and production costs" (L104), "even accounting for updated
    pricing as a result of the Inflation Reduction Act".
- Alternatives (L52-61): No Action; Alternative A (Preferred; adopted); Alternative B. "TVA assessed in
  detail a No Action Alternative and two action alternatives" (L50). A "blended alternative" is named and
  rejected as "not a viable alternative" (L61). "No clear environmentally preferred alternative emerges
  from the comparison." (L111).
- Component lists differ by passage: SUMMARY (L26) lists CC plant, 16 aero CTs, new switchyard, solar
  site, BESS, "new transmission line infrastructure", plus the Ridgeline pipeline; Alternative A
  description (L53) lists CC plant, 16 aero CTs, solar, BESS, 161-kilovolt switchyard; the Decision
  sentence (L131) lists CC plant, 16 aero CTs, solar site, BESS only.
- Other lists:
  - Tennessee Valley region, 7 states: "Tennessee and parts of Virginia, North Carolina, Georgia, Alabama,
    Mississippi, and Kentucky" (L30).
  - Pipeline counties, 8: "Trousdale, Smith, Jackson, Putnam, Overton, Fentress, Morgan, and Roane
    counties, Tennessee" (L57).
  - Transmission upgrades: "four transmission lines on the Eastern Transmission Corridor and one
    transmission line on the Western Transmission Corridor" (L55).
  - Bats, 3: "the gray bat, Indiana bat, or northern long-eared bat" (L90).
  - Renewable queue locations: "West Tennessee, North Alabama, and North Mississippi" (L45).
  - Archaeology: "the only recorded National Register of Historic Places (NRHP)-eligible archaeological
    site within the CC/aero CT Plant site" (L93, TVA actions) vs "seven NRHP-eligible archaeological
    sites that require further evaluation" (L96, ETNG actions) - different actors and areas.
  - Resource-effect lists per alternative: L83-84 (retirement/demolition), L85-91 (Alt A TVA), L95-97
    (ETNG), L98-99 (Alt B), L110 (comparison of A and B).
  - Mitigation commitments (L140-218), 12 headed groups; [cir] bullets counted from the text:
    Soils 3 (L141-143); Water Resources 6 (L145-150) with 5 [ssquf] sub-items (L151-155); Biological
    Resources 7 (L157, L158, L159, L166, L167, L169, L170) with 3 [ssquf] sub-items (L160-161);
    Cultural Resources 4 (L172-175); Waste Management 1 (L177); Public and Occupational Health and
    Safety 1 (L179); Transportation 3 (L181-183); Noise 1 (L185); Visual 1 (L187); Air Quality and GHG
    Emissions 9 (L189-198); Blasting/Explosives 4 (L200, L205, L206, L207) plus an unbulleted sentence
    (L208); Floodplains 8 (L210-218). ETNG measures 3 (L220-222). "non-routine mitigation measures" (L223).
  - Mitigation thresholds: "30-meter buffers" (L172); "at least one-half mile" (L174); "at least 100 feet
    in width" (L175); "between November 15 and March 31" (L167); "within 0.5 miles of known bat
    hibernacula" (L168); "no soil rutting of 12 inches or more" (L155); "maximum sulfur content in diesel
    fuel of 15 ppm" (L194); "one foot above the 100-year flood elevation" (L215, L216); "above elevation
    750" (L218); "24-hour security" (L207).
- Dates, deadlines and FR citations:
  - Final EIS NOA "published in the Federal Register on February 23, 2024" (L26; again L119 with "(89 FR 13717)").
  - Scoping: "30-day public scoping period on June 15, 2021 ... (85 FR 31780, June 15, 2021)" (L115);
    "live virtual public scoping meeting on June 29, 2021" (L115).
  - Draft EIS NOA "May 19, 2023, initiating a 45-day public comment period that ended on July 3, 2023
    (88 FR 32215, May 19, 2023)" (L117).
  - FERC NOI "issued by FERC on September 22, 2023 (88 FR 65383), and was amended on December 18, 2023
    (89 FR 6108)" (L57); "FERC Docket No. CP23-516-000 and amended CP23-516-001" (L57).
  - "Revised Biological Assessment ... filed March 11, 2024 (FERC Docket No. CP23-516, accession no.
    20240311-5269)" (L90); "Karst Hazards Mitigation Guidance Plan submitted to FERC on July 18, 2023" (L220);
    "updated programmatic consultation (May 2023)" (L169).
  - "On March 25, 2024, EPA submitted comments in accordance with section 309 of the Clean Air Act and
    section 102(2)(C) of NEPA" (L121); "additional public comments in March 2024" (L120).
  - "In 2019, TVA completed its Integrated Resource Plan (IRP)" (L34); "2020 Effluent Limitation Guidelines" (L37);
    "40 Code of Federal Regulations (CFR) 1500 through 1508, as updated April 20, 2022" (L30); "2008 Ash Spill" (L145).
- Comment counts (actuals): "approximately 56 scoping comments, a form letter from Sierra Club with 583
  signatories, and a petition from Energy Alabama with eight signatories" (L115); "602 comments on the
  Draft EIS, with one form letter containing approximately 4,350 signatures" (L118); after the Final EIS
  "several hundred comment submissions" (L119) - no number.
- Statutes and regulations cited: NEPA "42 U.S. Code [U.S.C.] 4321 et seq." (L30); "18 CFR 1318" (L30);
  "40 CFR 1505.2(b)" (L126); Clean Water Act "CWA 316(a)" and "CWA 316(b)" (L82), "CWA section 404", "CWA
  section 401" (L147); "section 7 of the Natural Gas Act" (L57, L97); "section 7 of the Endangered Species
  Act" (L90); "section 106 of the National Historic Preservation Act" (L93); "section 111 of the Clean Air
  Act" (L92); "section 309 of the Clean Air Act" (L121); "Inflation Reduction Act" (L67, L104); "Invasive
  Species Executive Order 13112" (L157); "18 CFR part 380", "49 CFR part 192" (L138); "40 CFR part ... 85",
  "40 CFR part 1039" (L193-194); "40 CFR part 60, subpart KKKK (NOX and SO2), and subpart TTTT (GHGs)"
  (L196); "TDEC Air Pollution Control Rule 1200-3-8" (L192).
- Batteries: lithium-ion appears only at L26 and L223 (the 100 MW BESS). "battery storage" also L26, L74,
  L223; Alternative B BESS L59-60. Nothing on battery recycling, battery chemistry beyond "lithium-ion",
  or critical minerals; "recycling" appears once, about demolition debris ("transport to a recycling
  facility or landfill" L135).
- Funding statutes: none for the project. "TVA receives no taxpayer funding and derives virtually all its
  revenue from the sale of electricity." (L30). The Infrastructure Investment and Jobs Act / Bipartisan
  Infrastructure Law is not mentioned. The Inflation Reduction Act appears twice, about the solar
  supply chain (L67) and Alternative B pricing (L104). "does not include tax incentives for carbon
  capture and storage" (L92).
- Hedged or conditional claims:
  - Gas supply "by ETNG's Ridgeline Expansion Project, if approved by the Federal Energy Regulatory
    Commission (FERC)" (L56); "FERC will issue an EIS with its findings prior to making a decision on
    the Ridgeline Expansion Project" (L97) - the pipeline was not yet approved; ETNG verbs are "would".
  - "may affect but are not likely to adversely affect" (L90) - a formal determination phrase.
  - "may increase environmental, economic, and reliability risks" (L34); "is likely to result in
    cascading delays" (L38); "could require potentially significant rate increases" (L52); "it is
    projected that it will take 3 to ... 5 years" (L67-68); hydrogen capability conditional on "once a
    reliable hydrogen source is identified" (L223).
  - Firm: "TVA has decided to implement the Preferred Alternative identified in the Final EIS:
    Alternative A" (L131); "EPA has served as a cooperating agency for this EIS" (L116).
- Operative definitions, rules and scope exceptions: purpose-and-need test "mature, proven technologies,
  capable of being constructed, and operating by the end of 2027" (L50); project costs "include capital,
  transmission, and production costs" (L104); demolition in floodplains "considered temporary uses" (L83).
- Amendments or contradictions (recorded neutrally; the document gives no precedence):
  - Coal-fleet year: "retiring TVA's entire coal fleet by 2035" and "planning assumptions for the
    retirement of all TVA coal units by 2033" in the same paragraph (L35); "phased 2035 coal fleet
    retirement plan" (L38).
  - Citation oddities as printed: "(85 FR 31780, June 15, 2021)" (L115) while other 2021 items in the
    bundle carry volume 86 (D05 L229, L307); "amended on December 18, 2023 (89 FR 6108)" (L57) while
    other 2023 items carry volume 88. Not resolvable from the bundle.
  - "ENTG" (L90) vs "ETNG" elsewhere.
- Notes / passages not fully interpretable: "TVA's review of the 2023 Solar Energy Industries Association
  affirms this finding" (L68) lacks a noun (which publication is not stated). "table 3.824" (L90) is
  printed that way. The L9 rule line is doubled.
- Coverage: FULL. Read L1-231 in one pass (every line). Nothing remains unread.

## D05 - Department of the Treasury, Semiannual Regulatory Agenda

- Source: text/D05.txt (docs/fr_2024_16461.txt) | header says "[Pages 66858-66864]" (L6); page markers
  run 66857-66864 (L9 "[[Page 66857]]" is the Part cover page, outside the header range).
- Written or submitted by: Department of the Treasury (L21, L34, L40). Signer "Michael Briskin, Deputy
  Assistant General Counsel for General Law and Regulation." (L59-60). No "Dated:" line is printed.
  Bureaus with entries: Financial Crimes Enforcement Network (FINCEN / FinCEN), "Customs Revenue Function
  (CUSTOMS)", Internal Revenue Service (IRS).
- Type, date, edition: "ACTION: Semiannual Regulatory Agenda." (L42); "Part XIII" (L19); "31 CFR Subtitles
  A and B" (L36); published "Friday, August 16, 2024" (L3, L5); 89 FR, Number 159; section "[Unknown
  Section]" (L5); "FR Doc No: 2024-16461" (L7); "Filed 8-15-24; 8:45 am" and "BILLING CODE 4810-01-P;
  4810-02-P; 9111-14-P" (L555). One edition only; no other agenda edition is in the bundle.
- Scope rule (what is printed): "Treasury's printed agenda entries include only: (1) Rules that are in the
  regulatory flexibility agenda ... because they are likely to have a significant economic impact on a
  substantial number of small entities; and (2) Rules that have been identified for periodic review under
  ... section 610 of the Regulatory Flexibility Act." (L52-55). "Printing of these entries is limited to
  fields that contain information required by the Regulatory Flexibility Act's Agenda requirements" (L56).
  Authority: "Regulatory Flexibility Act and Executive Order 12866" (L46); "5 U.S.C. 602" (L52).
- Period covered: timetable dates run from "04/04/16" (L271) to "02/00/26" (L340). Dates of the form
  "MM/00/YY" appear for planned actions; the document does not explain the "00" day. Calendar dates only.
- Tables:
  - Index tables L62-155, one per bureau and stage; columns "Sequence No.", "Title", "Regulation
    Identifier No." They are collapsed onto run-on lines (title words and RIN interleaved); every title
    and RIN is restated cleanly in the detailed entries L163-553, which were used to read them.
  - Each detailed entry has a "Timetable:" or "Completed:" table with columns "Action" (or "Reason"),
    "Date", "FR Cite". No units; dates are MM/DD/YY.
- Entry universe: 21 entries, sequence 177-197. By bureau: FinCEN 12 (177-188), Customs Revenue
  Function 2 (189-190), IRS 7 (191-197). By stage: Proposed Rule 5 (177, 178, 179, 189, 191); Final Rule 4
  (180, 181, 190, 192); Long-Term Actions 5 (182-186); Completed Actions 7 (187, 188, 193-197).
  "Regulatory Flexibility Analysis Required: Yes" for every entry except 191 ("No", L445).

| Seq | Title (detailed heading) | RIN | Bureau, stage | Dated actions as printed | Lines |
| --- | --- | --- | --- | --- | --- |
| 177 | Section 6101. Establishment of National Exam and Supervision Priorities | 1506-AB52 | FinCEN, Proposed | NPRM 07/00/24; NPRM Comment Period End 09/00/24 (no FR cites) | L163-177 |
| 178 | Revisions to Customer Due Diligence Requirements for Financial Institutions | 1506-AB60 | FinCEN, Proposed | NPRM 10/00/24; NPRM Comment Period End 12/00/24 | L179-193 |
| 179 | Investment Adviser Customer Identification Program Requirements for Registered Investment Advisers and Exempt Reporting Advisers | 1506-AB66 | FinCEN, Proposed | NPRM 05/21/24 89 FR 44571; NPRM Comment Period End 07/22/24; Reviewing Comments 08/00/24 | L195-213 |
| 180 | Residential Real Estate Transaction Reports and Records | 1506-AB54 | FinCEN, Final | ANPRM 12/08/21 86 FR 69589; ANPRM Comment Period End 02/07/22; NPRM 02/16/24 89 FR 12424; NPRM Comment Period End 04/16/24; Final Action 08/00/24 | L221-236 |
| 181 | Anti-Money Laundering Program and Suspicious Activity Report Filing Requirements for Investment Advisers | 1506-AB58 | FinCEN, Final | NPRM 02/15/24 89 FR 12108; NPRM Comment Period End 04/15/24; Final Action 08/00/24 | L238-252 |
| 182 | Amendments to the Definition of Broker or Dealer in Securities (Crowd Funding) | 1506-AB36 | FinCEN, Long-Term | NPRM 04/04/16 81 FR 19086; NPRM Comment Period End 06/03/16; Final Action To Be Determined | L260-277 |
| 183 | Clarification of the Requirement To Collect, Retain, and Transmit Information on Transactions Involving Convertible Virtual Currencies and Digital Assets With Legal Tender Status | 1506-AB41 | FinCEN, Long-Term | NPRM 10/27/20 85 FR 68005; NPRM Comment Period End 11/27/20; Second NPRM 07/00/25; Second NPRM Comment Period End 09/00/25 | L279-294 |
| 184 | Section 6110. Bank Secrecy Act Application to Dealers in Antiquities and Assessment of Bank Secrecy Act Application to Dealers in Arts | 1506-AB50 | FinCEN, Long-Term | ANPRM 09/24/21 86 FR 53021; ANPRM Comment Period End 10/25/21; NPRM To Be Determined | L298-313 |
| 185 | Section 6212. Pilot Program on Sharing of Information Related to Suspicious Activity Reports Within a Financial Group | 1506-AB51 | FinCEN, Long-Term | NPRM 01/25/22 87 FR 3719; NPRM Comment Period End 03/28/22; Final Rule To Be Determined | L315-329 |
| 186 | Commercial Real Estate Transaction Reports and Records | 1506-AB61 | FinCEN, Long-Term | NPRM 12/00/25; NPRM Comment Period End 02/00/26 | L331-345 |
| 187 | Requirements for Certain Transactions Involving Convertible Virtual Currency or Digital Assets | 1506-AB47 | FinCEN, Completed | Withdrawn 04/12/24 (row printed twice, L362-363) | L353-368 |
| 188 | Beneficial Ownership Information Access and Safeguards | 1506-AB59 | FinCEN, Completed | Final Action 12/22/23 88 FR 88732 | L370-382 |
| 189 | Entry of Low-Value Shipments | 1515-AE84 | Customs, Proposed | NPRM 07/00/24 | L390-406 |
| 190 | Enforcement of Copyrights and the Digital Millennium Copyright Act | 1515-AE26 | Customs, Final | NPRM 10/16/19 84 FR 55251; NPRM Comment Period End 12/16/19; Final Rule 07/00/24 | L414-427 |
| 191 | Base Erosion and Anti-Abuse Tax (Section 610 Review) | 1545-BR20 | IRS, Proposed | NPRM 11/00/24 | L435-447 |
| 192 | Mental Health Parity and Addiction Equity Act and the Consolidated Appropriations Act, 2021 | 1545-BQ29 | IRS, Final | NPRM 08/03/23 88 FR 51552; NPRM Comment Period Extended 09/28/23 88 FR 66728; NPRM Comment Period Extended End 10/17/23; Final Action 07/00/24 | L455-468 |
| 193 | Section 30D Clean Vehicle Credit Regulations | 1545-BQ52 | IRS, Completed | Public Hearing 01/31/24 89 FR 1858; Final Action 05/06/24 89 FR 37706; Final Action Effective 07/05/24 | L476-493 |
| 194 | Elective Payment of Applicable Credits Under Section 6417 | 1545-BQ63 | IRS, Completed | Final Action (TD 9988) 03/11/24 89 FR 17546; Correction 04/16/24 89 FR 26786 | L495-504 |
| 195 | Transfer of Certain Credits Under Section 6418 | 1545-BQ64 | IRS, Completed | Final Action 04/30/24 89 FR 34770; Final Action Effective 07/01/24 | L506-516 |
| 196 | Transfer Provisions of Sections 30D and 25E | 1545-BQ86 | IRS, Completed | NPRM 10/10/23 88 FR 70310; Public Hearing 01/31/24 (no cite); Final Action 05/06/24 89 FR 37706 | L518-531 |
| 197 | Section 30D Foreign Entity of Concern | 1545-BQ99 | IRS, Completed | NPRM 12/04/23 88 FR 84098; NPRM Comment Period End 01/18/24; Public Hearing 01/31/24 (no cite); Final Action 05/06/24 89 FR 37706 | L533-553 |

- Other figures and rules inside abstracts:
  - 189: "low-value shipments not exceeding $800" (L393); synthetic opioids "such as fentanyl" (L393).
  - 184: proposed rules "within 360 days of enactment of the AML Act" (L303). 185: rules "within one year
    of enactment of the AML Act" (L319). 182 note: "it replaces RINs 1506-AB24 and 1506-AB29" (L266).
  - 180: "proposed February 16, 2024" (L225). 181: "proposed February 15, 2024" (L242). 188: final rule
    issued "on December 22, 2023" (L374). 183 is joint with "The Board of Governors of the Federal Reserve
    System" (L283).
  - Statutes named: Anti-Money Laundering Act of 2020 sections 6101(b) (L167), 6110 (L302), 6212 (L319);
    Corporate Transparency Act sections 6403(d) (L183), 6403(a) (L374); Securities Act of 1933 section
    4(a)(6) (L264); 19 U.S.C. 1321 (L392); Pub. L. 114-125 (L416); 26 U.S.C. 59A (L437); Pub. L. 116-260,
    Pub. L. 110-343 (L457); Inflation Reduction Act of 2022 sections 13801(a) (L497), 13801(b) (L508).
- Section 30D clean vehicle credit / foreign entity of concern (entries 193, 196, 197):
  - 193 abstract (L478-482): "Section 13401 of the IRA amends 30D(b) of the Code to, among other things,
    provide a maximum credit of $7,500 per vehicle, consisting of $3,750 in the case of a vehicle that
    meets certain critical minerals requirements and $3,750 in the case of a vehicle that meets certain
    battery components requirements." Requirements "are applicable to vehicles placed in service after
    the date on which the Secretary of the Treasury or her delegate issues proposed guidance" (L478).
    Defined-term lists (each term is wrapped in double-backtick / double-apostrophe quote marks in the
    source, omitted here): extracted, processed, recycled, free trade agreement (4 terms, L478, after
    "These clarifications include definitions of terms such as"); final assembly, North America,
    manufacturer's suggested retail price, placed in service (4 terms, L482, same lead-in). Both lists
    are open ("such as"). Vehicle classes "vans, sport utility vehicles, pickup trucks, or other vehicles"
    (L482). "IRS Notice 2023-1, as modified by IRS Notice 2023-16" (L482). Legal authority "26 U.S.C. 7805;
    26 U.S.C. 30D" (L478). Contacts Maggie M. Stehn and Rika Valdman (L490-491).
  - 196 abstract (L521-523): "Section 30D(g)(1)"; "Section 25E(f)"; "On October 5, 2022, Notice 2022-46 was
    published in I.R.B. 2022-43" (L522); "On December 8, 2022, Revenue Procedure 2022-42 was published in
    I.R.B. 2022-52" (L523). Legal authority "26 U.S.C. 25E; 26 U.S.C. 30D; 26 U.S.C. 6213; 26 U.S.C. 7805" (L520).
  - 197 abstract (L535-540): "section 30D(e)(3)"; "Section 30D(e)(1)(B) and 30D(e)(2)(B) provide applicable
    percentage requirements ... beginning with vehicles placed in service before January 1, 2024" (L535).
    Exclusion rule (L536-537): "Section 30D(d)(7) provides that for purposes of this section, the term
    new clean vehicle shall not include: (1) any vehicle placed in service after December 31, 2024, with
    respect to which any of the applicable critical minerals contained in the battery of such vehicle
    ... were extracted, processed, or recycled by a foreign entity of concern (as defined in section
    40207(a)(5) of the Infrastructure Investment and Jobs Act (42 U.S.C. ... 18741(a)(5))), or any vehicle
    placed in service after December 31, 2023, with respect to which any of the components contained in
    the battery of such vehicle ... were manufactured or assembled by a foreign entity of concern (as so
    defined)." "On April 17, 2023, proposed regulations were published in the Federal Register, 88 FR
    23370" (L538). Contact "Rika Valdman, Senior Technician Reviewer" (L551).
  - "foreign entity of concern" appears at L154 (index), L533 (heading), L536, L537, L540. D05 does not
    define the term itself, does not name any excluded entity or country, and does not mention DOE.
- Forecasts vs actuals: planned (MM/00/YY or "To Be Determined") actions are in 177, 178, 179 (08/00/24),
  180, 181, 182, 183, 184, 185, 186, 189, 190, 191, 192. Fully dated completed actions are in 187, 188, 193-197.
- Hedged / proposed-vs-final wording: entries 193 and 197 sit under "Completed Actions" with a Final
  Action row, yet their abstracts speak of proposals: "The proposed regulations provide clarity" (L478);
  "These proposed regulations will provide guidance regarding foreign entity of concern" (L540).
- Amendments or contradictions (recorded neutrally; no precedence stated):
  - 197 abstract: "intend to publish proposed regulations and a revenue procedure regarding vehicle
    transfer elections provided for in sections 25E(f) and 30D(g). As of the date of preparing this RIN
    request, such proposed regulations and revenue procedure have not yet been published." (L539), while
    entry 196 (same subject) prints "NPRM 10/10/23 88 FR 70310" (L527).
  - The April 17, 2023 proposal "88 FR 23370" is in 197's abstract (L538) but in no timetable; entry
    193's table has no NPRM row.
  - Final Action "05/06/24 89 FR 37706" is printed for three entries (193 L486, 196 L527, 197 L548);
    only 193 prints "Final Action Effective 07/05/24" (L486). Public Hearing 01/31/24 carries the cite
    "89 FR 1858" only in 193.
  - 187: the "Withdrawn 04/12/24" row is duplicated (L362-363).
- Notes / passages not fully interpretable: the run-on index tables (L62-155) cannot be parsed column by
  column from the text alone; the "00" day convention is unexplained; "her delegate" (L478).
- Coverage: FULL. Read L1-556 in one pass (every line). Nothing remains unread.

## D06 - EPA, Lead Wheel Weights; Petition for Rulemaking Under TSCA; Decision Not To Proceed With a Rulemaking

- Source: text/D06.txt (docs/fr_2024_30401.txt) | FR pages 104486-104493 (L6; markers 104487-104493).
- Written or submitted by: Environmental Protection Agency (L11, L19). Signer "Michal Freedhoff, Assistant
  Administrator, Office of Chemical Safety and Pollution Prevention." (L238-239). Technical contact "Sean
  Duenser, Existing Chemicals Risk Management Division (7404M), Office of Pollution Prevention and
  Toxics", "(202) 343-9157" (L32). Petitioners and commenters are named parties, not authors.
- Type, date, edition: Proposed Rules section; "ACTION: Petition; reasons for Agency response." (L21);
  "40 CFR Chapter I" (L13); "[EPA-HQ-OPPT-2024-0085; FRL-5398-06-OCSPP] RIN 2070-AJ64" (L15); published
  "Monday, December 23, 2024" (L3, L5); 89 FR, Number 246; "FR Doc No: 2024-30401" (L7); "DATES: This
  decision is effective December 23, 2024." (L27); "Dated: December 16, 2024." (L237); "Filed 12-20-24;
  8:45 am" (L240); "BILLING CODE 6560-50-P" (L241); "Authority: 15 U.S.C. 2601 et seq." (L235).
- Timeline (as printed):
  - 2000: Albuquerque loss-rate study "published" (L147; Ref. 18 "2000 Oct", L220).
  - "In May 2009, Petitioners submitted a TSCA section 21 petition" (L102); Ref. 1 "May 28, 2009" (L199).
    Summary form: "a citizen petition filed with the Agency in 2009" (L25, L74).
  - "EPA requested public comment on the petition in July 2009 (Ref. 7)" (L102); Ref. 7 "74 FR 34342, July
    15, 2009 (FRL-8424-7)" (L207).
  - "granted the petition on August 26, 2009 (Ref. 8)" (L102; repeated L107; Ref. 8 L208).
  - "May 14, 2021" Ninth Circuit opinion on dust-lead hazard standards (L178).
  - Canada: text says prohibited "in February 2024 (Ref. 14)" (L124); Ref. 14 reads "February 3, 2023"
    with URL ".../2023/2023-02-15/..." (L215).
  - "88 FR 50444, August 1, 2023 (FRL-8524-01-OCSPP)" dust-lead proposed rule (L176, Ref. 10 L211).
  - Mandamus: "In 2023" (L25, L74); "In August 2023" (L104); "August 2023 mandamus petition" (L172); Ref. 2
    "August 22, 2023" (L200). Case "Ecology Center, et al. v. U.S. EPA, No. ... 23-70158 (9th Cir.)" (L74-75).
    "A joint motion to dismiss the petition for writ of mandamus was filed and granted." (L104) - no date.
  - "EPA published for comment a proposed settlement agreement with the petitioners in March 2024" (L75).
  - ANPRM: "issued in April 2024" (L25); "In April 2024, EPA published an ANPRM" (L81); "EPA issued an
    ANPRM on April 3, 2024" (L112); Ref. 3 "89 FR 22972, April 3, 2024 (FRL-5398-05-OCSPP)" (L201).
  - "89 FR 37028, May 3, 2024 (FRL-8529-02-OCSPP)" risk-evaluation procedures rule (Ref. 24, L230).
  - Comments in the reference list dated "May 9, 2024" (Refs. 5, 13, 15, 16) and "May 10, 2024" (Refs. 12, 17).
    "the 30-day public comment period for the ANPRM" (L167). No ANPRM comment-deadline date is printed.
  - "Abt. Memo ... July 23, 2024" (Ref. 6, L205-206).
  - "EPA and the Petitioners then entered into a settlement agreement in September 2024" (L75).
  - "89 FR 89416, November 12, 2024 (FRL-8524-02-OCSPP)" dust-lead final rule (L178).
  - "Technical Support Document for Lead Wheel Weights. ... December 2024" (Ref. 4, L202-203).
  - Court-linked obligation, no deadline printed: "EPA was required to either (1) sign a proposed rule
    and request publication by the Office of the Federal Register, or (2) request publication in the
    Federal Register of a determination not to proceed with regulating lead wheel weights." (L104).
- Comment counts (two different statements of what was "received"):
  - "The Agency received 128 comments providing input on whether to move forward" (L82).
  - "EPA received 21,297 comments, of which 128 were posted to the docket, including 8 unique comments
    from Petitioners; mass mailers; comments from the recycling, metal, and automotive industries; and a
    scientific organization (Ref. 11)." (L112). The breakdown gives a number only for the 8 petitioner
    comments; the other categories are unnumbered.
- State bans: "Nine States in the United States have banned the sale, distribution, and/or use of lead
  wheel weights." (L93); "nine States" also L124, L130; "Nine U.S. States have banned lead wheel weights
  since this loss rate study was conducted" (L147). Only one state is named: "such as Maine" (L124).
  "All State bans took place after the 2009 petition was granted." (L124). Canada: "manufacturing or
  importing wheel weights containing more than 0.1% lead by weight" (L124).
- Lead and exposure quantities:
  - "1.6 million pounds of lead is lost when wheel weights fall off during normal driving conditions"
    (L106) - printed inside a petitioner claim: "Petitioners also claimed that ... given EPA acknowledged that".
  - Lead content "from the over 90% ... to the current 0.1%" (L122) - a commenter's statement (Ref. 5).
  - Baseline "100.06 [mu]g/g and 79.16 [mu]g/g respectively" (soil, dust); wheel weights "an additional
    3.02 [mu]g/g and 1.15 [mu]g/g respectively in the near-roadway scenario" (L141).
  - IQ: "0.026 IQ points at the higher-end" (L141, L143; "0.026 points" L163) vs baseline "2.61 IQ points"
    (L141); prose comparisons "over 100 times higher" (L141) and "added approximately 1 percent to the IQ
    loss already attributable to exposure to other sources of lead" (L163).
  - Blood lead: "0.012 [mu]g/ dL at the higher end" and "a less than 1% estimated increase" (L143);
    NTP "below 5 [micro]g/dL" (L119). Ages: "children up to age 7" (L141); "ages 1 through 7" (L143);
    "a 2-year-old child" (L141); "At ages 2 and 7" (L163). "All Ages Lead Model (AALM) version 3.0" (L143).
  - Loss rate "approximately five hundred 1-ounce lead wheel weights lost per mile of roadway per year"
    (L147); "slightly more than 257 1- ounce lead wheel weights simulated to enter the 1-mile stretch of
    stream" (L152); "maximum time ... between street cleaning events (6 months)" (L152); "1-mile roadway",
    "1-day rainfall event", "six-lane road in Albuquerque, New Mexico" (L147).
  - Acute: "0.0000164 [mu]g/L (less than 0.1 parts per trillion)" (L153, L154) vs "65 [mu]g/L" (L153, L154);
    "50 cubic feet per second", "100% of a lead wheel weight dissolves per year", "only two rainfall
    events per year" (L153).
  - Chronic: "0.0009 [mu]g/L (less than 1 part per trillion)"; CCC "ranges from 1.3 to 7.7 [mu]g/L
    depending on water hardness with a default value at 2.5 [mu]g/L (corresponding to 100 mg/L hardness
    as CaCO3)" (L156). Restated in other units: "65 parts per billion for acute exposure, and 2.5 parts
    per billion for chronic exposure" (L166); both scenarios "less than 1 part per trillion" (L165).
  - Market: "approximately 95 percent of the new light-duty vehicles in the United States" (L131-135,
    L167) / "approximately 95 percent of new cars sold in the United States" (L147); "one remaining
    domestic manufacturer" (L97; L130 "one remaining lead wheel weight manufacturer"); "multiple importers" (L97).
  - Dust-lead action levels "5 [mu]g/ft\2\, 40 [mu]g/ft\2\, and 100 [mu]g/ft\2\ for floors, window sills,
    and troughs, respectively" (L179). "at least 50 percent of TSCA risk evaluations" from the 2014 Work
    Plan (L189); "a 3-year robust and comprehensive review" (L189); Task Force "comprises 17 Federal
    departments and offices" (L176).
  - All modelled values are EPA estimates from the TSD (Ref. 4); tables "4-8" (L141) and "5-2" (L141) are external.
- Lists:
  - Petitioner groups (L74), 11 organisations plus "one individual": Ecology Center, Sierra Club, Alliance
    for Healthy Homes, Center for Environmental Health, Environmental Health Watch, Coalition to End
    Childhood Lead Poisoning, United Parents Against Lead, Louisiana ACORN, Lead Technicians, Tulane
    University, Drexel School of Public Health.
  - NAICS list (L44-63): 23 printed entries, 22 distinct codes - "Lead die-castings, unfinished,
    manufacturing (NAICS code 331523)" is printed twice (L45, L46).
  - References: 26 numbered items (L199-233).
  - Comment-summary heads a-e (L115, L121, L123, L125, L127).
- Commenter attribution (who said it vs who is mentioned), via the reference numbers:
  - Ref. 5 = Alliance for Automotive Innovation (L204); called "a trade association representing the auto
    industry" (L124) and "an industry group" (L147); named in text L131, L167.
  - Ref. 12 = "Ecology Center et al." (L213) = Petitioners' ANPRM comment.
  - Ref. 13 = "Project TENDR (Targeting Environmental Neuro-Development Risks), The Arc of the U.S." (L214).
  - Ref. 15 = "Steel Manufacturers Association (SMA)" (L216): scrap-stream / electric arc furnace concern (L125).
  - Ref. 16 = "Recycled Materials Association (ReMA)" (L217): existing CAA rules suffice (L126) and the
    economic-value comment about "a recycled material that meets the" ropes "specification" (L128-129;
    the word ropes is in quote marks in the source).
  - Ref. 17 = "Association of Battery Recyclers, Inc. ... (ABR), Battery Council International (BCI), and
    International Lead Association (ILA)" (L218-219): "recycling facilities are heavily regulated under
    Federal environmental statutes" (L128).
- Lead-acid batteries and recycling: the string "lead-acid" does not occur in D06, and "batter" occurs
  only in the two organisation names of Ref. 17 (L218-219). Recycling statements: "processing (including
  recycling)" (L81, L84); "comments from the recycling, metal, and automotive industries" (L112); heads d
  and e (L125-129); removal from "end-of-life vehicles (ELVs) by automotive dismantlers and metal
  shredding facilities" (L126).
- Statutes and regulations cited: "TSCA section 21, 15 U.S.C. 2620" (L69); "TSCA sections 4, 6, or 8 or an
  order under TSCA sections 4 or 5(e) through (f)" (L69); section 6(a) (L69, L181); section 6(b) (L84, L181-182);
  "subsection (b)(4)(A)" (L181); "section 6(b)(4)(F)" (L182, L193); "TSCA section 18" (L77); "TSCA section
  26(h)" (L193); "TSCA Title IV" and "15 U.S.C. 2681(10)" (L177-178); "Title X" "(Pub. L. 102-550)" (L177);
  "40 CFR part 63, subparts EEEEE (Iron and Steel Foundries), YYYYY (Electric Arc Furnace Area Sources),
  and ZZZZZ (Iron and Steel Foundries Area Sources)" (L126); "40 CFR 745.83 and 745.223" (L179);
  "40 CFR 702.5(c)(2)" (L189).
- Hedged or attributed claims:
  - "lead wheel weights may still be used for wheel balancing in auto repair and maintenance of vehicles
    post-sale" (L97): "may" attaches to continued use.
  - "the Agency preliminarily found that risk associated with residential exposure is lower than
    previously believed" (L83).
  - "EPA expects that this assumption is an overestimate" (L147); "actual average lead concentrations ...
    are likely lower" (L156); "EPA may also need to develop a peer-reviewed threshold" (L188).
  - "The commenter stated that this approach appears to have mitigated the potential for unreasonable
    risk" (L122): a commenter's view, hedged with "appears".
  - Firm: "has decided not to proceed with the development of a proposed rule" (L25); "This action serves
    as EPA's final decision in response to the 2009 petition." (L77); "prioritization and risk evaluation
    for lead and lead compounds have not yet been initiated (Ref. 26)" (L189).
- Operative definitions, rules and scope exceptions: "This action is limited to lead for lead wheel
  weights." (L74); "this action will not have a preemptive effect on State actions under TSCA section 18"
  (L77); occupational exposure not assessed here (L188); "other health effects ... were not evaluated"
  (L143); wheel weights definition (L91); DLAL definition (L179).
- Amendments or contradictions (recorded neutrally; no precedence stated):
  - Comments "received": 128 (L82) vs 21,297 with 128 posted (L112).
  - Canada prohibition "in February 2024 (Ref. 14)" (L124) vs Ref. 14 dated "February 3, 2023" (L215).
  - Action sequence, not a conflict: the 2009 petition was granted ("which EPA granted" L25; L102); an
    ANPRM followed in April 2024; this document is the "decision not to regulate" (L73). No proposed or
    final wheel-weight rule was issued.
  - Proposed vs final (dust-lead rule, a different rulemaking): proposed "88 FR 50444, August 1, 2023"
    (L176) and final "89 FR 89416, November 12, 2024" (L178), both described in D06.
- Notes: the duplicated NAICS line (L45-46). FR page break splits "(Ref. ... 5)" etc. across lines.
- Coverage: FULL. Read L1-242 in one pass (every line). Nothing remains unread.

## D07 - EPA, Significant New Use Rules on Certain Chemical Substances (26-2); Proposed rule

- Source: text/D07.txt (docs/fr_2026_08012.txt) | FR pages 22075-22083 (L6; markers 22076-22083).
- Written or submitted by: Environmental Protection Agency (L11, L19). Signer "Mary Elissa Reaves,
  Director, Office of Pollution Prevention and Toxics." (L281-282). Contacts: "James Yan, New Chemicals
  Division (7405M)", "(202) 564-2138" (L33); "William Wysong", "(202) 564-4163" (L35-40); TSCA hotline (L41).
- Type, date, edition: Proposed Rules section; "ACTION: Proposed rule." (L21); "40 CFR Part 721" (L13);
  "[EPA-HQ-OPPT-2025-2932; FRL-13085-01-OCSPP] RIN 2070-AB27" (L15); batch "(26-2)" (L17); published
  "Friday, April 24, 2026" (L3, L5); 91 FR, Number 79; "FR Doc No: 2026-08012" (L7); "Dated: April 21,
  2026." (L280); "Filed 4-23-26; 8:45 am" (L364); "BILLING CODE 6560-50-P" (L365).
- Deadlines and dates:
  - "Comments must be received on or before May 26, 2026." (L27).
  - Export: "any persons who export or intend to export ... on or after May 26, 2026 are subject to TSCA
    section 12(b)" (L62).
  - "EPA designates April 24, 2026 as the cutoff date for determining whether the new use is ongoing." (L153);
    "Any person with an outstanding consent order as of April 24, 2026" (L101).
  - Notice period: "at least 90 days before commencing" (L25, L53, L266).
  - TSCA Order effective dates: "March 16, 2026 (P-25-152) and April 9, 2026 (P-25-73)" (L176);
    "March 16, 2026 (P-25-151) and April 7, 2026 (P-25-137)" (L196).
  - No final-rule effective date is printed (proposal only).
- Chemical substances (two proposed sections; both names are generic, both "CASRN: Not available." L175, L195):

| Proposed CFR section | PMNs with signed orders | Additional PMNs with outstanding consent orders | Name as printed | Lines |
| --- | --- | --- | --- | --- |
| 40 CFR 721.12219 | P-25-73, P-25-152 | P-23-120, P-25-93, P-25-125, P-25-135, P-25-145 (5; L99) | "Cobalt lithium manganese nickel oxide, metals-doped (generic)" (L174, L300, L306, L308) | L173-192, L306-333 |
| 40 CFR 721.12220 | P-25-137, P-25-151 | P-23-122, P-24-180, P-25-144 (3; L100) | "Cobalt lithium manganese nickel oxide, metals-doped (generic)" in the preamble (L194) and section list (L304); "Metal cobalt lithium manganese nickel oxide, metals-doped (generic)" in the section heading (L335) and paragraph (a)(1) (L337) | L193-215, L335-362 |

- Substance facts common to both sections:
  - Twelve PMN numbers are named in all (4 + 8). "The proposed SNURs extend the protective measures from
    the signed consent orders for P-25-73, P-25-152, P-25-137, and P-25-151" (L101).
  - Use: "The PMNs state that the generic (non-confidential) use will be in batteries." (L177, L200).
    "The PMN substance is a type of mixed metal oxide" = MMO; "Cathode Active Material (CAM)" (L177, L200).
    Three EPA 2026 documents are named in each basis paragraph (L177, L200).
  - "Multiple PMNs were submitted due to the fact that review of the first PMN received had not yet been
    completed and the PMN substance was not yet on the inventory." (L177, L200).
  - The two preamble blocks (L173-192 and L193-215) are parallel: same requirements, thresholds and
    label text on reading. Differences noticed: PMN numbers, order dates, and the heading "Basis for
    the TSCA Orders:" (L177) vs "Basis for TSCA Orders:" (L200). Not machine-diffed.
- Order requirements listed in the preamble (L178-190; again L201-213). Bullets are lost and two lines
  hold two items each (L183, L188), so 13 items by sentence start: battery-manufacture-only use; exterior
  label; dust controls "with an overall minimum combined capture and control efficiency of 99%"; air
  release limit; one-year limit (air release); one-year limit (inhalation exposure); disposal; no release
  to water; respirator before monitoring; respirator after monitoring; dermal PPE; engineering and
  administrative controls; hazard communication program.
- Designated significant new uses in the regulatory text, six heads per section (721.12219 L311-328;
  721.12220 L343-357):
  - (i) Protection in the workplace: "Sec. ... 721.63(a)(1), (a)(3) through (6), and (c)" (L311-312).
  - (ii) Hazard communication: "Sec. ... 721.72(a) through (d), (f), (g)(1), (g)(3)(iii), and (g)(5)" (L316-317);
    "this substance may cause: ... carcinogenicity, genetic toxicity, skin sensitization, respiratory
    sensitization, reproductive toxicity, neurotoxicity, and specific target organ toxicity" (L318-319) - 7 hazards.
  - (iii) Industrial, commercial, and consumer use (L320): more than one year "if there is any release of
    the substance to air or inhalation exposure to workers"; use "other than as a substance for use in
    the manufacture of batteries"; manufacture, process "(all processing includes recycling or
    reclaiming substances from batteries or other items containing the PMN substance)", or use "except
    with the use of dust controls with an overall minimum capture and control efficiency of 99%"; use
    without battery labels, with conditions (A)-(D) (L321-324).
  - (iv) Disposal: "other than by hazardous waste landfill in compliance with the Resource Conservation
    and Recovery Act Subtitles C or incineration, where the incinerator ash must be disposed of by
    hazardous waste landfill in compliance with the Resource Conservation and Recovery Act Subtitle C" (L325).
  - (v) Release to water: "Sec. ... 721.90(a)(1), (b)(1), and (c)(1)" (L326-327).
  - (vi) Release to air: "rolling average concentration over 14 days at the property boundary would be
    more than a maximum of 1.3E-4 mg/m\3\ of the substance individually or in any combination (i.e., in
    aggregate) with other cobalt containing mixed metal oxide (MMO) chemical substances" (L328).
  - Paragraph (b): recordkeeping "Sec. ... 721.125(a) through (k)" (L330-331); "Sec. 721.185" (L333).
- Thresholds (same values at L186-188, L209-211, L314-315, L345):
  - Before monitoring: respirator "assigned protection factor (APF) of at least 1,000" (L185).
  - Respiratory Protection Limits by 8-Hour Time Weighted Average (TWA), in mg/m\3\ (tier bounds
    paraphrased from "more than or equal to ... but less than ..."; values as printed):
    - "less than 5.3E-4 mg/m\3\, no respiratory protection is required"
    - from 5.3E-4 up to but not including 5.3E-3: "a minimum APF of 10"
    - from 5.3E-3 up to but not including 2.7E-2: "a minimum APF of 50"
    - from 2.7E-2 up to but not including 5.3E-1: "a minimum APF of 1000"
    - from 5.3E-1 up to but not including 5.3E+00: "a minimum APF of 10,000"
    - "If the 8-Hour TWA exceeds 5.3E+00 mg/m\3\, then manufacturing, processing, and use must cease"
    - As written, a TWA of exactly 5.3E+00 falls in no tier. The APF is printed "1000" in the fourth
      tier and "1,000" in the pre-monitoring rule (L185).
  - "an APF below 50 is only permitted when the PMN substance contains less than or equal to 3% cobalt by weight" (L186).
  - Aquatic toxicity "may occur at concentrations from 1-5 ppb" (L177, L200).
- Exceptions / carve-outs:
  - Article exemption (L309; L337-338): "The requirements of this section do not apply to quantities of
    the substance after the substance has been incorporated into an" article "as defined at 40 CFR 720.3,
    except as to the battery labeling requirements in the Industrial, commercial, and consumer use
    section." (the word article is in quote marks in the source). "The article exemption applies
    unless/until the article has been shredded or processed such that dust is generated." "Once the
    article containing the substance is or has been shredded or otherwise handled such that there is
    potential for exposure to or release of the substance, the article exemption no longer applies."
  - Label text example: "This battery contains substances that are subject to TSCA restrictions, including
    for recycling and reclamation activities. For details, contact the battery manufacturer or the EPA
    TSCA hotline." (L179, L202; "TSCA Hotline" in L321, L350).
  - "the SNUR will apply to the chemical substance regardless of whether or not a PMN was submitted" (L172).
  - "Although the Order does not require these tests" (aquatic toxicity testing; L192, L215).
- Cost, fee and burden figures (estimates unless marked):
  - "an estimated $45,496 per SNUN submission for large business submitters and $14,976 for small business
    submitters" (L70); basis: "the cost to prepare and submit the SNUN (including registration for EPA's
    Central Data Exchange (CDX)), and the payment of a user fee" (L70).
  - User fee (actual): "a $37,000 user fee required by 40 CFR 700.45(c)(2)(ii) and (d)"; small business
    "as defined at 13 CFR 121.201, a reduced user fee of $6,480 (40 CFR 700.45(c)(1)(ii) and (d))" (L70);
    repeated "from $37,000 to $6,480" (L248).
  - Second statement of the small-firm total: "about $14,967 per SNUN submission for qualifying small
    firms" (L249), described as "the total reporting and recordkeeping cost".
  - Export notification: "on a per unit basis is approximately $106" (L71); "a one-time notice ... for the
    first export or intended export to a particular country" (L71).
  - Burden: "between 30 and 170 hours per submission" (L237); OMB control number "2070-0038 (EPA ICR No.
    1188)" (L233); "EPA Form No. 7710-25" (L142).
  - SNUN counts (actuals): "9 in fiscal year FY2022, 23 in FY2023, and ... 7 in FY2024" (L246-247); "SNURs
    covering over 1,000 chemicals" (L246).
  - UMRA: "$100 million or more (in 1995 dollars)" (L253); "$183 million or more in any one year (the 1995
    dollars are adjusted to 2023 dollars ...)" (L254).
  - NAICS "codes 325 and 324110" (L59).
- Statutes and regulations cited: TSCA "section 5(a)(2) (15 U.S.C. 2604(a)(2))" (L49); 5(a)(1)(A) (L124),
  5(a)(1)(B) (L106); 5(a)(3) (L106), 5(a)(3)(A), (B), (C) (L98, L113, L135); 5(b) and 5(d)(1) (L124);
  5(b)(1)(A) (L143); 5(e) (L107), 5(e)(1)(A) (L98, L168); 5(f) (L146), 5(f)(4) (L101, L110, L168); 5(g)
  (L130); 5(h)(1), (2), (3), (5) (L124); section 4 (L143), 4(h) (L145); "section 12(b) (15 U.S.C. ...
  2611(b))" (L62-63); "section 13 (15 U.S.C. 2612)" (L61); "sections 5, 6, 7 and Title IV" (L61). CFR:
  "19 CFR 12.118 through 12.127, 19 CFR 127.28, and 40 CFR 707.20" (L61); 40 CFR 721.20 (L62); "40 CFR
  part 707, subpart D" (L64); 40 CFR 700.45 (L70); 13 CFR 121.201 (L70); "40 CFR parts 2 and 703" (L76);
  40 CFR 721.11 (L118); 721.1(c) (L124); part 720 (L124); part 700 (L125-126); 720.85 (L135); 720.40 and
  721.25 (L142); 720.50 (L144); part 9 (L232); 720.3 (L309). Other: PRA "44 U.S.C. 3501 et seq." (L232);
  RFA "5 U.S.C. 601 et seq." (L243); UMRA "2 U.S.C. ... 1531-1538" (L253-254); NTTAA "section 12(d) (15 U.S.C.
  272 note)" (L274); "Authority: 15 U.S.C. 2604, 2607, and 2625(c)." (L291). Executive Orders 12866
  "(58 FR 51735, October 4, 1993)" (L223), 14192 "(90 FR 9065, February 6, 2025)" (L227), 13132 (L258),
  13175 (L262), 13045 (L266), 13211 (L270); prior SNUR "June 2, 1997 (62 FR 29684) (FRL- 5597-1)" (L249).
- Lists: four TSCA 5(a)(2) factors (L87-90); five information items per substance (L158-162); objectives
  (L110-113; the first is printed twice, L110 and L111); Statutory and Executive Order Reviews A-J (L221-274).
- Hedged or conditional claims:
  - Proposal status: "These SNURs, if finalized as proposed, would require" (L53); "would designate" (L191, L214).
  - "the Agency believes that it is highly unlikely that any of the significant new uses identified in
    Unit ... III. are ongoing" (L135-136).
  - "EPA predicts that toxicity to aquatic organisms may occur" (L177): "may" attaches to the toxicity itself.
  - "EPA is unable to make any estimate of the likely number of export notifications" (L71); "EPA cannot
    presently determine how many, if any, there may be" (L246).
  - "this substance may cause:" (L318) is hazard-statement wording.
  - Firm (actuals): Orders "have been issued" (L135); SNUN counts (L246-247); fees (L70).
- Amendments or contradictions (recorded neutrally; the document states no precedence):
  - Small-business SNUN cost: "$14,976" (L70) vs "about $14,967" (L249). Mapper arithmetic: 45,496 - 37,000
    = 8,496 and 14,976 - 6,480 = 8,496; 14,967 - 6,480 = 8,487.
  - Name of the 721.12220 substance: with and without the leading word "Metal" (L194, L304 vs L335, L337).
  - Determination cited: orders "issued under TSCA section 5(e)(1)(A), as required by the determinations
    made under TSCA section 5(a)(3)(B)" (L98, L168) vs "have undergone premanufacture review and received
    determinations under TSCA section 5(a)(3)(C)" (L135); L113 describes 5(a)(3)(C) as "not likely to
    present an unreasonable risk".
  - Hazards: preamble concerns "carcinogenicity, reproductive toxicity, specific target organ toxicity,
    and dermal and respiratory sensitization" (L177) vs regulatory text adding "genetic toxicity" and
    "neurotoxicity" (L319).
  - Dust controls: "combined capture and control efficiency" (L180) vs "capture and control efficiency" (L320).
  - "does not concern an environmental health or safety risk" and "does not concern a human health risk"
    (L266) beside the health concerns listed at L177.
  - "most of the chemical identities ... are also CBI" (L118) vs "the identities of the chemical
    substances subject to this proposed rule have been claimed as confidential" (L135).
- Notes / passages not fully interpretable: missing spaces in the 721.12219 regulatory text (L312-319,
  e.g. "whichpersons", "Forpurposes", "isrequired"); "thedocket" (L177, L200); "Subtitles C" (L325, L354);
  fused requirement bullets (L183, L188, L206, L211); duplicated objective (L110-111). All are in the original.
- Coverage: FULL. Read L1-366 in one pass (every line). Nothing remains unread.

<!-- Read actual candidate-relevant passages with context and search the entire bundle for
duplicates/substitutes. A search is not a full read. Expand coverage when the candidate needs it;
lists/counts require the complete relevant universe, and needed gaps stay blocking. -->

## Shared ground (navigation only)

Searches run across all seven text files for this section (patterns): 40207 | 18741 | Pub. L. 117-58 |
Infrastructure Investment and Jobs Act | Bipartisan Infrastructure Law | BIL | IIJA; 30D | Inflation
Reduction Act | IRA | 13401 | clean vehicle; the FR cites 88 FR 84098, 89 FR 37706, 88 FR 23370, 88 FR 70310,
89 FR 1858, 88 FR 84082, 89 FR 37079; Notice 2023-1/2023-16; all "$" amounts; TSCA; EPA; DOE; TVA | Kingston |
Sierra Club | FinCEN; recycl; lead-acid | antimony; cobalt | graphite | manganese | nickel; 422 South
Clinton | Goodwill | TSCA Hotline; label; grid energy storage | BESS | lithium-ion | electric vehicle;
critical mineral | critical material; Executive Order 12866 | Regulatory Flexibility Act | Clean Air Act |
Ninth Circuit | Canada | environmental justice | Resource Conservation and Recovery; the key dates.

### Documents that cite, describe or depend on another document's rule

- D04 finalises D02 (same title, same "RIN 1901-ZA02": D02 L15, D04 L15). D04 L26 and L73: "On December 4,
  2023, DOE published ... (88 FR 84082). The comment period closed on January 3, 2024." D02 L6
  "[Pages 84082-84089]"; D02 L28 "no later than January 3, 2024". (Caller's documents; noted for linkage only.)
- D05 entry 197 and D02 share a Federal Register issue: D05 L544 "NPRM ... 12/04/23 88 FR 84098"; D02 L3-6
  "Monday, December 4, 2023", "[Pages 84082-84089]". D02 does not cite the Treasury proposal (no hit for
  "84098", "notice of proposed rulemaking" or "elsewhere in this issue" in D02).
- D05 entries 193, 196, 197 and D04 share a Federal Register issue: D05 L486, L527, L548 "Final Action ...
  05/06/24 89 FR 37706"; D04 L3-6 "Monday, May 6, 2024", "[Pages 37079-37091]". D04 L107: "the Treasury
  Department's final regulations on Clean Vehicle Credits under Sections 25E and 30D; Transfer of Credits;
  Critical Minerals and Battery Components; Foreign Entities of Concern published elsewhere in this issue
  of the Federal Register". D04 L186: "Treasury has incorporated DOE's FEOC guidance into its 30D rule".
  D05 does not mention DOE or the DOE interpretive rule.
- Comment deadlines on the two same-day proposals: DOE "no later than January 3, 2024" (D02 L28; D04 L73)
  vs Treasury "NPRM Comment Period End ... 01/18/24" (D05 L548).
- Effective dates on the two same-day finals: DOE "effective May 6, 2024" (D04 L28) vs Treasury "Final
  Action Effective ... 07/05/24" (D05 L486, entry 193 only).
- No other document in the bundle cites, amends or responds to another. D01, D03, D06 and D07 neither cite
  nor are cited by any other bundle document.

### Same statute, section or defined term in more than one document

- Infrastructure Investment and Jobs Act under different names: D01 L57 "Infrastructure Investment and Jobs
  Act (Pub. L. 117-58), also known as the Bipartisan Infrastructure Law" (no section number anywhere in
  D01); D02 L26 and D04 L26 "Infrastructure Investment and Jobs Act, also known as the Bipartisan
  Infrastructure Law (BIL)"; D04 L170 "(IIJA)"; D05 L536 "section 40207(a)(5) of the Infrastructure
  Investment and Jobs Act (42 U.S.C. ... 18741(a)(5))". Not mentioned in D03, D06 or D07.
- Section 40207(a)(5) / 42 U.S.C. 18741(a)(5), the "foreign entity of concern" definition: D05 L536-537;
  D02 L64-70; D04 L63-75. D05 only points to the definition; D02 and D04 state and interpret it.
- 26 U.S.C. 30D(d)(7) exclusion, same two dates in three places: D05 L536-537 ("after December 31, 2024"
  for critical minerals "extracted, processed, or recycled"; "after December 31, 2023" for components
  "manufactured or assembled"); D02 L68-69; D04 L72.
- Inflation Reduction Act: D05 L478 "Section 13401 of the IRA amends 30D(b)", L497, L508; D02 L68 and D04 L72
  "as amended by the Inflation Reduction Act of 2022 (IRA)"; D03 L67 and L104 (solar supply chain and
  Alternative B pricing only). D03 shares the Act's name with the others and nothing more specific.
- TSCA (D06 and D07 only; 25 and 39 lines; zero hits in D01-D05): "unreasonable risk" standard; section 5(e)
  and 5(f) (D06 L69; D07 L98, L110, L146); section 6 (D06 L69, L181-182; D07 L61); section 4 (D06 L69;
  D07 L143-145); Title IV (D06 L177-178; D07 L61); "potentially exposed or susceptible subpopulation(s)"
  (D06 L182, L188; D07 L113). D06 is a section 21 petition decision about section 6; D07 is a section 5 SNUR.
- "processing" including recycling: D06 L81 "processing (including recycling)"; D07 L180 "all processing
  includes recycling or reclaiming substances from batteries".
- Regulatory Flexibility Act and Executive Order 12866: D05 L46, L52-55; D07 L221-223, L241-249; D04 L280-281.
  Small-entity language: D05 L53; D07 L70 ("13 CFR 121.201"), L243-249.
- Clean Air Act: D03 L92 (section 111), L121 (section 309), L196 (40 CFR part 60 subparts KKKK, TTTT);
  D06 L126 (40 CFR part 63 subparts EEEEE, YYYYY, ZZZZZ). Different provisions.

### Entities that appear in more than one document

- EPA: issuer of D01, D06, D07; in D03 a named party only ("EPA has served as a cooperating agency" L116;
  section 309 comments "On March 25, 2024" L121; proposed GHG rule L92; "EPA-registered" herbicides L158).
  Zero hits for EPA in D02, D04, D05.
- EPA offices: D01 Office of Resource Conservation and Recovery (L23, L222); D06 and D07 both Office of
  Pollution Prevention and Toxics (D06 L32; D07 L33, L282) under OCSPP (FRL suffix "-OCSPP": D06 L15,
  D07 L15; D06 signer's office L239). Divisions differ: "Existing Chemicals Risk Management Division
  (7404M)" (D06 L32) vs "New Chemicals Division (7405M)" (D07 L33).
- TSCA hotline, one address, two operator names: "The TSCA Hotline, ABVI-Goodwill, 422 South Clinton Ave.,
  Rochester, NY 14620" (D06 L34) vs "The TSCA Assistance Information Service Hotline, Goodwill Vision
  Enterprises, 422 South Clinton Ave., Rochester, NY 14620" (D07 L41).
- DOE: issuer of D02 and D04; in D01 a named party ("U.S. Department of Energy" L62, L79, L91). Zero hits
  for DOE in D03, D05, D06, D07.
- Treasury: issuer of D05; in D02 and D04 a named party (OFAC D02 L65, D04 L70; CFIUS regulations D02 L146,
  D04 L216; the 30D rule D04 L107, L173, L176-178, L185-186, L190, L243).
- FinCEN: D05 entries 177-188 (the bureau's own agenda items); D02 L148, L186 and D04 L218, L254 cite
  FinCEN regulations ("31 CFR 1010.605(p)", "Beneficial Ownership Reporting Rule (31 CFR 1010.380(d))").
  D05 entry 188 is titled "Beneficial Ownership Information Access and Safeguards" (L370) - a different
  title; the bundle does not say how the two relate.
- Sierra Club: D03 L115 ("a form letter from Sierra Club with 583 signatories"); D06 L74 (one of the 2009
  petitioner groups).
- TVA / Kingston: D03 only (zero hits elsewhere).
- Same billing code "6560-50-P": D01 L224, D06 L241, D07 L365.

### Same subject stated with different figures or scope

- BIL money for DOE battery work: D01 L91 "For DOE, it provided more than $7 billion investment in the
  supply chain for batteries" vs D02 L64 and D04 L63 "Section 40207 of BIL (42 U.S.C. 18741) provides DOE
  $6 billion to support domestic battery material processing, manufacturing, and recycling". The labels
  differ (whole supply chain vs one section); no document reconciles the two.
- DOE grant programmes: D01 L62 "several grant programs to support battery collection, safe storage and
  transportation, recycling, and second-use" (future, unnamed) vs D02 L67 / D04 L72 "Battery Materials
  Processing and Battery Manufacturing and Recycling Grant Programs".
- Critical minerals: D01 L79 lists "antimony, cobalt, graphite, lithium, manganese, and nickel"; D07's
  substances are "Cobalt lithium manganese nickel oxide" (L174), i.e. four of those six names; D05 L478
  and L536 speak of "critical minerals" for the 30D credit without naming any; D02 and D04 use "critical
  mineral(s)" / "critical material(s)" (10 and 19 lines) - no hit there for cobalt, graphite, manganese
  or nickel. Zero hits for "critical mineral" or "critical material" in D03, D06, D07.
- Battery labelling: D01 voluntary labelling guidelines (L59, L174-192; "$15 million" L91) vs D07 required
  battery label as a SNUR condition (L179, L320-324). No cross-reference between them.
- Lead-acid batteries: D01 L122 only. D06 has no lead-acid statement; its only battery words are the
  organisation names in Ref. 17 (L218-219).
- Lithium-ion and grid storage: D01 L70, L79, L105 ("grid energy storage" L23, L60) and D03 L26, L223
  ("100 MW lithium-ion battery energy storage system"). Topic words only; no shared figure or statute.
- Vehicle-sector actors: D01 L23 ("dealerships, repair shops, auction houses, dismantlers, ... scrap
  yards") and D06 L50-63 (NAICS list), L126 ("automotive dismantlers and metal shredding facilities").
  Topic overlap only.

### Parallel attributes across documents (each located)

- Publication / signature / filing dates: D01 June 9, 2022 / June 3, 2022 / 6-8-22 (L3, L220, L223);
  D03 April 8, 2024 / April 2, 2024 / 4-5-24 (L3, L226, L229); D05 August 16, 2024 / none / 8-15-24 (L3,
  L555); D06 December 23, 2024 / December 16, 2024 / 12-20-24 (L3, L237, L240); D07 April 24, 2026 /
  April 21, 2026 / 4-23-26 (L3, L280, L364). D02 December 4, 2023 (L3); D04 May 6, 2024 (L3).
- Comment windows: D01 published June 9, 2022, comments by July 11, 2022 (L25); D02 published December 4,
  2023, comments by January 3, 2024 (L28); D03 "30-day public scoping period" from June 15, 2021 (L115)
  and "45-day public comment period that ended on July 3, 2023" (L117); D05 various per entry; D06 ANPRM
  April 3, 2024 with "the 30-day public comment period" (L112, L167), no deadline date; D07 published
  April 24, 2026, comments by May 26, 2026 (L27).
- Comment counts: D03 L115, L118; D06 L82, L112. None printed in D01, D05, D07.
- Signers: D01 Carolyn Hoskinson; D03 Jeff Lyash; D05 Michael Briskin; D06 Michal Freedhoff; D07 Mary Elissa Reaves.
- Docket / RIN identifiers: D01 EPA-HQ-OLEM-2022-0340 (no RIN); D02 and D04 RIN 1901-ZA02; D03 none;
  D05 21 RINs (table above); D06 EPA-HQ-OPPT-2024-0085, RIN 2070-AJ64; D07 EPA-HQ-OPPT-2025-2932, RIN 2070-AB27.

### Facts with two or more sources (repeats)

- Inside one document: D03 Final EIS NOA date (L26, L119); D06 petition granted August 26, 2009 (L102,
  L107), ANPRM April 3, 2024 (L112, L201), "nine States" (L93, L124, L130, L147), Alliance for Automotive
  Innovation "approximately 95 percent" (L131-135, L147, L167), IQ 0.026 (L141, L143, L163); D07 fee
  $37,000 / $6,480 (L70, L248), all Order requirements (preamble and regulatory text, for both sections),
  April 24, 2026 (L101, L153), May 26, 2026 (L27, L62); D05 Final Action 05/06/24 89 FR 37706 (L486, L527, L548).
- Across documents: the 30D(d)(7) exclusion and its two dates (D05 L536-537; D02 L68-69; D04 L72); the
  FEOC definition's location, section 40207(a)(5) (D05 L536; D02 L65; D04 L69); DOE proposal date and
  comment deadline (D02 L3, L28; D04 L26, L73); "$6 billion" (D02 L64; D04 L63); May 6, 2024 as the date
  of Treasury's final 30D regulations (D05 L486 by date and cite; D04 L3 with L107 by "this issue").
- Not repeated anywhere else in the bundle: every D03 figure; every D06 figure; every D07 cost, fee and
  threshold; D01's $10 million, $15 million and 40%; D05's $7,500 / $3,750 and all 21 RINs.

### Pairs that share nothing beyond a topic word

- D03 with D06 (only "Sierra Club", "EPA", "Clean Air Act" as names); D03 with D07 (only "EPA", "battery");
  D03 with D01 (only "lithium-ion", storage, "EPA"); D03 with D05, D02, D04 (only the name "Inflation
  Reduction Act"); D05 with D06 (nothing found); D05 with D07 (only the Regulatory Flexibility Act and
  Executive Order 12866 by name); D06 with D01 (EPA, recycling, vehicles as topics); D06 with D02, D04
  (nothing found by the searches above); D07 with D02 (nothing found) and with D04 (only the Regulatory
  Flexibility Act and Executive Order 12866 by name, D04 L280-281); D01 with D05 (the Act's name;
  "recycled" critical minerals as a topic); D01 with D07 (EPA, battery labelling and four mineral names,
  listed above, with no cross-reference).
