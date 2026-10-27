# aq-03120 - document map

Maintained by the caller and three `bundle-mapper` runs from `text/`. Navigation only: where things are,
not what to ask. Questions quote the documents, never this map.

## Bundle

- What it is: six submissions to the New Zealand Commerce Commission's Preliminary Issues paper ("PIP",
  10 August 2023) for its market study into personal banking services: three large banks (ANZ, ASB, BNZ),
  a fintech (Aera), a consumer body (Consumer NZ) and a farm lobby (Federated Farmers). Neither the PIP
  itself nor Westpac's or Kiwibank's submission is in the bundle.
- Documents: 6; local ids equal the task page's Doc numbers here (D01 = Doc 1 ... D06 = Doc 6).
- Gaps: none in the capture ("6 of 6 read in full", every `gap_characters` 0). Charts are absent as images;
  where a chart's data labels survived as a bare number run this is noted per document. BNZ (D04) carries
  66 confidentiality redactions printed as "[ ]".
- Extraction spot-checks (2026-10-11): every `text/Dnn.txt` equals its `docs/` original line for line except
  seven ellipsis characters normalised to "..." (D02 L169; D03 L47, L467; D04 L129, L442, L691, L850). Do not
  quote across those spans. No page structure (plain text); D06's bar-chart labels checked against its prose
  (79 percent with a mortgage vs "No Mortgage" 21.2%; satisfaction 56 percent vs "Total, Banks" 56.3%).
- Provenance: `notes/intake.json`, capture sha e96c8951..., all six `matches_capture: true`. The capture
  noted a page reload banner ("Docket has been updated. Reload this page...").
- Reuse binding: source hashes in `text/manifest.json`. New bytes: no earlier task shares them. Same family
  (parties' submissions on one NZCC paper): aq-02940, aq-03066.

## D01 - Aera submission (Doc 1)

- Written by: Aera, a fintech "launched in 2023" (L6). Dated 14 September 2023 (L5), a week after the others.
- Sub-headings (L12-18): Open Banking; Service and Experience vs Profitability over time; Broker Closure
  Rates and Competitive Tendering; Product Innovation/Sandbox. L19 lists barriers it does not cover (fixed
  rate break costs, customer inertia, cashbacks).
- Only figure: "Over the last decade, 30% of bank branches closed [KPMG, 2010-2020 KPMG Financial
  Institutions Performance Surveys]" (L35).
- Definitions: broker "closure rate" = applications settled vs applications received (L43); three "tenants"
  of open banking: account information, transaction information, payment initiation (L26).
- Coverage: full (69 lines read).

## D05 - Consumer NZ submission (Doc 5)

- Written by: Consumer NZ (contact Jon Duffy), 7 September 2023. Answers PIP questions 1, 2, 7, 8, 13, 15,
  17, 18, 22, 23, 25, 26, 29 only.
- Figures (line): four large banks "around 85% of the lending market" and "a 90% share of bank deposits",
  attributed to the Reserve Bank (L65); survey: 74% agree profits show overcharging (L67); savings-rate
  satisfaction 31 / 20 / 25 / 24% (L79); Sentiment Tracker sample "at least 1000" (L90); "1 in 7" had a
  problem in 12 months (L95); trust in banks "largest drop of nearly 20%" (L98); switching ease 41 / 32 / 27%
  (L122); "Only 4% had switched primary banks in the previous 12 months and 81% ... 5 or more years" (L124);
  75% of switchers found it easy (L126); UK "just 3%" switch each year, display rule 2018 (L141); BNZ 4.99%
  one-year rate via brokers vs advertised 6.45%, rivals 6.49% to 7.49% (L155); switching "still takes 5 days"
  (L157); open banking work began 2017, Minister's request 2019 (L166-171); FinTechNZ 2022: big four "85
  percent of the market", 27 percent of fintechs export (L177-178); Dutch name check 2017: 81% drop in fraud,
  67% fewer misdirected payments; UK 2020: 35% drop (L193).
- Lists: top five switching deterrents (L119); fintechs not yet in NZ: Revolut, Zeal, Jude, Douugh (L173);
  UK top-rated banks 2023: Monzo, Starling Bank, First Direct (L109); four "lagging" examples under Q26
  (real-time payments, name and account matching, least cost routing, other products) (L191-203).
- Scope position: credit cards should be a focus area; if so, personal loans too (L49-53).
- Images 1-3 are absent (captions only). Coverage: full (215 lines read).

## D06 - Federated Farmers submission (Doc 6)

- Written by: Federated Farmers of New Zealand, 7 September 2023. Sections: 1 Introduction, 2 Agricultural
  sector lending, 3 Banking surveys (May 2023 survey), 4 Comment on the PIP.
- Sector figures: lending "exceeds $63 billion", 1 point = "more than $63 million per annum" (L51); $12.1
  billion Jan 2000 to $63.4 billion July 2023 (L66); dairy "around three-fifths", $37.5 billion July 2023, peak
  $41.5 billion July 2019, $36.4 billion March 2023 (L70).
- May 2023 survey: 79 percent have a mortgage, up 2 points (L94); average mortgage $4.2 to $4.3 million,
  median $2.5 to $2.8 million (L96); average mortgage rate 6.29 to 7.84 percent, +155 bp since Nov 2022, +405
  bp since May 2021 low (3.79 percent) (L104-106); interest cost $163,300 to $337,800 (L51, L106); share
  paying under 5 percent 2.1 (10 in Nov 2022, peak 91 in May 2021), over 10 percent 1.8 vs 0.3 (L108-109);
  overdraft: 74 percent have one, average limit $293,000 (a $35,800 decrease), median $150,000 (L114); rate
  8.59 to 10.07, +148 bp, +379 since Nov 2021 low (L117); 0.3 percent under 5 percent, 34 percent over 10
  percent, up from 14 (L124); satisfaction 56 percent, down 3 points (L127); undue pressure 24 percent, up 6
  (L134); mental wellbeing 44 / 47 / 9 (L140); conditions easier 3.1, tougher 31 (L141); communication 53
  percent (L143); budgets 68 and 41 percent (L152-155).
- Chart label runs that survived: Figure 5 mortgage bank shares "32.2% 15.3% 18.9% 22.3% 10.1% 3.5% 21.2%"
  for "ANZ ASB BNZ Rabobank Westpac Other No Mortgage" (L119; the six bank shares sum to 102.3); Figure 10
  satisfaction by bank, three series over "Other Banks Westpac Rabobank BNZ ASB ANZ Total, Banks" (L136-137);
  Figure 14 communication by bank, same layout (L152-153). Figures 8 and 12 have axes only.
- Concentration (L181-183, fn 4 = RBNZ Dashboard, Asset Quality, March 2023 quarter): "more than 98 percent
  of agricultural loans are held by five banks (ANZ, BNZ, Rabobank, ASB, and Westpac)", remainder with "a
  further 10 banks" (mostly TSB and Heartland); top-five shares housing 95, consumer 82, business 95 percent.
- Events: ANZ acquired National Bank in 2003, which had acquired the Rural Bank in 1988 (L110); a "major
  rural lender" withdrew transaction accounts in 2021 (L192, fn 5 URL names Rabobank); Fonterra forecasts
  25 May, 4 August, 18 August 2023 (L99); regional banking hubs "page 74 of the preliminary issues paper"
  (L191); survey history: began May 2015, quarterly, six-monthly since 2017, next November 2023 (L83-91).
- Coverage: full (210 lines read).

## D02, D03, D04 - bank submissions

Per-document maps: [doc-map-D02.md](doc-map-D02.md) (ANZ), [doc-map-D03.md](doc-map-D03.md) (ASB),
[doc-map-D04.md](doc-map-D04.md) (BNZ). See those files for coverage ledgers.

## Shared ground (navigation only)

All six documents are fully read (D01, D05, D06 by the caller; D02-D04 by one mapper each, every line, ledgers in
the per-document files). Locations only; relationships are in [hooks.md](hooks.md).

- Same organisations' results quoted for different periods: Kiwibank home lending growth, first half of FY23 (D04
  L156, fn 7 L161) and FY23 (D03 L570); Heartland retail deposit growth lead, Q1 (D04 L214, L721) and Q1 and Q2 (D03
  L25, L585); Co-operative Bank mortgage growth, six-month update (D04 L200) and FY23 (D03 L26, L599; D04 L200).
- Word-for-word repeats (not single-source): SBS home lending "approximately 12% from $3.6 billion to $4.0 billion",
  "closer to 3.5%" (D03 L18, L585; D04 L216-217); TSB "1.6x system" (D03 L24, L585; D04 L197); Kiwibank $225 million
  (D03 L14, L571; D04 L129); KPMG return on equity 13.40% vs 15% (D02 L317; D04 L1099); Pepper Money / HSBC,
  1 September 2023 (D02 L681; D03 L980; D04 L232, L1478); Revolut launch (D02 L665 year only; D03 L1160 and D04 fn
  27, fn 204 with the day); deposit compensation $100,000 (D03 L342; D04 L507); 365-day payments May 2023 (D04 L359,
  L847; D02 fn 51).
- Single-source dated facts: ANZ Simple Switch pilot, April 2023, six weeks (D02 L753); CCCFA switching exception,
  May 2023 (D02 L752); ICBC registered 2020 (D02 L680); Dosh and Square One 2021 (D02 L676-678); Harmoney 2014,
  InvestNow 2017 (D03 L1158, L818); Resimac 2012, Heartland mortgage exit 2013/14 and re-entry 2020 (D04 L228,
  L1476); HSBC exit announcement June 2023 (D04 L1506); Kiwibank share 7.5% (D02 L183) and goal 10% (D04 L129).
- Bank groupings: "five larger banks" incl. Kiwibank (D02 L183; D03 L11; D04 L123); "four large banks" named (D05
  L65); five farm lenders ANZ, BNZ, Rabobank, ASB, Westpac plus "a further 10 banks" (D06 L181-183); 16 switching
  participants, four via agents (D02 Table 2, L797-808); "27 registered banks and 16 registered non-bank deposit
  takers" (D04 L113); Nelson Building Society as a non-bank deposit taker (D04 L225) and a switching participant
  (D02 L803); hub pilot "six banks" (D02 L514; D03 L889), "seven small towns" (D04 L1244).
- Parallel own-bank measures: digital use, ASB 90% June 2023 (D03 L1117), BNZ 87.9% enabled and 81.9% active July
  2023 (D04 L1223), ANZ 61.7% of sales (D02 L499); broker share, ANZ 57% (D02 L564), all lenders 50% (D04 L587);
  switching time, five business days (D04 L418), five to 10 working days (D02 L790), "5 days" (D05 L157).
- Statements that disagree: Revolut "not yet" able to serve New Zealand (D05 L173) vs launched 3 July 2023 (D03
  L1160); Pepper Money in New Zealand since 2011 (D03 L980; D04 L1478) vs "2019/20" (D04 L230).
- Chart data: none survived in D02-D04 (captions or redactions); D06 keeps three label runs (see D06 above).
- Financial year-ends that can be read from the text: Kiwibank and Heartland 30 June (D04 L161, L214); SBS 31 March
  (D03 L18; D04 L216); Co-operative Bank half-year 30 September (D04 fn 13). ASB, BNZ, ANZ year-ends are not stated.
