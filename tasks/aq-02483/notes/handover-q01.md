# aq-02483 q01 hand-over

Generated 2026-10-09 by `python tools/check_questions.py tasks/aq-02483 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 8fec74e3febe96f4dbbe2e23bacbf34cbd4fb461373b0efd2b50b701b676f08a: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D06 = Doc 6.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
The newest federal CCR amendments reflected in Wyoming's and Wisconsin's rules were published how many days apart?
```

### Number of asks

1 ask

### Gold answer

```text
76 days
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, Wyoming Partial Program): Wyoming's rules "adopt the Federal CCR regulations promulgated through December 14, 2020". That date is the cutoff of the federal version Wyoming adopted.
Step 2. Source input (Doc 2, Background): EPA lists its amendments to 40 CFR part 257, subpart D as August 5, 2016 (81 FR 51802), July 30, 2018 (83 FR 36435), August 28, 2020 (85 FR 53516), November 12, 2020 (85 FR 72506), May 8, 2024 (89 FR 38950) and November 8, 2024 (89 FR 88650). None is dated December 14, 2020.
Step 3. Derived (Doc 2): the newest amendment promulgated on or before the December 14, 2020 cutoff is the one published November 12, 2020 (85 FR 72506); the next, May 8, 2024, came after it. So the newest federal CCR amendment reflected in Wyoming's rules was published November 12, 2020.
Step 4. Source input (Doc 6, Wisconsin Partial Program and Background): Wisconsin's CCR regulations "reflect 40 CFR part 257, subpart D, as amended through August 28, 2020, for CCR landfills", and EPA's list in Doc 6 dates an amendment August 28, 2020 (85 FR 53516). So the newest federal CCR amendment reflected in Wisconsin's rules was published August 28, 2020.
Step 5. Calculation (Doc 2 and Doc 6): counting 60 days on from August 28, 2020 reaches October 27, 2020 (3 days to the end of August, 30 in September and 27 in October).
Step 6. Calculation (Doc 2 and Doc 6): from October 27 to November 12, 2020, the 4 remaining days of October and 12 of November: 4 + 12 = 16
Step 7. Calculation (Doc 2 and Doc 6): 60 + 16 = 76 days between the two publication dates.
Step 8. Look-alike check (Doc 2): December 14, 2020 is a cutoff for Wyoming's adopted version, not the date of any amendment, so measuring from it would overstate the gap.
```

### Answer components

Component 1

```text
76
```

### Evidence

Evidence 1: document Doc 2 (fr_2025_16801.txt), proves component 1. 76 (local note: Wyoming Partial Program, L280)

```text
The WDEQ's rules adopt the Federal CCR regulations promulgated through December 14, 2020.
```

Evidence 2: document Doc 2 (fr_2025_16801.txt), proves component 1. 76 (local note: Background, dated amendment list, L127)

```text
August 28, 2020 (85 FR 53516), November 12, 2020 (85 FR 72506), May 8, 2024 (89 FR 38950)
```

Evidence 3: document Doc 6 (fr_2026_18552.txt), proves component 1. 76 (local note: Wisconsin Partial Program, L308)

```text
Wisconsin's CCR regulations reflect 40 CFR part 257, subpart D, as amended through August 28, 2020, for CCR landfills
```

Evidence 4: document Doc 6 (fr_2026_18552.txt), proves component 1. 76 (local note: Background, dated amendment list, L126)

```text
August 28, 2020 (85 FR 53516), November 12, 2020 (85 FR 72506)
```

### Necessary documents

- Tick Doc 2 (fr_2025_16801.txt), role: Answer component
- Tick Doc 6 (fr_2026_18552.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_11907.txt), Doc 3 (fr_2026_08662.txt), Doc 4 (fr_2026_11312.txt), Doc 5 (fr_2026_14118.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Look-alike measure: Doc 2 says Wyoming adopted federal CCR rules promulgated through December 14, 2020; using that cutoff as an amendment date gives 108 days. Doc 2's dated list shows the newest amendment by then was November 12, 2020, 76 days after Wisconsin's August 28, 2020.
```

(46 / 50 words.)
