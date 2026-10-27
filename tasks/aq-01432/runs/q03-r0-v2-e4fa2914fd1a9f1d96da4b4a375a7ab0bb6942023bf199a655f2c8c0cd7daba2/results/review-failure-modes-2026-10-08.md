# q03 rev 0: review of the Targeted failure modes (fresh question-review agent), 2026-10-08

Raw return as received by the caller (agent hand-back text, with the harness's two-space indent removed;
tool trace not exported). Scope given: the new '## Targeted failure modes' section (one mode) and the
Lever checks bullet beginning "- Targeted failure modes (2026-10-08". By its report it ran no new solves
and wrote no file. The caller confirmed afterwards that only q03.md (the caller's own edits) had changed
in the bundle, that q03.md held exactly the caller's text, and that `report` still gave e4fa2914. The
harness noted that its safety classifier was unavailable while this agent's work was reviewed. After the
hand-back arrived, the task ended with an API error ("The response stopped arriving"). That notice's
result held only a progress line: "Box totals are 431 words (394 holding a letter), well over 150. Two
more confirmations follow: the recomputed lists, and whole-bundle searches for numbered-practice
references and the heading words." The hand-back below is complete: verdicts, failure_modes, findings
1-10 and a file list.

---

q03 (rev 0; tested_sha256: e4fa2914fd1a9f1d96da4b4a375a7ab0bb6942023bf199a655f2c8c0cd7daba2)

Scope: gate Q15 only. I wrote no files, ran no solves and did not run --handover. `docket_agent.py report` still gives e4fa2914. The floor shows 0 FAIL and the same 7 WARNs, with no failure-modes warning. The submission_sha256 docstring and the unchanged hash confirm that Targeted failure modes and Lever checks sit outside the fingerprint.

gold_verified: yes (checked again while testing the boxes). D10 L79 lists seven clauses, which map to D09 practice 5 (L439), 6 (L455-469), 7 (L477), 11 (L511), 17 (L601), 22 (L655) and 23 (L671). Practice N equals paragraph N by L573, fn39 L1593, fn112 L1885 and D08 L63/L159. In ascending order: 5, 6, 7, 11, 17, 22, 23. The two bait terms are matched by ordinary meaning, as before.
outcome: A: match; B: match. Both raw returns give 5, 6, 7, 11, 17, 22, 23 with high confidence, and both reject 21.
closed-book: misses. It gave "7, 16, 20, 21 and 32" on a wrongly shifted old numbering.
necessity: carried over from rev 0, with a search check. Outside D09, the only numbered-practice references in the bundle are 12, 13, 25 (D04, D11), 22 and 27 (D08) and 30 (D09 notes). D09 is therefore the only source for 5, 6, 7, 11, 17 and 23. D10 L77 is the only "promotional claims" heading. The high Doc 9 document-check risk recorded earlier is unchanged: the probe without D09 gave a forced guess equal to the gold (p 0.6).
shortcut: clear (carried over from rev 0; no passage pairs the theme with paragraph numbers).
source_assessment: no gaps. The report shows source_gaps [] and intake shows 11/11 complete with zero gap characters.
difficulty: easy (local suitability, carried over from rev 0). That is below the medium target, and declaring a failure mode does not change it.
verdict: question unchanged. The rev 0 review stands: ready on correctness and fairness, not suitable for medium, status draft. Separate verdict on failure modes: the form section (Failure mode 1) is READY. The Lever checks bullet needs REVISE for record accuracy only (findings 1-6). This needs no re-test and does not touch the fingerprint.

failure_modes:
- Is the trap real? Yes. Banned practice 21 (D09 L645-651) sits directly before 22 (L653-667). A grep of all of D09 finds "prize" only at L647, L651, L655, L659, L663 and L667. By script, the gold plus 21 gives 5, 6, 7, 11, 17, 21, 22, 23 (eight items), matching the stated wrong answer. Its pull is moderate:
  - The guide's wording is close to 22.
  - D08 L159 ties "won a prize" to paragraph 22.
  - Solver A, solver B, the shortcut audit and the probe without D09 all raised 21 and rejected it.
  - There is no platform run, so this is not a measured trap.
- Do the labels fit? Yes, both are the best options on the form's lists.
  - Trap: "Linking across documents" is right, because the error happens when a Doc 11 clause is linked to a Doc 9 practice. "Look-alike measure" is about metrics and "Wrong jurisdiction or scope" involves no other regime, so both fit less well.
  - Cause: "Wrong members in a list" is right, because the solver lets an extra item into the list. "Picks the wrong entity or section" would fit only a swap (5, 6, 7, 11, 17, 21, 23), and no return produced that.
  - The trap is not repeated, and no sibling declares one: q01 is dropped and q02 has no section.
- Does the wording rule the trap out? No. The question gives no count and nothing about prizes. Its only "Competition" is in the Act's name.
- Are the box claims true? Yes. Every quote matches its source word for word:
  - D10 L77 heading; the L79 sentence (curly apostrophes match); L85 "Illegal products"; L87 "aids to help people win prizes when gambling".
  - D09 L647; L655 (start of the sentence); "the consumer has won a prize" (L667); "paragraph 13 of Schedule 20" (L573).
  - "32 … chapter 3" is supported by D09 L49 and L95.
  - The paraphrases of the scratch-card example (L651) and the letter example (L667) are accurate.
  - Doc numbers are correct: Doc 11 = D10 and Doc 9 = D09 (intake numbers 11 and 9).
  - I found no overclaim, and the boxes claim no observed failures.
- Word counts (whitespace / words holding a letter): Where the trap sits 166/159, wrong answer 89/74, why avoided 176/161, total 431/394.
- Should more modes be declared? No. Every other route is either unobserved, ruled out by the wording, or found only in memory (finding 9). Adding a mode no check produced would weaken the section, as the review advised for aq-01278 q02.

findings:
1. Lever checks (c), attribution. Solver A's return reads: "BP15, BP20, BP21 (and one of BP24/BP31) are matched by no theme's wording; one could guess they belong here". The bullet gives only "15, 20 and 21", plus a ten-item list that solver A never printed. Fix: quote the full set, including one of 24/31, and label any assembled list as the caller's. The solver A line in Blind solve leaves out the same item; log a correction rather than rewriting that record.
2. "None answered with it" needs a scope. The probe without D10 gave the forced guess "paragraphs 21, 22, 23", with alternatives "7, 17, 21, 22, 23" and "5, 6, 7, 17, 21, 22, 23". The closed-book set included "prize promotions without a prize" (its "20"). Neither had both documents, so neither is the declared route. Fix: "none of these four"; mention both runs as evidence that 21 pulls when the guide's clause is absent.
3. "the question never mentions prizes or competitions" is not literally true, because the question contains "Competition" in the Act's name. Fix: "no prizes or prize competitions; its only 'Competition' is the Act's title".
4. (a) "no check with the documents used them" is inexact. The probe without D09 "recalled the 31 practices of the 2008 CPRs Schedule 1" as the base for a rebuild that reached the gold. Fix: "none answered in them". The conclusion still holds. No document prints the old numbers: fn38 at L1589 gives none, and the "Schedule 1, paragraph 10" at L1793 belongs to the Package Travel Regulations. Naming Schedule 20 of the 2024 Act also rules this route out.
5. Two quotes have lowered capitals: the sources print "Main trap" and "All themes cover all 32". Fix them if they are presented as exact quotes.
6. "Every check that had the whole bundle raised adding 21 as a weaker reading" does not describe the review. The review also had the whole bundle, but it called 21 a non-qualifying decoy ("does not qualify"). Fix: "every solve-type check".
7. Optional precision in the boxes. None of these is false.
   - "One of them sits in the sentence": two clauses sit there (the "free" one and the prize one). Name the prize clause.
   - Six practices open with "Claiming" (1, 2, 4, 17, 18, 21), including gold member 17, and practice 16 carries "promotional" exactly. The echo is weak; the real lure is the shared word "prize" and the adjacency.
   - Practice 22's example shows the cost-to-claim limb. Its first limb, "there is no prize or other equivalent benefit" (D09 L659), matches "if that’s not true" more directly.
8. Necessary documents. There is no `## Necessary documents` section, so the hand-over prints the default "Answer component" role for Doc 11 and Doc 9. That fits how each is used: Doc 11 supplies the members and Doc 9 the numbers. Writing the section would change the fingerprint, which then requires re-prepare and fresh checks. This is a hand-over gap, not a correctness finding.
9. Routes not declared, and why that is right:
   - (a) The old numbering exists only in memory and is ruled out by the wording.
   - (b) The bait terms: no check slipped, the slip has no single wrong answer, and it would need the same trap label.
   - (c) Theme scope is ruled out by "lists".
   - (d) Practice 20 has "no textual basis".
   - (e) Clause order is ruled out by "in ascending order".
   - Practice 29 for the rights clause (via D10 L95) is unobserved and would need the same label.
   - The FTC "Guides Against Bait Advertising" (D02 L178) gives no Schedule 20 number.
10. Platform status. latest_platform_record is null, so platform acceptance of this mode has not been observed. The form's "Each trap once per task" may span questions; that is a platform-only check and remains unknown.

Files:
- D:\Agents\Docket\tasks\aq-01432\questions\q03.md
- D:\Agents\Docket\tasks\aq-01432\runs\q03-r0-v2-e4fa2914fd1a9f1d96da4b4a375a7ab0bb6942023bf199a655f2c8c0cd7daba2\results\
- D:\Agents\Docket\tasks\aq-01432\text\D09.txt, D10.txt, D08.txt
- D:\Agents\Docket\tasks\aq-01432\notes\intake.json

---

Caller's response, 2026-10-08. Findings 1-6 are applied in the Lever checks bullet:
- Solver A's full set is quoted, "(and one of BP24/BP31)" included. The ten-item list is labelled the
  caller's assembly. A note says the solver A Blind solve line leaves that item out, and that line stays
  as written.
- "None of these four". The D10-absent probe and the closed-book solve are cited as evidence that 21
  pulls when the guide's clause is absent.
- "names no prize or prize competition (its only "Competition" is in the Act's name)".
- "No check answered in the old numbers". The D09 L1793 Package Travel reference is noted.
- Source capitals "Main trap" and "All themes cover all 32".
- "Each solve-type check with the whole bundle".

Finding 7's three optional precisions are applied in the boxes:
- The prize clause is named.
- The "Claiming" echo is replaced by "its text holds the first "prize" in Doc 9" (D09 L647 is the
  first "prize" in the document).
- Practice 22's two limbs are quoted.

Finding 9's practice 29 route is added to (b). Finding 8 needs no change, because the default Answer
component roles fit and writing the section would change the fingerprint. Finding 10 stays
platform-only.

A caller script then checked every quoted span in the three boxes against D10 or D09 (all verbatim). It
counted 437 words across the boxes (399 holding a letter). The floor is 0 FAIL and 7 WARN, and `report`
still gives e4fa2914. The same agent was asked to re-check the changes.

---

## Re-check by the same agent after the fixes (2026-10-08), raw return

Hand-back text as received, with the harness's two-space indent removed. Usage reported: 4 tool uses,
about 101 s.

aq-01432 q03 re-check (rev 0; tested_sha256: e4fa2914fd1a9f1d96da4b4a375a7ab0bb6942023bf199a655f2c8c0cd7daba2)

Findings 1-7 are all closed, and the changed text adds no material inaccuracy. Both the failure mode and the Lever checks bullet are now ready. I wrote no files, ran no solves and did not run --handover. `report` still gives e4fa2914 with no platform record, and the floor still shows 0 FAIL and the same 7 WARNs.

(1) Status of findings 1-7
1. Closed. Solver A's full set is now quoted exactly as solver-A.md prints it. The ten-item list is labelled as the caller's own. The Blind solve line ("would add unmatched 15, 20, 21") is quoted exactly and left as written.
2. Closed. The bullet now says "None of these four". The probe without D10 is quoted correctly ("paragraphs 21, 22, 23", with alternatives 7, 17, 21, 22, 23 and 5, 6, 7, 17, 21, 22, 23). The closed-book's "20" is correctly "prize promotions without a prize", next to its "32" for false "you've won" claims.
3. Closed. The bullet now reads "names no prize or prize competition (its only "Competition" is in the Act's name)".
4. Closed. The bullet now reads "No check answered in the old numbers". "Schedule 1, paragraph 10" matches D09 L1793 exactly, and that line belongs to the Package Travel Regulations.
5. Closed. The capitals now match the sources: "Main trap" and "All themes cover all 32".
6. Closed. The bullet now reads "Each solve-type check with the whole bundle". The review's "does not qualify" is quoted exactly.
7. Closed, and each new box claim is true:
   - The box now names the prize clause.
   - "its text holds the first "prize" in Doc 9" is correct: a script finds the first case-insensitive "prize" in D09 at L647, in practice 21.
   - "there is no prize or other equivalent benefit" matches D09 L659 exactly.
   - "requires the consumer to pay money or incur a cost" is an exact substring of L663. Paraphrasing L663's "taking any action in relation to claiming the prize" as "claiming it" is fair.
   - "the consumer has won a prize" is an exact substring of L667.
   - The "Claiming" echo sentence is gone.

(2) New inaccuracies
Nothing material. Two trivial points, neither of which is a defect:
- The Review note says the boxes "quote practice 22's first limb", but they quote both limbs (L659 and L663). This understates rather than misstates; "both limbs" would be exact.
- In the "Why" box, file line 89 is a short wrapped line ("claiming to offer a competition or"). This is cosmetic and does not change the word counts. Check how it pastes once you generate the hand-over.

The Review note's claims are accurate: its quotes "READY" and "REVISE for record accuracy only" match the saved return review-failure-modes-2026-10-08.md (line 28).

(3) Word counts after the change (all words / words holding a letter)

| Box | All words | Words holding a letter |
| --- | --- | --- |
| Where the trap sits | 164 | 156 |
| The wrong answer a careless solver gives | 89 | 74 |
| Why the correct answer avoids it | 184 | 169 |
| Total | 437 | 399 |

The form needs at least 150 across the three boxes.

(4) Verdicts
- **Failure mode 1:** ready (local only). Whether the platform reviewer accepts it has not been observed.
- **Lever checks bullet:** ready. Its claims match the sources and the raw returns.
- **Question:** unchanged. The rev 0 review stands: ready on correctness and fairness, local difficulty easy, so not suitable for the medium target. Status stays draft.

File: D:\Agents\Docket\tasks\aq-01432\questions\q03.md

---

Caller's response to the re-check, 2026-10-08: both trivial points fixed. The Review note now says the
boxes "quote both limbs of practice 22", and the short wrapped line in the Why box is reflowed (no word
change).
