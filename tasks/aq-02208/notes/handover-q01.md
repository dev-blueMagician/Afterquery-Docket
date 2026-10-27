# aq-02208 q01 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-02208 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 2, difficulty_target medium, origin claude.
- tested_sha256 d58f4220f4951db00837f467c9e5b8161d404fe8f100b7535ed07b1d292f4145: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D04 = Doc 4.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN documents: D04: exclusion role; a platform reviewer accepted it only for a document ruling out an item that exists without it, not for its own decoy (aq-01333 q01)
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Which proposed FCC space-launch coordination-request items, if any, do the final procedures require of no licensee? Any order.
```

### Number of asks

1 ask

### Gold answer

```text
Distance to the nearest aircraft landing area, and natural formations or structures shielding the antenna from aircraft
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 2, proposed data requirements for frequency coordination requests): the Bureau proposed that licensees give the third-party frequency coordinator, among other groups, "7. Additional launch site technical information", made of "a. Elevation of ground at antenna site above mean sea level in meters", "b. Overall height above ground to tip of antenna in meters", "c. Distance to nearest aircraft landing area in kilometers" and "d. Natural formations or existing man-made structures" that "would tend to shield the antenna from aircraft". Its emission details also asked, if bandwidth exceeds 5 megahertz, for an explanation of why it is necessary.

Step 2. Source fact (Doc 4, final frequency coordination requests): the final list that "Space Launch Service licensees shall provide" keeps licensee details, the registered launch site and stations, transmitter characteristics, emission details, launch details and additional station details. It has no launch-site technical group, and no item asks for the distance to an aircraft landing area or for structures that shield the antenna.

Step 3. Decoy check (Doc 4, final fixed and base station registration): the registration list includes "4. Overall height above ground to tip of antenna in meters" and "5. Elevation of ground at antenna site above mean sea level in meters", so proposed items a and b are still required, at registration, and do not qualify. A "justification for greater than five megahertz must be submitted in the initial station registration in ULS as a single attachment", so the bandwidth explanation does not qualify either.

Step 4. Decoy check (Doc 4, discussion of coordination data): operators "proposing suborbital launches need not provide" the list of objects to achieve orbit, the orbital location or transmission durations. The final list still contains these items for orbital launches, so some licensees must give them and they do not qualify.

Step 5. Source fact (Doc 4, registration of coordinated launch parameters): the post-coordination list (purpose of operation, start and end times, stations, launch site, transmission characteristics, coordinator response) contains neither the landing-area distance nor shielding structures, and neither does the launch site registration.

Step 6. Comparison (Doc 2 and Doc 4): every other proposed coordination item appears in a final list. Only the distance to the nearest aircraft landing area and the natural formations or man-made structures shielding the antenna from aircraft are required of no licensee.
```

### Answer components

Component 1

```text
Distance to the nearest aircraft landing area
```

Component 2

```text
natural formations or structures shielding the antenna from aircraft
```

### Evidence

Evidence 1: document Doc 2 (fr_2024_29833.txt), proves component 1. Distance to the nearest aircraft landing area (local note: L198, proposed coordination request item 7c)

```text
c. Distance to nearest aircraft landing area in kilometers; and
```

Evidence 2: document Doc 2 (fr_2024_29833.txt), proves component 2. natural formations or structures shielding the antenna from aircraft (local note: L199, proposed coordination request item 7d)

```text
Natural formations or existing man-made structures (hills, trees, water tanks, towers, etc.) which would tend to shield the antenna from aircraft.
```

Evidence 3: document Doc 4 (fr_2025_07643.txt), proves component 1. Distance to the nearest aircraft landing area (local note: L228, final coordination request list)

```text
Space Launch Service licensees shall provide the following data to the space launch frequency coordinator in a frequency coordination request:
```

Evidence 4: document Doc 4 (fr_2025_07643.txt), proves component 2. natural formations or structures shielding the antenna from aircraft (local note: L228, final coordination request list)

```text
Space Launch Service licensees shall provide the following data to the space launch frequency coordinator in a frequency coordination request:
```

### Necessary documents

- Tick Doc 2 (fr_2024_29833.txt), role: Answer component
- Tick Doc 4 (fr_2025_07643.txt), role: Exclusion / condition source

  Reviewer note:

```text
its final lists keep every other proposed coordination item (for example, elevation of ground and antenna height move to fixed and base station registration), ruling those items out; they exist in Doc 2 without it
```

Leave unticked: Doc 1 (fr_2024_20900.txt), Doc 3 (fr_2025_02961.txt), Doc 5 (fr_2026_06865.txt), Doc 6 (fr_2026_15415.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Conditional filter

Leave unticked: Unit normalization, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Wrong members in a list

#### Failure mode 2

Trap: Wrong jurisdiction or scope

How a careless solver fails: Misapplies a rule or premise

#### Failure mode 3

Trap: Linking across documents

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Doc 4's prose (adopting "the substantial majority", no significant reduction) suggests none. Diffing only its coordination list gives four items, but elevation and antenna height moved to fixed/base registration. Suborbital exemptions still bind orbital launches. Only Doc 2's landing-area distance and shielding structures appear in no final list.
```

(48 / 50 words.)
