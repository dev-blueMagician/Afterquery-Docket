# aq-04112 - document map

Navigation only, like the form's bundle overview: where things are, not what to ask. Questions quote
the documents, never this map. Written by the author (Claude) on 2026-10-13 after reading all three
documents in full.

Doc numbers are the task page's. Local ids are alphabetical by file name and differ:
Doc 1 = D03 (report), Doc 2 = D01 (26 October 2021 hearing), Doc 3 = D02 (9 November 2021 hearing).

## Bundle

- What it is: House of Commons Environment, Food and Rural Affairs Committee inquiry "Labour shortages in
  the food and farming sector" (HC 713): the Fourth Report of Session 2021-22 and the transcripts of the
  first two of its four oral evidence sessions.
- Documents: 3 (`text/manifest.json`: D01, D02, D03). Page: "Public policy · 3 documents · 82,696 prompt
  tokens", "3 of 3 read in full (381,633 characters)".
- Gaps: none in the capture (`notes/intake.json`: every document `incomplete: false`, `gap_characters: 0`).
  Not in the bundle, by design of the set: the hearings of 16 November 2021 (Eustice, Kennedy, Q169-282) and
  14 December 2021 (Foster, Rouse, Q283-408), which Doc 1 quotes; the written evidence (LS numbers); the
  report's Figure 1 (unemployment forecasts against outturns), of which only the caption survives.
- Extraction spot-checks (text/ against docs/): character counts 165,823 / 109,777 / 106,048 against
  captured 165,825 / 109,779 / 106,036 (header line added, trailing newline). Doc 1 Table 2 keeps its three
  rows with tab-separated cells ("Pork butchers 800 170 115 (14%)"); Table 3 keeps unit and total cost per
  line, with two rows run together on one line ("Travel ... Est £800 £40,000 Immigration Skills Charge
  £1,000/year £150,000"); Table 4 prints its three years on one line. Footnotes are inline after each page's
  text ("24 Q69 25 Q69 26 Q105 ..."). Transcripts: one paragraph per line, question-number markers intact,
  Q1-101 and Q102-168 all present.
- Provenance: capture AQ-04112_2026-10-13_1403.txt, sha256 f408e80a...; page said "Docket has been updated.
  Reload this page" at capture time. Source hashes in `notes/intake.json` match the capture.
- Reuse binding: D01 765b8cc3..., D02 1c54a2e5..., D03 261823fb... (`text/manifest.json`).
- Repeat-bundle check (2026-10-13): no match for these hashes or file names in 10.6, 10.7 or 10.8. Same
  family as aq-03950 and aq-03993 (committee report plus hearing transcripts, other inquiries).

## Doc 1 (D03) - Report, "Labour shortages in the food and farming sector"

- Written by: the Committee (Chair Neil Parish). Ordered to be printed 29 March 2022, published 6 April 2022.
- Structure: Summary; 1 Introduction (paras 1-4); 2 Current shortages (5-21, incl. pig sector 13-21);
  3 Responses (22-38: wages, temporary visas, when was Government warned); 4 Broader immigration policy
  (39-69: Skilled Worker Visa, English, costs, Shortage Occupation List, Seasonal Workers Pilot);
  5 Longer-term (70-75); 6 Conclusion (76-81); Conclusions and recommendations (15, each with its paragraph);
  Formal minutes (29 March 2022); Witnesses; Published written evidence (92 entries); list of reports.
- People lists: membership (11 MPs with party and constituency, "Kirtsy Blackman" misspelt there);
  formal minutes: present on 29 March 2022 Parish, Blackman, Davies, Gardiner, Hudson, Murray, Thomas;
  witness list for all four sessions with titles and Q ranges (26 Oct Q1-67 and Q68-101; 9 Nov Q102-146 and
  Q147-168; 16 Nov Q169-282; 14 Dec Q283-408).
- Tables: Table 1 temporary visas (poultry 5,500, deadline 15 Nov 2021, expiry 31 Dec 2021; HGV 4,700,
  1 Dec 2021, 28 Feb 2022; pork butchers 800, 31 Dec 2021, six months). Table 2 uptake (available /
  applicants / issued and % of available: 5,500 / 1,845 / 1,770 (32%); 4,700 / 135 / 130 (3%); 800 / 170 /
  115 (14%)). Table 3 Association of Labour Providers' cost of recruiting 50 workers for three years by the
  Skilled Worker route (unit and total cost per line; total £425,050, "equivalent to £2,834 per worker per
  annum, or £1.54 per hour"). Table 4 Seasonal Worker Visas 2022 / 2023 / 2024: 30,000 / 30,000 / 28,000.
- Rules stated: Skilled Worker Visa criteria (sponsor, RQF3, salary, English B1); general salary threshold
  £25,600; Shortage Occupation List entry reduces the salary requirement by 20%, other criteria unchanged;
  Seasonal Workers Pilot (6 months in any 12, edible horticulture only until 2022, no English requirement,
  four operators, cap 10,000 then 30,000 in 2021); Home Office visa charges £464 to £1,408.
- Dates: letter to Home Secretary 14 Sep 2021; inquiry launched 16 Sep 2021; MAC review Sep 2020, Home
  Secretary's reply Oct 2020; pilot's 2021 continuation announced 22 Dec 2020; 2022 confirmed 24 Dec 2021;
  NPA update January 2022; uptake data February / 3 March 2022; recommendation deadlines end of July 2022
  and six months from publication.
- Later facts only here: NPA January 2022 update (2,500 more sows, backlog still about 150,000, at least
  27,000 more culled, carcases "topping 95kg", processors not taking 30% of contracted pigs); BPC called the
  poultry visas a "success"; Foster's "fewer than 100 applications" for butcher visas in mid-December; a
  possible further 10,000 seasonal visas in 2022 "if necessary"; ornamentals admitted from 2022.
- Rounded prose beside figures: "12.5% structural vacancy rate" beside 500,000 of 4.1 million; "16% ...
  6,000" of a 40,000 workforce; "£2,834 per worker per annum" beside the itemised £425,050.
- Citation slip: footnote 19 gives Q66 for Nick Allen's "15% to 16%" (he said it at Q70; Q66 is Dear's).
- Coverage: read in full.

## Doc 2 (D01) - Oral evidence, Tuesday 26 October 2021, Q1-101

- Members present: Parish (Chair), Davies, Duffield, Hudson, Murray, Sturdy, Thomas.
- Panel I (in the room, Q1-67): Tom Bradshaw (NFU vice-president), Graeme Dear (chair, British Poultry
  Council), Derek Jarman (chair designate, British Protected Ornamentals Association; runs Hayloft Plants),
  Charlie Dewhirst (National Pig Association; header "Policy Adviser", himself "senior policy adviser").
  Panel II (video conference, Q68-101): Nick Allen (BMPA), James Russell (BVA), Ian Wright (FDF, his last
  appearance).
- "Written evidence from witnesses" header: NFU, BPC, NPA, BMPA, BVA, FDF (not the ornamentals body).
- Figures only here: butcher pay "£26,500 starting salary up to £35,000 to £40,000" (Q8); butcher training
  18 months; pig backlog building "about 15,000 a week"; NFU's need for 2022 "between 50,000 and 60,000"
  seasonal visas (Q30, Q34); nine-month visas "might add 10% or 15%"; 4.2 million jobs (Bradshaw) and
  "4.1 million to 4.2 million", "one in eight" (Wright); 1.4 million (and once 1.5 million) workers gone;
  ornamentals 15% short, 25% forecast; Allen's plant of 1,000 people "150 people short" (Q70), "about 15,000
  workers short" industry-wide, pig plants 6% to 7% below capacity, sheep 16%, beef 10% or 11%; vets 757
  registrations in 2019 against 250, 11.5% vacancies, 50 to 70 pig vets; unemployment 4.7%; agricultural
  inflation 22%.
- Forecasts made here: butchers' visas to be filled "extremely rapidly" (Q16, labour providers via
  Bradshaw); poultry visas "not going to work" (Q20); butchers arriving "after 20 November"; turkey shortage
  likely (Dear); visa turnaround "about five weeks".
- Proposals: Covid recovery visa for 12 months (Bradshaw Q10, Q54; Wright Q86); two-year visa (Dear);
  pilot made permanent, ornamentals included, more operators; VAT cut for plants to 12.5% (Jarman);
  MAC review of the food chain (Bradshaw Q50); poultry left out of the lifetime skills guarantee (Dear).
- Same first names: Derek Thomas (MP) and Derek Jarman (witness); Neil Parish and Neil Hudson.
- Coverage: read in full.

## Doc 3 (D02) - Oral evidence, Tuesday 9 November 2021, Q102-168

- Members present: Parish (Chair), Byrne, Sturdy, Thomas. Ends "we have lost a member".
- Panel I (in the room, Q102-146): Kate Nicholls (UKHospitality), Andrew Opie (British Retail Consortium),
  Tom Southall (Cold Chain Federation). Panel II (Q147-168): Ben Broadbent (Bank of England), Madeleine
  Sumption (Migration Observatory), Jo Swaffield (York; says she is a member of the Migration Advisory
  Committee, speaking personally).
- "Written evidence from witnesses" header: UKHospitality (misspelt), BRC, Cold Chain Federation.
- Figures only here: HGV tests "25,000 fewer" in 2020-21 against "about 42,000 a year"; pork storage scheme
  "approximately 15,000 tonnes", three to six months; frozen storage 80% to 85% full, creeping to 90% to
  95%; hospitality vacancy rate "50% higher" than pre-Covid, 20% of workers not back from furlough, sponsor
  licences taking "20 to 30 weeks", VAT back to 20% at the end of March; BRC food inflation 0.5%; Bank's CPI
  forecast 5% in Q2 2022; ONS fall of about 230,000 employed EU-born; 5.55 million settlement applicants.
- Statements about the visa schemes: Opie calls the poultry and HGV visas "three-month" visas, expects the
  poultry one to "work pretty well" and calls the HGV one "too little, too late" (Q127); Southall supports
  the Grant Thornton report's longer-term visa, 12 months (Q128).
- Slips in the text: the Chair says "It is the 13th today" (the hearing is dated 9 November); the Chair
  first uses "merry-go-round" (Q104), which Doc 1 credits to Opie.
- Same first names across hearings: Tom Southall here, Tom Bradshaw in Doc 2; Ian Byrne (MP) here, Ian
  Wright (witness) in Doc 2.
- Coverage: read in full.

## Shared ground (navigation only)

- Doc 1 quotes Docs 2 and 3 by Q number and repeats most of their headline figures: 500,000 vacancies;
  poultry 16% / 6,000 of 40,000; BMPA 15% to 16% and 10,000 to 12,000 butchers; 150,000 pigs, 8,000 culled,
  27,500 sows; 34% horticulture shortfall; 30,000 pilot visas; hospitality 10% / 200,000 and 15% to 20%;
  HGV 70,000 to 100,000 of 300,000; warehousing 10% to 20%. Those figures are never single-source.
- Single-source in Doc 1 (not in the transcripts): Tables 1-4, the salary threshold and 20% rule, written
  evidence figures, everything dated after 9 November 2021, the 16 November and 14 December evidence.
- Single-source in the transcripts: the lists under each document above.
- Same thing, different figures: workforce 4.1 million (Doc 1) and 4.2 million (Doc 2, Bradshaw); pilot
  announcement 22 December 2020 (Doc 1) and "23 December" (Doc 2); poultry visa length "six weeks" and
  "eight weeks" (Doc 2), "three-month" (Doc 3), deadline and expiry dates (Doc 1); seasonal visa need
  50,000 to 60,000 (Doc 2, NFU) and 50,000 to 80,000 (Doc 1, "the sector").
- Named in both transcripts with the same words: "lifetime skills guarantee" (Dear, Doc 2; Nicholls, Doc 3);
  the 12.5% hospitality VAT rate (Jarman, Doc 2; Nicholls, Doc 3); Grant Thornton's report (commissioners
  named by Opie in Doc 3 as "the NFU and FDF").
- Attendance: both hearings Parish, Sturdy, Thomas; of those, Sturdy was absent when the report was agreed.
