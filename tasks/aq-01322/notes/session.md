# Current bundle checkpoint

- Goal and user constraints: user 2026-10-06 "work on AQ-01322 ... difficulty_target to at least
  medium". Task page: slots Hard 0/2 · Medium 0/3 · Easy 0/1; quick tests 0/10; difficulty runs
  8/8; 9 submissions left. Expires Wed 11:12 AM unless saved.
- Verification target / measured platform tier: medium / pending (no platform access here).
- Runs: q01 rev 2 f103b326...aee1; q02 rev 0 bddecd6c...b256; q03 rev 1 f22ab113...d57a (full
  hashes in runs/ folder names). Probe runs: q01-r0-probe-k7/m2, q01-r1-probe-t3, q01-r2-probe-h8/w5.
- Bundle: aq-01322, six Cencora 8-K earnings releases, capture AQ-01322_2026-10-06_1139.txt (.txt
  format; split with docket-e1's splitter). intake.json all matches_capture true, no gaps;
  extraction diff vs originals 0. Ids: D01=Doc 4, D02=Doc 1, D03=Doc 5, D04=Doc 2, D05=Doc 6,
  D06=Doc 3. doc-map complete (bundle-mapper, full coverage).
- Phase: handed over. All three status checked (local only):
  q01 rev 2 ready, medium (marginal): edition trap, Flat; Medium or better ~40-50%; Doc 6
  removal-flag risk ~20-25%. Primary candidate.
  q02 rev 0 revise (target): adj FCF in the OneOncology quarter, $1.16B; Easy ~60%; Easy-slot
  fallback only.
  q03 rev 1 revise (target): Jan-Jun 2025 restatement carve-out, 5.2%; Too easy ~45-50%; reasoning
  Steps 10-11 need doc citations before any use. Not recommended.
- Decisions: q01 is the bundle's only untied edition trap. Avoid EPS windows after May 6, 2026
  (D05 "$17.70 to $17.90" vs D03 $17.65). Restated FY25 annual segment values print only rounded.
  i02 dropped (closed-book reached 7% to 9%); i04 near closed-book ($3.40B vs $3.38B).
- Changed files: questions q01-q03, notes/*, runs/*/results; memory notes (series-editions,
  general-knowledge, platform-quality-checks, MEMORY.md); gpt-project/lessons.md and playbook.md.
- Next action: user quick-tests q01 (optionally q02), runs full form checks (Save passage on the
  Doc 4 Other row; mark only Doc 4 and Doc 6), then the difficulty check; record the platform words.
- Runtime: Claude Code, Opus 5.5; role agents with omitClaudeMd; probes via docket_agent.bind_scope.
