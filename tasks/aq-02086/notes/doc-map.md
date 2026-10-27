# aq-02086 - document map

Navigation only (2026-10-08, caller read all five texts in full). Questions quote the documents.
Local ids are alphabetical by file name; platform Doc numbers differ (notes/intake.json):
D01 = Doc 4, D02 = Doc 1, D03 = Doc 2, D04 = Doc 3, D05 = Doc 5.

## Bundle

- What it is: five UK (England) housing-policy publications in two strands. Awaab's Law for social
  housing: consultation (Doc 1), consultation-stage impact assessment (Doc 2), government response
  (Doc 3). Decent Homes Standard (DHS) for private renting: consultation (Doc 4), response (Doc 5).
- Gaps: none. Capture "5 of 5 read in full"; every document matches the capture (intake.json,
  gap_characters 0). Plain-text capture, no pages; extraction = capture text.
- Extraction spot-checks: each D0n.txt equals its docs/ file (manifest hashes = intake hashes);
  tables checked: Doc 3 response tables, Doc 5 Annex A tables, Doc 4 Table 1/2; footnotes present
  at document ends (Doc 1 fn 1-31, Doc 2 fn 1-24, Doc 4 fn 1-11, Doc 5 fn 1).
- Reuse binding: source sha256 in text/manifest.json (D01 ca2a226e, D02 defb89eb, D03 c3c6f068,
  D04 44ed077b, D05 eac0d865).

## Doc 1 (D02) - Awaab's Law consultation, DLUHC, 8 weeks from 9 January 2024

- Proposals: investigate within 14 calendar days; written summary within 48 hours of the
  investigation (Proposal 2 also says within 14 days of awareness); begin repairs within 7 calendar
  days of the summary; complete in a reasonable period; emergencies within 24 hours; decant; records.
- Access example L653: enters day 16, summary within 48 hours, work begun "by day 23".
- Scenarios: Joe (reported 17 August 2023), Lucy (1 September 2023).
- Annex B L901-987: worked hazard examples with headings (emergency / significant risk / routine)
  and HHSRS type in brackets: 2.1(a) entry by intruders (emergency), 2.1(b) water supply (emergency),
  2.2(a) domestic hygiene, pests and refuse (significant), 2.2(b) entry by intruders (significant),
  2.3(a) water supply and 2.3(b) falling on stairs (routine). L98 and L102 hold further unlabelled
  examples (a broken window needing insulation within 7 days).
- HHSRS list of 29 hazards L385-415; review proposed 29 -> 21 (L417).
- Stats: non-decent social 759,000 (20%) 2010 -> 380,000 (10%) 2021 (L34, L239); 164,000 (4%)
  social homes with a category 1 hazard (L247); BRE 217,000 homes, NHS GBP 65m (L34, L291); damp
  2021 935,000 homes (4%), tenure rates 4% social / 11% PRS / 2% owner-occupied (L275).
- Housing Ombudsman damp/mould/leak complaints: 1,993 (2020-21), 3,530 (2021-22), 5,460 (2022-23 as
  of 16 Oct 2023) (L283); 5,398 in calendar 2022 (L293).
- Costs restated from Doc 2 (L693-727): PV GBP 1.6m familiarisation, PV GBP 154.5m summaries; GBP
  10.3m PRP + GBP 5.1m LARP = GBP 15.4m a year; 6% switching value; 10 fatalities; 40% urgent faults.
- Glossary L1047: RBH, "housing society, with 12,000 homes throughout Rochdale", the Ishak family's
  landlord. Footnote 12 L1115: BRE damp and mould hazards cost the NHS GBP 38m a year, GBP 269m to
  mitigate.

## Doc 2 (D03) - consultation-stage impact assessment, dated 9 January 2024

- Summary: 2019 prices, 2020 PV; NPSV -131.4m, BNPV -87.6m, GBP 10.2m a year net cost to business;
  analysis page: transition 1.6, average annual 17.9, total cost PV 156.0 (L111-154).
- Familiarisation L451-462: 12-18 pages (midpoint 15), 1 h read + 1 h understand per 20 pages; 10
  staff at small and 100 at large RPs; 234 large / 1,162 small PRPs, 163 large / 86 small LARPs;
  GBP 22.26/h; GBP 700k + 347k = 1.05m PRP; GBP 513k LA; GBP 1.56m.
- Written summaries L474-484: 15 minutes of staff time per report, GBP 18.57/h -> GBP 4.16; 53% by
  post, GBP 1.14 postage; Housemark 3 to 4 repairs, survey 4.2, IA uses 4 per property a year; 40%
  urgent proxy; 3.14m PRP and 1.57m LARP dwellings -> 5.0m and 2.5m reports; only 50% additional;
  GBP 10.3m + 5.1m = 15.4m. Net impact GBP 10.4m PRP and 5.2m LA per year (L448).
- Switching L519-570: 26.1-day average completion, 21-day maximum, 5.1-day gain; GBP 4.22, 7.55,
  4.42 per repair; 6% (1.1 million repairs); GBP 1.9m per fatality, 10 a year. Table 1 L654-698.
- Dates: amendment tabled 9 February 2023, Royal Assent 20 July 2023, in force "by Autumn 2024" (L405,
  L409). BRE: 75,000 homes with the most serious dampness in 2018, GBP 38m NHS (L624); GBP 1.4bn,
  GBP 18.5bn society, GBP 857m cold, GBP 219m stairs (L620-623).

## Doc 3 (D04) - Awaab's Law government response (Angela Rayner foreword), 2025

- Consultation 9 January - 5 March 2024, 1,028 responses (table L98-112). Yes/no tables give counts of
  all 1,028 incl. "Not Answered"; percentages are of 1,028. Q4 counts sum to 1,018 vs stated 1,015;
  Q20 prose says 86% beside the table's 90%.
- Final rules: investigate within 10 working days (report day = day zero); summary within 3 working
  days of the investigation; make safe within 5 working days; begin or take steps within 5 working
  days and physically start within 12 weeks; emergencies 24 hours; alternative accommodation.
- Phases L64-68, L176-180, Annex A L610-613: from 27 October 2025 damp and mould significant hazards
  and all emergency hazards; 2026 cold/heat, falls, structural collapse, fire, electrical/explosions,
  hygiene (13 types); 2027 the rest except overcrowding (14 types, "Ergonomics" = Doc 1's "Position and
  operability of amenities").
- Final IA: GBP 30-80 per dwelling staff cost (midpoint GBP 55); GBP 14.6m a year over 10 years.

## Doc 4 (D01) - DHS in the private rented sector consultation, 2 September - 14 October 2022

- PRS substandard 37.2% (2010) -> 21.0% (2020) (L235, L259); social 39% (2001) -> 13% (2020) (L259);
  "21% of properties that currently do not meet the Standard" (L924); 4.4m private renting
  households; NHS GBP 340m (PRS); GBP 1.4bn / 18.6bn (BRE 2021); GBP 9.3bn rent, GBP 3bn housing benefit.
- Levelling Up aim: halve substandard rented homes by 2030 (L235). Criteria A-D; Table 1 component
  lifetimes, Table 2 poor condition. Penalties up to GBP 30,000. Grace 6/12/18 months; phasing at
  12-month intervals.

## Doc 5 (D05) - response to the DHS consultation (Renters' Rights Bill), 2025

- Social non-decent 38% (2001) -> 10% (2023); PRS 21% non-decent in 2023 (L24). 1,032 responses =
  1,021 logged + 11 written; Shelter survey 251, Generation Rent 369. Immediate penalties up to GBP 7,000.
- Annex A tables Q1-Q62 with counts of 1,021; Annex B responding organisations (incl. Shelter, BRE).

## Shared ground and conflicts

- Awaab timescales: proposal (Docs 1, 2) vs final (Doc 3). Cost estimates: Doc 2 vs Doc 3 final IA.
- Non-decency series across Docs 1, 4, 5 (2001 social 39% vs 38%; PRS 2020 and 2023 both 21%).
- BRE: GBP 18.5bn (Doc 2) vs GBP 18.6bn (Doc 4); damp GBP 38m in Docs 1 and 2 (count in Doc 2,
  mitigation cost in Doc 1 footnote).
- RBH named in Docs 1, 2, 3; its stock only in Doc 1's glossary.
