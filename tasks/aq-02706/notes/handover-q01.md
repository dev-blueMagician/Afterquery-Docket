# aq-02706 q01 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02706 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 258ac5e3867ea6dc2b20499fec7818b3d4eee079e92000a7b92e7aa257dabe1e: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D04 = Doc 4, D07 = Doc 7.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Two banks, one national, one State nonmember, are each well capitalized, composite-rated 2, under $30 billion in assets and under its regulator's fair-lending consent order. Each moves its main office and 12 branches to other in-State cities. Under the OCC's 2026 licensing rule and FDIC's 2025 branch proposal, how many moves qualify for expedited treatment?
```

### Number of asks

1 ask

### Gold answer

```text
14 moves
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 7, definition of a covered community bank): a national bank qualifies if it has less than $30 billion in total assets, is well capitalized, and is not subject to a cease and desist order, consent order or formal written agreement that requires action to improve its financial condition. The OCC declined a commenter's request to exclude banks under fair lending orders. A fair-lending consent order does not concern financial condition, so the national bank is a covered community bank; the definition has no rating test.

Step 2. Source input (Doc 7, expedited review provisions): the rule adds covered community banks to the expedited review of applications to establish or relocate a branch and of applications to relocate a main office. Every move by the national bank qualifies.

Step 3. Calculation (Doc 7): the national bank's main-office move plus its branch moves: 1 + 12 = 13 moves.

Step 4. Source input (Doc 4, eligible depository institution): a filing to establish a branch gets expedited processing only from an eligible depository institution, which may not be subject to a consent order with its primary Federal regulator or chartering authority. The State nonmember bank is under one, so it is not eligible.

Step 5. Source input (Doc 4, definition of branch relocation): a branch relocation is a move within the same immediate neighborhood, and moving a branch outside its immediate neighborhood is the closing of a branch and the establishment of a new branch. The State bank's branch moves to other cities are therefore branch establishments by a bank that is not eligible. They get standard processing, so none of them qualifies.

Step 6. Source input (Doc 4, proposed expedited processing for relocations): an intrastate main office relocation gets expedited processing if the bank's composite rating is 3 or better, regardless of the other eligibility criteria. The State bank is rated 2, so its main-office move qualifies: 1 move.

Step 7. Calculation (Doc 4 and Doc 7): the two banks together: 13 + 1 = 14 moves qualify for expedited treatment.
```

### Answer components

Component 1

```text
14 moves
```

### Evidence

Evidence 1: document Doc 7 (fr_2026_04275.txt), proves component 1. 14 moves (local note: Sec. 5.3 definition, paragraph (1)(i), L284)

```text
Has less than $30 billion in total assets, as reported in the national bank's or Federal savings association's Call Report, and is not an affiliate of a depository institution or foreign bank with $30 billion or more in total assets
```

Evidence 2: document Doc 7 (fr_2026_04275.txt), proves component 1. 14 moves (local note: Sec. 5.3 definition, paragraph (1)(iii), L286)

```text
Is not subject to a cease and desist order, a consent order, or a formal written agreement, that requires action to improve the financial condition of the national bank or Federal savings association unless otherwise informed in writing by the OCC.
```

Evidence 3: document Doc 7 (fr_2026_04275.txt), proves component 1. 14 moves (local note: rejected commenter request, L77)

```text
the bank is not the subject of any fair housing, fair lending, or consumer protection orders, agreements, or investigations
```

Evidence 4: document Doc 7 (fr_2026_04275.txt), proves component 1. 14 moves (local note: OCC response, L91)

```text
the OCC does not believe expanding the scope of enforcement actions is necessary or appropriate because enforcement actions concerning specific laws are generally not relevant to many types of applications
```

Evidence 5: document Doc 7 (fr_2026_04275.txt), proves component 1. 14 moves (local note: branch applications, L108)

```text
Twelve CFR 5.30(f)(6) provides for expedited review of applications for establishment or relocation of a branch by an eligible bank.
```

Evidence 6: document Doc 7 (fr_2026_04275.txt), proves component 1. 14 moves (local note: main office applications, L113)

```text
Twelve CFR 5.40(c)(4) provides for expedited review of applications to relocate a main office or home office of an eligible bank or eligible savings association, respectively.
```

Evidence 7: document Doc 7 (fr_2026_04275.txt), proves component 1. 14 moves (local note: extension to covered community banks, L113)

```text
The OCC proposed adding covered community bank or covered community savings association to each of these provisions referencing an eligible bank or eligible savings association.
```

Evidence 8: document Doc 4 (fr_2025_13568.txt), proves component 1. 14 moves (local note: eligible depository institution, test (5), L92)

```text
(5) is not subject to a cease and desist order, consent order, prompt corrective action directive, written agreement, memorandum of understanding, or other administrative agreement with its primary Federal regulator or chartering authority.
```

Evidence 9: document Doc 4 (fr_2025_13568.txt), proves component 1. 14 moves (local note: proposed Sec. 303.43(a), L578)

```text
Filings to establish a branch by an eligible depository institution as defined in Sec. 303.2(r) will be acknowledged in writing by the FDIC and will receive expedited processing.
```

Evidence 10: document Doc 4 (fr_2025_13568.txt), proves component 1. 14 moves (local note: Sec. 303.41(b), L544)

```text
Moving a branch to a location outside its immediate neighborhood is considered the closing of an existing branch and the establishment of a new branch.
```

Evidence 11: document Doc 4 (fr_2025_13568.txt), proves component 1. 14 moves (local note: proposed Sec. 303.43(b), L581)

```text
Filings for intrastate branch relocations or intrastate main office relocations will be acknowledged in writing by the FDIC and will receive expedited processing if the bank received an FDIC-assigned composite rating of 3 or better under the Uniform Financial Institutions Rating System as a result of its most recent federal or state examination.
```

Evidence 12: document Doc 4 (fr_2025_13568.txt), proves component 1. 14 moves (local note: preamble on Sec. 303.43(b), L244)

```text
Expedited processing would apply under 12 CFR 303.43(b) regardless of whether the institution satisfies the other criteria in 12 CFR 303.2(r) for an eligible depository institution.
```

### Necessary documents

- Tick Doc 4 (fr_2025_13568.txt), role: Answer component
- Tick Doc 7 (fr_2026_04275.txt), role: Answer component

Leave unticked: Doc 1 (fr_2024_02663.txt), Doc 2 (fr_2024_21560.txt), Doc 3 (fr_2024_22189.txt), Doc 5 (fr_2025_13589.txt), Doc 6 (fr_2026_03818.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Wrong jurisdiction or scope

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Wrong jurisdiction or scope: Doc 4's composite-rating track covers main-office moves and branch moves within the same immediate neighborhood; stretching it to branches moved to other cities gives 26. Doc 4's any-consent-order bar applied to the national bank gives 1; Doc 7 bars only financial-condition orders, so 14.
```

(48 / 50 words.)
