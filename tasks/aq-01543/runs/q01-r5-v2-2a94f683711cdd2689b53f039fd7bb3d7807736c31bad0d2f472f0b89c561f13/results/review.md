# q01 rev 5 - independent review (fresh question-review subagent), 2026-10-08

Input: root, slug, question id, revision, fingerprint, target, source-gap hash, paths to the frozen snapshot, the
question file, the six raw returns of this fingerprint, the rev 4 review, both form screenshots and the emulator;
three adjudication requests (the fraction rule against every form message on record and rev 5's likely form result,
"= 22.83%" against the gold, failure-mode truth after the FM1/FM2 box changes). No writer conversation.
Agent id ad085258cc3145964 (62 tool calls). Raw return below, unchanged except for this header.

q01 (rev 5; tested_sha256: 2a94f683711cdd2689b53f039fd7bb3d7807736c31bad0d2f472f0b89c561f13)

gold_verified: yes. I recomputed from the docs/ originals with Decimal; all 41 corpus hashes match the snapshot.
- Doc 1 (D02): L10 gives 37,963 GWh; L11 gives "28,46TWh" (a decimal comma, so 28,460 GWh of coal plus nuclear); L13 gives nuclear at 41.6%.
- So nuclear is 15,792.608 GWh, coal is 12,667.392 GWh, and coal's share is 33.3677%.
- Doc 2 (D11) L13 gives Poland's 56.2%. The gap is 22.8323, which rounds to 22.8 percentage points.
- All four evidence quotes are verbatim and occur once each in both docs/ and text/ (the U+2019 apostrophe included).
- Alternatives:
  - 27.6% (September 2024 to August 2025) gives 28.6.
  - 27% (2025) gives 29.2.
  - 35% (2020) gives 21.2.
  - The 40.38% nuclear share from the other window gives 21.6.
  - Treating the whole baseload as coal gives -18.8.
  - Rebuilding Poland from TWh gives 55.85-56.03%, so 22.5-22.7; the printed 56.2% governs.
- Rounding shares early keeps 22.8. Rounding TWh to one decimal moves it: 15.8 gives 22.9, 12.7 gives 22.7, 38.0 gives 22.9. 22.9 needs a nuclear share of at least 41.6177%.

outcome: A: match; B: match. Both reach 22.8 percentage points by the gold's derivation and reject 28.6, 29.2 and 21.6. I re-ran audit_transcript.py on all six rev 5 agents: A 14 calls, B 11, auditor 17, closed-book 1 (hand-back only), probes 17 and 20. Every path stays inside its packet, each prompt is root plus packet plus the verbatim question, and each hand-back equals its saved return. Two fresh, uncontaminated matches.

closed-book: misses. It answered "about 28" (28.1 = 57.1 - 29.0), which is not equivalent to 22.8. The harness-attached git status and email are unrelated to the answer.

necessity:
- D02 is the only source of Bulgaria's 2024 production, baseload and nuclear share. The only other mentions of Bulgaria are in D13 (Romania), about trade and the BRUA pipeline; I checked with grep over docs/. The probe without it answered "not answerable"; its forced guess was 27.7 (p 0.03).
- D11 is the only document that names Poland. The probe without it answered "not answerable"; its forced guess was 23.7 (p 0.12, from a recalled 57.1%).
- No smaller valid set exists, and no repeated table or summary carries either country's figure.
- Residual risk: a platform model that recalls Poland's share as 56.12-56.21% would reach the gold without Doc 2. All ten local recalls of Poland's share gave 57.0-57.1%.

shortcut: clear. The shortest route is a lookup in D11 L13, a three-figure derivation from D02 L10, L11 and L13, and one subtraction. No passage states Bulgaria's 2024 coal share or the gap, and "22.8", "22.83" and "33.37" occur in neither document.

source_assessment: no gaps are recorded. source_gaps is [], its hash equals sha256("[]"), and intake shows 20 documents matching the capture with zero gap characters. D02 L44 points to a monthly production chart that has no data in docs/ or the platform text; this is absent in the original, not lost in extraction. At most it would give monthly totals for January-December 2024:
- premises: every 2024 input comes from the annual sentences at L10, L11 and L13.
- gold: totals with no fuel split cannot move 33.37%.
- exclusions: the question has none.
- uniqueness: the chart cannot create a competing 2024 coal share.
- necessity: it has no Poland data and cannot replace L11 or L13.
- shortcut: it cannot print the gap.

difficulty: medium (marginal), as local suitability only. Nothing solver-facing has changed since rev 1.
- For Medium: no printed 2024 Bulgarian coal share; an answer-shaped printed coal share (27.6%) whose window opens "September 2024"; and a nuclear share from another window that fits inside the correct subtraction.
- Against: Poland is a direct lookup, the Bulgarian inputs sit in Doc 1's first five paragraphs, and every strong local solve avoided both traps.
- Easy remains the likeliest single tier, and this bundle has no Easy slot.

verdict: ready, locally. Keep status checked with the platform result pending, and complete finding 1 before any paste.

failure_modes: both declared traps are real, and the changed boxes are true. I recomputed every wrong answer.
- FM1: the L18 paragraph is the Energy chapter's tenth, eight after L10, and its window runs eight months into 2025. 56.2 - 27.6 = 28.6, which is 5.77 above the gold ("almost six points"). The new third box is exact: 28,460 - 15,792.6 = 12,667.4; 33.37%; 56.2% - 33.37% = 22.83%, which rounds to 22.8 percentage points.
- FM2: 28,460 / 37,963 = 74.97%; 74.97% - 40.38% = 34.59%; 56.2% - 34.59% = 21.61%, which rounds to 21.6 (unrounded 21.612). The new second box is exact. The fifth paragraph does open "To support its energy needs". "Two numeric shares" holds, since L94's "more than one-third" is verbal.
- The traps are distinct, the labels and causes are on the form's lists and fit, and the wording rules out neither. The boxes total 244 and 216 words.
- Necessary documents: both take the default "Answer component" role, which matches their use.
- Nit: FM1's second box still writes "56.2 - 27.6 = 28.6" without "%". It is harmless and outside the fingerprint.

findings:

1. The hand-over is stale. /notes/handover-q01.md is still rev 4: fingerprint 6ab396cf, Step 6 "= 22.83 percentage points", the Decoy "56.2 - 27.6 = 28.6", FM2 "= 21.6", status "checked". Pasting it would bring back the rev 4 flag. Regenerate it with `check_questions.py --handover --q q01` and confirm it prints 2a94f683. q01.md currently says status: draft.

2. Fraction rule tested against every form message on record (your ask 1). I ran v2 and v3 in memory, with no files written.
   - q01: v3 reproduces rev 2 (33.37), rev 3 (22.8) and rev 4 (22.83) exactly. v2 misses rev 4. "22.8" and "22.83" are not in either document, so no substring match rescued them. The steps that passed also support percent-as-fraction: "41.6% of 37,963 = 15,792.6" and "= 33.37%".
   - Consistent with the rule elsewhere:
     - aq-01320 q01 rev 2, "10.44 - 10.72 = -0.28": a two-document step with a derived operand, and 0.28 is printed nowhere. This is clean.
     - aq-01321 q02 Steps 7, 8 and 11 passed (1,999, 1,942 and 20.26%, none printed). Step 6's 2,001 is printed in Doc 7, so it is not clean.
     - aq-00949 q04 rev 2, "153.2%": 0.026% off.
     - trial-01: "= 10.123%" passed, and the restatements were flagged.
   - New: aq-00949 q05 rev 0's unflagged "22.7" is explained by that bundle's Doc 7 printing "22.70" (L128-129), so a substring match passed it. This replaces the memory's display-cap guess, and it does not discriminate between rules.
   - Correction: the memory lists "2,028 / 5,175 = 39.19%" (0.004%) as accepted, but that step's first flag (5,175) masked its result, so its acceptance was never observed.
   - Other mechanisms that the fraction rule and v3 do not model:
     - aq-01321 q02 Step 9: the exact sum "1,942 + 1,999 = 3,941" was flagged.
     - aq-00949 q04 rev 0: a parenthesised expression was flagged. v3 is too lenient here.
     - aq-00949 q05 rev 0 Steps 1-2: figures after a quoted "(b)" label were flagged.
     - trial-01: an uncited step was flagged.
     - aq-00949 q03: the second "=" in one step was flagged.
     - Rev 5 has none of these triggers, except the last if the Decoy counts as part of Step 6.
   - v3 artifact: its "and \d+" strip misreads prose such as "and 7,926". It gives a false 153.2% flag on aq-00949 q04 rev 2. Rev 5 has no such pattern.

3. Rev 5 prediction: likely to clear, not established. v3 and v2 print nothing for it. Two numbers could still be flagged:
   - (a) "22.83%": no clean example exists yet of the form verifying a percent-minus-percent result.
   - (b) the Decoy's "28.6%": neither document prints "28.6%". Doc 2's "28.6 GW" covered rev 3/4's plain "28.6" by substring, so the old line was covered by both the arithmetic and the substring. Rev 5's line relies on the arithmetic alone. It fails if the form attaches the unnumbered Decoy to Step 6 and verifies only that step's first "=".
   - The Decoy has never been observed on its own, because the rev 3/4 Step 6 flag may have masked it. Whether to change it is your call.

4. Consistency (your ask 2): yes, it reads as one answer. "the gap in percentage points: 56.2% - 33.37% = 22.83%" is 22.83 points; the subtraction rules out the relative readings (40.6% or 68.4%); and 22.83 rounds to the gold 22.8 at the question's one decimal place. The rounding is left implicit in the reasoning (FM1's third box states it). That is a low risk for the model check "Reasoning reaches the answer".

5. Records, outside the fingerprint: Lever checks still says "four closed-book runs, four probes ... rev 4 included". Rev 5 adds one of each (57.1), making five and five. Add rev 4-5 to the failure-mode evidence list.

6. At hand-over, state the Poland recall risk (Doc 2 removal-flag risk about 5-10%, an open rev 2 finding), that the form's reaction is pending, and the Easy-tier risk.

Paths:
- D:/Projects/Projects/AfterQuery-Docket/10.7/tasks/aq-01543/questions/q01.md
- D:/Projects/Projects/AfterQuery-Docket/10.7/tasks/aq-01543/notes/handover-q01.md
- D:/Projects/Projects/AfterQuery-Docket/10.7/tasks/aq-01543/notes/helpers/form_check_v3.py
- D:/Projects/Projects/AfterQuery-Docket/10.7/tasks/aq-00949/docs/eog_ex991_2026-08-04.txt
- D:/Projects/Projects/AfterQuery-Docket/10.7/.claude/memory/docket-form-automated-checks.md
