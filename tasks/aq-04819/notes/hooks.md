# aq-04819 - cross-document hooks

Target: medium in files (user 2026-10-14: no Easy slot, "target medium and high"; page: Hard 0/5 ·
Medium 0/1 · Easy 0/0). Medium has one slot and runs on 2026-10-14 started at Medium (aq-04045) or
High (four other sets), so every hook is audited against the medium AND the high solver.
Page Doc numbers are used throughout (local ids in doc-map.md).

Structural finding: the eight primary studies are independent (different countries, samples, years);
none reuses another's data. Real cross-document links are (a) the two reviews summarising bundle
studies (Doc 5 rows (43) = Doc 9 and (45) = Doc 8; Doc 1 [49] = Doc 6), (b) papers citing each other
(Doc 2 -> Docs 7, 10; Doc 4 -> Doc 8), (c) shared instruments (PGSI/CPGI cut-offs in Docs 2, 3, 7) and
(d) background figures quoted by several papers (spend, Gambling Commission youth surveys). Any join of
type (c) or (d) is two lookups plus one operation, every step pointed at by the question's words.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | Doc 5 Table 2A rows (42) "152 parent/child dyads ... sporting sites" and (45) "basketball fans" n = 111; Doc 8 abstract/methods: interviews at basketball stadiums | children and teenagers surveyed at sports venues in the review's included studies = 152 + 111 = 263 | member qualified only by a second document (total before list) | 152 (review only), 304/415 (parents counted), 111 (sites read as websites) | "sporting sites" could be read as websites; 152 printed past char 20,000 in Doc 5 | sketch i01; quick test failed 2026-10-14 |
| h2 | Doc 5 rows (42) 152 children, (43) "59 family groups (at least 1 parent and 1 adolescent)"; Doc 9 results "59 parents and 61 adolescents" | young people in the review's parent-and-child studies = 152 + 61 = 213 | hidden count in the primary's results | 211 (59 assumed), 424/422 (all participants) | Doc 9's 61 sits near char 19,300 | sketch i02 -> q01; Run 1 Too easy, High 3/3 (2026-10-14); retired |
| h3 | Doc 5 row (45) attributes Instagram 52.3%, YouTube 21.6%, Snapchat 21.6% to 13-16-year-olds; Doc 8 Table 2: those are whole-sample shares, 13-16 = 69.6, 26.8, 32.1 | reconcile the review with the study (gap 17.3 pp on Instagram) | reconcile documents that disagree | review's figure taken as true | any question needing only the 13-16 figure is a one-document answer (Doc 8); naming the disagreement points at both cells | hold (two lookups once named) |
| h4 | Doc 1 £1.5bn UK marketing 2018; Doc 6 "80% ... occurs online" | UK spend outside online channels = £300m | calculate across documents | £1.2bn (online), Doc 4 TV £118.5m (2015) | 80% is "now" (2019 paper), year not tied to 2018; headline figures recallable closed-book | weak: pointed, recallable |
| h5 | Doc 1 Australia $273m 2018 (marketing and promotion, +33%/yr since 2011); Doc 9 $236m 2015 (SMI advertising, +160% since 2011) | 2015-2018 growth | - | - | two different measures; implied 2011 bases disagree ($37m vs $91m) | rejected (no one answer) |
| h6 | Doc 2 5,830 of 9,248; Doc 7 2,163 of 3,559 | share of respondents who gambled in the past year, Norway vs Sweden (63.0 vs 60.8, gap 2.3 pp) | calculate across documents | 32.7% response rate; 30,000 / ~7,000 bases | every step pointed | weak |
| h7 | Doc 7 SEK 1.3bn (2010) -> 3.7bn (2014); Doc 9 +160% 2011-2015 | compound annual growth 29.9% vs 27.0% | state the method | simple growth 46%/40%; Doc 1's 33% | convention must be named; pointed | weak |
| h8 | Doc 2 500 NOK ~ 49 €; Doc 10 250 NOK ~ 25 €, 100,000 NOK ~ 10,000 € | conversions | unit normalisation | the other paper's rate | answer depends on which rate unless named; naming points | rejected |
| h9 | Doc 6 bookmakers (Table 1); Doc 4 top-five brand recall (Table 2) | mentions of live-odds bookmakers by young people = 30 + 16 + 13 + 4 = 63 | match then exclude | Betway 18 (81) | Betfair's count unknown outside top five; pointed | weak |
| h10 | Doc 6 table note: nine more pre-match/half-time adverts were for upcoming matches (69 - 10 - 9 = 50) | adverts about the match on screen | table note adjusts headline | 59 | single document; Doc 1 adds nothing unique | rejected (one document) |
| h11 | Doc 6 average odds are inverted mean implied probabilities (overall 7.4 from bookmaker rows; naive mean 7.8) | combined average odds for a subset | method inference | naive weighted mean | single document | rejected (one document) |
| h12 | Doc 7 Table 2 PGSI 3+ = 55 vs text 56; NoNIGA 3+ = 32/1,796 = 1.8% vs text "1%" | - | exact table vs prose | - | single document; two defensible bases | rejected |
| h13 | Doc 3 weighted vs unweighted PGSI shares (moderate+problem: SB 17.19 vs EA 17.09 weighted; 14.1 vs 17.0 unweighted) | ranking of samples with Docs 2, 7 | exact table vs rounded | printed 17.1 = 17.1 tie | weighting must be named; the tie prompts the check | weak |
| h14 | Doc 2 names three representative predecessors (Binde & Romild 2019, Hanss 2015, Salonen 2018) with rates for two; Doc 7 3,559 of about 7,000 | highest response rate | hidden member | Norway 2013 43.6% | "about 7,000", panel wave; link to Doc 7 needs authorship inference | rejected |
| h15 | Doc 6 dates (2 Apr 2018 guidance; 6 Dec 2018 announcement); Doc 8 (30 Mar 2018 rules; Aug 2018 streaming) | order or day counts | ordered answers / dates | 30 Mar vs 2 Apr | date counts measured too easy on many sets | weak |

Delete-and-guess is recorded per sketch in notes/sketches/. The map is navigation; quotes come from
text/Dnn.txt.
