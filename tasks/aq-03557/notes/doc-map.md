# aq-03557 - document map

Written by the caller from `text/` on 2026-10-12. Navigation only, like the form's bundle overview: where
things are, not what to ask. Questions quote the documents, never this map.

## Bundle

- What it is: nine papers from the New Zealand Commerce Commission's retail grocery market study, first round.
  Seven submissions on the preliminary issues paper ("PIP", 10 December 2020, 51 numbered questions), one
  consultant's price benchmarking report filed with a submission, and one reply to other submissions. The PIP
  itself, the Cabinet paper and the Food & Grocery Council's submission are not in the bundle.
- Documents: 9; local ids from `text/manifest.json`. Local ids are alphabetical by file name and differ from
  the task page's Doc numbers:

  | Local id | Page Doc | Author | Chars |
  | --- | --- | --- | --- |
  | D01 | Doc 1 | Consumer NZ | 29,986 |
  | D03 | Doc 2 | Foodstuffs North Island (FSNI), submission | 96,096 |
  | D04 | Doc 3 | Foodstuffs South Island (FSSI), submission | 67,884 |
  | D05 | Doc 4 | T&G Fresh | 20,838 |
  | D06 | Doc 5 | The Warehouse Group (TWG) | 11,471 |
  | D07 | Doc 6 | United Fresh | 77,024 |
  | D09 | Doc 7 | Woolworths New Zealand (WWNZ), submission | 183,651 |
  | D08 | Doc 8 | NERA Economic Consulting for WWNZ, price benchmarking | 21,665 |
  | D02 | Doc 9 | FSNI, response to submissions | 23,234 |

- Gaps: none in the capture ("9 of 9 read in full", every document `incomplete: false`, `gap_characters: 0`).
  Figures and charts are absent from the text everywhere (WWNZ Figures 1-19, NERA Figures 5.1-5.18, Consumer NZ
  Figures 1-3, FSNI Diagram 1). NERA's Table A.1 loses its blue and orange shading, so which products are
  non-metro only cannot be read from the text. FSSI's Appendix 2 supply-chain diagram is OCR noise (D04 L585-609).
  FSNI and WWNZ are public versions with redactions ("[REDACTED]", "[ ]").
- Extraction spot-checks (2026-10-12): character counts match the capture's per-document counts to within 2
  (D01 29,986 against 29,988, and so on: the trailing rule). Table checked: NERA Table A.1 (D08 L213-232) parses
  to 69 products, the count D08 L106 gives for non-metro cities. Table checked: WWNZ Figure [9] (D09 L613-618)
  keeps its two rows and four year columns. Footnotes checked: D09 fn 140 (L1444) and D03 fn 36 (L359) sit beside
  their anchors. No page counts apply (plain text captures).
- Provenance: notes/intake.json, capture AQ-03557_2026-10-12_1718.txt, capture sha256 89cb5654..., all nine
  `matches_capture: true`. The capture note says the page asked for a reload; all nine documents are present.
- Reuse binding: source hashes in text/manifest.json (D01 60b5c958..., D02 8a721bfc..., D03 a50fa629...,
  D04 6263ee6f..., D05 53ab67a0..., D06 ac2113bb..., D07 f2cedac4..., D08 79f95296..., D09 dd007e39...). No earlier
  bundle in the workspace holds these files (searched every capture for "nzcc_grocery").
- Coverage: all nine documents read in full by the caller on 2026-10-12 (every line of each text file).

## D01 (Doc 1) - Consumer NZ submission

- Written by: Consumer NZ (contact Aneleise Gawn), 4 February 2021. Quotes the ACCC; cites Stats NZ, FSNI's and
  Woolworths Group's 2019 annual reports.
- Answers only some questions, each under a "Question N:" heading: 1, 4, 5, 12, 13, 15, 16, 27, 30, 39, 42, 43,
  44, 45, 46, 47, 48, 49, 50.
- Figures: L46 fruit and vegetable prices up 8.9 percent "last year", general inflation 1.4 percent (Food price
  index, December 2020). L51 63 / 55 / 53 percent (food, fuel, power as main worry); L59 survey of 1002. L87 2020
  survey of 825 delivery users. L109-111 June 2015 comparison of 20 "Homebrand" and "Woolworths Select" products:
  30 percent more in New Zealand; rolled oats $1.02 / $2 / $1.99. L194 2020 price survey: 22 items over 12 weeks.
  L218-220 maximum fine $600,000 per offence; Pak'nSave Mangere fined $78,000. L239 January 2020: Onecard two
  million members, Clubcard 1.6 million. L151 unfair contract terms for small business contracts under $250,000.
- Lists: L199-205 promotion terms by chain (Countdown: "Specials", "Great Price", Onecard-only deals; New World:
  "Saver", "Super-Saver", "Club Deal", "Everyday Value"; Pak'nSave: "Extra-low", "Everyday-low"; then "all stores
  offer multibuys").
- Scope: L28 suggests adding alcohol. L34 wants fruit and vegetables and other perishables in greater detail.
- Hedged claims: L105 accommodating behaviour "is a major risk"; L124 stores "appear to have 'turns'".

## D03 (Doc 2) - Foodstuffs North Island submission

- Written by: FSNI, undated public version (responds to the PIP; D02 dates the first-round submissions 4 February
  2021). Main body paras 1-39 (L8-178), Appendix A answers to questions 1-51 (L185-854), glossary (L862-868).
- Parallel text: FSSI's D04 follows the same template; see Shared ground for the differences.
- Lists: L197 omissions from Table 1 (pet food and pet care; beer, wine and tobacco; vitamins and health
  supplements; meal solutions; other general merchandise). L258 other retailers (The Warehouse/TheMarket, online
  and direct-to-consumer names, market gardeners). L266-274 wholesalers (Gilmours, Trents, Bidfoods, Service
  Foods, Davis Trading). L292-306 other participants (meal kits, online, seafood, health, pet, direct to consumer,
  department stores, eating places, liquor). L621 entry and expansion (Costco, Aldi, Lidl, Kaufland, the Honest
  Grocer, My Food Bag, Hello Fresh, Woop, TheMarket, Mighty Ape, Amazon, Circle K, Chemist Warehouse). L719-721
  eight supplier-relationship examples.
- Figures: L36 "10+ distinct shopping missions". L152 fn 21 Costco 2022; Farro Fresh three new stores, projected
  $100m revenue. L359 fn 36 at-home consumption about 75% of the food retail market. L384 7 in 10 shoppers.
  L509 5-10km radius "of limited or no value". L719 all-supplier events 3 times a year, 300 to 500 suppliers.
  L782-784 promotion periods 19 October 2020 to 18 January 2021 and 26 October 2020 to 25 January 2021 (shares
  redacted). L819 ACCC survey 28% / 57% / 10% / 22%. L841 $25 minimum spend for Fly Buys or Airpoints.
- Loyalty: L139 "The other FSNI brands do not offer a loyalty programme"; L831 PAK'nSAVE has no scheme.
- Internal difference: L114 "between 1 and 4 suppliers" against L695 "between 2-4 suppliers" (categories redacted).
- Footnotes 11, 18, 20, 22 number the Cabinet paper's four indicators.

## D04 (Doc 3) - Foodstuffs South Island submission

- Written by: FSSI, 4 February 2021; "prepared in consultation with" FSNI, "broadly similar ... with some
  variations" (L15). Appendix 1 answers questions 1-51 (L20-582); Appendix 2 diagram unreadable.
- Lists: L30-33 four omissions (no vitamins bullet). L97-108 other retailers (adds Mighty Ape's owner, Chemist
  Warehouse, Animates, international e-commerce, parallel importers The Shaver Shop and Pricewise). L120
  wholesalers (Trents, Bidfoods, Service Foods, Davis Trading). L133 meal kits (adds Eat). L216-230 eight COVID
  shopping changes. L418 entry and expansion (no Lidl or Kaufland). L431 wholesalers for entrants (adds Kaans,
  Trents). L451 and L474 nine supplier-concentrated categories, "2-4 suppliers".
- Figures: L152 Costco 2021/22. L359 catchment "up to a 15km radius". L495 about 3200 new products in 2020. L570
  spend $200 for a 40c per litre fuel discount.
- Loyalty: L558 PAK'nSAVE has no scheme; "Four Square and Raeward Fresh also do not operate loyalty schemes".
  L559 "It is our understanding that FreshChoice and SuperValue do not operate loyalty schemes". L564 says
  "FSNI would not expect" (template text left in).

## D05 (Doc 4) - T&G Fresh submission

- Written by: Turners and Growers Fresh Limited, 4 February 2021; the domestic business of T&G Global.
- Answers Q1-Q51 in order; these are printed with no answer: 19, 24, 26, 30, 31, 34, 35, 38, 43, 44, 46, 48, 49, 50.
- Figures: L22 May 2020 purchase of Freshmax New Zealand's domestic division. L23 own crops (apples, tomatoes,
  blueberries, citrus). L24 12 market floors, twelve towns named. L65 supermarkets as groups of ">30 stores".
  L107 independents lost about 2.5% market share. L159 Jadan, Tai Ping, Costco in Auckland in 2022.
- L63 Foodstuffs also owns Gilmours. L143-146 suppliers manage promotions so that banners do not clash.

## D06 (Doc 5) - The Warehouse Group submission

- Written by: TWG, signed Nick Grayston, 4 February 2021. No numbered answers; three areas (scope, barriers,
  consumer impacts).
- L10 says the PIP was "published on December 18" (other documents: 10 December 2020).
- L13 and L34 grocery attempt "in 2008". L49 scope additions: liquor sales, in-store baked goods, over the
  counter medicines. L76 Aldi and Lidl home brands "c.95% of offer". L103 supports a supplier code.

## D07 (Doc 6) - United Fresh submission

- Written by: United Fresh Technical Advisory Group (Dr Hans Maurer, Jacob Lawes), 03 February 2021. Members
  include both major retailers. Answers all 51, several with "best answered by the grocery retailers" or "cannot
  comment" (23, 28, 29, 40, 43, 47, 49).
- Figures: L28-36 Fruit in Schools (25 schools in 2004; 559 schools, about 25%; 123,000; 26 million servings;
  10,000 boxes a week). L57 study authorised 16 November 2020; L69 PIP 10 December 2020, 51 questions; L71 final
  report by 23 November 2021. L328 $800 million of imported produce. L351 Norway 5.3 million / 3 retailers,
  Denmark 5.8 / 5, Singapore 5.7 / 5. L359 about 200 SKUs against 600. L442 The Warehouse grocery venture 2006,
  ended 2008 "after store 4". L444 Aldi "about 150 stores in Australia".
- Unnamed entities: L471-481 three national produce wholesalers (one bought by a Munich-based parent, one a
  Wellington growers' co-operative, one family-owned); L464 names T&G Global's Freshmax purchase. L647 Lotatoes
  (fn 6 tandg.global). L503 "one of the two major grocery retailers" with a house brand on produce.
- L402 promotions kept out of the same week (potato example, under question 26). L413-424 the 1990 banana story.

## D09 (Doc 7) - Woolworths New Zealand submission

- Written by: WWNZ, 4 February 2021, public version. Sections (1)-(6) L9-905; Appendix One answers Q1-Q51
  L913-1500 (many point back to the sections).
- Store counts: L20 and L130 180 Countdown supermarkets, two Metros, three eStores; 71 SuperValue and FreshChoice.
  L31 and L233 56 PAK'nSAVE, 138 New World, 245 Four Square. L271-284 other supermarkets: Farro Fresh six (three
  more planned), Huckleberry six, Tai Ping eleven, Moore Wilson's three (L1258 "~4 stores"), Raeward Fresh four
  (the list breaks across footnotes between Tai Ping and Moore Wilson's). L290 The Warehouse 90. L61 and L530
  Chemist Warehouse 16, aiming for 70. L62 Costco "more than 700 stores" against L532 "~800 ... (including 12 in
  Australia)". L288 1,200 service stations, 4,000 dairies; L291 about 1,000 liquor outlets. L923 36 pharmacies.
- Market and money: L29 food market $29 to $40 billion, share 26% to 19%. L66 and L581 inflation 1.58%, food
  1.60% and 1.30% without restaurant meals, Countdown 0.7%, wages 3.7%, export prices 3.6% (June 2010 - June
  2020). L89 and L621 63 / 19 / 13 / 2 cents and 2.4 cents margin (FY2020). L613-618 food share of household
  income 2010-2019, two rows. L637 9.2% against 6.5%.
- Suppliers: L20 1,400 suppliers, 120 growers, 900 small; L173 800 farmers; L782 400 new in three years, 20% of
  new products; L798-800 14-day terms under $250,000 and $1 million. L835-873 twelve export shares.
- Online and meal kits: L40 and L353 3% in FY2014, over 12% now, "over 350%"; L367 other countries; L60 and L494
  My Food Bag 86%, HelloFresh 84%; L482 7% tried meal kits, 3% regular.
- Scope: L920 five "particularly notable omissions" (Wine/beer/cider, Pharmacy, Pet, Ready-to-Eat Food, Non-food
  General Merchandise); L935 general merchandise examples. The word "tobacco" does not occur in the document.
- Prices: L1409-1411 standard shelf prices ("Great Price") and five discount types. Loyalty: L1433-1437 who has a
  programme and who does not; fn 140 (L1444) PAK'nSAVE's fuel dockets; L1461 1.9 million registered Onecards used.
- Entry: L532 Costco (Westgate; Australian stores by city; A$2.59 billion in 2020); L532-548 Aldi (over 500
  stores since 2001, 25 a year; Western Australia 46 of 70).
- NERA: L91 and L664 the enclosed analysis; Figure [13] is the metro, 2020, average-rank chart.

## D08 (Doc 8) - NERA price benchmarking report

- Written by: NERA Economic Consulting (Mellsop, Taylor, Kaleff, Eyre) for WWNZ, 4 February 2021.
- L43 140 cities, 67 in the OECD. L44 89 products, two store categories. L46-47 PAK'nSAVE surveyed as
  "supermarket"; Countdown, New World and Farro Fresh as "mid-priced store" (EIU, 3 February 2021). L105-106 62
  products for 38 metro cities, 69 for 29 non-metro cities. L73 ranking example with 29 cities.
- L171-172 sensitivity test: drops alcohol and tobacco, and electric toasters, frying pans, batteries, light
  bulbs, aspirin and cough medicine. L213-232 Table A.1: 69 products; no cough medicine among them.
- Figures 5.1-5.12 base case (metro and non-metro, 2020 and 2019, three categories); 5.13-5.18 sensitivity, 2020.

## D02 (Doc 9) - FSNI response to submissions

- Written by: FSNI; file stamp "20210419". Replies to the Food & Grocery Council and Consumer NZ submissions of
  4 February 2021. A three-column table flattened to text: under each topic the FGC's points come first,
  Consumer NZ's second, FSNI's reply third. Footnotes cite paragraphs and answers of D03.
- Repeats D01's 8.9 percent and 1.4 percent (L90) and D03's supplier-relationship list (L202-220, without "3 times
  per year"). L116-144 the FGC's eight examples of accommodating behaviour, (b) and (g) redacted.

## Shared ground (navigation only)

- Entities in several documents: Costco (D03, D04, D05, D07, D09); Aldi (D03, D04, D06, D07, D09); The Warehouse's
  grocery venture (D01, D03, D04, D06, D07, D09); Farro Fresh (D03, D05, D07, D08, D09); Chemist Warehouse (D03,
  D04, D09); T&G (D03, D04, D05, D07 unnamed, D09); Gilmours and Trents (D03, D04, D05); Onecard and Clubcard
  (D01, D03, D04, D07, D09); Raeward Fresh (D04, D09 only); SuperValue and FreshChoice (D04, D09; D03 glossary).
- Documents that respond to others: D02 replies to D01 and cites D03; D08 is enclosed with D09; D04 follows D03.
- FSNI/FSSI differences (same template): scope omissions (five against four); wholesaler lists; meal-kit names;
  entry list (Lidl, Kaufland only in D03); concentrated categories (redacted in D03, listed in D04); Costco
  2022 against 2021/22; catchment 5-10km against 15km; loyalty spend thresholds; D04 alone names Raeward Fresh,
  FreshChoice and SuperValue as running no scheme.
- Same question, different lists: product categories each party wants in scope (D01 L28, D03 L197, D04 L30-33,
  D06 L49, D09 L920) beside NERA's dropped products (D08 L172).
- Same fact, different figures: PIP date (D06 against D04, D05, D07, D08); The Warehouse's grocery years (D06
  against D07); Aldi's Australian stores (D07 against D09); Costco's store total (D09 twice); Farro Fresh's
  revenue as forecast (D03) or as fact (D09).
