# q01 rev 0 blind solver A (fresh blind-solver, packet solver-1/, question only)

Date: 2026-10-06. tested_sha256: 866f2ddd97642838aeb5ce32828c7229cd162a80174786f807cf02307d3322ca

Raw return:

answer: 4,821,423 copies. This is the "How People Are Counted" brochure, summed over its 20 listed language and audience versions: 19 in Wave 2 and 1 Thai version in Wave 3.

confidence: high

path:
1. Which piece won the most awards. D06 Appendix F, "Awards Submitted and Won" (D06.txt lines 664-827), lists 55 awards ("TOTAL AWARDS WON 55"). Line 465 calls them "over 50 awards from the marketing and communications industry". The "Promotional Materials" category covers items 22-27:
   - Poster Series: 1 award (#22)
   - "Fotonovela": 1 award (#23)
   - Toolkit for Latinos: 1 award (#25)
   - The brochure: 3 awards, more than any other promotional material:
     - #24 "Bronze Quill 2010: "How People Are Counted" Brochure" (MN IABC Award)
     - #26 "2010 Census "How People Are Counted" Brochure" (Minnesota PRSA Classics)
     - #27 ""How People are Counted Brochure"" (AIGA Creative Block 2010)
   - Excluded: "Mural" (4 awards) and the Greg Biffle PSA (3) are under Advertising (Paid) and Public Relations/PSAs/Podcast. They are not partnership promotional materials and have no listed copy counts. Item #21 (IPG MERGE) is a paid-advertising award, which matches D03 line 92.
2. Why it counts as a partnership piece. D04 line 203 says "The Census Bureau created Partnership Program promotional materials in 28 different languages". D04 Appendix B, "List of Promotional Materials, Languages, and Quantities" (line 408), lists each wave with a "Distribution Timeframe".
3. Wave 2 rows (D04 lines 612-632, "Distribution Timeframe - April 2009 - December 2009"), items 29-47, all "Brochure - How People Are Counted":
   English 920,100; Spanish 392,785; Spanish (PR) 43,350; Native Hawaiian Pacific Islander 255,680; American Indian Alaskan Native 511,700; Russian 255,850; Polish 255,850; Arabic 255,850; Chinese 256,692; Vietnamese 255,850; Korean 255,851; Tagalog 255,850; Khmer 85,850; Hmong 85,850; Laotian 85,935; Bengali 134,810; Urdu 85,850; Hindi 85,850; Japanese 256,020. Wave 2 total 4,735,573.
4. Wave 3 row (D04 line 734): "3 Brochure - How People Area Counted Thai 85,850". "Area" is a typo for "Are"; it is the same brochure.
5. Calculation: 4,735,573 + 85,850 = 4,821,423. Grouped check: 9 rows near 255,850 total 2,303,493; 6 rows near 85,850 total 515,185; the other 5 total 2,002,745. Sum is 4,821,423.
6. Integrity checks:
   - All 121 Wave 2 rows add up to exactly 26,230,373. That matches the printed "PRINTED PROMOTIONAL MATERIALS WAVE 2 TOTAL 26,230,373".
   - Wave 3 rows 1-26, which include the Thai brochure, add up to exactly the printed total of 7,652,496. The printed total leaves out the last row (Thai Confidentiality Flyer, 44,775). This is a quirk in the source and does not affect the answer.
   - The ARRA, Reprint and Reorder lists have no brochure rows.
   - The original file in docs/ has identical rows (promotional.txt lines 611-631 and 733).

minimal_documents: D04 + D06. No alternatives: the awards list appears only in D06, and the per-version quantities appear only in D04.

readings:
- If you leave out the Wave 3 Thai row (because of the typo, or by counting only the main Wave 2 block), the answer is 4,735,573 across 19 versions. This is weaker because the question asks for all versions.
- If "piece" meant any campaign item, the Mural ad campaign won more awards (4). It has no listed distribution copies, so it cannot answer the question.

gaps:
- There are no PDF pages to inspect: the manifest gives method "text" and pages null.
- I read D04 in full. In D06 I read Appendix F plus the award and brochure passages.
- D01, D02, D03 and D05 were only searched (award, brochure, "How People", Counted) plus a few lines read for context. I did not read them in full.
- D04 section 5.7 says brochures were developed in the 9 languages added with ARRA funding, but no copy counts for them are listed. They are not included.

contaminated: no. The automatically attached git status showed only file names, with no answer or reasoning content.

(Files read: solver-1/text/D04.txt and solver-1/text/D06.txt.)
