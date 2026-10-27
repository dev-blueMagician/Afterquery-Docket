# Current bundle checkpoint

- Goal and user constraints: user 2026-10-15, "there is no slot for Easy or Medium Tier for this
  bundle, we should target high. do your best." Page: Hard 0/5, Medium closed, Easy 0/0 (Easy 1 in
  review); quick tests "against the high model" (page), 7 submissions left, 15 difficulty runs.
- Verification target / measured platform tier: hard / none measured.
- Prepared runs: q01 rev 0 runs/q01-r0-v2-9e693c0f...-platform, tested_sha256
  9e693c0f5d75ac75ec3fa3718f27b4f4e5e03bc2601ca0c9b359a1ea26f05327; q02 rev 0
  runs/q02-r0-v2-06c34c9d...-platform, tested_sha256
  06c34c9dcd2d1ff697be00e086eb036afdc301ef592de2567473d6cb57e81d84. No source gaps.
- Bundle: aq-05747; five Coca-Cola earnings releases (Doc 1 = D02 Q2'25, Doc 2 = D04 Q3'25,
  Doc 3 = D05 Q4/FY'25, Doc 4 = D01 Q1'26, Doc 5 = D03 Q2'26); capture complete; not a repeat.
- Phase: checked; full forms handed over (notes/handover-q01.md, handover-q02.md, questions/*.json).
- Questions: q01 checked rev 0 (largest single 2025 impairment = 1,274; lure 960), preflight
  0 FAIL, 4 WARN (strong-screen, origin, units, form-numbers 1,274 deep = expected false alarm).
  q02 checked rev 0 (comparable currency neutral EPS like for like = 1.5 points; lure 0.5),
  preflight 0 FAIL, 2 WARN (strong-screen, origin). Platform results pending.
- Sketches: i01 -> q01, i02 -> q02, both screen 3/3 (ledger rows 38-39) and both survived the
  user's quick test ("i01, i02 all survived"). Sentences and answers carried word for word.
- Open findings: q01 form risks ("Needs two or more documents" if Doc 3 alone is judged enough;
  "Asks about the world" advisory on "together"); q02 "approximately" inputs. User to read "One
  defensible answer" before each run.
- Changed files: questions/q01-q02.md/.json, notes/handover-q01-q02.md, sketches, ideas.md;
  ../../notes/hard-runs.md rows 38-39 (quick test survived, written up).
- Revision rounds used / open platform feedback: none.
- Efficiency: five-slot trial full (promote refused); timers stopped; none running.
- Checks 2026-10-16 (q01, screenshots, unbound): "Question in your own words" Failed (accurate,
  origin claude); "No single passage" advisory warning; One defensible answer, Needs two or more
  documents, Reasoning reaches the answer, Answer matches a stated figure Passed (feedback F1).
- Next action: the user rewrites q01 (and q02, same check) in their own words. For each new
  sentence: report readings against the gold, strong-solver screen on its exact words, record as
  rev 1 origin user+claude, prepare, preflight, full hand-over; never restyle Claude's sentence.
  Then the run, the saved page before Submit, the verdict (docket-feedback), ledger rows 38/39.
- Runtime/model/effort: Claude Opus 5.5 (claude-opus-5-5).
- Optional diagnostic: none.
