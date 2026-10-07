# Removal probes, round 1 (2026-10-06)

Each probe is a fresh blind-solver agent under the scope hook, given only the workspace root, a
packet that is a byte copy of q01 rev 0's solver-1 packet with one document removed (bound to the
read guard as its own run), the question verbatim, and an instruction to answer from the packet
or commit to a forced guess with its probability. It approximates the platform's document check
(high model re-solves with each marked document left out). Sketch-stage evidence, not final
check records. Returns copied verbatim. Process note: the folder names ("removal-noD02") were
visible to the probe, which inferred that a document had been removed; later probes use neutral
folder names.

## q01 rev 0 without D02 (runs/q01-r0-removal-noD02/solver-1)

answer: The packet does not settle this. It gives the bank figure, 7,541 banks on September 30, 2005, but no document states how many credit unions the US had at the end of 2002. My forced best guess is **2,147** (9,688 − 7,541). The probability that it is exactly right is about 35%.

confidence: high that the packet can't answer it. Low for the forced guess.

path:
1. Banks on Sept 30, 2005. D05 (GAO-06-387, OCC Preemption Rules, April 2006), text/D05.txt line 191, Background section: "As of September 30, 2005, there were 1,846 federally chartered banks and 5,695 state-chartered banks." 1,846 + 5,695 = **7,541**.
2. Credit unions at end of 2002: no figure anywhere in the packet. A search allowing for line breaks (`credit\s+union`, `credit.?union`, `CUs`, "share insurance", NCUSIF) across all of text/ and docs/ finds only three mentions, all in D03 (GAO-04-412T, predatory lending testimony; text lines 107, 111, 171). All three name the "National Credit Union Administration" as a regulator. None gives a count.
3. Year-end 2002 mentions elsewhere don't help. D04 (lines 7, 77, 173) says "In 2002, over 36,000 assisted living facilities served approximately 900,000 residents", which is a different topic. D03 line 149 mentions 2002 HMDA rule changes. No other count-sized figures relate to credit unions: D03 has 8,712 borrowers, and D05's 8,866 is in an OCC assessment-schedule table (text lines 727, 756).
4. Forced guess (not from the packet): I recall from memory, outside the documents, that NCUA reported 9,688 federally insured credit unions at year-end 2002. 9,688 − 7,541 = **2,147**.
   - Probability about 35%. I'm only moderately sure the 9,688 recollection is right.
   - Separately, the document the question was built from might have used a rounded figure (e.g., "about 9,700") or a different scope (e.g., including privately insured credit unions).
   - The packet folder's name ("removal-noD02") suggests a document D02 was removed, which may be where the figure was.

minimal_documents: D05 is enough for the bank count, and nothing in the packet could replace it. No packet document supplies the credit-union count, so no set of documents here answers the question.

readings:
- "Banks" could mean only one charter type. Federally chartered alone (1,846) or state-chartered alone (5,695) would change the subtraction. But the question says "banks", and D05 presents the two figures together as the dual banking system, so 7,541 is the natural reading.
- The credit-union figure is the bigger uncertainty. If the source said "about 9,700", the answer would be 2,159. If it counted all credit unions, including privately insured ones, the answer would be higher, roughly 2,400 or more.
- "About 1,900 national banks" (D05 line 393) is not dated September 30, 2005, so it isn't a substitute.

gaps:
- The credit union count at the end of 2002 is missing.
- D05's footnote 6, which presumably gives the source of the bank counts, is absent from both text/D05.txt and docs/gaoreports_gao_06_387.txt.
- All sources are plain text (method "text", pages null). There are no PDFs or Dnn.layout.txt files, so I couldn't check original pages, charts or footnotes.
- Coverage: I read D05 lines 150–259, 343–437, 535–546 and 660–681, D03 lines 100–179 and 205–226, and the opening 40 lines of D01 (household goods moving) and D06 (bankruptcy/child support). Everything else was covered only by searches for credit-union terms, comma-formatted numbers, and the "September 30, 2005" and 2002 dates. I did not read every line, but D01, D04 and D06 are on unrelated topics.

contaminated: no. The packet contains question.txt, which I did not open. One search over the whole packet folder counted a single "credit union" match in that file, but no content was shown. The 9,688 figure behind the forced guess comes from my own background memory, not from any leak or hint.

Result: gold 2,361 not reached; forced guess = decoy 2,147 (p 0.35). D02 needed in practice.

## q01 rev 0 without D05 (runs/q01-r0-removal-noD05/solver-1)

**answer:** The packet doesn't settle this. It gives the credit-union count for the end of 2002 (9,900) but has no count of U.S. banks on September 30, 2005. Forced best guess: **about 2,350 more credit unions** (9,900 minus about 7,550 commercial banks). The chance that this exact number is right is about 1%.

**confidence:** high that the packet can't answer it; low for the guess.

**path:**
1. Credit unions, D02 (GAO-03-971, August 2003), `text\D02.txt` line 231: "As of December 2002, 9,688 credit unions were federally insured, with about 81 million members and $483 billion in deposits." The same line says: "Almost all (98 percent) credit unions are federally insured."
2. D02 line 233: "As of December 2002, 212 credit unions* about 2 percent of all credit unions* chose to purchase private deposit insurance." Line 469 confirms the total: "Total 212".
3. D02 line 239, footnote 8: "we identified two uninsured credit unions, one was located in Idaho and the other was located in New Hampshire." This statement has no date.
4. Total credit unions at the end of 2002: 9,688 + 212 = 9,900. This matches the document's own percentages: 9,688 / 9,900 = 97.9% ("98 percent"), and 212 / 9,900 = 2.1% ("about 2 percent"). The packet gives no single printed total.
5. Banks on September 30, 2005: no document has this figure.
   - Neither "September 30", "Sept. 30" nor "third quarter" appears in any `text\` or `docs\` file.
   - The only "2005" hits are in D01 (a study planned for fiscal years 2003–2005) and D06 (the 2005 Bankruptcy Reform Act).
   - A scan of every comma-formatted number in all five documents found no bank count. The only institution counts are the D02 credit-union figures (9,688; 212; 1,462 in 1990).
   - D02 (2003) and D03 (2004) were written before that date. D01 covers household-goods movers, D04 assisted living, and D06 bankruptcy and child support. D06 never uses "bank" or "banks" as a whole word; its hits are "bankruptcy".
   - `manifest.json` lists D01–D04 and D06; there is no D05.
6. The forced guess uses a figure from outside the packet, from memory and unverified: about 7,550 FDIC-insured commercial banks in Q3 2005. I place this between roughly 7,630 at the end of 2004 and 7,526 at the end of 2005. 9,900 − 7,550 ≈ 2,350.
   - Why only about 1%: the bank count is from memory and I can only place it within a few dozen. The document that holds the real figure might use a different definition of "bank" or round the number. The credit-union base could also be read three ways (see readings).

**minimal_documents:** D02 is enough for the credit-union side. No document in the packet supplies the bank count, and I found no substitute for D02.

**readings:**
- Counting the two uninsured credit unions gives a base of 9,902, which adds 2 to any result (about 2,352).
- Counting only federally insured credit unions gives a base of 9,688, which lowers the result by 212 (about 2,138).
- If "banks" means all FDIC-insured banks and thrifts (from memory, about 8,860 in Q3 2005), the answer would be about 1,040. If it means only national banks, the answer would be roughly 8,000.

**gaps:**
- The main missing fact is the number of U.S. banks on September 30, 2005, along with which definition of "bank" the question intends.
- All documents are plain text (method "text", no pages). There were no PDFs or layout files, so I couldn't check any original page.
- I didn't read every document line by line. Coverage was targeted searches across all five `text\` files and all five `docs\` source files, plus direct reads of D02 lines 1–60, 215–254, 387–394, 463–472, 587–600, 643–650 and 1209–1218, and the opening lines of D01 and D04.

**contaminated:** no. The run folder name `q01-r0-removal-noD05` suggests a document was removed, but it reveals no answer, reasoning or source content.

Relevant files:
- `D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q01-r0-removal-noD05\solver-1\text\manifest.json`
- `D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q01-r0-removal-noD05\solver-1\text\D02.txt`
- `D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q01-r0-removal-noD05\solver-1\docs\gaoreports_gao_03_971.txt`

Result: gold 2,361 not reached (forced guess about 2,350, p about 0.01). D05 needed in practice; the
remembered bank count (about 7,550; the closed-book run said about 7,540) is near but not exact.
Design signal: this solver, reading D02's Background, took 9,900 and called the footnoted two
uninsured credit unions undated; it never read D02 1179 ("As of December 2002, 214 ... all but two
were privately insured"), the sentence that dates them. The trap bites a strong reader; the 1179
sentence is the deciding fact and must be in the evidence.


## q02 rev 0 without D02 (runs/q02-r0-probe-k7/solver-1; neutral folder name)

answer: Not answerable from this packet. The documents identify the state as Idaho, but none of them gives a count of credit unions without federal deposit insurance at end-2002, for Idaho or for the U.S. You asked for a forced best guess anyway: **5.7%**. That assumes about 12 of about 212 such credit unions were in Idaho. Both numbers come from my vague memory, not from the packet. I put the chance that this guess is exactly right at about 5%.

confidence: low (high that Idaho is the state; nothing in the packet supports the percentage)

path:
1. Identifying the state: D05 (GAO-06-387, *OCC Preemption Rules*), Appendix VI, Table 4, "Information on Funding for Selected State Bank Regulators", lines 819–821 of `D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q02-r0-probe-k7\solver-1\text\D05.txt`. The table's columns are run together in the text. The Idaho row, reassembled, reads: "The Idaho Department of Finance is funded by assessments of regulated financial institutions set by the director within a statutory limit. The assessment structure includes a graduated base fee and excess fee based on total assets and $100 per branch office." Its formula column says "Regressive schedule". So the state is **Idaho**.
2. Ruling out other states: no other state in Table 4 has a per-branch charge. California uses a flat rate based on assets, Georgia an asset-size schedule, Iowa assets plus CAMELS factors, New York a cost-based approach and North Carolina year-end assets. The other "$100" matches in D05 (lines 669 and 767) are about charter asset shifts and OCC's price of supervision. The other "branch" matches (lines 205, 359, 587 and 643) are about foreign-bank branches and the Riegle-Neal Act.
3. Looking for the credit-union counts:
   - I searched every text file for "credit union", "privately/private insured", "share insurance", "without federal", "NCUSIF", "federally insured", "deposit insurance", "insur", "Idaho" and end-of-2002 phrasings. I also checked docs/ for "credit union" and "branch".
   - "Credit union" appears only in D03 (lines 107, 111 and 171), and only as the National Credit Union Administration in the context of predatory-lending preemption.
   - D05 mentions "federally insured depository institutions" (line 613) and the FDIC (lines 183 and 533), but has no credit-union insurance data.
   - "Idaho" appears only in D05: in the list of states where GAO did its work, and in Table 4.
   - There are no figures on privately insured or non-federally insured credit unions by state, and no U.S. total, anywhere.
4. Calculation: not possible. It would need Idaho's count and the national total at end-2002, and neither is in the packet.

minimal_documents: D05 is enough for the first step (identifying Idaho). No document, alone or combined, covers the second step (the counts). I found no alternative source for either step.

readings:
- Questions with this shape usually come from a by-state table of privately insured credit unions at end-2002, giving Idaho's count divided by the U.S. total. My memory, which the packet does not confirm, puts the total at about 212 credit unions with private insurance. For Idaho I recall roughly 10–17, which would give about 4.7% to 8.0%; 12/212 = 5.66%, rounded to 5.7%.
- The total would change if credit unions insured by a non-federal public body were counted, such as Puerto Rico cooperatives insured by COSSEC. That is another reason exact agreement is unlikely.

gaps:
- The packet has no data on credit unions lacking federal deposit insurance: no count by state, no U.S. total, nothing as of end-2002.
- The manifest jumps from D01 to D03, and text/ has no D02. The document with the credit-union data may have been left out when the packet was prepared. If so, the caller needs to fix the preparation.
- There are no PDFs or Dnn.layout.txt files (the manifest shows the method as "text" with pages null), so I had no original page images to check against.
- Coverage: I found the evidence by keyword search across all five text files, plus selected checks of docs/. I did not read any document from start to finish. D01 (household goods moving), D04 (assisted living) and D06 (bankruptcy and child support) are off-topic; I checked them only by search and their opening lines.

contaminated: no. No answer, reasoning, lever or source hint was provided. The only extra context was the user's email address, which is irrelevant.

Result: gold 9.8% not reached (forced guess 5.7%, p about 0.05). D02 needed in practice. The probe
recalled the 212 private-insurance total from memory but not Idaho's count or the uninsured pair.


## q02 rev 0 without D05 (runs/q02-r0-probe-m3/solver-1; neutral folder name)

answer: Not answerable from this packet. None of the packet's documents says which state's bank regulator adds a $100 per-branch charge to an asset-based assessment. The manifest lists D01–D04 and D06 but no D05, which may be where that fact was. Forced best guess: **9.8%**, with roughly a 20% chance of being exactly right.

confidence: low

path:
1. Denominator, from D02 (GAO-03-971), Appendix I, p.54 (text/D02.txt line 1179): "As of December 2002, 214 state- chartered credit unions lacked federal deposit insurance, and all but two were privately insured." Federally chartered credit unions must be federally insured (line 231), so 214 is all U.S. credit unions without federal insurance.
2. D02, p.6 (line 233): "As of December 2002, 212 credit unions* about 2 percent of all credit unions* chose to purchase private deposit insurance."
3. D02, footnote 8 (line 239): "we identified two uninsured credit unions, one was located in Idaho and the other was located in New Hampshire."
4. Per-state counts of privately insured credit unions, from D02 Table 3, p.17 (line 467): "Alabama 3 … California 22 … Idaho 20 … Illinois 40 … Indiana 21 … Maryland 5 … Nevada 8 … Ohio 93 … Total 212". Figure 1 (December 2002) shows the same numbers, and Table 1 matches for Alabama, California, Illinois, Indiana and Ohio (total 179). I checked the sums: 3+22+20+40+21+5+8+93 = 212, and the web-site counts and percentages in Table 3 all add up.
5. Credit unions without federal insurance, by state, at end of 2002, as a share of 214:
   - Ohio: 93, 43.5%
   - Illinois: 40, 18.7%
   - California: 22, 10.3%
   - Indiana: 21, 9.8%
   - Idaho: 20 + 1 uninsured = 21, 9.8%
   - Nevada: 8, 3.7%
   - Maryland: 5, 2.3%
   - Alabama: 3, 1.4%
   - New Hampshire: 0 + 1 uninsured = 1, 0.5%
6. The missing link: I searched every text/ and docs/ file for "branch", "$100", "100", "hundred", "per/each/additional office", "asset", "assess", "fee", "charge", "supervisory fee" and "examination fee". The only "branch" hits are D02's site-visit branches, and the only "$100" hits are D02's deposit-insurance limits and deposit sizes. No document gives any state bank regulator's assessment formula.
7. Why 9.8% as the guess: there are nine candidate states, and nothing in the packet favours any of them. 9.8% (21/214) is the only result shared by two candidates, Indiana and Idaho, so it covers the most ground. It is a hedge, not evidence. The probability is the sum of my roughly equal priors for those two states, adjusted down a little for the chance that the intended state is outside this list or that the author used different counting.

minimal_documents: D02 supplies every count and the denominator. The document naming the state is not in the packet, and no other packet document can substitute for it: D01 is about household-goods movers, D03 predatory lending, D04 assisted living, D06 bankruptcy and child support.

readings:
- Denominator of 212 (counting only privately insured credit unions): Ohio 43.9, Illinois 18.9, California 10.4, Indiana 9.9, Idaho 9.4 (20/212), Nevada 3.8, Maryland 2.4, Alabama 1.4. The question says "all … without federal deposit insurance", which matches D02's 214 sentence, so 214 is the better reading.
- If Idaho is the state but its uninsured credit union is left out: 20/214 = 9.3%.
- Once the state is known, the list in path step 5 gives the answer directly.

gaps:
- The identity of the state whose bank regulator adds $100 per branch office to an asset-based assessment is missing.
- Unread coverage:
  - Read in full: D01, D02 (lines 1–1356).
  - D03: lines 1–259 read; the remaining lines (GAO ordering/contact boilerplate) were not read.
  - D04: read lines 1–80 only. The rest was checked only by keyword search.
  - D06: read lines 1–60 and 100–119 only. The rest was checked only by keyword search.
- No layout or PDF files exist (manifest method "text", pages null). D02's Figure 1 map and bar chart lost their state-to-number pairing in extraction, but Tables 1 and 3 settle it.
- I did not open question.txt.

contaminated: no

Packet files used:
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q02-r0-probe-m3\solver-1\text\D02.txt
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q02-r0-probe-m3\solver-1\text\manifest.json

Result: forced guess = gold 9.8% (p about 0.2). Indiana (21 privately insured) and Idaho (20 + 1
uninsured) both give 21 / 214 = 9.8%, so a guess without D05 lands on the gold for two of nine
states. The platform's document check (high model, D05 left out) could find D05 "not needed".
Disqualifying for q02.


## q04 rev 0 without D02 (runs/q02-r0-probe-k7/solver-1)

I couldn't answer this from the packet. It settles which state is meant (Idaho) but has no data at all on privately insured credit unions or on GAO's 2003 review of their Web sites.

    answer: not answerable from the packet. Forced best guess: 33.3%, about 4% chance of being exactly right.
    confidence: high that it is not answerable; low for the guess
    path:
      1. Which state. D05 (GAO-06-387, "OCC Preemption Rules", 04/28/2006), Appendix VI, Table 4 "Information on Funding for Selected State Bank Regulators", Idaho row (text/D05.txt lines 817-821): "The Idaho Department of Finance is funded by assessments of regulated financial institutions set by the director within a statutory limit. The assessment structure includes a graduated base fee and excess fee based on total assets and $100 per branch office." The extracted text mixes the table's columns together, but the sentence reads clearly. Table 4 also covers California, Georgia, Iowa, New York and North Carolina; none of them has a per-branch charge. A search for "branch office" across all five documents finds only this line. So the state is Idaho.
      2. The credit union step. I found no document about privately insured credit unions, private share insurance, or the notice that an institution lacks federal deposit insurance:
         - "credit union" appears only in D03 (GAO-04-412T, predatory lending), at lines 107, 111 and 171. Each one just names the National Credit Union Administration as a federal regulator.
         - "privately", "share insurance", "not federally" and "American Share" have no matches in text/ or in the docs/ originals.
         - "Web site" matches in the packet are GAO's standard "obtain copies" boilerplate, D03's Justice Department guide, or D04's Florida assisted-living locator. None is a review of credit union Web sites.
         - D05 mentions "Federal Deposit Insurance Corporation" only as a regulator GAO interviewed (lines 183, 533), and "federally insured depository institutions" once in a preemption argument (line 613).
         - The other documents are off topic: D01 (GAO-01-819T, household goods movers), D04 (GAO-04-684, assisted living), D06 (GAO-08-148R, bankruptcy and child support).
         So the packet has neither the number of privately insured credit unions in Idaho nor how many of their Web sites lacked the notice. No calculation is possible.
      3. How the guess was chosen. The answer has to be k/n with a small Idaho count n. Under a flat prior, 33.3% is the value the most small fractions produce (1/3, 2/6, 3/9, 4/12), so it is the most likely single guess. This is not based on remembering the actual report. Other values that are about as likely include 25.0, 22.2, 16.7 and 20.0.
    minimal_documents: D05 is enough for the state. No packet document covers the percentage, and no substitute was found among D01, D03, D04 or D06.
    readings: (a) The literal reading: Idaho credit unions whose Web site lacked the notice, divided by all privately insured credit unions in Idaho. Not answerable. (b) Lacking sites divided by only the Idaho credit unions whose Web sites GAO reviewed. Also not answerable, with the same guess. No other state fits the $100-per-branch description.
    gaps:
      - The source with the actual figure is missing. From memory, and not checked here, it is probably GAO's August 2003 report on Federal Deposit Insurance Act section 43 disclosures (GAO-03-971, I believe). The manifest skips D02, which may be the document that was left out.
      - Facts needed: the number of privately insured credit unions in Idaho in GAO's 2003 review, and how many of their Web sites lacked the notice.
      - Extraction: all documents are text-only (method "text", pages null), so there are no PDF pages or layout files to check. D05 Table 4 has its columns mixed together, but the Idaho sentence is readable.
      - Coverage: I read all of D03, the headers of D01, D04 and D06, and D05's appendices (lines 780-859). Everything else was covered by keyword searches across text/ and docs/ (credit union, privately, share insurance, deposit insurance, NCUA, Web site, Idaho, branch office, $100, 2003, disclose/notice, lacked). I did not read D01, D04, D05 or D06 line by line in full.
    contaminated: no. Only the workspace path, packet path and question were given.

Result: gold 25.0% not reached (forced guess 33.3%, p about 0.04; 25.0 listed among equally
likely small fractions). D02 needed in practice.

## q03 rev 0 without D05 (runs/q02-r0-probe-m3/solver-1)

**answer:** Not answerable from this packet. It gives the number of credit unions at the end of 2002 (9,902 in total, 9,688 of them federally insured). It has no count of U.S. banks for September 30, 2005, or for any other date. My forced best guess is **11.95%**, and I put the chance that it is exactly right at about 10%. That guess depends on a bank count I remember from outside the packet and have not checked.

**confidence:** high that the packet can't answer it; low for the forced guess.

**path:**
1. **Federally insured credit unions.** D02 is GAO-03-971, dated 08/20/2003 (`D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q02-r0-probe-m3\solver-1\text\D02.txt`). Line 231 says: "As of December 2002, 9,688 credit unions were federally insured" and "Almost all (98 percent) credit unions are federally insured."
2. **Privately insured credit unions.** Line 233 says: "As of December 2002, 212 credit unions* about 2 percent of all credit unions* chose to purchase private deposit insurance." Two tables agree:
   - Figure 1 (lines 249–259): 22+93+3+5+8+20+21+40 = 212.
   - Table 3 (line 469): "Total 212".
3. **Uninsured credit unions.** Footnote 8 (line 239) says: "we identified two uninsured credit unions". Line 1179 says: "As of December 2002, 214 state- chartered credit unions lacked federal deposit insurance, and all but two were privately insured."
4. **Total at the end of 2002:** 9,688 + 214 = **9,902**. As a check, 9,688/9,902 = 97.8%, which fits "98 percent", and 212/9,902 = 2.1%, which fits "about 2 percent".
5. **The bank count is missing.** I searched all five documents, both the text/ files and the docs/ originals (`...\solver-1\docs\`):
   - "September 30", "Sept. 30", "9/30", "third quarter" and "Q3" found nothing.
   - "2005" appears only in D06 (the bankruptcy Reform Act of April and October 2005) and D01 (an FMCSA study planned for FY2003–2005).
   - I listed every comma-formatted number (17 in total, the same in text/ and docs/). The only one that counts financial institutions is 9,688.
   - Other 4-digit numbers that aren't years are phone numbers, room numbers or legal citations.
   - Every line using "bank" or "banks" (13 in D02, 9 in D03) is descriptive, with no counts. D01, D04 and D06 don't use those words at all, and "thousand" never refers to banks.
6. **Formula if a bank count B were available:** (9,902 − B) / B × 100.
7. **Forced guess.** I used B = 8,845 FDIC-insured institutions on September 30, 2005. That number is my own memory and is not in the packet. (9,902 − 8,845) / 8,845 = 1,057 / 8,845 = 0.11950, or **11.95%**.
   - About 10% chance it is exactly right, because two things both have to hold. The question's author probably used 9,902 (I'd put that at roughly 65%). My memory of 8,845, and reading "banks" as all FDIC-insured institutions, also have to match their figure (roughly 15–20%).

**minimal_documents:** D02 covers the credit union side only. No document in the packet covers the bank side. The manifest lists D01–D04 and D06; there is no D05, and I can't tell what it would have contained.

**readings:** Other defensible readings, all still needing a bank count from outside the packet:
| Credit unions used | Banks (my unverified memory) | Result |
|---|---|---|
| 9,688 (federally insured only) | 8,845 | 843/8,845 = 9.53% |
| 9,900 (federally plus privately insured, leaving out the 2 uninsured) | 8,845 | 1,055/8,845 = 11.93% |
| 9,902 | ≈7,540 (commercial banks only) | 2,362/7,540 = 31.33% |
| 9,688 | ≈7,540 (commercial banks only) | 2,148/7,540 = 28.49% |

**gaps:**
- There is no count of U.S. banks (commercial banks or FDIC-insured institutions) for September 30, 2005, anywhere in the packet. That is the deciding missing fact.
- The packet also doesn't say whether "banks" means commercial banks only or banks plus thrifts.
- "As of December 2002" is taken to mean the end of 2002.
- There are no PDFs; the sources are GAO ASCII text files. D02's Figure 1 is a map, but its numbers came through as text and match Table 3.
- I didn't read every line of D01, D03, D04 or D06. Coverage there comes from the searches above. I read the relevant parts of D02 directly.

**contaminated:** no. The prompt had only the paths and the question, with no answer or hints. No project instructions or memory were visible to me, but I can't check how I was launched (fresh session or not, or whether the 2.1.271 requirement was met).

Result: gold 31.31% not reached (forced guess 11.95%, p about 0.1; the recalled 7,540 route gives
31.33%, also not the gold). D05 needed in practice.

## q03 rev 0 without D02 (runs/q02-r0-probe-k7/solver-1)

I couldn't answer this from the packet. None of the five documents gives a count of U.S. credit unions for the end of 2002. Only the bank side is there.

    answer: Not answerable from this packet. Forced best guess, not supported by the packet: 28.47%. Probability it is exactly right: about 25%.
    confidence: high that the packet does not settle it; low for the forced guess
    path:
    1. Bank count, D05 (GAO-06-387), text\D05.txt line 191: "As of September 30, 2005, there were 1,846 federally chartered banks and 5,695 state-chartered banks.6". Banks = 1,846 + 5,695 = 7,541. D05 line 393 roughly agrees: "OCC oversees about 1,900 national banks" (December 2004, rounded).
    2. Credit union count for end-2002: none in the packet.
       - "credit union" appears only 3 times, all in D03 (GAO-04-412T, lines 107, 111, 171). Each time it is part of the agency name "National Credit Union Administration", with no counts.
       - D01, D04 and D06 contain no "union" or "NCUA". D05's hits are only about thrifts and depository institutions.
       - The "2002" mentions are unrelated: D01 (FMCSA milestones), D03 (the Household settlement, First Alliance, HMDA changes, HUD's proposed rules), D04 ("over 36,000 assisted living facilities", ombudsman complaints) and D05 (OCC's 2002 guidance).
       - Scanning for numbers from 8,000 to 12,999 finds only "8,712 borrowers" (D03:211) and 8,866 in OCC's fee table (D05:727, 756).
    3. Forced guess (outside the packet): I assumed 9,688 credit unions. That is my recollection of the National Credit Union Administration's count of federally insured credit unions at year-end 2002, not a document fact.
       - (9,688 − 7,541) / 7,541 = 2,147 / 7,541 = 0.284710, which rounds to 28.47%.
       - Check: 7,541 × 0.2847 = 2,146.92.
       - Probability basis: about 0.9 that the intended bank count is 7,541, × about 0.65 that my recollection is accurate, × about 0.45 that the intended source uses that exact, unrounded, all-federally-insured total. That gives roughly 0.25.
    minimal_documents: D05 covers the bank count only. No document in the packet gives the credit union count, and I found no alternative source for either figure.
    readings:
    - If the source rounded to "about 9,700" credit unions: 2,159 / 7,541 = 28.63%.
    - A count of federally chartered credit unions only would be well under 7,541 by my recollection. That gives a negative result, which contradicts "exceed", so it is unlikely to be the intended reading.
    - Bank count: the packet has no other September 30, 2005 figure, such as one including thrifts.
    gaps:
    - The 2002 credit union count is missing from the packet.
    - D05's footnotes were not extracted, so footnote 6, which qualifies the bank count, can't be read.
    - D05's Appendix V table ("How Selected Federal Financial Industry Regulators Are Funded", lines 789–791) is lost; only "Source: GAO." remains.
    - docs/ holds only .txt files and no PDFs, so I couldn't check the original pages. The docs/ originals search the same way: "credit union|NCUA" matches only the 3 hits in D03.
    - The manifest lists D01 and D03–D06 but no D02, so a document may be missing from this packet.
    - Coverage: I read D05 lines 185–225, 289–296, 340–402 and 535–883, and the relevant sections of D03. For D01, D04 and D06 I only ran keyword searches and read the openings of D01 and D06.
    contaminated: no

Result: gold 31.31% not reached (forced guess 28.47% = the 9,688 decoy route, p about 0.25). D02
needed in practice: the recalled federally insured count lands on the decoy.

## q04 rev 0 without D05 (runs/q02-r0-probe-m3/solver-1)

**answer:** The packet doesn't answer this. No document in it says which state's bank regulator adds a $100 charge per branch office to its assessment. My forced best guess is **15.1%** (Ohio, 14 of 93). I put the chance that this is exactly right at about **12%**. That is roughly 1/8 for picking the right state, times about 0.85 that the denominator should be all privately insured credit unions in the state. The packet does give the figures for each state (path 5), so the answer follows once the state is known.

**confidence:** low

**path:**
1. D02 is GAO-03-971, "Federal Deposit Insurance Act: FTC Best Among Candidates to Enforce Consumer Protection Provisions", dated 08/20/2003. This is GAO's 2003 review.
2. D02, Table 3, page 17 (`D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q02-r0-probe-m3\solver-1\text\D02.txt`, lines 459–469): "Table 3: Number and Percent of Web Sites Reviewed without Required Disclosures". Its columns are: total number of privately insured credit unions; number of Web sites identified and analyzed; Web sites without required disclosures (number); and that number as a percent. The rows read: "Alabama 3 2 0 0 California 22 18 3 17 Idaho 20 7 5 71 Illinois 40 15 8 53 Indiana 21 7 4 57 Maryland 5 2 2 100 Nevada 8 4 3 75 Ohio 93 23 14 61 … Total 212 78 39 50".
3. D02, line 455 says what "lacking the notice" means: "39 of the 78 sites had not included language to notify consumers that the credit union was not federally insured." D02 Appendix I (lines 1213–1215) adds: "We attempted to locate Web sites for all 212 privately insured credit unions; however, we were able to only identify 78 Web sites." Figure 1 and Table 1 give the same counts (3, 5, 8, 20, 21, 22, 40, 93; 3+22+40+21+93 = 179).
4. I looked for the fact that identifies the state and found nothing. I searched every file in text/ and docs/ for "$100", "branch", "per/each/additional office", "assess", "fee", "bank regulator" and "Department of Financial Institutions". The only matches are:
   - D02: $100,000 coverage, branch locations GAO visited, the Rhode Island bank regulator (footnote 9), and Ohio's Department of Financial Institutions.
   - D03: Washington State's Department of Financial Institutions, in a predatory-lending context.
   
   None of these describes an assessment or a per-branch charge.
5. The percentage for each state, using the literal reading: credit unions whose Web site lacked the notice ÷ all privately insured credit unions in the state.

   | State | Calculation | Result |
   |---|---|---|
   | Alabama | 0/3 | 0.0% |
   | California | 3/22 | 13.6% |
   | Idaho | 5/20 | 25.0% |
   | Illinois | 8/40 | 20.0% |
   | Indiana | 4/21 | 19.0% |
   | Maryland | 2/5 | 40.0% |
   | Nevada | 3/8 | 37.5% |
   | Ohio | 14/93 = 15.054 | 15.1% |

   The columns add up to the printed totals: 212 credit unions, 78 sites, 39 lacking the notice (50%).
6. Why I guessed Ohio: nothing in the packet, and nothing I reliably remember, links any of these eight states to a $100-per-branch assessment. I started from roughly equal odds for each state. I chose Ohio on a weak salience heuristic: it has the most privately insured credit unions and is home to the remaining private insurer (ASI). I gave Alabama less weight because its answer would be 0.0%.

**minimal_documents:** D02, plus a document that names the state with the $100-per-branch charge. No document in the packet can stand in for that second one.

**readings:** If the denominator is instead the Web sites GAO analyzed, the answers are:
- Alabama 0.0%
- California 16.7%
- Idaho 71.4%
- Illinois 53.3%
- Indiana 57.1%
- Maryland 100.0%
- Nevada 75.0%
- Ohio 60.9%

Under that reading the Ohio guess becomes 60.9%. I think this reading is less likely, because the question says "Of the privately insured credit unions in the state".

**gaps:**
- The fact that identifies the state is not in the packet.
- In D02, Appendix III (NCUA's comment letter, pp. 59–60) and Appendix IV (FTC's comment letter, pp. 61–71) appear only as headers with no text. There is no PDF in the packet to check them. They seem unlikely to cover state bank assessments, but I couldn't confirm that.
- The manifest lists D01–D04 and D06 but has no D05.
- I read D02, D03 and D06 in full. For D01 (household moving) and D04 (assisted living) I read only the headers and searched them: neither contains "bank", "credit union", "deposit" or "branch". I did not read question.txt.

**contaminated:** no

Result: gold 25.0% not reached (forced guess 15.1% Ohio, p about 0.12). D05 needed in practice;
the eight per-credit-union values are distinct, so no coincidence.
