# q01 rev 0 shortcut audit (fresh shortcut-auditor, packet shortcut/, question only)

Date: 2026-10-06. tested_sha256: 866f2ddd97642838aeb5ce32828c7229cd162a80174786f807cf02307d3322ca

Raw return:

answer: 4,821,423 copies. The piece is the "How People Are Counted" brochure, listed in 20 language and audience versions: 19 in Wave 2 totalling 4,735,573, plus the Thai version in Wave 3 at 85,850.

verdict: clear

shortest_path:
1. Find the piece (D06, Appendix F "Awards Submitted and Won", lines 719-742). The brochure won three awards:
   - item 24: "Bronze Quill 2010: 'How People Are Counted' Brochure" (MN IABC Award)
   - item 26: "2010 Census 'How People Are Counted' Brochure" (Minnesota PRSA Classics)
   - item 27: "'How People are Counted Brochure'" (AIGA Creative Block 2010)
   Each other promotional-materials entry won one award: "Poster Series" (22), "Fotonovela" (23) and "Toolkit for Latinos" (25).
2. Get the quantities (D04, Appendix B "List of Promotional Materials, Languages, and Quantities", TOTAL QUANTITY column).
   - Wave 2 (lines 612-632), items 29-47: English 920,100; Spanish 392,785; Spanish (PR) 43,350; NHPI 255,680; AIAN 511,700; Russian, Polish and Arabic 255,850 each; Chinese 256,692; Vietnamese 255,850; Korean 255,851; Tagalog 255,850; Khmer and Hmong 85,850 each; Laotian 85,935; Bengali 134,810; Urdu and Hindi 85,850 each; Japanese 256,020. These sum to 4,735,573.
   - Wave 3 (line 734): "3 Brochure - How People Area Counted Thai 85,850". The title has a typo ("Area").
   - Total: 4,735,573 + 85,850 = 4,821,423. I checked this with a second grouping: 1,824,585 + 2,303,493 + 515,185 + 178,160 = 4,821,423.
3. Brochure appears nowhere else. It is not in Wave 1, 1A, ARRA or the Reprint table, and no total line or narrative gives the brochure's quantity.

sufficient_documents: D06 and D04 together are needed and enough. D06 names the piece but gives no quantities. D04 gives the quantities but never mentions awards. The source files docs/census_census2010_campaign_icp_summary.txt and docs/census_census2010_campaign_icp_promotional.txt match the extracted text row for row. Neither document can answer alone, and no other document can stand in for either.

searches:
- Award terms: "award" (case-insensitive) across all text files; award names and synonyms (Addy, Telly, MarCom, honor, prize, recognized). D06 Appendix F is the only per-item awards list. The award passages in D03, D05 and D06 only say "over 50 awards", "multi-award winning" or name campaign-level awards, never a specific piece.
- Piece terms: "How People", "Counted", "brochure", "People Area", "Poster Series", "Fotonovela", "Toolkit for Latinos" in both text/ and docs/.
- Quantity terms: "copies", "for distribution", "reprint".
- Read in full: D04 lines 1-998 (body and Appendices B-E) and D06 lines 460-470 and 640-830.
- Not read, as instructed: question.txt, snapshot.json and the sibling packets. One directory listing showed their file names only; I did not open them. D01, D02, D03 and D05 were covered by search only.

readings/gaps:
- Main pitfall: an exact search for "How People Are Counted" misses the Thai row (typo, separate Wave 3 table). That gives 4,735,573 (Wave 2 only), which falls short of "all of its language and audience versions".
- Other multi-award items: "Mural" ads (about 4 awards), Greg Biffle PSA (3), Issues Management (3) and 2010census.gov (several) are paid advertising, PR or web items, not partnership promotional materials. None appears in D04's quantity tables, so none yields a competing number.
- Item 21 (IPG MERGE "Inclusive Marketing Initiative of the Year") is a campaign-level award, not a piece.
- Robustness: the brochure still leads even if any one of its three awards were excluded.
- Difficulty risk, not a shortcut: once Appendix F names the brochure, a single search pulls up all the rows, and the arithmetic is a routine 20-row sum.
- No extraction gaps found: Wave 2 items 29-47 run continuously across the page break.

(The agent also listed the four files it read: shortcut/text/D06.txt, shortcut/text/D04.txt and the two matching docs/ originals.)
