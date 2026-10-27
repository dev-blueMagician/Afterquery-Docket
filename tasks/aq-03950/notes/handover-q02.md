# aq-03950 q02 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-03950 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target hard, origin claude.
- tested_sha256 cfc8c753dba45347e32f4e6fa70c03ba92491659befb6b21405a4af4ee4c475b: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D05 = Doc 6, D06 = Doc 7, D07 = Doc 1.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Judging by all the evidence the committee heard, which witnesses, if any, held or had held a role at VisitBritain? List them in any order.
```

### Number of asks

1 ask

### Gold answer

```text
Anthony Pickles, Patricia Yates, Ian Edwards
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 1, witness list): the report lists every witness with a title. Two titles are VisitBritain posts. Anthony Pickles is "Former Head of Tourism Affairs, VisitBritain" (first component). Patricia Yates is "Chief Executive, VisitBritain/VisitEngland" (second component). Doc 6 prints the same title for Pickles and Doc 7 the same title for Yates, each in its own list of witnesses.
Step 2. Source input (Doc 1, witness list): Ian Edwards is listed as "Chief Executive, The Celtic Collection and ICC Wales". His title shows no link to VisitBritain.
Step 3. Source input (Doc 6, Q158): Anthony Pickles tells the committee that Ian Edwards, "who you have heard from", "sits on the VisitBritain board". A seat on its board is a role at VisitBritain, so Edwards belongs in the list (third component). Doc 1 says only that "A Welsh representative sits on the VisitBritain board" and names nobody.
Step 4. Decoy (Doc 6, Q148): Annette Pritchard says she "previously did work for the Wales Tourist Board". That is a different body, so she is left out. No other title in Doc 1's witness list names VisitBritain.
Step 5. Final answer (Doc 1 and Doc 6): Anthony Pickles, Patricia Yates, Ian Edwards.
```

### Answer components

Component 1

```text
Anthony Pickles
```

Component 2

```text
Patricia Yates
```

Component 3

```text
Ian Edwards
```

### Evidence

Evidence 1: document Doc 1 (ukc_6476_report_40824.txt), proves component 1. Anthony Pickles (local note: Witnesses, 20 July 2022)

```text
Anthony Pickles, Former Head of Tourism Affairs, VisitBritain
```

Evidence 2: document Doc 6 (ukc_6476_oral_10647.txt), proves component 1. Anthony Pickles (local note: header, witnesses)

```text
Anthony Pickles, Former Head of Tourism Affairs, VisitBritain
```

Evidence 3: document Doc 1 (ukc_6476_report_40824.txt), proves component 2. Patricia Yates (local note: Witnesses, 1 February 2023)

```text
Patricia Yates, Chief Executive, VisitBritain/VisitEngland
```

Evidence 4: document Doc 7 (ukc_6476_oral_12643.txt), proves component 2. Patricia Yates (local note: header, witnesses)

```text
Patricia Yates, Chief Executive, VisitBritain/VisitEngland
```

Evidence 5: document Doc 1 (ukc_6476_report_40824.txt), proves component 3. Ian Edwards (local note: Witnesses, 20 April 2022)

```text
Ian Edwards, Chief Executive, The Celtic Collection and ICC Wales
```

Evidence 6: document Doc 6 (ukc_6476_oral_10647.txt), proves component 3. Ian Edwards (local note: Q158, Anthony Pickles)

```text
We have Ian Edwards, who you have heard from, who sits on the VisitBritain board, so he is Wales’s voice on there.
```

Evidence 7: document Doc 1 (ukc_6476_report_40824.txt), proves component 3. Ian Edwards (local note: para 66)

```text
A Welsh representative sits on the VisitBritain board.
```

Evidence 8: document Doc 6 (ukc_6476_oral_10647.txt), proves component 3. Ian Edwards (local note: Q148, Professor Pritchard)

```text
I previously did work for the Wales Tourist Board
```

### Necessary documents

- Tick Doc 6 (ukc_6476_oral_10647.txt), role: Answer component
- Tick Doc 1 (ukc_6476_report_40824.txt), role: Answer component; also tick Doc 7 (ukc_6476_oral_12643.txt) and choose it in Doc 1's "or..." box

Leave unticked: Doc 2 (ukc_6476_oral_10125.txt), Doc 3 (ukc_6476_oral_10124.txt), Doc 4 (ukc_6476_oral_10335.txt), Doc 5 (ukc_6476_oral_10428.txt)

### Reasoning tags

Tick: Cross-document join, Entity resolution

Leave unticked: Temporal alignment, Unit normalization, Conditional filter, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Linking across documents: Doc 1's witness list gives VisitBritain titles to Anthony Pickles and Patricia Yates only, and lists Ian Edwards as a hotel and convention-centre chief executive. His seat on VisitBritain's board appears only in Doc 6, in Pickles's answer. Titles alone give two names; the join adds Edwards.
```

(50 / 50 words.)
