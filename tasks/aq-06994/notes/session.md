# Current bundle checkpoint

- Goal and user constraints: user (2026-10-19): "no slot for Easy or Medium Tier for this bundle, we should
  target high. do your best." Repeat of aq-06801 (identical document bytes); asked per the standing rule, the
  user chose "Proceed, new stacks". Hard target; sketches first, screened, every fair sketch handed over.
- Verification target / measured platform tier: hard / none yet on aq-06994 (aq-06801 q01 High 3/3 Too easy).
- Prepared run / tested_sha256: none (no question file; sketches only).
- Bundle slug / documents (ids) / extraction warnings: aq-06994, 7 docs complete (capture
  AQ-06994_2026-10-19_0421.txt); D01=Doc 6, D02=Doc 7, D03=Doc 5, D04=Doc 4, D05=Doc 1, D06=Doc 3, D07=Doc 2.
  D02 segment table shifts prior-year cells. Map reused from aq-06801 (hashes match), all seven re-read 10-19.
- Phase: sketching, round 1 handed over (i01-i03), awaiting the user's quick tests.
- Questions: none.
- Screen results (blind-solver claude-opus-5-5 max): i01 3/3, i02 3/3, i03 3/3 (9 of 9 right, all high
  confidence); ledger rows 116-118; raw returns in runs/iNN-screen-*/solve-1..3.md.
- Decisions and constraints: aq-06801 families closed (Iridium Q2 selector, ARPU footnote, Comtech Q4 net
  income, trailing Adjusted EBITDA margin, preferred derivative). New mechanisms: 3M move on Comtech's fiscal
  Q4 2025 (i01, i03), net carrying vs borrowings with a 10-Q-only base date (i02). i01 needs D02 (D01's 14.8%
  alone reaches 2.48%). Rejected: h18 make-whole (D02 alone), h20/h21 Iridium net leverage (signpost / D06
  alone), h22 preferred holders' claim (lenders of later tranches unnamed), h23 (closed family).
- Changed files: notes/doc-map.md, hooks.md, ideas.md, sketches/i01-i03.md, runs/i0[1-3]-screen-*,
  ../../../notes/hard-runs.md rows 116-118.
- Five-candidate trial / timing: not enrolled; unmeasured (aq-06932 session held the single timer) -> partial.
- Next action and blocker, if any: user quick-tests i01-i03 (0 of 20 used); on a survivor, write it up word
  for word (prepare, preflight, full hand-over, ask for the capture before Submit). If all fail: round 2
  (reserve h19, or new hooks), or release, the user's choice.
- Runtime/model/effort: Claude Opus 5.5 (claude-opus-5-5); blind-solver role pinned to claude-opus-5-5, effort max.
- Optional diagnostic if needed: none
