# q01 rev 0 - removal probe without D09 (CMA207, platform Doc 9), 2026-10-06

Packet: runs/q01-r0-probe-t5/solver-2 (byte copy of solver-1 minus D09, ids renumbered D01-D10 so the
short guide is D09 inside the probe; neutral run name). Fresh blind-solver; question verbatim plus
"Answer from this packet's documents only. If they do not settle the answer, still commit to a single
forced best guess and state your probability (0-1) that it is correct."

Raw return as received:

**Not answerable from the packet** — the short guide lists 7 banned pressure-selling behaviours, but no document in the packet says which banned practices can lead to prosecution. Forced best guess: **6** (probability ≈ 0.55), based on my own unverified recollection of UK law rather than the documents.

    answer: Not answerable from this packet. Forced best guess: 6 of the 7 named behaviours (probability ~0.55).
    confidence: low (for the guess); high that the packet does not settle it
    path:
     1. Short guide = D09 (probe numbering; text/D09.txt), L13 "This is a short guide to the unfair commercial practices guidance to help businesses understand what they need to do." L67 practices "unfair in all circumstances and are always prohibited"; L69 "full list of 32 banned practices".
     2. D09 L89-91 "Pressure selling": "exaggerating the risks they face, pretending they have ordered something when they haven't, refusing to leave their home, hassling them by repeatedly contacting them, or making them feel they can't leave your shop without buying something. You mustn't ask children to buy products, or tell customers that if they don't buy your product then your livelihood will be at risk." → 7 behaviours.
     3. Only one behaviour is tied to a provision: D08 L63 refusing to leave "would be a breach of paragraph 27 of Schedule 20 to the DMCC Act" — not stated to be an offence.
     4. Only civil consequences in the packet: D09 L57 "The CMA and the courts can now fine traders ... up to 10% of their worldwide turnover. You may also have to compensate affected consumers." D10 paras 5 and 12 (probe numbering) say TSS and the CMA "enforce" the rules, no prosecution.
     5. Searched text/ and docs/ for prosecut|offence|offense|criminal|guilty|convict|imprison: no hit concerns banned practices (D08 L91 offence under the 2013 regulations; D08 L111/121 an example trader threatening "criminal proceedings"; D05 L91 a US FTC "Notice of Penalty Offenses").
     6. The missing fact is which Schedule 20 paragraphs are criminal offences (the Act's offences section or the full CMA guidance's offences chapter); neither is in the packet.
     Basis for the guess (outside the packet, unverified): under the CPUTRs 2008 every banned practice was an offence except the paid advertorial and the direct appeal to children; believed still excluded under the DMCC Act → 7 − 1 = 6.
    minimal_documents: D09 (probe numbering; the list of 7); no packet document supplies prosecutability.
    readings: strict packet reading 0 established; "prosecuted" as any enforcement 7; children also an offence 7; only the five "for example" items 5.
    gaps: offences provision and Schedule 20 numbers for 6 of the 7 not in the packet; US FTC docs searched not read in full; D04, D06-D10 (probe numbering) read in full.
    contaminated: no

Caller adjudication: not answerable from the remaining documents; the forced guess equals the gold
(p 0.55) through recalled CPUTRs law. Platform document-check risk for Doc 9: moderate (the high model
may answer "cannot be determined", which counts as needed, or recall the exclusion and answer 6).
Fallback: the one-line reviewer note ("Doc 9 is the only document stating which banned practices are
criminal offences (note 112 excludes paragraph 30)").
