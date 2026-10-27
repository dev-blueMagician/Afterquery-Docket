# Current bundle checkpoint (2026-10-08, q04 passed at Easy)

- Goal: user 2026-10-07: "there is no slot for Easy Tier for this bundle, we should target medium and
  high." Targets medium. Workflow v3.1: author arithmetic, one mechanical preflight + full hand-over,
  platform validation; no automatic local solves/probes/reviews.
- Bundle: 20 ITA CCG energy chapters, complete, no gaps. Doc N: D01=7 D02=1 D03=6 D04=10 D05=18 D06=9
  D07=19 D08=5 D09=8 D10=13 D11=2 D12=16 D13=20 D14=12 D15=4 D16=17 D17=11 D18=14 D19=15 D20=3.
- Feedback triage: [notes/feedback-index.md](feedback-index.md) (F1-F3 q01, F4-F6 q04, H1-H3 history).
  Trial owner: workspace notes/feedback-index.md; no aq-01543 candidate enrolled (q04 comes from the
  pre-trial sketch i05; old candidates are not backfilled).
- q01 DROPPED: revs 1-8 ("In 2024") drew the form's "Working the question from the documents does not
  give this answer"; rev 9 ("In calendar year 2024", 8671bcad...) Quick test "Too easy. Solver got it"
  (user, unconfirmed binding). No fair wording between the two. q02 dropped earlier (Too easy).
- q04 rev 0, status checked, tested_sha256 addb7a41e30a3b93fdb5f019e31590520c91c44a5de49e352a5dc1f6918593e0
  (runs/q04-r0-v2-addb7a41...-platform/). Koeberg 1,830 MW / Korea's 23 reactors in operation (Table 2
  sum 23,500 MWe, data as of Sep 25, 2025) = 7.79%. Traps: prose "approximately 26" GW(e) total installed
  (7.04%), "Expected to be in operation" rows (6.29%), Kori-3/4 blank status (7.20%). Floor 0 FAIL, 1 WARN
  (origin). Hand-over notes/handover-q04.md; JSON questions/q04.json.
- q04 difficulty check, verbatim (verdicts/AQ-01543_difficulty_2026-10-08_1236.txt; version a39f39 = rev 0):
  Run 1 "In band — Easy tier", Low 1/5 · Medium — · High —, "You can submit now", advisory "This question may be
  too vague" (7.20% x3 = merged Kori status rows, 7.04% x1 = prose 26 GW). Document check passed (both docs needed;
  without Doc 4 the high model gave 7.21%/7.23%, so the stated recall risk did not appear). Status stays checked
  (target medium). Failure modes rewritten to the new layout (46-word reason); user rule saved in memory.
- Lesson: the printed count of 23 that keeps FM3 fair is also the low model's check sum (1 of 5 used it) -> Easy.
- q03 rev 4 draft (808fc8ec), user paste pending; rated Easy-leaning locally.
- Environment: Bash needs PATH prefix
  `/usr/bin:/mingw64/bin:/c/Users/Administrator/AppData/Roaming/uv/python/cpython-3.12.15-windows-x86_64-none`.
- Next: user submits q04 at Easy if they choose (risk: reviewer may act on the "too vague" advisory); record
  submission/acceptance or a returned panel. Medium is still open on this bundle with no further family in hand.
