# aq-01539 - document map

Written once by `bundle-mapper` from `text/` (and `docs/` for flattened tables and scans).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

Locations are `text/Dnn.txt` line numbers (Lnn). `docs/` originals are the same text with no
2-line `# Dnn | source` header, so docs line = text line - 2 (verified D01). "p. N" = the
ECF footer "Case 2:24-md-03126-BMM-JTJ Document X Filed mm/dd/yy Page N of M" that ends page N.

## Bundle

- What it is: 14 court orders from one federal MDL, In re Snowflake, Inc., Data Security Breach
  Litigation, MDL No. 3126, Case No. 2:24-md-03126-BMM(-JTJ), U.S. District Court for the
  District of Montana, Butte Division, plus the JPML transfer order that created it. ECF filing
  dates run 10/08/24 (D01) to 08/19/26 (D14). D01 is by the Judicial Panel on Multidistrict
  Litigation (JPML). No signing judge's name is printed in the text of D02-D14 (signature blocks
  carry only "DATED this ..."); the judge appears only as caption/case-number suffixes "BMM"
  and "JTJ" and in D01 L76/L78 ("Chief Judge Brian Morris", "the Honorable Brian Morris") and
  D10 L28, D11 L24, D12-D14 L27 ("U.S. Magistrate Judge John T. Johnston" appointed Special
  Master, Doc. 383, described in the third person; D10-D14 speak as "The Court"). Whether D10-D14
  were signed by the district judge or the magistrate judge is not stated in the text.
  Signer attribution per document below is recorded only as the text supports it.
- Signature dates (text): D01 not legible (ECF filed 10/08/24); D02 March 12, 2025; D03 and D04
  May 22, 2025; D05 October 28, 2025; D06, D07, D08 October 29, 2025; D09 October 30, 2025; D10
  and D11 June 29, 2026; D12 July 1, 2026; D13 July 16, 2026; D14 August 19, 2026. Each matches its
  ECF "Filed" date.
- Documents: 14; ids D01-D14 from `text/manifest.json`; local Dnn = task page Doc N (intake.json
  numbers 1-14 map to the same sources in the same order). ECF numbers: D01 Doc. 1; D02 371; D03
  436; D04 437; D05 591; D06 592; D07 593; D08 594; D09 595; D10 739; D11 740; D12 744; D13 760;
  D14 780.
- Gaps: none in source capture (intake.json: every document `incomplete: false`,
  `gap_characters: 0`, `matches_capture: true`). Unread ranges: none (every document read in full;
  ledger in each entry's Coverage line). OCR noise: heavy in D01's certification stamp (L3-12; clerk
  name, day and month illegible, so the Panel's signature date is unresolved) and scattered OCR
  misspellings in D01 ("SnowHake", "Tlckclmaster", "QuoleWizard", "Cbaidez", "exllllration",
  "thefl"); D01 Schedule B lines merge several captions and district headings into one line (L110,
  L116, L117, L118, L128, L149, L153). Printed typos elsewhere are recorded per entry (e.g., D03/D04
  "PRELIMIMNARY", D04 "Bute", D05 "Doc. 4577", D07 "FCI Guidelines", D07 Exhibit 5 "dated April 18"
  with no year, D09 two items labelled "(4)", D11 "(5); HIPAA", D12 "FRP"). No PDF or page image
  exists in `docs/` (sources are .txt), so these cannot be checked visually: unresolved, not missing.
- Extraction spot-checks: method "text", pages null. ECF page footers present and sequential in
  every document (D01 8 pp; D02 22; D03 14; D04 14; D05 46; D06 36; D07 9; D08 22; D09 11; D10 8;
  D11 12; D12 22; D13 8; D14 13). Compared with `docs/` originals: D01 text L3-25 = docs L1-23
  (identical); D01 footnote 5-6 text L67-70 = docs L65-68 (identical); D03 deadline table text
  L134-157 = docs L132-155 (identical). Tables: no pipe/tab tables; the only tabular content is D01
  Schedules A/B (lists) and the flattened two-column deadline tables in D03 (L137-155) and D04
  (L128-145). Charts: not applicable.
- Provenance: notes/intake.json schema 1, capture_sha256 3ff05eb1...; 14 of 14 documents
  `matches_capture: true`; source sha256 values in text/manifest.json equal intake captured hashes.

## D01 - JPML Transfer Order (MDL No. 3124 and MDL No. 3126)

- Source: docs/uscourts_mtd_2_24_md_03126_0.txt | 8 ECF pages (footers L24, 44, 56, 73, 91, 104,
  133, 156); text L1-159.
- Written or submitted by: United States Judicial Panel on Multidistrict Litigation (L6 garbled
  "UNITED STATES .JUD1CIAL>^EL", L10 "MULTIDISTRICT LITIGATION", L83 "PANEL ON MULTIDISTRICT
  LITIGATION"). Signed L86-89: Nathaniel M. Gorton, Acting Chair; Matthew F. Kennelly, Roger T.
  Benitez, Dale A. Kimball, Madeline Cox Arleo. Footnote * L20: Judges Karen K. Caldwell and David
  C. Norton did not participate; Panel members who could be class members "have renounced their
  participation in these classes and participated in this decision."
- Type, date, edition: "TRANSFER ORDER" (L17), captioned In re: AT&T Inc. Cellular Customer Data
  Security Breach Litigation, MDL No. 3124, and In re: Snowflake, Inc., Data Security Breach
  Litigation, MDL No. 3126 (L13-16). The Panel's own signature date is not legible in the text
  (certification stamp L3-12 is OCR-garbled: "Clerk of the United States District Court for the
  District of Montana ... TYLER P, GtLti^N, Clerk", day/month blank). District docket footer:
  "Case 2:24-md-03126-BMM-JTJ Document 1 Filed 10/08/24" (L24). Order date = unresolved from text.
- Period covered: events July 23, 2024 to the hearing/decision; breach window "approximately April
  to June 2024" (L18) / "from approximately April through June 2024" (L38).
- Entities and aliases: fn 1 L21-22 defines defendants: AT&T Inc. and AT&T Mobility, LLC
  ("AT&T"); Advance Auto Parts, Inc. and Advance Stores Company, Inc. ("Advance Auto Parts");
  Cricket Wireless, LLC; Snowflake Inc. (OCR "SnowHake"); Ticketmaster LLC and Live Nation
  Entertainment, Inc. ("Ticketmaster/Live Nation"); The Neiman Marcus Group; Lending Tree LLC and
  QuoteWizard.com LLC ("Lending Tree"). L18: "Lending Tree's QuoteWizard.com subsidiary".
  Movants: plaintiff Young (MDL 3124 motion), plaintiff Chaidez (OCR "Cbaidez", MDL 3126 motion)
  (L19). MDL No. 3114 = separate earlier AT&T breach MDL (L35-36, fn 3 L41-42, fn 6 L69-71).
  Transferee judge "Chief Judge Brian Morris" (L76), "the Honorable Brian Morris" (L78).
  Schedule-caption spelling varies: "TICKETMASTER, LLC" and "TICKETMASTER LLC" (L110-118);
  "ADVANCE STORES COMPANY, INCORPORATED" (L141, L149); "AT&T MOBILITY LLC" (L97, L121).
- Numbers (all counts of actions unless stated):
  - "over 500 million individuals" (L18); "over 500 million consumers and employees" (L38).
  - July 23, 2024 Young motion "to centralize four putative class actions" re AT&T data; docketed
    MDL No. 3124 (L19).
  - July 29, 2024 Chaidez motion "to centralize 43 putative class actions ... (including two
    actions from MDL No. 3124)"; docketed MDL No. 3126 (L19).
  - "plaintiffs in three actions had filed responses supporting an AT&T MDL" (L27).
  - "45 actions pending in eight districts as listed on Schedules A and B" (L27).
  - "34 potential tag-along actions, including at least five additional AT&T actions" (L27).
  - "plaintiffs in over 30 actions support" (L34); "Plaintiffs in 21 actions request the District
    of Montana" (L34); "Plaintiffs in nine actions oppose"; "three of these" support the AT&T MDL
    (L35).
  - "at least 20 actions (including potential tag-along actions) name Snowflake together with a
    client as co-defendant" (L52).
  - "at least eleven actions naming Snowflake as a defendant in six districts outside Montana";
    AT&T actions "spread among eight districts" (L61).
  - fn 5 L67: counting all D. Mont. actions as one and all E.D.N.C. actions as one, "there still
    are 42 related actions pending in twelve districts."
  - "Fourteen actions on the motion and twelve potential tag-along actions are pending in this
    district" (D. Mont.); "Plaintiffs in over twenty actions request it as their first or second
    choice" (L66). Note L34 "21 actions" vs L66 "over twenty actions" (first or second choice).
  - fn 3 L41-42: MDL No. 3114 centralized "twelve actions" (J.P.M.L. June 5, 2024), AT&T breach
    announced March 2024, "over 70 million former and current AT&T customers".
- Tables/lists: Schedule A (MDL No. 3124) L93-102, 4 actions: N.D. Ga. Young v. AT&T Mobility LLC
  1:24-03185; D. Mont. Olivieri v. AT&T Inc. 2:24-00056; D.N.J. Schulte v. AT&T Inc. 3:24-07818;
  N.D. Tex. Winger v. AT&T Inc. 3:24-01797. Schedule B (MDL No. 3126) L106-154, 43 entries by
  district: C.D. Cal. 14 (Ryan 2:24-04482 ... Dickey-Johnson 2:24-06940, L110-118; Ticketmaster or
  Live Nation captions); N.D. Cal. 1 (Conte v. Snowflake 3:24-04443, L119); N.D. Ga. 2 (Young; Morgan
  v. Cricket Wireless 1:24-03253, L121-122); D. Mont. 14 (Leal 2:24-00046 through Hornthal 2:24-00068,
  L124-139, includes Olivieri and Miller v. Snowflake 2:24-00067); E.D.N.C. 10 (In re Advance Stores
  Company 5:24-00352 ... Carr 5:24-00445, L141-150); N.D. Tex. 1 (Weaver v. Snowflake 3:24-01915,
  L153); W.D. Wash. 1 (Leduc Montgomery v. AT&T Inc. 3:24-05581, L153-154; last list item).
  Young and Olivieri appear on both schedules (mapper count: 4 + 43 - 2 = 45 unique; districts on
  the schedules: C.D. Cal., N.D. Cal., N.D. Ga., D. Mont., E.D.N.C., N.D. Tex., W.D. Wash., D.N.J. =
  8). Note: there are two "Miller" actions (C.D. Cal. Miller v. Ticketmaster 2:24-05867 L117; D.
  Mont. Miller v. Snowflake 2:24-00067 L138) and two "Chaidez" actions (D. Mont. 2:24-00050 L125;
  E.D.N.C. Chaidez v. Advance Auto Parts 5:24-00354 L143).
- Forecasts, guidance, deadlines, effective dates: none (no deadlines set).
- Positions (L29-36): AT&T and Cricket Wireless support single MDL, suggest E.D.N.C., alternatively
  D. Mont.; Lending Tree supports Snowflake MDL in E.D.N.C.; Neiman Marcus supports without a
  district (fn 2 L39: alternatively D. Del. or N.D. Tex. for a Neiman Marcus MDL if no Snowflake
  MDL); Snowflake and Advance Auto Parts oppose (informal coordination); Ticketmaster/Live Nation
  "takes no position" (L32). Other plaintiffs' districts: C.D. Cal., W.D.N.C., W.D. Okla., N.D. Cal.
  (L35); AT&T-MDL supporters propose N.D. Ga., D.N.J., N.D. Tex. (L35); MDL 3114 leadership: N.D.
  Tex. (L35-36). D. Mont. unopposed by AT&T, Cricket Wireless, Ticketmaster/Live Nation, Neiman
  Marcus (L76); Snowflake "has its principal executive office in this district" (L76).
- Hedged claims: "allegedly occurred" (breach window L18), "allegedly resulted in the
  exfiltration ... of over 500 million individuals" (L18), "allegedly exfiltrated" (L38); "undoubtedly
  will involve some defendantspecific issues" (L50, not a hedge: firm); "parties seem likely to disagree on
  the proper venue" (L61); fn 6 breach facts "allegedly involved"/"allegedly involves" (L69-70).
- Rounded prose beside exact figures: "over 30 actions" / "21 actions" (L34); "over twenty actions"
  (L66); "at least" counts (L27, L52, L61).
- Notes: fn 4 L53-54 MFA definition ("electronic authentication method that requires a second form
  of authentication (in addition to standard log-in credentials)"). "shared responsibility"
  cybersecurity model (L47, L50). fn 6 L69-71: MDL 3114 breach announced March 2024, 2019 data
  set; Snowflake-hosted AT&T breach "announced in July 2024", call/text metadata "from May 1, 2022
  to October 31, 2022, and, for some customers, records from January 2, 2023" (citing Miller v.
  Snowflake, C.A. No. 24-0067 (D. Mont.) Compl. paras 38-39).
- Operative rulings: L65 District of Montana selected; L76 Chief Judge Brian Morris; L78-79
  Schedule A and B actions pending outside D. Mont. "are transferred to the District of Montana ...
  assigned to the Honorable Brian Morris ... to proceed in MDL No. 3126"; L81 separate MDL for
  Schedule A actions (MDL No. 3124) "is denied"; L62-63 reasons for denying AT&T-only MDL; fn 6 L69
  denies MDL 3114 leadership's N.D. Tex. request.
- Amendments or contradictions: none within document. Cross-bundle: later orders describe the
  breach window and counts differently (see Shared ground).
- Coverage: FULL. Read L1-159 (all 8 pages incl. footnotes and Schedules A/B). Unread: none.

## D02 - Order re: Potential Conflict of Interest of Plaintiffs' Co-Lead Counsel

- Source: docs/uscourts_mtd_2_24_md_03126_23.txt | 22 ECF pages (Doc. 371, Filed 03/12/25,
  footers L17-L187); text L1-190.
- Written or submitted by: U.S. District Court, District of Montana, Butte Division (L4-6),
  caption "2:24-MD-03126-BMM" (L13). Signing judge's name not printed (L185 "DATED this 12th day
  of March, 2025." only).
- Type, date, edition: "ORDER RE: POTENTIAL CONFLICT OF INTEREST OF PLAINTIFFS' CO-LEAD COUNSEL"
  (L14-16); dated March 12, 2025 (L185); ECF Doc. 371 filed 03/12/25.
- Period covered: June 5, 2024 to March 11, 2025 chronology (L10-59).
- Entities and aliases: Amy Keller ("Keller"), Co-Lead Counsel, firm "Dicello Levitt" (L8) /
  "DiCello Levitt" (L24 onward); Keller's partners Adam Levitt, Ken Abbarno (L51); Timothy Blood
  ("Blood") co-applicant not selected (L22-23); "4 Leads" = John Heenan, J. Devlan Geddes, Raphael
  Graybill, Jason S. Rathod (L26-27; also "4 Co-Leads" L167); ethics advisor Betsy Brandborg
  ("Brandborg"), former General Counsel and Ethics Counsel, State Bar of Montana (L48); Jerry Lynch
  ("Lynch"), retired federal magistrate judge, D. Mont. (L51). "AT&T I" = In re: AT&T Inc. Customer
  Data Security Breach Litigation, MDL 3114, Dkt. 139 (N.D. Texas), centralized June 5, 2024 (L10,
  L35); "AT&T II" = this MDL, "(Doc. 1; 2:24-MD-03126-BMM)", centralized in the District of
  Montana-Butte Division "on October 8, 2024" (L20). Also "North Texas MDL" (L43). Snowflake Inc.
  (L22).
- Dates and ECF cites (chronology): Sept 3, 2024 Keller filed a complaint in AT&T II (Doc. 357-1,
  Ex. 4 at 26) (L22) = "Miller v. Snowflake, Inc et al, 2:24- cv-96, Doc. 1" (L35); Oct 30, 2024
  Keller appeared for an individual plaintiff against Snowflake Inc. (Doc. 143) (L22); Nov 7, 2024
  Keller and Blood leadership motion (Doc. 222) (L22, L39); Nov 27, 2024 Court selected Keller
  (Doc. 253; Doc 255) (L23); Feb 17, 2025 4 Leads learned of the opt-out clients (L28, L43); Feb 20,
  2025 Brandborg consulted (Doc. 357 at 3) (L48); Feb 24, 2025 adverse opinion notified (L48;
  Doc. 357-1, Ex. 1); Mar 1, 2025 meeting (Doc. 357 at 6) (L51); Mar 4, 2025 response deadline and
  Keller's response (L51, L57); Mar 5, 2025 resignation deadline; Keller declined; Court noticed ex
  parte (L57-59); Mar 10, 2025 deadline for additional responses (L59); Mar 11, 2025 ex parte
  hearing (Doc. 369) (L59); global mediation with AT&T scheduled March 17, 2025 (L43; proposed
  event, not reported as held). Other ECF cites: Doc. 357 (4 Leads' notice), Doc. 350 (earlier order
  on incorporating Financial Institution claims; "Doc. 350 at 2- 3") (L147, L152), Doc. 344 at 4-5
  (Co-Lead Counsel filing on a financial institution spoke) (L149-152).
- Numbers: "apparently represents approximately 20,000 individual clients who intend to opt-out"
  (L24); "all 20,000 plaintiffs who decided to opt out" (L48); Keller "appointed to lead eight
  separate data privacy class actions" (L40, Doc. 222 at 10); "four other Co-Lead Counsel" (L26,
  L145, L162 "Four other"); Deola: five newer clients, six clients total, global settlement "$4.65
  million" (L106-109); Sheftelman class: bonds bought between October 1, 1982 and December 1, 1983
  (L129); "millions of class members" (L173).
- Rules cited: Mont. R. Prof. Conduct 1.7, 1.8(g), 1.10 (L31, L75, L79-86), 1.4 (L109), Preamble
  (14) (L171); ABA Model Rule 1.8 Cmt. 16 (L88); Fed. R. Civ. P. 23 and 23(a)(4) (L89, L130); D.
  Mont. LR 83.2(a) (L62); Bolch Best Practices at 31, 51, 53, 57 (L149-169); Newberg & Rubenstein
  s.19:24 (6th ed. 2024) (L145).
- Cases discussed: In re Marra, 87 P.3d 384 (Mont. 2004) (L97-102); In the Matter of Linda Deola,
  No. PR 16-0714 (Mont. Nov. 29, 2019) (L106-114); Sandoval v. Ali (L68, L92, L117-126); Sheftelman
  v. Jones (spelled "Scheftelman" at L140, L145) (L128-132); Ruderman ex rel. Schwartz v.
  Washington Nat. Ins. Co., 263 F.R.D. 670 (L134-138); Mehl (L91); In re Austrian & German Bank
  Holocaust Litig. (L91).
- Tables: not applicable. Lists: ORDERED list has one numbered item (L178-180).
- Forecasts, guidance, deadlines, effective dates: proposed global mediation March 17, 2025 (L43);
  no deadlines set by the order.
- Hedged claims: "apparently represents approximately 20,000" (L24, the client count/representation
  is hedged); "The record remains unclear when the individual clients ... retained DiCello Levitt.
  The Court assumes ..." (L35); "Keller allegedly disclosed a potential conflict" (L43); 4 Leads'
  single-limited-pot premise "remains speculative and hypothetical" (L145); "should have
  identified that a potential conflict may arise" (L157); "no actual conflict exists unless AT&T
  proposes a limited fund settlement" (L158, conditional).
- Operative definitions, rules and scope exceptions: disqualification standard (L68-69); Rule 1.7
  conflict test (L79-82); 1.8(g) text (L84-86). Disposition: "Keller's conflict does not warrant
  disqualification" (L175); ORDERED "1) Amy Keller of DiCello Levitt will remain as Co-Lead
  Counsel" (L180). Safeguards stated in Discussion/Conclusion (not numbered in ORDERED list): Keller
  "prohibited from attending the global mediation with AT&T" and from "any discussions regarding the
  allocation of any proposed settlement funds from AT&T" (L162, L176); exception: "This Order does
  not exclude Keller from receiving her share of any attorney's fees from an AT&T settlement" (L176);
  firm "will not attend the global mediation and will not advise its arbitration clients in AT&T I"
  (L176). Screening declaration: Declaration of Amy Keller para 27 (L104, L115, L161).
- Notes: "this MDL is a first of its kind in the District of Montana" (L168); data breaches in AT&T I
  and AT&T II "occurred years apart" (L111).
- Amendments or contradictions: D02 L20 dates JPML centralization of this MDL "October 8, 2024"
  (D01 bears only "Filed 10/08/24"). D02 L35 gives Keller's complaint as Miller v. Snowflake
  "2:24- cv-96"; D01 lists a different Miller v. Snowflake number, C.A. No. 2:24-00067 (D01 L138, fn
  6 L70 "24-0067"). Not reconciled in either document.
- Rounded prose beside exact figures: "approximately 20,000" (L24) vs "all 20,000" (L48); "millions
  of class members" (L173); no exact counterpart printed.
- Coverage: FULL. Read L1-95, L95-190 (all 22 pages). Unread: none.

## D03 - Amended Order Granting Preliminary Approval: Advance Auto Parts settlement

- Source: docs/uscourts_mtd_2_24_md_03126_26.txt | 14 ECF pages (Doc. 436, Filed 05/22/25,
  footers L19-L159); text L1-162.
- Written or submitted by: U.S. District Court, District of Montana, Butte Division (L3-5), "CASE
  No.: 2:24-MD-3126-BMM" (L14). Signing judge's name not printed (L157 "DATED this 22nd day of May,
  2025.").
- Type, date, edition: "AMENDED ORDER GRANTING PLAINTIFFS' UNOPPOSED MOTION FOR PRELIMIMNARY [sic]
  APPROVAL OF CLASS ACTION SETTLEMENT" (L15-16); "This Document Relates to Defendant: ADVANCE AUTO
  PARTS, INC. AND ADVANCE STORES COMPANY, INCORPORATED" (L8-13). Dated May 22, 2025 (L157). The text
  does not identify the earlier order it amends or what changed.
- Entities and aliases: Defendants Advance Auto Parts, Inc. and Advance Stores Company,
  Incorporated (L17), thereafter "Defendant" (singular). Plaintiffs/Class Representatives (6):
  Emmanuel Chaidez, Stefondra Monroe, Raymond Moule, Raven Richardson, Don Smith, Raymond Swain
  (L17, L41). Class Counsel (5): Devlan Geddes, Raph Graybill, John Heenan, Amy Keller, Jason Rathod
  (L43-45, Rule 23(g)). Settlement Administrator: Kroll Settlement Administration, LLC (L62). Motion
  = Doc. 415 (L17). Venue: Mike Mansfield Federal Courthouse, Butte, Montana (L50).
- Numbers: "$10,000,000 non-reversionary common fund Settlement" (L17); class "estimated to be
  approximately 2.3 million individuals" (L26); "more than 100 members" and amount in controversy
  "exceeds $5,000,000" (L37, 28 U.S.C. 1332); fees "up to 33.33% of the Settlement Fund" (L53);
  Service Awards "up to $2,500.00" each Class Representative (L53); objector history "within the 5
  years preceding" (L92, L96).
- Operative definitions: fn 1 L18 capitalized terms = Section II of the Settlement Agreement.
  Settlement Class (L26): "All persons in the United States whose Private Information was
  potentially compromised as a result of the Data Incident and who were sent notice of the Data
  Incident." Exclusions (1) governing board members of Defendant; (2) governmental entities; (3)
  the Court, immediate family, staff; (4) timely valid opt-outs (L26). California Settlement
  Subclass (L28-30): "All Settlement Class Members who are residents of California"; exclusions
  repeated L32 (worded "Excluded from the Settlement Class"). "Data Incident" is not defined in the
  order's text (only via fn 1).
- Deadlines and dates: para 8 L50: Final Approval Hearing "Thursday October 23, 2025, at 10:00
  a.m." Summary of Deadlines table (para 30, L134-155; columns EVENT / DEADLINE): commence Notice
  Program "Within 20 days of the Preliminary Approval Order" (L138); complete Notice Program "45 days
  before the original Final Approval Hearing date" (L139); Motion for Final Approval incl. fee
  application 45 days before (L140-145; also para 10 L55); Opt-Out Period Ends 30 days before (L149;
  para 15 L72 "postmarked no later than 30 days before"); Objection Period Ends 30 days before (L150;
  para 19 L85); Claim Form Deadline 15 days before (L151); "Final Approval Hearing July 10, 2025, at
  10:00 a.m. (or soon thereafter based on the Court's availability)" (L152-155). Para 28 L131: Court
  may adjourn/continue the hearing without further notice; new date posted on Settlement Website;
  may hold it by Zoom.
- Lists: objection contents a-j, 10 items (L86-107), last item j "the objector's signature (an
  attorney's signature is not sufficient)" (L107). Notices: Email Notice, Publication Notice, Long
  Form Notice, Claim Form (L65). Opt-out request contents (L72). Hearing issues (a)-(e) (L50).
- Rules/exceptions: no opt-out by telephone or email; no "Mass" or "class" opt-outs (L74-75);
  objections submitted "to the Settlement Administrator" (L85) by mail to the Long Form Notice address
  or via the Settlement Website (L109); non-material modifications by written agreement without
  further order (L65); para 24-25 order null and void if no final approval/termination/no Effective
  Date (L119-123); para 26 stay of "this matter and any deadlines" pending final approval (L126); para
  27 provisional injunction against Settlement Class claims vs Defendant and Released Parties (L128).
- Hedged claims: "finding it is likely to final certify it at Final Approval" (L24, L28); Settlement
  "is likely to be approved as fair, reasonable, and adequate" (L48); fee/service amounts "appear
  reasonable, but the Court will defer ruling" (L53); "Private Information was potentially
  compromised" (L26, the hedge is part of the class definition).
- Tables: Summary of Deadlines, L137-155 (text-flattened two-column table; Motion row wraps L140-145
  with deadline on L144-145; page break L146 inside table).
- Amendments or contradictions: SAME-DOCUMENT CONFLICT: para 8 (L50) "Thursday October 23, 2025"
  vs deadline table (L152) "July 10, 2025"; all relative deadlines key to "the original Final
  Approval Hearing date" (L55, L72, L85, L139-151). No precedence stated; para 28 (L131) permits
  rescheduling. Parallel order D04 has the identical conflict (see Shared ground).
- Period covered: settlement schedule from entry of the order (May 22, 2025) to the Final Approval
  Hearing; no period of the underlying "Data Incident" is printed.
- Rounded prose beside exact figures: class size "estimated to be approximately 2.3 million" (L26)
  vs "more than 100 members" jurisdictional finding (L37); fee cap "33.33%" (L53).
- Coverage: FULL. Read L1-80, L80-162 (all 14 pages). Unread: none.

## D04 - Amended Order Granting Preliminary Approval: Neiman Marcus settlement

- Source: docs/uscourts_mtd_2_24_md_03126_27.txt | 14 ECF pages (Doc. 437, Filed 05/22/25,
  footers L17-L152); text L1-155.
- Written or submitted by: U.S. District Court, District of Montana, Butte Division (L3-5), "CASE
  No.: 2:24-MD-3126-BMM" (L6). Signing judge's name not printed (L150 "DATED this 22nd day of May,
  2025.").
- Type, date, edition: "AMENDED ORDER GRANTING PLAINTIFFS' UNOPPOSED MOTION FOR PRELIMIMNARY [sic]
  APPROVAL OF CLASS ACTION SETTLEMENT" (L7-8); "This Document Relates only to Defendant: THE NEIMAN
  MARCUS GROUP, LLC" (L14-16). Dated May 22, 2025 (L150). Earlier order being amended not identified.
- Entities and aliases: Defendant The Neiman Marcus Group, LLC (L15-16; D01 fn 1 calls it "The
  Neiman Marcus Group" without "LLC"). Class Representatives (6): Marc Reichbart, Jamilla Sherman,
  Chrystal Pelosi, Natalie Gianne, Anastasia Kouriatova, Ron Slomwicz (L33). Class Counsel (5): John
  Heenan, Amy Keller, Raph Graybill, Jason Rathod, Devlan Geddes (L35). Settlement Administrator:
  Epiq Class Action & Claims Solutions, Inc. (L51). Motion = Doc. 413 (L9). Venue: Mike Mansfield
  Federal Courthouse in "Bute" [sic], Montana (L40).
- Numbers: "$3,500,000 non-reversionary common fund Settlement" (L9); "more than 100 members",
  amount in controversy "exceeds $5,000,000" (L27); fees "up to one-third of the Settlement Fund"
  (L43); Service Awards "up to $3,000.00" each (L43); objector history "within the 5 years" (L82,
  L86-88). No class-size estimate anywhere in D04.
- Operative definitions: fn 1 L10 capitalized terms = Section II of the "Settlement Agreement and
  Releases", Exhibit A to the motion. Settlement Class (L25): "All persons who live in the United
  States whose Personal Information was potentially compromised as a result of the Data Incident."
  Exclusions (a) governing board members of Defendant; (b) governmental entities; (c) the Court,
  family, staff; (d) "any individual who timely and validly opts-out" (L25). No subclass. No
  "sent notice" condition (contrast D03 L26).
- Deadlines and dates: para 7 L40: Final Approval Hearing "Thursday, October 23, 2025 at 10:00
  a.m." Summary of Deadlines table (para 29, L125-145): "Defendant will make Class List available to
  Class Counsel and the Settlement Administrator" "No later than 15 days after entry of the
  Preliminary Approval Order" (L129-132); commence Notice "Within 30 days following receipt of the
  Class List" (L133); complete Notice 45 days before "the initial scheduled Final Approval Hearing
  date" (L134); Motion for Final Approval 45 days before (L135-138; para 9 L44); Opt-Out Period Ends
  30 days before (L139; para 14 L61); Objection Period Ends 30 days before (L140; para 18 L75);
  Claim Form Deadline 15 days before (L141); "Final Approval Hearing July 10, 2025, at 10:00 a.m. (or
  soon thereafter based on the Court's availability)" (L142-145). Para 27 L120 adjournment/Zoom
  clause identical to D03 para 28.
- Lists: hearing issues (a)-(f), includes "(d) Class Counsel and Class Representatives shall be
  reappointed" (L42); objection contents a-k, 11 items (L77-97), first "a. the name of the Action",
  last "k. the objector's signature (an attorney's signature is not sufficient)" (L97); item f adds
  copies of orders on counsel's prior objections (L86-88). Notices: Email, Long Form, Publication,
  Claim Form (L53).
- Rules/exceptions: opt-out "personally signed ... with a 'wet' signature" (L61); no telephone/email
  or mass opt-outs (L65-66); objection "submitted to the Court" (L75) and "mailed to the Clerk of the
  Court, Class Counsel, Defendant's Counsel, and the Settlement Administrator" (L99-101); null/void
  and non-admission clauses paras 23-24 (L109-111); stay para 25 (L116); provisional injunction para
  26 (L118); claims to be dismissed are those "in the Consolidated Complaint against Defendant"
  (L42) (D03 L50: "Amended Representative Class Action Complaint").
- Hedged claims: "likely to final certify" (L24); "likely to be approved" (L38); amounts "appear
  reasonable, but the Court will defer ruling" (L43); "Personal Information was potentially
  compromised" (L25, inside class definition).
- Tables: Summary of Deadlines L128-145 (flattened two-column EVENT/DEADLINE; Class List row wraps
  L129-132).
- Amendments or contradictions: SAME-DOCUMENT CONFLICT: para 7 (L40) "Thursday, October 23, 2025" vs
  table (L142) "July 10, 2025"; relative deadlines key to "the initial scheduled Final Approval
  Hearing date" (L44, L61, L75, L134-141). No precedence stated; para 27 permits rescheduling.
- Period covered: settlement schedule from entry of the order (May 22, 2025) to the Final Approval
  Hearing; no period of the underlying "Data Incident" is printed.
- Rounded prose beside exact figures: fee cap "one-third" (L43; D03 prints "33.33%"); "more than
  100 members" (L27); no class-size figure.
- Coverage: FULL. Read L1-75, L75-155 (all 14 pages). Unread: none.

## D05 - Order on Motions to Dismiss Consumer Plaintiffs' Claims (Snowflake; Ticketmaster)

- Source: docs/uscourts_mtd_2_24_md_03126_33.txt | 46 ECF pages (Doc. 591, Filed 10/28/25,
  footers L15-L418); text L1-421.
- Written or submitted by: U.S. District Court, D. Mont., Butte Division (L4-6), "Cause No.
  2:24-md-03126-BMM" (L8). Signer not named (L416 "DATED this 28th day of October 2025.").
- Type, date, edition: "ORDER ON MOTIONS TO DISMISS CONSUMER PLAINTIFFS' CLAIMS" (L9-11); dated
  October 28, 2025 (L416).
- Entities and aliases (L13-22): Snowflake, Inc. ("Snowflake", the "hub"); "Spoke Defendants";
  "Ticketmaster" = Ticketmaster, LLC and Live Nation Entertainment, Inc. (L15); "LendingTree" =
  LendingTree, LLC and Quotewizard.com, LLC (L15); "Consumer Plaintiffs" = consumer customers of
  Ticketmaster and LendingTree (L15); "LAUSD Plaintiffs" = Los Angeles Unified School District
  (L15); "Financial Institution Plaintiffs" (L15); FAC spoke defendants (L21-22): Ticketmaster;
  "Advance Auto" = Advance Auto Parts, Inc. and Advance Stores Company, Inc.; LendingTree; "AT&T" =
  AT&T, Inc. and AT&T Mobility, LLC; "Innive" = Innive, Inc.; "Doe" Defendants associated with
  LAUSD. (Neiman Marcus is not in D05's FAC defendant list; Neiman Marcus appears only in the cited
  case Remijas v. Neiman Marcus Grp., LLC, L94.) Named Consumer Plaintiffs: Anderson (Ticketmaster
  customer; New York; fraud December 2024; L73-75, L400), Fitzgerald (New York; no notice letter;
  L73, L145, L400), Lozoya (L73), Xian (California Consumer Plaintiff, L73, L309, L334, L350),
  Garcia-Nixon and Neve (no notice letter, L145). Ticketmaster's "parent company" (L176, unnamed).
- Definitions: "hub-and-spoke" data breach (L13, citing Doc. 1 para 2); "Data Breach" (L18);
  "FAC" = Fourth Amended Complaint filed July 9, 2025, Doc. 485 (L20); MFA (L31); PII (L42, L68);
  CAMS = Visa Compromised Account Management System (L154); Montana CPA "consumer" (Mont. Code
  Ann. 30-14-102(1), L231); "unfair act" ("Roher v. Knudsen", L240-241); "deceptive act" (L241-243);
  CCPA private right (Cal. Civ. Code 1798.150(a)(1), L312-320) and "Personal Information" (1798.81.5
  (d)(1)(A) items (ii) and (iii), L320-327); Montana breach-of-contract elements (L360).
- Procedural ECF cites: Snowflake MTD Doc. 417 (memo Doc. 418); Consumer opposition Doc. 474;
  Ticketmaster MTD "or alternatively, to strike Consumers' Complaint" Doc. 456 (memo Doc. 457;
  L214 typo "Doc. 4577"); opposition Doc. 488; hearing October 6, 2025 (Doc. 569) (L23-24). Court
  applies earlier motions to the later FAC (L25). Complaint paragraphs are cited both as "Doc. 1"
  (L13, L27, L42 "Doc. 1 para 256", L392 "Doc. 1 paras 555-56") and "Doc. 485" (L70 "Doc. 485 para
  256" for the same nine-injury list).
- Events/dates (as alleged): threat actors accessed Spoke Defendants' Snowflake accounts "in April
  of 2024" (L29, FAC paras 162-166) / "obtained the data from Snowflake's servers in April 2024"
  (L89); Snowflake offered free MFA "since June 2015" (L31); advertisements of stolen data began
  "May 24, 2024" (L35); Snowflake announced the Data Breach "on May 30, 2024" (L35); Anderson's
  fraudulent card activity "December of 2024" (L74); CCPA notice letter sent "December 27, 2024"
  (L347); Ticketmaster's parent reported data-security risks "two months before the Data Breach"
  (L176).
- Numbers: dark-web ad "560 million customers full details" (L37, FAC para 473); Zappos "over 24
  million" customers (L84); Visa "over a hundred" CAMS alerts (L154, L334); nine injury categories
  (L41-42, L66-69); four traceability allegations (L150); three non-economic losses (L214); three
  CCPA dismissal grounds (L309); three Ticketmaster omissions (L370); 30-day CCPA pre-suit notice
  (L344-345); Montana CPA four elements (L224-226).
- Rulings by claim (Discussion): Article III standing found for all injury theories (actual/attempted
  fraud L72-77; imminent risk L79-94; lost PII value L96-101; mitigation L103-112; benefit of the
  bargain, Ticketmaster, L114-126; emotional distress L128-131); traceability incl. no-notice
  plaintiffs (L133-157); redressability (L159-161). Negligence (Montana law, L163-221): duty, breach,
  causation, damages and economic loss doctrine resolved for plaintiffs. Montana CPA (Mont. Code
  Ann. 30-14-101) survives vs Snowflake (consumers "through the intermediary", L237) and
  Ticketmaster (L223-266). Massachusetts Ch. 93A (vs Snowflake) survives; Ch. 93H has no private
  right (enforcement by Massachusetts AG, 93H s. 6) but 93A claim may proceed (L268-303). CCPA
  (California; Xian) survives, incl. Snowflake a "business" (1798.140(d)(1)) and pre-suit notice
  sufficient (L308-350). Breach of contract (Ticketmaster) analyzed "under Montana law" although
  plaintiffs' home states are "California, Massachusetts, Montana, New York, and Washington D.C."
  (L354-358): fails (L377-378; Terms of Use disclaimer). California UCL (Ticketmaster) "must be
  dismissed" (adequate legal remedy, Sonner) (L380-394). NY GBL 349 (Ticketmaster; New York
  plaintiffs Anderson and Fitzgerald) survives (L396-404).
- ORDER (L409-415): "1. Defendant Snowflake's Motion to Dismiss (Doc. 417) is DENIED." "2.
  Defendants Ticketmaster and Live Nation's Motion to Dismiss (Doc. 456) is GRANTED in part as to
  Count I (Breach of Contract) and Count IV (California UCL) and DENIED in part as to Count II
  (Montana CPA); Count III (NY GBL s. 349); Count V (CCPA); and Count VI (Negligence)." The text does
  not say "with prejudice", "without prejudice" or grant leave to amend for Counts I and IV; the
  alternative motion to strike is not separately ruled on. No LendingTree, AT&T, Advance Auto or
  Innive motion is decided here. Conclusion L407 restates the rulings.
- Hedged claims: "threat actors allegedly obtained the credentials" (L29); "Snowflake's alleged
  default setting turned off MFA" (L31); Snowflake's own announcement "became aware of potentially
  unauthorized access" (L35); Ticketmaster notice letter: exposed data "may include email, phone
  number, credit card information" (L37); notice letters "that their data may have been exposed"
  (L142); "plausibly could have been used ... This inference seems especially true" (L152); "at least
  plausible" (L154); FAC allegation "passport numbers may have been impacted for some individuals"
  and Ticketmaster told the Iowa Office of the Attorney General "passport numbers may have been
  impacted" (L335; hedge attaches to passport impact, not to name exposure); "Discovery ... may
  reveal that California Consumer Plaintiffs were not part of the limited number" (L340); UCL facts
  "appear to be the same facts" (L394).
- Rounded prose: "over a hundred" alerts; "560 million"; "majority received notice letters" (L142).
- Notes: Snowflake's "Shared Responsibility Model" (L237) and "Shared Responsibility Model and
  Security Addendum" (L251); Blackbaud FTC action May 17, 2024 (L251); Snowflake representation
  "industryleading features" (L181); Ticketmaster service-fee promise (L116, L252). Citation
  oddities: L166 "460 P.3d 882" vs L168 "406 P. 3d at 895" for Md. Cas. Co.; Caesars cited as
  "2025 U.S. Dist. LEXIS 15947" (L107, L137) and "159427" (L186 "LEXI", L221); L108 cites "In re
  Yahoo! Inc, Customer Data Sec. Breach Litig., 999 F. 3d 1247, 1263 (11th Cir. 2021)" while D02
  L40 cites the same reporter cite "999 F.3d 1247 (11th Cir. 2021)" as In re Equifax.
- Tables: not applicable.
- Amendments or contradictions: none stated; D05 applies earlier motions to the FAC (L25).
- Coverage: FULL. Read L1-70, L70-139, L139-208, L208-282, L282-356, L356-421 (all 46 pages).
  Unread: none.

## D06 - Order on Motions to Dismiss Financial Institution Plaintiffs' Claims

- Source: docs/uscourts_mtd_2_24_md_03126_34.txt | 36 ECF pages (Doc. 592, Filed 10/29/25,
  footers L17-L313); text L1-316.
- Written or submitted by: U.S. District Court, D. Mont., Butte Division (L4-6), "Cause No.
  2:24-MD-03126-BMM" (L8). Signer not named (L311 "DATED this 29th day of October, 2025.").
- Type, date, edition: "ORDER ON MOTIONS TO DISMISS FINANCIAL INSTITUTION PLAINTIFFS' CLAIMS"
  (L9-13); dated October 29, 2025 (L311).
- Entities and aliases: Introduction L15-24 repeats D05 L13-22 nearly verbatim (Snowflake hub,
  "Spoke Defendants", "Ticketmaster", "LendingTree", "Consumer Plaintiffs", "LAUSD Plaintiffs",
  "Financial Institution Plaintiffs", "Data Breach", FAC, "Advance Auto", "AT&T", "Innive", "Doe"
  Defendants). Representative plaintiff: New Orleans Firemen's Federal Credit Union ("Plaintiff" or
  "NOFFCU") (L43); class members are "financial institutions that issue payment cards, such as debit
  or credit cards, to their customers" (L44). "PCD" = payment card data (L71). Ticketmaster's movant
  name in ORDER: "Defendant Ticketmaster's and Defendant LiveNation's" (L309). Remijas v. Neiman
  Marcus Grp., LLC cited (L125; case citation only).
- Pleadings and ECF cites: FAC July 9, 2025 (Doc. 485) (L21); FI Plaintiffs' "Amended Complaint"
  April 8, 2025 (Doc. 393) (L22) = "Amended Representative Class Action Complaint ('Complaint')"
  filed April 8, 2025 (L44); claims: negligence, negligence per se, unjust enrichment, injunctive
  and declaratory relief (L44). Snowflake MTD filed June 26, 2025 (Doc. 469); Ticketmaster MTD June
  26, 2025 (Doc. 470) (L26); hearing October 6, 2025 (Doc. 569) (L26). Briefs cited: Doc. 471
  (Ticketmaster), Doc. 472 (Snowflake; L168), Doc. 503 and Doc. 504 (FI Plaintiffs), Doc. 524
  (Ticketmaster reply; L162 "Doc. 524 at n.2"), Doc. 527 (Snowflake; L91), and Doc. 417 at 24 (L76;
  Doc. 417 is Snowflake's consumer motion decided in D05).
- Background (L29-41) repeats D05 L27-37: April 2024 access; May 30, 2024 announcement (here cited
  "Doc. 393 at para 56", L33); May 24, 2024 advertisements (L34); Ticketmaster stolen-data list,
  notice letter "may include ..." (L36-38); "560 million customers full details" ad (L40).
- Numbers: "millions of credit and debit cards ('payment card data' or 'PCD') tied to Ticketmaster
  accounts" (L71, Doc. 504 at 11); Visa "over a hundred CAMS alerts" (L132, Doc. 393 para 143; also
  L86-89); Arby's quote: FTC "has pursued over fifty enforcement actions" (L261); Restatement
  section 145 four contacts (a)-(d) (L149-154); negligence per se five elements (L241); unjust
  enrichment three elements (L268-274).
- Choice of law (L142-165): Ticketmaster urges Louisiana law (Doc. 471 at 21-22, injury where
  plaintiffs operate); FI Plaintiffs urge Montana law (Doc. 503 at 15). Factors: conduct "occurred
  in Montana as far as the Court can tell"; "Snowflake is headquartered in Montana and has set up
  its servers in Montana" (L162); parties domiciled in Montana, Louisiana, California, others
  (L163); relationship center "remains unclear ... neutral" (L165). Holding: "Montana law most
  appropriately should be applied at the pleadings stage. The Court will make a conclusive
  choice-of-law finding after further discovery" (L165; Conclusion L299).
- Rulings by claim: standing found (injury L70-110: fraud reimbursement and card reissuance;
  traceability L111-132; redressability L134-137). Negligence (Montana law) duty/breach/causation/
  damages for both Snowflake and Ticketmaster (L138-214). Economic loss doctrine: depends on
  Louisiana law, declined; "Montana does not generally recognize the economic loss doctrine" (Jim's
  Excavating, L222-227); alternatively non-economic losses pleaded (L229-233). Negligence per se
  via FTC Act s. 5 (15 U.S.C. 45): Court "will adopt the more recent holding in Est. of Petersen"
  over Doyle v. Clark (L243-246; spelled "Est. of Peterson" L246); claim survives (L265). Unjust
  enrichment survives (L267-285; VISA Global Compromised Account Recovery Program argument rejected
  L285). Declaratory/injunctive relief dismissed under City of Reno v. Netflix (L290-296).
- ORDER (L301-309): "1. Defendant Snowflake's Motion to Dismiss (Doc. 469) is GRANTED in part as to
  Count IV (Declaratory and Injunctive Relief) and DENIED in part as to Count I (Negligence), Count
  II (Negligence per se), and Count III (Unjust Enrichment)." "2. Defendant Ticketmaster's and
  Defendant LiveNation's Motion to Dismiss (Doc. 470) is GRANTED in part as to Count IV ... and
  DENIED in part as to Count I ..., Count II ..., and Count III ...". No with/without prejudice or
  leave-to-amend language. Count numbering differs from D05 (D05 Count I = Breach of Contract).
- Hedged claims: "The Court does not see at this time how the harm ... proves too speculative"
  (L83); FI Plaintiffs: only partial PCD "confirmed stolen", CAMS alerts identified information
  "that may been included", Ticketmaster's representations "may have been incorrect" (L96);
  "more information may have been compromised" (L118); conduct in Montana "as far as the Court can
  tell at this point" (L162); "It can be inferred that this failure to implement MFA arose from
  Snowflake's failure to enforce its standards" (L188); Snowflake's no-benefit premise "may appear
  logical on the face" (L276).
- Contested fact: "Snowflake argues that it did require customers storing PCD to use MFA" (L187)
  vs FI allegation that Snowflake's "default setting turned off MFA" (L205, Doc. 393 para 51).
- Tables: not applicable. Lists: Restatement contacts (a)-(d) L149-154.
- Amendments or contradictions: none stated. Cross-doc: D06 places Snowflake's headquarters and
  servers in Montana (L162-163); D01 L76 says Snowflake "has its principal executive office in this
  district".
- Rounded prose beside exact figures: "millions of credit and debit cards" (L71); "over a hundred
  CAMS alerts" (L132); "over fifty enforcement actions" (L261); no exact counts printed.
- Coverage: FULL. Read L1-70, L70-139, L139-208, L208-267, L267-316 (all 36 pages). Unread: none.

## D07 - Order on Motions to Incorporate and/or Take Judicial Notice of Exhibits

- Source: docs/uscourts_mtd_2_24_md_03126_35.txt | 9 ECF pages (Doc. 593, Filed 10/29/25, footers
  L21-L115); text L1-118.
- Written or submitted by: U.S. District Court, D. Mont., Butte Division (L4-6), "Cause No.
  2:24-md-03126-BMM" (L8). Signer not named (L113 "DATED this 29th day of October 2025.").
- Type, date, edition: "ORDER ON MOTIONS TO INCORPORATE AND/OR TAKE JUDICIAL NOTICE OF EXHIBITS"
  (L9-12); dated October 29, 2025 (L113).
- Motion: Snowflake moves to incorporate/judicially notice "11 exhibits concurrently filed with
  Snowflake's Motion to Dismiss Plaintiffs' Second Amended Representative Class Action Complaint"
  (L14; motion Doc. 420; Snowflake brief Doc. 421 at 9-10 L73; Doc. 418 at 8, 62, 66 L69-70, L99).
  Plaintiffs' response Doc. 443: no opposition to Exhibits 1, 3, 4, 7-10; oppose 2, 5, 6, 11 (L15,
  L55, L62).
- Cross-reference: "The Court went into depth on the factual background ... on its previous order on
  Snowflake's motion to dismiss. (Doc. 591.)" (L18) = D05 (Doc. 591). Undisputed exhibits are
  incorporated "by reference to the Fourth Amended Complaint" (L56).
- List (Exhibits 1-11, L24-41; last item L41): 1 Snowflake's Shared Responsibility Model in effect at
  the time of breach; 2 "Snowflakes April 2024 Security Addendum in effect at the time of breach"; 3
  FTC article "Six Steps Toward More Secure Cloud Computing"; 4 Mandiant report "UNC5537 Targets
  Snowflake Customer Instances for Data Theft and Extortion"; 5 PCI Security Standards Council's
  PCI SSC Cloud Computing Guidelines "dated April 18" (no year printed); 6 Center for Internet
  Security's CIS Controls Cloud Companion Guide, dated March 25, 2022; 7 Notice of Data Incident from
  QuoteWizard by LendingTree to its consumers dated July 30, 2024; 8 Notices of Data Incident from
  QuoteWizard by LendingTree to Plaintiffs Aaron Macom, Antoun Nader, Linda Pierce, Nathan Thomas
  (4 names); 9 Notices of Data Breach from Ticketmaster to Plaintiffs Susie Garcia, Valerie Lozoya,
  Lavonne Madden, Jolinda Murphy, Molly O'Hara (5 names); 10 "Demand letter to Snowflake from
  Plaintiffs dated December 27, 2024"; 11 a 2017 report from the California Assembly Committee on
  Privacy and Consumer Protection on amendments to the CCPA.
- Rulings: Exhibit 2 judicially noticed as publicly available (L64-70; L70 reads "The Court judicial
  notice of" [sic]); Exhibit 5 incorporated by reference (FAC paras 192-194, n.65, 68-69; hyperlink;
  L72-83; L83 typo "FCI Guidelines"); Exhibit 6 incorporated (FAC para 197, n. 71-74; L85); Exhibit
  11: Court "takes judicial notice of the existence of legislative history ... but declines to take
  judicial notice of the document in its entirety and the facts contained within" (L90-104).
- ORDER (L106-112): "Snowflake's Motion for Judicial Notice and Incorporation by Reference in Support
  of Snowflake's Motion to Dismiss (Doc. 420) is GRANTED." "- The Court incorporates by reference
  and/or takes judicial notice of Exhibits 1-11." "- The Court shall take judicial notice of the
  existence of Exhibit 11. The Court declines to take judicial notice of the facts contained within
  Exhibit 11." (Motion stated as GRANTED although the Exhibit 11 facts are declined; no "in part"
  wording.)
- Rules: Fed. R. Evid. 201(b)(2), 201(c)(2), 201(a) advisory note (L49-52, L91); incorporation by
  reference (Khoja; "Mere mention of a document proves insufficient", L46); CCPA pre-suit notice "30
  days' written notice" Cal. Civ. Code 1798.150(b) (L101).
- Hedged claims: Snowflake's argument that the demand letter, "if it constitutes notice under CCPA",
  would defeat the notice-and-cure purpose (L99).
- Notes: Xian's pre-suit notice called "vague and improper" by Snowflake (L99). Security Addendum
  "establishes that both Snowflake and ... the Spoke Defendants, agreed to take security measures"
  (L69).
- Tables: not applicable.
- Amendments or contradictions: D07 calls Snowflake's underlying motion one to dismiss the "Second
  Amended Representative Class Action Complaint" (L14) while D05 (Doc. 591) applies Snowflake's
  motion (Doc. 417) to the Fourth Amended Complaint (D05 L20-25). D07 Exhibit 10 date (December 27,
  2024) matches D05 L347 CCPA notice letter date.
- Rounded prose beside exact figures: not applicable (counts are exact: 11 exhibits; 7 undisputed,
  4 disputed).
- Coverage: FULL. Read L1-118 (all 9 pages). Unread: none.

## D08 - Order on Motion to Dismiss LAUSD Plaintiffs' Claims

- Source: docs/uscourts_mtd_2_24_md_03126_36.txt | 22 ECF pages (Doc. 594, Filed 10/29/25,
  footers L16-L218); text L1-221.
- Written or submitted by: U.S. District Court, D. Mont., Butte Division (L4-6), "Cause No.
  2:24-md-03126-BMM" (L8). Signer not named (L216 "DATED this 29th day of October 2025.").
- Type, date, edition: "ORDER ON MOTION TO DISMISS LAUSD PLAINTIFFS' CLAIMS" (L9-12); dated October
  29, 2025 (L216).
- Entities and aliases: Introduction L14-22 repeats D05/D06 boilerplate (same aliases). Los Angeles
  Unified School District ("LAUSD", L29; "LAUSD Plaintiffs" L16); Innive (service provider; "LAUSD
  contracted with Innive to store the personal information", "Innive used Snowflake's systems", L29;
  "its service provider, Innive", L99). LAUSD Plaintiffs = "eight students from the LAUSD and four
  of their parents" (L31, FAC paras 142-53). Named: Rundle (para 144, parent), Singer (para 147),
  Harrison (para 150), Price (para 153) (L112). Remijas v. Neiman Marcus Grp. quoted (L87; citation
  only). CCPA expanded as "California Consumer Protection Act" (L53) and "California Consumer
  Privacy Act" (L170) within this order; heading "CALIFORNIA CPA CLAIM" (L169).
- ECF cites: Snowflake MTD Doc. 500 (brief Doc. 501 at 12-13, 21-28, 31-32); LAUSD opposition Doc.
  519 (at 19, 20, 32); hearing October 6, 2025 (Doc. 569) (L23-24); FAC Doc. 485; also "Doc. 458
  paras 355, 934, 936, 974-77" (L150) and "Doc. 28 at 28" (L171) for Snowflake's CCPA arguments, and
  Doc. 418 at 60-61 (L159, Snowflake's consumer brief).
- Cross-references to D05: "The Court previously described the facts ... in its order on Snowflake
  and Ticketmaster's motion to dismiss Consumer Plaintiffs' claims. (Doc. 591.)" (L27-28); other
  injuries handled by "The previous order on Snowflake's motion to dismiss Consumer Plaintiffs'
  claims ... (Doc. 591.)" (L66); negligence survives "for similar reasons as outlined in the Court's
  order on Snowflake's motion to dismiss against Consumer Plaintiffs" (L150); Montana CPA elements
  two-four "For the reasons stated in the order on Snowflake's motion to dismiss Consumer
  Plaintiffs' claims" (L157).
- Events/dates (as alleged): hackers obtained data "from Snowflake's servers in April of 2024";
  LAUSD information "sold on the dark web on June 1, 2024" (L86, FAC para 975); California class
  members' pre-suit notice "December 27, 2024" (L205, FAC para 363; notice "did not specifically
  identify LAUSD Plaintiffs", L205).
- Numbers: dark-web ad "Details 4M+ Student (grades K-12)" (L33, FAC para 975); independent
  investigation "uncovered 11 GB of data" (L106); seven harms (L37, L63); 8 students + 4 parents
  (L31); Zappos "over 24 million" (L79); CCPA notice "within 30 days" (L203); three CCPA dismissal
  grounds (L170-172); Snowflake: no fraud "within a year of the data breach" (L120).
- Lists: stolen data categories (L33, L106, L112); harms (1)-(7) (L37/L63); CCPA Personal Information
  items (ii)/(iii) (L184-190).
- Rulings: standing (imminent risk L68-87; loss of control L89-106; emotional distress L110-113;
  traceability L115-138; redressability L139-142); negligence survives (L143-152); Montana CPA
  survives, LAUSD Plaintiffs consumers via an indirect relationship (L154-167); CCPA survives:
  Snowflake a "business" via work with Innive (L170-177), personal information plausibly stolen
  (L195-197), pre-suit notice not a ground for dismissal (L202-205). Conclusion L208.
- ORDER (L210-211): "Defendant Snowflake's Motion to Dismiss (Doc. 500) is DENIED." No counts listed.
- Exclusion/negative facts: "Innive, the service provider, gave no notice to LAUSD Plaintiffs of any
  breach" (L34); "no LAUSD Plaintiffs received a data breach notice and some LAUSD Plaintiffs allege
  they do not know whether their children's data was compromised" (Snowflake's argument, L101); the
  school district and Innive "failed to provide notice" (L197); LAUSD Plaintiffs "have not yet had
  their information misused" (L82).
- Hedged claims: LAUSD Plaintiffs' explanation for no notice: "plausible explanations exist ...
  including a potential ongoing criminal investigation or simple negligence of duty" (L197); data
  "allegedly included" (L133); "Given the information available before discovery" (L195); Singer:
  records "could follow him/her" (L112, quoted fear).
- Notes: citation spellings "Scheibe" (L103) vs "Schiebe" (L197); Landon cited "2024 WL 5317240"
  (L128) and "2024 WL 531240" (L133).
- Tables: not applicable.
- Amendments or contradictions: none stated.
- Rounded prose beside exact figures: "4M+ Student" (ad, L33); "11 GB" (L106); no exact LAUSD
  student count printed.
- Coverage: FULL. Read L1-85, L85-164, L164-221 (all 22 pages). Unread: none.

## D09 - Order on Motion to Compel Arbitration (LendingTree)

- Source: docs/uscourts_mtd_2_24_md_03126_37.txt | 11 ECF pages (Doc. 595, Filed 10/30/25, footers
  L17-L105); text L1-108.
- Written or submitted by: U.S. District Court, D. Mont., Butte Division (L4-6), "Cause No.
  2:24-md-03126-BMM" (L8). Signer not named (L103 "Dated this 30th day of October, 2025.").
- Type, date, edition: "ORDER ON MOTION TO COMPEL ARBITRATION" (L9-10); dated October 30, 2025
  (L103).
- Entities and aliases: "LendingTree" = LendingTree, LLC and QuoteWizard.com, LLC, "a subsidiary of
  LendingTree, LLC" (L12). "LendingTree Plaintiffs" = Linda Pierce, Aaron Macom, Nathan Thomas,
  Antoun Nader (L17; same four names as D07 Exhibit 8 L36, different order). Two web forms: "the
  QuoteWizard form" and "the LendingTree form" (L69, L76). Oberstein v. Live Nation Ent., Inc. (L80)
  and Chabolla v. ClassPass, Godun v. JustAnswer, Berman v. Freedom Fin. Network cited (case names
  only).
- Cross-reference: "The Court fully addressed the facts ... in its order on Snowflake Inc.'s and
  Ticketmaster LLC's Motion to Dismiss Consumer Plaintiffs' claims. (Doc. 591.)" (L15) = D05.
- Claims vs LendingTree in FAC (Doc. 485 paras 683-720): negligence, Washington Consumer Protection
  Act (Wash. Rev. Code 19.86.020 et seq.), unjust enrichment (L20).
- Procedural dates/ECF: Motion to Compel Arbitration filed May 16, 2025 (Doc. 424; brief Doc. 425)
  (L12, L28-29); leave for arbitration discovery (Doc. 465) (L29); LendingTree served discovery
  responses August 8, 2025 (Doc. 549 at 11) (L29-30); LendingTree Plaintiffs' Response September 12,
  2025 (Doc. 549) (L30); hearing October 6, 2025 (Doc. 569) (L30); LendingTree consented to Ninth
  Circuit law at the hearing (Doc. 576 at 184) (L30). Exhibits: Doc. 425-1 at 51-52 (terms of use,
  arbitration clause), Doc. 549-1 at 50 and Doc. 560-1 at 24 (screenshots), Doc. 560-1 paras 7-14
  (current userflow).
- Definitions/rules: arbitration clause with delegation clause ("any dispute or disagreement
  regarding the enforceability, applicability or interpretation of any provision of this
  Agreement...") and class-action waiver; claims "arbitrated individually" (L24-27). "sign-in wrap"
  enforceable if the party "provid[ed] reasonabl[e] conspicuous notice" and the consumer
  "unambiguously manifest[ed] his or her assent" (Chabolla, L44). Godun context factors (1)-(4)
  (L49-51). Burden: valid written agreement + encompasses dispute (Ashbey, L39).
- Lists: LendingTree's "following five reasons" (L45) numbered (1), (2), (3), (4), (4) [two items
  labeled (4)]; includes "nine-point Arial font with a blue hyperlink" and button text "consent,
  acknowledge, and agree". Form text: "I acknowledge that I have read, understand, and agree to this
  Website's Privacy Policy and Terms of Use." (L82). Buttons "Get My Auto Quotes" / "View My Rates"
  (L74, L82); QuoteWizard blue text "our marketing and re-marketing network, and up to eight
  insurance companies of their affiliates" (L76).
- Rulings: context of the transaction weighs against conspicuous notice (L55-61; plaintiffs never
  entered credit card information or downloaded an app); visual design weighs against (L63-78:
  QuoteWizard "tiny gray font"; LendingTree form same white color but smaller; notice below the
  button; blue links on dark navy background); no unambiguous assent (L80-85); "The Arbitration
  Agreement proves unenforceable. 9 U.S.C. s. 2." (L87); stay unwarranted (L91); scope argument
  (Doc. 425 at 28), "as a matter of law" argument (Doc. 549 at 30) and unconscionability (Doc. 549
  at 33) not addressed (L91-97).
- ORDER (L100-101): "Defendant LendingTree's Motion to Compel Arbitration (Doc. 424) is DENIED."
- Hedged claims: LendingTree "alleges that the design and layout of the userflow has remained
  unchanged since January 2017" (L94-96, Doc. 560-1); "Smartphone and tablet users likely would have
  difficulties reading" (L72); hyperlinks "would appear difficult ... to read on a smartphone"
  (L76); same-color choice "likely would fail to 'alert a reasonably prudent user'" (L76);
  LendingTree Plaintiffs "believed LendingTree's websites functioned as search engines" (L59).
- Numbers/dates: nine-point font (L45); "up to eight insurance companies" (L76); January 2017
  (L96); May 16, 2025; August 8, 2025; September 12, 2025; October 6, 2025.
- Tables: not applicable.
- Amendments or contradictions: none stated.
- Rounded prose beside exact figures: not applicable.
- Coverage: FULL. Read L1-108 (all 11 pages). Unread: none.

## D10 - Order on Ticketmaster's Motion to Compel Discovery from Consumer Plaintiffs

- Source: docs/uscourts_mtd_2_24_md_03126_45.txt | 8 ECF pages (Doc. 739, Filed 06/29/26, footers
  L21-L79); text L1-82.
- Written or submitted by: U.S. District Court, D. Mont., Butte Division (L4-6), "Cause No.
  2:24-md-03126-BMM" (L8). The order speaks as "The Court" and describes the Special Master in the
  third person (L28); the issuing judicial officer is not named (L77 "DATED this 29th day of June,
  2026."). Whether the district judge or Magistrate Judge Johnston signed is not stated in the text.
- Type, date, edition: "ORDER ON TICKETMASTER'S MOTION TO COMPEL DISCOVERY FROM CONSUMER PLAINTIFFS"
  (L9-12); dated June 29, 2026 (L77).
- Entities and aliases: "Defendants Live Nation Entertainment, Inc. and Ticketmaster L.L.C.
  (collectively, 'Ticketmaster')" (L14-16); background boilerplate L24 uses "Ticketmaster, LLC, and
  Live Nation Entertainment, Inc. (collectively 'Ticketmaster')" (two spellings in one order).
  Consumer Plaintiffs (L24 boilerplate, same as D05). Named: Plaintiff Garcia (junk emails), Plaintiff
  Murphy (lack of spam emails) (L59). Special Master: "U.S. Magistrate Judge John T. Johnston"
  appointed under Fed. R. Civ. P. 53 (Doc. 383) (L28).
- Procedural ECF: motion Doc. 701 (brief Doc. 702); opposition Doc. 708; hearing June 11, 2026 (Doc.
  712) (L16); discovery motions "from Doc. 680 to Doc. 738" (L30); Consumer Plaintiffs' responses and
  objections served February 2, 2026 (Doc. 702 at 9) (L33); Ticketmaster raised concerns February 6,
  2026 (L34).
- Background facts: "Ticketmaster suffered a security breach in April and May of 2024 that
  compromised the financial and personal information of hundreds of millions of customers after a
  third party accessed their cloud platform." (L26); "This multi-district litigation commenced on
  October 8, 2024 ... (Doc. 1.)" (L26); "Substantial completion of discovery documents is due on July
  31, 2026. (Doc. 606 Ex. 1.)" (L26).
- Rulings: declines to hold objections waived (untimely "several days after the agreed upon
  deadline") and declines Consumer Plaintiffs' meet-and-confer objection (L47-50); "the numerous
  discovery motions filed recently appear to be a tit-for-tat game" (L50); Consumer Plaintiffs must
  "either produce additional requested information, or certify that such materials do not exist, or
  no longer exist" (L52, L56, L59); interrogatories answered under oath with efforts detailed (Gersh,
  L56); credit reports: Consumer Plaintiffs "less than forthcoming", should produce current reports
  (L64); release documents "allegedly signed by three named Consumer Plaintiffs in a mass
  arbitration with Ticketmaster" - Court "declines to further address" (L64-65); produce available
  supplemental information on alleged Ticketmaster misrepresentations (L66); "full supplementation by
  the close of discovery or certify under oath" (L70); "Ticketmaster requests no sanctions ... The
  Court will not order sanctions at this time" (L71).
- ORDER (L73-75): "Ticketmaster's Motion to Compel (Doc. 701) is GRANTED."
- Deadlines: July 31, 2026 substantial completion (L26, Doc. 606 Ex. 1); "by the close of discovery"
  (date not given) (L70).
- Hedged claims: motions "appear to be a tit-for-tat game" (L50); evidence "may include" notices,
  fraud documentation, communications (L52); plaintiffs "may not have meticulously catalogued" (L54);
  "The Court believes that Consumer Plaintiffs have been less than forthcoming" (L64); "the parties
  may have agreed on discovery related to the release documents allegedly signed by three named
  Consumer Plaintiffs" (L64); information "might not rise to the exact level requested" (L66).
- Numbers: three named Consumer Plaintiffs signed releases (alleged) (L64); "hundreds of millions of
  customers" (L26).
- Tables: not applicable.
- Amendments or contradictions: L26 breach window "April and May of 2024" (Ticketmaster) vs D01
  "approximately April to June 2024" and D05/D06/D08 "April of 2024" access (see Shared ground).
- Rounded prose beside exact figures: "hundreds of millions of customers" (L26); no exact figure.
- Coverage: FULL. Read L1-82 (all 8 pages). Unread: none.

## D11 - Order on Snowflake's Motion to Compel Discovery from Consumer Plaintiffs

- Source: docs/uscourts_mtd_2_24_md_03126_46.txt | 12 ECF pages (Doc. 740, Filed 06/29/26, footers
  L18-L103); text L1-106.
- Written or submitted by: U.S. District Court, D. Mont., Butte Division (L4-6), "Cause No.
  2:24-md-03126-BMM" (L8). Speaks as "The Court"; signer not named (L101 "DATED this 29th day of
  June, 2026."). Special Master paragraph L24 (Magistrate Judge John T. Johnston, Doc. 383).
- Type, date, edition: "ORDER ON SNOWFLAKE'S MOTION TO COMPEL DISCOVERY FROM CONSUMER PLAINTIFFS"
  (L9-12); dated June 29, 2026 (same date and same day's filing as D10).
- Background L16-27 repeats D10 L19-30 (hub-and-spoke; party aliases; "Ticketmaster suffered a
  security breach in April and May of 2024 ... hundreds of millions of customers"; MDL "commenced on
  October 8, 2024"; substantial completion "due on July 31, 2026. (Doc. 606 Ex. 1.)"; Special Master;
  docket "from Doc. 680 to Doc. 738").
- Procedural ECF: Snowflake motion Doc. 721 (brief Doc. 722; exhibits Ex. A at 46:1-8, Ex. B lawyer
  letter, Ex. C at 141 interrogatory, Ex. F at 5-6 RFP); Consumer Plaintiffs' opposition Doc. 727 and
  motion for protective order Doc. 726 (L14).
- Discovery requests (L29-31): Interrogatories No. 8 and No. 9 and RFP No. 9 on industry standards;
  RFP No. 8 on emotional distress incl. medical or psychiatric records. RFP text (L49): documents on
  mental, emotional, or psychological health "following the [Data Breach] and for the five (5) years
  preceding the [Data Breach]". Court's characterization (L53): "seven years of their 'mental,
  emotional, or psychological health conditions or disorders.'" Interrogatory text (L80): "Identify
  each industry standard You contend Snowflake breached, the industry to which You contend it applies,
  the source of that standard, and the identities of other entities to which You contend that
  standard applies."
- Numbers: stipulation to nominal damages "of an amount no more than $20 per class member" (L31);
  five years preceding (L49); seven years (L53); lawyer-letter list of six "purported industry
  standards": "(1) NIST-800; (2) ISO27001; (3) PCI DSS; (4) FERPA; (5); HIPAA; and (6) FTC Act,
  Section 5." (L80, last item FTC Act s. 5; item 5 printed as "(5); HIPAA").
- Definitions: "garden variety and expected aggravation and anxiety" (Consumer Plaintiffs, L31);
  "'Garden-variety emotional distress' involves 'ordinary or commonplace emotional distress, that
  which is simple or usual.'" (Pringle, L66); non-garden-variety "may be complex, such as that
  resulting in a specific psychiatric disorder" (L66); general phrases ("mental and emotional
  distress", "pain and suffering", "stress, internal turmoil, trauma, and anxiety") are garden variety,
  while "post-traumatic stress disorder, depression, insomnia, and suicidal ideation" are not (L70);
  Stallworth "middle ground approach" to psychotherapist-privilege waiver (L72).
- Positions: Consumer Plaintiffs assert no standalone/independent emotional distress claim (L31,
  L55); stipulation that "all of our plaintiffs had angst and frustration from other sources in their
  life" (L50, L55); Snowflake says emotional-distress allegations "helped them defeat Defendants' Rule
  12 motions to dismiss in establishing injury-in-fact" (L51; cf. D05 L128-131); Consumer Plaintiffs
  point to FAC "an entire section" on industry standards (Doc. 485 paras 179-198, 296) (L85).
- Rulings: medical records - "The Court agrees with Consumer Plaintiffs"; nominal garden-variety
  assertions "fail to open the door to burdensome and extensive discovery" (L53-58); Snowflake can
  cross-examine (L57, L77); warning: plaintiffs "may open the door ... should their emotional distress
  allegations extend beyond garden-variety anxiety, aggravation, and frustration" (L74). Industry
  standards - request "inappropriate, overbroad" and seeks work product/legal conclusions beyond fact
  discovery (L87-90). "The Court declines to grant Snowflake's motion" (L91).
- ORDER (L93-96): "Snowflake's Motion to Compel (Doc. 721) is DENIED. IT IS FURTHER ORDERED that
  Consumer Plaintiffs' Motion for Protective Order (Doc. 726) is GRANTED."
- Hedged claims: harm "may be causally attributable to the Data Breach as opposed to another factor"
  (L57, Snowflake's right to test); conditional "may open the door" (L74); "these standards might
  apply to other actors" (L90).
- Tables: not applicable.
- Amendments or contradictions: none stated; RFP's "five (5) years preceding" plus post-breach period
  vs Court's "seven years" (L49 vs L53) are both printed.
- Rounded prose beside exact figures: "hundreds of millions of customers" (L22); cap "no more than
  $20 per class member" (L31).
- Coverage: FULL. Read L1-106 (all 12 pages). Unread: none.

## D12 - Order on Consumer Plaintiffs' Motion to Compel Discovery from Ticketmaster

- Source: docs/uscourts_mtd_2_24_md_03126_47.txt | 22 ECF pages (Doc. 744, Filed 07/01/26, footers
  L21-L191); text L1-194.
- Written or submitted by: U.S. District Court, D. Mont., Butte Division (L4-6), "Cause No.
  2:24-md-03126-BMM" (L8). Speaks as "The Court"; signer not named (L189 "DATED this 1st day of July,
  2026."). Special Master paragraph L27-30.
- Type, date, edition: "ORDER ON CONSUMER PLAINTIFFS' MOTION TO COMPEL DISCOVERY FROM TICKETMASTER"
  (L9-12); dated July 1, 2026 (L189).
- Entities and aliases: "Defendants Live Nation Entertainment, Inc. and Ticketmaster L.L.C.
  (collectively, 'Ticketmaster')" (L14); boilerplate L24 "Ticketmaster, LLC, and Live Nation
  Entertainment, Inc." CrowdStrike ("a cybersecurity forensics company, not a law firm", L62); Paul
  Hastings law firm (L62, L93); DOJ antitrust litigation (L168-173). Background L19-30 repeats D10/D11
  ("April and May of 2024", "hundreds of millions of customers", MDL "commenced on October 8, 2024",
  substantial completion "due on July 31, 2026", Doc. 606 Ex. 1; Special Master Doc. 383; Docs.
  680-738).
- Procedural ECF: Consumer Plaintiffs' motion Doc. 680 (brief Doc. 682); Ticketmaster opposition and
  "responsive motion for protective order" (Doc. 697, Doc. 698) (L15); hearing June 11, 2026 (Doc.
  712) (L15-16); Ticketmaster reply Doc. 725 (L77); Doc. 735 (Ticketmaster, L71, L121, L169); Doc. 707
  at 22-23 (L168-173); Doc. 681 at 14 (Special Master's custodian instruction quoted, L173); Doc. 702
  at 15, 28-31 (Ticketmaster brief, cited L33-39).
- Dates: "Ticketmaster retained CrowdStrike to handle the investigation of the breach on May 17,
  2024. (Doc. 702 at 15.)" (L33); "CrowdStrike had produced no 'final written report' as of June 21,
  2026. (Doc. 682 at 9, citing Ex. 1 at 14.)" (L33; printed date is later than the June 11, 2026
  hearing on this motion, L15); Ticketmaster agreed to produce a privilege log on May 21, 2026, after
  the Special Master instructed Consumer Plaintiffs to file a motion to compel (L34); Special Master's
  custodian window "from January 1, 2022, through December 31, 2024" (L173).
- Numbers: Ticketmaster's Interrogatory No. 4 answer: "what it paid Snowflake for cloud storage in
  three years - $750,000 (2022), $1,312,500 (2023), $1,386,467.97 (2024)" (L144; Doc. 682 at 24;
  dollars, exact to cents for 2024); "the amount it has paid Snowflake from 2022 to 2024" (L165, L167;
  no total printed); Burlington four factors (L131); McMenamins factors (L107-109); sanctions "$5000"
  (L184, L187); "increase the sanctions ten-fold each subsequent time" (L184); payment "within 15 days
  of this order" (L187).
- Requests: Interrogatory No. 4 (fee revenue allocated to cybersecurity, fraud prevention, data
  protection) (L142); Document Requests Nos. 12 and 14 (L144; "FRP 12" L146); RFP #4 ("the relevant
  FRP", L91, breach investigation); Rule 30(b)(6) witness "unable to answer" (L144). Service-fee
  promise quoted: "the costs of the technology, people and resources needed to provide a safe and
  secure ticket-buying experience" (L36-38; cf. D05 L116).
- Rulings: (I) breach-investigation documents: attorney-client privilege - primary purpose test (In re
  Grand Jury), "it appears Ticketmaster has abandoned" the assertion (L77); "The Court denies
  Ticketmaster's assertions of attorney-client privilege to the extent Ticketmaster has not already
  abandoned this assertion" (L95). Work product - "because of" test (Torf); Court "remains unpersuaded
  that work-product privilege applies" (L106); compels "any documents or information Ticketmaster
  possesses related to the CrowdStrike Data Breach investigation, including but not limited to
  CrowdStrike's investigative results"; exception: "not compelling production of documents created by
  counsel, counsel's edits, or communications by counsel" (L128). Privilege-log waiver: "declines to
  conclude that Ticketmaster has waived its privileges" (L138). (II) fee/cybersecurity documents:
  compels "a good-faith response ... beyond simply the amount it has paid Snowflake from 2022 to 2024";
  "does not compel production of transaction-by-transaction breakdowns" (L163-165); suggests requests
  for admission or Rule 37(b)(2)(A)(i) established-fact order (L167); orders custodian search "now" to
  the extent not done (L173). (III) Sanctions under Rule 37 imposed (L180-184).
- ORDER (L186-187): "Consumer Plaintiffs' Motion to Compel (Doc. 680) is GRANTED. IT IS FURTHER
  ORDERED that Ticketmaster's Motion for Protective Order (Doc. 697) is DENIED. Ticketmaster shall pay
  $5000 to Consumer Plaintiffs as sanctions for its abuse of the discovery process within 15 days of
  this order."
- Hedged claims: "it appears Ticketmaster has abandoned" (L77); "It appears from the agreement that
  the primary focus of the investigation was for business reasons" (L85); "'a primary purpose test'
  could prove appropriate"; "it appears that the non-legal, business purpose ... predominated"; "The
  agreement suggests" (L89); results communicated "in some form, though it may not have been a formal
  final report" (Ticketmaster concession, L123); facts "likely would have been produced" (L123); "It
  appears to the Court that Ticketmaster has been less than forthcoming" (L151); "The Court believes
  that responsive documents must exist" (L163); Ticketmaster "must have allocated at least some
  percentage" (L152, firm inference).
- Negative/exclusion facts: Ticketmaster "does not allocate ticket or fee services to cybersecurity
  on a transaction-by-transaction basis" and "does not assign a dollar amount or percentage of each
  fee to cybersecurity" (L39, L146); In re Cap. One preexisting retainer "a fact not shared here"
  (L69); "to date, Ticketmaster has provided no documents, privilege log, or information regarding
  CrowdStrike's investigation" (L34).
- Tables: not applicable (three-year payment figures are inline prose, L144).
- Amendments or contradictions: none stated in-document beyond the June 21, 2026 date noted above.
- Rounded prose beside exact figures: exact yearly Snowflake payments at L144 ($750,000; $1,312,500;
  $1,386,467.97) vs later prose "the amount it has paid Snowflake from 2022 to 2024" with no total
  printed (L165, L167); "hundreds of millions of customers" (L25).
- Coverage: FULL. Read L1-100, L100-194 (all 22 pages). Unread: none.

## D13 - Order on Snowflake's Motion to Compel Discovery from Defendant Innive Inc.

- Source: docs/uscourts_mtd_2_24_md_03126_49.txt | 8 ECF pages (Doc. 760, Filed 07/16/26, footers
  L21-L87); text L1-90.
- Written or submitted by: U.S. District Court, D. Mont., Butte Division (L4-6), "Cause No.
  2:24-md-03126-BMM" (L8). Speaks as "The Court"; signer not named (L85 "DATED this 16th day of July
  2026."). Special Master paragraph L27-28.
- Type, date, edition: "ORDER ON SNOWFLAKE'S MOTION TO COMPEL DISCOVERY FROM DEFENDANT INNIVE INC."
  (L9-12); dated July 16, 2026 (L85).
- Entities and aliases: "Defendant Innive Inc. ('Innive')" (L15-16; D05/D06/D08 write "Innive, Inc.").
  Innive's former counsel: Robert A. Kashfian, Troy D. Krouse, Kuan-Ting Huang of Kashfian and
  Kashfian LLP; local counsel Matthew McKeon of Datsopoulos, MacDonald, & Lind, P.C. (L34). "Innive's
  purported current counsel" (unnamed, L49-50). Background L19-28 repeats D10-D12 boilerplate.
- Cross-references: "The Court filed several orders resolving these discovery disputes. (Doc. 739,
  Doc. 740, Doc. 744.)" (L28) = D10, D11, D12. Earlier withdrawal order: Doc. 671, granted May 1, 2026
  (L34; conditions quoted "Id. at 5-6", L48).
- Procedural ECF: Snowflake motion Doc. 749 (brief Doc. 750 at 5-11; Ex. B at 1); "Innive has failed
  to respond" (L16).
- Dates/deadlines: Innive's communications with former counsel "ceased since March 23, 2026" (Doc.
  671 at 2) (L34); withdrawal granted May 1, 2026 (L34); condition 1: new counsel "within twenty (20)
  days of this Order granting withdrawal" (L36); Innive's deadline to respond to Snowflake's discovery
  requests "passed on May 10, 2026" (L50); deadline to enter appearance of new counsel "lapsed on May
  21, 2026" (L51; L72 "by May 21, 2026"). (May 1 + 20 days = May 21, consistent.)
- Lists: withdrawal conditions 1-5 (L36-46; last: "5. Innive promptly shall produce all relevant
  insurance policies and related coverage material"); Rule 37(b)(2)(A)(i)-(vii) sanctions list
  (L62-65; last "(vii) treating failure to obey most kinds of orders as contempt").
- Snowflake's needs (L68): "what data was stored in the Innive Snowflake environment, who was
  responsible for Innive's cybersecurity controls, and what Snowflake-provided and/or third-party
  cybersecurity controls Innive did or did not implement"; prejudice re scheduling depositions of
  LAUSD Plaintiffs (L68).
- Rulings: "a straightforward Rule 37 violation" (L69); Court "remains unconvinced" that compelling
  and sanctioning will produce anything, but "mere entry of default or dismissal of Innive will not
  solve Snowflake's demonstrated prejudice" so grants motion (L69-72); sanctions: "The Court warned the
  parties that it initially would award sanctions of $5000 for discovery abuses and increase the
  sanctions ten-fold each subsequent time. The Court will impose $5000 in sanctions against Innive to
  be awarded to Snowflake." (L78; same warning sentence as D12 L184).
- ORDER (L82-84): "Snowflake's Motion to Compel (Doc. 749) is GRANTED. The Court orders Innive to
  respond to Snowflake's discovery requests within 7 days of this order. Innive shall pay $5000 to
  Snowflake as sanctions for its abuse of the discovery process within 15 days of this order."
- Negative facts: Innive "has produced no documents ..., served no interrogatory responses, and has
  served no objections" (Snowflake, L68); "No new counsel for Innive has entered an appearance on the
  docket" (L48); former local counsel "not in receipt of any documents from Innive" (L50).
- Hedged claims: failure to find counsel "may result in the entry of default" (L36, quoted condition);
  "additional applicable insurance coverage may need to be located" (L40); "It appears that Innive's
  former counsel have complied" (L48); "The Court remains skeptical whether sanctions will prompt
  Innive to respond" (L78).
- Tables: not applicable.
- Amendments or contradictions: none stated. D13's date (July 16, 2026) is 15 days after D12 (July 1,
  2026); D13 says nothing about Ticketmaster's D12 sanction payment.
- Rounded prose beside exact figures: "hundreds of millions of customers" (L25); otherwise not
  applicable.
- Coverage: FULL. Read L1-90 (all 8 pages). Unread: none.

## D14 - Order on Snowflake's Motion to Compel Discovery from LendingTree and QuoteWizard

- Source: docs/uscourts_mtd_2_24_md_03126_52.txt | 13 ECF pages (Doc. 780, Filed 08/19/26, footers
  L19-L115); text L1-118.
- Written or submitted by: U.S. District Court, D. Mont., Butte Division (L4-6), "Cause No.
  2:24-md-03126-BMM" (L8). Speaks as "The Court"; signer not named (L113 "DATED this 19th day of
  August 2026."). Special Master paragraph L27-30.
- Type, date, edition: "ORDER ON SNOWFLAKE'S MOTION TO COMPEL DISCOVERY FROM LENDINGTREE AND
  QUOTEWIZARD" (L9-13); dated August 19, 2026 (L113). Latest-dated document in the bundle.
- Entities and aliases: "LendingTree, LLC and QuoteWizard.com, LLC (collectively 'LendingTree')"
  (L15); boilerplate shortened to "and LendingTree ('Consumer Plaintiffs')" (L23). "Four named
  plaintiffs (collectively 'LendingTree Plaintiffs') filed a class action against QuoteWizard and
  LendingTree" (L34; names not repeated here; D09 L17 and D07 L36 name four). Coinbase, Inc. v.
  Bielski, 599 U.S. 736 (2023) (L16).
- Background variants vs D10-D13: substantial completion "was due on July 31, 2026" (past tense,
  L25; D10-D13 "is due"); docket range "from Doc. 680 to Doc. 779" (L30; D10-D13 "to Doc. 738");
  orders list "(Doc. 739, Doc. 740, Doc. 744, Doc. 760, Doc. 761, Doc. 766.)" (L30) = D10, D11, D12,
  D13 plus Docs. 761 and 766 (not in bundle).
- Procedural ECF/dates: Snowflake motion Doc. 773 (brief Doc. 774 at 1, 5-8; Ex. A meet-and-confer;
  Ex. B subpoena topics; Ex. 7); LendingTree opposition Doc. 778 (at 8-9); Doc. 779 at 4 (L103).
  Snowflake served "a Rule 45 subpoena and Rule 30(b)(6) deposition notices ... on July 7, 2026"
  seeking "fifteen topics" (incl. "the Incident", LendingTree's cybersecurity controls, the
  compromised account and credentials, the data, LendingTree's investigation and customer
  communications) (L31). LendingTree responded "July 27, 2026, with a single objection" based on its
  pending interlocutory appeal of the order denying arbitration "(Doc. 595)" and Coinbase (L32).
- Cross-references to D09: "LendingTree moved to compel arbitration as to these claims. (Doc. 424.)
  The Court denied LendingTree's motion to compel arbitration. (Doc. 595.) LendingTree promptly
  appealed the Court's decision to the Ninth Circuit. (See Doc. 596.)" (L38-40). Claims against
  LendingTree: negligence, Washington Consumer Protection Act, unjust enrichment (Doc. 485 paras
  683-720, 749) (L35-38; D09 cites paras 683-720). Claims of LendingTree Plaintiffs against Snowflake:
  negligence and Montana Unfair Trade Practices and Consumer Protection Act (Doc. 485 paras 328-53);
  "undisputably are not subject to arbitration" (L41).
- Rules: Rule 37(b)(2)(A)(i)-(vii) list (L52; same seven items as D13 L62-65); Rule 45(a)(1)(A)(iii),
  45(d)(3)(A) four quash grounds (L58-59); 28 U.S.C. 1407(b) (L94-106); Griggs (L75-77).
- Rulings: "The Coinbase stay cannot extend to the entire Snowflake MDL and specifically does not
  extend to the LendingTree Plaintiffs' claims against Snowflake." (L83); Rule 45 subpoena proper
  (L87-93); "No indications exist that Snowflake's subpoena seeks compliance outside the 100-mile
  zone" (L104); section 1407(b) authorizes jurisdiction (L106); "Snowflake requests no sanctions ...
  The Court will not order sanctions at this time." (L106).
- ORDER (L107-108): "Snowflake's Motion to Compel Discovery from LendingTree (Doc. 773) is GRANTED."
- Hedged claims: conditional "if the Ninth Circuit agrees with LendingTree on appeal, LendingTree
  will depart the litigation and move to arbitration" (L88); subpoena "appears unusual" (L88);
  "judicial efficiency might be lost without a stay" (Coinbase reasoning, inapplicable, L85); Packaged
  Seafood: power "may necessarily include" deposition subpoenas, "may not extend" to documents-only
  subpoenas (L103).
- Numbers: fifteen topics (L31); four named plaintiffs (L34); 100-mile zone (L104); seven Rule 37
  sanctions (L52); four Rule 45 quash grounds (L59).
- Tables: not applicable.
- Amendments or contradictions: none stated; D14's statement that the denial order (Doc. 595) is on
  interlocutory appeal is later than D09 (which itself found "A stay of proceedings proves
  unwarranted", D09 L91).
- Rounded prose beside exact figures: "hundreds of millions of customers" (L25); otherwise not
  applicable.
- Coverage: FULL. Read L1-118 (all 13 pages). Unread: none.

## Shared ground (navigation only)

Facts and locations only; no reconciliation beyond what the documents state.

### Entities that appear in more than one document, and where

- Snowflake, Inc.: D01 defendant, opposed centralization (L32), "principal executive office in this
  district" (L76); D02 L22 (Keller appeared vs "Snowflake Inc."); movant in D05 (Doc. 417, DENIED
  L411), D06 (Doc. 469, Count IV granted L304), D07 (Doc. 420, GRANTED L107-108), D08 (Doc. 500,
  DENIED L211), D11 (Doc. 721, DENIED L94-96), D13 (Doc. 749, GRANTED, $5000 to Snowflake L84), D14
  (Doc. 773, GRANTED L108); D06 L162-163 "headquartered in Montana and has set up its servers in
  Montana"; boilerplate "hub" in D05-D06, D08, D10-D14. Not a party to D03/D04 settlements.
- Ticketmaster / Live Nation name forms: D01 fn 1 "Ticketmaster LLC and Live Nation Entertainment,
  Inc. (together, 'Ticketmaster/Live Nation')" (L21-22), schedule captions "TICKETMASTER, LLC" and
  "TICKETMASTER LLC" (L110-118); D05 L15, D06 L17, D08 L16, D10 L24, D11 L21, D12 L24, D13 L21, D14
  L23 "Ticketmaster, LLC and Live Nation Entertainment, Inc. (collectively 'Ticketmaster')"; D10 L14
  and D12 L14 "Live Nation Entertainment, Inc. and Ticketmaster L.L.C."; D09 L15 "Ticketmaster LLC's
  Motion"; D05 L413 "Ticketmaster and Live Nation's Motion"; D06 L309 "Defendant LiveNation's"; D05
  L150 dark-web "Livenation / Ticketmaster". Actor in D05, D06 (movant), D10 (movant), D12
  (respondent, sanctioned). Mention only: D09 L80 "Oberstein v. Live Nation Ent., Inc." (case).
- LendingTree / QuoteWizard name forms: D01 L18 "Lending Tree's QuoteWizard.com subsidiary", fn 1
  L22 "Lending Tree LLC and QuoleWizard.com [OCR] LLC (together, 'Lending Tree')"; D05/D06/D08/D10-
  D13 boilerplate "LendingTree, LLC, and Quotewizard.com, LLC (collectively, 'LendingTree')"; D07
  L34/L36 "QuoteWizard by LendingTree"; D09 L12 "QuoteWizard.com, LLC, a subsidiary of LendingTree,
  LLC"; D14 L15 "LendingTree, LLC and QuoteWizard.com, LLC". Actor: D01 (supports E.D.N.C., L29), D09
  (movant, DENIED), D14 (respondent, motion against it GRANTED).
- Advance Auto Parts, Inc. / Advance Stores Company, Inc(orporated): D01 fn 1 L21 ("Advance Auto
  Parts"), L32 (opposed centralization), Schedule B E.D.N.C. L141-150; D03 L10-13, L17 (settling
  defendant, $10,000,000); D05 L21, D06 L22, D08 L21 ("Advance Auto" in FAC spoke list). Similar
  names that are different entities (case citations): D11 L72 "Daniels v. Advanced Grp."; D14 L92
  "Jacobs v. Advanced Dermatology".
- Neiman Marcus: D01 L18 "The Neiman Marcus Group", fn 1 L22, L29, fn 2 L39, L76; D04 L15-16 "THE
  NEIMAN MARCUS GROUP, LLC" (settling defendant, $3,500,000). Mention only (cited case "Remijas v.
  Neiman Marcus Grp., LLC", 7th Cir. 2015): D05 L94, D06 L125-126, L132, D08 L87. Absent from the FAC
  spoke lists (D05 L21-22, D06 L22-23, D08 L21-22).
- AT&T (AT&T Inc. / "AT&T, Inc." and AT&T Mobility, LLC): D01 (fn 1 L21; MDL No. 3124; Schedule A);
  D02 throughout ("AT&T I" = MDL 3114, "AT&T II" = this MDL; global mediation March 17, 2025, L43);
  D05 L21-22, D06 L22, D08 L21-22 (FAC spoke list). No AT&T motion is decided in the bundle.
- Cricket Wireless, LLC: D01 only (L18, fn 1 L21, L29, L50, L76, Schedule B Morgan L122). Absent
  from FAC spoke lists.
- Innive: D05 L22, D06 L22-23, D08 L22 "Innive, Inc." (D08 L29, L34, L99, L150, L174, L197: LAUSD's
  storage vendor, "gave no notice"); D13 "Innive Inc." (non-responsive defendant, sanctioned $5000).
- Plaintiff groups (Consumer / LAUSD / Financial Institution): defined identically in D05 L15, D06
  L17, D08 L16, D10 L24, D11 L21, D12 L24, D13 L21-24, D14 L23. Main subject: Consumer (D05, D10,
  D11, D12), FI (D06; NOFFCU L43), LAUSD (D08; depositions mentioned D13 L68). D02 L147-152: earlier
  financial-institution "spoke" order Doc. 350 and Co-Lead filing Doc. 344 (not in bundle).
- Plaintiffs' leadership: Amy Keller (D02 throughout; D03 L43; D04 L35); John Heenan (D02 L26; D03
  L43; D04 L35); "J. Devlan Geddes" (D02 L27) / "Devlan Geddes" (D03 L43, D04 L35); "Raphael
  Graybill" (D02 L27) / "Raph Graybill" (D03 L43, D04 L35); "Jason S. Rathod" (D02 L27) / "Jason
  Rathod" (D03 L43, D04 L35). D02: "four other Co-Lead Counsel" (L26, L145, L162); D03/D04: five
  Class Counsel.
- Judges: "Chief Judge Brian Morris" / "the Honorable Brian Morris" only in D01 (L76, L78); case
  suffix "BMM" in all captions; "U.S. Magistrate Judge John T. Johnston" as Special Master (Doc. 383)
  in D10 L28, D11 L24, D12 L27, D13 L27, D14 L27; suffix "JTJ" in every ECF footer. No signing name
  is printed in D02-D14.
- Same surnames in different roles (the documents do not state identity links): Chaidez (D01 L19
  movant "Cbaidez", L125 Chaidez v. Snowflake (D. Mont.), L143 Chaidez v. Advance Auto Parts
  (E.D.N.C.); D03 L17/L41 "Emmanuel Chaidez" Class Representative); Smith (D01 L144 Smith v. Advance
  Auto Parts; D03 L17/L41 "Don Smith"; cases D09 L91, D12 L163); Anderson (D01 L116 Anderson v.
  Ticketmaster; D05 L73-75, L400 plaintiff; case D05 L244, L260); Xian (D01 L116 Xian v. Ticketmaster
  2:24-04726; D05 L73, L309, L334, L350; D07 L99); Miller (D01 L117 Miller v. Ticketmaster, L138
  Miller v. Snowflake 2:24-00067 and fn 6 L70 "24-0067"; D02 L35 Miller v. Snowflake "2:24- cv-96";
  D12 L102-103 Arthur R. Miller, treatise); Young (D01 L19, L97, L121 movant/plaintiff; case "Young v.
  Flathead County" D05 L190, D06 L198); Weaver (D01 L153 Weaver v. Snowflake; D05 L210 case; D05 L283
  article author); Garcia (D05 L145 "Garcia-Nixon" did not receive notice; D07 L38 "Susie Garcia"
  recipient of a Ticketmaster Notice of Data Breach, Exhibit 9; D10 L59 "Plaintiff Garcia"); Lozoya
  (D05 L73; D07 L38 "Valerie Lozoya"); Murphy (D07 L38 "Jolinda Murphy"; D10 L59 "Plaintiff
  Murphy"); Fitzgerald (D05 L73, L145, L400 plaintiff; D11 L66 "Fitzgerald v. Cassil" case);
  LendingTree Plaintiffs Pierce, Macom, Thomas, Nader (D07 L36; D09 L17; D14 L34 count only).
- Organizations acting vs only mentioned: Epiq (D04 L51 appointed administrator; D05 L309 "Karter v.
  Epiq Systems" case); Kroll (D03 L62 only); CrowdStrike and Paul Hastings (D12 only); Mandiant (D07
  L28 only); Visa (D05 L154, L334; D06 L86, L132, L285 "VISA Global Compromised Account Recovery
  Program"); FTC (D05 L244-251; D06 L239-261; D07 L26 Exhibit 3; D11 L80 lawyer-letter item);
  Equifax (D02 L40 Keller credential; D05 L175; D06 L107-124, L176, L265; case citations); Marriott
  (D02 L40; D06 L97-106 case); Blackbaud (D05 L251 FTC action, L309 case; D06 L157 case); Iowa Office
  of the Attorney General (D05 L335, informed by Ticketmaster); Massachusetts Attorney General (D05
  L278); DOJ antitrust litigation (D12 L168-173); DiCello Levitt (D02); Kashfian and Kashfian LLP and
  Datsopoulos, MacDonald, & Lind, P.C. (D13 L34).

### Repeated boilerplate (same paragraphs in several documents)

- Motion-to-dismiss intro (hub-and-spoke "Doc. 1 para 2", plaintiff groups, FAC July 9, 2025 Doc.
  485, spoke list): D05 L13-22; D06 L15-24 (adds FI Amended Complaint April 8, 2025, L22); D08 L14-22.
- Breach background (April 2024 access, malware, May 30, 2024 announcement, May 24, 2024 ads,
  Ticketmaster stolen-data list, notice letter "may include", "560 million" ad): D05 L27-37; D06
  L29-41 (cites "Doc. 393 at para 56" for the announcement, L33).
- Rule 8/12(b)(6) standard (Navarro, Mendiondo, Balistreri, Iqbal, Lee): D05 L44-52; D06 L45-53; D08
  L43-51. Article III standard (Lyons, TransUnion, Laidlaw, Lujan, Zappos): D05 L60-66; D06 L61-69;
  D08 L54-61. Negligence elements (Md. Cas. Co.): D05 L164-166; D06 L139-140; D08 L144-148. Duty
  (Fisher, Poole, Hinkle, Equifax): D05 L168-175; D06 L173-176. Causation (Busta, Young v. Flathead,
  Perez, Creel, Teeter): D05 L188-198; D06 L198-199. Economic loss (Sheen, Urban Outfitters,
  Smallman): D05 L219-221; D06 L218-232. Redressability (Greenstein): D05 L160-161; D06 L135-137; D08
  L140-142. Zappos facts ("over 24 million"): D05 L84-86; D08 L79.
- Discovery-order background ("Ticketmaster suffered a security breach in April and May of 2024 ...
  hundreds of millions of customers"; MDL "commenced on October 8, 2024 (Doc. 1)"; substantial
  completion July 31, 2026, Doc. 606 Ex. 1; Special Master Doc. 383; competing motions): D10 L19-30;
  D11 L16-27; D12 L19-30; D13 L19-28; D14 L19-30. Discovery legal standard (Hunt, Nei, Rule 26(b)(1),
  Oppenheimer, Schulz, Rule 37(a)(1)): D10 L38-45; D11 L36-41; D12 L42-49; D13 L54-61; D14 L43-51.
  Rule 37(b)(2)(A)(i)-(vii) list: D13 L62-65; D14 L52. Rule 37(b) quote + Dreith + "$5000 ...
  ten-fold" warning: D12 L176-184; D13 L74-78.
- Settlement-order text: D03 and D04 share near-identical paragraphs (jurisdiction D03 L37/D04 L27;
  Rule 23 findings D03 L39/D04 L29-31; notice findings D03 L66-69/D04 L57-58; opt-out D03 L72-80/D04
  L61-68; claims D03 L113-117/D04 L104-105; termination D03 L119-123/D04 L109-111; stay D03 L126/D04
  L116; injunction D03 L128/D04 L118; adjournment D03 L131/D04 L120; deadline tables).
- Conclusion passages restating the ORDER: D05 L407 vs L411-415; D06 L299 vs L304-309; D08 L208 vs
  L211; D09 L90-91 vs L101; D11 L91 vs L94-96; D02 L175-176 vs L180 (safeguards appear only in
  Discussion/Conclusion, L162, L176, not in the numbered ORDER item).

### Dated events reported in more than one document (agreement)

- MDL centralization/commencement: D01 ECF stamp "Filed 10/08/24" (L24; Panel's own date not
  legible); D02 L20 "October 8, 2024"; D10 L26, D11 L22, D12 L25, D13 L25, D14 L25 "commenced on
  October 8, 2024 ... (Doc. 1.)". Agree.
- MDL No. 3114 ("AT&T I") centralized June 5, 2024: D01 fn 3 L41-42; D02 L10, L35. Agree (N.D. Tex.).
- Breach window (differently scoped wording): D01 L18 "approximately April to June 2024", L38
  "approximately April through June 2024" (cluster of breaches); D05 L29, D06 L29 access "in April of
  2024"; D05 L89, D08 L86 data obtained "from Snowflake's servers in April 2024/April of 2024"; D10
  L26, D11 L22, D12 L25, D13 L25, D14 L25 "Ticketmaster suffered a security breach in April and May
  of 2024".
- Announcements: Snowflake announced the Data Breach May 30, 2024 (D05 L35; D06 L33); AT&T announced
  the Snowflake-hosted AT&T breach "in July 2024" (D01 fn 6 L70); MDL 3114 breach announced by AT&T
  "in March 2024" (D01 fn 3 L42, fn 6 L69). Advertisements began May 24, 2024 (D05 L35; D06 L34);
  LAUSD data sold on dark web June 1, 2024 (D08 L86 only); Ticketmaster retained CrowdStrike May 17,
  2024 (D12 L33 only). Same calendar date, different events: May 17, 2024 = FTC Blackbaud action
  (D05 L251) and CrowdStrike retention (D12 L33).
- CCPA pre-suit notice / demand letter December 27, 2024: D05 L347 ("sent a notice letter on behalf
  of the class"); D07 L40 (Exhibit 10 "Demand letter to Snowflake from Plaintiffs"); D08 L205 ("sent
  the required pre-suit notice"). Agree.
- FAC filed July 9, 2025 (Doc. 485): D05 L20; D06 L21; D08 L20. D07 L14 instead describes
  Snowflake's motion as directed to the "Second Amended Representative Class Action Complaint" while
  incorporating exhibits "to the Fourth Amended Complaint" (D07 L56).
- Motion hearing October 6, 2025 (Doc. 569): D05 L24; D06 L26; D08 L24; D09 L30. Agree.
- Discovery hearing June 11, 2026 (Doc. 712): D10 L16; D12 L15-16. Agree.
- Substantial completion July 31, 2026 (Doc. 606 Ex. 1): "is due" D10 L26, D11 L22, D12 L25, D13
  L25; "was due" D14 L25.
- LendingTree arbitration: motion filed May 16, 2025 (Doc. 424) and denied (Doc. 595, D09 dated
  October 30, 2025); D14 L38-40 repeats the motion and denial and adds appeal "(See Doc. 596.)".

### Documents that cite, apply or respond to another bundle document

- D02 L20 -> D01 ("(Doc. 1; 2:24-MD-03126-BMM)").
- D10-D14 "(Doc. 1.)" for MDL commencement -> D01. Note: "Doc. 1" is also cited with paragraph
  numbers for complaint allegations ("Doc. 1 para 2" hub-and-spoke: D05 L13, D06 L15, D08 L14, D10
  L19, D11 L16, D12 L19, D13 L19, D14 L19; "Doc. 1 para 158/162-166/174/256/555-56" in D05 L27-42,
  L392; D06 L29-34). D01 (ECF Document 1) contains no "hub" wording and no numbered paragraphs.
- D07 L18 -> D05 ("its previous order on Snowflake's motion to dismiss. (Doc. 591.)").
- D08 L27-28, L66 -> D05 (Doc. 591); D08 L150, L157 apply D05's reasoning by description; D08 L159
  cites Doc. 418 (Snowflake's consumer brief).
- D09 L15 -> D05 (Doc. 591).
- D06 L76 cites Doc. 417 (Snowflake's consumer motion decided in D05).
- D11 L51 (Snowflake's position) refers to emotional-distress allegations that "helped them defeat
  Defendants' Rule 12 motions" (cf. D05 L128-131).
- D12 L33-39 cites Doc. 702 (Ticketmaster's brief on the motion decided in D10; D10 L32) for the
  CrowdStrike date and ESI-protocol/allocation positions; D12 L138, L146 cite Doc. 698 for the same
  positions.
- D13 L28 -> D10, D11, D12 ("(Doc. 739, Doc. 740, Doc. 744.)").
- D14 L30 -> D10, D11, D12, D13 ("(Doc. 739, Doc. 740, Doc. 744, Doc. 760, Doc. 761, Doc. 766.)";
  761 and 766 not in bundle). D14 L32-40 -> D09 (Doc. 595) and its appeal (Doc. 596).
- D03 and D04 are titled "AMENDED ORDER" but neither names the order it amends; no bundle document
  states that it supersedes, vacates or amends another bundle document (D02 L40 "vacated" refers to
  a Marriott case history).

### Deadlines set in one order and acted on or referenced in another

- D02 (March 12, 2025): global mediation with AT&T "scheduled ... for March 17, 2025" (L43); Keller
  barred from attending (L162, L176). No later bundle document mentions a mediation, settlement or
  outcome with AT&T (grep "mediation"/"settlement" finds only D02-D04; D12 L123 "remediation").
- D02 keeps Keller as Co-Lead (L180) -> D03 L43 and D04 L35 (May 22, 2025) designate Keller among
  Class Counsel.
- D03/D04 Final Approval Hearing ("Thursday October 23, 2025" in para 8/7 vs "July 10, 2025" in each
  table) and relative deadlines (20/15/30/45/30/30/15 days): no later bundle document reports the
  hearing, final approval or claims results; D05/D06/D08 (October 2025) still list "Advance Auto" in
  the FAC spoke list (D05 L21) without mentioning the settlement.
- Doc. 671 (May 1, 2026, not in bundle): Innive new counsel "within twenty (20) days" -> lapsed May
  21, 2026; Innive discovery responses due May 10, 2026 (D13 L34-51).
- D12 (July 1, 2026): Ticketmaster to pay $5000 "within 15 days of this order" (L187); Special
  Master's custodian search Jan 1, 2022 - Dec 31, 2024 ordered "now" (L173); privilege-log
  "rolling ... last one due before discovery closes" (L138). D13 is dated July 16, 2026 (15 days
  later) and does not mention Ticketmaster's payment.
- D13 (July 16, 2026): Innive to respond "within 7 days" and pay $5000 "within 15 days" (L84). D14
  (August 19, 2026) lists Doc. 760 (L30) but reports nothing on Innive's compliance.
- D10 (June 29, 2026): Consumer Plaintiffs' "full supplementation by the close of discovery" (L70;
  no date). Substantial completion July 31, 2026 (D10-D14 background).
- D09 (October 30, 2025) denial -> LendingTree's interlocutory appeal (D14 L16, L32, L40) and
  Coinbase stay argument rejected for the LendingTree Plaintiffs' claims against Snowflake (D14 L83).
- D14: Rule 45 subpoena served July 7, 2026; LendingTree objection July 27, 2026 (L31-32).

### Same-label figures or terms that differ across (or within) documents

- Final Approval Hearing date: D03 L50 "Thursday October 23, 2025" vs D03 L152 "July 10, 2025";
  D04 L40 "Thursday, October 23, 2025" vs D04 L142 "July 10, 2025". No precedence stated.
- Settlement terms D03 vs D04: fund $10,000,000 vs $3,500,000; fee cap "up to 33.33%" vs "up to
  one-third"; service award "up to $2,500.00" vs "up to $3,000.00"; administrator Kroll vs Epiq;
  class "Private Information ... and who were sent notice" (est. "approximately 2.3 million") vs
  "Personal Information" of persons "who live in the United States" (no estimate); California
  Settlement Subclass only in D03; objection items a-j (10) vs a-k (11); objection submitted to the
  Settlement Administrator vs to the Court (mailed to Clerk, Class Counsel, Defendant's Counsel,
  Administrator); notice start "Within 20 days of the Preliminary Approval Order" vs Class List "No
  later than 15 days after entry" then notice "Within 30 days following receipt of the Class List";
  reference date "original" vs "initial scheduled" Final Approval Hearing date; complaint "Amended
  Representative Class Action Complaint" vs "Consolidated Complaint"; motions Doc. 415 vs Doc. 413.
- Counts labelled "Count I-VI": D05 L413-415 (I Breach of Contract, II Montana CPA, III NY GBL 349,
  IV California UCL, V CCPA, VI Negligence) vs D06 L304-309 (I Negligence, II Negligence per se, III
  Unjust Enrichment, IV Declaratory and Injunctive Relief).
- People affected: D01 L18/L38 "over 500 million" (whole cluster); D05 L37 / D06 L40 dark-web ad
  "560 million customers" (Ticketmaster); D10-D14 "hundreds of millions of customers" (Ticketmaster);
  D03 L26 "approximately 2.3 million" (Advance settlement class); D08 L33 "4M+ Student" (LAUSD ad);
  D01 fn 3 L42 "over 70 million" (MDL 3114 AT&T); D06 L71 "millions of credit and debit cards"; D02
  L24/L48 "approximately 20,000" / "all 20,000" DiCello Levitt clients (AT&T I).
- Visa CAMS alerts "over a hundred": D05 L154, L334 (FAC para 475) and D06 L132 (Doc. 393 para 143).
- Action counts (D01 only): 4 (Young motion), 43 (Chaidez motion), 45 in eight districts, 34
  tag-alongs, 42 in twelve districts (fn 5), at least 20 co-defendant actions, at least eleven
  Snowflake actions in six districts outside Montana, AT&T actions "among eight districts", 14 + 12 in
  D. Mont.; MDL 3114 "twelve actions" (fn 3). Mapper schedule check: Schedule B = 43 entries; A + B =
  45 unique (Young, Olivieri on both); 8 districts; AT&T-captioned schedule entries = 5 in 5 districts
  (Young, Olivieri, Schulte, Winger, Leduc Montgomery) while L61 says eight districts (tag-alongs not
  listed); Snowflake-first-captioned schedule entries outside Montana = 2 (Conte, Weaver) while L61
  says at least eleven (captions show only first-named defendants).
- Miller v. Snowflake number: D01 L138 "2:24-00067", fn 6 L70 "24-0067" vs D02 L35 "2:24- cv-96".
- Ticketmaster service-fee quote: D05 L116 "covers the costs of the technology, people, and
  resources needed to provide a safe and secure ticket-buying experience"; D05 L252 "cover the cost
  of technology, people, and resources ..."; D12 L36-38 "the costs of the technology, people and
  resources needed to provide a safe and secure ticket-buying experience".
- CCPA name: "California Consumer Privacy Act" (D05 L309; D07 L41, L90; D08 L170) vs "California
  Consumer Protection Act" (D08 L53). Montana statute: "Montana Unfair Trade Practices & Consumer
  Protection Act" (D05 L224), "Montana Consumer Protection Act ('MCPA')" (D08 L53), "Montana Unfair
  Trade Practices and Consumer Protection Act" (D14 L41). Incident label: "Data Breach" (D05-D14
  boilerplate), "Data Incident" (D03 L26, D04 L25, D07 L34/L36 notice titles), "the Incident" (D14
  L31); the phrase "Data Security Incident" does not occur in any document.
- CCPA notice wording: "30- day pre-suit notice" (D05 L344); "30 days' written notice" (D07 L101);
  "written notice within 30 days before seeking statutory damages" (D08 L203).
- Citation variants: "999 F.3d 1247 (11th Cir. 2021)" = In re Equifax (D02 L40) vs In re Yahoo! (D05
  L108); Caesars "LEXIS 15947" (D05 L107, L137; D06 L112; D08 L71) vs "159427" (D05 L186, L221; D06
  L191, L232); Md. Cas. Co. "460 P.3d" (D05 L166; D06 L140; D08 L147) vs "406 P. 3d" (D05 L168; D06
  L173); Landon "2024 WL 5317240" (D05 L145; D08 L128) vs "531240" (D08 L133).
- Claims vs LendingTree: D09 L20 "Doc. 485 paras 683-720" vs D14 L38 "paras 683-720, 749".
- Discovery-order docket range: "Doc. 680 to Doc. 738" (D10 L30, D11 L27, D12 L30, D13 L28) vs "Doc.
  680 to Doc. 779" (D14 L30).

### Hedge-scope index (hedge word -> what it attaches to)

- "allegedly" -> breach facts (D01 L18, L38, fn 6); "apparently ... approximately 20,000" -> DiCello
  Levitt client count (D02 L24); "potentially compromised" -> inside both settlement class
  definitions (D03 L26; D04 L25); "appear reasonable, but the Court will defer ruling" -> fee and
  service-award amounts (D03 L53; D04 L43); "may include" -> Ticketmaster notice-letter data (D05 L37;
  D06 L38); "passport numbers may have been impacted for some individuals" -> passport exposure only
  (D05 L335), Court's CCPA holding firm (L338-341); "as far as the Court can tell" -> place of conduct
  (D06 L162); "It can be inferred" -> MFA enforcement failure (D06 L188); "appear to be a tit-for-tat
  game" -> discovery motions (D10 L50); "may open the door" -> conditional future discovery (D11 L74);
  "it appears ... abandoned" -> Ticketmaster's attorney-client privilege (D12 L77); "It appears ...
  complied" -> Innive's former counsel (D13 L48); "if the Ninth Circuit agrees" -> LendingTree leaving
  the litigation (D14 L88); "LendingTree alleges ... unchanged since January 2017" -> userflow
  (attributed, D09 L94-96).

### Governing-law and claim index (as stated in the orders)

- D05 (Consumer Plaintiffs): negligence analysed under Montana law (Md. Cas. Co., Fisher, Poole;
  L163-210); economic loss doctrine discussed via California/Nevada authority (L219-221); Montana
  CPA, Mont. Code Ann. 30-14-101 (L223-266); Massachusetts Ch. 93A vs Snowflake (L268-303); CCPA,
  California, plaintiff Xian (L308-350); breach of contract "under Montana law" although home states
  are California, Massachusetts, Montana, New York and Washington D.C. (L354-358); California UCL
  (L380-394); New York GBL 349, plaintiffs Anderson and Fitzgerald (L396-404).
- D06 (Financial Institution Plaintiffs): Montana law "at the pleadings stage", Louisiana law urged by
  Ticketmaster, conclusive choice later (L142-165); negligence, negligence per se via FTC Act s. 5,
  unjust enrichment (Montana elements, L271-274), declaratory/injunctive relief (Declaratory Judgment
  Act, City of Reno).
- D08 (LAUSD Plaintiffs): negligence (Md. Cas. Co., L147), Montana CPA (Kostelecky, L157), CCPA
  (L169-205).
- D09/D14 (LendingTree Plaintiffs): claims vs LendingTree = negligence, Washington Consumer Protection
  Act (Wash. Rev. Code 19.86.020), unjust enrichment (D09 L20; D14 L35-38); Ninth Circuit law applied
  by consent (D09 L30); claims vs Snowflake = negligence and Montana Unfair Trade Practices and
  Consumer Protection Act (D14 L41).
- D02: Montana Rules of Professional Conduct govern attorney conduct in D. Mont. (D. Mont. LR
  83.2(a), L62).

### Negative and exclusion facts

- Cricket Wireless and Neiman Marcus are absent from the FAC spoke lists (D05 L21-22; D06 L22-23; D08
  L21-22). AT&T and Advance Auto are listed there but no motion by them is decided in the bundle.
- No D05 ruling on any LendingTree consumer claim (only Snowflake and Ticketmaster motions, L23-24).
- Plaintiffs without notice letters: Fitzgerald, Garcia-Nixon, Neve (D05 L145); no LAUSD Plaintiff
  received notice and Innive gave none (D08 L34, L101, L197).
- LendingTree Plaintiffs "never entered credit card information or downloaded an app" (D09 L59).
- Ticketmaster "does not allocate ... on a transaction-by-transaction basis" (D12 L39, L146).
- No sanctions: D10 L71 ("Ticketmaster requests no sanctions"); D14 L106 ("Snowflake requests no
  sanctions"). Sanctions imposed only in D12 (Ticketmaster) and D13 (Innive), $5000 each.
- D05 Counts I and IV and D06 Count IV are granted without any "with/without prejudice" or
  leave-to-amend wording; D07 grants the motion in full while declining Exhibit 11's facts.
