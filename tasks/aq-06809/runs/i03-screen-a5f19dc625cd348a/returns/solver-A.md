# i03 strong-solver screen, solver A (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 13).

answer: 13 basis points (Fifth Third ≈58.13% vs Huntington ≈58.00%; Fifth Third higher by 12.96 bp → +13 bp)

confidence: high

path:
1. Fifth Third Q2 2026 noninterest expense — D01 Income Statement Highlights (line 103): "Noninterest expense|2,109 2,395 1,264"; non-GAAP reconciliation (line 1634): "Noninterest expense (w)|2,109".
2. Fifth Third itemized merger charges in expense — D01 line 1636: "Merger-related charges|(203) (635) —"; footnote (line 133): "Pre-tax merger-related charges increased noninterest expense by $203 million".
3. Fifth Third merger charges in revenue for Q2 2026: none — D01 line 192/1627: "Merger-related charges|— 22 —" (22 is Q1 2026).
4. Fifth Third FTE revenue — D01 line 1668: "Total revenue (FTE) (a) + (u)|$3,279" (= NII FTE 2,220 + noninterest income 1,059).
5. Huntington Q2 2026 total noninterest expense — D03 Table 8 (line 295): "Total noninterest expense|$|1,809".
6. Huntington itemized acquisition charges — D03 Table 9 (line 318): "Acquisition-related expenses included in Notable Items|$|152"; all Q2 2026 Notable Items are acquisition-related (total Notable Items also $152, line 317; line items 38+74+15+2+4+8+7+4 = 152); narrative (line 320): "Notable Items in the second quarter of 2026 included $152 million of acquisition-related expenses". Table 10 (line 339): "Total adjusted noninterest expense|$|1,657".
7. No Huntington revenue-side Notable Item in Q2 2026 (Table 7 notable item is only the Q3 2025 corporate trust gain; "—" for Q2 2026).
8. Huntington FTE revenue — D03 Table 3 (line 153): "Total revenue - FTE (1) $ 2,857" (= 2,072 + 785; also D04 line 738).
9. Calculation: Fifth Third = (2,109 − 203)/3,279 = 1,906/3,279 = 58.1275%; Huntington = (1,809 − 152)/2,857 = 1,657/2,857 = 57.9979%; difference = 0.12958 pp = 12.96 bp → 13 bp. Rechecks: 3,279 × 0.5813 = 1,906.08 → ratio 0.5813 − 0.0000252 = 0.581275; 2,857 × 0.58 = 1,657.06 → ratio 0.58 − 0.000021 = 0.579979.
10. Deliberately not excluded: Huntington's intangible amortization (54) and securities gains (2), which its own efficiency ratio removes (D04 line 1128 definition "Noninterest expense less amortization of intangibles divided by… excluding gains (losses) on sales of securities"); Fifth Third's other certain items (impairments 7, severance 7, interchange litigation, securities repositioning, deferred compensation) used in its 57.1% adjusted ratio — the question says "only" merger/acquisition charges and defines the ratio as noninterest expense over FTE revenue. Merger-related provision items (Fifth Third's "Merger-related Day 1 ACL build," Huntington's "CECL double count") are not noninterest expense and are zero in Q2 2026 anyway.

minimal_documents: D01 + D03. Alternative: D02 can replace D01 (slide 42: noninterest expense $2,109, "Merger-related charges (203)", "Revenue (FTE) (c) + (e) 3,279", "—" Q2 merger charge in noninterest income; slide 40 "$203 million pre-tax… merger-related charges"). D04 cannot replace D03 (it has 1,809 and 2,857 but does not itemize the $152M pre-tax acquisition charge — only "Notable Items, after tax 116"). D05 (KeyCorp) irrelevant (no Fifth Third/Huntington/Comerica/Cadence matches).

readings:
(a) Applying Huntington's own efficiency-ratio convention to Huntington while removing only acquisition charges: (1,755 − 152)/2,855 = 56.147% → 58.127 − 56.147 = 198 bp (conflicts with the question's explicit definition and "only").
(b) No exclusions at all (question's definition): 2,109/3,279 = 64.318% vs 1,809/2,857 = 63.318% → 100 bp.
(c) Headline reported ratios (64.3% − 61.5%) → 280 bp (different definitions, ignores exclusion).
(d) Using Fifth Third's 57.1% adjusted ratio is not supported (removes more than merger charges; Huntington publishes no comparable adjusted ratio in this packet).
Intended reading gives 13.

gaps: Inputs are rounded to $ millions (a ±$1M change in a numerator moves a ratio ≈3 bp; the printed figures give 12.96 bp, so 13 is the document-supported answer). Not read in full: D01 (read lines 1–260 and 1590–1729 plus search hits), D02 (lines 1–30, 85–100), D04 (lines 160–299, 680–749, 1085–1134 plus search hits), D05 (searched only); D03 read in full. Original docs/ files not separately read (manifest marks them plain text; no layout files/page markers), but every decisive figure is corroborated by at least two independent locations (table plus narrative or D01 plus D02).

contaminated: no
