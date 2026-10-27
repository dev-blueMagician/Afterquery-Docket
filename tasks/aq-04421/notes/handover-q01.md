# aq-04421 q01 hand-over

Generated 2026-10-14 by `python tools/check_questions.py tasks/aq-04421 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target hard, origin claude.
- tested_sha256 ea2e57ccd766b0f9a92faa32d5be891ea913637e24adddf7d02657a6c03246b1: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D03 = Doc 3, D04 = Doc 4.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN list-items: cannot determine every list boundary from the answer; use comma-separated quoted items or one bullet per item, then review the item count on the platform
  - WARN short-answer: the answer reads like a sentence or an explanation; give the value
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Which firms, if any, whose Entity List entries BIS added or corrected in September 2025 have premises on the same road as a site on BIS's October 2024 list of validated end users? List them alphabetically.
```

### Number of asks

1 ask

### Gold answer

```text
Hexin Xingtong Technology (Beijing) Co., Ltd., Jicun Semiconductor Technology (Shanghai) Co., Ltd. and Sino IC Technology Co., Ltd.
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 4, "Additions to the Entity List" and "Corrections to Entries on the Entity List"): the September 2025 rule adds new entities and corrects existing entries. Sino IC Technology Co., Ltd. and Jicun Semiconductor Technology (Shanghai) Co., Ltd. are among the entities it adds. Hexin Xingtong Technology (Beijing) Co., Ltd., "first added to the Entity List on May 9, 2024", is among the entries it corrects.
Step 2. Source input (Doc 3, Supplement No. 7): the October 2024 list names each validated end user and prints the address of every site it may receive items at. The table prints its columns side by side, so an address can run on with item codes from the next column in the middle of it.
Step 3. Source input (Doc 4, Entity List table, and Doc 3, Supplement No. 7): Sino IC Technology's address is on Guoshoujing Road in the Shanghai free trade zone. Shanghai Huahong Grace, a validated end user, has its HFab 2 site on Guoshoujing Road, Zhangjiang Hi-Tech Park, Shanghai. Same road, so Sino IC Technology qualifies (third component).
Step 4. Source input (Doc 4, Entity List table, and Doc 3, Supplement No. 7): one of Jicun's addresses is on "Feila Road" in the China (Shanghai) Pilot Free Trade Zone. Lam Research Service, a validated end user, has a bonded warehouse site on "Fei La Road", Waigaoqiao Free Trade Zone, Shanghai. Neither document says so, but these are two spellings of one road name in one city, so Jicun qualifies (second component).
Step 5. Source input (Doc 4, Entity List table, and Doc 3, Supplement No. 7): one of Hexin Xingtong's addresses is on Bi Bo Road, Shanghai. Lam Research Service's Shanghai office is in Hua Hong Science & Technology Park, Zhangjiang Hi-Tech Park; Doc 3 prints its road as "Bi" and then, after two item codes from the next column, "Bo Road". Read without the item codes, the office is on Bi Bo Road, so Hexin Xingtong qualifies (first component).
Step 6. Decoy (Doc 4 and Doc 3): Beijing Tsingke Biotech Co., Ltd., an added firm, has addresses on Jinghai 3rd Road and Jinghai 4th Road in Beijing, while Lam's Beijing warehouse is on Jinghai Second Road. These are three different roads, so Beijing Tsingke is left out.
Step 7. Final answer (Doc 3 and Doc 4): no other road in Doc 3's site addresses appears among the addresses of the entries that Doc 4 adds or corrects. In alphabetical order: Hexin Xingtong Technology (Beijing) Co., Ltd., Jicun Semiconductor Technology (Shanghai) Co., Ltd. and Sino IC Technology Co., Ltd.
```

### Answer components

Component 1

```text
Hexin Xingtong Technology (Beijing) Co., Ltd.
```

Component 2

```text
Jicun Semiconductor Technology (Shanghai) Co., Ltd.
```

Component 3

```text
Sino IC Technology Co., Ltd.
```

### Evidence

Evidence 1: document Doc 4 (fr_2025_17893.txt), proves component 1. Hexin Xingtong Technology (Beijing) Co., Ltd. (local note: Corrections to Entries on the Entity List)

```text
``Hexin Xingtong Technology (Beijing) Co., Ltd.,'' first added to the Entity List on May 9, 2024
```

Evidence 2: document Doc 4 (fr_2025_17893.txt), proves component 1. Hexin Xingtong Technology (Beijing) Co., Ltd. (local note: Entity List table, Hexin Xingtong row)

```text
Building 8, No. 912 Bi Bo Road,
```

Evidence 3: document Doc 3 (fr_2024_22587.txt), proves component 1. Hexin Xingtong Technology (Beijing) Co., Ltd. (local note: Supplement No. 7, Lam Research Service, double-asterisk sites)

```text
These Items Authorized ** Lam Research Service
```

Evidence 4: document Doc 3 (fr_2024_22587.txt), proves component 1. Hexin Xingtong Technology (Beijing) Co., Ltd. (local note: Supplement No. 7, Lam Research Service, double-asterisk sites)

```text
Destinations Identified 1st Floor, Area C, Hua by double asterisks Hong Science &
```

Evidence 5: document Doc 3 (fr_2024_22587.txt), proves component 1. Hexin Xingtong Technology (Beijing) Co., Ltd. (local note: Supplement No. 7, Lam Research Service, double-asterisk sites)

```text
Technology Park, 177 Bi 2B350.d, 2B350.g, Bo Road, Zhangjiang Hi-
```

Evidence 6: document Doc 4 (fr_2025_17893.txt), proves component 2. Jicun Semiconductor Technology (Shanghai) Co., Ltd. (local note: Additions to the Entity List)

```text
The ERC determined to add GMC Semiconductor Technology (Wuxi) Co., Ltd.; and Jicun Semiconductor Technology (Shanghai) Co., Ltd., under the destination of China, to the Entity List.
```

Evidence 7: document Doc 4 (fr_2025_17893.txt), proves component 2. Jicun Semiconductor Technology (Shanghai) Co., Ltd. (local note: Entity List table, Jicun Semiconductor row)

```text
Room 115, 1F, No. 45, Feila Road,
```

Evidence 8: document Doc 4 (fr_2025_17893.txt), proves component 2. Jicun Semiconductor Technology (Shanghai) Co., Ltd. (local note: Entity List table, Jicun Semiconductor row)

```text
China (Shanghai) Pilot Free Trade
```

Evidence 9: document Doc 3 (fr_2024_22587.txt), proves component 2. Jicun Semiconductor Technology (Shanghai) Co., Ltd. (local note: Supplement No. 7, Lam Research Service row)

```text
Lam Research Service These Items Authorized * Lam Research
```

Evidence 10: document Doc 3 (fr_2024_22587.txt), proves component 2. Jicun Semiconductor Technology (Shanghai) Co., Ltd. (local note: Supplement No. 7, Lam Research Service row)

```text
Bonded Warehouse), c/o
```

Evidence 11: document Doc 3 (fr_2024_22587.txt), proves component 2. Jicun Semiconductor Technology (Shanghai) Co., Ltd. (local note: Supplement No. 7, Lam Research Service row)

```text
No. 55, Fei La Road,
```

Evidence 12: document Doc 3 (fr_2024_22587.txt), proves component 2. Jicun Semiconductor Technology (Shanghai) Co., Ltd. (local note: Supplement No. 7, Lam Research Service row)

```text
Waigaoqiao Free Trade
```

Evidence 13: document Doc 3 (fr_2024_22587.txt), proves component 2. Jicun Semiconductor Technology (Shanghai) Co., Ltd. (local note: Supplement No. 7, Lam Research Service row)

```text
Shanghai, China 200131.
```

Evidence 14: document Doc 4 (fr_2025_17893.txt), proves component 3. Sino IC Technology Co., Ltd. (local note: Additions to the Entity List)

```text
Sino IC Technology Co., Ltd., under the destination of China
```

Evidence 15: document Doc 4 (fr_2025_17893.txt), proves component 3. Sino IC Technology Co., Ltd. (local note: Entity List table, Sino IC Technology row)

```text
No. 351, Guoshoujing Road, China
```

Evidence 16: document Doc 4 (fr_2025_17893.txt), proves component 3. Sino IC Technology Co., Ltd. (local note: Entity List table, Sino IC Technology row)

```text
(Shanghai) Pilot Free Trade Zone,
```

Evidence 17: document Doc 3 (fr_2024_22587.txt), proves component 3. Sino IC Technology Co., Ltd. (local note: Supplement No. 7, Shanghai Huahong Grace row)

```text
1C350.c.4, 1C350.d.14, Shanghai Huahong Grace 78 FR 32981, 6/3/
```

Evidence 18: document Doc 3 (fr_2024_22587.txt), proves component 3. Sino IC Technology Co., Ltd. (local note: Supplement No. 7, Shanghai Huahong Grace row)

```text
Corporation--HFab 2, 668 3B001.e, 3B001.f, Guoshoujing Road,
```

Evidence 19: document Doc 3 (fr_2024_22587.txt), proves component 3. Sino IC Technology Co., Ltd. (local note: Supplement No. 7, Shanghai Huahong Grace row)

```text
Zhangjiang Hi-Tech Park, 5B002, and 5E002 Shanghai 201203 China.
```

Evidence 20: document Doc 4 (fr_2025_17893.txt), proves component 2. Jicun Semiconductor Technology (Shanghai) Co., Ltd. (local note: Entity List table, Beijing Tsingke Biotech row)

```text
Jinghai 3rd Road, Beijing, China; and Room 401, Building 5, Jinghai
```

Evidence 21: document Doc 3 (fr_2024_22587.txt), proves component 2. Jicun Semiconductor Technology (Shanghai) Co., Ltd. (local note: Supplement No. 7, Lam Research Service row)

```text
28, Jinghai Second Road,
```

### Necessary documents

- Tick Doc 3 (fr_2024_22587.txt), role: Answer component
- Tick Doc 4 (fr_2025_17893.txt), role: Answer component

Leave unticked: Doc 1 (fr_2023_00888.txt), Doc 2 (fr_2024_06067.txt), Doc 5 (fr_2026_10712.txt), Doc 6 (fr_2026_14132.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Entity resolution

Leave unticked: Temporal alignment, Unit normalization, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Document convention

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Document convention: Doc 3's table runs its columns together, so Lam's Shanghai office reads "177 Bi 2B350.d, 2B350.g, Bo Road". Matching road names without separating the columns misses Bi Bo Road and gives Jicun and Sino IC only; Hexin Xingtong, on Bi Bo Road (Doc 4), completes the list.
```

(49 / 50 words.)
