# aq-02749 q01 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02749 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 1ce4f5889eaa59d89a3effd065782446eee5cef2ebd4839da1742bccc2ab7dd5: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D03 = Doc 3, D05 = Doc 5.
- Floor: 0 FAIL, 6 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 3: Doc 2 doesn't mention 7. Doc 2 prints it first at character 21,166, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: Doc 3 doesn't mention 45. Doc 3 prints it first at character 34,425, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: Doc 3 doesn't mention 15. Doc 3 prints it first at character 20,660, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 5: Doc 3 doesn't mention 15. Doc 3 prints it first at character 20,660, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 7: Doc 5 doesn't mention 35. Doc 5 prints it first at character 40,713, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
A utility needs a new coal-ash landfill permit in Wyoming (notices a week apart), a capacity increase at a Virginia landfill and, at an Alabama landfill, a liner redesign and an identical replacement monitoring well. Hearings on the capacity increase and the redesign come 40 days after notice. At minimum, how many public-comment days is that in total?
```

### Number of asks

1 ask

### Gold answer

```text
169 days
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, Public Comment Period): an applicant for a new solid waste permit, which covers a coal-ash landfill, must "complete two public comment periods during the permitting process", one on the complete application and one on the proposed permit.
Step 2. Source input (Doc 2, Public Comment Period): the applicant publishes each notice "once a week for two consecutive weeks", and "Each public comment period begins on the first day of the notice publication and continues until 30 days after the second publication."
Step 3. Calculation (Doc 2): with the second notice one week after the first, days from the first notice to the close of one Wyoming comment period: 7 + 30 = 37.
Step 4. Source input (Doc 3, Public Notice and Participation in the CCR Permit Application Process): a permit modification that "would expand a facility or increase capacity" follows "the same public participation procedures as outlined above for new solid waste permits". Those require "that the public comment period last at least 45 days, with the public hearing scheduled at least 30 days following the public notice and the public comment period extending at least 15 days after the public hearing."
Step 5. Calculation (Doc 3): with the hearing 40 days after the notice, the earliest close of Virginia's comment period, in days after the notice: 40 + 15 = 55. That is later than the minimum length quoted in Step 4, so the hearing rule sets Virginia's minimum.
Step 6. Source input (Doc 5, Permit Modifications): a change in the design of a liner needs a major modification, and "Major modifications require a public notice and public comment period under the same procedures as for issuance of initial permits." Replacing existing groundwater monitoring wells with wells "of similar design and depth" is listed among the minor modifications "that do not require a public notice or comment", so the replacement well adds no comment days.
Step 7. Source input (Doc 5, Public Comment Period): "a 35-day public comment period is provided", and it "will be extended to include comments submitted at a public hearing, if one is held on a proposed permitting action, if the hearing is scheduled after the end of the original 35-day comment period." A hearing 40 days after the notice falls after that period ends, so the liner redesign's comment period runs to the hearing, 40 days after the notice.
Step 8. Calculation (Doc 2 and Doc 3): Wyoming's total over its two comment periods, in days: 37 + 37 = 74.
Step 9. Calculation (Doc 2 and Doc 3): Wyoming and Virginia together, in days: 74 + 55 = 129.
Step 10. Final answer (Doc 2, Doc 3 and Doc 5): adding Alabama's liner redesign, in days: 129 + 40 = 169.
```

### Answer components

Component 1

```text
169
```

### Evidence

Evidence 1: document Doc 2 (fr_2025_16801.txt), proves component 1. 169 (local note: Public Comment Period, L220)

```text
All applicants for solid waste permits that submit a new, renewal, closure or major amendment permit application are required to complete two public comment periods during the permitting process.
```

Evidence 2: document Doc 2 (fr_2025_16801.txt), proves component 1. 169 (local note: Public Comment Period, L221)

```text
The applicant is required to publish each written notice once a week for two consecutive weeks in a newspaper of general circulation
```

Evidence 3: document Doc 2 (fr_2025_16801.txt), proves component 1. 169 (local note: Public Comment Period, L221)

```text
Each public comment period begins on the first day of the notice publication and continues until 30 days after the second publication.
```

Evidence 4: document Doc 3 (fr_2026_08662.txt), proves component 1. 169 (local note: Public Notice and Participation in the CCR Permit Application Process, L198)

```text
If the modification would expand a facility or increase capacity, the process follows the same public participation procedures as outlined above for new solid waste permits.
```

Evidence 5: document Doc 3 (fr_2026_08662.txt), proves component 1. 169 (local note: Public Notice and Participation in the CCR Permit Application Process, L195)

```text
The regulation requires that the public comment period last at least 45 days, with the public hearing scheduled at least 30 days following the public notice and the public comment period extending at least 15 days after the public hearing.
```

Evidence 6: document Doc 5 (fr_2026_14118.txt), proves component 1. 169 (local note: Permit Modifications, L216)

```text
a permittee must request a major modification for the addition of, or a change in the design of, a liner and/or leachate collection system
```

Evidence 7: document Doc 5 (fr_2026_14118.txt), proves component 1. 169 (local note: Permit Modifications, L216)

```text
Major modifications require a public notice and public comment period under the same procedures as for issuance of initial permits.
```

Evidence 8: document Doc 5 (fr_2026_14118.txt), proves component 1. 169 (local note: Permit Modifications, L217)

```text
lists certain categories of minor modifications that do not require a public notice or comment:
```

Evidence 9: document Doc 5 (fr_2026_14118.txt), proves component 1. 169 (local note: Permit Modifications, L218)

```text
addition of new groundwater monitoring wells or replacement of existing wells (of similar design and depth)
```

Evidence 10: document Doc 5 (fr_2026_14118.txt), proves component 1. 169 (local note: Public Comment Period, L240)

```text
a 35-day public comment period is provided for ADEM to receive comments related to the proposed permitting action.
```

Evidence 11: document Doc 5 (fr_2026_14118.txt), proves component 1. 169 (local note: Public Comment Period, L240)

```text
The comment period will be extended to include comments submitted at a public hearing, if one is held on a proposed permitting action, if the hearing is scheduled after the end of the original 35-day comment period.
```

### Necessary documents

- Tick Doc 2 (fr_2025_16801.txt), role: Answer component
- Tick Doc 3 (fr_2026_08662.txt), role: Answer component
- Tick Doc 5 (fr_2026_14118.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_11907.txt), Doc 4 (fr_2026_11312.txt), Doc 6 (fr_2026_18552.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Wrong jurisdiction or scope

How a careless solver fails: Misapplies a rule or premise

#### Failure mode 2

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Wrong jurisdiction or scope: Doc 3's 15 days after a hearing is Virginia's rule; Doc 5 extends Alabama's 35 days only to the hearing. Carrying it over gives 184. Look-alike measure: Doc 2 labels Wyoming's periods "30-day", but each runs 37 days; the label gives 155. Gold: 169.
```

(48 / 50 words.)
