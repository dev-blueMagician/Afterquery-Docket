# aq-04874 - document map

Maintained by the caller from `text/` (and `docs/` for layout issues). Navigation only, like the form's
bundle overview: where things are, not what to ask. Questions quote the documents, never this map.

## Bundle

- What it is: "Industry research" set of five Australian housing / household-debt texts: two RBA Research
  Discussion Papers (2020, 2023), two RBA Bulletin articles (Oct 2024, May 2026) and the Treasury's NCC
  Modernisation Project interim report (30 April 2026). 80,087 prompt tokens.
- Documents: 5. Local ids are alphabetical by file name and differ from the task page's Doc numbers:
  D02 = Doc 1, D05 = Doc 2, D01 = Doc 3, D03 = Doc 4, D04 = Doc 5 (notes/intake.json).
- Gaps: none. Capture 2026-10-14 12:17 says "Documents: 5 of 5 read in full (343,606 characters)"; every
  intake record `incomplete: false`, `gap_characters: 0`, `matches_capture: true`. The capture carried the
  page's "Docket has been updated. Reload this page ..." notice (form state only; documents complete).
- Extraction spot-checks: plain-text captures (no PDFs, no page counts). Checked per document: D01 Table A.1-A.4
  and endnotes; D02 Tables 1-4, A1, A2, B1 and footnotes 24-47; D03 Table 1 and endnotes 1-13; D04 Table 1
  and case-study boxes; D05 Tables 1-4, D1 and footnotes 1-15. Charts are flattened into label strings
  (values unreadable) in all four RBA texts; several tables are column-scrambled (see per-document notes).
- Provenance: notes/intake.json (capture_sha256 7345db24...), source hashes per document there.
- Reuse binding: new bundle, all mapped from the current source hashes (2026-10-14).
- Repeat check (2026-10-14): no document shared with any bundle in 10.6, 10.7, 10.8 or docket-capture.

## D02 = Doc 1 - RBA RDP 2020-05 "How Risky is Australian Household Debt?"

- Written by: Jonathan Kearns, Mike Major, David Norman (RBA Financial Stability Department), August 2020.
- Period: cross-country panel of 22 advanced economies 1980-2018; stress tests on ABS SIH 2015-16 (17,768
  households), SIH-HES matched 10,046 households; time comparison 2003-04, 2009-10, 2015-16.
- Tables: Table 1 descriptive stats (l.295-386, columns scrambled: means/sd/min/max lists); Table 2 regression
  (l.415-586, narrow/wide/all-countries columns as separate lists); Table 3 robustness (scrambled); Table 4
  stress scenario (l.967-994): employment -8, investment income -30, bonus/overtime -50, lending rates 0 ppt;
  housing -40, equities -40, super and trust funds -30 (note a: average, depends on age profile), other 0.
  Table A2 sample starts (l.1481-1538; (a) not in narrow regression, (b) not in narrow or wide). Table B1 probit.
- Rules and assumptions (Section 3): default if financial margin negative and LVR at default above 90 per cent
  (l.1017, fn 24); current LVR under 90 self-cures; foreclosure costs 10 per cent of the loan (l.1040); LMI
  assumed for LVR currently above 80 per cent, payout ratio 70 per cent (fn 30, l.1058); personal/credit card
  debt repays 2 per cent of principal a year (l.1036); minimum consumption = HEM (HPL in 2003-04, l.1272);
  superannuation counted only if household head over 40, vested linearly until 60 (l.1114); hand-to-mouth =
  liquid wealth below half of income each pay period, MPCy 1 (l.1266); MPCw 3 cents (housing 2.5, financial 5),
  MPCy 55 cents (l.1139-1141); 2003-04 comparison: bonuses/overtime do not fall (l.1272).
- Results: debt-at-risk 0.8 -> 2.1 per cent of housing debt; consumption falls 12 (uniform), 11 (Yao), 12.5
  (age-varying; Hviid-Kuchler fn 43), 17.8 (larger MPCs), ~0.5 ppt below baseline (hand-to-mouth); 10.8 / 11.0 /
  11.5 per cent for 2003-04 / 2009-10 / 2015-16 (fn 47 constant MPCs: 9.6 / 10.8). DTI +125 ppt 1988-2018;
  +30 ppt 2003-04 to 2015-16. Less than 10 per cent of new Australian loans above 90 per cent LVR.
- Coverage: full read by the caller.

## D05 = Doc 2 - RBA RDP 2023-01, credit constraints and housing prices (survey experiment)

- Written by: Tom Cusbert (RBA Economic Research Department), January 2023.
- Data: Fuster and Zafar (2021) US SCE survey, 2014: 20% down payment / 6.5% rate baseline; 5% minimum down
  payment; 4.5% rate; US$100K inheritance (l.284-302). Michigan example: five households, US$140,000 homes,
  WTPs US$40,000-200,000; average change US$28,000, marginal US$10,000 (l.184-189).
- Tables: Table 1 log changes (l.373-396): collateral 0.16 / 0.06 / 0.10; rate 0.04 / 0.05 / 0.00; inheritance
  0.11 / 0.07 / 0.04. Table 2 by home-value quintile (l.450-518). Tables 3-4 OLS fits and coefficients. Table D1.
- Rules: normalised WTP = WTP / home value; WTP equal to home value excluded; 5 per cent trim (Table 1 note);
  down payment binding if wealth available for a deposit is below 20 per cent of home value (Figure 6 note a).
- Australia (Section 9.4, l.971-1017): SIH 2003/04-2019/20, biennial, 2007/08 omitted (fn 14); 15 ppt loosening;
  home ownership 72 per cent (2003/04) -> 69 per cent (2019/20). Spain/Switzerland highest/lowest OECD home
  ownership (l.1025). GE multiplier, alpha 0.72, around 15 per cent (l.1089). LTV tightening -1.5 per cent after a
  year, -8 per cent over four years (Richter et al, l.259-260). Before-tax 5.5 / after-tax 3.6 per cent (l.631-633).
- Coverage: full read by the caller.

## D01 = Doc 3 - RBA Bulletin, October 2024: interest costs and rents

- Written by: Declan Twohig, Anirudh Yadav, Jonathan Hambur (RBA). Date only in the file name (body has none).
- Data: every investor filing a personal tax return 2006/07-2018/19, annual (l.75); SA4 = local housing market.
- Figures: median monthly interest payment for leveraged investors up around $850, April 2022-January 2024
  (Securitisation Dataset, endnote 5); 1 cent per dollar on average (less than $10 a month, ~0.4 per cent of
  median monthly rent, January 2024); biggest 3 cents (~$25 a month, ~1 per cent). One-third of households
  rent; median renter 25 per cent of disposable income on rent in 2022.
- Rules: windows (Table A.1, l.389-414; text l.419-421): narrow rent growth [-10, 30] per cent and interest growth
  within +/-5 ppt of the indicator-rate change; medium lowers the interest floor to -15; wide [-50, 50] both;
  non-mortgagors kept even outside the windows (Table A.1 note a). Graph 5 note misprints the narrow floor as
  "below 10 per cent" (l.275). Rising-rate years 2008/09, 2011/12, 2017/18, 2018/19; not rising 2009/10 and
  2012/13-2016/17 (2007/08 and 2010/11 unclassified) (l.275, l.289-293). IV imputes debt = interest / rate (l.463).
- Tables A.2-A.4 (l.488-654) scrambled; observations 2,795,198 / 3,683,960 / 6,785,979.
- Coverage: full read by the caller.

## D03 = Doc 4 - RBA Bulletin, May 2026: new data on housing investors

- Written by: Alexandra Michielsen (RBA Financial Stability Department).
- Data: ABS PLIDA-WHAM rental property schedules, 1999/2000-2022/23, individuals only (endnote 1: partnerships
  and trusts excluded; foreign rental property excluded); 2021 Census household leverage; latest two FYs missing.
- Figures: 2.3 million individual investors 2022/23 (~10 per cent of working-age population); investment
  properties ~20 per cent of dwelling stock (endnote 3 on scope); 70 per cent one property, 30 per cent several
  holding ~half of all investment properties; multi-owner share +7 ppt over two decades; 80 per cent same state,
  30 per cent same SA3 (8 per cent of all investors); median age 45 -> 51; over-60 share 12 -> 28 per cent (40 per
  cent of change from population ageing); top income quintile nearly 40 per cent (Graph 5 quintiles: full
  income-tax distribution); ~80 per cent leveraged; 2021: ~20 per cent of leveraged investors DTI above 6
  (RBA/APRA higher risk); both-type households ~70 per cent of DTI>6 households.
- Table 1 (l.568-618, scrambled; order fixed by text l.554-556): single/no OO $224,000, DTI 1.6; single/OO
  $655,000, 4.1; multiple/no OO $498,000, 3.2; multiple/OO $1,054,000, 5.9 (prose: "around $220,000",
  "a median of $1 million"). Graph 10: top quintile ~$720,000, bottom ~$300,000; endnote 13 investor-household
  quintile thresholds Q1 < $78,000 ... Q5 > 234,000.
- Rules: leverage = interest expenses / interest rate x 100 (Appendix A); 30-year term; residence after
  1 January 2006; fixed-rate share 17 per cent; investor household = a member filed a rental schedule; local
  area = SA3 (359 SA3s); endnote 11: since 2018 ~40 per cent of new investor lending interest-only (OO 8-12).
- Coverage: full read by the caller.

## D04 = Doc 5 - Treasury, NCC Modernisation Project Interim Report, 30 April 2026

- Written by: The Treasury (three project leads named). Figures: Accord target 1.2 million homes, period ends
  mid-2029; NCC 2022 energy changes ~$185 a year; $50m Housing Support Program; 26,000 homes; $120m National
  Productivity Fund; consultation 6 workshops (42 participants), 21 discussions (7 with ABCB), 213 submissions;
  CIE ~$300m a year, about half realised; state variations ~600 pages (NCC 2022); Victoria 115 -> 60
  variations, 29 pages, from 1 May 2026; waterproofing 20-40 per cent of apartments, BCR 4.3 / 4.9, $306m + $4m,
  ~$1.3b avoided (2025-2034); 10-year approval; reforms every five years with 12-month implementation.
- Coverage: full read by the caller. No link to the RBA texts beyond the housing-supply theme.

## Shared ground (navigation only)

- No document cites, amends or responds to another bundle document (author and reference lists checked).
- People: Hambur (Doc 3 author) and Cusbert (Doc 2 author) co-wrote MARTIN (2019), cited in Doc 1; Yadav (Doc 3
  author) is thanked in Doc 2; Hambur co-wrote Bradshaw et al (2025), cited in Doc 4. Agarwal, Gao and Garner
  (2023) is cited by Doc 3 and Doc 4.
- Data overlap: ABS SIH in Doc 1 (2003-04, 2009-10, 2015-16; 2017-18 mentioned) and Doc 2 (biennial 2003/04-2019/20,
  no 2007/08); investor tax data in Doc 3 (2006/07-2018/19) and Doc 4 (1999/2000-2022/23); F5 rates in Doc 3 and
  Doc 4; securitisation data in Doc 3 ($850) and Doc 4 (17 per cent fixed share, rate benchmark).
- Same label, different definitions: "local housing market" = SA4 (Doc 3) vs SA3 (Doc 4); DTI = aggregate debt to
  disposable income (Doc 1) vs household housing debt to gross income (Doc 4); "ownership of housing" = share
  of dwellings owned by households (Doc 1) vs home-ownership (owner-occupier) rate (Doc 2); investor debt
  imputed from interest at the indicator SVR (Doc 3) vs a 17 per cent fixed-weighted discounted rate (Doc 4).
- Ages/thresholds: super counted from 40, fully at 60 (Doc 1) vs investor median ages 45 and 51 (Doc 4).
- LVR/deposit: Doc 1 LMI above 80, default above 90 per cent LVR vs Doc 2's 20 per cent / 5 per cent deposits.
