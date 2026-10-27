# Current bundle checkpoint

- Goal and user constraints: user 2026-10-08: "there is no slot for Easy Tier for this bundle, we should target medium and
  high. do your best." Page: Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions, 0 of 10 quick tests.
- Verification target / measured platform tier: medium (hard where possible) / pending, no platform result yet.
- Prepared runs: q01 rev 2 tested_sha256 96e6a6cda1bbcb43aaf17650609786185b165bdb9c28d1bcd9859c14060bafe2; q02 rev 1
  3f07aa5c9392794bb17c691ceb94cf2b41fa0007449e4d717022783f44a99cd5 (dropped).
- Bundle: 5 Cabinet Office papers (Docs 1-4 Civil Service McCloud remedy consultations 2021-22 and 2023 with responses;
  Doc 5 2017 compensation-scheme consultation). Local ids differ: D02=Doc 1, D01=Doc 2, D04=Doc 3, D03=Doc 4, D05=Doc 5.
  Capture complete, no gaps; all five read in full.
- Phase: no live question. q01 (rev 2) and q02 (rev 1) both quick-tested "too easy" and dropped (2026-10-08).
- Questions: q01 response-statistics family closed (stated condition too easy; untied wording reopens Doc 4's
  printed 107 as a second reading). q02 union-list family closed (low model resolved the PGA alias).
- Decisions: no count stated in q02 (list-contract advisory kept: a count would expose the PGA and decoy traps).
  Question lengths 27 and 26 words; watch the form's length-spread advisory.
- Candidate families tried: response statistics (q01), union membership (q02); parked h3-h5, h8 (two lookups + one
  operation); rejected h6 (one-document final rule), h7 (contradictions). See notes/hooks.md, notes/ideas.md.
- Revision rounds: q01 two (wording; reasoning), q02 one (evidence). Platform feedback: F1 (q01 form flag, repaired), F2 (q02 Too easy).
- Feedback index: notes/feedback-index.md (no platform rows yet). Five-candidate trial: not enrolled (all five slots
  were already filled); i01 time recorded in ../../../notes/efficiency.json.
- Next action: user's choice: vet the platform's "Harder variations" for q01/q02, or stop on this bundle. Remaining
  hooks (h3-h5, h8) are two lookups plus one operation; no new fair Medium mechanism found after a full re-search.
- Runtime/model/effort: Claude Code, claude-opus-5-5, effort max (settings.json); subagents blind-solver (Opus 5.5).
- Optional diagnostics run: removal probes (user instruction 2026-10-08) and one full-corpus blind solve per question for
  concrete fairness issues (q01 reading conflict, q02 PGA alias). Raw returns under runs/*/results/.
