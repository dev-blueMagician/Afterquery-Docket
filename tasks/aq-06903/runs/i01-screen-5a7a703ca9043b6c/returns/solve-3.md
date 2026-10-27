# i01 strong-solver screen, solve 3 of 3 (blind-solver, fresh context; launch label "i01 blind solve 3")

Judged by the author against gold +0.19: RIGHT.

answer: +0.19 (billion dollars; unrounded +0.1875)

confidence: high

path:
1. April estimate, D03 (FCX 1Q 2026 release, filed 2026-04-23). Liquidity section line 322: "FCX's consolidated operating cash flows are expected to approximate $8.7 billion for the year 2026, including $0.2 billion of working capital and other sources ... assuming prices of $6.00 per pound of copper, $4,500 per ounce of gold and $25.00 per pound of molybdenum for the remainder of 2026." The highlights at line 37 say the same.
   - Before working capital: 8.7 − 0.2 = 8.5.
2. July estimate, D04 (FCX 2Q 2026 release, filed 2026-07-23). Line 312: "expected to approximate $8.3 billion for the year 2026, net of $0.3 billion of working capital and other uses ... assuming prices of $6.00 per pound of copper, $4,000 per ounce of gold and $30.00 per pound of molybdenum for the second half of 2026." The highlights at line 35 say the same.
   - Before working capital: 8.3 + 0.3 = 8.6.
3. July sensitivities, D04 line 312: "The impact of price changes for the second half of 2026 on operating cash flows would approximate $150 million for each $0.10 per pound change in the average price of copper, $40 million for each $100 per ounce change in the average price of gold and $45 million for each $2 per pound change in the average price of molybdenum."
4. Repricing July to April's prices:
   - Gold: $4,000 to $4,500 is +$500, so 5 × $40M = +$200M.
   - Molybdenum: $30 to $25 is −$5, so 2.5 × $45M = −$112.5M.
   - Copper: $6.00 in both releases, so no adjustment.
   - Net: +$87.5M.
   - Repriced July estimate before working capital: 8.6 + 0.0875 = 8.6875.
5. Change from April to July: 8.6875 − 8.5 = +0.1875, which rounds to +0.19 billion.
6. Check on the working-capital classification: the cash-flow statements put the PTFI insurance items in the adjustments section, not under "Changes in working capital and other":
   - D03 line 613: "PTFI mud rush incident insurance settlement|(699)".
   - D04 lines 666–667: gain (699) and proceeds 699.
   - In D04, the six-month working-capital lines (268 − 171 − 48 − 362 − 144 = −457) match footnote e: "$457 million for the first six months of 2026". So the guidance's "working capital and other" figure is the one to remove; the insurance proceeds don't change the result.

minimal_documents: D03 and D04. Both are needed: D03 gives the April estimate and prices; D04 gives the July estimate, prices and sensitivities. No replacements exist. D01 and D02 (BHP operational reviews) were searched for "freeport|FCX|operating cash flow". D01 had no matches, and D02 had only BHP's own guidance lines (lines 112–116), so neither can stand in.

readings:
- Repricing with April's sensitivities ($50M per $100 of gold, $90M per $2 of molybdenum; D03 line 322): +250 − 225 = +$25M, giving 8.625 − 8.5 = +0.125, so +0.13 (or +0.12 with half-even rounding). This is weaker. Those sensitivities cover April through December, while the July estimate's open price period is the second half of 2026, which is what D04's sensitivities cover.
- Not removing working capital (this ignores "before working-capital effects"): 8.3 + 0.0875 − 8.7 = −0.3125, so −0.31.
- I don't think any other reading holds up. Copper needs no adjustment.

gaps:
- All headline figures are approximations printed to one decimal ("approximate $8.7 billion", "$0.2 billion", "$0.3 billion"). The two-decimal precision comes only from the sensitivity arithmetic.
- The source files are text (manifest method "text", pages null). No PDF page images were available or needed, and no extraction problems affected the paragraphs used.
- Coverage:
  - D03 and D04: I read the highlights (about lines 30–40), the consolidated unit cost outlook (110–140), the PTFI, molybdenum and liquidity sections (290–340 and 290–330), the cash-flow statements, and the U.S. mines sensitivity lines.
  - Searched all four documents for operating cash flow, working capital, sensitivity and insurance terms.
  - Not read in full: the rest of D03 and D04, and all of D01 and D02 apart from search hits.
  - Not opened: question.txt in the packet.

contaminated: no
