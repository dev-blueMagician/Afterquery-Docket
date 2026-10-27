# aq-02208 q02 hand-over

Generated 2026-10-09 by `python tools/check_questions.py tasks/aq-02208 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 d21d65331df3f34739c848fe0d64bade4dd5a635b93b98bb9d6249bd87c1c6b5: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D04 = Doc 4.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
How many more transmitter-characteristic items did the FCC's final space-launch frequency-coordination request list contain than its December 2024 proposed list?
```

### Number of asks

1 ask

### Gold answer

```text
5 more items
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 2, proposed data requirements for frequency coordination requests, item "5. Transmitter characteristics for each transmit station (center frequency)"): the proposed list runs from "a. Transmitter make/model" to "l. Emission designator", one lettered item each for make/model, output power, antenna type, number of antennas deployed, antenna gain, beam width, frequency tolerance, orientation, antenna polarization, EIRP per antenna, total EIRP and emission designator.

Step 2. Source fact (Doc 2, proposed fixed and base station registration): "b. Antenna azimuth" and "c. Antenna elevation angle" were proposed only for initial station registration, not for the transmitter list in Step 1.

Step 3. Source fact (Doc 4, final frequency coordination requests, under the same heading "5. Transmitter characteristics for each transmit station (center frequency)"): the final list runs from "a. Transmitter make/model" to "q. Emission designator". Its items a to i are the proposal's a to i, and its o to q are the proposal's EIRP per antenna, total EIRP and emission designator, so no proposed item was dropped.

Step 4. Source fact (Doc 4, the same final list): the items inserted between them are "j. Antenna azimuth", "k. Antenna elevation angle", "l. For fixed and base stations, projected space launch tracking arc path", "m. For fixed and base stations, the height AGL to the radiation center" and "n. For mobile and itinerant stations, maximum antenna height AGL". The Bureau's discussion explains only the last three, requested by SBE and AFTRCC; azimuth and elevation angle move in from the proposed registration list without comment, so counting only the discussed additions misses them.

Step 5. Calculation (Doc 2 and Doc 4): items moved in from proposed registration (azimuth, elevation angle) plus newly requested items (arc path, radiation center height, maximum antenna height): 2 + 3 = 5. With nothing dropped, the final list (lettered a to q) holds 5 more items than the proposed list (lettered a to l).
```

### Answer components

Component 1

```text
5
```

### Evidence

Evidence 1: document Doc 2 (fr_2024_29833.txt), proves component 1. 5 (local note: L172, proposed coordination request item 5 heading)

```text
5. Transmitter characteristics for each transmit station (center frequency):
```

Evidence 2: document Doc 2 (fr_2024_29833.txt), proves component 1. 5 (local note: L184, last proposed transmitter item)

```text
l. Emission designator.
```

Evidence 3: document Doc 2 (fr_2024_29833.txt), proves component 1. 5 (local note: L128, proposed fixed and base station registration)

```text
b. Antenna azimuth (if the antenna is tracking, state
```

Evidence 4: document Doc 2 (fr_2024_29833.txt), proves component 1. 5 (local note: L129, proposed fixed and base station registration)

```text
c. Antenna elevation angle (if the antenna is tracking, state
```

Evidence 5: document Doc 4 (fr_2025_07643.txt), proves component 1. 5 (local note: L236, final coordination request item 5 heading)

```text
5. Transmitter characteristics for each transmit station (center frequency):
```

Evidence 6: document Doc 4 (fr_2025_07643.txt), proves component 1. 5 (local note: L246, final transmitter item j)

```text
j. Antenna azimuth (if the antenna is tracking, state
```

Evidence 7: document Doc 4 (fr_2025_07643.txt), proves component 1. 5 (local note: L247, final transmitter item k)

```text
k. Antenna elevation angle (if the antenna is tracking, state
```

Evidence 8: document Doc 4 (fr_2025_07643.txt), proves component 1. 5 (local note: L248, final transmitter item l)

```text
l. For fixed and base stations, projected space launch tracking arc path;
```

Evidence 9: document Doc 4 (fr_2025_07643.txt), proves component 1. 5 (local note: L249, final transmitter item m)

```text
m. For fixed and base stations, the height AGL to the radiation center when the antenna is pointed along the horizon;
```

Evidence 10: document Doc 4 (fr_2025_07643.txt), proves component 1. 5 (local note: L250, final transmitter item n)

```text
n. For mobile and itinerant stations, maximum antenna height AGL;
```

Evidence 11: document Doc 4 (fr_2025_07643.txt), proves component 1. 5 (local note: L253, last final transmitter item)

```text
q. Emission designator;
```

### Necessary documents

- Tick Doc 2 (fr_2024_29833.txt), role: Answer component
- Tick Doc 4 (fr_2025_07643.txt), role: Answer component

Leave unticked: Doc 1 (fr_2024_20900.txt), Doc 3 (fr_2025_02961.txt), Doc 5 (fr_2026_06865.txt), Doc 6 (fr_2026_15415.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Aggregation

Leave unticked: Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Linking across documents

How a careless solver fails: Picks the wrong entity or section

#### Why these are traps (at most 50 words)

```text
Look-alike measure: Doc 4's discussion names three commenter-requested additions; taking that count as the list's growth gives 3. Linking: Doc 2 has azimuth and elevation in its registration section; linking Doc 4's items there treats them as proposed: 3. Doc 4's a-q list against Doc 2's a-l gives 5.
```

(49 / 50 words.)
