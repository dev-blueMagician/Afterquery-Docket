# q02 rev 1 solver A (fresh blind-solver, packet solver-1), 2026-10-08
tested_sha256: 53dd017c0f9da582fc906b18dfc8a11177ed8e5ea1f0f0c8d41f7387eb1dd1f8
Transcript audit (audit_transcript2.py): 21 tool calls; one Read of its own overflowed search output; otherwise inside the packet (clean).

answer: +15.3% (higher): Software services $166M in 2Q26 against $144M in 1Q24 on the current presentation basis.
confidence: high

path:
1. 2Q26 (D10, July 16, 2026): revenue header "(Dollars in millions) 2Q26 1Q26 2Q25"; row "Software services 166 169 169 (1.8) (1.8)" (text line 223; docs line 228); footnote "GAAP 2Q26 Software services of $166 million"; 2Q26 notable items "—".
2. D09 footnote (1) line 245 (and (b) line 99): lending-related fees reclassified to Other fee revenue and the caption changed to Software services, prior periods reclassified -> Software services = old Software and processing fees minus Lending related and other fees = old Front office software and data. Checks: 1Q25 D09 158 = D05 FOSD 158 = 225 - 67; 4Q25 D09 163 = D08 line 215; 2Q25 D10 169 (adjusted 193) = D06/D07 FOSD $169M (adjusted $193M).
3. 1Q24 (D05 revenue table, header "1Q25 4Q24 1Q24 % QoQ % YoY"; docs lines 268-270): "Front office software and data 158 197 144 (19.8) 9.7"; "Lending related and other fees 67 62 63 8.1 6.3"; "Software and processing fees 225 259 207 (13.1) 8.7" -> 144 (= 207 - 63); 14/144 = 9.7% matches; only 1Q24 notable item the FDIC assessment in Other expenses.
4. 22 / 144 = 0.152778 -> +15.3%.
5. No other 1Q24 fee-line figure (D02 3Q24/2Q24/3Q23; D03 4Q24/3Q24/4Q23; D01, D04 no quarterly software revenue).

minimal_documents: D10 + D05 + D09 (explicit definition). Weaker alternative D10 + D05 + D06 (or D07) by matching numbers (2Q25 $169M with $24M rescoping, adjusted $193M): an inference, not a stated definition.

readings: 1Q24 base as "Software and processing fees" (207): -19.8%, rejected (lending fees moved out, prior periods reclassified). Ex-notables: same +15.3%.

gaps: no recast 1Q24 "Software services" figure printed; 144 from D05's FOSD via D09's note, confirmed for 1Q25, 2Q25, 4Q25. Text-only packet. Read D09 60-270; D10 1-130, 205-264, 368-387; D05 1-30, 90-111, 240-284; D01 1-40; D04 1-32; D02, D03, D06, D07, D08 by keyword search. Did not read question.txt.
contaminated: no
