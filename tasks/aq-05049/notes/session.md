# Current bundle checkpoint

- Goal and user constraints: user 2026-10-14: "let's work on AQ-05049_2026-10-14_1621. there is no slot
  for Easy or Medium Tier for this bundle, we should target high. do your best." Page (16:21): "Corporate
  filings · Easy or Hard only"; "Still open on this set: Hard"; "Hard 0/5 · Medium closed · Easy 0/0".
- Verification target / measured platform tier: hard / none yet. The check starts at the High model (two
  solvers x 3; both must miss at least once, not every attempt wrong).
- Prepared runs / tested_sha256: q01 rev 0 020c90c4c47e5bc69ede187837da3afc20e0fb7b13ae7dbb8f3fa5d6f7bb0ce2;
  q02 rev 0 80657857049f776a36de5bcc982a4e98b03ec5db88596fa3f5a2593ecd426d60 (runs/qNN-r0-v2-*-platform/).
- Bundle slug / documents: aq-05049 / D01 = Doc 1 (Docusign Q1 FY26 release), D04 = Doc 2 (Q4 FY25),
  D02 = Doc 3 (Q3 FY25), D03 = Doc 4 (Q3 FY25 10-Q), D07 = Doc 5, D06 = Doc 6, D05 = Doc 7 (Paylocity
  Q3, Q2, Q1 FY25) / capture complete 7 of 7, no gaps. New bundle (no repeat in 10.6-10.8).
- Phase: checking; both quick-test survivors written up word for word and handed over.
- Questions:
  - q01 (i10) Docusign total income tax benefit, quarter ended July 31, 2024: $816.3M; lure $837.7M (Note
    13 discrete release). Checked, 0 FAIL / 2 WARN (local screen 3/3; origin). D01 + (D02 or D03).
  - q02 (i02) Docusign buyback cash under the program by Jan 31, 2025: $892M; lure $829M (two printed
    years). Checked, 0 FAIL / 7 WARN (local screen 3/3; origin; four deep-figure form false alarms in Doc
    4: 200.0, 2022, 200,000, 769,641; points-or-percent false positive on "share buybacks"). D03 + D04.
    Open reading named to the user: "fiscal 2025 only" ($684M), weaker since "Altogether".
- History: round 1 screens all 3/3 (i01, i10, i20, i21); my first report withheld them and advised
  release; user objected ("you even didn't give me any questions ... without trying even once?"); all
  fair sketches handed over; user quick test: "1 2 failed, 3 4 survived" (i20, i21 failed; i10, i02
  survived). hard-runs.md rows 7-11; efficiency outcomes: i01/i20/i21 retired, i10/i02 pending.
- Decisions and constraints: Hard playbook (screen ranks, never withholds); survivor sentences word for
  word; one declared mode each (the lazy-default wrong answer); no tier odds; ask for the capture before
  Submit in the last message before any run; read "One defensible answer" before a run.
- Changed files: questions/q01.md, q02.md (+ .json), notes/handover-q01.md, handover-q02.md, ideas.md,
  hooks.md, session.md, sketches/i01, i02, i10, i11, i20, i21.md; runs/*; workspace notes/hard-runs.md,
  notes/efficiency.json.
- Five-candidate trial: not enrolled (promote refused: all five slots enrolled). Timer: peer-held; time
  not recorded.
- Next action: user pastes q01/q02 (own words for the own-words checks), reads Checks ("One defensible
  answer" first), runs difficulty; send the saved page before Submit to align failure modes.
- Runtime/model/effort: Claude Code in VS Code, claude-opus-5-5.
