# q01 rev 1 full-corpus blind solve: solver-1

- Date: 2026-10-08
- Role: blind-solver (fresh, omitClaudeMd), packet tasks/aq-02102/runs/q01-r1-v2-8b03da09.../solver-1 (all five documents, local ids)
- Question: verbatim q01 rev 1 (tested_sha256 8b03da09facfd900e42756fe23f4b662486b20d196a4d13286e9c14c89b1b04b)
- Why run: confirm that rev 1's stated condition resolves the rev 0 reading conflict (Doc 4 Table 2 "Total Received" 107)

## Raw return (verbatim)

answer: 3.81 percentage points (individuals' share fell from ≈99.54% in 2021-22 to ≈95.73% in 2023)

confidence: high

path:
1. D01 = 2021-22 consultation response (L6 "This response is published on 4 March 2022"; L58-59 consultation "began on 22 November 2021 and ended on 17 January 2022").
2. D01 para 3.7 (L174): "The Cabinet Office received 1,268 responses in total from scheme members and trade unions which directly addressed the questions in the consultation. These consisted of 1,263 responses from individuals, and five responses from trade unions ... In addition, a response from Audit Wales was also received. Another 32 responses were received from individuals that did not address the questions posed by the consultation".
3. D01 Table 2 (L239-278, rows scrambled in extraction but reconcilable): Individuals 1,295; "Of which: Queried the effect of the remedy (i.e. didn't answer the consultation questions)" 32; Unions 5; Other organisations 1; Total 1,301. Annex A L649 "Individuals – 1295"; Audit Wales is the one "other organisation" (Annex A L645; para 4.57 in source). Consistency: 1,263+32 = 1,295; 1,295+5+1 = 1,301 (docs/ source L254, 344, 371, 846 confirm).
4. D03 = 2023 consultation response (L28 "began on 6 March 2023 and closed on 14 May 2023"; L6 "© Crown copyright 2023").
5. D03 para 3.9 (L189): "The Cabinet Office received 107 responses in total ... which in some way addressed the consultation questions. These consisted of 102 responses from individuals and five responses from organisations. In addition another ten responses were received from individuals that did not address the questions posed by the consultation". Table 2 (L203-209): Individuals 102, Unions 3, Other organisations 2, Total 107 — this total excludes the extra 10; its "of which" 68 ("didn't answer the consultation questions in all respects") is a subset of the 102, so not "addressing no question".
6. Calculation: 2021-22 share = 1,295 / 1,301 = 99.5388%; 2023 share = (102+10)/(107+10) = 112/117 = 95.7265%; fall = 99.5388 − 95.7265 = 3.8123 pp. Exact: (1295×117 − 112×1301)/(1301×117) = 5,803/152,217 = 0.0381232 → 3.81 pp (no rounding-boundary issue; rounding shares first, 99.54 − 95.73, also gives 3.81).

minimal_documents: D01 + D03 (no replacements: D02 = Nov 2021 consultation paper and D04 = 2023 consultation paper contain no response counts — searched for numbered responses/respondents/individuals with none found; D05 = 2017 Civil Service Compensation Scheme consultation, unrelated to McCloud).

readings: (a) Excluding Audit Wales from the 2021-22 base: 1,295/1,300 = 99.6154% → 3.89 (weaker: Audit Wales's response was received and counted in Table 2's 1,301 total). (b) Taking each Table 2 as printed (D01 table includes the 32 non-answering individuals, D03 table omits the 10): 99.5388 − 95.3271 = 4.21 — ruled out by "including those addressing no question". (c) Only question-addressing responses (ignores that wording): 1,263/1,268 vs 102/107 → 4.28 (4.20 with Audit Wales in base 1,263/1,269).

gaps: Only .txt sources (no PDFs) so original page layouts not checked; D01 Table 2 is scrambled in extraction but its figures match para 3.7 and Annex A. Minor D01 internal inconsistency (para 3.10 "1,239 out of 1,268" individual responses, though 1,268 includes 5 unions) does not affect the answer. Coverage: D01 read L1-330, L620-699; D03 L1-260, L535-579; D02, D04, D05 headers only, plus targeted searches across all five documents (not exhaustively read).

contaminated: no (session context included a git-status listing of file names for a different task, aq-00949, and workspace memory/agent files; none concern this question and none were read; only the packet's text/ and docs/ were accessed).

## Author record

- outcome: match (3.81), confidence high. Rev 1's wording removed the rev 0 conflict: the solver called 4.21 "ruled out by 'including those addressing no question'" and resolved Doc 4's 68 row as "a subset of the 102, so not 'addressing no question'".
