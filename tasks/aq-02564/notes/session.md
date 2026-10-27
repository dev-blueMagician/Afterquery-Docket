# Current bundle checkpoint

Replace this file at each phase boundary; keep it under 4,000 characters.
It is working memory for resuming the bundle and is never submitted.

- Goal and user constraints: user 2026-10-09 "no slot for Easy Tier ... target medium and high"; 2026-10-10
  "submitted as medium tier. check out the arrived verdict and improve your performance".
- Verification target / measured platform tier: medium / q02 rev 1 "In band — Medium tier", Low 0/5 ·
  Medium 3/5 (Run 2, Version 8ce393), at target. Not acceptance.
- Prepared run / tested_sha256: q02 rev 1, runs/q02-r1-v2-27f12de0...-platform, 27f12de0085381a8970d...
- Bundle slug / documents (ids) / extraction warnings: aq-02564, 7 plain-text FR documents, complete;
  D01 = Doc 2, D02 = Doc 1, D03-D07 = Doc 3-7.
- Phase: submitted; feedback recorded.
- Questions: q01 dropped (quick test too easy). q02 FROZEN: status submitted, accepted_tier: Medium Tier,
  rev 1, gold $2,375, file sha256 911b0af5... at freezing. Do not edit; later observations go to
  notes/feedback-q02.md. observed_platform_status: unknown (review pending).
- Platform feedback: notes/feedback-index.md P1-P2 quick tests too easy (q01, i02), P3 i03 survived, P4
  q02 rev 0 Easy (Low 2/5), P5 q02 rev 1 Medium (Low 0/5, Medium 3/5). Raw: the two captures in
  verdicts/ (2026-10-10 02:27 and 03:56). Platform Checks (39): no capture, unknown.
- What separated solvers on Run 2: hosted subscribers' set fees left off the host's bill ($875, Low x3);
  user fees unpriced ($1,750, Low 1 and Medium 3); BYX credit kept ($2,125 Low 5; $2,387.50 Medium 5).
  Declared mode 2 (Scope, $1,625) caught no attempt (soft spot noted in notes/feedback-q02.md).
- Decisions and constraints: only the EDGX/BYX pair joins fairly; the Medium came from several independent
  easy steps in one scenario, not from a single trap. Page: 8 of 10 difficulty runs left, 8 submissions
  left if the page counted this one; Medium 1/3 in review, Hard 0/2.
- Candidate families: h1, h2 closed; h13 -> i03 -> q02 (submitted). A second question on this bundle
  would reuse the same two notices and fee inputs (sibling of q02): only on the user's request.
- Changed files since the last checkpoint: questions/q02.md (Run 2 record, status submitted),
  notes/feedback-q02.md (new), notes/feedback-index.md (P5); memory lessons (calibration, redesign, index).
- Revision rounds used: 2 sketch rounds; q02 rev 0 -> rev 1; 2 difficulty runs.
- Five-candidate trial: not enrolled (workspace trial full, 5/5); no timer started by this session.
- Efficiency ledger / candidate ID / active timer ID: ../../../notes/efficiency.json / none / none.
- Next action and blocker: none unless the platform returns the task; then log the panel verbatim in
  notes/feedback-q02.md first.
- Runtime/model/effort: Claude Opus 5.5 (claude-opus-5-5) in Claude Code, VS Code extension.
- Optional diagnostic if needed: none run.
