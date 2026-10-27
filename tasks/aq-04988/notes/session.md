# Current bundle checkpoint

- Goal and user constraints: user 2026-10-14: "let's work on AQ-04988_2026-10-14_1417. there is no slot for Easy Tier
  for this bundle, we should target medium and high. do your best." Page at capture (14:17): Hard 1/5 · Medium 0/1 ·
  Easy 0/0; quick tests 0 of 15 (up to 5 sketch slots); difficulty runs 15 of 15; 8 submissions left. Capture carried
  "Docket has been updated. Reload this page ...".
- Verification target / measured platform tier: q01/q02 files say medium (pre-playbook); the page now reads "Easy or
  Hard only" (Easy 0/0), so only Hard is left and new work uses hard. Measured: q02 rev 0 Run 1 Too easy, High 3/6.
- Prepared run / tested_sha256: q01 rev 0 4d36678e54a5fb6d8d7d40c6b421a3ac5748ee032f1abc3d3791669e3fd7dfec;
  q02 rev 0 690ceb30daf99d042d7791cfe2238ba84829d9b0e467f66d83eb3df7ea8c3aae (runs/q0N-r0-v2-*-platform/).
- Bundle slug / documents / extraction warnings: aq-04988 / ten salt-reduction papers; local D01-D10 differ from page
  Doc 1-10 (table in doc-map.md) / capture complete 10 of 10, no gaps; some tables/figures never in the platform text.
- Repeat check: no document hash or file name shared with any bundle in 10.6, 10.7, 10.8 or docket-capture (2026-10-14).
- Phase: checking. Quick tests (user 2026-10-14, "both survived"): i01 -> q01, i02 -> q02, sentences and answers
  word for word. Both checked rev 0 (q01 0 FAIL / 5 WARN, q02 0 FAIL / 8 WARN: origin, units, exclusion role and
  deep-number false alarms; answered in Lever checks). Full hand-overs: notes/handover-q01.md, handover-q02.md.
- Questions: q02 checked rev 0: Run 1 (7:25 PM, Version ff8991) "Too easy", Low — · Medium — · High 3/6, refunded;
  routes unread; by the gate one solver 0/3, the other 3/3; hook retired (playbook: High Too easy = replace).
  q01 checked rev 0, not run; its sentence (i01) screened 3/3 right (ranked last; ledger row 16).
  Index: notes/feedback-index.md F1; ledger ../../../notes/hard-runs.md rows 13 and 16.
- Round 2 (done): screens i03, i04, i05 each 3/3 right (ranked last; ledger rows 20, 18, 19); author C found no new
  fair Hard sketch (hooks.md, Round 2). Every fair sketch is now screened and handed to the user.
- Decisions and constraints: sketch only until the user reports a quick-test survivor; a survivor's sentence goes onto
  the form word for word; target medium in files; count unpointed steps (high-solver audit); delete-and-guess per
  ticked document; no tier odds; ask for the capture before Submit in the last message before any run.
- Candidate families tried: hooks.md h1-h12 (caller), all zero unpointed steps or failing necessity/one-answer so far.
  Internal inconsistencies to avoid as golds are listed in doc-map.md.
- Changed files since the last checkpoint: notes/doc-map.md, hooks.md, ideas.md, session.md, sketches/i01.md,
  sketches/i02.md; docs/, text/, intake.json by tools.
- Revision rounds used / open platform feedback: sketch round 1 of 3 (two survivors) / none.
- Active feedback index / issue ids / current fix: notes/feedback-index.md (template, empty).
- Five-candidate trial: not enrolled (promote refused 2026-10-14: all five slots enrolled). Efficiency: one sketch interval
  recorded (session 1b116548..., started 18:22Z, stopped before the authors' wait); a later start was refused
  because a peer session (aq-05000) holds the workspace's only timer: this session's timing is partial (not estimated).
- Next action and blocker: the user's choice: run q01 (written up; a Too-easy run is refunded), quick-test or run any
  of i03-i05 (write-up on request), or release. No new fair Hard hook found after two rounds.
- Runtime/model/effort: Claude Code in VS Code, claude-opus-5-5.
- Optional diagnostic if needed: none run.
