# Question-author C, sketch round 2 (raw return, 2026-10-06)

Fresh question-author agent (Claude Code, claude-opus-5-5), target medium, given round 1's results
and constraints and asked for scope-selection, late-buried-input and exact-versus-approximate
designs outside the partial-period family; no files written. Origin: claude. 1,412 s, 33 tool
uses. Return copied verbatim.

---

Three sketches are fair, but none is expected to reach Medium more often than q01 (Medium about 12%). For mechanism (3) I found no fair design. Origin: claude. Every fact below comes from `tasks/aq-01430/text/Dnn.txt`. I wrote no files.

**c01 — scope (G7 minus the US, sign flip)**
- **Question (27 words):** "How did gas-fired electricity generation in the G7 countries other than the United States change from 2024 to 2025? Give the change in TWh with its sign."
- **Answer:** +13 TWh
- **Facts:**
  - D01 L100: "In 2025, gas generation in the G7 fell by 50 TWh, from 2,627 TWh to 2,577 TWh"
  - D07 L703: "The largest gas power decline in 2025 was in the United States (−63 TWh, −3.4%)". L958 repeats −63.
- **Documents:** D01 (Doc 8) and D07 (Doc 4). G7 totals appear only in D01; the US 2025 change appears only in D07.
- **Removal tests:**
  - Without D07: D01's 26%/37% shares plus D06's 1,865 give +4. D01's +474 (2015–25) against D06's +531 (2015–24) gives +7.
  - Without D01: there is no G7 total. Only D06 L1032's "more than double the gas generation of all other G7 members combined" remains.
- **Levers:** who belongs where; calculate across documents
- **Decoys:** −50 (whole G7); −8.5 (Japan, D07 L709); +34 (EU, D07 L1022); +8 (D07 L713 1,807 minus D06 L861 1,865); +7 (window route above)
- **Arithmetic (python):** (2,577 − 2,627) − (−63) = 13. Cross-check: non-US level 770 (2025) minus 757 (2024, D07 basis) = 13.
- **Alternative figures:** the US change is printed once (−63, twice). The level and window routes give +8 and +7 by mixing in the April-2025 data.
- **Overview exposure:** only 2,577 (Doc 8). The 2,627, −50 and −63 figures are not there.
- **Closed-book risk:** low to moderate. The G7 total is from June 2026, and the sign flip guards against a guess.
- **Tags:** cross-document join; conditional filter
- **Tier:** Too easy 40%, Easy 45%, Medium 12%
- **Biggest risk:** one lookup plus one subtraction, and the question names the exclusion. The +8 and +7 routes may be read as a second answer.

**c02 — scope and timing (China's share of 25 years of demand growth)**
- **Question (24 words):** "What share of the world's growth in electricity demand between 2000 and 2025 came from China? Give the percentage to one decimal place."
- **Answer:** 55.9%
- **Facts:**
  - D06 L960: "increased sevenfold from 2000 (1,347 TWh) to 2024 (10,066 TWh)"
  - D07 L553: "reaching 10,573 TWh of electricity demand in 2025"
  - D07 L525: "31,779 TWh"
  - World 2000 demand: D01 L50 "15,279 TWh in 2000 to 31,774 TWh in 2025", or D06 L520 + L522 (4,199 + 11,079)
- **Documents:** D06 and D07. D01 is optional.
- **Removal tests:**
  - Without D07: the 2000–2024 route gives 56.0, and D06's 2024 China with D01's 2025 world gives 52.9. Both miss.
  - Without D06: only "less than 10%" (D07 L553) remains.
- **Levers:** same-label decoy for a different period; calculate across documents
- **Decoys:**
  - 59% (D07 L543, "This accounted for 59% of the global net increase", 2025 alone)
  - 66.7% (D05 L454, "two-thirds of the growth in global hydro ... since 2000")
  - 56.0 and 52.9 (above)
  - 33.3% (share of the 2025 level)
- **Arithmetic and alternative figures:** each mix of 31,779/31,774 and 15,278/15,279 gives 55.912–55.932, all 55.9. I rejected the percentage-point version (24.454), because it splits 24.4/24.5 under half-even rounding.
- **Overview exposure:** none.
- **Closed-book risk:** moderate. Estimates land around 55%.
- **Tags:** cross-document join; temporal alignment; aggregation
- **Tier:** Too easy 30%, Easy 50%, Medium 15%
- **Biggest risk:** the removal test on D06. China's 2000 demand (1,347 TWh) matches the official Chinese statistic, and recalling 1,350 alone gives 55.9 without D06.

**c03 — buried input in the country chapters (France's 2025 nuclear level appears nowhere)**
- **Question (21 words):** "What percentage of the world's nuclear-generated electricity in calendar year 2025 came from France? Give the answer to one decimal place."
- **Answer:** 13.9%
- **Facts:**
  - D06 L819: "ahead of China (445 TWh), and France (379 TWh)" (2024)
  - D07 L751: "Nuclear generation in France rose by 11.6 TWh"; L185 has "+12 TWh"
  - D07 L741: "to an all-time high of 2,812 TWh"
- **Documents:** D06 and D07
- **Removal tests:**
  - Without D06: recalling EDF's widely cited lower figures gives 13.3, and per capita × population gives 14.35. Both miss.
  - Without D07: D06 alone gives the 2024 share, 13.7.
- **Levers:** bury the input late; same-label 2024 level
- **Decoys:** 13.5 (stale 379/2,812); 13.7 (379/2,768); 69% (France's own mix, D07 L765 and D05 L402)
- **Arithmetic:** 390.6/2,812 = 13.890; 391/2,812 = 13.905. Both are 13.9.
- **Overview exposure:** none.
- **Closed-book risk:** low to moderate, because Ember's gross figure differs from EDF's.
- **Tags:** cross-document join; temporal alignment
- **Tier:** Too easy 30%, Easy 55%, Medium 12%
- **Biggest risk:** it is one routine year-alignment step. A hidden restatement is also possible: D07 revised China's 2024 nuclear (445→451) and the world total (2,768→2,777), so France's base in the later edition is unknowable. The gold rests on the only route the bundle offers.

**Mechanism (3): no fair design**
- **The rounded proxy usually sits beside its exact value in the same D07 sentence:** L201, L589, L904, L906, L1102, L1266.
- **Where the exact value needs another document, the older input is a widely known figure:**
  - US coal (D06 L905 653 + L1018 1,364 = 2,017; D07 L968 "nearly two-thirds (-1,279 TWh)") gives 36.6%. The EIA's 2007 coal peak (about 2,016 TWh) gives 36.56%, so D06 fails the removal test.
  - China's 2000 demand has the same problem as c02.
- **Or the editions conflict:** D01 L90 says the US was "just under one-third" of global gas growth, but D06 + D07 give 474/1,377 = 34.4%.
- **Or the rounded inputs are stated as plain figures:** D01 L98's "37%" and "26%" give a US share of G7 gas of 70.3%, against 70.1% from 1,807/2,577. That is two defensible answers.

**Other rejections**
- **Europe vs EU:** asking about the EU leads straight to the EU figures, and D01 L70's Europe 23.8% has no year.
- **OECD solar:** 2024 is only implied by the rounded "58%" non-OECD share (D06 L279).
- **DC vs AC capacity:** D06 L403's 277 GWac has no exact DC counterpart.
- **G7 wind share:** 819 ÷ (2,577/0.329) moves between 10.44% and 10.47% with the rounding of 32.9%.
- **Russia gas:** D07's "−13 TWh, −2.3%" implies a base of about 565, against D06's 538, which gives 7.6 vs 8.0.
- **India's coal share:** 14.2 vs 14.1, alongside the printed 69% − 55%.
- **Japan's clean generation vs 2000:** D07 restates 2024, and a model without the documents can estimate it.

**Set notes:** no shared answer paths with q01/q02. c02 and c03 reuse q01's document pair (D06 + D07) for different quantities. c02 and c03 are the same broad shape: rebuild a level that no document prints.

**Unresolved:** nothing has been checked yet beyond my own reading. My recommendation is to quick-test c02 and c03 only after a removal probe without D06, and to tell the user the bundle probably has no fair Medium design.
