# Current bundle checkpoint

Replace this file at each phase boundary; keep it under 4,000 characters.
It is working memory for resuming the bundle and is never submitted.

- Goal and user constraints: user 2026-10-08: no Easy slot, "target medium and high". Latest report: "q01 and q04 is too easy to pass quick test. q05 is too hard ... I added verdict".
- Measured so far: q01 rev 1-3 question Too hard (Run 1, version d017fd, 0/15, all at 22.69%); q01 rev 4 quick test too easy; q02, q03, q04 quick tests too easy (dropped); q05: user says "too hard", but the attached 13:59 capture holds only q01's stale Run 1 ("for an earlier version"; still "7 of 8 runs left"), so no q05 platform text is on file.
- Phase: handed over (2026-10-08): q01 rev 5 (9a5dcb40...) and q05 rev 2 (f70bb5c4...), both checked; q02, q03, q04 dropped.
- q01 rev 5: "How much did the assets for which State Street was actually the investment manager grow between June 30, 2025 and June 30, 2026, in percent to two decimal places?" Gold 22.40%. Midpoint between the Too hard (no cue) and too easy ("as opposed to all of its reported AUM") wordings; last wording step for this family. FMs: Part vs total (22.69%, Alternatives 22.96%), Linking across documents (19.62%, 23.41%).
- q05 rev 2: "...from the latest figure it had published before it launched its Digital Asset Platform to its figure for June 30, 2026? Give the sign and round to one decimal place." Gold -16.5% (Doc 7 $401M to Doc 10 $335M); decoy Doc 8's own $320M (+4.7%). Rev 1's "when it launched" could be read as the launch release's own figure.
- Feedback: notes/feedback-index.md r1-r7; trial slots 4 (i14 = q04, retired) and 5 (i15 = q05, rev 2); owner workspace notes/feedback-index.md, ledger notes/efficiency.json.
- Next: user reloads the page, pastes q01 rev 5 and q05 rev 2 whole from notes/handover-q01.md / -q05.md, runs quick tests and, if they survive, difficulty runs (7 of 8 left); save each capture to verdicts/ right after its own run. If q01 rev 5 fails either way, retire the family. If q05 rev 2 is too easy, retire it; if Too hard, redesign. Ask for the q05 quick-test text if there was one.
- Runtime: Claude Code VS Code extension, Opus 5.5 max; no local model runs.
