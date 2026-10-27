# aq-02749 q02 - observations after submission

questions/q02.md is frozen as submitted (rev 0, status submitted, accepted_tier: Medium Tier; file sha256
275be2a42807f1e64feaf940b0dc493b71d9afe2d3113ce3332c9c319010e52d at freezing, 2026-10-11; tested_sha256
8f89465983f0b3a73ca73e16c7476db9c094d7fcb510483c8fa96053fa60e7ce). Do not edit it. Append later platform
observations below, oldest first, with date, source, exact words and artifact link.

## State at submission (2026-10-11)

- Difficulty: Run 1, Oct 11, 2026, 10:34 AM, Version 94672c (current), "In band — Medium tier", Low 0/5 · Medium 3/5 ·
  High — ([verdicts/AQ-02749_difficulty_2026-10-11_1128.txt](../verdicts/AQ-02749_difficulty_2026-10-11_1128.txt));
  "+$20 Medium+ bonus if accepted"; "9 of 10 runs left".
- Identity: the run quotes the question verbatim and shows "Your answer: 10 amendments"; the Document check removed
  Docs 5, 6 and 2, the three ticked documents. Reasoning, evidence, tags and failure-mode boxes are not in the capture.
- Document check: every-document attempt reached 10; without Doc 5: 9 (twice); without Doc 6: 3 (twice); without
  Doc 2: 1 (twice). Closed-book: "Two.", needed the documents. No Coach panel, no "may be too vague" advisory, no
  "marked document may not be needed".
- Submission: user report in chat, "submitted as medium tier" (2026-10-11). The submitted form fields were not
  captured; the hand-over was notes/handover-q02.md (rev 0). Whether the failure modes were pasted as handed over is
  not recorded.
- Platform Checks (39): no capture recorded; clearance unknown.
- Pending: reviewer outcome; acceptance (not observed).
- observed_platform_status: unknown (submitted; no review result yet).

## What each attempt did (platform grades; routes read from each attempt's own Full answer and Reasoning)

Corrected 2026-10-12 from the second capture of the same run
([verdicts/AQ-02749_difficulty_2026-10-12_0028.txt](../verdicts/AQ-02749_difficulty_2026-10-12_0028.txt), every
Reasoning block loaded; the first capture still showed "Loading the reasoning" for the closed-book attempt, Low 1
and Low 3). The 2026-10-11 version of this section named the two medium routes from their numbers alone and had
both wrong; see the last section.

- Low 1-5 (0, 0, 0, 0, "One (40 CFR 257.90(g))"): two inferences failed in every attempt. (a) Wyoming: each took it
  to lack only the provisions its proposal names (257.50(e), vegetative cover, 257.90(g), 257.95(h)(2)), never
  expanding the grouped "Amendments made in the Legacy ... Final Rule" into the twenty entries. (b) Wisconsin: each
  took its eleven-entry approved list as approving all twenty ("Wisconsin ... includes all of the above", Low 2),
  so absence from an enumerated list was not read as no approval. Four of the five did read Alabama's three
  definitions as unapproved, the one exclusion printed as an explicit "not being approved" list. Three also counted
  provisions outside the 2024 rule.
- Medium 1, 3, 5: 10, with the full table (Wyoming lacking all, Alabama three, Wisconsin nine).
- Medium 2: 9. Wyoming and Wisconsin right; Alabama's list read as "17 amendments, but appears to be the same 20",
  so Alabama lacked none and only Wisconsin's nine counted.
- Medium 4: 6. Wyoming and Wisconsin right; Alabama's seventeen entries mapped to the wrong members ("Missing A10,
  A14, A15": it kept the three unapproved definitions and dropped "Inactive CCR surface impoundment" and the two
  "Technically ..." entries), leaving six entries missing in Wyoming and Wisconsin only. It is not the list-length
  subtraction, although 17 - 11 is also 6.
- High, every document: 10, from a five-column table identical to the lever checks' matrix (it also counts the twelve
  more prescriptive amendments as lacking in all five). No second reading raised. Without Doc 5: 9 (twice); without
  Doc 6: 3 (twice); without Doc 2: 1 (twice).

## Known soft spot if a reviewer asks

- Declared mode 1 ("Linking across documents", Wyoming left out, 1): the Wyoming link failed every low attempt, with
  committed answers 0 and "One"; the number 1 came only from the Document-check attempts without Doc 2.
- Declared mode 2 ("Wrong jurisdiction or scope", Alabama given Wisconsin's two approved definitions, 8): no attempt
  wrote 8, but both medium misses are the same place going wrong, Alabama's list read with the wrong members (9 with
  all twenty, 6 with the wrong three missing). The mode's mechanism was observed; its number was not.
- If the question is handed back, the measured modes are: the Wyoming link (0), and Alabama's shorter list read as
  the full list (9) or with the wrong three entries missing (6).

## What the 2026-10-11 reading got wrong

- It called Medium 4's 6 "the list-length subtraction 17 - 11" and Medium 2's 9 "a miscount". Both Reasoning blocks
  were loaded in the first capture (lines 1485-1781 and 1038-1211); I read their opening lines only and matched the
  numbers to routes I had predicted.
- It described the low failure as Wyoming alone. The Wisconsin inference failed in all five as well.
- It said declared mode 2 "caught no attempt". Its mechanism caught both medium misses.
- Those statements also went into the calibration memory, the memory index, ideas.md, session.md and the report to
  the user; all were corrected on 2026-10-12. tools/verdict_summary.py now prints each attempt's line span, whether
  its Reasoning was loaded, and a note when a wrong attempt's Full answer is a bare value.

## 2026-10-12 - "Revision requested" (second send-back; the question is handed back and editable again)

Source: user screenshot of the task list row, saved as
[verdicts/AQ-02749_revision-requested_2026-10-12.png](../verdicts/AQ-02749_revision-requested_2026-10-12.png).
Row: "Coal Ash Program Approvals · AQ-02749 (revision requested)" · "Government_Consultations" · "Needs Revision" ·
"Revise & Resubmit". The panel says an earlier send-back went unapplied; that first panel was never supplied to this
workspace, and the reasoning the reviewer quotes ("these documents are not to be counted", "contains another three
entries", "None of them have an approved version in Wyoming and Wisconsin only", "the two entries have no approved
version in Wyoming only") is not the hand-over's wording, so the submitted reasoning was a reworded version that was
not captured here. Panel text, verbatim:

> Revision requested
> None of the changes requested in the previous send-back were applied; all items below are still open. The gold
> answer (10) is correct and both traps land, so no change to the question or answer is needed. Please add Docs 3 and
> 4 as necessary documents, add the supporting quotes, and fix the wording in Steps 2, 4, 6 and 7.
>
> Requested changes
> - Add Doc 3 (Virginia) and Doc 4 (Louisiana) as necessary documents, role 'Exclusion / condition source'. The
>   'exactly two States' condition depends on both approving all 20 all-unit amendments. Also remove 'these documents
>   are not to be counted' from Step 4.
> - Add verbatim evidence: (a) one quote each from Doc 3's and Doc 4's approved lists showing they approve
>   'Infiltration', 'Liquids' and a Wisconsin-missing item such as '2. 40 CFR 257.50(c)'; (b) one quote supporting
>   Step 4's claim that the more prescriptive all-unit amendments are approved in no State, e.g. Doc 5: 'ADEM did not
>   adopt these amendments and did not seek approval of these provisions.'
> - Fix the solution explanation wording. Step 2: Alabama's not-approved list has 5 entries (incl. 40 CFR 257.71(d)
>   and 257.90(g)); only 3 are 2024 Legacy Rule definitions, so say '3 of the 5 entries'. Step 6: change 'None of them
>   have an approved version in Wyoming and Wisconsin only' to 'each lacks an approved version only in Wyoming and
>   Wisconsin'. Step 7: reword 'the two entries have no approved version in Wyoming only' so it clearly says items
>   missing in only one State, or in three, are excluded.
>
> Issues the reviewer found
> - Evidence · Wrong / missing evidence: Not fixed from the last send-back. Docs 3 (Virginia) and 4 (Louisiana) are
>   still missing from the necessary documents, and Step 4 still says they are 'not to be counted'. They are needed:
>   the 'exactly two States' condition only holds because Virginia and Louisiana approve all 20 all-unit amendments.
>   Doc 3's approved list includes '2. 40 CFR 257.50(c)', '11. ``Infiltration''' and '12. ``Liquids'''. Add Docs 3 and
>   4 as 'Exclusion / condition source' with a verbatim quote from each approved list.
> - Evidence · Unsupported claim: Not fixed from the last send-back. Step 4 claims the more prescriptive all-unit
>   amendments (e.g. 'Operator', 'Owner', 40 CFR 257.80(b)(6), 257.102(c)(2)) are approved in no State, but no quote
>   supports it. It is true: Docs 3 and 5 each say the State 'did not adopt these amendments and did not seek approval
>   of these provisions.' Add one such quote. Component 1 (10) also still has no quotes from Virginia or Louisiana, so
>   the evidence does not prove the answer on its own.
> - Other · Factual error: Not fixed from the last send-back. Solution explanation Step 2 still says Alabama's
>   not-approved list 'contains another three entries'. Doc 5's list ('as enumerated below, are not being approved')
>   has 5 entries: 'Contains both CCR and liquids', 'Infiltration', 'Liquids', 40 CFR 257.71(d) and 40 CFR 257.90(g).
>   Only the first 3 are 2024 Legacy Rule all-unit definitions. Say '3 of the 5 entries'. Answer is unaffected.
> - Other · Ambiguous wording: Not fixed from the last send-back. Step 6 still says the 8 items 'None of them have an
>   approved version in Wyoming and Wisconsin only'; change it to 'each lacks an approved version only in Wyoming and
>   Wisconsin' (Virginia, Louisiana and Alabama approve them). Step 7 still ends 'the two entries have no approved
>   version in Wyoming only', which is unclear; reword it so it clearly says items missing in only one State
>   (Wyoming), or in three States ('Contains both CCR and liquids'), are excluded.
> - Other · Unsupported claim: Component 1 ("10") is not supported by the cited evidence. The 12 quotes cover
>   Wyoming, Alabama and Wisconsin only. Nothing from Doc 3 (Virginia) or Doc 4 (Louisiana) shows they approve all 20
>   amendments, so the quotes cannot rule out a third State lacking the 10 items. The gold value 10 is correct.

observed_platform_status: revision requested (2026-10-12). Question and gold confirmed correct by the reviewer.

Author's reading of the cause (mine, not the reviewer's words): rev 0 left Docs 3 and 4 unticked because the
Document check finds a document "not needed" when the answer survives its removal, and its Step 4 relied on them and
on the "more prescriptive" amendments without a quote. The reviewer's test is different: every State the count
depends on must be evidenced and its document marked, here with the exclusion role. Rev 0's Step 2 also said the
not-approved list "holds three more" although the list has five entries.

Action: rev 1 in questions/q02.md applies the three requested changes and nothing else (question, answer, components,
tags and failure modes unchanged). Ticking Docs 3 and 4 changes the necessary documents, so the platform needs a new
difficulty result before resubmission.

## 2026-10-13 - difficulty Run 2 on rev 1: "Between levels"

Source: [verdicts/AQ-02749_difficulty_2026-10-13_0712.txt](../verdicts/AQ-02749_difficulty_2026-10-13_0712.txt)
(saved 07:12; every Reasoning block loaded; "13 of 15 runs left"). Run 2, Oct 13, 2026, 12:56 AM, Version 54eee2
(current), Low 0/5 · Medium 4/5 · High —. "What changed before this run: the documents or the documents marked
necessary changed". Page: "Too hard for the low model but too easy for the medium model. Make it a little harder, so
the medium model reaches your answer only some of the time, then run the check again." and "One in-band run on this
page measured an earlier version, so it does not count." No High attempts and no Document check in this run.

Each attempt, from its own Full answer (what it cleared / where it left the gold):

- Low 1: found both lists; took Wyoming as meeting the standard and the three definitions as missing only in Alabama: 0.
- Low 2: found both lists; Wyoming read as lacking only 257.90(g) and 257.95(h)(2); the first list "covered": 0.
- Low 3: "All five States adopted the same core set of 20": 0.
- Low 4: the three added definitions read as approved for Wyoming, Virginia and Louisiana and missing in Alabama and
  Wisconsin: 3. (Wisconsin's list has two of the three.)
- Low 5: the first list read as covered in every State, Wisconsin included: 0.
- Medium 1, 2, 3: 10, by the State-by-entry table. Medium 2 also lists the more prescriptive twelve as lacking in all
  five; Medium 1 and 3 never mention that list.
- Medium 4: read "all-unit amendments" as the more prescriptive list only: none (all 12 lack a version in all five).
- Medium 5: graded Right; "This attempt's text was not recorded." Route unread.

Coach (one item, under "Make it harder"): define the term in the question as both lists. Its reason says the low
answers "show it read only one list"; the Full answers above show the low attempts read both lists and failed on
Wyoming and Wisconsin. Not taken.

Across Runs 1 and 2 (one solver task; only the ticks differed): Medium right 7 of 10. Of the six right attempts with
recorded text, five never mention the more prescriptive list (Run 1 Medium 1, 3, 5; Run 2 Medium 1, 3).

Action: rev 2 adds a second parallel count ("and how many in all five?"; gold "10, 12"). Rev 1's reviewer changes are
kept. A wording-only edit was not used: it would have measured the same task a third time. Result pending.

## 2026-10-13 - difficulty Run 3 on rev 2 and the form's checks (screenshots only)

Source: four user screenshots, verdicts/AQ-02749_form_2026-10-13_run3_question-gold.png, _checks.png, _difficulty.png
and _history.png. No text capture of the run was supplied, so no attempt's Full answer or Reasoning has been read:
routes unread.

- Run 3, Oct 13, 2026, 10:41 AM, Version e40592 (current). "What changed before this run: question: removed "States?";
  added "States, and how many in all five? Give the two counts in that order.". answer: removed "10 amendments"; added
  "10, 12"". Low model 0/5 right, Medium model 2/6 right ("Medium model: three solvers try up to 3 times each. Ready when
  at least two get it wrong twice and one gets it right twice. A level stops as soon as more attempts could not change
  the result."). "Solver summary: Run 3 · A marked document may not be needed · 2 of 11 right".
- Gate: "A marked document is not needed" · "Result the gate uses". "The result on the current content is still
  answerable without a document marked necessary, so the gate does not pass." Banner: "Your answer can still be reached
  without documents 3 and 4. Either those documents are not needed, or the question does not yet depend on them. If the
  document is needed (for example, it holds the item your question excludes), name it as excluded in your reasoning
  ("Document 4 is excluded because..."): that clears submit without a new run, and the reviewer checks it. Or leave a
  one-line note for the reviewer below. Otherwise fix the question or the documents you marked necessary, then run the
  check again." Note box: "Is documents 3 and 4 needed? Say why in one line. The note goes to the reviewer, and any edit
  to the question, answer, reasoning or necessary documents clears it." (0 / 200).
- Submit: blocked, "The difficulty check found the answer can still be reached without one of the documents you marked
  necessary. ..."
- Coach, "What to change: Make it depend on the marked documents": "If Document 2 must be necessary, ask something that
  only Document 2 answers ..." with "From a run (High model · attempt 2): Reached the gold answer without Document 2
  (Wyoming), inferring Wyoming's non-adoption of the 2024 Legacy Rule from the other States' partial-program
  descriptions". The banner names documents 3 and 4 only, and Run 1's check answered 1 without Doc 2 both times. The
  Coach's statement is unverified until the text capture is read.
- Checks rows shown: "Left-out items do not qualify" Warning · advisory ("Docs 1 and 2 (not the documents you marked)
  also give this answer. Doc 1: "12, 1993 (OMB Memo M-94-3), the approval of State program amendments is" Doc 2: "the
  Wyoming CCR Permit Program, see page 7 (PDF page 10) of the"" and the same with Doc 4: "2024), or the February 10,
  2026 final rule (91 FR 5806)."); "Each description fits one thing" Warning · advisory (""all five" - 3 matches:
  Virginia (Doc 3, prose), Louisiana (Doc 4, prose), Alabama (Doc 5, prose)"; ""the 2024 Legacy Rule's all-unit
  amendments" - 3 matches: Virginia (Doc 3, prose), Alabama (Doc 5, prose), Wisconsin (Doc 6, prose)"). Passed: "No
  single passage gives the answer", "Answer matches a stated figure", "Answer covers every ask", "Needs the documents".
- Slots line: "Hard 0/3 · Medium 0/2 · Easy 0/0 ... In review: Medium 1. 7 submissions left on this document set."
  "12 of 15 runs left".

Reading (author's, not the platform's): the two advisory rows are text matches, not second answers. The digits 12 and
10 of the gold occur in a date and a page number in documents that say nothing about amendments; the two phrases match
prose in several proposals because the question is about all five. Neither blocks, and changing the question for them
would cost the Run 3 result. The block is the one predicted when Docs 3 and 4 were ticked at the reviewer's request: a
solver working from the other proposals still reaches the answer. The form's route is the one-line note.

Note handed to the user for the difficulty-check box (within its 200 characters):
"Docs 3 and 4 are condition sources the reviewer asked for: Virginia and Louisiana approve all 20 first-list
amendments and did not adopt the other 12, so two States lack the 10 and all five the 12."

What I had not given the user in the rev 2 hand-over: this note. I wrote that the reviewer note in the Necessary
documents panel was "the form's route"; the page blocks Submit until a separate one-line note is saved in the
difficulty check, and the two advisories were not announced either.

## State at resubmission (2026-10-13)

questions/q02.md is frozen again as submitted (rev 2, status submitted; file sha256 10f2afcf0e214af3deb9faaf3742a56d98ea8a7a57a10c4e574024e50736476c
at freezing; tested_sha256 f8ddf50d5b33dbee9db14f4c8ada6e8cf9041f00c5e09542c9d14cfb5fd4fabe). Do not edit it.

- Submission: user report in chat, "submitted with that note. Let's wait for the result" (2026-10-13). The note is the
  one-line reviewer note handed over for the difficulty-check box (197 characters, text above). The submitted form
  fields were not captured; the hand-over was notes/handover-q02.md (rev 2).
- Difficulty: Run 3, Version e40592, Low 0/5 · Medium 2/6; run label "A marked document is not needed"; no tier label
  observed for this run, so accepted_tier is not recorded. The slot line before submission read "In review: Medium 1".
- Not done before Submit: the Run 3 text capture was not supplied, so the attempts' routes are unread, the Coach's
  claim about Document 2 is unverified, and the failure modes went in as handed over (Wyoming link; Alabama scope)
  without being matched to Run 3's misses.
- Open questions a reviewer could raise (from the lever checks): the question and answer changed after the reviewer
  wrote that no change was needed; whether "amendments" in the second count means the twelve entries; whether Docs 3
  and 4 are accepted on the note.
- Pending: reviewer outcome; acceptance (not observed).
- observed_platform_status: unknown (resubmitted; no review result yet).

- 2026-10-13, later the same day | source: user chat, verbatim "oh, it was medium tier" | observation: rev 2 was
  submitted at the Medium tier (accepted_tier: Medium Tier). This supplies the tier that the Run 3 screenshots did not
  show; the counts were Low 0/5 · Medium 2/6. The question file was already frozen when this arrived, so its front
  matter is left as submitted and the tier is recorded here and in notes/session.md. Review outcome still pending.

- 2026-10-13, after resubmission | source: user screenshot of the task list row, saved as
  verdicts/AQ-02749_review-ready_2026-10-13.png (no message text) | observation: the row now reads "State Coal Ash
  Approvals · AQ-02749" · "Government_Consultations" · "Review Ready" · "View". On 2026-10-12 it read "Coal Ash Program
  Approvals · AQ-02749 (revision requested)" · "Needs Revision" · "Revise & Resubmit". The "Revision requested" panel
  shown under the row is word for word the 2026-10-12 panel logged above (same summary, same three requested changes,
  same five issue cards): a re-shown artifact of the earlier send-back, not a new return. No review result for rev 2 is
  shown. observed_platform_status: in review ("Review Ready"); acceptance not observed.
