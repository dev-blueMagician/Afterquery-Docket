# q03 rev 1 shortcut audit (fresh shortcut-auditor, packet shortcut), 2026-10-08
Question identical to rev 1 (tested_sha256 993076f2a58c67f3f234ea9ca851b4cd79a01733398a02ccf2428d51fec31b03).
Agent id ac678c19899bf73cd. Transcript audit (audit_transcript2.py): 19 tool call(s) (Glob, Grep, Read, handback), all inside the packet (clean).
Verbatim return follows.

answer: 16.6%. Under the reclassified basis, GAAP FX trading services revenue went from $337M in 1Q25 to $393M in 2Q25. (393 − 337) / 337 = 56 / 337 = 16.617%, which rounds to 16.6%.

verdict: clear

shortest_path:
1. D10 (stt_ex991_2026-07-16, the 2Q26 release), revenue table (columns 2Q26 / 1Q26 / 2Q25):
   - Line 224: "Other fee revenue 138 107 127". This is the only place where 2Q25 other fee revenue is $127M, so it identifies the classification adopted in 1Q26.
   - Line 221: "Foreign exchange trading services 494 435 393", so 2Q25 is $393M.
   - Footnotes (e)/(a), lines 93 and 255: "GAAP FX trading services revenue of $393 million in 2Q25 included a notable item … $3 million". This confirms $393M is the GAAP figure.
2. D09 (stt_ex991_2026-04-17, the 1Q26 release), line 231 (columns 1Q26 / 4Q25 / 1Q25): "Foreign exchange trading services(1) 435 350 337", so 1Q25 is $337M.
   - Footnote (1), lines 99 and 245: "revenue related to distribution and marketing activities was reclassified from Foreign exchange trading services to Management fees. Additionally, Lending related and other fees … was reclassified to Other fee revenue … Prior-period amounts have been reclassified."
   - D09 and D10 use the same basis: their shared 1Q26 column matches (FX 435, Other fee revenue 107, Software services 169). D09 shows no notable items in 1Q25, so $337M is GAAP.
3. (393 − 337) / 337 = 16.6%.

Reconciliation to the original basis (all consistent):
- 2Q25, from D06 lines 254–260: FX 431, Management fees 562, Other fee revenue 66, Lending related 61.
  - 66 + 61 = 127.
  - 431 − 38 = 393, and 562 + 38 = 600, which matches D10's management fees.
- 1Q25, from D05 lines 251–257: FX 362, Management fees 562, Other fee revenue 32, Lending related 67.
  - 32 + 67 = 99, which matches D09.
  - 362 − 25 = 337, and 562 + 25 = 587, which matches D09.
- Total fee revenue is unchanged between bases: 2,719 for 2Q25 and 2,570 for 1Q25.

sufficient_documents: D10 + D09, and there is no alternative pair.
- D10 is the only document with both the $127M anchor and the 2Q25 FX figure on the new basis.
- D09 is the only document with 1Q25 FX on the new basis, and the only place the 1Q25 reclassification amount ($25M) can be seen.
- No single document has both quarters on the new basis. Neither D09 nor D10 has a five-quarter revenue table; D09's five-quarter table covers AUM only.

searches:
- Literal terms: "127"; "other fee revenue/other fee"; "foreign exchange trading|FX trading"; "\b(337|393)\b"; "reclassif|recast|conform to the current|current presentation|change in presentation"; "distribution and marketing|will be reclass|beginning in the first quarter|Software services".
- Read in full: manifest, D10, D09, D01 (2024 UBS conference deck) and D04 (2025 SSGA deck). D01 and D04 are not relevant.
- Read in part: D06 (highlights, notable items, revenue section) and D05 (revenue table).
- Checked by grep only: D02, D03, D07 and D08. All are on the old basis; FX lines are D07 "416 431 374" and D08 "405 416 360". The "recast" hits in these files were the word "forecast", so none of them pre-announces the reclassification or shows recast tables.

readings/gaps:
- Main trap: on the old basis the QoQ change is 19.1%, printed directly in D06 ("Foreign exchange trading services 431 362 336 19.1 28.3", and "increased 19% compared to 1Q25"). It is ruled out because 2Q25 other fee revenue on that basis is $66M, not $127M.
- Ex-notables on the new basis: (390 − 337) / 337 = 15.7%. Ruled out because the question asks for GAAP.
- Mixing bases gives invalid answers: 393 / 362 → 8.6%, and 431 / 337 → 27.9%.
- Difficulty risk, not a shortcut: the route is two quick lookups plus a ratio. The $127M figure appears only in D10, and D09's reclassification footnote leads straight to the 1Q25 comparative, so a strong reader will solve it quickly. That is an allowed cross-document route.
- Gaps: none material. D02, D03, D07 and D08 were not read line by line, but the targeted greps cover the possible shortcuts. The manifest says every document was extracted as plain text, so there are no extraction gaps.
- Contamination: none. The session's system context included a git-status list of repo file names, mostly for a different task, but nothing about this question, its key or its reasoning. I did not open any of those files, or the packet's question.txt.

Files:
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01937\runs\q03-r1-v2-993076f2a58c67f3f234ea9ca851b4cd79a01733398a02ccf2428d51fec31b03\shortcut\text\D10.txt
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01937\runs\q03-r1-v2-993076f2a58c67f3f234ea9ca851b4cd79a01733398a02ccf2428d51fec31b03\shortcut\text\D09.txt
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01937\runs\q03-r1-v2-993076f2a58c67f3f234ea9ca851b4cd79a01733398a02ccf2428d51fec31b03\shortcut\text\D06.txt (old-basis distractor)
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01937\runs\q03-r1-v2-993076f2a58c67f3f234ea9ca851b4cd79a01733398a02ccf2428d51fec31b03\shortcut\text\D05.txt (old-basis 1Q25)
