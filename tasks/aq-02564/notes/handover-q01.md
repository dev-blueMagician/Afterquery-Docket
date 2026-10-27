# aq-02564 q01 hand-over

Generated 2026-10-09 by `python tools/check_questions.py tasks/aq-02564 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 d584a570459b55873345f63529150ee93b6af74b10bf4b24c600e5b881664aaa: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D05 = Doc 5, D06 = Doc 6.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
How much lower are a hosted subscriber's total monthly EDGX Top and BYX Top fees under the hosted programs than under the existing small-retail-broker programs, at 10,000 non-professional users?
```

### Number of asks

1 ask

### Gold answer

```text
$1,400
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 5, existing small retail broker program): EDGX charges a discounted Distribution Fee of $750/month for the EDGX Top Data Feed. Under the existing structure a hosted subscriber is assessed that fee, and it is in addition to the standard Professional and Non-Professional User fees.

Step 2. Source input (Doc 5, hosted program): the hosted subscriber's Distribution Fee is waived (a credit of $750/month for the EDGX Top Data Feed), and in lieu of the Non-Professional User fees it pays a set monthly fee of $750 for EDGX Top. Professional User fees remain the same under both programs, so they cancel. Both programs allow no more than 10,000 Non-Professional Data Users: the hosted program's cap, and the existing program's maximum raised from 5,000 to 10,000 by the same filing.

Step 3. Source input (Doc 5, footnote 12): the standard EDGX Top Non-Professional User fee is 0.10 dollars per user a month; footnote 12 prices 10,000 users at $1,000.

Step 4. Calculation (Doc 5): EDGX Top fees for 10,000 non-professional users fall by the waived Distribution Fee plus the replaced user fees, minus the set fee: 750 + 1,000 - 750 = 1,000 dollars a month.

Step 5. Source input (Doc 6, existing small retail broker program): BYX charges a discounted Distribution Fee of $250/month for the BYX Top Data Feed, in addition to the standard Professional and Non-Professional User fees.

Step 6. Source input (Doc 6, hosted program): the hosted subscriber's BYX Top Distribution Fee is waived (a credit of $250/month), and in lieu of the Non-Professional User fees it pays a set monthly fee of $100 for BYX Top. Professional User fees remain the same, and the same 10,000-user limits apply.

Step 7. Source input (Doc 6, footnote 12): the standard BYX Top Non-Professional User fee is 0.025 dollars per user a month; footnote 12 prices 10,000 users at $250.

Step 8. Calculation (Doc 6): BYX Top fees for 10,000 non-professional users fall by 250 + 250 - 100 = 400 dollars a month.

Step 9. Calculation (Doc 5 and Doc 6): combined monthly reduction for the EDGX Top and BYX Top feeds: 1,000 + 400 = 1,400 dollars, exact.
```

### Answer components

Component 1

```text
$1,400
```

### Evidence

Evidence 1: document Doc 5 (fr_2025_21640.txt), proves component 1. $1,400 (local note: existing program, L48)

```text
This program provides a discounted Distribution Fee of $750/month for EDGX Top Data Feed
```

Evidence 2: document Doc 5 (fr_2025_21640.txt), proves component 1. $1,400 (local note: existing structure, L62)

```text
both the External Hosted Subscriber and the Hosting Small Retail Broker Distributor are assessed the standard discounted Distribution Fee (and for Cboe One Summary, the discounted Data Consolidation Fee) under the existing Small Retail Broker Program. These fees are in addition to the standard Professional and Non-Professional User fees.
```

Evidence 3: document Doc 5 (fr_2025_21640.txt), proves component 1. $1,400 (local note: hosted program, L74)

```text
the External Hosted Subscriber shall also receive a waiver of the Distribution Fee (a credit of $750/month for EDGX Top Data Feed
```

Evidence 4: document Doc 5 (fr_2025_21640.txt), proves component 1. $1,400 (local note: hosted program, L74)

```text
it shall be a set monthly fee of $750 for EDGX Top
```

Evidence 5: document Doc 5 (fr_2025_21640.txt), proves component 1. $1,400 (local note: footnote 12, L77)

```text
10,000 Users x 0.10/Non-Professional User = $1,000
```

Evidence 6: document Doc 5 (fr_2025_21640.txt), proves component 1. $1,400 (local note: cap raised, L81)

```text
increase the number of Non- Professional Data User maximum from 5,000 to 10,000
```

Evidence 7: document Doc 6 (fr_2025_21890.txt), proves component 1. $1,400 (local note: existing program, L50)

```text
This program provides a discounted Distribution Fee of $250/month for BYX Top Data Feed
```

Evidence 8: document Doc 6 (fr_2025_21890.txt), proves component 1. $1,400 (local note: hosted program, L75)

```text
the External Hosted Subscriber shall also receive a waiver of the Distribution Fee (a credit of $250/month for BYX Top Data Feed
```

Evidence 9: document Doc 6 (fr_2025_21890.txt), proves component 1. $1,400 (local note: hosted program, L75)

```text
it shall be a set monthly fee of $100 for BYX Top
```

Evidence 10: document Doc 6 (fr_2025_21890.txt), proves component 1. $1,400 (local note: footnote 12, L79)

```text
10,000 Users x 0.025/Non-Professional User = $250
```

### Necessary documents

- Tick Doc 5 (fr_2025_21640.txt), role: Answer component
- Tick Doc 6 (fr_2025_21890.txt), role: Answer component

Leave unticked: Doc 1 (fr_2024_28745.txt), Doc 2 (fr_2024_28738.txt), Doc 3 (fr_2024_30509.txt), Doc 4 (fr_2025_00811.txt), Doc 7 (fr_2026_16290.txt)

### Reasoning tags

Tick: Cross-document join, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Linking across documents

How a careless solver fails: Picks the wrong entity or section

#### Why these are traps (at most 50 words)

```text
Look-alike: Doc 5 and Doc 6 footnote 12 print "maximum, savings" of $250 and $150, user fees only, giving $400; the gold adds the waived Distribution Fees. Linking: using Doc 5's EDGX figures for BYX gives $2,000; each feed takes its own notice's figures.
```

(44 / 50 words.)
