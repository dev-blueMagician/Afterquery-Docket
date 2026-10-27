# aq-02626 q01 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02626 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 3532a741860c275f2bd335b264f35a909d63776969a67a6bc3f1e9b27aac2fc5: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D03 = Doc 3.
- Floor: 0 FAIL, 5 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 3: Doc 2 doesn't mention 7. Doc 2 prints it first at character 21,166, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: Doc 3 doesn't mention 45. Doc 3 prints it first at character 34,425, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: Doc 3 doesn't mention 15. Doc 3 prints it first at character 20,660, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 5: Doc 3 doesn't mention 15. Doc 3 prints it first at character 20,660, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
For a new coal-ash permit, how many more public-comment days in all does Wyoming guarantee with notices a week apart than Virginia with its hearing 40 days after notice?
```

### Number of asks

1 ask

### Gold answer

```text
19 days
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, Public Comment Period): an applicant for a new solid waste permit, which includes a coal combustion residuals (coal ash) unit permit, must "complete two public comment periods during the permitting process", the first on the complete application and the second on the proposed permit.
Step 2. Source input (Doc 2, Public Comment Period): the applicant publishes each notice "once a week for two consecutive weeks", and "Each public comment period begins on the first day of the notice publication and continues until 30 days after the second publication."
Step 3. Calculation (Doc 2): with the second notice one week after the first, days from the first notice to the close of one Wyoming comment period: 7 + 30 = 37.
Step 4. Source input (Doc 3, Public Notice and Participation in the CCR Permit Application Process): for a new permit Virginia requires "that the public comment period last at least 45 days, with the public hearing scheduled at least 30 days following the public notice and the public comment period extending at least 15 days after the public hearing."
Step 5. Calculation (Doc 3): with the hearing 40 days after the notice, the earliest close of Virginia's comment period, in days after the notice: 40 + 15 = 55. That is later than the minimum length quoted in Step 4, so the hearing rule sets Virginia's minimum.
Step 6. Calculation (Doc 2 and Doc 3): Wyoming's total over its two comment periods, in days: 37 + 37 = 74.
Step 7. Final answer (Doc 2 and Doc 3): additional days of public comment guaranteed in Wyoming: 74 - 55 = 19.
```

### Answer components

Component 1

```text
19
```

### Evidence

Evidence 1: document Doc 2 (fr_2025_16801.txt), proves component 1. 19 (local note: Public Comment Period, L220)

```text
All applicants for solid waste permits that submit a new, renewal, closure or major amendment permit application are required to complete two public comment periods during the permitting process.
```

Evidence 2: document Doc 2 (fr_2025_16801.txt), proves component 1. 19 (local note: Public Comment Period, L221)

```text
The applicant is required to publish each written notice once a week for two consecutive weeks in a newspaper of general circulation
```

Evidence 3: document Doc 2 (fr_2025_16801.txt), proves component 1. 19 (local note: Public Comment Period, L221)

```text
Each public comment period begins on the first day of the notice publication and continues until 30 days after the second publication.
```

Evidence 4: document Doc 3 (fr_2026_08662.txt), proves component 1. 19 (local note: Public Notice and Participation in the CCR Permit Application Process, L195)

```text
Applications for new CCR permits are treated as a new solid waste permit, in accordance with 9VAC20-81-450 E.
```

Evidence 5: document Doc 3 (fr_2026_08662.txt), proves component 1. 19 (local note: Public Notice and Participation in the CCR Permit Application Process, L195)

```text
The regulation requires that the public comment period last at least 45 days, with the public hearing scheduled at least 30 days following the public notice and the public comment period extending at least 15 days after the public hearing.
```

### Necessary documents

- Tick Doc 2 (fr_2025_16801.txt), role: Answer component
- Tick Doc 3 (fr_2026_08662.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_11907.txt), Doc 4 (fr_2026_11312.txt), Doc 5 (fr_2026_14118.txt), Doc 6 (fr_2026_18552.txt)

### Reasoning tags

Tick: Cross-document join, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Look-alike measure: Doc 2 (Public Notice) labels each Wyoming comment period "30-day"; taking that figure gives 60 days and 5 more than Virginia's 55. Doc 2's Public Comment Period rule runs each period to 30 days after the second weekly notice, 37 days, so the gold is 19.
```

(48 / 50 words.)
