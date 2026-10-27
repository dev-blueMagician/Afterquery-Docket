# aq-02933 q01 hand-over

Generated 2026-10-11 by `python tools/check_questions.py tasks/aq-02933 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 7d25716d205f021d8287caf018e87ac0b68a0f96dc1c4e283f6c8ebc9d99b247: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D05 = Doc 6, D06 = Doc 5.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Where CMS reports both enrolled-hospice counts and home health agencies sharing one address, by what percentage did those States' combined hospice count grow from 2019 to 2023? One decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
57.7%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 5, Table 1, "Number of Enrolled Hospices in CY 2019 and CY 2023"): CMS gives enrolled-hospice counts for both years for Arizona, California, Nevada and Texas only. Nevada had 55 in CY 2019 and 138 in CY 2023. Texas had 718 and 1,081.

Step 2. Source input (Doc 6, section II.B): CMS found numerous HHAs operating out of a single, common practice location in Ohio, and adds that similar situations have been seen in Texas, Michigan, North Carolina and Nevada.

Step 3. Matching (Doc 5 and Doc 6): of the States in Step 1, only Nevada and Texas are among those in Step 2. Doc 6 names neither Arizona nor California there: it discusses Los Angeles County for the rise in its HHA numbers, not for shared addresses, and Doc 5's remark about a single building in Los Angeles County concerns hospices. Ohio, Michigan and North Carolina have no hospice counts for these years.

Step 4. Calculation (Doc 5 and Doc 6): combined CY 2019 count for Nevada and Texas: 55 + 718 = 773.

Step 5. Calculation (Doc 5 and Doc 6): combined CY 2023 count: 138 + 1,081 = 1,219.

Step 6. Calculation (Doc 5 and Doc 6): hospices added between the two years: 1,219 - 773 = 446.

Step 7. Final answer (Doc 5 and Doc 6): growth as a share of the CY 2019 count, to one decimal place: 446 / 773 = 57.7%.
```

### Answer components

Component 1

```text
57.7%
```

### Evidence

Evidence 1: document Doc 5 (fr_2026_09718.txt), proves component 1. 57.7% (local note: Table 1 title, offset 15,561)

```text
Table 1--Number of Enrolled Hospices in CY 2019 and CY 2023
```

Evidence 2: document Doc 5 (fr_2026_09718.txt), proves component 1. 57.7% (local note: Table 1, Nevada row, offset 16,047)

```text
Nevada.......................................................... 55 138 151
```

Evidence 3: document Doc 5 (fr_2026_09718.txt), proves component 1. 57.7% (local note: Table 1, Texas row, offset 16,123)

```text
Texas........................................................... 718 1,081 51
```

Evidence 4: document Doc 6 (fr_2026_09717.txt), proves component 1. 57.7% (local note: section II.B, offset 18,479)

```text
CMS has recently detected several situations in Ohio where numerous HHAs are operating out of a single, common practice location
```

Evidence 5: document Doc 6 (fr_2026_09717.txt), proves component 1. 57.7% (local note: section II.B, offset 18,838)

```text
Similar situations have been seen in Texas, Michigan, North Carolina, and Nevada.
```

### Necessary documents

- Tick Doc 6 (fr_2026_09717.txt), role: Used to identify
- Tick Doc 5 (fr_2026_09718.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_08676.txt), Doc 2 (fr_2025_15492.txt), Doc 3 (fr_2026_03971.txt), Doc 4 (fr_2026_04653.txt), Doc 7 (fr_2026_17622.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Picks the wrong entity or section

#### Failure mode 2

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Linking: Doc 6 names Nevada only in its 'Similar situations' sentence; its later co-located-HHAs passage names Michigan and Texas, so Texas alone gives 50.6%. Look-alike measure: Doc 5's Table 1 prints per-State increases of 151 and 51; averaging gives 101.0%. Combined counts give 57.7%.
```

(44 / 50 words.)
