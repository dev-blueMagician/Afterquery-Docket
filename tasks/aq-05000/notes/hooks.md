# aq-05000 - cross-document hooks

Target: hard (only Hard open on the page; the user named Medium and High, the page says "Medium closed").
The check is expected to start at the High level (two solvers, up to 3 tries each; passes only if both
miss at least once and not every attempt misses). Audit every hook against the high model: a step is
pointed when a lookup of any word, year, name, measure or condition in the question reaches it; a sweep
of a named property and an inference the scope phrase invites are pointed too.

No earlier captures: new bundle (no document file name, title or distinctive phrase found in 10.6,
10.7, 10.8 or docket-capture, 2026-10-14).

Structural finding: the seven reports are mostly independent. Real cross-document links are few:
Doc 6 -> Doc 5 (Doc 5 cites and extends Doc 6; BTOS and RPS in both), Doc 2 / Doc 1 (both ONS, both
BICS but different waves and AI questions), Doc 3 / Doc 4 (both DSIT-commissioned 2025, same five AI
types, no shared figures), Doc 6 / Doc 7 (the Turing UK public-sector survey: numbers in Doc 6,
citation only in Doc 7). No forecast/actual pair on one population, no amendment, no restated table.

| Hook | Source inputs and locations | World fact / possible ask | Lever(s) | Decoy / counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | Doc 6 L98 RPS Aug-24 28%; Doc 5 L151 Any 40.7, YoY 9.7 | RPS work-GenAI rise Aug 2024 -> Nov 2025 = 12.7 pp; or first quarter Aug -> Nov 2024 = 31.0 - 28 = 3.0 pp | Calculate across documents; Same series | "about 41" prose gives 13; 9.7 (YoY) taken for the whole rise | Doc 6's label "Share of Working Age Adults" vs Doc 5 "of the workforce" (base reading); 28% (Aug 2024) is a widely reported headline, recall risk for Doc 6's necessity | screened as i02 (growth form): 3/3 right, rejected |
| h2 | Doc 5 L77-86 SBU employment-weighted 78 / 54 (Table 1, unit "Firms"); fn 9 L268 equal-weighted 69.4 / 46.4; Doc 6 L92 + fn 2 L157 BTOS 20% employment-weighted vs 8.8% firm-weighted six-month | share of firms (not of the labour force) is a footnote figure in both notes | Exact table vs footnote; Unit or basis | table values 78 / 54 / 20 taken as shares of firms | any ratio across the two notes mixes periods (Sep 2023 - Feb 2024 vs Nov 2025) and surveys: no document connects them; within Doc 5 alone it is single-document | screened as i01 (Dallas vs SBU firm shares) and i03 (weighting alone, two footnotes): 3/3 right each, rejected |
| h3 | Doc 5 L30, L65 legacy BTOS +68% (3.9 pp) year to Sep 2025, fn 2 4-period moving average; Doc 6 fn 5 L163 3.7% Feb 2024 -> 6.6% Sep 2024 | legacy-question level Sep 2025 = 3.9 / 0.68 + 3.9 = 9.6% | Figure that must be computed | 18% (new question) | Doc 6's Sep 2024 6.6% + 3.9 = 10.5% is a second route (point vs moving average): two defensible answers | rejected (one-answer failure) |
| h4 | Doc 3 L411 B3 "currently using it (including piloting)"; Doc 2 L200-204 DCMS 2022: 15% adopted, ~2% piloting | on DSIT's convention 2022 = 17%, so 2025's 16% is a fall of 1 point, not a rise | Definition applied to instances; sign flip | naive 16 - 15 = +1 | "around 2%"; documents never say the 15% and 2% are disjoint; populations differ (all businesses vs >= 5 employees private sector) | rejected (not one defensible answer) |
| h5 | Doc 7 L531/L1085 Bright et al. (2025) cited on adoption trajectories; Doc 6 L105 Bright et al. (2024), 938 people, Nov-23, 22%; Doc 7 L331 JRC early-2024 30% / 44% | public-sector GenAI shares: 30 - 22 = 8 points | Who belongs where; Calculate across documents | 44% (planned) or 74% | Doc 7 is not needed (Doc 6 names the UK public-sector survey directly); measures differ (encountered vs using); Turing 22% widely reported | rejected (necessity) |
| h6 | Doc 3 L168, L2795 size floor 5 employees; Doc 5 L163 "about 57 percent of firms have fewer than five employees" | share of US firms inside the DSIT size floor = 43% | Definition applied to instances | MES floor 10 (Doc 1) is not computable from Doc 5 | contrived (a UK survey's scope applied to US firms); every step pointed | rejected |
| h7 | Doc 5 L124-127, fn 6-7: BTOS new-series and RPS rates by industry; manufacturing only as growth (159% / 7.5 pp; 58% / 14.5 pp) | industry with the largest worker-to-firm ratio (wholesale 48 / 13) | Aggregation; Figure that must be computed | manufacturing derived 39.5 / 12.2 = 3.2 | single document | rejected (one document) |
| h8 | Doc 6 L96 Chamber row: "AI Uptake 40%", note says "use generative AI"; L48 text says only Dallas asks about GenAI | which firm surveys measured GenAI | Mentions vs does | Dallas only (text) | the document contradicts itself; single document | rejected |
| h9 | Doc 1 L96 text "83% ... specialised equipment" vs Table 1 L101 43 | AI firms also using specialised equipment | Exact table vs prose | 83 | internal error, single document | rejected |
| h10 | Doc 2 L298 BICS 9,399 / 39,338 = 23.9%; L292 OPN 41%; Doc 3 L2775 9%; Doc 4 L186 3%; Doc 5 L205-207 BTOS ~20,000 of 200,000 | rank surveys by response rate | Ordered answers | - | BTOS ~10% vs DSIT 9% too close ("about 20,000"); without BTOS every step is a lookup | rejected |
| h11 | Doc 1 L359 BICS AI waves 92, 98, 105, 111, 117; Doc 2 L180, L298 wave 80 (3-16 April 2023), "fortnightly" | waves asking about AI; wave dates by cadence | Bury one list item late | - | neither list claims completeness; strict fortnightly dating puts wave 92 in September 2023, before the MES period Doc 1 matches it to | rejected |
| h12 | Doc 1 L72 MES rates "by the share of employment" (dataset); Doc 6 L52, L92 BTOS 20% employment-weighted; Doc 5 L77, L84 SBU 78 / 54; decoys Doc 6 L60-62, Doc 2 L184, Doc 3 L206, Doc 2 L294 | business surveys reporting employment-weighted AI adoption: BTOS, SBU, MES (author A) | Mentions vs does; member stated only in reworded form | Doc 6's "approximately employment-weighted" surveys; BICS "weighted by count"; DSIT size-and-sector weights | open universe unless named; MES figures only in the dataset; a sweep for "employment" reaches Doc 1 L72 | screened as i04: 3/3 right, rejected |
