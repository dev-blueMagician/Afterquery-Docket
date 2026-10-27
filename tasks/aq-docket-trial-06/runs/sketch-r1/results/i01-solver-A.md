# i01 blind solver A (sketch screen, 2026-10-08), packet runs/sketch-r1/solver-1 (all six documents)

answer: 77.3%
confidence: high
path:
1. The state is California (D05, GAO-06-387, Appendix VI, Table 4, text/D05.txt 803-809): "The California Department of Financial Institutions levies assessments on the bank and nonbank entities it regulates..." and "The assessment (minimum of $5,000 and a maximum of $2.20 per $1,000 of assets on a sliding scale) reflects a statutory limit applicable to banks." No other document has "2.20" or a similar cap.
2. The visits (D02 407 and 1197): "unannounced site visits to 57 locations of privately insured credit unions (49 main and 8 branch locations) in five states"; work "between February and August 2003" (1235).
3. California figures (D02 Table 1, 423): "California 22 21 b 6 29" = 22 privately insured credit unions, 21 sites visited (note b), 6 without signage, 29%. 411 confirms "six of the 21 sites visited in California". Table 3 (467) and Figure 1 give the same 22.
4. Note b (429-431): one credit union main + three branch locations; another main + one branch. So 4 of California's 21 sites were extra branch visits to 2 credit unions whose mains were also visited.
5. Cross-check: note a (Alabama) 2 branch sites, 3 mains; note b 4 branch, 17 mains; note c (Illinois) 2 branch-only, 8 mains; Indiana 5 and Ohio 16 mains ("we visited 16 credit unions", 393). Branches 2+4+2 = 8, mains 3+17+8+5+16 = 49, matching "49 main and 8 branch".
6. 21 - 4 = 17 credit unions; 17/22 = 0.772727 -> 77.3%.
minimal_documents: D02 + D05.
readings: counting sites as credit unions 21/22 = 95.5% (rejected: ignores note b and "at least one visit"); applying only the first sentence of note b (21-3)/22 = 81.8% (not defensible).
gaps: text extractions only, no PDF layout check; read parts of D02 and D05, keyword-searched the rest; the 22 is dated December 2002 by Figure 1 and Table 3.
contaminated: no (automatic git status listed unrelated task files only).
