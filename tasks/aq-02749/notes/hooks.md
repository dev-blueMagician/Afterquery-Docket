# aq-02749 - cross-document hooks

Target: medium (user 2026-10-10: "there is no slot for Easy Tier for this bundle, we should target medium and
high. do your best."). The six documents are byte for byte those of aq-02483 and aq-02626, so their inventories
(h1-h24) and measured results carry over: [aq-02483 hooks](../../aq-02483/notes/hooks.md),
[aq-02626 hooks](../../aq-02626/notes/hooks.md), [aq-02626 ideas](../../aq-02626/notes/ideas.md).
Locations are text/DNN lines (D0N = Doc N).

## Closed on the same bytes (measured on the platform, 2026-10-09 and 2026-10-10)

- Quick test too easy: newest amendments in two States' versions (76 days); Legacy definitions still federal
  (3); two State comment rules as a difference (19 days, h13); STAG per permitted facility ($62,260, h14);
  publication-to-deadline days summed (307, h23); renewals over 25 years (4) and no-expiry units with Wisconsin's
  scope (50), both h24.
- Difficulty check too easy after a quick-test survival: Wisconsin vs Wyoming deadlines (28 weeks, Low 5/5); stale
  amendment list (1,271 days, Low 5/5, h15); no-expiry landfills (16, Low 4/5, h24).
- Difficulty check "In band - Easy tier": impoundments in States where EPA approves the State's version of one named
  definition (24, Low 3/5, h22). Both misses added Wyoming: its proposal has no itemised list, and the attempts
  could not recall whether one existed. The Alabama decoy caught nobody.
- What the traces show: the low model does five-document lookups, date counts and "label beside its rule" cases
  without error. Its only misses were on which near-identical proposal says what. No design so far gave it a
  complete-looking wrong route.

## New hooks (caller, 2026-10-10)

Aim of this round: the two measured Medium shapes not yet tried here. One scenario total in which each cell follows
a different stated rule (aq-02564 q02 rev 1: two cells Easy, four cells Medium), and a parallel-rule total where one
program's rule must not be carried into the other (aq-02486, aq-02562).

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h25 | D02 L220-L221 (new permit: two comment periods, each to 30 days after the second weekly notice); D03 L198 (a modification that would "expand a facility or increase capacity" follows the new-permit procedures), L195 (at least 45 days, hearing at least 30 days after notice, comment at least 15 days after the hearing); D05 L216 (liner design change = major modification, initial-permit procedures), L217-L218 (replacement wells of similar design and depth: no notice or comment), L240 (35 days, extended to include a hearing held after it ends) | Minimum public-comment days for four permit actions in three States, one total: 74 + 55 + 40 + 0 = 169 | Calculate across documents; Scatter the pieces; Mentions it vs does it (the well replacement) | Labels 60 + 45 + 35 = 140; Wyoming label 155; Virginia read as an "other major modification" 144, or at its 45-day floor 159; Alabama without the hearing extension 164, or with Virginia's 15 days carried over 184; well replacement given a 35-day period 204 | Extends closed h13 (two cells, quick test too easy) with two classification gates, Alabama's two cells and a total; the scenario is long (58 words); day lengths follow the documents' "days after" convention | q01 (i01) quick test too easy 2026-10-10: closed |
| h26 | D03 L195 (comments at least 15 days after the hearing); EPA's own hearing and comment dates in the DATES lines of D02-D06 (gaps 4, 12, 14, 11, 1 days) | Days by which EPA's five comment deadlines fall short of Virginia's own post-hearing rule: 11 + 3 + 1 + 4 + 14 = 33 | Calculate across documents; Scatter the pieces | The 45-day minimum instead of the post-hearing rule gives 0 (every EPA period is 60 days or more) | A hypothetical standard (EPA is not bound by a State rule); five plain date gaps, the family the low model solved 5 of 5 | i02 quick test too easy 2026-10-10: closed |
| h27 | D05 L208, L210 (design life, at most ten years; renewal 180 days ahead); D04 L193-L194, L202 (at most 10 years; renewal 365 days ahead) | Days between renewal-application deadlines for same-day permits in Louisiana and Alabama | Calculate across documents | Design-life gate ignored | Without a design-life condition the answer is 365 - 180; with one, the scenario asks about renewing a landfill past its design life | reject (trivial or unnatural) |
| h28 | Approved-as-State-version lists D03 L246-L272, D04 L316-L338, D05 L308-L329, D06 L309-L320; D05 L337-L341 (three definitions not approved); D02 L282 (no Legacy amendment sought); D06 L290, L339 (impoundments stay federal) | Units outside any approved State version of "infiltration": Wyoming 19 + Alabama 16 + Wisconsin's 3 impoundments = 38 | Mentions it vs does it; Match, then exclude | Keyword route gives Alabama only, 16; Wisconsin's approved entry read as covering its impoundments, 35 | Same family as h22 (measured Easy, no slot). Unit-level wording also rests on no Louisiana impoundment falling under its unapproved "no longer contain water" exclusion (D04 L393-L394), which the documents do not state | reject (family measured below target; unstated assumption) |
| h29 | D05 L161 (North Dakota final approval, Nov 17, 2025), L402 (North Dakota proposal, May 16, 2025); D03 L333-L334 (Virginia's revised application, March 4, 2026, leaves existing permits out) | Days from EPA's North Dakota proposal to Virginia's permit-excluding application: 292 | Same series, right edition | Final-approval date 107; original application 21 | Each date is labelled in its sentence; a named-step edition choice was Low 5/5 on aq-02631 | reject |
| h30 | Penalties D02 L252, D04 L269-L270, D05 L265, D06 L266-L268 | Total maximum penalty for one multi-day violation in several States | Rule application | Per-day rate carried into Alabama | Alabama's sentence is silent on days, Louisiana's two rates may stack, Wisconsin's "environmental violations" is undefined (as h8, h20) | reject (fairness) |
| h31 | Wyoming decision chain D02 L221, L224-L225, L233-L235 (37 + 20 + 30 + 15 = 102 days from first notice to the last day for a decision after a hearing) | A bounded timeline only Wyoming states | Calculate | Label 30 gives 95; no-hearing route 67 | One document; no other State bounds its decision time, so any second document is bolted on | reject (one source) |
| h32 | Approved-as-State-version lists D03 L247-L272 (20 entries), D04 L317-L338 (the same 20), D05 L309-L329 (17: the 20 less "Contains both CCR and liquids", "Infiltration", "Liquids", which L338-L341 list as not approved), D06 L310-L320 (11, including "Infiltration" and "Liquids"); D02 L280-L282 (Wyoming seeks no Legacy Rule amendment) | The State-by-amendment matrix: 9 amendments approved in four States, 10 in three, 1 in two; from the other side, 10 lack an approved State version in exactly two of the five States | Who belongs where; Match, then exclude | Count shortcut 17 - 11 = 6; one-sided difference 8; four-State set 9; Wyoming forgotten or taken as approving gives 1 | Same list family as h22 (single entry, Easy, Low 3/5) and as list diffs measured too easy elsewhere; needs every entry of four lists; small-integer answer; an entry absent from Wisconsin's enumerated approved list is read as not approved | i04 -> q02: difficulty Run 1 "In band — Medium tier", Low 0/5, Medium 3/5; submitted at Medium 2026-10-11. i03 closed as its sibling |

Not re-opened: 180-day review clock (only months printed for the completeness letters, h19); tribal counts
(recallable); Louisiana's total comment time (its pre-application notice also takes comments, length unstated).

The map is navigation; quotes come from text/DNN.txt. A short valid calculation or ID join is
eligible. Prior failures suggest tests/priority, not a universal veto.

Independent authors were not dispatched: aq-02483's caller and two independent authors inventoried these bytes on
2026-10-09, and aq-02626's caller re-read every State-specific section on 2026-10-10. This round re-read the
permitting, participation, enforcement, resources, partial-program and permits sections against the scenario-total
recipes and the low-model traces of aq-02626's three difficulty runs.
