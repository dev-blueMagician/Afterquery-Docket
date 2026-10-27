# q02 rev 1 informative mapping probe, left out: D06, D07 and D09 (Docs 6, 7, 9; none ticked) - packet q02-r1-alt-t6/shortcut (renumbered: original D08 -> D06, original D10 -> D07), 2026-10-08
Question identical to q02 rev 1 (tested_sha256 53dd017c0f9da582fc906b18dfc8a11177ed8e5ea1f0f0c8d41f7387eb1dd1f8).
Purpose (rev 0 review): test whether the ticked documents (Doc 5, Doc 10) carry the Software services mapping without the reclassification note (Doc 9) or the 2Q25 overlap (Docs 6, 7).
Transcript audit (audit_transcript2.py): 19 tool calls (Glob, Grep, Read, handback), all inside the packet (clean).

answer: +15.3% (2Q26 Software services 15.3% higher than 1Q24)
confidence: high; forced best guess +15.3%, about 88%, depending on treating "Software services" as the renamed "Front office software and data" line ("No document states the rename outright").

path (probe ids; probe D07 = original D10, probe D06 = original D08):
1. 2Q26: original D10 revenue row "Software services 166 169 169 (1.8) (1.8)" (text line 223; docs line 228); footnote "GAAP 2Q26 Software services of $166 million"; no 2Q26 notable items.
2. Mapping: original D10 l.374 "Software services ARR ... annualizing the revenue from the last month of the relevant quarter for CRD and CRD for Private Markets and includes ... SaaS, maintenance and support revenue, FIX, and value-added services"; D05 l.389 (and original D08 l.360) "Front office software and data ARR ... annualizing current quarter revenue for CRD and CRD for Private Markets and includes ... SaaS, maintenance and support revenue, FIX, and value-added services": same scope, only the annualization changed. Highlights move from "Front Office Software and Data: ... ARR increased approximately 11%" (original D08 l.86) to "Software services: ... ARR increased approximately 14%" (original D10 l.75). Drivers match (original D10 l.247 On-premises, Professional services, software and data; original D08 l.238 On-premises and Professional Services, software-enabled). Sizes match (FOSD 167, 163 in 3Q25, 4Q25; Software services 169, 166 in 1Q26, 2Q26; old Software and processing fees 227, 221). Original D10's six fee lines sum to total fee revenue 3,188 with no lending-fee line; under the old layout Software and processing fees = FOSD + lending (1Q24 144 + 63 = 207; 4Q25 163 + 58 = 221).
3. 1Q24: D05 l.254 (docs 268) "Front office software and data 158 197 144 (19.8) 9.7"; 14/144 = 9.7% matches; FDIC assessment is an expense.
4. 22 / 144 = 0.152778 -> +15.3%.

minimal_documents: D05 + original D10 (ARR definitions and values); original D08 supporting only. D05 irreplaceable (only 1Q24 revenue).
readings: (a) old Software and processing fees 207 -> -19.8%, weaker (no lending line in 2026; sizes and ARR scope match FOSD); (b) ex-notables same +15.3%.
gaps: no document states the rename outright (inferred); no overlapping quarter in both layouts in this packet; original D10 says only ARR was recast.
contaminated: no.

Caller classification: reaches the gold without Docs 6, 7 and 9 (informative, not a removal of a ticked document): the ticked spans (both ARR definitions on the same CRD scope, the 1Q24 split 144 + 63 = 207) carry the mapping; Doc 9 remains a number-free confirmation in the reasoning.
