# i01 strong-solver screen, solve 1 of 3 (blind-solver, fresh context; launch label "i01 blind solve 1")

Judged by the author against gold +0.19: RIGHT.

answer: +$0.19 billion (repriced July $8.6875B less April $8.50B = +$0.1875B, which rounds to +0.19)
confidence: high

path:
1. April estimate, D03 (Freeport 1Q26 release, filed 2026-04-23), line 322 and the line-37 bullet, which says the same: "FCX's consolidated operating cash flows are expected to approximate $8.7 billion for the year 2026, including $0.2 billion of working capital and other sources … assuming prices of $6.00 per pound of copper, $4,500 per ounce of gold and $25.00 per pound of molybdenum for the remainder of 2026."
   - Before working capital: 8.7 − 0.2 = **$8.50B**.
2. July estimate, D04 (Freeport 2Q26 release, filed 2026-07-23), line 312 and the line-35 bullet, which also match: "expected to approximate $8.3 billion for the year 2026, net of $0.3 billion of working capital and other uses … assuming prices of $6.00 per pound of copper, $4,000 per ounce of gold and $30.00 per pound of molybdenum for the second half of 2026."
   - Before working capital: 8.3 + 0.3 = **$8.60B**.
3. July's price sensitivities, D04 line 312: "The impact of price changes for the second half of 2026 on operating cash flows would approximate $150 million for each $0.10 per pound change in the average price of copper, $40 million for each $100 per ounce change in the average price of gold and $45 million for each $2 per pound change in the average price of molybdenum."
   - These are the right ones to use. July's estimate only depends on second-half prices, and the question asks to reprice July's estimate.
4. Repricing July to April's prices:
   - Gold: +$500/oz is 5 × $40M = **+$200M**.
   - Molybdenum: −$5.00/lb is 2.5 × $45M = **−$112.5M**.
   - Copper: $6.00 in both releases, so no change.
   - Net effect: **+$87.5M**.
   - Repriced July before working capital: 8.60 + 0.0875 = **$8.6875B**.
5. Change from April to July: 8.6875 − 8.50 = **+0.1875**, which rounds to **+0.19** ($ billions).
   - Arithmetic checked a second time.

minimal_documents: D03 + D04. Both are needed and nothing else in the packet can replace either:
- D04 does not restate April's $8.7B estimate, its $0.2B working-capital figure, or April's gold and molybdenum prices. Searching D04 for "4,500", "$25.00" and "8.7 billion" found only an unrelated tonnage cell (line 535).
- D03 has no July figures.
- D01 and D02 are BHP documents. The only operating-cash-flow mentions are BHP's own guidance (D02 lines 112–116), and neither mentions Freeport or FCX.

readings:
- **Reprice with April's sensitivities** (D03 line 322: $50M per $100 gold, $90M per $2 molybdenum). Gold +250, molybdenum −225, net +25, giving 8.625 − 8.50 = +0.125, so +0.13 (+0.12 with round-half-even). This is weaker: April's sensitivities cover April–December, while July's estimate only depends on second-half prices.
- **Keep working capital in** (ignoring the question's "before working-capital effects"): 8.3 + 0.0875 − 8.7 = −0.3125, so −0.31.
- **Reprice April to July's prices instead** (opposite direction, using April's sensitivities): 8.50 − 0.25 + 0.225 = 8.475 against 8.60, giving +0.125, so +0.13. This is not what the question asks.
- The main answer is +0.19.

gaps:
- The inputs are rounded to $0.1B in the releases ("approximate"), so the two-decimal result reflects the formula, not more precise underlying data. No unrounded estimate appears in either release.
- The molybdenum adjustment assumes the $45M-per-$2 sensitivity scales linearly over a $5 move.
- Coverage:
  - D03 and D04: read lines 1–140 and about 290–360, plus targeted searches for operating cash flow, working capital, the sensitivity wording and the dollar figures.
  - D01: searched only.
  - D02: searched, plus lines 108–117 read.
- The documents are text sources, so there were no PDF pages to inspect.

contaminated: no
