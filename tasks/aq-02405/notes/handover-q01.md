# aq-02405 q01 hand-over

Generated 2026-10-09 by `python tools/check_questions.py tasks/aq-02405 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 441a66f47acf7fd1b48f78471d90dd09fb3d9417cf3241f836e6d46bcb771a4e: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 3, D06 = Doc 6.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Recomputing all of ATF's 2026 proposals' savings at $26.10 an hour, how much would an individual save per paper Form 1, to the nearest cent?
```

### Number of asks

1 ask

### Gold answer

```text
$48.05
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 6, fingerprint cost savings): an individual NFA applicant who files on paper would submit one fingerprint card instead of two, a per-application savings of 18 dollars.

Step 2. Source fact (Doc 6, photograph cost savings): a paper filer who sends a copy of a photo identification document instead of a 2 x 2 photograph saves 17 dollars per application.

Step 3. Source fact (Doc 6, time estimates): NFA individual applicants who submit paper applications save up to 0.25 hours by no longer obtaining a paper photograph.

Step 4. Source fact (Doc 3, benefits and savings): removing the copy for the chief law enforcement officer saves the time it takes an individual to copy the form, 0.25 hours per application; every Form 1 applicant now forwards that copy.

Step 5. Calculation (from Steps 3 and 4; Doc 6 and Doc 3): hours saved per paper Form 1: 0.25 + 0.25 = 0.5 hours.

Step 6. Calculation (from Step 5 and the question's hourly value of 26.10 dollars, also printed as the unrounded leisure wage in Doc 6 and Doc 3): value of the time saved: 0.5 * 26.10 = 13.05 dollars.

Step 7. Calculation (from Steps 1 and 2; Doc 6): cash saved: 18 + 17 = 35 dollars.

Step 8. Calculation (from Steps 6 and 7; Doc 6 and Doc 3): total saved per paper Form 1: 35 + 13.05 = 48.05 dollars, which needs no rounding to the nearest cent.
```

### Answer components

Component 1

```text
$48.05
```

### Evidence

Evidence 1: document Doc 6 (fr_2026_13587.txt), proves component 1. $48.05 (local note: L200, Fingerprint Cost Savings)

```text
resulting in a per-application savings of $18 for this two percent of applicants
```

Evidence 2: document Doc 6 (fr_2026_13587.txt), proves component 1. $48.05 (local note: L220, Photograph Cost Savings)

```text
could realize a capital savings of $17 per application
```

Evidence 3: document Doc 6 (fr_2026_13587.txt), proves component 1. $48.05 (local note: L253, time estimates)

```text
up to 0.25 hours for GCA individual/RP applicants and NFA individual applicants who submit paper applications and would no longer have to obtain paper 2'' x 2'' photographs
```

Evidence 4: document Doc 3 (fr_2026_08912.txt), proves component 1. $48.05 (local note: L141, Benefits and Savings)

```text
ATF estimates that it would take 15 minutes (0.25 hours) for an individual to copy the relevant form prior to submitting the original to ATF
```

Evidence 5: document Doc 3 (fr_2026_08912.txt), proves component 1. $48.05 (local note: L66, Application To Make a Firearm)

```text
all applicants and responsible persons must currently forward a complete copy of Form 1
```

### Necessary documents

- Tick Doc 3 (fr_2026_08912.txt), role: Answer component
- Tick Doc 6 (fr_2026_13587.txt), role: Answer component

Leave unticked: Doc 1 (fr_2024_28711.txt), Doc 2 (fr_2026_08918.txt), Doc 4 (fr_2026_09157.txt), Doc 5 (fr_2026_09182.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization, Aggregation

Leave unticked: Temporal alignment, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Picks the wrong entity or section

#### Failure mode 2

Trap: Document convention

How a careless solver fails: Rounding, scale or sign

#### Why these are traps (at most 50 words)

```text
Part vs total: Doc 6's paper-individual savings ($42, or $41.53 at $26.10) is one proposal's part; Doc 3's CLEO-copy time adds 0.25 hours. Document convention: both documents round $6.50 time values up to $7, so adding the printed $42 and $7 gives $49. Gold: $48.05.
```

(45 / 50 words.)
