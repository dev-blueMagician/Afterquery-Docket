# aq-02208 - document map

Maintained by the caller from `text/`. Navigation only, like the form's bundle overview: where
things are, not what to ask. Questions quote the documents, never this map. Line numbers are
`text/Dnn.txt` lines (line 1 is the `# Dnn` header).

## Bundle

- What it is: six Federal Register documents on US space launch licensing (Space Launch Licensing
  Filings, Public policy), 2024-2026: two FAA rulemakings (final rule, NPRM) and four FCC items
  (Bureau public notice, Commission final rule, Bureau final procedures, Commission NPRM).
- Documents: 6; ids from `text/manifest.json`. Local ids equal the task page's Doc numbers
  (D01 = Doc 1 ... D06 = Doc 6; file names sort in page order).
- Gaps: none. Capture "6 of 6 read in full (490,832 characters)"; `notes/intake.json` shows every
  document `incomplete: false`, `gap_characters: 0`, `matches_capture: true`.
- Extraction spot-checks (2026-10-08): plain-text sources, method `text`, no pages. Character
  counts match the splitter within header/whitespace (D01 112,564 vs 112,572 written, D06 equal).
  Tables checked: D01 Table 1 (changes by section, lines 334-425, column text interleaved by the
  FR text rendering, readable); D05 small-entity table (lines 306-308, pipe-free single rows).
  Footnotes checked: D01 \1\-\6\, D06 \1\-\14\ present inline. D03 line 296 is an omitted graphic
  ("[GRAPHIC] [TIFF OMITTED] TR07MR25.000", the US Table page 38) - not recoverable from text; the
  NG42 footnote text that follows (lines 298-302) is present. D03 lines 143-150 (emission mask) print
  the power term as "55 + 10 log10 pY dB" (source rendering of P); D03 line 375/378 same.
- Provenance: notes/intake.json, capture AQ-02208_2026-10-08_1841.txt sha256 96c08c13...6a67c;
  page notice "Docket has been updated. Reload this page so its checks and buttons keep working."
- Coverage: all six documents read in full by the caller, 2026-10-08.
- Reuse binding (sha256): D01 4265ada6...86e, D02 ae472200...c460, D03 def27f9f...6fa6f,
  D04 cff2e008...397, D05 97319ce5...cadcef, D06 ca7dd34a...4de8.

## D01 - FAA final rule, U.S. Commercial Space Launch Competitiveness Act Incorporation

- Source: docs/fr_2024_20900.txt; 89 FR 76714-76730, Sept 19, 2024; FR Doc 2024-20900;
  Docket FAA-2023-1656; RIN 2120-AL19.
- Written by: FAA (DOT); signed Michael Gordon Whitaker, Administrator (line 1038).
- Dates: effective and compliance date November 18, 2024 (30-31); NPRM published August 18, 2023,
  88 FR 56546 (112); CSLCA statutory changes in effect since 2015 (106, 427).
- Comments: 15 comments (118); 17 comment areas listed (121-137).
- Changes from proposed rule: lines 100-102 and 139-141 ("human being" replaced; government
  personnel definition not changed; training "ensure ... trained"; electronic tracking).
- Definitions (401.5, lines 553-594): government astronaut, international partner astronaut,
  launch (begin/end, 565-574), launch accident (> $25,000 property damage, 575-581), reentry,
  reentry accident, space flight participant. 401.7 repeats (604-617).
- Human space flight compliance lists (415.8, 431.8, 435.8, 437.21(b)(3), 450.45(e)(5)): 460.5,
  460.7, 460.11, 460.13, 460.15, 460.17, 460.51, 460.53, 460.59, 460.61, 460.67 (647, 661, 676, 737,
  946-947); Table 1 says 460.59, 460.61 and 460.67 were added (364-392, 418-420).
- Part 437 (experimental permits): suborbital rocket -> reusable suborbital vehicle; 437.21(b)(1)(i)
  NEPA general text (733), (b)(1)(iv) approved EA/EIS/CATEX/re-evaluation required (735); 437.9
  unlimited launches (723); permits only for suborbital (271).
- Part 440: MPL definition with 1-in-10,000,000 and 1-in-100,000 probability thresholds (872-874);
  third party (879-887, government astronaut excluded); 440.9(b) additional insureds incl. (4) space
  flight participants, ceases Sept 30, 2025 unless public law modifies (896-900); 440.17(f) same
  sunset "as of September 30, 2025" (920); appendices B-E moved to AC 440.17-1.
- Part 460 new subparts C (460.55-460.61) and D (460.63-460.67) (958-1035).
- Regulatory notices: UMRA $100 million adjusted, "$183 million using the most current (2023)
  Implicit Price Deflator" (319, 446); Pub. L. 96-354, 96-39, 104-4 (319); categorical exclusion
  FAA Order 1050.1F para 5-6.6f (454); authority 51 U.S.C. 50901-50923 (77, 541).
- Commenters named: Sierra Space, Virgin Galactic, Blue Origin, SpaceX, ALPA, Ascendant Spaceflight
  Services, Space Infrastructure Foundation, Space Law & Policy Solutions, individuals.

## D02 - FCC WTB Public Notice proposing Space Launch Service licensing/coordination procedures

- Source: docs/fr_2024_29833.txt; 89 FR 104502-104508, Dec 23, 2024 [Proposed Rules]; DA 24-1232
  released December 6, 2024 (46); ET Docket 13-115; signed Amy Brett, Chief of Staff, WTB (263-264).
- Comments due January 22, 2025 (28) - only document with this date.
- Background: Second R&O (89 FR 63296-01, Aug 5, 2024) allocated 2025-2110 and lifted 2200-2290
  four-sub-band limit (66-70); LCA enacted Sept 26, 2024; 90-day and 180-day mandates (71-76);
  Second Further Notice cited as "89 FR 6488-01, February 1, 2024" (71; D03 says February 2, 2024).
  "Space Launch Service, which at present includes the 2025-2110 and 2200-2290 MHz bands" (77).
- Proposed initial registration lists (91-145): launch site (4), itinerant/mobile (a-c, antenna
  details i-ix), launch vehicles as mobile stations (a-d), fixed/base (a-j incl. h coordinates).
- Bandwidth > 5 MHz justification at initial registration (147).
- Proposed coordination-request data (162-220): 9 groups; group 7 "Additional launch site technical
  information" a-d (195-199: elevation of ground, overall height to tip, distance to nearest aircraft
  landing area, natural formations/structures shielding the antenna) - c and d appear in no other
  document; group 5 transmitter characteristics a-l; group 6 emission details a-e (e = >5 MHz
  explanation); group 8 launch details a-p; group 9 additional station details a-c.
- Part 87 data list for flight-test coordination (159) incl. "trajectory (azimuth, heading)".
- Proposed timings: SBE local coordinator receives requests >= 60 days before launch, response 15
  days after receipt (230); NTIA FAB / AFC >= 60 days (239); 96-hour pre-launch notice for
  2360-2395 (234); 320 km (200 miles) radius with discretion to expand (233-234).
- SBE showing: <= 0.5 dB noise-threshold increase at ENG receive sites (229) - only in D02.
- Post-coordination registration proposed list 1-7 (253-259).

## D03 - FCC Third Report and Order, Allocation of Spectrum for Non-Federal Space Launch Operations

- Source: docs/fr_2025_02961.txt; 90 FR 11480-11493, March 7, 2025; FCC 24-132 adopted December 23,
  2024, released December 31, 2024 (34); signed Marlene Dortch, Secretary (262-263).
- DATES: rules effective April 7, 2025, except amendatory instruction 9 (Sec. 26.202(d)) indefinitely
  delayed (27-28); ordering clauses: effective 30 days after FR publication, 26.202 awaits OMB (246-247).
- LCA "act in the first instance by December 25, 2024" (137) - only document printing that date.
- Second R&O "September 2023", published 89 FR 63296, Aug 5, 2024 (25, 181); Second Further Notice
  released September 2023, published 89 FR 6488, February 2, 2024 (45, 177).
- 2360-2395: secondary non-Federal SOS (Earth-to-space and space-to-Earth) over the entire band
  (46, 57, 80, NG42 at 299-302); Mobile allocation limits launch telemetry to three frequencies
  (US276, 87.303(d)(1); 57) - values not printed here; 2390-2395 co-primary Amateur (51).
- Band directions: 2025-2110 ground-to-launch-vehicle telecommand only; 2200-2290 vehicle-to-ground
  telemetry/tracking (76); 2360-2395 either direction (79-80).
- Scope: no on-orbit communications after payload separation (77-78); definition of space launch
  operations (47, 284).
- License term 10 years, renewal 10 years (85); 15-year term rejected (237); no construction
  requirement; no partition/disaggregation/leasing (86).
- Technical: 5 MHz authorized bandwidth with case-by-case justification (139-140); emission mask
  <= 1 MHz and > 1 MHz breakpoints (143-150, 373-378); 25 W EIRP and output power (156-157, 386).
- FRFA statistics (203-219): 33.2 million small businesses (99.9%); 530,109 small exempt orgs;
  90,837 local governments, 48,724 small; 13 part 90 frequency coordinators; Satellite Telecom 275
  firms (2017), 242 < $25M, SBA $44M; All Other Telecom 1,079 firms, 1,039 < $25M, SBA $40M;
  Nonscheduled charter 1,148 firms, 1,129 < 250 employees; principal launch operators: Blue Origin,
  Lockheed Martin, Northrop Grumman, SpaceX, Boeing, Virgin Galactic (218).
- STAs valid for a single launch and expire after six months (236).
- LCA = Public Law 118-85, 138 Stat. 1546 (245, 318).

## D04 - FCC WTB final licensing and coordination procedures (DA 25-270)

- Source: docs/fr_2025_07643.txt; 90 FR 18789-18800, May 2, 2025 [Rules and Regulations]; released
  March 25, 2025 (31); signed Amy Brett, Acting Chief of Staff (301-302).
- Effective 30 days after FR publication except new/modified information collections (296).
- Record: eight comments and seven ex parte letters (70).
- Third R&O adopted December 23, 2024 (62); cites Third R&O as 90 FR 11480-01, March 7, 2025 (47).
- Decisions: antenna details moved from ULS registration to coordination requests (87); launch
  vehicle not a mobile station (93-96); > 5 MHz justification as single attachment (106, 205);
  SBE/AFTRCC additions (122); suborbital exemptions (122); no blanket missions (124); single federal
  destination NTIA OSM FAB (134); AFTRCC via online portal (135); no mandated timeframes, 60 days
  "would best facilitate" (139-140); AFTRCC asked 80 days, SpaceX 5-10 days, Virgin Galactic 15 or 30
  (137-138); no incumbent response deadline (142-146); 320 km maintained (149-155); center
  frequencies 2,364.5 / 2,370.5 / 2,382.5 MHz (155) - only document printing them; NTIA automated
  mechanism "when available" fulfills 180-day obligation (157); no cut-off for changes, 6-month STAs,
  48 hours' notice in part 5 (165-172); 96-hour notice not mandated (173-179).
- Final lists (Section III, 197-295): launch site 1-4; fixed/base 1-8; itinerant/mobile 1-6;
  coordination request 1-8 (transmitter characteristics a-q, emission details a-h, launch details
  a-q incl. m trajectory); post-coordination registration 1-7 (Eastern Time Zone).
- Commenters named: AFTRCC, SBE, ULA, SpaceX, Virgin / Virgin Galactic, Blue Origin.

## D05 - FCC NPRM, "Spectrum Abundance for Weird Space Stuff" (SB Docket 26-54, FCC 26-13)

- Source: docs/fr_2026_06865.txt; 91 FR 17914-17931, April 9, 2026; adopted March 26, released
  March 27, 2026 (46); comments May 11, replies June 8, 2026 (28); signed Marlene Dortch.
- Up to 20,000 MHz connectivity proceeding (68); "from zero non-Federal spectrum available today to
  support emergent space operations to at least 25 megahertz" (69).
- Federal S-band 2025-2110 / 2200-2290 and X-band 8400-8450 / 8450-8500 heavily used (103-107);
  "full 85 megahertz" of 2025-2110 not available to non-Federal operations (181).
- 2320-2345 MHz: 25 MHz SDARS band, Sirius 2320.0-2332.5 / XM 2332.5-2345 (12.5 MHz each) (162, 167);
  licenses auctioned 1997; XM 2001, Sirius 2002 service; merged 2008; GSO 85 and 115 W.L. (164);
  ~32.8 million subscribers as of June 30, 2025 (165); proposal: secondary SOS Earth-to-space +
  de facto leasing, SiriusXM coordination certification (182-205); TT&C often <= 100 kHz (181).
- Adjacent bands: 2315-2320 / 2345-2350 (WCS C/D, SiriusXM 2024) (222-228); 2305-2315 / 2350-2360
  (WCS A/B, AT&T) (229-248); 128 WCS licenses 1997, 12 REAGs, 52 MEAs (236); 45/55 MHz contiguous
  (238); US100: 2312.5 MHz shared for launch-vehicle telemetering (233); US97 145 km of Goldstone
  (224, 232); US100 non-Federal flight test provision expired January 1, 2020 (235); ten WCS licenses
  in the Pacific Island REAG in inventory (247).
- Costs (264-280): operator team $128,473.60 (2 lawyers $106.10/h + 2 engineers $94.64/h x 320 h);
  NTIA team $77,443.20 (3 x $80.67 x 320 h); $205,916.80 per coordination; ~80 applications/yr,
  50% -> 40; "approximately $8.2 million"; negotiation $33,952.00 per lease, "approximately $1.4
  million"; "at least $6.8 million" net (exact operands give 6,878,592); intersatellite links 25 x
  (1.5 h x $106.10 + $140) "approximately $7.4 thousand" (exact 7,478.75).
- IRFA: 34.75 million small businesses (299); 48,724 of 90,835 local governments (303); NAICS table
  (306-308; Satellite row 195/332 printed 88.69% - inconsistent).
- Does not mention the Launch Communications Act or part 26.

## D06 - FAA NPRM, Waiver of Specified Statutory Requirements for Commercial Space Launch and Reentry

- Source: docs/fr_2026_15415.txt; 91 FR 47997-48002, July 30, 2026; Docket FAA-2026-8614, Notice
  26-11, RIN 2120-AM51; comments due August 31, 2026 (29); signed Sean P. Duffy, Secretary (382-383).
- E.O. 14335 signed August 13, 2025, published 90 FR 40219 Aug. 19, 2025 (46-50).
- Authority 51 U.S.C. 50905(b)(2)(C) (55, 61-65); CSLA codified 50901-50924 (60).
- 13 laws listed (100-112) and in proposed 400.3(b) with narrower citations (296-311); 4 licensing
  circumstances (123-127, 313-317); 8 further laws invited for comment (136-137); 6 questions a-f.
- Proposed 400.3(a): licenses/permits under parts 420, 433, 437, 450 "issued or modified on or after
  [EFFECTIVE DATE OF FINAL RULE]" (291-294); conforming amendments 420.15(b), 433.7(a),
  437.21(b)(1)(i), 450.47(a) (327-378).
- UMRA $193,000,000 ($100,000,000 adjusted, most current IPD) (183); FAA Order 1050.1G, DOT Order
  5610.1D (196-197); Pub. L. 96-39 (178); significant regulatory action (163).

## Shared ground (navigation only)

- LCA enactment Sept 26, 2024 and its 90/180-day mandates: D02 71-76, D03 25/38/137/181, D04 53.
  Not in D05.
- Band edges 2025-2110 / 2200-2290 / 2360-2395 MHz: D02, D03, D04 throughout; D05 103, 181, 224.
- Proposal -> final: D02 (proposed procedures) -> D04 (final procedures; restates most proposals
  except the full coordination/registration lists). D03 affirms D02's proposals (132).
- Third R&O: D03 (the order) and D04 62-65 (adoption date and content, not its effective date).
- Same CFR paragraph: 14 CFR 437.21(b)(1)(i) revised by D01 (726-735) and proposed again by D06
  (358-363); 450.45 (D01) vs 450.47 (D06) are different sections.
- UMRA threshold: D01 319/446 ($183M, 2023 IPD) vs D06 183 ($193M).
- Small-entity statistics series: D03 FRFA 203-219 vs D05 IRFA 299-308.
- Entities in several documents: SpaceX (D01, D03, D04), Virgin Galactic (D01, D03, D04), Blue
  Origin (D01, D03, D04), AFTRCC (D03, D04, D05; D02 says "part 87 frequency advisory committee"),
  SBE (D02, D04), NTIA (D02-D05), NASA (D01, D03, D05, D06), SiriusXM / AT&T (D05 only).
- Launch-vehicle telemetry frequencies: D04 155 (three in 2360-2395); D05 233 (2312.5 MHz).
- Six-month STAs: D03 236, D04 170.
