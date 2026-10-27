# Current bundle checkpoint

- Goal and user constraints: user 2026-10-10 "there is no slot for Easy Tier for this bundle, we should target
  medium and high. do your best." Target medium, hard welcome. The page saved at 14:21 prints "Hard 0/2 - Medium
  0/3 - Easy 0/1" and "Still open on this set: Hard, Medium, Easy"; asked the user twice whether Easy is really
  closed, no answer yet. The user's instruction governs until they say otherwise.
- Verification target / measured platform tier: medium / Easy on q02 rev 1 (below target, so not `ready`).
  Two difficulty runs used (8 of 10 left).
- Prepared run / tested_sha256: q02 rev 1 = f6fbc2102c7db07e0cf47777435215640a9a146af4f4cd711e03ac85a6d0bbd8
  (runs/q02-r1-...-platform). History: q02 rev 0 = 1fabf5a4..., q01 rev 0 = 258ac5e3... (dropped).
- Bundle: aq-02706 "Bank Merger Act Rulemaking", D01-D07 = Doc 1-7 (identity). Full capture, no gaps.
- Phase: feedback (decision with the user). Sketch rounds used: 2 of 3.
- Questions:
  - q01 rev 0, dropped: 14 moves (D04 x D07). Quick test "too easy" (user chat, no panel). Family h4 closed.
  - q02, checked, origin claude, D01 x D02, gold 583 = 661 - 78 (decoy 558 from D02's later count 636).
    - rev 0 ("every small entity the OCC then counted"): Run 1, Version 14960d, "Answer not supported",
      Low 1/5, high model 558 on all three every-document attempts.
    - rev 1 ("On the count the OCC had published by then"): Run 2, Version 1c9adf, "In band - Easy tier",
      Low 3/5, "You can submit now."; every-document attempt right, both documents needed, closed-book needed
      the documents. Floor 0 FAIL / 3 WARN (origin; 661 and 78 deep in their documents).
    - Raw: verdicts/AQ-02706_difficulty_2026-10-10_1603.txt and ..._1749.txt. Records in q02 Platform
      validation and Feedback log; index rows P3 (resolved) and P4 (open).
    - The form currently holds rev 1 with its passing result: do not edit Question, Answer or documents there
      unless the user chooses to give up the Easy result.
- Sketches: i02 (48.03%) quick test too easy; i03 held (closed family).
- Finding: on q02 the low and high models moved together (soft anchor: low 1/5, high 0/3; firm anchor: low
  3/5, high 1/1). One judgment of this kind has no Medium point, and no independent capability-dependent step
  could be added from D01/D02 (every candidate was single-document or had two defensible answers). Caller and
  two question-author runs found no other cross-document mechanism (hooks h1-h12).
- Recommendation given: submit q02 rev 1 at Easy if that slot is in fact open; otherwise release. No rev 2
  and no third wording. Declared failure mode already matches the observed wrong answer (558).
- Decisions and constraints: notes/hooks.md "Structure of the bundle".
- Feedback index: notes/feedback-index.md rows P1-P4. Calibration memory: aq-02706 entries (quick tests; q02
  ladder).
- Efficiency ledger: ../../../notes/efficiency.json; i01 and i04 unpromoted (trial full); three short timed
  intervals; platform attempts run1-14960d and run2-1c9adf recorded for i04. No active timer.
- Next action: user's decision. If submitted: set status submitted and accepted_tier, freeze q02, later
  observations to notes/feedback-q02.md. If released: mark q02 dropped with the reason.
- Runtime/model/effort: Claude Code, claude-opus-5-5 (caller); agents as pinned.
- Optional diagnostic if needed: none run.
