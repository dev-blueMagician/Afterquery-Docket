# Current bundle checkpoint

- Goal and user constraints: aq-03950 (Welsh Affairs Committee, "Wales as a global tourist destination").
  User 2026-10-13: no Easy slot, "target medium and high". Never offer an Easy submission.
- Verification target / measured platform tier: q02 file target hard / measured "In band — Medium tier"
  (Low 0/5 · Medium 2/6), submitted at Medium. q03 target medium / no run yet.
- Prepared runs / tested_sha256: q02 runs/q02-r0-v2-cfc8c753...-platform /
  cfc8c753dba45347e32f4e6fa70c03ba92491659befb6b21405a4af4ee4c475b (the run is bound to it for question,
  answer and necessary documents). q03 runs/q03-r0-v2-864acc27...-platform /
  864acc277ec1e127bce87277b7ea23abf6aaaa7d75395dcf016081251a13395e. q01 9e00cc4c..., dropped.
- Bundle / documents: Doc 1 = D07 report, Doc 2 = D02, Doc 3 = D01, Doc 4 = D03, Doc 5 = D04, Doc 6 = D05,
  Doc 7 = D06. Complete capture, hashes match, no gaps.
- Phase: feedback recorded for q02; q03 ready and untested.
- Questions:
  - q01 (i01, count 9): dropped. Quick test failed 2026-10-13; so did i04.
  - q02 (i02): SUBMITTED, frozen (status submitted, accepted_tier Medium Tier, file sha256 cdfb937f... at
    freezing). Do not edit. Observations go to notes/feedback-q02.md. observed_platform_status: unknown
    (in review; acceptance not observed).
  - q03 (i03): checked, rev 0, floor 0 FAIL 2 WARN (origin; exclusion role on Doc 3). Quick test survived.
    No "One defensible answer" result and no difficulty run yet. Gold Miles-Payne, Yen.
- Decisions and constraints: verdict capture read in full (17 attempts). Nine of nine recorded wrong answers
  were Pickles and Yates, the declared failure mode. The user submitted before sending the capture.
- Lessons folded in (2026-10-13): sketches only until a quick-test survivor (docket-new step 6,
  docket-start-from-measured-misses); alternatives are left out together in the Document check
  (docket-series-editions-necessity); difficulty_target is the lowest tier the user named as open;
  recipe 6 list form measured Medium here (docket-local-solver-calibration); verdict_summary.py now
  shows a whole bulleted answer.
- Open findings: q02 soft spot if a reviewer asks: "a role" against "an employee" (the strongest solver
  hesitated before counting the board seat). q03 readings still possible: Miles-Payne left out (Yen alone)
  or Sweatman added.
- Changed files: questions/q02.md (frozen), notes/feedback-q02.md, feedback-index.md, ideas.md,
  verdicts/AQ-03950_difficulty_2026-10-13_1354.txt (user capture).
- Revision rounds used / open platform feedback: sketch round 1 of 3; none open.
- Active feedback index: notes/feedback-index.md (F1 historical, F2 resolved). Trial: not enrolled.
- Efficiency ledger / candidate / active timer: ../../../notes/efficiency.json / i01 (one interval) / none.
- Next action: if this document set is claimed again, q03 is the next candidate: paste
  notes/handover-q03.md, look at "One defensible answer" first, run difficulty, and send the saved page.
  For q02, log any review panel verbatim in notes/feedback-q02.md before anything else.
- Runtime/model/effort: Claude Opus 5.5 in the VS Code extension.
- Optional diagnostic: none run, none needed.
