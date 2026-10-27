# aq-05177 q02 hand-over

Generated 2026-10-15 by `python tools/check_questions.py tasks/aq-05177 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target hard, origin claude.
- tested_sha256 4ef235de62ffe00be7ea42179bce316774b9cb66fe71936002fceb2428848168: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D05 = Doc 5, D06 = Doc 6, D07 = Doc 7.
- Floor: 0 FAIL, 4 WARN.
  - WARN strong-screen: the strong solver was right in every fresh solve of this exact sentence: likely Too easy at High. Say so with the hand-over; the user decides whether to run it. Never reword or re-screen the sentence to find a miss
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN documents: D06: exclusion role; a platform reviewer accepted it only for a document ruling out an item that exists without it, not for its own decoy (aq-01333 q01)
  - WARN single-passage: one passage of D08 holds the answer: '...made considerable efforts to provide an accurate transcription. there may be material errors, omissions, or inaccuracies in the reporting of th...' (rules 2-3)
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
At which of its 2024 guidance updates, if any, did RadNet change any guidance range for its Digital Health segment? List them in date order.
```

### Number of asks

1 ask

### Gold answer

```text
May, November
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 7, the CFO's guidance remarks in the third-quarter 2024 call): the 2024 guidance levels were "released in conjunction with our 2023 year-end results in March of this year and revised in May and August", and this November call revises them again. The updates are therefore May, August and November 2024; March set the ranges and changed nothing.
Step 2. Source input (Doc 5, the CFO's guidance update in May 2024): for the Digital Health segment the company raised its Adjusted EBITDA range and its non-capitalized R&D range, each by one million dollars, "and all other guidance ranges remain the same for the digital health platform". So non-capitalized R&D is one of the segment's guidance ranges, and the May update changed two of them.
Step 3. Source input (Doc 6, the CFO's guidance update in August 2024): "For the digital health segment, our guidance ranges all remain the same". Decoy: August was a guidance update, but it changed no Digital Health range.
Step 4. Source input (Doc 7, the CFO's guidance update in November 2024): "For the digital health segment, our guidance remains substantially the same. We did increase our spend by $1 million on non-capitalized R&D". The non-capitalized R&D range named in Step 2 was raised again, so the November update changed a Digital Health range; "substantially the same" describes the rest.
Step 5. Final answer (Doc 5, Doc 6 and Doc 7): Digital Health ranges changed at the May and November updates but not at the August one; in date order, May, November.
```

### Answer components

Component 1

```text
May
```

Component 2

```text
November
```

### Evidence

Evidence 1: document Doc 7 (rdnt_call_transcript_2024-11-12.txt), proves component 1. May (local note: CFO, guidance history)

```text
released in conjunction with our 2023 year-end results in March of this year and revised in May and August
```

Evidence 2: document Doc 5 (rdnt_call_transcript_2024-05-13.txt), proves component 1. May (local note: CFO, May 2024 Digital Health guidance)

```text
EBITDA guidance by $1 million both at the low end and the high end of the range to $13 million to $15 million
```

Evidence 3: document Doc 5 (rdnt_call_transcript_2024-05-13.txt), proves component 1. May (local note: CFO, May 2024 Digital Health guidance)

```text
We increased our non-capitalized R&D expenditures by $1 million to $12 million to $14 million, and all other guidance ranges remain the same for the digital health platform.
```

Evidence 4: document Doc 6 (rdnt_call_transcript_2024-08-09.txt), proves component 1. May (local note: CFO, August 2024 guidance history)

```text
which we amended after reporting our first quarter 2024 financial results in May
```

Evidence 5: document Doc 7 (rdnt_call_transcript_2024-11-12.txt), proves component 2. November (local note: CFO, November 2024 Digital Health guidance)

```text
For the digital health segment, our guidance remains substantially the same. We did increase our spend by $1 million on non-capitalized R&D
```

### Necessary documents

- Tick Doc 5 (rdnt_call_transcript_2024-05-13.txt), role: Answer component
- Tick Doc 7 (rdnt_call_transcript_2024-11-12.txt), role: Answer component
- Tick Doc 6 (rdnt_call_transcript_2024-08-09.txt), role: Exclusion / condition source

  Reviewer note:

```text
rules out the August update, which Doc 7 shows took place ("revised in May and August") but which changed no Digital Health range
```

Leave unticked: Doc 1 (rdnt_call_transcript_2023-05-11.txt), Doc 2 (rdnt_call_transcript_2023-08-09.txt), Doc 3 (rdnt_call_transcript_2023-11-13.txt), Doc 4 (rdnt_call_transcript_2024-03-05.txt), Doc 8 (rdnt_call_transcript_2025-03-05.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Conditional filter

Leave unticked: Unit normalization, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Linking across documents: Doc 7's November update says Digital Health guidance "remains substantially the same", so careless solvers answer May alone. Its next sentence raises non-capitalized R&D, which Doc 5 lists among the segment's guidance ranges, so November also changed one.
```

(41 / 50 words.)
