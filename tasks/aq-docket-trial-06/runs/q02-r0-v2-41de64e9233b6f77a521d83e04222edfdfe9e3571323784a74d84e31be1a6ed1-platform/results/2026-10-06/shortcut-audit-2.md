# q01 rev 0 replacement shortcut audit (2026-10-06)

Fresh shortcut-auditor agent (scope hook), launched at the reviewer's request as one replacement
for the first audit's "ambiguous" record (kept as results/shortcut-audit.md). Input: workspace
root, shortcut packet path, question verbatim. Return copied verbatim.

**answer:** 2,361. The U.S. had 9,902 credit unions at the end of 2002 and 7,541 banks on September 30, 2005.

**verdict:** clear

**shortest_path:**
1. D02 (GAO-03-971), text/D02.txt line 231: "As of December 2002, 9,688 credit unions were federally insured". Line 233: "As of December 2002, 212 credit unions* about 2 percent of all credit unions* chose to purchase private deposit insurance." Footnote 8 at line 239: "we identified two uninsured credit unions, one was located in Idaho and the other was located in New Hampshire."
2. D02 Appendix I, line 1179, dates those two to December 2002: "As of December 2002, 214 state- chartered credit unions lacked federal deposit insurance, and all but two were privately insured." Line 231 adds that federally chartered credit unions "must be federally insured." So the two groups don't overlap and together cover every credit union. Total = 9,688 + 214 = 9,902. This fits the "98 percent" (97.8%) and "about 2 percent" (2.2%) statements. The Figure 1 state counts (3, 5, 8, 20, 21, 22, 40, 93) add up to 212, which also checks out.
3. D05 (GAO-06-387), text/D05.txt line 191: "As of September 30, 2005, there were 1,846 federally chartered banks and 5,695 state-chartered banks." Total = 1,846 + 5,695 = 7,541.
4. 9,902 − 7,541 = **2,361**.

**sufficient_documents:** D02 and D05 together, and both are needed. D02 is the only document with credit union counts; D03 mentions the National Credit Union Administration only as a regulator. D05 is the only document with the September 30, 2005 bank count. Neither document alone answers the question, and no other document duplicates either input. Within D02, the 214 figure (line 1179) can be swapped for 212 + 2 (lines 233 and 239).

**searches:**
- Terms used: "credit union(s)" with numbers in front; "September 30, 2005", "September 2005", "third quarter of 2005", "2005"; "December 2002", "December 31, 2002", "end of 2002"; "uninsured", "all credit unions", "number of credit unions"; "1,846", "5,695", "7,5xx", "7,541"; numbers followed by banks/thrifts/institutions; "number of banks", "all banks", "nation's banks"; OCR-spaced numbers like "1, 462"; "10,xxx", "thousand", "approximately".
- Inspected: manifest.json; D02 lines 140–259 and 1170–1194; D05 lines 170–249; the D04 header; grep hits in D01, D03 and D06.
- Topics of the unrelated documents:
  - D01: household-goods arbitration under the ICC Termination Act
  - D03: predatory lending
  - D04: assisted living
  - D06: bankruptcy and child support
- I also checked that the key D02 and D05 passages match the source files in docs/.
- No question files, notes, gold answers or author reasoning came up, so the packet is not contaminated.

**readings/gaps:**
- **2,359** (9,900 − 7,541): counts only federally and privately insured credit unions and leaves out the two uninsured ones. This is the most likely trap. It's weaker because D02 line 1179 explicitly dates the two uninsured credit unions to December 2002.
- **2,147** (9,688 − 7,541): counts only federally insured credit unions. The question asks for all credit unions, so this doesn't fit.
- **Bank scope:** D05 footnote 6, which is attached to the bank-count sentence, is missing from both the text extraction and the docs/ source. It might say what "banks" covers (for example, whether thrifts are included). It probably wouldn't change the sum, because the question uses D05's own wording and date. D05 line 393 ("about 1,900 national banks") is approximate and from a different period, so I didn't use it.
- **Difficulty risk:** once both inputs are found, this is a simple cross-document subtraction, which the rules allow. The real difficulty is building the 2002 credit union total from three pieces in different parts of D02.

Relevant files:
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q01-r0-v2-41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1\shortcut\text\D02.txt
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q01-r0-v2-41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1\shortcut\text\D05.txt
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q01-r0-v2-41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1\shortcut\docs\gaoreports_gao_03_971.txt
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q01-r0-v2-41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1\shortcut\docs\gaoreports_gao_06_387.txt
