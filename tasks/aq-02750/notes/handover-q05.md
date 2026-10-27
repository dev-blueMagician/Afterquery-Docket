# aq-02750 q05 hand-over

Generated 2026-10-11 by `python tools/check_questions.py tasks/aq-02750 --handover --q q05` from questions/q05.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target easy, origin claude.
- tested_sha256 6881cae301e88637a4a3fca9f83e4e7b8599ac1b7e02ae3883064d861d9da5e6: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D04 = Doc 4, D05 = Doc 5, D06 = Doc 6.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN sibling: q04 has the same answer; do the two ask for the same fact?
  - WARN sibling: six words shared with q04: '18 days after that order was'
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q05.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Suppose on June 25, 2026, CDC received 30 letters and 27 portal comments on its interim quarantine rule and 21 letters on its June 21 Ebola entry order, and that 22 and 19 portal comments later reached its June and July orders, each 18 days after that order was issued. How many would meet CDC's requirements on method and timing?
```

### Number of asks

1 ask

### Gold answer

```text
89 comments
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 4, DATES and ADDRESSES): comments on the interim final rule must be received by June 26, 2026. They may be submitted by one method only, the Federal eRulemaking Portal, and all comments must be submitted electronically.

Step 2. Application (Doc 4 and Doc 5): the 30 letters on the rule were not submitted electronically, so they do not meet the rule's method requirement. The 27 portal comments on the rule arrived on June 25, before June 26, and count.

Step 3. Source input (Doc 5, SUMMARY, DATES and ADDRESSES): the June order was issued on June 21, 2026. Comments on it may be submitted through the portal or by mail and must be received on or before July 10, 2026.

Step 4. Application (Doc 4 and Doc 5): the 21 letters on the June order came by mail, a method that order accepts, on June 25, before July 10, and count.

Step 5. Calculation (Doc 5 and Doc 6): June has 30 days, so the days of June left after June 21 are 30 - 21 = 9.

Step 6. Calculation (Doc 5 and Doc 6): the rest of the 18 days fall in July: 18 - 9 = 9. The June order's batch arrived on July 9, before July 10, so its 22 comments count.

Step 7. Source input (Doc 6, SUMMARY and DATES): the July order was issued on July 13, 2026, and written comments on it must be received on or before July 31, 2026.

Step 8. Calculation (Doc 5 and Doc 6): the July order's batch arrived on this day of July: 13 + 18 = 31. July 31 is the last day that order allows, so its 19 comments count.

Step 9. Application (Doc 5 and Doc 6): Doc 6 also says the June order provided a 15-day comment period. That phrase does not replace the dates the notices print: comments must be received on or before July 10 for the June order and on or before July 31 for the July order, and both batches meet them.

Step 10. Calculation (Doc 4 and Doc 5): the rule's timely portal comments plus the June order's letters: 27 + 21 = 48.

Step 11. Calculation (Doc 5 and Doc 6): adding the June order's batch: 48 + 22 = 70.

Step 12. Calculation (Doc 5 and Doc 6): adding the July order's batch: 70 + 19 = 89.
```

### Answer components

Component 1

```text
89 comments
```

### Evidence

Evidence 1: document Doc 4 (fr_2026_10543.txt), proves component 1. 89 comments (local note: DATES, L30)

```text
Comment date: Comments must be received by June 26, 2026.
```

Evidence 2: document Doc 4 (fr_2026_10543.txt), proves component 1. 89 comments (local note: ADDRESSES, L33)

```text
You may submit comments, identified by CDC-2026-0991, by the following method:
```

Evidence 3: document Doc 4 (fr_2026_10543.txt), proves component 1. 89 comments (local note: ADDRESSES, L34)

```text
Federal eRulemaking Portal: http://www.regulations.gov.
```

Evidence 4: document Doc 4 (fr_2026_10543.txt), proves component 1. 89 comments (local note: ADDRESSES, L39)

```text
Because of staff and resource limitations, all comments must be submitted electronically to www.regulations.gov.
```

Evidence 5: document Doc 5 (fr_2026_12790.txt), proves component 1. 89 comments (local note: SUMMARY, L25)

```text
This Order was issued on June 21, 2026, and shall remain in effect through 4:59 p.m. Eastern Daylight Time (EDT) on Tuesday, July 21, 2026.
```

Evidence 6: document Doc 5 (fr_2026_12790.txt), proves component 1. 89 comments (local note: DATES, L27)

```text
This action took effect June 21, 2026, at 5:00 p.m. EDT. Written comments must be received on or before July 10, 2026.
```

Evidence 7: document Doc 5 (fr_2026_12790.txt), proves component 1. 89 comments (local note: ADDRESSES, L29)

```text
by either of the methods listed below. Do not submit comments by email. CDC does not accept comments by email.
```

Evidence 8: document Doc 5 (fr_2026_12790.txt), proves component 1. 89 comments (local note: ADDRESSES, L32)

```text
Mail: Division of Global Migration Health, Centers for Disease Control and Prevention, 1600 Clifton Road NE, MS H16-4, Atlanta, GA 30329.
```

Evidence 9: document Doc 6 (fr_2026_14365.txt), proves component 1. 89 comments (local note: SUMMARY, L25)

```text
This Order was issued on July 13, 2026, and shall remain in effect through 4:59 p.m. Eastern Daylight Time (EDT) on Wednesday, August 12, 2026.
```

Evidence 10: document Doc 6 (fr_2026_14365.txt), proves component 1. 89 comments (local note: DATES, L27)

```text
This action took effect July 13, 2026, at 5:00 p.m. EDT. Written comments must be received on or before July 31, 2026.
```

### Necessary documents

- Tick Doc 4 (fr_2026_10543.txt), role: Answer component
- Tick Doc 5 (fr_2026_12790.txt), role: Answer component
- Tick Doc 6 (fr_2026_14365.txt), role: Answer component

Leave unticked: Doc 1 (fr_2024_10390.txt), Doc 2 (fr_2024_30500.txt), Doc 3 (fr_2025_23970.txt), Doc 7 (fr_2026_16706.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Conditional filter, Aggregation

Leave unticked: Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Wrong jurisdiction or scope

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Wrong jurisdiction or scope: Doc 5's order accepts mailed comments, and the question's own letters on that order count, but Doc 4's interim rule takes comments only through the portal. Carrying the order's mail rule to the rule counts its 30 letters: 119. The rule's own terms give 89.
```

(49 / 50 words.)
