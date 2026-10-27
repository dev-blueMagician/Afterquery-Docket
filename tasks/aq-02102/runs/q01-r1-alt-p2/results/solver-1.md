# q01 rev 1 removal probe: solver-1 (left out D01 = Doc 2)

- Date: 2026-10-08
- Role: blind-solver (fresh, omitClaudeMd), packet tasks/aq-02102/runs/q01-r1-alt-p2/solver-1 (renumbered D01-D04)
- Question: verbatim q01 rev 1 (tested_sha256 8b03da09facfd900e42756fe23f4b662486b20d196a4d13286e9c14c89b1b04b)
- Input: workspace root, packet path, question, and the instruction to add a forced guess with probability if not answerable
- Packet ids (probe-map.json): D02->D01, D03->D02, D04->D03, D05->D04

## Raw return (verbatim)

answer: not answerable from this packet (2023 side computable: individuals 112 of 117 responses = 95.73%; no 2021-22 response counts exist in the packet). Forced best guess: a fall of ≈ 1.80 percentage points, probability ≈ 0.01 that it is correct — based on no document (see basis below).

confidence: high (that the packet cannot answer it); forced guess very low

path:
1. 2023 consultation = D02 (text/D02.txt), Cabinet Office post-consultation report: L28 "which began on 6 March 2023 and closed on 14 May 2023". Para 3.9 (L189): "The Cabinet Office received 107 responses in total ... which in some way addressed the consultation questions. These consisted of 102 responses from individuals and five responses from organisations. In addition another ten responses were received from individuals that did not address the questions posed by the consultation". Table 2 (L205-209) matches: "Individuals|Email|102", "Total||107"; its row "Of which: Queried the effect of the remedy (i.e. didn't answer the consultation questions in all respects)|68" is a subset of the 102, not additive. Including those addressing no question: individuals 102 + 10 = 112; total 107 + 10 = 117; 112/117 = 95.7265% → 95.73%.
2. 2021-22 consultation = D01 (text/D01.txt), the consultation paper itself: L32 "From 22/11/2021 to 17/01/2022" (L9 typo "ends on 17 January 2021" immaterial); L56 "A response to this consultation exercise is due to be published by 10 February 2022" — that response document is not in the packet. D01 ends with draft regulations (Annex E) and contains no response counts; its only "respondents" mentions are the privacy notice (L394), HM Treasury's 2020 consultation (L498) and a People Survey (L919).
3. D03 = the 2023 consultation paper (no response counts); D04 = 2017 Civil Service Compensation Scheme consultation (unrelated, no response counts).
4. Searches of every document for numbers adjacent to "responses", "respondents", "individuals", "organisations", "submissions", "received" found only the D02 figures.
5. Required calculation: (2021-22 individuals' share) − 95.73; the 2021-22 share is missing.

minimal_documents: D02 (2023 half) + D01 (identifies the 2021-22 consultation only); no document in the packet supplies the 2021-22 half, and none substitutes.

readings: If the ten no-question responses were excluded for 2023, share = 102/107 = 95.33% (0.40 pp lower), still needing the missing 2021-22 figure. Treating the 68 "queried the effect" responses as the no-question ones would be wrong (they are already inside the 102/107; share stays 95.33%, or 95.73% once the extra ten are added). Either way "fall" implies the 2021-22 share exceeded 95.73% (or 95.33%).

Forced-guess basis: no documentary support. Only constraint: 2021-22 share > 95.73%. Assumed ≈5–7 organisations (as in 2023: three unions, two other bodies) against roughly 200–300 individual responses → share ≈97–98% → fall ≈1.3–2.3 pp; picked midpoint ≈1.80. No reliable memory of the actual 2022 counts.

gaps: Missing fact: the 2021-22 consultation response/outcome ("Civil Service Pension Scheme: 2015 Remedy and civil service member contributions") giving counts of responses from individuals and organisations (and any that addressed no question). Read in full: D02 L1–650 (except footnotes after 650), D01 L1–519, L900–939, L1090–1430, D03 L1–140; searched but not read line by line: D01 L519–900 and L939–1090 (EQIA member tables, contribution-rate table), D03 L140–1300, all of D04. Text files only (manifest method "text", pages null), so no PDF pages to check; docs/ search hit counts matched text/ for every file.

contaminated: no

## Author record

- result: misses (unforced "not answerable"); forced guess 1.80 at p 0.01 (gold 3.81).
- Under rev 1's wording the probe resolved Doc 4's 68 row correctly ("already inside the 102/107") and used 112/117 for 2023.
