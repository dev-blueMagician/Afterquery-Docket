# i07 strong-solver screen, solver A (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 9.0). Named 8.9 (shares rounded first) as excluded by the question.

answer: 9.0 percentage points (Fifth Third 27.6347% − KeyCorp 18.6791% = 8.9556)
confidence: high

path:
1. Fifth Third 2Q26 average total deposits — D01 (fitb_ex991_2026-07-17), Average Deposits table, p.7 (text lines 320-341): "Demand|$63,976 $55,770 $40,885" and "Total average deposits $231,506 $209,352 $163,575" (June 2026 column first). Highlights line 64 repeats "Average deposits|231,506".
2. Fifth Third "Demand" = noninterest-bearing: D01 average balance sheet p.21 (lines 1096-1104): "Total interest-bearing deposits|167,530" then "Total interest-bearing liabilities", with "Demand deposits|63,976" listed outside the interest-bearing block (no rate); 167,530 + 63,976 = 231,506 = total. D02 (fitb_ex992) slide 9 "Core deposit trends (average)" labels that series "Non Interest-Bearing $ ... $40.9 $41.2 $41.8 $55.8 $64.0". (Neither Fifth Third document uses the literal word "noninterest-bearing".)
3. KeyCorp 2Q26 average — D05 (key_ex991_2026-07-21), "Consolidated Average Balance Sheets ... From Continuing Operations," p.19 (lines 1071, 1078): "Total interest-bearing deposits|120,011" and "Noninterest-bearing deposits|27,566 26,934 27,473"; Average Deposits table p.4 (line 170): "Total deposits|$|147,577". Reconciles: 120,011 + 27,566 = 147,577. Text: sequential increase of $278M ("147,577 − 147,299") "was driven by growth in noninterest bearing deposits" (+632) — consistent.
4. KeyCorp's "Demand deposits|61,013 280 1.84" (line 1066) are interest-bearing (1.84% rate; inside interest-bearing deposits) — not counted.
5. Calculation: Fifth Third 63,976 / 231,506 = 0.27634705 → 27.634705% (check: 231,506 × 0.27634705 = 63,976.0); KeyCorp 27,566 / 147,577 = 0.18679062 → 18.679062% (check: 147,577 × 0.18679062 = 27,566.0); difference = 8.955643 pp → 9.0. (Rounding shares first, 27.6 − 18.7, would give 8.9 — excluded by the question.)

minimal_documents: D01 + D05. (D01 alone supplies Fifth Third numerator, denominator and the balance-sheet structure establishing "Demand" as noninterest-bearing; D05 alone supplies both KeyCorp figures. Alternative: D02 + D05 — D02 slide 9 gives $64.0B noninterest-bearing and $231.5B average deposits (rounded to $0.1B): 27.6458% − 18.6791% = 8.967 → still 9.0. D02 is corroborative, not necessary for the alias. D03/D04 (Huntington) not needed; their only "Key" hits are "Key Statistics" headings.)

readings:
- Using D02's printed "Non Interest-Bearing %" ("28.0%" for 2Q26): its base is core deposits ($228.5B; 63,976 / 228,516 = 27.9963%), not total deposits → 27.996 − 18.679 = 9.3. Wrong denominator for "average total deposits."
- Period-end instead of average: Fifth Third D01 period-end balance sheet (lines 908, 914) Demand 63,928 / total deposits 234,141 = 27.303%; KeyCorp D05 lines 901-902: 30,893 / 153,089 = 20.180% → 7.1. Excluded — question says "average."
- Treating KeyCorp "Demand deposits" (61,013) as noninterest-bearing: 41.343% → Fifth Third would be 13.7 pp lower. Not defensible (that line bears an interest rate).
- KeyCorp Consumer Bank segment only (D05 lines 328-329: 14,082 / 87,399 = 16.112%) → 11.5. Not consolidated.
- Rounding shares first: 8.9 — excluded by the question.

gaps: None material. Packet has only .txt sources (manifest method "text"; no layout files/PDFs), so no original-page check possible; tables used reconcile internally, so extraction appears sound. D03/D04 not read in full (searched only for Fifth Third/KeyCorp references); D01/D02/D05 not read page-by-page — targeted searches for deposit/noninterest-bearing terms and reading of matching sections. Did not open question.txt in the packet, as instructed.

contaminated: no
