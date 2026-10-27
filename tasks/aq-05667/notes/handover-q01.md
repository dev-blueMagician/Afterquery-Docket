# aq-05667 q01 hand-over

Generated 2026-10-15 by `python tools/check_questions.py tasks/aq-05667 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target hard, origin claude.
- tested_sha256 a725fc659557686a8d0c8d4e44d4e13e4bc4e8ac0b5b331af5d03276d42609f1: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 3, D02 = Doc 7.
- Floor: 0 FAIL, 3 WARN.
  - WARN strong-screen: the strong solver was right in every fresh solve of this exact sentence: likely Too easy at High. Say so with the hand-over; the user decides whether to run it. Never reword or re-screen the sentence to find a miss
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN units: the answer is a bare number; give its units (form: 'short and checkable, with units')
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
What was Sherwin-Williams' actual 2025 increase in interest expense minus the increase it had anticipated for that year in its annual report for 2024, in millions of dollars to one decimal place?
```

### Number of asks

1 ask

### Gold answer

```text
-10.7
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 3, outlook for 2025): Doc 3 expects Interest expense to increase by approximately 40 million dollars in 2025, from refinancing at higher interest rates the long-term debt maturities due in 2025, together with those refinanced during 2024.
Step 2. Source input (Doc 3, same outlook paragraph, next sentence): "In addition", Doc 3 expects about 100 million dollars of additional costs in 2025 from the transition into the new global headquarters and R&D center, which include about 80 million dollars of selling, general and administrative expenses and about 20 million dollars of Interest expense.
Step 3. Calculation (Doc 3): the increase in Interest expense anticipated for 2025 is the refinancing rise plus the headquarters interest: 40 + 20 = 60 million dollars (derived).
Step 4. Source input (Doc 7, results of operations for 2025): Doc 7 states that Interest expense "increased $49.3 million in 2025 compared to 2024", partly from interest related to the new global headquarters and R&D center, both placed into service in 2025.
Step 5. Final answer (Doc 3 and Doc 7): actual increase minus anticipated increase: 49.3 - 60 = -10.7 million dollars.
```

### Answer components

Component 1

```text
-10.7
```

### Evidence

Evidence 1: document Doc 3 (shw_10k_mdna_2024-12-31.txt), proves component 1. -10.7 (local note: outlook for 2025, interest expense)

```text
Together with the long-term debt maturities refinanced during 2024, Interest expense is expected to increase by approximately $40 million in 2025.
```

Evidence 2: document Doc 3 (shw_10k_mdna_2024-12-31.txt), proves component 1. -10.7 (local note: outlook for 2025, headquarters transition)

```text
In addition, we expect to incur additional costs associated with the transition into our new global headquarters and research and development (R&D) center in 2025 of approximately $100 million, which includes approximately $80 million of Selling, general and administrative expenses and approximately $20 million of Interest expense.
```

Evidence 3: document Doc 7 (shw_10k_mdna_2025-12-31.txt), proves component 1. -10.7 (local note: results of operations, interest expense)

```text
Interest expense increased $49.3 million in 2025 compared to 2024 primarily due to an increase in long-term debt, interest expense related to the new global headquarters and research and development center which were both placed into service in 2025
```

### Necessary documents

- Tick Doc 3 (shw_10k_mdna_2024-12-31.txt), role: Answer component
- Tick Doc 7 (shw_10k_mdna_2025-12-31.txt), role: Answer component

Leave unticked: Doc 1 (shw_10q_mdna_2024-06-30.txt), Doc 2 (shw_10q_mdna_2024-09-30.txt), Doc 4 (shw_10q_mdna_2025-03-31.txt), Doc 5 (shw_10q_mdna_2025-06-30.txt), Doc 6 (shw_10q_mdna_2025-09-30.txt), Doc 8 (shw_10q_mdna_2026-03-31.txt), Doc 9 (shw_10q_mdna_2026-06-30.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Aggregation

Leave unticked: Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Part vs total: Doc 3's 2025 outlook prints a $40 million interest-expense rise, then adds "In addition" about $20 million of headquarters interest. Using $40 million alone gives +9.3. The anticipated total is $60 million; Doc 7's actual rise is $49.3 million, so -10.7.
```

(44 / 50 words.)
