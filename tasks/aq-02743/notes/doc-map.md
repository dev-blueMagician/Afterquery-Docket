# aq-02743 - document map

Navigation only, like the form's bundle overview: where things are, not what to ask. Questions quote the
documents, never this map. Local ids equal the task page's numbers here: D01 = Doc 1 ... D07 = Doc 7.

## Bundle

- What it is: "Federal Web Accessibility Rulemakings", seven Federal Register texts retrieved on the word
  "accessibility". Only D03 (DOJ title II interim final rule, April 20, 2026) and D04 (HHS section 504 interim final
  rule, May 11, 2026) are about the same subject. D04 discusses D03; D03 never mentions HHS or section 504.
- Documents: 7; ids from `text/manifest.json`.
- Gaps: none. Capture "7 of 7 read in full (501,057 characters)"; `notes/intake.json` shows every document
  `incomplete: false`, `matches_capture: true`.
- Extraction spot-checks (2026-10-10): plain-text captures, no pages. Character counts match the capture's list
  within 1-10 characters per file (trailing whitespace). D03 Table 1 and Table 2 and D04 Tables 1-4 are flattened
  onto single lines with dot leaders (row labels and all cells present; column order Baseline, IFR, Savings, each
  Undiscounted then Discounted). Footnotes are inline blocks between dashed rules; D03 fn 82 and fn 88 and D04
  fn 26, fn 75 and fn 81 checked against `docs/`. D04's SUMMARY breaks a sentence across two lines ("fewer than
  fifteen" / "(15) employees"), so quotes there must stay inside one line.
- Provenance: `notes/intake.json`, capture sha256 bee75bdd...; one capture, AQ-02743_2026-10-10_1811.txt.
- Reuse binding: source hashes in `notes/intake.json` (D03 c5a0703a..., D04 31bc90aa...). Refresh this map if
  they change.
- Coverage: caller read D03 and D04 in full, and the passages of D01, D02, D05, D06, D07 that mention
  accessibility law, populations, thresholds or costs (keyword passages with context, not a full read). Two
  independent question-author runs each read all seven texts in full (returns summarised in `notes/hooks.md`).

## D03 - DOJ, extension of title II web/mobile compliance dates (interim final rule)

- Source: docs/fr_2026_07663.txt | 91 FR 20902-20912, April 20, 2026 | 77,457 characters.
- Written by: Civil Rights Division, Department of Justice; signed Todd Blanche, Acting Attorney General
  (dated April 16, 2026; filed 4-17-26).
- Type, date: interim final rule with request for comments. Effective April 20, 2026 (L28). Comments by
  June 22, 2026 (L29).
- Operative rule (SUMMARY L25, repeated L262, L267, amendment L494-495): total population of 50,000 or more:
  April 24, 2026 -> April 26, 2027. Total population under 50,000, "or any special district government":
  April 26, 2027 -> April 26, 2028. Definitions of "total population" and "special district government" are in
  28 CFR 35.104 and Appendix D, cited at L63, NOT reprinted.
- History (L63-127): 2024 final rule published April 24, 2024, effective June 24, 2024. 2010 ANPRM (about 400
  comments; six months to two years), 2016 SANPRM (about 200; two to three years; commenters immediate to 10
  years), 2017 withdrawal, 2023 NPRM (about 345 comments; alternatives one year for all, one/three, three/four).
- Letters (L138-166): higher-education associations (May 12, 2025), SBA Office of Advocacy (same date; 2023
  letter asked four or five years under 50,000), a Congressman, K-12 associations (one surveyed 60 members),
  accessibility organizations (July 26, 2025) and the National Federation of the Blind (June 9, 2025) against delay.
- Cost figures, all past character 57,000: FRIA "with the longer dates" annualized net benefits "$1.3 billion" at
  7 percent (L312); fn 82 (L318) benefits $4,509.5 million, costs $3,249 million. Cost Savings Estimate (L333-376):
  $2.775 billion present value, $395 million annualized; small entities $1.47 billion (53%), $210 million;
  implementation $16,949 million, recurring $1,990 million; Table 1 (status quo 27,959, IFR 25,185, savings
  -2,775 discounted, -1,990 undiscounted); fn 88 (3%: $2,355 million, $276 million); Table 2 (original 10-year
  total costs $24,688 million, small $13,095 million).
- Rounded prose beside exact figures: "$1.3 billion" vs fn 82's components (1,260.5); "$1.47 billion" vs Table 2's
  1,472; "$13.1 billion", "$24.7 billion" vs Table 2.
- Internal inconsistencies (do not build on them): the prose says the dropped recurring year has a present value of
  "roughly $1,012 million" while Table 1's total implies 1,738 (Year 2); 27,959 - 25,185 = 2,774, printed -2,775;
  Table 1's status-quo present value (27,959) differs from Table 2's "original 10-year total costs" (24,688).
- No dollar year is stated. Benefits of the delay not quantified (L381).
- Regulatory sections: E.O. 12866 significant, major rule, RFA not required, PRA none.

## D04 - HHS, extension of section 504 web/mobile compliance dates (interim final rule)

- Source: docs/fr_2026_09266.txt | 91 FR 25496-25507, May 11, 2026 | 85,328 characters.
- Written by: Office for Civil Rights, HHS; signed Robert F. Kennedy, Jr. (filed 5-7-26, 4:15 pm).
- Type, date: interim final rule with request for comments. Effective May 7, 2026 (L30), four days before its
  Federal Register date. Comments by July 6, 2026 (L31).
- Operative rule (SUMMARY L26-27, repeated L245-246, L251, amendment L491-492): recipients with fifteen or more
  employees: May 11, 2026 -> May 11, 2027. Fewer than fifteen: May 10, 2027 -> May 10, 2028.
- History: 2024 final rule published May 9, 2024, effective July 8, 2024; NPRM September 14, 2023, 5,269 comments.
- What it says about DOJ (prints no DOJ compliance date): 2024 title II rule "less than a month prior" (L110-114),
  "differentiates between small and large covered entities based on population size" (L114); fn 26 (L118) "now three
  (3) and four (4) years"; "On April 20, 2026, DOJ published an IFR delaying the compliance dates ... by one year"
  (L162); overlap of covered entities (L112, L143); consistency rationale and "short timeframe" (L297); fn 75 (L342).
- Letters and figures it alone describes (all past character 20,000): NACo survey, 18 responses (3 under 50,000; 12
  at 50,000-500,000; 3 over 500,000), asks July 1, 2027 for all entities, exemption under 10,000, cure period
  (L162-166); NLC, over 16,000 municipalities under 10,000 with budgets of $2 million or less, quotes $10,000 to
  $20,000, annual up to $70,000, a city of about 275,000 needing 1,300 staff hours, asks (L175); FQHC comments
  (L186); Talkiatry and DOGE-0995 comments (L125-135).
- Cost figures, all past character 61,000, constant 2022 dollars: 2024 RIA annualized costs $934.7 million and
  benefits $1,265.6 million at 7% (L340, original timeline = the tables' Baseline column, L328). Table 1 (7%)
  annualized 934.7 / 820.3 / -114.3; Table 2 (3%) 916.9 / 823.7 / -93.3; Table 3 (7%) 1,265.6 / 1,061.0 / -204.6;
  Table 4 (3%) 1,311.8 / 1,122.0 / -189.8. Net decrease in benefits $90.2 million or $96.5 million annualized,
  $633.7 million or $823.2 million total (L374). E.O. 14192: $52.18 million annualized, perpetual horizon, 2024
  dollars = $49.1 million in 2022 dollars (L398, fn 81).
- Small inconsistencies: L375 says "$189.9 million" where Table 4 prints -189.8; 204.6 - 114.3 = 90.3 against the
  printed 90.2 (the tables' IFR cells give 240.7 net, the printed changes 240.6).
- APA basis: 5 U.S.C. 553(a)(2) (grants) and good cause; RFA not required; PRA none.

## D01 - Education, National Center on Digital Access in Education (notice inviting applications)

- Source: docs/fr_2023_28871.txt | 62,572 characters. Office of Special Education and Rehabilitative Services.
- Dates: applications available January 3, 2024; deadline March 4, 2024; intergovernmental review May 2, 2024.
- Figures: maximum award $1,500,000 a year; $4,500,000 budget cap; project period up to 60 months; "85 percent of
  710 teachers". Mentions section 504, title II (28 CFR part 35) and WCAG 2.2 AA (L120) as an example standard;
  cites no DOJ or HHS web rule or date.
- Coverage: caller keyword passages only; full reads by both independent authors.

## D02 - FTA, Bus Safety and Accessibility Research Program (notice of funding opportunity)

- Source: docs/fr_2024_26835.txt | 57,178 characters. Up to $10,000,000; 80% maximum Federal share; applications
  due January 17, 2025. "Accessibility" is physical bus accessibility (49 CFR part 38). No link to D03/D04.
- Coverage: caller keyword passages only; full reads by both independent authors.

## D05 - DoD, assistance to entertainment media productions (final rule)

- Source: docs/fr_2026_11505.txt | 69,129 characters. Effective July 9, 2026. PRA: about 200 requests a year,
  45 minutes, $30.10 per request ($40.13 median hourly wage), Federal review $37.12 per response ($49.50 GS-12
  rate), total $7,424. Single-document oddity: non-Government total printed as $5,869.50. No link to D03/D04.
- Coverage: caller keyword passages only; full reads by both independent authors.

## D06 - FCC, broadband label requirements (final rule)

- Source: docs/fr_2026_16503.txt | 71,191 characters. Keeps the requirement that labels be accessible to people
  with disabilities (L48, L102-108); no WCAG reference.
- RFA boilerplate (L196): small governmental jurisdictions are those "with populations of less than fifty
  thousand"; "at least 48,724 out of 90,835 local government jurisdictions have a population of less than 50,000"
  (2022 Census of Governments). Same 50,000 line as D03's tiers, but the documents never connect them.
- Coverage: caller keyword passages only; full reads by both independent authors.

## D07 - MARAD, Title XI vessel and shipyard financing (interim final rule)

- Source: docs/fr_2026_17636.txt | 78,209 characters. Effective August 28, 2026; comments by October 27, 2026.
  Removes 14 of 34 sections; application fee $5,000 -> $1,000. "Accessibility" means readable regulation text.
- Coverage: caller keyword passages only; full reads by both independent authors.

## Shared ground (navigation only)

- Entities in more than one document: DOJ and its 2024 title II rule (D03; D04 L110-118, L143, L162, L297);
  NACo (D04 survey and asks; D03 only a 2024 generative-AI survey footnote, L201); the higher-education
  associations' letter and SBA Advocacy's letter to OMB, both May 12, 2025 (D03 L138-146; D04 L150-159); WCAG 2.1
  (D03, D04) and WCAG 2.2 (D01 L120; D03 L195 as a newer standard not incorporated).
- Documents that cite another: D04 cites D03 (91 FR 20902) at fn 26, fn 39, fn 65. No other cross-citation.
- Parallel structure: D03 and D04 share the preamble skeleton (need, amendments, severability, APA, E.O. sections)
  and each extends two tiered dates "by one year". Tier tests differ: population and special-district status (D03),
  number of employees (D04). Each document prints only its own compliance dates.
- Public facts a solver may recall: the 2024 rules' original dates (April 24, 2026 / April 26, 2027; May 11, 2026 /
  May 10, 2027). Three of the four new dates equal the original plus exactly one year; DOJ's April 26, 2027 does
  not (April 24, 2026 plus 367 days).
- Same threshold, unrelated documents: 50,000 population (D03 tiers; D06 RFA count).
