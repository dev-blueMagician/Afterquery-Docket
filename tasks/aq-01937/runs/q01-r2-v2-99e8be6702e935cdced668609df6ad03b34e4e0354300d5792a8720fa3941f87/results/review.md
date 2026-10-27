# q01 rev 2 independent re-review (fresh question-review), 2026-10-08
tested_sha256: 99e8be6702e935cdced668609df6ad03b34e4e0354300d5792a8720fa3941f87

Summary: locally sound (gold checks out from originals, A and B match, closed-book misses, audit clear, both probes refuse); rev 1 findings resolved. Still: difficulty below target (easy against medium); notes/handover-q01.md was stale (rev 1) and must be regenerated before pasting.

gold_verified: yes. Decimal arithmetic from docs/: Doc 10 L58 6,278 (2Q26) and 5,117 (2Q25); Doc 10 L360 about $157B; Doc 6 L394 about $116B; Doc 6 L223 dates 5,117 at June 30, 2025 (unchanged in Docs 7-10). 6,121 / 5,001 - 1 = 22.395521% -> 22.40% (half-up and half-even; truncation 22.39; 0.00052 points above the boundary; $ billions, rounding once). Other readings: headline 22.69%; end-only 19.62%; start-only 25.53%; whole Alternatives 22.96%; rounded trillions 23.25% / 23.53%; March/September amount 22.15% / 23.11%; midpoint 22.63%; Alternatives interpolation 22.42%. Gold needs June 2025 amount in [115.979, 116.387] and June 2026 in [156.526, 157.026]. Floor 0 FAIL, 1 WARN; fingerprint 99e8be67...; no source gaps; no platform record.

outcome: A: match; B: match (22.40% high confidence, separate packets; both rejected 22.69% and 22.96%; citations check out). Not re-audited by the reviewer (transcript store access denied); independence rests on the recorded audit_transcript2.py results.

closed-book: misses ("unknown").

necessity: Doc 6 only source of the June 30, 2025 carve-out; every other release prints only its own quarter-end amount (Doc 2 $83B, Doc 3 $82B, Doc 5 $106B, Doc 7 $145B, Doc 8 $173B, Doc 9 $184B, Doc 10 $157B); best estimates without Doc 6 give 22.15%, 22.42%, 22.63%, 23.11% or the headline 22.69%; rev 2 probe (renumbered packet verified against originals) "cannot be determined", forced 22.69% (p 0.30). Doc 10 only source of 6,278 and the June 2026 amount; probe "cannot be determined", forced 8.70%. {Doc 6, Doc 10} the only minimal set.

shortcut: clear. Route Doc 10 L58 -> L189 (note 2) -> L360 -> Doc 6 L394; two subtractions and a ratio; no passage, overview line or value search (22.4, 22.39, 1,120, 5,001, 6,121) gives the adjusted AUM or its growth. "investment manager" leads to note (2): finds an input, not the answer; a difficulty risk, not a Guide violation.

source_assessment: no intake gaps; doc-map visual gaps (Doc 1 charts, Doc 4 slides) and the uncaptured non-GAAP Addendum contain no quarter-end AUM or SPDR amounts; no effect on premises, gold, exclusions, uniqueness, necessity, shortcut.

difficulty: easy (local suitability only; weak for the Medium target). Helps: answer-shaped headline decoy; note (2) on the Alternatives line tempts the 22.96% misreading; start-date amount in another release; two decimals defeat neighbour estimates. Hurts: "investment manager" mirrors note (2) printed in eight releases; "marketing agent" then finds both amounts; measured carve-outs cued by the question's own words were Too easy or Easy (aq-01432 q01, aq-01322 q03, aq-00745 q01). Estimate: Too easy ~30%, Easy ~45%, Medium ~15%, Between levels ~7%. No Easy slot on this bundle, so an Easy result fills nothing; whether to spend a difficulty run is the caller's or user's decision.

verdict: ready, for local correctness and fairness only. Target-suitable difficulty not established; check_questions.py (L1009-1012) refuses status ready while the review's difficulty is below Medium, even after a platform pass. Keep status draft or checked; platform pending.

failure_modes: FM1 (Part vs total; Takes the wrong line item) real: 1,161 / 5,117 = 22.689% -> 22.69%; "increased 23%" verbatim at Doc 10 L70; claims true; 202 words. FM2 (Linking across documents; Misapplies a rule or premise) real: 1,004 / 5,117 = 19.621% -> 19.62%; variants correct; rev 1 defect fixed ("Doc 6, the 2Q25 release dated July 15, 2025" matches Doc 6 L16/L18); 231 words. No trap repeated; no run produced either wrong answer and the boxes do not claim one did.

findings:
1. Rev 1 findings resolved: FM2 label; reasoning (Step 1 "year-earlier 2Q25 column", Step 3 dates 5,117 from Doc 6 L223, Steps 5 and 7 give 22.40% and 22.69%; form_check_v4 in-process on the frozen reasoning against docs/ and text/: no messages in normal or --strict mode); Doc 6 quote verbatim at docs L415; record slips fixed. Unchanged as assessed: precision, recall, near-copy, platform-only checks, default roles. Probe packets still show the dated gap; both refused anyway.
2. Evidence: all four quotes in docs/ (Doc 10 L59 differs only by a tab after "(2)"; Doc 10 L193; Doc 10 L371; Doc 6 L415); both necessary documents quoted.
3. Required before any hand-over (no re-test): regenerate notes/handover-q01.md (it was rev 1).
4. Stale records (outside the fingerprint): "Rev 1 probes pending"; "Warnings answered: pending floor run"; "Measured attempts (rev 0)" omits revs 1-2.
5. Precision (moderate, not a blocker): second decimal rests on the "approximately" amounts (+/-0.5B spans 22.37-22.42%); 22.40% stands; a platform reviewer could still call it false precision.
6. Records: all rev 2 records carry rev 2 and 99e8be67...; every packet's question.txt identical (sha256 4f447285...); closed-book packet holds only question.txt.
7. Set: q02 shares no answer path or wording with q01; neither contains the other's answer.
8. Unknown (platform-only): restricted names, Original question / Not a duplicate, token window, the form's "One defensible answer" solvers.
