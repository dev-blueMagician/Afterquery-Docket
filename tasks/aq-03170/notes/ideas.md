# aq-03170 - lean candidate sketches

Current target: hard (user, 2026-10-12: "no slot for Easy Tier ... target medium and high", then "mediums slots full";
2026-10-13: "medium tier, but no slot left"). q01 measured Medium, then Hard, then Medium (Runs 1-3). The task page saved 2026-10-12 00:54 reads "Medium questions are full on this set — only a Hard or
Easy question can still be submitted" (Hard 0/2 · Medium 3/3 · Easy 0/1); reported to the user.

After q01's Run 3 (2026-10-13): i04 and i06 are the two active sketches (families other than q01's); i02 is a third, in q01's family with a different deciding fact; i05 is retired; i03 is parked.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) | h1: more than one earlier letter (MFA, IAA, Blockchain Association) | Own-account answer (MFA, Blockchain Association) fails because ICAN's letter shows the IAA's June 2023 letter. Necessary: Doc 3, Doc 13, Doc 8, and Doc 6 or Doc 10 | Promoted to q01. Rev 1 (date order) was blocked by the form's "One defensible answer" check: both form solvers gave MFA and Blockchain Association. Rev 2 states the counting rule ("including letters only others mention") and asks alphabetical order: "One defensible answer" Passed, "Needs two or more documents" Failed (Docs 3 and 13 "not needed"). Rev 3 unticks those two: difficulty Run 1 "In band — Medium tier" (Low 0/5 · Medium 1/5), Medium slots full per the user. Rev 4, target hard: "Judging by all these letters together": Run 2 "In band — Hard tier" (Low 0/5 · Medium 0/5 · High 1/5, five-attempt gate), submitted, returned by the reviewer for the two ticks. Rev 5 (ticks only): Run 3 "In band — Medium tier" (Low 0/5 · Medium 2/6, three-solver gate; the third medium solver, text not recorded, right twice). No untested fair wording of this question is on file: nothing named = form block, evidence named = this result, clause = Medium |
| i02 | [sketches/i02.md](sketches/i02.md) | h2: earlier letter cited by a different commenter (IAA, FIA, MFA, RER) | Named citations give IAA and FIA; the joint letter Blackstone cites adds its signers RER and MFA. Necessary: Doc 10, Doc 2, Doc 3 | Untested; third in line; marks narrowed to Doc 10, Doc 2, Doc 3 by the removal test |
| i03 | [sketches/i03.md](sketches/i03.md) | h2n: days from the joint letter to its signers' next letter (48) | Either signer's letter alone gives 48 | Parked: one indispensable document group |
| i04 | [sketches/i04.md](sketches/i04.md) | h3: numbered questions taken up by two commenters (3 and 4) | "None" fails on MFA's range 1 – 6. Necessary: Doc 3, Doc 7 | Active, untested. A wrong route (AGC's request numbers) also reaches 3 and 4 |
| i05 | [sketches/i05.md](sketches/i05.md) | h1 as a count: months of 2023 holding earlier letters (6) | 5 without ICAN's June; 7 with third parties, meetings or the letters in the bundle. Necessary: Doc 12, Doc 3, Doc 8, Doc 13 | Retired 2026-10-13: June is reachable from a third party's letter, and the wording is q01 rev 0's |
| i06 | [sketches/i06.md](sketches/i06.md) | h10: one Federal Register citation, two dates (6 days) | 22 days (the proposing release's two dates) fails "the same Federal Register citation". Necessary: Doc 1, Doc 9 | Active, untested. A footnote detail: reviewer may call it trivia |

Screens: `docket_agent.py screen` clean for i01-i05 on 2026-10-12 and for i02, i04, i06 on 2026-10-13 (structure and quotes only). Author recomputation:
date gaps and the question-number intersection by script the same day. No local model checks run and no tier guessed.
