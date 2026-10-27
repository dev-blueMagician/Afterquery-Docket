# Removal probe return: q04 rev 0 without Doc 2 (D01)

- Date: 2026-10-08
- tested_sha256: eac6be225d1a155bb5ad5a0fba29143f2b2ea6d6b556c6acad6ff6a65f0ab4dc
- Packet: tasks/aq-02157/runs/q04-r0-alt-f2/solver-2 (Doc 1 -> D01, Doc 4 -> D02, Doc 5 -> D03, Doc 3 -> D04; neutral headers)
- Role: blind-solver (fresh context, question only)

Raw return (verbatim):

answer: 13.1%. The minimum duty on a 20-pack rose from £6.9572 (about £6.96) to £7.87.
confidence: medium-high. The arithmetic is certain. The only doubt is the label "smokefree consultation response", discussed under readings.

path:
1. Pack-insert impact assessment (D02). Header: "Title: Tobacco pack inserts", "IA No: 9609", "Date: May 2023", "Stage: Consultation". In the rates table at D02.txt lines 1795-1806 (under "Duty rate (October 2021)", Cigarettes, "Highest of:"):
   - "£262.90 per 1,000 cigarettes plus 16.5% of retail price"
   - "£347.86 per 1,000 cigarettes (MET)"
   MET is the minimum excise tax, the floor in the "Highest of" rule. Para 123 (line 1811) confirms that idea: the average pack "is above the MET threshold".
   For a 20-pack: £347.86 x 20 / 1,000 = £6.9572 (about £6.96).
2. Smokefree consultation (D01, "Creating a smokefree generation and tackling youth vaping: your views"). Line 646: "tobacco has VAT and duty (at least a £7.87 duty on a packet of 20 cigarettes)". "At least" on a 20-pack is the minimum-duty figure.
3. Calculation: (7.87 - 6.9572) / 6.9572 = 0.9128 / 6.9572 = 0.13120 -> 13.120% -> 13.1%.
   - Check: using the rounded £6.96 gives 0.91 / 6.96 = 13.07% -> 13.1%.
   - Per-1,000 check: £7.87 x 50 = £393.50; (393.50 - 347.86) / 347.86 = 13.12%.
4. Exclusions:
   - D02's "£7.98 duty paid per pack" (line 1811) is the estimated duty on an average-priced pack, not a minimum. Using it would give a fall of -1.4%, which contradicts "rise".
   - D02's specific-duty-only figures are not the minimum: £262.90/1,000 in the table, and a different £294.72/1,000 (£5.89 per pack) in para 123.
   - D03 and D04 contain no duty figures: the search for excise|duty|duties|per 1,000|20 cigarettes found nothing in either.

minimal_documents: D01 + D02. No other document can replace either one. D03 is the pack-insert consultation government response and D04 is the pack-insert consultation; neither gives any duty figure.

readings:
- Main reading: "smokefree consultation response" means D01, the only smokefree-generation document in the packet, giving 13.1%. D01 is the consultation itself, not a government response. It says "The consultation closes on 6 December 2023 ... you can respond via our online survey", and its URL ends "...-your-views". So the question's "response" wording does not strictly match D01, but D01 holds the only 20-pack minimum-duty figure in any smokefree document.
- Strict reading: if the phrase means the government's later response to the smokefree consultation, that document is not in the packet, so the answer is "not answerable from the packet". From memory and unverified: if that response restated the minimum duty using the rate after November 2023 (MET about £421.48 per 1,000, or about £8.43 per pack), the answer would be about 21.2%. I found no documentary support for this.
- Another possible target is D03, the pack-insert government response, whose summary is headed "Creating a smoke-free UK". It has no duty figures, so on that reading the question is not answerable.

gaps:
- The government response to the smokefree consultation is not in the packet.
- I did not read the documents in full. I searched all four with targeted terms (excise / duty / MET / minimum / per 1,000 / £ amounts / 20-pack, smokefree, respon) and read these sections:
  - D01: lines 1-60 and 636-680
  - D02: lines 1-80, 1726-1733, 1780-1839 and 3312-3336
  - D03 and D04: lines 1-60 each
- I did not read the docs\ folder, as instructed.
- The text extraction has no page markers and there is no layout file, so I could not check the D02 table against the original PDF. The MET row does extract cleanly.
- D02 is internally inconsistent: the table says "October 2021", but para 123 uses a different specific rate (£294.72). This does not change the printed MET of £347.86.

contaminated: no

forced_guess: 13.1%
forced_guess_probability: 0.82
forced_guess_source: documents
