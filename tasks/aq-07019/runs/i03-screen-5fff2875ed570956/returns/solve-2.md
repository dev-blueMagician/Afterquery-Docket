# i03 strong-solver screen, solve 2 (blind-solver, claude-opus-5-5, effort max, fresh context)

Raw return as received 2026-10-19:

answer: US$177.3 per tonne (unrounded value 177.2895)

confidence: high

path:
Packet text: D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-07019\runs\i03-screen-5fff2875ed570956\solver-1\text\D01.txt and \D02.txt. I checked the key rows against the docs/ source .txt files and they are the same.

1. Target quarter: the quarter ended 30 June 2025 is Q4 FY25, since BHP's fiscal year ends on 30 June. No document states the Q4 FY25 steelmaking coal price directly. D02 only gives rounded comparisons ("v Q4 FY25 31%").
2. Nine-month FY25 price. D01 line 120 (steelmaking coal panel, p.3): "Average realised price US$200.25/t 0% YTD Mar FY25 US$200.12/t".
3. Full-year FY25 price. D02 line 167 (steelmaking coal panel, p.4): "Average realised price US$210.21/t é8% FY25 US$193.82/t".
4. Sales volumes (BHP share, kt):
   - D01 line 418 (Appendix 2, BMA sales, p.10): "Hard coking coal|kt|…|3,708|4,831|4,428|4,302|3,842|12,572|12,676|(1)%". The columns are the Mar 2025, Jun 2025, Sep 2025, Dec 2025 and Mar 2026 quarters, then YTD Mar 2026 and YTD Mar 2025. So YTD Mar FY25 = 12,676 and the Jun 2025 quarter = 4,831.
   - D02 line 483 (Appendix 2, p.11): "Hard coking coal|kt|…|4,831|4,428|4,302|3,842|5,522|18,094|17,507|3%". So the Jun 2025 quarter = 4,831 and YTD Jun 2025 (FY25) = 17,507.
   - Check: 17,507 − 12,676 = 4,831, which matches the reported quarter.
5. Which volume to use. The energy coal price footnotes say BMA's energy coal tonnes are priced in the energy coal line, not the steelmaking coal line. D01 line 157: "Export sales only. Includes thermal coal sales from steelmaking coal mines." D02 line 218: "Includes energy coal sales from steelmaking coal mines." So hard coking coal is the right weight. BMA energy coal sales were 199 kt in the Jun 2025 quarter (D02 line 484) and 114 kt for YTD Mar FY25 (D01 line 419).
6. Calculation:
   - (193.82 × 17,507 − 200.12 × 12,676) / 4,831
   - = (3,393,206.74 − 2,536,721.12) / 4,831
   - = 856,485.62 / 4,831 = 177.2895, which rounds to 177.3
   - Cross-check: 193.82 − 6.30 × (12,676 / 4,831) = 193.82 − 16.5305 = 177.2895.
7. Test of the weighting method using BHP's own FY26 figures:
   - Hard coking coal weights: (200.25 × 12,572 + 232.88 × 5,522) / 18,094 = 210.208. This matches the reported FY26 price of 210.21 (D02 line 205).
   - The same method for H2 FY26: (226.76 × 3,842 + 232.88 × 5,522) / 9,364 = 230.369. This matches the reported 230.37.
   - Total BMA sales as weights instead gives FY26 = (200.25 × 12,737 + 232.88 × 5,905) / 18,642 = 210.59. That does not match 210.21, so total BMA sales is the wrong weight.
8. Sanity check: the Q4 FY26 price of 232.88 divided by 177.2895 is 1.314, consistent with the printed "v Q4 FY25 31%" (D02 line 205).

minimal_documents: D01 + D02, and both are needed. D01 is the only source of the YTD Mar FY25 price (200.12). D02 is the only source of the FY25 price (193.82). The volumes can come from either: D01 gives 12,676 + 4,831, and D02 gives 17,507 and 4,831, with the other figure derivable by subtraction. D03 and D04 (Freeport) do not mention coal, BHP or BMA, so they cannot replace either document.

readings:
- (a) Weighting by total BMA sales including energy coal (17,820 / 12,790 / 5,030 kt; D02 line 319, D01 line 258): (193.82 × 17,820 − 200.12 × 12,790) / 5,030 = 177.8007, or 177.8. I reject this because of the footnotes in step 5 and because it does not reproduce FY26's 210.21 (step 7).
- (b) Using the rounded percentage: 232.88 / 1.31 = 177.77, or 177.8. Allowing for rounding of the 31%, the range is about 177.1 to 178.5. The question rules this out with "without rounding intermediate values", and it is too imprecise for one decimal place.
- Note that both rejected readings give 177.8.

gaps:
- D03 and D04 were not read in full. I only searched them for steelmaking/coking/coal/BHP/BMA (no hits) and for "realized price" lines (Freeport copper, gold and molybdenum only).
- The packet has no PDFs (manifest method "text", pages null), so the italic "adjusted since previously reported" markers cannot be seen. The Jun 2025 quarter hard coking coal figure is identical in D01 and D02 and the totals reconcile, so no restatement is apparent.
- Prices are footnoted as "provisional, unaudited estimates".
- Per instructions I did not read question.txt in the packet.

contaminated: no
