# q01 rev 0 blind solver B, 2026-10-08, fresh blind-solver, packet solver-2 (prepared), question verbatim
tested_sha256: b1d76e8b8523a739b7e870882852a50d12ce83f9c974ca88274ea161ef58fca3

answer: 40.5%
confidence: high
path:
1. Which states. GAO-06-387 (D05, April 2006, OCC's preemption rules) line 183: "We conducted site visits or phone interviews with officials and representatives of state attorneys general offices, state banking departments, ... in six states (California, Georgia, New York, North Carolina, Idaho, and Iowa)." Appendix I (533) the same. Table 4 (797-849): "funding arrangements for six state bank regulators that we interviewed" = California Department of Financial Institutions, Georgia Department of Banking and Finance, Idaho Department of Finance, Iowa's Division of Banking, New York State Banking Department, North Carolina Commission on Banking. D05 also mentions Michigan and New Jersey only as case or legal examples, not interviews.
2. Privately insured credit unions at the end of 2002. GAO-03-971 (D02) line 233: "As of December 2002, 212 credit unions ... chose to purchase private deposit insurance." Line 243: "are located in eight states." Table 3 (467): Alabama 3, California 22, Idaho 20, Illinois 40, Indiana 21, Maryland 5, Nevada 8, Ohio 93, total 212; Figure 1 (December 2002) same numbers. Georgia, New York, North Carolina, Iowa: 0. Denominator California 22 + Idaho 20 = 42.
3. The 2003 visits. D02 157: "unannounced site visits to 57 locations of privately insured institutions in Alabama, California, Illinois, Indiana, and Ohio." 1197: "(49 main and 8 branch locations)"; 167: "between February and August 2003." Idaho had no visits.
4. California. Table 1 (423-431) "California 22 21 b": 21 sites; docs file same row order (421). Note b: one credit union main + three branches; another main + one branch: 21 - 3 - 1 = 17 distinct credit unions. Cross-check: notes a (AL, 2 branches), b (CA, 4), c (IL, 2 branch-only): 8 branches; mains 3+17+8+5+16 = 49 ("49 main and 8 branch"). Note b cannot belong to Alabama (implies at least 6 sites; Alabama had 5).
5. 17 / 42 = 0.40476 -> 40.5%.
minimal_documents: D02 + D05; neither replaceable (D03 mentions OCC preemption opinions but no interviews of state bank regulators about the 2004 rules; D01, D04, D06 unrelated).
readings:
- Site visits instead of distinct credit unions: 21/42 = 50.0% (the highlights loosely say "57 privately insured credit unions"; the question asks about credit unions that got at least one visit; note b resolves to 17).
- Only interviewed states that had visits (California only): 17/22 = 77.3%, or 21/22 = 95.5% by sites; drops Idaho, which conflicts with "across the states whose bank regulators GAO later interviewed."
- Website reviews counted as visits (California 18 + Idaho 7): 25/42 = 59.5%; rejected: the question says unannounced visits.
gaps: ASCII text only (no PDF); footnote placement consistent across text, docs and the 49/8 totals. Partial coverage: D02 1-70, 150-293, 395-475, 1180-1239 plus searches; D05 1-20, 170-189, 520-560, 780-857 plus searches; D01, D03, D04, D06 headers and keyword searches. No missing facts for the main reading.
contaminated: no. The packet root contains question.txt; it appeared in a file listing but was not opened. Read only text/ and one docs/ file (gaoreports_gao_03_971.txt) to check the extraction.
