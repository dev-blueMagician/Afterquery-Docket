# aq-05000 - document map

Maintained by the caller from `text/` (all seven texts read in full, 2026-10-14). Navigation only:
questions quote the documents, never this map. Line numbers are `text/Dnn.txt` lines.

## Bundle

- What it is: "Surveys and polls" (page label "Easy or Hard only"). Seven survey reports on AI adoption:
  three UK government/ONS business surveys, one UK AI-sector labour-market survey, two Federal Reserve
  FEDS Notes on US AI-adoption surveys, one JRC report on GenAI in EU public administrations.
- Documents: 7; local ids are alphabetical by file name and differ from the page's Doc numbers:

| Page Doc | Local | Title (short) | Author / date |
| --- | --- | --- | --- |
| Doc 1 | D03 | Management practices and the adoption of technology and AI in UK firms: 2023 | ONS, released 24 March 2025 |
| Doc 2 | D07 | Understanding AI uptake and sentiment among people and businesses in the UK: June 2023 | ONS, released 16 June 2023 (correction 31 July 2024) |
| Doc 3 | D01 | Artificial Intelligence Adoption Research | DSIT (IFF Research + Technopolis), January 2026 |
| Doc 4 | D02 | AI Labour Market Survey 2025 | Gardiner & Theobald for DSIT, 2025 |
| Doc 5 | D05 | Monitoring AI Adoption in the US Economy (FEDS Note) | Jeffrey S. Allen, 3 April 2026 |
| Doc 6 | D04 | Measuring AI Uptake in the Workplace (FEDS Note) | Crane, Green and Soto, 5 February 2025 |
| Doc 7 | D06 | The adoption of Generative AI in EU public administrations | JRC (Mikalef, Medaglia, Tangi, Rodriguez Müller), 2026 |

- Gaps: none. Capture "7 of 7 read in full"; intake.json all `matches_capture: true`, no incomplete flags.
  Charts are flattened to label/number runs (D01 Figures 3-27, D02 Figures 5, 13-31): several are not
  readable as a unique mapping (D02 Figure 5 AI types; D01 Figures 20-22 middle values). Do not build
  a gold on a flattened chart unless its text states the value.
- Extraction spot-checks: plain-text capture; `docs/` = capture bodies (hash match). Tables checked:
  D03 Table 1 (conditional adoption), D05 Tables 1-3, D04 Table 1 (17 rows), D06 Table A1 (31
  durations sum to 1,122 min = "18 h 42 min"), D01 Tables 7-9. Footnotes present: D04 fn 1-7,
  D05 fn 1-12, D02 fn 1-10, D06 fn 1-12.
- Provenance: notes/intake.json (capture sha 56979369...). Capture page note: "Docket has been updated.
  Reload this page so its checks and buttons keep working."
- Page state at capture (14:08): "Still open on this set: Hard"; "Hard 0/5 · Medium closed · Easy 0/0";
  "Easy questions aren't open on this set — only a Hard question can still be submitted"; quick tests
  0 of 15 used; difficulty runs 15 of 15; 8 submissions left. Recent-mix line: 5 × Linking across
  documents, 2 × Document convention, 1 each Look-alike company / Wrong jurisdiction or scope /
  Look-alike measure / Part vs total / Unit or basis / Figure that must be computed.

## Doc 1 (D03) - ONS, MES 2023 technology and AI adoption

- Scope: MES wave 3, Nov 2023 - Mar 2024, ~55,000 businesses sampled; firms with employment >= 10 in
  production and services; excludes sections A (agriculture...) and K (financial and insurance);
  weighted to the population of firms (L64, L84-85). Adoption = used as part of methods or processes,
  "so excludes firms that have tested advanced technologies but are yet to implement them" (L70).
- Headline 2023: AI 9%, cloud 69%, specialised software 61%, specialised equipment 36%, robotics 4% (L72);
  AI projected 22% for 2024 (L74); 15% of 2023 non-adopters planned AI for 2024 (L299).
- Table 1 conditional adoption (L98-105): X=AI row 91 / 83 / 12 / 43 / 4. Text L96 says "83% of the
  firms using AI also used specialised equipment" while the table gives specialised software 83,
  specialised equipment 43 (internal inconsistency).
- Industry: services 9%, manufacturing 5% (L117); information and communication 27%, business services
  12%, textiles 11% (L147). Size: robotics 3% (10-19) vs 16% (250+) (L151).
- Management deciles: 88% vs 51% any technology (L179); AI top decile "twice the UK average" (L181);
  Table 2 predicted AI 2 / 8 / 10 at 10th / 50th / 90th percentile (L251-257).
- Barriers 2023: use cases 39%, cost 21%, skills 16% (L265); regulation 3% vs 7%, skills 12% vs 21%
  bottom vs top decile (L267). Would-be adopters: upgrade 69%, automate 42%, expand 24% (L329).
- MES-BICS link: BICS waves 92 and 98 (2023, 2,655 obs) and 105, 111, 117 (2024, 2,895 obs), unweighted
  (L359-361). ML data processing 9%, AI-enabled robotics 3% (L365). Follow-through 38% of planners vs
  27% of non-planners; deciles 48% / 31% / 17% (L399-401).
- Productivity: AI 6% bottom vs 10% top turnover-per-worker quartile (L424); log-point regressions
  17.7 (19%), 11.3 (12%), 36.0 (43.3%), 32.3 (38.2%), 14.9 (16%), 20.8 (23%) (L428-432).
- Glossary: AI, cloud, robotics, specialised equipment (excl. robotics), specialised software (excl.
  AI and general-purpose software), would-be adopters (L480-522).

## Doc 2 (D07) - ONS, AI uptake and sentiment, June 2023

- Correction 31 July 2024: Table 1 current/planned rows had been swapped (L11-21).
- OPN 4-14 May 2023 (GB adults 16+): 72% could explain AI at least partly (19% detail + 53% partial) vs
  PADAI 56% (10% + 46%) (L53, L120); 5% a lot / 45% a little / 50% not at all (L57, L126); 70+ 68% not
  at all; 34% used chatbots in past month (uses 50/33/19/19; 70+ 63/28; 16-29 58/29) (L142-144);
  impact 32% neutral, 6% / 5% extremes; PADAI 21/58/16 vs OPN 21/62/18 (L150, L172).
- KPMG: UK trust 34% (2023) vs 26% (2021); France 31, Canada 32, Australia 34, Germany 35, US 40,
  India 75, China 67; knowledge China 82, India 77, UK 32 (L176); 20% of UK respondents say employer
  uses AI (L210).
- BICS wave 80, 3-16 April 2023 (39,338 sampled, 9,399 responses, 23.9%) (L298): 16% currently use at
  least one listed AI application; spam filters 11, chatbots 4, facial recognition 3, voice assistants 1,
  personalised shopping 1 (L180); 78% "not applicable" (Figure 5); industries N/A: arts 92, transport
  89, construction 87; information and communication 63, wholesale/retail 71 (L216-226); <10 employees
  79% vs >250 48% (L228). Planned: 13% / unsure 15% / N/A 74% (L234-242). Table 1 base "% of businesses
  that selected at least one option excluding not sure and not applicable": 16% current, 13% planned.
- DCMS 2022 study: 15% adopted at least one AI technology, ~2% piloting, 10% planned (L200-208).
- Intentions among applicable: cybersecurity 35, efficiencies 35, personalised service 27, new product
  18 (L252). PADAI jobs 34% negative / 33% positive; WEF 50% growth / 25% losses 2023-2027 (L274);
  7.4% of England's employed at high risk of automation in 2017 (L278).
- OPN sample 4,961, 2,045 responded (41%) (L292); PADAI wave 2: 4,320 online + 200 telephone (L323).

## Doc 3 (D01) - DSIT AI Adoption Research (January 2026)

- Scope: CATI 12 Feb - 2 May 2025, 3,500 interviews, UK private-sector businesses with >= 5 employees;
  sector exclusions only O-Q and T-U; J, KL, MN oversampled; weighted by size and sector (L31-33,
  L163-207). 100 qualitative interviews, March - May 2025. Cognitive testing 20 interviews 20-27 Jan
  2025; pilot 50 interviews 3-5 Feb 2025 (L2144, L2264).
- Status (Figure 1, base 3,500): 16% use, 5% plan, 80% neither; 51% see AI as not relevant (L243-259).
  Size: large 36%, mid-sized 23%, micro 14% (small not printed) (L261). Sectors: J 43%, KL 21%, MN 23%;
  F 88%, G 86%, H 90%, I 88% neither (L263-265). London 20%; Scotland 84% neither (L267).
- B3 question counts piloting as current use: "currently using it (including piloting)" (L411, base 986
  "use AI or plan to"). Figure 3: NLP 61/19, CV 25/19, ML 15/19, hardware 8/18, agentic 5/13 using/planning.
- Figure 4 (base 700 current users): NLP 85, CV 35, ML 21, hardware 11, agentic 7, other 11; 50% >1 type;
  32% two, 12% three, 6% four or five; mean 1.7 (L436-469). Per-technology current-user bases 598 / 232 /
  169 / 86 / 59 (L531); planner bases 150 / 79 / 95 / 80 / 50 (L708).
- Staff using AI (base 700): average 30%; 77% under half, 21% over half; micro 38%, small 26%, medium 18%,
  large 20% (L775-811). Expected in 1-2 years: average 43% (L817).
- Frequency (700): constantly 53, weekly 27 (80% weekly), fortnightly 7, monthly 5, few times a year 3,
  rarely 2, DK 3 (L966-1003). Oversight 67/17/10/2/1/3 (L1012-1038).
- Spending 2024: 35% DK; 11% < £1,000; 16% £1,000-9,999; 7% > £10,000; mean £19,000, median £2,000 among
  those giving a figure; mean £22,000 among current users; 31% spent £0; 27% of users £0 (L1132-1134).
- Readiness: users (700) 13 + 41 = 54% ready, 23% unsure, 12% not ready; planners (219) 34 / 33 / 32
  (L1215-1270). Barriers (Figure 20): no use 71%, skills 60%, tools 48% then a flattened run; bases
  700 / 2,800 / 219 / 2,581 (L1306-1372). Significance: ethics 80, cost 76, regulation 72 (L1374-1377).
- Impact (700): productivity 75, processes 57; revenue up 12, no change 77, DK 11; productivity +56%
  (24/16/16), no change 35 (L1843-2001). D4 base 85.
- Appendix: Table 7 achieved by size 1,402 / 1,171 / 609 / 318; Table 8 38,983 called, 9% response,
  screen-outs "not aware of AI" 40 and "<5 employees" 351 (L2779-2843); Table 9 weighted by size
  1,794 / 1,400 / 245 / 62 (L2929-2935). Survey interviews averaged 20 minutes (L163).
- Glossary (L2123-2136): agentic AI examples "Autonomous Vehicles and Robotic Process Automation (RPA)".

## Doc 4 (D02) - AI Labour Market Survey 2025 (G&T for DSIT)

- Survey launched January 2025, sent to 3,940 organisations; 119 responded (3%); 2020 study 118; 20
  interviews (50 in 2020) (L168-186). Commissioned December 2024 (L147).
- Groups: commercial developers 66%, internal 14%, users/procurers 20% (L253-264); sizes micro 54 (45%),
  small 43 (36%), medium 14 (12%), large 8 (7%) (L272-282). Region counts sum to 130 (not 119) (L304-356).
- Five AI types same as Doc 3; NLP used 49% -> 83% ("surged by 34%" = points); 22% used all five
  (Group 1 23%, Groups 2-3 10%); agentic plan 57% (L437-528). Figure 5 values are not mappable.
- Uses "%" for point changes throughout (L770, L1248, L1863-1866); key-findings "programming ... fallen
  by 26%" vs body "16 percentage point reduction" (52 -> 36) (L1248 vs L1395).
- Vacancies, recruitment, pathways, international (38% of 69), skills gaps (60/38/36/36/34/27/23/15),
  training (88/52/40; Group 1 25 of 78 external, 51 of 78 internal; Groups 2-3 20 of 41 each), diversity
  (women 24 -> 20; firms with no women 53 -> 41; ethnic 27/27, 40 -> 41; non-UK 32 -> 27, 28 -> 38;
  disabled 7% of orgs, ~1% of roles; LGBTQIA+ 43% of orgs, 12.6% of roles in 32 orgs; neurodiverse 40%).

## Doc 5 (D05) - FEDS Note, Monitoring AI Adoption in the US Economy (3 April 2026)

- Cites Doc 6: "Crane, Green, and Soto (2025) examined 16 such surveys ... as of mid-2024 ... about 5 to
  40 percent" (L49).
- BTOS: ~18% of firms at end-2025 (new question since Nov 2025, "in any of its business functions"; old
  "producing goods or services") (L29, L55-56, L65); legacy growth "68 percent (3.9 percentage points)"
  year to September 2025 (L30, L65); ~9% planned at start of 2025, in line by June; >20% expect H1 2026
  (L65). 4-period moving average for all BTOS calculations (fn 2, L254). DK rate 10-11% (L187).
  1.2 million businesses, cohorts of 200,000 every 12 weeks, ~20,000 responses (L205-207).
- RPS (individuals, quarterly since August 2024): work GenAI ~41% (Table 2 "Any 40.7", YoY 9.7, 31.3%);
  daily 12 (2.9, 32); weekly 35.2 (8.9, 33.7); non-work ~50% (+26%, 10.4 pp) (L31, L75, L147-153).
- SBU (Atlanta Fed, Nov 2025, 1,032 responses): employment-weighted AI 78%, LLM 54% (Table 1, L79-86);
  equal-weighted 69.4% and 46.4% (fn 9, L268); employment weighting ~ share of labour force at adopting
  firms (L77). Seven AI categories (L218).
- Table 3 size distributions (L167-177); ~57% of firms have < 5 employees (L163).
- Industries (BTOS new): professional ~33, financial ~30 (L124); jumps new vs legacy 47% (10.6 pp)
  professional to 159% (7.5 pp) manufacturing; legacy median growth 76%; financial 127% (9.3 pp) (L124-126);
  fn 6: accommodation 8, wholesale 13, real estate 24, information 37. RPS: financial 63, professional 62;
  manufacturing growth 58% (14.5 pp); fn 7: accommodation 21, wholesale 48, real estate 58, information 70.
- Other: Gallup mid-2025 8% daily; Hartley et al. Dec 2025 33% of GenAI-using workers daily; SBU 35%
  up to 1 hour, 29% 1-5 hours (L143-145). Best-source conclusion (L201).

## Doc 6 (D04) - FEDS Note, Measuring AI Uptake in the Workplace (5 February 2025)

- 16 surveys, 17 table rows (firm rows 1-7, individual rows 8-17) (L32, L46, L64, L89-107).
- BTOS: 5% (two-week, firm-weighted, Sep 2023 - Feb 2024, 164,500 firms); 20% (employment-weighted,
  six-month, specific types); fn 2: firm-weighted six-month 8.8%; SE ~0.05 pp (L49-60, L157).
- Firm rows: NY Fed 350 firms Aug-24 25% service / 16% manufacturing (~80% of AI users use GenAI);
  Richmond 211 firms 34%; Dallas 363 firms 38.30% AI / 19.60% GenAI; Chamber 1,100 firms 40% (note quotes
  "40% of small businesses ... use generative AI"; 23% in 2023); ABA 440 firms 2023 10.90% (fn 6: 15% ->
  21% "from their 2022 and 2023 surveys").
- Individual rows: RPS Aug-24 3,216 people 28% GenAI; Pew Feb-24 20% (ever used ChatGPT for tasks at
  work); Morning Consult Jan-24 44% AI; Humlum/Vestergaard 36%; Conference Board 31%; JetBrains 84.20%;
  GitHub 97%; Alan Turing Institute (Bright et al. 2024) 938 people Nov-23 22% (UK public servants);
  National Bank of Slovakia 45%; Wharton 72%.
- Growth (L79, fn 4-7): Chamber 73% (23 -> 40), BTOS 78.4% "annualized" (3.7% Feb 2024 -> 6.6% Sep 2024),
  ABA 38% (15 -> 21), Pew 145% (8 -> 20, Mar 2023 -> Feb 2024). These growth figures do not all
  reconcile with their endpoints.
- Conference Board: management unaware for 29% of respondents (L74). Richmond sample: < 10 workers 20% of
  sample vs ~80% of population (L60).

## Doc 7 (D06) - JRC, GenAI adoption in EU public administrations (2026)

- 8 case studies, 31 semi-structured interviews, March - November 2025, two researchers, average stated
  35 minutes (Table A1 durations sum to 1,122 min = 36.2 average) (L228-234, L1242-1379).
- Cases: Copenhagen 5, Helsinki 4 (860-employee Copilot trial), German BMZ 4, Greek Presidency 3 (incl.
  Ministry of Digital Governance, University of the Aegean), Italian INPS 3, DG DIGIT 3, Norwegian NAV 4,
  Catalonia 5 (L240-276, L1253-1309).
- Statistics quoted: MIT NANDA 2025 90%; JRC early-2024 survey 30% of public managers using ChatGPT or
  similar, 44% planned (L330-331); Gartner < 25% by 2027; Deloitte 2024 56% and 78%; SAS 13% daily,
  14% none (L492). PSTW > 200 GenAI cases (L315). Bright et al. (2025) cited (L531, L556, L1085) = the
  Alan Turing Institute survey listed in Doc 6 as Bright et al. (2024).

## Shared ground (navigation only)

- Same survey in two documents: BTOS and RPS (Doc 6 -> Doc 5; Doc 5 cites Doc 6); BICS (Doc 2 wave 80;
  Doc 1 waves 92, 98, 105, 111, 117); the Turing UK public-sector survey (Doc 6 row; Doc 7 citation);
  Conference Board 2023 (Doc 6 numbers; Doc 5 cites without numbers).
- Same taxonomy: Doc 3 and Doc 4 use the same five AI types. Doc 3 and Doc 4 both DSIT-commissioned 2025.
- UK business AI adoption figures: Doc 2 BICS April 2023 16%; Doc 2 DCMS 2022 15% (+2% piloting);
  Doc 1 MES 2023 9% (>= 10 employees, excl. A and K, excludes testers); Doc 3 2025 16% (>= 5 employees,
  piloting counted as use).
- US firm adoption: Doc 6 BTOS 5% / 8.8% / 20%; Doc 5 BTOS 18% (new question), legacy +3.9 pp (68%);
  SBU 78 / 69.4.
- Worker GenAI: Doc 6 RPS 28% (Aug 2024); Doc 5 RPS 40.7 (Nov 2025), YoY 9.7.
- Look-alike numbers across documents: 16% (Doc 2, Doc 3), 22% (Doc 1 projection, Doc 4 all-five, Doc 6
  Turing), 9% (Doc 1 AI, Doc 5 planned, Doc 3 response rate), 78% (Doc 5 SBU, Doc 2 N/A, Doc 7 Deloitte).
