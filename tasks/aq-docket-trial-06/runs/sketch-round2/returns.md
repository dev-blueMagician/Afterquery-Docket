# Sketch round 2 (user request: questions like Trial 2's q01 or Trial 6's q02), 2026-10-06

Sketch-stage evidence only, not final check records. Blind solves are fresh blind-solver agents
given the workspace root, a packet from q01's prepared run (same corpus bytes; scope guard) and
the sketch question verbatim. Closed-book agents get the question only. Removal probes use the
neutral-named packet q02-r0-probe-m3 (corpus without D05). Returns copied verbatim.

## i14 blind solve (q01 run solver-1 packet)

**Answer: 10.3%.** California had 22 of the 214 U.S. credit unions that were not federally insured as of December 2002.

answer: 10.3%

confidence: high

path:
1. **The state is California.** In D05 (GAO-06-387), Appendix VI, Table 4 "Information on Funding for Selected State Bank Regulators", text/D05.txt lines 803–809, the California row says: "The California Department of Financial Institutions levies assessments … The assessment (minimum of $5,000 and a maximum of $2.20 per $1,000 of assets on a sliding scale) reflects a statutory limit applicable to banks." This is the only "2.20" in the packet; I searched both text/ and docs/.
2. **The national total is 214.** D02 (GAO-03-971), Appendix I, text/D02.txt line 1179 (docs original line 1177): "As of December 2002, 214 state- chartered credit unions lacked federal deposit insurance, and all but two were privately insured."
   - This fits D02 line 233: "As of December 2002, 212 credit unions* about 2 percent of all credit unions* chose to purchase private deposit insurance."
   - It also fits footnote 8 at line 239: "we identified two uninsured credit unions, one was located in Idaho and the other was located in New Hampshire." 212 + 2 = 214.
   - Federally chartered credit unions don't change this total. Line 231 says they "must be federally insured by the National Credit Union Share Insurance Fund," so all 214 are state-chartered.
3. **California's count is 22.** D02 Table 3, line 467: "California 22 18 3 17", with total "212" at line 469.
   - The same 22 appears in Table 1 (line 423, "California 22 21 b 6 29") and in the Figure 1 and Highlights state counts (December 2002).
   - Neither uninsured credit union is in California (they are in Idaho and New Hampshire), so California's count of credit unions without federal insurance is 22.
   - The eight state counts add up: 3 + 22 + 20 + 40 + 21 + 5 + 8 + 93 = 212.
4. **Calculation:** 22 / 214 = 0.1028037, which is 10.28%, or **10.3%** to one decimal.

minimal_documents: D02 + D05. No alternatives exist in the packet: D05 is the only document with the $2.20 cap, and D02 is the only one with credit-union deposit-insurance counts.

readings: If "not federally insured" meant only the privately insured credit unions (leaving out the two uninsured ones), the answer would be 22 / 212 = 10.377%, or 10.4%. I think this reading is weaker, because D02 directly says 214 "lacked federal deposit insurance." That is exactly the group the question asks about, and the two uninsured ones are located outside California.

gaps:
- **Not fully read:** D02 (I read lines 1–300, 400–520 and 1172–1215, and searched the rest) and D05 (lines 1–18 and 740–849).
- **Searched only:** D01, D04 and D06 were searched by keyword ("2.20", "credit union", "per $1,000", "214/212", "all credit unions"). None of them mention credit unions.
- **D03:** it is about predatory lending, and its three credit-union mentions concern NCUA preemption only.
- **Source files:** the packet's sources are text files, not PDFs. I checked the decisive quotes against the docs/ originals and found no extraction problems.
- **Assumption:** footnote 8 about the two uninsured credit unions has no date. I treated it as December 2002 because Appendix I gives the 214 and "all but two" figures "As of December 2002."

contaminated: no

## i15 blind solve (q01 run solver-2 packet)

answer: 25.0% (5 of Idaho's 20 privately insured credit unions). If the question means the share of Web sites GAO analyzed, the answer is 71.4% (5 of 7). See readings.

confidence: medium. The facts and arithmetic are solid. The uncertainty is which denominator the question means.

path:
1. **Finding the state (D05, GAO-06-387, dated 04/28/2006).** Appendix VI, Table 4, "Information on Funding for Selected State Bank Regulators," is at text/D05.txt lines 799–821 (docs/gaoreports_gao_06_387.txt lines 815–819). The Idaho row says: "The Idaho Department of Finance is funded by assessments of regulated financial institutions set by the director within a statutory limit. The assessment structure includes a graduated base fee and excess fee based on total assets and $100 per branch office." The extracted text mixes the table's columns together, so I put this sentence back together. The other five states in the table (California, Georgia, Iowa, New York, North Carolina) have no per-branch charge. Searching for "$100" and "branch" across all six documents found no other per-branch assessment. The state is Idaho.
2. **The 2003 source (D02, GAO-03-971).** It is dated "DATE: 08/20/2003" (line 17). At line 455 it says: "we also reviewed 78 Web sites of privately insured credit unions … 39 of the 78 sites had not included language to notify consumers that the credit union was not federally insured … (see table 3)."
3. **The Idaho figures (D02, Table 3, lines 459–469).** The table is "Number and Percent of Web Sites Reviewed without Required Disclosures." Its columns are: Total number of privately insured credit unions; Number of Web sites identified and analyzed; then, for sites without required disclosures, Total number and Total percent. The Idaho row reads: "Idaho 20 7 5 71". The total row reads: "Total 212 78 39 50".
4. **Checking the columns line up.** The credit union counts add to 212 (3+22+20+40+21+5+8+93). The Web sites add to 78 (2+18+7+15+7+2+4+23). The non-compliant sites add to 39 (0+3+5+8+4+2+3+14). Six states are above 50%, which matches the text's "six of the eight states." Idaho's 20 also matches Figure 1 (line 257, "3 5 8 20 21 … 40 … 22 … 93"). Table 3 counts the same 39 sites that the text says lacked the "not federally insured" language, so it measures what the question asks about.
5. **Calculation.**
   - Literal reading: 5 ÷ 20 = 0.25, so **25.0%**.
   - Alternative: 5 ÷ 7 = 0.714286, so 71.4%. GAO printed this as 71.
6. **Why the literal reading comes first.** The question names its base as "the privately insured credit unions in the state." That matches Table 3's column "Total number of privately insured credit unions" (20), not the column of Web sites analyzed (7). Credit unions with no Web site found were not credit unions that "had Web sites that did not tell consumers." GAO notes: "We attempted to locate Web sites for all 212 privately insured credit unions; however, we were able to only identify 78 Web sites" (lines 1213–1215).

minimal_documents: D05 and D02, both required.
- D05 is the only document that ties a $100 per-branch-office charge to a state.
- D02 is the only document with the Web site results. A search for "privately insured" found matches only in D02.
- There are no substitutes: D01, D03, D04 and D06 cover household goods moving, predatory lending, assisted living, and bankruptcy and child support.

readings:
- (a) Share of all of Idaho's privately insured credit unions (December 2002 count) with Web sites lacking the notice: **25.0%**. This is my primary answer.
- (b) Share of Idaho Web sites GAO identified and analyzed that lacked the notice: **71.4%**. This is GAO's printed "71" recalculated to one decimal. It fits a reading where "as GAO found" points to GAO's own reported percentage, and the one-decimal request points to refining the rounded 71.
- (c) Copying the printed figure as 71.0% is not defensible at one decimal, because the counts give 71.4.

gaps:
- The packet has no PDFs and no layout files (the manifest lists method "text" with pages null). I could not check either table against an original page. Both tables come through with their columns mixed together. Table 3's column order is confirmed by its totals, and D05's Idaho row is clear once reassembled.
- For the 13 Idaho credit unions with no Web site found, the report does not say whether they had sites GAO missed. So 25.0% reflects what GAO found, not necessarily the true share.
- Coverage: I read D02 lines 1–60, 225–284 and 400–489, plus searched matches; D05 lines 790–849 plus searched matches; and only the titles and dates of D01, D03, D04 and D06, which I searched for "$100," "branch," "privately insured," "Web site" and "Idaho."
- I did not open question.txt.

contaminated: no. The input contained only the workspace root, packet path and question.

## i15 closed-book

answer: 33.3% (a guess)
confidence: low
basis: I remember that GAO's August 2003 report GAO-03-971, "Federal Deposit Insurance Act: FTC Best Among Candidates to Enforce Consumer Protection Provisions," checked whether privately insured credit unions disclosed that they lacked federal insurance. I can't recall which state's regulator adds $100 per branch office to its assessment. Idaho, Nevada, Indiana or Ohio seem possible, but that's a guess. I also don't remember GAO's state-level website figures, so the number is not based on actual recall. The report text is needed for the real figure.
contaminated: no

Result: misses (gold 25.0%).

## i14 closed-book

answer: about 40.6% (my guess is that the state is Ohio)
confidence: low
basis: I'm working from memory and inference, not from a document. I recall that at the end of 2002 there were about 212 credit unions without federal insurance. Almost all were insured privately by American Share Insurance (ASI) across roughly 9 to 10 states, and Ohio had the most. I could not remember which state's bank regulator caps its assessment at $2.20 per $1,000 of assets, so picking Ohio is a guess. Ohio's count of about 86 is also a rough estimate. The exact state-by-state counts and the assessment-cap detail would be in the source document, which I don't have.
contaminated: no

Result: misses (gold 10.3%). Note: the model recalls "about 212" as the count without federal insurance, i.e. the decoy denominator.

## i15 removal probe without D05 (packet q02-r0-probe-m3)

**answer:** The packet doesn't settle this. No document in it says which state's bank regulator adds a $100 charge per branch office to its assessment. My forced best guess is **15.1%**, which assumes the state is Ohio and counts all of the state's privately insured credit unions. I put the chance that this is exactly right at about 10%.

**confidence:** low

**path:**
1. `text/manifest.json` lists D01, D02, D03, D04 and D06. There is no D05. Four of the documents are on other subjects: D01 household goods moving (GAO-01-819T), D03 predatory lending (GAO-04-412T), D04 assisted living (GAO-04-684) and D06 bankruptcy and child support (GAO-08-148R). D02 is GAO-03-971, "August 2003 FEDERAL DEPOSIT INSURANCE ACT FTC Best Among Candidates to Enforce Consumer Protection Provisions" (D02:47).
2. The fact that would identify the state is in none of the five documents:
   - "branch" appears only in D02. All six hits are about GAO's site visits, for example "(49 main and 8 branch locations)" (D02:407).
   - "assessment" appears only in D02 and D06, and none of those hits is about fees.
   - The only plain "$100" amount is "$100 and $500 million" (D02:515). Every other match is $100,000.
   - No document matches per/each/every/additional followed by branch, office or location.
   - D02 mentions fees only as "fees paid by federal credit unions" to NCUA (D02:599).
3. D02 has the Web site data in "Table 3: Number and Percent of Web Sites Reviewed without Required Disclosures" (D02:459-469). Its columns are: total number of privately insured credit unions, number of Web sites identified and analyzed, number without required disclosures, and percent. The row text reads: "Alabama 3 2 0 0 California 22 18 3 17 Idaho 20 7 5 71 Illinois 40 15 8 53 Indiana 21 7 4 57 Maryland 5 2 2 100 Nevada 8 4 3 75 Ohio 93 23 14 61 … Total 212 78 39 50".
4. The text supports the table: "39 of the 78 sites had not included language to notify consumers that the credit union was not federally insured" (D02:455). The method was: "We attempted to locate Web sites for all 212 privately insured credit unions; however, we were able to only identify 78" (D02:1215).
5. Arithmetic checks: the credit unions sum to 3+22+20+40+21+5+8+93 = 212, the sites to 78, and the non-compliant sites to 39.
6. The question asks for the share "of the privately insured credit unions in the state", so I divided non-compliant sites by all of the state's privately insured credit unions:

| State | Calculation | Result |
|---|---|---|
| Alabama | 0/3 | 0.0 |
| California | 3/22 | 13.6 |
| Idaho | 5/20 | 25.0 |
| Illinois | 8/40 | 20.0 |
| Indiana | 4/21 | 19.0 |
| Maryland | 2/5 | 40.0 |
| Nevada | 3/8 | 37.5 |
| Ohio | 14/93 = 15.05 | 15.1 |

7. Basis for the guess: nothing in the packet points to a particular state, and I don't have a reliable memory of which state's regulator charges $100 per branch. I chose Ohio only because it is the largest and most prominent state in D02 (93 credit unions; the private insurer ASI is regulated there). I put the chance that Ohio is the right state at about 15–20%, and the chance that this denominator is the intended one at about 60%. Together that gives roughly 10%.

**minimal_documents:** D02 plus a document that identifies the state, which this packet does not contain. None of the other four documents can stand in for it.

**readings:**
- **Percent of the Web sites GAO analyzed:** if the denominator is the sites reviewed rather than all credit unions, the results are Alabama 0.0, California 16.7 (3/18), Idaho 71.4 (5/7), Illinois 53.3 (8/15), Indiana 57.1 (4/7), Maryland 100.0 (2/2), Nevada 75.0 (3/4) and Ohio 60.9 (14/23). Under this reading the guess for Ohio becomes 60.9.
- **Printed whole-number percents:** the table itself gives 0, 17, 71, 53, 57, 100, 75 and 61, which are not at the requested one-decimal precision.
- If you know the state, use its row in the table in step 6 or above.

**gaps:**
- The packet does not identify the state whose bank regulator adds a $100 per-branch charge. The missing D05 in the manifest suggests the document that would identify it was left out of this packet. Preparation needs to be fixed before this question can be answered properly.
- The source files are plain-text extractions with no PDFs or layout files. Table 3's rows are flattened into one line but are internally consistent.
- I read D02 in its relevant sections (lines 40–69, 240–275, 400–479, 1209–1216) and searched it in full. For D01, D03, D04 and D06 I read only the opening lines (about 40 each) and covered the rest with targeted searches.

**contaminated:** no

Result: gold 25.0% not reached (forced guess 15.1% Ohio, p about 0.1). D05 needed; per-credit-union
values are distinct across the eight states, so no coincidence.

## i14 removal probe without D05 (packet q02-r0-probe-m3)

**answer:** Not answerable from this packet. No document says which state's bank regulator caps its assessment at $2.20 per $1,000 of assets. My forced best guess is **9.8%**, with about a 15% chance of being exactly right.

**confidence:** high that the packet can't settle it; low for the guess.

**path:**
1. The total of credit unions without federal insurance comes from D02 (GAO-03-971), Appendix I (text/D02.txt line 1179): "As of December 2002, 214 state- chartered credit unions lacked federal deposit insurance, and all but two were privately insured." Line 231 says federally chartered credit unions "must be federally insured", so 214 covers the whole U.S.
2. D02 line 233: "As of December 2002, 212 credit unions* about 2 percent of all credit unions* chose to purchase private deposit insurance."
3. D02 footnote 8 (line 239) covers the two uninsured ones: "we identified two uninsured credit unions, one was located in Idaho and the other was located in New Hampshire."
4. D02 Table 3 (line 467) gives counts by state: "Alabama 3 … California 22 … Idaho 20 … Illinois 40 … Indiana 21 … Maryland 5 … Nevada 8 … Ohio 93 … Total 212". Table 1 (lines 423–427) agrees, and so do the Highlights map numbers (lines 69–73): "22 93 / 3 5 (Md.) 8 / 20 21 40". The sum checks: 3+22+20+40+21+5+8+93 = 212.
5. The state-identifying fact is missing. I searched all of text/ and docs/ for "2.20", "2. 20", "per $1,000", "1, 000" (the D02 extraction puts spaces inside numbers, e.g. "1, 462"), "thousand", "basis point", "assessment", "cap", "fee" and "bank regulator". None of the hits is a state regulator's assessment cap:
   - D01 is about household-goods movers.
   - D03 is about predatory lending.
   - D04 is about assisted living.
   - D06 is about bankruptcy and child support.
   - In D02, the only "bank regulator" phrase is about Rhode Island's oversight of RISDIC (footnote 9), with no assessment figure.
   - The manifest jumps from D04 to D06, so a document D05 appears to have been left out of this packet.

Percentage for each possible state, using 214 as the denominator:

| State | Count | Share |
|---|---|---|
| Ohio | 93 | 43.5% |
| Illinois | 40 | 18.7% |
| California | 22 | 10.3% |
| Indiana | 21 | 9.8% |
| Idaho (20 privately insured + 1 uninsured) | 21 | 9.8% |
| Nevada | 8 | 3.7% |
| Maryland | 5 | 2.3% |
| Alabama | 3 | 1.4% |
| New Hampshire (uninsured only) | 1 | 0.5% |
| Any other state | 0 | 0.0% |

**Forced guess basis:** 9.8% is the answer for two of the states (Indiana, and Idaho once its uninsured credit union is counted). The wording "all … not federally insured" suggests the question writer meant to include the two uninsured credit unions, which is what makes Idaho fit. The next most likely is 43.5% (Ohio, roughly 13–15%). The guess rests only on how the question is worded, not on any document, so I put its chance of being exactly right at about 15%.

**minimal_documents:** D02 alone supplies all the counts and the denominator. A second document identifying the state is needed and is not in the packet. No other packet document can stand in for D02.

**readings:**
- If "not federally insured" means only the privately insured (212 as the denominator):
  - Ohio 43.9%
  - Illinois 18.9%
  - California 10.4%
  - Indiana 9.9%
  - Idaho 9.4%
  - Nevada 3.8%
  - Maryland 2.4%
  - Alabama 1.4%
- If Idaho's uninsured credit union is left out of its count but 214 is kept: Idaho 20/214 = 9.3%.

**gaps:** The packet lacks any statement linking a state to the $2.20 per $1,000 cap; D05 is likely the missing source. There are no PDFs or layout files, so I couldn't check the Figure 1 map, but Table 3 gives the same per-state counts. I read D01, D02 and D03 in full; D04 and D06 were checked only by keyword searches.

**contaminated:** no. I did not open question.txt.

Result: gold 10.3% not reached (forced guess 9.8%, p about 0.15). D05 needed. Design signal: the
probe read "all ... not federally insured" as a sign the writer meant to include the uninsured pair,
so the wording itself points careful readers at the remainder.
