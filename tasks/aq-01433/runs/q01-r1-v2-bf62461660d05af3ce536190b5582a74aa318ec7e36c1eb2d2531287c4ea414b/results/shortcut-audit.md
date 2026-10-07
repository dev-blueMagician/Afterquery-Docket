# q01 rev 1 shortcut audit (fresh shortcut-auditor, packet shortcut/, question only)

Date: 2026-10-06. tested_sha256: bf62461660d05af3ce536190b5582a74aa318ec7e36c1eb2d2531287c4ea414b

Raw return:

answer: 4,821,423 copies of the "How People Are Counted" brochure.

verdict: clear

shortest_path:
1. Find the piece (D06, Appendix F "Awards Submitted and Won", text/D06.txt lines 664-827). Under Promotional Materials, the brochure has three awards:
   - #24 MN IABC, "Bronze Quill 2010: 'How People Are Counted' Brochure"
   - #26 Minnesota PRSA Classics, "2010 Census 'How People Are Counted' Brochure"
   - #27 AIGA Creative Block 2010, "How People are Counted Brochure"
   Every other promotional material has one: Poster Series #22, "Fotonovela" #23, Toolkit for Latinos #25. #21, IPG MERGE's "Inclusive Marketing Initiative of the Year", isn't tied to a specific piece. "Mural" (4 awards) and "Puerto Rico Doors" (2) are paid advertising, not partnership promotional material.
2. Find the quantities (D04, Appendix B "List of Promotional Materials, Languages, and Quantities").
   - Wave 2, rows 29-47 (lines 612-632), 19 editions: English 920,100; Spanish 392,785; Spanish (PR) 43,350; Native Hawaiian/Pacific Islander 255,680; American Indian/Alaska Native 511,700; Russian, Polish, Arabic, Vietnamese and Tagalog 255,850 each; Chinese 256,692; Korean 255,851; Japanese 256,020; Khmer, Hmong, Urdu and Hindi 85,850 each; Laotian 85,935; Bengali 134,810.
   - Wave 3, row 3 (line 734): "Brochure - How People Area Counted Thai 85,850". "Area" is a typo for "Are".
3. Add them up.
   - Wave 2 = 1,356,235 + 767,380 + 2,047,813 + 564,145 = 4,735,573. I checked this a second way with a row-by-row running total and got the same figure.
   - Adding the Thai row: 4,735,573 + 85,850 = 4,821,423.
   The brochure does not appear in Wave 1, Wave 1A, ARRA, the reprint/reorder tables, or Appendix E. Appendix E gives only language-level surplus totals.

sufficient_documents: D06 (docs/census_census2010_campaign_icp_summary.txt) plus D04 (docs/census_census2010_campaign_icp_promotional.txt). Both are required. D06 has the awards but no quantities; D04 has the quantities but no awards for any specific piece. No alternative source holds either input. The figures in docs/ match text/.

searches:
- Literal and concept terms: award, "Appendix F", "how people", "people (are|area) counted", "counted brochure", brochure, "poster series", fotonovela, "toolkit for latinos", "most award", "award-winning", recognized, copies.
- Ready-made totals: 4,821,423, 4,735,573, "4.8 million", "4.7 million". None found.
- Read in full: D06 Appendix F; D04 table of contents, Executive Summary, sections 1-5.19, and Appendices B through E; D02's promotional-items section (lines 385-424); D03's award and brochure lines.
- Coverage gap: D01 and D05 were only searched by keyword, with no brochure hits.
- Shortcut attacks that failed: No narrative names the most-awarded piece or gives its copy total. No single document has both the awards and the quantities. The question's wording doesn't give the piece away, because several posters also have many language rows in D04. The route is a name join between documents plus a 20-row sum.
- Difficulty risk (not a shortcut): The join is an exact title match, and the sum is routine, though long and split across two wave tables.

readings/gaps:
- 4,735,573: the Wave 2 total alone, which is what you get if the Thai row is missed because of the "Area" typo. The strongest reading includes it: Wave 3 is the in-language follow-on that adds Thai versions of the Wave 2 items (Awareness Poster, Final Fact Sheet and Religious Leaders guide, all in Thai).
- 920,100: the English edition only. This is weak given the question says "In total".
- Mural (paid advertising, 4 awards): excluded because the question says "partnership promotional piece".
- Not checked: extraction is text-only, so original page images weren't reviewed. D01 and D05 weren't read in full.
- Contamination: none. I deliberately did not open the packet's question.txt. The only background context was a git-status list of file names with no contents.
