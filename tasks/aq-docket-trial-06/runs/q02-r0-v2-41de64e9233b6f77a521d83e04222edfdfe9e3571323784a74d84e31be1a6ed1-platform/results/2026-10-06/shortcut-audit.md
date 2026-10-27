# q01 rev 0 shortcut audit (2026-10-06)

Fresh shortcut-auditor agent (scope hook), input: workspace root, shortcut packet path, question
verbatim. Return copied verbatim.

answer: **2,361** if "credit unions" means all US credit unions, which is my preferred reading (9,902 − 7,541). If it means only federally insured credit unions, the answer is **2,147** (9,688 − 7,541).

verdict: ambiguous

The question needs two documents and a simple subtraction, and I found no shortcut. I didn't mark it "clear" because the credit-union count has two defensible readings that give different answers.

shortest_path:
1. Banks on September 30, 2005 come from D05 (GAO-06-387), line 191: "As of September 30, 2005, there were 1,846 federally chartered banks and 5,695 state-chartered banks." Adding them gives 1,846 + 5,695 = **7,541**.
2. Credit unions at the end of 2002 come from D02 (GAO-03-971):
   - Line 231: "Almost all (98 percent) credit unions are federally insured. As of December 2002, 9,688 credit unions were federally insured."
   - Line 233: "As of December 2002, 212 credit unions* about 2 percent of all credit unions* chose to purchase private deposit insurance."
   - Line 239, footnote 8: "we identified two uninsured credit unions, one was located in Idaho and the other was located in New Hampshire."
   - Line 1179: "As of December 2002, 214 state- chartered credit unions lacked federal deposit insurance, and all but two were privately insured."
   - The total is 9,688 + 214 (that is, 212 + 2) = **9,902**. The report's percentages fit this total: 9,688 / 9,902 is 97.8%, matching "98 percent", and 212 / 9,902 is 2.1%, matching "about 2 percent".
3. The difference is 9,902 − 7,541 = **2,361**.

The question asks how many credit unions "the United States" had. D02 itself says 9,688 is only the federally insured 98%, and it gives the remaining 214. That is why I prefer the full total.

sufficient_documents: D02 and D05 together. Both are needed, and there is no alternative source. No other packet document gives a credit-union count or a September 30, 2005 bank count, and no single document covers both. The answer isn't given away by the wording. The only route is an ordinary cross-document subtraction, so it is easy, but it is not a shortcut.

searches:
- **Terms used:** "September 30, 2005"; "end of 2002", "December 31, 2002", "year-end 2002", "in 2002"; "credit union" (counts by file); number patterns before "credit unions", "banks", "institutions" and "thrifts", including OCR-spaced commas like "1, 462"; "privately insured", "uninsured", "lacked federal deposit insurance"; candidate totals (9,9xx, 9,6xx, 10,0xx, "about 10,000"); "7,541", "1,846", "5,695"; "thrift", "savings institutions", "commercial banks", "Quarterly Banking Profile", "Statistics on Depository".
- **Coverage:**
  - All six text files were searched. "Credit union" appears only in D02 (159 hits) and D03 (3 hits, none with counts).
  - D01 (household goods movers), D04 (assisted living) and D06 (bankruptcy and child support) are off-topic; I checked their titles.
  - The only other bank count is D05 line 393, "about 1,900 national banks", which refers to December 2004 and isn't relevant.
  - I checked the key D02 and D05 figures against the original files in docs/; they match.
- **Not read:** the question.txt in the packet root, per the rules. No notes, other packets or outside material were used, so there is no contamination.

readings/gaps:
- **Alternative answers:**
  - **2,147:** uses only the headline "9,688 credit unions" figure (federally insured). This is a plausible intended answer if the question writer took that figure at face value.
  - **2,359:** counts federally and privately insured credit unions but leaves out the two uninsured ones (9,900 − 7,541).
  - Reading "banks" as federally chartered banks only doesn't fit the question; the D05 sentence describes the whole dual (federal and state) banking system.
- **Gaps:**
  - Footnote 6 of D05, which may define what "banks" covers at line 191 (for example, whether savings institutions are excluded), is missing from both the text/ and docs/ versions. The question's word "banks" matches the document's sentence, so I kept 7,541.
  - The two uninsured credit unions were "identified through our discussions with state regulators," so that count may not be exhaustive. Line 1179 does state the 214 figure as a December 2002 fact.

Files used:
- `D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q01-r0-v2-41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1\shortcut\text\D02.txt`
- `D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q01-r0-v2-41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1\shortcut\text\D05.txt`
- `D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q01-r0-v2-41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1\shortcut\docs\gaoreports_gao_03_971.txt`
- `D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q01-r0-v2-41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1\shortcut\docs\gaoreports_gao_06_387.txt`
