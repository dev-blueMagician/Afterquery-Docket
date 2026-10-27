# aq-01543 q01 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-01543 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 9, difficulty_target medium, origin claude.
- tested_sha256 8671bcadc7e9098c7dcbcdad07cdd2d8586acf925b93cf85e02bab5fe163daf5: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D02 = Doc 1, D11 = Doc 2.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN revision: more than two revision rounds; replace an ineffective question family or record why new evidence justifies another revision
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
In calendar year 2024, what was coal's share of Poland's electricity generation minus coal's share of Bulgaria's, in percentage points to one decimal place?
```

### Number of asks

1 ask

### Gold answer

```text
22.8 percentage points
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, Energy Sector, Power Generation): Poland's coal share of its electricity generation for the calendar year, "In 2024, the share of coal in electricity generation was 56.2%".

Step 2. Source input (Doc 1, Energy): Bulgaria's electricity production for the calendar year, which fell "to some 37,963 GWh in 2024".

Step 3. Source input (Doc 1, Energy): Bulgaria's output from coal and nuclear plants together for the calendar year, "Baseload power plants (coal, nuclear) generated a total of 28,46TWh of electricity in 2024", where the comma is a decimal comma.

Step 4. Calculation (Doc 1, unit conversion of the baseload total): 28,46 TWh = 28,460 GWh.

Step 5. Source input (Doc 1, Energy): Bulgaria's nuclear share for the calendar year, "In 2024, nuclear power accounted for approximately 41.6% of Bulgaria’s total electricity generation".

Step 6. Calculation (Doc 1, nuclear output from the nuclear share and the production total): 41.6% of 37,963 GWh = 15,792.6 GWh.

Step 7. Calculation (Doc 1, coal output, because the baseload total covers only coal and nuclear plants): 28,460 - 15,792.6 = 12,667.4 GWh.

Step 8. Calculation (Doc 1, Bulgaria's coal share of its production): 12,667.4 / 37,963 = 33.37%.

Step 9. Calculation (Doc 1 and Doc 2, Poland's coal share applied to Bulgaria's production, the coal output Bulgaria would need to match Poland's share): 56.2% * 37,963 = 21,335.206 GWh.

Step 10. Calculation (Doc 1 and Doc 2, how far Bulgaria's actual coal output falls short of that level): 21,335.206 - 12,667.4 = 8,667.806 GWh.

Step 11. Calculation (Doc 1 and Doc 2, the shortfall as a share of Bulgaria's production, which equals Poland's coal share minus Bulgaria's in percentage points): 8,667.806 / 37,963 = 22.83%.

Step 12. Final answer: the question asks for one decimal place, so 22.83% is rounded once, at this last step, to the gold answer in percentage points.
```

### Answer components

Component 1

```text
22.8 percentage points
```

### Evidence

Evidence 1: document Doc 2 (ccg_energy_cleantech_sectors_poland.txt), proves component 1. 22.8 percentage points (local note: Energy Sector, Power Generation, L13)

```text
In 2024, the share of coal in electricity generation was 56.2%
```

Evidence 2: document Doc 1 (ccg_energy_cleantech_sectors_bulgaria.txt), proves component 1. 22.8 percentage points (local note: Energy, L10)

```text
to some 37,963 GWh in 2024
```

Evidence 3: document Doc 1 (ccg_energy_cleantech_sectors_bulgaria.txt), proves component 1. 22.8 percentage points (local note: Energy, L11)

```text
Baseload power plants (coal, nuclear) generated a total of 28,46TWh of electricity in 2024
```

Evidence 4: document Doc 1 (ccg_energy_cleantech_sectors_bulgaria.txt), proves component 1. 22.8 percentage points (local note: Energy, L13)

```text
In 2024, nuclear power accounted for approximately 41.6% of Bulgaria’s total electricity generation
```

### Necessary documents

- Tick Doc 1 (ccg_energy_cleantech_sectors_bulgaria.txt), role: Answer component
- Tick Doc 2 (ccg_energy_cleantech_sectors_poland.txt), role: Answer component

Leave unticked: Doc 3 (ccg_energy_cleantech_sectors_vietnam.txt), Doc 4 (ccg_energy_cleantech_sectors_south_korea.txt), Doc 5 (ccg_energy_cleantech_sectors_israel.txt), Doc 6 (ccg_energy_cleantech_sectors_chile.txt), Doc 7 (ccg_energy_cleantech_sectors_angola.txt), Doc 8 (ccg_energy_cleantech_sectors_mauritius.txt), Doc 9 (ccg_energy_cleantech_sectors_germany.txt), Doc 10 (ccg_energy_cleantech_sectors_china.txt), Doc 11 (ccg_energy_cleantech_sectors_united_arab_emirates.txt), Doc 12 (ccg_energy_cleantech_sectors_south_africa.txt), Doc 13 (ccg_energy_cleantech_sectors_mexico.txt), Doc 14 (ccg_energy_cleantech_sectors_united_kingdom.txt), Doc 15 (ccg_energy_cleantech_sectors_uruguay.txt), Doc 16 (ccg_energy_cleantech_sectors_portugal.txt), Doc 17 (ccg_energy_cleantech_sectors_spain.txt), Doc 18 (ccg_energy_cleantech_sectors_finland.txt), Doc 19 (ccg_energy_cleantech_sectors_indonesia.txt), Doc 20 (ccg_energy_cleantech_sectors_romania.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Unit normalization

Leave unticked: Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Out-of-range period

How a careless solver fails: Uses the wrong period or date

Where the trap sits:

```text
Doc 1, Bulgaria's Energy chapter, the paragraph that opens "From September 2024 to August 2025, electricity consumption in Bulgaria relied primarily on low-carbon sources" and closes "Fossil fuels account for about 32.73% of the energy mix, with coal being dominant at 27.6% and natural gas providing a minimal 5.13%." It is the tenth paragraph of the Energy chapter, eight paragraphs after the one with the 2024 production figure, and it is the most detailed coal percentage in Doc 1, so a search that pairs "coal" with a percentage finds it. Its twelve-month window starts in September 2024 and runs eight months into 2025, and it is framed as the consumption mix rather than one calendar year's generation.
```

The wrong answer a careless solver gives:

```text
28.6 percentage points. The solver takes 27.6% as Bulgaria's coal share for 2024 and subtracts it from Poland's printed 56.2%: 56.2% - 27.6% = 28.6%. The answer overstates the gap by almost six points because it borrows a figure from a different twelve-month window.
```

Why the correct answer avoids it:

```text
The question asks about calendar year 2024. The paragraph's own opening words date the 27.6% to September 2024 through August 2025, a twelve-month window that is not a calendar year, so it is not a calendar-2024 figure. Doc 1 holds the calendar-2024 inputs in its opening paragraphs: production of 37,963 GWh, baseload output "(coal, nuclear)" of 28,46 TWh, and nuclear at about 41.6% of 2024 generation. Coal is baseload minus nuclear, 28,460 - 15,792.6 = 12,667.4 GWh, which is 33.37% of production, and 56.2% - 33.37% = 22.83%, which rounds to 22.8 percentage points.
```

(255 words across the three boxes; the form needs at least 150.)

#### Failure mode 2

Trap: Figure that must be computed

How a careless solver fails: Uses the wrong period or date

Where the trap sits:

```text
Doc 1, Bulgaria's Energy chapter. No sentence states coal's share of Bulgaria's 2024 generation, so it has to be computed from the 2024 baseload total, "Baseload power plants (coal, nuclear) generated a total of 28,46TWh of electricity in 2024", minus nuclear output. Doc 1 gives nuclear two numeric shares: "approximately 41.6%" of 2024 generation, credited to the IAEA in the Energy chapter's fifth paragraph (the one that opens "To support its energy needs"), and "about 40.38%" of electricity supply for September 2024 to August 2025, in the same paragraph as the 27.6% coal figure.
```

The wrong answer a careless solver gives:

```text
21.6 percentage points. The solver sets up the right subtraction but takes the September to August nuclear share: coal plus nuclear is 28,460 / 37,963 = 74.97% of 2024 production, so coal comes out at 74.97% - 40.38% = 34.59%, and 56.2% - 34.59% = 21.61%, which rounds to 21.6. The result mixes a calendar-2024 total with a share from a different window.
```

Why the correct answer avoids it:

```text
Both terms of the subtraction must come from calendar year 2024. The Energy chapter's fifth paragraph states the 2024 nuclear share directly: "In 2024, nuclear power accounted for approximately 41.6% of Bulgaria’s total electricity generation". With it, nuclear output is 15,792.6 GWh, coal output is 12,667.4 GWh, coal's share is 33.37%, and the gap from Poland's 56.2% is 22.8 percentage points.
```

(218 words across the three boxes; the form needs at least 150.)
