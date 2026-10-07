# q02 rev 0 shortcut audit (fresh shortcut-auditor, packet shortcut/, question only)

Date: 2026-10-06. tested_sha256: dfe07e432e8c034d865a97dc46d70ed4a0e119a055cd5b466fd51d51aab295e6

Raw return:

answer: 4,865,000 poster and fact-sheet copies. That is 345,000 Action Posters, 4,250,000 General Public Fact Sheets and 270,000 Awareness Posters.

verdict: clear

shortest_path:
1. Which languages were added (D03, paid advertising report, lines 316-322): "Base funding allowed the replication of the 14 languages used in Census 2000: ... Chinese (... Simplified Chinese for print media) ... Haitian Creole (French) ..." and "ARRA funding allowed us to add 14 languages including: Hmong, Laotian, Thai, Pakistani (Urdu), Bangladeshi (Bengali), Portuguese, French, Italian, German, Iranian (Farsi), Armenian, Greek, Yiddish, and Ukrainian." Line 78 says the same: "14 additional languages added because of funding provided by the American Recovery and Reinvestment Act."
2. The ARRA wave table (D04, promotional materials report, Appendix B, lines 781-826): "WAVE ARRA - AWARENESS IN-LANGUAGE MATERIALS". I kept only posters and fact sheets in the added languages:
   - Action Posters: Italian 25k, Portuguese 75k, German 25k, Farsi 70k, Ukrainian 50k, Armenian 25k, Greek 25k, Yiddish 25k, French 25k = 345,000
   - General Public Fact Sheets: Italian 250k, Portuguese 750k, German 250k, Farsi 750k, Armenian 250k, Greek 250k, Yiddish 250k, Urdu 500k, Bengali 500k, Ukrainian 500k = 4,250,000
   - Awareness Posters: French, Italian, German 25k each, Farsi 70k, Armenian, Greek, Yiddish 25k each, Ukrainian 50k = 270,000
   - Excluded as base languages: Haitian Creole (French) poster 75k and fact sheet 750k, Chinese-Simplified poster 75k, and the English Hispanic Targeted Poster 500k.
3. Cross-checks:
   - All posters and fact sheets in rows 1-31 total 6,265,000. Subtracting the 1,400,000 excluded copies gives 4,865,000.
   - Rows 1-36 add up exactly to the printed "PRINTED PROMOTIONAL MATERIALS WAVE ARRA TOTAL 14,385,004", so the text extraction lost no rows.

sufficient_documents: D03 + D04.
- D04 alone does not give this answer. Its own list (line 212) is "additional nine languages: Armenian, Farsi, French, German, Greek, Italian, Portuguese, Ukrainian, and Yiddish", and it puts Bengali and Urdu in the base plan for promotional materials. Using only D04 gives 3,865,000.
- D03 alone has no quantities.
- A weaker alternative for D03: D05 lines 498-509 and 527 show Bengali and Urdu among the languages tested in Phase 2 copy testing "for languages added ... as a result of the ARRA funds."

searches:
- Terms searched: ARRA, Recovery Act, Reinvestment; added, additional, new, legacy or emerging languages; individual language names (Yiddish, Ukrainian, Armenian, Hmong, Laotian, Urdu, Bengali); poster and fact sheet; the candidate totals 4,865 / 3,865 / 4,940 / 5,690 / "4.9 million" (none found anywhere).
- Read closely: D03 sections 5.10-5.13; D04 front matter, sections 5.5-5.19, Appendix B pages 28-34 and Appendix E; D06 budget section and Appendices A-D; D05 copy-testing section.
- D01 and D02 were checked by search only; neither mentions ARRA or added languages.
- I compared the D04 docs/ original against the text layer and they match.
- No shortcut found:
  - No total for this question appears in any document.
  - D04 Appendix E (surplus by language) covers all waves and all printed items, and does not match the ARRA table (German 30,000 against 300,000; Portuguese 900,000 against 825,000).
  - The question names neither the languages nor any quantities.

readings/gaps:
- Using D04's nine-language list gives 3,865,000. The question ties the languages to paid advertising, which points to D03's 14-language list, so I treat this as a misreading. It is also the main trap.
- Including the unlabeled "REPRINT Promotional Materials" list (D04 lines 848-860, which follows the ARRA wave and adds Bengali Action Poster 50,000 and Thai Action Poster 25,000) gives 4,940,000. I think this reading is weak: that list has its own "TOTAL QUANTITIES 4,000,040" and sits outside the labeled ARRA wave total. It is still a minor ambiguity risk.
- Counting Haitian Creole (French) as French gives 5,690,000. D03 explicitly lists Haitian Creole as a base language, so this is wrong.
- Using D06's "New Legacy Languages" list only gives 2,075,000, which is also wrong.
- Difficulty risk: the cross-document step is a simple filtered sum once D03's list is found. The difficulty comes from the competing D04 list and the look-alike language labels.
- Gaps: I did not read the full bodies of D01, D02, D05 and D06, or D04's Wave 1/1A/2 tables. They are not labeled ARRA, and searches found nothing relevant in them. I did not open question.txt, notes or other packets, and nothing leaked.

(Files: shortcut/text/D03.txt, shortcut/text/D04.txt, shortcut/docs/census_census2010_campaign_icp_promotional.txt.)
