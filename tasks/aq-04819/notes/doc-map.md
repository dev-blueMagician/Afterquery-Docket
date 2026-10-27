# aq-04819 - document map

Navigation only (from `text/`); questions quote the documents, never this map. Line numbers are
`text/Dnn.txt` lines. **Page Doc N differs from local Dnn** (local ids are alphabetical by file name).

## Bundle

- What it is: ten academic papers on gambling advertising/marketing (two literature reviews, two
  population/panel surveys, one two-survey paper, four youth or family studies, one content analysis,
  one interview study). UK, Australia, Norway, Sweden.
- Documents: 10; capture `AQ-04819_2026-10-14_0948.txt`, "10 of 10 read in full (465,476 characters)".
- Gaps: none. No author lists or reference lists in the captured texts (citations are numbered or
  author-year only). Tables are pipe tables in the text.
- Extraction spot-checks (2026-10-14): text captures, no pages; each Dnn.txt matches its docs/ file
  (split + extract, `matches_capture: true` for all ten in notes/intake.json). Tables checked: Doc 6
  Table 1 (D05 133-147, column sums 31/4/4/3/27 = 69), Doc 7 Tables 1-2 (D08 117-149, rows sum to
  2,163; Table 2 sums to 2,090), Doc 3 Table 1 (D09 78-107), Doc 8 Tables 1-3 (D10 157-246).
- Provenance: notes/intake.json (capture sha 54bdf8b8...). Repeat check 2026-10-14: no file name or
  title shared with any bundle in 10.6, 10.7 or 10.8 (only other "Academic papers" set, aq-01650, is
  financial literacy).

| Page Doc | Local | Paper |
| --- | --- | --- |
| Doc 1 | D02 | Emergent gambling advertising; a rapid review (25 studies, 2015-2020) |
| Doc 2 | D07 | Norway 2019 survey: exposure to advertising types, impact, problem gambling (n = 5,830) |
| Doc 3 | D09 | Britain: marketing and unplanned spend, two YouGov surveys (emerging adults 2019, sports bettors 2020) |
| Doc 4 | D06 | UK (South London) recall of gambling ads/sponsorship, 99 young people + 71 adults, May-Jul 2018 |
| Doc 5 | D03 | Systematic review: gambling marketing strategies and the Internet (21 studies, 2000-Feb 2020) |
| Doc 6 | D05 | Live-odds advertising, 2018 World Cup on ITV (69 adverts, 32 matches) |
| Doc 7 | D08 | Sweden, Swelogs wave 4 (2014): self-reported negative influence of advertising (2,163 gamblers) |
| Doc 8 | D10 | Victoria: 111 basketball fans aged 11-16, timing/placement of ads, May-Jul 2018 |
| Doc 9 | D04 | Victoria: 59 family groups (59 parents, 61 adolescents 14-18), qualitative |
| Doc 10 | D01 | Norway: 12 people with current (5) or lifetime (7) gambling disorder, direct marketing, fall 2017 |

## Doc 1 (D02) rapid review

- Spend (D02 30-32): Australia "increased by 33% per year since 2011 to $273 million in 2018 [5]";
  UK "grew over 17% per year from 2014 to 2018, reaching an estimated total of £1.5 billion [6]",
  "10.34% of the £14.5 billion gross yield ... in 2018 [7]".
- Screening (98-105): 1353 + 16 records; 434 titles; 109 abstracts; 35 full texts; 10 excluded (7 off-topic,
  3 conference abstracts); 25 included. Findings (114): 6 qualitative, 15 mixed, 4 quantitative; UK 12,
  Australia 9, Sweden 1, UK+Spain 3. Themes: content 23 studies, delivery 15, structure 11.
- Live odds (199): "During the 2018 World Cup, 69 televised 'live odds' advertisements were shown across
  32 matches by five bookmakers on British television [49]" (= Doc 6); "63 instances ... across 2 months
  (28 matches) of 2016 Premier League" [4] (not in bundle). Whistle-to-whistle ban "before 21:00 in 2019" (201).
- Other included-study figures: social casino ads n = 115, nearly 90% no protective content [36] (183);
  Hing [51] 95% of 223 websites, $200 bonus / $1000 (183, 246-249); [55] 358 refs boxing 4.70/min, 2595 refs
  five football matches 2.75/min, 1% / 3% (186, 201); [54] n = 300, one in seven, one in ten, two-fifths
  (187, 277); tweets 89-202 [34], 33-398 [52], affiliates 594/day [45] (212-214); 20 content studies, 11
  with several coders (302).

## Doc 2 (D07) Norway 2019 survey

- Sample (62-64): 30,000 drawn; 9,248 valid; 32.7% after excluding 1,676 returned invitations and 22
  responses; gamblers n = 5,830. Raffle "200 gift cards, each valued at 500 NOK (approximately 49 €)" (62).
- Demographics (70): mean age 44.27; "48.5% women (n = 2854)"; birthplace counts sum to 5,816.
- CPGI (74): non-problem 4,624 (78.7%), low 814 (13.9%), moderate 286 (4.9%), problem 126 (2.1%) - counts
  sum to 5,850, not 5,830. Dichotomy for regressions: non-problem/low vs moderate/problem (104).
- Tables 1-4 (130-210): exposure and impact means by risk group; regression betas.
- Cites Binde & Romild 2019 (= Doc 7), Syvertsen et al. 2020 interview study (= Doc 10, line 296),
  Newall et al. 2019 (a review, not Doc 6). Comparable surveys: Norway 2013 43.6%, Finland 2016 36% (274).

## Doc 3 (D09) British unplanned-spend surveys

- Emerging adults 16-24, n = 3,549, July/Aug 2019; current gamblers (past year) n = 1,496 (42.1%).
  Sports bettors 18+, wave two n = 3,195 (82.6% retention), Nov 2020; current (past three months)
  n = 2,980 (93.2%) (29, 53-60). "Not sure" n = 114 excluded (66).
- Table 1 (78-107): unweighted and weighted n and % for sex, unplanned-spend frequency, PGSI, awareness,
  direct marketing, following brands. Headline 31.2% / 29.5% weighted (33, 142, 175); 87.0% of problem
  gamblers in both samples (142, 175). PGSI >= 8 problem (128).

## Doc 4 (D06) UK recall study

- 71 family groups, 99 young people 8-16, 71 adults, six South London sites, May-July 2018 (11, 84-86);
  £5 Amazon voucher (99). SPSS: "IBM Statistical Program for Social Sciences (SPSS) 22.0" (143).
- Background (33): TV spots 152,000 (2006) to 1.39 million (2012); "£118.5m on television advertising"
  in 2015, +46% since 2012; Paddy Power 19% per annum (2018). EPL 2018-19: 9 of 20 and 17 of 24
  Championship gambling shirt sponsors (39). 2017-18: nine EPL teams (109).
- Magnet board (111-113): four gambling-sponsored teams, 23 logos incl. "15 other gambling (Fun88,
  Unibet, 32 Red, OPE, Ladbrokes) and non-gambling brands". "respectively" list maps Stoke/West Ham
  opposite to the discussion (360: Bet365-Stoke, Betway-West Ham).
- Tables 1-5 (159-293): brand recall (top five per group), matches, reasons, locations (prompted and
  unprompted). Normalisation 74 of 95 (78%), 59 of 69 (86%) (297, 308).
- Cites a Gambling Commission survey of 2881 11-16-year-olds: 80% TV, 39% weekly+, 70% social media,
  66% other websites (374, 379); boys 2.0% vs girls 1.3% problem gambling (355); Australian 8.30 pm
  study [21] (= Doc 8, 383).

## Doc 5 (D03) systematic review

- Search Feb-Mar 2020, papers Jan 2000-Feb 2020 (7, 59). Flow (90-92): 91 -> 7 duplicates -> 34 excluded
  (29/4/1) -> 50 -> 29 excluded (13/11/5) -> 21. Contradiction (333): "Twenty articles ... among 64".
- Results (100): Europe 2, Canada 1, USA/Australia 1, Australia or NZ 17; methods 7/5/4/4 (sums to 20).
- Tables 2A-2D (111-150), refs 29 and 34-53: 2A sport has 12 rows incl. Pitt et al. (42) 2016 "152
  parent/child dyads (children 8 to 16-years old) conducted on ... sporting sites ... 304 participants"
  (123); Pitt et al. (43) 2016 BMC Public Health, "59 family groups (at least 1 parent and 1 adolescent
  14 to 18-years-old)" (124) = Doc 9; Thomas et al. (45) 2018, 111 basketball fans 11-16 (126) = Doc 8,
  whose row says "The 13 to 16-year-olds used social media ... Instagram (52.3%), YouTube (21.6%), and
  Snapchat (21.6%)" - in Doc 8 these are whole-sample shares (D10 221; 13-16 column: 69.6, 26.8, 32.1).
- Newall et al. (72) live-odds World Cup study (= Doc 6) cited in discussion only (214), not in tables.
- Gainsbury (50) "11.9%" (141) vs "11.2%" (273). Background: Canada 17.1% / 41% (41); 51% online (49).

## Doc 6 (D05) live-odds 2018 World Cup

- 69 adverts, 32 ITV matches (BBC shows no ads, "only half [32] of the 2018 World Cup's 64 matches") (81,
  10, 127). Table 1 (133-147) by bookmaker (Bet365 31, Betfair 4, Coral 4, Ladbrokes 3, William Hill 27):
  timing 22/37/10, average odds, determined-before-end 27, types 13/2/27/3/24, improving 17, flash 11.
- Table note (149): "A further nine of the adverts shown pre-match or at half-time corresponded to events
  relevant to upcoming matches" (plus the 10 post-match ones). Text "17 advertised bets (24.1%)" (153)
  vs 24.6% elsewhere (13, 161). Average odds are inverted mean implied probabilities (91; checks: 7.4).
- 2014 World Cup [7]: three bookmakers, 7.8% home-draw-away, 35.9% correct score, 38.8% goalscorer, 4%
  complex (38-44, 166-169). Guidance in force April 2nd 2018 (32); whistle-to-whistle announced
  December 6th 2018 (191); "80% of all UK gambling marketing spending occurs online [27]" (180); 2018
  survey 14% of 11-16 gambled in previous week, 66% saw TV ads (189); 17% of World Cup ads gambling (26).

## Doc 7 (D08) Swelogs EP4 (2014)

- EP1 2008-09: 15,000 contacted, >8,000 took part; EP4 2014: about 7,000 contacted, 3,559 responded,
  2,163 past-year gamblers (85-87). Table 1 (117-123) NIGA by question; merged 86/12/2% (127).
- Unlicensed: "only 228 individuals (6%)" (6% = of 3,559), 38 of them (17%) (133).
- PGSI 3+: "2.6% (56 individuals)" (137) vs Table 2 (143-149) 36 + 8 + 11 = 55; NoNIGA PGSI 3+ = 32 of
  1,796 (1.8%) vs text "only 1%" (137); SeveralNIGA 8 of 41 = 19.5% (137). Ad spend SEK 3.7bn (2014) vs
  1.3bn (2010) (45); Sweden 2015 ~134,000 moderate-risk/problem gamblers (237).

## Doc 8 (D10) Victorian basketball fans

- n = 111, 11-16, "Interviews were conducted at basketball stadiums between May and July 2018" (11);
  recruited at three community basketball stadiums (110); drink bottle (117); SPSS (145, no version).
- Tables 1-3 (157-246) by gender (66/45) and age (55 aged 11-12, 56 aged 13-16). Regulations: 30 March
  2018, 5:00 am-8:30 pm live sport; August 2018 streaming; G programs 6-8:30 am and 4-7 pm (65-66, 317).
- Background cites GC 0.9% = 31,000 and 1.3% = 45,000 (27); Finland 3.0% + 4.9% (29); Sweden 2.26% vs
  0.81% (30); "over 75%" brand recall (39).

## Doc 9 (D04) Victorian families

- "A total of 59 parents and 61 adolescents were interviewed across 59 family groups" (135); interviews in
  the family home (98); recruited by a market research company (85); $100 grocery voucher (92);
  adolescent males 33 (54.1%) (135). SMI 2011-2015 +160%, "$236 million spent on advertising in 2015"
  (34); AFL-Crown Bet $50m, Sportsbet-NRL $60m (48); William Hill $5m, 1000 sign-ups per day (51).

## Doc 10 (D01) Norwegian interview study

- 12 participants (5 current, 7 lifetime GD; two women), fall 2017, 28-51 min (avg 37), "250 NOK
  (approximately 25 €)" (99); quantifier scale "a few" 1-3, "several" 4-5, "many" 6-8, "most" 9-11,
  "all" 12 (130); seven got special offers (170); 6,000 NOK offer (229); 100,000 NOK ~ 10,000 € (160).

## Shared ground (navigation only)

- Review -> primary: Doc 1 [49] = Doc 6; Doc 5 (45) = Doc 8, (43) = Doc 9, (72) = Doc 6 (not included);
  Doc 4 [21] = Doc 8; Doc 2 cites Doc 7 and Doc 10; Doc 3 cites Binde & Romild 2019 (Doc 7).
- Same population/period: Doc 4 and Doc 8 both May-July 2018 youth recall; Doc 2 and Doc 10 Norway;
  Doc 8 and Doc 9 Victoria; Doc 1 and Doc 6 2018 World Cup live odds.
- Same instrument: PGSI/CPGI cut-offs identical in Docs 2, 3, 7 (8+ problem; 3+ moderate-or-problem).
- Spend series: Australia Doc 1 ($273m 2018, marketing and promotion) vs Doc 9 ($236m 2015, SMI
  advertising) - different measures; UK Doc 1 (£1.5bn 2018) with Doc 6 (80% online) and Doc 4 (TV 2015).
- Currency: Doc 2 500 NOK ~ 49 €; Doc 10 250 NOK ~ 25 €, 100,000 NOK ~ 10,000 €.
