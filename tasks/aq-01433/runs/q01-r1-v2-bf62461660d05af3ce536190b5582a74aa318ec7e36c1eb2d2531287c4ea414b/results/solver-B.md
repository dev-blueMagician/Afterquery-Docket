# q01 rev 1 blind solver B (fresh blind-solver, packet solver-2/, question only)

Date: 2026-10-06. tested_sha256: bf62461660d05af3ce536190b5582a74aa318ec7e36c1eb2d2531287c4ea414b

Raw return:

answer: 4,821,423 copies. That's the "How People Are Counted" brochure in all 20 languages: 4,735,573 in Wave 2 plus 85,850 for the Thai version in Wave 3.

confidence: high

path:
1. Which piece won the most awards (D06, Appendix F, "Awards Submitted and Won", lines 664-827). In the Promotional Materials group:
   - Item 22, "Gold Award: 2010 Census Poster Series": 1 award.
   - Item 23, "Honorable Mention: 2010 Census 'Fotonovela'": 1 award.
   - Item 25, "2010 Census Toolkit for Latinos": 1 award.
   - The "How People Are Counted" brochure won 3 awards (all from Weber Shandwick submissions): Item 24, MN IABC: "Bronze Quill 2010: 'How People Are Counted' Brochure"; Item 26, Minnesota PRSA Classics: "2010 Census 'How People Are Counted' Brochure"; Item 27, AIGA Creative Block 2010: "'How People are Counted Brochure'".
   - Pieces excluded for not being printed partnership materials: "Mural" (paid advertising, 4 awards), "Puerto Rico Doors" print/out-of-home ads (paid, 2), Greg Biffle PSA (3), Issues Management (3), and the 2010census.gov website.
2. It is a printed partnership piece (D04). Line 81: "Printed materials for the Partnership Program were printed and distributed through contracts with the Government Printing Office." Line 79: "Weber Shandwick was the lead contractor who worked on developing promotional materials." In Appendix B the brochure rows fall under "PRINTED PROMOTIONAL MATERIALS".
3. Quantities (D04, Appendix B, "List of Promotional Materials, Languages, and Quantities").
   - Wave 2 ("Distribution Timeframe - April 2009 - December 2009", lines 612-632), rows 29-47, "Brochure - How People Are Counted": English 920,100; Spanish 392,785; Spanish (PR) 43,350; Native Hawaiian Pacific Islander 255,680; American Indian Alaskan Native 511,700; Russian, Polish, Arabic, Vietnamese and Tagalog: 255,850 each; Chinese 256,692; Korean 255,851; Japanese 256,020; Khmer, Hmong, Urdu and Hindi: 85,850 each; Laotian 85,935; Bengali 134,810.
   - Wave 3 (line 734): "3 Brochure - How People Area Counted Thai 85,850". The "Area" is a typo in the source.
4. Calculation.
   - Wave 2: 2,123,615 (English through AIAN) + 2,047,813 (the 255,850 group plus Chinese, Korean and Japanese) + 564,145 (the 85,850 group plus Laotian and Bengali) = 4,735,573.
   - Adding the Thai row: 4,735,573 + 85,850 = 4,821,423. I summed this a second way and got the same total.
   - Check against the source: adding all 121 Wave 2 rows gives exactly the printed "PRINTED PROMOTIONAL MATERIALS WAVE 2 TOTAL 26,230,373". So all 19 brochure rows were extracted correctly.
   - The brochure appears in no other wave or list (Waves 1 and 1A, ARRA, reprint and reorder lists).

minimal_documents: D04 + D06. I found no alternatives: the per-item award list exists only in D06, and the per-language quantities only in D04.

readings:
- If "in total" means all language editions and waves (my primary reading): 4,821,423.
- If the misspelled Thai row in Wave 3 is missed or left out: 4,735,573 (Wave 2 only).
- If only the English edition counts: 920,100.
- If "printed piece" is read loosely to include paid print advertising, "Mural" (4 awards) would lead. But it is a paid-advertising campaign, not a partnership promotional piece, and D04 lists no distribution copies for it.

gaps:
- The packet has only text files (manifest method "text", pages null), so I could not inspect an original PDF.
- In D04, the printed Wave 3 total (7,652,496) is 44,775 less than the sum of its rows (7,697,271). The gap equals one confidentiality-flyer row, so it doesn't affect the brochure.
- I fully read the D06 appendix and the relevant parts of D04 (lines 1-110, 232-236, 298-301, 400-998), plus D02 lines 390-411. I covered D01, D03 and D05 only by keyword searches ("award", "brochure", "How People"/"Counted"). They had no hits about the brochure, and the award mentions in D03 and D05 are general.

contaminated: no. The session context included a git-status snapshot with file and directory names only (for example tasks/aq-01433/), with no answers, reasoning or source hints. I did not read the packet's question.txt.

(Files used: solver-2/text/D04.txt, solver-2/text/D06.txt.)
