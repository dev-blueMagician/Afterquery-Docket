# aq-06809 - document map

Maintained by the caller from `text/` (and `docs/` for layout issues). Navigation only, like the form's
bundle overview: where things are, not what to ask. Questions quote the documents, never this map.

## Bundle

- What it is: PEER corporate filings, three US regional banks' second-quarter 2026 earnings materials:
  Fifth Third (release + presentation), Huntington (release + financial supplement), KeyCorp (release with its
  financial supplement appended). Fifth Third closed Comerica and Huntington closed Cadence on February 1, 2026.
- Documents: 5; local ids (text/manifest.json) vs task-page Doc numbers (notes/intake.json):
  D01 = Doc 1 fitb_ex991 (FITB release, 2026-07-17); D02 = Doc 2 fitb_ex992 (FITB 2Q26 presentation);
  D03 = Doc 4 hban_ex991 (HBAN release, 2026-07-23); D04 = Doc 5 hban_ex992 (HBAN financial supplement);
  D05 = Doc 3 key_ex991 (KEY release + supplement, 2026-07-21). Ids sort by filename, so D03-D05 differ from Doc N.
- Gaps: none. All five read in full (2026-10-18). Capture says "5 of 5 read in full"; intake: every document
  matches the capture, no clipped range. The page carried a stale-page notice ("Docket has been updated. Reload
  this page ..."), which concerns the form's buttons, not the documents.
- Extraction spot-checks: plain-text sources (method "text", no pages). Tables arrive as pipe rows; columns
  are mostly readable, with known misalignments: D01 L1382-1396 (NCO ratio by product, cells shifted), D01
  L588/697 (credit-quality rows), D05 L1019-1029 (average-balance header). D02 is slide text run together;
  charts are bare number strings (e.g. slide 9 "4.50% ... 3.75% 1.80% 1.81% 1.71% 1.58% 1.54% Fed Funds Rate
  Total Cost of Deposits 2Q25 ... 2Q26": Fed funds first, then total cost of deposits).
- Provenance: notes/intake.json (capture sha 3553109e..., per-document hashes); corpus sha ce0f338a0e1a6ad5 (mine.md).
- Reuse binding: map written against text/ of corpus ce0f338a; refresh only if a source hash changes.

## D01 - Fifth Third Bancorp Q2 2026 earnings release (Doc 1)

- Source: docs/fitb_ex991_2026-07-17.txt | 1,763 lines
- Written by: Fifth Third Bancorp. Period: quarters Jun-26, Mar-26 (and Dec-25, Sep-25, Jun-25 in the
  Quarterly Financial Review); YTD June 2026 vs June 2025 columns (L531-555, L750-802, L1124-1191).
- Tables: highlights L15-80; income statement highlights L93-113; NII L137-158; noninterest income L162-200
  (certain items L185-197); noninterest expense L204-244 (certain items L226-241: merger-related (203) (635));
  average/period-end balances L248-318; deposits L320-350; credit quality L377-445 (ALLL roll L403-416:
  PCD 180, PSL 481 at acquisition); capital L447-474; financial highlights 5-quarter L637-743; statements of
  income L747-861; balance sheets L865-1011; equity changes L1015-1042 ("Impact of Comerica acquisition
  12,676"; no shares acquired for treasury in 2026); average balance sheets L1046-1191; loans L1195-1264;
  regulatory capital L1268-1308; credit loss by product L1312-1398 (consumer NCO ratio 0.53% L1395);
  asset quality L1402-1489; non-GAAP L1493-1677 (efficiency (FTE) = (w)/[(a)+(u)] L1665; adjusted L1666;
  merger-related charges 203 / 657 and Day 1 ACL build 83 L1607-1614); segments L1680-1759.
- Footnotes: "(h)/(a)/(d) Excludes net charge-offs of $111 million which were taken immediately at the time of
  acquisition" (Q1 2026; L438, L633, L743, L1398, L1489) - conflicts with D02 slide 10 note ($21 million);
  NPA ratio excludes nonaccrual HFS 167 (L1450, L1485); ACL ratio over portfolio loans (excl. HFS).
- Prose figures: "$933 million of pre-tax merger related impacts" YTD (L474; detail sums to 943) and "approximately
  65% of the expected full-year total" (L244); "no share repurchase activity in the first half of 2026" (L474).
- Coverage: full.

## D02 - Fifth Third 2Q26 earnings presentation (Doc 2)

- Source: docs/fitb_ex992_2026-07-17.txt | 99 long lines (slides as paragraphs)
- Unique to D02: FY2026 and 3Q26 guidance (slides 13-14: NII $8.74-8.80B, FY25 baseline $6.00B; NIE $7.22-7.26B
  excl. acquisition charges; 3Q26 NII up 2-2.5% on $2.22B); NII walk 1Q26->2Q26 (slide 5: "Additional month of
  Comerica 196"); total cost of deposits chart (slide 9, 1.54% 2Q26); CET1 walk and CET1 incl. AOCI 8.7%
  (slide 12; end note 2 "Excludes AOCI on cash flow hedges"); NPL rollforward with acquired nonaccrual loans
  (slide 31); 4Q25/3Q25 adjustment columns (slides 41-42: merger-related 13 in 4Q25); end notes (slide 10 note 2
  "1Q26 excludes net charge-offs of $21 million which were taken immediately at time of merger"; slide 39 note 3:
  Comerica merged into Fifth Third "on February 1, 2026" - the only place the FITB closing date is printed).
- Coverage: full.

## D03 - Huntington Bancshares Q2 2026 earnings release (Doc 4)

- Source: docs/hban_ex991_2026-07-23.txt | 434 lines
- Tables (five quarters Q2'26 ... Q2'25): Table 1 L65-101; Table 2 Notable Items L103-136 (Q2'26 acquisition-
  related (152); Q1'26 (263) + CECL double count (8); Q2'25 FDIC +3 and staffing (6)); Table 3 revenue L139-153;
  Table 4 NIM L154-172; Table 5 average earning assets L176-211 (acquisition dates and acquired balances L209:
  Cadence completed February 1, 2026, $36.9B loans; Veritex October 20, 2025, $9.3B); Table 6 liabilities
  L213-242 (Cadence $43.5B deposits, Veritex $10.5B, L240); Table 7 noninterest income L245-275 (Q2'25 $58M
  securities loss "as part of ongoing portfolio positioning" L274); Table 8 NIE L278-297; Table 9 Notable Items
  by line L301-320 (acquisition-related row L318: 152 263 154 14 —); Table 10 adjusted NIE L322-342 (1,657 ...
  1,194); Table 11 credit L345-389 (consumer NCO 0.30% in prose L387); Table 12 capital L392-406; tax L408-409.
- Coverage: full.

## D04 - Huntington Q2 2026 quarterly financial supplement (Doc 5)

- Source: docs/hban_ex992_2026-07-23.txt | 1,596 lines
- Key statistics (quarter L172-237, YTD L242-284; efficiency definition note (4) L294); balance sheets L301-363
  (Dec 31, 2025 column); loans by type/segment L367-409 (five quarter-ends); deposits L413-450; average balances
  L454-521; interest income/expense L525-584; yields L588-658 (total cost of deposits 1.88% L655); income
  statement L662-740; mortgage banking L744-780; credit reserves L784-848 (PCD 322, PSL 245 at acquisition, ASU
  2025-08 note L825); NCO by type L852-896 (total consumer 0.30 L895); NALs/NPAs L900-946; past due L950-977;
  Basel III L981-1026 (adjusted CET1 = CET1 + AOCI - CFH AOCI, L1013-1023); TCE L1045-1069; ROTCE and efficiency
  calculations L1087-1128; YTD averages, rates, income, reserves, NCOs, NPAs L1132-1592.
- Coverage: full.

## D05 - KeyCorp Q2 2026 earnings release with financial supplement (Doc 3)

- Source: docs/key_ex991_2026-07-21.txt | 1,520 lines
- Release L9-457 (headline $472M is continuing operations to common; GAAP net income to common 473, L561);
  supplement L460-1520: highlights L538-723 (cash efficiency, marked CET1); non-GAAP L728-866 (cash efficiency
  N/Q L838; marked CET1 = CET1 + AFS and pension AOCI L783-795; operating leverage S - T L853-859: 1.28 for
  Q2'26); balance sheet L871-924; income statement L929-1009; average balances L1015-1187; loans L1229-1269
  (total loans exclude $182M discontinued education loans, note (b) L1253); loan-loss experience L1288-1362
  (consumer charged off 26, recoveries 6, L1314/L1331); asset quality L1368-1436; line of business L1441-1475
  (Consumer Bank NCO ratio 0.54%, L1458 - a segment, not the consumer loan category); selected items L1479-1518
  ("No items" Q2'26, Q1'26, Q2'25).
- Coverage: full.

## Shared ground (navigation only)

- Same-day closings: Comerica into Fifth Third (D02 slide 39 note only) and Cadence into Huntington (D03 L209),
  both February 1, 2026; Q1 2026 holds two months of each.
- Each bank's own efficiency definition: FITB NIE / (FTE NII + noninterest income) (D01 L1665); HBAN NIE less
  amortization / (FTE revenue less securities gains) (D04 L294, L1128); KEY cash efficiency, NIE less
  amortization / TE revenue (D05 L736, L838).
- Deal-cost labels: FITB "Merger-related charges" (D01 L232, L1607); HBAN "Acquisition-related expenses"
  (D03 L113-117, L318); KEY none ("No items").
- AOCI-inclusive CET1 on three bases: FITB 8.7% excl. CFH AOCI (D02); HBAN adjusted CET1 9.0% excl. CFH (D04
  L1023); KEY marked CET1 9.8%, AFS and pension AOCI only (D05 L746, L795).
- Periods no document reports on its own: Q1 2025 for all three (six months 2025 less Q2 2025); FY2025 for FITB
  and HBAN (H1 2025 + Q3 + Q4 2025); KEY prints Q3/Q4 2025 only for credit, segments and HFS flows.
- Consumer NCO rates: FITB 0.53% and HBAN 0.30% printed; KEY prints only segment (0.54%) and total (0.42%).
- Deposit costs: interest-bearing in each release (FITB 2.13%, HBAN 2.29%, KEY 2.01%); total cost only in
  D02 (1.54%), D04 (1.88%) and D05 (1.63%).
