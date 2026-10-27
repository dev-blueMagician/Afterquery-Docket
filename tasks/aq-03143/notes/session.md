# Current bundle checkpoint

- Goal and user constraints: AQ-03143 "Public policy", seven UK Ministry of Justice legal aid documents (civil
  2025: consultation, impact assessment, response, response-stage impact assessment; criminal 2022: interim
  response and two impact assessments). User, 2026-10-11: no Easy slot, "target medium and high"; 2026-10-12:
  "easy tier. but no slot." Never offer an Easy submission.
- Verification target / measured platform tier: medium (Hard welcome) / none reached. Run 1 (Version 45b6c4,
  rev 0): "In band — Easy tier", Low 2/5, now "an earlier version". Run 2 (Version c26715, rev 1): "Too easy",
  Low 5/5; the gate fails on the page's current content. 14 of 16 runs left; 6 of 10 quick tests used.
- Prepared run / tested_sha256: rev 1 12f43234d2873bbdd1d527ee27df1f65ca4e4e836af43d92116bb0777c8422f9 (Run 2);
  rev 0 ee19a33b0ef41d29c36426c96e4dc26659b8a199cb8f1ea7dcf4552b9e030079 (Run 1); 3bf58824... never tested.
- Bundle slug / documents / extraction warnings: aq-03143. D04 = Doc 1 (civil consultation), D02 = Doc 2,
  D01 = Doc 3 (civil response), D03 = Doc 4, D07 = Doc 5, D06 = Doc 6, D05 = Doc 7. Complete, gap 0. Tables are
  flattened in row order. Doc 1's Higher Courts travel example contradicts its Annex B and Doc 3: never use it.
- Phase: closed after two rounds. Release recommended to the user; nothing submitted.
- Questions: q01 dropped (origin claude). Rev 0: two legal help matters on opposite sides of their escape
  thresholds plus housing attendance, £1,032.50. Rev 1: 2024 housing matter, new immigration matter, attendance in
  a housing and a discrimination case, £1,054.25. Both records and both captures are in questions/q01.md and
  verdicts/.
- What the runs showed (routes read from the attempts' own answers; hooks.md "Measured results"):
  - Every stated-rule gate (escape multiples, commencement, scope of the increase) was cleared by every low
    attempt, 15 of 15, whether or not the question's words pointed at it.
  - The only split was rev 0's attendance cell: £49.00 twice (75% of the non-London rate against the single
    printed £52.00) and £34.65 once (proposed row). On rev 1 no attempt made either miss.
  - Run 1's document check: Doc 1 and Doc 3 both needed. Closed book never came near.
- Quick tests: i01, i03, i04, i05 did not survive; i02 and i07 survived and are the two measured versions;
  i08, i09 (subsets of i07) and i06 (£0.1 million, two lookups and a subtraction) untested and closed.
- Decisions and constraints: hooks h1, h11, h12 retired. No third round: no remaining idea rests on a miss this
  solver made (h6 dated bridge, h7 base choice, i06). My repair for rev 1 added gates of the family Run 1 had
  shown solved; lesson recorded in .claude/memory/docket-start-from-measured-misses.md (2026-10-12 entry) and
  docket-local-solver-calibration.md.
- If these bytes come back as another task: start from hooks.md "Measured results"; do not rebuild a stated-rule
  bill; the unmeasured remainder is only the table-against-rule cell on its own, which reached Easy.
- Changed files: questions/q01.md (status dropped, Run 2 record and log); notes/hooks.md, ideas.md,
  feedback-index.md (F1, F2), session.md, events/q01-run2.json, q01-retired.json; workspace memory notes.
- Revision rounds used / open platform feedback: 1 / none open (F1 historical, F2 closed by retirement).
  Sketch rounds used: 2 of 3.
- Five-candidate trial: not enrolled (slots taken). Ledger events: two difficulty attempts, one revision, outcome
  retired_before_submission. Timing partial; tokens unknown.
- Next action and blocker: the user's decision to release the bundle.
- Runtime: Claude Opus 5.5, VS Code extension; no subagents, no diagnostics run.
