# Question-author A, sketch round 1 (raw return, 2026-10-06)

Fresh question-author agent (Claude Code, claude-opus-5-5), target medium, given the caller's
notes/hooks.md and the measured calibration; no files written by the agent. Origin of sketches:
claude. Return copied verbatim from the task notification.

---

I evaluated the six hooks and found two new designs with stronger mechanisms than plain partial-year arithmetic, giving four ranked sketches (a01–a04). origin: claude. None of these is validated yet. All facts come from `D:\Dev\Docket\tasks\aq-01430\text\D01.txt`–`D08.txt`; I read every document in full and checked the capture overview (lines 32–86). Every quote below matched its line exactly, and all arithmetic was rerun in python.

## Hook verdicts

- **h1: worth a write-up (becomes a02).** Its wrong figure carries the year label ("up from 15 in 2024", larger markets only). The correct 2024 count (42) sits in a sentence that says "now" with no year. No later document restates the all-country count, and the overview doesn't show it.
- **h2: not worth a write-up (+57 TWh confirmed).** It is plain full-year minus first-half arithmetic, the shape measured Too easy before. Asking for July–December rules out every decoy, and China's hydro recovery in late 2023 is roughly public knowledge.
- **h3: Easy fallback only (+17 TWh confirmed).** Same document pair and mechanism as h2. It is slightly better because D06 L1008 blames the 2023 fall on "a milder summer", yet July–December demand rose. Never use it alongside h2.
- **h4: valid but weak (40.6%; a04, ranked last).** Standard Q1–Q3-to-Q4 arithmetic, and the global inputs (498, 636) appear in the overview.
- **h6: not recommended.** D03 L180 never says whether 380 and 232 GW are DC or AC, while D07 L237 gives 647 as GW(DC). The question would have to assert a basis the documents don't confirm.
- **h15: optional, Easy-leaning.** Ranking is China 168, US 41, India 36, EU 23 (the full-year and first-half orders put the EU above India). It shares a03's mechanism and D03/D07 path.
- **h7 (not asked):** the two-route problem is confirmed (+13 from the printed changes, +8 using D06's 1,865). The G7 "26%/37%" rounding variants also give different answers at one or two decimals. Avoid.

## Sketches (ranked)

### a01 — EU coal, 2019 to 2021
- **difficulty_target:** medium
- **question (24 words):** "How much did coal-fired electricity generation in the European Union change from 2019 to 2021? Give the answer in TWh with its sign."
- **answer:** −34 TWh
- **facts:**
  - D06 L1076 "Over the last five years, coal generation has fallen by 182 TWh (-40%)". The next sentence fixes the window: "was 139 TWh (-24%) lower in 2024 than it was in 2019".
  - D07 L1036 "Coal generation accounted for almost two-thirds of the EU’s fossil power decline (-162 TWh) since 2021."
  - D07 L1020 "Coal generation declined by 5% (-14 TWh) in 2025".
- **documents:** D06, D07
- **dependency:** Only D06 anchors 2019 and only D07 anchors 2021.
  - No other source has EU coal TWh for these years: D04 L63 gives a percentage, D05 L103 only the sign, D02 L345 a first half, D06 L1068 only 2024.
  - Removal: without either document the gap cannot be closed, and the rounded percentages don't land on −34.
- **selected_levers:** Calculate across documents; Same series, right edition (the windows end in 2024 and 2025 respectively).
- **lever_checks:**
  - Ignoring the 2025 step gives −20; getting the 2025 sign wrong gives −6.
  - The printed window figures −182 and −162, and the 2021–2024 change of −148, are all answer-shaped decoys.
- **arithmetic_check:** −182 − (−162 − (−14)) = −34. Second route via levels: 2019 = 455, 2024 = 273, 2021 = 421, so −34 (−7.5%).
- **shortcut_search:** Searched EU/Europe + coal, "2019", "since 2021" and "last five years" across all eight documents, plus the overview. No passage prints the 2019–2021 change.
- **tags:** Cross-document join, Temporal alignment, Aggregation
- **completeness:** Full text read. The "Loading data..." charts are equally absent for solvers.
- **portfolio:** Overlapping-window family. An alternative in the same family is EU fossil 2021–2023 = −257 − 18 + 75 = −200 (D07 L1034/L1018, D06 L218). It is rounder and probably recallable from the widely reported 2023 fall, so use only one.
- **unresolved:** Whether readers attribute "(-162 TWh)" to coal (the fossil total is −257, which settles it), and whether "last five years" is read as 2019–2024.
- **tier:** Too easy 15 / Easy 35 / Medium 35 / Hard+ 15.
- **biggest risk:** Misreading the −162 attribution or the D06 window, which could tip it into ambiguous or Too hard.

### a02 — countries above 10% solar (strengthened h1)
- **difficulty_target:** medium
- **question (20 words):** "How many more countries generated more than a tenth of their electricity from solar power in 2025 than in 2024?"
- **answer:** 8 countries
- **facts:**
  - D07 L617 "50 countries generated more than a tenth of their electricity from solar in 2025, up from 15 in 2020."
  - D07 L617 decoy: "19 countries exceeded a 10% solar share in 2025, up from 15 in 2024 and none in 2020."
  - D06 L685 "42 countries now generate at least a tenth of their electricity from solar." The surrounding lines (L681 "in 2024") date it.
- **documents:** D06, D07
- **dependency:** Only D06 has the 2024 all-country count; only D07 has 2025. Without D06 the remaining figures give 35, 4, 7 or 28; without D07 there is no 2025 count.
- **selected_levers:** Scatter the pieces; Same series, right edition
- **lever_checks:**
  - 50 − 15 = 35 (mixing populations); 19 − 15 = 4 (larger markets only); first-half counts 29 − 22 = 7 (D03 L168).
  - D05 L155 and D02 L202 also print "50 countries", but for wind and solar combined and for monthly records.
- **arithmetic_check:** 50 − 42 = 8. Optional percentage variant: 19%.
- **shortcut_search:** Searched "tenth", "10%", "42 countries", "50 countries" in all documents and the overview. No printed difference.
- **tags:** Cross-document join, Temporal alignment, Conditional filter
- **completeness:** Full.
- **portfolio:** Uses different sections from a01; no giveaway between them.
- **unresolved:** D06 says "at least a tenth" while D07 says "more than a tenth"; D06's "now" means 2024.
- **tier:** 25 / 45 / 25 / 5.
- **biggest risk:** The D06 sentence is easy to find.

### a03 — China's fossil generation, second half of 2025
- **difficulty_target:** medium
- **question (27 words):** "How did China's fossil-fuel electricity generation in July–December 2025 compare with July–December 2024? Give the change in TWh, rounded to the nearest whole number, with its sign."
- **answer:** +3 TWh
- **facts:**
  - D07 L139 "In China, it fell by 56 TWh (-0.9%)".
  - D03 L277 "Coal generation fell by 56 TWh (-2%)", "gas generation dropped by 2.7 TWh (-2%)", "Other fossil fuels fell by 0.1 TWh (-1.8%)." D03 prints no first-half fossil total.
  - D03 L152 shows that fossil = coal + gas + other fossil.
- **documents:** D03, D07. D08 is not needed: it only yields Q3 (+7) or Q4 (−4).
- **dependency:** Only D03 has the first-half components and only D07 has the full year.
- **selected_levers:** Scatter the pieces; Calculate across documents (a total the reader must build)
- **lever_checks:**
  - Coal alone used as the first-half fossil figure: its −56 equals the full-year fossil −56, giving 0. D07 L239 "flat for nearly two years" reinforces that reading.
  - Coal-only second half gives −15; full year minus Q1–Q3 gives −4.
- **arithmetic_check:** −56 − (−58.8) = +2.8. By component: coal −15, gas +16.7, other +1.1. If the printed integers were themselves rounded, the true value would sit between +1.7 and +3.9, so the sign is robust; whole TWh survives early rounding.
- **shortcut_search:** Searched "second half", "H2", "Q4" and China fossil passages. No second-half value is printed.
- **tags:** Cross-document join, Temporal alignment, Aggregation
- **completeness:** Full.
- **portfolio:** Full-year-minus-partial family, shared with a04 and h15. Submit only one of them.
- **unresolved:** Reviewers may object to whole-TWh precision.
- **tier:** 30 / 40 / 25 / 5.
- **biggest risk:** The low model knows the transformation and sums the components.

### a04 — China's share of Q4 2025 solar growth (h4)
- **difficulty_target:** medium
- **question (22 words):** "What share of the world's year-on-year increase in solar generation in October–December 2025 came from China? Give the nearest whole percent."
- **answer:** 41%
- **facts:** D07 L179 (China +336, world +636); D08 L59 (China 280); D08 L27 (world 498)
- **documents:** D07, D08 (each holds one side of the calculation)
- **selected_levers:** Calculate across documents; Scatter the pieces
- **lever_checks:** Full year 53%, Q1–Q3 56%, first half 55% (all printed as "more than half"); using D08's ~640 forecast gives 39%.
- **arithmetic_check:** 56/138 = 40.58%
- **shortcut_search:** "more than half", "Q4". The global inputs are in the overview.
- **tags:** Cross-document join, Temporal alignment
- **tier:** 50 / 35 / 12 / 3.
- **biggest risk:** It is a standard transformation.

## Bundle note

I confirm the hooks file's finding that there is no fair analogue of the event-selects-earlier-estimate trap: every forecast exists in only one edition, and restated figures create two defensible answers. The strongest mechanisms this bundle offers are a01 and a02, so quick-test those first. All four still need blind solves, removal probes and a closed-book check.
