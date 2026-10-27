# aq-02743 q03 hand-over

Generated 2026-10-11 by `python tools/check_questions.py tasks/aq-02743 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 d0212279a629d820b389216c91160ec4dc5087263675cd166696ebb952ed0bad: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 3, D04 = Doc 4.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN sibling: six words shared with q02: '000 or more people and 15'
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q03.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
An HHS-funded county has 50,000 or more people and 15 or more employees. How many more days did HHS's interim rule give it before any federal rule required it to meet WCAG 2.1?
```

### Number of asks

1 ask

### Gold answer

```text
350 days
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 3, SUMMARY and DATES): for State and local government entities with a total population of 50,000 or more, the Justice Department's compliance date for the WCAG 2.1 requirements is extended from April 24, 2026, to April 26, 2027, and that interim rule is effective April 20, 2026.

Step 2. Source input (Doc 4, SUMMARY and DATES): for recipients of HHS assistance with fifteen (15) or more employees, the date for meeting the web accessibility requirements, which adopt WCAG 2.1, is extended from May 11, 2026, to May 11, 2027, and that interim rule is effective May 7, 2026.

Step 3. Source input (Doc 3 and Doc 4, coverage): Doc 4 says the Justice Department's rule applies to State and local government entities whether or not they receive Federal financial assistance, and that some recipients of HHS assistance are also public entities under that rule. The county is one of them, so both rules bind it.

Step 4. Application (Doc 3 and Doc 4): April 20, 2026 is before May 7, 2026, so just before HHS's interim rule took effect the Justice Department's date was already April 26, 2027 while HHS's date was still May 11, 2026. The first date on which any federal rule required the county to meet WCAG 2.1 was then May 11, 2026.

Step 5. Application (Doc 3 and Doc 4): once HHS's interim rule took effect, HHS's date became May 11, 2027, which is later than April 26, 2027. The first date on which any federal rule requires it became April 26, 2027.

Step 6. Calculation (Doc 3 and Doc 4): 12 months of 30 days each, in days: 12 × 30 = 360.

Step 7. Calculation (Doc 3 and Doc 4): a common year is 5 days longer than that, and no leap day falls between May 11, 2026 and May 11, 2027, so that year has, in days: 360 + 5 = 365.

Step 8. Final answer (Doc 3 and Doc 4): April 26, 2027 falls 15 days before May 11, 2027, so the days from May 11, 2026 to April 26, 2027 are: 365 - 15 = 350.
```

### Answer components

Component 1

```text
350 days
```

### Evidence

Evidence 1: document Doc 3 (fr_2026_07663.txt), proves component 1. 350 days (local note: SUMMARY, L25)

```text
The compliance date for State and local government entities with a total population of 50,000 or more is extended from April 24, 2026, to April 26, 2027.
```

Evidence 2: document Doc 3 (fr_2026_07663.txt), proves component 1. 350 days (local note: DATES, L28)

```text
Effective date: This IFR is effective April 20, 2026.
```

Evidence 3: document Doc 4 (fr_2026_09266.txt), proves component 1. 350 days (local note: SUMMARY, L26)

```text
The compliance date for recipients with fifteen (15) or more employees is extended from May 11, 2026, to May 11, 2027.
```

Evidence 4: document Doc 4 (fr_2026_09266.txt), proves component 1. 350 days (local note: DATES, L30)

```text
Effective date: This IFR is effective May 7, 2026.
```

Evidence 5: document Doc 4 (fr_2026_09266.txt), proves component 1. 350 days (local note: coverage, L143)

```text
DOJ's rule applied to State and local government entities covered by title II of the ADA, regardless of whether those entities also receive Federal financial assistance.
```

Evidence 6: document Doc 4 (fr_2026_09266.txt), proves component 1. 350 days (local note: overlap, L143)

```text
There is significant overlap between covered entities under both rules since some recipients of financial assistance from HHS are also public entities governed by title II of the ADA.
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

Trap: Superseded date or version

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Superseded date or version: Doc 4's SUMMARY keeps the old HHS date, May 11, 2026, which bound the county first before HHS's rule. Comparing only the extended dates, where Doc 3's April 26, 2027 comes first, gives 0 days. The gold counts from May 11, 2026: 350.
```

(47 / 50 words.)
