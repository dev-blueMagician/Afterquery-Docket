# Independent review, q01 rev 1 (2026-10-08)

Role: question-review (fresh context; frozen fields, corpus, raw returns and floor output).
tested_sha256: 6fa7875382f3e0998151a32334fa280b2f1f698e99c654aecb5fe82f95c7232a

Raw return (verbatim):

q01 (rev 1; tested_sha256: 6fa7875382f3e0998151a32334fa280b2f1f698e99c654aecb5fe82f95c7232a)

**Summary:** the gold holds, the question is fair, and every rev 0 finding is fixed. On local evidence it is still Easy-leaning for a Medium target.

**Record binding.** `docket_agent.py report` gets the same fingerprint from the current file, and the corpus hashes match the snapshot. `source_gaps` is [] (gap hash 4f53cda1...). Solvers A and B, the closed-book run, the audit and both probes all carry this fingerprint. The question.txt in all four rev 1 packets matches the frozen question exactly. The rev 1 packets are byte copies of the corpus. The probe packets (runs\q01-r0-alt-k3\solver-1 and solver-2) are byte copies minus D03 or D07, with renumbered ids and identical text bodies. Floor: 0 FAIL, 2 WARN (origin is accurate; the sibling warning is the deliberate q02 alternative). There is no platform record.

**gold_verified: yes.** I recomputed it with an exact-decimal script.
- Inputs:
  - Doc 7 l.63-64: the $100 automatic payment goes to the No Bankruptcy Group only.
  - Doc 7 l.66 and l.73: each payment is the member's points over all claimants' points, 3 against 1.
  - Doc 7 footnotes 2-3: both groups are defined by the April 22, 2025 report.
  - Doc 6 l.47, l.49 and l.61: 920 eliminated and a list of 57,233; 20,891; 36,317.
- 62,673 / 98,990 = 63.31246%, which is 63.3 under half-up, half-even and half-down rounding.
- Every other stated-figure route also gives 63.3:
  - aged count as 57,233 − 20,891: 63.296
  - no-record count as 57,233 − 36,317: 63.340
  - TEST records dropped: 63.310 or 63.314
  - Doc 7's fund residual (2,090,000 / $100 = 20,900) with 36,317 or with 57,233 − 20,900: 63.322 or 63.312
- Margin: the no-record count can move −56/+33 and the aged count −58/+97 before the answer changes.
- Wrong routes:

| Route | Result |
| --- | --- |
| March split | 64.962 (65.0) |
| 920 removed from the no-record group | 64.0 |
| 920 removed from the aged group | 65.5 |
| $2.1M reserve as the no-record count | 63.433 / 63.487 |
| June 2022 sample | 72.3 |
| Head count | 36.5 |
| $1,000 / $350 weights | 62.2 |
| Reversed points | 16.1 |

- Opt-outs after the May 2025 notice are reported nowhere. The groups are fixed by the April report, so these counts are the documents' only answer. Low risk.

**outcome: A: match; B: match.** Both answered 63.3% with high confidence from D03 + D07, in fresh contexts. Neither opened question.txt; the only extra context was an auto-attached git status listing unrelated file names. Both rejected the March counts (the groups rest on the April definitions) and the reserve readings (approximate). That is two uncontaminated matches.

**closed-book: misses.** It answered 22.6% after guessing a different case (Ramirez) with equal shares. Not equivalent.

**necessity**
- **Doc 7 (D03):** the only source of the settlement terms: who gets the automatic payment, the 3:1 points, the pro-rata rule and the April-report definitions.
  - The only other settlement (Clark, in D05) has no money terms, and the other documents predate the settlement.
  - Probe without it: "not answerable", forced guess 36.5% (p 0.12).
- **Doc 6 (D07):** the only source of 20,891, 36,317 and 57,233 (confirmed by grep).
  - D06 lists the April report as an exhibit with no counts. D05 has only the June 2022 sample and projections.
  - Doc 7's reserve or fund residual gives about 21,000 or 20,900 no-record members, but no aged count and no class total.
  - Probe without it: "not answerable", forced guess 72.3% (p 0.20).
- The no-Doc-7 probe's side reading (aged head-count share, 63.5) is 0.2 from the gold but differs at the asked precision.
- No smaller source set and no alternative pair exist.

**shortcut: clear.** The shortest route is Doc 7 l.63-73 plus footnotes 2-3, then Doc 6 l.47-61, then one weighted share.
- Search finds inputs, not the answer. No passage states the share, a point total, or the April split as a pair, and Doc 6 never uses the group names.
- The bundle's percentages (27.7, 32.0, 17.3, 27.5, 4.75, "30 percent") all measure other things.
- Two other routes reach the gold (20,891 with 57,233; the fund residual with 57,233), but both still need both documents.
- The overview prints the March split beside 57,233. That exposes the decoy, not the answer.

**source_assessment:** not applicable. The capture is complete, with no gaps, and the current bytes match the snapshot and intake.json.

**difficulty: easy, marginal toward medium** (local suitability only, below the Medium target).
- The mechanism is a superseded version in the same document. The March pair is followed in the next sentence by the re-run, and its sum (58,153) does not match the 57,233 list.
- The April counts sit unlabeled in expert-sample sentences, and the deciding date is in Doc 7's footnotes.
- The closest measured analogue is aq-00745 q01, a tied edition trap that measured Easy (Low 1/5). The Medium passes used decoys that looked current or carried the asked label.
- Finding 20,891 alone, plus the printed 57,233, already gives 63.3, which weakens the trap.

**verdict: ready.** Gold, two matches, the closed-book miss, a clear audit, both probes and every applicable fairness check hold, and no fixable defect remains. Caveat: this review does not support the gate's "target-suitable difficulty" for Medium. Treat q01 as a quick-test candidate, not a likely Medium.

**failure_modes**
- **Mode 1 (Superseded date or version / Uses the wrong period or date):** real.
  - Doc 6 l.47 gives 66,636 / 102,577 = 64.962%, which rounds to 65.0 (recomputed).
  - The wording doesn't rule it out, the labels are the best fit, and the boxes total 234 words (186 with letters).
  - These claims are true: the March 12 PACER report; first split Doc 6 prints; 58,153 vs 57,233; 920 eliminated; samples drawn by Trans Union's experts; $2,089,100 fits $2.1M where $2,221,200 does not.
  - One nit: "paraphrases the two definitions that Doc 7 gives" reverses the chronology (Doc 6 is earlier). The March search was also keyed on SSN plus two surname letters. "Describes the same two categories" would be exact. Optional, and outside the fingerprint.
- **Mode 2 (Linking across documents / Rounding, scale or sign):** real.
  - 21,000 with 57,233 − 21,000 gives 63,000 / 99,233 = 63.487%, which rounds to 63.5 (recomputed).
  - Not ruled out by the wording. The labels are acceptable ("Takes the wrong line item" is also defensible). The boxes total 274 words (223 with letters).
  - These claims are true: Doc 7 gives no counts; Doc 6 never names the groups; an "Approximately" figure cannot fix the count within the −56/+33 window.
  - The box correctly says no run gave this as an answer. It is weaker than mode 1; keep or withdraw at your discretion.
- No trap repeats. Both documents default to "Answer component", which fits how each is used.

**findings**
1. **Rev 0 findings are all resolved.**
   - Failure-mode overclaims are corrected, mode 2's route is made consistent (63.5), and its unobserved status is disclosed.
   - Steps 4-6 now cite "Doc 6 and Doc 7", with one a-op-b each and the result straight after "=".
   - D03 l.64 and footnote 3 are now quoted. All ten evidence rows are verbatim in both text\ and docs\.
   - The lever-check notes on the second distribution and the D05 projections are corrected.
2. **Form number rule (emulated): no flag expected.**
   - "$100.00" is printed in Doc 7. "April 22, 2025" is printed whole in Doc 7 footnotes 2-3 and in Doc 6 l.127. 920, 57,233, 20,891 and 36,317 are in Doc 6.
   - The unnumbered Decoy line holds only Doc 6 figures and "March 2025".
   - Derived operands in two-document steps follow the pattern that passed in aq-00949 q05. The rule itself remains unconfirmed.
3. **Rule 10 and length:** it asks about the world, not the document set. No "the group of / set of" wording. 40 words, so the 60-word warning doesn't apply.
4. **Platform risks:**

| Check | Estimate | Why |
| --- | --- | --- |
| "Too vague" block | ~5-10% | Both form solvers would have to land on the same wrong answer, most likely 65.0 |
| "Answer matches a stated figure" | advisory only | No document states the share; a false positive keyed on $2,882,000.00, $1,000/$350 or "30 percent" is possible |
| Document check | <5% | Both probes off the gold; inputs are post-cutoff; no rounded-figure route lands on 63.3 without either document |
| "Answer not supported" | ~3-5% | Six of six local full-document runs reached 63.3 |
| Closed-book | <2% | |

5. **Tier estimate** (judgment, not measurement):

| Outcome | Estimate |
| --- | --- |
| Too easy | ~25% |
| Easy | ~45% |
| Medium | ~15% |
| Between levels | ~8% |
| High | ~3% |
| Too hard / Answer not supported | ~4% |

   - A usable result (Medium or High) is about 15-20% likely. Rev 1 changed only fields the difficulty solvers don't see.
6. **Minor local notes (outside the fingerprint):**
   - The Necessity bullet in Lever checks still says "Removal probes: pending".
   - The Blind solve comment points only to the rev 0 raw folder.
   - The probe packets kept the original docs\ file names. The no-Doc-7 probe inferred a missing later filing from the numbering gap but still answered "not answerable". Rename docs\ in future probe packets.
7. **Optional evidence (inside the fingerprint; would need rev 2 and fresh checks):** the link between 36,317 and the April report rests on context. Doc 6 footnote 5 (l.127, "a sample of the final class list … April 22, 2025") makes it explicit.
8. **Set:**
   - q02 is a near-copy alternative (token ratio 0.652, a 10-token shared run). Submit only one of q01 and q02.
   - q03 reuses Doc 6's 20,891 and 57,233 and the same superseded-version trap. Its phrase "class list in place when Trans Union moved to decertify" points at the April list.
   - Avoid pairing q01 with q03 if "each trap once per task" applies across the whole task (not confirmed).
   - Outside this bundle, the closest workspace question has a ratio of 0.259.
9. **Unknown (platform-only):** restricted names, platform-wide originality and duplicates, and the real number-check behaviour. I did not run `--handover` because it writes a file.

Files:
- D:\Agents\Docket\tasks\aq-01541\questions\q01.md
- D:\Agents\Docket\tasks\aq-01541\runs\q01-r1-v2-6fa7875382f3e0998151a32334fa280b2f1f698e99c654aecb5fe82f95c7232a\results\
- D:\Agents\Docket\tasks\aq-01541\runs\q01-r0-alt-k3\
- D:\Agents\Docket\tasks\aq-01541\text\D03.txt
- D:\Agents\Docket\tasks\aq-01541\text\D07.txt
