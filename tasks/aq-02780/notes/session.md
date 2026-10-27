# Current bundle checkpoint

- Goal and user constraints: user 2026-10-10 "there is no slot for Easy Tier for this bundle, we should target
  medium and high. do you best."; 2026-10-11 "pass as an easy tier. but no slot for easy now". Target medium,
  hard welcome. The page still prints "Hard 0/2 - Medium 0/3 - Easy 0/1"; the user's instruction governs.
- Verification target / measured platform tier: medium / Easy on q01 rev 1 (below target, so not `ready`).
  Difficulty runs: 2 used, 8 of 10 left.
- Prepared run / tested_sha256: q01 rev 5 = 9a1c7f695d366cdad73ac51798f5c08f9cd9d6f3062e7455da391726f398b4bc
  (runs/q01-r5-v2-...-platform). History: rev 4 = 2dbe139a..., 3 = 3d92ec69..., 2 = 8d0a0160..., 1 = 1c342b41..., 0 = f6541c05...
- Bundle: aq-02780 "Bank Merger Act Rulemaking", D01-D07 = Doc 1-7 (identity). Full capture, no gaps. Bytes
  identical to tasks/aq-02706; its map and measured results apply (h4, h11 too easy; h12 Easy); not reopened.
- Phase: rev 5 checked; two form checks failed (index P4, P5); waiting for the user. Sketch rounds: 1 of 3.
- Question q01, checked, origin user+claude, D04 x D07, sketch i01, hook h13 (one plan for a covered community
  bank, a covered community savings association and a State nonmember bank; one count per agency):
  - rev 0 (9 changes): Run 1, Version 5d70b5, "Answerable without the documents" (2 + 3 + 4 = 9). Index P1.
  - rev 1 (4 by the OCC, 6 by the FDIC): Run 2, Version fb0985, "In band - Easy tier", Low 1/5; Document
    check passed. Four low attempts gave OCC 12, FDIC 6 (the association's branch provision read as an
    expedited filing); nobody fell for the main office or home office limits. Index P2.
  - rev 2 (3 by the OCC, 7 by the FDIC; 27 changes; 59 words): the bank forms four qualifying operating
    subsidiaries (after-the-fact notice, no approval), the association forms one (application) and opens
    eight branches (none), State bank opens six and moves five next door; head offices as before. Only the
    correct assignment of the question's items gives 3 and 7. No run: the form flagged its question text
    as AI-generated (index P3; accurate, the caller wrote it; no agent rewording was given).
  - rev 3, 4, 5 (same gold and fields): the question is the user's own wording, kept verbatim; rev 5
    (State bank first, "forms 4", 59 words) is current; none measured yet. Floor 0 FAIL / 2 WARN (origin;
    revision count). Hand-over: notes/handover-q01.md.
- Rev 1's passing Easy result is replaced once the form holds rev 5; rev 1's fields stay in runs/q01-r1-...
- Sketch i02 (D03 x D04, 3 filings): quick test only.
- Open risks: "qualifying" must be read as meeting the rule's structural and activity requirements;
  D07 fn 15's exempt associations are not described. The form's "One defensible answer" check screens this.
- Decisions: a second Easy result means the hook's level is Easy: stop and recommend release. Edit question
  files with Edit/Write, never a scripted splice.
- Feedback index: notes/feedback-index.md rows P1 (resolved), P2 and P3 (repaired, platform pending). Efficiency
  ledger: ../../../notes/efficiency.json; attempts AQ-02780:run1:5d70b5 and run2:fb0985 recorded for i01; no
  timed intervals (timing unknown).
- Memory: docket-general-knowledge-check; docket-local-solver-calibration (aq-02780 entry).
- Form checks on rev 5 (screenshots 2026-10-11/12, Question box shows rev 5 verbatim): "One defensible
  answer" Failed, message truncated by the form after agreeing with the OCC count of 3 (P4, cause unknown);
  "Question in your own words" Failed (P5). No agent rewording is supplied for the own-words check.
- Next action: user's decision. To continue: get the rest of the message (page capture or Question Coach),
  then one content repair; the own-words check needs the user's own rewrite or an admin. Else release.
- Runtime: Claude Code, claude-opus-5-5.
- Tool gap flagged: no floor check for a gold equal to a sum of the question's numbers.
