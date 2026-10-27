# aq-04830 - document map

Maintained by the caller from `text/` (and `docs/` for layout). Navigation only; questions quote
the documents, never this map.

## Bundle

- What it is: "Industry research" set on Australian public finance plus one EU brief: three
  statements of the 2026–27 Budget Paper No. 1 (3 fiscal strategy, 7 debt, 8 forecasting
  performance), Treasury's 2025 Economic Reform Roundtable paper, ABS GFS June quarter 2026, three
  RBA Bulletin articles (2021 global fiscal response; 2021 bond markets; Oct 2024 inflation-linked
  markets), RBA RDP 2022-02 (bond purchases), and a July 2026 European Commission brief on Belgium.
- Documents: 10. Local ids are alphabetical and differ from page Doc numbers:
  page Doc 1 = D01, Doc 2 = D02, Doc 3 = D03, Doc 4 = D09, Doc 5 = D05, Doc 6 = D04, Doc 7 = D07,
  Doc 8 = D08, Doc 9 = D06, Doc 10 = D10.
- Gaps: capture complete (10 of 10, intake.json, no gap characters). Charts are images: their
  values are not in the text (e.g. D03 Charts 8.1-8.15, D04 Charts 1-11, D05/D09 graphs, D07
  Graph 2). D08 read only in part (intro, system design); it shares no entity with the rest.
- Extraction: plain-text capture; PDF tables are flattened column by column. D01 Table 3.1 prints
  each year's column as an unlabeled block (2024-25 Actual block at D01 lines 144-160, identified
  by UCB -10.0 / -0.4 and gross debt 928.6 / 33.4, which Table 3.6 prints under "Actual 2024-25",
  lines 1635-1657). D02 Tables 7.4-7.6 print coupon, amount, timing and maturity as separate
  lists in the same order (29 / 6 / 9 lines). D07 Table A.3 prints per-country groups of four
  numbers after the row labels.
- Provenance: notes/intake.json (capture AQ-04830_2026-10-14_1111.txt, sha256 8633001786f5...).

## D01 (page Doc 1) - BP1 Statement 3: Fiscal Strategy and Outlook (2026-27 Budget)

- Commonwealth general government, cash (UCB, receipts, payments) and accrual (Appendix A).
  Financial years July-June ("2025–26"). Editions compared: 2022 PEFO, 2025 PEFO, 2025-26 MYEFO.
- Table 3.1 (lines 67-200): 2024-25 Actual and 2025-26 to 2029-30 estimates; 2036-37 projection
  in % of GDP. 2024-25 Actual: UCB -10.0 (-0.4%), receipts 717.0, tax 657.8, non-tax 59.1,
  payments 726.9, gross debt 928.6 (33.4%), net debt 532.3, net interest 13.7.
- Table 3.3 (UCB reconciliation 2025 PEFO -> MYEFO -> Budget), Table 3.4 (payments), Table 3.5
  (UCB to headline cash balance, IFAPPs), Table 3.6 (balance sheet, 2024-25 Actual to 2029-30),
  Table 3.7 (accrual), Table 3.9 (net zero measures, footnote markers for MYEFO commitments).
- Comparisons vs MYEFO: gross debt peak 35.8% in 2028-29, "1.2 percentage points lower and two
  years earlier than at MYEFO" (lines 18, 272, 1694). Medium-term payment growth, Budget vs MYEFO
  (lines 1461-1481): NDIS 3.6 vs 7.6; PDI 8.8 vs 10.7; hospitals 7.3 vs 5.9; defence 6.4 vs 5.9;
  child care 5.4 vs 5.7; aged care 5.4 vs 4.9; medical benefits 5.1 vs 5.8.
- Since 2022 PEFO: savings $177.9b; UCB +$263.8b over eight years to 2029-30; 76% of tax receipt
  upgrades returned; real payments growth 1.5% (8 yrs) / 1.1% (4 yrs) vs 30-year 3.3%.
- Box 3.3: IMF all-levels, calendar-year basis (deficit 2.1% in 2027; gross debt 50.7%).
- Coverage: full read.

## D02 (page Doc 2) - BP1 Statement 7: Debt Statement

- Face value (gross debt) vs market value; Treasurer's Direction max $1,200b face value (line 47).
- Table 7.1 end-year and within-year peak face value 2025-26..2029-30 (982.0 ... 1,249.0;
  peaks 999.9 Feb-26 ... 1,273.0 May-30). Table 7.2 MYEFO face values 993/1,069/1,142/1,213.
- Table 7.3 at 1 May 2026: TB 878,849; TIB 40,242 (market 50,313); Notes 47,500; total 966,597.
  Footnote 38: TIB face value excludes the inflation uplift.
- Table 7.4: 29 TB lines incl. one Green Treasury Bond (21-Jun-34). Table 7.5: six TIB lines,
  maturities 21-Nov-27, 20-Sep-30, 21-Nov-32, 21-Aug-35, 21-Aug-40, 21-Feb-50; quarterly coupons.
  Table 7.6: nine Treasury Note lines (8-May-26 .. 11-Sep-26), no coupon.
- Footnote 40: 4.25% 21 March 2036 line tapped 3 Sep 2025 (~$1,006m per $1,000m) and
  18 Mar 2026 ($948m per $1,000m). Non-resident holdings 50% (Dec 2025 quarter).
- Tables 7.7-7.10: net debt components, reconciliation, interest payments (cash) and expense.
- Layout notes (round 2): Table 7.4's lines sum to 878,850 against Table 7.3's 878,849 ($1m rounding);
  Table 7.8's year blocks print in reverse order (the 754.8 block is 2028-29); line 744 ("lower across
  the forward estimates") sits beside D01 line 1058's +$17.5m in 2026-27 for debt-management payments.
- Coverage: full read.

## D03 (page Doc 3) - BP1 Statement 8: Forecasting Performance and Sensitivity Analysis

- 2024-25 outcome vs 2024-25 Budget forecast (lines 57-130): real GDP 1.3%; nominal GDP 3.6% vs
  2 3/4%; total receipts grew 4.1% vs 0.9%, $18.5b higher; tax receipts 3.9% vs 0.6%, $15.3b
  higher; non-tax 7.1% vs 4.4%, $3.2b higher; payments 8.0% vs 6.4%, $0.2b higher; UCB deficit
  0.4% of GDP vs 1.0%, $18.3b higher. No forecast levels printed.
- Line 46: tax forecasts use "base plus growth"; the last outcome is the base.
- Confidence intervals (2026-27): receipts 25.8% (70%: 24.3-27.3); payments 26.8%; UCB -1.0%.
- Sensitivities: oil (Table 8.1); yields +/-100bp: UCB -/+0.3 pp by 2036-37, gross debt +1.9 /
  -1.8 pp at 30 June 2037. Coverage: full read.

## D04 (page Doc 6) - Economic Reform Roundtable: Budget sustainability and tax reform (2025)

- Built on the 2025-26 Budget / 2025 PEFO. Chart 7 note (line 139): growth rates for the October
  2022-23 Budget (2022-23 to 2032-33) and the 2025-26 Budget (2025-26 to 2035-36).
- Medium-term growth (2025-26 Budget): interest 9.5% (14.4% three years ago); NDIS ~8% (13.8%);
  hospitals ~6%; Medicare 5.6%; aged care 5.2% (6.2%); child care 5.1%; defence no figure.
- Gross debt: 39.1% peak 2020-21; est. 33.7% 2024-25; next peak 37.0% in 2029-30; 31.9% 2035-36.
- 2024-25 deficit "around 1/2 per cent of GDP, around half the size of the estimated deficit at
  the 2025-26 Budget". UCB improved $207b (2022 PEFO -> 2025 PEFO, 7 yrs to 2028-29); ~$100b
  savings; 70% of tax upgrades ($248.6b) returned; real payments 1.7% vs 30-year 3.2%.
- Coverage: full read.

## D05 (page Doc 5) - RBA Bulletin 2021: Government Bond Markets in Advanced Economies

- Mostly graphs. Defines bills as short-term securities up to one year (line 25). Cites Hudson et
  al (2021) = D09. Coverage: full read.

## D06 (page Doc 9) - ABS Government Finance Statistics, Australia, June 2026

- All levels of government combined (general government, PNFC). Quarterly Sep-25..Jun-26 ($m):
  taxation, revenue, expenses, NOB, net lending/borrowing; Jun-25 to Jun-26 in $b chart table.
  National-accounts tables split national (Commonwealth) / state and local, current prices and
  chain volume. No annual 2025-26 sum printed. Coverage: full read.

## D07 (page Doc 7) - RBA Bulletin Oct 2024: Inflation-linked Financial Markets

- Data cut-off end August 2024 (endnote). Indexed bonds < 5% of debt in Australia, Canada,
  Germany. Australia stopped issuing in 1989-1992 and 2004-2008.
- Table A.3 (lines 784-816): Australia 38 nominal lines, 7 indexed lines, average maturity
  mismatch 139 days, 10-year benchmark mismatch 61 days. Note (a): "Current outstanding bills or
  bonds, not including non-standard bonds on issue (e.g. green bonds and Treasury STRIPS)." Note
  (b): "Average difference between current indexed bonds outstanding and the closest maturity
  nominal bond." These sit at about character 29,500-29,900 (past the form's number-check reach).
- Coverage: full read.

## D08 (page Doc 8) - EC Economic Brief 094 (July 2026): Belgian unemployment benefit reform

- Belgian rules and EUROMOD results; no link to any other document. Coverage: partial (intro,
  system description); not needed for any sketch.

## D09 (page Doc 4) - RBA Bulletin June 2021: The Global Fiscal Response to COVID-19

- Narrative; ranges of support (5-24% of 2019 GDP). Coverage: full read.

## D10 (page Doc 10) - RBA RDP 2022-02: Yield and Market Function Effects of Bond Purchases

- Footnote 2 (line 156): AGS/semis split per program: market function $40.3b + $11.1b = $51.3b
  (20 Mar-6 May 2020); yield target $29b AGS (5 Aug 2020-22 Oct 2021); BPP $223.7b + $57.0b =
  $280.7b (5 Nov 2020-10 Feb 2022). 3-year AGS = residual maturity closest to three years.
- Table 1: nine event days, 10-year yield changes summing to -33 bps ("around 30").
- Internal inconsistency: line 415 "$4 billion per month" vs line 419 "$4 billion per week".
- Coverage: sections 1-5 read; regression tables skimmed.

## Shared ground (navigation only)

- Same budget, three statements: D01/D02/D03 repeat gross debt, net debt, interest figures.
- Editions: D04 (2025-26 Budget, 2025 PEFO) vs D01 (2026-27 Budget, MYEFO comparisons).
- Forecast/actual: D03 (2024-25 forecast errors, growth and dollars) vs D01 (2024-25 actual levels).
- Definition/data: D07 Table A.3 notes vs D02 Tables 7.4-7.6 (lines at 1 May 2026).
- RBA purchases: D10 footnote 2; D02 line 565 mentions the 2020-21 purchases.
- D05 cites D09. D07 and D10 share an author (Titkov); D05 and D07 share Nick Baker.
