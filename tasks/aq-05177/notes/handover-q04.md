# aq-05177 q04 hand-over

Generated 2026-10-15 by `python tools/check_questions.py tasks/aq-05177 --handover --q q04` from questions/q04.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target hard, origin claude.
- tested_sha256 aecc807b38a5d3aebfe7d55bcb7c3d87861233133ad8174f1eb6d59e368a988d: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D05 = Doc 5, D06 = Doc 6, D07 = Doc 7.
- Floor: 0 FAIL, 2 WARN.
  - WARN strong-screen: the strong solver was right in every fresh solve of this exact sentence: likely Too easy at High. Say so with the hand-over; the user decides whether to run it. Never reword or re-screen the sentence to find a miss
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q04.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Besides revenue, how many of RadNet's 2024 guidance ranges did the company increase at every one of its updates that year?
```

### Number of asks

1 ask

### Gold answer

```text
3 guidance ranges
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 7, the CFO's guidance remarks in the third-quarter 2024 call): the 2024 guidance levels were "released in conjunction with our 2023 year-end results in March of this year and revised in May and August", and this November call revises them again, so 2024 had three updates: May, August and November.
Step 2. Source input (Doc 5, the CFO's guidance update in May 2024): the company raised its imaging center Adjusted EBITDA range, its capital expenditures range and its free cash flow range; it decreased cash paid for interest; for Digital Health it raised Adjusted EBITDA and non-capitalized R&D and left the other ranges unchanged.
Step 3. Source input (Doc 6, the CFO's guidance update in August 2024): the company raised the imaging center Adjusted EBITDA, capital expenditures and free cash flow ranges and lowered cash interest expense; "For the digital health segment, our guidance ranges all remain the same".
Step 4. Source input (Doc 7, the CFO's guidance update in November 2024): the company raised the imaging center Adjusted EBITDA, capital expenditures and free cash flow ranges and decreased cash interest expense; Digital Health guidance stayed "substantially the same" apart from a higher non-capitalized R&D range.
Step 5. Classification (Doc 5, Doc 6 and Doc 7): leaving out revenue, the ranges increased at all three updates are imaging center Adjusted EBITDA, capital expenditures and free cash flow. Cash interest fell each time; Digital Health Adjusted EBITDA rose only in May; non-capitalized R&D rose in May and November but not in August. Decoy: in each call the CEO's summary names only revenue, Adjusted EBITDA and free cash flow as increased, but the CFO's detail raises capital expenditures at every update too.
Step 6. Final answer (Doc 5, Doc 6 and Doc 7): 3 guidance ranges.
```

### Answer components

Component 1

```text
3
```

### Evidence

Evidence 1: document Doc 5 (rdnt_call_transcript_2024-05-13.txt), proves component 1. 3 (local note: CFO, May 2024 guidance update)

```text
Also for the imaging center segment, we’ve increased our EBITDA guidance by $5 million at the low end and the high end of our range.
```

Evidence 2: document Doc 5 (rdnt_call_transcript_2024-05-13.txt), proves component 1. 3 (local note: CFO, May 2024 guidance update)

```text
For capital expenditures for the imaging center segment, we increased our guidance both at the low end and the high end of the range by $5 million.
```

Evidence 3: document Doc 5 (rdnt_call_transcript_2024-05-13.txt), proves component 1. 3 (local note: CFO, May 2024 guidance update)

```text
we increased our free cash flow generation guidance level by $3 million to $68 million to $78 million
```

Evidence 4: document Doc 6 (rdnt_call_transcript_2024-08-09.txt), proves component 1. 3 (local note: CFO, August 2024 guidance update)

```text
We increased our EBITDA guidance range by $2 million at the low and the high ends
```

Evidence 5: document Doc 6 (rdnt_call_transcript_2024-08-09.txt), proves component 1. 3 (local note: CFO, August 2024 guidance update)

```text
We also increased our capital expenditures in the imaging center segment by $5 million to $135 million to $145 million.
```

Evidence 6: document Doc 6 (rdnt_call_transcript_2024-08-09.txt), proves component 1. 3 (local note: CFO, August 2024 guidance update)

```text
We increased our free cash flow guidance range by $4 million
```

Evidence 7: document Doc 6 (rdnt_call_transcript_2024-08-09.txt), proves component 1. 3 (local note: CFO, August 2024 Digital Health guidance)

```text
For the digital health segment, our guidance ranges all remain the same
```

Evidence 8: document Doc 7 (rdnt_call_transcript_2024-11-12.txt), proves component 1. 3 (local note: CFO, November 2024 guidance update)

```text
We’ve also increased for the imaging center segment our EBITDA guidance by $5 million
```

Evidence 9: document Doc 7 (rdnt_call_transcript_2024-11-12.txt), proves component 1. 3 (local note: CFO, November 2024 guidance update)

```text
For capital expenditures, we have increased our guidance level to $145 million to $155 million
```

Evidence 10: document Doc 7 (rdnt_call_transcript_2024-11-12.txt), proves component 1. 3 (local note: CFO, November 2024 guidance update)

```text
Our free cash flow guidance range, we’ve increased our level to $83 million to $93 million
```

### Necessary documents

- Tick Doc 5 (rdnt_call_transcript_2024-05-13.txt), role: Answer component
- Tick Doc 6 (rdnt_call_transcript_2024-08-09.txt), role: Answer component
- Tick Doc 7 (rdnt_call_transcript_2024-11-12.txt), role: Answer component

Leave unticked: Doc 1 (rdnt_call_transcript_2023-05-11.txt), Doc 2 (rdnt_call_transcript_2023-08-09.txt), Doc 3 (rdnt_call_transcript_2023-11-13.txt), Doc 4 (rdnt_call_transcript_2024-03-05.txt), Doc 8 (rdnt_call_transcript_2025-03-05.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Part vs total: in Docs 5, 6 and 7 the CEO's headline names only revenue, Adjusted EBITDA and free cash flow as increased, a part of the full list, so careless solvers count 2 besides revenue. The CFO's detail raises capital expenditures at every update too, giving 3.
```

(48 / 50 words.)
