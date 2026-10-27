# aq-02486 - document map

Maintained by the caller from `text/` (plain-text Federal Register captures, no layout issues).
Navigation only: where things are, not what to ask. Questions quote the documents, never this map.
Line numbers are `text/Dnn.txt` lines (line 1 = extraction header).

## Bundle

- What it is: seven unrelated Federal Register documents on agency fees, five of them FOIA rules
  (FLRA final 2023, Peace Corps final 2024, NRC final 2026, ONCD proposed 2026, Access Board proposed
  2026), plus the Copyright Office's proposed 2026 fee schedule and DHS's proposed Form I-246 fee.
  No proposal/final pair for one agency, no editions of one series.
- Documents: 7; local ids D01-D07 equal page Doc 1-7 (alphabetical file names match the page order).
- Gaps: none. Capture says "7 of 7 read in full (512,260 characters)"; notes/intake.json shows every
  document complete, `matches_capture: true`, gap_characters 0. Caller read all seven texts in full
  on 2026-10-09 (D02 and D03, D04 in chunks; every line covered).
- Extraction spot-checks: text captures, method `text`; extraction equals source minus the header
  (D01 35,918 -> 35,915 chars etc.). Checked tables: D04 fee tables (lines 293-303, 339-358,
  412-425, 553-571) keep current/proposed/cost columns in row order but flattened; D06 Tables 1-3
  (lines 205-271) flattened with values in order. Footnotes kept inline (D04 \1\-\113\, D06 \1\-\24\).
  No page images; not-applicable.
- Provenance: notes/intake.json, capture AQ-02486_2026-10-09_0906.txt sha256 440105323f50...
- Reuse binding: source sha256 per doc in text/manifest.json (D01 4649cc1b..., D02 0bb96d07...,
  D03 629f5727..., D04 fccca899..., D05 6dfc4c86..., D06 91190780..., D07 b5df280d...). No other
  workspace bundle holds these files (sha256 search 2026-10-09).

## D01 - FLRA, Availability of Official Information, final rule (5 CFR 2411)

- Written by: Federal Labor Relations Authority. FR Sept 29, 2023; "Effective September 29, 2023" (25);
  approved Sept 21, 2023 (240). Exempt from comment (55).
- Cites OMB 2020 Update, 85 FR 81955 (Dec. 17, 2020) (30-31). Authority line gives FOIA Improvement
  Act "130 Stat. 528" (69; D02/D03/D07 print 538).
- Fees (2411.13): request = agreement to pay "up to $25.00" unless waiver sought (88); records sent
  with response if fee "less than $250.00" (129, 156); direct costs basic pay plus 16 percent (174);
  first 100 pages and two hours free except commercial; "No search or review fees will be charged for a
  quarter-hour period unless more than half of that period is required" (179); no fee if cost of
  collecting >= fee (180); duplication "Twenty-five cents per page" (206); manual search at employee
  salary rate (204); interest from 31st day (209-210); advance payment if likely > $250; 30 days (211-217).
  No "$25 or less, no fee" rule.
- Time: 20 working days; 10 days misdirected (122-127); appeal 90 calendar days (145); appeal decision
  20 working days (154). Annual report "as requested by the Department of Justice's Office of
  Information Policy" (235).

## D02 - Peace Corps, FOIA disclosure procedures, final rule (22 CFR 303)

- FR April 11, 2024; "effective May 13, 2024" (27); signed March 27, 2024 (560).
- FOIA Improvement Act signed June 30, 2016; prior rule April 10, 2014 (79 FR 19816), effective
  May 12, 2014 (31). Proposed Nov 28, 2023 (88 FR 83044) (87); "30-day comment period between
  November 28 and December 28, 2023", "nine comments from three members of the public and one
  501(c)(3) nonpartisan organization" (91); eight numbered comment responses (99-141).
- Definitions 303.2 (183-218): compelling need has a third prong (193); search note "2 hour search" (208).
- Timing: 20 business days, extension up to 10 business days (286); expedited decision "Within 10
  business days" (296) vs "within 10 calendar days" (315); tracking if > 10 working days (354);
  appeal 90 calendar days (386). OIP consulted on exclusions (363). GRS 4.2 (431).
- Fees 303.16: three requester categories (438-441); "For each quarter hour spent" (462); photocopies
  "no charge up to 100 pages" (465) but no per-page rate printed anywhere; quarter-hour more-than-half
  rule (478); first 100 pages / 2 hours free (479-481); "No fee will be charged when the total fee, after
  deducting the 100 free pages ... and the first 2 hours of search, is equal to or less than $25" (482-483);
  notice > $25.00 (484); interest 31st day (492, 518); aggregation presumption 30-day (493); advance
  > $250.00 (495); 30 calendar days (496-497); minimal amount rule (516).

## D03 - NRC, FOIA implementing regulations, final rule (10 CFR 9 subpart A)

- FR March 6, 2026; "effective on March 6, 2026" (40); dated March 4, 2026 (746). No comment (149-150).
- E.O. 14300 signed May 23, 2025 (72; table: "May 29, 2025", 242-244). Initial FOIA regs June 29, 1967
  (76). OGIS assessment Sept 16, 2020; DOJ OIP template Dec 2, 2022 (77). SECY-24-0024 March 20, 2024;
  SRM "April 24, 2024" (82) vs table "dated April 26, 2024" (220-222).
- Definitions 9.13 (326-357): direct costs 16 percent (339); five fee categories incl. "Other requester" (348).
- Timing 9.26: 20 working days (499); three tracks, complex > 30 working days (502-505); extension <= 10
  working days, six factors (511-517); expedited 10 calendar days (529). Business info: 30 calendar days to
  object (573); disclosure >= 30 calendar days after notice (578). Appeal 90 days; expedited-denial appeal
  10 calendar days (590-591); decision 20 working days (604).
- Fees: 9.35 PDR contractor rates "$0.30 per page" paper, priority $0.35, fax etc. (629-642); NRC copies
  elsewhere "$0.20 per page" (647). 9.37 FOIA: electronic response, no duplication fee unless paper/scan,
  then "$0.20 per page" (659-660); search/review "rounded up to the nearest full hour", GG-9/step 7,
  GG-14/step 7, ES-Maximum, plus 16 percent (661-664); fee category within 20 calendar days (667); first
  100 pages / two hours free for other requesters (680-681); no fee if collection cost >= fee (685); advance
  > $250.00 "will require" (708); notice > $25.00 (711); interest 31st day (723); aggregation 45-day (727-731).
  No "$25 or less, no fee" rule. GRS 4.2 (735).

## D04 - Copyright Office fees, proposed rule (37 CFR 201, 202, 203)

- FR March 20, 2026; comments by May 4, 2026 (29-30); dated March 18, 2026 (838). Last adjustment
  March 2020 (85 FR 9374, Feb. 19, 2020, effective Mar. 20, 2020) (40-43); study from August 2023 (115).
- FRD cost study: "$15.6 million in annual direct costs and $81.8 million in annual indirect costs" with
  itemized parts (144; itemized indirect plus overhead sums to $71,848,110, not 81.8); median CPI +23%
  2020-2025, 3% a year projected 2026-2030 (150); +33% since FY2016; average fee rise 43% (221);
  60% recovery 2009-2018, 41% in FY2024 (193); revenue $51M vs $41M, 53% recovery (236).
- Tables (current / proposed / calculated cost): basic registrations (293-303), group (339-368), other
  registration and special services (412-425), recordation (478-512), records retrieval/search (553-571),
  misc (587-595), Licensing (627-637). Proposed regulatory text tables (683-800).
- FOIA: hourly search/review rate under 37 CFR 203.11(a)(1) (648-655), no amount printed; payment by
  201.6(a) methods replacing check/money order (652, 835). Footnote 112 cites OMB Fee Guidelines, 52 FR
  10012, 10017 (Mar. 27, 1987) (644-645).

## D05 - ONCD, FOIA and Privacy Act, proposed rule (32 CFR 2200-2201)

- FR March 31, 2026; "Comments must be received by May 15, 2026" (28); dated March 27, 2026 (443). First
  FOIA/PA regulations (26).
- FOIA part 2200: direct cost 16 percent (146); working day (157); 30 calendar days clarification (172);
  20 working days (204); expedited 10 calendar days (211, 219); appeal 90 calendar days (261); appeal decision
  20 working days (268).
- Fees 2200.9: "Charges for time less than a full hour will be in increments of quarter hours" (279);
  no search fee for educational/scientific/news; first two hours free for other non-commercial (281-282);
  "photocopied at a rate of ten cents ($0.10) per page ... shall not be charged for the first 100 pages of
  copies unless the copies are requested for a commercial use" (284); "Fees likely to exceed $25" =
  notice only, 30-day closure (286); advance > $250 (287). No "$25 or less, no fee" rule and no
  cost-of-collection rule in part 2200.
- Privacy Act part 2201: "$.10 per page for all copying of 4 pages or more. There is no charge for
  duplication 3 or fewer pages." (435); notice > $25.00 (436); 10 business days (408); 180 days (418);
  30 business days (420).

## D06 - DHS/ICE, Form I-246 fee adjustment, proposed rule (8 CFR 103.7(d)(6))

- FR May 7, 2026; comments by July 6, 2026 (39). Fee $155 -> $755 (36); unchanged since 1989 (144),
  INS/EOIR Fee Schedule 54 FR 13513 (April 4, 1989) (147); 2025 fee analysis on a Spring 2020 labor survey,
  ~$755 per stay request (150, 188).
- Table 1: $155, $755, difference $600, "387" percent (203-207). Payments: 10,494 FY2017 high, 1,537 FY2022
  low, 3,745 FY2025; transfers $2.25 million (210-217). CPI alternative $395 "rounded up from $392"; CPI-U
  1989 123.967, 2024 313.689, factor "1.530", increment $237.15; text says purchasing power "in 1988"
  (232-239). Adjudicators GS-11/GS-12, ~30 percent supervisors, GS-11 assumed (242). UMRA $206 million in
  2024 dollars from CPI-U 1995 152.383 (289-294). OMB A-25 58 FR 38142 (July 15, 1993) (108).

## D07 - Access Board, FOIA regulations, proposed rule (36 CFR 1120)

- FR Aug 4, 2026; "Submit comments by September 3, 2026" (28); approved by vote July 29, 2026 (125).
- History: 1980 (45 FR 80976, Dec. 8, 1980), 1987 (52 FR 43195, Nov. 10, 1987), 1990 (55 FR 2521, Jan. 25,
  1990) (44). DOJ guidance June 26, 2019 via justice.gov/oip URL (49). OMB guidelines 52 FR 10012 (March 27,
  1987), 85 FR 81955 (Dec. 17, 2020) (98).
- Old fees "search fee at $14.00 per hour, review fee at $20.00 per hour, and duplication fee at $0.20 per
  page" (99); new search/review at GS-9/step 5, GS-14/step 5, EX-Level IV plus 16 percent, "round down search
  and review time to the nearest hour" (104-106); keeps $0.20 per page (107); "typically does not charge
  fees" (117).
- Fees 1120.10: direct costs 16 percent (270); search fees "rounded down to the nearest full hour" (292-295);
  "$0.20 per page" photocopies (298); review at search rates (303); first 100 pages and two hours free except
  commercial (310-312); "$25.00 or less for any request, no fee will be charged" after deducting free pages and
  hours (313); cost-of-collection rule (314); notice > $25.00 (315-317); interest 31st day (321); aggregation
  30-day (322); advance > $250.00 (329); 30 calendar days (330-331). Appeal 90 calendar days (249); CCI
  designations expire 10 years (220).

## Shared ground (navigation only)

- Entities in several documents: DOJ Office of Information Policy (D01 235 full name; D02 363 "(OIP)";
  D03 77, 480-481; D07 49 URL only). OGIS (D01-D03, D05, D07). OMB Fee Guidelines (D01 30, D02 141, D03 324,
  D04 644, D05 122, D07 98, 147). OMB Circular A-25 (D04 fn 49 "(2017)"; D06 108 "July 15, 1993").
- Parallel FOIA fee parameters (D01, D02, D03, D05, D07): 16 percent benefits; 100 free pages and two free
  search hours; $25 notice; $250 advance; 31st-day interest; 90-day appeals. Differences: per-page rate
  (D01 $0.25, D03 $0.20 FOIA / $0.30 PDR, D05 $0.10, D07 $0.20, D02 none); search-time increments (D01/D02
  quarter hour, charged only if more than half used; D03 rounded up to the full hour; D05 quarter-hour
  increments; D07 rounded down to the full hour); "$25 or less, no fee" only in D02 (482-483) and D07 (313);
  aggregation presumption D02/D07 30 days, D03 45 days; salary benchmarks D03 GG-9/7, GG-14/7, ES-Max vs
  D07 GS-9/5, GS-14/5, EX-IV. No document prints a dollar hourly FOIA rate except D07's old $14/$20.
- Fee-setting rules with cost analysis: D04 (cost-of-service tables) and D06 (I-246 full cost, CPI-U).
- No document cites, amends or responds to another bundle document. No forecast/actual pairs.
