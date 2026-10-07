# q02 rev 0 blind solver A (fresh blind-solver, packet solver-1/, question only)

Date: 2026-10-06. tested_sha256: dfe07e432e8c034d865a97dc46d70ed4a0e119a055cd5b466fd51d51aab295e6

Raw return:

answer: 4,865,000 copies. That is 615,000 posters (345,000 Action plus 270,000 Awareness) and 4,250,000 General Public Fact Sheets, across 27 table rows.

confidence: high

path:
1. Which languages count (D03, 5.11, D03.txt lines 316-322). The 14 languages added to paid advertising with Recovery Act money are listed: "ARRA funding allowed us to add 14 languages including: Hmong, Laotian, Thai, Pakistani (Urdu), Bangladeshi (Bengali), Portuguese, French, Italian, German, Iranian (Farsi), Armenian, Greek, Yiddish, and Ukrainian." The list has exactly 14 names, so "including" here means the full set. The same section lists the Census 2000 base languages, which include "Chinese (... Simplified Chinese for print media)" and "Haitian Creole (French)". Line 78 repeats "14 additional languages added because of funding provided by the American Recovery and Reinvestment Act."
2. Which table is the ARRA wave (D04, Appendix B, D04.txt lines 781-826). The heading reads "WAVE ARRA - AWARENESS IN-LANGUAGE MATERIALS", with the timeframe "November 2009 - March 2010**". The docs/ source copy has the same figures at lines 780-825.
3. Rows included (all poster and fact-sheet rows in an added language):
   - Action Poster (9 rows): Italian 25,000; Portuguese 75,000; German 25,000; Iranian (Farsi) 70,000; Ukrainian 50,000; Armenian 25,000; Greek 25,000; Yiddish 25,000; French 25,000. Subtotal 345,000.
   - General Public Fact Sheet (10 rows): Italian 250,000; Portuguese 750,000; German 250,000; Iranian (Farsi) 750,000; Armenian 250,000; Greek 250,000; Yiddish 250,000; Urdu (Pakistani) 500,000; Bengali (Bangladeshi) 500,000; Ukrainian 500,000. Subtotal 4,250,000.
   - Awareness Poster (8 rows): French, Italian, German, Armenian, Greek and Yiddish at 25,000 each; Iranian (Farsi) 70,000; Ukrainian 50,000. Subtotal 270,000.
   - Total: 345,000 + 4,250,000 + 270,000 = 4,865,000.
4. Rows excluded:
   - Action Poster and Fact Sheet "Haitian Creole (French)" (75,000 and 750,000). Haitian Creole is a base language in D03, which lists "French" separately among the added ones. D04 Appendix E also lists "French" and "French (Haitian Creole)" as separate rows.
   - Action Poster "Chinese-Simplified" (75,000), a base language.
   - "Hispanic Targeted Poster English" (500,000), a base language.
   - Coloring books and teacher companions, the "TQA Calling Card English-based, with 5 additional languages", and the trinkets, because none are posters or fact sheets.
   - Hmong, Laotian and Thai have no rows in this wave.
5. Arithmetic check. Rows 1-36 add up to exactly "PRINTED PROMOTIONAL MATERIALS WAVE ARRA TOTAL 14,385,004": 495,000 + 5,000,000 + 270,000 + 500,000 + 420,000 + 14,004 + 180,000 + 6,000 + 7,500,000. All poster and fact-sheet rows total 6,265,000; subtracting the excluded 1,400,000 leaves 4,865,000. The promotional-items total of 12,747,000 also matches its rows.

minimal_documents: D03 and D04. D04 alone is not enough: 5.7 (line 212) gives the promotional-materials program's own lists, not the paid-advertising one. No other document can stand in for D03. D05 lists only some of the added languages (lines 504-508), and D06 Appendix C groups languages as "Emerging Audiences" and "New Legacy Languages" without the ARRA list.

readings:
- Promotional program's list instead of paid advertising's: 3,865,000. D04 5.7 names nine added languages ("Armenian, Farsi, French, German, Greek, Italian, Portuguese, Ukrainian, and Yiddish") and treats Urdu and Bengali as base. Dropping those two fact-sheet rows (1,000,000) gives 3,865,000. The question explicitly ties the languages to paid advertising, so this is the weaker reading.
- Including the "REPRINT Promotional Materials" table: 4,940,000. It sits right after the ARRA tables and adds Action Poster Bengali 50,000 and Thai 25,000. I rejected this because the reprint table has its own title and total ("TOTAL QUANTITIES 4,000,040") and is outside the WAVE ARRA total, which matches rows 1-36 exactly.
- Counting Haitian Creole (French) as French: 5,690,000. Not defensible, given the documents' explicit split between the two.
- Adding Wave 3: about 5,463,338 (weak). D04's body text says "Wave 3 materials, purchased with ARRA funding". Adding Wave 3's Thai, Hmong, Laotian, Bengali and Urdu poster, fact-sheet and flyer rows (598,338) would give that figure. However, that table is labeled "WAVE 3", not ARRA.
- Posters only: 615,000; fact sheets only: 4,250,000.

gaps:
- The documents are plain text only ("method": "text", no PDF pages), so I couldn't check page images. The "**" footnote on the ARRA timeframe has no explanation in the text, but it doesn't affect the count.
- I did not read D01, D02, D05 or D06 in full. I searched all six documents for ARRA/Recovery Act, the added-language names, "additional/added languages" and poster/fact-sheet terms. The only poster and fact-sheet hits outside D04 were unrelated Take 10 and RRFP fact sheets in D01 and a heading in D06.

contaminated: no. I did not open the packet's question.txt or any notes.

(Files used: solver-1/text/D03.txt, solver-1/text/D04.txt, solver-1/docs/census_census2010_campaign_icp_promotional.txt.)
