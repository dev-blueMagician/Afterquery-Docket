# q04 rev 1 - independent review (summary of the verbatim return)

- Date: 2026-10-06. The rev 0 question-review agent (claude-opus-5-5), resumed with a delta request
  naming the changed fields and the fresh rev 1 returns; it re-read the files itself. No writer
  conversation beyond that request.
- tested_sha256: c199d813c5fd35ac6b473e5fd6f893b5718e5eca410e0066b2d8dad87e8fb1ce

## Key lines (quoted or closely summarised from the task notification)

- "Rev 1 is still revise, with difficulty easy. The form changes work, and correctness and fairness
  all hold on the new fingerprint."
- Binding: report tool recomputes c199d813...; question, answer, components, documents, tags and levers
  byte-identical to rev 0; corpus hashes identical; floor 0 FAIL, 1 WARN (origin).
- gold_verified: yes (739 / 3,635 = 20.3301%). Outcome: A match, B match (fresh rev 1 packets, high).
  Closed-book: misses ("unknown", rough 22-25%). Necessity unchanged {D10, D12}; rev 0 probes still
  apply (question, answer, documents and corpus byte-identical). Shortcut: clear. No source gaps.
- Difficulty: easy; "Too easy about 40%, Easy about 45%, Medium about 10%, Hard or Too hard about 5%."
- Finding 1 (new): Steps 4 and 6 cite only Doc 12 while their derived operands (1,856; 406) came partly
  from Doc 10; write "Doc 10 and Doc 12" (risk low to moderate; the form rule is inferred).
- Finding 2: all ten quotes verbatim (with and without pipes); five are pipe rows (D10 l.25, l.27,
  l.245; D12 l.428, l.444); the Warnings line lists only three; each necessary document keeps
  plain-text quotes (D10 l.13, l.17, l.233; D12 l.420, l.457).
- Finding 3: rev 0 findings closed (Step 2 link to the 2026 structure; decoy line; one operation per
  step apart from finding 1); open as expected: Save passage step and difficulty; optional: Entity
  resolution tag, summary-only probe record; set with q01 unchanged (can sit together).
- Finding 4: no new solver-facing risk (41 words; no em or en dashes, no semicolons).
- Recommendation: leave question and answer; quick-test the current pair now; put finding 1 and the
  five-row Save passage list into rev 2, then fresh A/B, audit and closed-book on its fingerprint.
