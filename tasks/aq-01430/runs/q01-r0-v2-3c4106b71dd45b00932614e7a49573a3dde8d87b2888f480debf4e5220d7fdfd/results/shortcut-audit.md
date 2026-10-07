# q01 rev 0, shortcut audit (raw return, 2026-10-06)

Fresh shortcut-auditor agent (Claude Code, claude-opus-5-5, omitClaudeMd), packet shortcut of run
q01-r0-v2-3c4106b71dd45b00932614e7a49573a3dde8d87b2888f480debf4e5220d7fdfd; input: workspace root,
packet path and question verbatim. 183 s, 32 tool uses. Return copied verbatim.

---

answer: **−34 TWh.** EU coal-fired generation was about 34 TWh lower in 2021 than in 2019.

verdict: clear

shortest_path:
1. **D06** (Global Electricity Review 2025), EU section, line 1076: "Over the last five years, coal generation has fallen by 182 TWh (-40%)". The starting year is 2019: the same paragraph says gas "was 139 TWh (-24%) lower in 2024 than it was in 2019", and line 1078 says wind and solar rose "from 17% in 2019 to 29% in 2024". So coal 2024 minus coal 2019 = −182.
2. **D07** (Global Electricity Review 2026), line 1036: "Coal generation accounted for almost two-thirds of the EU's fossil power decline (-162 TWh) since 2021." The −162 TWh is the coal figure, not the fossil total. Line 1034 gives the 2021–2025 fossil decline as −257 TWh, and 162/257 = 63%, which matches "almost two-thirds". Gas at −81 TWh is "almost a third". So coal 2025 minus coal 2021 = −162.
3. **D07** line 1020: "Coal generation declined by 5% (-14 TWh) in 2025". So coal 2025 minus coal 2024 = −14.
4. Calculation: 2021 minus 2019 = (−182) − (−162) + (−14) = **−34 TWh**.
5. Cross-check against the older reports:
   - D04 line 63 says EU coal fell 20% in 2020.
   - D05 lines 103 and 229 say EU coal "strongly rebounded compared to 2020, but remained below 2019 levels".
   - The derived numbers fit both: 2019 ≈ 455 TWh (182/0.40), 2020 ≈ 364, 2021 ≈ 421, which is about 7.5% below 2019.

sufficient_documents: D06 and D07 together; both are needed. I found no alternative set. D07 has nothing on EU coal in 2019, and D06 has nothing on 2021. D04 and D05 only give percentages or qualitative statements with no EU TWh values, so they serve as consistency checks only.

searches:
- Terms: EU, EU-27, European Union and Europe combined with coal; coal near 2019 or 2021; every coal line with a TWh figure in D06 and D07; all EU mentions in all eight documents.
- Read in full: D04 and D05. Also read: the EU sections of D02, D03, D06 and D07, all truncated long lines that matched, and the EU lines in D08 and D01.
- Checked the three key quotes against the original docs/ files; they match.
- Coverage: every EU coal mention in the packet was inspected. None gives the 2019–2021 change directly, as a single document or as a whole-answer lookup.

readings/gaps:
- **Revision risk between editions:** D06 and D07 use different years' versions of the Ember dataset, so historical values could be revised by a few TWh. The stated percentages are consistent: D06's −40% and its 2024 figure of −16% (−50 TWh) both put 2024 at about 267–273 TWh.
- **Rejected reading 1:** treating −162 TWh as the total fossil decline would make coal about −108, giving an answer of −88. That conflicts with the explicit −257 TWh fossil total on line 1034.
- **Rejected reading 2:** taking "last five years" in D06 to start in 2020 would make the 2020–2021 change −34. That contradicts D05's statement that EU coal "strongly rebounded" in 2021, and D06's own 2019 baseline sentences.
- **Difficulty risk, not a shortcut:** the route is a simple three-term sum across two documents. The obvious 2021 and 2022 reviews (D04, D05) do not give the EU TWh figures.
- **Extraction gaps:** none material. All files are plain-text extractions (manifest method "text", no pages).

Files:
- D:\Dev\Docket\tasks\aq-01430\runs\q01-r0-v2-3c4106b71dd45b00932614e7a49573a3dde8d87b2888f480debf4e5220d7fdfd\shortcut\text\D06.txt
- D:\Dev\Docket\tasks\aq-01430\runs\q01-r0-v2-3c4106b71dd45b00932614e7a49573a3dde8d87b2888f480debf4e5220d7fdfd\shortcut\text\D07.txt
- D:\Dev\Docket\tasks\aq-01430\runs\q01-r0-v2-3c4106b71dd45b00932614e7a49573a3dde8d87b2888f480debf4e5220d7fdfd\shortcut\text\D04.txt
- D:\Dev\Docket\tasks\aq-01430\runs\q01-r0-v2-3c4106b71dd45b00932614e7a49573a3dde8d87b2888f480debf4e5220d7fdfd\shortcut\text\D05.txt
