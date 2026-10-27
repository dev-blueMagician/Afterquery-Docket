# aq-02673 - document map

Maintained by the caller or optional `bundle-mapper` from `text/` (and `docs/` for layout issues).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

Conventions used below: `Lnn` = line number in `text/Dnn.txt` (the original `docs/` file is the same
text two lines earlier, because `text/` adds a two-line header). Quotes are verbatim. Anything marked
`[mapper arithmetic]` or `[inferred]` is NOT printed in the document.

## Bundle

- What it is: "Commercial Fishing Quota Regulations" - seven NOAA/NMFS Federal Register texts
  (Oct 3, 2025 - Sep 3, 2026): one temporary/emergency rule, two final rules, four proposed rules.
- Documents: 7; ids from `text/manifest.json`. Local Dnn = task-page Doc N (intake.json `number` 1-7 in
  the same order as the alphabetical file names).
  - D01 fr_2025_19459 - Northeast multispecies emergency-rule extension (temporary rule), 90 FR 47989, Oct 3, 2025
  - D02 fr_2025_24264 - Atlantic shark proposed rule, 91 FR 215, Jan 5, 2026 (mapped by the caller)
  - D03 fr_2026_09059 - Atlantic HMS quotas proposed rule, 91 FR 24789, May 7, 2026 (mapped by the caller)
  - D04 fr_2026_09973 - 2026 West Coast salmon final rule, 91 FR 29092, May 19, 2026
  - D05 fr_2026_10389 - electronic logbook proposed rule (Gulf/South Atlantic/Atlantic), 91 FR 30604, May 26, 2026
  - D06 fr_2026_16870 - Atlantic HMS quotas final rule, 91 FR 53526, Aug 19, 2026 (mapped by the caller)
  - D07 fr_2026_18031 - Pacific halibut IFQ vessel use caps proposed rule, 91 FR 56606, Sep 3, 2026
- Gaps:
  - D01 Tables 6-8: missing source text, not unread coverage. L54 says updates "are provided in Tables 1-8";
    the text holds Tables 1-5 (L56-90) and then three `[GRAPHIC] [TIFF OMITTED] TR03OC25.000/.001/.002`
    placeholders on pages 47992-47994 (L96, L100, L104). That the three graphics are Tables 6-8 is [inferred].
    The same placeholders are in `docs/fr_2025_19459.txt`, so the original cannot resolve it.
  - D01 Table 1 column assignment: the header is flattened onto run-together lines (L57-58) in both text and
    original; cell-to-column mapping below follows dot-leader order and is [inferred] where leaders are used.
  - D02, D03, D06: read in full and mapped by the caller (2026-10-10); the mapper inspected only grep hits there.
  - No clipped ranges in D01, D04, D05, D07; every line of each was read (ledgers under each document).
- Extraction spot-checks (text vs original `docs/`):
  - Page markers `[[Page N]]`: docs and text counts match for all seven (D01 9, D02 12, D03 12, D04 15,
    D05 6, D06 13, D07 5). D01 pages 47989-47998 (10 pages, 9 markers); D04 29092-29107 (16 pages, 15 markers);
    D05 30604-30609 (6 pages, 6 markers incl. first page); D07 56606-56611 (6 pages, 5 markers).
  - Table row: D01 Table 3 `GB Cod............................ 1.68 0.08` text L74 = docs L72; D04 Table 3
    `North of Cape Falcon......... 24.0 18.0 16.0 12.0 None` text L539 = docs L537.
  - Footnote: D01 `n/a: not allocated to sectors` text L61 = docs L59; D04 `\1\ A subarea guideline is not a
    hard cap` text L397 = docs L395; D04 `Metric equivalents: 24.0 in = 61.0 cm` text L475 = docs L473.
  - D05 and D07: tables and footnotes not applicable (none present); sentence checks D05 text L116 = docs L114
    ("average 10 minutes per electronic fishing report"), D07 text L101 = docs L99 ("132,900 lb (60.3 mt), which
    is 63,360 lb (28.7 mt)").
  - No Markdown pipe tables in any of the seven texts (grep `| ---` = 0); tables are dot-leader/space text.
- Provenance: `notes/intake.json` schema 1, capture_sha256
  `7e9cc7fab48af5130291239a5317f0039a477dea1e52be90b0aca02fd6767666`; all seven `incomplete: false`,
  `gap_characters: 0`, `matches_capture: true`. Plain-text capture; extraction method `text`, `pages: null`.
- Reuse binding (source sha256; `text/manifest.json` records the same value as intake `source_sha256` and no
  separate extracted-text hash; chars from manifest). Map date 2026-10-10. No earlier map existed.
  - D01 docs/fr_2025_19459.txt 923149f83538498c07a5e19cf02306ce072c099428340d53844d2b29def94470 - 40,698 chars - MAPPED FULL
  - D02 docs/fr_2025_24264.txt 15628ec4cd70afddfa8b436d9f0ed45fbf39688c70668ca391a85cb75d433284 - 84,403 chars - caller-mapped
  - D03 docs/fr_2026_09059.txt 5e3ce7bed4bedebad0520c0c22c4a268bc78fb064f1e219740f4910da5464917 - 82,357 chars - caller-mapped
  - D04 docs/fr_2026_09973.txt 18db8e9fa2e51bd00c4f8713190b567ffb88293fd5eb2920850bf26a5ec80503 - 110,628 chars - MAPPED FULL
  - D05 docs/fr_2026_10389.txt b1bbdd7406bd75d318de6c5e6b4e5a213116636312ad15c9a1bd54a91ab1c9d8 - 39,830 chars - MAPPED FULL
  - D06 docs/fr_2026_16870.txt 8848d42ea14abe0a6a08aee9a730992e54ea45befc69dcae8dd9bf58a4215457 - 90,937 chars - caller-mapped
  - D07 docs/fr_2026_18031.txt 9db337411d2c9ee4675723c3c326e1e8e3bb78271adaf0b8ccc095ee075f3433 - 38,418 chars - MAPPED FULL

## D01 - Northeast Multispecies Fishery; Temporary Rule To Extend Fishing Year 2025 Measures

- Source: docs/fr_2025_19459.txt | text/D01.txt 216 lines | FR pages 47989-47998 | Doc 1
- Written or submitted by: NMFS/NOAA, Commerce (L22); signed Samuel D. Rauch III (L212-213). Mentioned, not
  authors: New England Fishery Management Council ("Council", L46); commenters CLF, SBCBA, NSC, GFCPF, "one
  individual" (L112); SSC, NRCC, PDT (L178, never expanded), Northeast Fisheries Science Center, ASMFC (L142).
- Type, date, edition: "Temporary rule; emergency action" (L24). 90 FR No. 190, Friday Oct 3, 2025 (L5);
  FR Doc 2025-19459; 50 CFR Part 648; Docket No. 250424-0072; RIN 0648-BN64; dated Oct 1, 2025 (L211);
  filed 10-2-25 (L214). It extends the May 2, 2025 emergency rule 90 FR 18804 (L31, L38), which is NOT in the bundle.
- Period covered: Northeast multispecies fishing year 2025 = May 1, 2025 through April 30, 2026 (L46 "start of
  the fishing year on May 1, 2025"; L192 "end of the fishing year on April 30, 2026"). Not a calendar year.
- Entities and aliases: Northeast multispecies = "groundfish" (L42); GOM = Gulf of Maine, GB = Georges Bank
  (L39); four-stock cod structure EGOM, WGOM, GB, SNE cod (L144) vs the FMP's two stocks GOM cod and GB cod;
  ACL, TAC, ACE (L42), SAP (L44), DAS (L45), BSIA (L143), OFL/ABC (L144), MSY (L161), SIR (L33), "$33M" (L128).
  SNE/MA, CC/GOM appear only as table row labels, never expanded.
- Tables (all "[Mt, live weight]"; fishing year 2025 only; no prior-year column):
  - Table 1 "Catch Limits for the 2025 Fishing Year" L56-61. 20 stock rows. Columns (header flattened, L57-58):
    Total ACL ("A to H"); Groundfish sub-ACL ("A+B+C"); A Sector sub-ACL; B Common pool sub-ACL; C Recreational
    sub-ACL; D Midwater trawl fishery; E Scallop fishery; F Small-mesh fisheries; G State waters sub-component;
    H Other sub-component. Footnote L61: "n/a: not allocated to sectors." (cells print "na" for the last five
    rows: N. Windowpane, S. Windowpane, Ocean Pout, Atlantic Halibut, Atlantic Wolffish). Rows as printed
    (Total / Groundfish / Sector / Common pool / then non-blank cells):
    GB Cod 186/140/135/5, G 16, H 31; GOM Cod 327/297/169/7, C 120, G 30, H 0.0; GB Haddock 1,478/1,449/1,415/33,
    D 29, G 0, H 0; GOM Haddock 2,183/2,108/1,343/36, C 729, D 22, G 46, H 7.6; GB Yellowtail 68/56/52/3.7,
    E 11.0, F 1.3, G 0.0, H 0.0; SNE/MA Yellowtail 38/33/24/9.0, E 2.7, G 0.2, H 2.0; CC/GOM Yellowtail
    873/808/761/48, G 28, H 37; American Plaice 5,009/4,957/4,803/154, G 26, H 26; Witch Flounder
    1,196/1,146/1,102/44, G 19, H 31; GB Winter Flounder 1,446/1,431/1,360/71, G 0, H 15; GOM Winter Flounder
    772/607/514/93, G 153, H 12.1; SNE/MA Winter Flounder 604/441/375/66, G 19, H 144; Redfish 7,859/7,859/7,762/98,
    G 0, H 0; White Hake 1,825/1,816/1,795/21, G 0, H 10; Pollock 12,683/11,619/11,492/127, G 598, H 465;
    N. Windowpane 127/94/na/94, E 27, G 0.0, H 6.8; S. Windowpane 205/30/na/30, E 71, G 6.4, H 98; Ocean Pout
    83/49/na/49, G 0, H 34; Atlantic Halibut 75/58/na/58, G 16, H 1.2; Atlantic Wolffish 87/87/na/87, G 0, H 0.
    Column letters for C-F cells are [inferred] from dot-leader order. Mixed precision (integers and one decimal).
    Printed components do not always sum to printed totals, e.g. GB Cod 140+16+31 = 187 vs "186"; GOM Cod
    169+7+120 = 296 vs "297"; GB Haddock 1,415+33 = 1,448 vs "1,449" [mapper arithmetic].
  - Table 2 "Fishing Year 2025 Common Pool Trimester TACs" L63-66. 14 stocks x Trimester 1/2/3. Omits SNE/MA
    Winter Flounder and the five "na" stocks. e.g. GB Cod 1.3/1.6/1.8; GOM Cod 3.4/2.3/1.2; GB Haddock
    9.0/11.0/13.3; Pollock 35.6/44.6/47.1. No stated rule ties Table 2 to Table 1 column B; row sums are close to
    column B (GB Cod 4.7 vs 5; GB Yellowtail 3.7 vs 3.7; SNE/MA Yellowtail 9.0 vs 9.0) [mapper arithmetic].
  - Table 3 "Common Pool Incidental Catch TACs" L70-80. 7 stocks; columns "Percentage of common pool sub-ACL"
    and "2025" (mt): GB Cod 1.68 / 0.08; GOM Cod 1 / 0.07; GB Yellowtail 2 / 0.07; CC/GOM Yellowtail 1 / 0.48;
    American Plaice 5 / 7.68; Witch Flounder 5 / 2.19; SNE/MA Winter Flounder 1 / 0.66. The percentage applies to
    Table 1 column B (rule in the column header only; base values 55 lines earlier at L59).
  - Table 4 "Incidental Catch TACs for Each Special Management Program" L82-86. Same 7 stocks; columns "Regular
    B DAS program" and "Eastern U.S./Canada haddock SAP": GB Cod 0.05 / 0.03; GOM Cod 0.07 / n/a; GB Yellowtail
    0.04 / 0.04; CC/GOM Yellowtail 0.48 / n/a; American Plaice 7.68 / n/a; Witch Flounder 2.19 / n/a; SNE/MA
    Winter Flounder 0.66 / n/a. ("n/a" here is not footnoted.)
  - Table 5 "Regular B DAS Program Quarterly Incidental Catch TACs" L88-90. Columns "1st quarter (13 percent)",
    "2nd quarter (29 percent)", "3rd quarter (29 percent)", "4th quarter (29 percent)". GB Cod 0.01 x4; GOM Cod
    0.01/0.02/0.02/0.02; GB Yellowtail 0.00/0.01/0.01/0.01; CC/GOM Yellowtail 0.06/0.14/0.14/0.14; American
    Plaice 1.00/2.23/2.23/2.23; Witch 0.28/0.64/0.64/0.64; SNE/MA Winter Flounder 0.09/0.19/0.19/0.19.
  - Tables 6-8: not in text (see Gaps). "Table 1" and "Figure 1" at L151 and L182 refer to the May 2, 2025
    emergency rule ("Table 1 (2025 Atlantic Cod Quotas Calculated Using Council's Recommendations in Framework
    69)"), not to D01's own Table 1.
- Lists: emergency rule's actions L39-45 (nine items by [mapper count]; several share a line; last = "Closed
  the Regular B Days-at-Sea (DAS) program", L45). Comment letters L112: four ("One individual; the Conservation
  Law Foundation (CLF); the Stellwagen Bank Charter Boat Association (SBCBA); and an attorney on behalf of the
  Northeast Seafood Coalition (NSC) and the Gloucester Fishing Community Preservation Fund (GFCPF)"). Numbered
  comments printed: 1-9 and 11 (L116-187); there is no "Comment 10". Emergency-rule criteria: 3 (L122).
  Comment attribution: C1 individual + NSC/GFCPF (L116); C2 CLF (L121); C3 CLF (L129); C4 NSC/GFCPF + SBCBA
  (L141-142); C5 individual (L150); C6 CLF (L155); C7 NSC/GFCPF (L166-167); C8 CLF (L176); C9 SBCBA + individual
  (L182); C11 individual (L187). Responses: "agrees" C1 (L117); "disagrees" C2 (L122), C4 (L143), C9 (L183),
  C11 (L188); mixed C6 "disagrees ... but agrees" (L156), C8 "agrees ... However, NMFS disagrees" (L177-178);
  C3, C5, C7 responses carry no agree/disagree word.
- Forecasts, guidance, deadlines, effective dates:
  - L31 "Effective as of October 3, 2025, Sec. Sec. 648.14 and 648.89 as amended at 90 FR 18804 is extended
    through April 30, 2026." L200: "implement this action on October 29, 2025 (the day the original emergency
    would have ended)". L198: measures "would end on October 28, 2025".
  - L52 "The emergency rule is in effect for 180 days, from May 1, 2025, through October 28, 2025 ... an
    emergency rule can be extended for an additional 186 days." The text does not count the extension's own
    length. [mapper arithmetic: May 1-Oct 28, 2025 is 181 days counting both ends; Oct 29, 2025-Apr 30, 2026 is
    184 days counting both ends.]
  - L38 emergency rule published May 2, 2025; L192 it "solicited public comment through June 2, 2025"; L198
    "provided 30 days for public comment".
  - L144 "On May 19, 2025, NMFS notified the Council that Amendment 25 was disapproved"; June 2024 management
    track assessments; SSC July 2024 meeting; L170 SSC October 2024 meeting; L149 "At its August 2025 meeting,
    the NRCC decided not to re-assess Atlantic cod stocks until at least 2027."
  - L47 Framework 69 "remains under consideration by NMFS" and "cannot be implemented when the current emergency
    rule expires on October 28, even if the framework is approved on or before that date" (L47-51).
  - L129-130 statutory "within 15 days" (16 U.S.C. 1854(b); section 304(b)).
- Hedged claims: L54 "would remain in place through April 30, 2026, unless replaced by other measures"; L128
  "estimated to result in an estimated commercial groundfish revenue of approximately $33M relative to no
  action"; L149 "the possibility of incorporating the RecBio information" (attaches to a 2027-or-later review).
- Rounded prose beside exact figures: L127 "vast majority of the commercial groundfish fleet" vs L198
  "Groundfish sectors constitute 96 percent of all commercial groundfish catch" (fleet vs catch); L161 "a
  50-percent reduction in cod quotas overall from the 2024 fishing year" (2024 values not printed in D01);
  L183 "47 mt (103,617 lb)" (the only lb figure in D01).
- Notes: figures on different bases - L168 "2025 U.S. ABC for GB haddock at 1,556 mt" vs Table 1 GB Haddock
  Total ACL 1,478 (ABC vs ACL). Sector "fifteen years"/"15 years" L202. PRA: no information collection (L204).
- Operative definitions, rules and scope exceptions:
  - Default specifications, L146: "provisions, at Sec. 648.90(a)(3), for setting default specifications for up
    to 6 months. Default catch limits are set at the lesser of 75 percent of the previous year's specifications
    or the Council's recommended specifications for the current year." Application L146-147: 75 percent "would
    exceed" the Council's recommended ABCs, so specs follow the four-stock ABCs. Commenters' proposal (not
    adopted), L141: "set at 75 percent of the 2024 ACLs for the remainder of the 180-day effective period".
  - Sub-component rule and instance, L183: "recreational catch of GB cod would contribute to catch in the State
    Waters sub-component and the Other sub-component. The interim GB cod sub-components ... are very low at a
    combined 47 mt (103,617 lb)"; instance values are Table 1 GB Cod G 16 and H 31 (L59), 124 lines earlier.
  - Emergency criteria L122 (62 FR 44421; August 21, 1997), three numbered criteria.
  - Overfishing definition L161 (Sec. 600.310(e)(2)(i)(B)).
  - Management uncertainty buffer L178: Sec. 648.90(a)(4)(i)(B); "whether the 100-percent monitoring coverage
    target supports a zero percent buffer".
  - Possession prohibitions L42-43 (recreational vessels and common pool commercial vessels may not possess GB
    cod); "Allocated zero common pool trips" into the Closed Area II SAP (L44); "Closed the Regular B
    Days-at-Sea (DAS) program and prohibit usage of Regular B DAS in fishing year 2025" (L45) - while Tables 4
    and 5 (L82-90) print Regular B DAS incidental catch TACs.
  - RFA exemption L203; good-cause waivers L197-200 (5 U.S.C. 553(b)(B), 553(d)(3)).
- Amendments or contradictions (both locations, no resolution):
  - L53 "remainder of the 2025 fishing year (through April 30, 2025)" vs L31, L54, L192 "April 30, 2026".
  - L31 "Effective as of October 3, 2025" vs L200 "implement this action on October 29, 2025".
  - L143 "National Standard 2 guidelines codified at 50 CFR 600.315" vs L161 "National Standard 1 guidelines
    codified at Sec. 600.315" (followed by a cite to Sec. 600.310).
  - L112 "four comment letters" vs comment numbering 1-9, 11 (no 10).
  - L54 "errors in table formatting in the original emergency rule are corrected" and allocations "updated in
    this extension to reflect the final rosters" (which cells changed is not stated). Amendment 25 "was
    disapproved" (L47, L144); Framework 69 pending (L47).
  - Table 1 cell "na" vs footnote key "n/a" (L60-61).
- Coverage: FULL. Read L1-216 in one pass. Remaining unread: none. Missing source: Tables 6-8 graphics.

## D02 - Atlantic HMS; Revisions to Commercial Atlantic Blacknose and Recreational Atlantic Shark Fisheries Management Measures

- Source: docs/fr_2025_24264.txt | 91 FR 215-227 | text/D02.txt L1-452 (caller read in full, 2026-10-10)
- Written or submitted by: NMFS (HMS Management Division); proposed rule, RIN 0648-BM88, 50 CFR part 635
- Type, date, edition: proposed rule, published January 5, 2026 (dated December 31, 2025); comments by
  March 6, 2026 (L30, L189); webinars January 22 and January 29, 2026 (Table 3, L193-194). No final rule in
  the bundle.
- Period covered: data windows 2017 through 2022 (observer and eDealer data); permits "As of October 2023"
  and "As of December 2023" (L213); 2022 shark ex-vessel revenue about $2.2 million (L212)
- Entities and aliases: Directed / Incidental shark limited access permit (LAP); SCS, LCS; blacknose vs
  non-blacknose SCS; "thresher" renamed "common thresher"; "pelagic sharks other than blue or porbeagle"
  renamed "common thresher and shortfin mako sharks" (L173-181)
- Tables: preamble Table 1 (L117-134) recreational minimum size ranges and defaults by shark group;
  preamble Table 2 (L147-161) recreational retention ranges ("1 to 3", "1 to 4", "1 to 5") and defaults;
  Table 3 (L193) webinars; regulatory Table 1 to paragraph (e) (L285-300) adds a shortfin mako row (males
  71 in, females 83 in, "No range") and prints ranges from "0 in"; regulatory Table 1 to paragraph (c)
  (L321-337) prints ranges from 0 ("0-3", "0-4", "0-5"), adds sandbar, silky, shortfin mako ("0-1") and
  prohibited rows, with footnotes 1 (group limit applies to the list as a whole) and 2 (no hammerheads in
  the Caribbean). The preamble and regulatory range floors differ (1 vs 0).
- Lists: alternatives A1-A2, B1-B3, C1-C5, D1-D3 (preferred A2, B2, C4, D2); management groups in the
  revised definition (L275)
- Forecasts, guidance, deadlines, effective dates: Draft Amendment 16 not expected "until early 2026" (L70)
- Hedged claims: economic impacts "neutral to minor beneficial" etc. per alternative (L220-249)
- Rounded prose beside exact figures: "approximately 36 percent" (L79) vs "36.3 percent" (L222, L232);
  "approximately 3,326 sharks" vs "3,326.4" (L92); "24.3 sharks/trip" vs default 25
- Notes: worked derivation of the default limit (L91-92): quota 37,921 lb dw (17.2 mt dw; the text prints
  "(17,2 mt lb)" once), average 11.4 lb dw per shark, 3,326 sharks, 5 vessels with 78 percent of landings
  averaging 137 trips a year, 24.3 per trip. Maximum 60 from an observed 54 interactions (L90). Revenue
  (L226, L231-232): about $402 per trip at 25 sharks, $0 to $964 over 0-60; $1.41 per lb dw; fleet average
  $19,394 a year; full quota $53,532; $3,149 per vessel across 17 active vessels or $10,706 for the top five.
  Maximum size rule: about 12 inches above the longest female size at maturity (L107-111; common thresher
  83 in gives 95 in; the text prints 210.8 cm and 210.3 cm for the same 83 inches).
- Operative definitions, rules and scope exceptions: Directed LAP default 25, range 0-60, Atlantic region
  (L355); Incidental LAP 16 SCS and pelagic sharks combined, at most 8 blacknose (L356); Gulf of America
  vessels may not retain blacknose (L355); HMS Commercial Caribbean Small Boat default 3 sharks, range zero
  to three (L357); closure at 80 percent of quota and projected 100 percent, effective no fewer than 4 days
  from filing (L396); base quotas 17.2 mt dw blacknose, 273.0 blue, 1.7 porbeagle, 488.0 common thresher and
  shortfin mako (L368-371); display/EFP 57.2 mt ww (41.2 mt dw) (L374)
- Amendments or contradictions: "This final rule is not an E.O. 14192 regulatory action" in a proposed rule
  (L204); Table 2 preamble floors vs regulatory floors as above
- Coverage: full (L1-452)

## D03 - Atlantic HMS; North Atlantic Swordfish, South Atlantic Swordfish, North Atlantic Albacore, and Atlantic Bluefin Tuna Quotas (proposed)

- Source: docs/fr_2026_09059.txt | 91 FR 24789-24800 | text/D03.txt L1-334 (caller read in full, 2026-10-10)
- Written or submitted by: NMFS; proposed rule, RIN 0648-BN60, Docket No. 260430-0121; docket folder
  NOAA-NMFS-2025-0053
- Type, date, edition: proposed rule, published May 7, 2026 (dated May 4, 2026). D06 is its final rule.
- Period covered: bluefin quota for 2026-2028; swordfish TAC 2025-2027, baseline "for 2026-2027";
  albacore baseline adopted for 2024 through 2026; 2024 prices; 2025 permit counts
- Entities and aliases: ICCAT Recommendations 25-10 (and 24-10) North Atlantic swordfish, 22-04 (21-03,
  17-03 not named here) South Atlantic swordfish, 23-05 (21-04) northern albacore, 25-05 (22-10, 10-03,
  06-06) bluefin; IBQ; NED; dw / ww
- Tables: Table 1 (L132-155) proposed bluefin baseline quotas and subquotas, total 1,509.98, set-aside
  62.5, annual total 1,572.48 (identical to D06 Table 4)
- Lists: alternatives A1/A2, B1/B2, C1/C2, D1/D2/D3 (preferred A2, B2, C2, D3; the text also calls D1 and
  D2 the "two additional alternatives" at L185)
- Forecasts, guidance, deadlines, effective dates: comments by June 8, 2026 (L32, L191); webinar May 28,
  2026, 2 p.m. to 4 p.m. EDT (L32, L193); a temporary final rule to adjust 2026 quotas "could be combined
  with the final rule" (L58)
- Hedged claims: U.S. "unlikely to achieve 100-percent quota utilization in the short term" (L224 etc.)
- Rounded prose beside exact figures: "approximately 26 percent of the TAC" (L67) vs 3,907 of 14,769
  [caller arithmetic: 26.45 percent]; the document's own working uses 0.26 (L67)
- Notes, D03-only inputs (Grep of all seven texts): swordfish TAC 2025-2027 "14,769 mt" (L66-67); 11
  possible TACs "from 4,764 mt ww to 17,628 mt ww" (L65); bluefin TAC 3,081.6 mt, U.S. 49 percent when the
  TAC exceeds 2,660 mt (L124); overall U.S. bluefin quota 1,572.48 mt, the 62.5 mt derived from the eastern
  TAC (L126-127); overharvest payback 100 percent, at least 125 percent after two consecutive years
  (L128); carryover "limited to 10 percent of the baseline quota" (L161) and ICCAT "10 percent of the ...
  initial quota allocation" (L127); South Atlantic transfers "first established in 2010 ... in place through
  2026" (L96); up to 150.4 mt dw (200 mt ww) landed between 5 N and 5 S countable to the North Atlantic
  quota (L97); total small entities 7,664 (L213).
- Operative definitions, rules and scope exceptions: dw x 1.33 = ww for swordfish (L44); North Atlantic
  swordfish adjusted quota = baseline + underharvest limited to 15 percent, Reserve 50 mt, Incidental 300
  mt, directed = adjusted - both, semi-annual = directed / 2 (L80-87); South Atlantic carryover up to 100
  percent of 75.2 mt dw (L96-99); albacore carryover 25 percent, maximum baseline 950 mt, maximum adjusted
  1,187.5 mt (L106-107); bluefin category percentages 54 / 22.6 / 15.9 / 4.5 / 0.1 / 2.9 (L310); school
  bluefin at most 10 percent of the baseline quota inclusive of the set-aside, trophy 3.1 percent of
  Angling, 52.8 percent south of 39 18 N (L318-320); set-aside allocated by IBQ share to ATL shareholders
  (L298)
- Amendments or contradictions: IRFA bluefin revenue is quota in mt ww times a price per lb with no dw
  factor (L238-256); the set-aside's "$1.2 million" (L249) and the "$15.4 million" total (L248) do not match
  the stated formula and parts [caller arithmetic: 1.03 and 16.5]; per-permit figures C1 $3,833 / $20,353 /
  $50,702, C2 $4,398 / $23,344 / $65,482, gains $565 / $2,991 / $14,780. Semi-annual seasons printed
  "January through June; June through December" (L87).
- Coverage: full (L1-334)

## D04 - West Coast Salmon Fisheries; 2026 Specifications and Management Measures

- Source: docs/fr_2026_09973.txt | text/D04.txt 646 lines | FR pages 29092-29107 | Doc 4
- Written or submitted by: NMFS/NOAA, Commerce (L22); signed Samuel D. Rauch III (L643). Mentioned, not
  authors: Pacific Fishery Management Council ("Council", L32) and its STT, SAS; WDFW, ODFW, CDFW; USCG; Pacific
  Salmon Commission; IPHC; commenters "Let Our Salmon Come Home campaign" (L133) and Golden Gate Fishermen's
  Association (GGFA, L136). The Pacific Coast Federation of Fishermen's Associations is named only as a group
  GGFA said it aligned with (L136), not as a commenter. Columbia River Treaty Tribes and Confederated Tribes of
  the Colville Reservation testified (L54).
- Type, date, edition: Final rule (L24). 91 FR No. 96, Tuesday May 19, 2026; FR Doc 2026-09973; 50 CFR Part
  660; Docket No. 260514-0235; RIN 0648-BO06; dated May 14, 2026 (L642); filed 5-15-26 4:15 pm (L645).
  Effective "0001 hours Pacific Daylight Time, May 16, 2026, until the effective date of the 2027 management
  measures ... which we expect to be 0001 hours Pacific Daylight Time, May 16, 2027" (L30). Predecessor 2025
  rule cited at L57, L154-155 (90 FR 20810, May 16, 2025; 90 FR 26943, June 25, 2025), not in the bundle.
- Period covered: "2026 ocean salmon fishing season" = May 16, 2026 until the 2027 measures (L28); L619 "The
  annual salmon management cycle begins May 16 and continues through May 15 of the following year." Also sets
  early-2027 openings; pre-May-16-2026 dates shown "for information purposes" (L154-155). ACL paragraphs say
  "in 2025" (L112, L114, L116) inside the 2026 rule.
- Entities and aliases: MSA; FMP = Pacific Coast Salmon FMP; KRFC, SRFC, CC Chinook, SONCC coho, LCR/LCN coho,
  LCR natural tule Chinook, OCN coho, OPI, SRKW, FNMC, ESU, MSST, SMSY, SI (Sacramento Index), ER vs HR, PST,
  KMZ (Oregon KMZ and California KMZ; C.10 definition L377), YRCA, GSI, PRE I/II/III. "ACL" expanded as "Annual
  Catch Limits" (L105) and once as "Allowable Catch Limit" (L85). "SFRC" at L107 beside "SRFC". Subarea names
  Neah Bay, La Push, Westport, Columbia River (L391-408); Fort Bragg, San Francisco, Monterey (L238-253).
- Tables:
  - Table 1 "Minimum Size Limits for Salmon in the 2026-2027 Commercial Salmon Fisheries" L272-305. Inches.
    Columns: Chinook Total length, Chinook Head-off, Coho Total length, Coho Head-off, Pink. Blocks "Area (when
    open in 2026)" and "Area (when open in 2027)". 2026: North of Cape Falcon 27 / 20.5 / 16 / 12 / None; Cape
    Falcon to Humbug Mountain 28 / 21.5 / 16 / 12 / None; Humbug Mountain to OR/CA border 28 / 21.5 / - / - /
    None; OR/CA border to Humboldt South Jetty 27; Latitude 40[deg]10' N to Point Arena 27; Point Arena to Pigeon
    Point through August 27; Latitude 38[deg]02' N to Pigeon Point, September 26; Pigeon Point to U.S./Mexico
    border 27. 2027: North of Cape Falcon blank; Cape Falcon to Humbug Mountain 28; Humbug Mountain to OR/CA
    border 28; OR/CA border to Humboldt South Jetty 27; Lat. 40[deg]10'0'' N to Point Arena 27; Point Arena to
    Pigeon Point 27; Latitude 38[deg]02' N to Pigeon Point, September 27; Pigeon Point to U.S./Mexico border 27.
    Footnote L305: "Metric equivalents: 28.0 in = 71.1 cm, 27.0 in = 68.5 cm, 21.5 in = 54.6 cm, 20.5 in = 52.1
    cm, 16.0 in = 40.6 cm, and 12.0 in = 30.5 cm." (no equivalent for 26). Rows exist for areas the season text
    lists as "Closed" in 2026 (L231-238).
  - Table 2 "Minimum Size Limits for Salmon in the 2026-2027 Recreational Salmon Fisheries" L461-475. Inches,
    one decimal. Columns Chinook / Coho / Pink. 2026: North of Cape Falcon (Westport and Columbia River) 22.0 /
    16.0; North of Cape Falcon (Neah Bay and La Push) 24.0 / 16.0; Cape Falcon to Humbug Mountain 24.0 / 16.0;
    Humbug Mountain to Oregon/California border 24.0 / 16.0; Oregon/California border to Latitude 40[deg]10' N
    20.0 / blank / 20.0; Latitude 40[deg]10' N to Point Arena 20.0 / blank / 20.0; Point Arena to Pigeon Point
    20.0 / blank / 20.0; Pigeon Point to U.S./Mexico border 20.0 / blank / 20.0. 2027: both North of Cape Falcon
    rows blank; Cape Falcon to Oregon/California border 24.0; OR/CA border to 40[deg]10' N 20.0; 40[deg]10' N to
    Point Arena 20.0; Point Arena to Pigeon Point 24.0; Pigeon Point to U.S./Mexico border 24.0. Footnote L475:
    "Metric equivalents: 24.0 in = 61.0 cm, 22.0 in = 55.9 cm, 16.0 in = 40.6 cm." (no equivalent for 20.0).
    The four California 2026 rows run together on L467.
  - Table 3 "Minimum Size Limits for Salmon in the 2026 Treaty Indian Ocean Salmon Fisheries" L538-540. One
    row: North of Cape Falcon, Chinook 24.0 / 18.0, Coho 16.0 / 12.0, Pink None.
  - Footnote \1\ L395-397 (attached to the Neah Bay Chinook guideline): "A subarea guideline is not a hard cap
    requiring closure when it is reached, but inseason action will be considered if the fishery is approaching
    the guideline."
  - Section 5 landmark list L587-605 (19 entries, latitude only). Last two entries print the same latitude:
    "Point Conception, CA 34[deg]27'00'' N lat." and "U.S./Mexico border 34[deg]27'00'' N lat."
- Lists:
  - Four STT reports L46-56 (Review of 2025 Ocean Salmon Fisheries; PRE I; PRE II; PRE III).
  - Fisheries opened before May 16, 2026 under the 2025 rule: four items L58-60.
  - Limiting stocks: south of Cape Falcon L73-77 "KRFC ... SRFC ... CC Chinook ... SONCC coho" (four); north
    L78 LCN coho, OCN coho, LCR natural tule Chinook (three); Queets spring/summer Chinook "was not a limiting
    stock" (L78). L152 repeats the southern list with three names (KRFC, CC Chinook, SONCC coho).
  - Stocks with ACLs: SRFC, KRFC, Willapa Bay natural coho (L107); FNMC has none (international exception).
  - Commercial troll areas north to south L168-263; recreational areas L390-455; tribes in C.1 L546-565
    (S'Klallam, Makah, Quileute, Hoh, Quinault).
  - Numbered comments: Comment 1 (L133), Comment 2 (L136) only; other comments summarized L125-131.
- Forecasts, guidance, deadlines, effective dates:
  - Process: 90 FR 61127 (Dec 30, 2025) and 91 FR 7263 (Feb 17, 2026) notices (L45); agendas 91 FR 5926 (Feb
    10, 2026), 91 FR 13591 (Mar 20, 2026); Council met "March 3 to 9, 2026" (L51); hearings "March 23, 2026, for
    Washington and California, and on March 24, 2026, for Oregon" (L52).
  - Forecast/projection pairs printed: SI forecast 392,349 (L85); KRFC projected natural spawners 30,143 (L83)
    vs MSST 30,525; KRFC 3-year geometric mean 34,093 (2023-2025) (L80); SRFC projected escapement 211,143 (L85);
    OCN prediction 218,600 (L99); Willapa projected escapement 29,800 (L117).
  - 2027 opening dates: commercial North of Cape Falcon May 1 (L188); Cape Falcon to Humbug Mountain, Heceta
    areas, Humbug Mountain to OR/CA border March 15 (L216, L222, L226, L230); California KMZ May 1 "under a 3,000
    Chinook salmon quota" (L233); Fort Bragg, San Francisco, Monterey May 1 (L239, L250, L261). Recreational:
    Cape Falcon to OR/CA border March 15 (L420); California KMZ May 1 (L434); Fort Bragg, San Francisco, Monterey
    April 3 (L440, L448, L455). Treaty troll May 1 (L527). Halibut retention April 1, 2027 (L350-351).
  - PRA: OMB 0648-0433, "expires on November 30, 2026"; "15 minutes per response" (L636-637).
- Hedged claims: L83 "potential for critically low natural spawner abundance could be considered high"; L84
  "considerable uncertainty exists over how removal ... might affect"; L86 "Indicators for the SRFC return in
  2026 are mixed"; L87 "could cause upward of 25 percent egg-fry mortality in natural spawners"; L30/L57
  "which we expect to be May 16, 2027"; L152 TAC comparisons "slightly lower" / "increased" with no totals printed.
- Rounded prose beside exact figures:
  - SRFC projected escapement "211,143" (L85) vs "211,100" (L113). KRFC "30,143" (L83) vs "30,144" (L115).
  - CC Chinook buffer, L94: "For 2026, the percent error is 43.3 percent. Therefore ... buffered pre-season
    age-4 KRFC harvest rate of 8.6 percent (i.e., 16 percent age-4 KRFC ocean HR- (0.463*0.16 percent age-4
    KRFC))". [mapper arithmetic: 16 x (1-0.463) = 8.59; 16 x (1-0.433) = 9.07.] Repeated at L139 "8.6 percent
    for age-4 KRFC (increased from 7.7 percent in 2025)".
  - FABC rounding: "FABC = FMSY x 0.90 = 0.52" (L112), "FMSY x 0.95 = 0.68" (L114), "= 0.70" (L116)
    [mapper arithmetic: 0.522, 0.6745, 0.703].
  - Comment counts: L122 "329 written comments ... and 8 oral comments"; "158 people; 37 people provided oral
    comments"; L629 "374 oral and written public comments" [mapper arithmetic: 329+8+37 = 374]. L124 "NMFS
    received no comments via the Federal Rulemaking Portal".
  - L141 Sacramento model expansion "approximately 10-20 percent" vs Klamath "92 percent"; L139 exceeded "from
    2018 through 2022 by 88 percent on average"; L142 "2025 recreational harvest guideline was exceeded by 25
    percent"; L626 "on average, 7 percent of commercial and recreational harvest occurred prior to May 16 during
    the years 2020 through 2024".
  - Halibut: "46,096 pounds (20,909 kg) preseason allocation to the salmon troll fishery" (L580).
- Notes: section line ranges - Background L39-41; Process L43-61; NEPA L63-65; Resource Status L67-103; ACLs
  L105-118; Public Comments L120-147; Specifications intro L149-157; Section 1 Commercial L159-379 (A L166-268, B
  L270-305, C L309-379); Section 2 Recreational L381-522 (A L388-455, B L457-475, C L477-522); Section 3 Treaty
  Indian L524-575; Section 4 Halibut Retention L577-581; Section 5 L583-605; Section 6 L607-610; Classification
  L612-640. L625 "coordination of management actions of four states" (rule text names Washington, Oregon,
  California).
- Operative definitions, rules and scope exceptions:
  - Exploitation/harvest-rate limits: KRFC "de minimis fishing ... total allowable exploitation rate of 25
    percent (including all ocean and river fisheries, including tribal fisheries)" (L81-82); SRFC "maximum
    allowable exploitation rate (ER) of 52 percent and a minimum hatchery and natural area escapement of 188,328
    adults", conservation objective range "122,000-180,000" (L85), goal "at least 180,000" (L86); SONCC coho "15
    percent for all populations ... except the Trinity River coho salmon population, which is limited to 16
    percent" (L89); CC Chinook "not to exceed a 16 percent age-4 ocean harvest rate (HR) on KRFC" (L90); LCR coho
    "not to exceed 23 percent" (L96); LCR tule "maximum of 41 percent" (L98); OCN coho "not to exceed 30.0
    percent" (L99).
  - CC Chinook buffer rule L90-94: "average percent error (defined as the difference between the preseason
    projected HR and the post-season estimated HR divided by the post-season estimated HR and expressed as a
    percentage) averaged over the most recent 5 years ... Only positive percent error will be applied". Scope
    L139: catch limit and landing/possession limits "currently apply only to the commercial fleet"; "buffered
    conservation objective applies to both the commercial and recreational fleets".
  - ACL formulas and worked numbers L111-117: escapement-based; "For SRFC in 2025, FMSY = 0.58 ... SOFL = 392,349
    x (1- 0.58) = 164,787. Because SRFC is a Tier-2 stock, FABC = FMSY x 0.90 = 0.52 ... SABC = 392,349 x
    (1-0.52) = 188,328"; KRFC "FMSY = 0.71 ... 40,191 x (1-0.71) = 11,655 ... Tier-1 stock, FABC = FMSY x 0.95 =
    0.68 ... 40,191 x (1- 0.68) = 12,861"; Willapa Bay natural coho "FMSY = 0.74 ... 35,153 x (1-0.74) = 9,140
    ... 0.70 ... 35,153 x (1-0.70) = 10,546". L111 "Where the conservation objectives exceed the ACLs, the
    management measures are designed to achieve the conservation objectives." Exclusion L107: ACLs are required
    for stocks "not managed under an international agreement, listed under the ESA, or designated as hatchery
    stocks" (50 CFR 600.310(h)(1)(ii)).
  - KRFC status L80: "MSST = 30,525"; declared overfished 2018; rebuilding plan 2020; now "not
    overfished-rebuilding". L83 escapement 30,143 "would represent the 18th lowest value over the past 48 years".
    SRFC overfished 2018, rebuilt 2021 (L85). Queets spring/summer Chinook overfished 2023 (L78).
  - SRKW threshold L101-103: 2026 estimate "exceeds the threshold", so Amendment 21 measures "are not required".
  - Commercial quotas, North of Cape Falcon: spring "May 16 through the earlier of June 29 or the attainment of
    37,300 Chinook salmon. If the Chinook salmon quota is exceeded, the excess will be deducted from the summer
    all-salmon season" (L171); subarea guidelines "No more than 7,460" (U.S./Canada Border to Queets River,
    L173-174) and "No more than 5,590" (Leadbetter Point to Cape Falcon, L175-176); weekly limits 50 then 80; 60
    then 250; 50 then 80 Chinook "per vessel per landing week" (L178-186), "Landing week is Thursday through
    Wednesday" (L177); summer "July 1 through the earlier of September 30, the attainment of 18,700 Chinook
    salmon, or the attainment of 19,600 marked coho salmon" (L191), 50 marked coho per vessel per landing week
    (L193).
  - Commercial south of Cape Falcon: Cape Falcon to Humbug Mountain "April 14, 2026-May 15, 2026; September
    1-October 31" (L211-212), "7,000 non-mark-selective coho salmon quota", 100 coho and 100 Chinook per vessel
    per landing week (L214); Cape Falcon to Heceta Bank Line "May 16-June 30; July 16-July 31" (L218-219);
    Heceta Bank Line to Humbug Mountain "May 16-June 30" (L224); Humbug Mountain to OR/CA border "April 14-30;
    May 16-June 17" (L227-228); California KMZ, Humboldt South Jetty to 40[deg]10' N, and Fort Bragg "Closed"
    (L231-238); San Francisco open periods L240-242; "Harvest limit of 83,000 Chinook salmon applicable to all
    open periods and management areas south of Point Arena from May through August. Landing limit of 160 Chinook
    salmon per vessel per open period" (L243, repeated L258); 38[deg]02' N to Pigeon Point subarea "September
    4-8, 11-15, 18-22, 25-30. Harvest limit of 20,000 Chinook salmon ... Landing limit of 100" (L247-248);
    Monterey open periods L253-257. Far-away companion rules: L156 "Fish caught in the areas south of Point Arena
    between May 1, 2026, and the date on which this rule becomes effective, are counted towards the harvest limit
    of 83,000"; C.8.h L371 "considered when total harvest reaches 50 percent of the harvest limit".
  - Recreational quotas, North of Cape Falcon (all "June 20 through the earlier of September 30 or attainment
    of"): Neah Bay "10,700 marked coho salmon subarea quota, with a subarea guideline of 13,110 Chinook
    salmon.\1\" (L391-395); La Push 2,680 / 2,200 (L403); Westport 38,070 / 21,910 (L406); Columbia River 51,450 /
    16,780 (L408). Bag limits L400-409 (1 salmon per day June 20-30 at Neah Bay and La Push; June 20-28 at
    Westport; 2 per day at Columbia River "no more than 1 of which may be a Chinook salmon").
  - Recreational south of Cape Falcon: mark-selective coho "June 6 through the earlier of August 23 or
    attainment of a 47,600 marked coho salmon quota" (L417); non-mark-selective "September 1 through the earlier
    of September 30 or attainment of a 27,500 non-mark-selective coho salmon quota" (L425); California
    area-specific harvest guidelines 3,900 (KMZ, L431), 5,100 (Fort Bragg, L438), 34,900 (San Francisco, L443),
    21,800 (Monterey, L451); "area-specific harvest guideline of 20,000 Chinook salmon applicable to the
    September and October open dates" (L446) and "statewide harvest guideline of 20,000 ... September and
    October open dates" (L454).
  - Treaty Indian L531-533: "May 1 through the earlier of June 30 or attainment of the 22,500 Chinook salmon
    quota"; "July 1 through the earlier of a date in September ... or attainment of the 22,500 Chinook salmon
    quota or 42,500 coho salmon quota".
  - Halibut: C.7 L341-361 - "no less than 32 inches (81.3 cm) in total length ... landed with the head on"
    (L344-345); "no more than 1 Pacific halibut per 2 Chinook salmon, except 1 Pacific halibut may be possessed or
    landed without meeting the ratio requirement, and no more than 35 halibut may be possessed or landed per
    trip" (L351). Section 4 L579-581 - Area 2A; either the incidental fishery "or in the directed commercial
    fishery targeting halibut but not both"; closure trigger at "46,096 pounds (20,909 kg)" or the total Area 2A
    non-Indian commercial allocation. L581 says TAC "for each IPHC management area, are listed under C.7"; C.7
    as read (L341-361) prints no TAC figures.
  - Other rules: 48-hour closed-area landing rule C.1 L311; Garibaldi 28-inch rule L204; 24-hour electronic fish
    ticket rule C.12 L379 and area text; transfer/rollover rules C.8 L364-371 and C.5 L512-518; KMZ definition
    for California code C.10 L377.
- Amendments or contradictions (both locations, no resolution):
  - Transmittal date: L56 "transmitted the recommended management measures to NMFS on April 24, 2026" vs L124
    "transmitted to NMFS on April 23, 2026".
  - L94 "43.3 percent" vs "0.463" in the same sentence (see Rounded prose).
  - L85 "211,143" vs L113 "211,100"; L83 "30,143" vs L115 "30,144".
  - L85 "Allowable Catch Limit" vs L105 "ACLs (Annual Catch Limits)".
  - L349 "Pacific Halibut Catch Share Plan" vs L579 "Pacific Halibut Fisheries Catch Sharing Plan" (same FR cite).
  - L604-605 identical latitudes for Point Conception and the U.S./Mexico border.
  - L73 four southern limiting stocks vs L152 three.
  - L139 framework "adopted into regulation in 2024"; 2026 "the first year of full implementation".
- Coverage: FULL. Ledger: L1-109, L110-229, L230-379, L380-528, L529-646 read in five chunks. Remaining
  unread: none. No graphics omitted; coordinates lists read (L354-361, L497-502, L587-605).

## D05 - Electronic Logbook Reporting in Commercial Fisheries of the Gulf of America and Atlantic

- Source: docs/fr_2026_10389.txt | text/D05.txt 177 lines | FR pages 30604-30609 | Doc 5
- Written or submitted by: NMFS/NOAA, Commerce (L24); signed Samuel D. Rauch III (L125). Mentioned, not
  authors: Gulf Fishery Management Council ("Gulf Council"), South Atlantic Fishery Management Council ("South
  Atlantic Council") (L43); SEFSC; GARFO; Atlantic HMS Management Division; ACCSP (L84); Mid-Atlantic and New
  England Fishery Management Councils (L70, L107).
- Type, date, edition: "Proposed rule; request for comments" (L26). 91 FR No. 100, Tuesday May 26, 2026; FR
  Doc 2026-10389; 50 CFR Part 622; Docket No. 260507-0128; RIN 0648-BN11; regulations.gov NOAA-NMFS-2025-0570;
  dated May 20, 2026 (L124); filed 5-22-26 (L176). Comments "no later than June 25, 2026" (L32).
- Period covered: no fishing-year table. Economic data "From 2017 through 2021" annual averages (L102), "All
  dollar figures presented below are in 2021 dollars" (L101). Program history 1990-2004 (L59).
- Entities and aliases: "Commercial Electronic Logbook Amendments" (L30) - once "Commercial Electronic
  Reporting Amendments" (L38); CFLP = "commercial coastal fisheries logbook program" (L55); CMP; "Gulf of
  America (Gulf)"; IFQ (Gulf, two programs) vs ITQ (South Atlantic wreckfish); eVTR/VTR; SRD and RA appear in
  the regulatory text (L141, L143) without expansion; PRA; OMB 0648-0016 "Southeast Region Logbook Family of
  Forms" (L114).
- Tables: not applicable (none). Footnotes: none.
- Lists:
  - Four FMP amendments L47-51: "(1) Amendment 35 to the CMP FMP; (2) Amendment 4 to the Dolphin and Wahoo FMP;
    (3) Amendment 54 to the Snapper-Grouper FMP; and (4) Amendment 57 to the Reef Fish FMP".
  - Four permit/species groups L51: CMP species in the Gulf and Atlantic; Atlantic dolphin and wahoo; South
    Atlantic snapper-grouper; Gulf reef fish.
  - CFLP roll-out L59: "began the CFLP in 1990" (Gulf reef fish); "South Atlantic snapper-grouper fishery
    (1992), the CMP fishery in the Gulf and Atlantic (1998), and the Atlantic dolphin and wahoo fishery (2004)";
    L60 shark fishermen under the HMS FMP "are also included in the CFLP".
  - Data-field changes named in the preamble L85-86: added - trip start time, trip end date, trip end time,
    trip type, primary area fished; removed - "including state trip ticket number and payment of catch";
    modified/defaulted - "hours/days", "sales disposition", catch disposition; signature field replaced by a
    perjury statement. Counts stated elsewhere: L105 "Six data fields would be added (although one is optional),
    three would be removed, and two would be modified"; L114 "a net difference of adding two required data fields
    and modifying two existing data fields".
  - Amended CFR sections L137-175: Sec. 622.26(a)(1) and new (a)(3) (Gulf reef fish); Sec. 622.176(a)(1), (4)
    and new (a)(5) (South Atlantic snapper-grouper); Sec. 622.271(a) (Atlantic dolphin and wahoo); Sec.
    622.374(a) ("king or Spanish mackerel", last, L173).
- Forecasts, guidance, deadlines, effective dates:
  - L46 "On November 20, 2025, NMFS published a notification ... (90 FR 52349). NMFS received 20 submissions";
    "On February 13, 2026, the Secretary approved the Commercial Electronic Logbook Amendments under section
    304(a)(3)".
  - L75 HMS e-logbook proposed rule "(89 FR 72796, September 6, 2024)"; "As of April 2026, the HMS Management
    Division has not published a final rule."
  - L107 "Since November 10, 2021, all commercial vessels with Federal permits issued by NMFS GARFO ... are
    required to submit eVTRs within 48 hours".
  - No effective date is proposed; L88 "Prior to the implementation date of a final rule".
- Hedged claims: L70 "may need to continue to submit multiple reports"; L87 "other vendors may create
  additional software applications. These vendors may charge a fee"; L104 "If each commercial vessel ...
  represents a unique commercial fishing business, then all ... are small"; L80-82 "NMFS expects"; L46 "if NMFS
  publishes a final rule"; L68 "NMFS is developing a separate proposed rule" (wreckfish ITQ).
- Rounded prose beside exact figures: L102 "annual average of 1,030 owners or operators ... reported making
  22,912 trips within the South Atlantic"; "666 owners or operators ... 8,037 trips within the Gulf" beside L106
  "reports 22 trips per year" (South Atlantic) and "12 trips per year" (Gulf) [mapper arithmetic: 22.2 and
  12.1]. L103 "$25,498" per active South Atlantic vessel; "$94,001" per active Gulf vessel; Gulf reef fish
  vessel "$121,609"; South Atlantic king mackerel vessel "$29,138"; largest "approximately $3 million"; "2,200
  inactive vessels with a commercial permit for Atlantic dolphin and wahoo".
- Notes: L62 current paper program - "selects 20 percent of permit holders" for trip expense and "20 percent"
  for the discard survey; "carbon paper logbook of approximately 100 pages containing 3 sections"; mailed "every
  December"; "in place since at least 2004". L68 "14 Gulf reef fish species though 2 IFQ programs". L116 burden
  "10 minutes per electronic fishing report and 2 minutes per no-fishing report". L104 small-business standard
  "$11 million" (NAICS "11411", 50 CFR 200.2).
- Operative definitions, rules and scope exceptions:
  - Current deadline L62: "within 7 days after finishing a trip or after a month without any fishing activity".
    Proposed L83: "no later than 7 days after the end of each fishing trip ... If no fishing occurred during a
    calendar month, an electronic no-fishing report must be submitted electronically no later than 7 days after
    the end of that month ... a no-fishing report may be submitted anytime in advance". L79 "The deadline ...
    would not change"; selection process for trip expense and discard portions "would also remain the same".
    Regulatory text repeats the 7-day rule four times (L141, L152, L165, L173) with "no later than" / "not later
    than" variants.
  - Other programs' timings (not changed by this rule): GARFO eVTR "generally within 48 hours of the end of a
    commercial fishing trip (50 CFR 648.7)" (L70), "(unless required sooner, as with some northeast groundfish
    sector programs)" (L107); HMS via CFLP "within 48 hours of completion or before offloading fish from the
    vessel, whichever is sooner ... postmarked within 7 days of offloading all HMS" (L71).
  - Scope: applies to commercial permits for Gulf reef fish, Gulf or Atlantic CMP species, Atlantic dolphin and
    wahoo, South Atlantic snapper-grouper (L101); also vessels without a CMP permit that harvest cobia (L101).
    Exclusions: "The IFQ and ITQ reporting systems are not logbook programs and operate independently of the
    CFLP ... would remain unchanged" (L69); "would not change any other existing reporting requirements" (L101,
    L107). L100 "no new reporting, record-keeping, or other compliance requirements are introduced".
  - Catastrophic-conditions clause (new in each amended section): L143, L153-157, L166, L174.
  - L87 "paper logbooks would no longer be accepted"; ACCSP software "would be free".
- Amendments or contradictions (both locations, no resolution):
  - L107 "Since November 10, 2021" vs, in the next sentence, "since November 21, 2021".
  - L30 "Commercial Electronic Logbook Amendments" vs L38 "Commercial Electronic Reporting Amendments".
  - L105/L114 field counts (6 added, 3 removed, 2 modified) vs the fields named at L85-86 (five additions and
    two removals named).
  - Juxtapositions, not necessarily conflicts: L59 CMP joined the CFLP in 1998 and dolphin/wahoo in 2004 beside
    L62 requirement "in place since at least 2004 for the affected Federal fisheries"; L100 "No duplicative,
    overlapping, or conflicting Federal rules have been identified" beside L112 "expected to reduce duplication
    or overlap of existing record-keeping and reporting requirements".
- Coverage: FULL. Read L1-177 in one pass. Remaining unread: none.

## D06 - Atlantic HMS; North Atlantic Swordfish, South Atlantic Swordfish, North Atlantic Albacore, and Atlantic Bluefin Tuna Quotas (final)

- Source: docs/fr_2026_16870.txt | 91 FR 53526-53539 | text/D06.txt L1-398 (caller read in full, 2026-10-10)
- Written or submitted by: NMFS; final rule, temporary quota adjustment and temporary quota transfer, RIN
  0648-BN60, Docket No. 260813-0186
- Type, date, edition: final rule for D03, published and effective August 19, 2026 (dated August 13,
  2026); temporary adjustments and transfer effective through December 31, 2026 (L30)
- Period covered: 2025 and 2026 columns in every quota table; 2025 landings; 2024 prices; 2025 permits
- Entities and aliases: as D03; transfers to Costa Rica (2025), Namibia, Cote d'Ivoire, Belize
- Tables: Table 1 (L83-88) North Atlantic swordfish 2025 / 2026: baseline 2,937.6 / 2,937.6; transfers
  (-) 225.6 / 0; "Underharvest from Previous Year" 2,558.3 / 2,514.9 (each column holds the prior year's
  shortfall); carryover (+) 440.6 / (+) 440.6; adjusted 3,152.6 / 3,378.2; directed 2,802.6 / 3,028.2;
  incidental 300; reserve 50. Table 2 (L98-102) South Atlantic: 75.2 throughout, transfers (-)75.2. Table 3
  (L115-118) albacore: baseline 889.4; underharvest 838.9 / 923; carryover 222.4; adjusted 1,111.8 /
  1,111.8. Table 4 (L132-158) bluefin baseline subquotas (same as D03 Table 1). Table 5 (L188-195) bluefin
  2025 / 2026: baseline 1,316.14 / 1,509.98; total 1,341.14 / 1,572.48; under or over harvest -141.2 /
  74.8; adjusted 1,199.94 / 1,647.28; baseline Reserve 38.2 / 43.8; adjusted Reserve NA / 112.2.
- Lists: comments 1-5 (L209-231); "39 written comments" (L62, L208, L258)
- Forecasts, guidance, deadlines, effective dates: says the comment period "closed on June 6, 2026" (L62;
  D03 set June 8, 2026)
- Hedged claims: as D03's analysis
- Rounded prose beside exact figures: "3,963-mt dw" (L75) for D03's 3,963.0
- Notes, D06-only inputs: 2025 landings 637.7 mt dw swordfish (2,514.9 mt dw under the adjusted quota,
  L78), none for South Atlantic (L95), 188.8 mt albacore (923 mt under, L113), 1,125.1 mt bluefin against
  an adjusted 1,199.94 mt including the 25-mt NED set-aside (L185); bluefin carryover cap "10 percent of
  its total annual quota, which equates to 134.1 mt for 2025" (L184; D03 says baseline quota); inseason
  chain (L166-169): July 6.4 mt Reserve to Harpoon (65.6, then 74.3 on the new baseline), February 30.8 mt
  Reserve to Longline (240.1, then 270.9), Reserve 1 mt, then 6.6, then 37.4 after 30.8 mt back from
  Longline, then 112.2 with the 74.8 mt underharvest (L186).
- Operative definitions, rules and scope exceptions: regulatory text L353-396 repeats D03's with "(e)(2) or
  (e)(3)" added in section 635.15(d)(1) and (2) (L235)
- Amendments or contradictions: FRFA bluefin revenue re-done with "1.25 dw conversion factor" (L301-317):
  totals $11.1 million (C1) and $13.2 million (C2); per permit C1 $3,066 / $16,282 / $40,562, C2 $3,518 /
  $18,675 / $52,386, gains $452 / $2,393 / $11,824. Swordfish and albacore figures unchanged from D03
  ($33,365,000; $39,141,000; $34,755; $40,772; $6,017; $4,519,000; $4,826,000; $1,698; $1,813; $115).
  D03's total of 7,664 small entities is dropped. Slip at L79: carryover "to the 2025 fishing year".
- Coverage: full (L1-398)

## D07 - Pacific Halibut IFQ Vessel Use Caps in IFQ Regulatory Areas 4A, 4B, 4C, 4D, and 4E

- Source: docs/fr_2026_18031.txt | text/D07.txt 189 lines | FR pages 56606-56611 | Doc 7
- Written or submitted by: NMFS/NOAA, Commerce (L22); signed Samuel D. Rauch III (L153). Mentioned, not
  authors: North Pacific Fishery Management Council ("Council", L46); IPHC; Pacific Fishery Management Council
  (L118, named separately from "the Council"); CQE for Adak; CDQ groups.
- Type, date, edition: "Proposed rule; request for comments" (L24). 91 FR No. 170, Thursday Sep 3, 2026; FR
  Doc 2026-18031; 50 CFR Part 679; Docket No. 260817-0010; RIN 0648-BO24; regulations.gov NOAA-NMFS-2026-1025;
  dated Aug 28, 2026 (L152); filed 9-2-26 (L188). "Submit comments on or before October 5, 2026" (L30).
- Period covered: worked numbers use 2026 catch limits (2026 annual management measures, 91 FR 14464, March
  25, 2026; L45, L78, L101). Temporary cap removals cover IFQ fishing years 2020-2027 (L82). Revenue data year
  2024; participation window 2020-2024 (L141). IFQ "fishing year" is not defined by dates in the text.
- Entities and aliases: IFQ Program (halibut and sablefish; "specific to halibut unless otherwise noted", L58);
  QS = quota share; CQE = Community Quota Entity; CDQ = Western Alaska Community Development Quota Program;
  "Area 4" = Areas 4A-4E collectively (L51); "vessel use cap" = "vessel harvest limit" = "vessel limit";
  "Alaska coastwide" (L71) also "coastwide vessel use cap" (L101); "the Analysis" = draft RIR (L37, L125);
  Halibut Act = Northern Pacific Halibut Act of 1982; CV = catcher vessel. Area definitions L59: 2C Southeast
  Alaska; 3A Central Gulf of Alaska; 3B Western Gulf of Alaska; 4A eastern Aleutian Islands; 4B central and
  western Aleutian Islands; 4C, 4D, 4E Bering Sea.
- Tables: not applicable (none). Footnotes: none.
- Lists: four QS vessel categories A-D (L61); four other IFQ Program limits (L64); three ways "annual
  commercial catch limit" is defined (L77); four numbered changes proposed (L94-95); three existing caps that
  continue (L97-98); four FR cites for the temporary actions (L82, repeated L135; last "88 FR 48137, July 26,
  2023"); proposed Sec. 679.42(h)(1)(i)-(v) with (v)(A)-(D) (L172-186).
- Forecasts, guidance, deadlines, effective dates: comments due Oct 5, 2026 (L30); "the temporary removal of
  vessel use caps will expire, and the Alaska coastwide vessel use cap ... would apply to all Area 4 halibut IFQ
  fishing activity beginning in the 2028 fishing season" (L83-84); impacts assessed "after the 2027 fishing
  season" (L84, L144). No effective date proposed. Historical cites: IFQ Program 58 FR 59375, November 9, 1993
  (L47); proposed rule 57 FR 57130, December 3, 1992 (L70); CQE for Adak 79 FR 8870, February 14, 2014 (L65);
  small-entity standard 80 FR 81194, December 29, 2015 (L140).
- Hedged claims: L89 "possibly necessitated by the need to travel longer distances"; L90 "suggest that raising
  vessel use caps may enable ... potentially leading to greater catch utilization"; L99 Area 4 limit "could
  exceed" the coastwide limit; L100-101 "would generally be a larger amount"; L101 counterfactual "had this Area
  4 vessel use cap been in place in 2026, it would have been 132,900 lb"; L112 "may afford"; L141 "some vessels
  ... may be fully or partially owned by CDQ groups".
- Rounded prose beside exact figures: every weight is printed as lb with rounded mt - "69,540 lb (31.5 mt)",
  "28,100 lb (12.7 mt)" (L78); "132,900 lb (60.3 mt)", "63,360 lb (28.7 mt)" (L101); "100,000 lb (45.4 mt))",
  "32,900 lb (14.9 mt)" (L107); "50,000 lb (22.7 mt)" (L73, L98, L181). [mapper arithmetic: lb route 132,900 -
  69,540 = 63,360 and 69,540 - (100,000 - 63,360) = 32,900 match the print; mt route 60.3 - 31.5 = 28.8 and 31.5
  - (45.4 - 28.7) = 14.8 differ from the printed 28.7 and 14.9 by 0.1.] Underlying catch limits are not printed
  [mapper arithmetic: 69,540/0.005 = 13,908,000 lb; 28,100/0.01 = 2,810,000 lb; 132,900/0.05 = 2,658,000 lb].
- Notes: RFA facts L141-142 - "2024 revenue data exist for 87 vessels that actively participated in the
  halibut IFQ fishery in Areas 4A, 4B, 4C, and 4D from 2020-2024. Of the 87 vessels, 85 were considered small
  entities in 2024"; "Six CDQ groups are considered to be small entities". NAICS printed "114111" (L140). L129
  "Senior Lead Counsel for Regulation". PRA: no information collection (L121). E.O. 14192 not mentioned.
- Operative definitions, rules and scope exceptions:
  - Current caps L71-74: "no vessel can be used to harvest more IFQ halibut than one-half percent of the
    combined total catch limits of halibut of those areas" (Areas 2C, 3A, 3B, 4A-4E; "Alaska coastwide");
    "temporary exception that exempts vessels harvesting IFQ halibut in Areas 4A, 4B, 4C, and 4D from this
    Alaska coastwide vessel use cap through 2027 (Sec. 679.42(h)(1)(iii))"; Area 2C "more than one percent of the
    annual commercial catch limit for halibut in Area 2C"; CQE "more than 50,000 lb (22.7 metric tons (mt))".
  - Instances, L78: "Calculated as proportions of the applicable annual commercial catch limits, the 2026
    Alaska coastwide and Area 2C IFQ halibut vessel use caps are 69,540 lb (31.5 mt) and 28,100 lb (12.7 mt),
    respectively."
  - Definition L77: "annual commercial catch limit" three ways - Areas 2C and 3A "annual commercial allocation
    minus an Area-specific estimate of commercial halibut wastage"; Areas 3B and 4A "total allowable removals by
    persons fishing IFQ halibut"; Areas 4B, 4C, 4D, 4E "annual total allowable halibut removals by persons
    fishing IFQ and CDQ". L109-111: "annual commercial catch limits" replaces "total catch limits" and "does not
    change the calculation".
  - Proposed Area 4 cap L94-99 and SUMMARY L28: "five percent of the total annual commercial catch limit across
    Areas 4A, 4B, 4C, 4D, and 4E"; "separate from and could exceed the Alaska coastwide vessel use cap". Instance
    L101 (132,900 lb; 63,360 lb greater than the 69,540 lb coastwide cap).
  - Accrual rule L99, L102-107 and reg text L183: "the amount of a vessel's harvest of IFQ halibut in area 4
    equal to the difference between the area 4 vessel limit and the Alaska coastwide vessel limit will not count
    towards the Alaska coastwide vessel limit." Worked example L107: "a vessel operating under the 2026 catch
    limits harvests 100,000 lb (45.4 mt)) in Area 4 and deducts ... (63,360 lb (28.7 mt)) ... This would allow
    that vessel to harvest an additional 32,900 lb (14.9 mt) across Areas 2C, 3A, and 3B".
  - Exceptions: CQE-held QS in Area 4B "does not count toward this area 4 vessel limit" (L180, L185; preamble
    L108) but "all CQE-derived IFQ halibut would continue to count toward the Alaska coastwide vessel limit"
    (L108; reg L183 "(including IFQ halibut derived from CQE-held QS)"); CQE limit plus limits (i)-(iii) both
    apply (L181). CDQ allocations "are not subject to a vessel use cap and are not affected" (L65); "halibut
    harvested in Area 4E is currently entirely allocated under the CDQ Program" (L72). L182 limits "are applied
    at the time of landing".
  - Paragraph renumbering: current (h)(1)(i) Area 2C, (h)(1)(ii) CQE, (h)(1)(iii) temporary exception (L72-74);
    proposed (h)(1)(i) coastwide, (ii) Area 2C, (iii) Area 4, (iv) CQE, (v) calculations (L97-98, L173-186).
  - L143 "this proposed rule does not increase catch limits in Area 4".
- Amendments or contradictions (both locations, no resolution):
  - Years of the temporary removal: L82 "Areas 4B, 4C, and 4D for IFQ fishing years 2020-2027 and in Area 4A
    for 2021-2027" (also L135) vs L95 "in the years 2023 through 2027" and L98 "from 2023-2027".
  - Coastwide area list: L71, L97, L173 include 3B vs L136 "IFQ Areas 2C, 3A, 4A, 4B, 4C, 4D, and 4E".
  - Regulated universe: L130 "Areas 4A, 4B, 4C, 4D, or 4E" vs L139 "Area 4A, 4B, 4C, or 4D".
  - Cite for the Area 2C cap: L72-73 "(Sec. 679.42(h)(1)(i))" vs L75-76 "Area 2C (Sec. 679.42(h)(1))".
  - Unbalanced parenthesis at L107 "100,000 lb (45.4 mt))".
- Coverage: FULL. Read L1-189 in one pass. Remaining unread: none.

<!-- Read actual candidate-relevant passages with context and search the entire bundle for
duplicates/substitutes. A search is not a full read. Expand coverage when the candidate needs it;
lists/counts require the complete relevant universe, and needed gaps stay blocking. -->

## Shared ground (navigation only)

Scope: D01, D04, D05, D07 against all seven texts. D02/D03/D06 locations below come from grep snippets only,
not from a read of those documents.

- Boilerplate present across the set (listed once): issuer NMFS/NOAA/Commerce and signer "Samuel D. Rauch III"
  in all seven (D01 L212, D02 L257, D03 L278, D04 L643, D05 L125, D06 L340, D07 L153); small-business standard
  "$11 million" (D02 L208/L212, D03 L210-211, D05 L104, D06 L263-268, D07 L140; absent from D01 and D04, which
  state RFA does not apply: D01 L203, D04 L635); NAICS "11411" in D02/D03/D05/D06 vs "114111" in D07 L140;
  80 FR 81194 (D03 L210, D06 L263, D07 L140); E.O. 12866 (D02-D07); E.O. 14192 "not ... regulatory action" (D01
  L203, D02 L204, D03 L200, D04 L618, D05 L97), "is an Executive Order 14192 deregulatory action" (D06 L253),
  not mentioned in D07; E.O. 13175 (D01 L205, D06 L254-255); good-cause waivers 5 U.S.C. 553(b)(B)/(d)(3) (D01
  L197-200, D04 L619-631, D06 L241-242); PRA "no information collection" (D01 L204, D02 L250, D03 L271, D06
  L333, D07 L121) vs collections 0648-0433 (D04 L636) and 0648-0016 (D05 L114); National Standards 1/2 (D01
  L143-171, D02 L52, D03 L51, D06 L56) and 7 (D05 L44); 50 CFR 600.310 cited in D01 L161 and D04 L107
  (different paragraphs).
- Entities that appear in more than one document, and where:
  - Pacific halibut 2026 annual management measures, same FR cite: D04 L349 "See the most current Pacific
    Halibut Catch Share Plan for more details (91 FR 14464, March 25, 2026)" and D04 L579 "Pacific Halibut
    Fisheries Catch Sharing Plan 2026 annual management measures (91 FR 14464, March 25, 2026)"; D07 L45 "The
    IPHC's 2026 annual management measures were published in the Federal Register on March 25, 2026 (91 FR
    14464)", also D07 L78, L101. D04 covers Area 2A (L579-580, "46,096 pounds (20,909 kg) preseason allocation to
    the salmon troll fishery"); D07 covers Areas 2C, 3A, 3B, 4A-4E (L59) and never mentions Area 2A. IPHC: D04
    L581; D07 L45-46, L114, L118-119. Halibut Act authority: D04 L616 "16 U.S.C. 773(c)" and L640 "Authority: 16
    U.S.C. 773-773k; 1801 et seq."; D07 L46 "16 U.S.C. 773c", L129 "(16 U.S.C. 773-773k)". "Catch Sharing Plan"
    is in D07's title (L20).
  - Pacific Fishery Management Council: D04's "Council" (L32); D07 L118 "Regulations governing the U.S.
    fisheries for halibut are developed by the IPHC, the Pacific Fishery Management Council, the Council, and
    the Secretary" (there "the Council" = North Pacific, L46).
  - "Council" means a different body in each: New England (D01 L46), Pacific (D04 L32), Gulf and South Atlantic
    (D05 L43), North Pacific (D07 L46). No "Council" in D02/D03/D06 other than "HMS Advisory Panel" hits (D02
    L70, D06 L62, L208, L258).
  - New England Fishery Management Council / GARFO / 50 CFR part 648 / groundfish sectors: D01 (whole rule; L15,
    L34, L46; L198 "Groundfish sectors constitute 96 percent of all commercial groundfish catch") and D05 L70
    "All commercial vessels with Federal permits issued by NMFS GARFO for species managed by the Mid-Atlantic or
    New England Fishery Management Councils are required to submit vessel trip reports (VTRs) electronically as
    eVTRs generally within 48 hours ... (50 CFR 648.7)" and D05 L107 "(unless required sooner, as with some
    northeast groundfish sector programs)". D01 itself says nothing about VTR/eVTR or logbooks (grep: none; only
    "at-sea monitoring coverage" L176 and "100-percent monitoring coverage target" L178).
  - Shark limited access permit holders and their gear: D05 L71 "NMFS also uses the CFLP to collect HMS
    landings and effort related data from vessel owners primarily with commercial, limited access shark fishing
    permits using bottom longline, gillnet, or vertical line (including bandit) gear"; D05 L60 "Fishermen that
    target shark species under the FMP for highly migratory species (HMS) ... are also included in the CFLP".
    D02 L58 "Directed shark limited access permit (LAP) holders and ... Incidental shark LAP holders"; D02 L90
    "commercial fishermen fishing with gillnet and bottom longline gears"; D02 L353/L356 "pelagic longline,
    bottom longline, or gillnet gear". D02 data sources named: "Southeast Fisheries Science Center Observer
    Program data from 2017 through 2022" (L90-91) and "HMS electronic dealer reporting system (eDealer) data from
    2017 through 2022" (L92); D05's source is "SEFSC logbook data" (L103) for 2017-2021 (L102).
  - HMS Management Division: D05 L60, L66, L71, L75; D02 L35; D06 L332 (website references in D02/D06).
  - HMS species named in D05 L60 "various tunas, billfishes, and sharks" = subject fisheries of D02 (sharks)
    and D03/D06 (swordfish, northern albacore, bluefin tuna).
  - Catch-share acronyms, different programs: Gulf "IFQ" and South Atlantic wreckfish "ITQ" (D05 L66-69, L101,
    L107); Alaska halibut/sablefish "IFQ Program" (D07 L47, L58); pelagic longline "IBQ" (D03 L171 ff., D06 L202,
    L359). Limited-access wording: D07 L60 "quota share (QS), which is the limited access permit"; D01 L151 "each
    limited access permit holder"; D02 L58 LAP.
  - Canada: D01 L40 "shared stocks between the United States and Canada" and Table 4 "Eastern U.S./Canada
    haddock SAP"; D04 L71 Pacific Salmon Treaty, L51 U.S./Canadian salmon managers; D07 L45 Convention with
    Canada. No "Canad" in D02, D03, D05, D06.
  - "Halibut" as a word: D01 L61 only as the stock row "Atlantic Halibut" (75 / 58 / na / 58 / 16 / 1.2); D04 18
    hits and D07 65 hits are Pacific halibut; none in D02, D03, D05, D06.
  - "Sector": D01 = groundfish sectors with operations plans (L42, L198); D02 L69/L136 "recreational sector
    ACLs"; D05 L112 "commercial fishing sectors"; D03 L211 / D06 L264 "respective sector's standard".
  - Tribal content: D04 Treaty Indian fisheries (L524-575) and tribal testimony (L53-55); D01 L205 and D06
    L254-255 only the E.O. 13175 statement.
- Periods or series that more than one document covers, and where:
  - Fishing-year conventions differ: D01 May 1-April 30 (L46, L192); D04 May 16-May 15 (L619); D05 none; D07
    "IFQ fishing year" undated; D02 "start of each fishing year" (L84, L355); D06 temporary adjustments
    "through December 31, 2026" (L30) and "calendar year" (L359).
  - Publication order: D01 Oct 3, 2025; D02 Jan 5, 2026; D03 May 7, 2026; D04 May 19, 2026; D05 May 26, 2026;
    D06 Aug 19, 2026; D07 Sep 3, 2026. DATES lines: D01 L31, D02 L30 ("by March 6, 2026"), D03 L32 ("by June 8,
    2026"), D04 L30, D05 L32, D06 L30, D07 L30.
  - Data windows: D05 2017-2021 (L102); D02 2017-2022 (L90-92, L231); D07 2020-2024 and 2024 revenue (L141); D03
    L211 / D06 L268 2024 revenue.
- Documents that cite, amend or respond to another document in the bundle:
  - None of D01, D04, D05, D07 is cited by FR page, docket or RIN in any other document, and none of them
    cites another bundle document (full `NN FR NNNN` cite list inspected for all seven). Their shared external
    cite is 91 FR 14464 (D04/D07) only.
  - Caller-owned pair, located by cite grep only: D06 L47, L62, L240 cite "91 FR 24789" = D03's first page (D03
    L6 "[Pages 24789-24800]"); both carry RIN 0648-BN60 (D03 L20, D06 L18) and docket NOAA-NMFS-2025-0053 (D03
    L34, D06 L208).
  - Out-of-bundle predecessors: D01 extends 90 FR 18804; D04 follows 90 FR 20810 / 90 FR 26943; D05 follows
    90 FR 52349 and mentions 89 FR 72796; D07 follows 85 FR 41197, 86 FR 28294, 87 FR 34215, 88 FR 48137.
- Forecast/actual pairs, repeated/changed tables, same-period conflicts and scope relationships (locations only):
  - Weight-unit pairs printed with both units: D01 L183 "47 mt (103,617 lb)"; D07 L73-107 (seven lb/mt pairs);
    D04 L580 "46,096 pounds (20,909 kg)"; D02 L91 "37,921 pounds (lb) dressed weight (dw) (17.2 metric tons (mt)
    dw)". No document prints a lb-per-mt factor (grep "2,204|2204": none). Weight bases differ: D01 "live weight"
    (table captions L56-88); D02 "dressed weight"; D03 L44 / D06 L48 "The conversion factor between dw and ww for
    swordfish is 1.33", "1.15 dw conversion factor" (D03 L231, D06 L295), "1.25 dw conversion factor" (D06 L302).
  - Limits computed as a percentage of a total: D07 one-half percent / 1 percent / 5 percent of annual commercial
    catch limits (L71-72, L99); D01 75 percent default rule (L146) and Table 3 percentages of the common pool
    sub-ACL (L70-80); D04 FABC = FMSY x 0.90 or x 0.95 (L112-116) and 50 percent trigger (L371); D06 L112, L118
    "25 percent of its baseline quota (i.e., 222.4 mt)" and D03 L107, L115 (carryover cap).
  - Reporting-timing rules: D05 7 days (L62, L83) and 48 hours (L70, L71, L107); D04 24 hours for electronic
    fish tickets (L233, L379) and landing after closures (L196). No "48 hours", "7 days" (other than meeting
    notices D02 L191, D03 L192) or logbook wording in D02, D03, D06.
  - ACL/ABC/OFL vocabulary: D01 (15 hits; L39, L144-147, L168-171), D04 (13 hits; L105-118, escapement-based),
    D02 L59, L61 (overfished), L69, L136, L163, L172 (ACL framework), D03 (16 hits) and D06 (6 hits) - TAC in
    every hit inspected (first 30 of the combined list; D03 hits past L67 not inspected), D07 L146 once
    ("annual catch limits").
  - Emergency-rule content exists only in D01 (grep "emergenc" in D02-D07: none).
  - Proposed vs final within these four: none are paired (D01 temporary rule, D04 final rule with no proposal in
    the bundle, D05 and D07 proposals with no final rule in the bundle).
- Searches run over all seven texts and inspected (hits recorded above; "none" = no match outside the home
  document): `91 FR 14464`; halibut; logbook|CFLP (none outside D05); `89 FR 72796`|eVTR|VTR|electronic report
  (none outside D05); council names; shark|HMS|swordfish|tuna|albacore|billfish (in D01/D04/D05/D07: D05 only);
  limited access|bottom longline|gillnet|bandit|vertical line; GARFO|Greater Atlantic|groundfish|part 648 (D01,
  D05 only); IFQ|ITQ|IBQ|quota share; `$11 million`; NAICS; 2,204|conversion factor|dressed/whole/live weight;
  emergenc; fishing year|calendar year; Rauch|Dated|Filed; Executive Order numbers; place names (Gulf of
  Maine, Georges Bank, New England, Alaska, West Coast, Pacific, Oregon, California, Massachusetts, Gloucester,
  Bering, Aleutian: in D02/D03/D06 only "Northeast Distant"/"Northeast Coastal" at D03 L41, L171, L258, D06 L185);
  Canad; 600.3xx|National Standard; OMB control numbers; 553(b)(B)|553(d)|16 U.S.C.; salmon|cod|haddock|
  pollock|mackerel|dolphin|wahoo|cobia|snapper|grouper|reef fish|wreckfish|sablefish (in D02/D03/D06: none; D07
  L58 sablefish); ACL/TAC family; Indian|Tribe|CDQ; RIR|Supplemental Impact Report; ICCAT|one stop|inseason;
  observer|at-sea monitoring|VMS; Atlantic region|blacknose; all `NN FR NNNN` cites; DATES lines; docket/RIN.
