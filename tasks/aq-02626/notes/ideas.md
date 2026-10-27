# aq-02626 - lean candidate sketches

Current target: medium (user 2026-10-10: "there is no slot for Easy Tier for this bundle, we should target medium
and high. do your best."); measured platform success pending. All sketches origin claude (caller). No local model
checks were run. The task page offers 10 quick tests on up to 5 ideas ("Quick tests used: 0 of 10" at capture) and
lists "Picking the right measure" and "A single-value answer" as shapes it is short of.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) | h13: Wyoming's two comment periods by rule (2 x 37 = 74 days) minus Virginia's minimum with a hearing on day 40 (55): 19 days | Labels give 15, 5 or 29; D02 and D03 each sole source | q01 rev 0 (3532a741...): quick test too easy (user 2026-10-10); dropped, hook closed (feedback-index P1) |
| i03 | [sketches/i03.md](sketches/i03.md) | h14: STAG funding per permitted facility, Alabama minus Virginia: $62,260 | Alabama's larger total gives $87,684; D03 and D05 each sole source | q02 rev 0 (eaf8ef1c...): quick test too easy (user 2026-10-10); dropped, hook closed (P2) |
| i05 | [sketches/i05.md](sketches/i05.md) | h13 with one condition: 29 days | Same Wyoming path as q01, one gate fewer | dropped untested (dominated by q01's result) |
| i04 | [sketches/i04.md](sketches/i04.md) | h16: five-State awarded total, $4,033,152 | Same Alabama measure choice as q02, nothing else | dropped untested (dominated by q02's result) |
| i02 | [sketches/i02.md](sketches/i02.md) | h15: days from Wyoming's chapter 18 taking effect to EPA's latest amendment as of September 2026: 1,271 | Wyoming's own list gives 812; February 10, 2026 is in D03-D06 (alternatives group) | round 2: quick test survived (user 2026-10-10); promoted unchanged to q03; rev 0's Step 4 drew a form number-check line on 365 (P5), rev 2 splits the day count into two-operand steps with no number words, checked (0 FAIL), tested_sha256 f3d04aef...; difficulty check too easy (user 2026-10-10, no capture); dropped, hook closed (P7) |
| i06 | [sketches/i06.md](sketches/i06.md) | h22: impoundments in States where EPA approves the State's version of "contains both CCR and liquids": Virginia 18 + Louisiana 6 = 24 | Alabama's identical entry sits under "not being approved" (37); Wisconsin's list omits it (27) | round 2: quick test survived (user 2026-10-10); promoted unchanged to q04 rev 0 (gold now "24 surface impoundments"), checked (0 FAIL), tested_sha256 c18fded5...; difficulty Run 1 (Version d686ca): "In band — Easy tier", Low 3/5, below target and no Easy slot: held, not submitted, no repair (P4) |
| i07 | [sketches/i07.md](sketches/i07.md) | h23: days from publication to comment deadline, summed over the five proposals: 307 | The printed "60-day" label gives 300; five sole-source inputs | q05 rev 0 (15e8c0cd...): quick test too easy (user 2026-10-10); dropped, hook closed (P6) |
| i08 | [sketches/i08.md](sketches/i08.md) | h24: landfills in States whose CCR-program permits have no set expiry: Virginia 7 + Wyoming 3 + Wisconsin 6 = 16 | Wisconsin's ten-year plan update (10); Alabama's "design life" and Louisiana's "active life" under ten-year caps (19) | round 2: quick test survived (user 2026-10-10); promoted unchanged to q06 rev 0 (gold "16 landfills"), checked (0 FAIL), tested_sha256 8b7ea010...; difficulty check too easy (user 2026-10-10, no capture); dropped, hook closed (P10) |
| i09 | [sketches/i09.md](sketches/i09.md) | h24 as one stated case: renewal applications over 25 years in Alabama, Louisiana and Wisconsin: 2 + 2 + 0 = 4 | Wisconsin's ten-year plan updates counted as renewals give 6 | round 2: quick test too easy (user 2026-10-10); dropped (P9) |
| i10 | this table | h24 with Wisconsin's scope added: coal-ash units that would be permitted by States whose CCR-program permits carry no set expiry: Virginia 25 + Wyoming 19 + Wisconsin's 6 landfills = 50 | Wisconsin's 9 units give 53; its 3 impoundments stay with EPA (D06 L290); same duration sentences as q06 | quick test too easy (user 2026-10-10); dropped (P11) |
| i13 | this table | h24 plus the Coach's second condition (Run 3, Version 8bf6fe): "How many coal-ash landfills are in States that have already issued CCR-program permits and put no limit in years on a permit's life?": Virginia 7 + Wisconsin 6 = 13 | Skipping either condition gives 16 (Wyoming, uncapped but none issued, D02 L302; or Alabama, issued but capped, D05 L208); D03 and D06 each sole source. Risk: the only miss in Run 3 left Wyoming out, which this version makes correct | offered as a free quick test; write-up (q06 rev 1) only on survival |

Round 1 (2026-10-10): q01 and q02 both quick-test too easy. Round 2: i02 and i06 survived the quick test and are
written up as q03 and q04; i07, i08 and i09 were not tested (user: "i02 i06 survived, rest of them not tested") and
stay as sketches. Set rule: write up at most one of i08/i09 (shared duration sentences); q03 and q04 share no fact.
Rejected hooks and reasons: hooks.md h17-h21 and aq-02483's h2-h12.

Outcome (2026-10-10): three rounds used. Measured: q01, q02, q05, i09, i10 quick-test too easy; q03 (Low 5/5) and q06 (Low 4/5) too easy at
the difficulty check after surviving the quick test; q04 "In band — Easy tier" (Low 3/5), held because the bundle
has no Easy slot. No design reached Medium. Recommendation to the user: release the bundle. Untested and in q04's
measured family only: approvals in Alabama's list but not Wisconsin's (8; count shortcut 6) and the five-State total
of approved amendments (68).

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
