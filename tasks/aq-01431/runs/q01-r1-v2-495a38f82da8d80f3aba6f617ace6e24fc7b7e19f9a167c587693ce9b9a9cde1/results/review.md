# q01 rev 1 - independent review (fresh question-review), 2026-10-08

tested_sha256: 495a38f82da8d80f3aba6f617ace6e24fc7b7e19f9a167c587693ce9b9a9cde1

Bottom line: verdict ready (local only), difficulty medium (marginal). No wording change is required before a platform run. The main risk is that the platform may decide Doc 4 is not needed, because its one key fact can be recalled from memory.

gold_verified: yes. Recomputed from the documents.
- Doc 6 (D01): footnote 23, line 147: the letter is dated "Apr. 11, 2023" and filed under "File Nos. S7-29-22; S7-31-22; and S7-32-22". Footnote 2, line 15: ICI's comment under S7-30-22 is on the Regulation NMS minimum-pricing proposal; footnote 13 calls that proposal the "Rule 610/612 Proposal" (Dec. 29, 2022). Footnote 2 also puts ICI's "Order Competition Rule Letter" under S7-31-22. Footnote 13, lines 99-101: Best Execution is S7-32-22 (Jan. 27, 2023); Order Competition was published Jan. 3, 2023.
- Doc 4 (D05): line 126 ties the letter to "the Commission's market structure proposals". Footnote 15 (line 141) puts it in the s7-29-22 comment file. Footnote 16 (lines 160-161) closes the set at four. Disclosure of Order Execution Information (88 FR 3786, Jan. 20, 2023) is the only one left, so it is S7-29-22.
- Arithmetic (Python datetime, end date minus start date, 2023 not a leap year): 98 + 81 + 74 = 253, and 253 / 3 = 84.333 -> 84.3.
- Alternatives: 91.7 (the named trio), 86.0, 94.0, 89.0 (all four), 85.3 (counting both end days).
- Where both documents give a date, they agree, so no rounding route exists. All nine evidence quotes appear word for word in text/, docs/ and the capture's own Doc 6 and Doc 4 text.

outcome: A: match; B: match. Both answered 84.3 using the file-number map plus elimination, and both named and rejected 91.7. The packets match the corpus byte for byte, and question.txt holds only the verbatim question. The only extra context was the harness's git-status listing, so neither is contaminated.

closed-book: misses. About 76.3, not equivalent to 84.3. It picked the gold trio by subject matter but guessed an April 3 letter date. All three closed-book runs (83.7, 90.7, 76.3) recalled the four Federal Register dates exactly; only the bundle's letter date stands between memory and the gold.

necessity: neither document can be replaced, and no smaller source set exists.
- Doc 6 (D01): only source of the letter's file set and of the S7-30/31/32-22 map (a whole-bundle search with dash variants finds those numbers only in D01, plus D05's s7-29-22 URL). Without it, 84.3, 86.0, 91.7 and 94.0 all stay possible. Probes: unforced "cannot be determined" twice; forced 84.3 at p 0.35 (rev 0) and 94.0 at p 0.6 (rev 1).
- Doc 4 (D05): only source of the Order Execution Information proposal, the 3786 citation, Jan. 20, 2023, and the "set of four" that closes the elimination. Without it, the answer is (172 + x) / 3, or the decoy. Probes: unforced "cannot be determined" all three times; forced 84.3 at p 0.6 (sketch), 91.7 at p 0.6 (rev 0, with 84.3 as runner-up at 0.25), 84.3 at p 0.75 (rev 1); each gold guess came from memory.
- The probe packets are the current corpus minus one document, renumbered without gaps, with the matching original removed from docs/.

shortcut: clear. Auditor's route confirmed: "Antitrust" -> D01 line 147 and D05 line 141 -> footnotes 2 and 13 -> footnote 16 -> elimination and arithmetic. No passage prints 84.3, 253 or 91.7. The capture overview shows only "April 11, 2023" and "Department of Justice" under Doc 4, and "December 29, 2022" (the decoy's date) under Doc 6. The search finds the inputs, not the whole answer.

source_assessment: the report shows source_gaps []. Intake shows 12 of 12 documents complete, and all corpus hashes match the snapshot. No exact gap labels to map. The image-only ranges named in hooks.md hold nothing relevant: D02 lines 59-61 (a CDP Scope 3 table), D04 line 213 (a PRI survey graphic) and the D10 figures (DEI word counts); none holds file numbers, Federal Register dates, the DOJ letter or equity-market proposals, so they cannot touch the premises, gold, exclusions, uniqueness, necessity or shortcut. Not a claim that the corpus is complete.

difficulty: medium (marginal), local suitability only.
- For: an answer-shaped decoy sits in the path. Footnote 23's trio echoes the question's "three ... equity market structure" and is dated in the same letter. Escaping it needs footnote 2, about 130 lines earlier, plus elimination from another letter's list.
- Against: the file numbers sit in the decoy's own citation, so the trap is partly tied (Easy risk). The arithmetic is trivial, and Doc 4's input is public.

verdict: ready (local). Keep status checked; the platform result is pending.

failure_modes:
- FM1 (Linking across documents / Wrong members in a list) is real. Recomputed: 103 + 98 + 74 = 275, 275 / 3 = 91.67 -> 91.7. The wording does not rule it out.
- Trap and cause are the best fit from the form's lists; "Picks the wrong entity or section" is a weaker alternative cause.
- All three boxes are true (284 words in total). Rev 0's fixes (4) and (5) are made.
- Optional wording point: box 3 calls Order Execution Information "the fourth" proposal, which could be read as its position in the list; footnote 16 lists it first.
- Roles: "Answer component" for both documents fits how they are used. Doc 6 supplies the Jan. 3, Jan. 27 and Apr. 11 dates and the selection; "Used to identify" would also fit Doc 6, but no change is needed.

findings:
1. Rev 0's required fixes are done correctly. A snapshot diff shows only the reasoning and failure-mode boxes changed; question, answer, components, evidence, roles, metadata and corpus byte-identical. The report recomputes the fingerprint as 495a38f8...; Lever checks and failure modes sit outside it. Steps 8 and 9 and both arithmetic decoy lines now name their documents (all decoy inputs are in Doc 6). Step 2 and box 3 now describe footnote 2 correctly.
2. Form number check: every new result follows "=". Steps 8 and 9 reuse derived operands in steps citing Doc 4 and Doc 6. That pattern passed on aq-00949 q05; the one contrary case (aq-01321) had a period label. Residual risk low.
3. Possible false-positive advisory: Doc 6 footnote 12's "average of 38 days" (also in the overview) may trigger "Answer matches a stated figure". Different measure; advisory only.
4. Optional, not required: Step 4 credits a body-text sentence (Doc 4 line 126) to "footnotes 15 and 16".
5. Records: all six rev 1 records carry rev 1 and this fingerprint, and the raw headers match. The report shows no mechanical failures. Floor 0 FAIL and 1 WARN (origin claude is accurate; the export restriction is the user's call).
6. Platform-only checks unknown: restricted names, Original question / Not a duplicate, token window, the model checks. Doc 4 line 514 has "philanthropic", which a substring-based vendor-name scrub could hit; speculative.
7. Set: no sibling question yet. Any future question on this bundle should avoid the DOJ-letter / equity-proposal path.

Platform estimate (if the form checks pass): Too easy 2%; Easy 33%; Medium 40%; High 6%; Between levels 14%; Too hard / Answer not supported 5%. A usable Medium-or-High tier about 46%.
Removal flag, weighing all five probes: Doc 4 about 28% (15-45%): two of three forced guesses hit the gold from exact recall (S7-29-22 = Rule 605, Jan. 20, 2023), but the platform's document check does not always guess. Doc 6 about 10% (5-20%): recall of the letter's coverage is inconsistent (forced 84.3, then 94.0). Either flag about 35%. A usable first-run pass (Medium or High with no flag) about 30%. The form's free "One defensible answer" block (both form solvers answering 91.7) about 15%.

Required changes before a platform run: none to the question, answer, documents, roles or reasoning. No fair rewording removes the Doc 4 recall risk, so state it at hand-over. Do not tighten the wording toward file numbers.
