# aq-04112 q02 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-04112 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 4e6e6e745b081c165f8086737a5f4d86e2a3e2eeb24d7285816e934136382bdb: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D01 = Doc 2, D03 = Doc 1.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 3: Doc 1 doesn't mention 25,600. Doc 1 prints it first at character 53,105, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Had the Migration Advisory Committee's advice on butchers been accepted, by how much would a skilled butcher's quoted starting salary have exceeded the Skilled Worker Visa salary threshold?
```

### Number of asks

1 ask

### Gold answer

```text
£6,020
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, Charlie Dewhirst of the National Pig Association, answering the Chair on what a skilled butcher is paid): the pay is a "£26,500 starting salary", rising with experience.
Step 2. Source input (Doc 1, section on the operation of the Shortage Occupation List): the Migration Advisory Committee proposed adding butchers, among other jobs, to the Shortage Occupation List, and the report says its recommendations had still not been accepted. Accepting the advice would therefore have put butchers on that list.
Step 3. Source input and calculation (Doc 1, key features of the immigration policy and the section on the list): entry on the list reduces the salary requirement for a Skilled Worker Visa by 20%, which leaves 80% of the general salary threshold. That threshold, the one the report sets against butchers' pay, is £25,600: 25,600 × 80% = 20,480 pounds.
Step 4. Calculation (Doc 1 and Doc 2): the starting salary less the threshold butchers would have faced on the list: 26,500 - 20,480 = 6,020 pounds.
Step 5. Wrong route, for comparison (Doc 1 and Doc 2): set against the threshold as printed, with butchers off the list, the margin is 26,500 - 25,600 = 900 pounds. That is the position the Government kept, not the one the Committee advised.
Step 6. Final answer (Doc 1 and Doc 2): the starting salary would have exceeded the threshold by £6,020.
```

### Answer components

Component 1

```text
£6,020
```

### Evidence

Evidence 1: document Doc 2 (ukc_1497_oral_2900.txt), proves component 1. £6,020 (local note: Q8, the Chair)

```text
These are people who are paid probably £500 to £600 a week, a skilled butcher, I suspect.
```

Evidence 2: document Doc 2 (ukc_1497_oral_2900.txt), proves component 1. £6,020 (local note: Q8, Charlie Dewhirst)

```text
Yes, £26,500 starting salary up to £35,000 to £40,000 once they are
```

Evidence 3: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. £6,020 (local note: para 54, the Committee's proposal)

```text
on to the SOL, including: veterinary nurses; meat hygiene inspectors; jobs in the fishing industry; and butchers.
```

Evidence 4: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. £6,020 (local note: para 56)

```text
The MAC’s recommendations still have not been accepted some 20 months later.
```

Evidence 5: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. £6,020 (local note: para 39, key features)

```text
The Shortage Occupation List (SOL)—a subset of the occupations that are eligible for a Skilled Worker Visa. Entry onto the SOL allows the applicable minimum salary requirement for a SWV to be reduced by 20%.
```

Evidence 6: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. £6,020 (local note: para 53)

```text
can make it easier to recruit to those roles by reducing the general salary threshold of £25,600
```

Evidence 7: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. £6,020 (local note: para 45, Cranswick)

```text
the skilled vacancies for butchers meet the earnings threshold of £25,600
```

Evidence 8: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. £6,020 (local note: para 58, the Minister)

```text
putting the role on the SOL would not help as the pay being offered by recruiting firms was above £25,600 in any case
```

### Necessary documents

- Tick Doc 1 (ukc_1497_report_9580.txt), role: Answer component
- Tick Doc 2 (ukc_1497_oral_2900.txt), role: Answer component

Leave unticked: Doc 3 (ukc_1497_oral_2977.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization

Leave unticked: Temporal alignment, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Look-alike measure: Doc 1 prints the general threshold, £25,600, as the figure butchers' pay clears, so a careless solver subtracts it from Doc 2's £26,500 and answers £900. The advice would have put butchers on the Shortage Occupation List, whose threshold is 20% lower, £20,480: £6,020.
```

(46 / 50 words.)
