# Current bundle checkpoint

- Goal and user constraints: user 2026-10-06 "work on AQ-01322 ... difficulty_target to at least
  medium". Task page: slots Hard 0/2 · Medium 0/3 · Easy 0/1; quick tests 0/10; difficulty runs
  7/8 after q03's run (2026-10-06); 9 submissions left. Expires Wed 11:12 AM unless saved.
- Verification target / measured platform tier: medium / q01 rev 3 accepted_tier medium (user report
  2026-10-07, submitted); q03 rev 1 Too easy (Low 4/5); q02 unmeasured.
- Runs: q01 rev 3 32031947...0eeb (rev 2 f103b326 superseded); q02 rev 0 bddecd6c...b256; q03 rev 1 f22ab113...d57a (full
  hashes in runs/ folder names). Probe runs: q01-r0-probe-k7/m2, q01-r1-probe-t3, q01-r2-probe-h8/w5.
- Bundle: aq-01322, six Cencora 8-K earnings releases, capture AQ-01322_2026-10-06_1139.txt (.txt
  format; split with docket-e1's splitter). intake.json all matches_capture true, no gaps;
  extraction diff vs originals 0. Ids: D01=Doc 4, D02=Doc 1, D03=Doc 5, D04=Doc 2, D05=Doc 6,
  D06=Doc 3. doc-map complete (bundle-mapper, full coverage).
- Phase: q01 submitted (frozen; later findings go to notes/feedback-q01.md). Others:
  q01 rev 3 ready, medium (marginal): edition trap, Flat; rev 3 only swaps "the group of businesses"
  (form rule-10 warning) for "the reporting category"; Medium or better ~45-50%; Doc 6 removal-flag
  risk ~20-30%. Primary candidate; measure before any further change.
  q02 rev 0 revise (target): adj FCF in the OneOncology quarter, $1.16B; Easy ~60%; Easy-slot
  fallback only.
  q03 rev 1 REJECTED: platform difficulty check Run 1 "Too easy", Low 4/5 (closed-book 1.3%, miss
  at 5.7% from the fiscal six-month tables); Coach's "which businesses" rewrite needs outside
  knowledge, not adopted. Piped evidence quotes passed the form's verbatim check.
- Decisions: q01 is the bundle's only untied edition trap. Avoid EPS windows after May 6, 2026
  (D05 "$17.70 to $17.90" vs D03 $17.65). Restated FY25 annual segment values print only rounded.
  i02 dropped (closed-book reached 7% to 9%); i04 near closed-book ($3.40B vs $3.38B).
- Changed files: questions q01-q03, notes/*, runs/*/results; memory notes (series-editions,
  general-knowledge, platform-quality-checks, MEMORY.md); gpt-project/lessons.md and playbook.md.
- Next action: none required. Optional: q02 for the Easy slot; new Medium/Hard designs need a fresh
  mechanism (no second untied edition event in this bundle). Paste the exact submitted q01 text if
  the local record should hold it (notes/feedback-q01.md).
- Runtime: Claude Code, Opus 5.5; role agents with omitClaudeMd; probes via docket_agent.bind_scope.
