# aq-03143 - document map

Navigation only, written by the caller (claude) on 2026-10-11 from `text/`. Questions quote the documents,
never this map. Local ids are alphabetical by file name and differ from the task page: **D04 = Doc 1, D02 = Doc 2,
D01 = Doc 3, D03 = Doc 4, D07 = Doc 5, D06 = Doc 6, D05 = Doc 7.**

## Bundle

- What it is: two unrelated Ministry of Justice fee exercises. Civil (2025): the consultation "Civil legal aid:
  Towards a sustainable future" (Doc 1), its impact assessment (Doc 2), the government response CP 1333 (Doc 3) and
  the response-stage impact assessment (Doc 4). Criminal (2022): the interim response to the Criminal Legal Aid
  Independent Review consultation (Doc 5), its final impact assessment (Doc 6) and the consultation-stage impact
  assessment (Doc 7).
- Documents: 7; ids from `text/manifest.json`.
- Gaps: none. Capture says "7 of 7 read in full (449,815 characters)"; every `gap_characters` is 0. The capture
  carries the page's reload notice ("Docket has been updated. Reload this page...") only.
- Extraction spot-checks: plain-text capture, no pages. Compared captured bodies with `docs/` (hashes match in
  `notes/intake.json`). Tables are flattened: labels, current rates, uplifts and new fees sit in separate blocks in
  row order (checked on Doc 3's Q11 table, whose printed percentages reproduce count/83 row by row, and on Doc 1 /
  Doc 3 rate annexes, where rate blocks follow the activity blocks in order). Footnotes present as numbered lines.
- Provenance: `notes/intake.json`, capture sha256 3015eb12...; one capture, no history.
- Reuse binding: text hashes in `text/manifest.json` (D01 a7698c41..., D02 75081cd8..., D03 92be9551...,
  D04 ff5cb1f5..., D05 6d2b8336..., D06 547ba50f..., D07 cbeaf85c...). No earlier bundle shares these bytes.

## D04 = Doc 1 - Civil legal aid: Towards a sustainable future (consultation, CP 1268)

- Written by: Ministry of Justice; foreword Sarah Sackman KC MP. Originally laid January 2025, re-laid February 2025.
- Dates: consultation 24/01/25 to 21/03/25 (L52), "eight weeks" (L232); response "due ... Spring 2025" (L75);
  implement "by the end of Autumn 2025" (L232); "up to six months from the time the consultation response is
  published" (L578); Immigration first (L578).
- Rules: minimum hourly rate £65.35/£69.30 non-London/London, else +10% (L217-218, L519); fixed fees uplifted by
  the underlying rate's percentage, national fees take the higher uplift (L564, L872); rounding to 5p / £1 (L551);
  travel and waiting and attendance at court or conference with counsel at 50% of the preparation rate (L527,
  L594-595); letters and calls harmonised at the highest rate (L603-609); "from 77 to 45" rates (L611).
- Escape mechanism (only here in the bundle): "two or three times the fixed fee" (L293); 2023 immigration change,
  legal help threshold "twice the value of the fixed fee" (L415); housing legal help "three times", £669 (L556);
  asylum legal help "two times", £1,118 (L566). Housing legal help £157 "broadly equivalent to 3.5 hours" (L297, L318).
- Worked examples L553-566, L597-599, L605-609. **Conflict:** the travel example (L598-599) gives £34.65 and 16%
  for Higher Courts travelling and waiting; Annex B (L1542, L1717) and Doc 3 give £39.35 and 31%. Avoid that cell.
- Percent uplifts in prose: overall spend +24% Housing & Debt, +30% Immigration (L185); "30% to Immigration fees,
  21% for Housing fees, 16% for Debt fees, and 42% for HLPAS fees" (L550); £20m (L185, L551).
- Chapter Two (contract rules, only here): remote applications "must not exceed 50%" (L639), Immigration 75% since
  August 2024 (L643); office open "seven hours a day, from Monday to Friday" (L693); part-time presence for
  Claims Against Public Authorities, Clinical Negligence, Community Care, Discrimination, Education, Public Law (L694).
- Annex A (L822-909): benchmarking, £60 / £67, utilisation 70-80%, 1,200-1,300 hours = 71%-77%, 30 housing providers
  = 13-14% of the market, 17 family providers.
- Annex B (L913-1735): proposed rates. Controlled immigration hourly (L917-1082), immigration fixed fees
  (L1084-1356), housing controlled hourly (L1358-1430), housing fixed fees incl. two HPCDS rows (L1432-1510),
  licensed 10(a)/10(b)/10(c) (L1514-1619), Schedule 2 (L1621-1735). Legend: * 50% of preparation, # highest rate.
- Coverage: read in full except Annex B L1014-1082 and the questionnaire repeat, which were read for structure.

## D02 = Doc 2 - Impact assessment, consultation stage (IA MoJ015/2024, 24/01/2025)

- Option 1 cost £20m a year (Low £18m, High £22m). Table (L476-521): Housing & Debt baseline £25m, cost £6m,
  controlled 42%, licensed 10%, overall 24%; Immigration £47m, £14m, 32%, 10%, 30%; both £72m, £20m, 34%, 10%, 28%.
- Method: baseline = final bills 2023-24, excl. disbursements, incl. VAT (L434-436); immigration re-valued for the
  1 April 2023 escape multiplier, "+ around £4m" (L448-450); intermediate floor £59.40/£63 then +10% (L452);
  fee simplification "1% (£0.2m)" (L474); controlled rates rise "between 10% and 43%" (L396).
- Sensitivity tables L579-616 and L624-660.
- Only here (and Doc 1): "8 housing and debt areas with no direct provision and 5 HLPAS gaps" (L284).
- Coverage: read in full.

## D01 = Doc 3 - Consultation response (CP 1333, July 2025)

- 101 responses (L156, L199); sector split 34% / 31% / 15% / 4% / 4% / 1%, 12% unspecified (L199); four roundtables.
- Decision: attendance at court or tribunal or conference with counsel raised "from 50% to 75%" (L173, L475, L775);
  everything else as consulted; Immigration first (L444, L779).
- Per-question tallies L245-756: Q1 94, Q2 97, Q3 94, Q3a 92, Q4 94, Q5 94, Q6 95, Q7 91, Q7a 55, Q7b 47, Q8 88,
  Q9 93, Q9a 53, Q9b 61, Q10 81, Q11 83, Q12 90, Q13 86, Q13a 51, Q14 64. Percentages exclude non-answers (L243).
- Q11 table (L641-683): Immigration and asylum 46, Housing and debt 42, Public law 29, Family (private) 21, Welfare
  benefits 19, Community care 18, Family (public) 17, Claims against public authorities 12, Discrimination 10,
  Mental health 7, Clinical negligence 6, Education 5; "% of responses" on 83.
- Other spending: £1.4m (2024), £1.7m (2025) accreditation; £1.5m trainee housing solicitors (L431).
- Annex A updated tables (L795-2091), same order as Doc 1 Annex B plus a "New table" column. Differences from Doc 1:
  eight attendance rows now at 75% (£59.05, £52.00, £49.00; legend "+" L2087) and the two HPCDS rows removed
  ("Table 6 ... will be deleted as the fee is no longer claimable", L1509). No mention of escape thresholds.
- Coverage: L150-795 and the licensed/Schedule 2 tables read in full; controlled tables L800-1400 read for the
  rows used and compared with Doc 1 by amount multiset (script, 2026-10-11).

## D03 = Doc 4 - Impact assessment, response stage (02/07/2025)

- Same structure as Doc 2. Changes: attendance "75% of the relevant preparation rates" (L420, L426, L504-505);
  licensed uplift 11% in Table 1 (L527-561) while para 50 still says 10% (L581); fee simplification "1% (£0.3m)"
  (L513); sensitivity rows +£9m, £30m, £20m, £22m where Doc 2 has +£8m, £29m, £19m, £21m (L629-656, L678-706).
- Coverage: L90-752 read in full; the summary sheet above it mirrors Doc 2.

## D07 = Doc 5 - Government's interim response on criminal legal aid (20 July 2022)

- 203 responses (L65); 15% uplifts, PCE scope, ENP abolition; SI in force 30 September 2022 (L89-91, L222, L272).
- Money: "£115m p.a. at steady state, at our projected 2024/25 volumes", further £20m, total £135m (L103).
- Question tallies L115-176 (counts with percentages). Not uplifted: prison law, PPE and trial-length payments.
- Coverage: read in full.

## D06 = Doc 6 - Criminal impact assessment, final (20/07/2022)

- Cost £95m - £115m (2019-20 / 2024-25 volumes); Crime Lower £41m - £44m, Crime Higher £54m - £69m; solicitors'
  firms 9% or £55m - £63m; barristers 15% or £31m - £39m; experts £9m - £11m; "43% ... Crime Lower and 57% on Crime
  Higher (based on 2019-20 volumes)". Training grants excluded (L253).
- Footnotes on revised data: barristers £31m "changed from the £30m" (L883); Crime Lower 36 "was £37m" (L1115);
  quarterly expenditure footnote 7 (Q1 £175m, Q2 £186m, Q3 and Q4 about £200m, 2019/20 average £210m).
- Rounding rule for estimates (as Doc 7 para 54). Tables include or exclude disbursements as their notes say.
- Annex C (L2050-2094, only here): median AGFS income £46,200 to £53,100, "£7,000".
- Coverage: summary, the passages that differ from Doc 7 (sentence diff, 2026-10-11), L1118-1147 and Annex C read;
  the rest is parallel text to Doc 7, which was read in full.

## D05 = Doc 7 - Criminal impact assessment, consultation stage (14/03/2022)

- Cost £97m - £115m including £2.5m training grants (£2m trainees, £0.5m higher rights); solicitors' firms
  £58m - £66m; barristers £30m - £39m; "42% ... Crime Lower, 55% on Crime Higher and 3% on other grants".
- Tables 1-15 and Annexes A-B (LGFS distribution, firm characteristics). Prison law baseline 18 with disbursements
  (Tables 2, 6), 13 without (Tables 3, 7). Scenario C total 92 (Doc 6: 89).
- Coverage: read in full.

## Shared ground (navigation only)

- Proposal to final, civil: Doc 1 Annex B vs Doc 3 Annex A (attendance 50% to 75%; HPCDS rows dropped).
- Edition pairs: Doc 2 vs Doc 4 (four cost cells, licensed 10% to 11%, £0.2m to £0.3m); Doc 7 vs Doc 6 (training
  grants out, small data revisions that Doc 6 footnotes).
- Rule in one document, data in another: Doc 1's contract rules (remote limit, office hours, part-time categories)
  against Doc 3's Q9-Q14 tallies; Doc 1's escape thresholds against the fees and rates both annexes print; Doc 5's
  £115m / £20m / £135m against the volumes columns of Doc 6 and Doc 7.
- Repeated facts: £65.35/£69.30 and £20m in Docs 1-4; RoCLA survey figures in Docs 1, 2 and 4; fee and rate rows in
  Docs 1 and 3; nearly every criminal cost figure in both Doc 6 and Doc 7.
- No link between the civil and criminal families beyond the department.
