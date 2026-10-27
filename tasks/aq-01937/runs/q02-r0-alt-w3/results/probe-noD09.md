# q02 rev 0 removal probe, left out: D09 (Doc 9; NOT ticked) - packet q02-r0-alt-w3/shortcut (renumbered: D10 -> D09), 2026-10-08
Question identical to q02 rev 0 (tested_sha256 aee5e0cb38f1665d5c02bc6410c8b80d5dfaa51b40b1d83490b6009504361adc).
Transcript audit (audit_transcript2.py): 24 tool calls; one Read of its own overflowed search output; otherwise inside the packet (clean).

answer: +15.3% (Software services revenue in 2Q26, $166M, was about 15.3% higher than in 1Q24, $144M)
confidence: high (about 0.85; the one inferential step is matching the renamed line)
Forced best guess: +15.3%, about 0.85.

path (probe ids): (1) 2Q26 release (probe D09 = original D10) line 216 header "2Q26 1Q26 2Q25", line 223 "Software services 166 169 169"; lines 94/256 "GAAP 2Q26 Software services of $166 million"; no 2Q26 notable items. (2) 1Q24: D05 line 254 "Front office software and data 158 197 144 (19.8) 9.7"; (158 - 144) / 144 = 9.7% matches. (3) Label match, no document stating the rename: 2Q26 release line 94 "GAAP Software services revenue of $169 million in 2Q25 included a notable item related to a client rescoping of $24 million ... adjusted 2Q25 Software services of $193 million"; D06 line 307 "GAAP Front office software and data of $169 million in 2Q25 included ... $24 million ... adjusted 2Q25 Front office software and data of $193 million"; D06 line 257 and D07 line 206 front office 2Q25 169; the 2Q26 release's 2Q25 Other fee revenue 127 = 66 + 61; management fees +38 and FX -38 recast, software line left at 169; ARR definitions both based on CRD. (4) 22 / 144 = +15.3%.

minimal_documents: 2Q26 release + D05 + D06 (D07 can replace D06); D05 has no substitute.
readings: Software and processing fees base 207 -> -19.8% (not defensible: 2Q25 is 169, not 230); ARR +32.8% (invalid); strict reading "cannot be determined" if an implied label match is not accepted (the probe considered the 2Q25 match strong enough).
contaminated: no.

Caller classification: REACHES the gold unforced without Doc 9. Doc 9 is not ticked in q02 (documents D05, D10), so this confirms the decision: ticking Doc 9 would make the platform's Document check find it not needed. Doc 9 stays an unticked explanatory source.
