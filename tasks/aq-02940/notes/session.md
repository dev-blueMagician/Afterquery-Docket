# Current bundle checkpoint

Replace this file at each phase boundary; keep it under 4,000 characters.

- Goal and user constraints: aq-02940 "Public policy", 16 documents from the NZ Commerce Commission's 2026 consultation on commercial credit card interchange caps. User, 2026-10-11: "there is no slot for Easy Tier for this bundle, we should target medium and high. do you best." Difficulty runs left: 9 of 10.
- Verification target / measured platform tier: medium (Hard welcome) / Easy. Run 1, q04 rev 0: "Between levels", Low 0/5, Medium 5/5. Run 2, q06 rev 0: "In band - Easy tier", Low 3/5 (a pass below target; user: "easy tier but no slot for that"). Difficulty runs left: 8 of 10.
- Prepared runs / tested_sha256: q06 rev 0 11f51dc8ef9b4931a5bbf087dbcdc5a4e82f89824a1d12fcb7cb4b8c87db0fa7 (the version on the platform, Easy pass recorded); q04 rev 3 0a5f5f69... (never run). History: q04 rev 0 fa9effab... (Run 1), rev 1, rev 2 (quick test too easy).
- Bundle / documents: D01-D16, complete. Local ids differ from the page: D13 = Doc 1, D09 = Doc 2, D06 = Doc 8, D01-D05 = Docs 3-7, D07 = Doc 9, D08 = Doc 10 (Mastercard), D12 = Doc 11, D14 = Doc 12, D15 = Doc 13, D16 = Doc 14 (Westpac), D10 = Doc 15, D11 = Doc 16.
- Phase: feedback recorded; hook h13 exhausted for Medium; decision returned to the user.
- Questions (origin claude):
  - q06 rev 0 (i12, h13): lowest and highest proposed caps, Mastercard's minimum lead times and Westpac's timing requests, 292 days and 384 days. Run 2 Easy, Low 3/5 (misses 274 and 365: no first of the month); Document check needed Docs 1, 10, 14. Status checked (pass below target).
  - q04 rev 0 (ASB + Westpac, 262 days): Run 1 Between levels; low 5 x 243, medium 5 x 262. q04 rev 3 (highest cap, 384 days) survived one quick test, never run.
  - Dropped: q01, q02, q03, q05. Held sketches: i08 (0.29 points), i10, i04 (all same family as the round-1 failures or untested).
- What the two runs show (author's reading): the only mechanism that separates the solvers here is Westpac's first-of-month sentence. With ASB's lead date twelve days past Westpac's printed 1 March 2027 the low solver stops early (0/5) but the medium solver always reads on (5/5); with Mastercard's later dates the low solver reads on too (3/5). No fair second gate for the medium solver was found (searched: cap identity, extra parties, slack, cost of delay, seasonal remarks, which are ambiguous).
- Decisions and constraints: Doc 1 holds every rule. Quick tests measure only the low solver; the buried first-of-month clause holds low at 0/5 but medium reads it every time, so rev 1 adds a second gate (which caps, hence which of Mastercard's two lead times). No which-submitter answers (rule 10).
- Changed files: questions/q06.md (Platform validation, Feedback log); notes/feedback-index.md (P7), ideas.md, hooks.md, session.md.
- Sketch rounds used: 2 of 3. Feedback index: P1-P7, none open.
- Efficiency ledger: ../../notes/efficiency.json; i09 timed (sketch, draft, revision), one difficulty attempt and one revision recorded; no timer open.
- Next action: user decides: release the bundle (recommended), submit q06 if an Easy slot is usable, or ask for a third sketch round on a different hook (low odds; 8 difficulty runs and few quick tests left).
- Runtime: Claude Code, claude-opus-5-5, 2026-10-11. Optional diagnostic: none run.
