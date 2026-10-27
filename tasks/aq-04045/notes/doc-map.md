# aq-04045 - document map

Maintained by the caller from `text/` (and `docs/`). Navigation only: where things are, not what to ask.
Questions quote the documents, never this map. Local ids D01-D07 equal the task page's Doc 1-7
(notes/intake.json).

## Bundle

- What it is: seven Federal Register texts on space regulation, 2024-2025. Six are FCC: two on orbital
  debris (D01, D03), three in one regulatory-fee proceeding, MD Docket No. 24-85 (D02, D05, D06), one on
  application streamlining (D07). D04 is a Commerce (BIS) export-control proposal, unrelated to the rest.
- Documents: 7; ids from `text/manifest.json`. Capture: "7 of 7 read in full (520,340 characters)".
- Gaps: none reported by the splitter (every document `incomplete: false`, gap 0). The capture carried the
  page's reload notice ("Docket has been updated. Reload this page ..."); documents were all present.
- Extraction spot-checks (2026-10-13): plain-text sources, no pages. Character counts match the capture
  (D01 46,152 ... D07 81,550), and a script check found every text/Dnn.txt body identical to its docs/
  file. Character positions of the fee figures were read from docs/. No tables in any document;
  FR-style quotes print as two backticks and two apostrophes; a paragraph can break across lines
  (D06 para 40 breaks before "100 space stations").
- Provenance: notes/intake.json, capture sha256 bd5fbe17...; no earlier capture of these documents in
  10.6, 10.7 or 10.8 (file names, FR numbers and source hashes all checked: no match).
- Read coverage: D01, D02, D03, D05, D06 read in full. D07 read in full to line 244 and the rest (FRFA
  end, ordering clauses, rule text) at 520 characters per line. D04 NOT read in full: headings and keyword
  hits only (debris, servicing, telemetry, FCC, constellation); nothing in it is used by any sketch.

## D01 - FCC, Orbital Debris Reconsideration Order (89 FR 13276, Feb 22, 2024)

- Denial of three petitions against the 2020 Orbital Debris Order. Adopted Jan 25, 2024, released
  Jan 26, 2024, effective Feb 22, 2024.
- Petitioners (para 1 and ordering clause 35): Combined Petition = Boeing, EchoStar, Hughes, Planet,
  Spire, Telesat; SpaceX; Kuiper (Kuiper Systems LLC). Opposers/commenters: Viasat, OneWeb, Maxar,
  Kepler Communications Inc., ARCLab. Maxar opposed the Combined Petition and supported Kuiper's.
- Dates: NPRM "released" Nov 19, 2018 (84 FR 4742, Feb 19, 2019); 2020 Order adopted April 23, 2020,
  published Aug 25, 2020 (printed "86 FR 52422" in para 1; D03 prints 85 FR 52422); petitions filed
  Sept 24, 2020; oppositions by Nov 24, 2020.
- Figures: collision probability 0.001; disposal reliability 0.9, goal 0.99 for large systems; NASA
  handbook 1E-4 and 1.5 orders of magnitude; ODMSP 5 mm, 25 years, 100 object-years.
- Which petitioners argued which issue: maneuverability (Boeing, Planet, Spire); disposal reliability
  (Boeing, Planet, Spire, Telesat); deployment devices (Boeing, Planet, Spire, EchoStar, Hughes).

## D02 - FCC, small-satellite fee rule for FY 2024 (89 FR 60572, July 26, 2024)

- Report and Order adopted and released June 13, 2024; effective Sept 13, 2024.
- Small satellite fee for FY 2024 kept at the FY 2023 level, $12,215 (char 8,984). Old method (III.A):
  average of the calculated NGSO-Other and NGSO-Less Complex rates x 5% (1/20), rounded to the nearest $5;
  small-satellite revenue "deducted from the share of space station regulatory fees allocated to ... NGSO";
  the rest split 80/20 between Other and Less Complex. "For FY 2024 ... deduct this amount from the NGSO
  share" (char 12,494).
- RPO, OOS and OTV space stations put in the small satellite category on an interim basis, whatever their
  orbit, per license/call sign. Declined: all ISAM stations, crewed/habitable stations, a definition by
  characteristics, separate fees for attached RPO/OOS (deferred).
- NPRM released March 13, 2024 (89 FR 20582, March 25, 2024): 16 comments, 17 reply comments.
- FRFA: Satellite Telecommunications size standard $38.5 million; 2022 Universal Service Monitoring
  Report, as of December 31, 2021: 65 providers, about 42 with 1,500 or fewer employees (printed three
  times, chars 33,113 / 34,472 / 38,845). 33.2 million small businesses.

## D03 - FCC, orbital debris rules: effective date and five-year rule (89 FR 65217, Aug 9, 2024)

- OMB approval July 2, 2024 (control number 3060-1327, expires July 31, 2027): 28 respondents and
  responses, 4-15 hours each, 341 hours, $53,900. Effective Sept 9, 2024; compliance with the five-year
  amendments not required until Sept 29, 2024.
- Summarises the 2022 Second Report and Order (FCC 22-74): LEO disposal by uncontrolled re-entry no later
  than five years after end of mission (was a 25-year benchmark); "end of mission" defined; applies to
  market access, small satellites (25.122), Part 5 and Part 97. Grandfathering: satellites in orbit
  exempt; two years from Sept 29, 2022; modification applications by March 29, 2024. Waiver factors;
  "at least 50% funded by the U.S. Government, excluding funding for launch operations".
- NPRM "adopted" Nov 15, 2018 (D01 says released Nov 19, 2018).
- FRFA carries the 2022 order's older data: size standard $38 million; 2021 Monitoring Report, as of
  December 31, 2020: 71 providers, about 48 with 1,500 or fewer employees (char 36,522); All Other
  Telecommunications on 2012 Census data (1,442 firms).

## D04 - BIS, proposed space export-control changes (89 FR 84784, Oct 23, 2024)

- Not read in full. Comments due Nov 22, 2024; 19 comments on the Commerce ANPRM in 22 topics; ECCN
  9A515 revisions (9A515.a.4 covers servicing, life-sustaining and debris-removal spacecraft), new 9C515,
  License Exception CSA. No fee, licensing-count or debris-rule figure shared with the FCC documents.

## D05 - FCC, fee FNPRM (90 FR 11918, March 13, 2025)

- Comments due March 27, 2025; replies April 11, 2025. History of the fee categories, paras 3-10:
  2020 80% GSO / 20% NGSO; 2021 20/80 Less Complex/Other; 2022 small satellite at 1/20th of the average;
  June 2024 $12,215 (char 9,800); September 2024 60% GSO / 40% NGSO (char 10,772).
- ONLY source of FY 2024 unit counts (para 28, char 32,469): 16 small satellite, 140 GSO, 6 less complex,
  11 other. Para 34 (char 41,895): 60/40 "was the case for FY 2024".
- Proposals: fees on authorized stations; alternative methodology (one unit per GSO station or per NGSO
  system up to 100 stations, extra units per 500 or 1,000); NGSO-Other split into Large (more than 1,000)
  and Small (1,000 or fewer) at 50/50; earth station categories. "Less complex" = 20 or fewer U.S.
  authorized earth stations, primarily EESS and/or AIS. Up to ten space stations per small satellite license.
- Named commenters: Kepler, Astro Digital, Iridium, Kineis, Kuiper, SpaceX (also "Space X"), Maxar and
  Telesat. No per-unit fee for FY 2024 is printed here.

## D06 - FCC, fee rule for FY 2025 (90 FR 29760, July 7, 2025)

- Third Report and Order adopted June 5, 2025, released June 9, 2025; effective Sept 14, 2025.
- ONLY source of FY 2024 per-unit fees (para 40, char 46,796): NGSO-Other $964,200, NGSO-Less Complex
  $441,925; same paragraph: 80%/20% "after subtracting a pro rata amount of the total fees assessed for
  NGSO--Small Satellites from each category". $12,215 at char 9,307; 60/40 GSO/NGSO at char 10,322.
  The GSO per-unit fee is printed nowhere in the bundle.
- Adopted: fees on authorized stations as of the start of the fiscal year (October 1, 2024); Small
  (fewer than 1000) and Large (1000 or more) constellations, 60% small / 40% large; "an estimated 24 NGSO
  small constellations as compared to three NGSO large constellations" (para 48, char 54,165). Declined:
  alternative methodology, TT&C-only exemption (one transition exception, para 31), earth station
  categories. FNPRM drew 19 comments and 17 reply comments.
- FRFA: size standard $44 million, no provider count; 34.75 million small businesses.

## D07 - FCC, application streamlining (90 FR 41790, Aug 27, 2025)

- Second Report and Order adopted Aug 7, 2025, released Aug 8, 2025; effective Sept 26, 2025 except
  listed sections delayed indefinitely. Baseline earth station license, 60-day NGSO notifications, renewal
  windows (12 months to 30 days), 30-day shot clock, savings about $45,000 ($34,000 over 44 filings,
  $11,000 over 3,000 applications). 14 comments, 12 replies.
- FRFA: 2024 Monitoring Report, as of December 31, 2023: 57 providers, about 40 with 1,500 or fewer
  employees (char 63,902); size standard $44 million.

## Shared ground (navigation only)

- One fee proceeding in three steps: D02 (June 2024 order) -> D05 (February/March 2025 further notice) ->
  D06 (June 2025 order). FY 2024 units are only in D05, FY 2024 per-unit fees only in D06, the
  small-satellite deduction rule in D02 and D06, $12,215 in all three.
- Proposal against final: D05 Large = more than 1,000 with a 50/50 split of NGSO-Other only; D06 Large =
  1000 or more with 60/40 over all NGSO systems.
- Debris pair: D01 (2020 order dates, petitioners) and D03 (effective dates, five-year rule). D06 paras
  27-31 refer to post-mission disposal plans; no figure links them.
- Repeated FRFA paragraph on satellite telecommunications providers, three editions: D03 (2020), D02
  (2021), D07 (2023). D05 and D06 print no count. The later-published D03 carries the oldest data.
- Companies in both D01 and D05: SpaceX, Kuiper, Telesat (petitioners in D01); Maxar, Kepler (opposers in D01).
