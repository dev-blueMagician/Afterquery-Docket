# q02 rev 0 shortcut audit (fresh shortcut-auditor, packet shortcut), 2026-10-08
tested_sha256: aee5e0cb38f1665d5c02bc6410c8b80d5dfaa51b40b1d83490b6009504361adc
Transcript audit (audit_transcript2.py): 28 tool calls (Glob, Grep, Read, handback), all inside the packet (clean).

answer: +15.3%. Software services $166M in 2Q26 and $144M in 1Q24: (166 - 144) / 144 = +15.28%.
verdict: clear

shortest_path:
1. D10 text line 223 (header "2Q26 1Q26 2Q25"): "Software services 166 169 169 (1.8) (1.8)"; no notable item in this line in 2Q26.
2. Bridge: D09 lines 99 and 245 (reclassification note): Software services = old Software and processing fees minus Lending related and other fees = old Front office software and data. Overlaps: 1Q25 D09 158 = D05 front office 158 (not 225); 2Q25 D10 169 = D06 169, with the $24M client-rescoping notable item in that line in both; 4Q25 D09 163 = D08 163.
3. D05 line 247 header "1Q25 4Q24 1Q24", line 254 "Front office software and data 158 197 144 (19.8) 9.7": 1Q24 = $144M; cross-check 207 - 63 = 144 (lines 256, 255).
4. 22 / 144 = 0.152777 -> +15.3%.

sufficient_documents: D05 + D09 + D10; the bridge can come from D06 instead of D09 (2Q25: 169 in D06 and D10). No single document: 2Q26 only in D10, 1Q24 revenue lines only in D05. D05 + D10 alone leave the mapping to inference from descriptions (CRD on-premises, professional services, software and data, the ARR definition) because they share no quarter: plausible but not verified.

searches: "software"; "software services|software-enabled|SaaS|on-premises|professional services"; "reclassif|caption|recast|conform to the current"; row regex for Front office software and data / Lending related and other fees / Software and processing fees / Software services (text\ and docs\); "1Q24"; "FY24|full-year"; quarter headers. D01 and D04 have no revenue-line data; "1Q24" in D02/D03 only in AUM rollforwards; D03 has no full-year table by line; D10 has no 1Q24 column. Front office software and data 2024-2025 values consistent in every edition (2Q24 152, 3Q24 146, 4Q24 197, 1Q25 158, 2Q25 169, 3Q25 167, 4Q25 163); no other restatement.

readings/gaps:
- Wrong reading: renamed caption matched to old Software and processing fees: 1Q24 = 207, (166 - 207) / 207 = -19.8%; ignores the lending-fee reclassification and the overlaps; "the main difficulty risk". "The figure '(19.8)' printed in D05 line 254 is only a coincidence" (the line's QoQ change).
- Ex-notables: no change.
- No disqualifying shortcut: no single-document comparison; wording gives nothing away; ordinary cross-document work (a caption bridge plus a ratio).
- Context note: auto-attached git status (file names only); not contamination.
