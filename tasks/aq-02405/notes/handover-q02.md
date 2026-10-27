# aq-02405 q02 hand-over

Generated 2026-10-09 by `python tools/check_questions.py tasks/aq-02405 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 65b28e8644afab8c987b8a798cdfe1a2fa8ef53109d0c06c6b9a819c34a560d8: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D04 = Doc 4, D05 = Doc 5.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
If ATF's 2026 proposals were all finalized as written, which paragraph of 27 CFR 478.124 would require checking a non-immigrant-visa buyer's exception or waiver papers?
```

### Number of asks

1 ask

### Gold answer

```text
Paragraph (c)(5)(iv)
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 5, proposed 478.124(c)(5), Licensee verifications): ATF's Form 4473 proposal rewrites 27 CFR 478.124 so that paragraph (c)(5) lists the licensee's verification steps as items (i) to (v).

Step 2. Source fact (Doc 5, proposed 478.124(c)(5)(iii)): item (iii) applies to all transfers in which the transferee is an alien admitted under a non-immigrant visa who states that an exception to, or a waiver from, the prohibition in section 922(g)(5)(B) applies, and requires the licensee to examine the documents establishing the exception or waiver; items (iv) and (v) begin "For non-over-the-counter transfers" and "For over-the-counter transfers".

Step 3. Source fact (Doc 4, footnote 37): ATF's non-over-the-counter proposal makes its changes to 478.124(c)(5) as it has been proposed for revision in the Form 4473 proposal, where (c)(5) has the heading "Licensee verifications".

Step 4. Source fact (Doc 4, amendatory instruction 3): it redesignates paragraphs (iii) through (v) of 478.124(c)(5) as (iv) through (vi) and adds a new paragraph (iii) for non-over-the-counter transfers subject to a NICS check; its edits to the newly designated (v) and (vi) start from the words "For non-over-the-counter transfers" and "For over-the-counter transfers", which open Doc 5's items (iv) and (v).

Step 5. Combination (Steps 2 to 4; Doc 5 and Doc 4): with both proposals applied, Doc 5's item (iii) on non-immigrant-visa buyers becomes item (iv), so the requirement would sit in 27 CFR 478.124(c)(5)(iv).
```

### Answer components

Component 1

```text
Paragraph (c)(5)(iv)
```

### Evidence

Evidence 1: document Doc 5 (fr_2026_09182.txt), proves component 1. Paragraph (c)(5)(iv) (local note: L582, proposed 478.124(c)(5)

```text
(5) Licensee verifications. After the transferee has executed the transferee portion of Form 4473, the licensee must:
```

Evidence 2: document Doc 5 (fr_2026_09182.txt), proves component 1. Paragraph (c)(5)(iv) (local note: L585, proposed 478.124(c)(5)(iii)

```text
(iii) For all transfers in which the transferee is an alien admitted to the United States under a non-immigrant visa who states that the alien falls within an exception to, or has a waiver from, the prohibition in section 922(g)(5)(B) of the Act, examine applicable documents establishing the exception or waiver
```

Evidence 3: document Doc 4 (fr_2026_09157.txt), proves component 1. Paragraph (c)(5)(iv) (local note: L194, footnote 37)

```text
This would be Sec. 478.124(c)(5) as it has been proposed for revision in the Revising Firearms Transaction Record, Form 4473, proposed rule
```

Evidence 4: document Doc 4 (fr_2026_09157.txt), proves component 1. Paragraph (c)(5)(iv) (local note: L490, amendatory instruction 3.a)

```text
Redesignating paragraphs (iii) through (v) as paragraphs (iv) through (vi);
```

Evidence 5: document Doc 4 (fr_2026_09157.txt), proves component 1. Paragraph (c)(5)(iv) (local note: L494, amendatory instruction 3.c)

```text
In newly designated paragraph (v), adding the phrase
```

### Necessary documents

- Tick Doc 5 (fr_2026_09182.txt), role: Answer component
- Tick Doc 4 (fr_2026_09157.txt), role: Answer component

Leave unticked: Doc 1 (fr_2024_28711.txt), Doc 2 (fr_2026_08918.txt), Doc 3 (fr_2026_08912.txt), Doc 6 (fr_2026_13587.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Superseded date or version

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Superseded version: Doc 5's rewritten 478.124(c)(5) lists the non-immigrant-visa check as item (iii). Doc 4, which amends that rewritten text (its footnote 37), redesignates (iii) through (v) as (iv) through (vi), so reading Doc 5 alone gives (c)(5)(iii). Gold: (c)(5)(iv).
```

(40 / 50 words.)
