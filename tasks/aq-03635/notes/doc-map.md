# aq-03635 - document map

Maintained by the caller from `text/`. Navigation only: where things are, not what to ask.
Questions quote the documents, never this map. Line numbers are those of `text/Dnn.txt`.

## Bundle

- What it is: eleven papers from the NZ Commerce Commission's 2019 market study into the retail fuel
  sector: the draft report's executive summary (20 August 2019), nine written comments on it (dated
  13 September 2019 or undated) and one post-conference submission (11 October 2019).
- Documents: 11; ids from `text/manifest.json`. Local ids are alphabetical and differ from the task
  page's Doc numbers:

  | Local | Doc | Author | Chars |
  | --- | --- | --- | --- |
  | D09 | 1 | Commerce Commission, draft report executive summary | 42,015 |
  | D01 | 2 | NZ Automobile Association (NZAA / AA) | 10,013 |
  | D03 | 3 | BusinessNZ | 7,895 |
  | D04 | 4 | Gull New Zealand (redacted version) | 9,961 |
  | D06 | 5 | Mobil Oil New Zealand | 13,352 |
  | D07 | 6 | Motor Trade Association (MTA) | 66,640 |
  | D08 | 7 | Refining NZ | 11,633 |
  | D10 | 8 | Waitomo Group | 18,262 |
  | D11 | 9 | Z Energy | 102,515 |
  | D02 | 10 | BP New Zealand (BPNZ) | 131,217 |
  | D05 | 11 | Major Electricity Users' Group (MEUG) | 8,151 |

- Gaps: none in the capture (11 of 11 read in full, gap 0 for every document). Charts carry no data
  except where their labels survive as text (D11 two waterfalls, D02 two site-count charts and two
  axis-only charts). D02 has many redactions that leave a blank where a figure stood; D04 one
  redacted block; D11 "[REDACTED]" paragraphs. No figure used may come from a redacted spot.
- Extraction spot-checks: plain-text capture, so no page counts. Checked against the capture file:
  D11 Appendix 2 (tab-separated rows, header rows printed after each table: "$m 2015 2016 2017 2018"
  and "$m 2016 2017 2018 2015"), D11 footnotes 6 and 40, D09 footnote 3, D02 footnote 2. All match.
- Provenance: `notes/intake.json` (capture sha 848628885a8c...; every document `matches_capture`, not
  incomplete). Capture note: the page asked for a reload ("Docket has been updated").
- Reuse binding: source hashes in `text/manifest.json` as of 2026-10-12. Not a repeat bundle (the
  fuel-study file names occur in no earlier capture in 10.6, 10.7 or 10.8). Same family as aq-03120
  (banking), aq-03423 (mobile), aq-03557 (grocery), aq-02940 (interchange), aq-03066 (fibre).
- Coverage: all eleven documents read in full by the caller on 2026-10-12.

## D09 (Doc 1) - Commission draft report, executive summary

- Dated 20 August 2019. Associated documents table (lines 13-22): 12 Dec 2018 guidelines and statement
  of process, 31 Jan 2019 preliminary issues, 18 Apr 2019 two working papers. X129 (388): comments due
  13 September 2019; final report "published on 5 December 2019"; X17 "by December 2019".
- Volumes X3 (34): ~3.2bn L petrol, ~3.6bn L diesel a year; service stations and truck stops take about
  98% of petrol and 73% of diesel; "more than $10 billion".
- Refinery X25 (87): Marsden Point ~58% of petrol, 67% of diesel. X26: majors import to Mt Maunganui,
  Wellington and Lyttelton; over 90% of supply. X28: premium about 23% of petrol.
- Sites X29-X30 (104-106): more than 1,300 sites, 20 brands; ~65% non-major brands with 20% of volumes
  "as at March 2019". X31: TOSL building at Timaru, trading from 2020.
- Price components X39 (137-138), 1 July - 31 December 2018, regular 91: board $2.20, discount 6c, taxes
  "roughly 97 cents", fuel 83c, gross margin 34c. X41: Australia December 2018 NZ$1.56 (98c pre-tax),
  margin 24c. The graphic itself (Figure X3 = Figure 2.2 of the report) is not in the text.
- Profitability X45 (157-164): margins doubled since 2008; returns on new investment 20% a year over 5
  years vs reasonable return "(6.9 - 8.6%)" and comparators "less than 10%"; q of 1.5 - 1.8.
- X47 (166) and footnote 3 (178): Z's May 2019 presentation, "35 new sites", capacity +2%, petrol -1.5%;
  "For the year ended 31 March 2019" (Z's financial year end).
- Discounts X60 (200): 41% of sales discounted in 2018 (22% in 2011); average discount 2c to 11c (petrol),
  2c to 16c (diesel). X63: 10c discount goes with 1 - 2.7c (91) and 2.4 - 4.9c (diesel) board rises.
- X67: fuel cards about a quarter of retail-site volumes. X74 (230): premium 13-15c above regular now,
  7-8c in 2011. X93: refinery capacity on a three-year average of market shares. X97: ports under
  coordination up to 40% of the time. X110.2 (331): contracts commonly 10 to 15 years.
- Options X124-X126 (368-380): contractual freedom; wider infrastructure participation; refinery
  allocation; less information sharing; premium prices on boards; better information.
- Hedges: most findings are "we currently consider" / "appear"; X43.1 "appear to have been making".

## D01 (Doc 2) - NZ Automobile Association

- 13 September 2019. 1.7 million Members; road users pay over $3 billion in taxes.
- Lines 17-19, 30-34: queries Figure 2.2. ETS 5.49 / 5.62 / 6.36 cpl (91 / 95 / diesel) for 1 July -
  31 December 2018; excise rose 3.5cpl on 30 September; total taxes incl. GST $1.0235 at $2.20 (91),
  $1.0431 at $2.34 (95), $0.2751 at $1.55 (diesel, "similar to the figure"). Figure 2.2 puts 95 and 98
  importer cost 2cpl above 91; Hale & Twomey about 4cpl during 2018.
- Positions: supports terminal gate pricing (TGP), real-time price data, premium prices on boards.

## D03 (Doc 3) - BusinessNZ

- 13 September 2019. Footnote 2 (16): its 15 June 2018 submission asked for "at least 8 weeks" to
  comment on a draft report. Footnote 3: draft report paras 8.44 (page 239), B12 (page 250).
- 76,000 employers and businesses. No fuel figures.

## D04 (Doc 4) - Gull

- Undated, redacted version. Supports a TGP regime; lists five design points (22-27). Not in the B&L
  system, does not see joining it as a way into the South Island.
- Line 47: third price sign at one Auckland outlet about $7,500; other regions + $1,000 a site; about
  $720,000 for its network. Opposes all-product price boards. Line 30: May 2017 study.

## D06 (Doc 5) - Mobil

- 13 September 2019. About 200 staff, about 1,000 at branded stations, $200 million since 2012, about 170
  sites, "six bulk-storage terminals in Tauranga, Wellington, Christchurch and Bluff" (19).
- Line 76: the report's list of proprietary terminals: BP 8 (Auckland, Mount Maunganui, New Plymouth,
  Napier, Wellington, Nelson, Lyttelton, Dunedin); Mobil 5 (Mount Maunganui, Wellington, Lyttelton,
  Christchurch (Woolston), Bluff); Z 7 (Mount Maunganui, Napier, Wellington, Nelson, Lyttelton, Timaru,
  Dunedin). Line 79: Mobil lifts from BP's Dunedin terminal.
- Positions: for TGP-style disclosure and premium prices on boards (about 12 months); against limits on
  exclusivity or contract length, forced open access and divestment. Wants "importer margin" and "gross
  margin" off the graphic (117-121).

## D07 (Doc 6) - Motor Trade Association

- 13 September 2019; letter (paras 1-13) then Schedule 1, a table of responses keyed to draft-report
  paragraph and page (281-541). Preliminary-issues submissions "due on 21 February 2019"; "424-page"
  report (24). Its own earlier papers: 22 February 2019, 7 May 2019, 28 February 2019 (to MBIE).
- Independent retailers "less than 50% but perhaps as high as 40%" (195-201). "20% ROACE" (149).
- Schedule: Waitomo in Wellington undercut by $0.001/litre, others 2-9 cpl dearer (317-318); unmanned
  sites save about $250k a year (339); survey 51% loyal, 77% of those tied to a card (468); Gull 1998
  to its 2017 purchase by Caltex (532); does not support publishing retail prices (167, 519); TGP and
  an "oil code" "could have some merit" (441, 511).

## D08 (Doc 7) - Refining NZ

- 13 September 2019. 40% of energy and 70% of transport fuel needs (petrol, diesel, jet); 400 staff, 250
  contractors, 1,100 Northland jobs, 2,400 elsewhere (14-17). Cargoes 30,000MT in the report, now 36,000
  to 40,000 tonnes (47). One third of product storage (50); 60% of domestic stock (66); IEA 90 days.
- Supports a shorter allocation period (75) and less information sharing; footnotes 3-8 cite outside
  reports (Hale & Twomey April 2017).

## D10 (Doc 8) - Waitomo

- Undated. Founded 1947, "around 65 Fuel Stops", supplied by Mobil (5-7). "7th site this year in
  mid-September", three more in development including the first South Island site (20); third
  Wellington site in Johnsonville (54). Upper Hutt prices down "up to 20 cents a litre" (21, 50).
- "roughly 97 cents a litre" taxes (37). No discount schemes (35, 60). 95 price not on its boards (65).
  Sites near Mobil: Cambridge, Foxton, Bulls, Upper Hutt, Epsom, central Hamilton (90).

## D11 (Doc 9) - Z Energy

- 13 September 2019 (footnote 6: earnings update 12 September 2019). Parts A-E, Appendix 1 (nine
  suggestions, 889-915), Appendix 2 (919-950).
- ROACE: Z's own about 11.3% for 2016-2018 against the report's about 22% (89, 102); 14% on the comparator
  basis (220); "by approximately 9%" (105). Benchmarks 7.5% simple, 5.9% weighted, NZX50 8.9% (224-230).
- Waterfall text (118-124): 141, 134, 41, 254, 79, 200, 2,085, 17, 1,254 ($m, 2016 to 2018 average
  capital employed). Earnings waterfall (164-172): 23, 231, 14, 45, 16, 283.
- Chevron: bought 2016 for $785m; goodwill $158m, contracts $433m, "75%" (129-131). Revaluation gains
  $322m since 2014, $174m in 2014 (184). FY19 items: leases $282m, terminal uplift $149m, D&R $68m
  (199-205); $217 million (272). Shares 400 million, not 429 million (255). IRR 34% vs about 20% (336-340).
- Appendix 2 capital employed, $m, 2015-2018: Z 1,469 / 1,533 / 2,631 / 2,714; the Commission 1,006 /
  1,101 / 1,425 / 1,463; seven adjustment rows. Earnings, $m, 2016-2018: Z NOPAT 181 / 245 / 267; the
  Commission 202 / 308 / 339; HC-RC difference (72) / 61 / 58; PPE revaluations 115 / 5 / 15.
  The printed averages are means of the yearly opening-and-closing averages.
- Proposals: TGP by industry code (94-99); distributor contracts capped at 7 years (111, 131), dealer
  contracts treated differently (112, 135-140); merchant refinery (155); premium and post-discount
  prices on boards (174-177). Distributors named: NPD, Waitomo, McKeown (523-531).
- Footnote 40 (467): Gull's 22 February response. Gull "owned by Caltex Australia" (461, 701-705).

## D02 (Doc 10) - BP New Zealand

- 13 September 2019. Sections 1-8 follow the report's chapters; Annex 1 lists 26 competitor sites.
- New sites in five years (60-65): Allied 16 South Island + 13 North Island, NPD 21 SI, Gull 12 NI,
  Waitomo 14 NI. "38 new sites" SI and 45 NI (196); charts 850 to 895 (NI) and 386 to 424 (SI),
  2014 to 2019 (198-215); "76 new sites opened by independents" (545); "a net 36" SI and "a net 40" NI
  against 2 and 5 by the majors (586-587).
- Z's downgrade (146): FY20 EBITDAF $390-430 million, was $450-490 million; "~$250 million" off its
  market capitalisation. Hurdle rates 15%, payback three years (47-50, 161-169).
- Imports: three ports take about 75% (137). Nelson coordination 35% (387). "WACC of 8%" (485).
  BP market share 25% (482). GAS "more equivalent to a large multi-site dealer" (548-550). NPD supplied
  by Mobil (277); Waitomo supplied by Mobil (630). 104 sites (703). Loyalty programme "AASF".
- No mention of terminal gate pricing anywhere.

## D05 (Doc 11) - Major Electricity Users' Group

- 11 October 2019, after the conference "held 24 th and 25th September" (12). Third MEUG submission
  (31-Jan-19 on the guidelines, 21 February 2019 on preliminary issues). Argues for Economic Value
  Added as the measure of excess profit; no formula and no figures.

## Shared ground (navigation only)

- Price components for 1 July - 31 December 2018: D09 137-138; D01 17-34; D10 37; D11 77; D06 117-121;
  D02 126.
- Return measures: D09 159-164; D11 89-105, 220-230, 336-340, 919-950; D07 149; D02 485; D05 throughout.
- Z Energy quoted by others: D09 166 and 178 (May 2019 presentation); D02 146 (12 September downgrade).
- Site counts: D09 104-106, 166; D02 60-65, 196-215, 545, 586-587; D10 5, 20; D06 19; D11 318.
- Terminals and ports: D06 19, 76-79; D09 89, 93; D02 137, 268-270; D11 461.
- Process dates: D09 13-22, 388; D03 9, 16; D07 24; D02 13-15; D05 12-21.
- Contract terms: D09 331; D11 111-112, 131, 135; D06 62-63, 134.
- Who supplies whom: Waitomo by Mobil (D10 7; D02 630); NPD by Mobil (D02 277); GAS by BP (D02 550).
- Earlier submissions cited: D11 467, 526; D08 29-30; D05 21; D07 213, 441; D02 52, 148.
