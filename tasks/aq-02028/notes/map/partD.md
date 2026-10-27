# aq-02028 - document map, part D (D03, D05, D06, D08, D09)

Group D output of the bundle-mapper run, for the caller to merge into `notes/doc-map.md`.
Navigation only: where facts sit, not what to ask. Questions quote the documents, never this map.
Citation convention: "Dnn Lx" = line x of `text/Dnn.txt`. "Mapper arithmetic" marks checks done
by the mapper; those results are not document statements.

## Bundle (part D scope)

- What it is: 20 plain-text submissions (D01-D20) to the Productivity Commission's 2022 inquiry into
  the long-term productivity of Australia's maritime logistics system. This part maps D03, D05, D06,
  D08 and D09 in full. Other documents are cited only as repeat locations found by whole-bundle
  keyword searches plus local context reads (not full reads; other groups map them).
- Documents in this part (sha256 as listed in `text/manifest.json`; `notes/intake.json` shows
  source_sha256 = captured_sha256 and `incomplete: false` for each):
  - D03 `docs/pcau_maritime_r1_sub014_maritime_logistics.txt` 1df70ca93b560340dcf67803801add58a53019c24cc87d4f4c4374186b2b908a (32,132 chars; 263 text lines)
  - D05 `docs/pcau_maritime_r1_sub017_maritime_logistics.txt` 1d652c64e4ce58225ae77bd17282eb700bdb8b7c99d4a5f5206952a518d304ab (30,130 chars; 312 lines)
  - D06 `docs/pcau_maritime_r1_sub021_maritime_logistics.txt` 632dd4a755a43131e57bb9ecfdf7480499f214af03062fed947dc12040ed4028 (24,881 chars; 170 lines)
  - D08 `docs/pcau_maritime_r1_sub024_maritime_logistics.txt` d3c0863e27fb7b4e77a24ff8a5f64f6d060d1376efb9eabe6c7c0958cd4b1501 (29,086 chars; 324 lines)
  - D09 `docs/pcau_maritime_r1_sub025_maritime_logistics.txt` e742cfaa194fd3542a96fa9d980ad1cdf395844b48cd57574fb871cb54a99c0d (23,682 chars; 177 lines)
- Extraction: method "text", pages null; originals are plain text (no PDF/page images in the bundle,
  so charts, logos and visual table layouts cannot be inspected: such items are "unresolved").
  Caller-verified: text = NFKC-normalised source; the only normalised characters in this part are
  2 ellipses in D06 (L130; original docs line 128 holds two U+2026).
- Line offset: text line = original line + 2 (two-line `# Dnn | path` header) for D03, D05, D06, D09
  on every spot-check. D08: +2 up to text L86, +1 from text L88 onward: original L85-86 are two empty
  lines that appear as one empty line (text L87); no content lost (checked).
- Extraction spot-checks (original vs text): listed under each document's Coverage.
- Reuse binding: every entry below is bound to the five sha256 values above; refresh entries whose
  source or text changes.

## D03 - National Farmers' Federation (NFF) submission

- Source: `text/D03.txt` L1-263 | printed page markers "Page | 5" (L36) through "Page | 16" (L254);
  front matter pages (contents L39 lists "NFF Member Organisations ... ii", "Statistics ... iv") carry no markers.
- Written or submitted by: National Farmers' Federation (L3, L10). "Prepared by Mr Ash Salardini" (L5),
  "Chief Economist and General Manager Trade" (L256); signed "Tony Mahar, CEO, National Farmers
  Federation" (L257-260). Organisations quoted or cited (not authors): Productivity Commission (PC) and
  its vulnerable supply chains review (L170-172, L187, L219, L223); LEK Consulting 2020 benchmarking
  study (L85); World Bank (L98); a 2019 ACCC study into class exemptions for Ocean Liner Shipping
  (L193-199); Australian Conservation Foundation (L34, 1989 Landcare history); NHVR (L252). NFF quotes
  its own earlier submission to the PC vulnerable supply chains review (L174-184).
- Type, date, edition: submission dated 14 February 2022 (L6); title "Submission to the Productivity
  Commission review in Australia's Maritime Logistics System" (L4); running header carries typo
  "reiviewinto" (L37, L42, L69 ...). One edition.
- Period covered: financial-year labels "2019-20" (L21, L24) and "2021-2022" (L24, forecast); calendar
  years 2018/2019/2021/2022 for freight and stevedoring prices (L91-96); "In 2021" employment (L27);
  "over the past four years" (L96), "in the space of four years" (L110). No fiscal convention defined.
- Entities and aliases: NFF; PC; ACCC; "section X exemptions from Competition and Consumer Act 2010"
  (L59), "Section X" (L71, L112, L193) vs "Part X exemptions" (L198) for the same exemption regime;
  "three alliances" of shipping lines (L123, L201); "stevedoring service providers"/"stevedores" (L140-148,
  L202); "infrastructure owners" (L72, L137-138, L204); Port of Fremantle, "Port Melbourne" (L152);
  Canada, Indonesia, South Australia (L86); United States, New Zealand (L206); Modern Manufacturing
  Strategy and Supply Chain Resilience Initiative (L80, L223, L232); "regularly updated National
  Freight Strategy" (L213); NHVR (L252); "Ad-Blue" (L186) / "AdBlue" (L218); HPVs = high
  productivity vehicles (L158-159, L237-238).
- Quantitative index (all NFF statements unless a source is named; none carry footnotes):
  - L11 NFF established 1979. L21 2019-20: approximately 87,800 farm businesses. L24 2019-20: farm-gate
    agriculture 1.9 per cent of GDP; gross value of farm production "forecast to reach $78 billion in
    2021-2022". L27 2021: agriculture, forestry and fishing employ approximately 313,700 people incl.
    over 215,800 full-time. L29 more than 26 per cent of workforce casual. L32 farmers manage 49 per
    cent of land mass; 7.79 million hectares set aside for conservation. L34 1989 Landcare.
  - L44 and L83: exports "more than 75%" of farm-gate output; L44 target "$100 billion industry by 2030".
  - L56 per-kilometre freight cost from Australia "3-4 times higher than competitors such as Canada";
    L135 "up to three to four times more than competitors, such as Canada".
  - L85 (LEK Consulting 2020): "up to 50% of the final price of grain can go towards freight and logistics".
  - L86 SA-to-Indonesia container of grain costs the same as Canada-to-Indonesia; Australian journey
    "some 10,000 km shorter (one-third the journey as compared to Canada)".
  - L91 2019 carrier charges "as low as $USD550 for 20ft containers, and $USD850 for 40ft containers
    (not including fuel adjustment surcharges)"; "In 2021 price peaked:".
  - L93 20ft: $USD3000 (excl. fuel adjustment surcharges) + destination congestion $USD300 + domestic
    congestion $USD360 = "Total $USD3660 per container".
  - L95 40ft: $USD3500 + destination congestion $USD500 + domestic congestion $USD442 = "Total
    $USD4442 per container".
  - L96 stevedoring costs "from $25 per container in 2018 to $122 per container currently"; "In January
    2022, stevedores added further levies ... of up to $30 per container ... bringing the total to $152
    per container in 2022" (AUD not stated explicitly; no "USD" label).
  - L110 "The total cost of container freight has risen 633% in the space of four years" (basis not stated).
  - L123 three alliances "more than 80% of the market". L130 new-ship orders "would increase the global
    fleet by 20% by 2023". L145 stevedore price per container and revenues "rose despite lower
    throughput in 2020". L150 maritime workers' "salaries of $200,000 per annum on a pro rata basis".
  - L204 proposed price-change notification period "(60 days)". L213 "$2.5 billion over the four
    years" (Infrastructure Fund; also L77). L240 "$140 million over four years" (local road access).
    L246 "axle load tolerance of up to 10% for fluid dynamic loads". L221 "coming twelve-months".
  - Mapper arithmetic: 3000+300+360 = 3660 and 3500+500+442 = 4442 (components sum to printed totals);
    122+30 = 152. The 633% figure is not reproduced by simple combinations of the printed components
    (e.g. (3660+152)/(550+25) = 6.63 times); the document gives no basis.
- Tables: none. Front "Statistics on Australian Agriculture" panels are prose (L17-32: "Social >",
  "Economic >", "Workplace >", "Environmental >").
- Lists (count; last item):
  - L45-52 scope of review requested: 4 (containerised; bulk; livestock; landside), last L52.
  - L57-65 causes of high cost/low productivity: 5, last L65 (landside first/last mile).
  - L69-81 summary recommendations: 8, last L81 (shared services for local government road access).
  - L99-104 consequences of port skipping: 4, last L104 (farm inputs at wrong port).
  - L110-118 market-subversion points: 4, last L118. L121-126 barriers: 3, last L126.
  - L141-148 evidence of stevedore monopoly-like status: 4, last L148.
  - L174-184 vulnerabilities quoted from NFF's earlier PC submission: 6, last L184 (biosecurity risk).
  - L186 near-miss events (prose): Ad-Blue, fertiliser, workforce, pallet shortages.
  - L192-255 detailed recommendations 1-8; recommendation 8 runs L234-255 and adds $140 million
    (L240) and a broader heavy-vehicle access proposal: 4 bullets L244-250 plus an unbulleted fifth
    item on NHVR resources L252-255.
- Forecasts, guidance, deadlines, effective dates: $78 billion farm production forecast for 2021-2022
  (L24); $100 billion by 2030 target (L44); global fleet +20% by 2023 (L130); 60-day notification
  proposal (L204); $2.5 billion over four years (L77, L213); $140 million over four years (L240);
  advisory council to identify risks "in the coming twelve-months" (L221).
- Hedged claims: L66 inefficiencies have "the potential for significant impact"; L85 "up to 50% ...
  can go"; L128 increases "cannot be deemed as purely market driven"; L130 "would increase"; L155
  "there would likely be more pushback" (hedge on the counterfactual); L196 ACCC study "suggested that
  the class exemptions offered could be narrowed"; L199 operational exemptions "could be maintained";
  L201 price-related exemptions "could fall outside of the exemption"; L206 "A potential option is";
  L209 "arbitration may rule in favour of claims made by maritime workers" (side clause; the
  recommendation itself is firm); L238 "Feedback from NFF members suggest". Firm: L135 "This
  discrepancy can only be attributable to domestic factors"; L105 costs "cannot be apportioned to
  international supply and demand drivers".
- Rounded prose beside exact figures: "3-4 times" (L56) vs "up to three to four times" (L135); "more
  than 75%" (L44, L83); "some 10,000 km shorter (one-third)" (L86); 633% (L110) beside itemised prices
  (L91-96); "millions of dollars" for the Fremantle diversion (L104, L152, L209).
- Operative definitions, rules and scope exceptions: L59/L112 Section X exemption described as
  "allowing the coordination of supply and sharing of price data"; L198-201 split of exemptions:
  operational coordination ("scheduling of services collectively, pooling vessels etc.") could be
  maintained vs "price coordination, sharing of commercial data, and coordinating the allocation of
  market share between the three alliances" could fall outside; L202 stevedores to be barred from
  ad-hoc levies "particularly on parties that have no contractual arrangements with the stevedore";
  L207 arbitration "as per the powers afforded to it by the Fair Work Act based on national interest
  considerations"; L246 tolerance applies "where overall mass is within limit". L53 scope note: "The
  examples provided in the current submission focus on containerised freight." L172 quoted PC scope
  exclusion: "Food, while essential, is excluded from the analysis ...".
- Actions vs mentions: NFF actually "provided significant verbal feedback directly to the Productivity
  Commission" in February (L54) and promises case studies "in subsequent submissions" (L54, intent);
  NFF "sought that food and fibre production be explicitly analysed" in its earlier submission (L174);
  shipping lines "often simply skipped ports" (L99); stevedores "added further levies" in January
  2022 (L96); farm machinery "was instead diverted to Port Melbourne" (L152). Recommendations are
  proposals only.
- Amendments or contradictions (internal): "Section X" vs "Part X" naming (L59/L71/L112/L193 vs L198);
  summary recommendation 2 (L72, "restrictions against stevedores having the ability to impose ad-hoc
  levies") vs detailed recommendation 2 (L202-204, adds 60-day notice); recommendation 6 "industry-
  government council" (L79, L217) vs "industry-government-civil society advisory council" (L221).
- Coverage: FULL. Ledger: L1-263 read sequentially (one chunk); nothing remaining. Spot-checks: page
  markers 5-16 all present; table n/a; footnote n/a; 40ft freight line L95 = original L93, identical.
  Gap (unresolved, not unread): heading "NFF Member Organisations" (L8; contents L39 says page ii) has
  no member list in text or original (original L6) - likely non-text content.

## D05 - South Australian Wine Industry Association Incorporated (SAWIA) submission

- Source: `text/D05.txt` L1-312 | 12 printed pages: cover L3-15; page numbers sit at the end of the
  repeated letterhead lines (2 L19, 3 L42, 4 L72, 5 L116, 6 L143, 7 L178, 8 L206, 9 L234, 10 L265,
  11 L280, 12 L307); ends "E N D" (L309). Footnotes 1-19 at page feet (L109-112, L138-139, L172-174,
  L228-230, L258-261, L275-276, L301-303).
- Written or submitted by: SAWIA, "SUBMISSION OF: SOUTH AUSTRALIAN WINE INDUSTRY ASSOCIATION
  INCORPORATED" (L9-10), ABN 43 807 200 928 (L3), address National Wine Centre, Botanic Road,
  Adelaide (L11-14). No individual signatory. Organisations quoted/cited (not authors): Wine Australia
  (fn1, fn4, fn6, fn7; quote L137-145); Hillebrand and Flinders Port Holdings (reported inside the Wine
  Australia quote, L137, L145); ACCC (L147-149, L160-179, L207-236, L256, L268; fn8-12, fn14-15); SA
  Government Consumer and Business Services (fn2); SA Department of Treasury and Finance (fn5);
  Australian Financial Review / David Marin-Guzman (fn13 L260); Department of Infrastructure,
  Transport, Regional Development and Communications (L274, fn16); Infrastructure SA (fn17);
  Infrastructure Australia (fn18); Reuters, S&P Global, The Loadstar (fn19); PC Workplace Relations
  Framework Inquiry 2015 (L239-250). Own data: SAWIA survey January-February 2022 (L119-134, L151,
  L196) and a member example (L153-154).
- Type, date, edition: submission dated 11 February 2022 (L15). One edition.
- Period covered: calendar-year export data "12 months to 31 December 2021" (fn4 L112), "year ended
  December 2021" (L116), "year to December 2021" (L107); survey "January-February 2022" (L119);
  "last 12 months" (L151); "Over the last two years" (L26, L132, L154); financial-year label "since
  2013-14" (L265); ACCC report "2020-21" (fn8 etc.) and "2017-18" (fn12).
- Entities and aliases: SAWIA = "South Australian Wine Industry Association (Incorporated)" (L3, L20,
  L43); founded 1840 as "the Society for the Introduction of Vines" (L43). ACCC named "The Australian
  Competition and Consumer Commission (ACCC)" (L147) but "Australian Consumer and Competition
  Commission" in fn8, fn10, fn11, fn12, fn14 (L173, L228, L229, L258, L261); report titles "ACCC's
  Stevedoring report" (L160), "Container Stevedoring monitoring reports" (L226). Infrastructure SA
  (L280, L301) = "Infrastructure South Australia" (L286). Ports: Port Adelaide (L128, L299), "the
  Adelaide port" (L270), Adelaide (L26, L149, L196, L265-266), Melbourne/Port of Melbourne (L128,
  L266, L268), Sydney (L128, L209, L212, L266), Port Botany (L268). Patrick Terminals (L251). Fair
  Work Act 2009, Fair Work Commission (L224). Wineries named: Henschke's Eden Valley estate, d'Arenberg
  in McLaren Vale, Penfolds Magill Estate (L84). Regions: Southern Flinders Ranges, Mount Gambier,
  Kangaroo Island, Riverland (L81). Roads/rail: Sturt, Dukes, Riddoch, Princes Highways; Melbourne-
  Adelaide and Sydney-Adelaide rail lines (L271); Sturt Highway (Renmark to Gawler) project (L272);
  Sturt Highway and Truro bypass project (L287).
- Quantitative index:
  - L24 and L86: SA "58% of the volume and close to 70% of the value of total Australian wine exports".
  - L32, L81, L254: 18 wine regions. L47 membership "approximately 96% of the grapes crushed in South
    Australia and about 36% of the land under viticulture". L68 SA "more than half, 52%, of the
    national grape crush".
  - L82 "1,200 licensed producers" (fn2, SA Government CBS 2019); 2016 Census "around 8,400 people"
    in grape growing or wine manufacturing in SA (fn3 exclusions L111).
  - L103 "In 2021, 813 wine producers exported South Australian wine."
  - L105 "March 2021 confirmation of the imposition of 218% duties imposed by China, effectively closing
    that market to Australian bottled wine until 2026"; China market "$1.2b for Australian wine ($700m
    for SA)" (no footnote).
  - L107 wine was SA's largest export commodity by value "Up until December 2021"; "33% fall ($637M) in
    export value in the year to December 2021"; overtaken by wheat (fn5 SA DTF, SA Overseas Exports,
    December 2021).
  - L116 (Wine Australia, fn6) national wine exports fell "30% in value and 17% in volume in the year
    ended December 2021"; China exports fell 97% in value and 93% in volume, "a loss of nearly $1
    billion". L117 exports go to 96 countries.
  - L128 ports used: Port Adelaide (100%), Melbourne (71%), Sydney (14%) (base not stated).
  - L132 survey ("always or often"): delay in departures 77%; difficulty accessing containers 65%; delay
    in delivery 60%; delays to pick up 58%. L134 missing port 40%.
  - L145 (Wine Australia quote, Flinders Port Holdings) "Australia also represents only 1 per cent of
    global container throughput".
  - L149 (ACCC, fn8) "20% of shipping services bypassing Adelaide". Note: the "8" opening L149 is the
    footnote marker, not a quantity.
  - L151 members' cost increases in the last 12 months: 63% saw 100-200%; 15% saw 200-400%; 7% saw
    400-600% (mapper arithmetic: 85% accounted for; remainder not described).
  - L153-154 one member in "more than 100 markets" saw "a 400% increase in shipping costs over the last
    two years".
  - L196 outlook: 46% "about the same"; 45% "worse or much worse" (mapper: 91% accounted for).
  - L200 clearance delays "up to two weeks". L209-212 (ACCC, fn10): Sydney and Melbourne "in the bottom
    15%-10% of ports globally"; median in-port time "3 times longer than Japan, twice as long as China
    and 50% longer than Singapore or New Zealand"; "4 of out 5 Australian ports" in bottom quartile;
    "average of 21 hours sitting idle in Sydney".
  - L223 enterprise agreements approved after disputes of "up to two and a half years in some cases".
  - L256 (ACCC, fn14) "over the last decade only 10-12% of containers ... transported by rail".
  - L265 (fn15 Ibid = ACCC 2020-21) rail market share "increased with over 16% in Adelaide since
    2013-14, whereas it has declined with one percent nationally" (points vs percent not stated).
  - L266 Adelaide rail share "more than 20%", Melbourne 6%, Sydney 15% ("five major Australian ports").
  - L280 (Infrastructure SA, fn17) national target "80% of all road rating above three stars"; "74%"
    of SA roads rated one or two stars out of five. L282 (Infrastructure Australia, fn18) "75% of
    state-owned roads in South Australia are life-expired".
  - L285 20-Year State Infrastructure Strategy released 2020 (fn17: May 2020); L286 Capital Intentions
    Statement covers "the next five years"; L287 "2021 Capital Intentions Statement".
- Tables:
  - Figure 1 "Crush by State" (L72-80; source fn1 L109 Wine Australia 2021, National Vintage Report
    2021). Column "% of total crush": SA 52%, NSW 29%, Vic 17%, WA 2%, Tas 1%, Qld <1%. Mapper
    arithmetic: printed shares sum to 101% plus "<1%" (rounding).
  - Figure 2 "Wine exports by State" (L88-102; source fn4 L112 Wine Australia 2022, SA State Export
    Report, 12 months to 31 December 2021). Columns: Volume (million L) | % of total volume | Value
    (million AUD) | % of total value. Rows: SA 362 | 58% | $1,376 | 68%; NSW 163 | 26% | $357 | 18%;
    Vic 88 | 14% | $245 | 12%; WA 5.6 | "1" (no % sign, L99) | $42 | 2%; Tas 0.7 | <1% | $9.3 | <1%;
    Qld 0.1 | <1% | $0.6 | <1%; TOTAL 619 | 100% | $2,029 | 100%. Mapper arithmetic: volumes sum to
    619.4; values sum to 2,029.9 vs printed $2,029 (component rounding).
  - Unlabelled survey table "top five export destinations" (L119-127; SAWIA survey Jan-Feb 2022),
    captured as: "Rank Country % of respondents / 1 UK Canada 82% Singapore 2 / US 79% Hong Kong / 3
    EU, exl Germany 75% / 4 NZ 71% / 5 / South Korea 69% Japan". Nine country names for five ranks;
    the alignment of Canada, Singapore, Hong Kong and Japan to ranks/percentages is ambiguous. The
    original has the same layout (original L120): UNRESOLVED visual table.
- Lists (count; last item): L51-56 SAWIA service areas 4 (last "Promotion and Opportunities" L56);
  L59-63 terms of reference addressed: 2, 3, 5 (three items, last L63); L84 three named vineyards;
  L160-179 ACCC-quoted consequences: 8, last "Inability to meet contractual obligations" L179 (after the
  page-6 footnotes and page break); L185-193 member mitigations: 8, last "Notify customers..." L193;
  L207-213 ACCC port-performance points: 5, last "Protracted industrial disputes" L213; L241-246 PC 2015
  inquiry matters: 4, last L246; L271 National Land Transport Network examples ("to name a few");
  L294-299 requested Federal actions: 4, last "Investigate capacity issues at Port Adelaide for bulk
  carriers" L299.
- Forecasts, guidance, deadlines, effective dates: China duties close market "until 2026" (L105);
  industry "does not expect the challenges to resolve in 2022" (L36); Wine Australia quote: crisis "not
  expected to be resolved before the end of 2022" (L145); survey outlook (L196); on-dock rail at
  Melbourne and Port Botany "over the next couple of years" (L268, ACCC); media: "further deterioration
  predicted" (L290, fn19).
- Hedged claims: L38 and L291 governments "may have little power and influence" (hedge on government
  capacity; the following "should be able to alleviate" is firm); L145 "not expected to be resolved"
  (quoted forecast); L158 FOB costs "may flow on to the wine producer"; L200 "what has been perceived as
  inefficient inspection and approval processes"; L224 IR system "appears to embolden unions"; L236
  quoted ACCC 2018: "This may be having an impact on the ability of Australia's ports to be
  internationally competitive"; L251 "too early to say whether this is an isolated improvement or an
  industry-wide trend"; L256 "this could result in increased road congestion" (conditional on the split
  continuing). Firm: L30/L198 ports "have been internationally uncompetitive ... well before the
  outbreak"; L248 "SAWIA is unaware of the Federal Government responding to the recommendations via
  legislation" (negative evidence).
- Rounded prose beside exact figures: "close to 70% of the value" (L24, L86) vs Figure 2 68% (L96);
  "58% of the volume" (L24, L86) = Figure 2 58%; "more than half, 52%" (L68) = Figure 1 52% (L75);
  "loss of nearly $1 billion" (L116) vs China market "$1.2b" (L105, a market value, different measure);
  "around 8,400 people" (L82).
- Operative definitions, rules and scope exceptions: fn3 (L111) the 8,400 Census count "excludes casual
  workers such as grape pickers and other seasonal workers not working in those industries in the week
  prior to the Census" and "people who worked in the wine and grape production industry as a second
  job"; L158 FOB contracts: "increased costs are incurred by the customer"; L224 Fair Work Act 2009 /
  Fair Work Commission oversee industrial action and enterprise agreement applications; L280 national
  target definition "80% of all road rating above three stars".
- Actions vs mentions: SAWIA ran the Jan-Feb 2022 survey (L119); members "implemented a number of
  changes" (L185-193); wineries "reported orders being cancelled" (L27, L181); Patrick Terminals
  announced an in-principle agreement (L251, reported via fn13); ACCC "noted" issues in consecutive
  reports (L226). SAWIA's requests (L294-299) and "would recommend" (L250) are proposals.
- Amendments or contradictions (internal): body "in November 2018, the ACCC noted" (L234) vs fn12
  "Container stevedoring monitoring report, 2017-18, October 2018" with publication year "2021" (L258);
  ACCC name inverted in footnotes (above); "close to 70%" (L24, L86) vs 68% (L96); Figure 2 value
  total (above). Note: SA wine export value from two different sources: Figure 2 SA $1,376m (Wine
  Australia, fn4) and the $637M / 33% fall (SA DTF, fn5); mapper arithmetic: $637M is 31.6% of
  $1,376m + $637m, so the two sources are not on an identical basis; the document does not reconcile.
- Coverage: FULL. Ledger: L1-312 read sequentially (one chunk); nothing remaining. Spot-checks: 12
  page numbers present; Figure 2 rows L96/L102 = original L94/L100 (tab-separated, identical); fn9
  "Ibid. p. ix" L174 = original L172; survey table garble identical in original L120. Gaps
  (unresolved): L274 "Source: Department of Infrastructure, Transport, Regional Development and
  Communications 2020" has no figure content (map/graphic absent in text and original L272); survey
  table alignment (L119-127).

## D06 - Australian Food and Grocery Council (AFGC) submission

- Source: `text/D06.txt` L1-170 | printed page markers "| 2" L8, "| 3" L15, (no "| 4"), "| 5" L45,
  "| 6" L64, "| 7" L89, "| 8" L112, "| 9" L128, "| 10" L140, "| 11" L157, "| 12" L160, "| 13" L166
  (page 13 carries only the running header). Key Recommendations (L32-43) sit between the "| 3" and
  "| 5" markers. Stray "‘" at L13. No footnotes.
- Written or submitted by: Australian Food and Grocery Council (L11, L30); signed Tanya Barden OAM, CEO
  (L28-30). Organisations quoted/cited (not authors): ACCC Container Stevedoring Monitoring Report
  (L19, L119-133); Productivity Commission's study on Vulnerable Supply Chains (L19); Essential Services
  Commission of Victoria (L121, inside the ACCC findings list); World Bank and IHS Markit and UNCTAD
  (L133, only inside an ACCC quote); Competition Policy Review (Harper Review) 2015 (L144); Biosecurity
  Australia (L98-99); AFGC's own "Sustaining Australia 2030 report" (L138). Member examples are AFGC's
  own evidence (L56-115, L132, L138).
- Type, date, edition: submission, "February 2022" (L6, running header); no day given. One edition.
- Period covered: "over the past 12 months" (L138), "YoY" (L73), "over recent years"/"past few years"
  (L56, L138), "a decade" (L138), "the past 3 years" (L126, ACCC), 2019 (L133, UNCTAD), 2020 (L121
  ESC), 2015 (L144), target 2030 (L118), exemption to 31 March 2022 (L152).
- Entities and aliases: AFGC; "fast-moving consumer goods (FMGC)" (L50, sic) = "FMCG" (L126); ACCC;
  "terminal access charges (TACs)" (L142; also L33, L137, L163); "general rate increases (GRIs)" (L75);
  "Chain of Responsibility (CoR) fees" (L114); "Part X of the Competition and Consumer Act 2010" (L38,
  L144, L148, L163); "section 11 exemption of the Coastal Trading (Revitalising Australian Shipping) Act
  2012" (L40, L152, L163); "Sydney (Port Botany)" (L84-85); Melbourne (L78-79, L85, L121, L133); Port
  of Melbourne (L121); Western Australia (L152); "East-to-West Coast rail line and Stuart Highway"
  (L115); "Biosecurity Australia" (L98-99); "Competition Policy Review (Harper Review)" (L144).
- Quantitative index:
  - L11 "$132 billion food and grocery supply industry", "employing 270,000 people". L18 "over $80
    billion of the nation's two-way international trade"; sector called "Australia's largest
    manufacturing sector".
  - L73 "YoY shipping freight costs have escalated up to ten-fold". L138 "Current prices have escalated
    10-fold over the past 12 months" (context: detention charges, tariffs and surcharges); "millions of
    dollars" in TACs, surcharges and detention fees over "the past few years"; sector profitability fell
    "from $8bn to $5bn" over a decade (AFGC Sustaining Australia 2030 report).
  - L118 ambition "to double in size by 2030 to $250 billion" (beside $132 billion at L11).
  - L121 "Privatisation of the 4 major container ports" (ACCC finding).
  - L126-130 ACCC quote: "in the past 3 years ... an exporter ... had to deliver its cargo to another
    port for a period of 3 weeks ... This cost the exporter $200,000".
  - L133 ACCC quote: World Bank and IHS Markit study "ranked Australia's largest container ports,
    Melbourne, and Sydney, in the bottom 15% and 10%, respectively, of the 351 global ports"; UNCTAD
    "in 2019, the median in-port time ... was 3 times longer than Japan, twice as long as China and 50%
    longer than Singapore or New Zealand".
  - L158 "a projected doubling of the number of trucks required" (no figure or source).
  - L163 "The AFGC presents seven key recommendations" (= 7 listed L33-43).
- Tables: none.
- Lists (count; last item): L21-25 aims 3; L33-43 recommendations 7, last R7 L43 (infrastructure
  investment: larger ships, rail access, empty container parks); L57-69 key impacts of shipping delays
  9 (spans page break; last L69 reserve stocks); L70-81 examples of freight costs 6 (last L81); L82-92
  cancellation of sailings 6 (last L92); L93-99 uncertainty/capacity 5 (last L98-99 Biosecurity
  Australia); L100-103 digital technologies 3; L104-115 other matters 8 (last L115 East-West rail line
  and Stuart Highway; coastal shipping); L119-125 ACCC findings 4 (last L125 industrial relations).
  Section headings L82, L93, L100, L104 echo the inquiry terms-of-reference wording (see D19 L696-698).
- Forecasts, guidance, deadlines, effective dates: s11 exemption "for voyages by container and
  roll-on, roll-off vessels to Western Australia until 31 March 2022" (L152); 2030 doubling to $250
  billion (L118); carriers "expected to attract premium freight rates" with cleaner fuels such as
  hydrogen (L134); charges "unlikely to subside over the short-to-medium term" (L138); "projected
  doubling" of trucks (L158).
- Hedged claims: L56 AFGC "understands" costs were "primarily driven by" the pandemic response; L79
  "may lead to further issues with reverse logistics"; L97 "Emerging evidence"; L98 "There is evidence";
  L134 "may add further costs" and "are expected to attract premium freight rates"; L138 "unlikely to
  subside"; L148 "There is growing risk that without repeal that shipping lines could use Part X to
  artificially elevate freight rates" and "the ACCC could administer processes"; L158 "This may reduce
  cost-associated pressures", rail "considered more efficient"; L163 performance metric "may act to
  drive competition"; L164 "may also act to support". Firm: L55 absorption "categorically
  unsustainable"; L138 "Current prices have escalated 10-fold".
- Rounded prose beside exact figures: "up to ten-fold" (L73) vs "10-fold" (L138); "double in size ...
  to $250 billion" (L118) vs $132 billion (L11); "millions of dollars" (L138).
- Operative definitions, rules and scope exceptions: R4 (L38) repeal Part X "with retention of shipper
  collective bargaining provisions"; L144 Harper quote "A block exemption granted by the ACCC should be
  available for liner shipping agreements that meet a standard of pro-competitive features" (D10
  L103 and D11 L94 render the same recommendation with "minimum standard"); L146 class exemption scope
  favoured by stakeholders: "limited to operational coordination that should not include prices";
  L152 s11 exemption scope (container and ro-ro voyages to WA, to 31 March 2022); L137 proposed rule
  that stevedores levy charges on shipping clients "rather than on third party transport operators";
  L19 scope: "We do not address the terms of reference in full."
- Actions vs mentions: Federal government granted the s11 exemption (L152, actual); "The ACCC has also
  proposed to develop a class exemption" and ran "a public review seeking stakeholder views" (L146,
  stated in present tense; compare D10 L115-120); ESC Victoria "found in 2020" (L121); AFGC members
  "have absorbed millions of dollars" (L138); "To date the costs ... have been absorbed" (L55). The
  seven recommendations are proposals.
- Amendments or contradictions (internal): FMGC/FMCG spelling (L50 vs L126); missing page-4 marker;
  otherwise recommendation count consistent (7 at L33-43 and L163).
- Coverage: FULL. Ledger: L1-170 read sequentially (one chunk); nothing remaining. Spot-checks: page
  markers as listed ("| 3"/"| 5" at original L13/L43); table n/a; footnote n/a; Recommendation 7 L43 =
  original L41; L130 ellipses = original L128 (two U+2026). Gaps: none beyond the absent page-4 marker.

## D08 - Victorian Transport Association (VTA) submission

- Source: `text/D08.txt` L1-324 | "Page 1 of 15" (L3) through "Page 15 of 15" (L312), all 15 present.
  Footnote-style source notes "(1)" at L109, L144, L165.
- Written or submitted by: "Submission on behalf of the Victorian Transport Association" (L6-7);
  "Submitted by: Peter Anderson - Chief Executive Officer" (L9-11; signature L320-321); address Level 1,
  Mirrat House, 46 Kooringa Way, Port Melbourne VIC 3207 (L13-15). Organisations mentioned (not
  authors): Victorian Government, which created the VPPM (L78); Dept of Transport "Voluntary Performance
  Monitoring Framework - Q3" (data source, L144, L165); VTA Industry Survey (own data, L109);
  stevedores, shipping lines, empty container parks (throughout); Sydney's PIBLIS arrangement "managed by
  an independent Government Statutory Authority" (L214-216).
- Type, date, edition: submission dated 11 February 2022 (L8), title "Response to the Inquiry into the
  long-term productivity of Australia's Maritime Logistics System" (L4-5). One edition.
- Period covered: calendar quarter "3rd quarter of 2021 (July/ August/September)" (L86); footnote
  "Q3" without year (L144, L165); "per annum"/"pa" throughput and costs (L147-155); "three years ago"
  / "in 3 years" (L131, L206); history from 1969 (L316).
- Entities and aliases: VTA (L7, L19, L51); "Voluntary Port Performance Model (VPPM)" (TOC L25; L78-82;
  heading "2.2 VPPM" L80) vs footnote name "Dept of Transport- Voluntary Performance Monitoring Framework
  - Q3" (L144, L165); stevedore charge names: "Infrastructure Access Charge" (L131), "Infrastructure
  Levy"/"Infrastructure levy" (L206), "Infrastructure Charge" (L206), "Infrastructure fee ... now called
  the Infrastructure Access Fee" (L235); "PIBLIS" (L214, L218; spelled "PBLIS - Port Botany Landside
  Improvement Strategy" in D13 L88); "Wharf Carriers Depot" (L152); vehicle types "Single Semi trailers",
  "B/Double", "HPFV/A/Double" (L105-107), "multi combinational" (L140), "HPV's"/"Higher capacity
  vehicles" (L265-266); "Carrier" used for the road transport operator (L159-161, L271-285); Port of
  Melbourne / "Melbourne wharves" / "port of Melbourne" (L71, L140, L188, L219, L313, L316); Yarra River
  (L64); Port Rail Shuttle project, Inland rail (L191); Sydney waterfront (L214-218).
- Quantitative index:
  - L51 "over 800 members"; L52 "over 100 years' experience"; L64 ships worked "within a kilometre of the city".
  - L82 VPPM released data "for the past 3 months". L86-93 table (below).
  - L100 average age of port vehicles "7 years".
  - L105-107 fleet table (below).
  - L131 "Infrastructure Access Charge increasing from $3.57 to more than $140.00 per TEU in 3 years".
  - L140 "approximately 50% of the vehicles now attending the Melbourne wharves are multi combinational
    with a carrying capacity of 6-8 TEU each the current average is 2.5 TEU (1) with vehicle
    backloading at 25%" (source L144).
  - L147 "approximately 3million TEU pa (1) handled through Melbourne with a load factor of 2.5 TEU
    vehicle per trip resulting in approximately 1.2million truck trips pa" (source L165).
  - L148 load factor 3 TEU per vehicle per trip cuts trips by 200,000 pa; 3.5 TEU cuts trips by 342,857
    pa. L150 4 TEU cuts trips "by approximately 450,000 pa".
  - L152 "over 95% of all international shipping containers are transited via a Wharf Carriers Depot".
  - L155 balanced-loading inefficiency "additional cost of approximately between $69,000,000.00 and
    $155,250,000.00 per annum" (method not stated). L156 emissions, social licence and congestion
    values "have not been evaluated".
  - L179 penalty proposal: ship arriving or departing "outside an allotted 6 hour window either side of
    its schedule movement"; L181 "24 hours notice on late arrival"; L183 "Applied in 6 hour blocks".
  - L195 stevedores operate "24 hours per day, 7 days a week"; delivery points "Monday to Friday
    between 7am and 5pm"; import containers collected "within 3 days or be fined hundreds of dollars per
    day". L196 empties returned "within 10 days of collection or be fined hundreds of dollars a day by
    the shipping line"; container parks "only operate 8 hours per day, Monday to Friday".
  - L206 "Infrastructure Levy of currently up to $140.00 per container"; "increase of the Infrastructure
    Charge from less than $3.57 per TEU three years ago to over $140.00 per TEU today".
  - L208 operators "increase charges to customers 3-4 times per year". L211 planning "24 hours prior".
  - L214 PIBLIS in Sydney "in place for over 10 years". L247 "current average load per vehicle is <2.5
    TEU per movement. The estimated capacity is 3.5 TEU per vehicle." L283 "all three container
    stevedores". L316 first container movement 1969.
  - Mapper arithmetic: 3,000,000/2.5 = 1,200,000; /3 = 1,000,000 (-200,000); /3.5 = 857,142.86
    (-342,857.14); /4 = 750,000 (-450,000): printed reductions match. $69,000,000/200,000 = $345 and
    $155,250,000/450,000 = $345; no per-trip cost is stated in the document.
- Tables:
  - L86-93 VPPM summary "For the 3rd quarter of 2021 (July/ August/September)": Average TEU per Vehicle
    <2.5; Average balanced loading <25%; Average slots available / day <1300; Average total Containers to
    be moved / day >3,000; Average TEU's handled / Timeslot <2.0; Average Containers per Truck <2.0
    (values are bounds, tab and "-" separated). Port implied by section "2.0 Containers in the Port of
    Melbourne" (L71).
  - L102-109 fleets servicing the container ports, "categorized approximately" (source "(1) Source: VTA
    Industry Survey" L109). Columns: Type | Number | Capacity/vehicle | Ave $ / Hour. Rows: Single Semi
    trailers | >50% | 2 x TEU | 80.00; B/Double | <40% | 3 x TEU | 115.00; HPFV/A/Double | <10% | 4 x
    TEU | 135.00. "Number" is given as percentage shares; currency only "$".
- Lists (count; last item): TOC L18-45 (sections 1.0-6.0; 3.1-3.12); L111-124 factors restricting
  productivity 12 (numbered 1.1-1.12, last "Pricing / Cost Redistribution" L124); L158-161 load-factor
  measures 2; L241-299 three areas: 4.1 Asset Utilisation 7 (I-VII, L246-266, last "Promote the use of
  HPV's"), 4.2 Service Levels 6 (I-VI, L270-285, last "Slot Booking Fees"), 4.3 Network 4 (I-IV,
  L289-299, last "Social responsibility"); L301-313 VTA Recommendations 6, recommendation 6 alone on
  Page 15 (L313).
- Forecasts, guidance, deadlines, effective dates: containerised freight "expected to grow dramatically
  over the coming decades" (L76); Port Rail Shuttle "may alleviate" (L191); "planned terminal in the
  west of Melbourne"; "no decision on the Inland rail destination" (L191). No dated deadlines.
- Hedged claims: L128 stakeholders "may not have a direct commercial relationship" (side clause; main
  claim that this "allows for actions and directions that are monopolistic in practice" is firm, and
  ports, rail and shipping are "not, by definition, a monopoly"); L135 levies "not necessarily a bad
  thing"; L177 "a ship may miss its window" (scenario); L191 "may alleviate a percentage"; L259
  "arguably has one the biggest impact"; L271 "would see a marked improvement"; L285 "There could be
  process improvement"; L290 "This could lead to building things once"; L293 "would/could"; L296
  "would definitely lead". Firm: L131 "An exorbitant increase with no measurable productivity
  improvement"; L154 utilisation "is unsustainable"; L277 "There is no penalty of a ship being late".
- Rounded prose beside exact figures: VPPM bounds (<2.5, <25%) at L88-89 vs "current average is 2.5
  TEU ... backloading at 25%" (L140), "<2.5 TEU per movement" (L247) and "load factor of 2.5" (L147);
  "approximately 3million TEU" (L147); exact 342,857 (L148) beside "approximately 450,000" (L150);
  charge qualifiers "$3.57 to more than $140.00" (L131) vs "less than $3.57 ... to over $140.00" and "up
  to $140.00" (L206).
- Operative definitions, rules and scope exceptions: L73 verbatim definition: "'Landside' can be
  described as all transport activities relating to Import and/or Export of freight to or from the
  vessel, and/or to or from the end client" (import: from leaving the vessel to delivery incl. de-hire;
  export: from exporter's premises to loading, incl. hiring/collection of containers). L195-196 container
  handling rules (3 days; 10 days; fines "hundreds of dollars"). L200 duty rule: "an importer has up to
  the time of collection from the terminal to pay duties, upon which the container is released". L214
  PIBLIS applies "the same fines value and process to both Stevedores and the transport operator". L163
  load-factor measures "can only be enacted by the Stevedores". L111 factor list "include but are not
  limited to".
- Actions vs mentions: Victorian Government "has tried to alleviate ... by creating the VPPM model"
  (L78); VPPM "has recently released its data" (L82); stevedores "have elected to open their operations
  at 24/7" (L108); stevedores introduced the Infrastructure fee (L235); PIBLIS in place in Sydney
  (L214) vs proposal that it "needs to be implemented" in Melbourne (L219); ship-window penalty is a
  proposal (L179-185).
- Amendments or contradictions (internal): section numbering differs from TOC (factor list numbered
  1.1-1.12 at L113-124 vs TOC 3.1-3.12; "3. 1" L127; "2.12 Pricing / Cost Redistribution" L233 vs TOC
  3.12; "8. VTA Recommendations" L301 vs TOC "5.0"; "In Summary" L315 vs TOC "6.0 SUMMARY"; TOC "3.2 Fees
  and Penalties" vs heading "3.2 Fees, Penalties and Levies" L129); charge units "per TEU" (L131, L206)
  vs "per container" (L206); vehicle capacity 2/3/4 x TEU (L105-107) vs "6-8 TEU each" for multi
  combinations (L140) vs "estimated capacity is 3.5 TEU per vehicle" (L247); vehicle mix >50% semis /
  <40% B-doubles / <10% HPFV (L105-107) vs "approximately 50%" multi combinational (L140).
- Coverage: FULL. Ledger: L1-324 read sequentially (one chunk); nothing remaining. Spot-checks: 15/15
  page markers; fleet row L107 = original L106 and "(1) Source: VTA Industry Survey" L109 = original L108
  (identical); VPPM row L90 = original L89. Offset +2 to text L86 (original L84), +1 from text L88
  (original L87): original L85-86 (two empty lines) became one empty line (text L87); no content lost.

## D09 - Minerals Council of Australia (MCA) submission

- Source: `text/D09.txt` L1-177 | cover L3-7; running "Minerals Council of Australia | n" markers 2-10
  (L9, L14, L34, L47, L66, L79, L102, L127, L151); footnotes 1-9 (L74-77, L98-100, L125, L147, L149,
  L174). Bullets use a private-use glyph and several bullets are run together on one line (L23, L40, L64,
  L70, L83, L103, L112, L117); footnote 4 text (L98) and the lone marker "5" (L94) are interleaved with
  the Fair Work Act bullet list (L95-104).
- Written or submitted by: Minerals Council of Australia (L3-4, L9). No named signatory. Sources cited
  (not authors): Drewry World Container Index (fn1 L74); Sea-Intelligence GLP report issue 124, 27
  December 2021 (fn2 L76); Caterpillar Inc. quarterly report for period ended 30 September 2021, p. 50
  (fn3 L77); IHS Markit / The World Bank, The Container Port Performance Index 2020, published 2021 (fn4
  L98); PC Workplace Relations Framework Inquiry Report, Vol 2, 21 December 2015, pp. 683, 820 (fn5
  L99-100); NSW Ports, 30 Year Master Plan, October 2015, p. 44 (fn6 L125); BITRE Yearbook 2020 p. 69
  (fn7 L147); ACCC Container stevedoring monitoring report 2020-21, "released October 2021", p. 28 (fn8
  L149); BITRE 2019 aggregate freight forecasts, Research Report 152, p. 57 (fn9 L174); iMOVE CRC
  report (L135, no footnote). Industry examples "provided [to] the MCA" by participants (L59) are
  second-hand member evidence.
- Type, date, edition: submission dated 11 February 2022 (L7). One edition.
- Period covered: calendar-year labels (2019, 2020, 2021, "fourth quarter of 2021", January 2022, 3
  February 2022); "over the past year" (L21, L91); projection 2018-2040 (L163). No fiscal years.
- Entities and aliases: MCA; "IHS Markit in collaboration with the World Bank" (L86) = "IHS Markit / The
  World Bank" (L98), "Container Port Performance Index"; ACCC (L91, L143, L158-159; "Australian
  Competition and Consumer Commission" fn8 L149); NSW Government (L152); "NSW Ports Operations Hold Co Pty
  Ltd and its subsidiaries Port Botany Operations Pty Ltd and Port Kembla Operations Pty Ltd (together:
  NSW Ports)" (L152); "NSW Port Authority" (L109); Port of Newcastle, Port Botany, Port Kembla (L152-160);
  Gladstone/Port of Gladstone, Toowoomba (L115, L173); Port of Fremantle (L64); "Mining Equipment
  Technology and Services (METS)" (L71); Caterpillar Inc. (L73); "BITRE" = "Bureau of Infrastructure,
  Transport and Regional Economics" (L147, L174); Coastal Trading Act 2012 (L128); Shipping Legislation
  Amendment Bill 2015 (L132); Fair Work Act 2009 ss 172, 194, 409 (L97-104); Part IIIA of the Competition
  and Consumer Act 2010 and "the Treasurer" (L159); Australian Parliament (L95); National Freight Data Hub
  (L139); Inland Rail; Western Sydney Airport (L171-173).
- Quantitative index:
  - L17 "In 2021 Australia's resources exports totaled $351 billion or 68 per cent of total export
    revenue" (no source).
  - L23 (summary) a project "delayed by 40 days with a 22 per cent cost increase due to a break-bulk
    shipping provider reducing its services to charter only services"; haul-truck lead time "increased to
    15 months with cost increases of 12-15 per cent". L24 importer: berthing delays and demurrage in WA
    "cost its business $2 million".
  - L51 global steel demand rose "from September 2020". L57 flooding "in January 2022" disrupted freight
    to WA and NT.
  - Box 1 (L59-64): two projects - 8 per cent cost and 30 days delay; 22 per cent and 40 days (L61);
    trucks: mid-2021 little delay, "fourth quarter of 2021 ... 15-month lead time ... cost increases of
    12 to 15 percent" (L63); "In October 2021" an east-coast container shipment cost "double the cost of
    shipping the same container to China" (L64); importer "cumulative costs of $2 million" (L64); "At
    least five iron ore and gold mining companies in Western Australia" hit by industrial disruption at
    the Port of Fremantle (L64).
  - L69-70 "The average cost of shipping a 40' container peaked at over US$10,000 in mid-September" (year
    not printed); "As at 3 February 2022 it remains at least 79 per cent higher than a year ago" (fn1
    Drewry). L70 schedule reliability "approximately 33-40 per cent" (fn2). L71 METS: container shipping
    costs "rising by a factor of 4 to 5".
  - L86 CPPI covers "351 container ports"; "in 2020 Australian container ports ranked well towards the
    bottom" (no percentile printed in D09).
  - L89 "the four stevedoring companies that operate Australia's container ports".
  - L107 Port Botany terminal capacity "at least 7.2 million twenty-foot equivalent unit (TEU) per year"
    (fn6); "the port handled only 2.6 million TEU in 2019". L109 road carries "more than 80 per cent of
    Port Botany's container imports".
  - L152 privatisations "During 2013 and 2014"; "50-year port commitment deeds". L156 cap "30,000 TEUs
    per annum adjusted by an annual growth rate"; compensation "equivalent to the wharfage fee". L158
    (ACCC) arrangement "effectively doubles the cost of moving a container at the Port of Newcastle".
    L159 ACCC federal court case "in 2018 was dismissed and is currently on appeal".
  - L163 freight task "expected to grow by 25 percent from 2018 to 2040" (fn9 BITRE).
- Tables: none (Box 1 and Box 2 are prose boxes).
- Lists (count; last item): L23-24 summary examples 3; L36-45 recommendations 7 bullets, last the
  "principled framework for investment" with 4 sub-criteria L42-45 (last "considers and allows for the
  importance of resilience to disruption"); Box 1 examples 5 (last: Port of Fremantle disruption, L64);
  L68-71 global shipping points 3; L81-83 section summary 3; L95-104 Fair Work Act changes 4 (s172
  phrase; s194 prohibition; remove employer-union matters from s172; s409 "reasonable belief", last
  L104); L111-113 congestion measures 3 (last: land for warehousing); L115-117 regional-port investment
  conditions 3 (no resilience criterion, unlike L42-45); L170-173 possible investments 3, last
  "Investigating the viability of extending Inland Rail from Toowoomba to the Port of Gladstone" (L173).
- Forecasts, guidance, deadlines, effective dates: freight task +25 percent 2018-2040 (L163); suppliers
  "foreshadowing that higher costs will increasingly need to be passed on" (L26); regional port
  investments "will need to be made" in the medium term (L115); demand for supply-chain data "will only
  increase" (L141). Newcastle cap fixed "At the time of the privatisations" (L156). No dated deadlines.
- Hedged claims: L26 suppliers' foreshadowing (reported); L55 shipments delayed "in a few cases"; L73
  impact "is uneven"; L81 performance "could be improved"; L86 time in port "is arguably the most
  important" factor (hedge attaches to the ranking of the factor; the methodology statement "IHS Markit
  has applied a robust approach" is firm); L130 "have the potential to contribute more"; L143 risk "can
  (and in most cases is) addressed through price monitoring"; L159 regulation "could be achieved through
  a declaration by the Treasurer under Part IIIA"; L170 investments "could be supported ... may include".
  Firm: L27 global factors "are the most significant causes"; L128 the 2012 Act "reduced competition";
  L160 deeds "are a long-term barrier".
- Rounded prose beside exact figures: summary L23 "12-15 per cent" = Box L63 "12 to 15 percent"; "over
  US$10,000", "at least 79 per cent", "approximately 33-40 per cent" (L69-70); "at least 7.2 million"
  vs "only 2.6 million" (L107); "more than 80 per cent" (L109).
- Operative definitions, rules and scope exceptions: L152-156 port commitment deeds - Newcastle
  operators "must pay to compensate the operators of Port Botany and Port Kembla if container traffic at
  the Port of Newcastle is above a specified cap"; cap 30,000 TEUs pa adjusted by annual growth;
  compensation = wharfage fee. L97-104 proposed Fair Work Act text changes (s172 "'matters pertaining
  to' ... to 'matters directly related to'"; s194 express prohibition; s409 delete "reasonable belief").
  L128 regime contrast: previous licensing regime "allowed both Australian and foreign-flagged ships to
  engage in coastal trade"; current regime "discriminates against foreign-flagged vessels". L132 Bill
  2015 "would introduce a single permit system ... subjecting all vessels to the same conditions". L86
  CPPI scope: measures "the total amount of time ships are required to spend in port"; "restricted
  nature of the assessment".
- Actions vs mentions: curfew relaxation "was authorised temporarily during the early stages of the
  COVID-19 pandemic" (L112, actual past); NSW Port Authority "has prioritised" rail at Port Botany
  (L109); ACCC case 2018 dismissed, on appeal (L159); "federal government has also resisted regulation"
  (L159); National Freight Data Hub prototype website established (L139); Shipping Legislation Amendment
  Bill 2015 reforms "were proposed" (L132; no enactment stated); MCA recommendations are proposals.
- Amendments or contradictions (internal): summary example says the provider reduced "its services to
  charter only services" (L23) while Box 1 says it reduced "its regular break-bulk shipping services to
  Australia" (L61) and gives two projects (8%/30 days; 22%/40 days); investment criteria 4 (L42-45) vs 3
  (L117).
- Coverage: FULL. Ledger: L1-177 read sequentially (one chunk); nothing remaining. Spot-checks: page
  markers 2-10 present; fn1 L74 = original L72; fn4 L98 = original L96; Box 2 cap sentence L156 = original
  L154; "| 10" L151 = original L149. Table n/a.

## Shared ground (navigation only, part D documents)

- Submission dates: D03 14 February 2022 (L6); D05 11 February 2022 (L15); D06 "February 2022" (L6);
  D08 11 February 2022 (L8); D09 11 February 2022 (L7).
- ACCC Container Stevedoring Monitoring Report 2020-21 cited by D05 (fn8, fn9, fn10, fn11, fn14, fn15;
  L147-149, L160-179, L207-230, L256-268), D06 (L19, L119-133), D09 (L143, fn8 L149; also L91, L158-159);
  D05 also cites the 2017-18 edition (fn12 L258); D03 cites a separate 2019 ACCC study on ocean liner
  class exemptions (L193-199).
- World Bank / IHS Markit port ranking: D03 L56, L98 (bottom quartile, "according to the World Bank");
  D05 L209-211 (via ACCC); D06 L133 (ACCC quote, 351 ports); D09 L86, fn4 L98 (CPPI 2020, published 2021).
- Part X / "Section X": D03 L59, L71, L112, L193-201; D06 L38, L144-148, L163.
- Fair Work Act: D03 L207; D05 L224 (Fair Work Act 2009, Fair Work Commission); D09 L97-104.
- PC Workplace Relations Framework 2015: D05 L239-250; D09 L92, fn5 L99. PC vulnerable supply chains
  study: D03 L170-172, L219, L223; D06 L19.
- Coastal shipping and the January 2022 east-west disruption: D06 L40, L95, L115, L151-152, L163; D09
  L40, L57, L64, L122-132.
- Stevedore landside charges: D03 L96 (stevedoring costs per container); D06 L33, L137, L142, L163
  (TACs); D08 L131, L206, L235 (Infrastructure Access Charge/Levy/Fee); D09 L38 (TACs).
- Port of Fremantle disruption: D03 L152; D09 L64. Port of Melbourne: D03 L152; D05 L128, L209, L266,
  L268; D06 L78-79, L85, L121, L133; D08 throughout. Sydney / Port Botany: D05 L128, L209, L212, L266,
  L268; D06 L84-85, L133; D08 L214-218; D09 L107-109, L152-154. Adelaide: D05 L26, L128, L149, L196,
  L265-266, L270, L299.
- Curfews: D08 L193, L280; D09 L40, L112. Inland Rail: D08 L191; D09 L171, L173. HPVs: D03 L158-159,
  L237-240; D08 L107, L265-266. Empty container parks: D06 L43, L114; D08 L98, L108, L196, L237, L258.
  Detention/demurrage: D05 L156; D06 L34, L36, L138, L158; D08 L196, L237; D09 L24, L64.
- Periods: D05 Figure 2 = 12 months to 31 December 2021 (calendar); D08 VPPM table = calendar Q3 2021
  (July-September); D03 financial-year labels 2019-20 and 2021-2022 (undefined); D05 "since 2013-14".
- Forecast/ambition locations (no actuals for them inside part D): D03 L24 ($78 billion 2021-2022),
  L44 ($100 billion by 2030), L130 (fleet +20% by 2023); D06 L118 ($250 billion by 2030); D09 L163
  (+25 percent 2018-2040); D05 L36, L145, L196 (2022 outlook).
- Proposed vs actual: D06 L40 (permanence proposed) vs L152 (exemption granted to 31 March 2022); D06
  L146 (ACCC class exemption "proposed") vs D10 L115-120 (consultation from 3 December 2019; on hold since
  2020); D09 L132 (2015 Bill "proposed") vs L128 (2012 Act in force); D08 L214 (PIBLIS in Sydney) vs L219
  (proposed for Melbourne); D08 L179-185 (ship-window penalty proposal) vs L277 (no current penalty).

## Repeats elsewhere in the bundle

Whole-bundle searches of text/D01-D20 (regex, case-insensitive) with context reads of each hit. Values
are recorded neutrally with both locations; "different value" items carry different labels, periods or
sources as stated.

1. World Bank / IHS Markit port ranking and in-port time.
   - D06 L133 (ACCC quote): Melbourne and Sydney "bottom 15% and 10%, respectively, of the 351 global
     ports"; UNCTAD 2019 median in-port time 3x Japan, 2x China, 50% longer than Singapore or New Zealand.
   - D10 L39 (ACCC's own submission): same "bottom 15% and 10%, respectively, of the 351 global ports".
   - D13 L120-121: same, "15 per cent and 10 per cent respectively"; D13 L123 UNCTAD 2019, "three times".
   - D05 L209: "Sydney and Melbourne, ranking in the bottom 15%-10% of ports globally" (order Sydney then
     Melbourne; no "respectively", no port count); L210 same in-port ratios (no UNCTAD/2019 label); L211
     "4 of out 5 Australian ports ranking in the bottom quartile"; L212 "21 hours sitting idle in Sydney"
     (21 hours found nowhere else).
   - D09 L86 / fn4 L98: CPPI, 351 ports, "in 2020 ... ranked well towards the bottom" (no percentiles).
   - D16 L112-118 (Shipping Australia article, June 2021, on CPPI 2020): all Australian container ports
     except Brisbane in the worst 25%; Brisbane in the second-from-bottom 25%; all in the bottom 50%.
   - Bottom-quartile prose: D03 L56, L98; D16 L142. D07 L206, L604, L695 cite a different World Bank
     publication (2007 Port Reform Toolkit).
2. Stevedore infrastructure / terminal access charges (same subject, different values and units).
   - D08 L131 "$3.57 to more than $140.00 per TEU in 3 years"; L206 "up to $140.00 per container" and
     "from less than $3.57 per TEU three years ago to over $140.00 per TEU today" (Melbourne context).
   - D19 L336 (quoted statement, Port of Melbourne): "access fees ... increased from $3.60 to $80.00 per
     container over the past 2 years"; "infrastructure access fee by over 2 000 per cent in just two
     years"; Port of Melbourne lease "in March 2016".
   - D02 L174-182 Attachment A "INFRASTRUCTURE SURCHARGES - AS AT 25 January 2022 per full container /
     excluding GST" (columns STEVEDORE PORT EXPORT IMPORT EFFECTIVE; collated by APSA, FTA, CTAA).
     Melbourne rows: DP World $105.90 / $144.70 (1-Jan-22); Patrick $84.90 / $129.50 (1-Mar-21), then
     101.90 / 155.40 (7/03/2022); VICT $141.80 / $141.80 (1-Jan-22). Also Adelaide (Flinders Adelaide
     Container Terminal $75.00/$75.00, then 79.50/112.50 from 1/04/2022), Brisbane, Fremantle, Sydney.
   - D03 L96: "$25 per container in 2018 to $122 per container currently", plus up to $30 per container
     from January 2022, "total to $152 per container in 2022" (no port named).
   - D02 L104-113 (CTAA): NSW average fee for unloading an import container "$24.52 in mid-2017 to
     $121.87 in March 2021"; Table 1 (2017 | 2021 | Rise | Percentage rise): NSW $24.52 | $121.87 |
     $97.35 | 397%; QLD $34.63 | $118.59 | $83.96 | 242%; VIC $27.07 | $128.51 | $94.44 | 348%; Eastern
     Seaboard average $28.74 | "$122,99" | $93.55 | 325%.
   - D13 L222 "Infrastructure Surcharge/Terminal Access Charge (TAC) Increased 2,600% in 11 years";
     D13 L225-226 VICT Melbourne Landside Update 30 January 2019.
   - D11 L49-54: TACs at the Port of Melbourne increased "over the last 5 years" (chart not in text);
     D11 L60 a hay grower's extra $25,000 in the last year.
   - D02 L124-125 (ACCC quote): landside share of stevedore revenue ~13% (2010-11) to ~38% (2020-21);
     TACs ~20% of total revenue in 2020-21. D16 L152-159 'Infrastructure Surcharge' = 'Terminal Access
     Charges' (AMIC Rec 5, NTC review). D04 L63 regulation of TACs. D06 and D09 give no figures.
3. Notice period for charge changes: D03 L204 proposes 60 days; D02 L131-134 NTC voluntary guideline 30
   days, "Sixty days' notice operates at Port Botany"; D04 L60 "Min 30 days' notice periods"; D16 L136 US
   rule "30-day notice period by shipping lines".
4. Freight-rate increases (different measures and periods).
   - D03 L91-95 2019 $USD550/$USD850 vs 2021 peaks $USD3660 (20ft) and $USD4442 (40ft) per container
     incl. congestion charges; L110 "633% in the space of four years".
   - D09 L69-70 40' container average "peaked at over US$10,000 in mid-September" (Drewry WCI); "at
     least 79 per cent higher than a year ago" as at 3 February 2022; L71 METS "factor of 4 to 5".
     40-foot container 2021 peak: D03 L95 $USD3500 base / $USD4442 total vs D09 L69 over US$10,000
     (different series; neither document reconciles).
   - D06 L73 "up to ten-fold" YoY; L138 "10-fold over the past 12 months".
   - D05 L151 member ranges (100-200%, 200-400%, 400-600% in the last 12 months); L154 400% over two years.
   - D13 L82 (ACCC report) freight rates on key global routes "about seven times higher than ... just over
     a year ago"; D13 L61 "2-3 times the rates per km" Asia-USA/Europe; D10 L22 ACCC: rates "will abate".
5. Part X / class exemption / Harper Review.
   - D06 L148 "There is growing risk that without repeal that shipping lines could use Part X to
     artificially elevate freight rates in the future" ~ D10 L74 (ACCC) "there is a growing risk that
     shipping lines could use Part X of the CCA to artificially elevate freight rates in the future".
   - Harper quote: D06 L144 "meet a standard of pro-competitive features" vs D10 L103 and D11 L94
     "minimum standard of pro-competitive features".
   - Class exemption status: D03 L193-199 ("A 2019 ACCC study ... suggested"); D06 L146 ("The ACCC has
     also proposed to develop a class exemption"); D10 L115 consultation commenced 3 December 2019, L118
     support for operational cooperation (sailing timetables, slot swaps, pooling vessels), L120 work "put
     on hold in 2020", "yet to recommence".
   - Other Part X/Harper locations: D10 L71-75, L92-121; D11 L23, L94, L98; D15 L11, L105-117; D16
     L133-136; D19 L701 (TOR 7: Government's "in-principle acceptance" of Harper's repeal recommendation).
6. ACCC report 2020-21 release date (same report, different dates): D05 fn8/fn10/fn11/fn14 (L173, L228,
   L229, L261) "October 2021"; D09 fn8 L149 "released October 2021"; D10 L20 "On 3 November 2021, the ACCC
   released its Stevedoring Report 2020-21"; D10 fn1 L31 "ACCC website, 4 November 2021".
7. Repeated ACCC findings or quotations.
   - Regional monopolies: D09 L143 quotes "have the ability to extract monopoly rents" (report p. 28);
     D10 L66 "can extract monopoly rents".
   - ESC Victoria 2020 finding on Port of Melbourne land rents: D06 L121; D10 L68 (privatisation in 2016;
     L69 ESC final report 28 January 2022, revenue requirement overstated by around $300-650 million);
     D11 L74; D07 L263, L618.
   - Investment to fix inefficiencies "caused by larger ships, lack of rail access to Australian container
     ports and shortage of space in empty container parks": D06 L43 (AFGC R7); D10 L78 (ACCC finding);
     D15 L101.
   - "family and friends": D09 L91 (attributed to ACCC); D03 L150 ("family, friends and union members",
     NFF's own claim); D02 L162.
   - Pandemic effect wording: D05 L160 "derailed the global container freight supply chain" (report
     p. ix); D10 L22 "destabilised the global container freight supply chain".
   - Industrial action over "the past 3 years": D06 L126-130 (ACCC quote; exporter, 3 weeks, $200,000);
     D10 L42 ("for the past three years").
8. Patrick Terminals enterprise agreement: D05 L251, fn13 L260 (AFR, David Marin-Guzman, February 7
   2022; in-principle agreement "removing some of the restrictive work practices"); D10 L43 (26 October
   2021 application to terminate the MUA agreement), L44 (7 February 2022 in-principle agreement; "all
   employment decisions will now be at the full discretion of Patrick Terminals"), L61-62 (same AFR
   article). D18 L3 is a separate document dated 7 February 2022.
9. Coastal shipping and the January 2022 east-west disruption.
   - D06 L152 s11 exemption for container and ro-ro voyages to WA "until 31 March 2022"; D19 L205
     ("In January of this year ... the federal government exempted vessels from the requirements under
     the Coastal Trading (Revitalising Australian Shipping) Act 2012", no end date); D17 L24 ("temporary
     legislation" for foreign shipping between Eastern and Western states due to flooding); D19 L38
     (Jan 2022 SA flood, east/west rail inoperable); D13 L102 (Trans-Australia Railway washed away;
     "Stuart highway" flooded); D09 L57 (flooding January 2022, eastern states to WA and NT).
   - Coastal Trading Act 2012 elsewhere: D14 L28-48 (five-voyage temporary licence minimum); D20 L27-106
     (Act from July 2012; cabotage; 2019 review), L121-196 (temporary licence process); D19 L79 (coastal
     shipping ~17% of the domestic freight task), L97 (BITRE-based estimates). D09 L129 (coastal shipping
     flat in tonne-km, BITRE 2020) has no matching figure elsewhere.
10. Rail share and Port Botany (different values and periods).
   - Sydney/Port Botany rail share: D05 L266 "15% in Sydney" (ACCC via fn15) vs D13 L174 "Currently
     430,000 pa (14%) moving by rail. Target 3 million pa (40%) by rail by 2045".
   - Port Botany throughput: D09 L107 "2.6 million TEU in 2019" (capacity at least 7.2 million TEU per
     year, NSW Ports 2015 plan) vs D13 L167 "2.7 million TEU (today) to 8.4 million per annum by 2045".
   - Road share: D09 L109 road "more than 80 per cent of Port Botany's container imports" vs D13 L169
     "80% Import Containers delivered within a 40 kms radius of Port Botany" (different measure).
   - National rail share 10-12% (D05 L256) and Adelaide/Melbourne shares (D05 L265-266): no other
     location found.
11. Port of Melbourne volumes, terminals and operating hours.
   - D08 L147 "approximately 3million TEU pa" (Dept of Transport VPMF Q3) vs D01 L33 Port of Melbourne
     "currently services over 2.88 million" TEU annually.
   - D08 L283 "all three container stevedores" (Melbourne) ~ D01 L35 VICT is "the third international
     container terminal in the Port of Melbourne"; D09 L89 "four stevedoring companies" (national); D13
     L167, L198 "3 stevedores" (Port Botany).
   - 24/7 operation: D08 L108 "the stevedores have elected to open their operations at 24/7", L195
     "Stevedores operate 24 hours per day, 7 days a week" vs D01 L51 "VICT is the only terminal operator
     to perform Receipt & Delivery 24/7".
   - Truck turnaround: D08 L283 large variations across the three stevedores; D01 L63 VICT average
     "less than 35 minutes".
12. Port of Newcastle: D09 L145, L152-160 (privatised "During 2013 and 2014" with Botany and Kembla;
   50-year deeds; 30,000 TEUs pa cap; ACCC case 2018; Part IIIA declaration "by the Treasurer"); D12 L19
   (Port of Newcastle privatised in 2014 via long-term lease to Port of Newcastle Operations Pty Ltd
   (PNO)), L21-36 (Glencore Part IIIA application May 2015; ACCC arbitration; navigation service charges
   $0.76/$0.61/$1.04/$0.81 per gross tonne; NSWMC application July 2020) - D12 refers to "the designated
   Minister" (no "Treasurer" in D12); D13 L182 (Newcastle and/or Port Kembla as alternate container
   port); D04 L31; D07 L289 (NSW privatised Port Kembla and Port Botany).
13. Port of Fremantle industrial disruption: D03 L152; D09 L64; D18 L43, L48 (Qube dispute; MUA mooring
   bans, 27 October 2021 article); D15 L123.
14. NFF figures repeated by other agriculture submissions: "$2.5 billion over the four years" Infrastructure
   Fund (D03 L77, L213) = AMIC Recommendation 3 "$2.5bn over four years" (D16 L31, L138, L140); "$100
   billion industry by 2030" (D03 L44) ~ "$100 billion in farmgate value by 2030" (D16 L62, L65); New
   Zealand North-South routes (D03 L206) ~ VFF Recommendation 4 (D11 L25, L100); bottom quartile plus
   high freight prices (D03 L56, L135) ~ D16 L142.
15. Empty containers: D05 L149 (ACCC: shipping lines reluctant to send empties to Adelaide) ~ D11 L83
   (reluctance to send empty containers to Australia). ECP capacity and fees: D13 L186-201 (July 2021
   utilisation c.94% near Port Botany, c.27% outer, c.70% overall), L275; D02 L137 (Attachment B, some ECP
   fee increases "over 1,500 percent"); D16 L153-155. D08 L196 return rules (10 days) have no match.
16. PBLIS: D08 L214-218 "PIBLIS" (Sydney, over 10 years, reciprocal fines, statutory authority) = D13 L88,
   L271, L369 "Port Botany Landside Improvement Strategy (PBLIS) Mandatory Standards" (NSW Government
   model).
17. Freight task growth (different sources/periods): D09 L163 +25 percent 2018-2040 (BITRE 2019) vs D13
   L292 (NTC) domestic freight growth "26 percent by 2026".
18. Terms of reference: D05 L59-63 quotes TOR 2, 3, 5 ~ D19 L694-701 (Appendix B, TOR 1-7 full text);
   D06 L82, L93, L100, L104 headings echo TOR 2/5 wording; D06 L19 does not address TORs in full.
19. Curfews: D08 L193, L280; D09 L40, L112 ~ D11 L106 (truck curfews near the port); D19 L696 (TOR 2).
20. National freight strategy naming: D03 L213 "regularly updated National Freight Strategy" ~ D02 L79
   and D19 L701 "National Freight and Supply Chain Strategy".
21. Same number, different label: $200,000 = D03 L150 maritime salary per annum; D06 L130 one exporter's
   cost (ACCC quote); D19 L306 cadetship cost "$200,000 to $300,000". 68% = D05 L96 SA share of wine
   export value; D09 L17 resources share of total export revenue. "$140" = D08 L131/L206 per TEU or
   container; D03 L240 "$140 million"; D19 L403 "$140m annually".
22. No other location found for: D05 Adelaide bypass 20% (L149), 1 per cent of global container
   throughput (L145), 21 hours idle (L212), wine figures (wine appears only in D05 apart from single
   mentions in D02 and D07); D03 LEK 50% and Canada comparisons; D08 truck-trip and $69m-$155.25m
   figures; D09 $351 billion, 79 per cent, 33-40 per cent reliability, 30,000 TEU cap; D06 $132 billion,
   $250 billion, $8bn-$5bn.

## Gaps (part D)

- Unread ranges: none. D03 L1-263, D05 L1-312, D06 L1-170, D08 L1-324, D09 L1-177 all read in full.
- Unresolved (no visual original in bundle): D03 member-organisation list (heading L8 only); D05 figure
  after L274 (source line only); D05 survey table alignment L119-127; D11 L49-54 chart (other group).
- Resolved: D08 one-line offset change (original L85-86 two empty lines -> text L87 one empty line);
  cite D08 by text line numbers.
- Other documents were searched, not read in full; repeat locations above rely on local context reads.
