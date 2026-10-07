# aq-docket-trial-03 - document map

Written once by `bundle-mapper` from `text/` (and `docs/` for flattened tables and scans).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map. Line numbers below (L...) are lines in
`text/Dnn.txt`; in every spot-check the original `docs/` line was text line minus 2 (id header plus
blank line).

## Bundle

- What it is: seven Federal Register documents: three DOT Semiannual Regulatory Agendas (July 2023,
  February 2024, August 2024), a DOT NPRM (October 2025) and the DOT final rule on the same RIN
  (July 2026) on procedures for unfair or deceptive practices rulemakings, a CFPB circular on credit
  card rewards (December 2024 FR printing), and a CCC/USDA final rule establishing the Regional
  Agricultural Promotion Program (November 2023).
- Documents: 7; ids D01-D07 from `text/manifest.json`; local ids equal platform Doc 1-7.
- Section order in this file (caller's mapping order, not id order): D01, D03, D04, agenda
  cross-edition RIN ledger, D06, D07 (with "D06 vs D07"), D05, D02, Shared ground.
- Gaps: none in readable text. All lines of text/D01-D07 read (ledgers per document). No scans,
  charts, images or pipe tables; no "[... not shown ...]" markers. Not inspected (outside this
  mapping's inputs): the capture file AQ-DOCKET-TRIAL-03_2026-10-05_1519.md and any platform bundle
  overview it holds -- overview exposure of any fact listed here is unresolved.
- Extraction spot-checks: plain-text sources, no pages (`pages: null`; FR page markers inline).
  Each document's header, one timetable/table row where present, one footnote where present and
  anomalous strings were grep-checked against docs/ originals (details per document); all matched.
  Text line N corresponded to original line N-2 in every check (D01 L103/orig L101; D03 L837/orig
  L835; D04 L323/orig L321; D05 L239/orig L237; D06 L95/orig L93; D07 L69/orig L67; D02
  L35/orig L33).
- Provenance: notes/intake.json schema 1, capture_sha256 db3d1421...a0d3; all 7 documents
  `incomplete: false`, `gap_characters: 0`, `matches_capture: true`; source sha256 in manifest
  equal captured sha256 for every document.

## D01 - DOT Semiannual Regulatory Agenda, FR July 27, 2023

- Source: docs/fr_2023_14549.txt | text/D01.txt 935 lines | no pages (FR pages printed inline as
  `[[Page 48581]]`..`[[Page 48590]]`).
- Written or submitted by: Office of the Secretary, Department of Transportation; signed "John
  Edward Putnam, General Counsel, Department of Transportation." (L93-95; no signing date printed).
  General contact Daniel Cohen, Assistant General Counsel for Regulation, (202) 366-4702 (L67).
- Type, date, edition: FR Vol. 88, No. 143, Thursday July 27, 2023, [Proposed Rules], pages
  48582-48590, "Part XIII" (L3-21); "Semiannual Regulatory Agenda" / "Reg Flex Agenda" (L27-31);
  docket [DOT-OST-1999-5129] (L53); heading "Department Regulatory and Deregulatory Agenda;
  Semiannual Summary" (L55); FR Doc. 2023-14549 Filed 7-26-23 (L933). The text never calls itself
  "Spring"; season label not printed in D01.
- Period covered: "planned regulatory activity for the next 12 months" (L65). Dates in timetables
  are MM/DD/YY; projected dates use day "00" (e.g. "11/00/23").
- Reg Flex / Section 610 preamble (L85-87): "each DOT operating administration divides its rules
  into 10 different groups and plans to analyze one group each year. In each Fall Regulatory
  Agenda, each operating administration will publish the results of the analyses it has completed
  during the previous year. The most recent results appeared in the Department's 2022 Fall
  Regulatory Agenda Preamble, which was published in the Federal Register on February 22, 2023."
  Also cites EO 12866, EO 13563 "76 FR 3821 (January 18, 2011)". No Section 610 appendix in D01.
- Consultation paragraph EO 13132 / 13175 (L89-91).
- Summary tables (L97-323): heading per administration+stage, columns "Sequence No. / Title /
  Regulation Identifier No."; legend "+ DOT-designated significant regulation." Sequence numbers
  135-157 (23 entries). Detailed entries L325-931.
- Marker facts: 135 printed "++ A" (summary L103 and entry L331; original identical; no legend for
  "++" or "A" anywhere in D01). "+" on 137-143, 145, 146, 152-157. No marker on 136, 144, 147-151.
  FAA Proposed (L113-129), FMCSA Proposed (L191-199) and SLSDC Completed (L217-247) tables have no
  legend line.
- RIN ledger (seq | admin | stage | title as printed | timetable as printed | RFA | contact):
  - 135 | OST | Final Rule Stage | "++ A Refunding Airline Tickets and Fees for Delayed Checked Bags
    and Ancillary Services That Are Not Provided" [2105-AF04] (L331) | NPRM 08/22/22 87 FR 51550;
    NPRM Comment Period End 03/28/23; Final Rule 11/00/23 (L341) | Yes | Blane A. Workie, Assistant
    General Counsel, 202 366-9342 (L347). Abstract L333-335: 49 U.S.C. 41712 interpretation;
    defines cancellation/significant change; "the rulemaking under RIN 2105-AE53 has been merged
    into this rulemaking"; checked-bag fees (FAA Extension, Safety and Security Act of 2016);
    ancillary fees (FAA Reauthorization Act of 2018); government-restriction protections.
  - 136 | FAA | Proposed Rule Stage | "Requirements To File Notice of Construction of
    Meteorological Evaluation Towers and Other Renewable Energy Projects (Section 610 Review)
    (Section 610 Review)" [2120-AK77] (L357; "(Section 610 Review)" printed twice also in summary
    L125-127) | NPRM 08/00/23 (L371) | No | Juan Yanguas 202 267-1082 (L375). Abstract L361-365:
    towers "50 feet above ground level (AGL) up to 200 feet AGL"; "statutory mandate under section
    2110 of the FAA Extension, Safety, and Security Act of 2016 (Pub. L. 114-190)".
  - 137 | FAA | Final Rule Stage | "+Registration and Marking Requirements for Small Unmanned
    Aircraft" [2120-AK82] (L385) | Interim Final Rule 12/16/15 80 FR 78593; Interim Final Rule
    Effective 12/21/15; OMB approval of information collection 12/21/15 80 FR 79255; Interim Final
    Rule Comment Period End 01/15/16; Final Rule 02/00/24 (L395-399) | Yes | Bonnie Lefko, Oklahoma
    City, 866 762-9434 (L403).
  - 138 | FAA | Long-Term Actions | "+Regulation of Flight Operations Conducted by Alaska Guide
    Pilots" [2120-AJ78] (L415) | Next Action Undetermined (L423) | Yes | Jeff Smith 202 365-3617
    (L427). Statutory mandate sec. 732 Wendell H. Ford AIR-21 (Pub. L. 106-181) (L421).
  - 139 | FAA | Long-Term | "+Drug and Alcohol Testing of Certain Maintenance Provider Employees
    Located Outside of the United States" [2120-AK09] (L431) | ANPRM 03/17/14 79 FR 14621; Comment
    Period Extended 05/01/14 79 FR 24631; ANPRM Comment Period End 05/16/14; Comment Period End
    07/17/14; Next Action Undetermined (L441-445) | Yes | Julia Brady 202 267-8083 (L451-453).
    Mandate sec. 308(d) FAA Modernization and Reform Act of 2012 (Pub. L. 112-95) (L435).
  - 140 | FAA | Long-Term | "+Applying the Flight, Duty, and Rest Requirements to Ferry Flights
    That Follow Commuter or On-Demand Operations (FAA Reauthorization)" [2120-AK26] (L457) | Next
    Action Undetermined (L473) | Yes | Chester Piolunek 202 267-3711 (L477).
  - 141 | FAA | Long-Term | "+Aircraft Registration and Airmen Certification Fees" [2120-AK37]
    (L483) | Next Action Undetermined / To Be Determined (L503) | Yes | Isra Raza 202 267-8994
    (L507).
  - 142 | FAA | Long-Term | "+Helicopter Air Ambulance Pilot Training and Operational Requirements
    (HAA II) (FAA Reauthorization)" [2120-AK57] (L511) | Next Action Undetermined (L519) | Yes |
    Chris Holliday 202 267-4552 (L523). Mandate sec. 306(e) FMRA 2012 (L517).
  - 143 | FAA | Completed Actions | "+Airport Safety Management System" [2120-AJ38] (L535) | NPRM
    10/07/10 75 FR 62008; NPRM Comment Period Extended 12/10/10 75 FR 76928; NPRM Comment Period End
    01/05/11; End of Extended Comment Period 03/07/11; Second Extension of Comment Period 03/07/11
    76 FR 12300; End of Second Extended Comment Period 07/05/11; Second NPRM 07/14/16 81 FR 45871;
    Second NPRM Comment Period End 09/12/16; Final Rule 02/23/23 88 FR 11642; Final Rule Effective
    04/24/23 (L545-553) | Yes | James Schroeder 202 267-4974 (L557).
  - 144 | FMCSA | Proposed Rule Stage | "Self-Insurance Program Cost Recovery (Section 610 Review)"
    [2126- AC58] (L569) | NPRM 06/00/23 (L581) | No | Kenneth Riddle, Office Director 202 366-9616
    (L585). Abstract L575: 49 CFR 360.3T/360.3; L&I Account; Treasury.
  - 145 | FMCSA | Long-Term | "+Safety Monitoring System and Compliance Initiative for Mexico-
    Domiciled Motor Carriers Operating in the United States" [2126-AA35] (L595) | NPRM 05/03/01 66 FR
    22415; NPRM Comment Period End 07/02/01; Interim Final Rule 03/19/02 67 FR 12758; IFR Comment
    Period End 04/18/02; IFR Effective 05/03/02; Notice of Intent to Prepare an EIS 08/26/03 68 FR
    51322; EIS Public Scoping Meetings 10/08/03 68 FR 58162; Next Action Undetermined (L609-611) |
    Yes | Sarah Stella 202 366-0192 (L617). Abstract dated events L603: "within 18 months";
    "On January 16, 2003, the Ninth Circuit ... remanded"; "On June 7, 2004, the Supreme Court
    reversed"; "FMCSA originally planned to publish a final rule by November 28, 2003."
  - 146 | FRA | Final Rule Stage | "+Train Crew Staffing" [2130-AC88] (L629) | NPRM 07/28/22 87 FR
    45564; NPRM Comment Period End 12/21/22; Final Rule 02/00/24 (L637) | Yes | Amanda Maizel,
    Attorney-Adviser 202 493-8014 (L641). Authority 49 CFR 1.89(a); 49 U.S.C. 20103 (L631).
  - 147 | SLSDC | Completed | "Seaway Regulations and Rules: Periodic Update, Various Categories
    (Completion of a Section 610 Review)" [2135-AA51] (L655) | Final Action 03/07/22 87 FR 12590;
    Final Rule Effective 03/21/22 (L671) | No | Michal Chwedczuk 202 366-0091 (L675).
  - 148 | SLSDC | Completed | "Tariff of Tolls (Completion of a Section 610 Review)" [2135-AA52]
    (L681) | Final Action 03/02/22 87 FR 11585; Final Rule Effective 03/02/22 (L691) | No |
    Chwedczuk.
  - 149 | SLSDC | Completed | "Seaway Regulations and Rules: Periodic Update, Various Categories
    (Completion of a Section 610 Review)" [2135-AA53] (L701) | Final Rule 03/08/23 88 FR 14266; Final
    Rule Effective 03/22/23 (L713) | No | Chwedczuk.
  - 150 | SLSDC | Completed | "Tariff of Tolls (Completion of a Section 610 Review)" [2135-AA54]
    (L725) | Final Action 03/13/23 88 FR 15274; Final Action; Correction 03/20/23 88 FR 16556; Final
    Rule Effective 03/22/23 (L735) | No | Chwedczuk.
  - 151 | PHMSA | Proposed | "Pipeline Safety: Gas Pipeline Leak Detection and Repair" [2137- AF51]
    (L755) | NPRM 05/18/23 88 FR 31890; NPRM Comment Period End 07/17/23 (L765) | Yes | Sayler
    Palabrica 202 366-0559 (L771). "mandate from section 113 of the ... PIPES Act of 2020" (L759).
  - 152 | PHMSA | Proposed | "+Pipeline Safety: Pipeline Operational Status" [2137-AF52] (L777) |
    NPRM 11/00/23 (L787) | Yes | Sayler Palabrica (L793-797).
  - 153 | PHMSA | Proposed | "+Pipeline Safety: Safety of Gas Distribution Pipelines and Other
    Pipeline Safety Initiatives" [2137-AF53] (L801) | NPRM 07/00/23 (L811) | Yes | Ashlin
    Bollacker, Technical Writer 202 366-4203 (L817). "title II of the ... (PIPES Act of 2020)".
  - 154 | PHMSA | Completed | "+Hazardous Materials: Enhanced Safety Provisions for Lithium
    Batteries Transported by Aircraft (FAA Reauthorization Act of 2018)" [2137-AF20] (L827) | Interim
    Final Rule 03/06/19 84 FR 8006; IFR Effective 03/06/19; IFR Comment Period End 05/06/19; Final
    Rule 12/21/22 87 FR 77995; Final Rule Effective 01/20/23 (L839-845) | Yes | Eugenio Cardez
    202 366-8553 (L851). Abstract L833: enumerated (1)-(3); "not more than a 30 percent state of
    charge"; exception "not more than two replacement lithium cells or batteries" for medical
    devices; ICAO Technical Instructions 2015-2016 edition.
  - 155 | MARAD | Proposed | "+Cargo Preference--U.S. Flag Vessels Regulatory Update (Section 610
    Review)" [2133-AB97] (L863) | NPRM 08/00/23 (L873) | Undetermined | Thomas Mitchell Hudson
    202 366-9373 (L879). sec. 3502 FY23 NDAA; 46 U.S.C. 55305(d) (L867).
  - 156 | MARAD | Proposed | "+Amendment to the Federal Ship Financing Program Regulations;
    Financial Requirements (Section 610 Review)" [2133-AB98] (L883) | NPRM 04/25/23 88 FR 24962;
    NPRM Comment Period End 06/26/23; Final Rule 09/00/23 (L891-893) | No | "Mitch Hudson,
    Attorney" 202 366-9373 (L899; same phone as Thomas Mitchell Hudson). NDAA FY2020 Pub. L. 116-92.
  - 157 | MARAD | Final Rule Stage | "+Establishing Safe and Secure Merchant Marine Training
    (Section 610 Review)" [2133-AB99] (L911) | Final Action 07/00/23 (L923) | Undetermined | Thomas
    Mitchell Hudson (L929). FY23 NDAA; 46 U.S.C. chapter 513.
- Entities and aliases: SLSDC heading "Saint Lawrence Seaway Development Corporation (SLSDC)"
  (L651) vs abstract "Great Lakes St. Lawrence Seaway Development Corporation (GLS)" and "St.
  Lawrence Seaway Management Corporation (SLSMC) of Canada" (L659-663, L685). PIPES Act of 2020 =
  "Protecting our Infrastructure of Pipelines and Enhancing Safety Act of 2020" (L759, L805).
  Billing codes: 4910-13-P (L561), 4910-EX-P (L621), 4910-06-P (L647), 4910-61-P (L747),
  4910-60-P (L855), 4910-81-P (L935).
- Tables: timetables only (Action / Date / FR Cite), flattened onto one or a few lines; no numeric
  tables or units.
- Lists: 23 entries; last entry 157 MARAD (L911). Section 610 titles: "(Section 610 Review)" on
  136, 144, 155, 156, 157; "(Completion of a Section 610 Review)" on 147-150.
- Forecasts/projected dates (vs FR date 07/27/23): 144 NPRM 06/00/23; 153 NPRM 07/00/23; 157 Final
  Action 07/00/23; 136 NPRM 08/00/23; 155 NPRM 08/00/23; 156 Final Rule 09/00/23; 135 Final Rule
  11/00/23; 152 NPRM 11/00/23; 137 and 146 Final Rule 02/00/24.
- Hedged claims: 142 "may continue to see the unacceptable high rate of aircraft accidents" (L517,
  conditional on "Without these changes"); 144 "FMCSA may also need to amend 49 CFR 360.5T/360.5"
  (L575); 156 "MARAD expects ... will reduce the economic burden" and "could encourage the
  construction of vessels" (L885). Preamble disclaimer: publication "does not impose any binding
  obligation" (L77).
- Rounded prose beside exact figures: not applicable (no numeric tables).
- Operative definitions, rules and scope exceptions: none operative (agenda); 154 abstract states
  rule content and medical-device exception (L833).
- Amendments or contradictions: 135 merges RIN 2105-AE53 (L335). 136 title duplicates "(Section 610
  Review)". 156 sits under Proposed Rule Stage while its timetable already lists the NPRM and a
  projected Final Rule. 144 projects an NPRM for 06/00/23, a month before this edition's FR date.
- Extraction spot-check: header/FR page range (L3-11), summary row 135 with "++ A" (orig L101),
  timetable row "NPRM 08/22/22 87 FR 51550" (orig L339), legend lines and Fall-agenda sentence
  (orig L85) match the original; footnote: not applicable (no footnotes); page count: not
  applicable (text source; FR pages 48581-48590 inline).
- Coverage: FULL. Ledger: L1-320, L320-639, L640-935 read (all lines).

## D03 - DOT Semiannual Regulatory Agenda with Appendix A (Section 610 plans), FR February 9, 2024

- Source: docs/fr_2024_00449.txt | text/D03.txt 2,110 lines | FR pages `[[Page 9607]]`..
  `[[Page 9624]]` inline.
- Written or submitted by: Office of the Secretary, DOT; signed "Subash Iyer, Acting General
  Counsel, Department of Transportation." (L93-95; no signing date). Contact Daniel Cohen,
  "Assistant General Counsel for Regulation and Legislation" (L67; D01 L67 said "Assistant General
  Counsel for Regulation"), (202) 366-4702.
- Type, date, edition: FR Vol. 89, No. 28, Friday February 9, 2024, [Proposed Rules], pages
  9608-9624, "Part XIII" (L3-21); docket [DOT-OST-1999-5129] (L53); same heading/summary text as
  D01 (L55-91). FR Doc. 2024-00449 Filed 2-8-24 (L2107). Season label ("Fall 2023") not printed
  for the agenda itself.
- Preamble L87 is word-for-word D01 L87, including "The most recent results appeared in the
  Department's 2022 Fall Regulatory Agenda Preamble, which was published in the Federal Register on
  February 22, 2023." (printed although D03's own Appendix A carries Section 610 results).
- Appendix A--Review Plans for Section 610 and Other Requirements (L97-1413):
  - Part I The Plan (L99-123): "The Department began a new 10-year review cycle with the Fall 2018
    Agenda." (L109). Section 610 rule criteria (1) published within last 10 years; (2) SEISNOSE
    (L113-115). Changes to plan (L117-123): "Some reviews may be conducted earlier than scheduled.
    For example, events, such as accidents, may result..."; "we will note the change in the
    following Agenda".
  - Part II Review Process (L127-143): year convention L131: "a year will coincide with the
    publication annually of the fall Agenda ... Year 1 (2018) begins in the fall of 2018 and ends in
    the fall of 2019; Year 2 (2019) begins in the fall of 2019 ... The exception ... is the FAA ...
    for FAA Year 1 (2017) begins in the fall of 2017 and ends in the fall of 2018; Year 2 (2018)
    begins in the fall of 2018". L137: "In each Fall Agenda, the agency will publish the results of
    the analyses it has completed during the previous year"; negative-finding explanations; SEISNOSE
    parts get "a formal section 610 review during the following 12 months" and a pre-rulemaking
    Agenda entry.
  - Part III (L145-147): pending reviews flagged by inserting "(Section 610 Review)" after the title.
  - Per-administration tables (columns Year / Regulations to be reviewed / Analysis year / Review
    year; rows flattened; analysis year N+2017 and review year N+2018 for every row except FAA):
    - OST (L153-189): 1 49 CFR parts 91 through 99, 14 CFR parts 200 through 212, 48 CFR parts 1201
      through 1224 | 2018 | 2019; 2 48 CFR parts 1227 through 1253 and new parts and subparts | 2019
      | 2020; 3 14 CFR parts 213 through 232 | 2020 | 2021; 4 14 CFR parts 234 through 254 | 2021 |
      2022; 5 14 CFR parts 255 through 298 and 49 CFR part 40 | 2022 | 2023; 6 14 CFR parts 300
      through 373 | 2023 | 2024; 7 14 CFR parts 374 through 398 | 2024 | 2025; 8 14 CFR part 399 and
      49 CFR parts 1 through 15 | 2025 | 2026; 9 49 CFR parts 17 through 28 | 2026 | 2027; 10 49 CFR
      parts 29 through 39 and parts 41 through 89 | 2027 | 2028.
    - FAA (L541-565; intro L533-537 "two-step, two-year process", "10% block", "section 610 (b)"):
      1 14 CFR parts 141-147 and 170-187 | 2020 | 2021; 2 189-198 and 1-16 | 2021 | 2022; 3 17-33 |
      2022 | 2023; 4 34-39 and 400-405 | 2023 | 2024; 5 43-49 and 406-415 | 2024 | 2025; 6 60-77 |
      2025 | 2026; 7 91-107 | 2026 | 2027; 8 417-460 | 2027 | 2028; 9 119-129 and 150-156 | 2028 |
      2029; 10 133-139 and 157-169 | 2029 | 2030.
    - FHWA (L677-695): 1 None | 2018 | 2019; 2 23 CFR parts 1 to 260; 3 420 to 470; 4 part 500; 5
      620 to 637 | 2022 | 2023; 6 645 to 669 | 2023 | 2024; 7 710 to 924; 8 940 to 973; 9 1200 to
      1252; 10 New parts and subparts | 2027 | 2028.
    - FMCSA (L815-819): 1 49 CFR part 386; 2 385; 3 382 and 383; 4 380 | 2021 | 2022; 5 387 | 2022
      | 2023; 6 398 | 2023 | 2024; 7 392; 8 375; 9 367; 10 395 | 2027 | 2028.
    - NHTSA (L875-923): 1 49 CFR 571.223 through 571.500, and parts 575 and 579; 2 23 CFR part
      1300; 3 49 CFR parts 501 through 526 and 571.213; 4 571.131, 571.217, 571.220, 571.221,
      571.222; 5 571.101 through 571.110, and 571.135, 571.136, 571.138 and 571.139 | 2022 | 2023; 6
      571.141, and 49 CFR parts 529 through 578, except parts 571 and 575 | 2023 | 2024; 7 571.111
      through 571.129 and parts 580 through 588; 8 571.201 through 571.212; 9 571.214 through
      571.219, except 571.217; 10 parts 591 through 595 and new parts and subparts | 2027 | 2028.
    - FRA (L1093-1133): 1 49 CFR parts 200, 207, 209, and 210; 2 211-215; 3 216-220; 4 221-225; 5
      227, 228, 229, 230, and 231 | 2022 | 2023; 6 232, 233, 234, 235, and 236 | 2023 | 2024; 7
      printed "237, 238, 249, 240, and 241" (L1117; original L1115 identical) | 2024 | 2025; 8 242,
      243, 244, 250, and 256; 9 261, 262, 264, 266, and 268; 10 269, 270, and 272 | 2027 | 2028.
    - FTA (L1197-1219; RFA intro L1189-1195): 1 49 CFR parts 604, 605, and 624; 2 609 and 640; 3
      633; 4 611; 5 655 | 2022 | 2023; 6 602 and 614 | 2023 | 2024; 7 661 and 663; 8 625, 630, and
      665; 9 613, 622, 670 and 674; 10 650, 672 and 673 | 2027 | 2028.
    - MARAD (L1243-1267): 1 46 CFR parts 201 through 205, 315 through 340, 345 through 347, 381 and
      382; 2 221-232; 3 249-296; 4 298 | 2021 | 2022; 5 307-309 | 2022 | 2023; 6 310 | 2023 | 2024;
      7 315 through 340; 8 345 through 381; 9 382 through 389; 10 390 through 393 | 2027 | 2028.
    - PHMSA (L1311-1341): 1 49 CFR part 178; 2 178 through 180; 3 172 and 175; 4 part 171, sections
      171.15 and 171.16; 5 106, 107, 171, 190, and 195 | 2022 | 2023; 6 174, 177, and 199 | 2023 |
      2024; 7 176, 191 and 192; 8 172 and 178; 9 172, 173, 174, 176, 177, and 193; 10 173 and 194 |
      2027 | 2028.
    - Great Lakes Saint Lawrence Seaway Development Corporation (L1391-1403): 1 "* 33 CFR parts 401
      through 403" | 2018 | 2019; footnote "* The review for these regulations is recurring each year
      of the 10-year review cycle (currently 2018 through 2027)." (L1403).
  - Year-list headings with parts and findings (all findings "no SEISNOSE" unless noted):
    - OST "Year 10 (Fall 2018) List of Rules Analyzed and Summary of Results" (L191-349): 49 CFR
      parts 30, 31, 37 (no finding stated; DOT "will need to conduct a section 610 review"; RINs
      2105-AF08 and 2105-AF07), 38 (same; RIN 2105-AF09; USAB guidelines December 14, 2016), 39
      ("found SEISNOSE", L225-227; plans to explore rulemaking; service-animal definition; DOJ July
      23, 2010; 14 CFR 382.3 amended December 10, 2020), 71 (technical corrections; "OST has
      initiated a rulemaking"), 79, 92 (49 CFR 92.5(g) eight-item list L267-283), 98 (49 CFR 98.2
      changes incl. "Saint Lawrence Seaway Development Corporation ... should be changed to the Great
      Lakes Saint Lawrence Seaway Development Corporation", L293), 99; 48 CFR parts 1201-1224 (RIN
      2105-AE26 final rule "published on October 7, 2022", L311; 18 part lines L313-349, incl.
      "1208-1210--[Reserved]").
    - OST "Year 1 (Fall 2018) List of Rules That Are Under Ongoing Analysis" (L351-377): 49 CFR part
      93; 14 CFR parts 200, 201, 203, 204, 205, 206, 207, 208, 211, 212 (no findings).
    - OST "Year 2 (Fall 2019) List of Rules Analyzed" (L379-417): 48 CFR parts 1227-1253, no
      SEISNOSE, RIN 2105-AE26 Oct 7, 2022; 15 part lines.
    - OST "Year 3 (Fall 2020) List of Rules Analyzed" (L419-485): 14 CFR 213, 214, 215, 216, 218,
      221 (non-substantive technical correction, L469), 222, 223.
    - OST "Year 6 (Fall 2024) List of Rules That Will Be Analyzed During the Next Year" (L487-527):
      14 CFR parts 300, 302 (findings printed: "Section 610 (Subpart D)" no SEISNOSE; "Rule was
      updated in 2019"), 303, 305 (findings printed; "Rule was updated in 2019"), 313, 323, 325, 330,
      372.
    - FAA "Defining SEISNOSE for FAA Regulations" (L567-583): RFA does not define "significant
      economic impact" or "substantial number"; "a substantial number must be at least one but does
      not need to be an overwhelming percentage such as more than half"; three steps referencing
      parts 34-39 and 400-405 "since 2013".
    - FAA "Year 1 (Fall 2023) List of Rules Analyzed and Summary of Results" (L585-649): 14 CFR parts
      34, 35, 36, 39, 400, 401, 404, 405 (each "no amendments ... promulgated since January 2013 has
      or will have a SEISNOSE"; 37, 38, 402, 403 not listed).
    - FAA "Year 2 (2024) List of Rules To Be Analyzed the Next Year" (L651-671): 14 CFR parts 43
      through 49 and 406 through 415; listed 43, 45, 47, 48 ("Registration and Marking Requirements
      for Small Unmanned Aircraft"), 49, 406, 413, 414, 415.
    - FHWA preamble (L699-701): "FHWA believes" title 23 regulations lack SEISNOSE; "preliminary
      conclusion". "Year 5 (Fall 2022) List of Rules Analyzed" (L703-783): 23 CFR parts 620, 625 (RIN
      2125-AF88, 87 FR 32 (January 3, 2022)), 626 (proposing, RIN 2125-AF96), 627, 630 (RINs
      2125-AG03 and 2125-AG05), 633 (RIN 2125-AG11), 635 (RIN 2125-AF83, 87 FR 67553 (November 9,
      2022)), 636, 637. "Year 6 (Fall 2023) List of Rules That Will Be Analyzed During the Next Year"
      (L785-809): 645, 646, 650, 655, 656, 657, 658, 660, 661, 667, 668, 669 (12 parts).
    - FMCSA "Year 4 (2021) List of Rules With Ongoing Analysis" (L821-851): 49 CFR part 380, no
      SEISNOSE; footnote \1\ (L837) quotes Section 31307 LCV definition ("more than one trailer or
      semitrailer ... gross vehicle weight of more than 80,000 pounds"); ELDT compliance date
      "February 7, 2022" (L841); "Training Provider Registry (TRP)" then "TPR" (L845). "Year 5 (2022)
      List of Rules With Ongoing Analysis" (L853-865): part 387 "found no SEIOSNOSE" (sic, L859);
      "affects a substantial number of small entities, but ... does not impose a significant economic
      impact" (L863). "Year 6 (2023) ... Next Year" (L867-869): part 398.
    - NHTSA "Years 1 Through 6 (Fall 2019-2024) List of Rules With Ongoing or Pending Analysis"
      (L925-1087): 80 lines = 33 FMVSS sections 571.101-571.500 (L927-991; "49 CFR 571.141" printed
      without "part", L955) + 45 parts 501-579 (L993-1083) + 23 CFR parts 1200 and 1300 (L1085-1087).
      Counts by grep.
    - FRA "Year 5 (Fall 2022) List of Rules Analyzed" (L1135-1167): 49 CFR parts 227, 228, 229
      ("There is a SEISNOSE.", L1153), 230, 231 (no SEISNOSE; "Although part 231 may have some impact
      on small railroads", L1167). "Year 6 (Fall 2023) List of Rules(s) That Will Be Analyzed During
      This Year" (L1169-1183): 232, 233, 234, 235, 236.
    - FTA "Year 5 (Fall 2022)" (L1221-1231): part 655, no SEISNOSE; amended "in 2023 (88 FR 27596)"
      for oral fluid testing. "Year 6 (Fall 2023) List of Rules To Be Analyzed This Year"
      (L1233-1237): 602, 614.
    - MARAD "Year 4 (2022) List of Rules Analyzed" (L1269-1279): 46 CFR 298, no SEISNOSE; "MARAD has
      initiated a rulemaking to amend the rule" (Title XI). "Year 5 (2023)" (L1281-1299): 307 (label
      printed "Section 307:", L1285), 308, 309. "Year 6 (2024) List of Rules With Ongoing Analysis"
      (L1301-1303): part 310 Merchant Marine Training.
    - PHMSA "Year 5 (Fall 2023) List of Rules Analyzed" (L1343-1381): parts 106, 107, 171 (joint
      finding; examples RIN 2137-AF41 "Hazardous Materials: Advancing Safety of Modal Specific
      Provisions" and 2137-AF57 "Hazardous Materials: Harmonization With International Standards";
      modal partners FMCSA, FRA, USCG), 190, 195. "Year 6 (Fall 2024) List of Rules That Will Be
      Analyzed During the Next Year" (L1383-1389): 174, 177, 199.
    - GLS "Year 1 (Fall 2018) List of Rules That Will Be Analyzed During the Next Year" (L1407-1413):
      33 CFR parts 401, 402, 403.
  - Heading/table inconsistencies (neutral; both locations): FAA preamble Year 1 = 2017 (L131) vs
    FAA table Year 1 analysis year 2020 (L543); FAA "Year 1 (Fall 2023)" list (L585) holds parts that
    the table assigns to Year 4 (L551); FAA "Year 2 (2024)" list (L651) holds table Year 5 parts
    (L553); OST "Year 10 (Fall 2018)" list (L191) mixes table Year 10 parts (30-39, 71, 79) with table
    Year 1 parts (92, 98, 99; 48 CFR 1201-1224) (L155-187); OST "Year 6 (Fall 2024)" (L487) vs table
    Year 6 analysis 2023 / review 2024 (L177); PHMSA "Year 5 (Fall 2023)"/"Year 6 (Fall 2024)"
    (L1343, L1383) vs table analysis years 2022/2023 (L1319-1325); MARAD headings Year 4 (2022), Year
    5 (2023), Year 6 (2024) equal the table's review years; NHTSA "Years 1 Through 6 (Fall
    2019-2024)" vs table Year 1 analysis 2018. FHWA, FRA, FTA and FMCSA headings match table
    analysis years. RIN 2105-AF08 titled "Service Animals and Other Amendments" (L211) and "Service
    Animals and Technical Corrections" (L233). "Ongoing analysis"/"will be analyzed" headings that
    nonetheless print findings: OST Year 6 parts 302/305; FMCSA Years 4-5.
- Agenda summary tables (L1415-1593): seq 396-415 (20 entries); no "+" markers and no legend
  lines anywhere in D03's tables (contrast D01).
- RIN ledger (seq | admin | stage | title | timetable | RFA | contact):
  - 396 | OST | Final Rule Stage | "Refunding Airline Tickets Ancillary Service Fees" [2105-AF04]
    (summary L1419; entry L1601) | NPRM 08/22/22 87 FR 51550; NPRM Comment Period End 03/28/23;
    Final Rule 02/00/24 (L1611) | Yes | Blane A. Workie (L1615). Abstract L1603-1605 repeats D01 and
    adds: "This rulemaking is informed by feedback received at four public meetings: three meetings
    of the Aviation Consumer Protection Advisory Committee on August 22, 2022, December 8, 2022, and
    January 12, 2023, and one public hearing on March 21, 2023. The docket for this rule was also
    open to public comment submission for approximately 130 days."
  - 397 | FAA | Proposed Rule Stage | "Drug and Alcohol Testing of Certain Maintenance Provider
    Employees Located Outside of the United States" [2120-AK09] (L1625) | ANPRM 03/17/14 79 FR 14621;
    Comment Period Extended 05/01/14 79 FR 24631; ANPRM Comment Period End 05/16/14; Comment Period
    End 07/17/14; NPRM 12/00/23 (L1639) | Yes | Julia Brady (L1643). Abstract omits D01's sentence
    "This action is necessary to increase the level of safety of the flying public."
  - 398 | FAA | Proposed | "Requirements To File Notice of Construction of Meteorological Evaluation
    Towers and Other Renewable Energy Projects (Section 610 Review)" [2120-AK77] (L1649; printed once)
    | NPRM 01/00/24 (L1663) | No | Juan Yanguas.
  - 399 | FAA | Final Rule Stage | "Registration and Marking Requirements for Small Unmanned
    Aircraft" [2120-AK82] (L1677) | IFR 12/16/15 80 FR 78593; IFR Effective 12/21/15; OMB Approval of
    Information Collection 12/21/15 80 FR 79255; IFR Comment Period End 01/15/16; Final Rule 02/00/24
    (L1687-1691) | Yes | Bonnie Lefko.
  - 400 | FAA | Long-Term | 2120-AJ78 Alaska Guide Pilots (L1707) | Next Action Undetermined (L1715)
    | Yes | Jeff Smith.
  - 401 | FAA | Long-Term | 2120-AK26 ferry flights (L1723) | Next Action Undetermined (L1741) |
    Yes | Chester Piolunek.
  - 402 | FAA | Long-Term | 2120-AK37 fees (L1751) | Next Action Undetermined / To Be Determined
    (L1765) | Yes | Isra Raza. Citation list printed under label "Legal Deadline:" (L1753; original
    identical; D01 L485 "Legal Authority:").
  - 403 | FAA | Long-Term | 2120-AK57 HAA II (L1773) | Next Action Undetermined (L1781) | Yes |
    Chris Holliday; same "may continue to see" sentence (L1779).
  - 404 | FMCSA | Proposed | 2126-AC58 Self-Insurance (L1799) | NPRM 10/00/24 (L1811) | No |
    Kenneth Riddle.
  - 405 | FMCSA | Long-Term | 2126-AA35 Mexico-domiciled (L1825) | same timetable as D01
    (L1845-1847) | Yes | "Crystal E. Williams" 202 366-0596 (L1853; D01: Sarah Stella).
  - 406 | FRA | Proposed | "Positive Train Control Systems (Section 610 Review)" [2130-AC95] (L1867;
    D03 only) | NPRM 01/00/24 (L1881) | Undetermined | Amanda Maizel. Abstract L1869-1875: amend 49
    CFR part 236, subpart I; objectives (1)-(2); flexibility "that expired on December 31, 2022"; new
    exception for non-revenue passenger trains.
  - 407 | FRA | Final Rule Stage | "Train Crew Staffing" [2130-AC88] (L1897) | NPRM 07/28/22 87 FR
    45564; NPRM Comment Period End 12/21/22; Final Rule 03/00/24 (L1905) | Yes | Amanda Maizel.
    Abstract adds (L1899): "FRA extended the comment period from 60 to 146 days and held a public
    hearing on December 14, 2022."
  - 408 | SLSDC | Prerule Stage | "Seaway Regulations and Rules: Periodic Update, Various Categories
    (Completion of a Section 610 Review)" [2135-AA55] (L1923) | ANPRM 02/00/24 (L1939) | No | Carrie
    Lynn Lavigne, Chief Counsel, 315 764-3231 (L1943; address printed "Great Lakes Street, Lawrence
    Seaway Development Corporation (GLS), 1200 New Jersey Avenue SW").
  - 409 | SLSDC | Prerule | "Tariff of Tolls (Completion of a Section 610 Review)" [2135-AA56] (L1949)
    | ANPRM 02/00/24 (L1959) | No | Lavigne. Legal Authority printed "33 U.S.C. 918 et seq." (L1951;
    other SLSDC entries "981").
  - 410 | PHMSA | Proposed | 2137-AF51 Gas Pipeline Leak Detection and Repair (L1977) | NPRM 05/18/23
    88 FR 31890; NPRM Comment Period End 08/16/23; Analyzing Comments 11/00/23 (L1987) | Yes | Sayler
    Palabrica. Abstract adds (L1981): public meeting "on May 5 and May 6, 2021"; "has scheduled a Gas
    Pipeline Advisory Committee meeting to discuss the NPRM for November 27 through December 1, 2023."
  - 411 | PHMSA | Proposed | 2137-AF52 Pipeline Operational Status (L1997) | NPRM 02/00/24 (L2007) |
    Yes | Anna Setzer, Transportation Specialist 202 366-4098 (L2011; D01: Palabrica).
  - 412 | PHMSA | Proposed | 2137-AF53 Gas Distribution (L2017) | NPRM 09/07/23 88 FR 61746; NPRM
    Comment Period End 11/06/23 (L2027) | Yes | Ashlin Bollacker, "Transportation Specialist" (L2031;
    D01 "Technical Writer").
  - 413 | MARAD | Proposed | 2133-AB97 Cargo Preference (L2045) | NPRM 06/00/24 (L2059) |
    Undetermined | Thomas Mitchell Hudson.
  - 414 | MARAD | Final Rule Stage | 2133-AB98 Ship Financing (L2073) | NPRM 04/25/23 88 FR 24962;
    NPRM Comment Period End 06/26/23; Final Rule 12/00/23 (L2081) | No | Mitch Hudson, Attorney.
  - 415 | MARAD | Final Rule Stage | 2133-AB99 Merchant Marine Training (L2089) | Final Action
    01/00/24 (L2099) | Undetermined | Thomas Mitchell Hudson.
- Projected dates vs FR date 02/09/24 (no-day "00" dates): 397 NPRM 12/00/23, 410 Analyzing Comments
  11/00/23, 414 Final Rule 12/00/23, 398 and 406 NPRM 01/00/24, 415 Final Action 01/00/24 (all
  before publication month); 396, 399 Final Rule 02/00/24; 408, 409 ANPRM 02/00/24; 411 NPRM
  02/00/24; 407 Final Rule 03/00/24; 413 NPRM 06/00/24; 404 NPRM 10/00/24.
- Entities and aliases: SLSDC heading (L1525, L1919) vs appendix "Great Lakes Saint Lawrence Seaway
  Development Corporation" (L1391) vs abstract "GLS" (L1927); 92.5(g) list names "St. Lawrence
  Seaway Development Corporation" (L281). SEISNOSE = "significant economic impact on a substantial
  number of small entities" (L115). USAB = U.S. Access Board (L215-219). Billing codes 4910-13-P
  (L1791), 4910-EX-P (L1859), 4910-06-P (L1915), 4910-61-P (L1969), 4910-60-P (L2037), 4910-81-P
  (L2109).
- Hedged claims: FHWA "believes ... preliminary conclusion" (L701); PHMSA 2137-AF41/AF57 impacts
  "not expected to be significant", "expected to result in" (L1361-1365); FRA part 231 "may have
  some impact" with finding stated firmly (L1167); Part I "Some reviews may be conducted earlier"
  (L119); OST part 39 "plans to explore whether" (L227-229); 410 "has scheduled" meeting (L1981).
- Rounded prose: 396 "approximately 130 days" (L1605) beside timetable dates NPRM 08/22/22 and
  comment end 03/28/23 (L1611); 407 "from 60 to 146 days" (L1899) beside NPRM 07/28/22 and comment
  end 12/21/22 (L1905).
- Extraction spot-check: header/page range L3-11; table row FRA Year 7 (orig L1115); footnote \1\
  (orig L835); "Legal Deadline" (orig L1751), "33 U.S.C. 918" (orig L1949), "Section 307:" (orig
  L1283) match the original. Page count not applicable (text source).
- Coverage: FULL. Ledger: L1-420, L420-839, L840-1259, L1260-1679, L1680-2110 read (all lines).

## D04 - DOT Semiannual Regulatory Agenda, FR August 16, 2024

- Source: docs/fr_2024_16457.txt | text/D04.txt 798 lines | FR pages `[[Page 66847]]`..
  `[[Page 66855]]` inline.
- Written or submitted by: OST, DOT; signed "Subash Iyer, Acting General Counsel, Department of
  Transportation." (L115-117). Contact Daniel Cohen, Assistant General Counsel for Regulation and
  Legislation, (202) 366-4702 (L67-69).
- Type, date, edition: FR Vol. 89, No. 159, Friday August 16, 2024, "[Unknown Section]" (L5; D01/D03
  "[Proposed Rules]"), pages 66848-66855, "Part XII" (L21; D01/D03 "Part XIII"); docket
  [DOT-OST-1999-5129] (L53); FR Doc. 2024-16457 Filed 8-15-24 (L795). Season label not printed for
  itself.
- Edition cross-reference (RFA paragraph L109): "The most recent results appeared in DOT's
  Regulatory and Deregulatory Fall 2023 Agenda Preamble, which was published in the Federal Register
  on February 9, 2024." (= D03's FR date, D03 L3-19). No Section 610 appendix in D04.
- Public Outreach section (L83-95; present only in D04): OST "hosted virtual public hearings" in
  "rulemakings to enhance the transparency of airline ancillary service fees and to improve the
  ticket refund process" and engaged the Aviation Consumer Protection Advisory Committee, "which
  comprises representatives for airlines, airport operators, consumers, and state and local
  governments" (L87); FMCSA "is planning a series of public listening sessions in summer 2024"
  (fitness methodology), listening sessions on ADS-equipped CMVs, AEB / Tech-Celebrate Now (TCN)
  program "Initiated in September 2019 and completed in February 2022, the first phase"; outreach
  accomplishments list (training materials and ROI guides; educational videos; web-based TCN
  ADAS-specific ROI calculator; "four articles on ADAS technologies"; program website) (L89); FTA
  virtual listening session (bus testing), recorded webinar (Rail Transit Roadway Worker Protection
  NPRM), "three listening sessions" (Transit Worker Hours of Service and Fatigue Risk Management
  ANPRM), ThinkTransit Conference in Tucson, Arizona (L91); FHWA MUTCD Notice of Proposed Amendments
  "on December 14, 2020", comment period "set to close on March 15, 2021", "extended the comment
  period by an additional two months", "a series of four public webinars" (L93); tribal bridge
  program consultations; RFIs in "the following three rulemakings: Update to National Electric
  Vehicle Infrastructure Standards and Requirements, Application of Buy America to Manufactured
  Products, Incorporating Safety Into Federal-aid Programs and Projects." (L95).
- Summary tables (L119-303): seq 159-176 (18 entries); no "+" markers, no legend lines.
- RIN ledger (seq | admin | stage | title | timetable | RFA | contact):
  - 159 | OST | Completed Actions | "Refunding Airline Tickets and Ancillary Services Fees"
    [2105-AF04] (summary L123; entry L313) | NPRM 08/22/22 87 FR 51550; NPRM Comment Period End
    11/21/22; Final Rule 04/26/24 89 FR 32760; Final Rule Effective 06/25/24 (L323; original L321
    identical) | No | Blane A. Workie 202-366-9342 (L327). Abstract = D01 text (merged RIN 2105-AE53;
    no four-meetings sentence).
  - 160 | FAA | Prerule Stage | "Aircraft Registration, Airman Certification, and Airman Medical
    Certificate Fees" [2120-AK37] (L337) | ANPRM 07/00/24 (L359) | Yes | Isra Raza (L363). Authority
    ends "Pub. L. 108-297, 118 Stat. 1095" (L349-351; D01/D03 end "118 Stat.").
  - 161 | FAA | Proposed | 2120-AK77 MET towers "(Section 610 Review)" (L373) | NPRM 07/00/24 (L387) |
    No | Juan Yanguas ("800 Independence Ave NW", L391).
  - 162 | FAA | Final Rule Stage | "Drug and Alcohol Testing of Certificated Repair Station Employees
    Located Outside of the United States" [2120-AK09] (L401) | ANPRM 03/17/14 79 FR 14621; Comment
    Period Extended 05/01/14 79 FR 24631; ANPRM Comment Period End 05/16/14; Comment Period End
    07/17/14; NPRM 12/07/23 88 FR 85137; NPRM Comment Period Extended 01/24/24 89 FR 4584; NPRM
    Comment Period End 02/05/24; End of Extended Comment Period 04/05/24; Final Rule 01/00/25 (L415)
    | Yes | Julia Brady (L419-421).
  - 163 | FAA | Long-Term | 2120-AJ78 Alaska Guide Pilots (L431) | Next Action Undetermined / To Be
    Determined (L443) | "Yes" (no period, contact on same line L445) | Jeff Smith.
  - 164 | FAA | Long-Term | 2120-AK26 ("To Ferry Flights", "flight crew member") (L449) | Next Action
    Undetermined (L465) | Yes | Chester Piolunek.
  - 165 | FAA | Long-Term | 2120-AK57 HAA II (L475) | Next Action Undetermined / To Be Determined
    (L487) | Yes | Chris Holliday.
  - 166 | FAA | Long-Term Actions | 2120-AK82 Small Unmanned Aircraft (summary L197; entry L497) |
    IFR 12/16/15 80 FR 78593; IFR Effective 12/21/15; OMB Approval 12/21/15 80 FR 79255; IFR Comment
    Period End 01/15/16; Final Rule 08/00/25 (L513-517) | Yes | Bonnie Lefko.
  - 167 | FMCSA | Proposed | 2126-AC58 (L533) | NPRM 06/00/25 (L545) | No | Kenneth Riddle.
  - 168 | FMCSA | Long-Term | 2126-AA35 (L559) | same timetable as D01/D03 (L573-575) | Yes |
    "Crystal Williams" 202 366-0596 (L581).
  - 169 | FRA | Proposed | "Positive Train Control Systems (Section 610 Review)" [2130-AC95] (L595) |
    NPRM 08/00/24 (L611) | No (D03: Undetermined) | Amanda Maizel, "Attorney Adviser", 202 308-3753
    (L615; D01/D03 phone 202 493-8014).
  - 170 | FRA | Completed Actions | "Train Crew Size Safety Requirements (Completion of a Section 610
    Review)" [2130-AC88] (summary L239; entry L627) | NPRM 07/28/22 87 FR 45564; NPRM Comment Period
    End 09/26/22; Final Rule 04/09/24 89 FR 25052; Final Action Effective 06/10/24 (L635; original
    L633 identical) | Yes | Amanda Maizel 202 308-3753 (L639). Abstract = D01 text (no hearing or
    60-to-146-days sentence).
  - 171 | PHMSA | Proposed | 2137-AF52 Operational Status (L653) | NPRM 12/00/24 (L663) | Yes | Anna
    Setzer.
  - 172 | PHMSA | Proposed | 2137-AF53 Gas Distribution (L673) | NPRM 09/07/23 88 FR 61746; NPRM
    Comment Period End 11/06/23; Analyzing Comments 04/00/25 (L683) | Yes | "Robert Jagger, Technical
    Writer" 202 366-4361 (L687).
  - 173 | PHMSA | Final Rule Stage | "Hazardous Materials: FAST Act Requirements for Real-Time Train
    Consist Information" [2137-AF21] (L697; D04 only) | ANPRM 01/19/17 82 FR 6451; ANPRM Comment
    Period End 04/19/17; NPRM 06/27/23 88 FR 41541; NPRM Comment Period End 08/28/23; Final Rule
    07/00/24 (L711) | Yes | Eamonn Patrick, Transportation Specialist, phone 202 366-8553 (L715-719;
    same phone printed for Eugenio Cardez in D01 L851). Abstract L701-705: FAST Act of 2015;
    Infrastructure Investment and Jobs Act of 2021 amended Section 7302 (fusion centers replaced by
    emergency response officials).
  - 174 | PHMSA | Final Rule Stage | 2137-AF51 Leak Detection (L723) | NPRM 05/18/23 88 FR 31890; NPRM
    Comment Period End 07/17/23; Final Rule 01/00/25 (L733) | Yes | Sayler Palabrica (L737). No
    meeting sentences (contrast D03 L1981).
  - 175 | MARAD | Proposed | 2133-AB97 Cargo Preference (L751) | NPRM 06/00/25 (L761) | No (D01/D03:
    Undetermined) | "Mitch Hudson, Senior Attorney" (L765). Authority "FY23 NDAA, Pub. L. 117-263, 46
    U.S.C. 55305." (L753).
  - 176 | MARAD | Final Rule Stage | "Establishing Safe and Secure Merchant Marine Training, Every
    Mariner Builds a Respectful Culture (EMBARC) (Section 610 Review)" [2133-AB99] (L775; summary
    L293-301 prints "Builds A") | Interim Final Rule 10/00/24 (L787) | No | Mitch Hudson, Senior
    Attorney (L791). New authority list (46 U.S.C. 50101, 51103, 51322, 57100; 49 CFR 1.93) and new
    abstract: USMMA and State Maritime Academy cadets; prohibited behavior list "assault, rape, sexual
    assault, relationship violence, stalking, harassment of any kind, including gender-based and
    sexual harassment, retaliation, and discrimination" (L781).
- Projected dates vs FR date 08/16/24: 160 ANPRM 07/00/24, 161 NPRM 07/00/24, 173 Final Rule
  07/00/24 (before publication month); 169 NPRM 08/00/24; 176 IFR 10/00/24; 171 NPRM 12/00/24; 162
  and 174 Final Rule 01/00/25; 172 Analyzing Comments 04/00/25; 167 and 175 NPRM 06/00/25; 166 Final
  Rule 08/00/25.
- Billing codes: 4910-13-P (L525), 4910-EX-P (L587), 4910-06-P (L645), 4910-60-P (L743), 4910-81-P
  (L797).
- Hedged claims: 165 "may continue to see" (L481); 167 "FMCSA may also need to amend" (L539);
  outreach "is planning" sessions in summer 2024 (L89). "These webinars significantly increased the
  number and quality of comment submissions" stated firmly (L93).
- Rounded prose: not applicable beyond FHWA "additional two months" (L93; no end date printed).
- Extraction spot-check: header L3-21 ("Part XII", orig L19); timetable rows 159 and 170 (orig
  L321, L633) and the Fall 2023 sentence (orig L107) match. Footnote: not applicable (none). Page
  count: not applicable (text source).
- Coverage: FULL. Ledger: L1-400, L400-798 read (all lines).

## Agenda editions D01 / D03 / D04 - cross-edition RIN ledger (navigation)

Edition facts: D01 FR 07/27/2023 (seq 135-157, signer Putnam, General Counsel); D03 FR 02/09/2024
(seq 396-415, signer Iyer, Acting GC, Appendix A); D04 FR 08/16/2024 (seq 159-176, signer Iyer,
Acting GC). D01 L87 and D03 L87 both name the "2022 Fall Regulatory Agenda Preamble ... published
... February 22, 2023" as most recent results; D04 L109 names the "Fall 2023 Agenda Preamble ...
February 9, 2024".

| RIN | D01 (seq, stage, key dates) | D03 (seq, stage, key dates) | D04 (seq, stage, key dates) |
|---|---|---|---|
| 2105-AF04 | 135 Final; "++ A Refunding Airline Tickets and Fees for Delayed Checked Bags and Ancillary Services That Are Not Provided"; NPRM 08/22/22; comment end 03/28/23; Final Rule 11/00/23; RFA Yes | 396 Final; "Refunding Airline Tickets Ancillary Service Fees"; same NPRM/comment end; Final Rule 02/00/24; four meetings + ~130 days sentence (L1605); RFA Yes | 159 Completed; "Refunding Airline Tickets and Ancillary Services Fees"; comment end printed 11/21/22; Final Rule 04/26/24 89 FR 32760; Effective 06/25/24; RFA No |
| 2120-AK77 | 136 Proposed; NPRM 08/00/23; "(Section 610 Review)" twice | 398 Proposed; NPRM 01/00/24 | 161 Proposed; NPRM 07/00/24 |
| 2120-AK82 | 137 Final; Final Rule 02/00/24 | 399 Final; Final Rule 02/00/24 | 166 Long-Term; Final Rule 08/00/25 |
| 2120-AJ78 | 138 Long-Term; undetermined | 400 Long-Term; undetermined | 163 Long-Term; undetermined |
| 2120-AK09 | 139 Long-Term; ANPRM history; next action undetermined; title "...Certain Maintenance Provider Employees..." | 397 Proposed; NPRM 12/00/23; same title | 162 Final; title "...Certificated Repair Station Employees..."; NPRM 12/07/23 88 FR 85137; ext. 01/24/24 89 FR 4584; comment end 02/05/24; extended end 04/05/24; Final Rule 01/00/25 |
| 2120-AK26 | 140 Long-Term | 401 Long-Term | 164 Long-Term |
| 2120-AK37 | 141 Long-Term; "Aircraft Registration and Airmen Certification Fees" | 402 Long-Term; "Legal Deadline:" label | 160 Prerule; "Aircraft Registration, Airman Certification, and Airman Medical Certificate Fees"; ANPRM 07/00/24 |
| 2120-AK57 | 142 Long-Term | 403 Long-Term | 165 Long-Term |
| 2120-AJ38 | 143 Completed; Final Rule 02/23/23 88 FR 11642; Effective 04/24/23 | absent | absent |
| 2126-AC58 | 144 Proposed; NPRM 06/00/23 | 404 Proposed; NPRM 10/00/24 | 167 Proposed; NPRM 06/00/25 |
| 2126-AA35 | 145 Long-Term; contact Sarah Stella | 405 Long-Term; Crystal E. Williams | 168 Long-Term; Crystal Williams |
| 2130-AC95 | absent | 406 Proposed; NPRM 01/00/24; RFA Undetermined | 169 Proposed; NPRM 08/00/24; RFA No |
| 2130-AC88 | 146 Final; "Train Crew Staffing"; NPRM 07/28/22 87 FR 45564; comment end 12/21/22; Final Rule 02/00/24 | 407 Final; same title; comment end 12/21/22; Final Rule 03/00/24; "from 60 to 146 days", hearing December 14, 2022 (L1899) | 170 Completed; "Train Crew Size Safety Requirements (Completion of a Section 610 Review)"; comment end printed 09/26/22; Final Rule 04/09/24 89 FR 25052; Final Action Effective 06/10/24 |
| 2135-AA51 / AA52 / AA53 / AA54 | 147-150 Completed (2022-2023 final actions) | absent | absent |
| 2135-AA55 / AA56 | absent | 408-409 Prerule; ANPRM 02/00/24 | absent |
| 2137-AF51 | 151 Proposed; NPRM 05/18/23 88 FR 31890; comment end 07/17/23 | 410 Proposed; comment end printed 08/16/23; Analyzing Comments 11/00/23; meetings May 5-6, 2021 and Nov 27-Dec 1, 2023 | 174 Final; comment end printed 07/17/23; Final Rule 01/00/25 |
| 2137-AF52 | 152 Proposed; NPRM 11/00/23; Palabrica | 411 Proposed; NPRM 02/00/24; Setzer | 171 Proposed; NPRM 12/00/24; Setzer |
| 2137-AF53 | 153 Proposed; NPRM 07/00/23 | 412 Proposed; NPRM 09/07/23 88 FR 61746; comment end 11/06/23 | 172 Proposed; + Analyzing Comments 04/00/25; Robert Jagger |
| 2137-AF20 | 154 Completed; Final Rule 12/21/22; Effective 01/20/23 | absent | absent |
| 2137-AF21 | absent | absent | 173 Final; NPRM 06/27/23 88 FR 41541; Final Rule 07/00/24 |
| 2133-AB97 | 155 Proposed; NPRM 08/00/23; RFA Undetermined | 413 Proposed; NPRM 06/00/24 | 175 Proposed; NPRM 06/00/25; RFA No |
| 2133-AB98 | 156 Proposed; NPRM 04/25/23; Final Rule 09/00/23 | 414 Final; Final Rule 12/00/23 | absent |
| 2133-AB99 | 157 Final; Final Action 07/00/23 | 415 Final; Final Action 01/00/24 | 176 Final; EMBARC title; Interim Final Rule 10/00/24; RFA No |

Same-label conflicts across editions (both locations; no edition states precedence): 2105-AF04
"NPRM Comment Period End" 03/28/23 (D01 L341, D03 L1611) vs 11/21/22 (D04 L323); 2130-AC88 "NPRM
Comment Period End" 12/21/22 (D01 L637, D03 L1905) vs 09/26/22 (D04 L635); 2137-AF51 "NPRM Comment
Period End" 07/17/23 (D01 L765, D04 L733) vs 08/16/23 (D03 L1987). RFA flag changes: 2105-AF04 Yes
(D01, D03) -> No (D04); 2130-AC95 Undetermined -> No; 2133-AB97 Undetermined -> No; 2133-AB99
Undetermined -> No.

## D06 - DOT NPRM "Procedures in Regulating and Enforcing Unfair or Deceptive Practices", FR October 30, 2025

- Source: docs/fr_2025_19692.txt | text/D06.txt 384 lines | FR pages 48849-48855 (`[[Page 48850]]`
  ..`[[Page 48855]]` inline).
- Written or submitted by: Office of the Secretary of Transportation (OST), DOT; "Issued in
  Washington, DC, under authority delegated in 49 CFR part 1.27(n): Gregory Zerzan, General Counsel."
  (L373-379; no signing date). Contacts: "Robert Gorman, Beth Brodsky, or Blane Workie, Office of
  Aviation Consumer Protection", 202-366-9342, fax 202-366-7152 (L57).
- Type, date, edition: FR Vol. 90, No. 208, Thursday October 30, 2025, [Proposed Rules] (L3-7); 14
  CFR Part 399; docket [DOT-OST-2025-0633]; RIN 2105-AF38 (L17-21); NPRM (L31); FR Doc. 2025-19692
  Filed 10-29-25; BILLING CODE 4910-9X-P (L381-383).
- Dates: "Comments must be received by December 1, 2025. To the extent practicable, DOT will consider
  late-filed comments." (L37). No effective date (proposal).
- SUMMARY (L35): "proposes to reinstate the hearing procedures used when conducting a discretionary
  rulemaking action under its authority to regulate unfair or deceptive practices in air
  transportation or the sale of air transportation"; "also seeks comment on the rescission of a final
  rule".
- Section map: I Rulemaking Background (L61-139: A statute L63-91; B 2020/2022 rules L93-119; C 2023
  Clarification L121-139); II Proposal To Reinstate (L141-189: 1 Hearing Procedures L165-185; 2
  Rationale L187-189); III Rescission of Other Rules (L191-199); "V. Administrative Procedure"
  (L201-211; no section IV printed, original L199 identical); VI Regulatory Analyses A-K
  (L213-293); List of Subjects (L295-297); regulatory text (L299-371).
- Statute and authority (L65-91): 49 U.S.C. 41712 (adjudicatory, "after notice and an opportunity
  for a hearing"); 49 U.S.C. 40113 rulemaking authority; 49 U.S.C. 46301 civil penalties. Two
  numbered procedures (L79-81): "1. Enforcement" and "2. Rulemaking: Trivial or speculative harms are
  insufficient to initiate a rulemaking. The Department may initiate a rulemaking only if it has
  evidence to suggest that an unfair or deceptive practice may be occurring." EO 14219 (February 19,
  2025) (L83); EO 12866 and DOT Order 2100.6B (L89).
- Dated procedural history with cites (text vs footnote):
  - 2020 UDP Rule "Defining Unfair or Deceptive Practices": text L95 "On December 20, 2020, the
    Department published"; footnote \1\ L103 "85 FR 78707 (RIN 2105- AE72) (Docket DOT-OST-2019-0182)
    (Dec. 7, 2020)" (internal date conflict; original L93/L101 identical).
  - 2022 UDP Rule "Procedures in Regulating Unfair or Deceptive Practices": text L97 "published on
    February 2, 2022"; footnote \2\ L105 "87 FR 5655 (RIN 2105-AF03) (Docket DOT-OST-2021-0142) (Feb.
    2, 2022)". Footnote \10\ L207 "87 FR at 5657" (2022 rule's notice-and-comment statement, L203).
  - Guidance "Guidance Regarding Interpretation of Unfair or Deceptive Practices": text L113 "on
    August 29, 2022 ... without going through notice and comment"; "The Department will rescind the
    Guidance at a later date."; footnote \3\ L117 "87 FR 52677 (RIN 2105-ZA18) (Docket
    DOT-OST-2019-0182) (Aug. 29, 2022)". L133 calls it "the 2023 Guidance".
  - 2023 Clarification "Clarification of Formal Enforcement Procedures for Unfair or Deceptive
    Practices": text L123 "June 16, 2023"; footnote \4\ L129 "88 FR 39352 (RIN 2105-AF18)
    (DOT-OST-2021- 0142) (June 16, 2023)". L125 ends "is grounded in statute, settled, and does need
    to be clarified in regulation." vs L193 "... settled, and does not need to be clarified."
  - RFI "Ensuring Lawful Regulation; Reducing Regulation and Controlling Regulatory Costs": text L133
    "On April 3, 2025"; footnote \5\ L137 "90 FR 14593 (Docket DOT-OST-2025- 0026) (April 3, 2025)".
    RFI respondents named (L133): "Airlines for America, the International Air Transport Association,
    United Airlines, and the Reason Foundation" recommended reinstating 2020 hearing procedures,
    rescinding the 2022 UDP Rule, and rescinding "the 2023 Guidance".
  - Footnote \6\ L157: DOT Order 2100.6B "Policies and Procedures for Rulemakings" (Mar. 10, 2025).
  - Footnote \7\ L159-161: NPRM "Administrative Rulemaking, Guidance, and Enforcement Procedures," 90
    FR 20956, 20967 (RIN 2105-AF32) (Docket DOT-OST-2025-0007) (May 16, 2025) (proposed section
    5.17(a)); "The comment period for this NPRM closed on June 16, 2025."
  - Footnotes \8\/\9\ L175-177: removed factor located at "14 CFR 399.75(b)(3)(ii) as finalized in the
    2020 UDP Rule" and "14 CFR 399.75(b)(2)(v) as finalized in the 2022 UDP Rule".
  - Footnote \11\ L229-231 (examples of DOT hearing experience): "Public Meeting on the Airline Ticket
    Refunds and Consumer Protections NPRM ... (Mar. 21, 2023)"; "Public Meeting on the Enhancing
    Transparency of Airline Ancillary Service Fees NPRM ... (Mar. 30, 2023)"; "Accessible Lavatories on
    Single-Aisle Aircraft: Part 1; Reopening of Comment Period and Public Meeting" (URL dated
    2021/11/19; "(Dec. 16, 2021)").
- Listed revisions (L143-145): "The 2022 UDP Rule made the following six revisions": (1) "public
  interest" standard for granting; (2) proof "from ``plausible'' to ``credible and convincing;''"; (3)
  rationale for granting, not only denying; (4) eliminated neutral hearing officer (adjudicator need
  not be neutral); (5) eliminated proposed findings on disputed facts; (6) closing procedures open to
  all interested parties. Stated reason (L147): "promulgated in response to Executive Orders that have
  since been rescinded".
- Scope and exception (L153): procedures apply to "discretionary aviation consumer protection
  rulemakings issued under Section 41712 that are not defined as high-impact or economically
  significant"; those are "subject to special procedures outlined in section 12 of DOT Order 2100.6B",
  "proposed to be reinstated in a separate pending rulemaking action" (fn 7). Hedge: "If adopted,
  these reinstated hearing procedures would increase transparency" (L153).
- Hearing standard in preamble (L167-171): petition to General Counsel "before the close of the
  comment period"; "plausible showing" of three elements (1) factual issues genuinely in dispute or
  that may not satisfy the Information Quality Act; (2) ordinary comment process unlikely adequate;
  (3) resolution "would likely have a material effect on the costs and benefits"; GC may deny if
  hearing "would not advance consideration"; proposes to remove the "unreasonably delay completion of
  the rulemaking" factor but "seeks comment on the removal of this factor"; new appeal to the
  Secretary (L185); neutral officer, minutes, proposed findings, statements by participants, GC's
  three options (L181-183).
- Proposed regulatory text (L299-371): authority "49 U.S.C. 41712, 40113(a)." (L307); Sec. 399.75
  (a) General (definitions in Sec. 399.79); (b) "Except as provided in paragraph (d)" (L319; the
  high-impact exception is lettered (c) at L359; original L317 identical); (b)(1) request; (b)(2)
  "plausible prima facie showing" (i)-(iii) (L327-333); (b)(3) denial; (b)(4) explanation and appeal
  "to the Secretary within 30 days of the date on which the General Counsel's explanation of the
  factual basis for the denial is issued" (L337); (b)(5) hearing notice; (b)(6)(i)-(iv) process
  ("neutral officer", L343); (b)(7)(i)-(iv) actions following hearing; (b)(8) OIRA interagency review
  (L357); (c) high impact / economically significant "within the meaning of DOT Order 2100.6B or 49
  CFR part 5" (L359). Amendment 3: Sec. 399.79 revise paragraph (f) heading "(f) Formal enforcement
  proceedings before an administrative law judge." and delete paragraph (g) (L367-369).
- Consolidation (L195-199): 14 CFR 399.75(a) and (c) consolidated into 399.75(a); two requirements
  ("First ... Second ...").
- Regulatory analyses: OMB "has not designated this rule a significant regulatory action under
  section 3(f)" (L217); "requests for hearings are expected to occur occasionally" (L221); "would not
  impose any more than de minimis regulatory costs" (L235); EO 14192 "not expected to be an Executive
  Order 14192 regulatory action" (L239); RFA small carrier "aircraft with up to 60 seats/18,000-pound
  payload capacity. See 14 CFR 399.73." (L247); no SEISNOSE determination (L249); Federalism: ADA
  preemption 49 U.S.C. 41713 (L255-257); PRA no new collections (L269); UMRA Title II n/a (L273); NEPA
  DOT Order 5610.1D "(July 1, 2025)", CE "23 CFR 771.117(c)(20)" (L277); Privacy Act 65 FR 19477-8
  April 11, 2000 (L283); authority 49 U.S.C. 40113(a) (L287-289); RIN paragraph: "The Regulatory
  Information Service Center publishes the Unified Agenda in Spring and Fall of each year." (L293).
- Hedged claims: L153 "If adopted ... would"; L189 "The Department believes"; L221 "the Department
  believes that any incremental costs and time would be small"; L223 "may reduce costs and time";
  L225 "believes that its experience with hearings would prevent ... excessive delays"; L239 "not
  expected to be"; L279 "does not anticipate any environmental impacts".
- Entities: OST; Office of Aviation Consumer Protection; General Counsel; Secretary; FTC (definitions
  modeled on FTC precedent, L109); OMB/OIRA; RFI commenters Airlines for America, IATA, United
  Airlines, Reason Foundation (L133).
- Rounded prose: not applicable.
- Extraction spot-check: header L3-21; footnote \1\ (orig L101) and text date (orig L93);
  "paragraph (d)" (orig L317); "V. Administrative Procedure" (orig L199) match. Tables: not
  applicable. Page count: not applicable.
- Coverage: FULL. Ledger: L1-130, L130-259, L259-384 read (all lines).

## D07 - DOT final rule "Procedures in Regulating and Enforcing Unfair or Deceptive Practices", FR July 1, 2026

- Source: docs/fr_2026_13295.txt | text/D07.txt 446 lines | FR pages 39872-39878 (`[[Page 39873]]`
  ..`[[Page 39878]]` inline).
- Written or submitted by: OST, DOT; "Issued in Washington, DC, under authority delegated in 49 CFR
  part 1.27(n). Gregory Zerzan, General Counsel." (L435-441; no signing date). Contacts same three
  OACP names as D06, 202-366-9342, no fax (L39).
- Type, date, edition: FR Vol. 91, No. 125, Wednesday July 1, 2026, [Rules and Regulations] (L3-7);
  14 CFR Part 399; [DOT-OST-2025-0633]; RIN 2105-AF38 (L17-21); "ACTION: Final rule." (L27); FR Doc.
  2026-13295 Filed 6-30-26; BILLING CODE 4910-9X-P (L443-445).
- Dates: "DATES: Effective July 31, 2026." (L35). SUMMARY (L31-33): revises 2022 procedures "to align
  them with the more robust due process protections originally set forth in 2020, ensuring the use of
  neutral hearing officers and the issuance of formal findings of fact"; rescinds the 2023
  Clarification.
- Section map: I Background (A UDP statute and recent rulemakings L45-103; B NPRM L105-175; C NPRM
  Comments L177-233; D DOT Response L235-277); Rulemaking Analyses A-K (L279-357); List of Subjects
  (L359-361); regulatory text (L363-433).
- Definition (footnote \2\ L65): "Discretionary rulemakings are ones that are not specifically
  required by statute. 14 CFR 399.75(b). If Congress specifically directed the Department to issue a
  rule finding a practice to be unfair or deceptive, then the hearing procedures described herein
  would not apply. Id."
- Dated procedural history with cites:
  - 2020 UDP Rule: text L49 "On December 7, 2020, the Department published"; fn \1\ L57 "85 FR 78707
    (RIN 2105- AE72) (Docket DOT-OST-2019-0182) (Dec. 7, 2020)" + transportation.gov URL.
  - 2022 UDP Rule: text L69 "On February 2, 2022"; fn \3\ L73 "87 FR 5655 (RIN 2105- AF03) (Docket
    DOT-OST-2021-0142) (Feb. 2, 2022)" (FR doc 2022-01589 URL). fn \8\ L155 "87 FR 5655, 5657".
  - Guidance: text L77 "On August 29, 2022"; fn \4\ L81 "87 FR 52677 (RIN 2105-ZA18) (Docket
    DOT-OST-2019-0182) (Aug. 29, 2022)" (FR doc 2022-18170 URL). Called "the 2022 Guidance" at L169,
    L197, L277 (D06 L133 "the 2023 Guidance").
  - 2023 Clarification: text L85 "On June 16, 2023"; fn \5\ L89 "88 FR 39352 (RIN 2105-AF18)
    (DOT-OST-2021- 0142) (June 16, 2023)" (FR doc 2023-12845 URL); fn \6\ L91-93: 2020 rule "did not
    mention DOT's separate statutory authority (at 49 U.S.C. 46016 and 46107)".
  - RFI: text L97 "On April 3, 2025"; fn \7\ L101 "90 FR 14593 (Docket DOT-OST-2025-0026) (April 3,
    2025)" (FR doc 2025-05557 URL). RFI respondents (L97): "industry stakeholders including Airlines
    for America (A4A), the International Air Transport Association (IATA), and United Airlines, as
    well as a libertarian think tank (Reason Foundation)".
  - NPRM: L107 "On October 30, 2025, the Department issued an NPRM proposing changes in three areas of
    the UDP framework"; fn \9\ L157 "90 FR 48849-48852"; fn \10\ L165 "Id. at 48852"; fn \11\ L171
    "Id. at 48851. A separate proceeding is necessary because the Office of the Federal Register has
    indicated that agencies cannot amend two distinct parts of the Federal Register in the same
    rulemaking document."
  - Other cites: fn \15\ L201 OACP Notice of Proposed Guidance "91 FR 385 (January 6, 2026)" (FR doc
    2025-24282 URL) and DOT proposed revisions to 49 CFR part 5 "90 FR 20956 (May 16, 2025)" (FR doc
    2025-08724 URL; same 90 FR 20956 NPRM as D06 fn \7\, RIN 2105-AF32 there); fn \17\ L217 DOT Order
    2100.7 page "(January 29, 2025), paragraph 5"; fn \18\ L219-221 49 U.S.C. 40101(a)(7); fn \19\
    L229-231 49 U.S.C. 40102(a)(45) "ticket agent"; fn \20\ L259 "Docket DOT-OST-2022-0089 (refund
    rule)"; fn \21\ L261 "See current 14 CFR 399.75(b)(2)(v)."; fn \23\ L273 "14 CFR 399.75(b)(1),
    below."; fn \24\ L297 examples: Airline Ticket Refunds public meeting "(Mar. 21, 2023) (UDP
    rulemaking)" and Accessible Lavatories "(Dec. 16, 2021) (civil rights rulemaking)" (no Mar. 30,
    2023 ancillary-fee meeting, which D06 fn \11\ L229 lists).
- Three NPRM areas (L107-171): "1. Revision to UDP Hearing Procedures" with lettered sub-items
  (a) Standard for Granting a Hearing (L117-123: 2020 three-part test quoted; 2022 "public interest"
  factors incl. "whether the hearing would unreasonably delay completion of the rulemaking"); (b)
  Level of Proof (L125-127: 2020 "plausible prima facie case"; 2022 "clear and convincing showing");
  (c) Explaining the Rationale; Appeal Rights (L129-131: "For the first time ... may be appealed to
  the Secretary within 30 days"); (d) Qualifications of Hearing Officer (L133-135: 2022 removed
  "neutral", allowing an officer from OACP); (e) Conduct of the Hearing (L137-141); (f) Issuance of
  Proposed Findings of Fact (L143-145); (g) Closing Procedures (L147-149) -- seven lettered items;
  "2. Revocation of 2023 Clarification" (L161-165); "3. Consolidation of Similar Provisions; Planned
  Revocation of Guidance" (L169: "consolidate 14 CFR 399.75(a) and (d)"; "Per 14 CFR 399.75(d), the
  Department's rulemaking must ``articulate the basis''").
- NPRM comments (L177-233): "The Department received 15 comments on the NPRM. Eight were from
  individuals who generally supported the proposed rule ..., although one cautioned that more rigid
  hearing procedures could slow down rulemaking" (L179). Named commenters and positions:
  - Supporting (Industry and Policy Groups, L181-203): A4A (L183; endorsed transparency, neutral
    officer, addressing findings, consolidation of 399.75(a) and (d); recommended retaining delay
    consideration, limiting participation to noticed factual issues, advance brief statement; fn \14\
    per-passenger vs per-flight issue "beyond the scope"); IATA (L195; supported "plausible" standard,
    neutral officer, limiting comments to participants, appeal right, consolidation; argued denial
    standard should focus on advancing consideration rather than delay); Reason Foundation and the
    Center for Regulatory Freedom (CRF) (L197). "A4A, IATA, Reason Foundation, and CRF supported
    rescinding the 2022 UDP Rule, the 2022 Guidance, and the 2023 Clarification." (L197).
  - Opposing (Consumer Advocates, L205-233): Samuel Levine, "former director of the Bureau of Consumer
    Protection for FTC" (L207); "Seven consumer advocacy organizations \16\ filed a joint comment"
    (L209), fn \16\ L215: "National Consumers League (NCL), American Economic Liberties Project,
    Consumer Action, Consumer Federation of America, FlyersRights, Travelers United, and U.S. PIRG";
    cites DOT Order 2100.7 (L209); asks to deny hearings to petitioners "who failed meaningfully to
    participate" (L211); Citizens Rulemaking Alliance (CRA) "urged the Department to withdraw or revise"
    (L225; "may have significant adverse effects on small businesses because it may change how DOT
    enforces").
  - United Airlines appears only as an RFI respondent (L97), not among NPRM commenters.
- DOT Response (L235-277): "After reviewing the comments, the Department is finalizing the NPRM as
  proposed." (L237); disagrees on burden/DOT Order 2100.7 and with CRA (L243); "Prior to 2020, the
  Department occasionally held hearings ... ad hoc basis" (L251); eliminates 2022 public-interest
  delay factor (L255, fn \21\); petition itself constitutes participation (L267); revoke 2023
  Clarification, consolidate "399.75(a) and (d)", "intend to revoke the 2022 Guidance in a separate
  rulemaking" (L277).
- Regulatory analyses: not significant under EO 12866 section 3(f) (L283); "returning to a
  ``plausible prima facie'' case standard ... than the previous ``clear and convincing showing''
  standard" (L287); "engaged with these parties with both the benefit of a formal process and without
  a formal hearing process" (L289; D06 L223 "without the benefit of a formal process"); de minimis
  costs (L301); EO 14192 (L311); RFA small carrier 60 seats/18,000-pound, 14 CFR 399.73 (L317), "does
  not have" SEISNOSE (L319); Federalism 49 U.S.C. 41713 (L323); PRA, UMRA (L329-337); NEPA DOT Order
  5610.1D (July 1, 2025), 23 CFR 771.117(c)(20) (L341-343); Privacy Act 65 FR 19477-8 (L347);
  authority 40113(a) (L351-353); RIN paragraph "Spring and Fall of each year" (L357).
- Final regulatory text (L363-433): authority "49 U.S.C. 41712, 40113(a)." (L371); "2. Revise Sec.
  399.75" (L379); (a) General (L383); (b) "Except as provided in paragraph (c)" (L385); (b)(1)-(8)
  (L387-419) same wording as D06 except (b)(2)(i) adds "(Section 515 of Pub. L. 106-554)" (L391); (c)
  high impact / economically significant, DOT Order 2100.6B or 49 CFR part 5 (L421); "3. Amend Sec.
  399.79 by revising the heading of paragraph (f), and removing paragraph (g)"; Sec. 399.79 heading
  "Policies relating to unfair and deceptive practices." (L427-433).
- Hedged claims: L179 "one cautioned that more rigid hearing procedures could slow down rulemaking";
  L225 CRA "may have ... may change"; L237 "We believe"; L287 "should make it easier"; L289 "the
  Department believes ... small"; L293 "believes that its experience with hearings prevent"; L311 "not
  expected to be"; L343 "does not anticipate".
- Rounded prose: not applicable.
- Extraction spot-check: header L3-35; "clear and convincing" (orig L67, L125, L285), "399.75(a) and
  (d)" (orig L167, L181, L193, L275), "paragraph (c), when" (orig L383), "Section 515" (orig L389)
  match. Tables: not applicable. Page count: not applicable.
- Coverage: FULL. Ledger: L1-120, L120-229, L229-338, L338-446 read (all lines).

### D06 vs D07 on the same facts (neutral; both locations)

- 2020 UDP Rule publication date: D06 text "December 20, 2020" (L95) vs D06 fn \1\ "Dec. 7, 2020"
  (L103) vs D07 text and fn "December 7, 2020" / "Dec. 7, 2020" (L49, L57).
- 2022 rule's level of proof: D06 "from ``plausible'' to ``credible and convincing''" (L143) vs D07
  "``clear and convincing'' showing" (L69, L127, L287).
- Count/structure of 2022 changes: D06 "six revisions" (1)-(6) (L143-145) vs D07 lettered items
  (a)-(g) under "1. Revision to UDP Hearing Procedures" (L117-149) within "three areas" (L107).
- Consolidated paragraphs: D06 "14 CFR 399.75(a) and (c)" (L195) vs D07 "399.75(a) and (d)" (L169,
  L183, L195, L277).
- Exception cross-reference in Sec. 399.75(b): D06 "Except as provided in paragraph (d)" (L319) vs D07
  "Except as provided in paragraph (c)" (L385); exception itself lettered (c) in both (D06 L359, D07
  L421).
- Guidance year label: D06 "the 2023 Guidance" (L133; Guidance dated Aug. 29, 2022 at L113/L117) vs
  D07 "the 2022 Guidance" (L169, L197, L277).
- Clarification sentence: D06 L125 "does need to be clarified in regulation" vs D06 L193 and D07 L163
  (quoting NPRM "Id. at 48852") "does not need to be clarified".
- Information Quality Act citation: D06 (b)(2)(i) none (L329) vs D07 "(Section 515 of Pub. L.
  106-554)" (L391).
- Hearing-experience examples: D06 fn \11\ three (Mar. 21, 2023; Mar. 30, 2023; Dec. 16, 2021)
  (L229-231) vs D07 fn \24\ two (Mar. 21, 2023; Dec. 16, 2021) (L297).
- Removal of "unreasonably delay" factor: D06 proposes removal and "seeks comment" (L171; fn \8\
  2020 rule 399.75(b)(3)(ii), fn \9\ 2022 rule 399.75(b)(2)(v)); D07 final eliminates it (L255,
  fn \21\ "current 14 CFR 399.75(b)(2)(v)").
- Appeal to Secretary within 30 days: D06 proposed (L185, L337); D07 "For the first time" (L131),
  adopted (L237, L399).
- RFI respondent list: D06 L133 four names; D07 L97 same four with A4A/IATA abbreviations and
  "libertarian think tank" label.
- Comment deadline December 1, 2025 is printed only in D06 (L37); D07 prints only the NPRM issue date
  October 30, 2025 (L107) and the effective date July 31, 2026 (L35).

## D05 - CFPB Consumer Financial Protection Circular 2024-07 (credit card rewards), FR December 30, 2024

- Source: docs/fr_2024_30988.txt | text/D05.txt 374 lines | FR pages 106277-106281 inline.
- Written or submitted by: Consumer Financial Protection Bureau; signed "Rohit Chopra, Director,
  Consumer Financial Protection Bureau." (L367-369). Contact George Karithanom, Regulatory
  Implementation & Guidance Program Analyst, Office of Regulations, 202-435-7700 (L33).
- Type, date, edition: FR Vol. 89, No. 249, Monday December 30, 2024, [Rules and Regulations]
  (L3-7); 12 CFR Chapter X; "Consumer Financial Protection Circular 2024-07: Design, Marketing, and
  Administration of Credit Card Rewards Programs" (L19); "ACTION: Consumer financial protection
  circular." (L23); "DATES: The CFPB released this circular on its website on December 18, 2024."
  (L29); FR Doc. 2024-30988 Filed 12-27-24; BILLING CODE 4810-AM-P (L371-373). No comment deadline;
  feedback by email (L31).
- Question presented (L37-39) and Response "Yes." (L41-45): three examples (1) devaluation of earned
  or purchased rewards; (2) revocation/cancellation/prevention "based on buried or vague
  conditions"; (3) points deducted without benefit, "including due to technical failures ... on
  merchant partners' systems". Response L43 "unfair, deceptive, or abusive"; L45 "unfair, deceptive,
  and abusive"; L199 restates the three areas "(1) ... (2) ... (3)" for "unfair or deceptive"; L201
  "These examples are illustrative and non-exhaustive."
- Section map: Background (L47-143); Analysis (L145-215); Devaluation of Rewards Already Earned or
  Purchased (L217-255); Hidden Conditions (L257-325); Inability To Redeem Rewards (L327-353); About
  Consumer Financial Protection Circulars (L355-365).
- Definitions (Analysis): unfair (L147) "(1) it causes or is likely to cause substantial injury to
  consumers that is not reasonably avoidable by consumers and (2) such injury is not outweighed by
  countervailing benefits"; fn \25\ 12 U.S.C. 5531(c)(1); deceptive (L163) "likely to mislead a
  reasonable consumer and is material"; material (L163); net impression (L163-167); abusive fn \36\
  (L205; 12 U.S.C. 5531(d), (1) and (2)(a)-(c)); "covered person" / "service providers" / "rewards
  program operators" fn \35\ (L195; 12 U.S.C. 5481(6), 5481(26)(A)).
- Figures (Background, with sources): "As of 2019, more than 90 percent of general purpose credit card
  spending occurred on rewards cards, and by the end of 2022, 75 percent of general purpose credit
  cards were rewards cards" (L49, fn \2\ 2023 Report at 99); "in 2022, consumers earned more than $40
  billion in rewards ..., more than a 50 percent increase from 2019" (L49, fn \4\); "Consumer rewards
  balances at the end of 2022 were more than $33 billion, up 40 percent relative to the fourth
  quarter of 2019" (L49, fn \5\); fn \2\ L53 applications 2021-2023: total "decreased by 2 percent",
  rewards cards "5 percent" and tiered "8 percent"; fn \5\ L63 "consumers also forfeit about $500
  million in rewards each year. Id. at 102."; fn \6\ L67 holiday survey "33 percent ... gifts and 25
  percent on groceries"; fn \7\ L75 "In 2021, more than one in three general purpose credit cards
  offered were co-branded"; fn \15\ L111 "In 2023, there was a more than 70 percent increase in
  complaints involving credit card rewards over pre-pandemic levels."; fn \34\ L193 "In 2022, rewards
  card spending was 90 percent of all consumer spending on general purpose credit cards" (2023 Report
  at 99); fn \46\ L307 "CFPB research suggests consumers lose hundreds of millions of dollars in
  earned rewards each year. 2023 Report, at 102."
- Rounded/duplicated figures (neutral): forfeited rewards "about $500 million" (fn \5\ L63) vs
  "hundreds of millions of dollars" (fn \46\ L307), both citing 2023 Report at 102; rewards-card share
  of spending "more than 90 percent" "As of 2019" (L49) vs "90 percent" "In 2022" (fn \34\ L193), both
  citing 2023 Report at 99.
- Lists: Hidden-conditions "illustrative examples of potentially unfair rewards program practices"
  (L267-285): three paragraphs (catch-all "gaming"/"abuse"; revocation tied to actions outside
  consumer control such as issuer closing an account; sign-up offers denied on hidden conditions --
  "churning", shortened earning periods, channel restrictions). Devaluation enforcer checks
  (L229-245): dynamic pricing, loss/downgrade of a major merchant partner, mergers, cost-per-point /
  weighted average redemption cost. Prudential regulators (L357): FDIC, OCC, Federal Reserve Board,
  NCUA; other Federal enforcers (L357): "the Department of Justice and the Federal Trade Commission,
  the Farm Credit Administration, the Department of Transportation, and the Department of
  Agriculture"; "18 other ``enumerated consumer laws''"; "$10 billion or less in assets".
- DOT, airline and air-travel mentions (all mentions; CFPB is the issuer): fn \7\ L75 lifestyle
  rewards "access to airport lounges and priority boarding"; L71 co-brand partner "such as an
  airline or hospitality chain"; L89 "(e.g., changes in flight pricing)"; fn \11\ L97 Southwest Rapid
  Rewards, Delta elite status (CNN Aug. 28, 2023), Alaska Airlines lounge (Nov. 9, 2023), United
  status thresholds (Nov. 11, 2022); fn \12\ L99 United Airlines MileagePlus (June 15, 2020), Delta
  SkyMiles (Sept. 14, 2020), American Airlines AAdvantage (Mar. 2021) investor presentations; fn \40\
  L239-241 "U.S. DOT, USDOT Requires Alaska and Hawaiian Airlines to Preserve Rewards Value, Critical
  Flight Service as Merger Moves Forward (Sept. 2024)" -- DOT "imposed ``rewards protections against
  devaluation,'' including requiring each earned loyalty program be converted to new program miles at
  1:1 ratio and prohibiting ``any actions that would devalue HawaiianMiles miles''"; approval based on
  "[p]ublic interest criteria [that] include preventing unfair, deceptive, predatory or
  anticompetitive practices"; fn \41\ L251 The Points Guy valuations "for 6 major US airlines" (Sept.
  8, 2023); L353 transfer to "a travel partner"; L357 DOT listed among other Federal enforcers. D05
  never cites 49 U.S.C. 41712 or any DOT rule/RIN.
- Hedged claims and what the hedge attaches to: L43/L45 "may violate" (the violation conclusion);
  L89 "apparently as a means to ``preserve'' or ``maintain'' profit margins" (the operators' purpose);
  L219 "may commit"; L221 "may have engaged in actions that resemble" and "may constitute"; L229
  "may be harder to detect"; L245 "that could suggest a firm has engaged in a bait-and-switch"; L255
  "could arguably be attributed" (attribution) with "may be liable" (liability); L263 New York statute
  "may render certain terms ... deceptive"; L287 "will often constitute deceptive", "could cause a
  substantial monetary injury ... and may be unfair", "may not be reasonably avoidable"; L291 stated
  firmly: "There are no countervailing benefits that outweigh the injury"; L341 "it may result in a
  deceptive practice" and "It would likely also be unfair"; fn \46\ "CFPB research suggests".
- Dated events: website release December 18, 2024 (L29); FR filing 12-27-24, FR date 12-30-24; DOT
  Alaska/Hawaiian action "Sept. 2024" (fn \40\); CFPB Circular 2024-03 "(June 2024)" (fn \42\ L263);
  New York General Business Law Sec. 520-e "(2023)" (fn \14\ L109); Capital One 10-K Feb. 24, 2023 (fn
  \41\); internal cross-reference "See Agarwal supra note 4, at 8" (fn \7\ L75) while Agarwal is cited
  in fn \3\ (L59) and note 4 is the Issue Spotlight (L61).
- Tables: none. Deadlines in days: none.
- Extraction spot-check: header L3-29; fn \40\ (orig L237), fn \7\ cross-reference (orig L73), "24.
  FR 9755" (fn \39\, orig L223), $500 million / hundreds of millions (orig L61, L305) match. Tables:
  not applicable. Page count: not applicable.
- Coverage: FULL. Ledger: L1-100, L100-199, L200-374 read (all lines).

## D02 - CCC/USDA final rule, Regional Agricultural Promotion Program (7 CFR part 1489), FR November 17, 2023

- Source: docs/fr_2023_25015.txt | text/D02.txt 1,134 lines | FR pages 80092-80108 inline.
- Written or submitted by: Commodity Credit Corporation; AGENCY line "Foreign Agricultural Service and
  Commodity Credit Corporation, U.S. Department of Agriculture (USDA)" (L23); signed "Marcus Graham,
  Acting Executive Vice President, Commodity Credit Corporation." (L1127-1129). Contact Curt Alt,
  (202) 690-4784 (L45-47). FAS administers RAPP on behalf of CCC (L57, L253).
- Type, date, edition: FR Vol. 88, No. 221, Friday November 17, 2023, [Rules and Regulations]
  (L3-7); 7 CFR Part 1489; RIN 0551-AB06 (L17-21); "ACTION: Final rule." (L25); FR Doc. 2023-25015
  Filed 11-16-23; BILLING CODE 3410-10-P (L1131-1133).
- Dates: "This rule is effective November 17, 2023. Although not required by the Administrative
  Procedure Act (APA), CCC will accept comments received by December 18, 2023." (L35); "effective upon
  publication" (L79); APA exemption for grants/benefits, "30-day delay" not required; CCC "may
  consider the comments" (L81).
- Preamble map: Background (L51-57; "Consistent with a bipartisan request from the Senate Committee
  on Agriculture, Nutrition, and Forestry"); Eligible Organizations (L59-61); General Provisions
  (L63-75); Effective Date and Comments (L77-81); EO 12866/13563 "non-significant", not reviewed by OMB
  (L83-91); RFA/SBREFA "not subject to the Regulatory Flexibility Act", not a major rule, major-rule
  delay "60 days" (L93-95); NEPA (L97-99); EO 12372 (2 CFR part 415, subpart C) (L101-103); EO 12988
  (L105-109); EO 13132 (L111-113); EO 13175 (L115-119); UMRA "$100 million or more in any 1 year"
  (L121-127); Assistance Listing "Regional Agricultural Promotion Program"--10.618 (L131); PRA control
  number 0551-0049 (L137; again Sec. 1489.35 L1125).
- Regulatory text (L145-1125): table of sections 1489.10-1489.35 (26 sections, L149-203); authority
  15 U.S.C. 714c(f) (L205). Section locations: 1489.10 L207; .11 Definitions L255; .12 L357; .13 L377;
  .14 L405; .15 L445; .16 L479; .17 L563; .18 L883; .19 L907; .20 L923; .21 L953; .22 L971; .23 L1003;
  .24 L1031; .25 L1037; .26 L1041; .27 L1047; .28 L1065; .29 L1091; .30 L1095; .31 L1107; .32 L1111;
  .33 L1115; .34 L1119; .35 L1123.
- Operative definitions (Sec. 1489.11, L255-355; 37 defined terms, Activity ... U.S. for-profit
  entity): e.g., "Brand participant ... This definition does not include any U.S. agricultural
  cooperatives." (L281); "Eligible commodity means any U.S. agricultural commodity or product thereof,
  excluding tobacco, that is comprised of at least 50 percent by weight, exclusive of added water"
  (L303); "Generic promotion" requires "at least two U.S. companies participate" when company names are
  used, unified theme rule (L313); "RAPP notice ... These notices have no legal effect." (L329-331);
  "SRTG ... nonprofit association of State-funded agricultural promotion agencies" (L339); "U.S.
  agricultural commodity" includes insects and fish harvested by a vessel "(as defined in title 46 of
  the United States Code)" (L351); "Administrative expenses" six categories (1)-(6) (L261-275).
- Eligibility lists: preamble (L61) "nonprofit U.S. agricultural trade organizations, nonprofit state
  regional trade groups, state agencies, U.S. agricultural cooperatives, and other entities"; Sec.
  1489.12(a) (L359-367) exactly four types: (1) nonprofit U.S agricultural trade organization; (2)
  nonprofit SRTG; (3) U.S. agricultural cooperative; (4) State agency. For-profit size limit "does not
  exceed 300 percent of the small business size standards ... 13 CFR part 121" (L61; again L453-455).
  Priority wording: preamble "the CCC will give priority" (L61) vs Sec. 1489.14(a)(2) "CCC may give
  priority" (L411).
- Thresholds and percentages: generic contribution "at least 10 percent" (L69, L481); brand
  contribution "at least 50 percent" (L69-71, L483); brand reimbursement "no more than 50 percent"
  (Sec. 1489.17(e), L863); funding-change notification "more than $25,000 or 25 percent of the approved
  funding level, whichever is greater" (L435-439) and below-threshold notice "no later than 30 days
  after the change" (L441); U.S. shows "no less than 30 percent of exhibitors" and "no less than 15
  percent of its visitors" from outside the U.S. (L587; L651 "countries other than the United States";
  L707 "countries other than the host country"); STRE "up to 25 percent" over Embassy guidelines
  without approval, above "125 percent" needs FAS Agricultural Counselor authorization (L693-699);
  admin support cap "shall not exceed eight percent of the RAPP Participant's total RAPP budget",
  "except for agricultural cooperatives" (L703); NASDA, SRTGs, Intertribal Agriculture Council admin
  support (L701); temporary contractor cap "daily gross salary of a GS-15, Step 10" (L645);
  compensation cap "125 percent of ... GS-15 Step 10" (L757); advances "shall not exceed 40 percent"
  of approved generic budget, none for brand (L913).
- Day/period deadlines (location): records three calendar years after budget period (L477); trade
  mission "minimum of five different companies", "no more than two representatives", "minimum of 6
  hours per day (except for the first and last days of the mission)" (L621-625); air travel business
  class when flight time "exceeds 14 hours" (employees etc., L661) or "exceeds five hours" (targets of
  market development, L667); rest period "of up to 24 hours" alternative for (C) and (D) (L671-673);
  "14-hour rule" per origin/destination (L675); target traveler "only eligible for a rest period when
  that traveler flies in economy class and meets the 14-hour test" (L679); relocations "at least 12
  months" (L783); dependents "six months or more" (L785); expenditures within "6 months following the
  expiration date" (L869); claims not later than 6 months after expiration (L891); overpayment repay
  "within 30 calendar days" (L893); disallowance "within 30 days" (L897); improper spending "30
  calendar days" (L899-901); advances expended "within 90 calendar days" (L919); records "three years
  after completion" (L929); contribution report 6 months (L955); trip reports "Not later than 45 days
  after completion of travel" (L957); research and evaluation reports 6 months (L959-961); annual
  results "no later than 6 months following the end of each Participant's budget period" (L979);
  compliance report repay "Within 60 calendar days of the date the compliance report cover letter is
  signed" (L1007); written notice repay "within 30 calendar days" (L1013); appeal "within 60 calendar
  days" (L1019); reconsideration "Within 30 calendar days" and hearing request (L1025-1027);
  contribution shortfall "within six months after the expiration date" (L1035); contract competition
  "every three years" (L1083); fraud report "within five business days" (L1099); brand claim repay
  "within 30 days" (L1103).
- Enumerated item sets: Sec. 1489.10(b)(1) seven regulations (i)-(vii) (L211-225) and (b)(4) eight
  items (i)-(viii) (L231-247); demonstration-project conditions (1)-(4) (L385-393); brand participation
  agreement requirements (1)-(9) (L457-477), origin terms list of 13 quoted phrases ("American" ...
  "Made in America") plus state/territory names (L467), 1/6 inch (.42 centimeters) letter "o"
  standard, non-qualifying examples "Cincinnati style chili, Gina's American Pizza" (L471); eligible
  contributions (d)(2) (i)-(xviii) (L503-537; (xv) "The cost of air and local travel in the United
  States"); ineligible contributions (d)(3) (i)-(x) (L541-559); reimbursable brand-or-generic costs
  (b)(1)-(19) (L573-641); generic-only reimbursable costs (c)(1)-(34) (L645-787); non-reimbursable
  costs (d)(1)-(33) (L791-861); program evaluation contents (1)-(7) (L983-995); contracting guideline
  contents (1)-(6) (L1075-1085).
- Internal cross-references (neutral): Sec. 1489.16(d)(3)(vii) excepts product development "as
  described in Sec. 1489.17(c)(22)" (L553) while Sec. 1489.17(d)(4) excepts it "as specified in
  paragraph (c)(21)" (L799); (c)(21) is the non-tariff-barrier item incl. "pest and disease research"
  (L749), (c)(22) is overseas office organization costs (L751).
- DOT / airline / air-travel content (D02 never names DOT): airline-ticket modification fees in
  international travel items (L591, L615, L647); full fare economy basis and "average of the full fare
  economy class rate for flights offered by three different airlines" for charter or no-economy flights
  (L653); business-class exceptions (L655-679); "Unused non-refundable airline tickets ... except where
  travel was restricted by U.S. Government action or advisory" not reimbursable (L823); "RAPP-funded
  air travel shall conform to the requirements of the Fly America Act (49 U.S.C. 40118)" (L873). Only
  "deceptive" use: Sec. 1489.27(e) "Deceptive or misleading promotions may result in cancellation or
  termination" (L1061).
- Exclusions/exceptions: cooperatives excluded from "brand participant" (L281) and from the eight
  percent admin-support item (L703); Sec. 1489.27(b) export-sales ban except cooperatives and
  for-profit entities (L1051); Sec. 1489.27(c) open-participation rule "does not apply to any U.S.
  agricultural cooperative when implementing its own brand program" (L1057); tobacco excluded from
  eligible commodity (L303); brand advances barred (L913); interest on advances "is not program income"
  (L917, L1109).
- Hedged claims: L53 "USDA recognizes that additional investments ... are needed" and "RAPP funding
  will ensure" (firm); L81 "may consider the comments"; L119 "does not, to the knowledge of FAS, have
  Tribal implications" (hedge attaches to FAS knowledge); L471 waiver "where the CCC has determined
  that such labeling will likely harm sales"; L913 "unacceptable risk ... will depend on a number of
  factors"; L1061 "may result in cancellation".
- Tables: none. Rounded prose: not applicable.
- Extraction spot-check: header L3-35 ("December 18, 2023", orig L33); "Sec. 1489.17(c)(22)" (orig
  L551), "three different airlines" (orig L651), "paragraph (c)(21)" (orig L797), Fly America Act
  (orig L871), signer (orig L1125) match. Footnotes: not applicable (none); page count: not
  applicable.
- Coverage: FULL. Ledger: L1-160, L160-359, L359-558, L558-757, L757-956, L956-1134 read (all lines).

## Shared ground (navigation only)

### Entities that appear in more than one document, and where

- Issuers vs mentions: DOT/OST issues D01, D03, D04, D06, D07. DOT is only mentioned in D05 (L357
  enforcer list; fn \40\ L239-241 DOT action on the Alaska/Hawaiian merger "(Sept. 2024)"). D02 never
  names DOT (cites 49 U.S.C. 40118 Fly America Act, L873). USDA issues D02 (CCC/FAS); "the Department of
  Agriculture" is mentioned in D05 L357. CFPB issues D05 only.
- Blane A. Workie / Blane Workie: agenda contact for RIN 2105-AF04 (D01 L347, D03 L1615, D04 L327; phone
  202 366-9342); contact for RIN 2105-AF38 with Robert Gorman and Beth Brodsky, Office of Aviation
  Consumer Protection (D06 L57, D07 L39; same phone). Fax 202 366-7153 (D01/D03/D04) vs 202-366-7152
  (D06).
- DOT General Counsel signers: John Edward Putnam, General Counsel (D01 L93); Subash Iyer, Acting General
  Counsel (D03 L93, D04 L115); Gregory Zerzan, General Counsel (D06 L377, D07 L439). Daniel Cohen contact
  (D01/D03/D04 L67; title differs D01 vs D03/D04).
- Aviation Consumer Protection Advisory Committee: three meeting dates in D03 L1605 (Aug 22, 2022; Dec 8,
  2022; Jan 12, 2023); composition in D04 L87. Office of Aviation Consumer Protection (OACP): D06 L57,
  D07 L39, L135 (2022 rule allowed an OACP officer to preside), fn \14\ L189, fn \15\ L201.
- Airlines: United Airlines -- D05 fn \11\ L97 (status thresholds article) and fn \12\ L99 (MileagePlus
  investor presentation); D06 L133 and D07 L97 (RFI respondent; not among D07's NPRM commenters).
  Alaska Airlines -- D05 fn \11\ L97, fn \40\ L239. Delta, Southwest, American Airlines, Hawaiian -- D05
  only. "airlines" in ACPAC composition (D04 L87).
- Industry/policy groups: Airlines for America (A4A), IATA, Reason Foundation -- D06 L133 (RFI) and D07
  L97 (RFI), L183-197 (NPRM commenters). Center for Regulatory Freedom (CRF) -- D07 L197, fn \15\ only.
- FTC: D05 (case law fn \26\-\33\, \37\-\39\, \45\; FTC Act); D06 L109 and D07 L49-53 (UDP definitions
  "modeled after Federal Trade Commission (FTC) precedent"); D07 L197 (Reason: "modeled after FTC's
  regime"), L207 (Samuel Levine, former FTC Bureau of Consumer Protection director).
- Saint Lawrence Seaway naming: D01 L651/L659 (SLSDC heading vs GLS in abstract); D03 L293 (rename
  instruction for 49 CFR 98.2), L1391 (Great Lakes ... appendix heading), L1525/L1919 (SLSDC headings),
  L1943 (contact address); absent from D04.
- Thomas Mitchell Hudson / Mitch Hudson (MARAD; phone 202 366-9373): D01 L879/L899/L929, D03
  L2063/L2085/L2103, D04 L765/L791 ("Senior Attorney").
- Recurring review/analysis statutes and orders (locations): EO 12866/13563 -- D01 L87, D03 L87, D04
  L109, D02 L83-91, D06 L215-217, D07 L281-283; EO 13132/13175 -- D01 L91, D03 L91, D04 L113, D02
  L111-119, D06 L253-263, D07 L321-327; Regulatory Flexibility Act -- D01 L85-87, D03 L85-87 and
  Appendix A, D04 L105-109, D02 L93-95, D06 L243-251, D07 L313-319; PRA -- D02 L133-137/L1125, D06
  L265-269, D07 L329-333; UMRA -- D02 L121-127, D06 L271-273, D07 L335-337; NEPA -- D02 L97-99, D06
  L275-279, D07 L339-343; EO 14192 -- D06 L237-239, D07 L309-311; Information Quality Act -- D06 L169,
  L219, L329; D07 L119, L285, L391.
- "Unfair"/"deceptive" standards: CFPA definitions printed in D05 (L147, L163, fn \36\ L205); 49 U.S.C.
  41712 UDP framework in D06/D07 (definitions referenced to 14 CFR 399.79, not printed); D01/D03/D04
  2105-AF04 abstracts describe 41712 as prohibiting "unfair practices" (D01 L333, D03 L1603, D04 L315);
  D05 fn \40\ L241 DOT merger "public interest criteria ... preventing unfair, deceptive, predatory or
  anticompetitive practices"; D02 L1061 "Deceptive or misleading promotions".

### Periods or series that more than one document covers, and where

- Agenda series (DOT-OST-1999-5129): D01 FR 07/27/2023, D03 FR 02/09/2024, D04 FR 08/16/2024 (see
  cross-edition RIN ledger above). Season labels: D04 L109 calls the February 9, 2024 publication the
  "Fall 2023 Agenda Preamble"; D01 L87 and D03 L87 call February 22, 2023 the date of the "2022 Fall
  Regulatory Agenda Preamble". D06 L293 / D07 L357: "The Regulatory Information Service Center publishes
  the Unified Agenda in Spring and Fall of each year." No document prints a season for D01 or D04.
- Section 610 cycle: D01 L87, D03 L87 and D04 L109 (10 groups, one per year, results in each Fall
  Agenda); D03 Appendix A (Fall 2018 start; Year conventions L131; per-administration tables).
- UDP rulemaking chain (D06/D07): 2020 UDP Rule (D06 L95 "December 20, 2020" vs fn \1\ "Dec. 7, 2020";
  D07 L49/L57 Dec. 7, 2020) -> 2022 UDP Rule Feb. 2, 2022 -> Guidance Aug. 29, 2022 -> Clarification
  June 16, 2023 -> RFI April 3, 2025 -> RIN 2105-AF32 NPRM May 16, 2025, comment period closed June 16,
  2025 (D06 fn \7\; D07 fn \15\ cites 90 FR 20956) -> NPRM October 30, 2025, comments by December 1,
  2025 (D06 L37) -> OACP proposed guidance January 6, 2026 (D07 fn \15\) -> final rule FR July 1, 2026,
  effective July 31, 2026 (D07 L35).
- Air-passenger refund rulemaking (RIN 2105-AF04) across D01/D03/D04 and hearing references in D06/D07
  (see "Documents that cite..." below).
- Dates of the non-DOT documents relative to agenda editions: D02 FR 11/17/2023 (between D01 and D03 FR
  dates); D05 released 12/18/2024, FR 12/30/2024 (after D04); D05 fn \40\ DOT merger action "(Sept.
  2024)" (after D04's FR date).

### Documents that cite, amend or respond to another document in the bundle

- D04 L109 names the publication date of D03 ("Fall 2023 Agenda Preamble ... February 9, 2024" = D03
  L3-19). D01 L87 and D03 L87 name a February 22, 2023 preamble (not in the bundle).
- D07 finalizes D06: same docket DOT-OST-2025-0633 and RIN 2105-AF38 (D06 L19-21, D07 L19-21); D07 L107
  "On October 30, 2025, the Department issued an NPRM"; fn \9\ "90 FR 48849-48852" (D06 printed FR pages
  48849-48855, L7); fn \10\ "Id. at 48852", fn \11\ "Id. at 48851"; L237 "finalizing the NPRM as
  proposed". Same-fact differences listed under "D06 vs D07" above.
- Refund-rule hearing cross-references: D03 L1605 (2105-AF04 abstract) "one public hearing on March 21,
  2023"; D06 fn \11\ L229 and D07 fn \24\ L297 "Public Meeting on the Airline Ticket Refunds and Consumer
  Protections NPRM ... (Mar. 21, 2023)"; D07 fn \20\ L259 "Docket DOT-OST-2022-0089 (refund rule)" (docket
  number not printed in the agendas); D04 L87 OST "hosted virtual public hearings" in the ancillary-fee
  transparency and ticket-refund rulemakings. D06 fn \11\ also lists an ancillary-fee NPRM meeting "(Mar.
  30, 2023)"; no ancillary-fee-transparency RIN appears in D01/D03/D04.
- RINs in D06/D07 (2105-AE72, 2105-AF03, 2105-ZA18, 2105-AF18, 2105-AF32, 2105-AF38) do not appear in any
  agenda edition (grep). RIN 2105-AE53 appears only as the merged RIN in the 2105-AF04 abstracts (D01
  L335, D03 L1605, D04 L317).
- CFR overlaps: 14 CFR part 399 (amended by D06 L299 / D07 L363) is in D03's OST Section 610 table Year 8
  "14 CFR part 399 and 49 CFR parts 1 through 15", analysis year 2025, review year 2026 (D03 L181-183);
  49 CFR part 5 (named in D06 L359, D07 L201/L421) falls within that Year 8 range "49 CFR parts 1 through
  15". 14 CFR 399.73 small-carrier definition (D06 L247, D07 L317). 14 CFR part 48 ("Registration and
  Marking Requirements for Small Unmanned Aircraft") listed in D03 FAA "Year 2 (2024) ... To Be Analyzed"
  (L661) shares its title with RIN 2120-AK82 (D01 L385, D03 L1677, D04 L497). 49 CFR part 236 subpart I
  (RIN 2130-AC95 abstract, D03 L1869-1871, D04 L597-599) is in D03 FRA "Year 6 (Fall 2023) ... Will Be
  Analyzed During This Year" (L1179). D03's 46 CFR part 298 finding (L1275-1279: "Title XI Program
  obligors", "MARAD has initiated a rulemaking to amend the rule") and RIN 2133-AB98's abstract (D01
  L885, D03 L2075: "Title XI Program") both use the term "Title XI Program"; neither names the other.
  46 CFR part 310 "Merchant Marine Training" (D03 L1303, "Ongoing Analysis") shares those words with
  RIN 2133-AB99's title; neither names the other.
- D05 and D02 cite no other bundle document.

### Forecast/actual pairs, changed tables, same-period conflicts, scope relationships (locations only)

- Projected-then-actual agenda dates (projection location -> actual location): 2105-AF04 Final Rule
  11/00/23 (D01 L341) and 02/00/24 (D03 L1611) -> 04/26/24 89 FR 32760, effective 06/25/24 (D04 L323);
  2130-AC88 Final Rule 02/00/24 (D01 L637) and 03/00/24 (D03 L1905) -> 04/09/24 89 FR 25052, effective
  06/10/24 (D04 L635); 2137-AF53 NPRM 07/00/23 (D01 L811) -> 09/07/23 88 FR 61746 (D03 L2027);
  2120-AK09 NPRM 12/00/23 (D03 L1639) -> 12/07/23 88 FR 85137 (D04 L415). Projections never matched by
  an actual in the bundle: 2133-AB98 Final Rule 09/00/23 (D01 L893), 12/00/23 (D03 L2081), absent in
  D04; 2135-AA55/AA56 ANPRM 02/00/24 (D03 L1939/L1959), absent in D04; 2137-AF21 Final Rule 07/00/24 (D04
  L711); others in the ledger table.
- Actual dates falling between agenda FR dates: 2137-AF53 NPRM 09/07/23 and 2120-AK09 NPRM 12/07/23
  (between D01 07/27/23 and D03 02/09/24; D03 still prints 2120-AK09 NPRM as projected "12/00/23",
  L1639); 2130-AC88 final 04/09/24 and 2105-AF04 final 04/26/24 (between D03 and D04). Events printed
  only in later editions although dated before the earlier edition: ACPAC meetings and March 21, 2023
  hearing (D03 L1605; not in D01's 2105-AF04 abstract L333-335); FRA hearing December 14, 2022 and 60-to-
  146-day extension (D03 L1899; not in D01 L631 or D04 L629); PHMSA public meeting May 5-6, 2021 (D03
  L1981; not in D01 L759 or D04 L727).
- Same-label conflicts across editions: comment-period-end dates for 2105-AF04, 2130-AC88, 2137-AF51
  (listed under the ledger table). Within-document duplicates/conflicts: D03 heading/table year
  mismatches (D03 section); D06 internal date and paragraph-letter conflicts (D06 section); D05 fn \5\
  vs fn \46\ and L49 vs fn \34\ (D05 section); D02 product-development cross-reference (D02 section).
- Rounded prose next to exact dates: D03 L1605 "approximately 130 days" with timetable dates at L1611;
  D03 L1899 "from 60 to 146 days" with NPRM 07/28/22 and comment end 12/21/22 at L1905 (D04 L635 prints
  comment end 09/26/22 for the same NPRM); D04 L93 FHWA "additional two months" (no end date printed).
- Scope/exclusion relationships: D07 fn \2\ L65 discretionary = "not specifically required by statute"
  (Congress-directed rules excluded); D06 L153 and Sec. 399.75(c) (D06 L359, D07 L421) exclude
  high-impact/economically significant rules to DOT Order 2100.6B / 49 CFR part 5 procedures; D05 L201
  examples "illustrative and non-exhaustive"; D02 cooperative and tobacco exclusions (D02 section).
- Comment universe for the D06 NPRM (D07 L177-233): total "15 comments"; "Eight were from individuals"
  (supporting, one cautioning); named: A4A, IATA, Reason Foundation, CRF (support); Samuel Levine;
  joint comment of seven organizations listed only in fn \16\ L215 (NCL, American Economic Liberties
  Project, Consumer Action, Consumer Federation of America, FlyersRights, Travelers United, U.S. PIRG);
  CRA (last named, L225). D07 does not state how the 15 are split beyond these sentences.
- Narrative passages that repeat other passages: D07 SUMMARY (L31-33) and section I.B (L105-171)
  restate D06's proposals; D07 regulatory text (L381-421) repeats D06's (L315-359) with the differences
  noted; agenda abstracts repeat verbatim across editions except where noted in the ledger; D02 preamble
  (L59-75) restates Sec. 1489.12-1489.17 thresholds (10 percent, 50 percent, 300 percent).
