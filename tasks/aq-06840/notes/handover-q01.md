# aq-06840 q01 hand-over

Generated 2026-10-19 by `python tools/check_questions.py tasks/aq-06840 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target hard, origin claude.
- tested_sha256 0ceca1740665758b49aacecb182284b1b8085e00ea95558febc0776acdf43ea1: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 7, D06 = Doc 5, D08 = Doc 6.
- Floor: 0 FAIL, 13 WARN.
  - WARN strong-screen: the strong solver was right in every fresh solve of this exact sentence: likely Too easy at High. Say so with the hand-over; the user decides whether to run it. Never reword or re-screen the sentence to find a miss
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN units: the answer is a bare number; give its units (form: 'short and checkable, with units')
  - WARN form-numbers: Step 2: Doc 5 doesn't mention 692,255. Doc 5 prints it first at character 21,633, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 5 doesn't mention 1,337,719. Doc 5 prints it first at character 21,717, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 6 doesn't mention 687,876. Doc 6 prints it first at character 23,070, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 6 doesn't mention 1,680,529. Doc 6 prints it first at character 23,154, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 7: Doc 7 doesn't mention 547,207. Doc 7 prints it first at character 20,614, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 7: Doc 7 doesn't mention 182,624. Doc 7 prints it first at character 20,697, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 8: Doc 7 doesn't mention 547,207. Doc 7 prints it first at character 20,614, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 8: Doc 7 doesn't mention 182,624. Doc 7 prints it first at character 20,697, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN period: names a quarter or fiscal year without 'fiscal'/'calendar'/'ended'; confirm the period is pinned (rule 9b)
  - WARN sibling: six words shared with q02: 'cash flow operating cash flow minus'
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
On the basis used in Albemarle's Q3 2025 earnings release, by how much did its free cash flow (operating cash flow minus capital expenditures) improve from Q4 2024 to Q1 2025? Answer in millions of dollars to one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
711.8
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 5, highlights, footnote (a) to free cash flow): free cash flow is "defined as operating cash flow minus capital expenditures", the definition the question states.
Step 2. Source input (Doc 5, selected consolidated cash flow data, nine months ended September 30, 2024 column): net cash provided by operating activities 692,255 and capital expenditures (1,337,719), in thousands of dollars. This column shows settlements of foreign currency forward contracts as an investing line, the revised presentation on which the Q3 2025 release reports 2024.
Step 3. Source input (Doc 6, selected consolidated cash flow data, year ended December 31, 2024 column, with the same investing line): net cash provided by operating activities 687,876 and capital expenditures (1,680,529), in thousands of dollars.
Step 4. Calculation (Doc 5 and Doc 6): no release prints the fourth quarter of 2024 on its own, so it is the year less the nine months; operating activities used cash in that quarter: 692,255 - 687,876 = 4,379 (thousands of dollars of outflow).
Step 5. Calculation (Doc 5 and Doc 6): fourth-quarter 2024 capital expenditures: 1,680,529 - 1,337,719 = 342,810 (thousands of dollars).
Step 6. Calculation (Doc 5 and Doc 6): fourth-quarter 2024 free cash flow was an outflow of capital expenditures plus the operating outflow: 342,810 + 4,379 = 347,189 (thousands of dollars).
Step 7. Source input (Doc 7, selected consolidated cash flow data, three months ended March 31, 2025 column, with the same investing line): net cash provided by operating activities 547,207 and capital expenditures (182,624), in thousands of dollars.
Step 8. Calculation (Doc 7): first-quarter 2025 free cash flow: 547,207 - 182,624 = 364,583 (thousands of dollars).
Step 9. Calculation (Doc 5, Doc 6 and Doc 7): improvement from the fourth-quarter 2024 outflow to the first-quarter 2025 inflow: 364,583 + 347,189 = 711,772 (thousands of dollars).
Step 10. Final answer (Doc 5, Doc 6 and Doc 7): 711,772 thousand dollars, given in millions of dollars to one decimal place as the question asks.
```

### Answer components

Component 1

```text
711.8
```

### Evidence

Evidence 1: document Doc 5 (albemarle-corporation-q3-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-11-05.txt), proves component 1. 711.8 (local note: highlights, footnote (a)

```text
A non-GAAP measure defined as operating cash flow minus capital expenditures
```

Evidence 2: document Doc 5 (albemarle-corporation-q3-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-11-05.txt), proves component 1. 711.8 (local note: selected consolidated cash flow data, nine months ended September 30, 2025 and 2024)

```text
|Net cash provided by operating activities|893,782|692,255|
```

Evidence 3: document Doc 5 (albemarle-corporation-q3-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-11-05.txt), proves component 1. 711.8 (local note: same table)

```text
|Capital expenditures|(434,416)|(1,337,719)|
```

Evidence 4: document Doc 5 (albemarle-corporation-q3-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-11-05.txt), proves component 1. 711.8 (local note: same table, investing activities)

```text
|Proceeds (payments) from settlement of foreign currency forward contracts, net|144,540|(1,956)|
```

Evidence 5: document Doc 6 (albemarle-corporation-q4-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-11.txt), proves component 1. 711.8 (local note: selected consolidated cash flow data, years ended December 31, 2025 and 2024)

```text
|Net cash provided by operating activities|1,282,267|687,876|
```

Evidence 6: document Doc 6 (albemarle-corporation-q4-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-11.txt), proves component 1. 711.8 (local note: same table)

```text
|Capital expenditures|(589,801)|(1,680,529)|
```

Evidence 7: document Doc 6 (albemarle-corporation-q4-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-11.txt), proves component 1. 711.8 (local note: same table, investing activities)

```text
|Proceeds (payments) from settlement of foreign currency forward contracts, net|114,236|(15,595)|
```

Evidence 8: document Doc 7 (albemarle-corporation-q1-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-05-06.txt), proves component 1. 711.8 (local note: selected consolidated cash flow data, three months ended March 31, 2026 and 2025)

```text
|Net cash provided by operating activities|346,244|547,207|
```

Evidence 9: document Doc 7 (albemarle-corporation-q1-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-05-06.txt), proves component 1. 711.8 (local note: same table)

```text
|Capital expenditures|(98,676)|(182,624)|
```

Evidence 10: document Doc 7 (albemarle-corporation-q1-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-05-06.txt), proves component 1. 711.8 (local note: same table, investing activities)

```text
|(Payments) proceeds from settlement of foreign currency forward contracts, net|(10,514)|50,245|
```

### Necessary documents

- Tick Doc 5 (albemarle-corporation-q3-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-11-05.txt), role: Answer component
- Tick Doc 6 (albemarle-corporation-q4-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-11.txt), role: Answer component
- Tick Doc 7 (albemarle-corporation-q1-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-05-06.txt), role: Answer component

Leave unticked: Doc 1 (albemarle-corporation-q3-2024-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2024-11-06.txt), Doc 2 (albemarle-corporation-q4-2024-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-02-12.txt), Doc 3 (albemarle-corporation-q1-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-04-30.txt), Doc 4 (albemarle-corporation-q2-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-07-30.txt), Doc 8 (albemarle-corporation-q2-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-08-05.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Superseded date or version

How a careless solver fails: Picks the wrong entity or section

#### Why these are traps (at most 50 words)

```text
Doc 2 (full-year 2024) and Doc 3 (Q1 2025) first printed cash flows that Doc 6 and Doc 7 restate on Doc 5's revised basis. Each period from its own release gives 717.8; on Doc 5's basis free cash flow was -347.2 in Q4 2024, 364.6 in Q1 2025.
```

(49 / 50 words.)
