# i01b blind solver (sketch screen, 2026-10-08), packet runs/sketch-r1/shortcut (all six documents)
Question: In 2003 GAO made unannounced visits to privately insured credit unions to check deposit-insurance notices. In the state whose Department of Financial Institutions caps bank assessments at $2.20 per $1,000 of assets, what percentage of the privately insured credit unions got at least one visit? Answer to one decimal place.

answer: 77.3% (17 of California's 22 privately insured credit unions; not 21/22 = 95.5%)
confidence: high
path:
1. State (D05 Table 4, 803-809, jumbled extraction): California row "The California Department of Financial ... Institutions levies assessments on the bank and nonbank entities it regulates ... The assessment (minimum of $5,000 and a maximum of $2.20 per $1,000 of assets on a sliding scale) reflects a statutory limit applicable to banks." "2.20" and "per $1,000" appear nowhere else. Ohio's DFI (D02 395) and Washington State's DFI (D03 169) are mentioned, but neither has an assessment cap. So California.
2. Visits (D02 167 "between February and August 2003"; 407 "57 locations ... (49 main and 8 branch locations) in five states").
3. D02 Table 1 (417-431): "California 22 21 b 6 29"; note b: one CU main + three branches; another main + one branch.
4. 21 - (3 + 1) = 17 distinct credit unions.
5. Cross-check: AL 5 sites (2 branches, 3 main); CA 4 branches, 17 main; IL 10 sites (2 branch-only, 8 main); IN 5; OH 16; branches 8, mains 49 = report.
6. Denominator 22 (Table 1, Table 3 467, Figure 1, Dec 2002).
7. 17/22 = 0.7727 -> 77.3%.
minimal_documents: D02 + D05; no substitutes.
readings: sites as credit unions 21/22 = 95.5% (ruled out by note b and "got at least one visit"); main-location visits only 17/22 (same); a different state such as Ohio (its DFI regulates ASI): no basis, only California is tied to the $2.20 cap.
gaps: none affecting the answer; partial line reads of D02 (155-182, 240-300, 400-480, 1180-1220) and D05 (760-839) plus searches; D01, D04, D06 titles/searches only.
contaminated: no
