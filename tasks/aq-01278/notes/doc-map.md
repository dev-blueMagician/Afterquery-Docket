# aq-01278 - document map

Written once by `bundle-mapper` from `text/` (and `docs/` for flattened tables and scans).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

Location convention: `Dnn Lx` = line x of `text/Dnn.txt` (the docs/ original is the same text
plus or minus a one-line header and blank-line collapse). `p.N` = the document's own printed page
number; `S N` = D03 "1Q 26 Supplement N"; D10 pages per its own footer. Figures are copied as
printed: parentheses = negative/unfavourable as printed, "—" = printed dash. Arithmetic checks
recorded here are consistency checks only (sums/differences of printed figures), not findings.

## Bundle

- What it is: ten SEC exhibit texts (EX-99.1 press releases and EX-99.2 supplements) from four
  US property-casualty insurers, two quarterly editions each for Q1 and Q2 calendar 2026:
  Allstate (D01 Q1 release, D02 Q2 release, D03 Q1 investor supplement), Chubb (D04 Q1, D05 Q2),
  Progressive (D06 March 2026 monthly/Q1 release, D07 June 2026 monthly/Q2 release), Travelers
  (D08 Q1 release, D09 Q2 release, D10 Q1 financial supplement). Release dates April 15 -
  August 5, 2026.
- Documents: 10; ids D01-D10 from `text/manifest.json` (local id = platform Doc number):
  D01 = Doc 5, D02 = Doc 10, D03 = Doc 6, D04 = Doc 4, D05 = Doc 9, D06 = Doc 1, D07 = Doc 7,
  D08 = Doc 2, D09 = Doc 8, D10 = Doc 3.
- Gaps: see the final "Gaps and continuation" section (kept current while mapping).
- Extraction spot-checks: all sources are plain text (method "text", pages null), so page
  counts are not applicable; printed page numbers are recorded instead. Per-document checks of
  one table row and one footnote against `docs/` are listed on each document's Coverage line.
- Provenance: `notes/intake.json` (schema 1, capture_sha256 8830215724...4366): ten documents,
  each `incomplete: false`, `gap_characters: 0`, `matches_capture: true`; source hashes equal
  `text/manifest.json` hashes. Caller-verified extraction report 2026-10-06: capture
  AQ-01278_2026-10-06_1140.txt says "10 of 10 read in full", no gap markers. No recovered-source
  history.

## D01 - Allstate first quarter 2026 earnings release (Exhibit 99.1)

- Source: `docs/all_ex991_2026-04-29.txt` -> `text/D01.txt` (491 lines); platform Doc 5
  (all_ex991_2026-04-29). Pages: not applicable (text); printed page numbers 1-11 at L32, L86,
  L136, L184, L225, L234, L308, L357, L390, L440, L488.
- Written or submitted by: The Allstate Corporation (NYSE: ALL), Northbrook, Ill. Contacts
  Nick Nottoli (Media Relations), Allister Gobin (Investor Relations) L14-15. Quoted: Tom Wilson
  "who leads The Allstate Corporation" L20-22; John Dugenske, "Interim Chief Financial Officer
  and President, Investments and Corporate Strategy" L221.
- Type, date, edition: press release, "FOR IMMEDIATE RELEASE", April 29, 2026 (L19); headline
  "Allstate Reports Strong Earnings and Increased Growth" L17; html name
  allcorp33126earningsreleas.htm L4. Conference call 9 a.m. ET Thursday, April 30 (L223).
- Period covered: "first quarter of 2026" = "three months ended March 31," 2026 vs 2025
  (calendar quarters; no fiscal-year statement). ROE and one total-return row are trailing
  twelve months to March 31. Balance sheet March 31, 2026 vs December 31, 2025.
- Entities and aliases: Allstate / The Allstate Corporation / ALL; segments Property-Liability,
  Allstate Protection (auto, homeowners), Protection Services ("comprised of five businesses"
  L145: Protection Plans, Roadside, Dealer Services, Identity Protection, Arity), Allstate
  Investments; brands/products Allstate brand, Affordable, Simple, Connected (ASC), Custom360,
  Esurance, Encompass (legacy, L110), National General legacy products (L141), Transformative
  Growth (strategy name, L22, L89).
- Tables (units $ millions unless noted; columns 2026 | 2025 | change):
  - p.2 Consolidated Highlights L36-58, "As of or for the three months ended March 31," cols
    2026 | 2025 | "% / pts Change": Consolidated revenues 16,941 | 16,452 | 3.0 %; Net income
    applicable to common shareholders 2,428 | 566 | NM; per diluted common share 9.25 | 2.11 | NM;
    Adjusted net income* 2,797 | 949 | NM; per diluted share* 10.65 | 3.53 | NM; ROE (trailing
    twelve months): net income 48.4 % | 21.4 % | 27.0, adjusted net income* 44.4 % | 23.7 % | 20.7;
    Common shares outstanding (in millions) 257.8 | 265.1 | (2.8)%; Book value per common share
    $113.52 | $74.61 | 52.2 %; Total policies in force (in thousands) (1) 212,052 | 206,898 |
    2.5 %. Footnote (1) L57 on total PIF: "Excludes policies in force related to the employer
    voluntary benefits and group health businesses sold in 2025." "NM = not meaningful" L56.
  - p.2 Property-Liability Results L63-77 (same column set): Premiums written 14,625 | 14,297 |
    2.3 %; Premiums earned 14,802 | 14,027 | 5.5 %; Recorded combined ratio 82.0 | 97.4 | (15.4);
    Underlying combined ratio* 80.3 | 83.1 | (2.8); Catastrophe losses 1,240 | 2,202 | (43.7)%;
    Underwriting income 2,658 | 360 | NM; Policies in force (thousands) 38,576 | 37,712 | 2.3 %.
  - p.3 Allstate Protection Auto Results L91-102: PW 9,850 | 9,848 | — %; PE 9,547 | 9,347 |
    2.1 %; Recorded CR 81.9 | 91.3 | (9.4); Underlying CR* 89.5 | 91.2 | (1.7); Underwriting
    income 1,729 | 816 | 111.9 %; PIF 25,758 | 25,100 | 2.6 %.
  - p.3 Allstate Protection Homeowners Results L114-129: PW 3,741 | 3,453 | 8.3 %; PE 4,164 |
    3,657 | 13.9 %; Recorded CR 83.5 | 112.3 | (28.8); Catastrophe Losses 1,046 | 1,824 |
    (42.7)%; Underlying CR* 60.5 | 62.4 | (1.9); Underwriting income (loss) 685 | (451) | NM;
    PIF 7,739 | 7,549 | 2.5 %.
  - p.4 Protection Services Results L147-170, "Three months ended March 31," cols 2026 | 2025 |
    "% / $ Change" (revenue rows show % change, adjusted net income rows show $ change): Total
    revenues (1) 922 | 860 | 7.2 %; Protection Plans 613 | 540 | 13.5; Roadside 63 | 55 | 14.5;
    Dealer Services 148 | 146 | 1.4; Identity Protection 40 | 40 | —; Arity 58 | 79 | (26.6);
    Adjusted net income (loss) 47 | 55 | (8); Protection Plans 41 | 45 | (4); Roadside 12 | 11 | 1;
    Dealer Services 5 | 4 | 1; Identity Protection 1 | 1 | —; Arity (12) | (6) | (6). Footnote (1)
    L170 on Total revenues: "Excludes net gains and losses on investments and derivatives."
    Layout: Roadside-Arity rows are tab rows after the pipe rows (L156-159, L166-169).
  - p.5 Allstate Investment Results L190-207, "Three months ended March 31," cols 2026 | 2025 |
    "$ / pts Change": Net investment income 938 | 854 | 84; Market-based (1) 791 | 719 | 72;
    Performance-based (1) 207 | 196 | 11; Net gains (losses) on investments and derivatives
    (405) | (349) | (56); Change in unrealized net capital gains and losses, pre-tax (2) (664) |
    540 | (1,204); Total return on investment portfolio (2) (0.2)% | 1.4 % | (1.6); same, trailing
    twelve months 4.2 % | 4.7 % | (0.5). Footnote (1) L206 "Investment expenses are not allocated
    between market-based and performance-based portfolios with the exception of investee level
    expenses." (2) L207 "Includes investments held for sale." Market-based + performance-based
    = 998, not 938 (expense split shown only in D03 S13/S14).
  - p.7 Condensed Consolidated Statements of Financial Position L236-306, March 31, 2026 |
    December 31, 2025 ($ millions except par value): fixed income 59,060 | 59,115 (amortized cost,
    net $59,338 and $58,730); equity securities 10,431 | 8,398 (cost $10,354 and $8,026);
    mortgage loans 868 | 879; limited partnership interests 8,946 | 8,844; short-term 4,705 |
    4,887; other investments 1,150 | 1,114; Total investments 85,160 | 83,237; cash 697 | 678;
    premium installment receivables 11,648 | 11,474; DAC 6,070 | 6,163; reinsurance and
    indemnification recoverables 8,422 | 8,501; accrued investment income 656 | 708; deferred
    income taxes (asset) 12 | —; property and equipment 606 | 627; goodwill 3,118 | 3,118; other
    assets 7,583 | 5,252; Total assets 123,972 | 119,758; reserve for P&C claims and claims
    expense 41,320 | 41,079; unearned premiums 28,863 | 29,080; claim payments outstanding
    1,473 | 1,419; deferred income taxes (liability) — | 227; other liabilities 13,238 | 9,874;
    Debt 7,491 | 7,490; Total liabilities 92,385 | 89,169; preferred stock 2,001 | 2,001 (82.0
    thousand shares, $2,050 aggregate liquidation preference, L282); common stock 9 | 9 ("258
    million and 260 million shares outstanding", L284); APIC 4,169 | 4,158; retained income
    64,540 | 62,393; treasury stock (38,820) | (38,206) ("642 million and 640 million shares",
    L289); AOCI: unrealized net capital gains and losses (221) | 297, FX (83) | (55), pension
    credit 10 | 11, discount rate 2 | 2, total (292) | 255; Total Allstate shareholders' equity
    31,607 | 30,610; noncontrolling interest (20) | (21); Total equity 31,587 | 30,589.
  - p.8 Condensed Consolidated Statements of Operations L310-355, three months ended March 31,
    2026 | 2025: P&C insurance premiums 15,553 | 14,698; accident and health insurance premiums
    and contract charges 136 | 487; other revenue 719 | 762; NII 938 | 854; net gains (losses)
    (405) | (349); Total revenues 16,941 | 16,452; P&C claims and claims expense 9,185 | 10,815;
    accident, health and other policy benefits 76 | 333; DAC amortization 2,178 | 2,087;
    operating costs and expenses 2,225 | 2,245; pension remeasurement 19 | 78; restructuring 5 |
    16; amortization of purchased intangibles 47 | 59; interest expense 98 | 100; Total costs
    13,833 | 15,733; pre-tax income 3,108 | 719; income tax 650 | 123; Net income 2,458 | 596;
    NCI 1 | 1; attributable to Allstate 2,457 | 595; preferred dividends 29 | 29; applicable to
    common 2,428 | 566; EPS basic 9.36 | 2.13 (weighted shares 259.4 | 265.3); EPS diluted 9.25 |
    2.11 (weighted 262.6 | 268.8). No gain-on-disposition row in this statement.
  - p.9 ANI reconciliation L371-388, three months ended March 31, consolidated 2026 | 2025 and
    per diluted share 2026 | 2025: NI applicable 2,428 | 566 | 9.25 | 2.11; net (gains) losses
    405 | 349 | 1.54 | 1.30; pension 19 | 78 | 0.07 | 0.29; amortization of purchased intangibles
    47 | 59 | 0.18 | 0.22; Gain on disposition (6) | — | (0.02) | —; income tax expense (benefit)
    (96) | (103) | (0.37) | (0.39); Adjusted net income 2,797 | 949 | 10.65 | 3.53.
  - p.10 ROE reconciliations L395-438, "For the twelve months ended March 31," 2026 | 2025: ROE
    numerator NI 12,027 | 3,927; beginning equity 20,054 | 16,638; ending equity (1) 29,606 |
    20,054; average 24,830 | 18,346; ROE 48.4 % | 21.4 %. ANI ROE: ANI 11,152 | 4,488; beginning
    20,054 | 16,638; less unrealized (351) | (819); adjusted beginning 20,405 | 17,457; ending
    29,606 | 20,054; less unrealized (221) | (351); adjusted ending 29,827 | 20,405; average
    adjusted 25,116 | 18,931; ANI ROE 44.4 % | 23.7 %. Footnote (1) L438 "Excludes equity related
    to preferred stock of $2,001 million for both periods shown."
  - p.11 Underlying combined ratio reconciliations L445-484, three months ended March 31, 2026 |
    2025 (rows add with printed signs): Property-Liability CR 82.0 | 97.4, catastrophe (8.4) |
    (15.7), prior year reserve reestimates excl. cats 6.9 | 1.7, amortization (0.2) | (0.3),
    underlying 80.3 | 83.1, memo "Effect of prior year catastrophe reserve reestimates" 0.1 |
    (0.1). Auto 81.9 | 91.3; (0.9) | (2.2); 8.8 | 2.5; (0.3) | (0.4); 89.5 | 91.2; memo — | (0.1).
    Homeowners 83.5 | 112.3; (25.1) | (49.9); 2.3 | 0.2; (0.2) | (0.2); 60.5 | 62.4; memo
    (0.4) | —.
- Lists: ANI exclusions L361-366 (five excluded item types plus related tax); underlying CR
  "four GAAP operating ratios" L442; Protection Services five businesses L145/L152-169; product
  availability L84 (ASC auto 45 states, ASC homeowners 36 states, Custom360 40 states).
- Forecasts, guidance, deadlines, effective dates: no numeric outlook. Forward-looking boilerplate
  L228-229. A "long-term adjusted net income return on Allstate common shareholders' equity
  goal" is mentioned with no value (L392).
- Hedged claims: L211 "quarterly volatility in reported results is expected" (performance-based
  income); L213 equity valuation declines in March "which have since recovered" (stated as
  fact); L360 "Our methods for calculating these measures may differ from those used by other
  companies".
- Rounded prose beside exact figures: revenues "$16.9 billion" (L20, L26) vs 16,941 and
  "$489 million or 3.0%"; NI "$2.4 billion" vs 2,428 (L20, L28); ANI "$2.8 billion" vs 2,797
  (L20, L30); "Policies in force reached 212 million" (L20) and "more than 212 million" (L232) vs
  212,052 thousand; "Investment income increased by 9.8%" (L20; table gives only $84 change);
  P-L earned premiums "$14.8 billion", UW income "$2.7 billion" (L61) vs 14,802 / 2,658;
  homeowners "Catastrophe losses of $1.0 billion ... decreased $778 million" (L134) vs 1,046 /
  1,824; "$85.2 billion portfolio" (L188) vs 85,160; duration "5.7 years" (L188; in D03 S13 5.7
  is the row "including interest rate derivative positions", the plain duration row is 5.5);
  market-based income "+$72 million, or 10.0%" and balances "$75.2 billion" (L209; D03 S14
  75,249); "Unrealized net capital losses totaled $282 million (pre-tax), a $664 million
  decrease to the prior quarter end" (L215) vs AOCI unrealized (221) on the balance sheet (L293,
  no pre-tax label); "44.4% over the last year" (L221).
- Notes: auto prior year reserve liabilities "lowered by $838 million as estimated claims costs
  for 2023 through 2025 were reduced, improving the current quarter combined ratio by 8.8
  points" (L106); auto new business +9.4%, active brand auto policies +3.5% (L110); homeowners
  underwriting "profit of $685 million increased from a loss of $451 million ... primarily
  reflecting 2025's California wildfire losses" (L112); Allstate brand homeowners average gross
  written premium +6.8% (L130); homeowners PIF +2.5%, Allstate brand homeowners policies +3.2%,
  National General legacy reduction (L141); capital: "$881 million of cash was provided to
  shareholders through dividends and share repurchases" (L221, no split); "higher dividends and
  increased share repurchases" (L22). Statement P&C insurance premiums 15,553 (L318) and
  Property-Liability premiums earned 14,802 (L70) are different line items (scope per D03 S17).
- Operative definitions, rules and scope exceptions:
  - Adjusted net income L361-366: "net income (loss) applicable to common shareholders,
    excluding: Net gains and losses on investments and derivatives / Pension and other
    postretirement remeasurement gains and losses / Amortization or impairment of purchased
    intangibles / Gain or loss on disposition / Adjustments for other significant non-recurring,
    infrequent or unusual items, when (a) ... reasonably unlikely to recur within two years, or
    (b) there has been no similar charge or gain within the prior two years / Related income tax
    expense or benefit of these items". Taxes "generally use a 21% effective tax rate" (L369).
  - ANI ROE L392: "calculated by dividing the rolling 12-month adjusted net income by the average
    of Allstate common shareholders' equity at the beginning and at the end of the 12-months,
    after excluding the effect of unrealized net capital gains and losses."
  - Underlying combined ratio L442: "computed as the difference between four GAAP operating
    ratios: the combined ratio, the effect of catastrophes on the combined ratio, the effect of
    prior year reserve reestimates, excluding catastrophes on the combined ratio, and the effect
    of amortization or impairment of purchased intangibles on the combined ratio." L443
    "Underwriting margin is calculated as 100% minus the combined ratio."
  - Total PIF scope: footnote L57 (excludes divested employer voluntary benefits and group
    health businesses "sold in 2025").
  - Book value per common share: value only (L53); denominator defined in D03 S3 (not here).
    Ending common equity for ROE excludes preferred $2,001 million (L438).
- Amendments or contradictions: none stated inside D01. Cross-document relationships under
  Shared ground.
- Coverage: FULL. Ledger: L1-491 read in one pass; remaining none. Spot-check vs `docs/`:
  table row "Book value per common share $|113.52 $|74.61 52.2 %" (docs line 54) and footnote
  "(1)Excludes policies in force related to the employer voluntary benefits..." (docs line 59)
  identical to text L53/L57.

## D02 - Allstate second quarter 2026 earnings release (Exhibit 99.1)

- Source: `docs/all_ex991_2026-08-05.txt` -> `text/D02.txt` (540 lines); platform Doc 10
  (all_ex991_2026-08-05). Pages: not applicable; printed page numbers 1-11 at L31, L93, L153,
  L210, L256, L265, L340, L394, L440, L490, L537.
- Written or submitted by: The Allstate Corporation; same contacts as D01 (L14-15). Quoted: Tom
  Wilson L19-21; John Dugenske, "President, Investments and Corporate Strategy" (L252; the D01
  title "Interim Chief Financial Officer and" is absent here).
- Type, date, edition: press release, August 5, 2026 (L18); headline "Allstate Reports Excellent
  Operating Results" L17; html allcorp63026earningsreleas.htm L4. Conference call 9 a.m. ET
  Thursday, August 6 (L254). Second Allstate release edition in the bundle (D01 is the first).
- Period covered: "second quarter of 2026" = three months ended June 30, 2026 vs 2025, plus six
  months ended June 30, 2026 vs 2025 (year to date); ROE and one total-return row trailing twelve
  months to June 30. Balance sheet June 30, 2026 vs December 31, 2025. No March 31, 2026 column
  anywhere in D02.
- Entities and aliases: as D01 (L91 adds nothing new; L156 "Allstate agent productivity").
- Tables (columns: Q2 2026 | Q2 2025 | change || 6M 2026 | 6M 2025 | change):
  - p.2 Consolidated Highlights L35-62, "As of or for the three months ended June 30, As of or
    for the six months ended June 30,": Consolidated revenues 18,596 | 16,633 | 11.8 % || 35,537 |
    33,085 | 7.4 %; NI applicable 3,241 | 2,079 | 55.9 % || 5,669 | 2,645 | 114.3 %; per diluted
    12.51 | 7.76 | 61.2 % || 21.73 | 9.85 | 120.6 %; ANI* 2,330 | 1,591 | 46.4 % || 5,127 | 2,540 |
    101.9 %; ANI per diluted* 8.99 | 5.94 | 51.3 % || 19.65 | 9.46 | 107.7 %. As-of rows (one pair
    only): ROE TTM net income 49.1 % | 29.6 % | 19.5, ANI* 44.2 % | 28.6 % | 15.6; Common shares
    outstanding (millions) 253.5 | 263.8 | (3.9)%; Book value per common share $123.38 | $82.40 |
    49.7 %; Total PIF (thousands) (1) 215,935 | 208,051 | 3.8 %. Footnote (1) L61 identical to D01
    L57. Pipe layout splits header labels across L38-42.
  - p.2 Property-Liability Results L67-83: PW 15,431 | 15,047 | 2.6 % || 30,056 | 29,344 | 2.4 %;
    PE 14,918 | 14,346 | 4.0 % || 29,720 | 28,373 | 4.7 %; Recorded CR 86.6 | 91.1 | (4.5) || 84.3 |
    94.2 | (9.9); Underlying CR* 79.4 | 79.5 | (0.1) || 79.8 | 81.3 | (1.5); Catastrophe losses
    1,722 | 1,990 | (13.5)% || 2,962 | 4,192 | (29.3)%; Underwriting income 2,006 | 1,280 | 56.7 %
    || 4,664 | 1,640 | 184.4 %; PIF 38,897 | 37,900 | 2.6 % (as of June 30 only).
  - p.3 Auto Results L98-113: PW 9,572 | 9,533 | 0.4 % || 19,422 | 19,381 | 0.2 %; PE 9,644 |
    9,528 | 1.2 % || 19,191 | 18,875 | 1.7 %; Recorded CR 83.3 | 86.0 | (2.7) || 82.6 | 88.6 |
    (6.0); Underlying CR* 87.6 | 87.8 | (0.2) || 88.5 | 89.5 | (1.0); UW income 1,606 | 1,331 |
    20.7 % || 3,335 | 2,147 | 55.3 %; PIF 25,951 | 25,243 | 2.8 %.
  - p.3 Homeowners Results L125-144: PW 4,752 | 4,395 | 8.1 % || 8,493 | 7,848 | 8.2 %; PE 4,201 |
    3,771 | 11.4 % || 8,365 | 7,428 | 12.6 %; Recorded CR 94.6 | 102.0 | (7.4) || 89.1 | 107.1 |
    (18.0); Catastrophe losses 1,408 | 1,614 | (12.8)% || 2,454 | 3,438 | (28.6)%; Underlying CR*
    61.5 | 58.6 | 2.9 || 61.0 | 60.5 | 0.5; UW income (loss) 226 | (76) | NM || 911 | (527) | NM;
    PIF 7,819 | 7,596 | 2.9 %.
  - p.4 Protection Services Results L162-196 ("% / $ Change"): Total revenues (1) 935 | 867 |
    7.8 % || 1,857 | 1,727 | 7.5 %; Protection Plans 615 | 563 | 9.2 || 1,228 | 1,103 | 11.3;
    Roadside 66 | 56 | 17.9 || 129 | 111 | 16.2; Dealer Services 147 | 148 | (0.7) || 295 | 294 |
    0.3; Identity Protection 40 | 41 | (2.4) || 80 | 81 | (1.2); Arity 67 | 59 | 13.6 || 125 | 138 |
    (9.4); ANI (loss) 53 | 60 | (7) || 100 | 115 | (15); Protection Plans 42 | 51 | (9) || 83 | 96 |
    (13); Roadside 13 | 11 | 2 || 25 | 22 | 3; Dealer Services 3 | 4 | (1) || 8 | 8 | —; Identity
    Protection 2 | 2 | — || 3 | 3 | —; Arity (7) | (8) | 1 || (19) | (14) | (5). Footnote (1) L196
    as D01 L170.
  - p.5 Investment Results L216-238 ("$ / pts Change"): NII 1,009 | 754 | 255 || 1,947 | 1,608 |
    339; Market-based (1) 837 | 733 | 104 || 1,628 | 1,452 | 176; Performance-based (1) 239 | 79 |
    160 || 446 | 275 | 171; Net gains (losses) 1,055 | (144) | 1,199 || 650 | (493) | 1,143; Change
    in unrealized net capital gains and losses, pre-tax (2) 185 | 492 | (307) || (479) | 1,032 |
    (1,511); Total return (2) 2.6 % | 1.4 % | 1.2 || 2.5 % | 2.8 % | (0.3); TTM total return 5.6 % |
    5.4 % | 0.2. Footnotes (1) L237, (2) L238 identical to D01 L206-207.
  - p.7 Statements of Financial Position L267-338, June 30, 2026 | December 31, 2025: fixed income
    60,809 | 59,115 (amortized cost $60,902 and $58,730); equity securities 11,159 | 8,398 (cost
    $10,071 and $8,026); mortgage loans 842 | 879; LP interests 8,967 | 8,844; short-term 4,872 |
    4,887; other investments 1,153 | 1,114; Total investments 87,802 | 83,237; cash 840 | 678;
    premium installment receivables 11,864 | 11,474; DAC 6,139 | 6,163; reinsurance recoverables
    7,880 | 8,501; accrued investment income 730 | 708; (no deferred-tax asset row); property and
    equipment 591 | 627; goodwill 3,118 | 3,118; other assets 5,792 | 5,252; Total assets 124,756
    | 119,758; claims reserve 40,979 | 41,079; unearned premiums 29,388 | 29,080; claim payments
    outstanding 1,552 | 1,419; deferred income taxes 172 | 227; other liabilities 11,495 | 9,874;
    Debt 7,492 | 7,490; Total liabilities 91,078 | 89,169; preferred 2,001 | 2,001; common stock
    9 | 9 ("254 million and 260 million shares outstanding", L316); APIC 4,219 | 4,158; retained
    income 67,504 | 62,393; treasury stock (39,842) | (38,206) ("646 million and 640 million
    shares", L321); AOCI unrealized (79) | 297, FX (126) | (55), pension 10 | 11, discount rate
    2 | 2, total (193) | 255; Total Allstate shareholders' equity 33,698 | 30,610; NCI (20) | (21);
    Total equity 33,678 | 30,589. December 31, 2025 column = D01's December 31, 2025 column.
  - p.8 Statements of Operations L342-392 (Q2 2026 | Q2 2025 | 6M 2026 | 6M 2025): P&C premiums
    15,670 | 15,041 | 31,223 | 29,739; A&H premiums 134 | 235 | 270 | 722; other revenue 728 | 747
    | 1,447 | 1,509; NII 1,009 | 754 | 1,947 | 1,608; net gains 1,055 | (144) | 650 | (493); Total
    revenues 18,596 | 16,633 | 35,537 | 33,085; P&C claims 9,862 | 10,249 | 19,047 | 21,064; A&H
    benefits 72 | 188 | 148 | 521; DAC 2,202 | 2,076 | 4,380 | 4,163; operating costs 2,315 |
    2,135 | 4,540 | 4,380; pension (146) | — | (127) | 78; restructuring 7 | 15 | 12 | 31;
    amortization of purchased intangibles 46 | 57 | 93 | 116; interest 96 | 100 | 194 | 200; Total
    costs 14,454 | 14,820 | 28,287 | 30,553; "Gain on disposition of operations" — | 890 | — | 890
    (L378); pre-tax 4,142 | 2,703 | 7,250 | 3,422; tax 871 | 604 | 1,521 | 727; Net income 3,271 |
    2,099 | 5,729 | 2,695; NCI — | (10) | 1 | (9); attributable to Allstate 3,271 | 2,109 | 5,728 |
    2,704; preferred dividends 30 | 30 | 59 | 59; NI applicable 3,241 | 2,079 | 5,669 | 2,645; EPS
    basic 12.66 | 7.86 | 22.00 | 9.98 (weighted 256.0 | 264.6 | 257.7 | 264.9); EPS diluted 12.51 |
    7.76 | 21.73 | 9.85 (weighted 259.1 | 267.9 | 260.9 | 268.4).
  - p.9 ANI reconciliations: three months L408-425: NI 3,241 | 2,079 | 12.51 | 7.76; net (gains)
    losses (1,055) | 144 | (4.07) | 0.54; pension (146) | — | (0.57) | —; amortization 46 | 57 |
    0.18 | 0.21; Gain on disposition (1) | (893) | — | (3.33); income tax 245 | 204 | 0.94 | 0.76;
    ANI 2,330 | 1,591 | 8.99 | 5.94. Six months L427-438: NI 5,669 | 2,645 | 21.73 | 9.85; net
    (gains) losses (650) | 493 | (2.49) | 1.84; pension (127) | 78 | (0.49) | 0.29; amortization
    93 | 116 | 0.36 | 0.43; Gain on disposition (7) | (893) | (0.03) | (3.33); income tax 149 |
    101 | 0.57 | 0.38; ANI 5,127 | 2,540 | 19.65 | 9.46.
  - p.10 ROE reconciliations L445-488, twelve months ended June 30, 2026 | 2025: NI 13,189 |
    5,705; beginning 22,018 | 16,592; ending (1) 31,697 | 22,018; average 26,858 | 19,305; ROE
    49.1 % | 29.6 %. ANI 11,891 | 5,650; beginning 22,018 | 16,592; less unrealized 36 | (938);
    adjusted beginning 21,982 | 17,530; ending 31,697 | 22,018; less unrealized (79) | 36;
    adjusted ending 31,776 | 21,982; average adjusted 26,879 | 19,756; ANI ROE 44.2 % | 28.6 %.
    Footnote (1) L488 preferred $2,001 million.
  - p.11 Underlying CR reconciliations L495-533 (Q2 2026 | Q2 2025 | 6M 2026 | 6M 2025):
    Property-Liability CR 86.6 | 91.1 | 84.3 | 94.2; cat (11.5) | (13.9) | (10.0) | (14.8); PYD
    excl. cats 4.6 | 2.6 | 5.8 | 2.2; amortization (0.3) x4; underlying 79.4 | 79.5 | 79.8 | 81.3;
    memo prior year cat reestimates 0.3 | — | 0.2 | —. Auto 83.3 | 86.0 | 82.6 | 88.6; (2.2) | (2.2)
    | (1.6) | (2.2); 6.6 | 4.3 | 7.7 | 3.4; (0.1) | (0.3) | (0.2) | (0.3); 87.6 | 87.8 | 88.5 | 89.5;
    memo (0.1) | (0.2) | (0.1) | (0.2). Homeowners 94.6 | 102.0 | 89.1 | 107.1; (33.5) | (42.8) |
    (29.3) | (46.3); 0.7 | (0.3) | 1.5 | —; (0.3) x4; 61.5 | 58.6 | 61.0 | 60.5; memo 1.6 | 0.5 |
    0.6 | 0.3.
- Lists: same ANI exclusion list (L398-403), same five Protection Services businesses (L160,
  L171-194); product availability L91 (ASC auto 45 states, ASC homeowners 41 states, Custom360
  41 states).
- Forecasts, guidance, deadlines, effective dates: no numeric outlook; forward-looking
  boilerplate L259-260; long-term ANI ROE goal mentioned without a value (L442).
- Hedged claims: L242 "quarterly volatility in reported results is expected"; L397 methods "may
  differ".
- Rounded prose beside exact figures: revenues "$18.6 billion" and "$2.0 billion or 11.8%"
  (L19, L25) vs 18,596 / 16,633; NI "$3.2 billion" vs "$2.1 billion" (L27); ANI "$2.3 billion,
  or $8.99" vs "$1.6 billion" (L29); "Share repurchases were increased to $1.0 billion for the
  quarter" (L19); cash returns "$3.5 billion, or 6.7% of market capitalization, over the last
  year" (L21); P-L earned premiums "$14.9 billion", UW income "$2.0 billion" vs "$1.3 billion"
  (L65); homeowners "Catastrophe losses of $1.4 billion ... decreased 12.8%" (L149) vs 1,408;
  "$87.8 billion portfolio", NII "$1.0 billion ... increased by $255 million" (L214) vs 87,802 /
  1,009; market-based +$104 million "or 14.2%", balances "$78.0 billion" (L240); net gains
  "$1.1 billion" (L244) vs 1,055; "Unrealized net capital losses totaled $97 million (pre-tax),
  a $185 million increase to the prior quarter end" (L246); "Allstate has 216 million policies in
  force" (L263) vs 215,935 thousand; capital "returned $1.3 billion to shareholders through $1.0
  billion in share repurchases and $280 million in dividends" (L252).
- Notes: Q2 P-L CR improvement "driven by lower catastrophe losses and more favorable prior year
  reserve releases, partially offset by higher legal expenses" (L87); underlying auto CR: "This
  quarter benefited from 2.4 points of favorable development on claims reported in the first
  quarter of 2026" (L119); auto new business +8.8% (L121); homeowners "Underwriting profit of
  $226 million increased from a loss of $76 million" (L123), Allstate brand homeowners average
  gross written premium +5.8% (L145), underlying 61.5 "2.9 points above ... reflecting higher
  loss costs" (L151), homeowners new business +16.4% (L156); Protection Services ANI "decreased
  by $7 million ... primarily due to higher Protection Plans claim costs" (L160) while Protection
  Plans ANI "decreased $9 million ... primarily reflecting lower margins on major appliances"
  (L198); Arity revenue +13.6% "driven by higher lead generation advertising sales" (L206).
  Q2 2025 "Gain on disposition of operations" 890 (statement L378) vs "Gain on disposition"
  (893) in the ANI reconciliation (L421); Q2 2026 statement row "—" vs reconciliation (1) (D03
  S2 footnote (1) explains contingent consideration in operating costs).
- Operative definitions: ANI L398-403 and 21% tax L406 (verbatim as D01); ANI ROE L442
  (verbatim as D01); underlying CR L492-493 (verbatim as D01); PIF footnote L61. BVPS value only
  (L58), no denominator printed in D02.
- Amendments or contradictions: none stated. D02's six-month and prior-year columns repeat or
  imply D01 figures (see Shared ground); no restatement language found.
- Coverage: FULL. Ledger: L1-540 read in one pass; remaining none. Spot-check vs `docs/`: BVPS
  row (docs line 63), PIF footnote (docs line 67) and gain-on-disposition rows (docs lines 448,
  496, 517) identical to text L58, L61, L378, L421, L436.

## D03 - Allstate Investor Supplement, First Quarter 2026 (Exhibit 99.2)

- Source: `docs/all_ex992_2026-04-29.txt` -> `text/D03.txt` (48 lines: cover L9, contents L11,
  one line per supplement page S1-S17 at odd lines L13-L45, end marker L47); platform Doc 6
  (all_ex992_2026-04-29). Pages: not applicable; printed footers "The Allstate Corporation 1Q 26
  Supplement N", N = 1-17 (S1 L13, S2 L15, S3 L17, S4 L19, S5 L21, S6 L23, S7 L25, S8 L27,
  S9 L29, S10 L31, S11 L33, S12 L35, S13 L37, S14 L39, S15 L41, S16 L43, S17 L45).
- Written or submitted by: The Allstate Corporation (no named people).
- Type, date, edition: investor supplement, "First Quarter 2026" (L9, L11); html
  allcorp33126investorsupp.htm L4; file date 2026-04-29 (same day as D01). No Q2 supplement in
  the bundle.
- Period covered: five quarterly columns: three months ended March 31, 2026; Dec. 31, 2025;
  Sept. 30, 2025; June 30, 2025; March 31, 2025 (as-of columns for balance items; S4 uses
  "twelve months ended" the same five dates; S8 uses four quarters Q1 2026-Q2 2025).
- Entities and aliases: segments Allstate Protection, Run-off Property-Liability (S6),
  Property-Liability (= Allstate Protection + Run-off, S6 footnote (1)), Protection Services,
  Corporate (S12); "Allstate Health and Benefits segment is no longer a reportable segment"
  starting Q3 2025 (L11, S5 footnote (2)); Answer Financial (S7 row), Ivantage (S17), Allstate
  Life Insurance Company (sold 2021, S2 footnote), Reciprocal Exchanges (S13/S14 footnotes).
- Tables ($ millions unless noted; five columns Q1 26 | Q4 25 | Q3 25 | Q2 25 | Q1 25):
  - S1 L13 Statements of Operations: P&C premiums 15,553 | 15,511 | 15,253 | 15,041 | 14,698; A&H
    premiums 136 | 114 | 110 | 235 | 487; other revenue 719 | 755 | 691 | 747 | 762; NII 938 | 892
    | 949 | 754 | 854; net gains (405) | 73 | 252 | (144) | (349); Total revenues 16,941 | 17,345 |
    17,255 | 16,633 | 16,452; P&C claims 9,185 | 7,736 | 8,654 | 10,249 | 10,815; A&H benefits 76
    | 68 | 67 | 188 | 333; DAC 2,178 | 2,125 | 2,101 | 2,076 | 2,087; operating costs 2,225 |
    2,332 | 2,265 | 2,135 | 2,245; pension 19 | (5) | (108) | — | 78; restructuring 5 | 13 | 17 |
    15 | 16; amortization 47 | 56 | 59 | 57 | 59; interest 98 | 98 | 101 | 100 | 100; Total costs
    13,833 | 12,423 | 13,156 | 14,820 | 15,733; Gain (loss) on disposition of operations — | (7) |
    720 | 890 | —; pre-tax 3,108 | 4,915 | 4,819 | 2,703 | 719; tax 650 | 1,088 | 1,075 | 604 | 123;
    Net income 2,458 | 3,827 | 3,744 | 2,099 | 596; NCI 1 | (5) | (2) | (10) | 1; attributable
    2,457 | 3,832 | 3,746 | 2,109 | 595; preferred dividends 29 | 29 | 29 | 30 | 29; NI applicable
    2,428 | 3,803 | 3,717 | 2,079 | 566; EPS basic 9.36 | 14.55 | 14.13 | 7.86 | 2.13 (weighted
    259.4 | 261.3 | 263.1 | 264.6 | 265.3); EPS diluted 9.25 | 14.37 | 13.95 | 7.76 | 2.11 (weighted
    262.6 | 264.7 | 266.4 | 267.9 | 268.8); "Cash dividends declared per common share" $1.08 |
    $1.00 | $1.00 | $1.00 | $1.00.
  - S2 L15 Contribution to Income: NI applicable 2,428 | 3,803 | 3,717 | 2,079 | 566; net (gains)
    losses 405 | (73) | (252) | 144 | 349; pension 19 | (5) | (108) | — | 78; amortization 47 | 56
    | 59 | 57 | 59; "Gain on disposition (1)" (6) | — | (723) | (893) | —; income tax (96) | 7 |
    283 | 204 | (103); ANI 2,797 | 3,788 | 2,976 | 1,591 | 949. Per diluted share: 9.25 | 14.37 |
    13.95 | 7.76 | 2.11; 1.54 | (0.28) | (0.95) | 0.54 | 1.30; 0.07 | (0.02) | (0.40) | — | 0.29;
    0.18 | 0.21 | 0.22 | 0.21 | 0.22; (0.02) | — | (2.71) | (3.33) | —; (0.37) | 0.03 | 1.06 | 0.76
    | (0.39); ANI 10.65 | 14.31 | 11.17 | 5.94 | 3.53. Footnote (1) on "Gain on disposition":
    "Includes changes in the value of contingent consideration related to the sale of Allstate
    Life Insurance Company and certain affiliates in 2021 that are included within operating
    costs and expenses on the Condensed Consolidated Statements of Operations."
  - S3 L17 Book Value per Common Share and Debt to Capital (as of March 31, 2026 | Dec. 31, 2025 |
    Sept. 30, 2025 | June 30, 2025 | March 31, 2025): numerator Allstate common shareholders'
    equity (1) 29,606 | 28,609 | 25,504 | 22,018 | 20,054; denominator "Common shares outstanding
    and dilutive potential common shares outstanding (2)" 260.8 | 263.8 | 265.8 | 267.2 | 268.8;
    BVPS $113.52 | $108.45 | $95.95 | $82.40 | $74.61; less unrealized net capital gains and losses
    on fixed income securities (220) | 303 | 357 | 40 | (351); adjusted equity 29,826 | 28,306 |
    25,147 | 21,978 | 20,405; BVPS excluding unrealized on fixed income* $114.36 | $107.30 |
    $94.61 | $82.25 | $75.91; Total debt 7,491 | 7,490 | 8,089 | 8,087 | 8,086; Total capital
    resources 39,098 | 38,100 | 35,594 | 32,106 | 30,141; debt to Allstate shareholders' equity
    23.7 % | 24.5 % | 29.4 % | 33.7 % | 36.7 %; debt to capital resources 19.2 % | 19.7 % | 22.7 %
    | 25.2 % | 26.8 %. Footnotes: (1) "Excludes equity related to preferred stock of $2,001
    million for all periods shown." (2) "Common shares outstanding were 257,804,210 and
    260,135,910 as of March 31, 2026 and December 31, 2025, respectively."
  - S4 L19 ROE, "As of or for the twelve months ended" the five dates: NI 12,027 | 10,165 | 8,261 |
    5,705 | 3,927; beginning equity 20,054 | 19,441 | 18,876 | 16,592 | 16,638; ending (1) 29,606 |
    28,609 | 25,504 | 22,018 | 20,054; average 24,830 | 24,025 | 22,190 | 19,305 | 18,346; ROE
    48.4 % | 42.3 % | 37.2 % | 29.6 % | 21.4 %; ANI 11,152 | 9,304 | 7,578 | 5,650 | 4,488; less
    unrealized at beginning (351) | (771) | 361 | (938) | (819); adjusted beginning 20,405 | 20,212
    | 18,515 | 17,530 | 17,457; less unrealized at end (221) | 297 | 351 | 36 | (351); adjusted
    ending 29,827 | 28,312 | 25,153 | 21,982 | 20,405; average adjusted 25,116 | 24,262 | 21,834 |
    19,756 | 18,931; ANI ROE 44.4 % | 38.3 % | 34.7 % | 28.6 % | 23.7 %. Footnote (1) preferred
    $2,001 million.
  - S5 L21 Policies in Force (thousands) (1), as of the five dates: Allstate Protection auto
    25,758 | 25,504 | 25,332 | 25,243 | 25,100; homeowners 7,739 | 7,697 | 7,642 | 7,596 | 7,549;
    other personal lines 4,902 | 4,898 | 4,908 | 4,885 | 4,874; commercial lines 177 | 176 | 174 |
    176 | 189; total 38,576 | 38,275 | 38,056 | 37,900 | 37,712. Protection Services: Protection
    Plans 165,210 | 164,650 | 163,451 | 162,315 | 161,503; Roadside 1,379 | 1,244 | 1,119 | 988 |
    867; Dealer Services 3,628 | 3,663 | 3,681 | 3,697 | 3,690; Identity Protection 2,752 | 2,626
    | 2,694 | 2,669 | 2,648; total 172,969 | 172,183 | 170,945 | 169,669 | 168,708. All other 507 |
    479 | 480 | 482 | 478. Total policies in force (2) 212,052 | 210,937 | 209,481 | 208,051 |
    206,898. Footnote (1): counts "based on items rather than customers" (multi-car = multiple
    items; lender-placed policies excluded; Protection Plans = active consumer product
    protection plans; Roadside = memberships, not wholesale partners; Dealer Services = service
    contracts etc., not TPAs; Identity Protection = individual customer counts; All other =
    certificate counts for the individual health business). Footnote (2): "Historical totals
    exclude employer voluntary benefits and group health businesses that have been divested."
  - S6 L23 Property-Liability Results: PW 14,625 | 14,572 | 15,630 | 15,047 | 14,297; PE 14,802 |
    14,776 | 14,533 | 14,346 | 14,027; other revenue 544 | 541 | 518 | 504 | 488; claims (8,992) |
    (7,567) | (8,466) | (10,084) | (10,660); DAC (1,821) | (1,772) | (1,757) | (1,742) | (1,732);
    operating costs (1,835) | (1,917) | (1,873) | (1,685) | (1,701); restructuring (1) | (10) |
    (15) | (13) | (16); amortization (39) | (45) | (46) | (46) | (46); Underwriting income (loss)
    (1) 2,658 | 4,006 | 2,894 | 1,280 | 360; catastrophe losses (1,240) | (209) | (558) | (1,990) |
    (2,202); claims expense excluding catastrophe expense (783) | (755) | (765) | (751) | (734);
    loss ratio 60.7 | 51.2 | 58.3 | 70.3 | 76.0; cat effect (8.4) | (1.4) | (3.8) | (13.9) |
    (15.7); PYD excl. cats 6.9 | 5.4 | 2.7 | 2.6 | 1.7; underlying loss ratio* 59.2 | 55.2 | 57.2 |
    59.0 | 62.0; expense ratio 21.3 | 21.7 | 21.8 | 20.8 | 21.4; amortization effect (0.2) | (0.3)
    x4; underlying expense ratio* 21.1 | 21.4 | 21.5 | 20.5 | 21.1; advertising effect (3.7) |
    (3.8) | (4.0) | (3.1) | (3.7); restructuring effect — | (0.1) x4; adjusted underwriting expense
    ratio* 17.4 | 17.5 | 17.4 | 17.3 | 17.3; claims expense ratio excl. cat expense 5.3 | 5.1 | 5.3
    | 5.2 | 5.2; adjusted expense ratio* 22.7 | 22.6 | 22.7 | 22.5 | 22.5; Combined ratio 82.0 |
    72.9 | 80.1 | 91.1 | 97.4; underlying CR* 80.3 | 76.6 | 78.7 | 79.5 | 83.1; "Effect of Run-off
    Property-Liability on combined ratio" — | — | 1.0 | — | —. Footnote (1) underwriting income:
    Allstate Protection 2,659 | 4,007 | 3,040 | 1,283 | 364; Run-off Property-Liability (1) | (1) |
    (146) | (3) | (4); Property-Liability 2,658 | 4,006 | 2,894 | 1,280 | 360. Other: NII 845 | 814
    | 873 | 687 | 783; income tax on operations (744) | (1,074) | (790) | (402) | (227); NCI 1 | (5)
    | (1) | (10) | 1.
  - S7 L25 Allstate Protection Profitability Measures: PW auto 9,850 | 9,399 | 9,869 | 9,533 |
    9,848; homeowners 3,741 | 4,110 | 4,607 | 4,395 | 3,453; other personal lines 768 | 784 | 887
    | 865 | 729; commercial 112 | 107 | 101 | 100 | 94; other business lines 154 | 172 | 166 | 154
    | 173; total 14,625 | 14,572 | 15,630 | 15,047 | 14,297. PE auto 9,547 | 9,622 | 9,593 | 9,528 |
    9,347; homeowners 4,164 | 4,055 | 3,880 | 3,771 | 3,657; OPL 820 | 814 | 800 | 779 | 741;
    commercial 101 | 103 | 99 | 104 | 113; other business 170 | 182 | 161 | 164 | 169; total 14,802
    | 14,776 | 14,533 | 14,346 | 14,027. UW income auto 1,729 | 1,851 | 1,726 | 1,331 | 816;
    homeowners 685 | 1,813 | 1,107 | (76) | (451); OPL 157 | 205 | 61 | (11) | (65); commercial
    21 | 45 | 93 | (17) | 16; other business 64 | 92 | 52 | 54 | 41; Answer Financial 3 | 1 | 1 | 2
    | 7; total 2,659 | 4,007 | 3,040 | 1,283 | 364. Claims expense excl. cat 783 | 755 | 741 | 750
    | 731. Ratios: loss 60.7 | 51.2 | 57.3 | 70.3 | 76.0; PYD 6.9 | 5.4 | 3.7 | 2.6 | 1.7;
    underlying loss 59.2 | 55.2 | 57.2 | 59.0 | 62.0; expense 21.3 | 21.7 | 21.8 | 20.8 | 21.4;
    adjusted UW expense 17.4 | 17.5 | 17.4 | 17.3 | 17.3; Combined ratio 82.0 | 72.9 | 79.1 |
    91.1 | 97.4; underlying CR 80.3 | 76.6 | 78.7 | 79.5 | 83.1; claims expense ratio excl. cat 5.3
    | 5.1 | 5.1 | 5.2 | 5.2. (Q3 2025 differs from S6: loss 57.3 vs 58.3, PYD 3.7 vs 2.7, CR 79.1
    vs 80.1, claims expense 741 vs 765, ratio 5.1 vs 5.3.)
  - S8 L27 Impact of Net Rate Changes Implemented on Premiums Written (four quarters; columns
    Number of locations (1) | Total (%) (2)(3) | Location specific (%) (4)): Q1 2026 auto 39 | — |
    —, homeowners (5) 18 | 1.4 | 7.2; Q4 2025 auto 34 | 0.2 | 1.8, homeowners 15 | 0.8 | 5.4; Q3
    2025 auto 46 | 0.6 | 2.4, homeowners 21 | 1.4 | 12.0; Q2 2025 auto 38 | 0.4 | 2.2, homeowners
    25 | 1.4 | 8.0. Footnotes: (1) locations = "U.S. states, the District of Columbia or Canadian
    provinces"; "In the first quarter of 2026, the combined impact of rate changes for auto netted
    to zero across brands." (2) % of total prior year-end premiums written. (3) "Implemented auto
    insurance rate decreases totaled $2 million in the first quarter of 2026, after implementing
    rate increases of $81 million, $232 million and $126 million in the fourth, third and second
    quarters of 2025, respectively." (4) % of prior year-end premiums written in those same
    locations. (5) homeowners "Excludes the impact to average premium from inflation in insured
    home replacement costs and other aging factor adjustments, which could be significant."
  - S9 L29 Auto Profitability Measures and Statistics: PW/PE/UW income as S7 auto; loss ratio
    60.6 | 58.9 | 60.6 | 65.0 | 69.3; cat (0.9) | (0.4) | (0.7) | (2.2) | (2.2); PYD 8.8 | 7.5 |
    5.0 | 4.3 | 2.5; underlying loss 68.5 | 66.0 | 64.9 | 67.1 | 69.6; expense 21.3 | 21.9 | 21.4 |
    21.0 | 22.0; amortization (0.3) x4 | (0.4); underlying expense 21.0 | 21.6 | 21.1 | 20.7 | 21.6;
    CR 81.9 | 80.8 | 82.0 | 86.0 | 91.3; underlying CR 89.5 | 87.6 | 86.0 | 87.8 | 91.2; annualized
    average earned premium ($) 1,483 | 1,509 | 1,515 | 1,510 | 1,490; average underlying loss
    (incurred pure premium) ($) 1,016 | 996 | 983 | 1,013 | 1,037, % change YoY (2.0) | (4.0) |
    (4.7) | (2.9) | (0.6); with expense ($) 1,327 | 1,322 | 1,303 | 1,326 | 1,359; new issued
    applications (thousands) exclusive agency 807 | 794 | 823 | 764 | 748, independent agency 742 |
    719 | 696 | 685 | 686, direct 848 | 713 | 809 | 708 | 757, total 2,397 | 2,226 | 2,328 | 2,157 |
    2,191; Allstate brand average premium gross written ($) 832 | 844 | 853 | 850 | 853.
  - S10 L31 Homeowners Profitability Measures and Statistics: PW/PE/UW as S7 homeowners; loss
    ratio 61.5 | 33.2 | 48.5 | 81.2 | 91.8; cat (25.1) | (4.2) | (12.3) | (42.8) | (49.9); PYD 2.3 |
    0.6 | 1.0 | (0.3) | 0.2; underlying loss 38.7 | 29.6 | 37.2 | 38.1 | 42.1; expense 22.0 | 22.1 |
    23.0 | 20.8 | 20.5; amortization (0.2) | (0.3) | (0.4) | (0.3) | (0.2); underlying expense
    21.8 | 21.8 | 22.6 | 20.5 | 20.3; CR 83.5 | 55.3 | 71.5 | 102.0 | 112.3; underlying CR 60.5 |
    51.4 | 59.8 | 58.6 | 62.4; new issued applications exclusive 241 | 237 | 262 | 251 | 232,
    independent 36 | 36 | 41 | 48 | 47, direct 81 | 69 | 69 | 54 | 41, total 358 | 342 | 372 | 353 |
    320; Allstate brand average premium gross written ($) 2,360 | 2,267 | 2,296 | 2,267 | 2,210.
  - S11 L33 Protection Services Segment Results: NPW 727 | 867 | 749 | 733 | 657; PE 751 | 735 |
    720 | 695 | 671; other revenue 117 | 126 | 124 | 111 | 128; intersegment premiums and service
    fees 31 | 31 | 33 | 36 | 37; NII 23 | 25 | 25 | 25 | 24; claims (199) | (175) | (193) | (170) |
    (161); DAC (348) | (345) | (337) | (328) | (318); non-deferrable commissions (126) | (120) |
    (117) | (109) | (101); operating costs (183) | (204) | (193) | (181) | (208); restructuring (4)
    | (2) | (1) | (1) | —; tax (15) | (14) | (16) | (18) | (17); NCI — | — | (1) | — | —; ANI (1)
    47 | 57 | 46 | 60 | 55; depreciation 4 | 4 | 5 | 5 | 5; adjusted earnings before taxes,
    depreciation and restructuring* 70 | 77 | 68 | 84 | 77. Protection Plans NPW 554 | 693 | 567 |
    558 | 487; PE 578 | 566 | 552 | 531 | 510; revenue 613 | 609 | 588 | 563 | 540; ANI 41 | 49 |
    34 | 51 | 45. Roadside revenue 63 | 61 | 59 | 56 | 55, ANI 12 | 12 | 12 | 11 | 11. Dealer
    Services revenue 148 | 148 | 148 | 148 | 146, ANI 5 | 7 | 6 | 4 | 4. Identity Protection revenue
    40 | 39 | 39 | 41 | 40, ANI 1 | 1 | 2 | 2 | 1. Arity revenue 58 | 60 | 68 | 59 | 79, adjusted net
    loss (12) | (12) | (8) | (8) | (6). Footnote (1) "Adjusted net income is the GAAP segment
    measure."
  - S12 L35 Corporate Segment Results: other revenue 17 | 19 | 24 | 23 | 15; NII 68 | 52 | 49 | 37
    | 22; operating costs (33) | (41) | (42) | (45) | (32); restructuring — | (1) | — | — | —;
    interest (98) | (98) | (101) | (100) | (100); tax benefit 16 | 14 | 12 | 21 | 27; preferred
    dividends (29) | (29) | (29) | (30) | (29); adjusted net loss (59) | (84) | (87) | (94) | (97).
  - S13 L37 Investment Position and Results ("As of or for the three months ended"): position
    fixed income 59,060 | 59,115 | 57,186 | 54,435 | 51,993; equity 10,431 | 8,398 | 5,338 | 2,397
    | 4,465; mortgage loans 868 | 879 | 831 | 807 | 770; LP 8,946 | 8,844 | 9,213 | 9,194 | 9,380;
    short-term 4,705 | 4,887 | 8,743 | 9,640 | 6,541; other 1,150 | 1,114 | 1,017 | 964 | 901;
    total 85,160 | 83,237 | 82,328 | 77,437 | 74,050. NII by asset: fixed income 666 | 665 | 634 |
    602 | 608; equity 41 | 43 | 19 | 17 | 20; mortgage 12 | 11 | 11 | 9 | 10; LP 206 | 140 | 226 | 74
    | 194; short-term 59 | 72 | 104 | 97 | 72; other 26 | 48 | 26 | 24 | 21; before expense 1,010 |
    979 | 1,020 | 823 | 925; investment expense (72) | (87) | (71) | (69) | (71); NII 938 | 892 |
    949 | 754 | 854. Fixed income pre-tax yield (1) 4.5 % | 4.6 % | 4.6 % | 4.4 % | 4.4 %. Net gains
    by type: sales (4) | 60 | 69 | (245) | (137); credit losses (7) | (7) | (23) | (4) | (76);
    valuation change of equity investments (388) | 18 | 200 | 170 | (117); derivatives (6) | 2 |
    6 | (65) | (19); total (405) | 73 | 252 | (144) | (349). Total return (1): NII 1.1 % | 1.1 % |
    1.2 % | 1.0 % | 1.2 %; valuation-interest bearing (0.8) | — | 0.6 | 0.2 | 0.4; valuation-equity
    (0.5) | — | 0.2 | 0.2 | (0.2); total (0.2) % | 1.1 % | 2.0 % | 1.4 % | 1.4 %. Duration (years)
    (1): fixed income 5.5 | 5.1 | 5.1 | 4.1 | 5.1; fixed income including interest rate derivative
    positions 5.7 | 5.1 | 5.0 | 4.0 | 5.1; fixed income and short-term including derivatives 5.3 |
    4.7 | 4.3 | 3.4 | 4.6. Footnotes: (1) "Beginning in the third quarter of 2024 and through 2025,
    calculations include investments held for sale." (2) "Includes (0.1%) impact related to
    losses recorded for variable interest in Reciprocal Exchanges." (marker "(2)" sits after the
    last value of the valuation-interest bearing row in the flattened text; exact cell
    unresolved).
  - S14 L39 Investment Position and Results by Strategy: market-based interest-bearing 65,014 |
    65,236 | 66,973 | 65,060 | 59,411; equity 10,052 | 8,009 | 4,762 | 1,786 | 3,795; LP and other
    alternative 183 | 146 | 232 | 211 | 281; total 75,249 | 73,391 | 71,967 | 67,057 | 63,487.
    Performance-based private equity 7,633 | 7,658 | 8,134 | 8,208 | 8,393; real estate 2,278 |
    2,188 | 2,227 | 2,172 | 2,170; total 9,911 | 9,846 | 10,361 | 10,380 | 10,563. Market-based
    income interest-bearing 748 | 758 | 759 | 716 | 698; equity 39 | 43 | 19 | 16 | 18; LP and other
    (1) 4 | 3 | 2 | 1 | 3; income for yield 791 | 804 | 780 | 733 | 719; pre-tax yield (2) 4.3 % |
    4.5 % | 4.5 % | 4.4 % | 4.4 %. Performance-based private equity 111 | 123 | 197 | 74 | 103; real
    estate 108 | 52 | 43 | 16 | 103; before expense 219 | 175 | 240 | 90 | 206; investee level
    expenses (12) | (29) | (13) | (11) | (10); income for yield 207 | 146 | 227 | 79 | 196; pre-tax
    yield 8.4 % | 5.9 % | 8.9 % | 3.0 % | 7.5 %. Total return market-based (2) (0.4) % | 1.2 % |
    2.0 % | 1.6 % | 1.5 %; "(3)" then performance-based 1.9 | 0.9 | 2.5 | 1.0 | 1.6. IRR
    performance-based: 10 year 11.1 % | 11.1 % | 10.9 % | 11.0 % | 11.2 %; 5 year 11.2 | 13.1 | 14.3
    | 14.4 | 12.2; 3 year 5.9 | 5.6 | 5.7 | 4.7 | 5.4; 1 year 7.6 | 5.8 | 7.1 | 5.0 | 4.5. Footnotes
    (1) net of investee level expenses; (2) held-for-sale inclusion Q3 2024-2025; (3) Reciprocal
    Exchanges (0.1%) (marker position between the market-based values and the performance-based
    label; exact cell unresolved).
- Lists: contents L11 (17 schedules); S5 footnote (1) seven bullet scope rules; ANI exclusions
  (S15, same as D01); S8 footnote (3) auto rate-change dollars for four quarters.
- Forecasts, guidance, deadlines, effective dates: none. L9 "results of operations for interim
  periods should not be considered indicative of results to be expected for the full year."
- Hedged claims: S8 footnote (5) "which could be significant"; S17 IRR "can vary significantly".
- Rounded prose beside exact figures: none (tables only); D01 prose values reconcile to D03
  rows (see Shared ground).
- Notes: S1 "Gain (loss) on disposition of operations" (statement line) — | (7) | 720 | 890 | —
  vs S2 "Gain on disposition (1)" (6) | — | (723) | (893) | — (footnote: contingent consideration
  in operating costs). S3 BVPS denominator 260.8 million (dilutive basis) vs D01 highlight
  "Common shares outstanding (in millions) 257.8" and S3 footnote (2) 257,804,210. S3 "less
  unrealized ... on fixed income securities" (220) vs S4 "less unrealized net capital gains and
  losses" (221) at March 31, 2026 (40 vs 36 at June 30, 2025). Debt fell from 8,089 (Sept. 30,
  2025) to 7,490 (Dec. 31, 2025) (S3).
- Operative definitions, rules and scope exceptions (S15 L41, S16 L43, S17 L45):
  - Underlying loss ratio: "computed as the difference between three GAAP operating ratios: the
    loss ratio, the effect of catastrophes on the combined ratio, and the effect of prior year
    reserve reestimates, excluding catastrophes on the combined ratio." (S15)
  - Underlying expense ratio: expense ratio minus the effect of amortization or impairment of
    purchased intangibles (S15).
  - Average underlying loss (incurred pure premium) and with expense: "calculated as the
    underlying loss ratio and the underlying combined ratio ... respectively, multiplied by the
    annualized GAAP earned premium" (S15).
  - Adjusted underwriting expense ratio: expense ratio minus effects of "advertising expense,
    restructuring and related charges and amortization or impairment of purchased intangibles";
    adjusted expense ratio = adjusted underwriting expense ratio plus claims expense ratio
    excluding catastrophe expense (S16).
  - Underlying combined ratio (supplement wording): "the sum of the underlying loss and
    underlying expense ratios" (S16; release wording D01 L442 is "difference between four GAAP
    operating ratios").
  - Protection Services adjusted earnings before taxes, depreciation and restructuring: "adjusted
    net income (loss), excluding taxes, depreciation and restructuring" (S16).
  - ANI ROE (S16) same calculation as D01 L392; the long-term goal sentence of the releases is
    absent in S16.
  - BVPS excluding unrealized on fixed income: "dividing Allstate common shareholders' equity
    after excluding the impact of unrealized net capital gains and losses on fixed income
    securities by total common shares outstanding plus dilutive potential common shares
    outstanding" (S16); GAAP BVPS denominator per S3 row label "Common shares outstanding and
    dilutive potential common shares outstanding".
  - Glossary S17: A&H premiums "include premiums for individual health, employer voluntary
    benefits through March 31, 2025 and group health through June 30, 2025"; ANI "is the GAAP
    segment measure used for the Protection Services and Corporate segments"; average equity
    "two-point average"; P&C insurance premiums "reported in the Allstate Protection and
    Protection Services segments"; annualized average earned premium "annualizing net earned
    premium reported in the quarter and year-to-date divided by policies in force at quarter
    end"; average premium gross written = gross premiums written / issued item count (policy
    term "generally 6 months for auto and 12 months for homeowners"); claims expense ratio
    excluding catastrophe expense = incurred LAE net of reinsurance excluding catastrophe
    expenses, "embedded within the loss ratio"; "Expense ratio: Other revenue is deducted from
    other costs and expenses"; new issued applications = item counts "regardless of whether the
    customer was previously insured by another Allstate Protection brand"; other business lines
    = Ivantage, non-proprietary life and annuity, lender-placed; Protection Services revenue =
    premiums earned + other revenue + intersegment premiums and fees + NII; LP income "generally
    recognized on a three-month delay"; quarterly and year-to-date pre-tax yield methods; total
    return method.
  - Contents note L11: "starting in the third quarter of 2025, the Allstate Health and Benefits
    segment is no longer a reportable segment."
- Amendments or contradictions: none stated. Same-quarter differences between S6 (Property-
  Liability) and S7 (Allstate Protection) arise in Q3 2025 from Run-off (S6 footnote (1)).
- Coverage: FULL. Ledger: L1-48 read in one pass (each page line displayed to its "Supplement N"
  footer, so no line truncation); remaining none. Spot-check vs `docs/`: 17 lines carry
  "Supplement N" footers in the original (grep count 17, including the S3 line holding footnote
  "(2) Common shares outstanding were 257,804,210 and 260,135,910 ...").

## D04 - Chubb first quarter 2026 earnings release (Exhibit 99.1)

- Source: `docs/cb_ex991_2026-04-21.txt` -> `text/D04.txt` (1,146 lines); platform Doc 4
  (cb_ex991_2026-04-21). Pages: not applicable; printed page numbers 1-11 at L77, L209, L376,
  L642, L670, L693, L711, L727, L747, L931, L1143.
- Written or submitted by: Chubb Limited (NYSE: CB), Bärengasse 32, CH-8001 Zurich, Switzerland
  (L11-17). Quoted: Evan G. Greenberg, Chairman and Chief Executive Officer (L203-216).
  Investor Contact Susan Spivak (L686).
- Type, date, edition: News Release, "ZURICH – April 21, 2026" (L81); html d145408dex991.htm
  (L4). Earnings call Wednesday, April 22, 2026, 8:30 a.m. Eastern (L678). Refers to a "Chubb
  Limited Financial Supplement, dated March 31, 2026" (L676) and to non-GAAP reconciliations "on
  pages 25-29 in the Financial Supplement" (L736-737) — that supplement is not in the bundle.
- Period covered: "quarter ended March 31, 2026" (Q1 2026 vs Q1 2025); ROE measures
  "Annualized"; balance sheet March 31, 2026 vs December 31, 2025; BVPS growth stated "from
  March 31, 2025" (L81) while the balance sheet compares with December 31, 2025. "All comparisons
  are with the same period last year unless otherwise specifically stated." (L674).
- Entities and aliases: Chubb / Chubb Limited / CB; segments North America Commercial P&C
  Insurance, North America Personal P&C Insurance, North America Agricultural Insurance (together
  "Total North America P&C Insurance", L407-409), Overseas General Insurance, Global Reinsurance,
  Life Insurance (International Life; Chubb Benefits / "North America Chubb Benefits"; Life
  reinsurance), Corporate (L715). Aggregates "P&C" and "Global P&C (excludes Agriculture)".
  Sub-line "Major accounts retail and excess and surplus (E&S) wholesale" (table L449) is called
  "Major accounts retail and specialty" in prose (L648). Huatai asset management companies
  (L733). "Bermuda law" (L157) / "Bermuda Economic Transition Adjustment" (L715).
- Tables (US$ millions; one value per line after each label; "$" in separate pipe cells):
  - p.2 First Quarter Summary L84-201, cols 2026 | 2025 | Change, then "(Per Share)" 2026 | 2025
    | Change: Net income $2,320 | $1,331 | 74.3% | $5.88 | $3.29 | 78.8%; Adjusted net realized
    (gains) losses and other, net of tax 343 | 59 | NM | 0.87 | 0.15 | NM; Integration expenses
    and severance, net of tax 7 | - | NM | 0.02 | - | NM; Market risk benefits (gains) losses, net
    of tax (12) | 78 | NM | (0.03) | 0.19 | NM; Amortization of deferred tax asset from Bermuda law
    31 | 21 | 47.6% | 0.08 | 0.05 | 60.0%; Core operating income, net of tax $2,689 | $1,489 |
    80.6% | $6.82 | $3.68 | 85.2%; Annualized ROE 12.6% | 8.2%; Core operating ROTE 20.6% |
    13.0%; Core operating ROE 14.0% | 8.6%.
  - p.3 Operating highlights L218-372 (Q1 2026 | Q1 2025 | Change): Consolidated NPW "(increase
    of 7.7% in constant dollars)" 14,005 | 12,646 | 10.7%. P&C NPW "(increase of 4.1% in constant
    dollars)" 11,716 | 10,926 | 7.2%; underwriting income 1,792 | 441 | 306.3%; combined ratio
    84.0% | 95.7%; CAY underwriting income excl. cat 2,006 | 1,827 | 9.8%; CAY combined ratio
    excl. cat 82.1% | 82.3%. Global P&C (excludes Agriculture) NPW "(3.9% cc)" 11,405 | 10,650 |
    7.1%; UW income 1,674 | 387 | 332.0%; CR 84.8% | 96.2%; CAY UW excl. cat 1,964 | 1,791 | 9.5%;
    CAY CR excl. cat 82.2% | 82.4%. Life Insurance NPW "(30.8% cc)" 2,289 | 1,720 | 33.1%; Segment
    income "(7.1% cc)" 316 | 291 | 8.5%.
  - p.4 Key segment items L391-637: Total North America P&C NPW 6,887 | 6,615 | 4.1%; CR 82.8% |
    99.8%; CAY excl. cat 79.1% | 79.7%. NA Commercial P&C NPW 4,895 | 4,787 | 2.3%; Major accounts
    retail and E&S wholesale 2,772 | 2,731 | 1.5%; Middle market and small commercial 2,123 |
    2,056 | 3.3%; CR 84.0% | 82.1%; CAY excl. cat 81.8% | 81.3%. NA Personal P&C NPW 1,681 |
    1,552 | 8.3%; CR 84.0% | 159.5%; CAY excl. cat 71.3% | 75.0%. NA Agricultural NPW 311 | 276 |
    12.7%; CR 37.5% | 67.5%; CAY excl. cat 77.6% | 78.9%. Overseas General NPW "(6.1% cc)" 4,466 |
    3,903 | 14.4%; Commercial P&C "(3.1% cc)" 2,695 | 2,432 | 10.8%; Consumer P&C "(11.1% cc)"
    1,771 | 1,471 | 20.5%; CR 83.6% | 83.4%; CAY excl. cat 85.4% | 85.5%. Global Reinsurance NPW
    "(decrease of 11.7% in constant dollars)" 363 | 408 | (11.2)%; CR 76.0% | 95.6%; CAY excl. cat
    73.7% | 74.3%. Life (repeat) NPW 2,289 | 1,720 | 33.1%; segment income 316 | 291 | 8.5%.
    Consistency: NA + Overseas General + Global Reinsurance NPW = 11,716 (P&C); P&C minus Global
    P&C NPW = 311 = NA Agricultural NPW.
  - p.10 Summary Consolidated Balance Sheets L751-927 (March 31, 2026 | December 31, 2025):
    Investments 170,195 | 168,720; Cash and restricted cash 2,634 | 2,470; Insurance and
    reinsurance balances receivable 17,101 | 15,944; Reinsurance recoverable on losses and loss
    expenses 20,159 | 20,338; Goodwill and other intangible assets 26,587 | 26,448 ("$25,966 and
    $25,775 represents Chubb portion as of 3/31/2026 and 12/31/2025", L795); Other assets 38,780 |
    38,407; Total assets 275,456 | 272,327; Unpaid losses and loss expenses 88,915 | 88,018;
    Unearned premiums 27,180 | 26,279; Other liabilities 79,449 | 78,251; Total liabilities
    195,544 | 192,548; Chubb shareholders' equity, excl. AOCI 79,699 | 78,732; AOCI (5,911) |
    (4,975); Chubb shareholders' equity 73,788 | 73,757; Noncontrolling interests 6,124 | 6,022;
    Total shareholders' equity 79,912 | 79,779; Book value per common share $189.93 | $188.59;
    Tangible BVPS $126.65 | $126.22; BVPS excl. AOCI $205.15 | $201.31; TBVPS excl. AOCI $140.35 |
    $136.91. No "Total invested assets" row (first appears in D05); shares outstanding not
    printed.
  - p.11 Summary Consolidated Financial Data L935-1139 (Three Months Ended March 31, 2026 |
    2025): Gross premiums written 16,551 | 15,105; NPW 14,005 | 12,646; Net premiums earned
    13,457 | 12,000; Losses and loss expenses 6,131 | 6,896; Policy benefits 1,785 | 1,227; Policy
    acquisition costs 2,596 | 2,313; Administrative expenses 1,149 | 1,080; Net investment income
    1,709 | 1,561; Net realized gains (losses) (407) | (116); Market risk benefits gains (losses)
    14 | (92); Interest expense 198 | 181; Other income (expense): separate account assets (12) |
    (10), Other 173 | 93; Amortization of purchased intangibles 73 | 75; Integration expenses and
    severance 9 | --; Income tax expense 646 | 321; Net income 2,347 | 1,343; Less NCI income 27 |
    12; Chubb net income 2,320 | 1,331; Diluted EPS: Chubb net income $5.88 | $3.29, core operating
    income $6.82 | $3.68; Weighted average shares outstanding 394.6 | 404.7; P&C ratios: loss and
    loss expense 55.6% | 67.8%, policy acquisition cost 20.0% | 19.4%, administrative expense 8.4%
    | 8.5%, P&C combined ratio 84.0% | 95.7%; P&C underwriting income 1,792 | 441.
- Lists: headline bullets L35-73 (ten); regional growth L49 (Latin America 17.8%, Europe 15.8%,
  Asia 12.1%); core operating income exclusions L715 (adjusted net realized gains (losses) and
  other, market risk benefits gains (losses), fair value amortization on acquired invested
  assets and debt, integration expenses and severance, Bermuda deferred tax asset amortization).
- Forecasts, guidance, deadlines, effective dates: Greenberg L216 "from what I see I remain
  confident in our ability to continue generating strong growth in operating earnings, and
  double-digit growth in EPS and tangible book value." Market view L213 "soft or softening";
  L216 "War in the Middle East raises the specter globally of higher inflation and slower
  economic growth". Forward-looking statement L740-742.
- Hedged claims: L216 "remain confident" (attaches to future earnings/EPS/TBV growth); L699
  measures "may be defined differently by other companies".
- Rounded prose beside exact figures: NI "$2.32 billion", core "$2.69 billion" (L37, L81) vs
  2,320 / 2,689; core "$2.7 billion ... both up more than 80%" (L204); NPW "$14.0 Billion"
  (headline L29) and "$14 billion" (L214) vs 14,005; P&C NPW "$11.72 billion" (L41) vs 11,716; P&C
  UW income "$1.79 billion" (L53) and "$1.8 billion, with a combined ratio of 84%" (L205) vs
  1,792 / 84.0%; CAY UW "$2.01 billion" (L53) vs 2,006; Life NPW "$2.29 billion" (L65, L664) vs
  2,289; NII "$1.71 billion, up 9.5%", adjusted NII "$1.84 billion, up 10.1%" (L69) and "$1.8
  billion was up more than 10%" (L205); "21% growth in our global consumer businesses, both P&C
  and Life" (L214); "Excluding CATs, core operating income was up 10.7% and EPS was up 13.5%"
  (L204; no ex-CAT table). Ex-large-account-property growth figures appear with different
  scopes: L45 "2.8% in commercial insurance, or 7.7% excluding large account property, both
  admitted and E&S"; L214 "Excluding large account property, admitted and E&S, North America
  grew 7.8%"; L648 NA Commercial "increased 2.3%, or 7.3% excluding large account property, both
  admitted and E&S" and major accounts "up 1.5%, or 10.9% excluding large account property, which
  was down 55.0%". The bullet's 2.8% "commercial insurance" is not the NA Commercial P&C table
  figure (2.3%, L447); D04 does not define the bullet's scope.
- Notes: catastrophe losses "$500 million compared with $1.64 billion last year, which included
  $1.47 billion from the California wildfires" (L57); favorable PPD "$286 million compared with
  $255 million" (L61); book value "unfavorably impacted by after-tax net realized and unrealized
  losses of $1.94 billion ... partially offset by $346 million of foreign currency gains" (L81);
  BVPS/TBVPS +15.8%/+21.5% and excl. AOCI +12.1%/+16.5% from March 31, 2025 (L81); capital L390
  "Total capital returned to shareholders was $1.52 billion, comprising share repurchases of
  $1.14 billion at an average purchase price of $325.06 per share and dividends of $380 million"
  (no authorization, remaining capacity or dividend dates); operating cash flow $3.95 billion,
  adjusted $3.80 billion (L386); NPE +12.1% (9.5% cc), P&C NPE +8.6% (5.9% cc) (L382); L214
  exposure reduction "by non-renewing a substantial percentage of our shared and layered
  property business that was up for renewal while purchasing additional reinsurance"; segment
  commentary L648-665 (NA Commercial financial lines down 5.7% "impacted by the increased use of
  reinsurance", CAY CR excl. cat +0.5 pts "primarily due to the reduction in property business";
  NA Personal CAY excl. cat −3.7 pts (loss −2.7, expense −1.0); NA Agricultural CR −30.0 pts
  (−22.2 from higher favorable PPD, −6.5 from lower cats); Overseas General CAY excl. cat −0.1
  (loss −0.5, expense +0.4, mix); Life: International Life "$1.94 billion, up 36.8%, or 15.7%
  excluding savings-oriented single premium business", Chubb Benefits +15.8%, segment income
  +8.5% "partially offset by non-recurring items that were favorable to the prior year within the
  North America Chubb Benefits and Life reinsurance businesses"); L679 acquisitions "reported at
  100%" except core operating income, net income, book value, TBV, ROE and per-share data (Chubb
  ownership only); 54 countries and territories, approximately 45,000 people (L682). Printed
  value 84.0% occurs for P&C CR (L276), NA Commercial CR (L475) and NA Personal CR (L501).
- Operative definitions, rules and scope exceptions (L697-737):
  - Constant dollars (L700): "translating prior period results using the same local currency
    exchange rates as the comparable current period".
  - Adjusted net investment income (L701): NII "excluding the amortization of the fair value
    adjustment on acquired invested assets from certain acquisitions of $2 million and $2 million
    in Q1 2026 and Q1 2025, and including investment income of $127 million and $107 million in
    Q1 2026 and Q1 2025, from partially owned investment companies (private equity partnerships)
    where our ownership interest is in excess of 3% that are accounted for under the equity
    method."
  - Adjusted net realized gains (losses) and other (L702): excludes crop derivatives (reclassified
    to adjusted losses) and participating-policy investment gains (to adjusted policy benefits).
  - P&C underwriting income (L704): "excludes the Life Insurance segment and is calculated by
    subtracting adjusted losses and loss expenses, adjusted policy benefits, policy acquisition
    costs and administrative expenses from net premiums earned."
  - P&C CAY underwriting income excl. cat (L705-706): "P&C underwriting income adjusted to exclude
    P&C catastrophe losses and prior period development (PPD)"; "References in this release to
    'current accident year' or 'underlying' metrics exclude catastrophe losses and prior period
    development, unless stated otherwise."
  - Core operating income (L715): excludes after-tax adjusted net realized gains (losses) and
    other, MRB gains (losses), fair value amortization, integration expenses and severance, and
    "the amortization of the deferred tax asset related to the tax benefit from the Bermuda
    Economic Transition Adjustment"; "relates only to Chubb income, which excludes noncontrolling
    interests".
  - Core operating ROE / ROTE (L717): "annualized ... The numerator includes core operating
    income (loss), net of tax. The denominator includes the average Chubb shareholders' equity for
    the period adjusted to exclude unrealized gains (losses) on investments, current discount
    rate on future policy benefits (FPB), and instrument-specific credit risk on market risk
    benefits (MRB), all net of tax and attributable to Chubb. For the ROTE calculation, the
    denominator is also adjusted to exclude Chubb goodwill and other intangible assets, net of
    tax." (GAAP "Annualized return on equity" has no definition in D04.)
  - P&C combined ratio (L718): "the sum of the loss and loss expense ratio, acquisition cost ratio
    and the administrative expense ratio excluding the life business and including the realized
    gains and losses on the crop derivatives"; CAY CR excl. cat (L719) excludes P&C cats and PPD.
  - Global P&C (L720-721): "comprise consolidated operating results (including corporate) and
    exclude the operating results of Chubb's Life Insurance and North America Agricultural
    Insurance segments."
  - Tangible BVPS (L722): "Chubb shareholders' equity less Chubb goodwill and other intangible
    assets, net of tax, divided by the shares outstanding." BVPS/TBVPS excl. AOCI (L731):
    "excludes AOCI from the numerator".
  - Adjusted operating cash flow (L733): excludes net investing activities of Huatai's asset
    management companies (Consolidated Investment Products). Life NPW and deposits (L735):
    includes deposits on universal life and investment contracts.
- Amendments or contradictions: none stated; differing ex-large-account-property percentages
  recorded above with their stated scopes.
- Coverage: FULL. Ledger: L1-1146 read in one pass; remaining none. Spot-check vs `docs/`
  (original keeps extra blank lines): goodwill row label (docs line 1223) and BVPS cell "189.93"
  (docs line 1368) identical to text L795/L893. Footnote check: not applicable (D04 has no
  numbered footnotes; its table notes are inline, e.g., the goodwill "Chubb portion"
  parenthetical and "NM – not meaningful comparison", L738).

## D05 - Chubb second quarter 2026 earnings release (Exhibit 99.1)

- Source: `docs/cb_ex991_2026-07-21.txt` -> `text/D05.txt` (1,473 lines); platform Doc 9
  (cb_ex991_2026-07-21). Pages: not applicable; printed page numbers 1-13 at L91, L226, L365,
  L533, L551, L820, L848, L871, L889, L908, L930, L1120, L1470.
- Written or submitted by: Chubb Limited (same address block L11-17). Quoted: Evan G.
  Greenberg (L356-372). Investor Contact Susan Spivak (L864).
- Type, date, edition: News Release, "ZURICH – July 21, 2026" (L95); html d78544dex991.htm (L4).
  Call Wednesday, July 22, 2026, 8:30 a.m. Eastern (L856). Refers to a Financial Supplement
  "dated June 30, 2026" (L854) and to reconciliations "on pages 27-33 in the Financial
  Supplement" (L919-920) — not in the bundle. Second Chubb edition (D04 is the first).
- Period covered: quarter ended June 30, 2026 vs Q2 2025; six months ended June 30, 2026 vs 2025
  (L222, L230-355, L547, L879, L1124-1466); balance sheet June 30, 2026 vs December 31, 2025;
  BVPS growth "from June 30, 2025" (L95) and "from December 31, 2025" (L222). No March 31, 2026
  balance-sheet values and no Q1-only columns.
- Entities and aliases: as D04; adds "Asia Life and North America Worksite businesses" (L360);
  bullet labels "North America Commercial", "Middle market and small commercial", "Major accounts
  and specialty", "North America Personal", "North America Agriculture" (L43-59).
- Tables (US$ millions):
  - p.2 Second Quarter Summary L97-220 (2026 | 2025 | Change | per share 2026 | 2025 | Change):
    Net income $2,854 | $2,968 | (3.8)% | $7.30 | $7.35 | (0.7)%; Adjusted net realized (gains)
    losses and other, net of tax (47) | (539) | (91.3)% | (0.13) | (1.33) | (90.2)%; Integration
    expenses and severance 6 | 2 | NM | 0.02 | - | NM; MRB (gains) losses (4) | 15 | NM | (0.01) |
    0.04 | NM; Amortization of deferred tax asset from Bermuda law 33 | 34 | (2.9)% | 0.08 | 0.08 |
    -; Core operating income $2,842 | $2,480 | 14.6% | $7.26 | $6.14 | 18.2%; Annualized ROE 15.3%
    | 17.6%; Core operating ROTE 21.2% | 21.0%; Core operating ROE 14.5% | 13.9%.
  - p.3 Six Months Ended Summary L230-353: Net income $5,174 | $4,299 | 20.4% | $13.17 | $10.63 |
    23.9%; Adjusted net realized (gains) losses and other 296 | (480) | NM | 0.75 | (1.18) | NM;
    Integration 13 | 2 | NM | 0.03 | - | NM; MRB (16) | 93 | NM | (0.04) | 0.23 | NM; Bermuda 64 |
    55 | 16.4% | 0.16 | 0.14 | 14.3%; Core operating income $5,531 | $3,969 | 39.4% | $14.07 |
    $9.82 | 43.3%; Annualized ROE 13.9% | 12.9%; Core ROTE 20.9% | 16.9%; Core ROE 14.3% | 11.2%.
    Tax sentence L355 (six months only): tax expenses (benefits) "$3 million and $55 million ...
    for adjusted net realized gains and losses and other; $(4) million and nil for integration
    expenses and severance; $3 million and $(16) million for market risk benefits gains and
    losses, and $1.32 billion and $937 million for core operating income." (D04 has no tax
    sentence.)
  - p.4 Operating highlights L373-529 (Q2 2026 | Q2 2025 | Change): Consolidated NPW "(increase
    of 2.0% in constant dollars)" 14,705 | 14,196 | 3.6%. P&C NPW "(increase of 1.4% in constant
    dollars) (increase of 6.3% excluding large account and E&S property)" 12,768 | 12,394 | 3.0%;
    UW income 1,937 | 1,631 | 18.8%; CR 83.8% | 85.6%; CAY UW excl. cat 2,129 | 2,012 | 5.8%; CAY CR
    excl. cat 82.2% | 82.3%. Global P&C NPW "(1.1% cc)" 11,992 | 11,661 | 2.8%; UW income 1,871 |
    1,566 | 19.5%; CR 83.5% | 85.4%; CAY UW excl. cat 2,049 | 1,946 | 5.4%; CAY CR excl. cat 81.9% |
    81.9%. Life NPW "(6.3% cc)" 1,937 | 1,802 | 7.5%; Segment income "(9.1% cc)" 332 | 305 | 9.0%.
  - p.6 Key segment items L555-815: Total NA P&C NPW 8,424 | 8,394 | 0.4%; CR 81.5% | 81.7%; CAY
    excl. cat 79.4% | 79.7%. NA Commercial NPW "(increase of 4.1% excluding large account and E&S
    property)" 5,594 | 5,723 | (2.3)%; Major accounts retail and E&S wholesale "(increase of 0.4%
    excluding large account and E&S property)" 3,257 | 3,578 | (9.0)%; Middle market and small
    commercial 2,337 | 2,145 | 8.9%; CR 85.4% | 83.5%; CAY excl. cat 81.8% | 81.1%. NA Personal NPW
    2,054 | 1,938 | 6.0%; CR 67.3% | 73.5%; CAY excl. cat 69.9% | 72.2%. NA Agricultural NPW 776 |
    733 | 6.0%; CR 89.7% | 89.1%; CAY excl. cat 87.6% | 88.8%. Overseas General NPW "(4.8% cc)"
    3,990 | 3,620 | 10.2%; Commercial P&C 2,259 | 2,077 | 8.8%; Consumer P&C 1,731 | 1,543 | 12.1%;
    CR 82.2% | 90.3%; CAY excl. cat 85.2% | 85.4%. Global Reinsurance NPW 354 | 380 | (6.7)%; CR
    76.1% | 71.0%; CAY excl. cat 76.9% | 73.5%. Life NPW 1,937 | 1,802 | 7.5%; "Net premiums written
    and deposits (increase of 12.9% in constant dollars)" 2,652 | 2,320 | 14.4%; segment income
    332 | 305 | 9.0%. D05 omits D04's constant-dollar notes for Overseas General commercial/consumer
    and Global Reinsurance; D04 has no Life "net premiums written and deposits" row.
  - p.12 Summary Consolidated Balance Sheets L934-1116 (June 30, 2026 | December 31, 2025):
    Investments 172,649 | 168,720; Cash and restricted cash 2,753 | 2,470; Total invested assets
    175,402 | 171,190; Insurance and reinsurance balances receivable 19,068 | 15,944; Reinsurance
    recoverable 20,284 | 20,338; Goodwill and other intangible assets 26,488 | 26,448 ("$25,859
    and $25,775 represents Chubb portion"); Other assets 40,080 | 38,407; Total assets 281,322 |
    272,327; Unpaid losses 89,669 | 88,018; Unearned premiums 28,511 | 26,279; Other liabilities
    82,297 | 78,251; Total liabilities 200,477 | 192,548; Chubb SE excl. AOCI 81,295 | 78,732; AOCI
    (5,923) | (4,975); Chubb SE 75,372 | 73,757; NCI 5,473 | 6,022; Total SE 80,845 | 79,779; BVPS
    $195.45 | $188.59; TBVPS $131.93 | $126.22; BVPS excl. AOCI $210.81 | $201.31; TBVPS excl. AOCI
    $145.67 | $136.91. December 31, 2025 column repeats D04's (plus the new invested-assets row).
  - p.13 Summary Consolidated Financial Data L1124-1466 (Q2 2026 | Q2 2025 | 6M 2026 | 6M 2025):
    GPW 17,947 | 17,276 | 34,498 | 32,381; NPW 14,705 | 14,196 | 28,710 | 26,842; NPE 13,889 |
    13,125 | 27,346 | 25,125; Losses and loss expenses 6,691 | 6,572 | 12,822 | 13,468; Policy
    benefits 1,615 | 1,406 | 3,400 | 2,633; Policy acquisition costs 2,632 | 2,415 | 5,228 |
    4,728; Administrative 1,168 | 1,125 | 2,317 | 2,205; NII 1,760 | 1,568 | 3,469 | 3,129; Net
    realized gains (losses) 162 | 160 | (245) | 44; MRB 5 | (17) | 19 | (109); Interest 200 | 181 |
    398 | 362; separate account 63 | (12) | 51 | (22); Other 133 | 667 | 306 | 760; Amortization of
    purchased intangibles 74 | 74 | 147 | 149; Integration 8 | 2 | 17 | 2; Income tax 742 | 717 |
    1,388 | 1,038; Net income 2,882 | 2,999 | 5,229 | 4,342; NCI 28 | 31 | 55 | 43; Chubb net income
    2,854 | 2,968 | 5,174 | 4,299; Diluted EPS net income $7.30 | $7.35 | $13.17 | $10.63, core
    $7.26 | $6.14 | $14.07 | $9.82; Weighted average shares 391.3 | 403.8 | 393.0 | 404.3; loss
    ratio 56.7% | 59.0% | 56.2% | 63.1%; acquisition 19.1% | 18.5% | 19.5% | 18.9%; administrative
    8.0% | 8.1% | 8.2% | 8.4%; P&C CR 83.8% | 85.6% | 83.9% | 90.4%; P&C UW income 1,937 | 1,631 |
    3,729 | 2,072.
- Lists: headline bullets L33-87 (fourteen, including segment sub-bullets L43-59); regional growth
  L63 (Latin America 15.6%, Asia 12.0%, Europe 5.1%).
- Forecasts, guidance, deadlines, effective dates: Greenberg L369 "The growth penalty we are
  paying in property will dissipate going forward."; L372 "CATs and FX aside, we are confident in
  our ability to continue to outperform and generate strong growth in operating earnings and EPS,
  and double-digit growth in tangible book value." (D04 L216 wording: "double-digit growth in EPS
  and tangible book value"). Market view L361, L369 ("soft market conditions are spreading to
  certain areas of casualty while financial lines also remain soft").
- Hedged claims: L372 confidence statement qualified by "CATs and FX aside"; L369 "will
  dissipate" stated without hedge.
- Rounded prose beside exact figures: NI "$2.85 billion versus $2.97 billion", core "$2.84
  billion" (L35, L95) vs 2,854 / 2,968 / 2,842; core "$2.8 billion" (L358); NPW "$14.7 Billion"
  (L29) vs 14,705; P&C NPW "$12.77 billion" (L39) vs 12,768; P&C UW "$1.94 billion, up 18.8%"
  (L67) and "more than $1.9 billion, up almost 19%" (L359) vs 1,937; CAY UW "$2.13 billion" vs
  2,129; Life NPW "$1.94 billion" (L79, L842) vs 1,937; Life NPW and deposits "$2.65 billion, up
  14.4%" (L79) vs 2,652; NII "$1.76 billion, up 12.3%" (L83) vs 1,760 | 1,568 (ratio of the printed
  figures is 1.1224); adjusted NII "$1.88 billion, up 11.4%" (L83), "a record $1.88 billion, up
  more than 11%" (L360); "Our invested asset now stands at $175 billion, up 9% over the last 12
  months" (L360) vs Total invested assets 175,402 (L968; no June 30, 2025 value printed); "Life
  income grew 9% to $332 million" (L360); "P&C premiums rose 3% ... or 6.3% excluding large
  account and E&S property" (L371); "North America was up about 0.5%" (L371) vs 0.4% (L585);
  "personal lines and agriculture each grew 6%" (L371); "Commercial was up 4.1% excluding major
  and specialty property" (L371) vs table label "(increase of 4.1% excluding large account and
  E&S property)" (L601); "In our international life insurance business, premiums and deposits
  rose 14.4%" (L371) vs L79/L803 where 14.4% is the Life Insurance segment's NPW and deposits;
  six months "net income was $5.17 billion, or $13.17 per share, and core operating income was
  $5.53 billion, or $14.07 per share" (L222).
- Notes: catastrophe losses "$475 million compared with $630 million" (L71); favorable PPD "$283
  million compared with $249 million" (L75); Q2 book value "favorably impacted by after-tax net
  realized and unrealized gains of $388 million ... partially offset by $254 million of foreign
  currency losses" (L95); six months "unfavorably impacted by after-tax net realized and
  unrealized losses of $1.55 billion ... partially offset by $92 million of foreign currency
  gains" (L222); BVPS/TBVPS +12.3%/+17.1% from June 30, 2025 and excl. AOCI +11.4%/+15.8% (L95),
  +3.6%/+4.5% and excl. AOCI +4.7%/+6.4% from December 31, 2025 (L222); capital L547 "Total
  capital returned to shareholders in the quarter was $1.37 billion, comprising share repurchases
  of $979 million at an average purchase price of $327.18 per share and dividends of $395
  million. Total capital returned to shareholders for the six months was $2.90 billion,
  comprising share repurchases of $2.12 billion at an average purchase price of $326.03 per share
  and dividends of $775 million." (no authorization or dividend dates); operating cash flow
  $3.73 billion, adjusted $3.48 billion (L543); NPE +5.8% (4.0% cc), P&C NPE +5.5% (3.6% cc)
  (L539); segment CR point attributions L826-838 (NA Commercial +1.9: cats +1.3, CAY loss excl.
  cat +0.5; NA Personal −6.2: PPD −2.4, cats −1.5, CAY loss −1.5; NA Agricultural +0.6: cats +1.8,
  underlying expense −0.7, CAY loss −0.5; Overseas General −8.1: cats −6.5, PPD −1.4, CAY loss
  −0.6, underlying expense +0.4); Life L842-843: International Life "$1.59 billion, up 6.2%",
  Chubb Benefits +14.0%, segment income +9.0% "primarily reflecting growth in International Life
  of 13.0%". Printed value 1,937 is both P&C underwriting income (L423, L1454) and Life NPW (L511,
  L785). Q2 2025 "Other" income 667 (L1278) carries no explanation in D05.
- Operative definitions: same Regulation G section as D04 (L875-921) with Q2 adjusted-NII inputs
  "$1 million and $4 million" amortization and "$119 million and $115 million" PE-partnership
  income, plus six-month inputs "$3 million and $6 million" and "$246 million and $222 million"
  (L879); "current accident year"/"underlying" rule L893; core operating income L894-896; core
  ROE/ROTE L898; P&C CR L899; Global P&C L901-902; TBVPS L903/L912; excl. AOCI L914.
- Amendments or contradictions: none stated; outlook wording change vs D04 recorded above.
- Coverage: FULL. Ledger: L1-1473 read in one pass; remaining none. Spot-check vs `docs/`: tax
  sentence (docs line 539), "Total invested assets" label (docs line 1470), BVPS "195.45" (docs
  line 1633) identical to text L355, L966, L1082. D05 has no numbered footnotes; the L355 tax
  sentence is its table note.

## D06 - Progressive March 2026 monthly (and first quarter) release (Exhibit 99)

- Source: `docs/pgr_ex991_2026-04-15.txt` -> `text/D06.txt` (483 lines); platform Doc 1
  (pgr_ex991_2026-04-15). Pages: not applicable; printed "- 1 -" to "- 9 -" at L48, L120, L170,
  L229, L276, L323, L395, L412, L480.
- Written or submitted by: The Progressive Corporation (NYSE: PGR), 300 North Commons Blvd.,
  Mayfield Village, Ohio 44143; Company Contact Douglas S. Constantine, (440) 395-3707 (L10-13).
  Named officers (L401): Tricia Griffith, CEO; John Sauerland, CFO.
- Type, date, edition: NEWS RELEASE "PROGRESSIVE REPORTS MARCH RESULTS", April 15, 2026
  (L17-19); html pgr202603ex99earningsrelea.htm (L4); results "for the month and quarter ended
  March 31, 2026" (L19).
- Period covered: March 2026 vs March 2025 and the quarter (Q1 = year-to-date) ended March 31.
  The month income statement (p.2) and month supplement (p.5) print the current month only; March
  2025 month values appear only in the p.1 summary. Fiscal year = calendar (10-K "for the year
  ending December 31, 2025", L474).
- Entities and aliases: Progressive / The Progressive Corporation / PGR; Personal Lines
  (Vehicles: Agency, Direct; Property), Special lines (PIF row), Commercial Lines; transportation
  network company (TNC) policies (L272); Name Your Price, Snapshot, HomeQuote Explorer (L407).
- Tables ($ millions unless noted):
  - p.1 summary L21-30 (March 2026 | 2025 | Change || Quarter 2026 | 2025 | Change): NPW 9,911 |
    9,041 | 10% || 23,641 | 22,206 | 6%; NPE 7,519 | 6,787 | 11% || 20,968 | 19,409 | 8%; Net income
    712 | 522 | 36% || 2,818 | 2,567 | 10%; Per share available to common shareholders 1.21 | 0.89 |
    37% || 4.80 | 4.37 | 10%; Total pretax net realized gains (losses) on securities (218) | (211)
    | 3% || (120) | (212) | (43)%; Combined ratio 88.8 | 90.9 | (2.1) pts. || 86.4 | 86.0 | 0.4 pts.;
    Average diluted equivalent common shares 586.2 | 587.7 | 0% || 586.9 | 587.7 | 0%. Changes are
    whole percents.
  - p.1 Policies in Force L32-44 (thousands; March 31, 2026 | 2025 | % Change): Agency – auto
    11,056 | 10,146 | 9; Direct – auto 16,572 | 14,771 | 12; Special lines 7,101 | 6,637 | 7;
    Property 3,640 | 3,576 | 2; Total Personal Lines 38,369 | 35,130 | 9; Commercial Lines 1,196 |
    1,162 | 3; Total 39,565 | 36,292 | 9.
  - p.2 Comprehensive income statement, month ended March 31, 2026, L50-116: NPW 9,911; NPE
    7,519; investment income 313; net realized gains on security sales 37; net holding period
    gains (losses) (255); total net realized (218); fees and other revenues 103; service revenues
    46; Total revenues 7,763; losses and LAE 5,179; policy acquisition costs 548; other
    underwriting expenses 1,054; investment expenses 3; service expenses 47; interest expense 24;
    Total expenses 6,855; income before income taxes 908; provision 196; Net income 712; OCI
    "Change in total net unrealized gains (losses) on fixed-maturity securities" (1,025); Total
    comprehensive income (loss) (313). Footnote 1 (L118, on "Comments on Monthly Results1"):
    Monthly Commentary and Note 1 of the 2025 audited statements.
  - p.3 YTD statements L122-168 (2026 | 2025): NPW 23,641 | 22,206; NPE 20,968 | 19,409;
    investment income 917 | 814; sales 96 | 1; holding period (216) | (213); total realized (120) |
    (212); fees and other 297 | 287; service revenues 126 | 111; Total revenues 22,188 | 20,409;
    losses and LAE 13,827 | 12,804; acquisition 1,538 | 1,456; other underwriting 3,048 | 2,719;
    investment expenses 8 | 7; service expenses 131 | 117; interest 70 | 70; Total expenses
    18,622 | 17,173; pre-tax 3,566 | 3,236; provision 748 | 669; Net income 2,818 | 2,567; OCI
    fixed-maturity (574) | 899; Total comprehensive income 2,244 | 3,466.
  - p.4 per-share and investment results L172-227 (March 2026 | YTD 2026 | YTD 2025): net income
    712 | 2,818 | 2,567; basic 1.22 | 4.81 | 4.38; diluted 1.21 | 4.80 | 4.37; comprehensive income
    (313) | 2,244 | 3,466; "Diluted1" (0.54) | 3.82 | 5.90 (footnote L209: "Basic earnings per
    share is disclosed where a comprehensive loss is reported since diluted comprehensive
    earnings per share are antidilutive."); average basic shares 585.0 | 585.6 | 586.0; dilutive
    1.2 | 1.3 | 1.7; diluted 586.2 | 586.9 | 587.7. FTE total return: fixed-income (1.1)% | 0.3% |
    2.5%; common stocks (5.0)% | (4.1)% | (5.0)%; total portfolio (1.3)% | 0.1% | 2.2%; pretax
    annualized investment income book yield 4.2% | 4.2% | 4.1%.
  - p.5 Supplemental Information, month L231-274 (columns Personal Lines Vehicles Agency | Direct
    | Property | Personal Lines Total | Commercial Lines Business(1) | Companywide Total): NPW
    2,951 | 4,094 | 277 | 7,322 | 2,588 | 9,911; % growth NPW 9% | 13% | (6)% | 10% | 7% | 10%; NPE
    2,670 | 3,646 | 268 | 6,584 | 935 | 7,519; % growth NPE 9% | 16% | 0% | 13% | 0% | 11%; loss/LAE
    67.8 | 69.4 | 59.5 | 68.4 | 71.8 | 68.8; expense 18.0 | 20.3 | 29.5 | 19.7 | 21.7 | 20.0;
    combined 85.8 | 89.7 | 89.0 | 88.1 | 93.5 | 88.8; "Net catastrophe loss ratio2" five values
    2.0 | 21.3 | 2.8 | 0.2 | 2.4 for six columns (merged cell not visible; see Gaps); Actuarial
    Adjustments3 reserve decrease/(increase): prior accident years $85 and current accident year
    14 (single companywide values), calendar year actuarial adjustment 35 | 62 | (1) | 96 | 3 | 99;
    Prior Accident Years Development favorable/(unfavorable): actuarial adjustment $85, all other
    development 56, total development $141; calendar year loss/LAE ratio 68.8; accident year
    loss/LAE ratio 70.7. Footnotes: 1 (on Commercial Lines "Business1") "Net premiums written
    include the March 1, 2026, renewal of our transportation network company (TNC) policies."; 2
    catastrophe losses "including development on prior events and the impact of reinsurance, if
    any, as a percent of net premiums earned"; 3 "Represents adjustments solely based on our
    normally scheduled actuarial reviews. For our Personal Lines property business, the actuarial
    reserving methodology includes changes to catastrophe losses, while the reviews in our
    personal and commercial vehicle businesses do not include catastrophes."
  - p.6 Supplemental Information, YTD L278-321 (same columns; no TNC marker): NPW 7,827 | 11,085 |
    693 | 19,605 | 4,033 | 23,641; growth 5% | 10% | (5)% | 7% | 3% | 6%; NPE 7,480 | 10,134 | 770
    | 18,384 | 2,583 | 20,968; growth 6% | 14% | (1)% | 10% | (4)% | 8%; loss/LAE 64.6 | 67.6 |
    49.0 | 65.6 | 67.4 | 65.9; expense 18.2 | 21.3 | 29.3 | 20.4 | 21.6 | 20.5; combined 82.8 |
    88.9 | 78.3 | 86.0 | 89.0 | 86.4; net cat loss ratio1 five values 0.9 | 12.5 | 1.4 | 0.2 | 1.3;
    actuarial adjustments2: prior accident years $122, current accident year 29, calendar year 49 |
    83 | (7) | 125 | 26 | 151; PAY development: actuarial $122, all other 329, total $451; calendar
    year loss/LAE 65.9; accident year loss/LAE 68.1. Personal Lines + Commercial Lines columns
    fall 1-3 short of Companywide NPW/NPE (e.g., 19,605 + 4,033 = 23,638 vs 23,641); no
    reconciling column is printed.
  - p.7 Balance sheet and other information L325-393 (March 31, 2026 only): fixed maturities(1)
    87,832 (amortized cost $88,408); short-term 2,126 (amortized cost $2,126); total
    available-for-sale 89,958; nonredeemable preferred stocks 240 (cost $259); common equities
    3,933 (cost $839); total equity securities 4,173; Total investments(2,3) 94,131; net premiums
    receivable 17,614; reinsurance recoverables 4,003 (including $3,748 on unpaid loss and LAE
    reserves); DAC 2,131; other assets 4,330; Total assets 122,209; unearned premiums 27,893; loss
    and LAE reserves 44,377; other liabilities(2) 9,514; Debt 8,386; Total liabilities 90,170;
    Shareholders' equity 32,039; Common shares outstanding 584.4; "Common shares repurchased in
    the current month" 768,273; "Average cost per common share" $204.48; Book value per common
    share $54.82; trailing 12-month return on average common shareholders' equity: net income
    35.0%, comprehensive income 35.2%; net unrealized pretax gains (losses) on fixed-maturity
    securities $(578); increase (decrease) from the previous month $(1,297); from December 2025
    $(726); debt-to-total capital ratio 20.7%; fixed-income portfolio duration 3.5; weighted
    average credit quality AA-. Footnotes: 1 hybrid securities "change in fair value of $2 million
    as a realized gain"; 2 "Includes $443 million of net unsettled security transactions
    classified in 'other liabilities.'"; 3 "Includes $6 billion, net of unsettled transactions, of
    investments in a consolidated, non-insurance subsidiary of the holding company."
- Lists: PIF table seven rows; Safe Harbor risk bullets L416-474 (30 bullets, last one L474).
- Forecasts, guidance, deadlines, effective dates: L401 Q1 conference call "currently scheduled
  to be held on Tuesday, May 5, 2026, at 9:30 a.m. eastern time" (60 minutes); "We plan to file
  our Quarterly Report on Form 10-Q with the SEC on Monday, May 4, 2026."; L403 "We plan to
  release April results on Wednesday, May 20, 2026, before the market opens." Event dates "are
  always subject to change" (L401). No financial outlook.
- Hedged claims: L401 dates "always subject to change"; L478 "Reported results, therefore, may be
  volatile in certain accounting periods."
- Rounded prose beside exact figures: none (no narrative results section).
- Notes: Monthly Commentary L399 "The companywide net premiums written growth rate for March is
  higher by about 3 percentage points due to February 28 being reported in March 2026, compared
  to February 2025, as a result of a nuance with our monthly closing process. Our first quarter
  2026 growth rate is unaffected." About L406 "the second largest personal auto insurer in the
  country, a leading seller of commercial auto, motorcycle, and boat insurance, and one of the top
  15 homeowners insurance carriers." Balance-sheet pretax unrealized changes $(1,297) month /
  $(726) from December 2025 (L384-385) vs income-statement OCI changes (1,025) month / (574) YTD
  (L112, L166; tax basis not labelled). No dividend declaration, record/payment dates or
  repurchase authorization (only month repurchases L375-376; risk bullet "the variable nature of
  our common share dividend policy" L466). No non-GAAP section; ratios labelled "GAAP Ratios".
- Operative definitions, rules and scope exceptions: catastrophe ratio footnotes L273 (month) and
  L320 (YTD: "during the year", no "if any"); actuarial adjustment footnotes L274/L321;
  comprehensive EPS footnote L209; TNC footnote L272; no BVPS definition (54.82 = 32,039 / 584.4
  shares, consistency check only).
- Amendments or contradictions: none.
- Coverage: FULL. Ledger: L1-483 read in one pass; remaining none. Spot-check vs `docs/`: TNC
  footnote (docs line 324) and BVPS row "54.82" (docs line 455) identical to text L272/L377.

## D07 - Progressive June 2026 monthly (and second quarter) release (Exhibit 99)

- Source: `docs/pgr_ex991_2026-07-15.txt` -> `text/D07.txt` (489 lines); platform Doc 7
  (pgr_ex991_2026-07-15). Pages: not applicable; printed "- 1 -" to "- 9 -" at L48, L124, L178,
  L235, L283, L330, L402, L418, L486.
- Written or submitted by: The Progressive Corporation; Company Contact Julianna Paterra, (719)
  432-2509 (L12-13; D06 named Douglas S. Constantine). Officers L408: Tricia Griffith, CEO;
  Andrew Quigg, CFO (D06 L401 named John Sauerland as CFO).
- Type, date, edition: NEWS RELEASE "PROGRESSIVE REPORTS JUNE RESULTS", July 15, 2026 (L17-19);
  html pgr202606ex99earningsrelea.htm; "the month and quarter ended June 30, 2026" (L19).
- Period covered: June 2026 vs June 2025; "Quarter" in the p.1 summary = Q2 2026 (three months to
  June 30) vs Q2 2025; YTD (six months) to June 30 on p.3, p.4 and p.6; p.2 and p.5 are June-only.
  No March or Q1-only figures reprinted.
- Entities and aliases: as D06; "Robinsons consumer segment" (L408, conference presentation
  topic).
- Tables ($ millions unless noted):
  - p.1 summary L21-30 (June 2026 | 2025 | Change || Quarter 2026 | 2025 | Change): NPW 6,772 |
    6,605 | 3% || 21,077 | 20,076 | 5%; NPE 7,100 | 6,954 | 2% || 21,573 | 20,310 | 6%; Net income
    779 | 1,124 | (31)% || 3,311 | 3,175 | 4%; per share 1.34 | 1.91 | (30)% || 5.67 | 5.40 | 5%;
    total pretax net realized gains (losses) (13) | 179 | (107)% || 604 | 387 | 56%; CR 90.0 | 86.6 |
    3.4 pts. || 87.3 | 86.2 | 1.1 pts.; average diluted shares 583.1 | 588.0 | (1)% || 584.2 | 587.8
    | (1)%.
  - p.1 PIF L32-44 (June 30, 2026 | 2025 | %): Agency – auto 11,211 | 10,423 | 8; Direct – auto
    16,721 | 15,245 | 10; Special lines 7,297 | 6,850 | 7; Property 3,631 | 3,608 | 1; Total
    Personal Lines 38,860 | 36,126 | 8; Commercial Lines 1,226 | 1,189 | 3; Total 40,086 | 37,315 |
    7.
  - p.2 month statement L50-120 (June 2026 only): NPW 6,772; NPE 7,100; investment income 329;
    sales 28; holding period (41); total realized (13); fees and other 104; service revenues 48;
    Total revenues 7,568; losses and LAE 4,937; acquisition 519; other underwriting 1,037;
    investment expenses 3; service expenses 51; interest 30; Total expenses 6,577; pre-tax 991;
    provision 212; Net income 779; OCI: fixed-maturity (120), foreign currency translation (1),
    OCI (121); Total comprehensive income 658. Footnote 1 L122 (accounting policies only).
  - p.3 YTD statements L126-176 (six months 2026 | 2025): NPW 44,718 | 42,282; NPE 42,541 |
    39,719; investment income 1,896 | 1,685; sales 112 | 20; holding period 372 | 155; total
    realized 484 | 175; fees and other 602 | 590; service revenues 274 | 244; Total revenues
    45,797 | 42,413; losses and LAE 28,399 | 26,409; acquisition 3,105 | 2,967; other
    underwriting 6,057 | 5,408; investment expenses 18 | 16; service expenses 285 | 256; interest
    158 | 139; Total expenses 38,022 | 35,195; pre-tax 7,775 | 7,218; provision 1,646 | 1,476; Net
    income 6,129 | 5,742; OCI: fixed-maturity (949) | 1,327, forecasted transactions 0 | 1, FX (1) |
    0, OCI (950) | 1,328; Total comprehensive income 5,179 | 7,070.
  - p.4 per share and investment L180-233 (June 2026 | YTD 2026 | YTD 2025): net income 779 |
    6,129 | 5,742; basic 1.34 | 10.49 | 9.80; diluted 1.34 | 10.47 | 9.77; comprehensive income 658
    | 5,179 | 7,070; diluted 1.13 | 8.84 | 12.03; basic shares 581.8 | 584.3 | 586.1; dilutive 1.3 |
    1.3 | 1.6; diluted shares 583.1 | 585.6 | 587.7. FTE total return: fixed-income 0.2% | 0.9% |
    4.3%; common stocks (0.3)% | 10.6% | 5.3%; total 0.2% | 1.3% | 4.3%; book yield 4.2% | 4.2% |
    4.2%.
  - p.5 Supplemental, month L237-281 (Agency | Direct | Property(1) | PL Total | Commercial Lines |
    Companywide): NPW 2,458 | 3,238 | 297 | 5,993 | 777 | 6,772; growth 0% | 5% | 4% | 3% | 1% | 3%;
    NPE 2,507 | 3,451 | 258 | 6,216 | 884 | 7,100; growth 0% | 6% | 2% | 3% | (6)% | 2%; loss/LAE
    70.5 | 72.1 | 35.2 | 69.8 | 66.6 | 69.5; expense 18.6 | 20.3 | 30.4 | 20.1 | 23.5 | 20.5; combined
    89.1 | 92.4 | 65.6 | 89.9 | 90.1 | 90.0; net cat loss ratio2 five values 2.4 | 8.9 | 2.6 | 0.6 |
    2.4; actuarial adjustments3: prior accident years $56, current accident year 52, calendar year
    19 | 30 | 14 | 63 | 45 | 108; PAY development: actuarial $56, all other 180, total $236;
    calendar year loss/LAE 69.5; accident year loss/LAE 72.8. Footnote 1 (L279, on the Property
    column header "Property1"): "Loss/LAE and combined ratios include a favorable 11.7 point
    impact related to an actuarial methodology process change, which impacted our incurred but not
    reported loss and loss adjustment expense reserves for our property products. The resulting
    one-time adjustment will not have an impact on future periods." No dollar amount is printed,
    the YTD table (p.6) carries no such footnote, and whether the item sits in the actuarial
    adjustment rows is not stated. Footnotes 2 and 3 as D06.
  - p.6 Supplemental, YTD L285-328: NPW 15,482 | 21,183 | 1,549 | 38,214 | 6,498 | 44,718; growth
    4% | 9% | (2)% | 6% | 3% | 6%; NPE 15,112 | 20,605 | 1,547 | 37,264 | 5,274 | 42,541; growth 5% |
    12% | 0% | 9% | (3)% | 7%; loss/LAE 66.4 | 68.6 | 48.4 | 66.9 | 65.3 | 66.7; expense 18.2 | 20.4 |
    29.7 | 19.9 | 21.8 | 20.2; combined 84.6 | 89.0 | 78.1 | 86.8 | 87.1 | 86.9; net cat loss ratio1
    2.3 | 13.0 | 2.7 | 0.4 | 2.4; actuarial adjustments2: prior accident years $283, current
    accident year 145, calendar year 115 | 173 | 36 | 324 | 104 | 428; PAY development: actuarial
    $283, all other 719, total $1,002; calendar year loss/LAE 66.7; accident year loss/LAE 69.1.
  - p.7 Balance sheet L332-400 (June 30, 2026 only): fixed maturities(1) 90,435 (amortized cost
    $91,485); short-term 1,978 (amortized cost $1,978); total AFS 92,413; nonredeemable preferred
    276 (cost $292); common equities 4,532 (cost $870); total equity securities 4,808; Total
    investments(2,3) 97,221; net premiums receivable 17,106; reinsurance recoverables 3,919
    (including $3,666 on unpaid loss and LAE reserves); DAC 2,211; other assets 4,468; Total assets
    124,925; unearned premiums 27,401; loss and LAE reserves 45,567; other liabilities(2) 9,237;
    Debt 8,387; Total liabilities 90,592; Shareholders' equity 34,333; common shares outstanding
    581.4; repurchased in the current month 845,952; average cost per common share $201.16; BVPS
    $59.05; TTM ROE net income 34.7%, comprehensive income 32.5%; net unrealized pretax gains
    (losses) on fixed maturities $(1,053); from the previous month $(152); from December 2025
    $(1,201); debt-to-total capital 19.6%; duration 3.5; credit quality AA-. Footnotes: 1 hybrid
    securities "$3 million as a realized gain"; 2 "$568 million of net unsettled security
    transactions"; 3 "$7 billion, net of unsettled transactions, of investments in a
    consolidated, non-insurance subsidiary of the holding company."
- Lists: Safe Harbor 30 bullets L422-480 (same as D06).
- Forecasts, guidance, deadlines, effective dates: L408 Q2 call "currently scheduled to be held
  on Tuesday, August 4, 2026, at 9:30 a.m. eastern time", 90 minutes, "an approximate 45-minute
  presentation on our Robinsons consumer segment"; "We plan to file our Quarterly Report on Form
  10-Q with the SEC on Monday, August 3, 2026."; L409 "We plan to release July results on
  Wednesday, August 19, 2026, before the market opens."
- Hedged claims: L279 one-time adjustment "will not have an impact on future periods" (stated
  without hedge); event dates "always subject to change" (L408).
- Rounded prose beside exact figures: none.
- Notes: Monthly Commentary L406 "The company has no additional commentary regarding June's
  results." About L412 "a leading seller of personal auto, commercial auto, motorcycle, and boat
  insurance, and one of the top 15 homeowners insurance carriers in the United States" (D06's
  "second largest personal auto insurer in the country" wording is absent). No dividend or
  authorization data (risk bullets L466, L472 only). Q2 per-share 5.67 (L27); YTD diluted 10.47
  (L199).
- Operative definitions: as D06 plus the methodology-change footnote L279; no BVPS definition
  (59.05 = 34,333 / 581.4, consistency check only).
- Amendments or contradictions: none stated; methodology process change is a stated one-time
  item (L279).
- Coverage: FULL. Ledger: L1-489 read in one pass; remaining none. Spot-check vs `docs/`:
  methodology footnote (docs line 329) and BVPS "59.05" (docs line 460) identical to text
  L279/L384.

## D08 - Travelers first quarter 2026 press release (Exhibit 99.1)

- Source: `docs/trv_ex991_2026-04-16.txt` -> `text/D08.txt` (790 lines); platform Doc 2
  (trv_ex991_2026-04-16). Pages: not applicable; printed page numbers 1-17 at L60, L67, L125,
  L177, L233, L289, L321, L389, L428, L476, L536, L573, L619, L654, L692, L749, L787.
- Written or submitted by: The Travelers Companies, Inc. (NYSE: TRV), 485 Lexington Avenue, New
  York, NY 10017-2630 (L10-13). Quoted: Alan Schnitzer, Chairman and Chief Executive Officer
  (L62-65). Contacts: Media Patrick Linehan 917.778.6267; Institutional Investors Abbe Goldstein
  917.778.6825 (L775-785).
- Type, date, edition: press release "Travelers Reports Excellent First Quarter Results" (L14),
  "New York, April 16, 2026" (L33); html a991pressrelease33126.htm (L4). Webcast 9:30 a.m.
  Eastern, Thursday, April 16, 2026 (L299), conference ID 5449478 (L301). Refers to the
  "statistical supplement" / "financial supplement" (L58, L299; D10 is that Q1 supplement), the
  10-Q filed April 16, 2026 and the 10-K filed February 12, 2026 (L420).
- Period covered: quarter ended March 31, 2026 vs Q1 2025 ("All comparisons vs. first quarter
  2025, unless noted otherwise", L109); "Twelve Months Ended March 31" columns (L440-448,
  L543-552); annual 2021-2025 plus "Average Annual 2005 - 2020" columns (L459-471, L520-531,
  L554-565); ten-year 2016-2025 tables (L621-640, L751-759); as-of March 31, 2026 / December 31,
  2025 / March 31, 2025.
- Entities and aliases: Travelers / The Travelers Companies, Inc. / TRV / "the Company";
  segments Business Insurance, Bond & Specialty Insurance, Personal Insurance; BI markets Select
  Accounts ("Select Accounts small commercial business", L64), Middle Market, National Accounts,
  National Property and Other, International; B&SI Management Liability, Surety, International;
  PI Automobile, Homeowners and Other, International; "the Canadian operations divested by the
  Company in the first quarter of 2026" (L127); Property Claim Services (PCS) (L571); Lloyd's
  (L310); Brazil joint venture (L312).
- Tables ($ millions; columns 2026 | 2025 | Change unless noted):
  - p.1 Consolidated Highlights L34-56 ("$ in millions, except for per share amounts, and
    after-tax, except for premiums and revenues"): NWP 10,338 | 10,515 | (2)%; Total revenues
    11,924 | 11,810 | 1; Net income 1,711 | 395 | 333; per diluted share 7.78 | 1.70 | 358; Core
    income 1,696 | 443 | 283; per diluted share 7.71 | 1.91 | 304; Diluted weighted average shares
    218.4 | 230.4 | (5); Combined ratio 88.6% | 102.5% | (13.9) pts; Underlying combined ratio
    85.3% | 84.8% | 0.5 pts; Return on equity 21.1% | 5.6% | 15.5 pts; Core ROE 19.7% | 5.6% |
    14.1 pts. As of March 31, 2026 | December 31, 2025 | March 31, 2025 | change from Dec 31, 2025 |
    from March 31, 2025: Book value per share 150.42 | 151.21 | 124.43 | (1)% | 21%; Adjusted BVPS
    161.60 | 158.01 | 138.99 | 2% | 16%.
  - p.3 Consolidated Results L69-106 (pre-tax unless noted): Underwriting gain (loss) 1,173 |
    (305) | 1,478, which includes net favorable PYD 413 | 378 | 35 and catastrophes, net of
    reinsurance (761) | (2,266) | 1,505; NII 1,008 | 930 | 78; Other income (expense), including
    interest expense (111) | (96) | (15); Core income before income taxes 2,070 | 529 | 1,541;
    Income tax expense 374 | 86 | 288; Core income 1,696 | 443 | 1,253; Net realized investment
    gains (losses) after income taxes 15 | (48) | 63; Net income 1,711 | 395 | 1,316. CR 88.6% |
    102.5% | (13.9) pts; impact of PYD (3.9) | (3.5) | (0.4) pts; catastrophes 7.2 | 21.2 | (14.0)
    pts; underlying CR 85.3% | 84.8% | 0.5 pts. NWP: BI 5,786 | 5,698 | 2%; B&SI 1,066 | 999 | 7;
    PI 3,486 | 3,818 | (9); Total 10,338 | 10,515 | (2)%.
  - p.4 Business Insurance L137-175: Underwriting gain 330 | 195 | 135; PYD 162 | 74 | 88;
    catastrophes (379) | (509) | 130; NII 708 | 656 | 52; Other income (expense) (3) | (9) | 6;
    pre-tax 1,035 | 842 | 193; tax 196 | 159 | 37; Segment income 839 | 683 | 156; CR 93.8% | 96.2%
    | (2.4) pts; PYD (2.9) | (1.3) | (1.6) pts; cats 6.9 | 9.3 | (2.4) pts; underlying 89.8% | 88.2%
    | 1.6 pts. NWP by market: Select Accounts 1,006 | 976 | 3%; Middle Market 3,329 | 3,166 | 5;
    National Accounts 343 | 312 | 10; National Property and Other 691 | 720 | (4); Total Domestic
    5,369 | 5,174 | 4; International 417 | 524 | (20); Total 5,786 | 5,698 | 2%.
  - p.5 Bond & Specialty L193-226: Underwriting gain 166 | 170 | (4); PYD 65 | 67 | (2); cats (8)
    | (19) | 11; NII 113 | 102 | 11; Other income 3 | 5 | (2); pre-tax 282 | 277 | 5; tax 28 | 57 |
    (29); Segment income 254 | 220 | 34; CR 83.3% | 82.5% | 0.8 pts; PYD (6.4) | (6.7) | 0.3 pts;
    cats 0.8 | 1.9 | (1.1) pts; underlying 88.9% | 87.3% | 1.6 pts. NWP: Management Liability 572
    | 553 | 3%; Surety 381 | 333 | 14; Total Domestic 953 | 886 | 8; International 113 | 113 | —;
    Total 1,066 | 999 | 7%.
  - p.6 Personal Insurance L245-278: Underwriting gain (loss) 677 | (670) | 1,347; PYD 186 | 237 |
    (51); cats (374) | (1,738) | 1,364; NII 187 | 172 | 15; Other income 18 | 18 | —; pre-tax 882
    | (480) | 1,362; tax 178 | (106) | 284; Segment income (loss) 704 | (374) | 1,078; CR 82.9% |
    115.2% | (32.3) pts; PYD (4.5) | (5.6) | 1.1 pts; cats 9.1 | 40.9 | (31.8) pts; underlying
    78.3% | 79.9% | (1.6) pts. NWP: Automobile 1,756 | 1,859 | (6)%; Homeowners and Other 1,730 |
    1,813 | (5); Total Domestic 3,486 | 3,672 | (5); International — | 146 | (100); Total 3,486 |
    3,818 | (9)%.
  - p.10 Net income to core income L438-474 (after-tax; three months 2026 | 2025, twelve months
    ended March 31 2026 | 2025): NI 1,711 | 395 | 7,604 | 4,271; net realized (gains) losses (15) |
    48 | (26) | 101; core 1,696 | 443 | 7,578 | 4,372. Pre-tax three months: NI 2,119 | 468;
    realized (49) | 61; core 2,070 | 529. Annual (2025 | 2024 | 2023 | 2022 | 2021 | Average Annual
    2005-2020): NI 6,288 | 4,999 | 2,991 | 2,842 | 3,662 | 2,988; loss from discontinued
    operations — x5 | (27); income from continuing operations 6,288 | 4,999 | 2,991 | 2,842 | 3,662
    | 3,015; realized 37 | 26 | 81 | 156 | (132) | (42); impact of changes in tax laws (1)(2) — x4 |
    (8) | 8; core 6,325 | 5,025 | 3,072 | 2,998 | 3,522 | 2,981; preferred dividends — x5 | 1;
    core less preferred 6,325 | 5,025 | 3,072 | 2,998 | 3,522 | 2,980. Footnotes (1) "Impact is
    recognized in the accounting period in which the change is enacted"; (2) "2017 reflects impact
    of Tax Cuts and Jobs Act of 2017 (TCJA)" (no separate 2017 column in this table).
  - p.11 per-share and segment reconciliations L478-501: diluted NI 7.78 | 1.70; realized (0.07) |
    0.21; core 7.71 | 1.91. Segment income BI 839 | 683; B&SI 254 | 220; PI 704 | (374); total
    segment income 1,797 | 529; Interest Expense and Other (101) | (86); total core 1,696 | 443.
  - p.11 Adjusted shareholders' equity L507-534: as of March 31 2026 | 2025: SE 31,986 | 28,191;
    NUI losses, net of tax 2,378 | 3,299; net realized (gains) losses, net of tax (15) | 48;
    adjusted SE 34,349 | 31,538. As of December 31 (2025 | 2024 | 2023 | 2022 | 2021 | average
    2005-2020): SE 32,894 | 27,864 | 24,921 | 21,560 | 28,887 | 25,023; NUI 1,478 | 3,640 | 3,129
    | 4,898 | (2,415) | (1,473); realized 37 | 26 | 81 | 156 | (132) | (42); tax law — x4 | (8) | 18;
    preferred stock — x5 | (39); discontinued — x5 | 27; adjusted SE 34,409 | 31,530 | 28,131 |
    26,614 | 26,332 | 23,514.
  - p.12 ROE and core ROE L541-565 (three months 2026 | 2025, twelve months 2026 | 2025):
    annualized NI 6,843 | 1,580 | 7,604 | 4,271; average SE 32,440 | 28,027 | 31,027 | 26,757; ROE
    21.1% | 5.6% | 24.5% | 16.0%; annualized core 6,785 | 1,773 | 7,578 | 4,372; adjusted average
    SE 34,361 | 31,521 | 33,353 | 30,079; core ROE 19.7% | 5.6% | 22.7% | 14.5%. Annual (2025 ...
    average): NI less preferred 6,288 | 4,999 | 2,991 | 2,842 | 3,662 | 2,987; average SE 29,924 |
    25,993 | 22,031 | 23,384 | 28,735 | 24,830; ROE 21.0% | 19.2% | 13.6% | 12.2% | 12.7% | 12.0%;
    core less preferred 6,325 | 5,025 | 3,072 | 2,998 | 3,522 | 2,980; adjusted average SE 32,643 |
    29,295 | 26,772 | 26,588 | 25,718 | 23,421; core ROE 19.4% | 17.2% | 11.5% | 11.3% | 13.7% |
    12.7%. The printed Q1 adjusted average (34,361) is not the simple average of the printed point
    values 34,409 (December 31, 2025, full-year realized adjustment) and 34,349.
  - p.13-14 Underlying underwriting income L581-640: pre-tax reconciliation (three months 2026 |
    2025): NI 1,711 | 395; realized (15) | 48; core 1,696 | 443; NII (833) | (763); other (income)
    expense incl. interest 92 | 81; underwriting income (loss) 955 | (239); tax on underwriting 218 |
    (66); pre-tax underwriting income (loss) 1,173 | (305); pre-tax PYD (413) | (378); pre-tax cats
    761 | 2,266; pre-tax underlying underwriting income 1,521 | 1,583. After-tax: PYD (325) | (297);
    cats 601 | 1,790; underlying underwriting income 1,231 | 1,254. Annual after-tax 2025 | 2024 |
    2023 | 2022 | 2021 | 2020 | 2019 | 2018 | 2017 | 2016 (L621-640): NI 6,288 | 4,999 | 2,991 |
    2,842 | 3,662 | 2,697 | 2,622 | 2,523 | 2,056 | 3,014; realized 37 | 26 | 81 | 156 | (132) | (11)
    | (85) | (93) | (142) | (47); tax law — x4 | (8) | — | — | — | 129 | —; core 6,325 | 5,025 |
    3,072 | 2,998 | 3,522 | 2,686 | 2,537 | 2,430 | 2,043 | 2,967; NII (3,254) | (2,952) | (2,436)
    | (2,170) | (2,541) | (1,908) | (2,097) | (2,102) | (1,872) | (1,846); other 326 | 308 | 337 | 277
    | 235 | 232 | 214 | 248 | 179 | 78; underwriting income 3,397 | 2,381 | 973 | 1,105 | 1,216 |
    1,010 | 654 | 576 | 350 | 1,199; PYD (815) | (559) | (113) | (512) | (424) | (276) | 47 | (409)
    | (378) | (510); cats 2,915 | 2,632 | 2,361 | 1,480 | 1,459 | 1,274 | 699 | 1,355 | 1,267 | 576;
    underlying underwriting income 5,497 | 4,454 | 3,221 | 2,073 | 2,251 | 2,008 | 1,400 | 1,522 |
    1,239 | 1,265.
  - p.15 Calculation of the Combined Ratio L656-686 (pre-tax): claims and CAE 6,382 | 8,006; less
    policyholder dividends 12 | 13 and allocated fee income 48 | 45; loss ratio numerator 6,322 |
    7,948; DAC amortization 1,766 | 1,778; G&A 1,541 | 1,459; less non-insurance G&A 136 | 109,
    allocated fee income 73 | 74, billing and policy fees and other 25 | 28; expense ratio numerator
    3,073 | 3,026; earned premium 10,605 | 10,710; loss and LAE ratio 59.6% | 74.2%; underwriting
    expense ratio 29.0% | 28.3%; CR 88.6% | 102.5%; PYD (3.9)% | (3.5)%; cats 7.2% | 21.2%;
    underlying 85.3% | 84.8%. Footnote (1) L686 on fee and billing-fee allocation and exclusion of
    non-insurance G&A.
  - p.16 BVPS reconciliation L694-716 (March 31, 2026 | December 31, 2025 | March 31, 2025): SE
    31,986 | 32,894 | 28,191; less NUI losses, net of tax (2,378) | (1,478) | (3,299); common SE
    excl. NUI 34,364 | 34,372 | 31,490; less goodwill 4,060 | 4,274 | 4,245 ("includes $208
    million of goodwill classified as held for sale as of December 31, 2025"), other intangible
    assets 331 | 337 | 356 ("includes $1 million ... held for sale as of December 31, 2025"),
    deferred tax on other intangibles (47) | (93) | (88); tangible SE excl. NUI 30,020 | 29,854 |
    26,977; common shares outstanding 212.6 | 217.5 | 226.6; BVPS 150.42 | 151.21 | 124.43;
    adjusted BVPS 161.60 | 158.01 | 138.99; TBVPS excl. NUI 141.18 | 137.24 | 119.07.
  - p.16 Total capitalization L718-737 (March 31, 2026 | December 31, 2025): debt 9,268 | 9,267;
    SE 31,986 | 32,894; total capitalization 41,254 | 42,161; less NUI (2,378) | (1,478); excl. NUI
    43,632 | 43,639; debt-to-capital 22.5% | 22.0%; excl. NUI 21.2% | 21.2%.
  - p.16-17 Invested assets L739-759: as of March 31 2026 | 2025: invested assets 102,978 |
    95,696; NUI pre-tax (3,008) | (4,172); excl. NUI 105,986 | 99,868. As of December 31 2025 ...
    2016: invested assets(1) 104,529 | 94,223 | 88,810 | 80,454 | 87,375 | 84,423 | 77,884 | 72,278
    | 72,502 | 70,488; NUI pre-tax (1,862) | (4,609) | (3,970) | (6,220) | 3,060 | 5,175 | 2,853 |
    (137) | 1,414 | 1,112; excl. NUI 106,391 | 98,832 | 92,780 | 86,674 | 84,315 | 79,248 | 75,031 |
    72,415 | 71,088 | 69,376. Footnote (1) L759 "Includes $3,347 million of invested assets
    classified as held for sale as of December 31, 2025."
- Lists: headline bullets L17-31 (eight); forward-looking topics L325-357 (17 bullets, the last
  "the impact of developments in the geopolitical environment, including the war with Iran");
  risk-factor groups L363-418; reportable segments L308-314 (three).
- Forecasts, guidance, deadlines, effective dates: L117 "The Company continues to expect the
  full year 2026 expense ratio to be approximately 28.5%."; L65 "We are confident that the
  advantages we have built will continue to drive strong results"; L63 dividend increase "In
  recognition of our very strong financial position and confidence in the outlook for our
  business"; debt-to-capital "target range of 15% to 25%" (L133); 2026 catastrophe disclosure
  threshold "$20 million to $30 million of losses before reinsurance and taxes" (L577); dividend
  "payable June 30, 2026, to shareholders of record at the close of business on June 10, 2026"
  (L135).
- Hedged claims: L117 "approximately 28.5%"; L765 operating statistics "dependent on the use of
  estimates and are therefore subject to change".
- Rounded prose beside exact figures: "Core income for the quarter was $1.7 billion" (L62);
  "underwriting income of $1.2 billion pre-tax" (L62) vs 1,173; "return more than $2.2 billion of
  excess capital ... including $2.0 billion of share repurchases" (L63) vs "$2.223 billion ...
  including $1.985 billion of share repurchases" (L31); NWP "$10.3 billion", BI "$5.8 billion",
  B&SI "by 7% to $1.1 billion", PI "$3.5 billion" (L64); "Net investment income increased 9% to
  $833 million after-tax" (L29) vs "Net investment income of $1.008 billion pre-tax ($833 million
  after-tax) increased 8%" (L123); "sixth consecutive quarter above $1.5 billion" (L19; D08
  prints pre-tax underlying underwriting income only for Q1 2026 and Q1 2025).
- Notes: Canadian divestiture: prior-year quarter NWP "included $223 million related to the
  Canadian operations divested by the Company in the first quarter of 2026. Excluding the impact
  of the sale, net written premiums increased slightly" (L127); BI $67 million, ex-sale +3%
  (L191); B&SI $10 million, ex-sale +8% (L243); PI $146 million, ex-sale −5% (L295). Capital L133:
  "The Company repurchased 6.0 million shares in the open market during the first quarter under
  its share repurchase authorizations at an average price of $300.30 per share for a total cost
  of $1.800 billion. In addition, the Company acquired 0.6 million shares for a total cost of $185
  million in connection with employee share-based compensation. At March 31, 2026, the Company had
  $5.215 billion of capacity remaining under its share repurchase authorizations approved by the
  Board of Directors."; statutory capital and surplus $31.063 billion; debt-to-capital 22.5%;
  excl. NUI 21.2%. Dividend L63/L135: "14% increase ... to $1.25 per share, marking 22 consecutive
  years of dividend increases with a compound annual growth rate of 8% over that period" (dividend
  dollars for the quarter not printed in D08; D10 p.1). SE L131: $31.986 billion, −3% from
  year-end; NUI losses "$3.008 billion pre-tax ($2.378 billion after-tax), compared to $1.862
  billion pre-tax ($1.478 billion after-tax) at year-end 2025", "driven by higher interest
  rates"; BVPS −1%, adjusted BVPS +2%. Realized gains "$49 million pre-tax ($15 million
  after-tax)" vs losses "$61 million pre-tax ($48 million after-tax)" (L33, L110). CR walk L113;
  expense ratio "+0.7 points to 29.0%, reflecting normal quarter-to-quarter variability" (L117);
  cats "severe wind and hail storms and winter storms in multiple states" (L121). PYD drivers: BI
  "commercial property and workers' compensation product lines for multiple accident years"
  (L190); B&SI "fidelity and surety product line for multiple accident years" (L241); PI "both the
  Automobile and Homeowners and Other product lines for recent accident years" (L293). B&SI L231
  "The underlying underwriting gain benefited from a non-recurring tax item and higher business
  volumes." Operating statistics L64 (Middle Market +5%, Select Accounts +3%, BI renewal premium
  change 5.8%, retention 86% "increased one point from recent quarters", record new business $775
  million; Management Liability retention 87%; Surety NWP +14%; PI positive renewal premium
  change in Auto and Homeowners). TTM core ROE 22.7% (L62, L552). About L304: "approximately
  34,000 employees and generated revenues of approximately $49 billion in 2025". The B&SI segment
  description still lists "certain surety and/or specialty insurance products in Canada" (L312).
- Operative definitions, rules and scope exceptions:
  - Core income (L436): "consolidated net income (loss) excluding the after-tax impact of net
    realized investment gains (losses), discontinued operations, the effect of a change in tax
    laws and tax rates at enactment, and cumulative effect of changes in accounting principles
    when applicable"; segment income "determined in the same manner ... on a segment basis".
  - Adjusted shareholders' equity (L505): "shareholders' equity excluding net unrealized
    investment gains (losses), net of tax, included in shareholders' equity, net realized
    investment gains (losses), net of tax, for the period presented, the effect of a change in tax
    laws and tax rates at enactment (excluding the portion related to net unrealized investment
    gains (losses)), preferred stock and discontinued operations."
  - ROE / core ROE (L538): "Return on equity is the ratio of annualized net income (loss) less
    preferred dividends to average shareholders' equity for the periods presented. Core return on
    equity is the ratio of annualized core income (loss) less preferred dividends to adjusted
    average shareholders' equity". Average SE (L540): "(a) the sum of total shareholders' equity
    excluding preferred stock at the beginning and end of each of the quarters for the period
    presented divided by (b) the number of quarters in the period presented times two".
  - Underwriting gain and underlying underwriting gain (L569): "net earned premiums and fee
    income less claims and claim adjustment expenses and insurance-related expenses"; underlying
    excludes catastrophes and prior-year development; "also referred to as underlying
    underwriting gain, underlying underwriting margin, underlying underwriting income or
    underlying underwriting result."
  - Catastrophe (L571-577): designated "by one or more industry recognized organizations ...
    such as Property Claim Services (PCS)"; threshold determined at segment level, aggregate
    international threshold, 2026 range $20-30 million. PYD (L579).
  - Combined ratio (L643-646): SAP-equivalent "except that the SAP underwriting expense ratio is
    based on net written premiums and the underwriting expense ratio as used in this earnings
    release is based on net earned premiums"; underlying CR (L650) "the combined ratio excluding
    the impact of net prior year reserve development and catastrophes".
  - Book value (L690): "Book value per share is total common shareholders' equity divided by the
    number of common shares outstanding. Adjusted book value per share is total common
    shareholders' equity excluding net unrealized investment gains and losses, net of tax,
    included in shareholders' equity, divided by the number of common shares outstanding."
    Tangible BVPS = adjusted BVPS excluding after-tax goodwill and other intangibles.
  - Total capitalization (L720) = total SE + debt. Other definitions L763-771: retention, renewal
    rate change, renewal premium change, new business; "For Business Insurance, retention,
    renewal premium change and new business exclude National Accounts. For Bond & Specialty
    Insurance, retention, renewal premium change and new business exclude surety and other
    products that are generally sold on a non-recurring, project specific basis. For each of the
    segments, production statistics referred to herein are domestic only unless otherwise
    indicated."; statutory capital and surplus; holding company liquidity.
- Amendments or contradictions: none stated.
- Coverage: FULL. Ledger: L1-790 read in one pass; remaining none. Spot-check vs `docs/`: BVPS
  row (docs line 55), capacity sentence (docs line 145), dividend sentence (docs line 147),
  shares/BVPS rows (docs lines 788-789) and footnote "(1) Includes $3,347 million of invested
  assets classified as held for sale ..." (docs line 843) identical to text L54, L133, L135,
  L713-714, L759.

## D09 - Travelers second quarter 2026 press release (Exhibit 99.1)

- Source: `docs/trv_ex991_2026-07-17.txt` -> `text/D09.txt` (850 lines); platform Doc 8
  (trv_ex991_2026-07-17). Pages: not applicable; printed page numbers 1-19 at L61, L67, L122,
  L152, L209, L259, L291, L342, L376, L441, L486, L538, L596, L633, L679, L714, L752, L809, L847.
- Written or submitted by: The Travelers Companies, Inc. (L10-13); Alan Schnitzer quoted
  (L63-65); same contacts (L835-845).
- Type, date, edition: press release "Travelers Reports Excellent Second Quarter and
  Year-to-Date Results" (L14), "New York, July 17, 2026" (L32); html a991pressrelease63026.htm.
  Webcast 9:00 a.m. Eastern, Friday, July 17, 2026 (L361). Forward-looking section still cites
  the 10-Q filed April 16, 2026 and the 10-K filed February 12, 2026 (L480). No Q2 Travelers
  supplement is in the bundle.
- Period covered: quarter ended June 30, 2026 ("All comparisons vs. second quarter 2025", L108);
  six months ended June 30 ("vs. year-to-date 2025", L127); twelve months ended June 30 in the
  core-income and ROE reconciliations (L502-510, L603-612); annual tables as D08; as-of June 30,
  2026 / December 31, 2025 / June 30, 2025. No March 31, 2026 column.
- Entities and aliases: as D08.
- Tables (Q2 2026 | Q2 2025 | Change || 6M 2026 | 6M 2025 | Change):
  - p.1 Consolidated Highlights L33-57: NWP 11,529 | 11,543 | — % || 21,867 | 22,058 | (1)%; Total
    revenues 12,153 | 12,116 | — || 24,077 | 23,926 | 1; NI 2,208 | 1,509 | 46 || 3,919 | 1,904 |
    106; per diluted 10.26 | 6.53 | 57 || 18.01 | 8.23 | 119; Core income 2,160 | 1,504 | 44 ||
    3,856 | 1,947 | 98; per diluted 10.04 | 6.51 | 54 || 17.73 | 8.42 | 111; diluted shares 213.6 |
    229.3 | (7) || 216.0 | 229.7 | (6); CR 83.6% | 90.3% | (6.7) pts || 86.1% | 96.3% | (10.2) pts;
    underlying CR 84.1% | 84.7% | (0.6) pts || 84.7% | 84.7% | — pts; ROE 27.1% | 20.9% | 6.2 pts ||
    24.1% | 13.4% | 10.7 pts; core ROE 24.9% | 18.8% | 6.1 pts || 22.3% | 12.3% | 10.0 pts. As of
    June 30, 2026 | December 31, 2025 | June 30, 2025 | change from Dec 31 | from June 30: BVPS
    158.81 | 151.21 | 131.11 | 5% | 21%; adjusted BVPS 168.20 | 158.01 | 144.57 | 6% | 16%.
  - p.3 Consolidated Results L69-105: Underwriting gain 1,738 | 1,022 | 716 || 2,911 | 717 |
    2,194; PYD 578 | 315 | 263 || 991 | 693 | 298; catastrophes (518) | (927) | 409 || (1,279) |
    (3,193) | 1,914; NII 1,070 | 942 | 128 || 2,078 | 1,872 | 206; other incl. interest (101) |
    (89) | (12) || (212) | (185) | (27); core pre-tax 2,707 | 1,875 | 832 || 4,777 | 2,404 | 2,373;
    tax 547 | 371 | 176 || 921 | 457 | 464; core 2,160 | 1,504 | 656 || 3,856 | 1,947 | 1,909;
    realized after tax 48 | 5 | 43 || 63 | (43) | 106; NI 2,208 | 1,509 | 699 || 3,919 | 1,904 |
    2,015. CR impact: PYD (5.4) | (2.9) | (2.5) || (4.6) | (3.2) | (1.4) pts; cats 4.9 | 8.5 | (3.6)
    || 6.0 | 14.8 | (8.8) pts. NWP: BI 5,984 | 5,792 | 3% || 11,770 | 11,490 | 2%; B&SI 1,237 |
    1,085 | 14 || 2,303 | 2,084 | 11; PI 4,308 | 4,666 | (8) || 7,794 | 8,484 | (8); Total 11,529 |
    11,543 | — || 21,867 | 22,058 | (1)%.
  - p.5 Business Insurance L156-193: UW gain 728 | 346 | 382 || 1,058 | 541 | 517; PYD 319 | 79
    | 240 || 481 | 153 | 328; cats (238) | (368) | 130 || (617) | (877) | 260; NII 762 | 662 | 100
    || 1,470 | 1,318 | 152; other 8 | 2 | 6 || 5 | (7) | 12; pre-tax 1,498 | 1,010 | 488 || 2,533 |
    1,852 | 681; tax 300 | 197 | 103 || 496 | 356 | 140; segment income 1,198 | 813 | 385 || 2,037
    | 1,496 | 541; CR 86.8% | 93.6% | (6.8) || 90.2% | 94.9% | (4.7); PYD (5.7) | (1.4) | (4.3) ||
    (4.4) | (1.4) | (3.0); cats 4.3 | 6.7 | (2.4) || 5.6 | 8.0 | (2.4); underlying 88.2% | 88.3% |
    (0.1) || 89.0% | 88.3% | 0.7. NWP by market: Select Accounts 1,040 | 1,004 | 4% || 2,046 | 1,980
    | 3%; Middle Market 3,235 | 3,034 | 7 || 6,564 | 6,200 | 6; National Accounts 344 | 329 | 5 ||
    687 | 641 | 7; National Property and Other 866 | 885 | (2) || 1,557 | 1,605 | (3); Total
    Domestic 5,485 | 5,252 | 4 || 10,854 | 10,426 | 4; International 499 | 540 | (8) || 916 | 1,064 |
    (14); Total 5,984 | 5,792 | 3% || 11,770 | 11,490 | 2%.
  - p.6 Bond & Specialty L225-257: UW gain 178 | 196 | (18) || 344 | 366 | (22); PYD 75 | 81 | (6)
    || 140 | 148 | (8); cats (4) | (5) | 1 || (12) | (24) | 12; NII 113 | 107 | 6 || 226 | 209 | 17;
    other 4 | 3 | 1 || 7 | 8 | (1); pre-tax 295 | 306 | (11) || 577 | 583 | (6); tax 61 | 62 | (1) ||
    89 | 119 | (30); segment income 234 | 244 | (10) || 488 | 464 | 24; CR 82.8% | 80.3% | 2.5 ||
    83.0% | 81.4% | 1.6; PYD (7.2) | (8.0) | 0.8 || (6.8) | (7.3) | 0.5; cats 0.4 | 0.5 | (0.1) ||
    0.6 | 1.2 | (0.6); underlying 89.6% | 87.8% | 1.8 || 89.2% | 87.5% | 1.7. NWP: Management
    Liability 611 | 589 | 4% || 1,183 | 1,142 | 4%; Surety 480 | 342 | 40 || 861 | 675 | 28; Total
    Domestic 1,091 | 931 | 17 || 2,044 | 1,817 | 12; International 146 | 154 | (5) || 259 | 267 |
    (3); Total 1,237 | 1,085 | 14% || 2,303 | 2,084 | 11%.
  - p.8 Personal Insurance L293-325: UW gain (loss) 832 | 480 | 352 || 1,509 | (190) | 1,699; PYD
    184 | 155 | 29 || 370 | 392 | (22); cats (276) | (554) | 278 || (650) | (2,292) | 1,642; NII 195
    | 173 | 22 || 382 | 345 | 37; other 13 | 17 | (4) || 31 | 35 | (4); pre-tax 1,040 | 670 | 370 ||
    1,922 | 190 | 1,732; tax 213 | 136 | 77 || 391 | 30 | 361; segment income 827 | 534 | 293 ||
    1,531 | 160 | 1,371; CR 79.5% | 88.4% | (8.9) || 81.2% | 101.7% | (20.5); PYD (4.5) | (3.6) |
    (0.9) || (4.5) | (4.5) | —; cats 6.7 | 12.7 | (6.0) || 7.9 | 26.6 | (18.7); underlying 77.3% |
    79.3% | (2.0) || 77.8% | 79.6% | (1.8). NWP: Automobile 1,858 | 1,968 | (6)% || 3,614 | 3,827 |
    (6)%; Homeowners and Other 2,450 | 2,520 | (3) || 4,180 | 4,333 | (4); Total Domestic 4,308 |
    4,488 | (4) || 7,794 | 8,160 | (4); International — | 178 | (100) || — | 324 | (100); Total 4,308
    | 4,666 | (8)% || 7,794 | 8,484 | (8)%.
  - p.12-13 reconciliations L500-561 (Q2 | 6M | twelve months to June 30): NI 2,208 | 1,509 |
    3,919 | 1,904 | 8,303 | 5,246; realized (48) | (5) | (63) | 43 | (69) | 45; core 2,160 | 1,504 |
    3,856 | 1,947 | 8,234 | 5,291; pre-tax NI 2,767 | 1,881 | 4,886 | 2,349, realized (60) | (6) |
    (109) | 55, core 2,707 | 1,875 | 4,777 | 2,404; annual table identical to D08 L459-474;
    diluted per share NI 10.26 | 6.53 | 18.01 | 8.23, realized (0.22) | (0.02) | (0.28) | 0.19, core
    10.04 | 6.51 | 17.73 | 8.42; segment income BI 1,198 | 813 | 2,037 | 1,496, B&SI 234 | 244 | 488
    | 464, PI 827 | 534 | 1,531 | 160, total segment 2,259 | 1,591 | 4,056 | 2,120, Interest Expense
    and Other (99) | (87) | (200) | (173), core 2,160 | 1,504 | 3,856 | 1,947.
  - p.13 Adjusted SE L567-594: as of June 30 2026 | 2025: SE 33,121 | 29,518; NUI 1,960 | 3,031;
    realized (63) | 43; adjusted SE 35,018 | 32,592; December 31 annual table identical to D08.
  - p.14 ROE L601-625 (Q2 | 6M | TTM, each 2026 | 2025): annualized NI 8,833 | 6,036 | 7,838 |
    3,808 | 8,303 | 5,246; average SE 32,553 | 28,854 | 32,497 | 28,441 | 31,952 | 27,735; ROE 27.1%
    | 20.9% | 24.1% | 13.4% | 26.0% | 18.9%; annualized core 8,640 | 6,015 | 7,713 | 3,894 | 8,234 |
    5,291; adjusted average SE 34,698 | 32,016 | 34,529 | 31,769 | 34,024 | 30,879; core ROE 24.9% |
    18.8% | 22.3% | 12.3% | 24.2% | 17.1%; annual table identical to D08.
  - p.15-16 Underlying underwriting income L641-700 (Q2 | 6M): NII after-tax (883) | (774) | (1,716)
    | (1,537); other 88 | 78 | 180 | 159; underwriting income 1,365 | 808 | 2,320 | 569; tax on
    underwriting 373 | 214 | 591 | 148; pre-tax underwriting income 1,738 | 1,022 | 2,911 | 717;
    pre-tax PYD (578) | (315) | (991) | (693); pre-tax cats 518 | 927 | 1,279 | 3,193; pre-tax
    underlying underwriting income 1,678 | 1,634 | 3,199 | 3,217; after-tax PYD (456) | (249) |
    (781) | (546); after-tax cats 410 | 732 | 1,011 | 2,522; after-tax underlying underwriting
    income 1,319 | 1,291 | 2,550 | 2,545; ten-year annual table identical to D08.
  - p.17 Calculation of the Combined Ratio L716-746 (Q2 | 6M): claims and CAE 5,922 | 6,789 |
    12,304 | 14,795; policyholder dividends 8 | 10 | 20 | 23; allocated fee income 49 | 45 | 97 |
    90; loss ratio numerator 5,865 | 6,734 | 12,187 | 14,682; DAC 1,786 | 1,802 | 3,552 | 3,580;
    G&A 1,565 | 1,545 | 3,106 | 3,004; non-insurance G&A 132 | 113 | 268 | 222; allocated fee
    income 77 | 79 | 150 | 153; billing and policy fees 22 | 29 | 47 | 57; expense numerator 3,120 |
    3,126 | 6,193 | 6,152; earned premium 10,753 | 10,921 | 21,358 | 21,631; loss and LAE ratio
    54.6% | 61.7% | 57.1% | 67.9%; underwriting expense ratio 29.0% | 28.6% | 29.0% | 28.4%; CR
    83.6% | 90.3% | 86.1% | 96.3%; PYD (5.4) | (2.9) | (4.6) | (3.2); cats 4.9 | 8.5 | 6.0 | 14.8;
    underlying 84.1% | 84.7% | 84.7% | 84.7%.
  - p.18 BVPS reconciliation L754-776 (June 30, 2026 | December 31, 2025 | June 30, 2025): SE
    33,121 | 32,894 | 29,518; less NUI (1,960) | (1,478) | (3,031); common SE excl. NUI 35,081 |
    34,372 | 32,549; goodwill 4,060 | 4,274 | 4,283; other intangibles 325 | 337 | 348; deferred
    tax on intangibles (48) | (93) | (93); tangible SE excl. NUI 30,744 | 29,854 | 28,011; shares
    208.6 | 217.5 | 225.1; BVPS 158.81 | 151.21 | 131.11; adjusted BVPS 168.20 | 158.01 | 144.57;
    TBVPS excl. NUI 147.41 | 137.24 | 124.42.
  - p.18 Capitalization L778-797 (June 30, 2026 | December 31, 2025): debt 9,068 | 9,267; SE
    33,121 | 32,894; total capitalization 42,189 | 42,161; less NUI (1,960) | (1,478); excl. NUI
    44,149 | 43,639; debt-to-capital 21.5% | 22.0%; excl. NUI 20.5% | 21.2%.
  - p.18-19 Invested assets L799-819: June 30 2026 | 2025: 103,179 | 98,065; NUI pre-tax (2,478) |
    (3,831); excl. NUI 105,657 | 101,896; December 31 ten-year table identical to D08 (footnote
    $3,347 million held for sale, L819).
- Lists: headline bullets L16-30 (eight); forward-looking topics L385-417 (17); segments
  L370-378.
- Forecasts, guidance, deadlines, effective dates: L137 "The Company expects the full year 2026
  expense ratio to be approximately 28.5%." (D08 L117: "continues to expect"); L65 "we remain
  highly confident in the outlook for Travelers"; target range 15%-25% (L150); 2026 cat threshold
  $20-30 million (L637); dividend "payable September 30, 2026 to shareholders of record at the
  close of business on September 10, 2026" (L154).
- Hedged claims: "approximately 28.5%" (L137); operating statistics "subject to change" (L825).
- Rounded prose beside exact figures: core "$2.2 billion" (L63); "Second quarter underwriting
  income of $1.7 billion pre-tax" (L63) vs 1,738; "return more than $1.5 billion of excess capital
  ... including $1.3 billion of share repurchases" (L63) vs "$1.577 billion ... including $1.311
  billion" (L30); NWP "$11.5 billion", BI "$6.0 billion, 5% higher than the prior year quarter
  adjusting for the sale of our Canadian business", B&SI "by 14% to $1.2 billion", PI "$4.3
  billion" (L64); NII "+14%" to $883 million after-tax (L28, L63) and "$1.070 billion pre-tax
  ($883 million after-tax) increased 14%" (L120); six-month NII "$2.078 billion pre-tax ($1.716
  billion after-tax) increased 11%" (L142); "core return on equity over the last four quarters to
  24.2%" (L63; table L612).
- Notes: Canadian divestiture prior-year NWP: Q2 2025 "$273 million" (L124; BI $79 million,
  ex-sale +5%, L207; B&SI $16 million, ex-sale +16%, L274; PI $178 million, ex-sale −4%, L340);
  six months 2025 "$496 million" (L144; BI $146 million, +4%, L223; B&SI $26 million, +12%,
  L289; PI $324 million, −4%, L357); consolidated ex-sale +2% (Q2, L124) and +1% (six months,
  L144). Capital L150: "The Company repurchased 4.3 million shares of its common stock during the
  second quarter at an average price of $304.06 per share for a total cost of $1.311 billion. At
  June 30, 2026, the Company had $3.915 billion of capacity remaining under its share repurchase
  authorizations approved by the Board of Directors." (no authorization/other split; D08 gave
  $5.215 billion at March 31); statutory capital and surplus $31.433 billion; debt-to-capital
  21.5%, excl. NUI 20.5%. SE L148: $33.121 billion, +1% over year-end; NUI losses "$2.478 billion
  pre-tax ($1.960 billion after-tax)"; BVPS +5%, adjusted BVPS +6%. Realized gains Q2 "$60
  million pre-tax ($48 million after-tax), compared to $6 million pre-tax ($5 million after-tax)"
  (L32, L109); six months "$109 million pre-tax ($63 million after-tax), compared to net realized
  investment losses of $55 million pre-tax ($43 million after-tax)" (L129). CR walks L112 (Q2) and
  L133 (YTD); YTD expense ratio "+0.6 points to 29.0%" (L137); cats L118 ("severe wind and hail
  storms in multiple states") and L141. PYD drivers: BI Q2 "workers' compensation product line
  for multiple accident years and in the commercial property product line for recent accident
  years" (L206), YTD "workers' compensation and commercial property product lines for multiple
  accident years" (L222); B&SI Q2 "general liability product line for management liability
  coverages for multiple accident years and in the fidelity and surety product line for recent
  accident years" (L272), YTD order reversed (L287); PI Q2 and YTD recent accident years (L338,
  L355). B&SI YTD "The underlying underwriting gain benefited from a non-recurring tax item."
  (L279; not in the Q2 paragraph L264). PI underlying Q2 "primarily reflecting improvement in
  Automobile" (L336), YTD "both Automobile and Homeowners and Other" (L353). Operating statistics
  L64 (Middle Market +7%, Select +4%; BI renewal premium change 4.8%, Middle Market 6.1%, Select
  9.4%; retention 86%; record new business $805 million, +8%; Management Liability retention 88%;
  B&SI new business +8%; Surety NWP +40% "reflecting success with large projects"; PI higher
  Homeowners new business). Repurchase-factor wording changed slightly vs D08 L419 (L479).
- Operative definitions: identical to D08 (core income L498; adjusted SE L565; ROE and average SE
  L598-600; underwriting gain, catastrophe, PYD L629-639; combined ratio L703-712; BVPS L750;
  total capitalization L780; other definitions L823-831).
- Amendments or contradictions: none stated; outlook verb change recorded above.
- Coverage: FULL. Ledger: L1-850 read in one pass; remaining none. Spot-check vs `docs/`: BVPS
  rows (docs lines 58, 851), capacity sentence (docs line 164), dividend sentence (docs line 168)
  and held-for-sale footnote (docs line 905) identical to text L55, L774, L150, L154, L819.

## D10 - Travelers Financial Supplement, First Quarter 2026 (Exhibit 99.2)

- Source: `docs/trv_ex992_2026-04-16.txt` -> `text/D10.txt` (1,312 lines); platform Doc 3
  (trv_ex992_2026-04-16). Pages: not applicable; contents L11-61, "Index" L65, printed page
  numbers 1-36 on their own lines at L103, L155, L196, L234, L274, L300, L318, L357, L391, L410,
  L440, L472, L501, L520, L545, L578, L610, L630, L647, L691, L735, L758, L826, L857, L900, L932,
  L968, L1013, L1069, L1097, L1145, L1174, L1217, L1242, L1280, L1309.
- Written or submitted by: The Travelers Companies, Inc. (no named people).
- Type, date, edition: "Financial Supplement - First Quarter 2026 Exhibit 99.2" (L9); html
  a992finsupp33126.htm; file date 2026-04-16 (same as D08). L63 unaudited; "should be read in
  conjunction with the Company's Form 10-Q which will be filed".
- Period covered: five quarterly columns 1Q2025 | 2Q2025 | 3Q2025 | 4Q2025 | 1Q2026 (p.1-22,
  26, 27, 29, 30, 33-34; p.27 and p.35 balances as of March 31, 2025 ... March 31, 2026);
  two-column as-of pages March 31, 2026 | December 31, 2025 (p.23-25, 28, 31, 32).
- Entities and aliases: segments as D08 plus "Interest Expense and Other" (p.22); BI organisation
  (L1301): Select Accounts; Middle Market (Commercial Accounts, Construction, Technology & Life
  Sciences, Public Sector Services, Energy, Excess Casualty, Inland Marine, Ocean Marine, Boiler
  & Machinery); National Accounts; National Property and Other (National Property, Northland
  Transportation, Agribusiness, Northfield, National Programs); International (Global Services
  and "a 20% quota-share reinsurance agreement with subsidiaries of Fidelis Insurance Holdings
  Limited"); Simply Business; Business Insurance Other (asbestos, environmental, runoff). B&SI
  Brazil surety via Junto Holding Brasil S.A., "The Company owns 49.5% of Junto" (L1305).
  Reinsurer and structured-settlement groups (p.28, below). A.M. Best Company (p.28).
- Tables ($ millions; quarterly columns 1Q25 | 2Q25 | 3Q25 | 4Q25 | 1Q26 unless noted):
  - p.1 Financial Highlights L67-101: NI 395 | 1,509 | 1,888 | 2,496 | 1,711; NI per share basic
    1.73 | 6.63 | 8.37 | 11.24 | 7.89, diluted 1.70 | 6.53 | 8.24 | 11.06 | 7.78; core income 443 |
    1,504 | 1,867 | 2,511 | 1,696; core per share basic 1.94 | 6.61 | 8.27 | 11.31 | 7.82, diluted
    1.91 | 6.51 | 8.14 | 11.13 | 7.71; ROE 5.6% | 20.9% | 24.7% | 31.0% | 21.1%; core ROE 5.6% |
    18.8% | 22.6% | 29.6% | 19.7%; total assets 135,977 | 138,873 | 143,678 | 143,708 | 142,309;
    total equity 28,191 | 29,518 | 31,609 | 32,894 | 31,986; BVPS 124.43 | 131.11 | 141.72 | 151.21
    | 150.42; less NUI per share (14.56) | (13.46) | (8.83) | (6.80) | (11.18); adjusted BVPS 138.99
    | 144.57 | 150.55 | 158.01 | 161.60; weighted shares basic 226.9 | 225.9 | 224.1 | 220.3 |
    215.2, diluted 230.4 | 229.3 | 227.5 | 224.0 | 218.4; common shares outstanding at period end
    226.6 | 225.1 | 223.0 | 217.5 | 212.6; "Common stock dividends declared" 241 | 252 | 250 | 244 |
    238; common stock repurchased "Under Board of Directors authorization" shares 1.0 | 1.8 | 2.3 |
    5.8 | 6.0, cost 250 | 500 | 625 | 1,650 | 1,800; "Other" shares 0.4 | 0.3 | — | — | 0.6, cost 108
    | 57 | 3 | 3 | 185.
  - p.2 L105-151: realized (gains) losses after-tax 48 | (5) | (21) | 15 | (15); per share
    adjustments basic and diluted 0.21 | (0.02) | (0.10) | 0.07 | (0.07); participating share-based
    awards allocated net income (3) | (11) | (13) | (19) | (12) -> NI available to common 392 |
    1,498 | 1,875 | 2,477 | 1,699; allocated core income (3) | (11) | (14) | (18) | (12) -> core
    available 440 | 1,493 | 1,853 | 2,493 | 1,684; dilutive securities 3.5 | 3.4 | 3.4 | 3.7 | 3.2.
  - p.3 Statement of Income L157-192: premiums 10,710 | 10,921 | 11,135 | 11,148 | 10,605; NII
    930 | 942 | 1,033 | 1,054 | 1,008; fee income 119 | 124 | 127 | 125 | 121; net realized
    investment gains (losses) (61) | 6 | 27 | (20) | 49; other revenues 112 | 123 | 148 | 125 | 141;
    total revenues 11,810 | 12,116 | 12,470 | 12,432 | 11,924; claims and CAE 8,006 | 6,789 | 6,594 |
    5,832 | 6,382; DAC 1,778 | 1,802 | 1,849 | 1,837 | 1,766; G&A 1,459 | 1,545 | 1,572 | 1,544 |
    1,541; interest expense 99 | 99 | 111 | 116 | 116; total claims and expenses 11,342 | 10,235 |
    10,126 | 9,329 | 9,805; pre-tax 468 | 1,881 | 2,344 | 3,103 | 2,119; tax 73 | 372 | 456 | 607 |
    408; NI 395 | 1,509 | 1,888 | 2,496 | 1,711; effective tax rate on NII 17.9% | 17.9% | 17.8% |
    17.7% | 17.4%; NII after-tax 763 | 774 | 850 | 867 | 833; catastrophes pre-tax 2,266 | 927 |
    402 | 95 | 761, after-tax 1,790 | 732 | 318 | 75 | 601; favorable PYD pre-tax 378 | 315 | 22 |
    321 | 413, after-tax 297 | 249 | 16 | 253 | 325.
  - p.4 L198-230 (net of tax): underwriting gain (loss) (239) | 808 | 1,099 | 1,729 | 955; NII 763
    | 774 | 850 | 867 | 833; other incl. interest (81) | (78) | (82) | (85) | (92); core 443 | 1,504
    | 1,867 | 2,511 | 1,696; realized (48) | 5 | 21 | (15) | 15. Ratios (1)(2): loss and LAE 74.2% |
    61.7% | 58.7% | 51.8% | 59.6%; underwriting expense 28.3% | 28.6% | 28.6% | 28.4% | 29.0%; CR
    102.5% | 90.3% | 87.3% | 80.2% | 88.6%; PYD (3.5) | (2.9) | (0.2) | (2.9) | (3.9); cats 21.2 |
    8.5 | 3.6 | 0.9 | 7.2; underlying 84.8% | 84.7% | 83.9% | 82.2% | 85.3%. Footnotes (1) "Before
    policyholder dividends." (2) allocation rule, with billing and policy fees 28 | 29 | 28 | 28 |
    25, fee income to LAE 45 | 45 | 48 | 48 | 48 and to underwriting expenses 74 | 79 | 79 | 77 | 73,
    non-insurance G&A 109 | 113 | 131 | 110 | 136.
  - p.5 Core Income L236-270: total revenues excluding realized 11,871 | 12,110 | 12,443 | 12,452 |
    11,875; core pre-tax 529 | 1,875 | 2,317 | 3,123 | 2,070; tax 86 | 371 | 450 | 612 | 374.
  - p.6 Selected Statistics, statutory L276-296: GWP 11,890 | 12,225 | 12,292 | 11,296 | 11,750;
    NWP 10,515 | 11,516 | 11,472 | 10,856 | 10,323; NEP 10,710 | 10,897 | 11,133 | 11,146 | 10,593;
    losses and LAE 7,947 | 6,731 | 6,537 | 5,768 | 6,310; underwriting expenses 3,098 | 3,260 |
    3,239 | 3,114 | 3,400; statutory underwriting gain (loss) (335) | 906 | 1,357 | 2,264 | 883;
    policyholder dividends 13 | 10 | 12 | 10 | 12; after dividends (348) | 896 | 1,345 | 2,254 | 871;
    reserves 58,091 | 59,072 | 59,620 | 59,747 | 59,215; increase (decrease) 1,765 | 981 | 548 | 127
    | (532); statutory capital and surplus 27,785 | 28,364 | 29,965 | 31,064 | 31,063; NWP/surplus
    (1) 1.57:1 | 1.55:1 | 1.48:1 | 1.43:1 | 1.42:1 (footnote "Based on 12 months of rolling net
    written premiums.").
  - p.7 Written and Earned Premiums L302-314 (GAAP): written gross 11,890 | 12,251 | 12,293 |
    11,296 | 11,765, ceded (1,375) | (708) | (820) | (440) | (1,427), net 10,515 | 11,543 | 11,473 |
    10,856 | 10,338; earned gross 11,487 | 11,749 | 11,964 | 11,952 | 11,438, ceded (777) | (828) |
    (829) | (804) | (833), net 10,710 | 10,921 | 11,135 | 11,148 | 10,605. (Statutory NWP/GWP on
    p.6 differ from these GAAP rows, e.g., 1Q26 NWP 10,323 vs 10,338.)
  - p.8 BI Segment Income L320-353: premiums 5,465 | 5,545 | 5,700 | 5,702 | 5,493; NII 656 | 662 |
    727 | 737 | 708; fee income 108 | 111 | 114 | 112 | 111; other revenues 82 | 95 | 111 | 91 | 104;
    claims 3,705 | 3,584 | 3,667 | 3,198 | 3,531; DAC 917 | 944 | 973 | 962 | 938; G&A 847 | 875 |
    894 | 866 | 912; pre-tax 842 | 1,010 | 1,118 | 1,616 | 1,035; tax 159 | 197 | 211 | 324 | 196;
    segment income 683 | 813 | 907 | 1,292 | 839; NII after-tax 539 | 545 | 598 | 607 | 586; cats
    pre-tax 509 | 368 | 139 | 57 | 379, after-tax 402 | 291 | 110 | 44 | 299; PYD favorable
    (unfavorable) pre-tax 74 | 79 | (125) | 205 | 162, after-tax 58 | 62 | (99) | 162 | 127.
  - p.9 BI L359-387: underwriting gain (net) 157 | 274 | 318 | 690 | 261; loss and LAE 66.8% |
    63.7% | 63.3% | 55.1% | 63.3%; expense 29.4% | 29.9% | 29.6% | 29.3% | 30.5%; CR 96.2% | 93.6% |
    92.9% | 84.4% | 93.8%; PYD (1.3) | (1.4) | 2.2 | (3.6) | (2.9); cats 9.3 | 6.7 | 2.4 | 1.0 | 6.9;
    underlying 88.2% | 88.3% | 88.3% | 87.0% | 89.8%; fee/billing allocation table L380-387.
  - p.10 BI statutory L393-406: GWP 6,740 | 6,359 | 6,284 | 5,840 | 6,791; NWP 5,698 | 5,765 |
    5,674 | 5,514 | 5,771; NEP 5,465 | 5,521 | 5,698 | 5,700 | 5,481; statutory underwriting gain 115
    | 287 | 430 | 947 | 231; after dividends 106 | 282 | 421 | 942 | 223.
  - p.11 BI NWP L412-436: by market Select Accounts 976 | 1,004 | 920 | 930 | 1,006; Middle Market
    3,166 | 3,034 | 3,232 | 3,109 | 3,329; National Accounts 312 | 329 | 273 | 348 | 343; National
    Property and Other 720 | 885 | 841 | 666 | 691; Total Domestic 5,174 | 5,252 | 5,266 | 5,053 |
    5,369; International 524 | 540 | 409 | 461 | 417; Total 5,698 | 5,792 | 5,675 | 5,514 | 5,786;
    by product line workers' compensation 950 | 821 | 792 | 786 | 980; commercial automobile 1,030
    | 1,019 | 1,030 | 1,017 | 1,106; commercial property 873 | 1,051 | 961 | 820 | 821; general
    liability 753 | 878 | 998 | 967 | 847; commercial multi-peril 1,532 | 1,486 | 1,447 | 1,461 |
    1,580; other 36 | (3) | 38 | 2 | 35.
  - p.12 B&SI L442-468: premiums 995 | 1,021 | 1,042 | 1,049 | 1,018; NII 102 | 107 | 116 | 120 |
    113; pre-tax 277 | 306 | 311 | 300 | 282; tax 57 | 62 | 61 | 64 | 28; segment income 220 | 244 |
    250 | 236 | 254; cats pre-tax 19 | 5 | — | 1 | 8; PYD pre-tax 67 | 81 | 43 | 30 | 65.
  - p.13 B&SI L474-497: underwriting gain (net) 133 | 154 | 150 | 132 | 159; loss and LAE 43.2% |
    40.5% | 42.9% | 43.5% | 43.0%; expense 39.3% | 39.8% | 38.7% | 39.5% | 40.3%; CR 82.5% | 80.3% |
    81.6% | 83.0% | 83.3%; PYD (6.7) | (8.0) | (4.2) | (2.8) | (6.4); cats 1.9 | 0.5 | — | 0.1 | 0.8;
    underlying 87.3% | 87.8% | 85.8% | 85.7% | 88.9%. Footnote (1) (billing fees only; no fee-income
    allocation sentence).
  - p.14 B&SI statutory L503-516: GWP 1,129 | 1,166 | 1,160 | 1,192 | 1,211; NWP 999 | 1,085 |
    1,080 | 1,098 | 1,066; underwriting expenses 422 | 434 | 424 | 433 | 676; statutory underwriting
    gain (loss) 143 | 173 | 171 | 159 | (95); after dividends 139 | 168 | 168 | 154 | (99) (no
    explanation printed for the 1Q26 expense level).
  - p.15 B&SI NWP L522-541: Management Liability 553 | 589 | 613 | 571 | 572; Surety 333 | 342 |
    342 | 337 | 381; Total Domestic 886 | 931 | 955 | 908 | 953; International 113 | 154 | 125 | 190
    | 113; by product line fidelity and surety 394 | 400 | 407 | 395 | 447; general liability 440 |
    469 | 475 | 458 | 455; other 52 | 62 | 73 | 55 | 51. ("Surety" market row and "Fidelity and
    surety" product-line row are different groupings.)
  - p.16-17 PI L547-606: premiums 4,250 | 4,355 | 4,393 | 4,397 | 4,094; pre-tax (480) | 670 |
    1,012 | 1,336 | 882; segment income (374) | 534 | 807 | 1,086 | 704; cats pre-tax 1,738 | 554 |
    263 | 37 | 374; PYD pre-tax 237 | 155 | 104 | 86 | 186; underwriting gain (net) (529) | 380 | 631
    | 907 | 535; loss and LAE 91.0% | 64.0% | 56.4% | 49.4% | 58.8%; expense 24.2% | 24.4% | 24.9% |
    24.6% | 24.1%; CR 115.2% | 88.4% | 81.3% | 74.0% | 82.9%; PYD (5.6) | (3.6) | (2.4) | (1.9) |
    (4.5); cats 40.9 | 12.7 | 6.0 | 0.8 | 9.1; underlying 79.9% | 79.3% | 77.7% | 75.1% | 78.3%.
    Footnote (1) L600: billing fees and fee income allocated to underwriting expenses.
  - p.18 PI statutory L612-626: GWP 4,021 | 4,700 | 4,848 | 4,264 | 3,748; NWP 3,818 | 4,666 |
    4,718 | 4,244 | 3,486; statutory underwriting gain (loss) (593) | 446 | 756 | 1,158 | 747;
    policies in force (thousands) Automobile 3,118 | 3,083 | 3,050 | 3,025 | 2,819, Homeowners and
    Other 5,980 | 5,882 | 5,768 | 5,679 | 5,449.
  - p.19 PI NWP L632-643: Automobile 1,859 | 1,968 | 2,062 | 1,856 | 1,756; Homeowners and Other
    1,813 | 2,520 | 2,489 | 2,229 | 1,730; Total Domestic 3,672 | 4,488 | 4,551 | 4,085 | 3,486;
    International 146 | 178 | 167 | 159 | —; Total 3,818 | 4,666 | 4,718 | 4,244 | 3,486.
  - p.20 Automobile L649-687: statutory NWP 1,955 | 2,074 | 2,165 | 1,956 | 1,756 (differs from
    p.19 domestic Automobile in 2025 quarters); NEP 2,071 | 2,091 | 2,091 | 2,075 | 1,892; CR 83.4%
    | 85.3% | 84.9% | 89.4% | 82.9%; PYD (6.0) | (5.0) | (4.3) | (3.0) | (6.3); cats 1.9 | 1.3 | 0.9 |
    0.2 | 0.9; underlying 87.5% | 89.0% | 88.3% | 92.2% | 88.3%; cats pre-tax 39 | 27 | 19 | 4 | 15;
    PYD pre-tax 125 | 104 | 89 | 61 | 120; PIF 3,118 | 3,083 | 3,050 | 3,025 | 2,819, change from
    prior-year quarter (2.9)% | (3.1)% | (3.4)% | (4.0)% | (9.6)%, from prior quarter (1.0)% |
    (1.1)% | (1.1)% | (0.8)% | (6.8)%.
  - p.21 Homeowners and Other L693-731: statutory NWP 1,863 | 2,592 | 2,553 | 2,288 | 1,730; NEP
    2,179 | 2,264 | 2,302 | 2,322 | 2,202; CR 145.5% | 91.3% | 78.0% | 60.3% | 83.0%; PYD (5.1) |
    (2.2) | (0.7) | (1.1) | (3.0); cats 78.0 | 23.2 | 10.7 | 1.5 | 16.3; underlying 72.6% | 70.3% |
    68.0% | 59.9% | 69.7%; cats pre-tax 1,699 | 527 | 244 | 33 | 359; PYD pre-tax 112 | 51 | 15 | 25
    | 66; PIF 5,980 | 5,882 | 5,768 | 5,679 | 5,449, change from prior-year quarter (4.1)% | (4.6)% |
    (5.5)% | (6.3)% | (8.9)%, from prior quarter (1.3)% | (1.6)% | (1.9)% | (1.5)% | (4.1)%.
  - p.22 Interest Expense and Other L737-754: interest 99 | 99 | 111 | 116 | 116; G&A 11 | 12 | 13 |
    13 | 13; loss (86) | (87) | (97) | (103) | (101).
  - p.23 Consolidated Balance Sheet L760-824 (March 31, 2026 | December 31, 2025): fixed
    maturities 90,736 | 89,833 (amortized cost $93,742 and $91,717); equity securities 591 | 618;
    real estate 899 | 900; short-term 6,660 | 5,716; other investments 4,092 | 4,115; total
    investments 102,978 | 101,182; cash 615 | 842 (restricted $134 and $132); investment income
    accrued 801 | 877; premiums receivable 11,423 | 10,992; reinsurance recoverables 7,988 | 7,886
    ("net of allowance for estimated uncollectible reinsurance of $130 and $129"); ceded unearned
    premiums 1,877 | 1,283; DAC 3,587 | 3,518; deferred taxes 1,101 | 887; contractholder
    receivables 3,051 | 3,010; goodwill 4,060 | 4,066; other intangible assets 331 | 336; other
    assets 4,497 | 4,279; assets held for sale (1) — | 4,550; total assets 142,309 | 143,708; claims
    and CAE reserves 66,912 | 65,737; unearned premium reserves 22,772 | 22,431; contractholder
    payables 3,065 | 3,026; payables for reinsurance premiums 1,123 | 529; debt 9,268 | 9,267; other
    liabilities 7,183 | 7,282; liabilities held for sale (1) — | 2,542; total liabilities 110,323 |
    110,814; common stock 26,092 | 25,910 ("212.6 and 217.5 shares issued and outstanding");
    retained earnings 56,404 | 54,931; AOCI (3,078) | (2,500); treasury stock (47,432) | (45,447)
    ("582.5 and 575.9 shares"); total SE 31,986 | 32,894. Footnote (1) L824 "Amounts relate to the
    Canadian operations divested by the Company in the first quarter of 2026."
  - p.24 Investment Portfolio L828-855 (carrying value; pre-tax book yield): taxable fixed
    maturities 63,394 (4.16%) | 63,051 (4.11%); tax-exempt 27,342 (3.35%) | 26,782 (3.29%); total
    fixed maturities 90,736 (3.91%) | 89,833 (3.86%); non-redeemable preferred 33 | 35; common
    stocks 558 | 583; short-term 6,660 (3.78%) | 5,716 (3.86%); private equities 2,732 | 2,749;
    hedge funds 208 | 212; real estate partnerships 821 | 832; other 331 | 322; total 102,978 |
    101,182; NUI net of tax (2,378) | (1,478). Footnote (2) December 31 column "Excludes $3,347
    million of total investments classified as held for sale."
  - p.25 Fixed maturities L859-898: by type (U.S. Treasury 3,383 | 3,857; munis total 31,980 |
    31,378; foreign governments 358 | 312; MBS 12,848 | 13,232; corporate 42,167 | 41,054);
    quality Aaa 27.8% | 27.7%, Aa 35.9 | 36.7, A 22.6 | 21.9, Baa 12.5 | 12.5, investment grade 98.8
    | 98.8, below investment grade 1,046 (1.2%) | 1,050 (1.2%); average weighted quality "Aa3, AA-"
    | "Aa2, AA"; weighted average duration 4.9 | 4.7. Footnote (1) "Excludes $3,243 million of fixed
    maturities classified as held for sale."
  - p.26 Investment Income L902-930: gross fixed maturities 812 | 833 | 874 | 914 | 899;
    short-term 57 | 55 | 73 | 68 | 75; other 76 | 67 | 101 | 82 | 47; investment expenses 15 | 13 | 15
    | 10 | 13; NII pre-tax 930 | 942 | 1,033 | 1,054 | 1,008; income taxes 167 | 168 | 183 | 187 |
    175; after-tax 763 | 774 | 850 | 867 | 833; average invested assets (1)(2) 101,000 | 102,173 |
    105,655 | 107,932 | 106,666; average yield pre-tax 3.7% | 3.7% | 3.9% | 3.9% | 3.8%, after-tax
    3.0% | 3.0% | 3.2% | 3.2% | 3.1%. Footnote (2) includes $3,347 million held for sale at December
    31, 2025.
  - p.27 Realized and unrealized L934-966: realized fixed maturities (31) | (17) | (2) | (19) | (22);
    equity securities (22) | 20 | 39 | 8 | 1; "Other (1)" (8) | 3 | (10) | (9) | 70; pre-tax (61) | 6
    | 27 | (20) | 49; related taxes (13) | 1 | 6 | (5) | 34; net (48) | 5 | 21 | (15) | 15; gross
    gains 4 | 41 | 45 | 13 | 277; gross losses before impairments (63) | (35) | (18) | (33) | (225);
    impairments (2) | — | — | — | (3). NUI as of March 31, 2025 | June 30, 2025 | September 30, 2025
    | December 31, 2025 | March 31, 2026: fixed maturities (4,171) | (3,833) | (2,481) | (1,859) |
    (3,003); other (1) | 2 | (3) | (3) | (5) (here "(1)" is the March 31, 2025 value); before tax
    (4,172) | (3,831) | (2,484) | (1,862) | (3,008); related taxes (873) | (800) | (514) | (384) |
    (630); balance (3,299) | (3,031) | (1,970) | (1,478) | (2,378). Footnote (1) L966 "Other net
    realized investment gains in the first quarter of 2026 were driven by net realized investment
    gains related to the Canadian operations divested by the Company in the first quarter of
    2026."
  - p.28 Reinsurance Recoverables L970-1011 (March 31, 2026 | December 31, 2025): gross on paid and
    unpaid claims 4,364 | 4,352; structured settlements 2,279 | 2,469; mandatory pools 1,475 |
    1,485; gross 8,118 | 8,306; allowance (130) | (135); less held for sale — | 285; net 7,988 |
    7,886. Top five reinsurer groups at March 31, 2026: Swiss Re Group (A+) $658; Berkshire
    Hathaway (A++) 411; Munich Re Group (A+) 363; Sompo Group (A+) 236; Fairfax Financial Group
    (A+) 220; "nearly one thousand different reinsurance entities, over half is attributable to 10
    reinsurer groups". Top five structured-settlement groups: Fidelity & Guaranty Life Group (A)
    $628; Genworth Financial Group (B-) 312; Symetra Financial Corporation (A) 160; Brighthouse
    Financial, Inc. (A) 158; John Hancock Group (A+) 152. Footnote (4): "$5.97 billion, or 90%, were
    rated by A.M. Best Company ... 94% were rated A- or better. The remaining 10% ...: 5% related
    to captive insurance companies, 1% related to voluntary pools and 4% were balances from other
    companies not rated by A.M. Best Company."
  - p.29 Net Reserves L1015-1065: statutory rollforward by segment (beginning, incurred, paid,
    foreign exchange and other (1), end): BI end 43,742 | 44,477 | 45,148 | 45,383 | 45,599 (1Q26 FX
    and other (612)); B&SI end 5,072 | 5,249 | 5,304 | 5,367 | 5,331 (1Q26 (137)); PI end 9,277 |
    9,346 | 9,168 | 8,997 | 8,285 (1Q26 (909)); total end 58,091 | 59,072 | 59,620 | 59,747 | 59,215
    (1Q26 FX and other (1,658); incurred 7,947 | 6,731 | 6,537 | 5,768 | 6,310; paid (6,241) |
    (5,964) | (5,922) | (5,665) | (5,184)). Prior-year development unfavorable (favorable): BI
    asbestos — | — | 277 | — | —; BI all other (74) | (79) | (152) | (205) | (162); BI total (2) (74) |
    (79) | 125 | (205) | (162); B&SI (67) | (81) | (43) | (30) | (65); PI (237) | (155) | (104) | (86) |
    (186); total (378) | (315) | (22) | (321) | (413). Footnotes (1) "The amount for 1Q2026 includes
    the impact of net reserves disposed of related to the Canadian operations divested"; (2)
    "Excludes accretion of discount."
  - p.30 Asbestos Reserves L1071-1093: net beginning 1,338 | 1,279 | 1,237 | 1,446 | 1,355; incurred
    gross — | — | 327 | — | —, ceded — | — | (50) | — | —; paid gross 72 | 83 | 84 | 98 | 77; net
    ending 1,279 | 1,237 | 1,446 | 1,355 | 1,293.
  - p.31 Capitalization L1099-1142 (March 31, 2026 | December 31, 2025): commercial paper 100 |
    100; "7.75% Senior notes due April 15, 2026" 200 | 200; total short-term debt 300 | 300;
    eighteen long-term instruments from "7.625% Junior subordinated debentures due December 15,
    2027" 125 to "5.70% Senior notes due July 24, 2055" 750 (three junior subordinated debentures:
    7.625% 2027 $125, 8.50% 2045 $56, 8.312% 2046 $73; fifteen senior notes marked (1)
    "Redeemable anytime with 'make-whole' premium"); total long-term debt 9,054 | 9,054;
    unamortized fair value adjustment 31 | 31; unamortized issuance costs (117) | (118); total debt
    9,268 | 9,267; common equity excl. NUI 34,364 | 34,372; total capital excl. NUI 43,632 | 43,639;
    debt to capital excl. NUI 21.2% | 21.2%.
  - p.32 Statutory to GAAP L1147-1170 (March 31, 2026 (1) | December 31, 2025): statutory capital
    and surplus 31,063 | 31,064; GAAP adjustments goodwill and intangibles 3,430 | 3,640;
    investments (2,291) | (1,238); noninsurance companies (4,907) | (4,876); DAC 3,449 | 3,478;
    deferred federal income tax (111) | (446); current federal income tax (7) | (6); reinsurance
    recoverables 160 | 41; furniture, equipment & software 877 | 948; agents balances 224 | 182;
    other 99 | 107; total 923 | 1,830; GAAP SE 31,986 | 32,894. Footnote (1) L1170 on the March 31,
    2026 column: "Estimated and Preliminary".
  - p.33-34 Statement of Cash Flows L1176-1240: operating cash flow 1,360 | 2,334 | 4,227 | 2,685 |
    2,198; "Proceeds from the divestiture of the Canadian business" — x4 | 2,384 (L1212); net
    investing (808) | (1,716) | (4,553) | (575) | (335); "Treasury stock acquired - share repurchase
    authorizations" (250) | (500) | (619) | (1,635) | (1,785); "Treasury stock acquired - net
    employee share-based compensation" (102) | (22) | (1) | (2) | (149); "Dividends paid to
    shareholders" (240) | (250) | (247) | (242) | (237); issuance of debt — | — | 1,233 | — | —;
    employee share options 57 | 70 | 36 | 51 | 86; net financing (535) | (702) | 402 | (1,828) |
    (2,085); cash end 724 | 659 | 729 | 842 | 615 (held for sale at 4Q25 171); income taxes paid 24 |
    538 | 194 | 518 | 12; interest paid 61 | 136 | 60 | 136 | 94.
  - p.35 Adjusted SE reconciliation L1259-1270 (as of March 31, 2025 | June 30, 2025 | September
    30, 2025 | December 31, 2025 | March 31, 2026): SE 28,191 | 29,518 | 31,609 | 32,894 | 31,986;
    NUI 3,299 | 3,031 | 1,970 | 1,478 | 2,378; net realized (gains) losses, net of tax 48 | 43 | 22 |
    37 | (15) (year-to-date amounts); adjusted SE 31,538 | 32,592 | 33,601 | 34,409 | 34,349.
- Lists: contents L11-61 (36 pages); top-five reinsurer and structured-settlement lists (p.28);
  debt instruments (p.31, 20 rows); BI organisation list (L1301).
- Forecasts, guidance, deadlines, effective dates: none (no outlook). Debt maturity date "April
  15, 2026" for the $200 million 7.75% senior notes (L1109).
- Hedged claims: statutory March 31, 2026 column "Estimated and Preliminary" (L1170).
- Rounded prose beside exact figures: none (tables only).
- Notes: Dividends declared 238 vs paid 237 in 1Q26 (p.1 L92 vs p.34 L1227); authorization
  repurchase cost 1,800 (p.1) vs treasury stock acquired under authorizations 1,785 (p.34);
  "Other" cost 185 (p.1) vs "net employee share-based compensation" 149 (p.34). December 31, 2025
  allowance: "$129" in the balance-sheet caption (L783) vs "(135)" on p.28 (L979, with held-for-
  sale amounts shown separately). Goodwill 4,066 / intangibles 336 on the December 31, 2025
  balance sheet (L792-794) vs 4,274 / 337 in D08's BVPS table (which states it includes $208
  million / $1 million held for sale). Total investments December 31, 2025 101,182 (L776) vs
  D08 invested assets 104,529 (includes $3,347 million held for sale). PI statistics pages (p.20,
  p.21) carry statutory NWP that exceed p.19 domestic NWP in 2025 quarters by the PI
  International amounts. 3Q25 BI unfavorable PYD (125) includes asbestos 277 (p.29, p.30).
- Operative definitions, rules and scope exceptions (p.35-36):
  - Core income (L1255) as D08.
  - Average SE (L1257): "the sum of total shareholders' equity at the beginning and end of each of
    the quarters for the period presented divided by (b) the number of quarters in the period
    presented times two" (no "excluding preferred stock", unlike D08 L540); adjusted SE (L1257)
    "excluding net realized investment gains (losses), net of tax, net unrealized investment gains
    (losses), net of tax, included in shareholders' equity for the periods presented and the
    effect of a change in tax laws and tax rates at enactment" (no "preferred stock and
    discontinued operations", unlike D08 L505).
  - ROE (L1272): "the ratio of annualized net income (loss) to average shareholders' equity"
    (no "less preferred dividends", unlike D08 L538); core ROE likewise.
  - Underwriting gain (L1274); catastrophe (L1276, threshold for 2026 $20-30 million); PYD
    (L1278); combined ratio and underlying CR (L1285: "the combined ratio adjusted to exclude the
    impact of prior year reserve development and catastrophes, net of reinsurance"); BVPS and
    adjusted BVPS (L1293; no tangible BVPS definition); "Total capital is the sum of total
    shareholders' equity and debt" (L1295); statutory capital and surplus (L1297); segment
    descriptions (L1299-1307).
- Amendments or contradictions: none stated; wording differences from D08 definitions recorded
  above.
- Coverage: FULL. Ledger: L1-400, L400-799, L799-1248, L1248-1312 read (four chunks, overlapping
  at boundaries); remaining none. Spot-check vs `docs/`: 39 matching lines for the 36 page-number
  lines plus the April 15, 2026 note row, the held-for-sale footnote and the divestiture-proceeds
  row (grep count 39), consistent with text page markers.

## Shared ground (navigation only)

- Entities that appear in more than one document, and where:
  - Issuers: Allstate (D01, D02, D03), Chubb (D04, D05), Progressive (D06, D07), Travelers (D08,
    D09, D10). No issuer names any of the other three.
  - People by issuer: Allstate Tom Wilson (D01 L20, D02 L19); John Dugenske (D01 L221 "Interim
    Chief Financial Officer and President, Investments and Corporate Strategy"; D02 L252
    "President, Investments and Corporate Strategy"); contacts Nick Nottoli, Allister Gobin (D01
    L14, D02 L14). Chubb Evan G. Greenberg (D04 L203, D05 L356); Susan Spivak (D04 L686, D05
    L864). Progressive Tricia Griffith (D06 L401, D07 L408); CFO John Sauerland (D06 L401) vs
    Andrew Quigg (D07 L408); contacts Douglas S. Constantine (D06 L12) vs Julianna Paterra (D07
    L12). Travelers Alan Schnitzer (D08 L62, D09 L63); Patrick Linehan, Abbe Goldstein (D08 L783,
    D09 L843).
  - Mentioned (non-issuer) organisations: Huatai asset management companies (D04 L733, D05 L916);
    Fidelis Insurance Holdings Limited, Simply Business, Junto Holding Brasil S.A. (D10 L1301,
    L1305); reinsurer and structured-settlement groups (D10 L987-991, L1001-1005); A.M. Best
    Company (D10 L1009); Property Claim Services (D08 L571, D09 L631, D10 L1276); Lloyd's (D08
    L310, D09 L372, D10 L1301); Allstate Life Insurance Company (sold 2021, D03 S2), Esurance,
    Encompass (D01 L110), National General (D01 L141), Answer Financial (D03 S7), Ivantage (D03
    S17), Reciprocal Exchanges (D03 S13/S14 footnotes); "Robinsons consumer segment" (D07 L408).
  - Events named by more than one issuer: 2025 California wildfires (Allstate D01 L112; Chubb D04
    L57, L204); war in the Middle East / "the war with Iran" (Chubb D04 L216; Travelers D08 L357,
    L409, D09 L417, L469).
- Periods or series that more than one document covers, and where:
  - Q1 2026 (quarter ended March 31, 2026): D01, D03, D04, D06 (with the March month), D08, D10.
    Q2 2026 (quarter ended June 30, 2026): D02, D05, D07 (with the June month), D09. Six months /
    year to date to June 30: D02, D05, D07 (p.3, p.4, p.6), D09. Trailing twelve months: Allstate
    ROE (D01 p.10, D02 p.10, D03 S4); Progressive ROE (D06 L379, D07 L386); Travelers core income
    and ROE (D08 L440, L543; D09 L502, L603). Chubb ROE measures are annualized period figures
    (D04 L185-201; D05 L204-220, L337-353). Five-quarter series 1Q25-1Q26 appear only in the
    supplements D03 and D10.
  - Progressive "Quarter" column = Q1 (= year to date) in D06 L21 but Q2 only in D07 L21 (D07 YTD
    on p.3). All issuers use calendar years; stated explicitly by Progressive (10-K "for the year
    ending December 31, 2025", D06 L474, D07 L480) and by Travelers' "Twelve Months Ended December
    31" tables (D08 L459, D09 L521).
  - Release dates: D06 April 15; D08 and D10 April 16; D04 April 21; D01 and D03 April 29; D07
    July 15; D09 July 17; D05 July 21; D02 August 5, 2026.
  - Q1 values derivable from the Q2 editions (six months minus Q2), checked equal to the Q1
    editions' printed values: Allstate D02 dollar rows on p.1-p.9 vs D01 (revenues, NI, ANI,
    Property-Liability/auto/homeowners premiums, catastrophes and UW income, Protection Services
    revenue and ANI by business, investment results, statement-of-operations lines, ANI
    reconciliation lines); Chubb D05 p.3 summary and p.13 data vs D04 p.2 and p.11; Travelers D09
    consolidated and segment rows (UW gain, PYD, catastrophes, NII, tax, segment income, NWP by
    market and line, combined-ratio-calculation dollars, underlying underwriting income) vs D08;
    Progressive D07 YTD minus D07 Quarter vs D06 Quarter (NPW, NPE, NI, realized gains). Ratios,
    ROE and per-share figures are not additive (e.g., Allstate 6M diluted EPS 21.73 vs 9.25 +
    12.51; Chubb 6M diluted EPS 13.17 vs 5.88 + 7.30; Chubb 6M P&C CR 83.9% vs 84.0% and 83.8%).
  - As-of March 31, 2026 values printed only in the Q1 editions: Allstate balance sheet, BVPS
    113.52, shares 257.8 million / 257,804,210, BVPS denominator 260.8, PIF 212,052 and segment
    PIF (D01 p.1-p.7; D03 S3, S5, S13, S14); Chubb balance sheet, BVPS 189.93, TBVPS 126.65, excl.
    AOCI 205.15 / 140.35 (D04 p.10); Progressive balance sheet, BVPS 54.82, shares 584.4, debt
    8,386, March repurchases (D06 p.7); Travelers SE 31,986, NUI 2,378, debt 9,268, shares 212.6,
    BVPS 150.42, adjusted 161.60, TBVPS 141.18, repurchase capacity $5.215 billion, statutory
    capital $31.063 billion (D08 L131-133 and p.16; D10 p.1, p.23, p.31, p.32). The Q2 editions
    reprint December 31, 2025 columns (Travelers also June 30, 2025), not March 31, 2026.
  - Repeated (duplicate) columns and tables: December 31, 2025 balance-sheet column D01 = D02
    (Allstate) and D04 = D05 (Chubb; D05 adds "Total invested assets" 171,190); Travelers December
    31, 2025 values (SE 32,894, NUI 1,478, debt 9,267, shares 217.5, BVPS 151.21, adjusted 158.01,
    TBVPS 137.24) in D08, D09 and D10; Travelers annual and ten-year tables identical in D08
    (L459-474, L520-534, L554-565, L621-640, L751-759) and D09 (L521-536, L580-594, L614-625,
    L681-700, L811-819); Allstate prior-year quarter values in D01/D02 repeat D03 S1-S14 columns;
    Travelers Q1 2026 figures in D08 repeat D10 p.1-p.21.
- Documents that cite, amend or respond to another document in the bundle:
  - D03 is the investor supplement for the D01 quarter (both "First Quarter 2026", April 29); D10
    is the financial supplement for the D08 quarter (both April 16; D08 L58 and L299 refer to the
    supplement). D01 L58 and D02 L62 point to their own definitions sections.
  - Out-of-bundle references: Chubb Financial Supplements dated March 31, 2026 and June 30, 2026
    (D04 L676, L736-737 "pages 25-29"; D05 L854, L919-920 "pages 27-33"); Travelers 10-Q filed
    April 16, 2026 and 10-K filed February 12, 2026 (D08 L420, D09 L480); Progressive 2025
    Shareholders' Report Note 1 (D06 L118, D07 L122) and planned 10-Q filings (D06 L401, D07
    L408); Allstate Form 10-K Risk Factors (D01 L229, D02 L260).
  - No document amends another and no restatement language was found. Later editions do not
    confirm the earlier editions' planned events (Progressive D06 L401-403).
- Forecast/actual pairs, repeated/changed tables, same-period conflicts and scope relationships
  (locations only):
  - Outlook statements: Travelers full-year 2026 expense ratio "approximately 28.5%" (D08 L117
    "continues to expect"; D09 L137 "expects"), with Q1 29.0% (D08 L117, L679) and Q2 and YTD 29.0%
    (D09 L137, L739); no full-year actual in the bundle. Chubb Greenberg outlook wording D04 L216
    vs D05 L372 ("double-digit growth in EPS and tangible book value" vs "CATs and FX aside ...
    double-digit growth in tangible book value"); D05 L369 "growth penalty ... will dissipate going
    forward". Progressive planned dates (D06 L401-403: 10-Q May 4, call May 5, April results May
    20; D07 L408-409: 10-Q August 3, call August 4, July results August 19); no April, May or July
    releases in the bundle. Travelers debt-to-capital target range 15%-25% (D08 L133, D09 L150).
  - Same-named measures with company-specific definitions: combined ratio (Allstate "recorded
    combined ratio", underwriting margin = 100% minus CR, D01 L443; Chubb P&C CR excludes life and
    includes crop derivatives, D04 L718; Progressive "GAAP Ratios" loss/LAE plus expense, D06
    L245-249; Travelers SAP-equivalent with an NEP-based expense ratio, before policyholder
    dividends, D08 L643-646, D10 L220); underlying combined ratio (Allstate excludes cats, PYD
    excl. cats and purchased-intangible amortization, D01 L442, D03 S16; Chubb "current accident
    year ... excluding catastrophe losses" excludes cats and PPD, D04 L706, L719; Travelers
    excludes PYD and cats, D08 L650; Progressive prints only an "Accident year loss/LAE ratio",
    D06 L270); BVPS denominator (Allstate common shares plus dilutive potential shares, D03 S3,
    S16; Travelers "number of common shares outstanding", D08 L690; Chubb TBVPS "divided by the
    shares outstanding", D04 L722; Progressive no definition); ROE (Allstate TTM two-point
    average of common equity excl. preferred, D01 L392, D03 S17; Chubb annualized core ROE/ROTE
    with FPB and MRB adjustments, D04 L717; Progressive trailing 12-month return on average common
    equity, D06 L379; Travelers annualized period ROE with quarter-endpoint averaging, D08
    L538-540, D10 L1257, L1272); operating earnings measure (Allstate adjusted net income, Chubb
    core operating income, Travelers core income; Progressive reports none); P&C scope (Chubb "P&C"
    vs "Global P&C (excludes Agriculture)", D04 L720; Allstate "Property-Liability" = Allstate
    Protection + Run-off, D03 S6, while statement "Property and casualty insurance premiums" also
    include Protection Services, D03 S17); policies in force (Allstate item counts, total excludes
    divested businesses, D03 S5, D01 L57; Progressive PIF table, D06 L32-44; Travelers Personal
    Insurance PIF only, D10 p.18); Travelers statutory vs GAAP NWP (D10 p.6 vs p.7).
  - Divestitures/dispositions and amounts: Allstate employer voluntary benefits and group health
    "sold in 2025" (D01 L57, D02 L61, D03 L11, S5 (2), S17); gain (loss) on disposition of
    operations — | (7) | 720 | 890 | — (D03 S1) vs reconciliation "Gain on disposition" (6) | — |
    (723) | (893) | — (D03 S2; footnote on contingent consideration from the 2021 Allstate Life
    sale); D02 Q2 2026 (1), six months (7), Q2 2025 statement 890 vs reconciliation (893) (D02 L378,
    L421, L436). Travelers Canadian operations divested in Q1 2026: prior-year NWP Q1 2025 $223
    million (D08 L127; BI 67, B&SI 10, PI 146), Q2 2025 $273 million (D09 L124; 79, 16, 178), six
    months $496 million (D09 L144; 146, 26, 324); held for sale at December 31, 2025: assets 4,550
    and liabilities 2,542 (D10 L796, L809), invested assets $3,347 million (D08 L759; D10 L855,
    L930), fixed maturities $3,243 million (D10 L896), goodwill $208 million and intangibles $1
    million (D08 L709-710, D09 L769-770), reinsurance recoverables 285 (D10 L980), cash 171 (D10
    L1236); divestiture proceeds 2,384 (D10 L1212); Q1 2026 "Other" realized gains 70 (D10 L942,
    L966); reserves disposed inside "Foreign exchange and other" (1,658) (D10 L1049, L1064); PI
    International NWP 146 | 178 | 167 | 159 | — (D10 L642). Chubb and Progressive state none.
  - One-time, non-recurring and methodology items: Progressive June property "favorable 11.7 point
    impact related to an actuarial methodology process change ... one-time adjustment" (D07 L279,
    month table only); Travelers B&SI "non-recurring tax item" (D08 L231; D09 L279 YTD; B&SI tax 28
    vs 57, D08 L209, D10 L458); Chubb Life "non-recurring items that were favorable to the prior
    year" (D04 L665); Progressive March NPW timing "February 28 being reported in March 2026" (D06
    L399); Allstate Q2 underlying auto CR "benefited from 2.4 points of favorable development on
    claims reported in the first quarter of 2026" (D02 L119); Allstate Q3 2025 Run-off effect 1.0
    point (D03 S6); Travelers 3Q25 asbestos charge 277 (D10 L1055, L1082-1083).
  - Capital actions: Allstate Q1 "$881 million of cash ... through dividends and share
    repurchases" (D01 L221, no split), Q2 "$1.0 billion in share repurchases and $280 million in
    dividends" (D02 L252), "$3.5 billion ... over the last year" (D02 L21), dividends declared per
    share $1.08 in Q1 2026 vs $1.00 (D03 S1), treasury shares 640 / 642 / 646 million (D01 L289,
    D02 L321). Chubb Q1 repurchases $1.14 billion at $325.06 and dividends $380 million (D04 L390);
    Q2 $979 million at $327.18 and $395 million; six months $2.12 billion at $326.03, $775 million,
    total $2.90 billion (D05 L547). Progressive month-only repurchases: March 768,273 shares at
    $204.48 (D06 L375-376), June 845,952 at $201.16 (D07 L382-383). Travelers Q1 authorization
    repurchases 6.0 million at $300.30 ($1.800 billion) plus employee-related 0.6 million ($185
    million), capacity $5.215 billion (D08 L133; D10 L95-99); Q2 4.3 million at $304.06 ($1.311
    billion), capacity $3.915 billion (D09 L150; the capacity figures differ by $1.300 billion);
    cash-flow treasury stock (1,785) and (149), dividends paid (237) vs declared 238 (D10
    L1225-1227, L92); $1.25 quarterly dividend declared in each release (D08 L135: payable June 30,
    record June 10; D09 L154: payable September 30, record September 10). Only Travelers prints
    repurchase authorization capacity.
  - Hedge scope and qualifiers: D10 L1170 "Estimated and Preliminary" attaches to the March 31,
    2026 statutory column, while D08 L133 states $31.063 billion without it; Travelers
    "approximately 28.5%" (D08 L117, D09 L137); Chubb "CATs and FX aside" (D05 L372); Allstate D03
    S8 footnote (5) "could be significant" (D03 L27); Allstate equity declines "which have since
    recovered" stated as fact (D01 L213).
  - Figures that differ between locations (no document-stated precedence): Allstate BVPS
    denominator 260.8 (D03 S3) vs common shares 257.8 (D01 L52); Allstate unrealized on fixed
    income (220) (D03 S3) vs total unrealized (221) (D03 S4, D01 L431) and "$282 million
    (pre-tax)" (D01 L215); Allstate duration "5.7 years" (D01 L188) = D03 S13 derivative-inclusive
    row (plain 5.5); Allstate S6 vs S7 Q3 2025 ratios (Run-off); Allstate Protection Services ANI
    drivers D02 L160 vs L198; Chubb ex-large-account growth 7.7% (D04 L45) / 7.8% (L214) / 7.3%
    (L648); Chubb "North America was up about 0.5%" (D05 L371) vs 0.4% (L585) and "international
    life ... 14.4%" (L371) vs Life segment 14.4% (L79, L803); Chubb NII "up 12.3%" (D05 L83) vs
    printed 1,760 | 1,568; Chubb identical 1,937 for P&C UW income and Life NPW (D05 L423, L511);
    Progressive month OCI (1,025) vs pretax unrealized change (1,297) (D06 L112, L384); Travelers
    NII "+9%" after-tax vs "+8%" pre-tax (D08 L29, L123); Travelers December 31, 2025 reinsurance
    allowance $129 (D10 L783) vs (135) (D10 L979); Travelers debt 9,268 at March 31 (D08 L727, D10
    L806) vs 9,068 at June 30 (D09 L787), with D10 L1109 listing $200 million notes due April 15,
    2026 (no repayment statement in the bundle); Travelers adjusted-SE and ROE definition wording
    D08/D09 vs D10 (preferred stock, discontinued operations, "less preferred dividends").
  - Narrative/overview passages that repeat table results (rounded): Allstate opening quotes and
    bullets D01 L20-30, D02 L19-29; Chubb headlines and bullets D04 L25-73, L81, L203-214 and D05
    L25-87, L95, L222, L356-371; Travelers headlines and bullets D08 L14-33, L62-64, L110-123 and
    D09 L14-32, L63-64, L109-144. Progressive (D06, D07) and the supplements (D03, D10) have no
    results narrative.
  - Issuer vs mentioned organisations, actions vs mentions: Travelers Board "declared" dividends
    (D08 L135, D09 L154); Progressive dividends appear only as a risk-factor mention (D06 L466, D07
    L472); Allstate "higher dividends and increased share repurchases" (D01 L22) with the
    per-share dividend only in D03 S1; Travelers B&SI segment description still lists Canada (D08
    L312, D09 L374, D10 L1303) after the Canadian divestiture; Chubb names Huatai only as a source
    of consolidated investment-company cash flows (D04 L733).
  - Exclusion and negative facts: Allstate total PIF excludes divested businesses (D01 L57) and
    lender-placed policies (D03 S5); Chubb Global P&C excludes Agriculture and Life (D04 L720) and
    P&C UW income excludes Life (D04 L704); Travelers retention, renewal premium change and new
    business exclude National Accounts (BI) and surety (B&SI) and are domestic only (D08 L765, D09
    L825); Travelers ratios "Before policyholder dividends" (D10 L220); Allstate Health and
    Benefits segment no longer reportable from Q3 2025 (D03 L11); Progressive YTD supplement tables
    carry no TNC or methodology footnote (D06 L285, D07 L292).
  - Late list members: Travelers forward-looking topics end with "the war with Iran" (D08 L357,
    D09 L417); Progressive safe-harbor bullets end at D06 L474 / D07 L480; D10 top-five lists end
    with Fairfax Financial Group (L991) and John Hancock Group (L1005); D10 debt list ends with the
    5.70% notes due July 24, 2055 (L1129); D10 BI organisation list ends with Simply Business and
    Business Insurance Other (L1301); Allstate D03 S5 footnote (1) ends "All other reflects
    certificate counts for the individual health business".

## Gaps and continuation

- Reading coverage: all ten documents read in full (D01 L1-491, D02 L1-540, D03 L1-48, D04
  L1-1146, D05 L1-1473, D06 L1-483, D07 L1-489, D08 L1-790, D09 L1-850, D10 L1-1312 in four
  chunks). No unread ranges; no continuation chunk is needed.
- Source completeness: `notes/intake.json` reports every document complete (gap_characters 0);
  no missing source text identified.
- Not applicable: page counts and page-image checks (plain-text sources, no PDFs or images).
- Unresolved layout items (the original is the same flattened text, so no visual check is
  possible):
  - Progressive "Net catastrophe loss ratio" rows print five values under six column headers
    (D06 L251, L299; D07 L258, L306); the merged-cell assignment is not visible in text.
  - D03 S13 and S14: position of the Reciprocal Exchanges footnote markers ("(2)", "(3)")
    relative to the total-return rows.
  - Chubb tables (D04, D05) are one value per line; column assignment follows the printed
    sequence (2026, 2025, change, then the per-share block); row sums checked consistent.
  - D10: "(1)" is a footnote marker in the realized-gains "Other" row (L942) but a value in the
    NUI "Other" row (L961); row totals confirm both readings.
  - Pipe-table cells split numbers from "%" or labels (e.g., D01 L52, D02 L57, D08 L54, D08 L682);
    readable, but cell-spanning quotes may not match the platform text (capture-pipe-tables
    memory).
- Material referenced but absent from the bundle (not a reading gap): Chubb Financial
  Supplements (D04 L676, D05 L854); Allstate Q2 investor supplement; Travelers Q2 financial
  supplement; Progressive April, May and July monthly releases (D06 L403, D07 L409); 10-Q/10-K
  filings; Travelers pre-tax underlying underwriting income for 3Q25 and 4Q25 (scope of D08 L19
  "sixth consecutive quarter"); Chubb shares outstanding; repurchase authorization amounts for
  Allstate, Chubb and Progressive.
- Not inspected by this mapper: the platform capture's bundle-overview text (outside the
  active-bundle read scope); check it at sketch time for overview exposure.
