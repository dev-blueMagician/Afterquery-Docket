# aq-01278 - cross-document hooks

Find facts that combine into a world answer before drafting wording. Record sources/locations,
input quantities and units/periods, the relationship, a possible ask and one or two selected levers.
Explore forecast/actual, proposal/final dates, changed/conflicting tables, amendments, hedge scope,
mentions/actions, entity/edition joins, ordered/late items, exclusions and ordinary cross-document
calculations. Find more viable hooks than questions requested without inventing a quota.

Target: medium. Local ids (Doc N): D01 Allstate Q1 (5), D02 Allstate Q2 (10), D03 Allstate Q1
supplement (6), D04 Chubb Q1 (4), D05 Chubb Q2 (9), D06 Progressive March (1), D07 Progressive June
(7), D08 Travelers Q1 (2), D09 Travelers Q2 (8), D10 Travelers Q1 supplement (3).

Structural finding (caller, 2026-10-06): every Q2 edition prints six-month or year-to-date columns
(Travelers D09 also twelve months ended June 30), so a Q1 edition is individually necessary only for
March 31 as-of values, Q1-only prose, Progressive's March month, and the Q1 supplements' 2025
quarterly detail (D03, D10). Forecasts are almost absent (Travelers' full-year expense ratio
"approximately 28.5%", unchanged in D09), so the measured aq-00964 outlook-edition trap has no home.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D07 June monthly supplemental, Property column footnote 1: "favorable 11.7 point impact related to an actuarial methodology process change" (one-time, property IBNR); D07 YTD and D06 YTD property NPE/ratios | property or companywide ratio for Q2/H1 excluding the one-time change | footnote that changes what a figure covers; calculate across documents | printed H1 78.1 / June 65.6 | one-decimal ratios: caller range check gives Q2 property 81.4-82.2 (not robust even at whole percent); H1 is one-document | investigate (precision) |
| h2 | D08/D09 Canadian divestiture: prior-year NPW included 223 (Q1: BI 67, B&S 10, PI 146) and 273 (Q2: BI 79, B&S 16, PI 178); International rows by segment; D10 2025 quarterly International rows | ex-Canada change of an International row or combined International NPW | carve-out; printed segment-level ex-sale % as answer-shaped decoy | printed "(8)%" International, "5%" segment ex-sale | D09 alone holds Q2 and H1 (Q1 = H1 - Q2): two-document necessity needs D10's 2025 quarters | investigate |
| h3 | D08 capacity $5.215B (Mar 31); D09 capacity $3.915B (Jun 30), Q2 4.3M shares, $1.311B, no authorization/other split; D10 splits by quarter | Q2 repurchases outside the authorization | footnoted-remainder style | $185M Q1 "other" | assumes no new authorization in Q2 (not stated): second defensible answer | drop (one-answer risk) |
| h4 | D02: Q2 underlying auto 87.6 "benefited from 2.4 points of favorable development on claims reported in the first quarter of 2026"; D01/D03 Q1 89.5 | Q1 re-estimate / Q2 ex-development | footnote-like qualifier | 89.5-2.4 = 87.1 equals the base-converted 87.08 at one decimal | invented concept "re-estimated Q1"; lever does not change the answer | drop |
| h5 | D03 BVPS denominator "common shares outstanding and dilutive potential common shares"; D02 BVPS 123.38, shares 253.5 | same-label definition differences across companies | entity/definition alignment | printed BVPS | "using X's definition" signposts | low priority |
| h6 | D10 quarterly series 1Q25-1Q26 (PYD by segment incl. 3Q25 asbestos 277 unfavorable; repurchases; PIF; reserve roll-forward); D09 Q2/H1/TTM | twelve-month or Q3-Q2 builds | calculate across documents | printed H1 or TTM totals | D09 prints TTM net/core income and ROE: check each quantity for a printed TTM figure | investigate |
| h7 | Allstate P-L quarterly underwriting income/premiums earned (D03 3Q25, 4Q25; D02 Q2, H1) | P-L combined ratio for twelve months ended June 30, 2026 (100 - UW income/PE) | stated method applied to an unreported period | H1 84.3 | simple average of quarterly ratios gives the same one-decimal value (lever weak) | investigate |
| h8 | D06/D07 policies in force by product (Mar 31, Jun 30) with year-over-year % columns | product that added most policies during Q2 | ordered/compare | printed YoY % (direct auto highest) | wording selects the right figure; lookup path | low priority |
| h9 | Chubb D04/D05: Global P&C (ex-Agriculture) printed beside P&C; repurchases Q1 1.14B at 325.06, Q2 979M at 327.18, H1 2.12B at 326.03 | carve-outs and share counts | n/a | n/a | carve-outs printed; share counts are one-operation lookups | low priority |

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.
