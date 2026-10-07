# q01 rev 0 blind solver B (fresh blind-solver, packet solver-2/, question only)

Date: 2026-10-06. tested_sha256: 866f2ddd97642838aeb5ce32828c7229cd162a80174786f807cf02307d3322ca

Raw return:

answer: 4,821,423 copies

confidence: high

path:
1. Finding the piece (D06, Appendix F "Awards Submitted and Won", D06.txt lines 664-827; "TOTAL AWARDS WON 55"). Six awards under the "Promotional Materials" category (line 723) name specific pieces:
   - 22 "Gold Award: 2010 Census Poster Series" (Mar Com)
   - 23 "Honorable Mention: 2010 Census "Fotonovela"" (Mar Com)
   - 24 "Bronze Quill 2010: "How People Are Counted" Brochure" (MN IABC Award, Weber Shandwick)
   - 25 "2010 Census Toolkit for Latinos" (Minnesota PRSA Classics)
   - 26 "2010 Census "How People Are Counted" Brochure" (Minnesota PRSA Classics)
   - 27 ""How People are Counted Brochure"" (AIGA Creative Block 2010)
   The brochure won 3 awards; every other promotional piece won 1. Item 21, "Inclusive Marketing Initiative of the Year," doesn't name a piece. D04 line 52 confirms these were partnership materials: "In support of both the National and Regional Partnership Programs, the contractors produced 288 different promotional materials". Weber Shandwick was "the lead contractor who worked on developing promotional materials" (line 79).
2. Quantities (D04, Appendix B "List of Promotional Materials, Languages, and Quantities"). These are the Wave 2 rows 29-47 (D04.txt lines 612-632, "TOTAL QUANTITY" column), each labelled "Brochure - How People Are Counted":
   English 920,100; Spanish 392,785; Spanish (PR) 43,350; Native Hawaiian Pacific Islander 255,680; American Indian Alaskan Native 511,700; Russian 255,850; Polish 255,850; Arabic 255,850; Chinese 256,692; Vietnamese 255,850; Korean 255,851; Tagalog 255,850; Khmer 85,850; Hmong 85,850; Laotian 85,935; Bengali 134,810; Urdu 85,850; Hindi 85,850; Japanese 256,020.
   Wave 3, row 3 (line 734) adds the Thai version under a misspelled name: "3 Brochure - How People Area Counted Thai 85,850". These rows match the source file solver-2/docs/census_census2010_campaign_icp_promotional.txt (lines 611-631 and 733).
3. Calculation (checked two ways):
   - Wave 2 subtotals: 2,123,615 for English, Spanish, Spanish (PR), NHPI and AIAN; 2,047,813 for the five 255,850 rows plus Chinese, Korean and Japanese; 564,145 for the four 85,850 rows plus Laotian and Bengali; Wave 2 total: 4,735,573 (19 versions).
   - Adding Thai: 4,735,573 + 85,850 = 4,821,423 (20 versions).
   - Cross-check by size group: 1,824,585 + 2,303,493 + 515,185 + 178,160 = 4,821,423.

minimal_documents: D04 + D06. D06 is the only source that gives awards by piece. D03 and D05 mention awards only in aggregate ("over 50 industry and leadership awards"). D04 is the only source of per-piece quantities; D01, D02, D03 and D05 contain no rows for this brochure. No substitute found for either document.

readings:
- Wave 2 list only, or missing the "Area" misspelling: 4,735,573. The question asks for all language and audience versions, so the Thai row belongs in the total.
- Most awards across all categories, not just promotional materials: the "Mural" paid ads (items 1, 2, 6, 10) have 4 awards. They are paid advertising, not a partnership promotional piece, and have no copy quantities, so this reading doesn't apply.
- Items 25 and 26 counted as one award: the brochure still leads with 2, so the answer doesn't change.

gaps:
- D04 line 212 says brochures were also developed in the nine languages added with recovery-act (ARRA) funding. The ARRA wave list (lines 786-826) has no brochure rows, so any such versions have no listed quantity and are excluded.
- The sources are plain text with no PDF or layout files, so I couldn't check page images. The Wave 2 header and rows read cleanly.
- Coverage: I read D04 in full. In D06 I read lines 40-43, 240-249, 455-474 and 655-830, and searched the rest. D01, D02, D03 and D05 were checked by search only (award, brochure, counted, "how people" and variants) plus the specific award lines in D03 and D05.

contaminated: no. The session context included a git status listing workspace file names only, with no answer, reasoning or source hints for this question. I can't confirm from inside the session whether it was a non-fork, omitClaudeMd invocation. No project instructions or memory content were visible, and I read nothing outside this packet's text/ and docs/ folders.
