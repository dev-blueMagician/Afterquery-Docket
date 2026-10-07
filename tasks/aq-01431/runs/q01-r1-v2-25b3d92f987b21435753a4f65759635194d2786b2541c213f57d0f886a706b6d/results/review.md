# q01 rev 1, independent review (fresh question-review agent), 2026-10-06

Input: frozen fields (snapshot.json, q01.md), corpus, capture, this run's raw returns, rev 0's review,
removal probes and platform difficulty check Run 1; no writer conversation. Return copied verbatim from
the task notification.

**q01 (rev 1; tested_sha256: 25b3d92f987b21435753a4f65759635194d2786b2541c213f57d0f886a706b6d)**

**gold_verified: yes.** I recomputed 1.65 from the original passages using exact decimals.
- Doc 12 (D12 l24): "$3.45 trillion address climate change/carbon and $1.23 trillion apply fossil fuel divestment policies". Footnote 4 dates it to the 2022 Trends report.
- Doc 7 (D07 l45): climate change and fossil fuel divestment at "a combined $4.8 trillion"; "The next largest ESG categories, military/weapons and tobacco" at $1.8T and $1.7T.
- Ranked as single issues: 3.45 > 1.8 > 1.7 > 1.23. "Next largest" caps every other category at 1.8.
- 3.45 − 1.80 = 1.65. Each input is printed once in the bundle; D10's "3.45", "1.23" and "1.65" strings are regression statistics.

Every alternative reading of rev 1's wording fails on the documents:
- **3.00** (4.8 − 1.8) treats a figure Doc 7 itself calls "combined" across two named issues as "single", against Doc 12's separate figures.
- **2.88** ((3.45 + 1.23) − 1.8) has the same conflict, and 4.68 is printed nowhere.
- **2.22**: 1.23 is below both 1.7 and 1.8.
- **0.10** is new with "single" (Doc 7 only, combined figure dropped, military/weapons minus tobacco). But a two-issue $4.8T means one issue is at least 2.4, which is above 1.8.
- **1.77** (4.8 − 1.23 as climate) sets a derived figure against a directly stated 3.45.
- **1.75** puts tobacco second.

The "2022" premise rests on context in D07 l23-24 (the 2022 report, "beginning of 2022", the same $8.4T total Doc 12 uses), not a year printed in l45. Residual risk is low and unchanged from rev 0. $1.8T is the only stated figure for its input, so no choice of figure can split the answer. Two decimals is formatting (true band 1.60-1.70); one decimal would split into 1.7 or 1.6 depending on rounding. Acceptable.

**outcome: A: match; B: match.**
- Both answered 1.65 from fresh, separate packets whose question.txt and all 25 corpus hashes equal the snapshot.
- Both read D07 and D12 in full, searched all 12 documents and are uncontaminated (the auto git status showed file names only).
- A (high confidence) rejected 3.00, 2.88 and 2.22 with document reasons. B (medium-high) rejected 3.00 ("combined" vs "single") and 2.22, and noted the precision band.

**closed-book: misses.** It answered 1.10 at low confidence ("roughly $4.5T minus $3.4T"), recalling only the 2020 report's $4.18T. That is not equivalent to 1.65. It is consistent with sketch i01 ("about $1 trillion") and the platform's rev 0 closed-book answer (1.30).

**necessity:**
- **Doc 12** holds the only single-issue climate figure (3.45). Without it, "single" rules out Doc 7's combined $4.8T, which only bounds the top issue at 2.4 or more. The answer becomes 3.00, 0.10 or "cannot determine", never 1.65 (rev 0's probe without D12 forced 3.00 at p 0.85).
- **Doc 7** is the only source of 1.8, 1.7 and the "next largest" cap. Without it, Doc 12 names two issues and gives 2.22 or "cannot determine" (the probe gave 2.22 at p 0.5).
- No closed-book run recalled 3.45 or 1.8.
- The whole-bundle search found no substitute. Other "trillion" figures are ICI/MFA member assets or IRA financing (D02's $1.7T has the same digits as tobacco but is unrelated). D10's US SIF material is fund-ownership data. No smaller document set exists.
- The probes used rev 0's wording, but the inputs are identical and "single" makes the case without Doc 12 less determinate, so their conclusions carry over.

**shortcut: clear.** I verified the auditor's route: one "US SIF" search finds D07 l45 and D12 l24, then the split ranking, then one subtraction. The search finds inputs, not the answer. No passage, footnote or overview line states 1.65; the capture overview prints 3.45, 1.23 and 4.8 but no military/weapons or tobacco figure. The risk is difficulty only.

**source_assessment:**
- **Exact gaps:** none. Snapshot and report show source_gaps [] (hash 4f53cda1…). Intake shows 12/12 documents complete, 0 gap characters, all matching the capture.
- **Image-only content the author noted** (also missing from the platform's own text) is irrelevant on every dimension:
  - **(a) Doc 1 (D02) l59, CDP table of Scope 3 shares by sector.** These are emissions percentages, not fund assets. They cannot support the US SIF premise, supply 3.45 or 1.8, add a category above 1.8, compete with the gold, replace either letter or state a dollar difference.
  - **(b) Doc 2 (D04) l213, a PRI survey finding on UK asset owners and securities lending.** It has no US SIF figures and no assets by ESG issue, so the same six points apply.
  - **(c) Doc 10 (D10) Figures 1-5,** including Fig. 5 Panel E "ESG Ownership (US SIF)". These are firm-level ownership heat-map cells (−0.2 to 0.3 scale), not dollar assets by issue, so they cannot change the premise, gold, exclusions, uniqueness, necessity or shortcut.
- This does not establish complete coverage.

**difficulty: medium (marginal).** This is local suitability only, at the top edge of the Medium band. My estimate for rev 1 on the platform:

| Outcome | Odds |
| --- | --- |
| Between levels again | ~45% |
| Medium | ~30% |
| Easy | 15-20% |
| Too hard / Answer not supported | ~3% |
| High | ~2% |
| Too easy | ~1% |

- **Low model:** rev 0's Doc 7-only 3.00 route (4 of 5 attempts) survives and is stronger now. The new wording echoes Doc 7: "2022 ... ESG fund assets" matches l23, and "largest / second-largest" matches l45's "by far the most significant ... next largest". The low model ignored Doc 12's exact label in rev 0, so it is unlikely to act on "single". Low 0/5 is about 80%; one attempt that splits the figure would land Easy.
- **Medium model:** all five rev 0 attempts already pulled Doc 12. Military/weapons is second under both grouped and split rankings, so the only new risk is choosing 4.8 over 3.45. "Single" against Doc 7's own word "combined" is a one-word check most attempts will make. I expect 4/5, perhaps 3/5. The 2.22 misreading (1/5 in rev 0) stays the main miss, and "single" may nudge it up by drawing attention to Doc 12's split pair.
- **Overshoot to Medium 0/5:** about 5%. The high model would then more likely score 4-5/5 (another Between levels) than 1-3/5.
- **D-checks:** D1, D2, D5 and D6 hold. D3 holds for the low model. D4 and D7 are weak, because "single" is both what makes the question fair and the cue the medium model follows.

**verdict: ready**

**findings:**
1. **Q13 / target.** No rev 1 platform record exists, and a second Between levels is the single likeliest outcome. Each version gets one final result; 7 of 8 runs were left after rev 0. "Single" is the last remaining cue, and it is what keeps the answer unique: without it, 3.00 becomes defensible, because Doc 7 presents the grouped figure as the top "ESG claim" before "the next largest ESG categories". I found no other cue that can come out without reopening 3.00. Whether to spend a run is the user's call. Needed: a platform run on this exact fingerprint.
2. **Q4.** Expect the "may be too vague" advisory again, from low-model attempts agreeing on 3.00. It is non-blocking (aq-00745 q01 passed with it), and the documents refute 3.00. The form's "One defensible answer" check is a platform-only unknown: its model is unknown, it may not have run on rev 0, and two solvers agreeing on 3.00 or 2.22 is roughly a 5-10% risk now that the label is gone.
3. **Records.** In q01.md, the "Removal probes" paragraph sits under the rev 1 records, and its "results/…" paths only resolve in the rev 0 run folder. Label it as rev 0 and give the full path. This is not blocking.
4. **Q9 / Q4 residuals.** D07 l45 is undated, and the two letters disagree (4.8 vs 4.68, a 0.12 gap). Neither changes the ranking or the gold, but a human reviewer may ask about both.
5. **Q14 / form emulation.**
   - Every reasoning number is in its cited document or comes straight after "=", including the decoy results.
   - All five quotes appear word for word, once each, in the docs/ originals. Both necessary documents are quoted and c1 is covered.
   - The question is 36 words, states the precision, and has no semicolons or dashes. Its only shared word with the answer is "trillion", the asked unit, as in rev 0.
   - Tags and levers are accurate.
   - Not checkable locally: restricted names, original-question and not-a-duplicate checks, and the model checks. The local near-copy proxy is 0.272 at most (aq-docket-trial-01 q04), with no shared run longer than 3 tokens. "Answer matches a stated figure" may fire as a false positive.
6. **Rule 10.** The question asks about fund assets in the world, and the answer is a number. It has no "group of / set of" wording and names no letter author.
7. **Records and authorship.** The report recomputes 25b3d92f…, and the records for A, B, the closed-book run and the audit all carry it. Packets and the live corpus match the snapshot. Status is draft. origin: claude is accurate, while the export accepts only "user"; that is the user's decision.
