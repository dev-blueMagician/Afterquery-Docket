# aq-docket-trial-04 - document map

Written once by `bundle-mapper` from `text/` (and `docs/` for flattened tables and scans).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

Locations are `Dnn:line` in `text/Dnn.txt` (the docs/ original line = text line minus 2, the
two-line "# Dnn | docs/<file>" header). No PDFs, so no page markers; D04-D08 print their own
CRS page footers (noted where useful). Ligature loss is in the source bytes: "mil ion",
"bil ion", "wil ", "ful y", "al ocation", "fiscal" etc. appear with a dropped "l"/"fi" in
D04-D08 - verbatim quotes must keep the source spelling.

## Bundle

- What it is: eight Congressional Research Service (CRS) products on U.S. foreign assistance:
  three In Focus notes (COVID-19 aid 2020; budget process 2020; abortion funding restrictions
  2024), the FAA-1961 authorizations/appropriations report (Jan 2023), three successive annual
  editions of "U.S. Foreign Assistance to Latin America and the Caribbean" (FY2023, FY2024,
  FY2025 appropriations) and a report on USAID localization (2024).
- Documents: 8; ids from `text/manifest.json`. Local ids are alphabetical by file name and
  differ from the task page's Doc numbers: D01=Doc 1, D02=Doc 2, D03=Doc 5, D04=Doc 4,
  D05=Doc 3, D06=Doc 6, D07=Doc 7, D08=Doc 8. Cite Doc N in form fields.
- Gaps: see the per-document Coverage lines and the Gaps section at the end.
- Extraction spot-checks: see each document's Spot-check line.
- Provenance: `notes/intake.json` schema 1, capture sha256 61b4c526...; all 8 documents
  `incomplete: false`, `gap_characters: 0`, `matches_capture: true`; manifest sha256 values
  equal intake `source_sha256` for all 8. Method `text`, `pages: null` for all.

## D01 - COVID-19 and Foreign Assistance: Issues for Congress

- Source: D01 = Doc 1, `docs/crs_if11496.txt` (10,640 chars; text lines 1-99). No page markers.
- Written or submitted by: Nick M. Brown (Analyst in Foreign Assistance and Foreign Policy),
  Marian L. Lawson (Specialist in Foreign Assistance), Emily M. Morgenstern (Analyst in Foreign
  Assistance and Foreign Policy) (D01:94-96). The text never names CRS or "IF11496" (file name only).
- Type, date, edition: In Focus-style brief, dated April 6, 2020 (D01:3). No edition statement.
- Period covered: FY2020 emergency/supplemental funding (Table 1 title); events March 6-27, 2020.
- Entities and aliases: USAID; State Department; Millennium Challenge Corporation (MCC); Peace
  Corps; Department of Health and Human Services (HHS); World Health Organization (WHO); U.N.;
  U.N. Food and Agriculture Organization; Famine Early Warning Systems Network (FEWSNET,
  "USAID-funded"); USAID Office of U.S. Foreign Disaster Assistance (OFDA); China; Russia.
- Dates/events: March 14 State authorized return of high-risk personnel (D01:13); March 26
  "as of" date for USAID's "$274 million in emergency funds for up to 64 of the most at-risk
  countries" (D01:31); P.L. 116-123 "signed into law on March 6" (D01:58); P.L. 116-136
  "signed into law on March 27" (D01:60); P.L. 116-127 "did not include foreign assistance
  funds" (D01:33, exclusion fact); P.L. 116-136 authorized State/USAID additional paid leave
  (D01:17-19). U.N. "$2 billion appeal" (D01:68). Peace Corps 2005: "272 volunteers" for
  Hurricane Katrina (D01:88).
- Tables: Table 1 "FY2020 Emergency/Supplemental Foreign Aid for COVID-19 Response",
  "(U.S.$ in millions)", whole millions, D01:35-56. Header "P.L. 116-123 | P.L. 116-136 | Total"
  (D01:39-41). Rows: USAID Op. Expenses 95 / total 95; USAID Insp. General 1 / 1; Global Health
  Programs 435 / 435; Economic Support Fund (ESF) 250 / 250 (D01:43-50, 3-column pipe table);
  Int'l. Disaster Assistance 300, 258, 558; Migration & Refugee Assist. 350 / 350; Peace Corps
  88 / 88 (D01:52, one flattened line); "Total, all accounts 986 791 1,777" (D01:54). Source:
  P.L. 116-123, P.L. 116-136. Note (D01:56): excludes State diplomatic/consular funds and HHS
  funding, "not considered foreign assistance under the Foreign Assistance Act of 1961".
  LAYOUT PROBLEM: single-value rows print only one figure plus the total, so the law column is
  not shown. The column totals and prose fix them: P.L. 116-123 "focused on replenishing
  emergency health and disaster assistance funds ... also included ESF funds" (D01:58);
  P.L. 116-136 "provided additional disaster assistance funds, new funding for migration and
  refugee assistance, and USAID and Peace Corps administrative funds" (D01:60-62). Mapper
  arithmetic (not printed): 435+250+300+1 = 986; 95+258+350+88 = 791. The IG row's placement
  rests on that arithmetic only; no prose names the Inspector General.
- Lists: USAID assistance focus, 4 items (equipment/training; lab and surveillance; WASH;
  livelihoods) D01:23-27. "Outlook" issues, 7 bullets D01:72-92: continuity of operations and
  program oversight; global health; global food security; fragile states and displaced
  populations; democratic backsliding; deployment of aid personnel domestically; global
  leadership (last, D01:92).
- Forecasts, guidance, deadlines, effective dates: none (only signing dates above).
- Hedged claims: PPE "is reportedly no longer being provided" (D01:23); MCC programs "are
  unlikely to address the pandemic significantly" (D01:31); outlook bullets use "may" for
  impacts (D01:72-92); "Some experts warn that the pandemic could be destabilizing" (D01:82).
- Rounded prose beside exact figures: "almost $1.8 billion in emergency foreign assistance funds
  through two supplemental appropriations bills" (D01:33) vs Table 1 total 1,777 (D01:54).
- Operative definitions, rules and scope exceptions: Table 1 note's exclusion of State
  diplomatic/consular and HHS funds (D01:56).
- Amendments or contradictions: none internal.
- Spot-check: Table 1 rows (docs lines 43, 50, 52) identical to text. No footnotes (not
  applicable). Page count not applicable (text source).
- Coverage: FULL - lines 1-99 read.

## D02 - U.S. Foreign Assistance: Budget Development and Execution

- Source: D02 = Doc 2, `docs/crs_if11515.txt` (11,293 chars; text lines 1-94). No page markers.
- Written or submitted by: Nick M. Brown, Analyst in Foreign Assistance and Foreign Policy (D02:93).
- Type, date, edition: In Focus-style brief; date "April 23, 2020" printed mid-text (D02:29).
  Title split by layout: "U.S. Foreign Assistance: Budget" (D02:3) + "Development and Execution"
  (D02:31); full title at D02:71, 93.
- Period covered: generic process; examples FY2018 Actuals / FY2020 CBJ (D02:73); FY2020 Act
  Section 7019 (D02:45); 2019 Ukraine apportionment episode (D02:91).
- Entities and aliases: Office of Management and Budget (OMB); State Bureau of Budget and Planning
  (State/BP); USAID Office of Budget and Resource Management (USAID/BRM); Office of Foreign
  Assistance Resources (State/F); Administering Bureau; Operating Units (OUs) - "Over 200
  headquarters bureaus and overseas posts"; House/Senate Appropriations Committees, Senate Foreign
  Relations Committee, House Foreign Affairs Committee (D02:11-23); Government Accountability
  Office (GAO) (D02:85, 91). FAA = Foreign Assistance Act of 1961, P.L. 87-195 (D02:5).
- Tables: none. Process stages are prose headings D02:33-77.
- Lists: Key actors, 6 entries (D02:11-23). Budget stages with timing: Mission/Bureau Resource
  Request "begins two years prior to fiscal year start" and passback "One year before" (D02:37);
  President's Budget and CBJ "early February prior to fiscal year start", 31 U.S.C. §1105; CBJ
  annexes "usually several weeks later" (FAA §634, 22 U.S.C. §2394) (D02:41); Appropriations
  Act/Conference Report/JES "required before start of fiscal year" (D02:45); 653(a) Report "30
  days after appropriations enacted" (FAA §653(a), 22 U.S.C. §2413) (D02:47-49); Apportionment
  "30 days after appropriations enacted" (31 U.S.C. §1512) (D02:57); CNs "No less than 15 days
  prior" (FAA §634A, 22 U.S.C. §2394-1) (D02:65); Reporting Spending "February following fiscal
  year end" (D02:71). "Allocated accounts", 9 items (D02:51): GHP; ESF; AEECA; INCLE; FMF; IMET;
  NADR; Development Assistance; Democracy Fund (last). "Situation-responsive accounts", 6 items
  (D02:53): PKO; Transition Initiatives; MRA; Complex Crisis Fund; ERMA; IDA (last).
  Issues for Congress, 6 headings (D02:81-91): Tracking Funds; Funding Requirements; Reporting
  Delays; Transparency; Program Planning; Apportionment Notifications.
- Forecasts, guidance, deadlines, effective dates: the stage timings above.
- Hedged claims: allotments "are not necessarily statutorily binding" (D02:61); delays "may
  impede congressional input" (D02:85); "decisions not to obligate may not" require CNs (D02:91).
- Rounded prose: "more than 700 annual SFOPS directives" on average (D02:83); 653(a) Report "five
  months late on average" (D02:85); Trump Administration requests "regularly proposed 30% less
  foreign assistance than Congress ultimately has enacted" (D02:89).
- Operative definitions, rules and scope exceptions: Titles III and IV set account
  appropriations; Title VII "General Provisions" has country directives (D02:45); "Section 7019 of
  the FY2020 Act" bars deviating below allocation-table levels "by more than 10% without
  congressional consultation" (D02:45); apportionment (D02:57); allotment/sub-allotment (D02:61);
  transfers ("a shift of funds across accounts") vs reprogramming ("redirecting funds within an
  account") (D02:63); obligate (D02:69); "Actuals" = "a final plan for allocation, but not
  necessarily final obligations or disbursements" (D02:73-75); Foreign Aid Explorer =
  "Authoritative final figures" (D02:77); CBJ public, 653(a) Report not (D02:87); Foreign Aid
  Transparency and Accountability Act of 2016, P.L. 114-191 (D02:87).
- Events: 2019 Ukraine security assistance "delayed without a CN. GAO determined this delay was
  improper, but OMB disputed that opinion" (D02:91).
- Amendments or contradictions: none internal. See Shared ground for the Titles description vs D03.
- Spot-check: D02:45, 73, 85 identical in docs (lines 43, 71, 83). No tables or footnotes
  (not applicable).
- Coverage: FULL - lines 1-94 read.

## D03 - Abortion Funding Restrictions in Foreign Assistance Legislation

- Source: D03 = Doc 5, `docs/crs_if12235.txt` (11,990 chars; text lines 1-70). No page markers.
- Written or submitted by: Luisa Blanchfield, Specialist in International Relations (D03:67).
- Type, date, edition: In Focus-style brief, "Updated April 12, 2024" (D03:3).
- Period covered: 1973-2024 legislative history; operative law cited is the FY2024 SFOPS Act =
  "Division F of P.L. 118-47" (D03:31).
- Entities and aliases: FAA (P.L. 87-195; 22 U.S.C. 2151 et seq.) (D03:11); SFOPS; UNFPA (United
  Nations Population Fund) (D03:51); USAID; GAO; Peace Corps; Department of Defense; HHS. People:
  Senator Jesse Helms, Senator Joseph Biden ("then-Senator"), Representative Mark Siljander,
  Senator Bob Kasten, Representative Jack Kemp, Senator Patrick Leahy, Representative Henry Hyde.
  Court cases: Roe v. Wade (1973); Dobbs v. Jackson Women's Health Organization (2022) (D03:7-9).
- Tables: none. Text box "The FAA and SFOPS Appropriations Acts" (D03:13-15): FAA parts I
  (development assistance), II (military and security), III (general/administrative/misc), IV
  (Enterprise for the Americas Initiative), V (debt reduction for developing countries with
  tropical forests); 22 U.S.C. 2412 requires authorization and appropriation; "Most foreign
  assistance is appropriated in Titles 3 through 6 of annual SFOPS legislation" (D03:15).
- Lists (named restrictions, "Overview of Key Restrictions", D03:27-57), 7 entries:
  Helms amendment - 1973; FAA §104(f) (22 U.S.C. 2151b(f)), part I only; in SFOPS since FY1980;
  FY2024 Act §7018 for part I activities; similar language under GHP heading "applies to all
  funding provided in the act" (D03:29-31). Peace Corps restriction - since FY1979; FY2024 Act
  includes rape/incest/life exceptions "As in some previous fiscal years" (D03:33-35). Biden
  amendment - 1981; 22 U.S.C. §2151b(f)(3); biomedical research; §7018 FY2024; part I in both laws
  (D03:39-41). Siljander amendment - 1981; FY1982 act; "lobby for or against abortion"; under GHP
  heading FY2024; "applies to all programs and activities appropriated under the act" (D03:43).
  Presidential certification - 1985 in FY1986 act; §7018 FY2024; part I (D03:45-47). Kemp-Kasten
  - FY1985 Supplemental Appropriations Act; coercive abortion/involuntary sterilization; in SFOPS
  "since FY1985"; "could apply to any entity; determinations have been made only regarding UNFPA"
  (D03:49-51). Leahy amendment (last) - 1994, FY1995 act; clarifies "motivate"; included since
  FY1995 incl. FY2024; "applies to all enacted authorization and SFOPS appropriations" (D03:55-57).
  Executive and domestic comparators (not legislative foreign-aid restrictions): Mexico City Policy
  (executive, since 1985; "typically instated by Republican Presidents and rescinded by Democratic
  Presidents") (D03:21-23); Hyde amendment (Labor-HHS acts) and DOD restriction (D03:25).
- Dates/events: August 2020 letter of 60 Members to the Trump Administration (Siljander); August
  2022 letter of 76 Members to the Biden Administration (Helms exceptions); similar letters to
  President Obama in 2011 and 2015; GAO Report 12-35 (Siljander); SFOPS acts "since FY2019"
  require written justifications for Kemp-Kasten determinations (D03:61).
- Hedged claims: "Since Helms was enacted, the executive branch has not appeared to interpret any
  exceptions" (D03:61); restrictions "may deter USAID global health partners" (advocates' view,
  D03:65); "some restrictions ... may only apply to certain entities or parts of the act" (D03:59).
- Operative definitions, rules and scope exceptions: scope by FAA part vs whole act (D03:59);
  Leahy text: "the term 'motivate,' ... shall not be construed to prohibit the provision,
  consistent with local law, of information or counseling about all pregnancy options" (D03:57).
- Amendments or contradictions: Siljander modified from "lobby for abortion" to "lobby for or
  against abortion" (D03:43). Cross-refs to other CRS products: R41360, IF12167, IN11960, RS21168,
  R46962 (not in bundle).
- Spot-check: D03:31, 51 identical in docs (lines 29, 49). No tables or footnotes (not applicable).
- Coverage: FULL - lines 1-70 read.

## D04 - Foreign Assistance Act of 1961: Authorizations and Corresponding Appropriations

- Source: D04 = Doc 4, `docs/crs_r40089.txt` (95,353 chars; text lines 1-1710). Printed page
  footers: 1 (D04:117), 2 (163), 3 (235), 4 (359), 5 (435), 6 (465), 7 (477), CRS-8 (525) ...
  CRS-28 (1687), 29 (1709).
- Written or submitted by: Dianne E. Rennack, Specialist in Foreign Policy Legislation (D04:1693);
  acknowledgment Susan G. Chesser (D04:1699). CRS report R40089.
- Type, date, edition: CRS report, "Updated January 18, 2023" (D04:5); "R40089 · VERSION 10"
  (D04:1707); "replaces an earlier issue of the same report, dated April 18, 2012" (D04:25).
- Period covered: FAA as enacted 1961 and as amended; appropriations = FY2023 SFOPS Act =
  "division K of the Consolidated Appropriations Act, 2023; P.L. 117-328; 136 Stat. 4459"
  (D04:23, 459). Footnote 5 (D04:461): page numbers cite the enrolled H.R. 2617, "presented to the
  President on December 28, 2022"; signed "December 29, 2022, as P.L. 117-328".
- Entities and aliases: FAA (P.L. 87-195; 22 U.S.C. 2151 et seq.; 75 Stat. 424); USAID; OPIC
  ("[U.S. International Development Finance Corporation]", D04:1227); TDA; Inter-American
  Foundation (D04:865); Export-Import Bank; BUILD Act of 2018 (D04:883-893); President Kennedy.
- Tables:
  Table 1 "Foreign Assistance Act of 1961, As Enacted" (D04:75-135, p.1-2): 8 rows, columns
  "Program Authorization" / "Funding Levels and Duration": development assistance $1.2 billion
  FY1962 and $1.5 billion each of next four years [§202]; development grants/technical
  cooperation <=$380 million [§212]; investment guarantees <=$90 million through June 30, 1964
  ("fiscal years, at that time, ran July through June") [§221]; surveys <=$5 million [§232];
  contributions to international organizations <=$153.5 million FY1962 [§302]; supporting
  assistance <=$465 million [§402]; contingency fund <=$300 million FY1962 [§451]; military
  assistance <=$1.7 billion FY1962-63 [§504] (last, D04:135).
  Table 2 "Selected Other Authorizations (in order of primary enactment)" (D04:171-431, p.3-5),
  columns "Popular Name: Purpose" / "Citation"; 14 laws, flattened two-column layout: Arms Export
  Control Act (P.L. 90-629; Oct 22, 1968); Trafficking Victims Protection Act of 2000 (P.L.
  106-386; Oct 28, 2000); U.S. Leadership Against HIV/AIDS, TB, and Malaria Act of 2003 (P.L.
  108-25; May 27, 2003); Millennium Challenge Act of 2003 (Title VI, Div. D, P.L. 108-199; Jan 23,
  2004); North Korean Human Rights Act of 2004 (P.L. 108-333; Oct 18, 2004); Iran Freedom Support
  Act (P.L. 109-293; Sept 30, 2006); DRC Relief, Security, and Democracy Promotion Act of 2006
  (P.L. 109-456; Dec 22, 2006); Energy Independence and Security Act of 2007 (P.L. 110-140; Dec
  19, 2007); Foreign Operations Appropriations, 2008 (P.L. 110-161; Dec 26, 2007; Development
  Grants Program, "Abolished by sec. 7080 of P.L. 113-235"); Supplemental Appropriations Act, 2009
  (P.L. 111-32; June 24, 2009; Pakistan Counterinsurgency Capability Fund $700 million); Enhanced
  Partnership With Pakistan Act of 2009 (P.L. 111-73; Oct 15, 2009; $1.5 billion each FY2010-14);
  NDAA FY2012 (P.L. 112-81; Dec 31, 2011; Global Security Contingency Fund, 80/20 DOD/State,
  authority ends Sept 30, 2021); SFOPS Appropriations Act, 2015 (P.L. 113-235 div. J; Dec 16,
  2014; Small Grants Program <=$2 million, §7080); Global Fragility Act of 2019 (last; P.L.
  116-94 title V; Dec 20, 2019; Prevention and Stabilization Fund $200 million and Complex Crisis
  Fund $30 million, each FY2020-2024) (D04:399-415). Table notes a-d (D04:417-431).
  Table 3 "Foreign Assistance Act of 1961, as Amended: Authorizations and Corresponding
  Appropriations in ... Appropriations Act, 2023" (D04:481-1685, pp. CRS-8 to CRS-28). Left column
  = FAA section, year added, latest authorized years; right column = FY2023 appropriation with
  enrolled-bill page. FLATTENED: left/right lines interleave and split sentences (e.g. D04:541-569,
  615-629, 659-669, 679-699, 717-769, 793-835, 921-931, 1009-1013, 1039-1067, 1359-1371,
  1431-1443, 1547-1587, 1605-1625). FY2023 appropriations ($ millions unless shown): GHP $4,165.95
  (USAID, to Sept 30, 2024, p.527) plus HIV/AIDS "$6,395,000,000" (State, to Sept 30, 2027, p.529)
  (D04:505-507); Development Assistance "$4,368,613,000" (p.529) (D04:511); Treasury International
  Affairs Technical Assistance $38 (D04:693-697); Democracy Fund $222.45 + $133.25 for DRL (p.530)
  (D04:727-735); AEECA $500.33 (p.530) (D04:739, 1177); International Organizations and Programs
  $508.6 (p.537) (D04:991); UNFPA $32.5 under §7057 (p.619) (D04:993); Debt Restructuring $52 (to
  Sept 30, 2026, p.533) (D04:1051); INCLE "$1,391 mil ion" (to Sept 30, 2024, p.534) (D04:1079);
  IDA $3,905.46 (p.529) (D04:1121); Transition Initiatives $80 (D04:1125); ESF "$4,301.3 mil ion"
  (p.530) (D04:1297); FMF "$6,053.05 mil ion" (p.536) (D04:1321); IMET $112.925 (p.535)
  (D04:1383); PKO $460.759 (p.535) (D04:1423); NADR $921 (p.534) (D04:1471); TDA $87 (p.542)
  (D04:1557); USAID Operating Expenses $1,743.35 (p.526) (D04:1577); Capital Investment Fund
  $259.1 (D04:1581); USAID OIG $80.5 (D04:1585); Tropical Forest and Coral Reef Conservation $20
  (D04:1641). Sector allocations: §7060(a) basic education >=$970, girls in conflict $150, higher
  education >=$285, partnerships >=$35, scholar rescue >=$7 (D04:615-629); §7060(b) "$18.5" (no
  unit) cooperative development and >=$31.5 ASHA (D04:825-833); §7060(d) >=$265 MSMEs (D04:923-931);
  §7060(e) >=$116.4 trafficking, of which >=$87 INCLE (D04:767); §7060(f) >=$25 reconciliation
  (D04:1359-1371); §7060(g) WASH >=$475, >=$237 sub-Saharan Africa, >=$17 latrines (D04:801-813);
  §7059 >=$250 gender-based violence (D04:769); §7061(i) >=$20 (D04:659-667); §7032(a)(1) "$2.9
  mil ion" for democracy programs and §7032(a)(2) $117.4 for DRL (D04:741); §7034(a) >=$10 INCLE
  "for DNA forensic technology programs to combat human trafficking in Central America and Mexico"
  (D04:745-761); §7034(f) up to $145 contingencies (D04:1009-1011). Table source "Compiled by CRS"
  (D04:1681); note a (D04:1683-1685): chapter 7 sections "are probably misnumbered" (should
  "probably" be secs. 471-476).
- Latin America-specific items in Table 3: §7045 "Latin America and the Caribbean (p. 603)" in
  the DA, ESF and FMF condition lists (D04:523, 1313, 1323); §7045(b) "relating to Colombia (p. 605)"
  in INCLE list (D04:1085); §7045(a) Central America trafficking references (D04:765); §7034(b)(2)
  forensic technology in Mexico (D04:1085); FAA §534 Administration of Justice in Latin America and
  the Caribbean, "Not more than $20,000,000" per fiscal year (D04:1353-1355); §222 originally a
  housing program for Latin America (D04:845-847); §224 Trade Credit Insurance Program for Central
  America (sunset FY1991) (D04:867-869); chapter 6 Central America Democracy, Peace, and
  Development Initiative, §465 $1.2 million FY1988-89 (D04:1015-1033); Part IV Enterprise for the
  Americas Initiative, §§701-710 (D04:1589-1629).
- Lists: General Provisions cited at Chapter 1 (D04:515-539) run §7007 ... §7067 (last). Many
  FAA sections "authorized for fiscal years 1986 and 1987" (e.g. D04:569, 577, 621, 835, 1001,
  1269, 1333, 1393, 1433, 1567).
- Forecasts, deadlines, effective dates: availability dates per account (above); BUILD Act §1464
  terminates OPIC and repeals FAA title IV "Effective at the end of the transition period"
  (D04:883-893); authority sunsets: §222 FY1992, §222A FY1988, §224 FY1991, §225 FY1992, §226 FY1998.
- Hedged claims: Act "is seen by some today as anachronistic" (D04:17); chapter 7 "probably
  misnumbered" (D04:1683); funding levels not in the act "may be detailed in the Explanatory
  Statement" (D04:471).
- Operative definitions, rules and scope exceptions: footnote 3 (D04:145-153): Section 10 of P.L.
  91-672 (22 U.S.C. 2412) requires authorization before appropriation; "routinely waived, most
  recently in Section 7022" of the FY2023 Act, "except funds appropriated under the heading 'Trade
  and Development Agency'" (D04:151). "Since 1985, the last year Congress passed a comprehensive
  reauthorization" (D04:143); from 1986 freestanding authorities (D04:137). "Beginning in FY2009"
  State and foreign operations consolidated in one bill (D04:473). §622(a),(c) Secretary of State
  supervision (D04:451-453). FAA §492: "2,794.18 mil ion" for each FY2017-2023, up to "$1,257.38
  mil ion" emergency food, additional "450 mil ion" (D04:1135). §516 EDA cap $500,000,000
  (D04:1279). §7065 up to 40 personal services contractors (D04:1587).
- Internal inconsistencies/typos (record as printed, do not resolve): GHP "$4,165.95 mil ion"
  (D04:505) vs "$4,165,95 mil ion" (D04:581); "P.L. 10-161" (D04:397) vs "P.L. 110-161" (D04:309);
  "$18.5" without unit (D04:829); "$2.9 mil ion" for §7032(a)(1) (D04:741); "Economic Support Fun"
  (D04:741); "counting Russian influence" (D04:1085); "eligible county" (D04:1651); "§7048 ... (125
  Stat. 1240)" (D04:1431-1443); "Sec. 497 ... (22 U.S.C. 2291)" (D04:1163) though chapter 10 range
  says §497 = 22 U.S.C. 2294 (D04:1141).
- Spot-check: Table 3 INCLE row (docs 1077), footnote 5 (docs 459), Table 2 "P.L. 10-161" (docs
  395), "$4,165,95" (docs 579) and Table 3 note a (docs 1681) identical to text. Page count:
  printed footers run 1-29 (version 10).
- Coverage: FULL - lines 1-1710 read in chunks (1-120, 120-270, 270-430, 430-600, 600-770,
  770-940, 940-1110, 1110-1280, 1280-1450, 1450-1650, 1650-1710).

## D05 - U.S. Foreign Assistance to Latin America and the Caribbean: FY2023 Appropriations

- Source: D05 = Doc 3, `docs/crs_r47331.txt` (72,908 chars; text lines 1-3588). Printed page
  footers: 1 (D05:121), 2 (147), 3 (171), 4 (205), 5 (229), 6 (361), 7 (477), 8 (511), 9 (537),
  10 (983), 11 (1103), 12 (1223), 13 (1323), 14 (1349), 15 (1377), 16 (1951), 17 (2377),
  18 (2867), 19 (3501), 20 (3587).
- Written or submitted by: Peter J. Meyer, Specialist in Latin American and Canadian Affairs
  (D05:9-21, 3575-3577). CRS report R47331.
- Type, date, edition: CRS report dated January 6, 2023 (D05:5); "R47331 · VERSION 2 · UPDATED"
  (D05:3585). Title split by layout over D05:3-7.
- Period covered: U.S. federal fiscal years; FY2023 began October 1, 2022 (D05:43). Column
  labels: FY2019, FY2020a, FY2021a (no status label), "FY2022 (est.)", "FY2023 (req.)", "% Change:
  FY22-FY23". Appendix: A-1 FY2021, A-2 "FY2022 Estimate", A-3 "FY2023 Request".
- Scope rule ("Report Notes", D05:127-135): figures cover only bilateral State/USAID-managed aid
  requested for countries or regional programs, "62.8% of the total aid obligated by all U.S.
  agencies ... in FY2019"; excludes COVID supplementals, humanitarian accounts (Food for Peace
  Title II, IDA, MRA), other agencies (DOD, MCC, Peace Corps) and multilateral bodies (OAS, IDB,
  PAHO). COVID text box (D05:209-211), Central America humanitarian box (D05:485-487) and
  Venezuela humanitarian box (D05:521-523) each say their funds "are not included in the country
  or regional totals found in Table 1, Table 2, or the Appendix".
- Entities and aliases: Inter-American Foundation (IAF), "established through the Foreign
  Assistance Act of 1969 (22 U.S.C. §290f)", "active in 26 countries" (D05:1095); Caribbean Basin
  Security Initiative (CBSI); Central America Regional Security Initiative (CARSI); Mérida
  Initiative; Plan Colombia; FARC; "Northern Triangle" = El Salvador, Guatemala, Honduras
  (D05:467); seven Central American nations = Belize, Costa Rica, El Salvador, Guatemala, Honduras,
  Nicaragua, Panama (D05:481); U.S.-Mexico Bicentennial Framework for Security, Public Heath [sic],
  and Safe Communities (launched October 2021, D05:517); U.S. Strategy for Addressing the Root
  Causes of Migration; Collaborative Migration Management Strategy (D05:467); Organization of
  American States (OAS); persons: President Jovenel Moïse (D05:491), Nicolás Maduro (D05:519),
  Senator Coons (D05:43, 1149).
- Narrative figures: FY2023 request "more than $2.4 billion" (D05:31, 185); "+$369.9 million
  (18.2%)" vs FY2022 estimate, exceeding "the 17.2% increase requested for SFOPS globally" (D05:185);
  IAF request $38.0 million (D05:33, 185); "four-year, $4 billion plan" for Central America
  (D05:37); Central America $986.8 million, of which $959.0 million within the regional request,
  $27.8 million in global accounts (D05:481, fn 15 D05:495), 44.4% bilateral / 55.6% regional
  programs, "+$282.8 million (41.8%)" (fn 16: excludes global accounts) (D05:481-483, 497); Haiti
  $274.8 million, +$55.6 million (25.4%) (D05:39, 491-515); Colombia $462.9 million, -$21.8 million
  (4.5%), largest cuts INCLE and NADR, request "released prior to Colombia's August 2022 change in
  government" (D05:489); Mexico $141.6 million, +$13.4 million (10.4%) "due to a proposed ESF
  increase", $17.0 million of Mexico ESF for Mexico's aid projects in Central America (D05:517);
  Venezuela $55.0 million, +$6.4 million (13.2%) (D05:519); CBSI $63.5 million, "a proposed $16.5
  million (20.6%) cut compared with the FY2022 appropriation" (D05:465). Accounts (D05:213-251):
  DA $865.9 million (36.0%), +$209.4 million (31.9%); ESF $535.5 million (22.2%), +$103.1 million
  (23.8%); GHP $303.5 million (12.6%) = $190.0 million State + $113.5 million USAID, State -$1.3
  million (0.7%), USAID +$22.0 million (24.0%); security $702.5 million (29.2%): INCLE $582.9
  million +$41.4 million (7.6%); NADR $32.1 million "same as the FY2022 estimate"; IMET $14.0
  million, "a $229,000 (1.7%) increase"; FMF $73.5 million, -$5.0 million (6.3%), "decreased aid
  to Costa Rica, Peru, and Colombia".
- Other figures: FY1946-FY2019 "$93.8 billion ($194.5 billion in constant 2019 dollars)" (D05:139);
  fn 2 "33 independent Latin American and Caribbean countries" (D05:143); poverty 45.3% to 30.4%,
  2002-2019 (D05:177); COVID box: P.L. 117-2 $10.8 billion; P.L. 116-123 and P.L. 116-136 "nearly
  $2.3 bil ion in international affairs funding"; P.L. 116-260 $4.0 billion; USAID ">= $539.0
  mil ion" to LAC as of June 2022; ">70 mil ion doses" as of December 2022 (D05:211); humanitarian
  aid to Central America and Mexico $272.2 million FY2021, $295.6 million FY2022 (D05:487);
  Venezuela crisis: 7.1 million migrants/refugees, ~6.0 million in LAC (UNHCR), FY2017-FY2022 "more
  than $2.3 bil ion", incl. $656.3 million in FY2022 (D05:523).
- Tables:
  Table 1 by account, "(millions of current U.S. dollars)", one decimal, D05:253-459 (pp.6-7).
  Rows FY2019 / FY2020 / FY2021 / FY2022 est / FY2023 req / %: DA 385.3, 457.8, 490.6, 656.5,
  865.9, +31.9%; ESF 402.3b, 377.6b, 378.5b, 432.4b, 535.5, +23.8%; GHP (USAID) 53.3, 53.3, 55.5,
  91.5, 113.5, +24.0%; GHP (State) 170.5, 157.7, 195.0, 191.3, 190.0, -0.7%; INCLE 564.3, 555.2,
  553.0, 541.5, 582.9, +7.6%; NADR 25.8, 27.3, 31.0, 32.1, 32.1, —; IMET 9.9, 13.1, 13.8, 13.7,
  14.0, +1.7%; FMF 82.8, 79.7, 76.9, 78.5, 73.5, -6.3%; Total 1,694.1, 1,721.7a, 1,794.3a, 2,037.5,
  2,407.4, +18.2% (D05:435-447). Sources: CBJs FY2021-FY2023; State FY2022 estimate data, August 16,
  2022 (D05:449). Note a: excludes COVID supplementals P.L. 116-123, 116-136, 117-2 (D05:453-455).
  Note b: extra ESF for the OAS "$9.0 mil ion ... in FY2019 and an additional $5.0 mil ion ...
  annually in FY2020, FY2021, and FY2022" not included (D05:457-459).
  Table 2 by country/regional program, "(thousands of current U.S. dollars)", D05:541-1091
  (pp.10-11); same five FY columns plus %. 25 country rows (Argentina ... Venezuela, alphabetical,
  D05:567-915), then Barbados and Eastern Caribbean; USAID Caribbean Development; USAID Central
  America Regional; USAID South America Regional; USAID Latin America and Caribbean Regional;
  State Central America Regional (b) — / — / — / 278,000b / 447,765 / +61.1% (D05:1023-1037);
  State Western Hemisphere Regional (b) 431,313 / 355,610 / 366,909 / 102,044b / 150,510 / +47.5%
  (D05:1039-1053); bracketed memo row "[Caribbean Basin Security Initiative]" [58,000] [60,000]
  [74,800] [80,000] [63,500] [-20.6%] (D05:1055-1069); Total 1,694,129 / 1,721,741a / 1,794,345a /
  2,037,548 / 2,407,408 / +18.2% (D05:1071-1079). Selected rows: Colombia 421,180; 460,183;
  465,092; 484,711; 462,875; -4.5% (D05:637-649); Haiti 193,752; 172,361; 189,577; 219,188;
  274,755; +25.4% (D05:749-761); Honduras 56,906; 73,365; 74,002; 108,306; 133,450; +23.2%;
  Mexico 162,410; 157,910; 158,910; 128,205; 141,575; +10.4% (D05:791-803); El Salvador 39,533;
  78,865; 78,790; 99,052; 124,800; +26.0%; Guatemala 80,351; 95,887; 98,049; 117,860; 162,800;
  +38.1%; Venezuela 22,500; 38,452; 38,000; 48,600; 55,000; +13.2%; Costa Rica ... 8,225; 600;
  -92.7%; Barbados and Eastern Caribbean ... 5,744; 19,720; +243.3% (D05:917-929). Sources
  (D05:1081) add CBSI FY2021/FY2022 totals from the Lowey explanatory statement (H.R. 133, Dec 21,
  2020, p. H8794) and DeLauro explanatory statement (H.R. 2471, March 9, 2022, p. H3007). Note b
  (D05:1089-1091): State Central America Regional Program created in FY2022, funding CARSI and
  activities formerly in the Western Hemisphere regional program.
  Table 3 IAF appropriations, "(millions of current U.S. dollars)" (D05:1109-1145): FY2019 22.5;
  FY2020 37.5; FY2021 38.0; FY2022 (est.) 38.0; FY2023 (req.) 38.0; —. Note: "an additional $10.0
  mil ion in FY2019" via transfers from USAID for Central America.
  Table 4 "U.S. Foreign Assistance for Selected Countries and Initiatives: FY2023 Appropriations
  Legislation", "(millions of current U.S. dollars)" (D05:1153-1305); columns FY2022 (est.) /
  FY2023 (req.) / H.R. 8282 and H.Rept. 117-401 / S. 4662 and explanatory statement / P.L.
  117-328 and explanatory statement: CBSI 80.0 / 63.5 / 82.0 / 80.0 / 82.0; Central America
  676.2a / 986.8a / NA / NA / NA; Colombia 484.7 / 462.9 / 487.4 / 471.4 / 487.4; Haiti 219.2 /
  274.8 / NA / NA / NA; IAF 38.0 / 38.0 / 47.0 / 47.0 / 47.0; Mexico 128.2 / 141.6 / NA / NA / NA;
  Venezuela 48.6 / 55.0 / 50.0 / 40.0 / 50.0. "NA indicates that comprehensive appropriation
  totals are not available" (D05:1301). Note a: FY2023 Central America includes $27.8 million of
  global accounts; FY2022 figure includes no global funding (D05:1303-1305). Sources include the
  Leahy explanatory statement on H.R. 2617, Congressional Record vol. 168, no. 198, December 20,
  2022, pp. S9285-S9302 (D05:1297-1299).
  Appendix Tables A-1 FY2021 (D05:1383-2109), A-2 FY2022 Estimate (D05:2111-2863), A-3 FY2023
  Request (D05:2871-3571), "(millions of current U.S. dollars)", one decimal; columns DA / ESF /
  GHP-USAID / GHP-State / INCLE / NADR / IMET / FMF / Total; same row set as Table 2 plus
  bracketed CBSI memo row. Colombia: A-1 70.0/141.0/2.0/1.7/189.0/21.0/1.9/38.5 = 465.1
  (D05:1505-1523); A-2 80.0/141.0/9.0/2.9/189.0/21.0/1.9/40.0 = 484.7 (D05:2235-2253); A-3
  72.0/156.0/10.0/—/175.0/10.0/1.9/38.0 = 462.9 (D05:2991-3007). Haiti: A-1 52.0/—/24.5/99.8/13.0/
  —/0.3/— = 189.6 (D05:1665-1683); A-2 56.0/5.5/24.5/103.1/30.0/—/0.1/— = 219.2 (D05:2419-2437);
  A-3 111.0/—/34.5/100.0/29.0/—/0.3/— = 274.8 (D05:3149-3167). Mexico: A-1 —/50.0/—/—/100.0/1.2/
  1.8/6.0 = 158.9 (D05:1725-1743); A-2 4.0/57.8/—/—/64.0/1.2/1.3/— = 128.2 (D05:2479-2497); A-3
  —/75.0/—/—/64.0/1.0/1.6/— = 141.6 (D05:3209-3227). Honduras A-3 DA 126.7, total 133.5
  (D05:3169-3187). CBSI memo rows: A-1 [—][32.3][—][—][35.0][—][—][7.5] = [74.8] (D05:2061-2079);
  A-2 [—][35.0][—][—][35.0][—][—][10.0] = [80.0] (D05:2817-2833); A-3 [—][27.0][—][—][29.0][—][—]
  [7.5] = [63.5] (D05:3543-3551). State Central America A-2 —/111.0/—/—/155.0/2.0/—/10.0 = 278.0
  (D05:2773-2791); A-3 —/169.0/—/43.6/219.7/5.0/—/10.5 = 447.8 (D05:3505-3523). Totals rows:
  A-1 D05:2081-2095 (1,794.3b), A-2 D05:2835-2849 (2,037.5b), A-3 D05:3553-3561 (2,407.4).
  Appendix notes: CBSI "is funded through the State Western Hemisphere Regional program"
  (D05:2105, 2859, 3571); note b on A-1/A-2: extra $5.0 million ESF via OAS not included
  (D05:2107-2109, 2861-2863). Sources: A-1 and A-3 CBJ Appendix 2 FY2023 (May 9, 2022); A-2 FY2022
  estimate data (August 16, 2022).
  Layout: every cell is on its own line; a few lines merge two cells (e.g. "72.0 156.0"
  D05:2993; "490.6 378.5b" D05:2083; "36.0 12.6" D05:3535). Row labels wrap ("Trinidad and" /
  "Tobago" D05:2599-2619). Figures 1 (map, D05:111) and 2 (FY1946-FY2019 obligations chart,
  D05:151-159) are not rendered (visual content unavailable; captions and notes only).
- Congressional action (FY2023): House Appropriations Committee reported H.R. 8282/H.Rept.
  117-401 and Senator Coons introduced S. 4662 "in July 2022"; no further action (D05:43, 1149);
  three CRs P.L. 117-180, P.L. 117-229, P.L. 117-264 funded most programs "at the FY2022 level from
  October 1, 2022, until December 29, 2022" (D05:43, 1149); Summary: Congress "concluded action
  ... on December 23, 2022, when it approved" P.L. 117-328 (D05:43); body: "December 29, 2022, when
  the President signed into law" P.L. 117-328, SFOPS = Division K (D05:1149). Explanatory statement
  incorporates H.Rept. 117-401 directives "unless specifically directed to the contrary" (D05:1151).
- Conditions, withholdings, certifications (P.L. 117-328 as described): Central America - withhold
  "60% of ESF and security assistance to support the central governments of El Salvador and
  Guatemala and 45% ... Honduras" until Secretary of State certifies; exceptions (anti-corruption,
  gender-based violence, human rights, food security/humanitarian); "As in prior years, the act
  also prohibits FMF for the Northern Triangle countries" (D05:1315). Colombia - 20% of INCLE until
  certification on coca strategy consistent with the 2016 peace accord; 5% of INCLE for the
  Colombian National Police until certification on police acts against protesters in 2020 and
  2021; 20% of FMF until human rights certification; exceptions for aviation instruction and
  maintenance and maritime/riverine security (D05:1331). Haiti - withhold any aid to support the
  Haitian government until certification of new president and parliament after free and fair
  elections or a broadly representative transitional government; exceptions listed; "As in prior
  years, the act prohibits assistance for the armed forces of Haiti" (D05:1339). Mexico - H.Rept.
  117-401 "states that the act does not provide FMF aid for Mexico" (D05:1353).
- Funding directives (FY2023): CBSI "not less than" $82.0 million, "$18.5 million more than the
  Administration requested and $2.0 million more than ... FY2022" (D05:1307); Central America "up
  to" $100.0 million locally led development in the Northern Triangle, $70.0 million violence
  against women and girls, $61.5 million anti-corruption, $15.0 million democracy programs in
  Nicaragua, $126.7 million DA for Honduras, $40.7 million security assistance for Costa Rica,
  "Some of these activities may overlap" (D05:1311-1313); Colombia $487.4 million "should be made
  available" (+$24.5 million vs request, +$2.7 million vs FY2022 est.), "not less than" $40.0
  million rural security, $37.5 million INCLE rule of law/human rights, $25.0 million ESF
  Afro-Colombian and Indigenous communities, $15.0 million DA biodiversity (D05:1329); Haiti $8.5
  million reforestation, "not less than" $5.0 million prisoners (D05:1337); IAF $47.0 million, "$9.0
  million more than the Administration requested or was appropriated ... in FY2022" (D05:1343);
  Mexico "commensurate with prior fiscal years", FY2022 estimated $128.2 million (D05:1353);
  Venezuela $50.0 million ESF democracy programs (D05:1359).
- Report deadlines: CBSI uses FY2015-FY2021 report "not later than 45 days after enactment"
  (D05:1307); Haiti prenatal/maternal care report, 45 days (D05:1341); Mexico Bicentennial
  Framework impact report "not later than 90 days" (D05:1355-1357); Western Hemisphere
  counternarcotics strategy report "not later than 120 days" (Bolivia, Colombia, Peru, Mexico,
  Central America) (D05:1363-1365); IMET use in Central America FY2012-FY2022 report (D05:1319-1327).
- Rounded prose beside exact figures: "$2.4 billion" vs 2,407.4 / 2,407,408; IMET "+$229,000" vs
  Table 1 13.7 -> 14.0; CBSI cut 16.5 (20.6%) vs Table 2 [80,000]->[63,500]; Table 2 (thousands)
  vs Appendix (millions, one decimal) for every country row.
- Hedged claims: "the 118th Congress may track" (D05:47); "Some of these activities may overlap"
  (D05:1313); "it remains to be seen how much ... will be allocated" (D05:1371); report "is also to
  assess the likelihood that the strategy will sustainably reduce" (D05:1335).
- Amendments or contradictions (internal): CBSI amount in P.L. 117-328 - Summary "the CBSI ($82.5
  million)" (D05:45) vs Table 4 "82.0" (D05:1189) and body "not less than $82.0 million" (D05:1307).
  No precedence stated. Enactment date - Summary "December 23, 2022, when it approved" (D05:43) vs
  body "December 29, 2022, when the President signed" (D05:1149) (different events named).
- Spot-check: see the Bundle spot-check list (Table 2 CBSI row, Table 4 CBSI row, fn 15).
- Coverage: FULL - lines 1-3588 read in chunks (1-110, 110-220, 220-330, 330-530, 530-790,
  790-1050, 1050-1250, 1250-1400, 1400-1700, 1700-2020, 2020-2340, 2340-2680, 2680-3020,
  3020-3380, 3380-3588).

## D06 - U.S. Foreign Assistance to Latin America and the Caribbean: FY2024 Appropriations

- Source: D06 = Doc 6, `docs/crs_r47721.txt` (82,056 chars; text lines 1-1129). Printed page
  headers "Congressional Research Service N": 1 (D06:111), 2 (125), 3 (141), 4 (159), 5 (183),
  6 (203), 7 (271), 8 (297), 9 (319), 10 (373), 11 (455), 12 (501), 13 (549), 14 (573), 15 (653),
  16 (679), 17 (713), 18 (745), 19 (753), 20 (827), 21 (909), 22 (991), 23 (1057), 24 (1120).
- Written or submitted by: Peter J. Meyer, Specialist in Latin American and Canadian Affairs
  (D06:41, 1124). CRS report R47721.
- Type, date, edition: "Updated August 6, 2024" (D06:5, 39); "R47721 · VERSION 10 · UPDATED"
  (D06:1120).
- Period covered: U.S. fiscal years; FY2024 from October 1, 2023 (D06:31, 557). Column labels
  (Tables 1, 2): "FY2021 (actual)", "FY2022 (actual)", "FY2023 (estimate)", "FY2024 (request)", "%
  Change: FY2023-FY2024". Table 3 uses "FY2023 (enacted)" (D06:511-513). Appendix: A-1 "FY2022
  Actual", A-2 "FY2023 Estimate", A-3 "FY2024 Request".
- Scope rule ("Report Notes", D06:129-131): bilateral State/USAID aid; these accounts "accounted
  for 60.3% of the total aid obligated by all U.S. agencies ... in FY2021"; excludes humanitarian
  accounts, other agencies (DOD, MCC, Peace Corps, International Development Finance Corporation)
  and multilateral bodies. Boxes excluded from totals: Central America humanitarian (D06:291-293),
  Haiti and the Global Fragility Act (D06:305-307), Venezuela humanitarian (D06:367-369).
  INCLUSION differs from D05: Table 1 note a "Sum includes $97.2 million of supplemental assistance
  appropriated in the American Rescue Plan Act of 2021 (P.L. 117-2)" (FY2021) and note b "Sum
  includes $64.0 million ... Additional Ukraine Supplemental Appropriations Act, 2022 (P.L.
  117-128)" (FY2022) (D06:273-275); Table 2 notes: "FY2021, FY2022, and FY2023 totals include $5
  million appropriated as voluntary contributions to the Organization of American States"
  (D06:487). "Figures may not sum to totals due to rounding" (D06:273, 487, 877, 1013, 1116).
- Entities and aliases: as D05 plus Americas Partnership Opportunity Fund (new, $51.4 million
  request, D06:25, 189); 2022 Summit of the Americas commitments, $18.0 million (D06:189); Global
  Fragility Act "(P.L. 116- 94, Division J, Title V)", Haiti designated priority country April
  2022, 10-year plan March 2023, funds: Prevention and Stabilization Fund (PSF), Complex Crisis
  Fund, Multi-Donor Global Fragility Fund (D06:305-307); Safe Mobility Offices (initial: Colombia,
  Costa Rica, Ecuador, Guatemala, fn 26 D06:545); Bureau of Population, Refugees, and Migration
  (D06:533); OMB Director Shalanda D. Young letters (Oct 20, 2023 to Patrick Murray, Speaker Pro
  Tempore; Aug 10, 2023 to Kevin McCarthy) (D06:537, 541); Rep. Granger explanatory statement.
- Narrative figures (FY2024 request): "nearly $2.5 billion" (D06:23, 167); increase over FY2023
  estimate "$427.3 million (20.9%)" in Summary (D06:23) but "$427.4 million (20.9%)" in body
  (D06:167); IAF $52.0 million (D06:23, 167, 493); Central America "at least $945.8 million",
  "$275.0 million (41.0%) more" (D06:25, 299), comprising El Salvador $124.8 million, Guatemala
  $164.5 million, Honduras $136.5 million, "a combined $17.1 million for the other four countries",
  CARSI $341.3 million, other regional $161.7 million (D06:299; fn 15 country set D06:309);
  Colombia $444.0 million, -$9.1 million (2.0%) (D06:27, 301); Haiti $291.5 million, +$60.6 million
  (26.2%) (D06:27, 303); Mexico $111.4 million, +$6.8 million (6.5%) (D06:27, 321); Venezuela $54.0
  million, -$3.4 million (5.8%) (D06:323); CBSI $64.5 million, "$17.5 million (21.3%) less than the
  FY2023 estimated allocation" (D06:27, 281). Accounts (D06:187-211): DA $970.7 million (39.3%),
  "+$307.1 million (46.3%)"; ESF $532.1 million (21.5%), +$59.6 million (12.6%); GHP $309.5 million
  (12.5%) = State $190.0 million (-$8.8 million, 4.4%) + USAID $119.5 million (+$4.0 million, 3.5%);
  security $658.3 million (26.6%): INCLE $536.5 million "+$66.4 million (14.1%)"; NADR $32.1
  million "a $9 million (21.9%) reduction" (Colombia assuming demining); IMET $16.2 million "+$3.6
  million (29.1%)"; FMF $73.5 million +$4.5 million (6.5%), "reduced aid to Costa Rica, Peru, and
  Colombia more than offset by increased funding for regional programs".
- Other figures: FY1946-FY2021 "$100.4 billion ($209.9 billion in constant 2021 dollars)" (D06:135);
  33 independent countries (fn 2, D06:137); poverty 45.3% to 30.4% (D06:153-161); humanitarian aid
  to Central America $209.8 million FY2021, est. $216.3 million FY2022, est. $139.9 million FY2023
  (D06:293); Venezuela: 7.8 million migrants/refugees, ~6.6 million in LAC; FY2017-FY2023 "more
  than $2.9 billion", incl. $591.0 million in FY2023; top recipients Colombia, Peru, Ecuador,
  Brazil (D06:369); IAF "active in 27 countries" (D06:493).
- Emergency supplemental request (D06:529-551): October 2023, $1.25 billion foreign assistance
  for LAC migration, modifying an August 2023 request of $782 million; $850.0 million MRA (base
  FY2024 request: $3.9 billion global MRA incl. anticipated $398.0 million Overseas Assistance for
  the Western Hemisphere); $400.0 million ESF; fn 23 "also included $50.0 million under the State
  Department's Diplomatic Programs account". P.L. 118-50 (April 24, 2024) "does not specifically
  designate any resources" for it; provides $9.15 billion humanitarian assistance, "a portion of
  which could be allocated to the region" (Division A, Title III) (D06:31, 725, 741).
- Tables:
  Table 1 by account, "(millions of current U.S. dollars)", D06:213-275 (flattened rows, one line
  per row): DA 490.6 / 656.5 / 663.7 / 970.7 / +46.3%; ESF 480.7a / 501.4b / 472.5 / 532.1 /
  +12.6%; GHP (USAID) 55.5 / 91.5 / 115.5 / 119.5 / +3.5%; GHP (State) 195.0 / 191.3 / 198.8 /
  190.0 / -4.4%; INCLE 553.0 / 541.8 / 470.2 / 536.5 / +14.1%; NADR 31.0 / 32.1 / 41.1 / 32.1 /
  -21.9%; IMET 13.8 / 11.3 / 12.5 / 16.2 / +29.1%; FMF 76.9 / 78.5 / 69.0 / 73.5 / +6.5%; Total
  1,896.5a / 2,104.4b / 2,043.3 / 2,470.7 / +20.9% (D06:241-265). Sources: CBJ Supplementary
  Tables FY2023 (May 2022), FY2024 (April 2023), FY2025 (April 2024) (D06:267, 273).
  Table 2 by country/regional program, "(thousands of current U.S. dollars)", D06:325-489; partly
  Markdown pipe tables (D06:357-361, 399-423), then one-line rows (D06:425-485). 26 country rows,
  alphabetical, now including Bolivia 4,000 / 0 / 0 / 0 / — (D06:401; no Bolivia row in D05).
  Selected rows FY2021 / FY2022 / FY2023 est / FY2024 req / %: Colombia 478,192 / 490,337 / 453,096
  / 444,025 / -2.0% (D06:404); Haiti 204,377 / 237,428 / 230,905 / 291,455 / +26.2% (D06:412);
  Honduras 79,902 / 117,878 / 141,774 / 136,450 / -3.8%; Mexico 158,910 / 127,107 / 104,575 /
  111,400 / +6.5% (D06:415); El Salvador 80,790 / 98,652 / 87,096 / 124,800 / +43.3%; Guatemala
  103,849 / 137,442 / 121,370 / 164,502 / +35.5%; Venezuela 38,000 / 48,600 / 57,350 / 54,000 /
  -5.8% (D06:423); Costa Rica 9,225 / 8,183 / 12,725 / 600 / -95.3%; Brazil 27,950 / 29,781 /
  39,198 / 42,000 / +7.1%; Barbados and Eastern Caribbean 7,700 / 24,621 / 22,220 / 24,000 / +8.0%
  (D06:425-427); USAID Central America Regional 5,000 / 35,000 / 29,950 / 85,178 / +184.4%; USAID
  South America Regional 15,000 / 27,000 / 26,000 / 55,400 / +113.1%; USAID LAC Regional 45,540 /
  38,697 / 56,850 / 41,678 / -26.7%; State Central America Regional — / 278,000 / 246,700 / 417,800 /
  +69.4%; State Western Hemisphere Regional 366,909 / 102,044 / 120,305 / 201,910 / +67.8%
  (D06:429-451); [CBSI] [74,800] [80,000] [82,000] [64,500] [-21.3%] (D06:481-483); Total
  1,896,495a / 2,104,421b / 2,043,300 / 2,470,653 / +20.9% (D06:485). Note: "Prior to FY2022,
  activities funded through the State Central America Regional program were funded under the
  State Western Hemisphere Regional program" (D06:487).
  Table 3 IAF, "(millions of current U.S. dollars)" (D06:503-527): FY2021 (actual) 38.0; FY2022
  (actual) 42.0; FY2023 (enacted) 47.0; FY2024 (request) 52.0; +10.6%.
  Table 4 selected countries/initiatives, "(millions ...)" (D06:575-643); columns FY2022 (actual)a /
  FY2023 (estimate) / FY2024 (request) / H.R. 4665 and H.Rept. 118-146 / S. 2438 and S.Rept.
  118-71 / P.L. 118-47 and explanatory statement: CBSI 80.0 / 82.0 / 64.5 / 97.5 / 82.0 / 88.0;
  Central America 704.9b / 670.8 / 945.8b / NA / NA / NA; Colombia 490.3 / 453.1 / 444.0 / NA /
  487.4 / 377.5c; Haiti 237.4 / 230.9 / 291.5 / NA / NA / NA; IAF 42.0 / 47.0 / 52.0 / 22.5 / 52.0
  / 47.0; Mexico 127.1 / 104.6 / 111.4 / NA / NA / NA; Venezuela 48.6 / 57.4 / 54.0 / 50.0 / 50.0
  / 50.0c (D06:619-637). Notes: NA = "not specified in the bill/legislation or report/explanatory
  statement"; a = FY2022 includes P.L. 117-128; b = Central America country set; c = totals "may
  not be comprehensive" (no IMET, NADR or GHP levels for Colombia; no GHP level for Venezuela)
  (D06:639-643).
  Appendix A-1 FY2022 Actual (D06:757-879), A-2 FY2023 Estimate (D06:881-1015), A-3 FY2024 Request
  (D06:1017-1116), "(millions ...)", columns DA / ESF / GHP-USAID / GHP-State / INCLE / NADR /
  IMET / FMF / Total; mixed pipe-table blocks and space-separated rows. No Bolivia row. Colombia:
  A-1 80.0/147.0a/9.0/2.9/189.0/21.0/1.5/40.0 = 490.3 (D06:785); A-2 86.0/144.0/8.8/3.0/150.0/21.0/
  1.9/38.5 = 453.1 (D06:929); A-3 103.0/122.0/9.0/—/160.0/10.0/2.0/38.0 = 444.0 (D06:1042). Haiti:
  A-1 59.0/20.5a/24.5/103.1/30.3/—/0.1/— = 237.4 (D06:803); A-2 46.4/7.0/30.0/102.5/45.0/—/—/— =
  230.9 (D06:943); A-3 113.2/—/33.0/100.0/45.0/—/0.3/— = 291.5 (D06:1050). Mexico: A-1 4.0/56.8/—/—/
  64.0/1.2/1.2/— = 127.1 (D06:810); A-2 —/54.0/—/—/48.0/1.0/1.6/— = 104.6 (D06:946); A-3 —/60.7/—/—/
  48.0/1.0/1.7/— = 111.4 (D06:1053). Honduras A-2 DA 126.7, total 141.8 (D06:944); A-3 DA 129.7,
  total 136.5 (D06:1051). CBSI memo: A-1 [—][35.0][—][—][35.0][—][—][10.0][80.0] (D06:871-873);
  A-2 [—][37.0][—][—][35.0][—][—][10.0][82.0] (D06:1007-1009); A-3 [—][28.0][—][—][29.0][—][—][7.5]
  [64.5] (D06:1110-1112). Totals: A-1 656.5 / 501.4a / 91.5 / 191.3 / 541.8 / 32.1 / 11.3 / 78.5
  / 2,104.4a (D06:875); A-2 663.7 / 472.5b / 115.5 / 198.8 / 470.2 / 41.1 / 12.5 / 69.0 / 2,043.3a
  (D06:1011); A-3 "Total 90.7 532.1 119.5 190.0 536.5 32.1 16.2 73.5 2,470.7" (D06:1114). A-1 note a
  (D06:877): ESF cells marked "a" (Colombia 147.0, Dominican Republic 3.0, Guatemala 20.0, Haiti
  20.5, Honduras 10.0, Barbados and Eastern Caribbean 10.0) "include a combined $64.0 million" of
  P.L. 117-128; ESF total includes $5.0 million OAS. A-2 note b: ESF total includes $5.0 million
  OAS (D06:1015). A-1 sources: FY2024 CBJ Supplementary Tables and DeLauro statement p. H3007; A-2
  sources: FY2025 CBJ Supplementary Tables and Leahy statement p. S9299; A-3: FY2024 CBJ
  Supplementary Tables (D06:877, 1013, 1116).
- Congressional action (FY2024): House Appropriations Committee reported H.R. 4665/H.Rept. 118-146
  on July 17, 2023; House passed it September 28, 2023; Senate Appropriations Committee reported
  S. 2438/S.Rept. 118-71 July 20, 2023 (D06:31, 557); CRs P.L. 118-15, P.L. 118-22, P.L. 118-35,
  P.L. 118-40 funded programs "at the FY2023 level from October 1, 2023, until March 23, 2024"
  (D06:557); P.L. 118-47 (Further Consolidated Appropriations Act, 2024) signed by President Biden
  March 23, 2024, SFOPS = Division F (D06:31, 557); explanatory statement (Granger, H.R. 2882,
  Congressional Record vol. 170, no. 51, March 22, 2024) incorporates H.Rept. 118-146 and S.Rept.
  118-71 "unless specifically directed to the contrary" (D06:561, 567); fn 30: explanatory
  statement directives "are not considered statutorily binding" but agencies "tend to follow"
  them (D06:569). P.L. 118-50 supplemental April 24, 2024 (D06:31, 725).
- Conditions, withholdings, certifications (FY2024, as described): Central America - withhold 60%
  of ESF and security assistance (e.g., INCLE and IMET) for the central governments of El
  Salvador, Guatemala, and Honduras; "Congress has enacted similar conditions annually since
  FY2016"; exceptions add "support women's economic empowerment"; FMF prohibition for the three
  "enacted annually since FY2021" (D06:659). Colombia - pre-obligation counternarcotics strategy
  report; pre-obligation report on U.S.-Colombian relations (D06:665-681); 20% of INCLE until
  certification on reduced coca cultivation/production/trafficking and cooperation "in the
  previous 12 months" (§7045(c)(3)(A)); 20% of FMF until human rights certification
  (§7045(c)(3)(B)) (D06:683). Haiti - withhold aid to the central government until certification
  "by January 1, 2025, that elections have been scheduled or held"; exceptions; armed forces
  prohibition "As in prior years" (D06:685). Mexico - withhold 15% of security assistance (e.g.,
  INCLE, NADR, IMET, FMF) until fentanyl/TCO/cooperation/extradition certification (§7045(h))
  (D06:693-715); S.Rept. 118-71 pre-obligation INCLE human-rights report (D06:715). Venezuela -
  50% of election-related funds withheld until a determination on diaspora participation,
  observation and opposition candidates (§7045(l)) (D06:719).
- Funding directives (FY2024): CBSI "not less than $88.0 million" (§7045(k)), "$23.5 million more
  than ... requested ... and $6.0 million more than ... FY2023", prioritized for transit-zone
  countries "most directly impacted by the crisis in Haiti" (D06:645); Central America $61.5
  million anti-corruption, $70.0 million violence against women and girls (§7045(b)(1)), $15.0
  million democracy and religious freedom programs in Nicaragua, $46.0 million security assistance
  for Costa Rica (D06:657); Colombia "at least $377.5 million ... including $77.0 million in IMET
  aid, $129.0 million in ESF aid, $134.5 million in INCLE aid, and $37.0 million in FMF aid",
  "$66.5 million less than ... requested ... and $75.6 million less than Congress appropriated
  ... in FY2023"; no GHP, NADR or IMET levels, "through which Colombia received nearly $34.6
  million in aid for FY2023" (D06:663); Haiti funds "shall be made available ... basic needs"
  (§7045(g)) (D06:685); IAF $47.0 million, "$5.0 million less than ... requested ... and the same
  amount ... in FY2023" (D06:689); Mexico "not less than $125.0 million in global ESF and INCLE"
  for counter-fentanyl programs "including in Mexico" (§7036) (D06:691); Venezuela $50.0 million
  ESF democracy programs; funds "shall be made available" for host communities (§7045(l)(3))
  (D06:719-721). Outlook: four broad priorities (D06:749).
- Report deadlines: CBSI FY2016-FY2022 uses, 45 days (H.Rept. 118-146 p.123) (D06:645-655); CARSI
  use FY2015-FY2023, IMET use FY2023 and other Central America reports (D06:661, fn 36); Haiti
  options report "not later than 60 days" (attributed to "H.Rept. 118-71", fn 43 cites H.Rept.
  118-146 p.119) and S.Rept. 118-71 90-day consultation on a second Haitian National Police
  training center (D06:687, 705-707); Mexico fentanyl alignment report 60 days (§7036(d)(2)) and
  Bicentennial Framework report 90 days (H.Rept. 118-146 p.120) (D06:717); Venezuela host-community
  report 45 days (H.Rept. 118-146 pp.60-61) (D06:721).
- Rounded prose beside exact figures (mapper arithmetic from Table 1, not printed): DA 970.7 -
  663.7 = 307.0 vs prose "$307.1 million"; INCLE 536.5 - 470.2 = 66.3 vs prose "$66.4 million";
  IMET 16.2 - 12.5 = 3.7 vs prose "$3.6 million"; NADR "$9 million" vs 41.1 - 32.1; total 2,470.7
  - 2,043.3 = 427.4 (body) vs Summary "427.3". Colombia FY2023 GHP+NADR+IMET from A-2 (8.8 + 3.0
  + 21.0 + 1.9 = 34.7) vs prose "nearly $34.6 million". Central America components (D06:299) sum
  to 945.9 vs "at least $945.8 million". Table 2 thousands vs Appendix millions throughout.
- Hedged claims: P.L. 118-50 humanitarian funds, "a portion of which could be allocated to the
  region" (D06:725); "It remains unclear how much ... may be allocated" (D06:749); Colombia total
  "may not be comprehensive, however" (D06:663); explanatory statement directives not
  statutorily binding (fn 30).
- Internal inconsistencies/typos (record as printed): "$427.3 million" (D06:23) vs "$427.4
  million" (D06:167); A-3 DA total "90.7" (D06:1114) vs Table 1 "970.7" (D06:241) and prose
  "$970.7 million" (D06:187); Colombia "$77.0 million in IMET aid" in the designation list vs "does
  not designate specific funding levels for Colombia under the GHP, NADR, or IMET accounts" in the
  same paragraph (D06:663) and Table 4 note c (D06:643); "P.L. 118-147" in country sections
  (D06:657, 665, 685, 689, 691, 717, 719) while the act is identified as "P.L. 118-47"
  (D06:31, 557); "H.Rept. 118-71" (D06:687); "The act also mains a prohibition" (D06:659); A-2
  total "2,043.3a" carries the regional-programs note letter (D06:1011); Figure 2 not rendered.
- Spot-check: A-3 total row (docs 1112), Table 2 Colombia pipe row (docs 402), "$427.3"/"$427.4"
  (docs 21/165) and "P.L. 118-147" lines identical in docs. Pipe tables render cells with "|"
  (see memory: platform text shows those rows without pipes).
- Coverage: FULL - lines 1-1129 read in chunks (1-130, 130-240, 240-330, 330-420, 420-480,
  480-560, 560-630, 630-690, 690-760, 760-880, 880-990, 990-1099, 1099-1129).

## D07 - Foreign Assistance: Where Does the Money Go?

- Source: D07 = Doc 7, `docs/crs_r48150.txt` (100,100 chars; text lines 1-743). Page headers
  "Congressional Research Service N": 1 (D07:103), 2 (127), 3 (143), 4 (163), 5 (189), 6 (211),
  7 (243), 8 (273), 9 (299), 10 (319), 11 (341), 12 (397), 13 (407), 14 (419), 15 (447), 16 (469),
  17 (489), 18 (515), 19 (541), 20 (571), 21 (621), 22 (643), 23 (673), 24 (703), 25 (729).
- Written or submitted by: Nick M. Brown, Analyst in Foreign Assistance (D07:45, 735). CRS
  report R48150.
- Type, date, edition: August 8, 2024 (D07:5, 43); "R48150 · VERSION 1 · NEW" (D07:729). The
  page-1 header reads "Congressional Research Service [draft, not for distribution beyond USAID]
  1" (D07:103). Not a localization-only report: general overview of aid delivery through
  implementing partners; "Local Partnering" is the last section (D07:677-731).
- Period covered: obligations data FY2013-2022 from foreignassistance.gov, "the last year for
  which data was fully reported" (D07:113; fn 5 D07:123); FY2023 appropriations "$66.1 billion"
  (D07:19, 107); some FY2023-FY2024 items (award shares, OE ratio, Ukraine).
- Cross-reference to a bundle document: "For more details on the funding process, see CRS In
  Focus IF11515, U.S. Foreign Assistance: Budget Development and Execution, by Nick M. Brown"
  (D07:39) = D02 (`crs_if11515`). Same author as D02; co-author of D01.
- Entities and aliases: USAID; State Department; Peace Corps ("Small Projects Assistance",
  D07:169); MCC (reports itself as implementing partner, fn 9 D07:175; compacts excluded from
  Figure 5); U.S. International Development Finance Corporation (D07:223); National Endowment for
  Democracy (D07:275); Global Fund to Fight AIDS, Tuberculosis and Malaria ("the Global Fund");
  Global Alliance for Vaccines and Immunization (GAVI); UNHCR; World Bank; World Food Programme
  (WFP); CGIAR; ICRC; IFRC; COFA countries = Marshall Islands, Micronesia, Palau (fn 57 D07:443);
  Palestinian Authority; Government of Jordan; Ukraine; MASHAV (Israel); Academy for Educational
  Development (AED) absorbed into FHI-360 (D07:627, 645). Spellings: "FHI 360" (Table 1, D07:359),
  "FHI360" (box, D07:605), "FHI-360" (D07:645). "DAI, a firm" (box, D07:315) and "Development
  Alternatives, Inc." (Table 1, box) - the text never states they are the same entity.
  "ADCI/VOCA" in Table 1 (D07:381) with note a "Agriculture Cooperative Development
  International/Volunteers in Overseas Cooperative Assistance" (D07:385). People: USAID
  Administrators Samantha Power, Rajiv Shah; Rep. Michael McCaul and Sen. Joni Ernst letter (April
  24, 2023, fn 72); Darrell E. Issa letter (April 26, 2012, fn 113); Sens. Tim Kaine and Marco
  Rubio (S. 2509, fn 115).
- Operative definitions ("Key T erms" box, D07:129-131): implementing partner; "Economic
  assistance is all nonmilitary foreign assistance"; project; scope of work; institutional support
  contractors; personal services contractors; for-profit firm ("contractor"); nonprofit
  organization. Also: "nonmilitary" = foreignassistance.gov "Economic" (D07:149); fn 6 project
  totals include "project-type" and "technical assistance" (D07:137); fn 7 inherently governmental
  functions = FAR Subpart 7.5; fn 10 "NGO" covers nonprofits and for-profits (D07:177); fn 13
  allowable / allocable / reasonable (D07:183); budget support (to governments) vs core
  contribution (to PIOs) (D07:197); loan guarantee (D07:221); administrative costs and the two
  Operating Expenses categories (D07:247-253); acquisition vs assistance box (D07:313-315: profit
  allowed under acquisition, not assistance; cooperative agreement = more USAID oversight than a
  grant, contracts more still); direct vs indirect costs (D07:325); PIOs (D07:389, fn 46 ADS 308);
  assessed contributions "are not considered foreign assistance" (D07:399); PASA vs PAPA
  (D07:481-491); local entities: August 2022 counts only organizations "registered and
  headquartered in the country in question" vs earlier "locally established partners" (local
  entities plus international organizations with local offices) (D07:681, fn 105); PIO assistance
  not subject to the 25% target (D07:705).
- Data (FY2013-FY2022 unless stated): USAID project obligations $181.5 billion, NGOs $109.8
  billion (60%) (D07:165); USAID = 69.8% of NGO-implemented nonmilitary obligations in 2022
  (D07:279); FY2023 new NGO awards by value: "three-quarters" assistance, "a quarter" acquisition
  (award ceilings, not obligations, fn 38) (D07:301, 309); nonprofits 59.8% / for-profit 40.2%;
  universities 6.5% and church/faith-based 5.8% of USAID nonprofit funding, over half of the latter
  to Catholic Relief Services (D07:301); "more than 6,000 unique NGOs", top ten "around 20%"
  (D07:301, 321); U.S. NGOs 82.7% / non-U.S. 17.3% (D07:323); administrative costs 7.7%
  (D07:247); PIOs implemented 35.4% of nonmilitary aid (D07:389); Global Fund $15.89 billion
  (D07:421); 49.6% of economic aid to PIOs project-based (D07:423); direct budget support 1.9%,
  "More than 87.3% of those funds went to four governments: 66.9% to the Government of Jordan
  and 29.5% to three Compact of Free Association (COFA) countries" (D07:427); loans 28% of
  economic aid 1962-1988 (D07:219); 20 sovereign loan guarantees 1993-2017, three active, none
  since 2017 (D07:221); interagency agreements "generally less than 1%" of USAID funding
  (D07:491); top five ~20% of USAID obligations to NGOs yearly, >1,300 NGOs above $1 million
  (D07:579); indirect costs: 2002 USAID estimate 30%, 2021 estimate up to 50%, E.U./U.N. caps
  ~7%, USAID de minimis 10% (D07:545, fn 71); OE obligations as share of USAID program accounts:
  10.31% (2009, Div. H of P.L. 111-8), 8.84% (2024, Div. F of P.L. 118-47), 8.19% (1989, P.L.
  100-461) (fn 71, D07:537); local partners 18% of project funds (2021 implementer analysis,
  D07:707); localization target 25% of acquisition and assistance dollars "by 2025" (D07:679);
  Ukraine "over $22.9 billion in FY2022 and FY2023" (Figure 5 note, D07:477); Pakistan $43 million
  de-obligations (D07:477); Chemonics 4,276 DEC documents vs WFP 62 (fn 95, D07:665); AED 90% and
  FHI-360 ">80%" (2023) U.S. government funding (D07:645).
- Tables: Table 1 "NGOs Obligated More than $1 Billion in U.S. Nonmilitary Foreign Assistance,
  FY2013-FY2022" (D07:343-385), exact dollars; columns Rank / Organization Name / Organization
  Type / Total Obligations FY2013-2022; 15 rows: 1 Catholic Relief Services (U.S. faith-based)
  $4,637,395,555; 2 Chemonics International, Inc. (U.S. for-profit) $4,536,397,348; 3 FHI 360
  (International nonprofit) $3,788,300,843; 4 Development Alternatives, Inc. (U.S. for-profit)
  $3,071,449,561; 5 Abt Associates, Inc. (U.S. for-profit) $2,629,027,445; 6 RTI International
  (U.S. university/research institute) $2,307,061,081; 7 John Snow International (U.S. nonprofit)
  $1,840,556,823; 8 Save the Children Federation, Inc. ("U.S. for-profit enterprise")
  $1,543,142,073; 9 ARD, Inc. (International nonprofit) $1,485,806,517; 10 Jhpiego Corporation
  (U.S. nonprofit) $1,260,308,627; 11 Deloitte (Non-U.S. for-profit) $1,174,468,049; 12 World
  Vision (International nonprofit) $1,166,734,792; 13 Mercy Corps (U.S. nonprofit)
  $1,135,480,585; 14 ADCI/VOCA (U.S. nonprofit) $1,084,647,816; 15 Population Services
  International (International nonprofit) $1,077,027,102 (last). Notes: "more than $50 billion
  ... obligated to 'redacted' or otherwise unspecified recipients"; U.S./international nonprofit
  split is CRS's own (D07:385); fn 39: list "incomplete; more than a third of obligations ... are
  marked as redacted or 'other'" (FATAA exceptions) (D07:311). Box table "NGOs by Number of
  Appearances as Annual Top Five USAID Partner, FY2013-FY2022" (D07:591-617): Chemonics 10;
  FHI360 10; Development Alternatives, Inc. 10; Abt Associates 9; Catholic Relief Services 8; RTI
  International 2; Management Sciences for Health 1 (last).
  Figures 1-5 (D07:145-149, 265-269, 291-295, 409-413, 473-477) are not rendered; captions and
  notes only (Figure 4 note: "All recipients over $1 billion are named"; Figure 5: "Recipients over
  $100 million are named") - the named recipients are not readable in text (visual gap).
- Lists: aid "types" - "five aid 'types': Projects, Administrative Costs, Core Contributions,
  Budget Support, Technical Assistance, and Other" (six names, D07:135); partner types (D07:257);
  fn 9 reporting categories (D07:175); summary trade-off questions, 5 bullets (D07:29-37); OE
  factors, 4 bullets (D07:519-525); localization initiatives: USAID Forward (Obama), USAID
  Transformation (Trump), Localization (current) (fn 103, D07:693).
- Actions vs proposals/mentions: Power's 25% target and the August 2022 counting rule are agency
  actions (D07:679-681); S. 2509 (Kaine/Rubio, New Partnerships Initiative) and H.R. 7710 are
  proposals (fn 115-116, D07:731, 741-743); "Congress has yet to weigh in through oversight,
  reports, or legislation on localization goals" (D07:731). History: 1981 FAA amendment requiring
  PVOs to get at least 20% of funding from non-U.S. government sources (§123(g), repealed), moved
  to appropriations in FY1998, "removed beginning in FY2005" with "No public explanation" (D07:627,
  fn 88); later called "the 80% limit and its 2005 removal" (D07:645). Last comprehensive
  reauthorization "P.L. 99-83" (fn 68, D07:509). FY2024 Ukraine budget support by loan, Section 507
  of Div. B of P.L. 118-50 (fn 23, D07:233). 2024 OIG-commissioned audit on NICRAs; USAID disputed
  two of three findings (D07:549-573, fn 80).
- Hedged claims: "These categories may be misleading" (D07:151); grants and cooperative agreements
  "appear to make up substantially more" (D07:301); fn 18 "It is possible that in earlier periods"
  (D07:207); 2023 analysis: USAID's approach "may both overestimate ... and under-count"
  (D07:681); "Such an example may not reflect" (D07:681-705); Risk Appetite Statement "may be a
  hurdle" (D07:709); "which may in part explain" (D07:623); "These costs may be substantial"
  (D07:545); audit "purported several deficiencies" (D07:549).
- LAC mentions: El Salvador CDCS FY2020-2025 (fn 16); Guatemala local NGO example (D07:681);
  Brazil and Chile trilateral cooperation (D07:471); NYT article on aid to Central America (fn 77).
- Internal inconsistencies (record as printed): "five" types vs six names (D07:135); "More than
  87.3%" vs 66.9% + 29.5% (mapper sum 96.4) (D07:427); fn 95 "the largest NGO partner with USAID
  from 2013 to 2022 was Chemonics International" (D07:665) vs Table 1 rank 1 Catholic Relief
  Services (D07:355-357) - Table 1 title says "U.S. Nonmilitary Foreign Assistance" while D07:301
  calls it "USAID's top reported NGO implementing partners"; Save the Children Federation typed
  "U.S. for-profit enterprise" (D07:369) vs fn 41 treating it as an international NGO domiciled in
  the U.S. (D07:329); Figure 2 note "See footnote 13" (D07:269) and fn 31 "See footnotes 11 and
  12" (D07:283) point to footnotes on other topics; "Risk Appetite Statement" cited as August 22,
  2022 (fn 12) and, as "current", June 2018 (fn 114).
- Spot-check: docs lines 101 (draft header), 133 ("five aid 'types'"), 367 (Table 1 row 8), 425
  ("More than 87.3%") and 663 (fn 95) identical to text.
- Coverage: FULL - lines 1-743 read in chunks (1-90, 90-180, 180-260, 260-340, 340-420, 420-490,
  490-550, 550-610, 610-670, 670-729, 729-743). Figures unreadable (see Gaps).

## D08 - U.S. Foreign Assistance to Latin America and the Caribbean: FY2025 Appropriations

- Source: D08 = Doc 8, `docs/crs_r48266.txt` (88,210 chars; text lines 1-1068). Page headers
  "Congressional Research Service N": 1 (D08:121), 2 (135), 3 (153), 4 (169), 5 (191), 6 (231),
  7 (293), 8 (321), 9 (349), 10 (367), 11 (425), 12 (459), 13 (487), 14 (509), 15 (539), 16 (569),
  17 (597), 18 (623), 19 (663), 20 (671), 21 (764), 22 (851), 23 (930), 24 (996), 25 (1063).
- Written or submitted by: Peter J. Meyer, Specialist in Latin American and Canadian Affairs
  (D08:37, 1059). CRS report R48266.
- Type, date, edition: "Updated January 14, 2025" (D08:5, 35); "R48266 · VERSION 4 · UPDATED"
  (D08:1063). fn 9 cites R47721 (= D06) for FY2024 appropriations (D08:223).
- Period covered: FY2025 request and bills; "FY2024 allocations are not yet publicly available"
  (D08:137, 281; Table 2 note "Final FY2024 allocations" D08:421). Prose comparison base: FY2025
  request vs "the estimated amount allocated for the region for FY2023 (the most recent fiscal
  year for which such data are available)" (D08:23, 177) - not FY2024. Column labels: Table 1
  "FY2022 (actual)", "FY2023 (est. actual)", "FY2025 (request)", "% Change (FY23-FY25)" (no FY2024
  column); Table 2 "FY2023 (est. actual)", "FY2024 (enacted)", "FY2025 (request)", "H.R. 8771 and
  H.Rept. 118-554", "S. 4797 and S.Rept. 118-200"; Table 3 "FY2021 (actual)", "FY2022 (actual)",
  "FY2023 (enacted)", "FY2024 (enacted)", "FY2025 (request)", "H.R. 8771", "S. 4797"; A-1 "FY2021
  (actual)", "FY2022 (actual)", "FY2023 (est. actual)", "FY2025 (request)", "% Change:
  FY2023-FY2025"; A-2 title "FY2023 Estimate"; A-3 title "FY2025 Request".
- Scope rule ("Report Notes", D08:139-143): accounts "accounted for about 54% of the total aid
  obligated by all U.S. agencies ... in FY2022"; other sources (Food for Peace Title II, IDA, MRA,
  DOD, MCC, Peace Corps, DFC) are included only in the Trends obligation data and excluded
  elsewhere "with the exception of the 'Migration and Refugee Assistance' text box".
- Trends and context: FY1946-FY2022 "$104.0 billion ($228.3 billion in constant 2022 dollars)"
  (D08:147); fn 2: DOD partial data FY2020-FY2022, DHS and Transportation partial FY2022
  (D08:149); poverty "By 2014 ... 27.7% (down from 44.1% at the start of the century)" (D08:171);
  fn 12 World Bank: 23 of 33 countries lower/upper middle income, 9 high income, Venezuela
  unclassified (D08:289); Figure 2 (FY1946-FY2022, constant 2022 dollars) not rendered.
- Summary/request figures: "$2.2 billion"; "$161.9 million (7.9%) above" FY2023 estimate; IAF
  $52.0 million; Central America "at least $632.6 million"; Colombia $413.3 million; Haiti $356.7
  million; Mexico $109.7 million; CBSI $81.0 million; Venezuela $53.8 million; these priorities
  "account for nearly 75%" (D08:23-25, 177, 375). Grouping: "economic and other development
  assistance programs: Development Assistance (DA), Economic Support Fund (ESF), and Global Health
  Programs (GHP)" = 68.2%; "military and civilian security assistance programs: Foreign Military
  Financing (FMF); International Military Education and Training (IMET); International Narcotics
  Control and Law Enforcement (INCLE); and Nonproliferation, Anti-terrorism, Demining, and Related
  programs (NADR)" = 31.8% (D08:221-233).
- Account prose (base = FY2023 estimate; House/Senate figures are global, not regional)
  (D08:285-359): DA $672.5 million (30.5%), +$8.8 million (1.3%), Honduras DA -$47.2 million "in
  part to bring assistance for Honduras back in line with prior years after a congressionally
  directed increase for FY2023", ~6.2 million Venezuelans in other South American countries (June
  2024); House -33.8%, Senate -8.4%. ESF $523.5 million (23.7%), +$51.0 million (10.8%); separate
  $100.0 million global ESF for Brazil's Amazon Fund; House -16.6%, Senate -0.7%. GHP $309.0 million
  (14.0%) = State $190.0 million (-$8.8 million, 4.4%) + USAID $119.0 million (+$3.5 million,
  3.0%); House -3.3% State / -9.2% USAID; Senate +0.2% State / -4.0% USAID. INCLE $584.9 million
  (26.5%), +$114.7 million (24.4%), Haiti increase (Kenyan-led Multinational Security Support
  mission); House +31.9%, Senate -10.6%. NADR $30.1 million (1.4%), -$11.0 million (26.8%)
  (Colombia assuming demining); House fully funds, Senate -4.0%. IMET $16.2 million (0.7%), +$3.7
  million (29.5%); House same as request, Senate fully funds. FMF $69.0 million (3.1%), same as
  FY2023; House +12.2%, Senate +1.3%.
- MRA text box (D08:361-371): FY2025 request $475.0 million MRA Overseas Assistance for the
  Western Hemisphere; FY2023 regional MRA obligations $543.9 million, which "may have included
  appropriations from multiple fiscal years"; ~6.6 million Venezuelan migrants in LAC; Safe
  Mobility Offices in Colombia, Costa Rica, Guatemala, Ecuador; House: MRA "nearly 49.0% less"
  globally, no SMO funds "unless expressly authorized by a subsequent Act of Congress"; the House
  "rejected a proposed amendment" H.Amdt. 1046 (IOM in the Western Hemisphere); H.Rept. 118-554
  IOM and host-community reports; Senate: MRA 5.3% more globally, resettlement support, Central
  American Minors report. IOM definition of irregular migration (D08:371).
- Tables:
  Table 1 by account, "(millions of current U.S. dollars)" (D08:235-283), one line per row:
  DA 656.5 / 663.7 / 672.5 / +1.3%; ESF 501.4a / 472.5 / 523.5b / +10.8%; GHP (USAID) 91.5 /
  115.5 / 119.0 / +3.0%; GHP (State) 191.3 / 198.8 / 190.0 / -4.4%; INCLE 541.8 / 470.2 / 584.9 /
  +24.4%; NADR 32.1 / 41.1 / 30.1 / -26.8%; IMET 11.3 / 12.5 / 16.2 / +29.5%; FMF 78.5 / 69.0 /
  69.0 / —; Total 2,104.4a / 2,043.3 / 2,205.2b / +7.9% (D08:257-279). Note a: "Sum includes $64.0
  million ... (P.L. 117-128)"; note b: "Sum does not include $100.0 million ... for a contribution
  to Brazil's Amazon Fund" (D08:281-283). Sources: CBJ Supplementary Tables FY2025 (April 2024) and
  FY2024 (April 2023).
  Table 2 "U.S. Foreign Assistance for Selected Countries and Initiatives: FY2025 Request and
  Appropriations Legislation", "(millions ...)" (D08:379-429): CBSI 82.0 / 88.0 / 81.0 / 97.5 /
  88.0; Central America 670.8a / NA / 632.6a / NA / NA; Colombia 453.1 / 377.5b / 413.3 / 208.5b /
  380.0; Haiti 230.9 / NA / 356.7 / NA / NA; Mexico 104.6 / NA / 109.7 / NA / NA; Venezuela 57.4 /
  50.0b / 53.8 / 50.0b / 50.0b (D08:405-419). No IAF row (IAF is Table 3). Notes: "NA indicates
  that appropriation totals are not specified in the bill or report"; CBSI "has been funded through
  the State Department's Western Hemisphere Regional program"; a = Central America country set
  (Belize, Costa Rica, El Salvador, Guatemala, Honduras, Nicaragua, Panama + State/USAID Central
  America regional programs); b = totals "may not be comprehensive" (D08:421-429).
  Table 3 IAF, "(millions ...)" (D08:627-649): 38.0 / 42.0 / 47.0 / 47.0 / 52.0 / 22.5 / 52.0 (no
  % column).
  Table A-1 by country/regional program, "(thousands of current U.S. dollars)" (D08:675-818);
  pipe blocks D08:703-707 and D08:739-744 (in the second block the label and FY2021 value share
  one cell, e.g. "| Nicaragua 12,592a |"), other rows one line each. FY2021 / FY2022 / FY2023
  est. actual / FY2025 req / %: Colombia 478,192a / 490,337c / 453,096 / 413,275 / -8.8% (D08:715);
  Haiti 204,377a / 237,428c / 230,905 / 356,655 / +54.5% (D08:731); Honduras 79,902a / 117,878c /
  141,774 / 86,300 / -39.1% (D08:733); Mexico 158,910 / 127,107 / 104,575 / 109,700 / +4.9%
  (D08:737); El Salvador 80,790a / 98,652 / 87,096 / 87,700 / +0.7%; Guatemala 103,849a /
  137,442c / 121,370 / 115,800 / -4.6%; Venezuela 38,000 / 48,600 / 57,350 / 53,750 / -6.3%
  (D08:752); Brazil 27,950a / 29,781 / 39,198 / 36,500b / -6.9% (D08:711); Bolivia 4,000a / 0 / 0
  / 0 / — (D08:709); Jamaica 24,446a / 24,300 / 22,524 / 9,750 / -56.7%; Peru 98,885a / 109,134 /
  100,379 / 94,800 / -5.6%; Bahamas 200 / 210 / 200 / 300 / +50.0%; Barbados and Eastern Caribbean
  7,700 / 24,621c / 22,220 / 22,500 / +1.3%; USAID Caribbean Development 15,800a / 15,438 / 13,000
  / 13,000 / —; USAID Central America Regional 5,000 / 35,000 / 29,950 / 29,950 / — (D08:788);
  USAID South America Regional 15,000 / 27,000 / 26,000 / 87,664 / +237.2%; USAID LAC Regional
  45,540 / 38,697 / 56,850 / 81,350 / +43.1%; State Central America Regional — / 278,000 / 246,700
  / 295,800 / +19.9%; State Western Hemisphere Regional 366,909 / 102,044 / 120,305 / 169,160 /
  +40.6% (D08:786-804); [CBSI]d [74,800] [80,000] [82,000] [81,000] [-1.2%] (D08:806-808); Total
  1,896,495a / 2,104,421c / 2,043,300 / 2,205,179b / +7.9% (D08:810). Notes (D08:812-818):
  rounding; "FY2021, FY2022, and FY2023 totals include $5 million appropriated as voluntary
  contributions to the Organization of American States"; Central America regional program history;
  a = "FY2021 sums include supplemental assistance appropriated in the American Rescue Plan Act of
  2021 (P.L. 117-2)"; b = Amazon Fund $100.0 million not included; c = "FY2022 sums include
  supplemental assistance appropriated in the Additional Ukraine Supplemental Appropriations Act,
  2022 (P.L. 117-128)"; d = CBSI funded through State Western Hemisphere Regional program. Cells
  marked a (FY2021): Bolivia, Brazil, Colombia, Costa Rica, Dominican Republic, Ecuador, El
  Salvador, Guatemala, Haiti, Honduras, Jamaica, Nicaragua, Panama, Paraguay, Peru, Trinidad and
  Tobago, Uruguay, USAID Caribbean Development, Total. Cells marked c (FY2022): Colombia, Dominican
  Republic, Guatemala, Haiti, Honduras, Barbados and Eastern Caribbean, Total.
  Table A-2 "by Account and by Country or Regional Program: FY2023 Estimate", "(millions ...)"
  (D08:820-952): columns DA / ESF / GHP-USAID / GHP-State / INCLE / NADR / IMET / FMF / Total; every
  cell matches D06 A-2 (e.g. Colombia 86.0/144.0/8.8/3.0/150.0/21.0/1.9/38.5 = 453.1, D08:870;
  Honduras DA 126.7, D08:879; Venezuela —/50.0/3.8/3.6 = 57.4, D08:894; [CBSI]b [—][37.0][—][—]
  [35.0][—][—][10.0][82.0], D08:924-926; Total 663.7 / 472.5c / 115.5 / 198.8 / 470.2 / 41.1 /
  12.5 / 69.0 / 2,043.3c, D08:946). Note c: total includes $5.0 million OAS (D08:952). Sources: CBJ
  Supplementary Tables FY2025 and Leahy explanatory statement p. S9299 (D08:948).
  Table A-3 "FY2025 Request", "(millions ...)" (D08:954-1055): Colombia 90.5/128.5/8.8/—/135.0/
  10.0/2.0/38.5 = 413.3 (D08:979); Haiti 46.4/7.0/34.0/100.0/169.0/—/0.3/— = 356.7 (D08:987);
  Honduras 79.5/—/6.0/—/—/—/0.8/— = 86.3 (D08:988); El Salvador DA 81.9, total 87.7 (D08:984);
  Guatemala DA 90.0, total 115.8 (D08:985); Mexico —/54.0/—/—/53.0/1.0/1.7/— = 109.7 (D08:990);
  Venezuela —/50.0/3.8/— = 53.8 (D08:1017); Brazil 29.0/—/6.5/—/—/—/1.0/— = 36.5 (D08:977); USAID
  Central America Regional "24.5 4.5 — — — — — — 29.5" (D08:1029); USAID South America Regional
  52.7/35.0 = 87.7; USAID LAC Regional 37.9/32.0/11.5 = 81.4; State Central America Regional
  —/105.2/—/43.6/129.5/5.0/—/12.5 = 295.8; State Western Hemisphere Regional —/72.8/—/26.4/46.4/
  10.6/—/13.0 = 169.2 (D08:1023-1045); [CBSI]b [—][37.0][—][—][35.0][—][—][9.0][81.0]
  (D08:1047-1049); Total 672.5 / 523.5 / 119.0 / 190.0 / 584.9 / 30.1 / 16.2 / 69.0 / 2,205.2
  (D08:1051). Source: CBJ Supplementary Tables FY2025.
- Country prose (base FY2023 estimate): CBSI $81.0 million, "$1.0 million (1.2%) less than the
  FY2023 estimated allocation and $7 million (8.0%) less than the FY2024 enacted"; CARICOM and the
  Regional Security System ("seven Eastern Caribbean countries and Guyana", fn 15) (D08:433, 445);
  Central America: "$4 billion over four years" (D08:461); FY2025 $632.6 million, "$38.2 million
  (5.7%) less", comprising El Salvador $87.7 million, Guatemala $115.8 million, Honduras $86.3
  million, "a combined $17.1 million for the other four countries", CARSI $232.5 million, other
  regional $93.3 million (D08:463; fn 22 country set D08:473); Colombia $413.3 million, -$39.8
  million (8.8%), "due, in part, to the Colombian government's shift away from coca eradication
  under the administration of President Gustavo Petro (2022-present)" (D08:495); Haiti $356.7
  million, +$125.8 million (54.5%) (D08:519); Mexico $109.7 million, +$5.1 million (4.9%), "largely
  due to a proposed increase in INCLE aid" (D08:549); Venezuela $50.0 million democracy + $3.8
  million GHP; same democracy level as FY2023 and GHP "-$3.6 million (49.0%)"; Maduro
  "(2013-present)", democracy aid increased "over the past seven years" (D08:581-599); IAF $52.0
  million, "currently active in 27" countries (D08:607).
- Congressional action (FY2025, as of January 14, 2025 - not concluded): House Appropriations
  Committee reported H.R. 8771/H.Rept. 118-554 June 14, 2024; House passed June 28, 2024; Senate
  Appropriations Committee reported S. 4797/S.Rept. 118-200 July 25, 2024; "The 118th Congress did
  not take further action on either bill"; CRs P.L. 118-83 and P.L. 118-158 fund programs "at the
  same rate, and under the same conditions and authority, as FY2024 (P.L. 118-47, Division F) from
  October 1, 2024, until March 14, 2025" (D08:29, 195); P.L. 118-158 expires March 14, 2025
  (D08:655). Priority lists: H.R. 8771 §7045(a)(1), 4 bullets (D08:199-207); S. 4797 §7045(a)(1),
  4 bullets (D08:209-217). Authorizations: "Congress has not enacted a comprehensive foreign
  assistance authorization since 1985 (P.L. 99-83)"; SFRC reported S. 841 (CBSI Authorization
  Act), which "would have authorized $82.0 million ... annually in FY2023 through FY2027"; H.R. 1802
  "introduced"; H.R. 3194, H.R. 3599 (D08:657). FY2024 reporting requirements listed (D08:665; fn
  56: P.L. 118-47 §§7036(d)(2), 7045(c)(1), and §7019(e) directing compliance with H.Rept.
  118-146, S.Rept. 118-71 and the explanatory statement, D08:667).
- Proposed conditions (bills, not enacted): Northern Triangle - H.R. 8771 withhold 60% of
  assistance for central governments, "more exceptions ... than SFOPS legislation enacted in prior
  years" (§7045(b)(2)); S. 4797 FMF prohibited except humanitarian assistance and disaster response,
  withhold 60% of ESF and international security assistance "(i.e., INCLE, NADR, IMET, FMF)", new
  30-day consultation before certification (D08:467, 491). "Similar to SFOPS legislation enacted
  each year since FY2016" (D08:467). Colombia - H.R. 8771 restrictions "similar to those enacted in
  annual SFOPS legislation since FY2017", pre-obligation relations report, withhold 30% of INCLE
  (§7045(c)) (D08:499-511); S. 4797 withhold 20% INCLE and 20% FMF (§7045(c)(2)) (D08:515). Haiti
  - H.R. 8771 withhold aid to the central government until certification "by January 1, 2025"
  (§7045(g)(2)-(3)) (D08:541); S. 4797 no armed-forces aid (§7045(e)(3)(B)) and no Prevention and
  Stabilization Fund money for Haiti (§7066), PSF "established by the Global Fragility Act of 2019
  (Title V of Division J of P.L. 116-94)" (D08:545). Mexico - H.R. 8771 no funds until a
  water-delivery agreement under the 1944 treaty is certified (fentanyl exception) and withhold
  30% of security assistance (§7045(h)) (D08:573); S. 4797 withhold 15% (§7045(f)) (D08:577).
  Venezuela - H.R. 8771 withhold "50% of the amount made available to support elections
  programming in FY2024" pending certification on the 2024 elections (§7045(l)); S. 4797 "would not
  place any conditions" (D08:601-603).
- Proposed directives (bills): CBSI H.R. 8771 "not less than" $97.5 million (+$16.5 million,
  20.3% vs request; +$9.5 million, 10.8% vs FY2024 enacted; §7045(k)), above-FY2024 funds
  prioritized for transit-zone countries most affected by the Haiti crisis; H.Rept. 118-554 asks
  State to consider FAA Section 516 (22 U.S.C. §2321j) excess defense articles (D08:435); S. 4797
  "not less than" $88.0 million (+$7 million, 8.6%; same as FY2024; §7045(h)) (D08:437). Central
  America: H.R. 8771 "not less than" $15.0 million DA for democracy programs in Nicaragua
  (§7045(i)); H.Rept. 118-554 $220.0 million INCLE for CARSI incl. $40.0 million for Costa Rica,
  $8.5 million FMF Costa Rica, $2.0 million FMF Panama (D08:465); S. 4797 $100.0 million locally
  led development (Northern Triangle), $70.0 million violence against women and girls, $61.5
  million anti-corruption (§7045(b)(1)); S.Rept. 118-200 $81.9 million DA El Salvador, $90.0
  million DA Guatemala, $79.5 million DA Honduras; "Some of these funding directives may overlap"
  (D08:469-489). Colombia: H.Rept. 118-554 $208.5 million (-$204.8 million, 49.6% vs request;
  -$244.6 million, 54.0% vs FY2023 estimated); no GHP/NADR/IMET levels, "through which Colombia
  received $34.6 million in aid for FY2023"; DA, ESF, INCLE cut 50% vs FY2024 enacted (D08:497); S.
  4797 "not less than" $380.0 million (-$33.3 million, 8.1%; -$73.1 million, 16.1%), INCLE "not
  less than" $40 million rural security; S.Rept. 118-200 $15 million DA biodiversity, $25 million
  ESF Afro-Colombian and Indigenous communities, $15 million ESF human rights (D08:513). Haiti: H.R.
  8771 basic-needs language (§7045(g)(1)); H.Rept. 118-554 $20.0 million ESF for maternal and
  neonatal units "within 10 kilometers of the border with the Dominican Republic" (D08:521); S.
  4797 purposes list, MSS support, coast guard purchases "under the Arms Export Control Act (22
  U.S.C. §§2751 et seq.)"; S.Rept. 118-200 $8.5 million reforestation, $5.0 million prisoners
  (D08:543). Mexico: H.R. 8771 "not less than" $175.0 million global ESF and INCLE for
  counter-fentanyl (§7036); S. 4797 "not less than" $170.0 million (§7036) (D08:551, 575). Venezuela:
  both bills $50 million democracy, no health level; S. 4797 "should be made available" (fn 53)
  (D08:601-603, 615). IAF: H.R. 8771 $22.5 million (-$29.5 million, 56.7% vs request; -$24.5
  million, 52.1% vs FY2024 enacted); S. 4797 fully funds $52.0 million (D08:609, 625).
- Rounded prose beside exact figures (mapper arithmetic, not printed): security shares 26.5 + 1.4
  + 0.7 + 3.1 = 31.7 vs "31.8%" (D08:221); Central America components (D08:463) sum to 632.7 vs
  "$632.6 million"; Venezuela GHP FY2023 (A-2: 3.8 + 3.6 = 7.4) to 3.8 = -3.6, i.e. 48.6% on the
  rounded cells vs printed "49.0%"; A-2/A-3 rounded cells vs A-1 thousands throughout.
- Hedged claims: MRA obligations "may have included appropriations from multiple fiscal years"
  (D08:363); "Some of these funding directives may overlap" (D08:489); House Colombia total "may
  not be comprehensive" (D08:497); Options section "may"/"could" (D08:653-665).
- Internal inconsistencies (record as printed): USAID Central America Regional - A-3 "24.5 4.5
  ... 29.5" (D08:1029) vs A-1 FY2025 "29,950" (D08:788); A-2 "24.5 4.5 ... 30.0" (D08:906) vs A-1
  FY2023 "29,950" (components print 29.0 in both).
- Spot-check: docs lines 277 (Table 1 total row), 411 (Table 2 Colombia row), 495 ("$34.6
  million"), 655 (P.L. 99-83 sentence) and 1027 (A-3 USAID Central America row) identical to text.
- Coverage: FULL - lines 1-1068 read in chunks (1-110, 110-210, 210-290, 290-360, 360-440,
  440-500, 500-560, 560-630, 630-720, 720-809, 809-899, 899-989, 989-1068).

## Shared ground (navigation only)

- Pending completion of D05-D08.

## Gaps

- D05-D08 unread at this checkpoint.
