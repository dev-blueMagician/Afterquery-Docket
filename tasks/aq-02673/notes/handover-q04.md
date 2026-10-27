# aq-02673 q04 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02673 --handover --q q04` from questions/q04.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 2, difficulty_target medium, origin claude.
- tested_sha256 50ca7237a3b9884f43cf280c9d7b3e7f49e4d0922b66166885a38c486bf2cc98: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 3, D06 = Doc 6.
- Floor: 0 FAIL, 5 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 1: Doc 6 doesn't mention 1,316.14. Doc 6 prints it first at character 33,492, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 6 doesn't mention 1,509.98. Doc 6 prints it first at character 20,691, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN sibling: q05 has the same answer; do the two ask for the same fact?
  - WARN sibling: six words shared with q05: 'adjustments how many more metric tons'
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q04.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Before under- or overharvest adjustments, how many more metric tons of western Atlantic bluefin tuna TAC went to the United States in total for 2026 than for 2025 (to two decimals)?
```

### Number of asks

1 ask

### Gold answer

```text
168.84 mt
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 6, Table 5 and Comment 1): the U.S. bluefin tuna baseline quota is 1,316.14 mt for 2025 and 1,509.98 mt for 2026, before any carryover.

Step 2. Source input (Doc 6, note to Table 5): on top of the baseline quota the United States is allocated an additional 25 mt for pelagic longline bycatch in 2025, and a larger bycatch allocation in 2026.

Step 3. Source input (Doc 3, bluefin tuna quota section): the new bycatch allocation is derived from the eastern Atlantic and Mediterranean bluefin tuna TAC, so for 2026 the western Atlantic TAC tonnage that went to the United States is the baseline quota alone.

Step 4. Source input (Doc 3, bluefin tuna quota section and set-aside section): the set-aside now comes from the eastern TAC "as opposed to the western Atlantic TAC", and the earlier recommendation subtracted the longline bycatch allocation from the TAC before the country quotas were calculated. The earlier bycatch allocation was therefore drawn from the western Atlantic TAC and counts for 2025.

Step 5. Calculation (Doc 6 and Doc 3): western Atlantic TAC tonnage that went to the United States for 2025: 1,316.14 + 25 = 1,341.14 mt, the 2025 Total Quota that Table 5 prints.

Step 6. Calculation (Doc 6 and Doc 3): increase from 2025 to 2026: 1,509.98 - 1,341.14 = 168.84 mt.
```

### Answer components

Component 1

```text
168.84 mt
```

### Evidence

Evidence 1: document Doc 6 (fr_2026_16870.txt), proves component 1. 168.84 mt (local note: Comment 1, baseline quotas)

```text
NMFS received multiple comments supporting the increased U.S. bluefin tuna baseline quota from 1,316.14 mt to 1,509.98 mt
```

Evidence 2: document Doc 6 (fr_2026_16870.txt), proves component 1. 168.84 mt (local note: Table 5, baseline row)

```text
Baseline Quota.......................... 1,316.14 1,509.98
```

Evidence 3: document Doc 6 (fr_2026_16870.txt), proves component 1. 168.84 mt (local note: note to Table 5, bycatch allocations)

```text
The United States is allocated an additional 25 mt in 2025 and 62.5 mt in 2026 to account for bycatch related to pelagic longline fisheries.
```

Evidence 4: document Doc 3 (fr_2026_09059.txt), proves component 1. 168.84 mt (local note: bluefin tuna quota section, source of the new allocation)

```text
this allocation is derived from the eastern Atlantic and Mediterranean bluefin tuna TAC
```

Evidence 5: document Doc 3 (fr_2026_09059.txt), proves component 1. 168.84 mt (local note: same paragraph, earlier treatment)

```text
Recommendation 25-05 removed a provision from a prior recommendation that provided for subtracting the longline bycatch allocation from the TAC before calculating the individual country quotas.
```

Evidence 6: document Doc 3 (fr_2026_09059.txt), proves component 1. 168.84 mt (local note: set-aside section, change of source)

```text
Recommendation 25-05 now specifies that the set-aside comes from the eastern Atlantic bluefin tuna TAC as opposed to the western Atlantic TAC.
```

### Necessary documents

- Tick Doc 3 (fr_2026_09059.txt), role: Answer component
- Tick Doc 6 (fr_2026_16870.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_19459.txt), Doc 2 (fr_2025_24264.txt), Doc 4 (fr_2026_09973.txt), Doc 5 (fr_2026_10389.txt), Doc 7 (fr_2026_18031.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Conditional filter

Leave unticked: Unit normalization, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Wrong jurisdiction or scope

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Part vs total: Doc 6 Table 5's Baseline row gives 193.84, leaving out 2025's 25 mt bycatch allocation, which Doc 3 says came from the western TAC. Wrong scope: its Total row gives 231.34, counting 2026's 62.5 mt, which Doc 3 says comes from the eastern TAC. Gold: 168.84.
```

(49 / 50 words.)
