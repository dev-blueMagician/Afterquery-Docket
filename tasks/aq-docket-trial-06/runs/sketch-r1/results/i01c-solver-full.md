# i01c blind solver (sketch screen, 2026-10-08), packet runs/sketch-r1/solver-1 (all six documents)
Question: In 2003 GAO made unannounced visits to privately insured credit unions to check deposit-insurance notices. In the state whose Department of Financial Institutions caps bank assessments at $2.20 per $1,000 of assets, what percentage of that state's privately insured credit unions did GAO visit? Answer to one decimal place.

answer: 77.3% (GAO visited 17 of California's 22 privately insured credit unions)
confidence: high
path:
1. State: D05 App. VI Table 4, California row (801-809): "The California Department of Financial Institutions levies assessments ..." and "The assessment (minimum of $5,000 and a maximum of $2.20 per $1,000 of assets on a sliding scale) reflects a statutory limit applicable to banks." "2.20" appears nowhere else. Ohio's DFI (D02 395, 1219) and Washington State's (D03 169) have no such cap. So California.
2. Visits: D02 167 (February-August 2003); 407 (57 locations, 49 main and 8 branch, five states).
3. D02 Table 1 (417-427): "California 22 21 b 6 29"; totals 179 and 57 check; Table 3 467 "California 22"; 411 "six of the 21 sites visited in California".
4. Note b (429-431): 4 California branch sites at 2 credit unions also visited at their mains, so 21 - 4 = 17 distinct credit unions.
5. Cross-check: AL 2 branch/3 main; CA 4/17; IL 2 branch-only/8 main; IN 5; OH 16 ("we visited 16 credit unions", 393); 8 branch, 49 main.
6. 17/22 = 0.7727 -> 77.3%.
minimal_documents: D05 + D02; no substitutes ("privately insured|private deposit insur|share insur": 114 matches, all D02).
readings: sites as credit unions 21/22 = 95.5% (the Highlights, 59, and App. I, 1197, loosely say "site visits to 57 privately insured credit unions", which supports this reading; rejected because note b shows 4 of the 21 sites were extra branches of 2 credit unions already visited); Table 3's base is the same 22; timing: base Dec 2002 vs visits Feb-Aug 2003, the report itself compares them in Table 1.
gaps: no PDFs; Figure 1 pairing lost (tables supply California = 22); read D02 229-284, 403-482, 1185-1229 and D05 770-858; other documents by searches only.
contaminated: no
