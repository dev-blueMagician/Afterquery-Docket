# aq-01937 q02 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-01937 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 53dd017c0f9da582fc906b18dfc8a11177ed8e5ea1f0f0c8d41f7387eb1dd1f8: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D05 = Doc 5, D10 = Doc 10.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Comparing the quarter ended June 30, 2026 with the quarter ended March 31, 2024, how much higher or lower was State Street's Software services revenue, as a signed percentage of the earlier quarter's figure to one decimal place?
```

### Number of asks

1 ask

### Gold answer

```text
+15.3%
```

### Step-by-step reasoning

```text
Step 1. Doc 10: Software services revenue was 166 ($ millions) in 2Q26 ("Software services 166 169 169", columns 2Q26, 1Q26, 2Q25).

Step 2. Doc 10: Software services is the revenue line of the CRD business: Software services ARR is calculated "for CRD and CRD for Private Markets", and the On-premises revenue that drives the line is defined as revenue "recognized in the CRD business".

Step 3. Doc 5: the 2024 layout splits the old Software and processing fees line into Front office software and data and Lending related and other fees; for 1Q24 they are 144 and 63, totalling 207. Doc 5's Front office software and data ARR is likewise calculated "for CRD and CRD for Private Markets", so the CRD revenue line, the one now reported as Software services, was 144 in 1Q24; the 207 total also holds the lending fees.

Step 4. Doc 9's reclassification note confirms the mapping in words: the lending-related fees were moved out to Other fee revenue when the Software and processing fees caption became Software services.

Step 5. Doc 5 and Doc 10: 166 - 144 = 22.

Step 6. Doc 5 and Doc 10: 22 / 144 = 15.3%.

Step 7. Doc 5 and Doc 10: treating Software services as the whole old Software and processing fees line gives 166 - 207 = -41.

Step 8. Doc 5 and Doc 10: -41 / 207 = -19.8%, which compares the CRD line with a total that still includes the lending fees, so it is not the asked measure.
```

### Answer components

Component 1

```text
+15.3%
```

### Evidence

Evidence 1: document Doc 5 (stt_ex991_2025-04-17.txt), proves component 1. +15.3% (local note: revenue table, L254)

```text
Front office software and data 158 197 144
```

Evidence 2: document Doc 5 (stt_ex991_2025-04-17.txt), proves component 1. +15.3% (local note: revenue table, L255)

```text
Lending related and other fees 67 62 63
```

Evidence 3: document Doc 5 (stt_ex991_2025-04-17.txt), proves component 1. +15.3% (local note: revenue table, L256)

```text
Software and processing fees 225 259 207
```

Evidence 4: document Doc 5 (stt_ex991_2025-04-17.txt), proves component 1. +15.3% (local note: In this news release, ARR definition, L389)

```text
Front office software and data ARR, an operating metric, is calculated by annualizing current quarter revenue for CRD and CRD for Private Markets
```

Evidence 5: document Doc 10 (stt_ex991_2026-07-16.txt), proves component 1. +15.3% (local note: revenue table, L223)

```text
Software services 166 169 169
```

Evidence 6: document Doc 10 (stt_ex991_2026-07-16.txt), proves component 1. +15.3% (local note: In this news release, ARR definition, L374)

```text
Software services ARR, an operating metric, is calculated by annualizing the revenue from the last month of the relevant quarter for CRD and CRD for Private Markets
```

### Necessary documents

- Tick Doc 5 (stt_ex991_2025-04-17.txt), role: Answer component
- Tick Doc 10 (stt_ex991_2026-07-16.txt), role: Answer component

Leave unticked: Doc 1 (stt_ex991_2024-02-27.txt), Doc 2 (stt_ex991_2024-10-15.txt), Doc 3 (stt_ex991_2025-01-17.txt), Doc 4 (stt_ex991_2025-03-05.txt), Doc 6 (stt_ex991_2025-07-15.txt), Doc 7 (stt_ex991_2025-10-17.txt), Doc 8 (stt_ex991_2026-01-16.txt), Doc 9 (stt_ex991_2026-04-17.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Entity resolution

Leave unticked: Unit normalization, Conditional filter, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

Where the trap sits:

```text
Doc 10 reports a Software services line, 166 in the June 2026 quarter, that no 2024 release prints. Doc 5, the only release with first-quarter 2024 revenue lines, still shows the old layout in the same table slot: Front office software and data 144, Lending related and other fees 63, and their total, Software and processing fees 207. The 2026 caption reads like a new name for that total line, and the reclassification note in Doc 9, the 1Q26 release that introduced it, says the old caption "has been changed to Software services".
```

The wrong answer a careless solver gives:

```text
-19.8%. A solver who treats Software services as the renamed Software and processing fees total takes the 2024 figure of 207 and compares it with the 2026 figure of 166 from Doc 10: (166 - 207) / 207 = -41 / 207 = -19.81%. The careless answer reports a fall in software revenue when the business actually grew.
```

Why the correct answer avoids it:

```text
Both releases define their software ARR on the same business, "for CRD and CRD for Private Markets", which ties Software services to the Front office software and data line, not to the total that also holds the lending fees. Doc 9's note says the same: the lending fees left the line when the caption changed. On that like-for-like basis 1Q24 was 144, and 166 / 144 gives a rise of 15.3%.
```

(222 words across the three boxes; the form needs at least 150.)
