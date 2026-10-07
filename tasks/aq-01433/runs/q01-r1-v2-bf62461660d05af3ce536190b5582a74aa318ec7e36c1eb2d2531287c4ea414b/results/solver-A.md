# q01 rev 1 blind solver A (fresh blind-solver, packet solver-1/, question only)

Date: 2026-10-06. tested_sha256: bf62461660d05af3ce536190b5582a74aa318ec7e36c1eb2d2531287c4ea414b

Raw return:

answer: 4,821,423 copies of the "How People Are Counted" brochure (19 versions in Wave 2 plus a Thai version in Wave 3).

confidence: high

path:
1. Which piece won the most awards. D06 Appendix F ("Awards Submitted and Won", from the "14" page marker, lines 719-742) has a "Promotional Materials" category covering items 22-27. Item 21 is a general DraftFCB award ("Inclusive Marketing Initiative of the Year"), not tied to one piece. Award counts by piece:
   - Poster Series: one award (item 22, "Gold Award: 2010 Census Poster Series", MarCom).
   - "Fotonovela": one award (item 23, Honorable Mention, MarCom).
   - Toolkit for Latinos: one award (item 25, Minnesota PRSA Classics).
   - "How People Are Counted" brochure: three awards, all submitted by Weber Shandwick: item 24, "Bronze Quill 2010: 'How People Are Counted' Brochure" (MN IABC Award); item 26, "2010 Census 'How People Are Counted' Brochure" (Minnesota PRSA Classics); item 27, "'How People are Counted Brochure'" (AIGA Creative Block 2010).
   Other pieces with several awards (Mural, Puerto Rico Doors, the Greg Biffle PSA, 2010census.gov) are paid ads, PSAs or the website, not printed partnership promotional materials. The appendix ends "TOTAL AWARDS WON 55".
2. Why it counts as a partnership piece. D04 line 81 says "Printed materials for the Partnership Program were printed and distributed through contracts with the Government Printing Office." Line 79 says "Weber Shandwick was the lead contractor who worked on developing promotional materials."
3. Quantities listed. D04 Appendix B ("List of Promotional Materials, Languages, and Quantities").
   - Wave 2 ("Distribution Timeframe - April 2009 - December 2009", lines 612-632), rows 29-47 numbered with no gaps: English 920,100; Spanish 392,785; Spanish (PR) 43,350; Native Hawaiian Pacific Islander 255,680; American Indian Alaskan Native 511,700; Russian, Polish, Arabic, Vietnamese and Tagalog: 255,850 each; Chinese 256,692; Korean 255,851; Japanese 256,020; Khmer, Hmong, Urdu and Hindi: 85,850 each; Laotian 85,935; Bengali 134,810. Wave 2 subtotal: 4,735,573.
   - Wave 3 ("Distribution Timeframe - November - December 2009", line 734): "3 Brochure - How People Area Counted Thai 85,850". "Area" is a typo; this is the same brochure.
4. Calculation. 4,735,573 + 85,850 = 4,821,423. I checked this two ways: grouped sums and pairwise sums.
5. Cross-checks.
   - Adding all 121 Wave 2 rows gives exactly the printed "PRINTED PROMOTIONAL MATERIALS WAVE 2 TOTAL 26,230,373", so the brochure rows were extracted correctly.
   - The Wave 3 rows add up to 7,697,271, but the printed total is 7,652,496. The gap is 44,775, which matches the Khmer or Thai Confidentiality Flyer row, not the brochure's 85,850.
   - The brochure has no rows in the Reprint or Reorder tables.
   - docs/ shows the same 21 matching lines as text/.

minimal_documents: D04 + D06.
- D06 is needed for the awards; no other document lists awards by piece (D05 and D02 only mention awards in general).
- D04 is needed for the quantities; no other document lists the brochure. D02 line 400 only mentions "brochures" in general.

readings:
- Counting only the main Wave 2 listing (leaving out the Thai row because of its misspelled title) gives 4,735,573.
- Counting only the English version gives 920,100.
- "Listed for distribution" could also be read as the Appendix E surplus figures, but those are broken down by language, not by item, so they don't give a brochure figure.

gaps:
- The packet has no PDFs or layout files, only plain text, so I couldn't check the original pages.
- Appendix F's category boundaries come from the order of the extracted text. Item 21 might belong under "Promotional Materials", but that doesn't change the result.
- The Wave 3 table total doesn't match its rows (noted above); this doesn't affect the brochure figure.
- I didn't read D01, D03 or D05 in full, or most of D02. I covered them with searches for award, industry, brochure, counted/How People, fotonovela, toolkit, poster series and copies.

contaminated: no. I didn't open question.txt, notes or anything outside the packet's text/ and docs/.

(Files: solver-1/text/D06.txt, solver-1/text/D04.txt.)
