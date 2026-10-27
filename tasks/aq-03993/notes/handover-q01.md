# aq-03993 q01 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-03993 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status draft, revision 1, difficulty_target medium, origin claude.
- tested_sha256 6ae7c9c570456e148158fb6482345c81913a7258239ad13ada374b8f615050de: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D03 = Doc 4, D04 = Doc 1.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 2: Doc 4 doesn't mention 1. Doc 4 prints it first at character 45,854, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- DRAFT: not locally checked. Use it for a quick test or a look at the form only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
How much grant money did the Future News Pilot Fund pay out, on average, to each project it funded?
```

### Number of asks

1 ask

### Gold answer

```text
About £50,000
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 1, section "An innovation fund for news"): the Government launched the £2 million Future News Pilot Fund in October 2019, and the report says the fund "issued grants to 20 projects".
Step 2. Source input (Doc 4, David Floyd of Social Spider answering Clive Efford on funding): Floyd, who says he worked on the fund, tells the committee "That was £2 million and about £1 million was grant funding." So only about half of the fund was paid out as grants.
Step 3. Calculation (Doc 1 and Doc 4): the grant funding is about £1 million and it went to the funded projects of Step 1, so the average is approximate: 1,000,000 / 20 = 50,000 pounds per funded project.
Step 4. Wrong route, for comparison (Doc 1 and Doc 4): dividing the whole fund by the funded projects gives 2,000,000 / 20 = 100,000 pounds, which counts money that Doc 4 says was not grant funding.
Step 5. Final answer (Doc 1 and Doc 4): the fund paid out about £50,000 of grant money, on average, to each project it funded.
```

### Answer components

Component 1

```text
About £50,000
```

### Evidence

Evidence 1: document Doc 1 (ukc_6536_report_33635.txt), proves component 1. About £50,000 (local note: para 41, launch of the fund)

```text
in October 2019 launched the £2 million Future News Pilot Fund (FNF), administered by Nesta
```

Evidence 2: document Doc 1 (ukc_6536_report_33635.txt), proves component 1. About £50,000 (local note: para 41, applications and grants)

```text
It received 178 applications and issued grants to 20 projects.
```

Evidence 3: document Doc 4 (ukc_6536_oral_10571.txt), proves component 1. About £50,000 (local note: Q254, David Floyd)

```text
You mentioned the NESTA Future News Fund, which I worked on to an extent. That was £2 million and about £1 million was grant funding.
```

### Necessary documents

- Tick Doc 1 (ukc_6536_report_33635.txt), role: Answer component
- Tick Doc 4 (ukc_6536_oral_10571.txt), role: Answer component

Leave unticked: Doc 2 (ukc_6536_oral_10244.txt), Doc 3 (ukc_6536_oral_10505.txt)

### Reasoning tags

Tick: Cross-document join, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Part vs total: Doc 1 prints the fund's £2 million total beside its 20 funded projects, so a careless solver divides the total and answers £100,000. Doc 4's witness says only about £1 million of it was grant funding, the part asked about: about £50,000.
```

(45 / 50 words.)
