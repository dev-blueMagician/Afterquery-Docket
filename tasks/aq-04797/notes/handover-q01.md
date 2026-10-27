# aq-04797 q01 hand-over

Generated 2026-10-14 by `python tools/check_questions.py tasks/aq-04797 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 386dec2871b92f88cc12dd9c0a04ca989af9b3f7744631df845a3d60b1d2fdd7: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D03 = Doc 7, D05 = Doc 1.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN format: say what to answer when nothing qualifies, e.g. 'which ..., if any, ...' (form: answer format stated)
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Relative to nominal capacity, which lithium-ion cells besides NASA cell B0005 end their constant-voltage charge at a current no higher than B0005's? List them alphabetically.
```

### Number of asks

1 ask

### Gold answer

```text
B0006, B0007, PANASONIC NCA cells
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 1, the NASA dataset description in the research methodology): B0005, B0006 and B0007 have a nominal capacity of 2 Ah and B0018 one of 1.35 Ah, and all four are charged at constant current and then at constant voltage until the current falls to a cutoff current of 20 mA.

Step 2. Calculation (Doc 1): B0005 ends its constant-voltage charge at 20 / 2 = 10 milliamps per ampere-hour of nominal capacity. B0006 and B0007 have the same capacity and the same cutoff current, so their ratio equals B0005's and is no higher: both qualify (components c1 and c2).

Step 3. Exclusion (Doc 1): B0018 ends at the same 20 mA on only 1.35 Ah, a higher current per ampere-hour than B0005's, so it does not qualify.

Step 4. Source input (Doc 7, Table 1 and the methods paragraph on the authors' own cycling tests): the PANASONIC cells, with an NCA cathode and a graphite anode, have a nominal capacity of 3.03 Ah and are held at 4.2 V until the charging current drops below 0.03 A.

Step 5. Calculation (Doc 1 and Doc 7): a 3.03 Ah cell at B0005's ratio would end at 3.03 × 10 = 30.3 milliamps. The PANASONIC cells' end current from Step 4 is below that, so they qualify (component c3).

Step 6. Exclusion (Doc 1 and Doc 7): a 27 Ah GOTION LFP cell, the authors' other tested cell type, would end at 27 × 10 = 270 milliamps at B0005's ratio, but Doc 7's methods paragraph has the GOTION cells end their hold at a far higher current, so they do not qualify. No other cell in Doc 1 or Doc 7 has both a stated end current and a stated nominal capacity.

Decoy: B0018 shares the NASA cells' 20 mA cutoff but has a smaller capacity, so its end current per ampere-hour is higher than B0005's (Step 3).

Final answer, in alphabetical order (Doc 1 and Doc 7): B0006, B0007, PANASONIC NCA cells.
```

### Answer components

Component 1

```text
B0006
```

Component 2

```text
B0007
```

Component 3

```text
PANASONIC NCA cells
```

### Evidence

Evidence 1: document Doc 1 (physics-informed-hybrid-reinforcement-learning-for-estimating-lithium-ion-battery-state-of-health-salem-et-al-scientific.txt), proves component 1. B0006 (local note: research methodology, NASA dataset, l65; Doc 1)

```text
batteries B0005, B0006, and B0007 utilize lithium nickel cobalt aluminum oxide (NCA) as the positive electrode and graphite as the negative electrode, with a nominal capacity of 2 Ah
```

Evidence 2: document Doc 1 (physics-informed-hybrid-reinforcement-learning-for-estimating-lithium-ion-battery-state-of-health-salem-et-al-scientific.txt), proves component 2. B0007 (local note: research methodology, NASA dataset, l65; Doc 1)

```text
batteries B0005, B0006, and B0007 utilize lithium nickel cobalt aluminum oxide (NCA) as the positive electrode and graphite as the negative electrode, with a nominal capacity of 2 Ah
```

Evidence 3: document Doc 1 (physics-informed-hybrid-reinforcement-learning-for-estimating-lithium-ion-battery-state-of-health-salem-et-al-scientific.txt), proves component 1. B0006 (local note: research methodology, NASA dataset, l65; Doc 1)

```text
All batteries underwent charging using a constant current-constant voltage (CC-CV) protocol at 1.5 A, with a cutoff voltage of 4.2 V and a cutoff current of 20 mA
```

Evidence 4: document Doc 1 (physics-informed-hybrid-reinforcement-learning-for-estimating-lithium-ion-battery-state-of-health-salem-et-al-scientific.txt), proves component 2. B0007 (local note: research methodology, NASA dataset, l65; Doc 1)

```text
All batteries underwent charging using a constant current-constant voltage (CC-CV) protocol at 1.5 A, with a cutoff voltage of 4.2 V and a cutoff current of 20 mA
```

Evidence 5: document Doc 1 (physics-informed-hybrid-reinforcement-learning-for-estimating-lithium-ion-battery-state-of-health-salem-et-al-scientific.txt), proves component 1. B0006 (local note: research methodology, NASA dataset, l65; Doc 1)

```text
battery B0018 utilizes lithium nickel manganese cobalt oxide (NMC) for the positive electrode and graphite for the negative electrode, with a nominal capacity of 1.35 Ah
```

Evidence 6: document Doc 1 (physics-informed-hybrid-reinforcement-learning-for-estimating-lithium-ion-battery-state-of-health-salem-et-al-scientific.txt), proves component 2. B0007 (local note: research methodology, NASA dataset, l65; Doc 1)

```text
battery B0018 utilizes lithium nickel manganese cobalt oxide (NMC) for the positive electrode and graphite for the negative electrode, with a nominal capacity of 1.35 Ah
```

Evidence 7: document Doc 7 (deep-learning-to-estimate-lithium-ion-battery-state-of-health-without-additional-degradation-experiments-lu-et-al-nature.txt), proves component 3. PANASONIC NCA cells (local note: Table 1, l49; Doc 7)

```text
|#3|PANASONIC|NCA/ Graphite|3.03|2.5-4.2|2770|1801|
```

Evidence 8: document Doc 7 (deep-learning-to-estimate-lithium-ion-battery-state-of-health-without-additional-degradation-experiments-lu-et-al-nature.txt), proves component 3. PANASONIC NCA cells (local note: Methods, battery cycling and dataset generation, l191; Doc 7)

```text
In each cycle of the battery from Dataset #3, the charge strategy is to charge at a constant-current rate of 0.3 C until the voltage reaches 4.2 V and then hold at 4.2 V until the charging current drops below 0.03 A
```

Evidence 9: document Doc 7 (deep-learning-to-estimate-lithium-ion-battery-state-of-health-without-additional-degradation-experiments-lu-et-al-nature.txt), proves component 3. PANASONIC NCA cells (local note: Table 1, l51; Doc 7)

```text
|#5|GOTION HIGH-TECH|LFP/ Graphite|27|2.0-3.65|4262|2238|
```

Evidence 10: document Doc 7 (deep-learning-to-estimate-lithium-ion-battery-state-of-health-without-additional-degradation-experiments-lu-et-al-nature.txt), proves component 3. PANASONIC NCA cells (local note: Methods, battery cycling and dataset generation, l191; Doc 7)

```text
In each cycle of the battery from Dataset #5, the charge strategy is to charge at a constant-current rate of 1 C until the voltage reaches 3.65 V and then hold at 3.65 V until the charging current drops below 1.35 A
```

### Necessary documents

- Tick Doc 1 (physics-informed-hybrid-reinforcement-learning-for-estimating-lithium-ion-battery-state-of-health-salem-et-al-scientific.txt), role: Answer component
- Tick Doc 7 (deep-learning-to-estimate-lithium-ion-battery-state-of-health-without-additional-degradation-experiments-lu-et-al-nature.txt), role: Answer component

Leave unticked: Doc 2 (state-of-health-evaluation-of-lithium-ion-batteries-using-the-statistical-properties-of-the-voltage-hammou-et-al-entropy.txt), Doc 3 (a-hybrid-ridge-regression-convolutional-bidirectional-long-short-term-memory-framework-with-dual-level-transfer-learning.txt), Doc 4 (state-of-health-estimation-for-lithium-ion-batteries-based-on-differential-thermal-voltammetry-features-and-particle-swa.txt), Doc 5 (battery-state-of-health-estimation-under-fast-charging-via-deep-transfer-learning-zhao-et-al-iscience.txt), Doc 6 (state-of-health-for-lithium-ion-batteries-based-on-explainable-feature-fragments-via-graph-attention-network-and-bi-dire.txt), Doc 8 (the-future-of-battery-data-and-the-state-of-health-of-lithium-ion-batteries-in-automotive-applications-von-et-al-communi.txt), Doc 9 (machine-learning-assisted-prediction-of-state-of-health-in-lithium-metal-batteries-with-electrochemical-impedance-spectr.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization, Conditional filter

Leave unticked: Temporal alignment, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Linking across documents: the PANASONIC NCA cells end their constant-voltage hold below 0.03 A on 3.03 Ah, a statement found only in Doc 7's methods paragraph on its own tests. A solver that stays with Doc 1's NASA cells answers B0006, B0007; the gold adds the PANASONIC cells.
```

(48 / 50 words.)
