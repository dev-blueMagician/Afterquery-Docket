# q01 rev 0 - blind solver B (fresh blind-solver context, packet solver-2)

Date: 2026-10-05. tested_sha256: 4f49c8dd057866863e7d56d99a0d8fd480d1dd1a37da4b261ee9d10c52b14c16
Task message: workspace root, packet path solver-2, exact question text only.

Raw return (verbatim):

answer: **47.0%** (493 million pounds sold in 1H 2026 ÷ 1.05 billion pounds full-year projection in force when the Cerro Verde stake was raised in May 2026 = 46.95% → 47.0%)

confidence: high

path:
1. **Timing of the stake increase** — D04 (2Q 2026 release, filed 2026-07-23), line 921: "In May 2026, FCX increased its ownership interest in Cerro Verde from 55.08% to 55.66%." Corroborated at line 39 ("During second-quarter 2026, FCX purchased 2.0 million shares of Cerro Verde common stock in the open market for $107 million, increasing its ownership interest in Cerro Verde from 55.08% to 55.66%") and footnote b, lines 457/511 ("FCX's interest in Cerro Verde is 55.66%, and prior to May 2026 it was 55.08%").
2. **Projection in force in May 2026** — D03 (1Q 2026 release, filed 2026-04-23), line 227: "Copper sales from South America operations are expected to approximate 1.05 billion pounds for the year 2026." D03 line 197 still describes Cerro Verde as "(55.08%-owned)", confirming this guidance predates the stake increase.
3. **Later (post-increase) guidance, for contrast** — D04 line 221: "Copper sales from South America operations are expected to approximate 1.0 billion pounds for the year 2026."
4. **First-six-months 2026 sales** — D04 line 205 (South America operating data, Six Months Ended June 30, 2026 column): "Sales|245|265|493|540". Confirmed by D04 supplemental schedule line 1423 ("Copper sales (millions of recoverable pounds)|493") and by quarterly sum: Q1 248 (D03 line 209) + Q2 245 (D04 line 205) = 493.
5. **Calculation** — 493 ÷ 1,050 = 0.469524 → 46.95% → **47.0%**. (Check: 1,050 × 0.469524 = 493.0.) Units consistent (millions of recoverable pounds of copper).

minimal_documents: D03 + D04. D04 supplies the stake-increase timing and the six-month sales; D03 supplies the guidance in force in May. Neither is replaceable: D01/D02 are BHP operational reviews whose only "Cerro" references are BHP's Cerro Colorado (D02 lines 55, 70, 156, 393; D01 line 327).

readings:
- Alternative (if "at the time" were read as the projection in D04, the release that first disclosed the stake increase): 493 ÷ 1,000 = **49.3%**. Rejected as the primary reading because that guidance was issued in July, after the May purchase.

gaps:
- No Freeport communication dated between 2026-04-23 and 2026-07-23 exists in the packet; the answer assumes the April guidance remained the operative projection in May (nothing in the packet indicates an interim change before the July update).
- Manifest lists all documents as plain text with no pages; no Dnn.layout.txt files or PDFs exist to inspect original pages (relevant tables extracted cleanly and are internally consistent).
- D01/D02 checked by keyword search only (not read in full); D03/D04 read only in the relevant sections (highlights, outlook, South America section, noncontrolling-interest note, South America six-month supplemental schedule).
- Did not open the packet's question.txt.

contaminated: no

Files read (as reported by the solver): solver-2\text\D03.txt, solver-2\text\D04.txt, solver-2\text\manifest.json
