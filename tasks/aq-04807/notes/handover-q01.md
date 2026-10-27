# aq-04807 q01 hand-over

Generated 2026-10-14 by `python tools/check_questions.py tasks/aq-04807 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin user+claude.
- tested_sha256 9d64a532290a4b062199162bd7df0bee4c4ebac8f2262e785b1e3d98a4c2b3ef: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 3, D05 = Doc 5.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin user+claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Which nonattainment areas had tribal lands remain at a lower classification after a state-requested reclassification? List the area names alphabetically, or state that none qualify.
```

### Number of asks

1 ask

### Gold answer

```text
Coachella Valley, Greater Connecticut
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 5, Overview of Proposal and summary): at the request of the Connecticut Department of Energy and Environmental Protection, the Greater Connecticut area was voluntarily reclassified from Moderate to Serious for the 2015 ozone standard, but "the tribal portions of the Greater Connecticut area remained classified as Moderate". The summary says the State's request did not include the areas governed by the Mashantucket Pequot Tribal Nation and the Mohegan Indian Tribe. Greater Connecticut qualifies (component c2).
Step 2. Source input (Doc 3, background on the area's classifications under the 1997 standard): the State requested that the Coachella Valley be reclassified from Severe-15 to Extreme, and EPA granted it. That reclassification applies only to the portions of the Coachella Valley under the State's jurisdiction, and EPA "did not reclassify any areas of Indian country within the boundaries of the nonattainment area".
Step 3. Entity resolution (Doc 3): Indian country is tribal land, so the tribal lands inside the Coachella Valley stayed Severe-15, below Extreme. Coachella Valley qualifies (component c1).
Step 4. Exclusions and decoy (Doc 3 and Doc 5, with the other proposals' accounts): Maryland's own request moved the whole Baltimore area from Moderate to Serious, and no part of that area is said to have been left behind, so Baltimore is the decoy and is out. The Washington, Phoenix-Mesa and Northern Wasatch Front reclassifications, and the Connecticut tribes' own reclassification that Doc 5 proposes, follow a failure to attain and happen by operation of law, not at a state's request. The Coachella Valley's earlier reclassification from Serious to Severe-15 is not said to have left any land out.
Step 5. Final answer, in alphabetical order (Doc 3 and Doc 5): Coachella Valley, Greater Connecticut.
```

### Answer components

Component 1

```text
Coachella Valley
```

Component 2

```text
Greater Connecticut
```

### Evidence

Evidence 1: document Doc 3 (fr_2025_04035.txt), proves component 1. Coachella Valley (local note: I.B, State's request)

```text
the State requested a reclassification of Coachella Valley from
```

Evidence 2: document Doc 3 (fr_2025_04035.txt), proves component 1. Coachella Valley (local note: I.B, request granted)

```text
which the EPA granted with an attainment date of not later than June 15, 2024
```

Evidence 3: document Doc 3 (fr_2025_04035.txt), proves component 1. Coachella Valley (local note: I.B, scope of the reclassification)

```text
the EPA's reclassification to Extreme nonattainment applies only to the portions of the Coachella Valley subject to the State's jurisdiction, and the EPA did not reclassify any areas of Indian country within the boundaries of the nonattainment area
```

Evidence 4: document Doc 5 (fr_2025_20497.txt), proves component 2. Greater Connecticut (local note: I.A.2, the State's request)

```text
At the request of CT DEEP, the Greater Connecticut area was voluntarily reclassified from Moderate to Serious for the 2015 ozone NAAQS before the August 3, 2024, nonattainment date
```

Evidence 5: document Doc 5 (fr_2025_20497.txt), proves component 2. Greater Connecticut (local note: I.A.2, tribal portions left behind)

```text
However, the tribal portions of the Greater Connecticut area remained classified as Moderate.
```

Evidence 6: document Doc 5 (fr_2025_20497.txt), proves component 2. Greater Connecticut (local note: summary, the request's scope)

```text
That request, however, did not include areas governed by the Mashantucket Pequot Tribal Nation and the Mohegan Indian Tribe that are located within this nonattainment area.
```

### Necessary documents

- Tick Doc 3 (fr_2025_04035.txt), role: Answer component
- Tick Doc 5 (fr_2025_20497.txt), role: Answer component

Leave unticked: Doc 1 (fr_2023_20555.txt), Doc 2 (fr_2024_26423.txt), Doc 4 (fr_2025_20357.txt), Doc 6 (fr_2026_01314.txt), Doc 7 (fr_2026_08372.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Entity resolution

Leave unticked: Temporal alignment, Unit normalization, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Linking across documents: Doc 5 calls Connecticut's left-out lands "tribal portions"; Doc 3 says the Coachella Valley's state-requested Extreme reclassification left "Indian country" unreclassified. A solver who does not link the two terms answers Greater Connecticut alone; the gold adds Coachella Valley.
```

(42 / 50 words.)
