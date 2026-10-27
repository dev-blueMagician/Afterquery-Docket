# i01 screen, solve 1 (blind-solver, fresh context; raw return as handed back, 2026-10-19)

answer: 2.47%

confidence: high

path:
The quarter is Q4 FY2025 (three months ended July 31, 2025). The ratio is ($1,861,000 operating income + $1,363,000 restructuring costs) / $130.4M net sales = 2.47%. The packet has no exact Q4 net sales figure; the rounding of $130.4M is covered under gaps.

1. Finding the quarter. Every quarter in the packet from Q1 FY2025 to Q3 FY2026 was a GAAP operating loss except Q4 FY2025.
   - Q3 FY2026 (ended Apr 30, 2026): D04 line 180, `|Operating loss|(3,122,000)|(1,532,000)|(7,115,000)|(140,959,000)|`. The columns are 3M FY26, 3M FY25, 9M FY26, 9M FY25.
   - Q2 FY2026: D03 line 186, `|Operating loss|(1,236,000)|(10,257,000)|(3,993,000)|(139,427,000)|`.
   - Q1 FY2026: D01 line 169 and D02 line 164, `(2,757,000)`; Q1 FY2025 was `(129,170,000)`.
   - Q4 FY2025: the FY2025 operating loss is `$(139,098,000)` (D04 line 313; also D01 line 298 and D03 line 317). Subtracting the 9M FY2025 loss of (140,959,000) gives -139,098,000 + 140,959,000 = **+1,861,000**.
   - Check: the D01 line 47 text gives the same figure: "$1.9 million of operating income in the immediately preceding quarter."
   - Check: Q1 to Q3 FY2025 add up to the 9M figure: 129,170,000 + 10,257,000 + 1,532,000 = 140,959,000.
2. Q4 FY2025 restructuring costs. D04 line 319 reads `|Restructuring costs|2,422,000|4,338,000|6,505,000|14,222,000|15,585,000|`, with FY2025 in the last column.
   - 15,585,000 − 14,222,000 = **1,363,000**.
   - Check: Q1 to Q3 FY2025 add up to the 9M figure: 6,484,000 (D01 line 304) + 3,400,000 (D03 line 323) + 4,338,000 = 14,222,000.
3. Operating income before restructuring costs = 1,861,000 + 1,363,000 = **3,224,000**.
4. Q4 FY2025 net sales come from D02 line 1588: "Consolidated net sales were $111.0 million, compared to $130.4 million in the fourth quarter of fiscal 2025".
   - D01 line 40 is consistent: "a decrease of 14.8% sequentially", which implies 111.032/0.852 ≈ 130.32.
   - D01 line 43 is also consistent: gross profit "$40.7 million" at "31.2%", which implies ≈ 130.45.
5. Ratio: 3,224,000 / 130,400,000 = 2.4724%, which rounds to **2.47%**.
   - If net sales sit anywhere in the rounding band 130.35 to 130.45, the result is 2.4714% to 2.4733%, still 2.47%.
   - Using the D01 implied values (130.32 or 130.45) also gives 2.47%.

minimal_documents:
- **D02 + D04.** D04 supplies the FY2025 and 9M FY2025 operating-loss and restructuring columns and the Q3 FY2026 loss. D02 supplies the $130.4M Q4 net sales and the Q1 FY2026 loss; Q2 FY2026 then follows as −7,115,000 + 3,122,000 + 2,757,000 = −1,236,000.
- **Alternative: D01 + D04.** This uses net sales implied by the 14.8% sequential decline or by the gross-profit margin, and still gives 2.47%.
- D04 cannot be replaced: Q3 FY2025 figures and the 9M FY2025 columns appear only there. D03 is redundant.
- D05–D07 are Iridium releases and irrelevant.

readings:
- **Rounded inputs:** using the narrative "$1.9 million" and 15.6 − 14.2 = 1.4 gives 3.3/130.4 = 2.53%. This is inferior because the exact dollar figures are printed.
- **"Before restructuring" read as the company's full Non-GAAP operating income** (which also excludes amortization, stock-based compensation, CEO transition costs and other items): Q4 FY2025 = −13,775,000 + 23,687,000 = 9,912,000, and 9,912,000/130.4M = 7.60%. This does not match the wording "before restructuring costs".
- Under any reading, the quarter is Q4 FY2025.

gaps:
- The packet has no exact FY2025 annual net sales, so Q4 FY2025 net sales are only available as the rounded $130.4M. The answer is unaffected at two decimals.
- D02 was not read in full. I read lines 1095–1155, 1455–1720 and 1800–1890 and ran targeted searches for fourth-quarter, restructuring and net-sales terms.
- D05–D07 were not read; a search showed zero mentions of "Comtech" in them.
- The sources are text extractions with no PDF pages, so there was nothing to check visually.

contaminated: no

Judgement (caller): right (gold 2.47%).
