# aq-01650 - cross-document hooks (round 2, restarted 2026-10-08 under gate v3)

Round 1 (q01 and its sketches) is archived in `archive/round1-q01/`; its complete-case/imputed-sample
family (Doc 5 Table 2 vs the decomposition means) is not reused. Ids: local Dnn (task page Doc N).
Sources and extraction re-verified against `notes/intake.json` and `text/manifest.json` (all seven
hashes match, no gaps), so `notes/doc-map.md` is reused as navigation.

The bundle's only same-population pair is the Osaka University Preference Parameters Study (PPS)
2010/2011 waves: D04 (Doc 3) check-ups, ages 40-64, N 2,208; D05 (Doc 4) cancer screenings, ages 40+,
N 2,693. Both print the same cross-tab layout by sex, degree and unemployment (Table 4) and by smoking,
drinking and gambling (Table 5), with counts. The CHFS trio (D02, D03, D06) and D01/D07 share
measures and citations but no joinable counts.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D04 T4 L209-216 (check-up "1" row: Female 418, Total 701); D05 T4 L84-97 (zero row: Female 723, Total 1311; Total row: Female 1347, Total 2693) | Women's share of 40-64 non-mandatory check-up takers minus their share of 40+ people with a counted cancer examination: 59.63 - 45.15 = 14.48 pp | Calculate across documents; Scatter the pieces | look-alike measure: within-sex column percentages (36.99%, 53.67%/46.33%) give -9.3 | dependent-variable wording differs inside D04 (L77 vs L79); describe the measured variable | sketch i05 |
| h2 | D04 T4 L212-216 (six group rates; unemployed 21 of 52 = 40.38% highest); D05 T4 unemployed column L87-97 (35/8/7/3/2 of 55) | Mean counted cancer examinations of the group with the highest check-up rate: 39/55 = 0.71 | Scatter the pieces; Calculate across documents | wrong group: women 36.99% (prose L243, 1% level) gives 1.01; overall mean 1.1508 | bridge visible in D04 prose (L243 prints 40.38%) and discussion (L403 "unexpected finding") | sketch i06 |
| h3 | D04 T4 (no check-up: Below 1096 of 1507); D05 T4 (zero: Below 1043 of 1311); D05 L78 prose "Of those who did not undergo cancer screening, more than half (51.43%) obtained lower than university qualifications" | Degree share among non-participants in each study: 72.73% vs 79.56% | Exact table vs prose | D05's own sentence misreads its column share (1043/2028) | the bundle states the decoy as the answer for the exact ask; no wording can exclude it without pointing at the counts | hold |
| h4 | D04 T2 smoker 0.2337, drinker 0.4864, gambler 0.1060 (L159-188); D05 prose "just under 22%", "almost 48%", "almost 10%" (L71-72) and T5 totals 583/1283/264 of 2693 (L122) | Prevalence gap 40-64 vs 40+: smokers 1.72 pp (prose route 1.4) | Exact table vs rounded prose | rounded prose route changes the one-decimal answer | a same-window rounded statement drew the form's "too vague" block before (aq-01321); naming the counts disarms it | hold |
| h5 | D03 T1 L98-108 (2015 CHFS: 2 correct 31.55%, 3 correct 10.77%, mean 1.414); D05 T6 L136-147 (Score >= 0.5: 1805 of 2693); D04 T2 literacy 0.6185 | Share with at least two of three questions right, Osaka 40+ vs CHFS 2015: 67.03 - 42.32 = 24.71 pp | Unit or basis | average-score threshold read as a share | round 1 family (archived i01); D04 0.62 prose sits beside its exact table | hold |
| h6 | D04 L72 (2,208 = 44.75% of 4,934); D05 L47 (2693 = 54.58% of 4943) | Reconciled 2011-wave total 4,934 | Reconcile documents that disagree | 4943 typo | answer printed in D04; D05 alone recovers 4,934 from its own share | reject |
| h7 | D01 T2 L231 "Household income (10,000 JPY)" 515.293; D04 T2 income 6,888,813 JPY | Income gap in yen | Unit normalization | unit printed in the row label (tied); income definitions differ (D01 L172 vs D04 L102) | arbitrary comparison | reject |
| h8 | D02 L310 (low = none right or unable, high = all right); D03 T1 | Intermediate share 46.01 + 31.55 = 77.56% | Definition applied to an instance | none: a plain partition | direct sum | reject |
| h9 | D04 T2 health status 0.0149 vs prose "approximately 14.9%" (L157); D05 prose "only 2%" (L74) | Poor-health gap | Exact table vs prose | D04 prose is a tenfold error | D05's 2% is rounded, so no supported precision | reject |

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.
