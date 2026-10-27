# aq-02626 - cross-document hooks

Target: medium (user 2026-10-10: "there is no slot for Easy Tier for this bundle, we should target medium and
high. do your best."). Same six documents as aq-02483, byte for byte, so that bundle's inventory h1-h12 and its
measured results carry over: [aq-02483 hooks](../../aq-02483/notes/hooks.md), [ideas](../../aq-02483/notes/ideas.md).
Locations are text/DNN lines (D0N = Doc N).

## Closed on aq-02483 (measured on the platform, 2026-10-09)

- Newest federal amendments in Wyoming's and Wisconsin's adopted versions, 76 days: quick test too easy.
- Legacy-added definitions still federal, Wyoming minus Virginia, 3: quick test too easy.
- Wisconsin's landfill deadline vs Wyoming's impoundment deadline, 28 weeks: quick test survived, difficulty
  Run 1 Too easy, Low 5/5 (the Wyoming rule names its own missing input).
- Untested there and still weaker: approved-list differences (h1), "Infiltration" landfills (16), deadline gaps.

## New hooks (caller, 2026-10-10, after re-reading every State-specific section)

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h13 | D02 L220-L221 (two comment periods; each to 30 days after the second weekly notice; labelled "30-day" at L205, L218); D03 L195 (at least 45 days; hearing at least 30 days after notice; comment at least 15 days after the hearing) | Public-comment days a new permit gets in Wyoming (74 with notices a week apart) against Virginia's minimum (45, or 55 with a hearing on day 40) | Calculate across documents; Scatter the pieces | Labels 60 and 45 give 15; Wyoming label with Virginia rule 5; Wyoming rule with Virginia label 29 | Both rules are stated in the sentences beside the labels; the gap between notices must be stated in the question | q01 (i01) quick test too easy 2026-10-10: closed; i05 dropped untested |
| h14 | D05 L276 (awarded $1,069,479; anticipated $203,390; "total of $1,272,869"), L397-L398 (permits for facilities (1)-(8)); D03 L226 (8 facilities, $571,396.00), L329 (all units permitted) | STAG funding per permitted facility, Alabama minus Virginia: $62,260 | Scatter the pieces; Calculate across documents; State the rounding | Alabama's larger total gives $87,684 | Derived ratio the documents do not print; Alabama's count exists only as a list | q02 (i03) quick test too easy 2026-10-10: closed |
| h15 | D02 L278 (chapter 18 effective August 19, 2022), L127 (six amendments, last November 8, 2024); D03 L119, D04 L122, D05 L127, D06 L126 (seventh amendment, February 10, 2026) | Days from Wyoming's chapter taking effect to EPA's latest amendment as of September 2026: 1,271 | Same series, right edition | Wyoming's own list gives 812 | The newer date is in four of five proposals; day-count reasoning needs printed operands | sketch i02, quick test first |
| h16 | Funding sentences D02 L268, D03 L226, D04 L291, D05 L276, D06 L294 | Total STAG funding already received or awarded in the five States: $4,033,152 | Scatter the pieces; Calculate across documents | Alabama's larger total gives $4,236,542 | One same-sentence trap; a stated sum measured too easy on aq-02405 | i04 dropped untested (same Alabama choice as q02) |
| h17 | D02 L221 (two weekly insertions per period, two periods); D04 L217-L221 (three notices, each in the State journal and a local newspaper unless in the journal's parish) | Notice insertions for one new permit: Wyoming 4, Louisiana 6 | Calculate across documents | One per stage gives 5 | Counting convention (journal vs newspaper, who publishes); small integer | hold |
| h18 | D03 L195/L220 (permit comment 45 days, settlement comment 30); D04 L225/L276 (permit comment 30, settlement comment 45) | Mirrored permit and settlement comment periods | Who belongs where | Swapped pair gives the same 15-day gap with the other State named | Each figure is a keyword hit ("settlement") | reject (lookup) |
| h19 | D02 fn 3 L138, D03 L132, D05 L137 (180-day clock starts at EPA's completeness determination); D05 L184 (July 2026), D06 L181 (September 2026) | When the statutory review period began for a State | Scatter the pieces | Application date as the start | Only a month is printed, so no exact date or day count | reject (answer the documents only bound) |
| h20 | Penalties D02 L252, D04 L269-L270, D05 L265, D06 L266-L268 | Maximum penalty for one multi-day violation across States | Rule application | Per-violation read as per-day | Alabama's sentence is silent on days; Louisiana's two rates may or may not stack; "environmental violations" undefined | reject (fairness) |
| h21 | D05 L216-L219 (modification classes); D03 L198; D06 L204-L209 | Comment required for one stated modification in two States | Definitions gate | Minor read as no notice | Only Alabama lists classes; Wisconsin's periods conflict (60 vs 30 days, L217 vs L228) | reject |
| h22 | Approved-as-State-version lists D03 L246-L272 (item 9), D04 L316-L338 (item 9); D05 L337-L339 (same entry under "are not being approved"); D06 L310-L320 (11 items, entry absent); D02 L282 (no Legacy amendment sought); impoundment counts D03 L226, D04 L290 | Impoundments in States where EPA approves the State's version of "contains both CCR and liquids": 18 + 6 = 24 | Mentions it vs does it; Match, then exclude | Alabama's identical entry: 37; Wisconsin added: 27 | Phrase search finds all three entries; the list heading sits two lines above Alabama's | sketch i06 (round 2) |
| h23 | Publication dates (L3 of D02-D06) and comment deadlines (DATES, L27/L32); "60-day public comment period" in every SUMMARY | Days from publication to deadline: 62, 63, 60, 62, 60 = 307 | Exact table vs rounded prose; Calculate across documents | Label gives 300 | Plain date arithmetic once the dates are used | sketch i07 (round 2) |
| h24 | Permit duration D03 L190 (life of the facility), D02 L204 (operating life through post-closure), D06 L192 (no expiration; plan updated every 10 years), D05 L208 (design life, no longer than ten years), D04 L194/L202 (active life; maximum of 10 years); landfill counts D02 L267, D03 L226, D06 L290 | Landfills where the CCR permit has no set expiry: 7 + 3 + 6 = 16; or renewals over 25 years in Alabama, Louisiana, Wisconsin: 4 | Mentions it vs does it; Scatter the pieces | Wisconsin's ten-year update read as a term: 10, or 6 renewals; "design life"/"active life" read as no expiry: 19 | Each duration is one plain sentence; Wyoming's chapter 18 permits not yet issued | sketches i08, i09 (round 2) |

Round 1 result (user, 2026-10-10): q01 (h13) and q02 (h14) both quick-test too easy; both hooks closed, with i05 and
i04 dropped untested as weaker forms of the same paths. Round 2 adds h22-h24 and still holds h15 (i02).

The map is navigation; quotes come from text/DNN.txt. A short valid calculation or ID join is
eligible. Prior failures suggest tests/priority, not a universal veto.

Independent authors were not dispatched this round: aq-02483's caller and two independent authors already
inventoried these bytes on 2026-10-09 (returns in its hooks.md). This round re-read the procedure, enforcement and
resources sections against the two mechanisms measured since then (aq-02486 Medium, aq-02562 Hard).
