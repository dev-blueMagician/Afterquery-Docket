# aq-02147 - cross-document hooks

Find facts that combine into a world answer before drafting wording. Record sources/locations,
input quantities and units/periods, the relationship, a possible ask and one or two selected levers.
Explore forecast/actual, proposal/final dates, changed/conflicting tables, amendments, hedge scope,
mentions/actions, entity/edition joins, ordered/late items, exclusions and ordinary cross-document
calculations. Find more viable hooks than questions requested without inventing a quota.

Target (user, 2026-10-08): no Easy slot, "target medium and high". Page: Hard 0/2 · Medium 0/3 ·
Easy 0/1, 9 submissions, 0 of 10 quick tests. Local ids: D04 = Doc 1, D02 = Doc 2, D05 = Doc 3,
D01 = Doc 4, D03 = Doc 5 (Doc N below is the page's number).

Design constraint found while mapping: every statutory parameter (LEL £118/£120/£123, flat SSP
£94.25/£116.75/£118.75, the 80% decision) is duplicated across documents and is recallable by a
strong model, so a document whose only contribution is one of them is at risk in the platform's
Document check. Hooks below are ranked by whether each necessary document adds a bundle-specific,
non-recallable input.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | Doc 5 L151 employees' median 90% (only source); Doc 3 L143 break-even definition (£123, five days, vs current entitlement), L149-151 Table 1 (2/3/4 weeks), L105 three waiting days, flat £116.75; Doc 4 L409-422 same profile as case study 1 | Break-even week at the employees' median rate: £110.70 a week vs £116.75 after waiting days, crossing in week 12 | Calculate across documents; Scatter the pieces | Extending Table 1's 2/3/4 pattern gives 5; April 2025 £118.75 gives 9; employers' 50% gives 2; 80% gives 4; no waiting days gives 1 | Profile (LEL earner, five days) is guessable without Docs 3/4, so group them as "or" alternatives | i01, promoted q01; RETIRED 2026-10-08: Run 1 "A marked document may not be needed" (without Doc 3 the high model used Doc 4's identical case study 1) and Low 2/5 (Easy band); feedback-index F1/F2 |
| h2 | Doc 5 L105 employers' median 50% (only source); Doc 4 L428-444 case study 2, £175 five days (only source), old cumulative column | Week the £175 employee is first worse off overall at employers' median: £87.50 a week, week 3 under either flat rate | Calculate across documents; Scatter the pieces | Doc 4's "always notionally better off under a rate at 80%" gives never; employees' 90% also never (flat rate); 60% gives 6 | Same family as h1; "3 weeks" is also printed as Table 1's 70% row (advisory coincidence; the break-even depends only on weekly SSP, 87.50 vs 86.10) | i02, promoted q02 |
| h9 | Doc 2 L853-L859 Table 3 median employer saving per retained employee £8,000 (only median; L808 prose £5,000-£11,000); Doc 3 L167-L171 Table 2 current £0.65bn, 80% £1.07bn (only current figure); Doc 3 L117 links the reform to retention (£30,614 average) | Retentions a year that offset an 80% rate's rise over current SSP costs: 0.42bn / 8,000 = 52,500 | Scatter the pieces; Calculate across documents (picking the right measure) | Doc 3's £30,614 gives 13,719; the £1.07bn total gives 133,750; component medians 84,000 / 135,484; Doc 5's £30m gap 3,750 | Two estimates from different years (stated as an assumption: "at the median saving"); Table 3 rounded (components sum to £8,100) | i03, promoted q03; CLOSED 2026-10-08: quick test "Too easy — solver got it" (feedback-index F3) |
| h3 | Doc 3 L163 waiting-period-only cost £1.02bn, Table 2 current £0.65bn and 80% £1.07bn; Doc 5 L184 chosen 80% | Waiting-period share of the cost rise at the chosen rate: 0.37/0.42 = 88.1% (decoys 95.3%, 94.9% at 60%, 86.7% per employee) | Calculate across documents | as listed | Doc 5's only input (80%) is recallable or inferable from Docs 3/4, so its necessity fails | parked |
| h4 | Doc 1 L606 2019 employer SSP cost £1.5bn; Doc 3 Table 2 current £0.65bn | Fall in the estimate: 56.7% | Rounding and sign | £1.07bn reform cost gives 28.7% | Two lookups and one operation | parked, Easy-leaning |
| h5 | Doc 1 L213 / Doc 2 L166 12.7m LTHC incl. 7.6m disabled; Doc 3 L115 15.9m incl. 10.5m | Non-disabled LTHC change 5.1m to 5.4m: 5.9% | Calculate across documents (carve-out) | Total 25.2%, disabled 38.2% | Docs 1 and 2 duplicate the 2019 pair; simple | parked, Easy-leaning |
| h6 | Doc 2 L417 LEL £120 (2021); Doc 5 L176 LEL frozen 2021, 2023, 2024; Doc 3 L107 £123 | LEL last rose in 2022, by £3 | Temporal alignment | £118 gives £5 | LEL history is recallable closed-book | rejected |
| h7 | Doc 2 L190 15 Jul-7 Oct 2019; Doc 5 L51 21 Oct-4 Dec 2024, "six weeks" | Duration difference 40 days (prose 42) | Exact vs rounded prose | 42 | Date gap, likely too easy; dates possibly recalled | rejected |
| h8 | Doc 1 L734 + fn 93 (80% = SSP/LEL ratio); Docs 3/4 £116.75/£123 | Same rule in 2024 gives 94.9% (prose 95%) | Exact vs rounded prose | 95.0 | Doc 4 alone holds the inputs; Doc 5 L175-176 implies the rationale | rejected |

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.
