# q01 rev 0 - closed-book diagnostic (optional, local)

- Date: 2026-10-10
- Bound to: q01 rev 0, tested_sha256 557d1f45c762fd58332d131ea8e9e203c9e0bd8b44e5fbd032fbaf71caea6d71
- Why it ran: a concrete necessity question. Doc 3's only indispensable input is the ICCAT North Atlantic
  swordfish TAC for 2025-2027 (14,769 mt), a public figure; the platform's Document check leaves each ticked
  document out in turn.
- Role: closed-book-solver (fresh context, question text only, no tools used). Model: the session's Claude
  model, not the platform's solver. It says nothing about a platform tier.
- Input, verbatim: "What percentage of the 2025 North Atlantic swordfish total allowable catch was U.S.
  underharvest not carried into 2026, to one decimal place?"

## Return, verbatim

answer: unknown

confidence: low

basis: Memory only, no tools called. I recall the general framework: an ICCAT North Atlantic swordfish TAC of 13,200 t ww, possibly raised to about 14,769 t under the 2024 management procedure; a U.S. baseline quota of about 2,937.6 mt dw (3,907 t ww); and carryover capped at 15% of baseline (about 440.6 mt dw). I do not recall the actual 2025 U.S. underharvest figure or which TAC the source uses, so a one-decimal answer is not derivable. Rough ballpark only: 15-18%.

contaminated: minor. The session auto-attached a git status snapshot (workspace file paths including task ID aq-00949, run directory names, memory file names) and a user email. No question content, answer key, document excerpts, hints or earlier results were visible, and none of it informed the answer.

## Reading (author)

- The question is not answerable closed-book: the 2025 underharvest is not recalled.
- The model does recall the Doc 3 input, 14,769 t, though hedged beside the older 13,200 t. With Doc 6 present
  and Doc 3 left out, a solver that recalls 14,769 reaches the gold (2,758.819 / 14,769 = 18.7%); one that
  uses 13,200 gets 20.9%. So Doc 3's necessity for q01 rests on a recallable public figure: a stated risk
  for the form's "Needs two or more documents" check, not a measured failure.
- The return reports minor contamination (workspace paths only), so it is not a clean blind record.
