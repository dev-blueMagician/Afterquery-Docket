# q02 rev 1 solver B (fresh blind-solver, packet solver-2), 2026-10-08
tested_sha256: 53dd017c0f9da582fc906b18dfc8a11177ed8e5ea1f0f0c8d41f7387eb1dd1f8
Transcript audit (audit_transcript2.py): 20 tool calls; one Read of its own overflowed search output; otherwise inside the packet (clean).

answer: +15.3% (higher)
confidence: high

path:
1. 2Q26: D10 revenue table text line 223 (docs line 228) "Software services 166 169 169 (1.8) (1.8)" (2Q26, 1Q26, 2Q25); line 94 "GAAP 2Q26 Software services of $166 million"; 2Q26 notable items "—" (line 110).
2. Meaning: D09 footnote lines 99 and 245 (reclassification of lending-related fees; caption changed to Software services; prior periods reclassified) -> Software services = old Software and processing fees minus Lending related and other fees = old Front office software and data.
3. Checks: D09 line 233 "Software services(1) 169 163 158" (1Q26, 4Q25, 1Q25): 1Q25 = D05 FOSD 158; 4Q25 = D08 line 215 163; 2Q25 D10 169 = D06 line 257 FOSD 169; D09 1Q25 Other fee revenue 99 = 32 + 67.
4. 1Q24: D05 lines 254-256 (docs 268-270): FOSD 144, Lending 63, Software and processing fees 207 -> 144 (= 207 - 63); 9.7% matches "increased 10% compared to 1Q24" (line 276); only 1Q24 notable item in Other expenses.
5. 22 / 144 = 0.152778 -> +15.3%.

minimal_documents: D05, D09, D10 (D05 only 1Q24 revenue figures; other 1Q24 hits are AUC/A and AUM tables, D02 line 158, D03 line 162; D10 only 2Q26; D09 only document stating the reclassification). Weaker substitute for D09: D06 + D10 by numbers ($169M with $24M rescoping; $193M adjusted).

readings: not like-for-like 207 base -> -19.8%, rejected; ex-notables same +15.3%; Software services ARR ($433M) is an operating metric, not revenue.

gaps: no restated 1Q24 Software services figure printed; mapping supported by the footnote and matched 1Q25, 2Q25, 4Q25. Text-only packet. Read D05 1-20, 58-112, 236-280; D09 1-130, 200-279; D10 1-130, 205-264; D01, D04; others by search.
contaminated: no
