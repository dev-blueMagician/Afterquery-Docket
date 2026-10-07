# q03 rev 0 blind solver A (2026-10-06)

Fresh blind-solver agent (scope hook), input: workspace root, solver-1 packet path, question
verbatim. Return copied verbatim.

answer: 31.31%

confidence: medium. Each input figure is quoted directly from the documents. However, no document states a single total for all credit unions, so I added the parts together. And footnote 6, which is attached to the bank count, is missing from both D05 files.

path:
1. Banks on September 30, 2005 (D05, text/D05.txt line 191; same text at docs/gaoreports_gao_06_387.txt line 189): "As of September 30, 2005, there were 1,846 federally chartered banks and 5,695 state-chartered banks.6" The same section calls this the "dual banking system" because banks can be "either federally or state-chartered." So the total is 1,846 + 5,695 = 7,541 banks.
2. Federally insured credit unions (D02, text/D02.txt line 231): "Almost all (98 percent) credit unions are federally insured. As of December 2002, 9,688 credit unions were federally insured…"
3. Credit unions without federal insurance (D02 line 1179, Appendix I): "As of December 2002, 214 state- chartered credit unions lacked federal deposit insurance, and all but two were privately insured." This agrees with line 233 ("As of December 2002, 212 credit unions… about 2 percent of all credit unions… chose to purchase private deposit insurance") and footnote 8 at line 239 ("we identified two uninsured credit unions, one was located in Idaho and the other was located in New Hampshire"). So 212 + 2 = 214.
4. Total credit unions at the end of 2002: 9,688 + 214 = 9,902. The report's own percentages back this up: 9,688 / 9,902 = 97.8%, matching "98 percent," and 212 / 9,902 = 2.1%, matching "about 2 percent."
5. Calculation: (9,902 − 7,541) / 7,541 = 2,361 / 7,541 = 0.313088, which is 31.31%. As a check, 7,541 × 0.3131 = 2,361.09, slightly above 2,361, so the result is just under 31.31% and rounds to 31.31.

minimal_documents: D02 + D05. No other document can stand in for either one. D02 is the only source of credit union counts. D05 is the only source with the September 30, 2005 bank count; "September 30, 2005" appears nowhere else. D03 mentions credit unions only as the National Credit Union Administration, with no counts. D01 (household goods moving), D04 (assisted living) and D06 (bankruptcy) are unrelated.

readings:
- If only insured credit unions are counted (9,688 federal + 212 private = 9,900, leaving out the 2 uninsured): 2,359 / 7,541 = **31.28%**.
- If the 9,688 federally insured figure is taken as "the number of credit unions": 2,147 / 7,541 = **28.47%**. This reading is weaker, because the document labels that figure "federally insured" and says that is only about 98% of all credit unions.
- For banks, I found no other defensible total. The "about 1,900 national banks" figure in D05 line 393 is a December 2004 number for national banks only, so it does not fit the date or scope.

gaps:
- Footnote 6 to the D05 bank-count sentence is missing from both text/D05.txt and docs/gaoreports_gao_06_387.txt; footnote text was stripped throughout that file. The manifest says the documents were extracted as text with no pages, and there is no PDF in the packet, so I could not check whether the footnote limits what "banks" covers (for example, whether savings institutions are left out).
- D02 never prints the 9,902 total, so it is derived. Its Figure 1 (privately insured credit unions by state) came through only as scattered numbers, but the text gives the 212 total directly, so the answer does not depend on the figure.
- Searches covered all six text/ files plus the docs/ copies of D02 and D05. I read D01, D04 and D06 only as far as their titles and keyword hits ("credit union" and "bank" in any capitalization, "September 30, 2005", and number patterns such as 9,9xx and 7,5xx), not their full text. I did not read question.txt.

contaminated: no
