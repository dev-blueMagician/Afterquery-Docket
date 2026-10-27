# aq-02157 q04 hand-over

Generated 2026-10-09 by `python tools/check_questions.py tasks/aq-02157 --handover --q q04` from questions/q04.md. Regenerate it after any edit. It is not a submission.

- Status ready, revision 3, difficulty_target medium, origin user+claude.
- tested_sha256 7790f824581b6cbee3fc9b98c51688851c9be1ebb33fc803cdb71472d6961f49: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 2, D03 = Doc 4.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN revision: more than two revision rounds; replace an ineffective question family or record why new evidence justifies another revision
  - WARN local-history: stale or unbound optional local records retained as history; no local rerun required
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin user+claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q04.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
What is the increase in the minimum excise duty on a pack of 20 cigarettes, to one decimal place, from the pack insert impact assessment to the government's response to the smoke-free consultation?
```

### Number of asks

1 ask

### Gold answer

```text
£1.5
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 2, affordability of vaping products): HMRC guidance on rates and allowances for Tobacco Products Duty estimates at least 8.46 pounds of excise duty on a packet of 20 cigarettes, so the minimum excise duty on a 20-pack in the response is 8.46 pounds.

Step 2. Source fact (Doc 4, the impact assessment's October 2021 duty rates table): cigarettes pay the highest of 262.90 pounds per 1,000 cigarettes plus 16.5% of retail price and 347.86 pounds per 1,000 cigarettes (the MET), so no pack pays less than 347.86 pounds per 1,000 cigarettes; the next paragraph calls this the MET threshold.

Step 3. Calculation (from Step 2; Doc 4 and Doc 2): minimum duty per cigarette: 347.86 / 1,000 = 0.34786 pounds.

Step 4. Calculation (from Step 3; Doc 4 and Doc 2): minimum duty per 20-pack: 0.34786 * 20 = 6.9572 pounds.

Step 5. Calculation (from Steps 1 and 4; Doc 2 and Doc 4): increase in the minimum from the impact assessment to the government's response: 8.46 - 6.9572 = 1.5028 pounds.

Step 6. Answer (from Step 5; Doc 2 and Doc 4): rounded to one decimal place, as the question asks, the increase of 1.5028 pounds is one and a half pounds.
```

### Answer components

Component 1

```text
£1.5
```

### Evidence

Evidence 1: document Doc 2 (Creating-a-smokefree-generation-and-tackling-youth-vaping-2.txt), proves component 1. £1.5 (local note: L1204, Affordability of vaping products)

```text
Guidance on rates and allowances for the Tobacco Products Duty estimates at least a £8.46 excise duty on a packet of 20 cigarettes
```

Evidence 2: document Doc 4 (Mandating-quit-information-messages-inside-tobacco-packs-2.txt), proves component 1. £1.5 (local note: L1795, paragraph 122)

```text
Tobacco duty rates set by HMRC are set out below
```

Evidence 3: document Doc 4 (Mandating-quit-information-messages-inside-tobacco-packs-2.txt), proves component 1. £1.5 (local note: L1799, duty table)

```text
Duty rate (October 2021)
```

Evidence 4: document Doc 4 (Mandating-quit-information-messages-inside-tobacco-packs-2.txt), proves component 1. £1.5 (local note: L1805, duty table)

```text
£262.90 per 1,000 cigarettes plus 16.5% of retail price
```

Evidence 5: document Doc 4 (Mandating-quit-information-messages-inside-tobacco-packs-2.txt), proves component 1. £1.5 (local note: L1806, duty table)

```text
£347.86 per 1,000 cigarettes (MET)
```

Evidence 6: document Doc 4 (Mandating-quit-information-messages-inside-tobacco-packs-2.txt), proves component 1. £1.5 (local note: L1811, paragraph 123)

```text
which is above the MET threshold
```

### Necessary documents

- Tick Doc 4 (Mandating-quit-information-messages-inside-tobacco-packs-2.txt), role: Answer component
- Tick Doc 2 (Creating-a-smokefree-generation-and-tackling-youth-vaping-2.txt), role: Answer component

Leave unticked: Doc 1 (Creating-a-smokefree-generation-and-tackling-youth-vaping.txt), Doc 3 (Mandating-quit-information-messages-inside-tobacco-packs.txt), Doc 5 (Mandating-quit-information-messages-inside-tobacco-packs-3.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Unit normalization

Leave unticked: Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

#### Failure mode 3

Trap: Linking across documents

How a careless solver fails: Picks the wrong entity or section

#### Why these are traps (at most 50 words)

```text
Doc 4 paragraph 123's £7.98 is an average-priced pack's duty: £0.5. Doc 1's £7.87 is the consultation's, not the response's: £0.9. Taking Doc 1's £7.87 as the impact assessment's figure gives £0.6. The minimum is Doc 4's MET, £347.86 per 1,000 (£6.9572 a pack): £1.5.
```

(45 / 50 words.)
