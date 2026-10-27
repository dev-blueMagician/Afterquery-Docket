# i06 strong-solver screen, solve 1 of 3 (blind-solver, fresh context; launch label "i06 blind solve 1")

Judged by the author against gold 74: RIGHT.

answer: $74 million

confidence: medium-high. The arithmetic checks out two independent ways. The only real risk is the reading: some will equate "sales made in Q1 2026" with all sales still open at March 31, 2026, which gives $98 million (see readings).

path:
1. D04 (2Q26 release), "DERIVATIVE INSTRUMENTS" table, text/D04.txt lines 839-849 (docs original line 878): Three Months Ended June 30, 2026, "|Revenues|$98|$40|$138|" (Prior Period / Current Period / Total). Footnote a: "Reflects adjustments to provisionally priced copper sales at March 31, 2026 and 2025." Footnote b: "Reflects adjustments to provisionally priced copper sales during the second quarters of 2026 and 2025." Footnote b at D04 line 70 gives the same figure: "$98 million ... in second-quarter 2026 ... $58 million ... for the first six months of 2026."
2. D04 lines 851-861 (docs line 892): Six Months Ended June 30, 2026, "|Revenues|$58|$59|$117|". Prior period footnote: "adjustments to provisionally priced copper sales at December 31, 2025". Current period footnote: "for the first six months of 2026."
3. D03 (1Q26 release), lines 741-751 (docs line 774): Three Months Ended March 31, 2026, "|Revenues|$34|$(55)|$(21)|". Prior period footnote: "at December 31, 2025". Current period footnote: "for the three months ended March 31, 2026." D03 line 70 confirms "$34 million ... in first-quarter 2026."
4. D03 line 735 and D04 line 833 both say final pricing comes "generally one to four months from the shipment date", so some sales from late 2025 can still be open at March 31. That makes the $98 million a mix of Q1-2026 sales and older 2025 sales.
5. Decomposition (revenues, $M):
   - Q2 repricing of sales open at Dec 31, 2025 = 58 (six-month prior period) - 34 (Q1 prior period) = 24.
   - Q2 repricing of sales made in Q1 2026 = 98 - 24 = **74**.
   - Independent check from the current-period columns: 59 (six-month current) = -55 (Q1 current) + Y + 40 (Q2 current), so Y = 59 - 40 + 55 = **74**. Same result.
   - Total check: -21 (Q1) + 138 (Q2) = 117 = six-month total. Correct.
   - Applying the same method to 2025 data also reconciles: Z = 63 - 70 = -7, Y = -35 + 7 = -28, and 46 - 28 + 69 = 87. Correct.
6. Side note, not asked: the same split applied to net income attributable to common stock gives 20 - 15 + 18 = 23 (and 35 - (24 - 12) = 23).

minimal_documents: D03 + D04. D04 alone cannot separate the $98M between Q1-2026 sales and older open sales, because without D03's Q1 split (34 / -55) the equations collapse into an identity. D03 alone has no Q2 data. Nothing else in the packet can stand in for either: D01 and D02 are BHP filings with no mention of "Freeport" or "FCX". D04 alone is enough only for the $98M reading.

readings:
- Alternative (literal footnote mapping): read "provisionally priced copper sales it had made in Q1 2026" as the prior-period column, "adjustments to provisionally priced copper sales at March 31, 2026". Answer: $98 million. This includes about $24M of repricing on pre-2026 sales still open at March 31.
- The net-income version ($23M by the split, $35M under the literal reading) does not fit, because the question asks about revenue.
- I rejected an estimate from D03 line 753 (136 million lbs at $5.58/lb, about $12M per $0.05 move). The filings report the actual figures, so an estimate isn't needed.
- I did not use the D04 segment tables. Their "Other revenue adjustments, primarily for pricing on prior period open sales" rows for Q2 2026 are U.S. copper mines $6M and South America copper $91M (+$7M other = $98M segment total). The Indonesia Q2 2026 table has no such line. These rows are segment-level, include non-copper metals and intercompany sales, and do not split by the quarter of sale.

gaps:
- No PDFs or layout files are in the packet. D03 and D04 come from .txt sources, and I checked the key table rows against the docs/ originals; they match.
- I read the derivative sections, the line-70 footnotes and part of D04's product revenue schedules. I did not read all of D03 or D04. I searched all four texts for "provisional" and searched D03/D04 for "adjustment", "open sales" and related terms; I found no other figure that conflicts.
- I searched D01 and D02 only for Freeport/FCX mentions and did not otherwise read them.
- The decomposition assumes the six-month "prior period" column is the cumulative repricing over January-June of sales open at December 31, 2025, which is what its footnote says. The filings never state the $74M directly.
- I deliberately did not open question.txt in the packet.

contaminated: no
