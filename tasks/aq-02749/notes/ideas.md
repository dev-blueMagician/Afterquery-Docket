# aq-02749 - lean candidate sketches

Current target: medium (user 2026-10-10: "there is no slot for Easy Tier for this bundle, we should target medium
and high. do your best."); measured platform success pending. All sketches origin claude (caller). No local model
checks were run. The task page offers 10 quick tests on up to 5 ideas ("Quick tests used: 0 of 10" at capture) and
10 difficulty runs. Its capture also reads "Question slots: Hard 0/2 · Medium 0/3 · Easy 0/1"; the user's instruction
governs the target, and the difference is reported to the user.

The same bytes were worked as aq-02483 and aq-02626: fourteen designs measured, none at Medium, best "In band -
Easy tier" (aq-02626 q04, Low 3/5). Their closed hooks are listed in hooks.md and are not re-tested here.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) | h25: minimum public-comment days for four permit actions in Wyoming, Virginia and Alabama, one total: 74 + 55 + 40 + 0 = 169 | Wrong routes 140, 144, 155, 159, 164, 184, 204, each failing a stated condition or a classification sentence; D02, D03 and D05 each sole source of its State's rule | q01 rev 0 (1ce4f588...): quick test too easy (user 2026-10-10); dropped, hook closed (feedback-index P1) |
| i02 | [sketches/i02.md](sketches/i02.md) | h26: days by which EPA's five comment deadlines fall short of Virginia's 15 days after a hearing: 33 | The 45-day minimum gives 0, which the question's "after a hearing" excludes; five sole-source date pairs plus D03's rule | quick test too easy (user 2026-10-10); dropped, hook closed (P2) |
| i03 | [sketches/i03.md](sketches/i03.md) | h32: 2024 all-unit amendments EPA would approve as the State's own version in exactly three States: 10 | 6 (17 - 11), 8 (one side), 9 (four-State set), 1 (Wyoming taken as approving); D03-D06 each needed, D02 unticked | round 2: quick test survived; closed as q02's sibling (same matrix and answer), not to be submitted |
| i04 | [sketches/i04.md](sketches/i04.md) | h32 from the other side: amendments lacking an approved State version in exactly two of the five States: 10 | 1 (Wyoming forgotten), 9, 8, 2; D02, D05, D06 needed, D03 and D04 unticked | round 2: quick test survived; q02 rev 0 (8f894659...) difficulty Run 1 (Version 94672c): "In band — Medium tier", Low 0/5, Medium 3/5; submitted at Medium 2026-10-11 (P4) |

Not sketched (reasons in hooks.md): h27 renewal-deadline gap (trivial or unnatural), h28 units outside an approved
State definition (the family measured Easy, with an unstated Louisiana assumption at unit level), h29 North Dakota
date gap (labelled dates), h30 penalties (fairness), h31 Wyoming decision chain (one source).

Still available from aq-02626 and untested there: i13, the platform Coach's own harder variant of its q06 ("How many
coal-ash landfills are in States that have already issued CCR-program permits and put no limit in years on a permit's
life?", Virginia 7 + Wisconsin 6 = 13). Same family as two too-easy results; a free quick test at most.

Round 1 (2026-10-10): i01 written up as q01, i02 held as a quick-test sketch; both quick-test too easy (user, same
day). Round 2: i03 and i04, the full approval matrix across the four itemised lists; both survived the quick test and
i04 is written up as q02 (Wyoming counts in every entry, so a low-model miss on Wyoming changes the answer).
User, same day: the difficulty check blocks the Easy tier on this set, so only Medium or Hard results are usable.

Outcome (2026-10-11): q02 measured "In band — Medium tier" (Low 0/5, Medium 3/5) and was submitted at Medium. Every
low attempt read Wyoming's grouped item as covering only the provisions it names and Wisconsin's shorter list as
approving everything; both medium misses misread Alabama's seventeen entries (as all twenty: 9; with the wrong three
missing: 6). Routes corrected 2026-10-12 from the fully loaded capture (notes/feedback-q02.md). Hook h32 is used; a
second question on the same lists would be a sibling.

Review (2026-10-12): the reviewer returned q02 ("Revision requested", second send-back): gold and traps confirmed, Docs 3 and 4 to be
ticked as exclusion sources with quotes, Steps 2, 4, 6 and 7 reworded. Rev 1 applies exactly that (feedback-index P5).

Run 2 (2026-10-13, rev 1, Version 54eee2): "Between levels", Low 0/5, Medium 4/5: the same question and answer as Run 1, measured again
because the ticks changed. Rev 2 adds one parallel count ("and how many in all five?", gold "10, 12"), which needs the
more prescriptive list that five of six recorded right medium attempts never used (P6).

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
