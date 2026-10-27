# q02 rev 1 shortcut audit (fresh shortcut-auditor, packet shortcut), 2026-10-08
tested_sha256: 53dd017c0f9da582fc906b18dfc8a11177ed8e5ea1f0f0c8d41f7387eb1dd1f8
Transcript audit (audit_transcript2.py): 30 tool calls (Glob, Grep, Read, handback), all inside the packet (clean).

answer: +15.3%. Software services $166M in 2Q26 and $144M in 1Q24 on the recast basis: (166 - 144) / 144 = 22 / 144 = 15.28%.
verdict: clear

shortest_path:
1. D10 REVENUE table text line 223 "Software services 166 169 169 (1.8) (1.8)" (2Q26 / 1Q26 / 2Q25); line 94 "GAAP 2Q26 Software services of $166 million"; no 2Q26 notable items (lines 105-110).
2. Caption mapping: D09 footnote (1) line 245 (same at line 99) -> Software services = Software and processing fees - Lending related and other fees = old FOSD. Recast values match the old line: D09 1Q25 158 = D05 FOSD 158 (225 - 67); D09 4Q25 163 = D08 FOSD 163 (221 - 58); D10 2Q25 169 = D06 FOSD 169 (230 - 61); D10 adjusted 2Q25 $193M = D06 adjusted FOSD $193M.
3. 1Q24: D05 REVENUE lines 247-256 (1Q25 / 4Q24 / 1Q24): FOSD 144; Lending 63; Software and processing fees 207 -> 144 = 207 - 63. 2025 releases did not restate FOSD for 2024 quarters (2Q24 152 in D02 and D06; 3Q24 146 in D02 and D07; 4Q24 197 in D03 and D08).
4. +15.3%.

sufficient_documents: D10 + D05 + D09; alternative to D09 for the mapping: D10 + D05 + D06 (2Q25 169 and $193M adjusted), or D07/D08 likewise. "D10 + D05 alone is not enough to verify the mapping; a reader would have to guess it from D10's narrative (On-premises, Professional services, software and data revenues)." D05 the only document with 1Q24 software revenue; no YTD or full-year software line.

searches: "software services", "software", "front office software", "software and processing", "lending related", "reclassif / caption / previously / formerly / renamed / conform", "1Q24", "March 31, 2024 / first quarter of 2024 / Q1 2024", "2024 / two years" in D10, Charles River / CRD / SaaS in D01 and D04; revenue tables read in D05, D09, D10; rows grepped in D02, D03, D06-D08; key lines confirmed in docs/. Shortcut attacks: no document states a 2Q26 vs 1Q24 comparison; no single document holds both endpoints; no YTD line for 1Q24; the wording does not give away the mapping.

readings/gaps:
- Trap: simple rename, 1Q24 Software and processing fees 207 -> -19.8%; ruled out by D09's footnote.
- Ex-notables: same +15.3%.
- 1Q24 only as a prior-year comparative in the Q1 2025 release; FOSD stable across overlapping releases, so 144 is robust.
- Difficulty risk, not a shortcut: once the D09 footnote is connected to D05's 1Q24 FOSD row, a one-step percent change; the main separator is avoiding the 207 trap.
- Contamination: none.

Caller note: the auditor judged D05 + D10 alone insufficient to *verify* the mapping (it did not weigh the two ARR definitions); the separate mapping probe without Docs 6, 7 and 9 reached the gold at 0.88 from those definitions (runs/q02-r1-alt-t6/results/probe-noD06-D07-D09.md).
