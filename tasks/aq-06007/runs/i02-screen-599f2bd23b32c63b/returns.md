# i02 strong-solver screen: raw returns (2026-10-16)

Three fresh blind-solver contexts (claude-opus-5-5, effort max), each given only the workspace root,
the packet path runs/i02-screen-599f2bd23b32c63b/solver-1 and the exact sentence. Gold: $9.2 billion.
Returns kept verbatim in substance (harness indentation removed).

## Solve 1: $9.2 billion (right), confidence high

answer: $9.2 billion. At $184,000 of gross value added per driver, the projected 2029 shortfall (78,000 drivers) would cost about $9.2 billion more in output than the 2024 shortfall in the IRU study behind that projection (28,000 drivers).
confidence: high
path:
1. The per-driver value comes from D02, the National Heavy Vehicle Regulator (NHVR) submission of 15 December 2025. Line 10 says "The National Heavy Vehicle Regulator (NHVR) is grateful…". Line 491 says "With each heavy vehicle driver contributing an estimated $184,000[fn14] in Gross Value Added (GVA)[fn15]". The extracted text runs the footnote numbers into the figures, so it reads "$184,00014". Footnote 14 is on line 501, so the figure is $184,000.
2. The 2029 projection is also in D02. Line 493 says "This driver shortfall is projected to rise to 78,000[fn16] by 2029, constraining an estimated $14.4 billion". Footnote 16, on line 504, names the source study: "International Road Transport Union (2024), 2024 Global Truck Driver Shortage Report."
3. The 2024 shortfall in that same IRU study comes from D10, the ALRTA submission.
   - Line 782: "The 2024 Global Truck Driver Shortage Report… estimates that Australia has over 28,000 unfilled truck-driver positions today, with the shortfall projected to reach 78,000 by 2029". Footnote 89, on line 793, cites the IRU 2024 Global Truck Driver Shortage Report.
   - Line 360: "NatRoad, drawing on the 2024 Global Truck Driver Shortage Report by the International Road Transport Union (IRU), reports that in Australia… there were around 28,000 unfilled truck driving positions, projected to rise to over 78,000 by 2029 as more than 50,000 drivers retire." Footnote 41 is on line 370.
   - Two other documents give the same 28,000: D05 (ALC) line 73: "In 2024, around 28,000 truck driver positions remained unfilled". Footnote 11 is an iru.org newsroom page about a new IRU report. D15 (ARA and NRA) line 50: "around 28,000… currently unfilled[4]… approximately 78,000 vacancies by 2029[5]". Footnote 5 cites NatRoad "citing IRU Global Driver Shortage analysis".
4. NHVR's own "current shortage of 26,000" (D02 line 490) is a different source. Its footnote 10, on line 495, cites "NatRoad (2024), Truck driver shortage: Australia in the global context", not the IRU study. The question asks for the 2024 figure "in the study behind that projection", so I did not use 26,000.
5. Calculation: (78,000 − 28,000) × $184,000 = 50,000 × $184,000 = $9,200,000,000, which is $9.2 billion. Check by computing each side first: 78,000 × 184,000 = $14.352 billion, and 28,000 × 184,000 = $5.152 billion. The difference is $9.2 billion. The $184,000 reading is confirmed by NHVR's own totals: 26,000 × 184,000 = $4.784 billion, which matches its "nearly $4.8 billion". 78,000 × 184,000 = $14.352 billion, which matches its "$14.4 billion".
minimal_documents: D02 + D10. Two weaker alternatives would also work: D02 + D15 (it ties 28,000 to the IRU study less directly, through NatRoad); D02 + D05 (the 28,000 is footnoted to an IRU report page, but D05 does not name the 2024 Global Truck Driver Shortage Report or give the 78,000 figure). The $184,000 figure appears only in D02, so D02 is needed in every case.
readings:
- If the 2024 baseline is NHVR's 26,000 (from NatRoad), the answer is (78,000 − 26,000) × $184,000 = $9.568 billion, which rounds to $9.6 billion. Subtracting NHVR's printed totals gives the same: $14.4 billion − $4.8 billion = $9.6 billion. I rejected this because the question points to the IRU study's 2024 figure.
- D10 line 360 says "over 78,000" and line 782 says "over 28,000". These are lower bounds, but the documents give no more precise numbers, so I used 28,000 and 78,000.
- D07 (Ai Group) projects "70,000 vacancies by 2030" (line 83). That is a different year and source, so it does not apply.
gaps: The packet has no PDFs or layout files; all 16 documents are plain text. The only extraction problem was footnote numbers running into figures ("$184,00014", "78,00016"). Footnotes 14 and 16 and the arithmetic check above resolve it. I did not read the IRU report itself, which is outside the packet. Coverage: searched all 16 text files for 2029, GVA/value added, 26,000/28,000/78,000, IRU/Global Truck Driver, 184/per driver/economic output, and unfilled/vacancy/shortfall/shortage. Read D02 L1-60 and 440-519; D05 L60-104; D07 L78-95; D10 L1-20, 350-379, 430-441 and 770-799; D14 L90-97; D15 L1-70. None of D01, D03, D04, D06, D08, D09, D11, D12, D13 or D16 apart from search hits. The packet also contains a question.txt, which I deliberately did not open.
contaminated: no

## Solve 2: $9.2 billion (right), confidence high

answer: $9.2 billion. The 2029 shortfall of 78,000 drivers minus the IRU study's 2024 shortfall of 28,000 drivers leaves 50,000 drivers. 50,000 × $184,000 = $9,200,000,000.
confidence: high
path:
1. The regulator's value-added figure is in D02, the NHVR submission (D02 line 10). Line 491 says: "With each heavy vehicle driver contributing an estimated $184,000[fn14] in Gross Value Added (GVA)". No other document gives a per-driver value-added figure. I searched all D01–D16 for "gross value added|GVA|184|value added|per driver".
2. The 2029 projection is at D02 line 493: "This driver shortfall is projected to rise to 78,000[fn16] by 2029, constraining an estimated $14.4 billion". Footnote 16 is at line 504: "International Road Transport Union (2024), 2024 Global Truck Driver Shortage Report." That report is the study behind the projection.
3. Other documents give the IRU study's 2024 shortfall as 28,000: D10 line 360 (IRU via NatRoad, "around 28,000 unfilled truck driving positions, projected to rise to over 78,000 by 2029", fn 41 line 370 "IRU's 2024 Global Truck Driver Shortage Report"); D10 line 782 ("over 28,000 ... today ... reach 78,000 by 2029", fn 89 "International Road Transport Union (IRU) 2024"); D05 line 73 ("In 2024, around 28,000", fn 11 IRU newsroom link); D15 line 50 (28,000 [fn 4 NatRoad, Global Driver Shortage Report 2024] and 78,000 by 2029 [fn 5 citing IRU]).
4. The NHVR's own current figure comes from a different source. D02 line 481 says "an estimated 26,000 driver positions currently unfilled[10]", and footnote 10 is "NatRoad (2024), Truck driver shortage: Australia in the global context". Line 490 repeats "The current shortage of 26,000", and the NHVR prices it at "nearly $4.8 billion". That figure is not from the IRU study, so it is not the 2024 shortfall the question asks for.
5. Calculation: 2029: 78,000 × $184,000 = $14.352bn; 2024 (IRU): 28,000 × $184,000 = $5.152bn; difference $9.200bn, which rounds to $9.2bn.
minimal_documents: D02 + D10. D02 cannot be replaced (only source for $184,000, the regulator's identity and the footnote naming the IRU study). D05 can replace D10 ("In 2024" with an IRU citation). D15 is a weaker replacement ("currently" in a December 2025 submission; its 28,000 footnote names a NatRoad report).
readings:
- NHVR's own baseline of 26,000 (NatRoad): (78,000 − 26,000) × $184,000 = $9.568bn, about $9.6bn; printed totals $14.4bn − $4.8bn = $9.6bn. Rejected: ignores "the study behind that projection".
- D10 "over 78,000" and "over 28,000": point estimates elsewhere; no change at one decimal place.
- D07 line 83 "70,000 vacancies by 2030": different year, not linked to the IRU study.
gaps: The IRU report itself is not in the packet; its 2024 Australian figure (about 28,000) comes only from secondary summaries in D10, D05 and D15, hedged "around" or "over". All documents are text extractions; D02's Figure 5 chart is garbled but irrelevant. Regex searches across all 16 documents for GVA/gross value added, 2029, shortfall/unfilled/vacanc/driver shortage, 184, IRU/Road Transport Union, 26,000/28,000/78,000/70,000, value added/economic output/per driver. Read D15 in full; D02 L1-30 and 420-514; D05 L60-79 and 89-94; D07 L80-95; D10 L340-370, 434-437 and 782-795; D14 L90-97.
contaminated: no. I did not read question.txt, notes or any other packet.

## Solve 3: $9.2 billion (right), confidence high

answer: $9.2 billion
confidence: high
path:
1. The GVA estimate is from the NHVR (D02 line 10). D02 line 491: "With each heavy vehicle driver contributing an estimated $184,000[fn14] in Gross Value Added (GVA)[fn15], the current shortfall is constraining nearly $4.8 billion in economic output." The extracted text runs the footnote number into the figure ("$184,00014"); docs/...sub004...txt line 489 has the same text. A search for "gross value|GVA|value added" across all 16 files only found D02.
2. D02 line 493: "This driver shortfall is projected to rise to 78,000[fn16] by 2029, constraining an estimated $14.4 billion in economic output." Footnote 16 (line 504): "International Road Transport Union (2024), 2024 Global Truck Driver Shortage Report." So the study behind the projection is the IRU 2024 report.
3. NHVR's own "current" shortage of 26,000 does not come from that study: D02 line 481 "an estimated 26,000 driver positions currently unfilled[fn10]", footnote 10 (line 495) "NatRoad (2024), Truck driver shortage: Australia in the global context".
4. The IRU study's 2024 shortfall is 28,000: D10 line 360 (fn 41, line 370, "summarising IRU's 2024 Global Truck Driver Shortage Report"); D10 line 782 (fn 89 IRU 2024); D05 line 73 ("In 2024, around 28,000", fn 11 iru.org "new-iru-report"); D15 line 50 (28,000; 78,000 by 2029).
5. Calculation: 78,000 − 28,000 = 50,000 drivers; 50,000 × $184,000 = $9,200,000,000 = $9.2 billion. Check: 78,000 × 184,000 = $14.352bn (D02's $14.4bn); 28,000 × 184,000 = $5.152bn; difference $9.2bn.
minimal_documents: D02 + D10. D05 can replace D10 (weaker: "In 2024, around 28,000" with an IRU report URL, no 78,000). D15 weaker (footnotes credit NatRoad citing IRU).
readings:
- NHVR's own current shortage of 26,000 instead of the IRU study's 2024 figure: $9.568bn, about $9.6 billion; D02's printed totals $14.4bn − $4.8bn = $9.6bn. Ruled out by "the 2024 shortfall in the study behind that projection" (26,000 is NatRoad's).
- "over 78,000" / "over 28,000": the gap stays 50,000; $9.2bn.
- D07 "70,000 vacancies by 2030": different year and source.
gaps: IRU report not in the packet; 28,000 from summaries (D10, D05, D15). Text-method sources, no PDFs. Searched all 16 files for shortage/shortfall, GVA/gross value/value added, 2029, unfilled, vacanc, 26,000, 28,000, 78,000, 184,000, IRU/Road Transport Union, per driver, each driver. Read the relevant passages in full in D02, D04, D05, D07, D10, D14 and D15; not D01, D03, D06, D08, D09, D11, D12, D13 or D16 beyond search hits. Did not open question.txt.
contaminated: no
