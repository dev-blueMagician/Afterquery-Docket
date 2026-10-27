# aq-02750 q03 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02750 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 d85c297f4b341f27b3fb7db8051074cf6fe658bf0b46c46d4597f47cb8620183: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D04 = Doc 4, D05 = Doc 5, D06 = Doc 6, D07 = Doc 7.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q03.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Commenters on a CDC Ebola entry-suspension order asked it to let lawful permanent residents return. How many days before that order's comment deadline did comments close on the rule ending their exemption?
```

### Number of asks

1 ask

### Gold answer

```text
14 days
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 6, SUPPLEMENTARY INFORMATION and responses to comments on previous orders): the order signed on June 21, 2026 came with a 15-day comment period, and the comments received in it are answered in Doc 6. In them, commenters asked CDC to reconsider allowing lawful permanent residents to return, as the original May 18, 2026 order had allowed. So the order they commented on is the June 21, 2026 order, not the July 13, 2026 order that Doc 6 prints.

Step 2. Source input (Doc 6, response to that comment): CDC answered that the removal of the exemption for lawful permanent residents resulted from amendments to 42 CFR 71.40(f). The rule ending the exemption is the interim final rule that amended that paragraph.

Step 3. Source input (Doc 4, DATES and amendatory text): Doc 4 is that interim final rule. It revises paragraph (f) of 71.40, and comments on it had to be received by June 26, 2026.

Step 4. Source input (Doc 5, DATES): Doc 5 prints the order that took effect on June 21, 2026. Written comments on it had to be received on or before July 10, 2026, which is that order's comment deadline.

Step 5. Calculation (Doc 4 and Doc 5): June has 30 days, so the days left in June after June 26 are 30 - 26 = 4.

Step 6. Calculation (Doc 4 and Doc 5): adding the days of July up to July 10 gives the days between the two deadlines: 4 + 10 = 14.
```

### Answer components

Component 1

```text
14 days
```

### Evidence

Evidence 1: document Doc 6 (fr_2026_14365.txt), proves component 1. 14 days (local note: SUPPLEMENTARY INFORMATION, L43)

```text
On June 21, 2026, the ASH signed a new 30-day Order continuing the previous Order, without change, and provided a 15-day comment period. During this time CDC received five comments, which are addressed below.
```

Evidence 2: document Doc 6 (fr_2026_14365.txt), proves component 1. 14 days (local note: Response To Comments on Previous Orders, L51)

```text
Three of the commenters requested that CDC reconsider allowing lawful permanent residents (LPRs) to return under the same screening and monitoring protocols that apply to U.S. citizens as was allowed in the original May 18, 2026, Order.
```

Evidence 3: document Doc 6 (fr_2026_14365.txt), proves component 1. 14 days (local note: Response To Comments on Previous Orders, L52)

```text
The removal of the exemption for LPRs resulted from amendments to 42 CFR 71.40(f) and is outside the scope of this Order.
```

Evidence 4: document Doc 4 (fr_2026_10543.txt), proves component 1. 14 days (local note: DATES, L30)

```text
Comment date: Comments must be received by June 26, 2026.
```

Evidence 5: document Doc 4 (fr_2026_10543.txt), proves component 1. 14 days (local note: section III, L125)

```text
The interim final rule will apply to lawful permanent residents.
```

Evidence 6: document Doc 5 (fr_2026_12790.txt), proves component 1. 14 days (local note: DATES, L27)

```text
This action took effect June 21, 2026, at 5:00 p.m. EDT. Written comments must be received on or before July 10, 2026.
```

Evidence 7: document Doc 7 (fr_2026_16706.txt), proves component 1. 14 days (local note: SUPPLEMENTARY INFORMATION, L41)

```text
The ASH continued the Order without change on June 21, 2026, for 30 days with a 15-day comment period; CDC received five comments in response.
```

### Necessary documents

- Tick Doc 4 (fr_2026_10543.txt), role: Answer component
- Tick Doc 5 (fr_2026_12790.txt), role: Answer component
- Tick Doc 6 (fr_2026_14365.txt), role: Used to identify; also tick Doc 7 (fr_2026_16706.txt) and choose it in Doc 6's "or..." box

Leave unticked: Doc 1 (fr_2024_10390.txt), Doc 2 (fr_2024_30500.txt), Doc 3 (fr_2025_23970.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Wrong year or edition: Doc 6 answers the permanent-resident comments under its own comment deadline, July 31, 2026, but they were made on the June 21 order. Using July 31 gives 35 days. That order's deadline is Doc 5's July 10, 14 days after Doc 4's June 26.
```

(48 / 50 words.)
