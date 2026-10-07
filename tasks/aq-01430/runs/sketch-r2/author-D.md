# Question-author D, sketch round 2 (raw return, 2026-10-06)

Fresh question-author agent (Claude Code, claude-opus-5-5), target medium, given round 1's results
and constraints and asked for cross-document qualitative levers and three-document chains outside
the partial-period family; no files written. Origin: claude. 3,668 s, 26 tool uses. Return copied
verbatim.

---

I found no fair design outside the window family that I would expect to reach Medium. Three fair sketches survived, all Easy-leaning (Medium about 12% each). They are ranked below; none has been through a fresh solve, closed-book run or audit yet, and I wrote no files. Origin: claude.

## d01 — G7 without the US (carve-out that flips the sign)
- **Question (25 words):** "By how many TWh did combined gas-fired electricity generation in the G7 countries other than the United States change in 2025? Give the sign."
- **Answer:** +13 TWh
- **Facts:**
  - D01 L100: "In 2025, gas generation in the G7 fell by 50 TWh, from 2,627 TWh to 2,577 TWh"
  - D07 L703: "The largest gas power decline in 2025 was in the United States (−63 TWh, −3.4%)" (repeated at L958)
  - The US is a G7 member: D06 L1032, "all other G7 members"
- **Documents:** D01 (Doc 8), D07 (Doc 4)
- **Removal tests:** Without D01 there is no G7 gas figure (D07 L663 gives G7 wind only). Without D07 there is no US 2025 change; estimates from D01's shares (L98) plus D06's 2024 level land on about +40, not +13.
- **Levers:** calculate across documents, with a printed whole-group decoy.
- **Decoys:** −50 (the printed G7 total), −113, and +8 (see biggest risk).
- **Arithmetic (python):** −50 − (−63) = +13. Integer rounding gives a band of 11.5–14.5. D07's implied 2024 US level (1,807 + 63 = 1,870) also gives +13.
- **Overview exposure:** the input 2,577 appears in the Doc 8 overview; the answer does not.
- **Closed-book risk:** moderate to low, because small answers near zero can be guessed.
- **Tags:** cross-document join, aggregation.
- **Tier:** Too easy 40%, Easy 45%, Medium 12%.
- **Biggest risk:** this is two lookups and one subtraction, the pattern the Coach says is usually solved. A second risk is one clear answer: working from levels with D06's 2024 US figure gives 770 − 762 = +8.

## d02 — the four largest emitters, full-year vs first-half solar share
- **Question (37 words):** "Among the four largest power-sector CO2 emitters, counting the EU as one economy, which got a smaller share of their electricity from solar over the whole of 2025 than in January–June 2025? List in any order."
- **Answer:** China, the United States, the European Union
- **Universe:** China, India, the EU and the US. D03 L51 and L249 name these as the top four emitters, and D07 L1106 and L1224 confirm the ranking.
- **Facts:**
  - January–June 2025 (D03): China 11.5% (L269), US 8.7% (L295), India 9.2% (L323), EU 14% (L345)
  - Full year 2025 (D07): EU 13.1%, US 8.6%, China 11.1% (L1050); India 9.4% (L1098)
- **Excluded item / decoy:** India, whose share rose from 9.2% to 9.4%. A quick reader who reasons from seasons alone would include it. This is not a keyword filter, because no passage states the direction for any item.
- **Removal tests:** D03 holds only the first-half shares, D07 only the full-year shares, and D08 prints no country shares.
- **Levers:** scatter the pieces, plus the decoy.
- **Arithmetic:** comparison only. EU 14% means 13.5–14.5, so 13.1 is lower whichever way it rounds. The smallest margin is the US, at 0.1 points.
- **Overview exposure:** none.
- **Closed-book risk:** low. The likely guess is "all four", which misses.
- **Tags:** cross-document join, temporal alignment, conditional filter.
- **Tier:** Too easy 45%, Easy 40%, Medium 12%.
- **Biggest risk:** it rests on eight labelled lookups (the trial-07 q05 pattern), and it uses the same mid-year/annual document pair as the window family, though with no arithmetic.

## d03 — India's record-year bridge
- **Question (29 words):** "By how many TWh did global wind generation growth in 2025 fall short of its growth in the year India set the hydropower record it broke in 2025?"
- **Answer:** 46 TWh
- **Facts:**
  - D07 L1100: "surpassing the previous record set in 2022 (175 TWh)"
  - D02 L212: "2021 saw the largest growth in wind generation in history (+268 TWh), but this slowed in 2022 (+251 TWh)"
  - D07 L181: 2025 growth "205 TWh"
- **Documents:** D07 (Doc 4), D02 (Doc 5)
- **Removal tests:** Only D02 gives 2022 wind growth (D06 L713 says growth slowed but gives no figure). Only D07 gives the bridge and the 2025 growth.
- **Levers:** scatter the pieces, plus calculate across documents.
- **Decoys:** 63 (2021 is in the same sentence), 60 (D07's 2021 record of 265), 61 (2024's +190), and the D05 2021 figure of 227.
- **Arithmetic:** 251 − 205 = 46.
- **Overview exposure:** none.
- **Closed-book risk:** low.
- **Tags:** cross-document join, temporal alignment.
- **Tier:** Too easy 45%, Easy 40%, Medium 12%.
- **Biggest risk:** the bridge is a date printed in one plain sentence (the aq-00949 q02 / aq-00998 q03 pattern). Without D07, a solver could also guess 2022 from D06 L1120 ("decline of 26 TWh in 2023"), and review may call the pairing manufactured.

## Why the qualitative levers and other routes fail here
- **Hedge applies:** each hedged forecast is settled by a single later sentence (D06 L425 → D07 L139; D06 L429 → D07 L139; D08 L107 → D07 L1096). A "which came true" question would be about Ember's statements, which rule 10 discourages, and each item is a lookup.
- **Mentions it vs does it:** every item prints its own cause (gas covering for weak hydro at D07 L701, L1022, L1260; nuclear vs renewables at L697), so these are keyword filters. Brazil is a real decoy (D07 L1254 says solar and wind were "more than sufficient", yet fossil generation rose by 6 TWh), but D07 alone settles all seven largest power sectors (L139, L1146, L1188).
- **Match then exclude:** the candidate universes are incomplete in the real world. A coal phase-out list misses Slovakia (2024) and Belgium (2016). G7 gas peaks are missing for France and Canada. Japan's 2025 emissions direction cannot be determined because the two editions use different units (493 MtCO2 at D06 L1226 vs 492 MtCO2e at D07 L1210).
- **Event-to-edition bridges:** D06 is the default latest full year before D07, so a solver can reach a 2024 answer without the bridging document. For example, "the last year wind out-generated solar" leads to 42 countries (D06 L685) even with D07 removed.
- **Renewables growth vs the 2024 record:** two defensible answers. Working from D07's own changes gives 887 − 35 = 852; working from levels across editions gives 10,730 − 9,841 = 889.

Quick-test d02 first, because its decoy is not keyword-driven; then d01, then d03.
