# Current bundle checkpoint

- Goal and user constraints: user 2026-10-08: "there is no slot for Easy Tier for this bundle, we should target medium
  and high. do your best." Page: Hard 0/2 · Medium 0/3 · Easy 0/1; "7 of 8 runs left" after q01's run.
- Verification target / measured platform tier: medium (hard possible) / no pass yet.
- Platform results:
  - q01 rev 0 (9563e169...) Run 1, Version 8b4bdc: "A marked document may not be needed" (without Doc 3 the high model
    used Doc 4's identical case study), Low 2/5 · Medium — · High —. Raw: verdicts/AQ-02147_difficulty_2026-10-08_1706.txt.
  - q03 rev 0 (ea5426d5...) quick test: "Too easy — solver got it". Raw: platform-feedback/q03-rev0-quick-test-2026-10-08.png.
- Bundle: five DWP/DHSC papers. Local ids: D04 = Doc 1, D02 = Doc 2, D05 = Doc 3, D01 = Doc 4, D03 = Doc 5. Capture
  complete, no gaps, all read in full (notes/doc-map.md).
- Questions: q01 dropped (h1: profile duplicated in Docs 3/4; Easy band). q03 dropped (h9: two table lookups, too easy).
  q02 checked rev 0 (b01169fc...): employers' median on Doc 4's £175 case -> Week 3; same mechanics as q01 but simpler,
  so expected too easy; quick test only if the user wants it.
- Decisions: each necessary document must hold an input no other document carries; look-alikes excluded by the
  question's own nouns do not catch the low model. Rounds used: 2 measured (q01, q03) of the workflow's 3.
- Candidate families: h1, h9 closed; h2 (q02) open; remaining h3-h5 are simpler than q03 or fail necessity (h3: Doc 5's
  only input is the recallable 80%; h5: Docs 1 and 2 duplicate the 2019 figures); h6-h8 rejected (notes/hooks.md).
- Feedback index: notes/feedback-index.md F1, F2 (q01), F3 (q03).
- Efficiency ledger: not in the five-candidate trial (slots full); i01 attempt and retirement, i03 retirement recorded.
- Next action: user opens "Harder variations" on q03 (or "Ask the Coach why") and pastes the suggestions; vet each for
  one defensible answer, two indispensable documents and a fair trap before any new run. Otherwise stop on this bundle.
- Runtime/model/effort: Claude Code, claude-opus-5-5, effort max. Optional diagnostics run: none.
