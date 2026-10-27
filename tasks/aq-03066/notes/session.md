# Current bundle checkpoint

- Goal and user constraints: AQ-03066 (NZ Commerce Commission fibre input methodologies: six December 2018
  submissions, emerging views summary paper 21 May 2019, workshop pack 25 June 2019). User 2026-10-11: no Easy slot,
  "target medium and high". Page: Hard 0/2, Medium 1/3, 10 quick tests and 10 difficulty runs unused at capture.
- Verification target / measured platform tier: medium / pending (nothing run yet).
- Prepared run / tested_sha256: runs/q01-r0-v2-e75da35c...-platform / e75da35cf12664c47ebfe20907ed55f04ca4f2bc61d3e1229fcc53e7ccf1a8d4
- Bundle slug / documents / extraction warnings: aq-03066; D01 = Doc 4 Chorus, D02 = Doc 6 CCHL, D03 = Doc 2 workshop
  pack, D04 = Doc 1 summary paper, D05 = Doc 8 InternetNZ, D06 = Doc 7 Axiom, D07 = Doc 5 Spark, D08 = Doc 3 Vodafone.
  All complete. Figures absent as text; D03's capex snapshot table is garbled (not used).
- Phase: round 1 closed (q01 and i02 both quick-test too easy, user chat 2026-10-11); round 2 sketching with two
  independent question-author runs.
- Questions: q01 rev 0 dropped (quick test too easy; no difficulty run spent). 2 of 10 quick tests used.
- Decisions and constraints: answer asked as a whole-percent fall because a rounded plain result cannot clear the
  form's number check; reasoning carries exact decimals (44 two-operand steps). q01 and i02 share D03's table: submit
  at most one.
- Candidate families tried / shortcut routes / source completeness: see notes/hooks.md (h1-h7). Spark, Axiom and
  Chorus print no usable figures; the only worked calculation is D03's appendix table.
- Changed files: notes/doc-map.md (+ doc-map-D01/D06/D07.md from mappers), hooks.md, ideas.md, sketches/i01.md,
  sketches/i02.md, questions/q01.md, q01.json, notes/handover-q01.md, runs/q01-r0-...
- Revision rounds used / open platform feedback: 0 / none.
- Active feedback index: ../../../notes/feedback-index.md (no entry yet; nothing returned).
- Five-candidate trial: all five slots already enrolled by other bundles; this work is tracked as unpromoted.
- Efficiency ledger / candidate / timer: ../../../notes/efficiency.json / aq-03066 i01 / none running (one sketch
  interval measured 2026-10-11; mapping time before it unmeasured, so timing coverage is partial).
- Round 2 (2026-10-11): two independent question-author runs both reached hook h8 (three companies' positions on
  the quality dimensions, Spark's stated as one grouped clause). Sketches offered for quick tests: i03 (list, gold
  ordering, provisioning, switching, faults), i05 (total, gold 14), optional i04. No figure-based design outside the
  closed table family met the necessity and exactness constraints (notes/hooks.md).
- Round 2 result (user chat 2026-10-11, "both of them too easy to pass quick test"): i03 and i05 too easy. 4 of 10
  quick tests used, 0 difficulty runs. Families closed: named-rule reruns of D03's table (h1, h2) and the
  quality-dimension membership (h8).
- Round 3 search by the caller found no fair design with a different mechanism: every remaining join is a date gap,
  a list diff, two lookups and one subtraction (the 5.56% / 6.09% copper WACC pair), a bridge into one cell, or rests
  on a statutory fact repeated across documents. Untested fair sketch left: i04 (ideas.md), expected too easy.
- Next action: user decides between releasing the bundle (recommended) and a last quick test of i04. Nothing is
  prepared or pending on the platform.
- Runtime/model/effort: Claude Opus 5.5 (claude-opus-5-5) in the VS Code extension; three bundle-mapper subagents.
- Optional diagnostic: none run (no removal probes, blind solves or reviews).
