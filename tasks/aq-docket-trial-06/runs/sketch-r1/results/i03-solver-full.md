# i03 blind solver (sketch screen, 2026-10-08), packet runs/sketch-r1/solver-1 (all six documents)
Question: In 2003 GAO made unannounced visits to privately insured credit unions to check deposit-insurance notices. Across the states whose bank regulators GAO interviewed while reviewing OCC's 2004 preemption rules, what percentage of the privately insured credit unions got at least one visit? Answer to one decimal place.

answer: 40.5%
confidence: high
path:
1. D05 (GAO-06-387) letter scope 183 and App. I 533: "site visits or phone interviews with officials and representatives of state attorneys general offices, state banking departments, ... in six states (California, Georgia, New York, North Carolina, Idaho, and Iowa)"; App. VI 797 "six state bank regulators that we interviewed"; Table 4 803-841 rows for the six.
2. D02 (GAO-03-971, Dec 2002 counts): privately insured credit unions only in eight states (App. I fn 3, 1207: Alabama, California, Idaho, Illinois, Indiana, Maryland, Nevada, Ohio); Table 3 467 "California 22 ... Idaho 20" (total 212; Figure 1 numbers match). Georgia, New York, North Carolina, Iowa had none. Denominator 22 + 20 = 42.
3. Visits (1197; also 59, 407): 57 privately insured credit unions (49 main, 8 branch) in AL, CA, IL, IN, OH. Idaho 0.
4. Table 1 (417-431) "California 22 21 b 6 29"; note b: 4 extra branch sites, so 21 - 4 = 17 California credit unions. Cross-check: branches 2 + 4 + 2 = 8, mains 3 + 17 + 8 + 5 + 16 = 49; rows sum to 179, 57, 21; docs/ copy identical.
5. (17 + 0)/(22 + 20) = 17/42 = 0.404762 -> 40.5%.
minimal_documents: D02 + D05; no substitutes (D03 is the predatory-lending testimony, not the OCC review; D01, D04, D06 no matches).
readings: sites instead of credit unions 21/42 = 50.0% (rejected: "at least one visit"); leaving out Idaho 17/22 = 77.3% (rejected: question asks across all interviewed states); no other defensible state list.
gaps: counts as of December 2002 vs visits February-August 2003 (minor); partial reads of D02 and D05; others by titles/keywords.
contaminated: no
