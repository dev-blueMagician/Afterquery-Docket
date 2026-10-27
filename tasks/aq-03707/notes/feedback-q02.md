# aq-03707 q02 - difficulty Run 1 read-out

Raw capture: [verdicts/AQ-03707_difficulty_2026-10-13_1256.txt](../verdicts/AQ-03707_difficulty_2026-10-13_1256.txt)
(saved 2026-10-13 12:56; 13 attempts read; no Document check and no high rung in the capture).
Read with `tools/verdict_summary.py` and then span by span. Platform words are quoted; the rest is the
caller's reading of each attempt's own Full answer and Reasoning.

## Identity

Run 1, "Oct 13, 2026, 12:26 PM · Version 3a92ac (current) · Low 0/5 · Medium 4/7 · High —". The solvers quote
rev 2's question word for word (20 times) and the page's "Your answer" is 22.2%, the file's gold. Bound to
rev 2, tested_sha256 f87a8c375913c55af3183756c4b9981fcd072db5a8b1a94039ef5a9d0c504962. Ticks, roles and
reasoning are not shown in the capture.

## Platform verdict (verbatim)

"The difficulty check finished: Between levels." "Too hard for the low model but too easy for the medium model.
Make it a little harder, so the medium model reaches your answer only some of the time, then run the check
again." "Low model: 0 of 5 attempts right" "Medium model: 4 of 7 attempts right" "Ready when 1–3 attempts at a
level are right, out of up to 5." "No specific changes were suggested for this version." Solver summary: "2 of
12 gave the same wrong answer: “10%”." "5 wrong attempts quoted the same passage: Doc 11 (“earnings before
interest, tax, depreciation, amortisation and rent”)." Closed-book: "Needed the documents ✓" (it named
Foodstuffs South Island and an EBIT margin of about 4 percent).

## What each attempt did (caller's reading)

Steps: (a) pick Foodstuffs North Island from the ROACEs in Doc 1; (b) take the two accepted kinds of margin
from Doc 11; (c) reach Doc 8's cost-of-goods sentence (para 4.19) and take the complement.

| Attempt | Lines | (a) | (b) | (c) | Committed answer |
| --- | --- | --- | --- | --- | --- |
| Low 1 | 287-456 | yes | yes | never reached | 15% gross (10% EBITDAR), the consultant's Table 1, called "illustrative" |
| Low 2 | 457-609 | yes | yes | never reached | the 13.1% ROACE itself, offered as the comparable measure |
| Low 3 | 610-769 | yes | yes | never reached | 13.1% ROACE, with Table 1's 15% and 10% as an alternative |
| Low 4 | 770-912 | yes | yes | never reached; read para 4.17 | the 4% NPAT margin, while saying gross or EBITDAR is the right kind |
| Low 5 | 913-1109 | yes | yes | never reached | 15% gross (10% EBITDAR) from Table 1 |
| Medium 1 | 1113-1122 | - | - | - | Right; "This attempt’s text was not recorded." |
| Medium 2 | 1123-1441 | yes | yes | reached on a last re-read of Doc 8 | Right: 22.2% (100 - 77.8) |
| Medium 3 | 1442-1719 | yes | yes | never reached; read para 4.17 | 10% (bare value; the Reasoning block is cut off while weighing Table 1's EBITDAR margin) |
| Medium 4 | 1720-1729 | - | - | - | Right; text not recorded |
| Medium 5 | 1730-2046 | yes | yes | never reached; read para 4.17 | "not provided" in the documents |
| Medium 6 | 2047-2437 | yes | yes | never reached; saw footnote 111's 24.4% for Woolworths NZ | 10% (bare value; the Reasoning block is cut off inside Table 1) |
| Medium 7 | 2438-2788 | yes | yes | reached after re-reading the question's period phrase | Right: 22.2% |

None of the eight wrong attempts mentions 77.8, 77.6 or the cost-of-goods sentence anywhere in its text.

## What this shows

- Steps (a) and (b), the two a word in the question points at, were cleared by every attempt with text.
- Step (c) is the only step nothing in the question points at. It decided every recorded attempt: no low
  attempt reached the sentence, and each recorded medium attempt was right exactly when it reached it. Nobody
  who reached it failed to take the complement.
- The wrong answers were the consultant's worked-example margins (15% twice, 10% twice, both once as an
  alternative), the ROACE itself (once, once with the example as alternative), the printed NPAT margin (once)
  and one refusal. The declared mode "Look-alike measure" (4%) was observed once; "Look-alike company"
  (22.4%, the other co-operative) was never observed.
- Medium 7 went back to Doc 8 after re-reading "over the years covered by that ROACE"; Medium 2 went back on
  a general last check. The period phrase is a pinning condition (rule 9b), so it is not removed.

## Repair considered (WORKFLOW section 6, repair orders 1 to 6)

The question has one unpointed step. A second must sit in a different passage and be sound. None was found:

- Woolworths NZ's margin on the same measure (footnote 111, 24.4%, against 24.0 from the body's 76%): the
  footnote hangs on the very sentence that held, so asking for it shows solvers that sentence; the exact
  against rounded pair has not trapped either solver on other bundles; the two figures leave a second answer.
- Dropping the period phrase (the one cue a right medium attempt is seen to follow): it would leave the
  question without a period, which weakens a defining condition.
- A second ask on a printed figure (the NPAT margin, the ROACE): changes no attempt's outcome.
- Picking the co-operative through a conference quote and its footnote instead of the ROACE: a labelled
  bridge, a kind every attempt cleared; it would also drop Doc 1.
- The same question for the other co-operative (22.4%): identical steps, so not a harder question; a new
  run on it would only resample the same difficulty, which is not a repair.

Decision: no fair repair inside hook h13. q02 dropped after one run. Not bound to any submission.
