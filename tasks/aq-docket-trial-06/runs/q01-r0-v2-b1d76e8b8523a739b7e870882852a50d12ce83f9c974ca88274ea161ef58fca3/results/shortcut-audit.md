# q01 rev 0 shortcut audit, 2026-10-08, fresh shortcut-auditor, packet shortcut (prepared), question verbatim
tested_sha256: b1d76e8b8523a739b7e870882852a50d12ce83f9c974ca88274ea161ef58fca3

answer: 40.5%. GAO visited 17 of the 42 privately insured credit unions in the overlapping states (17 / 42 = 40.476%).
verdict: clear
shortest_path:
1. States: D05 (GAO-06-387, 04/28/2006) docs\gaoreports_gao_06_387.txt line 181 (repeated 531, 559): "We conducted site visits or phone interviews with officials and representatives of state attorneys general offices, state banking departments, ... in six states (California, Georgia, New York, North Carolina, Idaho, and Iowa)." Line 795: "Table 4 provides more detailed information on the funding arrangements for six state bank regulators that we interviewed." Table 4 lists the same six (California Department of Financial Institutions, Idaho Department of Finance, ...).
2. D02 (GAO-03-971, 08/20/2003) docs line 1205: privately insured credit unions exist only in "Alabama, California, Idaho, Illinois, Indiana, Maryland, Nevada, and Ohio." Overlap: California and Idaho; the other four contribute 0.
3. D02 Table 3 (docs line 465): "California 22 ... Idaho 20", total 212 = "As of December 2002, 212 credit unions" (line 231) and Figure 1 (December 2002). Denominator 42.
4. Table 1 (docs line 421) "California 22 21 b 6 29": 21 sites; footnote b (427-429): one credit union main + three branches, another main + one branch: 21 - 3 - 1 = 17. Cross-check: branches AL 2 + CA 4 + IL 2 = 8; mains 3 + 17 + 8 + 5 + 16 = 49 ("57 ... (49 main and 8 branch locations)", line 1195). Idaho had no visits (only AL, CA, IL, IN, OH).
5. 17 / 42 = 0.40476 -> 40.5%.
sufficient_documents: D02 and D05 together; neither alone (D05 never mentions credit unions; D02 never mentions OCC's 2004 rules or the six states; D03 covers preemption generally, no interviewed states); no duplicates elsewhere.
searches: "unannounced", "privately insured", "preemption", "credit union", "interview", "bank regulators", "banking department", "Department of Financ", "officials in/from", all eight private-insurance states and the six D05 states, report numbers/titles/dates. Read D02 1-514, 1170-1229; D05 1-40, 170-199, 520-649, 778-852; D03 169 and state hits. D01, D04, D06 off-topic (no "credit union"/"preemption" hits). No single passage or document gives the whole answer; wording gives nothing away.
readings/gaps:
- Sites instead of credit unions: 21 / 42 = 50.0% (rejected: "got at least one visit"; footnote b makes the adjustment).
- Leaving out Idaho: 17 / 22 = 77.3% (or 21 / 22 = 95.5%), if a reader uses only Table 1 (visited states only); rejected: Idaho is an interviewed state with 20 privately insured credit unions.
- The 2003 report's own interviewed credit-union regulators (AL, CA, ID, IL, IN, MD, NV, NH, OH): 51 / 212 = 24.1%; rejected: the question asks about bank regulators interviewed later about OCC's 2004 rules.
- Difficulty risk, not a shortcut: an easy join of two state lists plus one ratio; non-trivial because of the footnote-b adjustment and taking Idaho's count from Table 3 rather than Table 1.
- Extraction gap: Figure 1 state labels separated from numbers; irrelevant (Table 3 labelled counts sum to 212).
- Contamination check: git status listed other tasks' file names only; uncontaminated.
