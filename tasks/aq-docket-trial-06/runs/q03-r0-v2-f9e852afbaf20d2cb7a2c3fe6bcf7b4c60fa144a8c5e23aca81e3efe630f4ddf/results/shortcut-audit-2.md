# q03 rev 0 replacement shortcut audit (2026-10-06)

Fresh shortcut-auditor agent (scope hook), launched at the rev 0 reviewer's request as one
replacement for the first audit's "ambiguous" record (kept as results/shortcut-audit.md). Input:
workspace root, shortcut packet path, question verbatim. Return copied verbatim. (Caller note: the
auditor's own answer is the 9,900 route; its searches for "uninsured credit union" cannot reach D02
text line 1179, which says "lacked federal deposit insurance, and all but two were privately
insured" without the word "uninsured".)

answer: **31.28%**. At the end of 2002 there were 9,900 U.S. credit unions and on September 30, 2005 there were 7,541 U.S. banks, so (9,900 − 7,541) / 7,541 = 2,359 / 7,541 = 0.312823, which is 31.28%.

verdict: clear

shortest_path:
1. D02 (GAO-03-971), text/D02.txt line 231: "Almost all (98 percent) credit unions are federally insured. As of December 2002, 9,688 credit unions were federally insured…"
2. D02, line 233: "As of December 2002, 212 credit unions* about 2 percent of all credit unions* chose to purchase private deposit insurance." The state table at line 469 ("Total 212 78 39 50") confirms 212.
   - Total credit unions: 9,688 + 212 = 9,900. This matches the document's own split of 98% federally insured plus 2% privately insured.
3. D05 (GAO-06-387), text/D05.txt line 191: "As of September 30, 2005, there were 1,846 federally chartered banks and 5,695 state-chartered banks."
   - Total banks: 1,846 + 5,695 = 7,541.
4. Calculation: 2,359 / 7,541 = 0.31282 = 31.28%.

The answer needs both documents: D02 has the 2002 credit union inputs and D05 has the 2005 bank inputs. Neither states the other's figure, and no document gives either total or the percentage, so this is not a shortcut. The difficulty risk is that it's easy: two sums within each document and one ratio across them.

sufficient_documents: D02 + D05, both required. There is no single-document alternative and no duplicated evidence that could replace either one. D01 (household goods moving), D04 (assisted living) and D06 (bankruptcy and child support) are irrelevant. D03 (predatory lending) mentions credit unions and banks only by regulator name, with no counts.

searches:
- **Literal terms:** "September 30, 2005", "credit unions" with numeric prefixes, bank counts by charter type, the totals 9,900, 9,902 and 7,541 (none appear anywhere), "all credit unions", "number of credit unions", "uninsured credit union", "Sept.", "September 2005", "third quarter".
- **Other bank figures checked:** every 4–5 digit number across D01–D06. None is a competing bank count. "About 1,900 national banks" (D05 line 393) is a December 2004 figure for OCC's national banks only, not total banks. The 3,163 / 1,884 / 1,279 figures (D05 line 641) are charter changes from 1990 to 2004.
- **Cross-checks:** the key D02 and D05 passages match the original docs/ files.
- **Coverage:** I read the manifest, the key passages in D02, D03 and D05, and the headers of D01 and D04; D06 was seen only at lines 99–106. I did not open question.txt or anything outside docs/ and text/. Nothing was contaminated.

readings/gaps:
- **31.31%:** D02 footnote 8 (line 239) mentions "two uninsured credit unions" (one in Idaho, one in New Hampshire). Adding them gives 9,902, and 2,361 / 7,541 = 31.31%. I rejected this because the footnote gives no date (it comes from a 2003 state-regulator survey). Only the 9,688 and 212 figures are dated December 2002, and the document's 98% plus 2% framing treats those two groups as all credit unions. This is a minor risk.
- **28.47%:** using only the 9,688 federally insured credit unions gives 2,147 / 7,541 = 28.47%. This is a weaker misreading, because the question asks for all U.S. credit unions and D02 explicitly counts the 212 privately insured ones separately.
- **Bank count:** D05 offers no other bank total for that date, so 7,541 is the only defensible figure.
- **Extraction gaps:**
  - D05's footnotes, including footnote 6 on the source of the bank counts, are missing from both the text and the original. It might define the bank universe (for example, whether thrifts are excluded), but it couldn't change the stated counts.
  - D02's Figure 1 is a graphic and comes through garbled, but its total is covered by the table at line 469.

Files used:
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q03-r0-v2-f9e852afbaf20d2cb7a2c3fe6bcf7b4c60fa144a8c5e23aca81e3efe630f4ddf\shortcut\text\D02.txt
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q03-r0-v2-f9e852afbaf20d2cb7a2c3fe6bcf7b4c60fa144a8c5e23aca81e3efe630f4ddf\shortcut\text\D05.txt
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q03-r0-v2-f9e852afbaf20d2cb7a2c3fe6bcf7b4c60fa144a8c5e23aca81e3efe630f4ddf\shortcut\text\manifest.json
