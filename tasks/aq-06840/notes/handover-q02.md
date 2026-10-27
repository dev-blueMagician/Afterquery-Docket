# aq-06840 q02 hand-over

Generated 2026-10-19 by `python tools/check_questions.py tasks/aq-06840 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 2, difficulty_target hard, origin claude.
- tested_sha256 03d88618b883af065f9ad34d566d624faa8e2551e92714f0fca72720987f8d9d: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 7, D04 = Doc 8.
- Floor: 0 FAIL, 12 WARN.
  - WARN strong-screen: the strong solver was right in every fresh solve of this exact sentence: likely Too easy at High. Say so with the hand-over; the user decides whether to run it. Never reword or re-screen the sentence to find a miss
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN units: the answer is a bare number; give its units (form: 'short and checkable, with units')
  - WARN form-numbers: Step 1: Doc 8 doesn't mention 709,997. Doc 8 prints it first at character 41,275, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 8 doesn't mention 71,731. Doc 8 prints it first at character 41,313, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 8 doesn't mention 638,266. Doc 8 prints it first at character 41,339, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 8 doesn't mention 538,180. Doc 8 prints it first at character 21,396, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 8 doesn't mention 302,252. Doc 8 prints it first at character 21,480, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 7 doesn't mention 547,207. Doc 7 prints it first at character 20,614, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 7 doesn't mention 182,624. Doc 7 prints it first at character 20,697, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN period: names a quarter or fiscal year without 'fiscal'/'calendar'/'ended'; confirm the period is pinned (rule 9b)
  - WARN sibling: six words shared with q01: 'cash flow operating cash flow minus'
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Using the most recently published figures, by how much did Albemarle's free cash flow (operating cash flow minus capital expenditures) for Q2 2026 exceed that for Q2 2025? Answer to the nearest million dollars.
```

### Number of asks

1 ask

### Gold answer

```text
767
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 8, reconciliation of free cash flow, three months ended June 30, 2026): net cash provided by operating activities $709,997 less capital expenditures (71,731) gives free cash flow of $638,266, in thousands of dollars, the definition the question states.
Step 2. Source input (Doc 8, selected consolidated cash flow data, six months ended June 30, 2025 column, the most recent printing of that half-year): net cash provided by operating activities 538,180 and capital expenditures (302,252), in thousands of dollars.
Step 3. Source input (Doc 7, selected consolidated cash flow data, three months ended March 31, 2025 column, the most recent printing of that quarter): net cash provided by operating activities 547,207 and capital expenditures (182,624), in thousands of dollars.
Step 4. Calculation (Doc 7 and Doc 8): no release prints the second quarter of 2025 on its own, so it is the six months less the first quarter; operating activities used cash in that quarter: 547,207 - 538,180 = 9,027 (thousands of dollars of outflow).
Step 5. Calculation (Doc 7 and Doc 8): second-quarter 2025 capital expenditures: 302,252 - 182,624 = 119,628 (thousands of dollars).
Step 6. Calculation (Doc 7 and Doc 8): second-quarter 2025 free cash flow was an outflow of capital expenditures plus the operating outflow: 119,628 + 9,027 = 128,655 (thousands of dollars).
Step 7. Calculation (Doc 7 and Doc 8): excess of the second-quarter 2026 inflow over the second-quarter 2025 outflow: 638,266 + 128,655 = 766,921 (thousands of dollars).
Step 8. Final answer (Doc 7 and Doc 8): 766,921 thousand dollars, given to the nearest million dollars as the question asks.
```

### Answer components

Component 1

```text
767
```

### Evidence

Evidence 1: document Doc 8 (albemarle-corporation-q2-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-08-05.txt), proves component 1. 767 (local note: reconciliation of free cash flow, three months ended June 30, 2026)

```text
|Net cash provided by operating activities|$709,997|
```

Evidence 2: document Doc 8 (albemarle-corporation-q2-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-08-05.txt), proves component 1. 767 (local note: same table)

```text
|Less: Capital expenditures|(71,731)|
```

Evidence 3: document Doc 8 (albemarle-corporation-q2-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-08-05.txt), proves component 1. 767 (local note: same table)

```text
|Free cash flow|$638,266|
```

Evidence 4: document Doc 8 (albemarle-corporation-q2-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-08-05.txt), proves component 1. 767 (local note: selected consolidated cash flow data, six months ended June 30, 2026 and 2025)

```text
|Net cash provided by operating activities|1,056,241|538,180|
```

Evidence 5: document Doc 8 (albemarle-corporation-q2-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-08-05.txt), proves component 1. 767 (local note: same table)

```text
|Capital expenditures|(170,407)|(302,252)|
```

Evidence 6: document Doc 7 (albemarle-corporation-q1-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-05-06.txt), proves component 1. 767 (local note: selected consolidated cash flow data, three months ended March 31, 2026 and 2025)

```text
|Net cash provided by operating activities|346,244|547,207|
```

Evidence 7: document Doc 7 (albemarle-corporation-q1-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-05-06.txt), proves component 1. 767 (local note: same table)

```text
|Capital expenditures|(98,676)|(182,624)|
```

### Necessary documents

- Tick Doc 8 (albemarle-corporation-q2-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-08-05.txt), role: Answer component
- Tick Doc 7 (albemarle-corporation-q1-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-05-06.txt), role: Answer component

Leave unticked: Doc 1 (albemarle-corporation-q3-2024-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2024-11-06.txt), Doc 2 (albemarle-corporation-q4-2024-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-02-12.txt), Doc 3 (albemarle-corporation-q1-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-04-30.txt), Doc 4 (albemarle-corporation-q2-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-07-30.txt), Doc 5 (albemarle-corporation-q3-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-11-05.txt), Doc 6 (albemarle-corporation-q4-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-11.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Superseded date or version

How a careless solver fails: Picks the wrong entity or section

#### Why these are traps (at most 50 words)

```text
Doc 3 first printed Q1 2025 operating cash flow as 545,383; Doc 7, the most recent printing, restates it as 547,207. Doc 3's figure makes Q2 2025 free cash flow -126.8 million and gives 765; with Doc 7's it is -128.7 million, so 767.
```

(44 / 50 words.)
