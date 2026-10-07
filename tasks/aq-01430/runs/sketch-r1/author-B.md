# Question-author B, sketch round 1 (raw return, 2026-10-06)

Fresh question-author agent (Claude Code, claude-opus-5-5), target medium, told NOT to read
notes/hooks.md or notes/ideas.md (independent of the caller and author A); no files written.
Origin of sketches: claude. 2,710 s, 36 tool uses. Return copied verbatim.

---

No clean version of the Medium mechanism you ranked first, (a), exists in this bundle. Of the five designs below, only b01 has a realistic Medium chance (about 30%); the rest lean Easy or Too easy. None has been checked locally or measured. Writer origin: claude.

**Why (a) has no fair analogue**
- The only outlook repeated across editions is the IEA stated-policies scenario: D06 L343 dates it to October 2024 (3.3% a year, 2023-2030), but D07 L392 gives 3.2% "to 2035" with no date. Saying which one was "in force when X happened" would need dates from outside the bundle.
- Ember's own 2025 forecasts appear in one edition only (D08 L53, L79).
- The dated 2025 events (Taiwan's last reactor in May, D07 L755; Finland and Ireland ending coal, L1036; China's June rule change, L894) have no matching value in another edition.
- Many 2024 figures conflict between D06 and D07 (for example, US gas 1,865 TWh in D06 L1032 against 1,807+63 in D07; global gas +103 against +183 TWh). This rules out cross-edition remainders for 2024.
- For (d), every qualitative filter I tried was answerable from D07 alone (its "first since…" sentences), had an incomplete set of candidates, or printed the answer pair outright (D03 L105).

---

**b01 (rank 1)**
- difficulty_target: medium
- question: How many more countries generated over 10% of their electricity from solar power in 2025 than in 2024?
- answer: 8 countries
- facts:
  - D07 L617: "50 countries generated more than a tenth of their electricity from solar in 2025, up from 15 in 2020… Among larger electricity markets, defined as those with more than 5 TWh… 19 countries exceeded a 10% solar share in 2025, up from 15 in 2024". L587 repeats the 50.
  - D06 L685 (2024 review): "42 countries now generate at least a tenth of their electricity from solar."
- documents: D06, D07
- dependency: D06 holds the only all-country count for 2024; D07 holds the only one for 2025. Other routes give different answers: D03 L168 (first-half counts) gives 7; D05 L155 (wind and solar, 2021) gives 7; interpolating D07's 2020 and 2025 counts gives about 7.
- selected_levers: same series, right edition; who belongs where (population scope)
- lever_checks:
  - The trap is in D07's own sentence: the larger-market pair gives 19−15 = 4, which is exactly the "2025 versus 2024" shape asked.
  - The question's "10%" matches the trap sentence's wording, while the correct sentences say "a tenth".
  - Other wrong routes: 50−15 = 35 and 29−22 = 7.
- arithmetic_check: Python, 50−42 = 8
- shortcut_search:
  - I searched "tenth", "10%" and "countries" across all eight documents. No 2024 all-country count exists outside D06, and the bundle overview doesn't mention any of these counts.
  - Strongest surviving route: searching "a tenth of their electricity from solar" finds D06 L685 and D07 L587 together.
- closed-book risk: low to moderate, since both counts were in April 2025 and April 2026 press coverage.
- tags: cross-document join; temporal alignment; conditional filter
- completeness: all text read. The chart placeholders in D07 chapter 3.3 are empty in the originals too.
- portfolio: no other sketch uses this mechanism.
- unresolved:
  - D06 says "at least" a tenth and D07 says "more than" a tenth.
  - The 42 comes from the April 2025 data. D07 prints no 2024 count for all countries.
- tier: Too easy 20%, Easy 40%, Medium 30%, Hard 10%. Biggest risk: the shared phrase finds both 50 and 42 at once.

**b02 (rank 2)**
- question: Between the first half of 2023 and the first half of 2024, by how many percentage points did wind and solar's combined share of global electricity generation change?
- answer: +1.4 percentage points
- facts:
  - D02 L180: "Together wind and solar generated 14.3% of global electricity in the first half of 2023… a 1.5 percentage points increase from the same period last year"
  - D03 L148: "up from 6.9% in the first half of 2024" (solar)
  - D03 L190: "up from 8.8% in the same period last year" (wind)
- documents: D02, D03
- dependency: no document prints a combined share for the first half of 2024 (searched for "15.7"). Other routes give different answers: D08 L48 (15.2% for January-September 2024) gives 0.9; D06 L548 (15%, full year) gives 0.7; D06's full-year 2023 figures give 2.3.
- selected_levers: same series, right edition; scatter the pieces
- lever_checks:
  - D02 prints a 1.5-point rise for the previous year.
  - Using the first-half 2025 shares gives 3.7.
  - Solar is 8.8% in 2025 and wind is 8.8% in 2024, so mixing them up gives 3.3.
- arithmetic_check: 6.9+8.8−14.3 = 1.4. The component route, (6.9−5.5)+(8.8−8.8), also gives 1.4.
- unresolved: if each one-decimal input is treated as rounded, the result could lie anywhere from 1.25 to 1.55. Face value (1.4) is the only stated route.
- closed-book risk: low to moderate. Ember's mid-2024 report (not in the bundle) may be recalled.
- tags: cross-document join; temporal alignment; aggregation
- tier: Too easy 25%, Easy 45%, Medium 22%, Hard 8%. Biggest risk: the question's period words rule out every decoy.

**b03 (rank 3)**
- question: For October–December 2025 versus the same months of 2024, what was the rise in global solar generation divided by the rise in global electricity demand, as a percentage to one decimal place?
- answer: 56.1%
- facts:
  - D08 L44: "Solar generation rose by 498 TWh… growth in demand of 603 TWh"
  - D07 L179: "636 TWh… increase in electricity demand of 849 TWh"
  - Trap inputs: D08 L53 "around 640 TWh" and L79 "831 TWh" (Ember's forecasts, in the same document as the nine-month figures)
- documents: D07, D08. D01 L58 repeats 636, so D01 is quoted but not listed.
- dependency: the 849 is only in D07. Using D01's "around 75%" instead gives 56.3%; the first-half route via D03 gives 68.8%.
- selected_levers: calculate across documents; forecast versus actual
- lever_checks: the forecast route gives 62.3%. Printed answer-shaped decoys are 75% (full year) and 83% (first half).
- arithmetic_check: 138/246 = 56.098%
- shortcut_search: no document prints fourth-quarter flows. The bundle overview lists all six inputs.
- portfolio: same family as b05 and shares the 849 input. Keep only one of the two.
- tier: Too easy 45%, Easy 40%, Medium 12%, Hard 3%. Biggest risk: full year minus nine months has been measured as too easy.

**b05 (rank 4)**
- question: For July–December 2025 compared with July–December 2024, what percentage of the rise in global electricity demand came from China? Give one decimal place.
- answer: 63.5%
- facts:
  - D03 L136: "Global demand rose by 369 TWh"
  - D03 L144: "China 54% (198 TWh)"
  - D07 L543: "adding 503 TWh… 59% of the global net increase… (+849 TWh)"
- documents: D03, D07. D08 has no China demand figure.
- lever_checks: the printed 54% (first half) and 59% (full year) are answer-shaped. A variant using the four largest emitters gives 83.6%, against D03's printed 81%.
- arithmetic_check: 305/480 = 63.54%
- tier: Too easy 40%, Easy 42%, Medium 15%, Hard 3%.

**b04 (rank 5)**
- question: In 2025, how much gas-fired electricity did the G7 countries other than the United States generate in total, in TWh?
- answer: 770 TWh
- facts:
  - D01 L100: "from 2,627 TWh to 2,577 TWh"
  - D07 L713: "producing 1,807 TWh"
  - D01 L98: G7 37% and US 26% of global gas
- documents: D01, D07
- dependency: using D01's percentages alone gives 2,577×11/37 = 766, so the TWh answer needs D07.
- lever_checks: I rejected a sign-flip version (the rest of the G7 rose by 13 TWh). Using D06's 2024 US figure of 1,865 gives +8 instead, so it would have two defensible answers.
- tier: Too easy 65%, Easy 27%, Medium 7%, Hard 1%. Biggest risk: two lookups and one subtraction, and the question names the exclusion.

**Recommendation:** quick-test b01 and b02 first. Quick-test only one of b03 and b05.
