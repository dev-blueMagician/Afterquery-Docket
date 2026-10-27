# aq-02770 - document map

Maintained by the caller from `text/` (line numbers are `text/Dnn.txt` lines; "ch" = character offset in
`docs/`). Navigation only: where things are, not what to ask. Questions quote the documents, never this map.

## Bundle

- What it is: seven DOE (EERE) Federal Register documents, 2022-2026, bundle title "Furnace Energy
  Conservation Rulemaking". Four are one story about commercial warm air furnaces (CWAFs): the 2022
  no-amendment standards determination (D02) and the TE2 test-procedure sequence (D03 tentative, D04 final,
  D05 proposed rescission). D01 is consumer furnaces, D06 a certification rule voided by Congress, D07 a
  2026 request for information on analytic methods.
- Documents: 7; local ids equal the task page's Doc numbers (D01 = Doc 1 ... D07 = Doc 7), per notes/intake.json.
- Gaps: none known. Capture says "7 of 7 read in full (445,616 characters)"; every document `incomplete: false`.
  Capture note carried forward: the page said "Docket has been updated. Reload this page so its checks and
  buttons keep working" (a reload warning on the saved page, not a document gap).
- Extraction spot-checks: plain-text sources, so no page count. Checked per document against `docs/`: header
  block (FR volume, date, pages, FR Doc No), one table (D01 Table II.1, D02 Table II.1, D04 Table I.1, D06
  Table 1 to paragraph (d) and Table 2, D07 Table 1) and one footnote (D01 fn 11, D02 fn 5, D03 fn 3/4, D04
  fn 3, D05 fn 2, D06 fn 3, D07 fn 31). Tables are flattened dot-leader rows; multi-line cells run together
  (D06 Table II.1 and Table 2 interleave columns, read with care). Characters: text = docs + 32-char header line.
- Provenance: notes/intake.json (capture sha256 9154ac35...; all seven `matches_capture: true`).
- Reuse binding: text/manifest.json sha256 per document (D01 3a543030, D02 f7e86639, D03 60e0b7d1,
  D04 e5ffacea, D05 26bc6e14, D06 e6ec6f1c, D07 fb9bf1c3).
- Read coverage (caller, 2026-10-10): D01-D05 and D07 read in full. D06 read in full except lines 596-689
  (product-specific certification text for water heaters, ice makers, walk-ins, pumps, portable ACs, small
  three-phase equipment), skimmed at 260 characters per line and keyword-searched (no furnace content).

## D01 - Consumer furnaces: preliminary TSD notice (87 FR 73259, Nov 29, 2022)

- Written by: DOE, Office of Energy Efficiency and Renewable Energy (EERE). Signed Nov 21, 2022 (Moreno).
- Type: notification of availability of preliminary technical support document; docket EERE-2021-BT-STD-0031.
- Dates (l.38-40): comments by January 30, 2023; webinar Monday, December 19, 2022, 1:00-4:00 p.m.
- Classes: NWOF, MHOF, WGF, WOF, EF (five subject classes); seven consumer classes in all (fn 10, l.239).
- Statute (l.93-95): 6 years after a final rule; three years after a determination not to amend.
  Rebuttable presumption: added cost under three times first-year savings (l.170). Anti-backsliding (l.177).
- Process deviation (l.193-201): no framework document; pre-NOPR comment period "not less than 75 calendar
  days" under appendix A sec. 6(d)(2), DOE gives "a 60-day comment period"; January 2022 RFI (Jan 28, 2022,
  87 FR 4513) had "a 31-day comment period"; NWGF/MHGF NOPR July 7, 2022 (fn 6).
- Standards history (l.211-235): original 75 percent AFUE mobile home, 78 percent others; "small" under
  45,000 Btu per hour; Nov 17, 1989 rule; Nov 19, 2007 rule (NWGF 80, WGF 81, MHGF 80, NWOF 82; compliance
  Nov 19, 2015); June 27, 2011 DFR (NWGF/MHGF 80 national, 90 Northern Region; NWOF 83; compliance May 1,
  2013 non-weatherized, January 1, 2015 weatherized); 2014 vacatur for NWGF/MHGF; Second Circuit remand 2009.
- Tables: II.1 current AFUE (l.241-247): NWOF 83, MHOF 75, WGF 81, WOF 78, EF 78. II.2 standby/off watts
  (l.249-252): NWOF 11/11, EF 10/10. Table I.1 EPCA requirement vs analysis (l.129-168).
- Not analysed (l.260, fn 11 l.293): AFUE for WOFs (no models) and EFs (near 100 percent); standby for WGF/WOF.
- National impact (l.327-336): furnaces "sold from 2030 through 2059"; 1.15 quads FFC at max-tech, 0.96 quads
  at Efficiency Level 1. Five screening criteria (l.278-284).
- Coverage: full.

## D02 - CWAF energy conservation standards: final determination (87 FR 78821, Dec 23, 2022)

- Written by: DOE EERE; signed Dec 16, 2022 (Moreno); docket EERE-2019-BT-STD-0042. Effective January 23, 2023.
- Decision: standards not amended (no clear and convincing evidence of economic justification); six-year lookback.
- Statute (l.104-116): 180 days, 18 months, 30 months after an ASHRAE 90.1 change; every six years; three
  years after a determination not to amend.
- Standards (l.120-137, ch 14,500-18,000): October 2004 rule, TE 80 percent gas-fired, 81 percent oil-fired;
  January 2016 rule, compliance January 1, 2023: gas-fired 81, oil-fired 82. Sentence set at l.135-136 gives
  all four class/date levels. fn 5 (l.130-131): ASHRAE 90.1-2019 Table 6.8.1-5 prints 80 percent for
  oil-fired before January 1, 2023 (DOE reads it as a typo for 81); 82 after.
- History: May 12, 2020 RFI (85 FR 27941); April 26, 2022 NOPD (87 FR 24455); February 25, 2022 test
  procedure NOPR proposing TE2 as optional (l.168).
- Commenters, Table II.1 (l.142-150): AHRI; AGA and APGA; Joint Advocates (ASAP, ACEEE, NYSERDA, NRDC); CA
  IOUs; Lennox; NEEA. Docket numbers in text: AHRI 29, Lennox 30, Joint Advocates 31, CA IOUs 32, NEEA 34.
  Support: AHRI, CA IOUs, Lennox (l.187-188). NEEA disagreed (l.188-189). AGA/APGA stance not described.
- Scope (l.206-224): CWAF = rated maximum input of 225,000 Btu per hour or more; three-phase furnaces under
  225,000 Btu/h "roughly 2 percent" of the market, not covered; Lennox: no new standard before 2029 (l.188).
- Findings (l.234-248): condensing standard "92-percent thermal efficiency" = 2.1 quads primary energy,
  2019 through 2048; TSL 5; 7-percent discount rate; one oil-fired model line above the 2016 levels (CCMS
  accessed Sept. 14, 2022).
- Small business (l.269-276): NAICS 333415, 1,250 employees; eight manufacturers, one small domestic.
- UMRA: Public Law 104-4, $100 million (l.307-310). Peer review: "December 2021 NAS report" (l.342).
- Coverage: full.

## D03 - CWAF TE2: notification of tentative determination (89 FR 104859, Dec 26, 2024)

- Written by: DOE EERE; signed Dec 13, 2024 (Marootian); docket EERE-2024-BT-DET-0012.
- Dates: comments "no later than January 8, 2025" (l.28).
- Statute (l.81-85): seven-year test procedure lookback; ASHRAE trigger; proposals need not less than 45 days.
- Background (l.102-120): May 5, 2020 RFI (85 FR 26626); February 25, 2022 NOPR, 60-day comment period,
  webinar March 29, 2022; ASHRAE 90.1-2022 released January 2023 (ANSI Z21.47-2021 gas, UL 727-2018 oil);
  June 2, 2023 final rule (88 FR 36217); AHRI petition August 1, 2023; Fourth Circuit remand February 6, 2024.
- Estimates (all past ch 27,000): TE2 "between 3.5 percent lower ... to 1 percent higher" (l.144); gas
  minimum "from 80 to 81 percent" and $284 average life-cycle saving (l.144); ASHRAE jacket loss limit 0.75
  percent of input rating (l.150); fn 3 (l.155) 95% of gas-fired CWAFs outdoors; jacket loss factor 3.3,
  "nearly 2.5 percent" (l.158); reduced input rate "as much as 2 percent higher or lower", TE2 "1 percent
  higher or lower", "weighting of 50 percent" (l.164-168); 81 percent TE gives 77.5 to 82 percent (l.176).
- Hedges: estimates are "could"/"can be as much as"; the determination itself is "tentatively determined".
- Coverage: full.

## D04 - CWAF TE2: final determination (90 FR 5560, Jan 17, 2025)

- Written by: DOE EERE; signed Jan 13, 2025 (Marootian); same docket as D03.
- Dates: "The effective date of July 3, 2023, for the TE2 test procedure is confirmed" (l.28).
- Reprints D03's authority/background sections nearly word for word (l.60-116), adding a variable-speed
  passage (l.86-87, "40% capacity") and the not-enforce commitment (l.111-115).
- Commenters, Table I.1 (l.119-130): Ravnitzky 2; AHRI 6; ASAP and NEEA "Joint Commenters" 7; Trane 8; JCI 9;
  Daikin 10 (text spells "Daiken" and once cites "No. 9", l.186).
- Comment period (l.163-179): 45-day minimum does not apply; NHTSA example 60 days, over 260 pages; "7-page"
  notice; "over 4 percent difference" (l.174); posted December 13, 2024; published December 26, 2024 "with a
  14-day comment period that ended on January 8, 2025"; "4 weeks" in total.
- Estimates (past ch 26,000): "as much as a 4.5 percent difference" (l.184-186); 80 to 81 and $284 (l.184);
  81 percent gives 77.5 to 82 (l.143, l.193); "50 percent weighting at full load and part load" (l.187);
  NEEA modeling "70 percent of the time at full load (and 30 percent ... part load)" to "25 percent ... full
  load (and 75 percent at part load)", warehouses over 50 percent full load, retail under (l.187-188); jacket
  losses "as much as a 2.5 percent difference" (l.189).
- Not in D04: the 0.75 percent limit, the 3.3 factor, the 2 percent reduced-rate figure, the 95% outdoor share.
- Coverage: full.

## D05 - CWAF test procedure: proposed rescission of Appendix B (90 FR 20909, May 16, 2025)

- Written by: DOE EERE; signed May 9, 2025 by Chris Wright, Secretary of Energy; docket EERE-2025-BT-TP-0035.
- Dates (l.28-30): comments on or before July 15, 2025; webinar Thursday, May 29, 2025, 1:00-4:00 p.m.
- Background (l.109-112): June 2, 2023 rule made Appendix A current for CWAFs "manufactured on and after May
  28, 2024"; Appendix B not required until TE2-based standards; petition, remand, January 17, 2025 determination.
- Proposal (l.116-118): remove "Thermal efficiency two" definition and Appendix B; DOE "overestimated the
  impacts of jacket losses and part-load operation" and "underestimated the burdens". Cites the procedure as
  "10 CFR part 430, subpart D" in prose (l.110, l.116) but amends part 431 (l.261-284).
- No efficiency figures. UMRA Public Law 104-4, $100 million (l.160-166). E.O. 14154, 14192 (l.197-198).
- Coverage: full.

## D06 - Certification, labeling and enforcement: CRA revocation final rule (90 FR 43371, Sept 9, 2025)

- Written by: DOE EERE; signed Sept 4, 2025 (Hrkman); docket EERE-2023-BT-CE-0001. Effective September 9, 2025.
- Events (l.79-83): October 9, 2024 final rule (89 FR 81994), effective December 23, 2024, first reports May
  7, 2025; H.J.Res. 42 introduced February 12, 2025, House March 5, Senate April 30, to the President May 6,
  signed May 9, 2025 (Pub. L. 119-8).
- Table II.1 (l.90-212): rescinded changes by product (CAC/HP, dishwashers, clothes washers, pool heaters,
  dehumidifiers, EPSs, battery chargers, CRACs, DX-DOASes, three-phase under 65,000 Btu/h ACUAC/ACUHP/VRF, CWH,
  ACIM, walk-ins, pumps, portable ACs, compressors, DPPPMs, air cleaners, SPVUs, CFLKs). No furnace row.
- Furnace mentions: annual filing Table 1 to 429.12(d) (l.359-379), "Consumer furnaces" and "Commercial warm
  air furnaces" under May 1; 429.12(i)(1) initial certification July 1, 2014 (l.383); AEDM Table 2 (l.718-763),
  "Commercial Warm-Air Furnaces ... Thermal Efficiency ..... 5% (0.05)" (l.762). The table prints the
  tolerance only; the rule text that applies it is not reprinted.
- Paperwork: 35 hours per response (l.233).
- Coverage: full except l.596-689 (skimmed, see Bundle).

## D07 - Analytic methods for energy conservation standards: request for information (91 FR 41578, July 7, 2026)

- Written by: DOE, Office of Critical Minerals and Energy Innovation; signed June 30, 2026 (Robertson);
  docket EERE-2022-BT-OT-0004. Comments on or before September 8, 2026.
- Background (l.95-100): Process Rule RFI December 18, 2017; NOPR February 13, 2019; NASEM contract July 15,
  2019; NASEM report transmitted January 7, 2022; Process Rule RFI April 17, 2025; 2026 Process Rule NOPR.
- Content: seven statutory factors (l.137-171); NASEM recommendations quoted by number (2-2, 2-3, 3-1 to 3-6,
  4-1 to 4-17, 5-1; several quoted twice); fn 9 discount rates 3% and 7% (l.221); elasticities 0.5, 1, 1.5
  (l.271); 30-year horizon (l.271, l.327, l.567, l.571); emissions no longer a factor in the 2026 Process Rule
  proposal (l.339, l.453).
- Table 1 (l.469-510): 27 commenter rows on the April 2025 Process Rule RFI with docket numbers 11-38 (no 32), fn 31 naming
  the 13 trade associations filing as "Joint Commenters"; "Joint Advocates" here = ASAP, ACEEE, CFA, NCLC.
- Additional topics (l.549-575, ch 89,000+): 30-year horizon; "9-year analysis timeframe ... (i.e., the 6-year
  review cycle plus the 3-year lead time provision under EPCA)"; "e.g., 30%" of the market already at a standard.
- Only furnace mention: fn 12 (l.274), December 2023 Consumer Furnaces Final Rule, 88 FR 87502.
- Coverage: full.

## Shared ground (navigation only)

- Entities in more than one document: AHRI (D02, D03, D04, D05, D07); NEEA (D02, D04, D07); ASAP (D02, D04,
  D07, inside differently named groups); Lennox (D02, D07); AGA/APGA (D01 litigation, D02, D07); ACEEE (D02,
  D07); ASHRAE 90.1 editions 2016/2019 (D02) and 2022 (D03, D04, D05). Group labels reused with different
  members: "Joint Advocates" (D02 vs D07), "Joint Commenters" (D04 vs D07).
- Same events, several documents: February 25, 2022 NOPR (D02, D03, D04); June 2, 2023 rule, August 1, 2023
  petition, February 6, 2024 remand (D03, D04, D05); January 17, 2025 determination (D04, D05); gas 80-to-81
  change and $284 (D03, D04); 77.5 to 82 range (D03, D04); May 9, 2025 (D05 signing, D06 Pub. L. 119-8).
- Documents that respond to another: D04 finalises D03 and answers its comments; D05 proposes to undo the
  procedure D03/D04 defend; D02 defers TE2 to the test procedure rulemaking; D07 follows the NAS review D02
  and D05 mention.
- Same-label figures on different scopes: CWAF TE standards by fuel and manufacture date (D02) beside the
  single 81 percent example (D03, D04); consumer AFUE classes (D01) beside CWAF TE classes (D02); "percent"
  used for percentage-point efficiency differences (D03, D04) and for a relative tolerance (D06); statutory
  clocks of 3, 6, 7 years and 45/60/75-day comment periods across D01-D04 and D07.
- Report date stated two ways: "December 2021 NAS report" (D02) vs transmitted "January 7, 2022" (D07).
