# Current bundle checkpoint

Working memory for resuming aq-03711; never submitted. Updated 2026-10-13 (q02 rev 1 quick-test too easy; no
live question; decision returned to the user).

- Goal and user constraints: user, 2026-10-12: "there is no slot for Easy Tier for this bundle, we should
  target medium and high. do your best." Easy is not usable: never offer it or re-ask.
- Verification target / measured platform tier: medium (Hard welcome) / none in band. No difficulty run spent.
  Quick tests (user chat, no panels, routes unread): q01 too easy; i11 too easy; q02 rev 0 survived; q02 rev 1
  "too easy for quick teset"; i21 taken as not surviving (the user reported only that the last spare survived).
  Page at capture (2026-10-12 21:32): "Hard 0/2 · Medium 0/3 · Easy 0/1", 8 submissions left.
- Prepared run / tested_sha256: none live. runs/ holds q01 and q02 snapshots (history; q02 rev 1 = 73468c0f...).
- Bundle / documents / extraction: fourteen papers from the NZ Commerce Commission's 2023-24 review of the 111
  Contact Code. Local -> Doc: D02 = 1, D01 = 2, D06 = 3, D07 = 4, D09 = 5, D11 = 6, D12 = 7, D13 = 8, D14 = 9,
  D03 = 10, D04 = 11, D08 = 12, D10 = 13, D05 = 14. Capture complete. Source defects: One NZ (Doc 5) lacks its
  page 3; Doc 12's tracked changes are flattened; Figure 1 is a caption only in Docs 2 and 3.
- Not a repeat bundle. Family: the other NZ Commerce Commission consultation bundles (doc-map.md).
- Phase: closed pending the user's decision. Sketch round 1 used, plus one repair of q02.
- Structural finding: Docs 2 and 3 summarise every submission, and each rule is printed twice (Docs 3 and 14;
  Docs 2 and 12). Only the submitters' own facts and a few figures are single-source (hooks.md).
- Questions and sketches (origin claude), all with a result (table in ideas.md, last section):
  - q01 (h1) dropped: Bupa's sites under two views, quick test too easy.
  - i11 (h15) dropped: battery cost per means, quick test too easy.
  - q02 (h2) dropped: rev 0 (draft commencement rule, starting date open) survived the quick test, then the
    form's "One defensible answer" Failed with both solvers on 18 March 2024 and 289 days; rev 1 (one reading,
    no cue, gold 26 September 2024 and 97 days) was quick-test too easy. The survival was the open reading.
  - i21 closed. i22 not offered: the draft round's deadline can be inferred from dates Doc 3 prints, so a
    ticked document would not be needed. h9 and the fuzzy lists not sketched (hooks.md, ideas.md).
- Platform feedback kept: notes/platform-feedback/2026-10-13-q02-checks-1.png, -2.png, -checks.txt (Checks on
  the user's own-words version of q02 rev 0; identity unbound).
- Decisions and constraints: no answer naming or counting the bundle's submitters; no working-day counts; no
  lists whose membership the documents leave open; no wording that reopens q02's second answer.
- Open findings: none on a live question.
- Revision rounds used / open platform feedback: q02 1 / none open. Feedback index: notes/feedback-index.md.
- Five-candidate trial: slots full; unpromoted. Efficiency ledger: no timer started (a peer's timer was open);
  quick tests carry no run identity and are not recorded there.
- Workspace lessons recorded: .claude/memory/docket-local-solver-calibration.md (three 2026-10-13 entries).
- Next action: the user decides whether to release the bundle (recommended: every fair sketch has a result).
  If the user sends any panel or capture, read it first. Do not reword q01, i11 or q02 again.
- Runtime/model/effort: Claude Opus 5.5, VS Code extension. Optional diagnostic: none run.
