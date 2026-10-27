# aq-03423 - document map

Maintained by the caller from `text/`. Navigation only: where things are, not what to ask.
Questions quote the documents, never this map. Line numbers are `text/Dnn.txt` lines.

## Bundle

- What it is: the New Zealand Commerce Commission's mobile market study, first round. One issues paper
  (31 August 2018), five submissions on the study's terms of reference (November-December 2017) and five
  responses to the issues paper (October 2018).
- Documents: 11; ids from `text/manifest.json`. Local ids are alphabetical by file name and differ from
  the task page's Doc numbers:

  | Local | Task page | Document | Chars |
  | --- | --- | --- | --- |
  | D05 | Doc 1 | Commerce Commission issues paper, 31 August 2018 | 160,361 |
  | D02 | Doc 2 | Chorus, terms of reference, 30 November 2017 | 20,398 |
  | D03 | Doc 3 | New Street Research, terms of reference, undated (c) 2017 | 9,373 |
  | D09 | Doc 4 | Vocus, terms of reference ("Scope Submission"), 30 November 2017 | 19,249 |
  | D06 | Doc 5 | Analysys Mason report for Trustpower, 28 November 2017 | 49,572 |
  | D01 | Doc 6 | Bluereach, terms of reference, undated (file name: 6 December) | 8,806 |
  | D08 | Doc 7 | 2degrees, response to the issues paper, "October 2018" | 140,509 |
  | D07 | Doc 8 | Covec report for 2degrees, 24 October 2018 | 47,563 |
  | D10 | Doc 9 | Vocus, response to the issues paper, 26 October 2018 | 57,709 |
  | D11 | Doc 10 | WISPA NZ, response to the issues paper, 26 October 2018 | 10,320 |
  | D04 | Doc 11 | Speedchecker Ltd, response to the issues paper, 2018 | 11,369 |

- Gaps: none known. Every document read in full by the caller on 2026-10-12 (D05 in three passes, D08 in
  three passes). Figures and charts are not in the text: D05 Figures 1-17 and Table 8, D06 Figures 2.1-2.6
  (axis labels only), D07 Figures 1-2, D02 Table 1 (four values survive: "$1.3 $0.7 $16.2 $11.7"), D10
  Appendix A slides (page headers only). D08 and D10 carry confidential redactions ("[C-I-C]", "[]CI").
- Extraction spot-checks: plain-text captures, no page counts. Capture header: "11 of 11 read in full
  (535,205 characters)"; split lengths sum to 535,225 with headers. D05 Table 5 (benchmark baskets) and
  Table 6 (termination rates) survive as text rows with scrambled headers; D05 footnotes are inline after
  each page. D11 opens with OCR noise ("fak UJISRRfs/z") and has OCR slips ("ZOOMhz" for 2000MHz, "SG" for 5G).
- Provenance: notes/intake.json, capture AQ-03423_2026-10-12_1149.txt, capture sha256 3e6c7336...; all
  eleven `matches_capture: true`, `incomplete: false`. Capture note: the page asked for a reload ("Docket
  has been updated"); no document was missing.
- Reuse binding: source hashes in text/manifest.json, first twelve characters: D01 a8c7a33da1e4, D02
  0b30583569b8, D03 0f8933748bc6, D04 9a73aaaef132, D05 81ea42e1cb98, D06 89089702220e, D07 385c2e08a29e,
  D08 4aa125a04dd2, D09 8a02d6c2b2e1, D10 5599fb3065e6, D11 8f7b0cd97e8a. Reuse this map only while they match.

## D05 - Doc 1 - Commerce Commission, Study of mobile telecommunications markets in New Zealand: Issues Paper

- Written by: Commerce Commission. Date 31 August 2018 (L10). Submissions due 5pm 12 October 2018 (L147).
- Timeline: study announced 6 October 2017 (L129); terms-of-reference submissions from 2degrees, Blue
  Reach, Chorus, InternetNZ, New Street Research, Spark, Trustpower, Vocus, Vodafone, WISPA NZ (L131); scope
  paper 27 March 2018 (L133); update "before the end of the year", conference "early 2019" (L141).
- Tables: Table 1 regulated services, dates and STD status (L248-264); Table 2 population coverage, total
  and 4G (L366-372); Table 3 three MVNOs and hosts (L385-388); Table 4 revenue by segment 27/41/32% (L431-437);
  Table 5 OECD benchmark, six baskets, NZD PPP, variance from Australia and OECD (L520-545); Table 6
  termination rates 7.48 / 5.88 / 3.97 / 3.72 / 3.56 cpm from 6 May 2011 to 1 Apr 2014 (L844-847); Table 7
  porting 4.9 / 5.4 / 4.8 / 4.7% for 2014-2017 (L990-991).
- Figures by topic: fixed wireless and mobile broadband prices per GB (L198); subscriber shares (L395-404);
  ARPU prepaid just over $13, on account over $50 (L409); Trilogy quote 24% overall, 15% post-paid (L441);
  2015 business survey 73% / 69% / 52% (L421, L936-946), satisfaction 93 / 81 / 77%, 80% overall (L456,
  L1061), switching 14% and other sectors (L995); prepaid share of subscribers 68% to 60% (L516); 3GB+
  bundles 133,000 to 319,000 (L548); SIM-only 25GB plans $65 Skinny Direct, $70 2degrees, and Australian
  plans (L550-551); 6.4 million connections 2017, up 5.1%, minutes (L566); unlimited plans and prices (L580);
  investment $200-400 million a year (L603-607); 700MHz auction prices (L613, fn 34); geographic coverage
  about 50% (L620); OpenSignal ranks (L621-626); spectrum holdings by band (L750); Spark's 70MHz at 2300MHz
  (L754); RBI1 154 new and 387 upgraded sites (L805); handset unlock fees (L966); Consumer NZ satisfaction
  by year (L1019-1027); complaints 603 (L1045); RCG 520 cell sites (L1169); Blue Reach spectrum (L1154, fn
  120); 3.5GHz 280MHz vs 400MHz, 100MHz each (L1268-1271); UK and Australian limits (L1271, L1283).
- Lists: 47 questions, in the text by chapter and again consolidated in Chapter 8 (L1328-1436). Six
  consolidated questions are worded differently from the in-text ones (Q3, Q11, Q22, Q23, Q41, Q43).
  Chapter 8 heads Q9-Q11 "Investment" although they are the quality questions.
- Definitions: MNO, MVNO, light and full MVNO (L223-236, L656); specified vs designated (L241-242);
  Schedule 3 five-yearly reviews (L281-284); availability (L622); "1 gigabyte = 1024 megabytes" (L41).
- Cites the bundle's submissions: Analysys Mason (fn 24, 27, 49, 142), Vocus (fn 47, 64, 66), Chorus (fn
  66). Blue Reach, Spark and Vodafone are cited only for their spectrum-consultation submissions.
- Coverage: full.

## D02 - Doc 2 - Chorus, terms of reference

- Date 30 November 2017 (L6). Public version.
- Figures: 92 fibre retailers (L16); OECD ranks 10th/32, 16th/31 fibre, 31 and 33 of 35 mobile broadband
  (L20-26, L107); "six" MVNOs under 1%, excluding Skinny (L28, L92); two largest mobile network owners "80%
  of the retail broadband market", unsourced (L38); MVNO share UK 13%, Australia 9.4% (L95); 129 RSPs
  (L100); per-GB chart values and the plan prices behind them, fn 15 (L129-131); termination rate quote,
  "5 May 2011", 3.56cpm, A1.7cpm, 1.22 eurocents (L142-143); 87% fibre by 2022 (L52); 70% and 40% (L72).
- Sources it cites: IDC 2017 (fn 1); Commission "2016 Annual Telecommunications Monitoring Report, May
  2017" (fn 2); 2015 report (fn 16).
- Coverage: full.

## D03 - Doc 3 - New Street Research, terms of reference

- Signed Ian Martin. Capex 11-12% of sales for Spark and Vodafone, 16-17% for Telstra, Optus, TPG (L32);
  Verizon 30m premises 2019 (L34); 150 companies, 200 clients, thirty analysts (L7-9). No other figures.
- Coverage: full.

## D09 - Doc 4 - Vocus, terms of reference

- Date 30th November 2017 (L5). Numbered paragraphs 1-49. Contact Graham Walmsley.
- Figures: 800 staff, 200 exchanges, 4,200km (L9-12); Spark over 10% of broadband base on fixed wireless
  (L28); MVNOs under 1% (L54); Australian MVNOs 200,000 of 444,000 new services, 45% (L56); Vocus 21,000
  MVNO services (L64); origination 8 to 9 cents (L136); termination 3.56c, Australia 1.7 from 3.6 cents,
  fixed 1c (L138-140). Brands: Slingshot, Orcon, Flip, 2Talk.
- Coverage: full.

## D06 - Doc 5 - Analysys Mason for Trustpower

- Date 28 November 2017 (L6). Mostly qualitative. 23,000 MVNO subscribers in 2016 (L83); over 20% MVNO
  share in Germany and Belgium (L83); least dense 18% in France (L238); candidate 5G bands table (L309-322);
  MVNO counting conventions in footnotes 5-6 (L114-117); glossary with HHI definition (L377).
- Coverage: full.

## D01 - Doc 6 - Bluereach, terms of reference

- Signed David Stone. Owner Malcolm Dick, founder of CallPlus; spectrum retained when CallPlus was sold
  (L6). Six issues listed (L18-27). Co-location STD "never used" (L35). No figures beyond "2019".
- Coverage: full.

## D08 - Doc 7 - 2degrees, response to the issues paper

- "October 2018" (L6-7); cites Covec's report of 24 October 2018 (fn 2). Executive summary (L11-168), then
  an answer under every one of the 47 questions (L172-1169); several answered jointly (Q3-Q4, Q9-Q10,
  Q25-Q26, Q42-Q43) or by reference (Q16, Q35). Confidential Appendix A.
- Figures: 98% own coverage, over 96% LTE (L26, L264); roaming under 1.5% of traffic (L38, L678); 1.3
  million (L80, L428); complaints 8.2 per 100,000 connections (L108, L416); spectrum shares 18.5 / 40 / 30%,
  Blue Reach/Cayman 11% (L120-122, L608, L642); 2015 survey 5%, 44%, 47% (fn 6, L256); fixed broadband
  shares Vocus 13%, 2degrees 4% (fn 7, L320), Trustpower 5% (fn 23, L601); prices 22% to 67% below OECD
  (L20, L328); $55 for 10GB with double data for 3 months, $129 unlimited (L335-337); 250% of data for 70%
  of price (L356); MVNO counts and prices by country (L492, L561-563, L582); penetration 120% (L531);
  2100MHz and 700MHz blocks (L624, L629); 3.5GHz positions (L626, L1056-1070); 2x35MHz of 2600MHz unused
  (fn 29, L669); 47% at launch (L682); 250 towers (L913); DFAS $355 (fn 43); 35% cap, 40MHz cap (L1103);
  RCG "a further $75m capex" (L1131); 3.4 million switched since 2007 (L848).
- Coverage: full.

## D07 - Doc 8 - Covec for 2degrees, Mobile Market Development in New Zealand

- Date 24 October 2018 (L3). Author John Small. Numbered paragraphs 1-100.
- Model of a fourth network (L224-246): revenue $2.75bn, margin 64%, $1.76bn; investment $240m + $200m +
  $60m = $500m; $694m before tax; $1.066bn; $566m; cost of capital 10%; build $550m; break-even share 10%.
- Other figures: Australia AU$22bn, eight times, five times population (L155-163); Table 1 Australian
  operator shares September 2017 (L175-179); roaming thresholds 10% and 65% (L74); three MNOs "75% of the
  fixed broadband market", fn 14 Key Facts 20 December 2017 (L307-308, L316); 98% and 92% coverage (L117).
- Coverage: full.

## D10 - Doc 9 - Vocus, response to the issues paper

- Date 26th October 2018 (L5). Numbered paragraphs 1-108. Contact Johnathan Eele. Brands now include
  CallPlus. Sections headed by the question numbers answered (L62-64, L206, L238-242, L264-272, L348-353,
  L361-363, L380-384, L407-408, L421-422).
- Figures: 16,000 power connections in 18 months (L29); 99% (L34); Slingshot +41% broadband, -12% mobile,
  December 2011 to September 2015 (L93-94); 2014-15 examples (L98-118); Skinny 30GB $57.39 excl GST, revised
  1 July 2018 (L133-138); Note 9 prices (L147); RCG $150 million via the levy (L285); 2degrees 5-10% lower
  (L356); termination and origination rates (L413-416). Quotes its own 2017 submission with paragraph
  numbers three lower than D09's (L275-282, L335-344). Quotes Ofcom, Link Economics, ACCC, OECD, Analysys Mason.
- Coverage: full.

## D11 - Doc 10 - WISPA NZ, response to the issues paper

- Date 26 October 2018 (L11). Signed Ernie Newman. Formed January 2017, 15 members, now 28 (L16).
  Answers Q3, Q4, Q14, Q15, Q16, Q20, Q33, Q34, Q40, Q41, Q44, Q45; quotes the in-text wording of Q3 and Q41.
- Coverage: full.

## D04 - Doc 11 - Speedchecker Ltd, response to the issues paper

- Author Steve Gledhill. Answers Q2.1, Q7, Q9, Q10, Q27, Q28, Q29, Q30, Q41 (consolidated wording of Q41).
  Ofcom data 0.2 Gb to nearly 2Gb, 63% (L50); 50% a year (L49, L52).
- Coverage: full.

## Shared ground (navigation only)

- Entities in more than one document: Spark, Vodafone, 2degrees (all); Skinny as Spark's brand (D05, D02,
  D10); Vocus and its brands (D05 Table 3, D09, D10, D08, D07); Blue Reach / Bluereach (D01, D05, D09, D10,
  D08); CallPlus (D01, D10, D09); Warehouse Mobile (D05, D08, D07); Digital Island (D09, D10); Rural
  Connectivity Group (D05, D08, D10, D11, D04); Trilogy as 2degrees' parent (D05); Chorus (D02, D05, D08, D07).
- Same figure in several documents: termination rate 3.56 (D05, D02, D09, D10); origination 8-9 cents (D05,
  D09, D10); MVNO share under 1% (D05, D02, D09) and "1%" (D08), "99%" (D10); 2degrees coverage 98% (D05,
  D08, D07), 4G 92% (D05, D07) against "over 96%" (D08); Spark's $84.99 and $69.99 plans (D05, D02); 20%
  bundle discount (D05, D07, D10); ten-year milestone (D05, D08, D07); four-to-three mergers (D08, D07, D10).
- Same quantity, different figures: fixed broadband share of the largest operators (D02 L38 against D07
  L307 with D08 L320); number of MVNOs (D02 "six", D05 and D08 "three"); largest MVNO (D09 L64 against D08
  L47 and D07 L221); German MVNO share (D08 L561 against D06 L83).
- Documents that respond to or cite another in the bundle: D05 cites D06, D09, D02; D08 cites D07 and D09;
  D07 cites D05 paragraphs 87, 90-91, 138; D10 cites D05 paragraph 130, D06 sections 2.2.2 and 2.4.2, D09;
  D08 Q5 answers D05 L550 (its own plan prices); D11 and D04 answer D05's numbered questions.
- Forecast/actual and dated pairs: D05 L286 expects the national roaming decision on 4 September 2018, D07
  fn 1 cites it; D05 deadline 12 October 2018 against response dates of 24-26 October 2018; D09 (November
  2017) and D10 (October 2018) as two editions of one submitter.
