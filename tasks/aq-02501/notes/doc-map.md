# aq-02501 - document map

Maintained by the caller from `text/` (plain-text captures; no PDFs). Navigation only, like the
form's bundle overview: where things are, not what to ask. Questions quote the documents, never this map.

## Bundle

- What it is: seven unrelated-but-thematic Federal Register texts on veterans' education benefits,
  discharge characterization and DoD personnel data (2022-2026). No editions of one series, no
  proposal/final pair, no document amends another.
- Documents: 7; ids D01-D07 from `text/manifest.json`; Dnn = task page Doc N (file names sort in
  the page's order, verified against notes/intake.json).
- Gaps: none known. Capture `AQ-02501_2026-10-09_1008.txt` says "7 of 7 read in full (399,572
  characters)"; splitter found no Incomplete notes or gap markers (intake.json `incomplete: false`,
  `gap_characters: 0` for all seven). Capture warning: "Docket has been updated. Reload this page..."
  (page-state warning only; documents present).
- Extraction spot-checks (2026-10-09, caller): text captures, so no page counts; each Dnn.txt equals
  its docs/ source plus the header (char counts 39,826-92,868 vs capture 39,827-92,872, header/newline
  normalisation only). Representative tables read in extraction: D05 Tables 1-3 (rows/units intact,
  flattened to single lines), D06 program-eligibility table (flattened). Footnotes intact (D02 n.1-5,
  D03 n.1-6, D04 n.1-9, D05 n.1-50). Federal Register page markers `[[Page N]]` preserved.
- Provenance: notes/intake.json (capture sha256 cca94f34...; per-document source hashes match capture).
- Reuse binding: map written from text/ hashes in text/manifest.json (2026-10-09). Refresh if a hash changes.
- Coverage: caller read all seven texts in full (2026-10-09).

## D01 - DoD DEERS system of records notice (Doc 1)

- Source: docs/fr_2022_11610.txt; 87 FR 32384-32389, published Tue May 31, 2022; dated May 25, 2022.
- Written by: DoD Office of the Secretary; contact Mr. Sam Peterson, DMDC Privacy Officer (L34).
- Type: notice of a modified system of records, DEERS, DMDC 02 DoD. Effective on publication; routine-use
  comments by June 30, 2022, routine uses effective at close of comment period (L27).
- Background: new routine use labelled "(KK)" for GPO in L42, but the list labels GPO use "LL" (L197) and
  "KK" is the breach-assistance use (L192); list skips JJ.
- Routine uses A-II, KK, LL (L124-197). D.6 / G.4: GI Bill programs (MGIB 10 USC 1606 / 38 USC 30, REAP
  1607, National Call to Service 510, Post-9/11 ch. 33, transferability) (L133-147). G.3: ED matching for
  dependent children of members killed in OIF/OEF (L146). F: student loan forgiveness (L141).
- Categories of individuals A-H (L98-108). Retention: optical disks 5 years; DEERS permanent (L206-208).
- History: July 27, 2016 81 FR 49210; Oct 16, 2019 84 FR 55293; corrected Dec 2, 2019 84 FR 65975 (L233).

## D02 - VA 85/15 rule final rule (Doc 2)

- Source: docs/fr_2024_00629.txt; 89 FR 2493-2502, Jan 16, 2024; RIN 2900-AR56; signed by Denis McDonough
  Jan 8, 2024 (L274); contact Thomas Alphonso (L29).
- Dates: effective Feb 15, 2024; applies to terms beginning on or after Jan 16, 2025, incl. waivers pending
  then (L27); NPRM published Oct 12, 2022 (L76, L87); PL 117-174 signed Aug 26, 2022 (L76).
- Definitions: institutional aid, VA aid (chapters 30, 31, 33, 35, 36 of title 38; ch. 1606 of title 10),
  supported / non-supported (L32; final text L298). Four removed (e)(2) categories listed L40.
- Figures: 56 comments (L72); Feb 2023 study 56% non-degree granting (L58); May 25, 2023: 9,247 approved
  institutions, 5,257 with 35% exemptions, "57 percent" (L80); PNPI AY 2015-16 4.9% of undergraduates
  veterans (L125, L203), MSIs 5.1% (L188), for-profit 9.2% (L204), 2021 6.4% of adults (L202); DOJ
  settlements $512,000 / $7.5 Million / over $100 Million (L112); UMRA $100 million (L248).
- Waiver criteria: four -> three (final text L306-310). Reporting: 30 days after each non-standard term (L304).
- Hedges: "presumably a large percentage" exempt (L80); "likely will not significantly increase" (L124).

## D03 - VA character-of-discharge final rule (Doc 3)

- Source: docs/fr_2024_09012.txt; 89 FR 32361-32373, Apr 26, 2024; RIN 2900-AQ95; signed by McDonough
  Apr 23, 2024 (L342); contact Robert Parks (L43).
- Dates: effective June 25, 2024; applies to applications received on/after June 25, 2024 or pending then
  (L40-41); proposal July 10, 2020 85 FR 41471 (L56); RFI Sept 2021; listening session Oct 2021 (L56-57).
- Figures: over 70 comments (proposal), over 45 (RFI), 148 total (L56-57, L91); OTH deemed eligible
  "more than 75%" Oct 1, 2019 - Sep 30, 2022 (L118-122); six statutory bars, five regulatory bars -> four
  (L55, L67); CRA 60-day delay (L334).
- Rules: GI Bill education only for honorable service (L82-86); willful-and-persistent windows 2/2/5 years,
  minor misconduct definition (L206, L397-401); AWOL statutory bar 180 days (L388); compelling-circumstances
  factors (L402-412); DRB upgrades pre/post Oct 8, 1977 (L414-416); one-year claim window (L292-294).

## D04 - ED CEVSS FY2024 notice inviting applications (Doc 4)

- Source: docs/fr_2024_11658.txt; 89 FR 46098-46103, May 28, 2024; signed Nasser H. Paydar (L269).
- Dates: applications available May 28, 2024; transmittal deadline July 29, 2024; intergovernmental review
  Sept 25, 2024 (L24-26).
- Figures: 2019-20 3.7% of undergraduates veterans; veterans' sector shares 28/12/34/13% (L41); completion
  48 vs 56%, 33 vs 59%, 13 vs 17% (L41-42); GI Bill recipients 10 vs 21%, 65% (L48); 15%, 47.3%, 47%, 62% (L59).
- Award: $8,910,000 available; $650,000-$750,000 for up to 36 months; average $700,000; max $750,000;
  12 awards (L154-159). Scoring 100 + up to 12 CPP points = 112 (L91, L191-222). Simplified acquisition
  threshold $250,000 (L236); FAPIIS $10,000,000 (L241). Definitions incl. military- or veteran-connected
  student (L121), underserved student (L133).

## D05 - DoD Discharge Appeal Review Board interim final rule (Doc 5)

- Source: docs/fr_2024_27268.txt; 89 FR 94603-94613, Nov 29, 2024; dated Nov 18, 2024 (L541).
- Dates: effective Nov 29, 2024; comments by Jan 28, 2025 (L30); NDAA FY2020 s.523 codified Dec 20, 2019;
  implementation deadline Jan 1, 2021 (L118, L131); memos Jan 29, 2021 / May 17, 2022; DTM May 5, 2023
  (L154-155); PDBR ceases Oct 1, 2024 (L232); first annual report Oct 1, 2022 with FY 2022 data (L530).
- Rules: DRB within 15 years (L70, L205); BCM/NR 3-year discovery deadline, waivable (L209); DARB
  eligibility four criteria incl. discharge on/after Dec 20, 2019 and less-than-honorable (incl. general)
  (L175-192, L428, L469-472); request within 365 calendar days of BCM/NR decision (L476); SECAF 30 days
  (L509); Secretary 90 days (L516); upgrade effective as of date of discharge (L522). GI Bill limited to
  honorable, general does not qualify (L329).
- Figures: 23,176 BCM/NR upgrade requests Oct 1, 2016 - Sep 30, 2021, 15% fully granted (L214); 4,635/yr,
  3,940 eligible, 75% petition -> 2,955 (L265); 63,294 less-than-honorable active-duty discharges since
  Dec 20, 2019 as of June 30, 2022 (L247); petitioner cost $62.38, text "$6.24 to $69.35" vs Table 1
  "$6.24 to $69.73" (L267-283); Tables 2-3 per-case $325.60 / $4,476.00 / $141.78, 41% mental-health,
  total $14,360,565 (L286-305); alternative #1 $14,455,783 (L311); FY2022 4 requests, none eligible (L262).

## D06 - VA proposed rule, Edith Nourse Rogers STEM Scholarship (Doc 6)

- Source: docs/fr_2026_00634.txt; 91 FR 1726-1732, Jan 15, 2026; RIN 2900-AS38; approved by Douglas A.
  Collins Dec 12, 2025 (L146); contact Thomas Alphonso (L32). Comments by Mar 16, 2026 (L28).
- Statutes: Colmery Act Aug 16, 2017 (s.111 effective Aug 1, 2019); Isakson-Roe Act Jan 5, 2021 (s.1001,
  terms beginning on/after Jan 5, 2021) (L34-41, L93-96).
- Rules: eligibility (3311 entitlement used up or within 180 days; 60 of 120 semester / 90 of 180 quarter
  credit hours) (L45-48, L170-179); program table (L191-205); monthly cohorts selected on the 7th (L72,
  L216-220); begin within six months of selection, use within two years (L82, L208-214); priority before
  and after Jan 5, 2021 (L86-96, L221-234); up to 9 months / $30,000 (L101, L244); caps $25M FY2019,
  $75M FY2020-2022, $100M FY2023+ (L102); funding released Oct 1 each FY, academic year Aug 1 (L82);
  Yellow Ribbon school-only (L110, L249); 48-month cap exclusion, ch. 35 81 months (L118-119, L252).

## D07 - DoD DMDC 01 system of records notice, retitled USHRIS (Doc 7)

- Source: docs/fr_2026_04170.txt; 91 FR 10373-10378, Mar 3, 2026; dated Feb 27, 2026 (L50); contact
  Samuel M. Peterson, DHRA Component Privacy Officer (L36).
- Dates: effective on publication; routine-use comments by Apr 2, 2026 (L27).
- Changes: retitled; DoE ("DoE" = Department of Education here) matching population expanded; PARIS routine
  uses removed (L25, L42). Categories A-S with date ranges (active duty from July 1, 1968; reserve since
  July 1975; AFEES from July 1, 1970; civilians since Jan 1, 1972; VEAP Jan 1977 - June 1985) (L79-100).
- Routine uses A-Z (L124-180), incl. L DVA (6 parts), Y DoE (3 parts). Record sources list both Department
  of Energy and Department of Education contexts (L117 lists "the Department of Energy").
- History: Nov 23, 2011 76 FR 72391; Feb 27, 2019 84 FR 6383; Mar 11, 2019 84 FR 8698; May 27, 2022
  87 FR 32145 (L217).

## Shared ground (navigation only)

- Entities in more than one document: Thomas Alphonso (D02, D06); Denis McDonough (D02, D03); Sam /
  Samuel M. Peterson (D01, D07); Department of Education (D01, D02, D04, D06, D07); Coast Guard and Space
  Force (D03, D05, D07); DRB / BCM-NR, 10 U.S.C. 1552/1553 (D03, D05).
- Periods/series: veterans' share of undergraduates AY 2015-16 (D02) and 2019-20 (D04); FY schedules
  (D06 caps; D05 FY reporting); OTH statistics FY2020-22 (D03) vs BCM/NR FY2017-21 (D05).
- Cross-references: none of the seven documents cites another bundle document. D07's history lists a
  May 27, 2022 DMDC 01 notice four days before D01's DEERS notice (different system).
- Repeated facts: GI Bill requires honorable discharge (D03 L82-86, D05 L329); identical VPEA 1998
  education-notification routine use (D01 L132, D07 L146); "$100 million" UMRA boilerplate (D02, D03,
  D05, D06) beside D06's $100,000,000 cap and D02's DOJ "over $100 Million".
