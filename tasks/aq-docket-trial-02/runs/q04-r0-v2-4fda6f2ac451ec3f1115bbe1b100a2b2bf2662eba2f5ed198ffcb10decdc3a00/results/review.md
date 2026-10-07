# q04 rev 0 - independent review (summary of the verbatim return)

- Date: 2026-10-06. Fresh question-review agent (claude-opus-5-5), given the frozen question file,
  corpus, raw returns, removal-probe packets, target and the user's reported platform results for
  q01/q03, without the writer's conversation.
- tested_sha256: 4fda6f2ac451ec3f1115bbe1b100a2b2bf2662eba2f5ed198ffcb10decdc3a00

## Key lines (quoted or closely summarised from the task notification)

- Verdict: "revise". "The gold and fairness checks hold up, but I expect Medium only about 10% of the
  time against your Medium target, and the form fields need small fixes before submission."
- Fingerprint: the report tool recomputes the same fingerprint; floor 0 FAIL, 1 WARN (origin).
- gold_verified: yes, three ways with exact fractions: full year + H1 2026 - H1 2025 (3,635 / 739);
  four quarters with Q4 = FY - 9M; H2 2025 (1,856 / 406) + H1 2026. "739 / 3,635 = 20.3301%, so
  20.33%. That is 0.0049 below the 20.335 rounding boundary."
- One clear answer: each input printed once; recast comparatives in D10, D11, D12 agree; cost-line
  rebuilds (383, 200, 582) give 20.36% or 20.39% (solver error, "Table may not sum due to rounding");
  quarterly-margin average 20.29%; as-reported mixes 19.11% and 19.14% contradict "that segment" as
  defined from 2026. "Without the pin, 19.11% would become defensible, so the pin has to stay. Inside
  the pin I found no second reading."
- Outcome: A match, B match (fresh, separate, uncontaminated, high confidence). Closed-book: misses.
- Necessity: {D10, D12} is the smallest valid set. D10 the only source of new-basis 2025 North America
  beyond the first half (estimates without it 19.14%-20.21%; probe 20.04%). D12 the only source of Q2
  and H1 2026 (estimates without it 18.69%, 18.94%, 20.04%). D11 and D09 must stay unmarked.
- Shortcut: clear. Source assessment: no gaps.
- Difficulty: easy (below target). "Too easy about 40%, Easy about 45%, Medium about 10%, Hard or Too
  hard about 5%." Leans easy: the pin names the deciding fact; D12 l.83 points to recast history; D10
  is titled "Segment Information (Recast)"; labelled cells; standard twelve-month build; no printed
  answer-shaped figure (unlike q01's 7.0%); profile like q03. Could push up: D09's heading "Twelve
  Months Ended December 31, 2025" echoes the question; several plausible mixed routes (18.32%, 19.11%,
  19.14%, 19.67%, 19.75%); any $1M slip flips the second decimal; aq-00998 q05's twelve-month build
  drew Low 2-3/5. The pin weakens the D09 decoy but cannot be removed.
- Finding 1: precision objection risk small (company percentages use unrounded data); q01 used the
  same convention.
- Finding 2: number check clean except a working-rule risk: Steps 3 and 4 chain three operands; split
  each into one-operation steps.
- Finding 3: all seven quotes verbatim; three pipe rows carry all six inputs; re-save via Save passage
  (a new revision).
- Finding 4: Step 2 should show that D10 is the 2026 recast (its six-month 2025 row equals D12's recast
  comparatives; it shows the EMEA segment), since the bundle has two recasts.
- Finding 5 (minor): the decoy line attributes "structure used before 2026" to D09, which D09 does not
  say.
- Finding 6: tags fit (Aggregation would also fit); components and wording fine (41 words, one ask).
- Finding 7 (minor): the without-D10 probe is stored as a summary with quoted key lines.
- Finding 8: q04 can sit beside q01 (no giveaway; shares D10 and the realignment theme only); no
  overlap with q02.
- Wording recommendation: keep the question and answer; quick-test this exact pair now. If "Too
  easy", stop or redesign; if it survives, make rev 1 with form-only changes (findings 2-4), re-run A,
  B, the audit and the closed-book solve on the new fingerprint, then run the difficulty check.
