# i01 strong-solver screen, solve 3 (blind-solver, claude-opus-5-5, effort max, fresh context)

Raw return as received 2026-10-19:

answer: US$85.7 per tonne

confidence: high

path:
1. Price basis. Footnote to the energy coal price: "Export sales only. Includes energy coal sales from steelmaking coal mines." (D02 Appendix 1, fn vi). D01's footnote ii says the same: "Export sales only. Includes thermal coal sales from steelmaking coal mines." So the weighting volume is NSWEC "Energy coal - Export" plus BMA "Energy coal" sales at BHP's 50% share. BMA is reported on a proportionate basis: D01 says "equity accounted investments and other operations are reported on a proportionate consolidation basis."
2. FY25 price. D02 Energy coal panel: "Average realised price US$104.28/t ê3% FY25 US$107.80/t". The appendix row agrees: 104.28, (3%).
3. Nine-month price to March 2025. D01 Energy coal panel: "Average realised price US$99.04/t ê15% YTD Mar FY25 US$115.99/t". The appendix row agrees: 99.04, (15%).
4. Sales volumes in kt. In D02 Appendix 2 (coal page), the columns run Jun 2025 quarter … YTD Jun 2026, then YTD Jun 2025.
   - NSWEC "Energy coal - Export": 3,554 in the Jun 2025 quarter and 13,569 for YTD Jun 2025.
   - BMA "Energy coal": 199 in the Jun 2025 quarter and 313 for YTD Jun 2025.
   - D01 Appendix 2 gives YTD Mar 2025 export 10,015 and BMA energy coal 114. The same Jun 2025 quarter values appear there (3,554 and 199).
   - Reconciliation: 10,015 + 3,554 = 13,569 and 114 + 199 = 313.
5. Weighting volumes:
   - FY25: 13,569 + 313 = 13,882
   - 9M FY25: 10,015 + 114 = 10,129
   - Q4 FY25: 3,554 + 199 = 3,753
6. Calculation:
   - 107.80 × 13,882 = 1,496,479.6
   - 115.99 × 10,129 = 1,174,862.71
   - Difference: 321,616.89 (US$k)
   - 321,616.89 / 3,753 = 85.6959… → 85.7
7. Rounding sensitivity. The published prices carry ±0.005 rounding, which moves the result by about ±0.03 (range 85.66–85.73). The answer stays 85.7.
8. Cross-checks:
   - D02 shows the Q4 FY26 energy coal price at 117.74, "v Q4 FY25" 37%. 117.74 / 85.696 = 1.374, which matches 37%.
   - The weighting basis also checks out on FY26. Using 9M FY26 (D01: 99.04 on 11,674 + 165 = 11,839 kt) and Q4 FY26 (117.74 on 4,224 + 383 = 4,607 kt) gives 104.278. Reported: 104.28.
   - Weighting by NSWEC exports alone gives 104.01 for FY26, which does not match.
   - D02 "v H2 FY25" 23% and D01 "v Q3 FY25" 8% are also consistent with 85.7.

minimal_documents: D01 + D02. Only D01 has the 115.99 nine-month FY25 price, and only D02 has the 107.80 FY25 price. The nine-month volumes can come from D01 or be derived from D02 (FY25 minus the Jun 2025 quarter). D01 also repeats the Jun 2025 quarter volumes. D03 and D04 (Freeport) can't replace either document: they have zero matches for "BHP" or "coal".

readings:
- NSWEC exports only, leaving out BMA energy coal: (107.80×13,569 − 115.99×10,015)/3,554 = 84.7. This goes against the footnote, implies about +39% instead of the reported 37%, and fails the FY26 check.
- Including NSWEC domestic sales: (107.80×15,502 − 115.99×11,377)/4,125 = 85.2. This goes against "Export sales only" and implies about +38%.
- BMA energy coal at 100% basis (398 / 626 / 228 kt): 86.6. The FY26 check fails (104.53 vs 104.28).
- Shortcut from the rounded percentage: 117.74/1.37 = 85.9. It's only approximate because 37% is rounded, and it doesn't use the volumes the question asks for.

gaps:
- BMA energy coal sales aren't split into export and domestic. I assumed all of them fall within the export price basis, as the footnote implies and the FY26 check supports.
- Unread material: D02 after about line 550 (JORC footnotes and signatures) was not read line by line, but a grep for energy coal, thermal coal, NSWEC and realised found nothing after line 490. D03 and D04 were not read; grep for BHP and coal returned 0 matches.
- The packet's documents are text only (no PDFs or layout files). The decisive rows in text/ match the docs/ source text.
- There's a typo in D02's coal sales header ("Dec 2026" instead of Dec 2025). It doesn't affect the answer.
- The packet's question.txt was not read.

contaminated: no
