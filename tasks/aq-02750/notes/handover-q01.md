# aq-02750 q01 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02750 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 a19557956fc4a5fa5640a7bcc5bd2c87a2873260d95dd5df7d428be21ea1d8a7: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D05 = Doc 5, D06 = Doc 6, D07 = Doc 7.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
By what percentage, to one decimal, did DRC's confirmed cases rise between the two counts in CDC's entry-suspension order in force when CDC raised its outbreak response to Level 1, its highest?
```

### Number of asks

1 ask

### Gold answer

```text
819.8%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 6, factual basis, section III.B, with its footnote): CDC escalated its response to the outbreak to a Level 1, the highest level in its Graduated Response Framework. The sentence carries no date; its footnote cites a CDC internal decision memo dated in late June 2026. Doc 7 repeats the sentence and the footnote.

Step 2. Source input (Doc 6, DATES): the order printed in Doc 6 took effect on July 13, 2026 and already reports the escalation, so the escalation came before that order.

Step 3. Source input (Doc 5, SUMMARY and DATES): the order printed in Doc 5 took effect on June 21, 2026 and was to remain in effect through July 21, 2026. Doc 5 does not report a Level 1 response, and the memo is dated after June 21, so the Doc 5 order was the one in force when CDC raised its response.

Step 4. Source input (Doc 5, factual basis, section III.B): Doc 5 cites two DRC confirmed-case counts: 91 confirmed cases on May 22, 2026, when the Amended Order was issued, and 837 confirmed cases as of June 15, 2026. Its text rounds the rise to more than 800 percent.

Step 5. Calculation (Doc 5 and Doc 6): the later count less the earlier count: 837 - 91 = 746.

Step 6. Calculation (Doc 5 and Doc 6): that rise as a percentage of the earlier count, to one decimal: 746 / 91 = 819.8%.
```

### Answer components

Component 1

```text
819.8%
```

### Evidence

Evidence 1: document Doc 6 (fr_2026_14365.txt), proves component 1. 819.8% (local note: section III.B, L178)

```text
Commensurate with the deterioration of the epidemiological situation in DRC, CDC escalated its response to the outbreak to a Level 1, the highest level within the agency's Graduated Response Framework.
```

Evidence 2: document Doc 6 (fr_2026_14365.txt), proves component 1. 819.8% (local note: footnote 18, L184)

```text
CDC, Internal Decision Memo, June 26, 2026.
```

Evidence 3: document Doc 6 (fr_2026_14365.txt), proves component 1. 819.8% (local note: DATES, L27)

```text
This action took effect July 13, 2026, at 5:00 p.m. EDT.
```

Evidence 4: document Doc 7 (fr_2026_16706.txt), proves component 1. 819.8% (local note: section III.B, L163)

```text
Commensurate with the deterioration of the epidemiological situation in DRC, CDC escalated its response to the outbreak to a Level 1, the highest level within the agency's Graduated Response Framework.
```

Evidence 5: document Doc 7 (fr_2026_16706.txt), proves component 1. 819.8% (local note: footnote 19, L169)

```text
CDC, Internal Decision Memo, June 26, 2026.
```

Evidence 6: document Doc 5 (fr_2026_12790.txt), proves component 1. 819.8% (local note: SUMMARY, L25)

```text
This Order was issued on June 21, 2026, and shall remain in effect through 4:59 p.m. Eastern Daylight Time (EDT) on Tuesday, July 21, 2026.
```

Evidence 7: document Doc 5 (fr_2026_12790.txt), proves component 1. 819.8% (local note: section III.B, L125)

```text
On May 22, 2026, when the Amended Order was issued, DRC reported 91 confirmed cases across 11 health zones.
```

Evidence 8: document Doc 5 (fr_2026_12790.txt), proves component 1. 819.8% (local note: section III.B, L125)

```text
As of June 15, 2026, DRC reports 837 confirmed cases across 31 health zones
```

### Necessary documents

- Tick Doc 5 (fr_2026_12790.txt), role: Answer component
- Tick Doc 6 (fr_2026_14365.txt), role: Used to identify; also tick Doc 7 (fr_2026_16706.txt) and choose it in Doc 6's "or..." box

Leave unticked: Doc 1 (fr_2024_10390.txt), Doc 2 (fr_2024_30500.txt), Doc 3 (fr_2025_23970.txt), Doc 4 (fr_2026_10543.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Wrong year or edition: Doc 6 and Doc 7 report the Level 1 response beside their own counts (123.8% and 130.5%), but their footnote dates it June 26, 2026, when Doc 5's June 21 order was in force. Its counts, 91 and 837, give 819.8%.
```

(45 / 50 words.)
