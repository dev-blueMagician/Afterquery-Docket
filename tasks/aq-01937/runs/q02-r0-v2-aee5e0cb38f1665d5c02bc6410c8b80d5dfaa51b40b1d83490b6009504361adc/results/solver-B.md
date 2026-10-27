# q02 rev 0 solver B (fresh blind-solver, packet solver-2), 2026-10-08
tested_sha256: aee5e0cb38f1665d5c02bc6410c8b80d5dfaa51b40b1d83490b6009504361adc
Transcript audit (audit_transcript2.py): 19 tool calls (Glob, Grep, Read, handback), all inside the packet (clean).

answer: +15.3% (Software services was about 15.3% higher in 2Q26 than in 1Q24: $166M vs a recast $144M)
confidence: high

path:
1. D10 revenue table, line 216 header "2Q26 1Q26 2Q25", line 223 "Software services 166 169 169 (1.8) (1.8)": $166M; no 2Q26 notable items (lines 107-110 "—"); line 94 "GAAP 2Q26 Software services of $166 million".
2. D09 line 99 / footnote (1) line 245: "Lending related and other fees, previously recognized within Software and processing fees, was reclassified to Other fee revenue, and the Software and processing fees caption has been changed to Software services. Prior-period amounts have been reclassified to conform to the current presentation." Recast Software services = old Software and processing fees minus Lending related and other fees = old Front office software and data.
3. D05 revenue table (line 247 header "1Q25 4Q24 1Q24"): line 254 "Front office software and data 158 197 144"; line 255 "Lending related and other fees 67 62 63"; line 256 "Software and processing fees 225 259 207". Recast 1Q24 = 207 - 63 = 144 = printed front office 144.
4. Mapping holds elsewhere: 1Q25 D09 158 = D05 FOSD 158; 4Q25 D09 163 = D08 line 215 FOSD 163; 2Q25 D10 169 = D06 line 257 FOSD 169. New Other fee revenue = old Other + Lending: 32 + 67 = 99 (D09); 59 + 58 = 117 (D09); 66 + 61 = 127 (D10).
5. (166 - 144) / 144 = 22 / 144 = 0.152778 -> +15.3%.

minimal_documents: D05, D09, D10. D09 is the only document that explicitly defines the reclassification; D10 has no "reclassif", "Lending related" or "Software and processing" text. A weaker alternative to D09: infer the mapping from numbers alone (D06 2Q25 FOSD 169 = D10 2Q25 Software services 169), but nothing would state it. D05 is the only document with a 1Q24 column for this line (D02 3Q24/2Q24/3Q23; D03 4Q24/3Q24/4Q23).

readings:
- Mixed-caption comparison (old 1Q24 Software and processing fees $207M): (166 - 207) / 207 = -19.8%; not like-for-like.
- Excluding notable items: same +15.3% (1Q24's FDIC item sits in Other expenses; 2Q26 none).

gaps: no printed recast 1Q24 "Software services" figure anywhere; derived from D05 rows and D09's definition, confirmed by the printed FOSD 144. Original 1Q24 release not in the packet. Searched all ten text files for software, Front office, Lending related and reclassification terms; read the revenue tables, highlights and footnotes of D05, D09, D10 and all of D01 and D04.
contaminated: no
