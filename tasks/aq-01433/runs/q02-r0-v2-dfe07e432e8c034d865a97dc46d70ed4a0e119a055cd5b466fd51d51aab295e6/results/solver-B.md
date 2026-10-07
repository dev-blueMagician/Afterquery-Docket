# q02 rev 0 blind solver B (fresh blind-solver, packet solver-2/, question only)

Date: 2026-10-06. tested_sha256: dfe07e432e8c034d865a97dc46d70ed4a0e119a055cd5b466fd51d51aab295e6

Raw return:

Answer: 4,865,000 copies. That is 615,000 posters plus 4,250,000 fact sheets.

answer: 4,865,000 copies (615,000 posters and 4,250,000 fact sheets)
confidence: high

path:
1. Which languages were added (D03, paid advertising, lines 78 and 316-322). The ads used "the 14 languages used in Census 2000 plus 14 additional languages added because of funding provided by the American Recovery and Reinvestment Act."
   - Base languages: "English, Spanish, Chinese (Mandarin and Cantonese for oral media, Simplified Chinese for print media), Vietnamese, Korean, Hindi, Tagalog, Russian, Polish, Arabic, Haitian Creole (French), Japanese, and Cambodian (Khmer)."
   - Added languages: "ARRA funding allowed us to add 14 languages including: Hmong, Laotian, Thai, Pakistani (Urdu), Bangladeshi (Bengali), Portuguese, French, Italian, German, Iranian (Farsi), Armenian, Greek, Yiddish, and Ukrainian." The list names exactly 14 languages, so "including" does not leave any out.
2. The ARRA wave (D04 Appendix B, lines 781-826). The table is headed "WAVE ARRA - AWARENESS IN-LANGUAGE MATERIALS / Distribution Timeframe - November 2009 - March 2010**". Rows 1-36 add up to exactly the printed "PRINTED PROMOTIONAL MATERIALS WAVE ARRA TOTAL 14,385,004", so no rows were lost in extraction.
3. Poster and fact-sheet rows in the added languages:
   - Action Poster (rows 2-9, 11): Italian 25,000; Portuguese 75,000; German 25,000; Iranian (Farsi) 70,000; Ukrainian 50,000; Armenian 25,000; Greek 25,000; Yiddish 25,000; French 25,000. Subtotal 345,000.
   - General Public Fact Sheet (rows 13-22): Italian 250,000; Portuguese 750,000; German 250,000; Farsi 750,000; Armenian 250,000; Greek 250,000; Yiddish 250,000; "Urdu (Pakistani) 500,000"; "Bengali (Bangladeshi) 500,000"; Ukrainian 500,000. Subtotal 4,250,000.
   - Awareness Poster (rows 23-30): French 25,000; Italian 25,000; German 25,000; Farsi 70,000; Armenian 25,000; Greek 25,000; Yiddish 25,000; Ukrainian 50,000. Subtotal 270,000.
   - Total: 345,000 + 4,250,000 + 270,000 = 4,865,000 (27 rows).
4. Excluded rows:
   - Base-language posters and fact sheets: "Action Poster Haitian Creole (French) 75,000", "Action Poster Chinese-Simplified 75,000", "General Public Fact Sheet Haitian Creole (French) 750,000", and "Hispanic Targeted Poster English 500,000".
   - Items that are not posters or fact sheets: the coloring and activity books and teacher companions (English/Spanish), the "TQA Calling Card English-based, with 5 additional languages 7,500,000", and all trinkets.
   - Cross-check: all ARRA posters and fact sheets come to 6,265,000. Subtracting the 1,400,000 excluded gives 4,865,000.
5. Consistency check (D04 Appendix E, lines 960-993). Per-language totals match the ARRA rows for Armenian, Greek, Italian, Yiddish (300,000 each), Farsi (890,000), Ukrainian (600,000) and French (50,000). Appendix E lists German at 30,000 against the 300,000 listed in the ARRA wave. The question asks what was listed in the wave, so the Appendix B figures stand.

minimal_documents: D03 + D04. Nothing else can replace D03:
- D05 (lines 498-509 and 527) partly supports it. Its Phase 2 copy-testing groups "for languages added ... as a result of the ARRA funds" cover Bengali, Hmong, Lao, Thai, Urdu, Armenian, Farsi, Greek and Portuguese, but leave out French, German, Italian, Yiddish and Ukrainian.
- D06 only gives budget groupings ("Emerging Audiences", "New Legacy Languages"), not which languages ARRA added.

readings:
- D04's own promotional-materials list (3,865,000). D04 line 212 describes a different split for the Partnership Program: 19 base languages, including Bengali, Urdu, Hmong, Laotian and Thai. It then says the Deputy Director "requested the following additional nine languages: Armenian, Farsi, French, German, Greek, Italian, Portuguese, Ukrainian, and Yiddish." Using that list drops the Urdu and Bengali fact sheets, giving 4,865,000 - 1,000,000 = 3,865,000. The question ties the languages to "its paid advertising", which is D03's list, so I rank this reading lower.
- Counting the reprint table (4,940,000). A "REPRINT Promotional Materials" table follows the ARRA trinkets (lines 848-860) and includes "Action Poster Bengali 50,000" and "Action Poster Thai 25,000". If it counts as part of the ARRA wave, the total is 4,940,000. It isn't labelled as ARRA, has its own "TOTAL QUANTITIES 4,000,040", and sits outside the 14,385,004 total, so I excluded it.
- Treating "Haitian Creole (French)" as French (5,690,000). This would add 825,000, but D03 lists Haitian Creole (French) as a base language and French separately as added, so I don't think this reading holds up.

gaps:
- The documents are plain text only (manifest says "method": "text", "pages": null). There are no PDFs or layout files, so no page images could be checked. The docs/ copy of D04 matches the text extraction for the decisive rows.
- I read D04 lines 196-215, 286-301, 470-509, 560-879 and 944-998; D03 lines 300-350; D05 lines 486-530; and D06 lines 266-281 and 535-570.
- I covered D01 and D02 only by searching for ARRA, Recovery Act and the added-language names. D01 had no hits, and D02's hits were unrelated words (for example "arrangements").

contaminated: no

(Packet files used: solver-2/text/D03.txt, solver-2/text/D04.txt, solver-2/docs/census_census2010_campaign_icp_promotional.txt.)
