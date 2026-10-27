# aq-02933 q05 hand-over

Generated 2026-10-12 by `python tools/check_questions.py tasks/aq-02933 --handover --q q05` from questions/q05.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 bbe7f74d7a88fcac490b8d166ee3fe2a14a9ccae0f0869a088021a27ca497269: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 3, D05 = Doc 6, D06 = Doc 5.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q05.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
CMS cites fraud cases in support of its three 2026 enrollment moratoria. In how many of those cases was a prison sentence handed down in 2024 or 2025?
```

### Number of asks

1 ask

### Gold answer

```text
13 cases
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 3, section II.B, the medical supply company cases): three cases have a prison sentence dated 2024: a California father and son (March 2024), a Texas man (February 2024) and a South Carolina man (March 2024). None is dated 2025. The other prison sentences in the list are dated 2023 or 2022, and the rest are a civil judgment and settlements. That makes 3.

Step 2. Source input (Doc 5, section II.A.2, the hospice cases): five cases have a prison sentence dated 2024 or 2025: a former Louisiana resident (June 2024), several California residents (2025), the owner of a Louisiana hospice (May 2024), the owner of two California hospice companies with his biller (March 2024) and a California physician (December 2024). Not counted: two California residents found guilty in December 2024 and a California man convicted in February 2024, for whom no sentence is stated, a prison sentence dated 2023, and the settlements. That makes 5.

Step 3. Source input (Doc 6, section II.B, the home health cases): five cases have a prison sentence dated in those two years: the owner of a Pennsylvania home care agency (June 2025), a part-owner of a Massachusetts provider (January 2025), the owner of home health care businesses in Ohio (April 2025), a Michigan HHA owner and operator (November of the earlier year) and a Texas man (August 2025). Not counted: a prison sentence from an earlier year, two convictions, a guilty plea and the settlements. That makes 5.

Step 4. Calculation (Doc 3 and Doc 5): medical supply and hospice cases: 3 + 5 = 8.

Step 5. Final answer (Doc 3, Doc 5 and Doc 6): adding the home health cases: 8 + 5 = 13.
```

### Answer components

Component 1

```text
13 cases
```

### Evidence

Evidence 1: document Doc 3 (fr_2026_03971.txt), proves component 1. 13 cases (local note: section II.B, offset 23,193)

```text
A California father and son in March 2024 were sentenced to prison
```

Evidence 2: document Doc 3 (fr_2026_03971.txt), proves component 1. 13 cases (local note: section II.B, offset 24,407)

```text
A Texas man was sentenced to prison in February 2024
```

Evidence 3: document Doc 3 (fr_2026_03971.txt), proves component 1. 13 cases (local note: section II.B, offset 28,739)

```text
A South Carolina man was sentenced to 9 years in prison in March 2024
```

Evidence 4: document Doc 5 (fr_2026_09718.txt), proves component 1. 13 cases (local note: section II.A.2, offset 18,071)

```text
A former Louisiana resident in June 2024 was sentenced to
```

Evidence 5: document Doc 5 (fr_2026_09718.txt), proves component 1. 13 cases (local note: section II.A.2, offset 19,780)

```text
Several California residents were sentenced to prison in 2025
```

Evidence 6: document Doc 5 (fr_2026_09718.txt), proves component 1. 13 cases (local note: section II.A.2, offset 25,642)

```text
was sentenced to 20 years in prison in May 2024
```

Evidence 7: document Doc 5 (fr_2026_09718.txt), proves component 1. 13 cases (local note: section II.A.2, offset 27,671)

```text
were sentenced to prison in March 2024
```

Evidence 8: document Doc 5 (fr_2026_09718.txt), proves component 1. 13 cases (local note: section II.A.2, offset 32,244)

```text
A California physician who worked for two hospices was sentenced to Federal prison in December 2024
```

Evidence 9: document Doc 6 (fr_2026_09717.txt), proves component 1. 13 cases (local note: section II.B, offset 20,017)

```text
The owner of a Pennsylvania home care agency was sentenced to prison in June 2025
```

Evidence 10: document Doc 6 (fr_2026_09717.txt), proves component 1. 13 cases (local note: section II.B, offset 22,434)

```text
A part-owner of a Massachusetts home health provider in January 2025 was sentenced in Federal court to 12 years in prison
```

Evidence 11: document Doc 6 (fr_2026_09717.txt), proves component 1. 13 cases (local note: section II.B, offset 24,543)

```text
A home health care owner was sentenced in April 2025 to 42 months in prison
```

Evidence 12: document Doc 6 (fr_2026_09717.txt), proves component 1. 13 cases (local note: section II.B, offset 27,261)

```text
In November 2024, a Michigan HHA owner and operator was sentenced to prison
```

Evidence 13: document Doc 6 (fr_2026_09717.txt), proves component 1. 13 cases (local note: section II.B, offset 28,845)

```text
A Texas man in August 2025 was sentenced to 75 months in Federal prison
```

### Necessary documents

- Tick Doc 3 (fr_2026_03971.txt), role: Answer component
- Tick Doc 6 (fr_2026_09717.txt), role: Answer component
- Tick Doc 5 (fr_2026_09718.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_08676.txt), Doc 2 (fr_2025_15492.txt), Doc 4 (fr_2026_04653.txt), Doc 7 (fr_2026_17622.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Look-alike measure: Doc 5 dates a guilty verdict to December 2024 and a conviction to February 2024 with no sentence; counting those outcomes as sentences gives 15. The gold counts only prison sentences dated 2024 or 2025: 3 in Doc 3, 5 in Doc 5, 5 in Doc 6.
```

(49 / 50 words.)
