# aq-02626 q05 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02626 --handover --q q05` from questions/q05.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 15e8c0cdba78f125b50663d7ec2eac6699f531aa2d5e80170f9fe45639f35729: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D03 = Doc 3, D04 = Doc 4, D05 = Doc 5, D06 = Doc 6.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN documents: 5 documents listed; the form's reasoning usually covers 2-4, only those the answer relies on
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q05.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Summed across EPA's five State coal-ash proposals, how many days after Federal Register publication did the comment deadlines fall?
```

### Number of asks

1 ask

### Gold answer

```text
307 days
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, header and DATES): the Wyoming proposal was published in the Federal Register on September 2, 2025, and "Comments must be received on or before November 3, 2025."
Step 2. Calculation (Doc 2): 60 days after September 2 is November 1, and November 3 is 2 days later, so the deadline fell this many days after publication: 60 + 2 = 62.
Step 3. Source input (Doc 3, header and DATES): the Virginia proposal was published on May 4, 2026, and "Comments must be received on or before July 6, 2026."
Step 4. Calculation (Doc 3): 60 days after May 4 is July 3, and July 6 is 3 days later: 60 + 3 = 63.
Step 5. Source input (Doc 4, header and DATES): the Louisiana proposal was published on June 5, 2026, and "Comments must be received on or before August 4, 2026."
Step 6. Derived (Doc 4): counting 60 days on from June 5 reaches August 4, the deadline itself, so this window is 60 days.
Step 7. Source input (Doc 5, header and DATES): the Alabama proposal was published on July 14, 2026, and "Comments must be received on or before September 14, 2026."
Step 8. Calculation (Doc 5): 60 days after July 14 is September 12, and September 14 is 2 days later: 60 + 2 = 62.
Step 9. Source input (Doc 6, header and DATES): the Wisconsin proposal was published on September 11, 2026, and "Comments must be received on or before November 10, 2026."
Step 10. Derived (Doc 6): counting 60 days on from September 11 reaches November 10, the deadline itself, so this window is 60 days.
Step 11. Final answer (Doc 2, Doc 3, Doc 4, Doc 5 and Doc 6): 62 + 63 + 60 + 62 + 60 = 307.
```

### Answer components

Component 1

```text
307
```

### Evidence

Evidence 1: document Doc 2 (fr_2025_16801.txt), proves component 1. 307 (local note: header, L3)

```text
Federal Register, Volume 90 Issue 167 (Tuesday, September 2, 2025)
```

Evidence 2: document Doc 2 (fr_2025_16801.txt), proves component 1. 307 (local note: DATES, L27)

```text
Comments must be received on or before November 3, 2025.
```

Evidence 3: document Doc 3 (fr_2026_08662.txt), proves component 1. 307 (local note: header, L3)

```text
Federal Register, Volume 91 Issue 85 (Monday, May 4, 2026)
```

Evidence 4: document Doc 3 (fr_2026_08662.txt), proves component 1. 307 (local note: DATES, L32)

```text
Comments must be received on or before July 6, 2026.
```

Evidence 5: document Doc 4 (fr_2026_11312.txt), proves component 1. 307 (local note: header, L3)

```text
Federal Register, Volume 91 Issue 108 (Friday, June 5, 2026)
```

Evidence 6: document Doc 4 (fr_2026_11312.txt), proves component 1. 307 (local note: DATES, L27)

```text
Comments must be received on or before August 4, 2026.
```

Evidence 7: document Doc 5 (fr_2026_14118.txt), proves component 1. 307 (local note: header, L3)

```text
Federal Register, Volume 91 Issue 133 (Tuesday, July 14, 2026)
```

Evidence 8: document Doc 5 (fr_2026_14118.txt), proves component 1. 307 (local note: DATES, L27)

```text
Comments must be received on or before September 14, 2026.
```

Evidence 9: document Doc 6 (fr_2026_18552.txt), proves component 1. 307 (local note: header, L3)

```text
Federal Register, Volume 91 Issue 175 (Friday, September 11, 2026)
```

Evidence 10: document Doc 6 (fr_2026_18552.txt), proves component 1. 307 (local note: DATES, L27)

```text
Comments must be received on or before November 10, 2026.
```

### Necessary documents

- Tick Doc 2 (fr_2025_16801.txt), role: Answer component
- Tick Doc 3 (fr_2026_08662.txt), role: Answer component
- Tick Doc 4 (fr_2026_11312.txt), role: Answer component
- Tick Doc 5 (fr_2026_14118.txt), role: Answer component
- Tick Doc 6 (fr_2026_18552.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_11907.txt)

### Reasoning tags

Tick: Cross-document join, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Look-alike measure: every proposal's SUMMARY calls its comment window a "60-day public comment period"; taking that label five times gives 300 days. The printed publication dates and deadlines give 62, 63, 60, 62 and 60 days (Docs 2 to 6), 307 in all.
```

(43 / 50 words.)
