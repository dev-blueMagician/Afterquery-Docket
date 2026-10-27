# aq-02750 q06 hand-over

Generated 2026-10-11 by `python tools/check_questions.py tasks/aq-02750 --handover --q q06` from questions/q06.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 b6ec9851a28cd7d4b180492f659308c07acbce74e3cd8acc84e034b66b812191: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D03 = Doc 3.
- Floor: 0 FAIL, 14 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 1: Doc 2 doesn't mention 1003.42. Doc 2 prints it first at character 22,612, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 2 doesn't mention 1208.31. Doc 2 prints it first at character 23,994, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 2 doesn't mention 1208.33. Doc 2 prints it first at character 21,746, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 2 doesn't mention 1208.35. Doc 2 prints it first at character 22,520, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 2 doesn't mention 1208.35. Doc 2 prints it first at character 22,520, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 2 doesn't mention 1208.33. Doc 2 prints it first at character 21,746, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 3 doesn't mention 1003.42. Doc 3 prints it first at character 21,149, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 3 doesn't mention 1235.6. Doc 3 prints it first at character 26,464, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: Doc 3 doesn't mention 1235.6. Doc 3 prints it first at character 26,464, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN precision: the answer is a rate or decimal; state the precision in the question
  - WARN format: a list answer: say the order, or 'in any order' (form: answer format stated)
  - WARN format: say what to answer when nothing qualifies, e.g. 'which ..., if any, ...' (form: answer format stated)
  - WARN list-contract: the answer lists 6 items; say how many to expect, or ask for one value (form: list contract)
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q06.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Which sections of 8 CFR parts 1003, 1208 and 1235 are amended by either EOIR's December 2024 interim rule on bars in fear reviews or the provisions of the 2020 Security Bars rule that survived the December 2025 partial withdrawal?
```

### Number of asks

1 ask

### Gold answer

```text
8 CFR 1003.42, 1208.13, 1208.16, 1208.31, 1208.33, 1208.35
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, amendatory instructions at the end of the rule): EOIR's interim rule amends Sec. 1003.42, Sec. 1208.31, Sec. 1208.33 and Sec. 1208.35. The amendment to Sec. 1208.35 is the rule's last instruction and only corrects a cross-reference.

Step 2. Application (Doc 2): footnote 8 says it was unnecessary to amend Sec. 1208.35 in order to clarify the review of bars. That does not take Sec. 1208.35 off the list: the preamble describes cross-reference corrections in 8 CFR 1208.33(a)(3)(i)(C) and 1208.35(a)(2)(i)(C), and the last instruction makes the one in Sec. 1208.35. No instruction in Doc 2 amends Sec. 1208.30.

Step 3. Source input (Doc 3, section III): the provisions of the Security Bars rule that remain will be codified, in part 1208, at 8 CFR 1208.13(c)(10) and 1208.16(d)(2). In parts 1003, 1208 and 1235 the rule will no longer amend 8 CFR 1003.42, 1208.16(f), 1208.30 and 1235.6.

Step 4. Application (Doc 3): within parts 1003, 1208 and 1235, the surviving provisions amend Sec. 1208.13 and Sec. 1208.16. Sec. 1208.16 stays on the list because only the change to its paragraph (f) was withdrawn; the corrected instruction still revises its paragraph (d)(2). Decoy: Sec. 1208.30 and Sec. 1235.6 look like members because both documents discuss them, but they are off the list: their Security Bars amendments were withdrawn and EOIR's rule has no instruction for them.

Step 5. Application (Doc 2 and Doc 3): Sec. 1003.42 stays on the list although the Security Bars amendment to it was withdrawn, because EOIR's interim rule amends it; Doc 3 says EOIR will maintain that later provision. The sections of parts 208 and 235 that the same passages name are outside the three parts asked about.

Step 6. Application (Doc 2 and Doc 3): the two sets together are Sec. 1003.42, 1208.13, 1208.16, 1208.31, 1208.33 and 1208.35, six sections.
```

### Answer components

Component 1

```text
8 CFR 1003.42
```

Component 2

```text
1208.13
```

Component 3

```text
1208.16
```

Component 4

```text
1208.31
```

Component 5

```text
1208.33
```

Component 6

```text
1208.35
```

### Evidence

Evidence 1: document Doc 2 (fr_2024_30500.txt), proves component 1. 8 CFR 1003.42 (local note: regulatory text, instruction 2, L335)

```text
2. Amend Sec. 1003.42 by:
```

Evidence 2: document Doc 2 (fr_2024_30500.txt), proves component 4. 1208.31 (local note: regulatory text, instruction 4, L378)

```text
4. Amend Sec. 1208.31 by:
```

Evidence 3: document Doc 2 (fr_2024_30500.txt), proves component 5. 1208.33 (local note: regulatory text, instruction 5, L406)

```text
5. Amend Sec. 1208.33 by:
```

Evidence 4: document Doc 2 (fr_2024_30500.txt), proves component 6. 1208.35 (local note: regulatory text, instruction 6, L442)

```text
6. Amend Sec. 1208.35 by removing the reference to
```

Evidence 5: document Doc 2 (fr_2024_30500.txt), proves component 5. 1208.33 (local note: preamble, technical edits, L187)

```text
in 8 CFR 1208.33(a)(3)(i)(C) and 1208.35(a)(2)(i)(C).
```

Evidence 6: document Doc 2 (fr_2024_30500.txt), proves component 6. 1208.35 (local note: preamble, technical edits, L187)

```text
in 8 CFR 1208.33(a)(3)(i)(C) and 1208.35(a)(2)(i)(C).
```

Evidence 7: document Doc 3 (fr_2025_23970.txt), proves component 2. 1208.13 (local note: section III, L219)

```text
These provisions will be codified at 8 CFR 208.13(c)(10), 1208.13(c)(10) (clarification with respect to asylum), and at 8 CFR 208.16(d)(2), 1208.16(d)(2) (clarification with respect to statutory and CAT withholding of removal).
```

Evidence 8: document Doc 3 (fr_2025_23970.txt), proves component 3. 1208.16 (local note: section III, L219)

```text
These provisions will be codified at 8 CFR 208.13(c)(10), 1208.13(c)(10) (clarification with respect to asylum), and at 8 CFR 208.16(d)(2), 1208.16(d)(2) (clarification with respect to statutory and CAT withholding of removal).
```

Evidence 9: document Doc 3 (fr_2025_23970.txt), proves component 3. 1208.16 (local note: section III, L221)

```text
to the extent that they would amend 8 CFR 208.16(f), 208.30, 235.6, 1003.42, 1208.16(f), 1208.30, and 1235.6, and the Security Bars Final Rule will no longer amend those provisions.
```

Evidence 10: document Doc 3 (fr_2025_23970.txt), proves component 3. 1208.16 (local note: corrections, L508)

```text
11. Amend Sec. 1208.16 by revising paragraph (d)(2) to read as follows:
```

Evidence 11: document Doc 3 (fr_2025_23970.txt), proves component 1. 8 CFR 1003.42 (local note: section II.E.4, L209)

```text
EOIR will maintain its later-enacted provision from the EOIR Bars IFR at 8 CFR 1003.42(d)
```

### Necessary documents

- Tick Doc 2 (fr_2024_30500.txt), role: Answer component
- Tick Doc 3 (fr_2025_23970.txt), role: Answer component

Leave unticked: Doc 1 (fr_2024_10390.txt), Doc 4 (fr_2026_10543.txt), Doc 5 (fr_2026_12790.txt), Doc 6 (fr_2026_14365.txt), Doc 7 (fr_2026_16706.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Part vs total: Doc 2's preamble names three sections for its wording change, and footnote 8 says amending Sec. 1208.35 was unnecessary, but the rule's last instruction amends Sec. 1208.35. Taking the part the preamble discusses for the whole gives five sections, without 1208.35. The instructions give six.
```

(48 / 50 words.)
