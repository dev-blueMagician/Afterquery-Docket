# aq-02102 q02 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-02102 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 3f07aa5c9392794bb17c691ceb94cf2b41fa0007449e4d717022783f44a99cd5: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 4, D05 = Doc 5.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN list-contract: the answer lists 5 items; say how many to expect, or ask for one value (form: list contract)
  - WARN single-passage: one passage of D03 holds the answer: '...tuc) unions - pcs (public and commercial services union) - prospect - fda - gmb - poa uk (prison officers' association) - unite non-affiliated...' (rules 2-3)
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Which unions accepted the 2016 Civil Service compensation offer and were engaged during the 2023 Civil Service McCloud consultation without written replies, if any? Any order.
```

### Number of asks

1 ask

### Gold answer

```text
FDA, GMB, Unite, NCOA, Prison Governors' Association
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 5, paragraph 1.3): the government's offer of 26 September 2016 on the Civil Service Compensation Scheme was agreed by eight of the ten unions: FDA, Prospect, GMB, UNISON, Unite, NCOA, the Defence Police Federation and PGA.

Step 2. Source fact (Doc 5, paragraph 1.4): the other two, the Prison Officers Association (POA) and the Public and Commercial Services Union (PCS), did not agree it.

Step 3. Source fact (Doc 4, paragraph 2.11): the unions engaged during the 2023 consultation were the NTUC unions PCS, Prospect, FDA, GMB, POA UK (Prison Officers' Association) and Unite, and the non-affiliated DPF (Defence Police Federation), the ISU, NCOA and the Prison Governors' Association.

Step 4. Source fact (Doc 4, paragraph 3.9, Table 2 and Annex A): only three unions sent written responses: Prospect, PCS and the Defence Police Federation. The other two responding organisations were the Civil Service Pensioners Alliance and Pen-gage, which are not unions.

Step 5. Matching (Doc 4 and Doc 5): of the ten engaged unions, seven had accepted the 2016 offer: FDA, Prospect, GMB, Unite, NCOA, the Defence Police Federation and the Prison Governors' Association, which is Doc 5's PGA (Doc 5's POA is the Prison Officers Association). PCS and POA UK refused it, and the ISU was not one of the ten unions party to it. UNISON accepted but was not engaged in 2023.

Step 6. Exclusion (Doc 4): Prospect and the Defence Police Federation responded in writing, so the unions left are FDA, GMB, Unite, NCOA and the Prison Governors' Association.

Decoy: POA UK, the Prison Officers' Association, was engaged and sent no written reply, but it refused the 2016 offer; it is not Doc 5's PGA. Prospect and the Defence Police Federation accepted the offer and were engaged, but replied in writing.
```

### Answer components

Component 1

```text
FDA
```

Component 2

```text
GMB
```

Component 3

```text
Unite
```

Component 4

```text
NCOA
```

Component 5

```text
Prison Governors' Association
```

### Evidence

Evidence 1: document Doc 5 (Consultation-on-reform-of-the-Civil-Service-Compensation.txt), proves component 1. FDA (local note: L65, paragraph 1.3)

```text
The offer was ultimately agreed with eight out of ten unions (FDA, Prospect, GMB, UNISON, Unite, NCOA, the Defence Police Federation and PGA).
```

Evidence 2: document Doc 5 (Consultation-on-reform-of-the-Civil-Service-Compensation.txt), proves component 2. GMB (local note: L65, paragraph 1.3)

```text
The offer was ultimately agreed with eight out of ten unions (FDA, Prospect, GMB, UNISON, Unite, NCOA, the Defence Police Federation and PGA).
```

Evidence 3: document Doc 5 (Consultation-on-reform-of-the-Civil-Service-Compensation.txt), proves component 3. Unite (local note: L65, paragraph 1.3)

```text
The offer was ultimately agreed with eight out of ten unions (FDA, Prospect, GMB, UNISON, Unite, NCOA, the Defence Police Federation and PGA).
```

Evidence 4: document Doc 5 (Consultation-on-reform-of-the-Civil-Service-Compensation.txt), proves component 4. NCOA (local note: L65, paragraph 1.3)

```text
The offer was ultimately agreed with eight out of ten unions (FDA, Prospect, GMB, UNISON, Unite, NCOA, the Defence Police Federation and PGA).
```

Evidence 5: document Doc 5 (Consultation-on-reform-of-the-Civil-Service-Compensation.txt), proves component 5. Prison Governors' Association (local note: L65, paragraph 1.3)

```text
The offer was ultimately agreed with eight out of ten unions (FDA, Prospect, GMB, UNISON, Unite, NCOA, the Defence Police Federation and PGA).
```

Evidence 6: document Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), proves component 1. FDA (local note: L137, paragraph 2.11)

```text
Unions engaged during the consultation process are listed below:
```

Evidence 7: document Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), proves component 2. GMB (local note: L137, paragraph 2.11)

```text
Unions engaged during the consultation process are listed below:
```

Evidence 8: document Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), proves component 3. Unite (local note: L137, paragraph 2.11)

```text
Unions engaged during the consultation process are listed below:
```

Evidence 9: document Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), proves component 4. NCOA (local note: L137, paragraph 2.11)

```text
Unions engaged during the consultation process are listed below:
```

Evidence 10: document Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), proves component 5. Prison Governors' Association (local note: L137, paragraph 2.11)

```text
Unions engaged during the consultation process are listed below:
```

Evidence 11: document Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), proves component 4. NCOA (local note: L159, paragraph 2.11)

```text
NCOA (National Crime Officers Association)
```

Evidence 12: document Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), proves component 5. Prison Governors' Association (local note: L161, paragraph 2.11)

```text
Prison Governors’ Association
```

Evidence 13: document Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), proves component 1. FDA (local note: L207, Table 2)

```text
Unions and other representative bodies: Prospect PCS Defence Police Federation
```

Evidence 14: document Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), proves component 2. GMB (local note: L207, Table 2)

```text
Unions and other representative bodies: Prospect PCS Defence Police Federation
```

Evidence 15: document Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), proves component 3. Unite (local note: L207, Table 2)

```text
Unions and other representative bodies: Prospect PCS Defence Police Federation
```

Evidence 16: document Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), proves component 4. NCOA (local note: L207, Table 2)

```text
Unions and other representative bodies: Prospect PCS Defence Police Federation
```

Evidence 17: document Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), proves component 5. Prison Governors' Association (local note: L207, Table 2)

```text
Unions and other representative bodies: Prospect PCS Defence Police Federation
```

### Necessary documents

- Tick Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), role: Answer component
- Tick Doc 5 (Consultation-on-reform-of-the-Civil-Service-Compensation.txt), role: Answer component

Leave unticked: Doc 1 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service.txt), Doc 2 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service-2.txt), Doc 3 (Civil-Service-Pensions-2015-Remedy-McCloud-consultation.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Entity resolution

Leave unticked: Temporal alignment, Unit normalization, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Wrong members in a list

#### Failure mode 2

Trap: Look-alike company

How a careless solver fails: Picks the wrong entity or section

#### Failure mode 3

Trap: Part vs total

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Doc 5 lists "PGA" only by acronym. Doc 4's Prison Governors' Association is that union, so dropping it leaves four. Doc 4's POA UK is the Prison Officers' Association, which refused (Doc 5). Prospect and DPF were engaged but wrote (Doc 4 Table 2), so including them gives seven.
```

(49 / 50 words.)
