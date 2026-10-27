# aq-02157 - document map

Maintained by the caller from `text/` (and `docs/` for layout issues), 2026-10-08.
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map. Line numbers are `text/Dnn.txt` lines.

## Bundle

- What it is: five UK public-policy documents on tobacco and vaping (2023-2024): the smokefree
  generation / youth vaping consultation and its government response, and the tobacco pack-insert
  (quit-message) consultation, its consultation-stage impact assessment and its government response.
- Documents: 5; local ids are alphabetical by file name and differ from the task page's Doc N:
  D01 = Doc 2, D02 = Doc 1, D03 = Doc 4, D04 = Doc 5, D05 = Doc 3 (notes/intake.json, text/manifest.json).
- Gaps: none. Capture says "5 of 5 read in full (422,952 characters)"; intake.json marks every document
  complete and matching the capture. The caller read all five documents in full on 2026-10-08.
- Extraction spot-checks (2026-10-08): non-blank lines of D01, D02, D04 and D05 are identical to docs/
  after whitespace normalisation. D03 (Doc 4) differs only by Unicode normalisation: "1½ / 3½" in the
  five summary sheets became "11⁄2 / 31⁄2" and Annex B's math-italic symbols became plain letters
  (docs lines with 𝑀𝑛𝑠 etc.). Quote those lines from docs/, never from text/D03.txt. Tables render as
  pipe tables in D01/D02 (Doc 2 Tables 1-53, Doc 1 Table 1); D03's summary sheets and stakeholder tables
  are flattened one cell per line.
- Provenance: notes/intake.json (capture AQ-02157_2026-10-08_1559.txt, sha256 f1a4e6fc...).
- Reuse binding: source hashes in notes/intake.json; reuse while unchanged.

## D02 = Doc 1 - Creating a smokefree generation and tackling youth vaping (consultation)

- Written by: DHSC with the Scottish Government, Welsh Government and NI Department of Health; UK-wide.
- Dates: command paper 4 October 2023 (L56); consultation closes 6 December 2023 at 11:59pm (L746);
  launch date not printed here (Doc 2 L98: 12 October).
- Smoking statistics: deaths ~80,000 UK = 64,000 England, 8,300 Scotland, 5,600 Wales, 2,200 NI (L32-40,
  rounded); ONS Adult smoking habits in the UK 2022: 6.4 million smokers, 12.9% UK; 12.7% England,
  14.1% Wales, 14.0% NI, 13.9% Scotland (L42-50; order England, Wales, NI, Scotland).
- Youth vaping: 20.5% of GB children tried vaping 2023 (L60); NI 21.3% (L60); fruit 60%, sweet 17% (L310);
  69% of 11-17 vape users mainly disposables (L508); NI 85.7% (L508); pouches 0.26% (L592), NI 4.8%.
- Flavour options (L318-342): how to restrict: Option 1 descriptions (example New Zealand, L322);
  Option 2 ingredients (example the Netherlands, L324-326); Option 3 characterising flavours (UK 2020
  menthol ban and Finland, L328-330). Which flavours: Options A/B/C (L334-340).
- Affordability: at least £7.87 duty per 20 cigarettes; smoking 3x vaping; ~£670/yr saving (L646);
  Table 1 vape unit costs: disposable £6, pre-filled pod kits £12, vape kits £40 (L654-660); Elf Bar £5/£8.
- Enforcement: max fine £2,500 (L700); FPN options £100/£200/Other (L720-738).
- Definitions: disposable = not rechargeable, not refillable, or neither (L494, L520).
- Coverage: full.

## D01 = Doc 2 - Smokefree generation and youth vaping consultation response (2024)

- Written by: DHSC with the devolved administrations.
- Figures: 80,000 deaths; >80% started before 20 (L30) / four in 5 before 20 (L80); £17bn England
  = 6.9p per £1 income tax; excise ~£10.2bn (L30, L82); 30 quit attempts (L80); 12.9% in 2022 (L417).
- Process: launched 12 October (L98), 8 weeks 12 October-6 December 2023 (L142); 118,756 received,
  90,835 bots, 27,921 analysed (L142); 896 organisations, 27,025 individuals (L144); 307 TI (L213);
  27 free text boxes (L195). Tables 1-3 respondents by nation/region/age (L150-191).
- Results (all respondents who answered): age of sale 63.2/32.2/4.6 (L267-271); proxy, notices, scope;
  flavours 47/51/2 (L509-513); Table 4 flavour-method combinations (L549-567, sums to 100.0);
  Table 5 (L607-616); POS 68.3/31.7; packaging Table 6; disposables 79.6/18/2.4 and 69/26.2/4.9;
  price 42.2/50.4/7.4; FPN 88.3/8.8/2.8; FPN levels (L1304-1352).
- Decisions: £100 FPN (L1380); no retail licensing scheme (L415, L800); disposable ban (L1190);
  vape age of sale unchanged (L433); duty at least £8.46 per 20 (L1204).
- Annex 1 (L1440-1914): individual and organisation percentages by nation for each closed question
  (Table 17 shows only single options plus all three; "not all option combinations are shown").
- Annex 2 (L1916-1954): international vaping-restriction tables 53a/53b.
- Note L473: "Denmark, Finland, the Netherlands and other EU member states have prohibited certain
  flavours of e-liquids" (does not distinguish their methods).
- Coverage: full.

## D05 = Doc 3 - Mandating quit information messages inside tobacco packs (consultation, OHID)

- Figures: ONS Adult smoking habits in the UK: 2021: UK 13.3%; 13% England, 14.8% Scotland, 14.1% Wales,
  13.8% NI (L68-76; order England, Scotland, Wales, NI); ~6.6 million (L78); deaths 64,000 / 8,260 /
  5,583 / 2,200 (L80-86, unrounded vs Doc 1); 72% lung cancer, ~4% admissions, £21bn (L88).
- Evidence summary (Thrasher, Moodie) L128-144; themes L146-162; Canada 8 cards (L196), June 2022 13
  designs (L218); 10 suggested conditions (L258-278); transition options 3/6/12 months (L306-312).
- Options 1-5 with rounded IA costs and quitters (L459-513): Option 2 31,525 quitters, £1.6bn;
  Option 3 19,104, £972m; Option 4 15,920, £802m. Odds-ratio definition L473.
- "We will aim to publish a response 12 weeks after the closing date." (L577); closing date not printed.
- Coverage: full.

## D03 = Doc 4 - Tobacco pack inserts consultation-stage impact assessment (May 2023)

- Summary sheets L9-579 (flattened; Option 3/4 sheet costs 212.4/17.2/4.6 and 152.4/10.5/2.4 differ from
  the detailed sections 180.7/14.6/3.9 and 129.7/8.9/2.4 and from Doc 3's rounded figures).
- Effect size (Option 2) L1378-1411: 13.3% x 53,188,204 = 7,074,031 smokers; 16% -> 1,131,845; 29% ->
  329,367 attempts; OR 1.57 adjusted to 1.46 (fn 46); 479,558 (42%), 150,191 more; 14% -> 21,177 a year;
  transition halves year 1 (10,588); year 2 20,937; total 31,525; 23,437 life years (L1458).
- Prices/duty: £12.61 average 20-pack; retailer margin 5% -> £0.60 (L1597, fn 68 formula); duty table
  October 2021 (L1795-1810: £262.90 per 1,000 + 16.5%, MET £347.86 per 1,000; HRT £351.03/kg);
  £7.98 per average pack using £294.72 per 1,000 (L1811); HRT £10.53 per 30g (L1815).
- Other: 2019 14.1% -> 2021 13.3% UK, "Declines were seen across all constituent countries" (L638);
  Smokefree 2030 target "5% or less by 2030" (L935); vape margin 10% (L3373); one-year implementation
  period (L1019, L1411); sensitivity L3118-3330 (text and Table 1 disagree); Annex B life years.
- Many internal inconsistencies (e.g. Option 3 "a total of 23,874" vs 19,104; 50.5% vs 50.8%).
- Coverage: full (Annex B tables read; formulas only in docs/).

## D04 = Doc 5 - Mandating quit information messages inside tobacco packs (government response)

- Dates: consultation ran 8 weeks, 14 August-10 October 2023 (L38, L146-148).
- Figures: ONS 2023 ~12% (L20, L72); 150,000 additional quit attempts and 30,000 quits "over the first
  2 years" (L42, L358); £48/week (~£2,500/yr) saving (L90); 67% GB support for inserts (L140).
- Methodology: 36 questions (15 MC, 21 free text, 14 IA) (L194-200); percentages rounded to whole numbers
  (L208); 13 TI responses (L214); 213 responses = 57 organisations, 117 personal, 39 professional (L220-226).
- Results L236-786 (e.g. conditions 121/118/114 respondents = 57/55/54% of 213; transition 40/37/24%).
- Decisions: two phases; slide and shell for cigarettes, flap for HRT (L48-66, L560-580); no retailer
  exemptions (L488); Tobacco and Vapes Bill list includes retail licensing powers (L118).
- Coverage: full.

## Shared ground (navigation only)

- ONS adult smoking prevalence series: 2019 UK 14.1% (D03 L638); 2021 by nation (D05 L68-76) and UK
  13.3% (D05, D03); 2022 by nation (D02 L42-50) and UK 12.9% (D02, D01 L417); 2023 UK ~12% (D04).
  The two nation lists are printed in different orders.
- Smoking deaths by nation: D02 (rounded) vs D05 (unrounded); 80,000 in D01, D04.
- Excise duty per 20 cigarettes: D03 table (Oct 2021) and £7.98; D02 £7.87; D01 £8.46.
- Pack-insert IA estimates restated in D05 (L459-513, rounded) and D04 (L42, L358, "first 2 years").
- Support polls: inserts 68% (D03 L712, ASH 2022) vs 67% (D04 L140); POS 74% England (D02 L408) vs
  74% GB (D01 L94).
- Flavour-method examples (D02 L320-330) vs D01's lumped country sentence (L473) and results (Table 4).
- Retail licensing: not proposed (D02 L148), no plans (D01 L415, L800), bill takes powers (D04 L118).
- Consultation process: smokefree 12 Oct-6 Dec 2023 (D01; D02 close only); pack inserts 14 Aug-10 Oct
  2023 (D04 only); D05 promises a response 12 weeks after closing.
