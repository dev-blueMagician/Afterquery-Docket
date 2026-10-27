# Current bundle checkpoint


- Goal and user constraints: AQ-03120 "Public policy": six submissions to the NZ Commerce Commission's Preliminary
  Issues paper for its personal banking market study (Aera, ANZ, ASB, BNZ, Consumer NZ, Federated Farmers; Sept 2023).
  User, 2026-10-11: "there is no slot for Easy Tier for this bundle, we should target medium and high. do your best."
  Capture: 0 of 10 quick tests used.
- Verification target / measured platform tier: medium / MEDIUM: q02 rev 2, difficulty Run 3 (Version 6243da, Oct
  12, 2026, 5:22 PM), "In band - Medium tier", Low 0/5 · Medium 2/5, Docs 3 and 4 each needed. Submitted at Medium
  2026-10-12 (user report); acceptance pending. Page after Run 3: 12 of 15 runs left.
- Prepared run / tested_sha256: q02 rev 2 = runs/q02-r2-v2-e0d20bd4...-platform /
  e0d20bd4982d08dc83e3396ad5f4816f4f70ff5a21006aa59096f178839bd31b (the submitted content). History: q02 rev 0
  a4f09e88... (Run 2, gate failed); rev 1 64ce77d2... (quick test too easy); q01 rev 0 ec5f8e4c... (Run 1, Easy).
- Bundle slug / documents / extraction warnings: aq-03120; D01-D06 = Doc 1-6 (same numbers). Complete capture (gap
  0). No chart data in D02-D04; D04 has 66 "[ ]" redactions, D03 59 "[Redacted]".
- Phase: submitted. questions/q02.md is FROZEN (status submitted, accepted_tier: Medium Tier): never edit it; later
  observations go to notes/feedback-q02.md.
- Questions (origin claude):
  - q02 rev 2, submitted: "How much did Kiwibank's home lending book grow in the half of its financial year that
    last ended before its owner announced a $225 million capital injection?" -> $0.5 billion (Doc 3 FY23 $1.1
    billion minus Doc 4 first half $0.6b; injection dated 1 August 2023 in Doc 4 footnotes).
  - q01 dropped (four versions). Sketches i01-i05 not promoted.
- What the seven versions of hook h1 measured (full routes in the question files' Feedback logs):
  plain in-period event from a third document, dollars: Easy, Low 1/5; event carrying the other half's label:
  form block twice; any cue to calculate (percentage, "stated or implied"): quick-test too easy twice; "financial
  half-year" (also a reporting label): counts in band, gate failed; structural period term, event dated after the
  period, no cue: Medium.
- Decisions and constraints: none open. Do not offer a lower-tier submission on this bundle.
- Candidate families tried / source completeness: hooks.md h1-h11; all six documents fully read.
- Changed files: questions/q02.md (Run 3 record, submitted), notes/feedback-q02.md (new), feedback-index.md (P7),
  ideas.md, hooks.md, session.md; verdicts/ (user's capture). Workspace: lessons folded into WORKFLOW.md, the
  docket-new / docket-check / docket-feedback commands, bundle-mapper, tools (screen warning) and memory notes.
- Revision rounds used / open platform feedback: q02 2, q01 3 / none open.
- Feedback index: notes/feedback-index.md (P1-P7). Five-candidate trial: slots full; unpromoted (candidate i07:
  two difficulty attempts, two revisions, outcome pending recorded).
- Next action: none unless the platform returns a review. If it does: log it in notes/feedback-q02.md verbatim; a
  "Revision requested" hands the question back (revise in place as a new revision, drop accepted_tier until
  resubmission).
- Runtime/model: Claude Code (VS Code), claude-opus-5-5. Optional diagnostic: none run.
