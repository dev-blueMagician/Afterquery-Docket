# aq-01539 q01 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-01539 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 8d6838652cbcd6e7710f0a7317e4db304ec928198129b7ede6cc6fcb31bcb77d: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 1, D03 = Doc 3.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
When the Snowflake breach cases were centralized in Montana, how many potential tag-along actions were pending in the district where the parties had been consolidating the cases against the defendant whose class settlement in that litigation included a California subclass?
```

### Number of asks

1 ask

### Gold answer

```text
3 actions
```

### Step-by-step reasoning

```text
Step 1. Doc 3: the amended preliminary approval order for the settlement with "Defendants Advance Auto Parts, Inc. and Advance Stores Company, Incorporated" states "The Court provisionally and preliminarily certifies the following California Settlement Subclass for settlement purposes only", defined as "All Settlement Class Members who are residents of California." No other settlement order in the litigation creates a subclass.

Step 2. Doc 1: before centralization the parties had been "consolidating the Advance Auto Parts actions in the Eastern District of North Carolina and Snowflake actions in the District of Montana", so the district asked about is the Eastern District of North Carolina.

Step 3. Doc 1: the two dockets held 45 actions on the motion, and the Panel had been notified of 34 potential tag-along actions: 45 + 34 = 79 related actions.

Step 4. Doc 1: in Montana, the transferee district, "Fourteen actions on the motion and twelve potential tag-along actions are pending": fourteen plus twelve = 26 related actions.

Step 5. Doc 1, footnote 5: counting all Montana actions as one action and all Eastern District of North Carolina actions as one action, "there still are 42 related actions pending in twelve districts". Twelve districts exceed the eight districts of the actions on the motion, so the 42 includes potential tag-alongs, and the two collapsed districts count once each: 42 - 2 = 40 related actions in the other districts.

Step 6. Related actions outside Montana: 79 - 26 = 53.

Step 7. Related actions in the Eastern District of North Carolina: 53 - 40 = 13.

Step 8. Doc 1, Schedule B: the Eastern District of North Carolina actions on the motion are In re Advance Stores Company, Chaidez, Smith, Dragone, Vogel, Riley, Levy, Cook, Clark and Carr: count = 10.

Step 9. Potential tag-along actions pending there: 13 - 10 = 3 actions.

Decoys: the transfer order's "twelve potential tag-along actions" are pending in Montana, not in the Eastern District of North Carolina, and 13 still counts the ten actions on the motion.
```

### Answer components

Component 1

```text
3 actions
```

### Evidence

Evidence 1: document Doc 3 (uscourts_mtd_2_24_md_03126_26.txt), proves component 1. 3 actions (local note: preamble, p. 1; L17)

```text
Defendants Advance Auto Parts, Inc. and Advance Stores Company, Incorporated should be preliminarily approved
```

Evidence 2: document Doc 3 (uscourts_mtd_2_24_md_03126_26.txt), proves component 1. 3 actions (local note: para. 2, p. 2; L28)

```text
The Court provisionally and preliminarily certifies the following California Settlement Subclass for settlement purposes only
```

Evidence 3: document Doc 3 (uscourts_mtd_2_24_md_03126_26.txt), proves component 1. 3 actions (local note: para. 2, p. 2; L30)

```text
All Settlement Class Members who are residents of California.
```

Evidence 4: document Doc 1 (uscourts_mtd_2_24_md_03126_0.txt), proves component 1. 3 actions (local note: p. 4; L61)

```text
consolidating the Advance Auto Parts actions in the Eastern District of North Carolina and Snowflake actions in the District of Montana
```

Evidence 5: document Doc 1 (uscourts_mtd_2_24_md_03126_0.txt), proves component 1. 3 actions (local note: p. 2; L27)

```text
the litigation in the two dockets consists of 45 actions pending in eight districts as listed on Schedules A and B. The Panel has been notified of 34 potential tag-along actions
```

Evidence 6: document Doc 1 (uscourts_mtd_2_24_md_03126_0.txt), proves component 1. 3 actions (local note: p. 4; L65)

```text
We are persuaded that the District of Montana is the appropriate transferee district for this MDL.
```

Evidence 7: document Doc 1 (uscourts_mtd_2_24_md_03126_0.txt), proves component 1. 3 actions (local note: p. 4; L66)

```text
Fourteen actions on the motion and twelve potential tag-along actions are pending in this district.
```

Evidence 8: document Doc 1 (uscourts_mtd_2_24_md_03126_0.txt), proves component 1. 3 actions (local note: footnote 5, p. 4; L67)

```text
Even counting all actions in the District of Montana as a single action and all actions in the Eastern District of North Carolina as a single action, there still are 42 related actions pending in twelve districts.
```

Evidence 9: document Doc 1 (uscourts_mtd_2_24_md_03126_0.txt), proves component 1. 3 actions (local note: Schedule B, p. 8; L141)

```text
IN RE ADVANCE STORES COMPANY, INCORPORATED, DATA BREACH
```

Evidence 10: document Doc 1 (uscourts_mtd_2_24_md_03126_0.txt), proves component 1. 3 actions (local note: Schedule B, p. 8; L150)

```text
CARR v. ADVANCE AUTO PARTS, INC.
```

### Necessary documents

- Tick Doc 1 (uscourts_mtd_2_24_md_03126_0.txt), role: Answer component
- Tick Doc 3 (uscourts_mtd_2_24_md_03126_26.txt), role: Used to identify

Leave unticked: Doc 2 (uscourts_mtd_2_24_md_03126_23.txt), Doc 4 (uscourts_mtd_2_24_md_03126_27.txt), Doc 5 (uscourts_mtd_2_24_md_03126_33.txt), Doc 6 (uscourts_mtd_2_24_md_03126_34.txt), Doc 7 (uscourts_mtd_2_24_md_03126_35.txt), Doc 8 (uscourts_mtd_2_24_md_03126_36.txt), Doc 9 (uscourts_mtd_2_24_md_03126_37.txt), Doc 10 (uscourts_mtd_2_24_md_03126_45.txt), Doc 11 (uscourts_mtd_2_24_md_03126_46.txt), Doc 12 (uscourts_mtd_2_24_md_03126_47.txt), Doc 13 (uscourts_mtd_2_24_md_03126_49.txt), Doc 14 (uscourts_mtd_2_24_md_03126_52.txt)

### Reasoning tags

Tick: Cross-document join, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Wrong jurisdiction or scope

How a careless solver fails: Picks the wrong entity or section

Where the trap sits:

```text
Doc 1, the transfer order, page 4, in the paragraph that picks the transferee court: "We are persuaded that the District of Montana is the appropriate transferee district for this MDL." Two sentences later it says "Fourteen actions on the motion and twelve potential tag-along actions are pending in this district." That is the only sentence in the order that gives a potential tag-along count for a particular district, and "this district" is Montana, the district named in the question's own opening clause.
```

The wrong answer a careless solver gives:

```text
12 actions. The solver either never pins down which district the question means, or reads "this district" as the district under discussion in the question, and copies the printed twelve. A solver who ties the California subclass to the "California class members" who sent Snowflake their consumer-privacy notice letter (Doc 5, Doc 8) takes Snowflake as the defendant, Montana as its consolidation district, and reaches the same 12.
```

Why the correct answer avoids it:

```text
Doc 3's California Settlement Subclass belongs to the class settlement with Advance Auto Parts, Inc. and Advance Stores Company, Incorporated, the only settlement order that creates a subclass, and Doc 1 page 4 places the consolidation of "the Advance Auto Parts actions in the Eastern District of North Carolina", a different district. The order never prints that district's tag-along count, so it has to be derived: footnote 5's 42 related actions in twelve districts, with Montana (26) and the Eastern District of North Carolina each counted as one, leave 40 elsewhere, so the Eastern District of North Carolina held 79 - 26 - 40 = 13 related actions, of which Schedule B lists ten on the motion, leaving 3.
```

(270 words across the three boxes; the form needs at least 150.)

#### Failure mode 2

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

Where the trap sits:

```text
Doc 1, footnote 5 on page 4: "Even counting all actions in the District of Montana as a single action and all actions in the Eastern District of North Carolina as a single action, there still are 42 related actions pending in twelve districts." Worked through with the page 2 totals (45 actions on the motion plus 34 potential tag-alongs), the footnote yields the number of all related actions in the Eastern District of North Carolina, actions on the motion and potential tag-alongs together, not the tag-alongs alone.
```

The wrong answer a careless solver gives:

```text
13 actions. The solver correctly derives 79 related actions in total, removes Montana's 26 and the other districts' 40, and stops at 79 - 26 - 40 = 13, reporting every related action pending in the Eastern District of North Carolina as if all of them were potential tag-alongs.
```

Why the correct answer avoids it:

```text
The question asks only for potential tag-along actions, which the order keeps separate from the actions on the motion (page 4 counts Montana's "Fourteen actions on the motion and twelve potential tag-along actions" separately). Schedule B on pages 7 and 8 lists ten Eastern District of North Carolina actions on the motion, from "IN RE ADVANCE STORES COMPANY, INCORPORATED, DATA BREACH" to "CARR v. ADVANCE AUTO PARTS, INC.", so the tag-alongs are 13 - 10 = 3.
```

(214 words across the three boxes; the form needs at least 150.)
