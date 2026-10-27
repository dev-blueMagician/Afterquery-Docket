# aq-02157 q01 hand-over

Generated 2026-10-09 by `python tools/check_questions.py tasks/aq-02157 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 5, difficulty_target medium, origin claude.
- tested_sha256 31ee6be207fec2e31b9554f6ffb88468957934a8e4da7ea61902e30faad720c6: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 1, D05 = Doc 3.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN points-or-percent: comparing a rate: say 'percentage points' or 'percent (relative)'
  - WARN revision: more than two revision rounds; replace an ineffective question family or record why new evidence justifies another revision
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
If each UK nation's adult smoking rate repeated its 2021-to-2022 percentage-point change yearly, how many points, to one decimal place, would separate the highest and lowest in 2030?
```

### Number of asks

1 ask

### Gold answer

```text
8.9 percentage points
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 3, ONS report Adult smoking habits in the UK): in 2021 the adult smoking rate was 13 per cent in England, 14.8 per cent in Scotland, 14.1 per cent in Wales and 13.8 per cent in Northern Ireland.

Step 2. Source fact (Doc 1, ONS report Adult smoking habits in the UK): in 2022 the rate was 12.7 per cent in England, 14.1 per cent in Wales, 14.0 per cent in Northern Ireland and 13.9 per cent in Scotland. This list gives the nations in a different order, so each nation is matched by name.

Step 3. Calculation (from Steps 1 and 2; Doc 3 and Doc 1): Northern Ireland's yearly change: 14.0 - 13.8 = 0.2 percentage points, a rise.

Step 4. Calculation (from Steps 1 and 2; Doc 3 and Doc 1): Scotland's yearly fall: 14.8 - 13.9 = 0.9 percentage points.

Step 5. Calculation (from Steps 1 and 2; Doc 3 and Doc 1): England's yearly fall: 13 - 12.7 = 0.3 percentage points.

Step 6. Calculation (from Steps 1 and 2; Doc 3 and Doc 1): Wales's change: 14.1 - 14.1 = 0 percentage points, so Wales stays at 14.1 per cent.

Step 7. Calculation (from Step 3; Doc 3 and Doc 1): Northern Ireland's rise over the eight years from 2022 to 2030: 0.2 * 8 = 1.6 percentage points.

Step 8. Calculation (from Steps 2 and 7; Doc 3 and Doc 1): Northern Ireland's rate in 2030, in per cent: 14.0 + 1.6 = 15.6 (the highest of the four).

Step 9. Calculation (from Step 4; Doc 3 and Doc 1): Scotland's fall over the same eight years: 0.9 * 8 = 7.2 percentage points.

Step 10. Calculation (from Steps 2 and 9; Doc 3 and Doc 1): Scotland's rate in 2030, in per cent: 13.9 - 7.2 = 6.7 (the lowest of the four).

Step 11. Calculation (from Step 5; Doc 3 and Doc 1): England's fall over the same eight years: 0.3 * 8 = 2.4 percentage points.

Step 12. Calculation (from Steps 2 and 11; Doc 3 and Doc 1): England's rate in 2030, in per cent: 12.7 - 2.4 = 10.3 (between Scotland and Wales).

Step 13. Calculation (from Step 2; Doc 1): gap between Northern Ireland and Scotland in 2022: 14.0 - 13.9 = 0.1 percentage points.

Step 14. Calculation (from Steps 7 and 9; Doc 3 and Doc 1): how much that gap widens by 2030 (Northern Ireland's rise plus Scotland's fall): 1.6 + 7.2 = 8.8 percentage points.

Step 15. Calculation (from Steps 13 and 14; Doc 3 and Doc 1): gap between the highest (Northern Ireland) and lowest (Scotland) in 2030: 0.1 + 8.8 = 8.9 percentage points.
```

### Answer components

Component 1

```text
8.9 percentage points
```

### Evidence

Evidence 1: document Doc 3 (Mandating-quit-information-messages-inside-tobacco-packs.txt), proves component 1. 8.9 percentage points (local note: L68, ONS 2021 report)

```text
Adult smoking habits in the UK: 2021 shows that the adult smoking rate in the UK is the lowest on record
```

Evidence 2: document Doc 3 (Mandating-quit-information-messages-inside-tobacco-packs.txt), proves component 1. 8.9 percentage points (local note: L70)

```text
13% in England
```

Evidence 3: document Doc 3 (Mandating-quit-information-messages-inside-tobacco-packs.txt), proves component 1. 8.9 percentage points (local note: L72)

```text
14.8% in Scotland
```

Evidence 4: document Doc 3 (Mandating-quit-information-messages-inside-tobacco-packs.txt), proves component 1. 8.9 percentage points (local note: L74)

```text
14.1% in Wales
```

Evidence 5: document Doc 3 (Mandating-quit-information-messages-inside-tobacco-packs.txt), proves component 1. 8.9 percentage points (local note: L76)

```text
13.8% in Northern Ireland
```

Evidence 6: document Doc 1 (Creating-a-smokefree-generation-and-tackling-youth-vaping.txt), proves component 1. 8.9 percentage points (local note: L42, ONS 2022 report)

```text
Adult smoking habits in the UK 2022 reported that 6.4 million people in the UK were current smokers
```

Evidence 7: document Doc 1 (Creating-a-smokefree-generation-and-tackling-youth-vaping.txt), proves component 1. 8.9 percentage points (local note: L44)

```text
12.7% in England
```

Evidence 8: document Doc 1 (Creating-a-smokefree-generation-and-tackling-youth-vaping.txt), proves component 1. 8.9 percentage points (local note: L46)

```text
14.1% in Wales
```

Evidence 9: document Doc 1 (Creating-a-smokefree-generation-and-tackling-youth-vaping.txt), proves component 1. 8.9 percentage points (local note: L48)

```text
14.0% in Northern Ireland
```

Evidence 10: document Doc 1 (Creating-a-smokefree-generation-and-tackling-youth-vaping.txt), proves component 1. 8.9 percentage points (local note: L50)

```text
13.9% in Scotland
```

### Necessary documents

- Tick Doc 3 (Mandating-quit-information-messages-inside-tobacco-packs.txt), role: Answer component
- Tick Doc 1 (Creating-a-smokefree-generation-and-tackling-youth-vaping.txt), role: Answer component

Leave unticked: Doc 2 (Creating-a-smokefree-generation-and-tackling-youth-vaping-2.txt), Doc 4 (Mandating-quit-information-messages-inside-tobacco-packs-2.txt), Doc 5 (Mandating-quit-information-messages-inside-tobacco-packs-3.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Aggregation

Leave unticked: Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Picks the wrong entity or section

#### Failure mode 2

Trap: Figure that must be computed

How a careless solver fails: Rounding, scale or sign

#### Failure mode 3

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Doc 3 lists 2021 rates England, Scotland, Wales, Northern Ireland; Doc 1 lists 2022 England, Wales, Northern Ireland, Scotland, so positional pairing gives 6.2. Northern Ireland rose 0.2; treating it as a fall gives 7.4. Keeping 2022's extremes, Wales and England, gives 3.8. By 2030: 15.6 minus 6.7.
```

(48 / 50 words.)
