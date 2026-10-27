# aq-03707 q03 - observations after submission

questions/q03.md is frozen as submitted (rev 1, origin claude, status submitted, accepted_tier: Medium Tier; file
sha256 c76c1cce659771b69ec02d108ce88e1902d3835752fe0b3b85c6de5eafa1c1c6 at freezing, 2026-10-13; tested_sha256
d2e05dac5ed34a5d0406306f50481bfe99b8c4c0f1b2e7be34917703a675fd53). Do not edit it. Append later platform
observations below, oldest first, with date, source, exact words and artifact link.

## State at submission (2026-10-13)

- Difficulty: Run 3, "Oct 13, 2026, 5:56 PM · Version 994c72 (current) · Low — · Medium 2/6 · High —", "In band —
  Medium tier", "The solvers reached your answer some of the time, which is the difficulty you want.", "You can
  submit now.", "+$20 Medium+ bonus if accepted", "Medium model: 2 of 6 attempts right (the question landed
  here)" ([capture](../verdicts/AQ-03707_difficulty_2026-10-13_1933.txt), saved 19:33). The check started at the
  Medium level: no low attempts were run. 12 of 15 runs left.
- Binding: the page's change list reads 'removed "a", "credits with four main", "players"; added "any",
  "describes as a four-player", "market"', which turns rev 0's sentence into rev 1's; the solvers quote rev 1's
  question word for word; "Your answer: Australia, the Netherlands"; the Document check removes documents 3, 5
  and 8. Question, answer and necessary documents are rev 1's. Reasoning, evidence rows, tags and failure modes
  as submitted were not captured; the hand-over was notes/handover-q03.md (rev 1).
- Closed-book check: "Needed the documents ✓" (it guessed Australia, Canada and the United Kingdom).
- Document check: "Needed document 3 ✓" twice, "Needed document 5 ✓" twice, "Needed document 8 ✓" twice. With
  every document, one attempt reached the answer and one did not (the Netherlands alone).
- No Coach panel and no "may be too vague" or "marked document may not be needed" line on this run.
- Submission: user report in chat, "Successfully submitted as a medium tier" (2026-10-13). The submitted form
  was not captured. The sentence on the form is Claude's rev 1 sentence as handed over; the outcome of "Question
  in your own words" on it was not sent.
- Pending: reviewer outcome; acceptance (not observed).
- observed_platform_status: unknown (submitted; no review result yet).

## Run 3 read-out (caller's reading of each attempt's own text)

| Attempt | Lines | Both four-player lists | Doc 5's aside | Committed answer |
| --- | --- | --- | --- | --- |
| Medium 1 | 270-327 | yes | not reached | the Netherlands |
| Medium 2 | 328-337 | - | - | Right; text not recorded |
| Medium 3 | 338-663 | yes | not reached; opened "Document 5 (Monopoly Watch)" by name and assigned Coriolis's list to it | Netherlands |
| Medium 4 | 664-721 | Doc 3 only | not reached; wrote that Monopoly Watch does not "list other countries' markets" | the Netherlands |
| Medium 5 | 722-731 | - | - | Right; text not recorded |
| Medium 6 | 732-1074 | yes | not reached; opened Document 5 by name and again assigned Coriolis's list to it | Netherlands |
| Every document, first | 1079-1210 | yes | not reached | Netherlands (✗) |
| Every document, second | 1211-1307 | yes | reached, quoted "Even Aussie is a 4-player market" | Australia, Netherlands (✓) |

- All four wrong medium attempts gave the one answer the declared failure mode names (the Netherlands alone).
  The single mode on the hand-over, Linking across documents / Wrong members in a list, therefore matches every
  observed wrong answer. The user submitted before sending the capture; nothing needed changing.
- The page's notes say three of these attempts "never checked", "did not consult" or "skipped" Doc 5. Their own
  text shows three of the four opened it by name and did not find the aside. Platform notes are not the route.
- Nobody added Canada or the United States in this run either.
- What changed between Run 2 (Medium 1/7, High 3/3, between levels) and Run 3 (Medium 2/6, in band): the
  membership test ("a submission ... credits with four main supermarket players" -> "any submission ...
  describes as a four-player supermarket market"), and the level the check started at (Run 3 ran no low and no
  high attempts). Both right medium attempts in Run 3 and the one in Run 2 have no recorded text, so whether
  the closer term is what moved the middle solver is not established: one more right attempt out of one
  fewer.

## What the bundle cost (for the next one)

Three designs, two difficulty runs spent below or outside the band before the pass, four revisions of q02's
sentence for the own-words check on a question that was then dropped. Process misses by the caller, each
already a written rule: q01 was written up in full before any quick test (it was too easy); q02 went to a
run with one step nothing in the question points at; q03's surviving sentence was changed (", if any,") between
the quick test and the run; release was mentioned while sketch i02 was still untested.

## Earlier: difficulty Run 2 read-out (rev 0)

Raw capture: [verdicts/AQ-03707_difficulty_2026-10-13_1607.txt](../verdicts/AQ-03707_difficulty_2026-10-13_1607.txt)
(saved 2026-10-13 16:07; 29 attempts read across Run 2 and the earlier Run 1; no Document check shown).
Read with `tools/verdict_summary.py` and then span by span. Platform words are quoted; the rest is the
caller's reading of each attempt's own Full answer and Reasoning.

### Identity

Run 2, "Oct 13, 2026, 3:38 PM · Version 752eb7 (current) · Low 0/5 (2 not scored) · Medium 1/7 · High 3/3".
The solvers quote rev 0's question word for word (8 times), the page's "Your answer" is "Australia, the
Netherlands", and the page's change list shows the q02 sentence replaced by this one. Bound to q03 rev 0,
tested_sha256 d5a12a0c1d7af15a78c783ecc4b657ea7c8891d87ae3e5e68285e8e71976033e. Ticks and reasoning are not
shown in the capture.

### Platform verdict (verbatim)

"The difficulty check finished: Between levels." "Too hard for the medium model but too easy for the high
model. Make it a little harder, so the high model reaches your answer only some of the time, then run the check
again." "Low model: 0 of 5 attempts right" "Medium model: 1 of 7 attempts right" "High model: 3 of 3 attempts
right". New wording of the gate on this page: "Medium model: three solvers try up to 3 times each. Ready when
at least two get it wrong twice and one gets it right twice. High model: two solvers try up to 3 times each.
Ready when both get it wrong at least once and not every attempt is wrong. A level stops as soon as more
attempts could not change the result." Solver summary: "3 of 15 gave the same wrong answer: “Netherlands.”."
Closed-book: "Needed the documents ✓" (it guessed Australia, Canada and the United Kingdom).

Coach, three findings (its words, not checked facts): 1 change "a submission" to the plural, because "The
phrase 'a submission' is ambiguous and points solvers at the wrong document"; 2 no change to the gold, "the
answer's two halves sit at very different difficulty levels"; 3 demand exhaustive coverage, for example "that
any submission ... credits with four main supermarket players (however phrased)", because Doc 5's sentence
"uses different wording ('4-player market') than the question ('four main supermarket players')".

### What each attempt did (caller's reading)

Steps: (a) the Council's list of countries with competition concerns (Doc 8 para 4.11); (b) the
four-player countries in the Council's own quotation (Doc 8) and in Coriolis's list (Doc 3); (c) Doc 5's
aside, "Even Aussie is a 4-player market"; (d) leave out Canada and the United States, credited only
through regions.

| Attempt | Lines | (a) | (b) Doc 8 / Doc 3 | (c) | Committed answer |
| --- | --- | --- | --- | --- | --- |
| Low 1, 3 | 305-320, 416-431 | - | - | - | "Not scored — our checker failed; replaced" |
| Low 2 | 321-415 | yes | quotes Doc 3's list, then names the Council's own quotation as "The submission" | no | None |
| Low 4 | 432-554 | yes | Doc 8 only ("The submission quoting countries ... is the NZFGC") | no | None |
| Low 5 | 555-669 | yes | Doc 3 | no | Netherlands |
| Low 6 | 670-812 | yes | Doc 3 | no | The Netherlands |
| Low 7 | 813-935 | yes | Doc 8 only | no | None |
| Medium 1 | 939-1163 | yes | both | no | Netherlands |
| Medium 2 | 1164-1521 | yes | both | no; checked Doc 5 three times and wrote that it "doesn't credit specific countries with four main players" | the Netherlands (as the one country on both lists) |
| Medium 3, 7 | 1522-1531, 1827-1836 | - | - | - | Wrong; text not recorded |
| Medium 4 | 1532-1587 | yes | both | no | the Netherlands |
| Medium 5 | 1588-1816 | yes | both (assigns the Council's quotation to Doc 5) | no | Netherlands |
| Medium 6 | 1817-1826 | - | - | - | Right; text not recorded |
| High 1-3 | 1840-1869 | - | - | - | Right, all three; text not recorded |

No recorded attempt's own text contains "Aussie" or "4-player". No recorded attempt added Canada or the
United States: step (d), the declared "Wrong kind of entity" trap, caught nobody.

### What this shows

- Every scored attempt found the Council's list. The medium solver always found both four-player lists; the
  low solver found one or the other.
- Doc 5's aside decided the result. No low or recorded medium attempt reached it, including one that went
  through the other submissions one by one; the high solver's three right attempts and the one right medium
  attempt have no text, so how they reached it is unread.
- Two low attempts read "a submission" as one particular submission (the Council's own), which is why they
  answered "None". The Coach's first finding is borne out by their text. The medium attempts did not read
  it that way.
- The Coach's third finding fits the misses: the question's phrase and the aside's phrase share only the
  number.

### Repair (one, for rev 1)

The Hard tier is not in reach: nothing in the question troubles the strongest solver, and no second sound
step exists to add. For the Medium tier the middle solver has to reach the aside some of the time. The repair
restates the membership test in one reading and in the sources' own kind of term, with no added clause:
"a submission ... credits with four main supermarket players" becomes "any submission ... describes as a
four-player supermarket market". "Any" removes the single-submission reading two low attempts took.
"Four-player market" is how Doc 3 ("four player model") and Doc 5 ("4-player market") put it. Not adopted:
the Coach's "(however phrased)", a clause that tells the solver to look for other wordings; clauses of that
kind measured Between levels or too easy on aq-03570 and aq-02933. Risk stated to the user: the closer term may
let the easier solver reach the aside too; a quick test shows that before a run is spent.
