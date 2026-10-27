# q04 rev 0 - closed-book diagnostic (optional, local)

- Date: 2026-10-10
- Bound to: q04 rev 0 (tested_sha256 in notes/handover-q04.md; the question text below is the tested wording)
- Why it ran: a concrete necessity question. Both of q04's deciding facts concern public ICCAT/NMFS figures
  (the 2025 U.S. bluefin baseline quota and the origin of the 25 mt longline allowance).
- Role: closed-book-solver (fresh context, question text only, no tools used). Model: the session's Claude
  model, not the platform's solver. It says nothing about a platform tier.
- Input, verbatim: "Before any underharvest or overharvest adjustment, how many more metric tons of the western
  Atlantic bluefin tuna total allowable catch was the United States allocated for 2026 than for 2025, to two
  decimals?"

## Return, verbatim

answer: 174.24 metric tons (US allocation about 1,490.38 mt for 2026 vs 1,316.14 mt for 2025; with the 25 mt NED bycatch allowance, 1,515.38 vs 1,341.14, same difference)

confidence: medium

basis: Memory plus arithmetic, no tools called. The 2025 figure of 1,316.14 mt is 49.00% of the 2,726 t ICCAT western TAC less 40 t of bycatch set-asides. For 2026 I recall the TAC rising to 3,081.6 t; the same formula gives (3,081.6 - 40) x 0.49 = 1,490.38. Uncertain points: the exact 2026 TAC and whether the 49% allocation key was unchanged.

contaminated: Partial. An auto-attached git status snapshot (workspace file names, task id aq-00949, commit titles) and the user email were present. No project instructions, answer key, document excerpts, hints or earlier results were visible, and nothing bore on the answer.

## Reading (author)

- Closed-book answer 174.24, not the gold 168.84: without the documents the solver does not know that the
  2026 quota is 49 percent of the whole TAC (1,509.98) or that the new allowance comes from the eastern TAC.
- It does recall, exactly, the 2025 baseline quota (1,316.14 mt), the 25 mt allowance and that this allowance
  came out of the western TAC (2,726 t "less 40 t of bycatch set-asides"), and the 2026 TAC (3,081.6 t).
  Consequence for the form's "Needs two or more documents" check, which leaves each ticked document out in
  turn: without Doc 6, Doc 3's 1,509.98 plus the recalled 1,316.14 + 25 reaches 168.84; without Doc 3, Doc 6's
  table plus the recalled origin of the 25 mt also reaches it. Both ticks therefore rest partly on facts a
  strong solver may know. A stated risk, not a measured failure.
- The return reports partial contamination (workspace paths only), so it is not a clean blind record.
