# aq-05747 q01 hand-over

Generated 2026-10-15 by `python tools/check_questions.py tasks/aq-05747 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target hard, origin claude.
- tested_sha256 9e693c0f5d75ac75ec3fa3718f27b4f4e5e03bc2601ca0c9b359a1ea26f05327: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 5, D05 = Doc 3.
- Floor: 0 FAIL, 4 WARN.
  - WARN strong-screen: the strong solver was right in every fresh solve of this exact sentence: likely Too easy at High. Say so with the hand-over; the user decides whether to run it. Never reword or re-screen the sentence to find a miss
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN units: the answer is a bare number; give its units (form: 'short and checkable, with units')
  - WARN form-numbers: Step 2: Doc 3 doesn't mention 1,274. Doc 3 prints it first at character 49,792, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Judging by Coca-Cola's earnings releases together, what was the largest single impairment charge the company recorded in fiscal 2025, in millions of dollars?
```

### Number of asks

1 ask

### Gold answer

```text
1,274
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 3, Asset Impairments, three months and year ended December 31, 2025): the largest charge Doc 3 describes as an impairment is "a charge of $960 million related to the impairment of our BODYARMOR trademark"; each other 2025 impairment charge it lists is smaller.
Step 2. Source input (Doc 3, Transaction Gains/Losses, same period): Doc 3 also records "a charge of $1,274 million related to our bottling operations in Africa that became held for sale", without calling it an impairment.
Step 3. Source input (Doc 5, Transaction Gains/Losses, three and six months ended July 3, 2026): Doc 5 records "a reduction in the previously recorded impairment charge" related to the same African bottling operations held for sale. Its second-quarter reduction is larger than its six-month reduction, so the first quarter of 2026 had added to that charge, and the second-quarter reduction is larger than that addition. The impairment charge being reduced therefore includes a charge recorded before 2026.
Step 4. Inference (Doc 3 and Doc 5): Doc 3's $1,274 million charge is the charge recorded on those same operations when they became held for sale, before 2026. Read together, the releases treat it as an impairment charge.
Step 5. Comparison (Doc 3 and Doc 5): $1,274 million is larger than the $960 million BODYARMOR impairment, so the largest single impairment charge recorded in fiscal 2025 is 1,274 million dollars. Doc 5's reductions were recorded in 2026 and do not change the fiscal 2025 amount.
```

### Answer components

Component 1

```text
1,274
```

### Evidence

Evidence 1: document Doc 3 (the-coca-cola-company-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-10.txt), proves component 1. 1,274 (local note: Transaction Gains/Losses, three months and year ended December 31, 2025)

```text
The company also recorded a charge of $1,274 million related to our bottling operations in Africa that became held for sale
```

Evidence 2: document Doc 3 (the-coca-cola-company-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-10.txt), proves component 1. 1,274 (local note: Asset Impairments, three months and year ended December 31, 2025)

```text
the company recorded a charge of $960 million related to the impairment of our BODYARMOR trademark
```

Evidence 3: document Doc 5 (the-coca-cola-company-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-07-28.txt), proves component 1. 1,274 (local note: Transaction Gains/Losses, three and six months ended July 3, 2026)

```text
the company recorded a reduction in the previously recorded impairment charge of $66 million and $56 million, respectively, related to our bottling operations in Africa, which are held for sale
```

### Necessary documents

- Tick Doc 3 (the-coca-cola-company-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-10.txt), role: Answer component
- Tick Doc 5 (the-coca-cola-company-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-07-28.txt), role: Used to identify

Leave unticked: Doc 1 (the-coca-cola-company-2q-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-07-22.txt), Doc 2 (the-coca-cola-company-3q-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-10-21.txt), Doc 4 (the-coca-cola-company-1q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-04-28.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Conditional filter, Entity resolution

Leave unticked: Unit normalization, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Picks the wrong entity or section

#### Why these are traps (at most 50 words)

```text
Linking: Doc 3 books a $1,274 million charge on its African bottling operations held for sale under Transaction Gains/Losses, never calling it an impairment; its impairment section peaks at $960 million (BODYARMOR), the wrong answer. Doc 5 reduces "the previously recorded impairment charge" on those operations, so 1,274.
```

(48 / 50 words.)
