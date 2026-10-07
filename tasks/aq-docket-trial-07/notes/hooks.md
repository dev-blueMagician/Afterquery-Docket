# aq-docket-trial-07 - cross-document hooks

Target: medium (user, 2026-10-06). Seven unrelated 2021 BLS Monthly Labor Review articles; no article
cites another, no shared states/entities beyond BLS programs. Cross-document links are shared calendar
periods (D03 quarterly 1992Q3-2020Q1; D04 monthly rail 1980-2020; D05 monthly Midwest 1990-2019),
shared BLS programs (QCEW/BED in D03 and D01 Table 3; CES in D04/D05; OEWS in D06) and comparable
measures. Per memory, the Medium mechanism in such bundles must come from one article's internals
(a same-label wrong value ruled out only by close reading) with an indispensable partner input elsewhere.

Caller inventory (preliminary, before maps; locations are text/Dnn.txt line numbers):

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D05 L1467 "bottomed out in February 2010 at 3.5 million"; D05 Chart 1 data: Dec 2009 3,528.4 (series minimum), Nov 2009/Jan 2010 3,528.7, Feb 2010 3,530.2; D04 Chart 1 rail Dec 2009 178.7, Feb 2010 178.2 | rail value/change keyed to Midwest manufacturing's lowest month | exact table vs prose; scatter | prose month Feb 2010 vs data min Dec 2009 | prose contradicts its own chart: a "one defensible answer" risk; near-ties (0.3K) | investigate, fairness risk |
| h2 | D05 L1467 "a 17.1-percent increase since the trough ... February 2010" = rounded 4.1/3.5; data Feb 2010 3,530.2 -> Dec 2019 4,083.7 = +15.68% (Dec 2009 base +15.74%); D04 rail Feb 2010 178.2 -> Dec 2019 163.4 = -8.31% | growth-rate comparison over a shared window | exact table vs rounded prose; calculate across docs | stated 17.1% vs computed 15.7% | needs "computed from monthly levels" wording or the stated 17.1% is defensible (trial-04 q03 risk) | investigate |
| h3 | D04 L3166 STB "31,000 jobs lost", T&E "46 percent", MoE "more than a quarter"; Chart 4 exact Nov 2018 148,981 -> Dec 2020 117,770 = 31,211; T&E 14,211 (45.5%); CES L11 "40,000"; Chart 1 184.1 -> 144.5 | Class I occupational losses vs CES industry losses | exact table vs rounded prose; who belongs where (CES vs STB) | 40,000 CES decoy; 31,000/46% rounded route | single-document; no natural partner yet | partner needed |
| h4 | D03 L1829 Q1 2020 total "663,000" (published BED, fn 9) vs wage-class components 40 + 47 + 587 = 674 | share of Q1 2020 net losses by class | component sum vs stated total | 663 vs 674 denominator | must pin the denominator; single-document | partner needed |
| h5 | D07 L69 prose: nine countries 35-40% incl. "five Central-Eastern European countries (Estonia, Cyprus, ...)", "one Southern European country (Portugal)"; region list L41 puts Cyprus in Southern Europe; Chart 1 adds Germany 35.3 (Continental) in range; prose Greece "56" vs chart 58.1 | country membership by region and band | who belongs where; exact table vs prose | prose miscounts (Cyprus, Germany) | single-document; prose/chart conflicts may read as ambiguity | partner needed |
| h6 | D05 L1629 prose small-state gains (Iowa +4,300 etc.) vs Chart 4 annual averages (+7.0K, +2.5K, +10.9K, +11.5K) | state gains | prose vs table basis | different basis (monthly vs annual average) | ambiguous basis | low priority |
| h7 | D01 Table 3 (QCEW tribal establishments, Q4 2017: 334.5K employment Dec 2017; casinos 168.0K) + Meister 296,000 (2020, "76.2 percent higher"); D03 L17 QCEW Q1 2020 147.0 million employees, 10.4 million establishments; D03 L19 BED uses third-month employment | QCEW-based comparisons | calculate across docs | none yet | period mismatch (2017 vs 2020) | investigate |

## Round 1, author B (question-author, non-time-series relationships, 2026-10-06): none viable

Checked 25 links outside D03/D04/D05 calendar alignment; returned no sketches. Failure classes: no
partner data to apply a rule to (D02 OMB 80% / DOD 8% / DOS 3% thresholds; D03 wage cutoffs; D07
schedule definition and regions; D01 domains; D06 categories); partner supplied by general knowledge
(location quotient; establishment = worksite; QCEW benchmarks CES; OEWS semiannual; NBER months; OMB
directive dates); one-sentence lookups or per-row keyword tags (BEA accounts fed by CE and QCEW;
intercity train fare row); manufactured links (D07 "2010 = recession year" applied to US series; D06
panel span vs D02 "prior 3 years"; D06 Nov 2017/Nov 2018 dates into rail); period/universe mismatch
(D01 Table 3 Q4 2017 vs D03 QCEW Q1 2020, rounded 2.3K establishments); rule 10 (Dey/Loewenstein
cited in D06 and D07). All same-label traps (D04 CES/STB, D01 168.0K/296,000, D07 Cyprus, D05 Chart 4
vs prose gains, D06 Table 2 subsets, D03 47 vs -37) are single-document or document errors.
Handoffs to the time-series family: H-A D04 flood note (March-April 2019, "probably") into D05 levels
(Feb 4,128.8, Mar 4,127.3, Apr 4,121.5; span must be pinned; plainly dated bridge, predicted Too easy);
H-B D03 Q1 2020 -663K vs rail Dec 2019-Mar 2020 -5.1K (0.769%; class sums 664/674 give 0.768/0.757;
quarter-average route 0.849; predicted Easy at best).

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.
