# Current bundle checkpoint

Replace this file at each phase boundary; keep it under 4,000 characters.
It is working memory for resuming the bundle and is never submitted.

- Goal and user constraints: user 2026-10-08: no Easy slot, "target medium and high. do your best", plus "check
  arrived verdicts with the feedback skill and fix". The length warning blocks the user in practice, so questions are
  about 12-20 words; the reasoning box must clear the form's number check (bare exact "a op b = r" steps).
- Verification target / measured platform tier: medium (hard welcome) / q02 rev 1 measured Too hard (0/15); rev 2 pending
- Prepared run / tested_sha256: q02 rev 2, runs/q02-r2-v2-c9e651b9...-platform, c9e651b935eb54e9dc9e6e9fe1cbf6de0da7719814573d17272fdfcd63eb9e6a
  (rev 1 1d3d4551..., rev 0 9d1e4488...; q01 dropped, last snapshot rev 4 5007fa6a)
- Bundle slug / documents / extraction warnings: aq-02028; D01-D20 = Doc 1-20; 20 Productivity Commission maritime
  logistics submissions (Feb 2022); complete, no gaps; text = NFKC(source); 2 ellipses in D06, 5 in D07.
- Phase: feedback triaged (F5), rev 2 checked, hand-over given; platform pending.
- Questions: q01 dropped (quick test "Too easy" on rev 4, F3). q02 checked rev 2, floor 0 FAIL / 1 WARN (origin), 20 words:
  yearly truck trips saved at 4 TEU loads vs VTA's current 2.5 (Doc 8) on the whole-port throughput stated by the newest
  terminal, VICT (Doc 1, 2.88m TEU) = 432,000. Traps: 450,000 (Doc 8's printed figure on its own 3m base), 120,000 (VICT's
  own 800k). Hand-over notes/handover-q02.md; JSON questions/q02.json.
- Rev 1 platform result (verdicts/AQ-02028_difficulty_2026-10-08_1348.txt, version cdda71): Too hard, Low 0/5 · Medium 0/5 ·
  High 0/5, "may be too vague". 9/15 read "port throughput [the terminal] states" as VICT's own 800k (120,000), 1 took 1.5m,
  5 took Doc 8's printed 450,000. Rev 2 = one focused repair ("whole-port"); the Coach's 120,000/450,000 golds rejected.
- Decisions and constraints: rule 10 excludes submitter-name/document-count answers. The easier solver solved a
  two-document date anchor (q01), so q02 relies on a printed same-scenario decoy beside the method. Rev 1 left 3.5 TEU
  because 2.88 / 3.5 never terminates.
- Candidate families tried: h1-h8 in notes/hooks.md; parked h2 (wine share), h3 (NSC basis), h6 (Port Botany growth);
  rejected same-label conflicts. Map: notes/map/partA-D.md (all 20 read in full), summary in doc-map.md.
- Open risks (stated at hand-over): with the scope named, solvers may find 2.88m easily (Easy/Too easy possible); Doc 8's
  method ignores Melbourne's 6% rail share (Doc 5 L266; road-only 406,080; one Medium attempt kept the method); "over 2.88 million".
- Changed files: tasks/aq-02028/** (scaffold, docs, text, notes, map parts, sketches i01-i04, q01/q02 .md/.json, runs/).
- Revision rounds used / open platform feedback: q01 4 (dropped); q02 2 (F4 rev 0 form flags; F5 rev 1 Too hard).
- Active feedback index / issue ids / current fix: notes/feedback-index.md F1-F3 (q01, closed); F4 closed; F5 -> rev 2
- Five-candidate trial: slot 3 = i01 -> q01, retired before submission (ledger outcome event); trial full, q02 not enrolled.
- Efficiency ledger / candidate ID / active timer ID: ../../../notes/efficiency.json / i01 / none (another session
  holds the single global timer; timing unknown, not estimated)
- Next action and blocker: user pastes handover-q02.md (rev 2) and runs the difficulty check (7 of 8 runs left). If it is
  Too hard or "too vague" again, retire the hook; if Too easy, report that no fair Medium mechanism remains (i04 is likely
  easier) rather than reword.
- Runtime/model/effort: Claude Opus 5.5 (claude-opus-5-5), VS Code extension session
- Optional diagnostic if needed: none run; none required
