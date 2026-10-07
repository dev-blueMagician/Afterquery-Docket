# q01 rev 0 - shortcut audit (raw, verbatim)

- Date: 2026-10-06. Fresh shortcut-auditor agent (claude-opus-5-5, omitClaudeMd, scope hook), given
  only the workspace root, the shortcut packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 61ba023040204aa9fed82b996bd73e101e327afa4c6a97a7741ec4bf96a62cce

## Return

answer: $948 million. This is Colgate's FY2025 Africa/Eurasia net sales excluding Russia and Belarus, which became part of Europe, Middle East &amp; Africa (EMEA).

verdict: clear

shortest_path:
1. The mapping is in D11 (`docs/cl_ex991_2026-05-01.txt`), line 85: "The results of the Europe and Africa/Eurasia (excluding Russia and Belarus) reportable operating segments and the skin health business (previously within the North America reportable operating segment) have been combined in a new Europe, Middle East &amp; Africa reportable operating segment. In conjunction with this realignment, Russia and Belarus, which were previously reported within the Africa/Eurasia reportable operating segment, are now reported within the Asia Pacific reportable operating segment."
2. D09 (`cl_ex991_2026-01-30`, Table 5) gives FY2025 net sales under the old structure: North America 4,045, Latin America 4,776, Europe 2,962, Asia Pacific 2,814, Africa/Eurasia 1,172. Oral, Personal and Home Care totals 15,769.
3. D10 (`cl_ex991_2026-03-17`, recast segment table) gives recast FY2025: North America 3,679, Latin America 4,776, EMEA 4,276, Asia Pacific 3,038. The total is the same 15,769.
4. Russia and Belarus = 3,038 − 2,814 = 224. Africa/Eurasia excluding them = 1,172 − 224 = **948**.
5. Independent check: skin health = 4,045 − 3,679 = 366, so 4,276 − 2,962 − 366 = **948**. Both routes agree, and Latin America is unchanged.
6. The quarterly figures agree up to rounding. Nine months: 863 − (2,259 − 2,092) = 696. Q4: 309 − (779 − 722) = 252. Q3 EMEA check: 801 + 236 + 77 = 1,114 against a reported 1,115.
7. The earlier recast effective July 1, 2024 (footnotes in D04, D05 and D06) moved Europe's skin health into North America. So in FY2025 all of skin health sat in North America, which fits step 5.

sufficient_documents: D09, D10 and D11 are all required, and I found no alternatives.
- D11 is the only document that states the mapping.
- D10 is the only source of recast FY2025 figures; D11 and D12 carry recast comparatives only for Q1, Q2 and the first half of 2025.
- D09 supplies the old-structure FY2025 figures. D08 plus D09's Q4 would also work, but still needs D09.
- No single document gives the answer, and the question's wording doesn't give it away.

searches:
- Terms: recast, realign, reorganiz, previously reported, new segment, Middle East, EMEA, Eurasia, effective January 1, Russia, Belarus, skin health, Filorga/EltaMD/PCA SKIN, and the segment table rows.
- Read in full: the manifest, D09 and D10. Read D11 lines 1–140 and the opening of D01, which is a 2019 performance stock unit award agreement and irrelevant.
- D02–D08 and D12 were searched by grep only, not read in full.
- Russia/Belarus appear only in D11 line 85, in both `text/` and the raw `docs/` (only `cl_ex991_2026-05-01.txt`), so this is not an extraction gap.
- D12's footnote only says recast data is on the website and gives no mapping.
- I did not read question.txt, notes or anything outside the packet, and no contamination was seen.

readings/gaps:
- Wrong answers a solver could reach:
  - 1,172: the whole Africa/Eurasia segment, which ignores Russia and Belarus moving to Asia Pacific.
  - 1,314: EMEA minus Europe, which wrongly counts skin health as coming from Africa/Eurasia.
  - 947: summing the four recomputed quarters, a rounding artifact. The full-year tables give 948 by both routes.
- Without D11, the numbers alone (North America −366, Asia Pacific +224, EMEA 142 above Europe plus Africa/Eurasia) fit several transfer patterns, giving 948 or 1,172 among others. So D11's footnote is the deciding input.
- Difficulty risk, not a shortcut: the answer comes from one footnote plus two subtractions. A strong reader would find the footnote quickly by searching "Africa/Eurasia" or "recast", but the answer still needs three documents joined.
- No unresolved extraction gaps that affect the answer.

Relevant files (all under `D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q01-r0-v2-61ba023040204aa9fed82b996bd73e101e327afa4c6a97a7741ec4bf96a62cce\shortcut\`):
- `text\D09.txt`
- `text\D10.txt`
- `text\D11.txt`
- `docs\cl_ex991_2026-05-01.txt`
