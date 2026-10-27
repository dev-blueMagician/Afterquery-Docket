# i02 blind solve 3 (fresh blind-solver, 2026-10-18) - judged RIGHT

Raw return, verbatim:

answer: 70%

confidence: high

path:
1. April 2005 testimony = D02 (GAO-05-532T), header "DATE: 04/14/2005" / "Thursday, April 14, 2005" (text/D02.txt lines 13, 45). It states the figure three times, consistently:
   - line 67: "under the regulation, management, and oversight of about 40 FEMA employees assisted by about 170 contractor employees."
   - line 119: "The private sector effort is regulated, managed, and overseen by about 40 FEMA employees with the assistance of about 170 contractor employees."
   - line 170: "according to a FEMA official, about 40 FEMA employees are responsible for regulating, managing, and overseeing the program ... FEMA is assisted in this effort by about 170 contractor employees."
   (Line 84's "approximately 2,500 staff" is all of FEMA on joining DHS, not NFIP staff, so excluded.)
2. December 2007 report = D09 (GAO-08-28), header "(28-DEC-07, GAO-08-28)" / "DATE: 12/28/2007" (lines 5, 11). Line 187 (Background): "As of September 2007, FEMA had about 68 employees, assisted by about 170 contractor employees, to manage and oversee the NFIP and the National Flood Insurance Fund".
3. Cross-checked in the originals under docs/: gaoreports_gao_05_532t.txt "about 40 FEMA employees" (lines 65, 117, 168); gaoreports_gao_08_28.txt "about 68 employees" (line 185). Identical to text/.
4. "FEMA's own employees" excludes the contractor employees (about 170 in both). (68 − 40) / 40 = 28 / 40 = 0.70 = exactly 70%; no rounding needed.

minimal_documents: D02 + D09. No alternatives: only these two mention NFIP or flood insurance at all (search counts D02 = 66, D09 = 79, all others 0), and no other document gives either staffing figure.

readings:
- Including contractors in both years: (68 + 170) − (40 + 170) = 28; 28 / 210 = 13.3% ≈ 13%. Contradicts "FEMA's own employees", so rejected.
- Using the later figure as the base: 28 / 68 = 41%. Not a standard "grew from X to Y" calculation, so rejected.
- Date reading: D09's figure is "As of September 2007" but appears in the December 2007 report, matching the question's wording; it does not change the answer.
- Primary answer: 70%.

gaps:
- Both figures are approximate ("about 40", "about 68"); the 2005 figure is credited to "a FEMA official". These hedges do not change the calculation.
- Plain-text sources (manifest method "text", no PDFs), so no PDF page to inspect and no extraction problems.
- Coverage: D02 and D09 not read in full. Read: headers and summary sections, D02 background/footnote area, the D02 section "Private Insurers Sell, Service, and Adjust Claims under FEMA Management and Oversight", D09 Background (lines 150–194). The rest of both was searched for employees, staff, staffed, personnel, workforce, people, FTE, full-time, headcount, human capital, contractor/FEMA/NFIP/program staff, and numeric "N employees/staff" patterns; in D09 the only real hits were line 162 (insurance company staff adjusters, irrelevant) and line 187.
- D01, D03–D08 (toy guns, alternative mortgages, OCC consumer assistance, insurance-sector preparedness, bankruptcy credit counseling, long-term care insurance, fair lending) checked only by title, date and keyword search; their one staffing hit, D04's "49 staff", is in the OCC report.

contaminated: no. The packet root has a question.txt, not read; only the question as given was used; no answer, reasoning or source hint leaked.
