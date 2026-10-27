# aq-03143 - cross-document hooks

Written by the caller (claude), 2026-10-11. Doc numbers are the task page's (D04 = Doc 1, D02 = Doc 2, D01 = Doc 3,
D03 = Doc 4, D07 = Doc 5, D06 = Doc 6, D05 = Doc 7).

## Earlier measurements

No earlier bundle shares these bytes or this family (UK legal aid). Nearest family: UK consultation + impact
assessment + response bundles (aq-02086, aq-02102, aq-02147, aq-02157, aq-02220). There the low solver handled
response-rate joins, list intersections, dated bridges and single rule sentences; the one Medium was a value derived
from a rule beside printed same-label decoys (aq-02157 q04). Scenario totals passed Medium elsewhere only when the
parallel documents' rules interact (aq-02564 q02, aq-02486 q01) and Hard when a gate elsewhere in the document
decides the exception (aq-02562 q01). So priority goes to h1.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | Doc 1: escape thresholds (L293, L415, L556, L566), found nowhere else. Docs 1 and 3: fixed fees and hourly rates (annex tables). Doc 3: attendance at court with counsel at 75% (L475; £52.00 rows), Doc 4 states the 75% rule (L420) | What a stated bill pays under the final fees when the same hours escape one fixed fee (immigration legal help, twice) and not another (housing legal help, three times), plus an attendance fee the response changed | Calculate across documents; apply a rule to a case; same series, right edition (proposal vs final rate) | Wrong routes recomputed: all hourly, all fixed, one multiplier for both, proposed £34.65 | Inputs sit deep in long annexes (form number check will not find them); question about 35-40 words | sketches i01, i02 (phrase variant), i03 (London sibling) |
| h2 | Doc 1: 50% remote limit, Immigration 75% (L639-643); part-time office categories (L694). Doc 3: Q11 table (L639-683) | Total of the Q11 counts for categories under both the 50% limit and the full-time office rule (106) | Match, then exclude; aggregation | Skipping the immigration exclusion gives 152; the part-time side is 80 | Two-list joins were quick-test too easy on earlier bundles | sketch i04 |
| h3 | Doc 2: fee simplification "1% (£0.2m)" (L474). Doc 4: "1% (£0.3m)" (L513), 75% incorporated (L504-505) | Rise in the yearly cost of fee simplification once attendance moved to 75% (£0.1m) | Same series, right edition; calculate across documents | Headline £20m is unchanged in both, so the wrong routes are £0 and £0.3m | Both inputs rounded to £0.1m; two lookups and a subtraction | sketch i06 (spare) |
| h4 | Doc 5: "£115m p.a. at steady state, at our projected 2024/25 volumes" (L103). Doc 6 / Doc 7: barristers £31m - £39m (Doc 6 L164), 2024-25 column 39 | Barristers' share of the interim response's £115m (34%) | Calculate across documents; temporal alignment (volumes basis) | 31/115 = 27% mixes bases; 31/95 = 33% answers the 2019-20 basis | The top of the range pairs naturally with £115m | sketch i05 |
| h5 | Doc 1 Annex B vs Doc 3 Annex A: HPCDS rows (£108, £102) dropped, "no longer claimable" (Doc 3 L1509) | Which proposed increase was dropped and its amount | Silent change between proposal and final | HLPAS stage two rows carry the same amounts, so Doc 1 is replaceable by coincidence | Two-part answer; fails necessity | closed |
| h6 | Doc 1: "up to six months from the time the consultation response is published" (L578), "end of Autumn 2025" (L232). Doc 3: July 2025 | Latest month on the consultation's own estimate (January 2026) | Calculate across documents (dates) | not applicable | Plain dated bridge; this family of design was too easy before | held as a spare |
| h7 | Doc 5: £20m might go on fees, "including potentially prison law fees" (L242-246). Doc 6 / Doc 7 Table 7: prison law baseline 13 without disbursements, 18 with | Share of the £20m a 15% prison law uplift would take (about 10%) | Picking the right measure | 18-based route gives about 14% | A what-if the documents only half pose; round answer; boundary rounding at £0.1m | held |
| h8 | Doc 2 vs Doc 4 Table 1 licensed uplift 10% to 11%; Doc 4 para 50 still says 10% | Change in licensed-work uplift | Edition | Doc 4 contradicts itself | Two readings inside one document | closed |
| h9 | Doc 7 vs Doc 6: £97m to £95m, solicitors £58m-£66m to £55m-£63m (training grants out) | Like-for-like change | Edition, part vs total | Differences are rounding once grants are removed | No stable gold | closed |
| h10 | Doc 1 worked example £34.65 / 16% vs Annex B and Doc 3 £39.35 / 31% for Higher Courts travel | Final higher-court travel rate | Exact table vs prose | Answer sits in Doc 3 alone; Doc 1 contradicts itself | Single-document answer | closed; keep this cell out of every sketch |

Search coverage for substitutes: "escape" appears with a multiplier only in Doc 1 (Docs 2 and 4 mention a "lower
escape multiplier" without a number; Docs 6 and 7 say "approximately three times" for police station work). "75%"
for attendance appears in Docs 3 and 4 only. The Q11 table and the part-time category list each appear once.
"£0.2m" appears in Doc 2 only, "£0.3m" in Doc 4 only. "£115m ... 2024/25 volumes" as one statement is in Doc 5 only.

## Measured results on these bytes

Run 1, q01 rev 0 (h1), 2026-10-12, capture verdicts/AQ-03143_difficulty_2026-10-12_1221.txt: "In band — Easy tier",
Low 2/5. Routes below are read from each attempt's own Full answer and Reasoning (wrong attempts in full, lines
668-965, 1211-1471, 1472-1710; the every-document attempt, lines 1715-2103; right attempts searched for the
attendance step). Each low Reasoning block is loaded but stops mid-sentence where the page cut it.

| Attempt | Committed | Where it left the gold |
| --- | --- | --- |
| Low 1, Low 3 | £1,032.50 | nowhere: both read the single "£52.00 +" row as a national rate |
| Low 2, Low 4 | £1,023.50 | attendance only: saw "£52.00 +", worked out that it is 75% of the London rate, then paid 75% of the non-London £65.35 (£49.00) because the question says outside London |
| Low 5 | £980.45 | attendance only: paid £34.65, the 50% row, reading the consultation's proposed rate into the response's table |
| High, every document | £1,032.50 | nowhere, after weighing £49.00 against £52.00 at length (single current rate, single new rate) |
| High, without Doc 3 (two) | £1,023.50 | 75% of £65.35 from Doc 4's rule: the printed £52.00 is only in Doc 3 |
| High, without Doc 1 (two) | £687; £1,454.00 | both fixed fees, or both by the hour: no threshold without Doc 1 |
| Closed book | £473 | recalled "three times" for both matters and wrong fees |

What it shows:
- The escape rule separated nobody: 5 of 5 low attempts applied three times to housing and twice to immigration,
  including the unprinted £634. The quick test had already solved the bare case (i01) and the London case (i03).
  A stated rule with printed inputs is not a gate on this bundle, however many matters it is applied to.
- All three misses sit in one £156 cell. Two are a table-against-rule choice (M1), one a proposal-against-final
  row (M2). M1 is a choice an attempt makes once, not a slip per cell: the two right attempts stated "applies
  nationally". Repeating the cell would not compound it.
- The document check passed for both ticked documents; Doc 4 did not stand in for Doc 3.

Round 2 therefore keeps the one cell that separated solvers, keeps one escape matter only as Doc 1's anchor, and
adds independent gates of a different kind: which work the increase reaches at all (h11, h12).

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h11 | Doc 3 L188 and Doc 1 L586: increases apply to "new certificates or determinations" after commencement. Doc 1 L554-556: current housing legal help fee £157, rate £45.95, threshold three times | A matter opened in 2024 stays on the current fee: 10 x 45.95 = 459.50 < 471, so £157 | Conditional filter; right edition (current vs final) | New fee £223 (+£66); new rate against the old threshold, £653.50 | Year must clearly precede commencement (response July 2025) | sketches i07, i08 |
| h12 | Doc 1 L531 and footnote 24: Table 10a rates rise for housing or immigration work only; Doc 3 L1596: table 10(a) remains for other work. Current lower-courts attendance £29.25 (Doc 1 L1547, Doc 3 L1716) | County court attendance in a discrimination case stays at £29.25 | Wrong scope (mentions vs does) | £52.00 applied to it (+£68.25 on 3 hours) | Table 10(b) prints £28.80 and its use is not explained; both documents tie other categories to Table 10(a) | sketches i07, i09 |

Run 2, q01 rev 1 (h1 + h11 + h12), 2026-10-12, capture verdicts/AQ-03143_difficulty_2026-10-12_1644.txt: "Too easy",
Low 5/5 (no Medium or High level, no document check). Read from each attempt's Full answer (lines 415-1594) and the
reasoning lines on the attendance rate:

| Attempt | Committed | Where it left the gold |
| --- | --- | --- |
| Low 1-5 | £1,054.25 | nowhere. Each put the 2024 matter on the old fee (459.50 < 471), escaped the immigration matter (653.50 > 634), paid housing attendance at £52.00 and discrimination attendance at £29.25 |
| Closed book | £1,456.81 | no document figures |

What it shows:
- The commencement gate (h11) and the scope gate (h12) stopped nobody. With the escape rule from Run 1, every
  stated-rule gate tried on this bundle is cleared by the easier solver, flagged or not.
- The attendance cell where three of five attempts went wrong on rev 0 stopped none on rev 1. Attempts 2 and 3
  again worked out that £52.00 is 75% of the London rate and that the non-London rate would give £49.01; attempt 2
  then noted the current £29.25 is a single rate, attempt 3 cross-checked the single travel rows, and both kept the
  printed figure (only these two reasoning passages were read; the other three were read as Full answers).
  Author's reading, not shown by the traces: the discrimination item sends the solver to the same row's current
  rate, which may have made the single national rate plain. Five attempts each way, so chance is not excluded.
- Attempt 4's extra sentence on VAT drew the "may be too vague" advisory; it was graded right.

Decision: h1, h11 and h12 are retired. Two measured versions, Easy then Too easy; a third version of the same bill
would be a wording ladder. No untested hook on this bundle has a measured miss behind it: i06 (two lookups and a
subtraction), h6 (dated bridge) and h7 (a base choice the solver's table reading settles) are all shapes this
solver handled here or on earlier bundles. Release recommended.
