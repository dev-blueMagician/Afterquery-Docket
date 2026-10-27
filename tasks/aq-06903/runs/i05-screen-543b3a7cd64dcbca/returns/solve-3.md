# i05 strong-solver screen, solve 3 of 3 (blind-solver, fresh context; launch label "i05 blind solve 3")

Judged by the author against gold 0: RIGHT.

answer: 0 million pounds. The implied July-December 2026 molybdenum sales were 44 million lb in both releases, so there was no change.

confidence: high

path:
1. D03 is the April 23, 2026 Q1 release. It gives the full-year 2026 estimate and the second-quarter estimate. Line 31 (repeated at line 118): "Consolidated sales are expected to approximate 3.1 billion pounds of copper, 650 thousand ounces of gold and 90 million pounds of molybdenum for the year 2026, including 690 million pounds of copper, 140 thousand ounces of gold and 22 million pounds of molybdenum in second-quarter 2026."
2. D03 also gives actual first-quarter sales. Line 29: "Consolidated sales totaled ... 24 million pounds of molybdenum in first-quarter 2026." The same figure appears in the summary operating data at line 97 ("Sales, excluding purchases|24|20"), in the selected operating data at line 437 ("Consolidated|22|23|24||20") and in the text at line 116 ("First-quarter 2026 sales of 24 million pounds were higher than January 2026 estimate of 22 million pounds").
3. D04 is the July 23, 2026 Q2 release. Line 29 (repeated at line 118): "... and 93 million pounds of molybdenum for the year 2026, including 750 million pounds of copper, 160 thousand ounces of gold and 22 million pounds of molybdenum in third-quarter 2026."
4. D04 gives actual sales of 25 for the second quarter and 49 for the first six months. Line 27: "Consolidated sales totaled ... 25 million pounds of molybdenum in second-quarter 2026." Line 97: "Sales, excluding purchases|25|22|49||42" (Q2 2026 | Q2 2025 | 6M 2026 | 6M 2025). The six-month table at line 489 says "Consolidated|45|45|49||42". Since 24 + 25 = 49, this agrees with D03's first-quarter figure.
5. Calculation:
   - April implied July-December = 90 − 24 (Q1 actual) − 22 (Q2 estimate) = 44 million lb.
   - July implied July-December = 93 − 49 (first-half actual) = 44 million lb. In D04's terms that is 22 for Q3 plus an implied 22 for Q4.
   - Change = 44 − 44 = 0 million lb.
   - The full-year estimate rose by 3 (90 to 93). That rise equals the second-quarter beat (25 actual against the 22 estimate), so the second-half figure did not move. D04 line 116 supports this: "Second-quarter 2026 sales of 25 million pounds were higher than both the April 2026 estimate and second-quarter 2025 sales of 22 million pounds, primarily reflecting a reduction in inventory."
6. Units are consolidated millions of recoverable pounds, excluding purchases. Both full-year estimates are consolidated, so the share net of noncontrolling interests cannot be worked out for the full year and does not apply.

minimal_documents: D03 + D04. Both are needed:
- D03 is the only source of the April full-year estimate (90).
- D04 is the only source of the July full-year estimate (93) and the first-half actual (49).
- There is no substitute in the packet. D01 and D02 (BHP operational reviews) only contain BHP's own payable molybdenum in tonnes (e.g. D02 line 313, D01 line 252). Neither mentions Freeport or FCX.

readings:
- Main reading (each release's own full-year figure minus the actuals and estimates it reports for January-June): 0.
- Using quarter actuals 24 + 25 in place of the printed six-month 49 also gives 0.
- Misreadings, which I do not think are defensible:
  - Comparing the full-year estimates gives +3 (93 − 90). That is not the July-December quantity asked for.
  - Using the January first-quarter estimate (22, from D03 line 116) instead of the actual 24 gives an April second half of 46 and a change of −2. This goes against "each release's own figures", because D03 reports the 24 actual.
  - Comparing April's second half (44) with July's third-quarter estimate (22) mixes up the periods.
- The full-year figures are "approximate" and rounded to whole millions. At that printed precision the answer is exactly 0.

gaps:
- There are no PDFs or layout files in the packet; the manifest shows method "text" and pages null. All decisive figures are plain text and repeated consistently across the highlights, the summary operating data and the selected operating data, so extraction loss is unlikely.
- Read in full: D03 lines 1–135 and 400–504; D04 lines 1–135 and 400–559.
- Searched only: the rest of D03 and D04 for molybdenum, molybdenum sales, "million pounds of molybdenum" and "90/93 million"; D01 and D02 for molybdenum, Freeport and FCX. The other "90/93 million" hits were unrelated: "$93 million" share purchases, "690 million" and "$90 million" price sensitivity.
- Not read: the remaining narrative and schedule sections of D03 and D04 (Grasberg, cautionary statement, cost reconciliations) and most of D01/D02.

contaminated: no. There was a question.txt in the packet root, and I did not open it.
