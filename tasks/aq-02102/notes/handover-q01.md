# aq-02102 q01 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-02102 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 2, difficulty_target medium, origin claude.
- tested_sha256 96e6a6cda1bbcb43aaf17650609786185b165bdb9c28d1bcd9859c14060bafe2: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 2, D03 = Doc 4.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
How many percentage points did individuals' share of responses, including those addressing no question, fall between the 2021-22 and 2023 Civil Service McCloud consultations (two decimal places)?
```

### Number of asks

1 ask

### Gold answer

```text
3.81 percentage points
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 2, paragraph 3.7, 2021-22 consultation): 1,268 responses directly addressed the consultation questions, 1,263 of them from individuals and five from trade unions. A response from Audit Wales was also received, and another 32 responses came from individuals that did not address the questions.

Step 2. Calculation (Doc 2), individual responses received in 2021-22: 1,263 + 32 = 1,295, the Individuals figure in Doc 2's Table 2 and Annex A, which therefore already includes the 32.

Step 3. Calculation (Doc 2), responses other than Audit Wales's: 1,268 + 32 = 1,300.

Step 4. Calculation (Doc 2), all responses received in 2021-22: 1,300 + 1 = 1,301, the Total Received in Doc 2's Table 2.

Step 5. Source fact (Doc 4, paragraph 3.9, 2023 consultation): 107 responses in some way addressed the consultation questions, 102 of them from individuals and five from organisations. In addition, another ten responses were received from individuals that did not address the questions.

Step 6. Source fact (Doc 4, Table 2): its Individuals row (102) and Total (107) leave out those ten responses, unlike Doc 2's table, which counts its 32. Doc 4's "Of which: Queried the effect of the remedy" row (68), responses that did not answer the questions in all respects, is part of the 102, not the ten.

Step 7. Calculation (Doc 4), all responses received in 2023: 107 + 10 = 117.

Step 8. Calculation (Doc 4), individual responses received in 2023: 102 + 10 = 112.

Step 9. Calculation (Doc 2 and Doc 4), first product for subtracting the unrounded shares of individuals over a common base: 1,295 * 117 = 151,515.

Step 10. Calculation (Doc 2 and Doc 4), second product: 112 * 1,301 = 145,712.

Step 11. Calculation (Doc 2 and Doc 4), difference of the products: 151,515 - 145,712 = 5,803.

Step 12. Calculation (Doc 2 and Doc 4), common base: 1,301 * 117 = 152,217.

Step 13. Calculation (Doc 2 and Doc 4), decrease in people's shares: 5,803 / 152,217 = 3.81%. The decrease was of those percentage points.
```

### Answer components

Component 1

```text
3.81
```

### Evidence

Evidence 1: document Doc 2 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service-2.txt), proves component 1. 3.81 (local note: L174, paragraph 3.7)

```text
The Cabinet Office received 1,268 responses in total from scheme members and trade unions which directly addressed the questions in the consultation.
```

Evidence 2: document Doc 2 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service-2.txt), proves component 1. 3.81 (local note: L174, paragraph 3.7)

```text
These consisted of 1,263 responses from individuals, and five responses from trade unions
```

Evidence 3: document Doc 2 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service-2.txt), proves component 1. 3.81 (local note: L174, paragraph 3.7)

```text
In addition, a response from Audit Wales was also received.
```

Evidence 4: document Doc 2 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service-2.txt), proves component 1. 3.81 (local note: L174, paragraph 3.7)

```text
Another 32 responses were received from individuals that did not address the questions posed by the consultation
```

Evidence 5: document Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), proves component 1. 3.81 (local note: L189, paragraph 3.9)

```text
The Cabinet Office received 107 responses in total from scheme members, trade unions and other organisations which in some way addressed the consultation questions.
```

Evidence 6: document Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), proves component 1. 3.81 (local note: L189, paragraph 3.9)

```text
These consisted of 102 responses from individuals and five responses from organisations.
```

Evidence 7: document Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), proves component 1. 3.81 (local note: L189, paragraph 3.9)

```text
In addition another ten responses were received from individuals that did not address the questions posed by the consultation
```

### Necessary documents

- Tick Doc 2 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service-2.txt), role: Answer component
- Tick Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), role: Answer component

Leave unticked: Doc 1 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service.txt), Doc 3 (Civil-Service-Pensions-2015-Remedy-McCloud-consultation.txt), Doc 5 (Consultation-on-reform-of-the-Civil-Service-Compensation.txt)

### Reasoning tags

Tick: Cross-document join, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Document convention

How a careless solver fails: Misapplies a rule or premise

#### Failure mode 2

Trap: Look-alike measure

How a careless solver fails: Picks the wrong entity or section

#### Failure mode 3

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Doc 2's Table 2 (1,295 of 1,301) already holds its 32 non-answering responses: adding them again gives 3.82, skipping Doc 4's ten gives 4.21. Doc 4's 68 "didn't answer" are inside its 107: 2.40. Doc 2's 1,268 "in total" omits Audit Wales: 3.89. Gold: 1,295/1,301 minus 112/117.
```

(47 / 50 words.)
