# aq-04421 - document map

Navigation only (like the form's bundle overview); questions quote `text/Dnn.txt`, never this map.
Reused from tasks/aq-02447 (same six documents: every `source_sha256` in notes/intake.json equals
aq-02447's, and the document sections of the two captures are identical line for line). The sections
D01-D06 and "Shared ground" below are aq-02447's map of 2026-10-09, unchanged. The section "Added
2026-10-13" is this session's.

## Bundle

- What it is: AQ-04421 "Semiconductor Export Control Filings" (Public policy), six Federal Register
  texts: five BIS (Commerce) export-control rules, Jan 2023 to Jul 2026, plus one unrelated EPA TSCA
  significant-new-use rule (May 2026). No proposal/final pairs, no editions of one series.
- Documents: 6; local ids = page Doc numbers (D01 = Doc 1 ... D06 = Doc 6; `notes/intake.json`).
- Gaps: none. Capture `AQ-04421_2026-10-13_1946.txt` says "6 of 6 read in full (403,368 characters)";
  intake records `incomplete: false`, `gap_characters: 0` for all six. Plain-text sources, no pages,
  charts or scans. The capture carried the page's "Docket has been updated. Reload" note.
- Extraction spot-checks (2026-10-13): text/Dnn.txt = docs/ bytes plus the `# Dnn` header (character
  counts 56,311 / 63,329 / 59,618 / 73,949 / 116,915 / 33,252 match the splitter's). Tables are
  flattened FR column text: D03 Supp. 7 interleaves the item column with the address column (L485
  "Corporation--HFab 2, 668 3B001.e, 3B001.f, Guoshoujing Road,"); D04 Entity List rows read in full.
  Footnotes 3 and 4 (D04 L1167-1168) and 1 to 5 (D06 L168-172) present.
- Source hashes (sha256, docs): D01 77c86372...; D02 59664232...; D03 40a5a47b...; D04 c0557904...;
  D05 9e812457...; D06 9513f06f... (text/manifest.json).
- Coverage this session (2026-10-13, caller): D01, D02, D03, D04 and D06 read line by line again.
  D05 read L1-264 (preamble, statutory reviews, list of the 35 sections); L265-896 (the SNUR
  regulatory text) not re-read this session, covered by aq-02447's full read. D05 is used by no sketch.

## D01 - BIS interim final rule: Macau added to the Oct 7, 2022 advanced computing/SME controls

- 88 FR 2821-2829, Jan 18, 2023 (FR Doc 2023-00888); effective Jan 17, 2023; comments due Jan 31, 2023.
- Oct 7 rule: displayed Oct 7, 2022, published Oct 13, 2022 at 87 FR 62186; its comment period
  (originally Dec 12, 2022) extended to Jan 31, 2023 by 87 FR 74966 (Dec 7, 2022) (L49-55).
- Macau added to RS control paragraph of seven ECCNs: 3A090, 3B090, 3D001, 3E001, 4A090, 4D090,
  4E001 (L67); 740.2(a)(9); 742.6(a)(6), (b)(10); 734.9(h),(i) FDP rules; 744.6(c)(2)(i)-(ix) and
  (e)(3); 744.23(a)(2)(i)-(v) and (d); General Order No. 4 TGL (Oct 21, 2022 - Apr 7, 2023).
  Section lettering skips C (A, B, D, E).
- Review standards: presumption of denial, but case-by-case for end users in China/Macau
  headquartered in the U.S. or a Country Group A:5 or A:6 country (742.6(b)(10) L233; 744.6(e)(3)
  L272; 744.23(d) L290).
- Savings clause: on dock/en route Jan 17, 2023; exported "before February 16, 2023" / "before
  midnight, on February 16, 2023" (L86).
- PRA (L93-96): 0694-0088 "Multi-Purpose Application" 29.4 minutes; 0694-0096 less than 1 minute;
  0607-0152 3 minutes; "does not anticipate any changes".
- CCL text: 3A090.a (600 Gbyte/s; 4800 bits x TOPS; L331-352); 4E001.b.1 APP > 15 WT; TSR/STA
  limits at 29 WT; STA bars for A:6 (3D001) and A:5 or A:6 (3E001, 4E001) (L425, L467, L569).
- Authority citations: part 742 and part 746 elsewhere cite "Sec. 1503, Pub. L. 108-11, 117 Stat.
  559" (D01 L219; also D02 L419, D06 L251); no document explains Pub. L. 108-11.

## D02 - BIS final rule: EAR end-user controls for SDN List persons (744.8 consolidation)

- 89 FR 20107-20116, Mar 21, 2024; effective Mar 21, 2024.
- 14 OFAC programs: 11 identifiers newly added to 744.8 (7 Russia/Belarus, 4 narcotics/criminal),
  3 continued (FTO, SDGT, NPWMD); before: 2 programs not subject at all (ILLICIT DRUGS-EO14059,
  TCO); the "eleven new" list at L151-153 prints ten (omits BELARUS-EO14038); Table 2 has 11 rows.
- Estimated new license applications: +5 a year (Russia/Belarus identifiers, L106-108), +15 a year
  (narcotics/criminal, L125); PRA (L295): 0694-0088 "Multi-Purpose Application" 29.6 minutes;
  0694-0096 less than one minute; 0607-0152 three minutes; "increasing the estimated number of
  submissions by twenty".
- Removes/reserves 744.10, 744.12, 744.13, 744.14, 744.18, 744.20 (six sections, L241, L412);
  740.2(a)(22) removed; 746.10(a)(2) revised. E.O. 12947 (Jan 23, 1995) revoked Sep 9, 2019.
- Savings clause: en route Mar 21, 2024; completed "no later than on April 22, 2024" (L284).
- 744.1(a)(1) intro rewritten (L343-349): 744.21 countries, 744.22 countries, 744.23 description.

## D03 - BIS final rule: Data Center Validated End User authorization (748.15 rewrite)

- 89 FR 80080-80093, Oct 2, 2024; effective Oct 2, 2024.
- Cites Oct 2022 (87 FR 62186) and Oct 2023 (88 FR 73424, 88 FR 73458) controls; Oct 2023 scope
  D:1, D:4, D:5 for advanced computing; worldwide end-use license for entities headquartered in
  Macau or D:5 (L43-47).
- General VEU: China, India; Data Center VEU: any destination needing a license for 3A090, 4A090,
  .z items, except D:5 (748.15(b), L152-155). Reports: General annual (Feb 15); Data Center
  semiannual (Jul 15 for Jan 1-Jun 30; Jan 15 for "June 30 to December 31") (L174-191).
- PRA (L116): 0694-0088 "Simplified Network Application Processing System", includes license
  applications, 29.4 minutes, total burden 33,133 hours; license applications "expected to be ten".
- Supp. 7 VEU list (L203-520): China - AMD China (3 sites), Advanced Micro-Fabrication Equipment,
  Applied Materials China (depots), Boeing Tianjin Composites, CSMC, Intel Dalian (4E001 limited to
  APP <= 12.0 WT), Lam Research Service, Samsung China Semiconductor (Xi'an, NAND), Shanghai Huahong
  Grace (3 fabs), SK hynix China (Wuxi, DRAM); India - GE India Industrial. Samsung and SK hynix
  "Excluded from 744.6(c)(2)(i-iii) and 744.23(a)(1)(iii) and (a)(2)(iii)".
- Supp. 8: part A (7 items, both VEU types), part B (10 data-center items) (L527-566).

## D04 - BIS final rule: Additions and Revisions to the Entity List

- 90 FR 44496-44511, Sep 16, 2025; effective Sep 12, 2025.
- "adding 32 entities": China (23), India (1), Iran (1), Singapore (1), Taiwan (1), Turkey (3),
  UAE (2) (L28). Entries, not organizations: Shanghai Fudan Microelectronics (HK) is listed under
  China, Singapore and Taiwan; Smart Mail Services under Iran and UAE (29 distinct organizations).
- Footnote 4 (734.9(e)(2)): Shanghai Fudan Microelectronics, Sino IC Technology. Footnote 3
  (734.9(g), Russian Procurement Entities): Atempo, EB Teknoloji (new), plus existing entries.
- One revision: Intertech Rus LLC, two addresses removed (Russia). 27 corrections: Belarus 3,
  China 11, Iran 1, Pakistan 1, Russia 9, Turkey 2 (L113-139), each with "first added" date.
- UAE entities: HAS General Trading LLC; Smart Mail Services (Ardakani network; OFAC designated
  Ardakani Dec 19, 2023). Turkey: Atempo, Dentun Elektronik, EB Teknoloji (policy of denial).
- Savings clause: en route Sep 12, 2025; completed "no later than on October 14, 2025" (L143).
- PRA (L158): 0694-0088 SNAP named; no per-submission estimate; no change anticipated.
- ERC: Commerce (Chair), State, Defense, Energy, Treasury where appropriate; majority vote to add,
  unanimous to remove or modify (L42).

## D05 - EPA final rule: Significant New Use Rules on Certain Chemical Substances (25-2.5e)

- 91 FR 31962-31979, May 29, 2026; effective Jul 28, 2026; promulgated Jun 12, 2026 (1 p.m.);
  proposed Nov 3, 2025 (90 FR 49180) = ongoing-use cutoff; signed May 26, 2026.
- 35 SNURs, 40 CFR 721.12184-721.12218 (L210-247). Eight photolithography substances exempt once
  "adhered (during photolithographic processes) onto a semiconductor wafer surface": 721.12209,
  12210, 12213, 12214, 12215, 12216, 12217, 12218; manufacture-duration limits 18 months
  (12209, 12210, 12215) or 9 months (12213, 12214, 12216, 12217, 12218).
- Costs (L70-72, L155-157): SNUN $45,000 large / $14,500 small, including user fee $37,000 /
  $6,480; export notification about $106 each (one-time per country). SNUNs received: FY2020 7,
  FY2021 9, FY2022 9, FY2023 23, FY2024 7. Burden 30-170 hours per SNUN (OMB 2070-0038).
  UMRA: $100 million (1995 dollars) = $183 million (2023 dollars).
- No link to BIS documents beyond exports and semiconductor wafers.

## D06 - BIS final rule: Enhanced Favorable Treatment for the UAE

- 91 FR 43034-43039, Jul 14, 2026; effective Jul 10, 2026 (filed 7-10-26). Post-cutoff content.
- UAE removed from D:3 and D:4, added to A:5; before: Country Group B plus D:3, D:4 (L54).
  New 740.2(a)(26) (STA only for approved UAE entities); 742.6(a)(6)(iii)(B) revised; ECCN
  country charts revised in 17 ECCNs (L276).
- Enforcement (L81): advanced computing license enforced only to D:1, D:4, D:5 (excluding A:5/A:6)
  and entities headquartered in D:5 or Macau; still enforced for the UAE except approved entities.
- Supp. 8 to part 740: UAE government agencies; G42 and Core42 (advanced computing only; expire
  Apr 6, 2027 absent notice); eight U.S.-headquartered AI companies (Amazon, Apple, Google, Meta,
  Microsoft, OpenAI, Oracle, X.AI). Advisory opinion: determination within 30 days, notice within 5.
- PRA (L103-105): about 50 fewer license applications a year, 25 fewer burden hours, $950 savings
  (0694-0088); 0694-0088 SNAP 29.7 minutes; 0694-0137 1.5 hours; 0694-0096 < 1 minute; 0607-0152
  3 minutes. Dated background: Sep 2024 Major Defense Partner; May 2025 technology deal; guidance
  May 13, 2025 and May 31, 2026; MTCR-type missile range 300 km.

## Shared ground (navigation only)

- OMB 0694-0088 per-submission burden: D01 29.4 ("Multi-Purpose Application"), D02 29.6 (same
  title), D03 29.4 (SNAP title, total 33,133 h), D04 no figure (SNAP), D06 29.7 (SNAP). Application
  count changes: D02 +20 (5 + 15), D03 "ten", D06 about -50 (-25 h, -$950). 0694-0096/0607-0152
  identical in D01, D02, D06.
- Country Groups: D01 A:5/A:6 headquarters exception; D03 D:1/D:4/D:5 and Data Center VEU
  eligibility (not D:5); D06 moves UAE from D:3/D:4 to A:5.
- Macau: D01 (whole rule), D03 L47 and D06 L81 (headquartered-in-Macau end-use scope).
- UAE: D04 Entity List entries (HAS General Trading, Smart Mail Services); D06 whole rule.
- Entity List: D01 (Oct 7 rule entities), D02 (Note 2 precedence over 744.8), D04 (additions);
  D04 rows for Harbin Institute of Technology and Northwestern Polytechnical University cite
  "87 FR 62202, 10/13/22" (the Oct 7 rule's publication date per D01/D03).
- 744.6(c)(2)(i)-(iii) and 744.23(a)(2)(iii): text in D01; VEU exclusions in D03 Supp. 7.
- 748.3(c) advisory opinions: D03 (VEU requests) and D06 (UAE approvals).
- Savings clauses: D01 (Jan 17 -> Feb 16, 2023), D02 (Mar 21 -> Apr 22, 2024), D04 (Sep 12 ->
  Oct 14, 2025); none in D03, D06.

## Added 2026-10-13 (this session; navigation only)

- UAE parties: only D04 and D06 mention the UAE at all (grep, all six texts). D04: HAS General
  Trading LLC (L58, table L1147; Dubai) and Smart Mail Services (L55, table L1155; Dubai, also listed
  under Iran L931). D06: Group 42 Holding Ltd d/b/a G42 incl. G42 Cloud Technology LLC and Core42
  Technology Projects LLC (table L191-197, named nowhere in the preamble, which says "two UAE-based
  AI companies", L83); MGX, one prose sentence (L87, favourable licence review only).
- D06 Supp. 8: table (b) Authorization for G42/Core42 is advanced computing items only; table (c)
  (eight U.S. companies) adds "License Exception STA". Note 1 to paragraph (b) (L200-201) says an
  entity in table (b) "may receive an item under License Exception STA at any of their addresses":
  it reads against the Authorization column, so any ask about who may use STA has two readings.
- D04 table, review policy column: 28 added entries "Presumption of denial"; Atempo, Dentun, EB
  Teknoloji "Policy of denial"; Aerospace Information Research Institute may use License Exception GOV
  (L273-278). Footnote 3 (734.9(g)) on 14 rows: Allchips, Furuida, Onstar (China); Perm Powder Plant,
  ODK-Klimov, Analytical Manufactory, Eluent, Medstandart, Rusmedtorg, Volgogradpromproyekt, UEC-Ufa
  (Russia); Atempo, Biopharmist, EB Teknoloji (Turkey). The preamble names only the two new ones.
  Rows citing 744.21(b): the eight Russia rows and Biopharmist. Preamble/table disagree on AHD
  International (first added March 22, 2018 vs "88 FR 66273, 9/27/23") and CETC 52nd (Dec 21 vs 12/17/21).
- Roads shared by D03's validated end-user sites and D04's entries (every D03 road name searched in
  D04): Guoshoujing Road, Shanghai (D03 L485 Shanghai Huahong Grace HFab 2, No. 668; D04 L891 Sino IC
  Technology, No. 351, an added entry); Fei La / Feila Road, Shanghai free trade zone (D03 L374 Lam's
  WGQ bonded warehouse, No. 55; D04 L641 Jicun Semiconductor, No. 45, an added entry; spelled two
  ways); Bi Bo Road, Shanghai (D03 L429-430 Lam Research Service (Shanghai), No. 177, split across
  lines; D04 L608 Hexin Xingtong, No. 912, a corrected entry). No other match.
- Savings clauses differ in wording: D01 L86 lists four states ("on dock for loading, on lighter,
  laden aboard an exporting carrier, or en route aboard a carrier to a port of export") and no order
  condition; D02 L284 and D04 L143 give only "en route aboard a carrier to a port" and add "pursuant
  to actual orders".
- D03 Supp. 7: all eleven entries are VEU type "General"; none is a Data Center VEU.
- Effective vs publication: D01 Jan 17 / Jan 18, 2023; D02 Mar 21 / Mar 21, 2024; D03 Oct 2 / Oct 2,
  2024; D04 Sep 12 / Sep 16, 2025; D05 Jul 28 / May 29, 2026; D06 Jul 10 / Jul 14, 2026.
