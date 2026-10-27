# Current bundle checkpoint

- Goal and user constraints: aq-04112 (EFRA Committee, "Labour shortages in the food and farming sector",
  HC 713). User 2026-10-13: "no slot for Easy Tier ... target medium and high", "do your best". Never offer
  an Easy submission.
- Verification target / measured platform tier: medium (hard open too) / none. q02 "Too easy", Low 4/5
  (Run 1, Version 402a46). q03 "Too easy", Medium 4/6 (Run 2, Version baa047; "Low —": the check started at
  the medium level). q04 "Too easy", High 3/3 (Run 3, Version daf97b; the check went straight to the high
  model, as every run in the workspace did on 2026-10-14). q01 rev 1 "Too easy", High 3/3 (Run 4, Version
  cfc84c; "15 of 19 runs left"). Every candidate measured below target.
- Prepared runs / tested_sha256: q01 rev 1 runs/q01-r1-v2-e21fa8ca... / e21fa8ca748e30dd744dff7a5d147206fd58ff0778b207792a37ce790c1f6eb6.
  q04 rev 0 runs/q04-r0-v2-ca843e5c... / ca843e5c3c94945af18ec57b1dc5aadf2c7545da0798456181b7140977dfff96
  (d90c4ca2... superseded before hand-over). Historical: q03 rev 0 and 1, q01 rev 0, q02.
- Bundle slug / documents: aq-04112; Doc 1 = D03 report, Doc 2 = D01 hearing of 26 October 2021 (Q1-101),
  Doc 3 = D02 hearing of 9 November 2021 (Q102-168). Complete capture, hashes match, no gaps.
- Phase: three sketch rounds used, all four questions measured too easy; options reported to the user,
  release recommended. The page says "Your last 3 runs all came back Too easy. Ask the Coach before running again."
- Quick tests (user chat, no panels): survived: i01 rev 0, i02, i06 (twice), q01 rev 1, i10 (2026-10-14).
  Failed: q03 rev 0 (i06 reworded), i07, i03.
- Questions (sentences are the quick-tested ones, word for word; do not change them):
  - q01 (i01), q02 (i02), q03 (i06), q04 (i10): all dropped after their runs; hooks h1, h2, h14, h16 closed.
    Page notes: q04's lists "pre-compute the set difference, leaving only a literal string match"; q01's
    high attempts included the one-off fee, and the printed 50-worker total "also allows direct scaling".
- Other sketches: i03, i07 failed; i04, i05 withdrawn; i08, i09 rejected before files. h9 is a spare.
- Author errors on record: a survivor's sentence changed at write-up twice (q03 rev 0, q01 rev 1); rule
  in .claude/commands/docket-add.md step 3. A changed sentence is a new sketch.
- Changed files this session: questions/q03.md, q04.md, q04.json; notes ideas, hooks (h16),
  feedback-index (r7-r9), handover-q04.md, sketches i06, i10; memories docket-local-solver-calibration.md
  and the user open-tier note.
- Revision rounds used / open platform feedback: sketch round 3 of 3. Index rows r1-r10 resolved; none open.
- Five-candidate trial: not enrolled (the workspace's five slots are taken). Timing in
  ../../../notes/efficiency.json, partial. A timer left open across an 11-hour break was discarded; i10's
  sketch and write-up intervals are timed; the Run 3 feedback pass is
  untimed (a peer session's timer was active); the Run 4 pass is timed.
- Next action: the user's decision among the reported options: release (recommended); h9 sketched for a
  quick test (set operations on printed lists); or a membership-judgement design with its "One defensible
  answer" risk. No fourth search-type design.
- Runtime/model/effort: Claude Opus 5.5 in the VS Code extension; effort as configured.
- Optional diagnostic: none run, none needed.
