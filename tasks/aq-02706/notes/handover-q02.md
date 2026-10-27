# aq-02706 q02 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02706 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 f6fbc2102c7db07e0cf47777435215640a9a146af4f4cd711e03ac85a6d0bbd8: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 1, D02 = Doc 2.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 2: Doc 1 doesn't mention 661. Doc 1 prints it first at character 44,862, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 2 doesn't mention 78. expected false alarm: Doc 2 prints it at character 83,894, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
The SBA's Office of Advocacy said the OCC's 2024 merger proposal could affect every small entity the OCC supervised. On the count the OCC had published by then, how many more entities is that than the final rule's estimate of small institutions affected in a year?
```

### Number of asks

1 ask

### Gold answer

```text
583 entities
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, Regulatory Flexibility Act section): the SBA's Office of Advocacy noted that all of the OCC's small entities may have been affected by the proposed rule. The final rule restates that point with its own later count of small entities, which a footnote dates to data accessed in August 2024, so that count had not been published when the comment was made.

Step 2. Source input (Doc 1, DATES line and Regulatory Flexibility Act section): comments on the proposal were due by April 15, 2024. The count the OCC had published by then is the proposal's own: 661 small entities.

Step 3. Source input (Doc 2, Regulatory Flexibility Act section): the OCC's estimate for the final rule is 78 small institutions affected in a given year.

Step 4. Calculation (Doc 1 and Doc 2): the small entities in the count published by then less the final rule's yearly estimate: 661 - 78 = 583 entities.
```

### Answer components

Component 1

```text
583 entities
```

### Evidence

Evidence 1: document Doc 2 (fr_2024_21560.txt), proves component 1. 583 entities (local note: Regulatory Flexibility Act section, L369)

```text
As the SBA's Office of Advocacy noted, all of the 636 small entities may have been impacted by the proposed rule to the extent that they elected to submit applications to the OCC for approval of business combination activities.
```

Evidence 2: document Doc 2 (fr_2024_21560.txt), proves component 1. 583 entities (local note: footnote 49, L372)

```text
Based on data accessed using FINDRS on August 18, 2024.
```

Evidence 3: document Doc 2 (fr_2024_21560.txt), proves component 1. 583 entities (local note: Regulatory Flexibility Act section, L369)

```text
the agency expects the annual impact of the final rulemaking could be 78 OCC-supervised small institutions in a given year, assuming that all merger applications are submitted by small banks
```

Evidence 4: document Doc 1 (fr_2024_02663.txt), proves component 1. 583 entities (local note: DATES, L40)

```text
Comments must be received by April 15, 2024.
```

Evidence 5: document Doc 1 (fr_2024_02663.txt), proves component 1. 583 entities (local note: Regulatory Flexibility Act section, L252)

```text
The OCC currently supervises 1,057 institutions (commercial banks, trust companies, federal savings associations, and branches or agencies of foreign banks) of which approximately 661 are small entities.
```

### Necessary documents

- Tick Doc 1 (fr_2024_02663.txt), role: Answer component
- Tick Doc 2 (fr_2024_21560.txt), role: Answer component

Leave unticked: Doc 3 (fr_2024_22189.txt), Doc 4 (fr_2025_13568.txt), Doc 5 (fr_2025_13589.txt), Doc 6 (fr_2026_03818.txt), Doc 7 (fr_2026_04275.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Wrong year or edition: Doc 2 restates the Office of Advocacy's point with its own count, 636, from data accessed August 18, 2024, after comments closed on April 15, 2024 (Doc 1). Using it gives 558. The count when the comment was made is Doc 1's 661, so 583.
```

(49 / 50 words.)
