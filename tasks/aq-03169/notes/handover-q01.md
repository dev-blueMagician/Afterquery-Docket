# aq-03169 q01 hand-over

Generated 2026-10-12 by `python tools/check_questions.py tasks/aq-03169 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 2, difficulty_target medium, origin claude.
- tested_sha256 4a2e25666dd4c8f96b34653454b061f638bb48ff3c6475669d991795739a9146: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D06 = Doc 6.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 3: Doc 2 doesn't mention 11. Doc 2 prints it first at character 42,019, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Under ICAEW's individual cap on each Big Four firm, how many FTSE 350 audits could the four hold in total, and how many years of tender wins, at the yearly rate Deloitte's five-year market-share target assumes, would bring them within that total, to the nearest whole year?
```

### Number of asks

2 asks

### Gold answer

```text
260 audits and 7 years
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 6, reply on how a cap should be measured): besides a collective cap, ICAEW describes an individual one, under which each Big Four firm could be restricted to auditing 65 of the FTSE 350 companies.
Step 2. Calculation (Doc 6): with every Big Four firm at that cap, the four together could audit 4 × 65 = 260 companies, which is the first answer.
Step 3. Source input (Doc 2, appendix reply on whether a cap's benefits could be realised): firms outside the four largest currently perform 11 audits of the FTSE 350. To hold a 20% share in the next five years they would need to win about 60 tenders.
Step 4. Calculation (Doc 2 and Doc 6): the Big Four audit the rest of the index today: 350 − 11 = 339 companies.
Step 5. Calculation (Doc 2 and Doc 6): to come within the cap they would have to give up 339 − 260 = 79 audits, each one a tender won by another firm.
Step 6. Calculation (Doc 2): the target's wins spread over its five years give a yearly rate of 60 / 5 = 12 wins.
Step 7. Calculation (Doc 2 and Doc 6): six years at that rate bring 12 × 6 = 72 wins.
Step 8. Final answer (Doc 2 and Doc 6): 79 − 72 = 7 wins are still missing after six years, more than half of one year's 12, so the time needed is closer to seven years than to six: 7 years to the nearest whole year. With the cap total from Step 2, the answer is 260 audits and 7 years.
```

### Answer components

Component 1

```text
260 audits
```

Component 2

```text
7 years
```

### Evidence

Evidence 1: document Doc 6 (cma_audit_itc_responses_icaew.txt), proves component 1. 260 audits (local note: Q19, para 87, L282)

```text
each Big Four firm could be restricted to auditing 65 of the FTSE 350 companies
```

Evidence 2: document Doc 6 (cma_audit_itc_responses_icaew.txt), proves component 2. 7 years (local note: Q19, para 87, L282)

```text
each Big Four firm could be restricted to auditing 65 of the FTSE 350 companies
```

Evidence 3: document Doc 2 (cma_audit_itc_responses_deloitte.txt), proves component 2. 7 years (local note: appendix 20.4, L616)

```text
Firms outside the four largest currently perform 11 audits of the FTSE 350 today
```

Evidence 4: document Doc 2 (cma_audit_itc_responses_deloitte.txt), proves component 2. 7 years (local note: appendix 20.4, L616)

```text
in order to hold a 20% share of the FTSE 350 audit market in the next five years, firms other than the four largest would need to win about 60 tenders
```

### Necessary documents

- Tick Doc 2 (cma_audit_itc_responses_deloitte.txt), role: Answer component
- Tick Doc 6 (cma_audit_itc_responses_icaew.txt), role: Answer component

Leave unticked: Doc 1 (cma_audit_itc_responses_bdo.txt), Doc 3 (cma_audit_itc_responses_ey.txt), Doc 4 (cma_audit_itc_responses_grant_thornton.txt), Doc 5 (cma_audit_itc_responses_hermes.txt), Doc 7 (cma_audit_itc_responses_moore_stephens.txt), Doc 8 (cma_audit_itc_responses_nexia_smith_williamson.txt), Doc 9 (cma_audit_itc_responses_standard_life.txt), Doc 10 (cma_audit_itc_responses_uss.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization

Leave unticked: Temporal alignment, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Part vs total: Doc 2 says other firms already perform 11 FTSE 350 audits; treating the whole index as the Big Four's gives 90 audits to shed and 8 years. Look-alike measure: Doc 6's summary gives a collective cap of around 60%: 210 audits, 11 years. The gold sheds 79.
```

(50 / 50 words.)
