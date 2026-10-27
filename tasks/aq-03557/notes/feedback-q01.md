# aq-03557 q01 - observations after submission

questions/q01.md is frozen as submitted (rev 2, origin user+claude, status submitted, accepted_tier: Medium Tier;
file sha256 8560b54de18fba223c8ac68dfb938b34fd0d74912ae75e717bd66be4cc5df683 at freezing, 2026-10-12;
tested_sha256 114f324f94a54e12d54cca42851d4d249f827dc0d4f5408a4b32b75b972080dd). Do not edit it. Append later
platform observations below, oldest first, with date, source, exact words and artifact link.

## State at submission (2026-10-12)

- Difficulty: Run 1, Oct 12, 2026, 10:51 PM, Version d8243a (current), "In band — Medium tier", Low 0/5 · Medium
  1/5 · High — (verdicts/AQ-03557_difficulty_2026-10-12_2319.txt). "The difficulty check passes on the current
  content." "+$20 Medium+ bonus if accepted". 14 of 15 runs left.
- Binding: the run quotes rev 2's question word for word ("With the number of stores Woolworths provides, how
  many supermarkets trade under banners that any retailer's submission says have no loyalty programme?"), shows
  "Your answer: 376 supermarkets" and removes documents 7 and 3 in its Document check. Question, answer and
  necessary documents are therefore rev 2's. Reasoning, evidence rows, tags and failure modes as submitted were
  not captured; the hand-over was notes/handover-q01.md (rev 2), and the user may have reworded the reasoning on
  the form.
- Closed-book check: "Needed the documents ✓" (the attempt guessed Aldi's Australian stores, about 590).
- Document check: every-document attempt 376 ✓; "Needed document 7 ✓" twice; "Needed document 3 ✓" twice (301 both
  times: without Doc 3 the high solver did not assume FreshChoice and had no status for Raeward Fresh).
- No Coach panel, no "may be too vague" advisory, no "marked document may not be needed" in the capture.
- Submission: user report in chat, "submitted as medium tier" (2026-10-12). The submitted form was not captured.
- Platform Checks (39): only rev 0's partial screenshots are recorded (notes/platform-feedback/). The outcome of
  "Question in your own words" on rev 2 was not sent; clearance unknown.
- Pending: reviewer outcome; acceptance (not observed).
- observed_platform_status: unknown (submitted; no review result yet).

## What each attempt did (read from its own Full answer and Reasoning)

Read in full: Low 1-5, Medium 1, Medium 4, the every-document attempt, the closed-book attempt. Medium 2: Full
answer read, Reasoning saved as "Loading the reasoning…". Medium 3: Full answer is the bare value 372 and its
Reasoning was not loaded, so its route is unread. Medium 5 is marked Right with no text recorded. The four
removal attempts: Full answers read, reasoning only in part (one not loaded).

| Attempt | Committed | What it cleared | Where it left the gold |
| --- | --- | --- | --- |
| Low 1 | 301 | Doc 7's loyalty answer (PAK'nSAVE, Four Square, SuperValue); Chemist Warehouse set aside as not a supermarket; Doc 3's Raeward Fresh sentence; Doc 7's rival counts | Dropped the 71: SuperValue is not counted apart from FreshChoice and it never read Doc 3's next sentence ("FreshChoice ... unknown"). Dropped Raeward Fresh: "Woolworths doc 7 mentions Farro Fresh six stores, etc. Not Raeward" |
| Low 2 | 301 | Doc 3's PAK'nSAVE, Four Square and Raeward Fresh sentence (also credited to Doc 2); Doc 7's rival counts | Did not read Doc 7's loyalty answer or Doc 3's next sentence ("Not SuperValue"); "Woolworths submission doesn't mention Raeward Fresh store counts" |
| Low 3 | 71 | Doc 7's loyalty answer; Doc 2's "other FSNI brands" | Believed Woolworths gives no PAK'nSAVE or Four Square counts, so it limited "the number of stores Woolworths provides" to Woolworths' own banners and answered with the 71 |
| Low 4 | 301 | Doc 2 and Doc 3 for PAK'nSAVE and Four Square; found Doc 7's rival counts late | "Raeward Fresh is mentioned but not in Woolworths list"; for the 71, "Does any submission say they have no loyalty? Possibly not mentioned" |
| Low 5 | 301 | Everything in Doc 7 (three banners, Chemist Warehouse set aside, rival counts, the 71); Doc 3's Raeward Fresh sentence; weighed 372 | "FreshChoice ... Not mentioned" (Doc 3's next sentence unread), so the 71 stayed out; "Woolworths doesn't provide Raeward Fresh" counts |
| Medium 1 | none | All five banners, Doc 3's FreshChoice sentence, 56, 245, 71 and Raeward Fresh's four stores in Doc 7's "Other supermarkets" list | Went looking for a split of the 71 it did not need; its output then repeated one phrase until it ended. No final answer |
| Medium 2 | 71 | Four banners including FreshChoice, with Doc 3's sentence quoted | Full answer: "Among the stores Woolworths provides, the SuperValue and FreshChoice banners are identified" - the opening phrase taken as Woolworths' own stores. Reasoning not loaded |
| Medium 3 | 372 | unread | Route unread (bare value, Reasoning not loaded). The platform's note says it omitted Raeward Fresh; not checked against the attempt |
| Medium 4 | 71 | Doc 7's loyalty answer; Doc 3's Raeward Fresh sentence (credited to Doc 2 as well) | First line: "the number of Woolworths supermarkets that trade under banners ...". Own-stores reading; SuperValue named, so 71; Doc 3's FreshChoice sentence unread |
| Medium 5 | right | not recorded | - |
| High, every document | 376 | Reached 372 first ("Woolworths doesn't provide a specific number for Raeward Fresh"), then found the list. Weighed the own-stores reading four times and set it aside: Woolworths' submission gives rivals' counts and the question says "any retailer's submission" | - |

## What separated the solvers

1. Doc 3's sentence on FreshChoice and SuperValue, one line below the Raeward Fresh sentence: no low attempt
   read it (four quoted or paraphrased the line above), so none could take the combined 71. Medium 1 and 2 read it.
2. Raeward Fresh's count in Doc 7, in a list of small rivals that resumes after a block of footnotes: no low
   attempt found it and four said outright that Woolworths gives none. Medium 1 found it; the high solver found
   it on a second look.
3. The opening phrase read as Woolworths' own stores (71): Low 3, Medium 2, Medium 4. This is a reading of the
   question, not of the documents. The high solver rejected it from the sentence's own words.

## Known soft spots if a reviewer asks

- Declared failure mode 2 ("Wrong kind of entity": Chemist Warehouse's 16 stores added, 392) caught no attempt;
  Low 1, Low 5 and the high solver set the chain aside explicitly. Mode 1 ("Linking across documents": Raeward
  Fresh left out, 372) describes a gate every low attempt failed, but their answers were 301 because they dropped
  the 71 as well; the one 372 (Medium 3) is unread. The commonest wrong answers were undeclared: 301 (four low
  attempts; Doc 3's FreshChoice sentence unread) and 71 (three attempts; own-stores reading). If the task is
  returned for its failure modes, the evidence-backed picks are "Part vs total" for 301 (the two banners Doc 7's
  own sentence names taken for the whole) and mode 1 as it stands.
- The reasoning's Step 1 says Woolworths "describes that chain as a pharmacy retailer"; no evidence row quotes
  that description (Doc 7 L61 "largest pharmacy retailer", L292 "Health and beauty retailers and pharmacies").
  A reviewer applying the rule that every side claim has a quote may ask for one.
- The 71 reading: three solvers took the question to be about Woolworths' own stores. A reviewer could call the
  opening loose. The answer under that reading (71) needs only what Doc 3 and Doc 7 say about SuperValue and
  FreshChoice; the question's "any retailer's submission" and Woolworths' rival counts are what rule it out.

## Later observations

