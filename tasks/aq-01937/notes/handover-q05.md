# aq-01937 q05 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-01937 --handover --q q05` from questions/q05.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 2, difficulty_target medium, origin claude.
- tested_sha256 f70bb5c4d40db316dece5baf84674261d106ecd62c4696bc952654f88f48c179: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D07 = Doc 7, D08 = Doc 8, D10 = Doc 10.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN period: names a quarter or fiscal year without 'fiscal'/'calendar'/'ended'; confirm the period is pinned (rule 9b)
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q05.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
By what percentage did State Street's quarter-end servicing fee revenue backlog change from the latest figure it had published before it launched its Digital Asset Platform to its figure for June 30, 2026? Give the sign and round to one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
-16.5%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 8, 4Q25 highlights, note (b)): State Street's Digital Asset Platform was launched on January 15, 2026.

Step 2. Source input (Doc 8, dateline): Doc 8, the release that reports the launch, is dated January 16, 2026, the day after the launch, so the quarter-end figures it reports had not been published before the platform launched.

Step 3. Source input (Doc 7, dateline and 3Q25 highlights): the 3Q25 release, dated October 17, 2025, reported quarter-end servicing fee revenue of $401 million to be installed in future periods.

Step 4. Doc 7 and Doc 8: October 17, 2025 is before the January 15, 2026 launch, and no release in the bundle falls between Doc 7 and Doc 8, so $401 million was the latest such figure published before the platform launched.

Step 5. Source input (Doc 10, 2Q26 highlights): quarter-end servicing fee revenue to be installed in future periods was $335 million at the end of 2Q26 (June 30, 2026).

Step 6. Source input (Doc 10, In this news release): the releases call servicing fee revenue to be installed the "backlog".

Step 7. Calculation (Doc 7 and Doc 10): 335 - 401 = -66 ($ millions).

Step 8. Calculation (Doc 7, change as a share of the earlier figure): -66 / 401 = -16.5% (one decimal place).
```

### Answer components

Component 1

```text
-16.5%
```

### Evidence

Evidence 1: document Doc 8 (stt_ex991_2026-01-16.txt), proves component 1. -16.5% (local note: 4Q25 highlights, note (b), L99)

```text
State Street’s Digital Asset Platform was launched on January 15, 2026
```

Evidence 2: document Doc 8 (stt_ex991_2026-01-16.txt), proves component 1. -16.5% (local note: dateline, L13)

```text
January 16, 2026
```

Evidence 3: document Doc 7 (stt_ex991_2025-10-17.txt), proves component 1. -16.5% (local note: dateline, L13)

```text
October 17, 2025
```

Evidence 4: document Doc 7 (stt_ex991_2025-10-17.txt), proves component 1. -16.5% (local note: 3Q25 highlights, future installations, L77)

```text
Quarter-end servicing fee revenue of $401 million to be installed in future periods
```

Evidence 5: document Doc 10 (stt_ex991_2026-07-16.txt), proves component 1. -16.5% (local note: 2Q26 highlights, future installations, L73)

```text
Quarter-end servicing fee revenue of $335 million to be installed in future periods
```

Evidence 6: document Doc 10 (stt_ex991_2026-07-16.txt), proves component 1. -16.5% (local note: In this news release, wins and backlog, L367)

```text
Servicing fee revenue wins (i.e., "sales") and backlog (i.e., "to be installed")
```

### Necessary documents

- Tick Doc 7 (stt_ex991_2025-10-17.txt), role: Answer component
- Tick Doc 8 (stt_ex991_2026-01-16.txt), role: Used to identify
- Tick Doc 10 (stt_ex991_2026-07-16.txt), role: Answer component

Leave unticked: Doc 1 (stt_ex991_2024-02-27.txt), Doc 2 (stt_ex991_2024-10-15.txt), Doc 3 (stt_ex991_2025-01-17.txt), Doc 4 (stt_ex991_2025-03-05.txt), Doc 5 (stt_ex991_2025-04-17.txt), Doc 6 (stt_ex991_2025-07-15.txt), Doc 9 (stt_ex991_2026-04-17.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Doc 8 lists the Digital Asset Platform launch among its 4Q25 highlights, beside a $320 million backlog, but dates the launch January 15, 2026, a day before its own release. The latest published figure was 3Q25's $401 million (Doc 7): Doc 10's 335 against 401 is -16.5%, not +4.7%.
```

(49 / 50 words.)
