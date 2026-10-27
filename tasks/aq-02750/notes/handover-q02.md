# aq-02750 q02 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02750 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 7a3b70a9ec1c100cd326b32581e715ab128e5566ecafa0c54c5ebb186deac2a3: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D06 = Doc 6, D07 = Doc 7.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
When Uganda declared its Ebola outbreak over, how many days remained to comment on CDC's entry-suspension order?
```

### Number of asks

1 ask

### Gold answer

```text
3 days
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 7, factual basis, section III.B): the Republic of Uganda Ministry of Health declared the outbreak over on July 28, 2026.

Step 2. Source input (Doc 7, DATES and SUPPLEMENTARY INFORMATION): the order printed in Doc 7 took effect on August 12, 2026, after the declaration. The order in force on July 28, and the only one then open for comment, was the one continued on July 13, 2026 for 30 days. Doc 7 says only that it had a 15-day comment period and prints no closing date for it.

Step 3. Source input (Doc 6, SUMMARY and DATES): Doc 6 prints that order. It was issued and took effect on July 13, 2026, and written comments on it had to be received on or before July 31, 2026, so July 31 was its comment deadline.

Step 4. Calculation (Doc 6 and Doc 7): both dates fall in July, so the days that remained for comment after the declaration are 31 - 28 = 3.
```

### Answer components

Component 1

```text
3 days
```

### Evidence

Evidence 1: document Doc 7 (fr_2026_16706.txt), proves component 1. 3 days (local note: section III.B, L125)

```text
On July 28, 2026, the Republic of Uganda Ministry of Health declared the outbreak over.
```

Evidence 2: document Doc 7 (fr_2026_16706.txt), proves component 1. 3 days (local note: DATES, L27)

```text
This action took effect August 12, 2026, at 5:00 p.m. EDT.
```

Evidence 3: document Doc 7 (fr_2026_16706.txt), proves component 1. 3 days (local note: SUPPLEMENTARY INFORMATION, L41)

```text
The ASH again continued the Order without change on July 13, 2026, for 30 days with a 15-day comment period, and no comments were received.
```

Evidence 4: document Doc 6 (fr_2026_14365.txt), proves component 1. 3 days (local note: DATES, L27)

```text
This action took effect July 13, 2026, at 5:00 p.m. EDT. Written comments must be received on or before July 31, 2026.
```

### Necessary documents

- Tick Doc 6 (fr_2026_14365.txt), role: Answer component
- Tick Doc 7 (fr_2026_16706.txt), role: Answer component

Leave unticked: Doc 1 (fr_2024_10390.txt), Doc 2 (fr_2024_30500.txt), Doc 3 (fr_2025_23970.txt), Doc 4 (fr_2026_10543.txt), Doc 5 (fr_2026_12790.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Wrong year or edition: Doc 7 reports Uganda's July 28 declaration beside its own comment deadline, September 1, 2026, but that order took effect August 12. Using it gives 35 days. The order in force on July 28 is Doc 6's, with comments due July 31, so 3 days.
```

(49 / 50 words.)
