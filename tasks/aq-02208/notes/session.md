# Current bundle checkpoint

- Goal and user constraints: user 2026-10-08: "let's work on AQ-02208_2026-10-08_1841. there is no slot for Easy
  Tier for this bundle, we should target medium and high. do your best." Page (capture 18:41): Hard 0/2 · Medium 0/3 ·
  Easy 0/1, 9 submissions left, 0 of 10 quick tests at intake, 8 of 8 difficulty runs.
- Verification target / measured platform tier: medium (hard where possible) / q02 passed at Easy (user report
  2026-10-09, binding assumed); below target; submitted at Easy by the user's decision.
- Bundle: six Federal Register documents (FAA CSLCA final rule; FCC WTB proposed procedures; FCC Third R&O; FCC WTB
  final procedures; FCC 2026 emergent-space NPRM; FAA 2026 waiver NPRM). Local ids = Doc numbers (D01 = Doc 1 ...).
  Complete capture, no gaps. Map: notes/doc-map.md; hooks: notes/hooks.md; feedback: notes/feedback-index.md.
- Phase: round 2 sketching (round 1 closed: q02 submitted, verdicts reviewed).
- Questions:
  - q01 rev 2 (d58f4220...) dropped: quick test "too easy" (user, 2026-10-08; f1).
  - q02 rev 0 submitted (Easy Tier), tested_sha256 d21d65331df3f34739c848fe0d64bade4dd5a635b93b98bb9d6249bd87c1c6b5 (20 words,
    quick-tested wording verbatim): how many more transmitter-characteristic items the final coordination-request
    list holds than the December 2024 proposal = 5 (17 - 12; Doc 4's discussion explains only three additions).
    Quick test survived (user, 2026-10-08; f2). Removal probes (runs/q02-r0-alt-t8): no Doc 2 -> 3 at p 0.75
    (the mode 1 decoy); no Doc 4 -> not answerable, forced 2 at p 0.2. Handover: notes/handover-q02.md.
- Revision rounds: none on q02. Five-candidate trial: not enrolled (all five slots taken). Timers stopped.
- q02 submitted 2026-10-09 at the Easy tier (user: "Passed with your first option"): status submitted,
  accepted_tier: Easy Tier; file frozen (later notes go to notes/feedback-q02.md). The first Submit was blocked on the
  failure modes (f3); the two-mode replacement passed. Verdict review: notes/feedback-index.md (2026-10-09).
- Slots after this: Easy used by q02; Medium 0/3 and Hard 0/2 open. No other fair Medium design found so far.
- Round 2 (user 2026-10-09: "ok, go for medium then"): target medium. Principles: cheapest mechanical route must land
  on the decoy; no twin facts (Doc 3/Doc 4, Docs 2-4); no FR+30 rebuildable dates; numeric first; batch quick test of
  sketches before write-up; probes for recallable inputs at sketch time. One fresh question-author searching
  (closed families listed in hooks.md). Caller's re-scan of Docs 2-4 numbers found nothing new.
- Round 2 result: third author found no fair Medium design; its best leftover i32 (95 MHz) passed both sketch-stage
  removal probes (no Doc 3 -> 60; no Doc 5 -> not answerable). Next: user quick-tests i32; full write-up only if it
  survives; if too easy, stop Medium on this bundle (three rounds, WORKFLOW section 6).
- Runtime/model/effort: Claude Code VS Code extension, claude-opus-5-5, effort max.
