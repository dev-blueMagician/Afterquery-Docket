# q01 rev 0 full-corpus blind solve: solver-1

- Date: 2026-10-08
- Role: blind-solver (fresh, omitClaudeMd), packet tasks/aq-02102/runs/q01-r0-v2-b7c12ecb.../solver-1 (all five documents, local ids)
- Question: verbatim q01 rev 0 (tested_sha256 b7c12ecb74dbef0da7954ed9c37189f3e29589e900757a0da78ce7ad47adfb36)
- Why run: concrete issue, one defensible answer (Doc 4's Table 2 column "Total Received" totals 107 while paragraph 3.9 adds ten received responses)

## Raw return (verbatim)

answer: 3.81 percentage points (individuals' share fell from 99.54% in 2021-22 [1,295 of 1,301] to 95.73% in 2023 [112 of 117]); if D03's printed Table 2 total is used instead, 4.21 (see readings).
confidence: medium — the 2021-22 figures are internally consistent three ways; D03 is internally inconsistent on the 2023 total (its Table 2 total omits ten responses its own text says were received).

path:
1. 2021-22 consultation = D01 (text\D01.txt), response to "2015 Remedy and civil service member contributions", L59: "began on 22 November 2021 and ended on 17 January 2022"; L52 ties it to "the McCloud litigation".
2. D01 para 3.7 (L174): "The Cabinet Office received 1,268 responses in total from scheme members and trade unions which directly addressed the questions … These consisted of 1,263 responses from individuals, and five responses from trade unions … In addition, a response from Audit Wales was also received. Another 32 responses were received from individuals that did not address the questions…"
3. D01 Table 2 "response method and source" (L239-278; garbled order in extraction, consistent with raw docs file L332-371): Individuals 1,295 (of which 32 queried effect of remedy; 24 personalised); Unions 5; Other organisations 1; "Total Received" 1,301. Annex A L649: "Individuals – 1295". Checks: 1,263 + 32 = 1,295; 1,295 + 5 + 1 = 1,301 (= 1,268 + 1 + 32).
4. 2023 consultation = D03 (text\D03.txt), L28: "began on 6 March 2023 and closed on 14 May 2023"; L24 calls the 2015 Remedy "(also known as 'McCloud')".
5. D03 para 3.9 (L189): "The Cabinet Office received 107 responses in total … which in some way addressed the consultation questions. These consisted of 102 responses from individuals and five responses from organisations. In addition another ten responses were received from individuals that did not address the questions posed by the consultation…"
6. D03 Table 2 (L203-209): Individuals 102 (of which 68 queried effect of remedy); Unions 3; Other organisations 2; Total 107 — i.e., excludes the ten extra, whereas D01's equivalent group (the 32) is included in its 1,301.
7. Like-for-like "all responses received" (both years): 2021-22 share = 1,295 / 1,301 = 1 − 6/1,301 = 99.538816%; 2023 share = (102 + 10)/(107 + 10) = 112/117 = 1 − 5/117 = 95.726496%. Fall = 3.812320 pp → 3.81 (rounding the shares first, 99.54 − 95.73 = 3.81, same).

minimal_documents: D01 + D03 (no substitutes: D02/D04 are the consultation papers themselves with no response counts; D05 is a 2017 Civil Service Compensation Scheme consultation, not McCloud).

readings: (a) Using each Table 2's printed "Total Received" literally (treating 107 as all 2023 responses): 1,295/1,301 = 99.538816% vs 102/107 = 95.327103% → fall 4.211713 → 4.21 (main alternative; "Total Received" is the table's own label, but it conflicts with para 3.9's "In addition another ten responses were received"). (b) Counting only responses that addressed the questions: 1,263/1,268 = 99.605678% vs 102/107 → 4.28 (with Audit Wales added to the 2021-22 base, 1,263/1,269 = 99.527187% → 4.20); weaker, since the question says "all responses received".

gaps: D03's Table 2 total (107) conflicts with its own para 3.9 (107 + ten more); the documents do not say which figure is authoritative. Only .txt sources (manifest method "text", pages null), no PDF to verify D01's garbled Table 2 against the original page, though its figures reconcile three ways. Not read in full: D02, D04, D05 (targeted searches only for response counts, "received", dates); D01 lines 300-600 and 680-end; D03 lines 230-535 and 580-end. No other response totals found in searches.

contaminated: no

## Author record

- outcome: match (3.81), confidence medium; the solver named 4.21 (Doc 4 Table 2 "Total Received" 107) as the main alternative and said the documents "do not say which figure is authoritative".
- Consequence: treated as a concrete one-defensible-answer risk (guide rule 4; the decoy's own label matches the question's words). q01 rev 1 states the condition in the question.
