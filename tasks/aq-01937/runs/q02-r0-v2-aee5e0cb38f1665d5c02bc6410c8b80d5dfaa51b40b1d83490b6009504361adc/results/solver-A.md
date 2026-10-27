# q02 rev 0 solver A (fresh blind-solver, packet solver-1), 2026-10-08
tested_sha256: aee5e0cb38f1665d5c02bc6410c8b80d5dfaa51b40b1d83490b6009504361adc
Transcript audit (audit_transcript2.py): 27 tool calls; one Read of its own overflowed search output; otherwise inside the packet (clean).

answer: +15.3% (Software services revenue was about 15.3% higher in 2Q26, $166M, than in 1Q24, $144M)
confidence: high

path:
1. 2Q26 (D10, docs/stt_ex991_2026-07-16.txt): revenue table text line 223 (source 228) "Software services 166 169 169 (1.8) (1.8)", columns 2Q26, 1Q26, 2Q25; line 94 "GAAP 2Q26 Software services of $166 million"; 2Q26 notable items "—".
2. Rename (D09 footnote (1) line 245, repeated line 99): "Lending related and other fees, previously recognized within Software and processing fees, was reclassified to Other fee revenue, and the Software and processing fees caption has been changed to Software services. Prior-period amounts have been reclassified to conform to the current presentation." Checks: D09 line 233 "Software services(1) 169 163 158": 1Q25 158 = D05 line 254 front office 158; 4Q25 163 = D08 line 215; D10's 2Q25 169 = D06 line 257 (not the old 230 total); recast 1Q25 Other fee revenue 99 = 32 + 67.
3. 1Q24 (D05, 1Q25 release): line 254 (source 268) "Front office software and data 158 197 144 (19.8) 9.7"; Lending 63; Software and processing fees 207; 144 + 63 = 207; only 1Q24 notable item the $130M FDIC assessment in Other expenses.
4. (166 - 144) / 144 = 0.152777 -> +15.3%.

minimal_documents: D05, D09, D10 sufficient (D05 only document with 1Q24; D10 only with 2Q26; D09 states the mapping). D06 or D07 could replace D09 by matching values (2Q25 $169M with the same $24M client rescoping), weaker than the footnote.

readings: old name treated as the new name: (166 - 207) / 207 = -19.8%; not on the same basis. Ex-notables: unchanged +15.3%.

gaps: 1Q24 only from D05's comparative column; current-basis 1Q24 inferred from D09's footnote and exact matches. Searched all ten files for "software"; read D01 and D04 in full; deciding rows checked against docs/.
contaminated: no
