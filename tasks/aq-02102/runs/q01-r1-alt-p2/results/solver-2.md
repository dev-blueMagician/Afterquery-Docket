# q01 rev 1 removal probe: solver-2 (left out D03 = Doc 4)

- Date: 2026-10-08
- Role: blind-solver (fresh, omitClaudeMd), packet tasks/aq-02102/runs/q01-r1-alt-p2/solver-2 (renumbered D01-D04)
- Question: verbatim q01 rev 1 (tested_sha256 8b03da09facfd900e42756fe23f4b662486b20d196a4d13286e9c14c89b1b04b)
- Input: workspace root, packet path, question, and the instruction to add a forced guess with probability if not answerable
- Packet ids (probe-map.json): D01->D01, D02->D02, D04->D03, D05->D04

## Raw return (verbatim)

answer: not answerable — the 2021-22 individuals' share is 99.54% (1,295 of 1,301), but no document gives the 2023 response counts. Forced best guess: a fall of about 9.54 percentage points (assumes individuals were 90.00% of 2023 responses; that 90% is my own assumption, not from the documents or a remembered figure — only the intuition that the 2021-22 total was inflated by one union's template, 1,239 identical emails, and a technical 2023 consultation would show a lower individual share). Probability the guess is correct to two decimals: ≈0.01.

confidence: high (that it is not answerable from the packet); 2021-22 figure high; guess very low

path:
1. D01 = 2021-22 consultation response: L6 "This response is published on 4 March 2022."; L58-59 consultation "began on 22 November 2021 and ended on 17 January 2022".
2. D01 para 3.7 (L174): "1,268 responses in total from scheme members and trade unions which directly addressed the questions … 1,263 responses from individuals, and five responses from trade unions … In addition, a response from Audit Wales was also received. Another 32 responses were received from individuals that did not address the questions posed by the consultation".
3. D01 Table 2 (L239-278; docs/ source L332-371): Individuals Email 1,295; "Of which: Queried the effect of the remedy (i.e. didn't answer the consultation questions)" 32; Unions 5; Other organisations 1; total 1,301. Annex A L649 "Individuals – 1295".
4. Checks: 1,263 + 32 = 1,295; 1,295 + 5 + 1 = 1,301 → share = 1,295/1,301 = 99.5388% (≈99.54%).
5. D03 = 2023 consultation paper, not its response: L1220 "Please send your response by 23:59 on 14 May 2023"; L1200-1212 list only respondent categories ("Organisation", "Scheme Members", "Unions" …) with no numbers; docs/ source L968, L1084 say details "will be published in the consultation response" — that response document is not in the packet.
6. D02 = 2021 consultation paper ("This consultation begins on 22 November 2021"), no response counts; D04 = 2017 Civil Service Compensation Scheme consultation, irrelevant.
7. Searches of all four docs/ sources for response/respondent/individual counts: counts exist only in D01.

minimal_documents: D01 alone suffices for the 2021-22 share; D03 identifies the 2023 consultation but has no counts; the required 2023 consultation response is absent (no alternative found).

readings: 2021-22 share excluding the 32 no-question responses would be 1,263/1,269 = 99.53% (or 1,263/1,268 = 99.61%) — ruled out by the question's wording; excluding Audit Wales from the total, 1,295/1,300 = 99.62%. Under every reading the 2023 share is still missing, so the fall can't be computed.

gaps: Missing fact: the 2023 McCloud consultation response's counts of individuals (including those addressing no question) and total responses. Read D01 L1-340 and L620-700, D03 L1-140 and L1160-1333, D02 L1-120, D04 L1-130 plus specific long lines found by search; the rest covered only by keyword/number searches, not line by line. No PDFs/layout files, so Table 2's row layout couldn't be checked against the original page (its numbers reconcile with para 3.7 and Annex A).

contaminated: no (no answer, reasoning or source hint supplied; my session context included a workspace git-status snapshot listing file names for other tasks, e.g. aq-00949, but no content for this question).

## Author record

- result: misses (unforced "not answerable"); forced guess 9.54 at p 0.01 (gold 3.81).
