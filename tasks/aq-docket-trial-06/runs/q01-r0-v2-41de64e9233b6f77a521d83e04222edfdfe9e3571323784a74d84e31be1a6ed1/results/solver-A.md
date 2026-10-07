# q01 rev 0 blind solver A (2026-10-06)

Fresh blind-solver agent (scope hook), input: workspace root, solver-1 packet path, question
verbatim. Return copied verbatim.

I found a direct figure for each side of the subtraction, but credit unions aren't given as a single total. The answer depends on whether two uninsured credit unions, which have no date attached, count toward the end-of-2002 total.

answer: 2,361 (9,902 credit unions at end of 2002 minus 7,541 banks on September 30, 2005). If the two undated uninsured credit unions are left out, the answer is 2,359.

confidence: medium

path:
1. **Banks on September 30, 2005** (D05, GAO-06-387, text/D05.txt line 191): "As of September 30, 2005, there were 1,846 federally chartered banks and 5,695 state-chartered banks." 1,846 + 5,695 = 7,541. This is the only bank count tied to that date anywhere in the packet. D05 line 393 also says "about 1,900 national banks", but that is approximate, has no date and covers only national banks, so I didn't use it.
2. **Federally insured credit unions, end of 2002** (D02, GAO-03-971, text/D02.txt line 231): "As of December 2002, 9,688 credit unions were federally insured". The same passage says "Almost all (98 percent) credit unions are federally insured", so 9,688 is not the total.
3. **Privately insured credit unions** (D02 line 233): "As of December 2002, 212 credit unions—about 2 percent of all credit unions—chose to purchase private deposit insurance." The state values in Figure 1 (93, 40, 22, 21, 20, 8, 5, 3) add up to 212, which confirms the figure. Members (81M + 1.1M) and deposits ($483B + $10.8B) match the report's "a little over 1 percent" and "2 percent" shares, so the 212 are separate from the 9,688.
4. **Uninsured credit unions** (D02 line 239, footnote 8): "Through our discussions with state regulators, we identified two uninsured credit unions, one was located in Idaho and the other was located in New Hampshire." Uninsured means they belong to neither group above. No date is given; GAO did this work between February and August 2003 (line 167).
5. **Total credit unions:** 9,688 + 212 + 2 = 9,902. The shares check out: 9,688 / 9,902 ≈ 97.8% (the report's "98 percent") and 212 / 9,902 ≈ 2.1%.
6. **Difference:** 9,902 − 7,541 = 2,361.
   - Excluding the two uninsured: 9,900 − 7,541 = 2,359.
   - Federally insured only: 9,688 − 7,541 = 2,147.

   I rechecked each sum and subtraction.

minimal_documents: D02 + D05. I found no substitutes:
- Credit unions are mentioned only in D02 and D03, and D03's three mentions contain no counts.
- The date September 30, 2005 and the bank figures 1,846 and 5,695 appear only in D05.

readings:
- **(a) Only credit unions explicitly dated December 2002** (federally plus privately insured): 9,900 − 7,541 = **2,359**. This is defensible because the two uninsured credit unions were found in 2003 conversations and carry no date. The report's own split (98% federally insured, about 2% privately insured) also treats "all credit unions" as roughly the insured ones.
- **(b) "Credit unions" taken to mean the 9,688 federally insured figure:** **2,147**. This is weaker, because the report itself says 9,688 is only about 98% of all credit unions.
- **Main answer: 2,361.** It counts all three groups the report identifies, on the view that uninsured credit unions are still credit unions.

The only thing separating 2,361 from 2,359 is the two credit unions in footnote 8 that have no date.

gaps:
- **Missing date:** footnote 8 doesn't give a date for the two uninsured credit unions.
- **Missing footnote:** D05 footnote 6, which would give the source and definition behind the bank counts (for example, whether thrifts are excluded), is missing. It's absent from both text/D05.txt and docs/gaoreports_gao_06_387.txt, and the packet has no PDF or layout file to check.
- **Garbled figure:** D02's Figure 1 came through garbled, but its numbers still add up to the 212 stated in the text.
- **Unread coverage:**
  - I did not read D01, D04 or D06 in full. Searches across all six documents for "credit union", "NCUA", "National Credit Union", "September 30, 2005", "September 2005" and four-digit counts of banks or institutions found nothing relevant in them.
  - In D03, I read only the passages that mention credit unions.
  - In D02 and D05, I read the background, scope and methodology, and end sections, plus targeted passages.

contaminated: no. I received only the workspace root, packet path and question, and read only files inside the packet's text/ and docs/ folders.

Relevant files:
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q01-r0-v2-41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1\solver-1\text\D02.txt
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q01-r0-v2-41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1\solver-1\text\D05.txt
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q01-r0-v2-41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1\solver-1\text\manifest.json
