# q02 rev 0 removal probe without Doc 2 (local D03)

Date: 2026-10-06. Probe packet: runs/q02-r0-probe-m7/solver-1 (copy of the rev 0 solver-1 packet
minus D03; remaining documents renumbered D01-D05 with manifest keys and header lines
rewritten: D01 mail response, D02 national partnership, D03 promotional, D04 research,
D05 summary; neutral folder name; bound to the read guard as its own run). Fresh blind-solver,
question text plus a forced-guess instruction. Question bytes match tested_sha256
dfe07e432e8c034d865a97dc46d70ed4a0e119a055cd5b466fd51d51aab295e6. In this return, "D03" is the
promotional report (bundle D04), "D04" the research report (bundle D05), "D05" the summary
(bundle D06).

Raw return:

answer: 3,865,000 copies. That is 615,000 posters (345,000 Action + 270,000 Awareness) plus 3,250,000 General Public Fact Sheets. This is my forced best guess. I put the probability that it is exactly right at about 0.5.

confidence: medium-low. The arithmetic is solid. The weak point is which languages count as "added to paid advertising."

path:
1. The added languages (D03, line 212). The only document that names ARRA-added languages is D03: "nineteen of these languages were identified in the base plan..." and "As part of the ARRA funding allocated to the Partnership Program... the Deputy Director requested the following additional nine languages: Armenian, Farsi, French, German, Greek, Italian, Portuguese, Ukrainian, and Yiddish... posters, brochures, and factsheets were developed inlanguage for these additional nine languages." Haitian Creole, Mandarin, Urdu and Bengali are in the base list.
2. The link to paid advertising.
   - D03, line 190: promotional materials "were produced in 28 languages and were also used for the Paid Advertising campaign."
   - D05, line 172: "hundreds of advertisements were developed in 28 different languages." That 28 equals 19 base plus 9 added.
   - D05, line 568 (Appendix C, the paid-media budget): "New Legacy Languages: French, German, Greek, Italian, Portuguese, and Yiddish," a row with N/A for Census 2000. "Emerging Audiences" in the same table include Farsi and "Urkrainian."
   - D04, lines 165 and 527: ARRA paid for new ad creative "for languages added... as a result of the ARRA funds," tested in Phase 2. Armenian was among the Phase 2 languages.
   - So all nine have a paid-advertising presence in the packet.
3. The wave (D03, lines 781-826). The table is headed "WAVE ARRA - AWARENESS IN-LANGUAGE MATERIALS." Wave 3 is separately "purchased with ARRA funding" (line 298), but it is not the wave labeled ARRA. Rows in the nine languages:
   - Action Posters: Italian 25,000, Portuguese 75,000, German 25,000, Iranian (Farsi) 70,000, Ukrainian 50,000, Armenian 25,000, Greek 25,000, Yiddish 25,000, French 25,000. Total 345,000.
   - General Public Fact Sheets: Italian 250,000, Portuguese 750,000, German 250,000, Farsi 750,000, Armenian 250,000, Greek 250,000, Yiddish 250,000, Ukrainian 500,000. Total 3,250,000. There is no French fact sheet.
   - Awareness Posters: French, Italian, German, Armenian, Greek and Yiddish at 25,000 each, Farsi 70,000, Ukrainian 50,000. Total 270,000. There is no Portuguese awareness poster.
4. Rows excluded as base languages or English: Haitian Creole (French) 75,000 + 750,000; Chinese-Simplified 75,000; Urdu (Pakistani) 500,000; Bengali (Bangladeshi) 500,000; Hispanic Targeted Poster English 500,000.
5. Checks.
   - All poster and fact-sheet rows in the wave total 6,265,000. Minus the excluded 2,400,000, that leaves 3,865,000.
   - Adding the coloring books (620,004) and the TQA card (7,500,000) gives 14,385,004, which matches the printed wave total.
   - By language: 300k + 890k + 50k + 300k x3 + 825k + 600k + 300k = 3,865,000.
   - Appendix E (D03, lines 960-993) matches for Armenian, Farsi, French, Greek, Italian, Ukrainian and Yiddish. German is printed as 30,000 with 93,817 marked unusable, so it is likely a typo for 300,000. Portuguese is printed as 900,000, which is 75,000 more than the wave lists. I used the wave listing, since the question asks what was "listed."
   - The REPRINT block (lines 848-860) is not labeled ARRA and has no rows in the added languages.

minimal_documents: D03 is enough for the language list and the counts. D05 (lines 172 and 568) or D04 (lines 165 and 527) supports the paid-advertising framing.

readings:
- D04 Phase 2 languages only, 3,315,000. Treat the languages added to ads as the audiences first tested in Phase 2 (Table 2, lines 470-478): Bengali, Hmong, Lao, Thai, Urdu, Armenian, Farsi, Greek, Portuguese. The wave then counts Portuguese 825k, Farsi 890k, Armenian 300k, Greek 300k, Urdu 500k and Bengali 500k. This leaves out French, German, Italian, Yiddish and Ukrainian even though D05 puts them in 2010 paid media, and it counts Urdu and Bengali, which D03 calls base languages. This is the strongest alternative because the question says "paid advertising," and I'd give it about 0.2.
- Both lists combined, 4,865,000.
- D05 "New Legacy" six only, 2,075,000. The packet never links this list to ARRA.
- D04's separately listed new audiences only (Armenian, Farsi, Greek, Portuguese), 2,315,000.

gaps:
- No document explicitly lists the languages ARRA added to paid advertising. D03's list is tied to the Partnership Program.
- D05's Appendix B (the ARRA expenditure plan) is blank in both the text/ and docs/ copies. It may have been an image lost in extraction.
- The packet is text-only: there are no PDFs or layout files to check.
- D01 and D02 were searched but not read in full; they have no relevant content. D04 and D05 were read selectively. Waves 1-2 of D03 Appendix B were not read row by row, but a search showed the nine languages appear only in the ARRA wave and Appendix E.

contaminated: no. The auto-attached git status showed file names only, with no answer, reasoning or lever for this question. I can't confirm how this session was invoked.

(Files used: probe solver-1/text/D03.txt, D04.txt, D05.txt.)
