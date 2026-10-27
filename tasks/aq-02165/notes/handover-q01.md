# aq-02165 q01 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-02165 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 768279d9e074d519077f204a42e2b699f5d88ead61d011e3ca2bb3b1b7e41bfe: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 2, D05 = Doc 5.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Under the 2017 compensation proposals, how many years before their MOD-funded pension age could MDP officers get employer pension top-ups?
```

### Number of asks

1 ask

### Gold answer

```text
7 years
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 5, section 4.3 and paragraph 5.6): the 2017 proposals allow an employer-funded top-up to pension only from age 55, with that minimum age "tracked 10 years behind state pension age". So the earliest age for an employer-funded top-up is the member's State Pension age minus 10 years.

Step 2. Source fact (Doc 2, paragraph 4.9, Defence Police Federation extract): the MOD funds MDP officers "an effective pension age equal to three years below State pension age". So the MOD-funded pension age of an MDP officer is the State Pension age minus 3 years.

Step 3. Calculation (from Steps 1 and 2; Doc 2 and Doc 5): both ages are set from the same State Pension age, which cancels out of the gap: (State Pension age minus 3) minus (State Pension age minus 10) equals 10 minus 3. So the gap is 10 - 3 = 7 years.
```

### Answer components

Component 1

```text
7 years
```

### Evidence

Evidence 1: document Doc 5 (Consultation-on-reform-of-the-Civil-Service-Compensation.txt), proves component 1. 7 years (local note: L301, section 4.3)

```text
only to allow employer funded top up to pension from age 55 and for this to track 10
```

Evidence 2: document Doc 5 (Consultation-on-reform-of-the-Civil-Service-Compensation.txt), proves component 1. 7 years (local note: L328, paragraph 5.2)

```text
which the proposals increase to age 55, and this is tracked 10 years behind the State Pension Age
```

Evidence 3: document Doc 5 (Consultation-on-reform-of-the-Civil-Service-Compensation.txt), proves component 1. 7 years (local note: L344, paragraph 5.6)

```text
increasing the minimum age at which an employer can receive an employer funded pension top up to 55, tracked 10 years behind state pension age
```

Evidence 4: document Doc 2 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service-2.txt), proves component 1. 7 years (local note: L359, paragraph 4.9)

```text
The MOD has agreed to fund a lower NPA for MDP officers by paying for an effective pension age equal to three years below State pension age
```

### Necessary documents

- Tick Doc 2 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service-2.txt), role: Answer component
- Tick Doc 5 (Consultation-on-reform-of-the-Civil-Service-Compensation.txt), role: Answer component

Leave unticked: Doc 1 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service.txt), Doc 3 (Civil-Service-Pensions-2015-Remedy-McCloud-consultation.txt), Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt)

### Reasoning tags

Tick: Cross-document join, Entity resolution

Leave unticked: Temporal alignment, Unit normalization, Conditional filter, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Figure that must be computed

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Doc 2's DPF extract puts Home Office police NPA 60 beside the MDP rule: 60-55 = 5. Holding Doc 5's top-up age at 55 against State Pension age 67 gives 64-55 = 9. Both ages track State Pension age: gap 7.
```

(41 / 50 words.)
