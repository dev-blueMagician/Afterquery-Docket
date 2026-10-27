# aq-02743 q02 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02743 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 73c6cbf66ae9e7dae4720acb365c6f1eb85b4ca6e4683df281e7d27b303b5aca: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 3, D04 = Doc 4.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN sibling: six words shared with q03: '000 or more people and 15'
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
An HHS-funded county has 50,000 or more people and 15 or more employees. How many days after HHS's interim rule took effect does any federal rule first require it to meet WCAG 2.1?
```

### Number of asks

1 ask

### Gold answer

```text
354 days
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 4, DATES): HHS's interim rule is effective May 7, 2026.

Step 2. Source input (Doc 4, SUMMARY): for recipients of HHS assistance with fifteen (15) or more employees, the date for meeting the web accessibility requirements, which adopt WCAG 2.1, is extended from May 11, 2026, to May 11, 2027.

Step 3. Source input (Doc 3, SUMMARY): for State and local government entities with a total population of 50,000 or more, the Justice Department's compliance date for the same WCAG 2.1 requirements is extended from April 24, 2026, to April 26, 2027.

Step 4. Source input (Doc 3 and Doc 4, coverage): Doc 4 says the Justice Department's rule applies to State and local government entities whether or not they receive Federal financial assistance, and that some recipients of HHS assistance are also public entities under that rule. The county is one of them, so two federal rules require it to meet WCAG 2.1, and April 26, 2027 comes before May 11, 2027: the first date on which any federal rule requires it is the Justice Department's.

Step 5. Calculation (Doc 3 and Doc 4): 12 months of 30 days each, in days: 12 × 30 = 360.

Step 6. Calculation (Doc 3 and Doc 4): a common year is 5 days longer than that, and no leap day falls between May 7, 2026 and May 7, 2027, so that year has, in days: 360 + 5 = 365.

Step 7. Final answer (Doc 3 and Doc 4): April 26, 2027 falls 11 days before May 7, 2027, so the days from May 7, 2026 to April 26, 2027 are: 365 - 11 = 354.
```

### Answer components

Component 1

```text
354 days
```

### Evidence

Evidence 1: document Doc 4 (fr_2026_09266.txt), proves component 1. 354 days (local note: DATES, L30)

```text
Effective date: This IFR is effective May 7, 2026.
```

Evidence 2: document Doc 4 (fr_2026_09266.txt), proves component 1. 354 days (local note: SUMMARY, L26)

```text
The compliance date for recipients with fifteen (15) or more employees is extended from May 11, 2026, to May 11, 2027.
```

Evidence 3: document Doc 4 (fr_2026_09266.txt), proves component 1. 354 days (local note: coverage, L143)

```text
DOJ's rule applied to State and local government entities covered by title II of the ADA, regardless of whether those entities also receive Federal financial assistance.
```

Evidence 4: document Doc 4 (fr_2026_09266.txt), proves component 1. 354 days (local note: overlap, L143)

```text
There is significant overlap between covered entities under both rules since some recipients of financial assistance from HHS are also public entities governed by title II of the ADA.
```

Evidence 5: document Doc 3 (fr_2026_07663.txt), proves component 1. 354 days (local note: SUMMARY, L25)

```text
The compliance date for State and local government entities with a total population of 50,000 or more is extended from April 24, 2026, to April 26, 2027.
```

### Necessary documents

- Tick Doc 3 (fr_2026_07663.txt), role: Answer component
- Tick Doc 4 (fr_2026_09266.txt), role: Answer component

Leave unticked: Doc 1 (fr_2023_28871.txt), Doc 2 (fr_2024_26835.txt), Doc 5 (fr_2026_11505.txt), Doc 6 (fr_2026_16503.txt), Doc 7 (fr_2026_17636.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Conditional filter

Leave unticked: Unit normalization, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Picks the wrong entity or section

#### Failure mode 2

Trap: Document convention

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Linking across documents: Doc 4's SUMMARY sets May 11, 2027 for such recipients, but the county is also a Doc 3 public entity due April 26, 2027; HHS's date gives 369 days. Document convention: Doc 4 is dated May 11, 2026 but effective May 7; its date gives 350.
```

(49 / 50 words.)
