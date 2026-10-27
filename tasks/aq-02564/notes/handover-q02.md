# aq-02564 q02 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02564 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 27f12de0085381a8970dd40a7202f9e40ea0e8509dbaf5b70ecc20244391e98f: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D05 = Doc 5, D06 = Doc 6.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
A hosting broker has 5,000 users of its own on each of EDGX Top and BYX Top, and two hosted subscribers: one takes only EDGX Top, with 4,000 users; the other has 4,000 EDGX Top and 10,500 BYX Top users. All users are non-professional. What is the host's monthly bill for the two feeds?
```

### Number of asks

1 ask

### Gold answer

```text
$2,375
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 5, EDGX's hosted program): EDGX's program covers the EDGX Top Data Feed, and its cap is 10,000 users of that feed. Both hosted subscribers take EDGX Top and are within the 10,000 maximum, so the host, which provides the data to at least one External Hosted Subscriber, keeps the credit of its EDGX Distribution Fee. The host is responsible for payment of all data fees of its hosted subscribers, and each one's EDGX Top fee is a set monthly fee of $750 in lieu of Non-Professional User fees.

Step 2. Source input (Doc 5, footnote 12): the standard EDGX Top Non-Professional User fee, which the host pays for its own users, is 0.10 dollars per user a month; footnote 12 prices 10,000 users at $1,000.

Step 3. Calculation (Doc 5): the host's EDGX Top bill is its own 5,000 users' fees plus the two set fees: 5,000 × 0.10 + 750 + 750 = 2,000 dollars a month.

Step 4. Source input (Doc 6, BYX's hosted program): BYX's program is a separate program for the BYX Top Data Feed, with its own cap of 10,000 users of that feed. The first subscriber receives no BYX data, so it is not a hosted subscriber of a BYX product. The second has more than the 10,000 maximum on BYX Top, so it is no longer eligible and must license BYX Top directly with the Exchange. The host stays eligible only so long as it has at least one External Hosted Subscriber, and here it has none under BYX's program, so it gets no BYX credit and pays the Distribution Fee it is normally responsible for under the existing Small Retail Broker Program, $250/month for the BYX Top Data Feed, with no BYX set fee on its bill.

Step 5. Source input (Doc 6, footnote 12): the standard BYX Top Non-Professional User fee is 0.025 dollars per user a month; footnote 12 prices 10,000 users at $250.

Step 6. Calculation (Doc 6): the host's BYX Top bill is the Distribution Fee plus its own 5,000 users' fees: 250 + 5,000 × 0.025 = 375 dollars a month.

Step 7. Calculation (Doc 5 and Doc 6): the host's combined monthly bill for the two feeds: 2,000 + 375 = 2,375 dollars, exact.
```

### Answer components

Component 1

```text
$2,375
```

### Evidence

Evidence 1: document Doc 5 (fr_2025_21640.txt), proves component 1. $2,375 (local note: host credit, L73)

```text
a Hosting Small Retail Broker Distributor providing the data to at least one External Hosted Subscriber would be eligible for a credit of its Distribution Fee (a credit of $750/month for EDGX Top Data Feed and a credit of $3,500/month for Cboe One Summary Feed) that it is normally responsible for under the existing Small Retail Broker Program
```

Evidence 2: document Doc 5 (fr_2025_21640.txt), proves component 1. $2,375 (local note: set fee, L74)

```text
it shall be a set monthly fee of $750 for EDGX Top
```

Evidence 3: document Doc 5 (fr_2025_21640.txt), proves component 1. $2,375 (local note: host pays, L70)

```text
ultimately the Hosting Small Retail Broker Distributor is responsible for payment of all data fees
```

Evidence 4: document Doc 5 (fr_2025_21640.txt), proves component 1. $2,375 (local note: cap per feed, footnote 12, L77)

```text
capped at 10,000 users for Cboe One Summary Feed and 10,000 for EDGX Top Data Feed
```

Evidence 5: document Doc 5 (fr_2025_21640.txt), proves component 1. $2,375 (local note: footnote 12, L77)

```text
10,000 Users x 0.10/Non-Professional User = $1,000
```

Evidence 6: document Doc 6 (fr_2025_21890.txt), proves component 1. $2,375 (local note: hosted subscriber defined, footnote 11, L70)

```text
An External Hosted Subscriber of an Exchange Market Data product is a Distributor that receives the Exchange Market Data product from an External Distributor through a hosted display solution
```

Evidence 7: document Doc 6 (fr_2025_21890.txt), proves component 1. $2,375 (local note: cap per feed, footnote 12, L79)

```text
capped at 10,000 users for Cboe One Summary Feed and 10,000 for BYX Top Data Feed
```

Evidence 8: document Doc 6 (fr_2025_21890.txt), proves component 1. $2,375 (local note: over the cap, L75)

```text
shall no longer be eligible for the program and will be required to directly license with the Exchange for the Applicable Feed
```

Evidence 9: document Doc 6 (fr_2025_21890.txt), proves component 1. $2,375 (local note: host eligibility, L76)

```text
the Hosting Small Retail Broker Distributor shall continue to remain eligible for this Program so long as it has at least one External Hosted Subscriber
```

Evidence 10: document Doc 6 (fr_2025_21890.txt), proves component 1. $2,375 (local note: host credit, L75)

```text
a Hosting Small Retail Broker providing the data to at least one External Hosted Subscriber would be eligible for a credit of its Distribution Fee (a credit of $250/month for BYX Top Data Feed and a credit of $3,500/month for Cboe One Summary Feed) that it is normally responsible for under the existing Small Retail Broker Program
```

Evidence 11: document Doc 6 (fr_2025_21890.txt), proves component 1. $2,375 (local note: footnote 12, L79)

```text
10,000 Users x 0.025/Non-Professional User = $250
```

### Necessary documents

- Tick Doc 5 (fr_2025_21640.txt), role: Answer component
- Tick Doc 6 (fr_2025_21890.txt), role: Answer component

Leave unticked: Doc 1 (fr_2024_28745.txt), Doc 2 (fr_2024_28738.txt), Doc 3 (fr_2024_30509.txt), Doc 4 (fr_2025_00811.txt), Doc 7 (fr_2026_16290.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Entity resolution, Aggregation

Leave unticked: Temporal alignment, Unit normalization

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Picks the wrong entity or section

#### Failure mode 2

Trap: Wrong jurisdiction or scope

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Linking: Doc 6's BYX credit needs a BYX hosted subscriber; counting Doc 5's EDGX subscribers keeps it, giving $2,125. Scope: Doc 6's 10,000 cap removes the second subscriber from BYX's program only; dropping it from EDGX's too gives $1,625. The gold does neither.
```

(43 / 50 words.)
