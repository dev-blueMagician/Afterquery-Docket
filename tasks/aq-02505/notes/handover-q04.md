# aq-02505 q04 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02505 --handover --q q04` from questions/q04.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 e5563dcdf1df206cd884939377863e39622733600c408b758c0ea441331a0874: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D04 = Doc 4, D06 = Doc 6.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 1: Doc 2 doesn't mention 107. expected false alarm: Doc 2 states it only in words ("One hundred and seven", character 36,837) in a passage quoted as evidence, and the form matches digits (aq-02505 q01); no wording clears it, so say so with the hand-over
  - WARN form-numbers: Step 7: Doc 6 doesn't mention 187. expected false alarm: Doc 6 states it only in words ("One hundred and eighty-seven", character 39,816) in a passage quoted as evidence, and the form matches digits (aq-02505 q01); no wording clears it, so say so with the hand-over
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q04.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
To one decimal place, what percentage of the entities first placed on the UFLPA Entity List from November 25, 2024 through August 3, 2026 mine or source copper or lithium?
```

### Number of asks

1 ask

### Gold answer

```text
4.6%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, dates and appendix 1): the notice publishes the UFLPA Entity List "updated as of November 25, 2024", superseding the list published on November 1, 2024. The list as of November 25, 2024 specifies "One hundred and seven entities" (107).

Step 2. Source input (Doc 2, summary and appendix 1): that update adds five entities (5) to the section 2(d)(2)(B)(ii) list and twenty-five entities (25) to the section 2(d)(2)(B)(v) list, and makes no removals.

Step 3. Source input (Doc 2, Xinjiang Daqo New Energy paragraph): one of the twenty-five, Xinjiang Daqo New Energy Co., Ltd., "was first listed on the UFLPA Entity List, pursuant to Section 2(d)(2)(B)(i), in June 2022", so it was not first placed on November 25, 2024. No other addition of that update is on another sub-list.

Step 4. Calculation (Doc 2 and Doc 6): sub-list additions in the November 25, 2024 update: 5 + 25 = 30.

Step 5. Calculation (Doc 2 and Doc 6): entities first placed on the list by that update, leaving out Xinjiang Daqo: 30 - 1 = 29.

Step 6. Calculation (Doc 2 and Doc 6): entities on the list before the November 25, 2024 update: 107 - 29 = 78.

Step 7. Source input (Doc 6, summary and appendix 1): the list as of August 3, 2026 specifies "One hundred and eighty-seven entities" (187); its summary reports only new entities and two name corrections.

Step 8. Calculation (Doc 2 and Doc 6): entities first placed on the list from November 25, 2024 through August 3, 2026: 187 - 78 = 109.

Step 9. Source input (Doc 2, appendix 1 and the Xinjiang Nonferrous Metals Industry Group paragraph): one of the five section 2(d)(2)(B)(ii) additions, Xinjiang Nonferrous Metals Industry Group Co., Ltd., "mines, smelts, and processes raw metallic materials, including copper, lithium", so it qualifies. Xinjiang Habahe Ashele Copper Co., Ltd. is already on the section 2(d)(2)(B)(ii) list as of November 25, 2024 without being one of those five, so it was first placed on the list earlier.

Step 10. Source input (Doc 4, appendix 1 and descriptions): the January 15, 2025 update adds Zijin Mining Group Co., Ltd., "principally engaged in the exploration and extraction of metals, including zinc, copper", which is on no earlier list and qualifies. It also adds Xinjiang Habahe Ashele Copper to the section 2(d)(2)(B)(v) list, a second sub-list for an entity already listed, so that entity is not counted. Xinjiang Zijin Zinc Industry and Xinjiang Zijin Nonferrous Metals handle zinc only.

Step 11. Source input (Doc 6, appendix 1 and the Baiyin, SDIC and Xinjiang Tianhongji paragraphs): the August 3, 2026 update adds Baiyin Nonferrous Group Co., Ltd. and Xinjiang Baiyin Mining Development Co., Ltd., which "are sourcing copper and molybdenum from the XUAR", and SDIC Xinjiang Lithium Industry Co., Ltd., which with its parent sources "potassium and lithium, respectively". These three qualify. The parent, SDIC Xinjiang Luobupo Potash, sources potassium, and Xinjiang Tianhongji Technology "sources carbon materials" for battery materials, so neither qualifies.

Step 12. Calculation (Doc 2, Doc 4 and Doc 6): qualifying entities across the three updates: 1 + 1 + 3 = 5.

Step 13. Calculation (Doc 2, Doc 4 and Doc 6): qualifying entities as a share of those first placed in the period, in percent, rounded to one decimal place: 5 / 109 = 4.6%.
```

### Answer components

Component 1

```text
4.6%
```

### Evidence

Evidence 1: document Doc 2 (fr_2024_27337.txt), proves component 1. 4.6% (local note: dates, L23)

```text
This notice announces the publication and availability of the UFLPA Entity List updated as of November 25, 2024
```

Evidence 2: document Doc 2 (fr_2024_27337.txt), proves component 1. 4.6% (local note: appendix 1, L77)

```text
This notice supersedes the UFLPA Entity List published in the Federal Register on November 1, 2024 (89 FR 87391).
```

Evidence 3: document Doc 2 (fr_2024_27337.txt), proves component 1. 4.6% (local note: summary, L21)

```text
This update adds five entities to the section 2(d)(2)(B)(ii) list of the UFLPA and twenty-five entities to the section 2(d)(2)(B)(v) list of the UFLPA.
```

Evidence 4: document Doc 2 (fr_2024_27337.txt), proves component 1. 4.6% (local note: Xinjiang Daqo New Energy paragraph, L160)

```text
This company was first listed on the UFLPA Entity List, pursuant to Section 2(d)(2)(B)(i), in June 2022.
```

Evidence 5: document Doc 2 (fr_2024_27337.txt), proves component 1. 4.6% (local note: appendix 1, L164)

```text
No removals are being made to the UFLPA Entity List at this time.
```

Evidence 6: document Doc 2 (fr_2024_27337.txt), proves component 1. 4.6% (local note: appendix 1, L165)

```text
One hundred and seven entities that meet the criteria set forth in the four required lists
```

Evidence 7: document Doc 2 (fr_2024_27337.txt), proves component 1. 4.6% (local note: Xinjiang Nonferrous Metals Industry Group description, L119)

```text
Xinjiang Nonferrous Metals Industry Group Co., Ltd. is a company based in Urumqi, Xinjiang Uyghur Autonomous Region that mines, smelts, and processes raw metallic materials, including copper, lithium, beryllium, nickel, manganese, and gold.
```

Evidence 8: document Doc 2 (fr_2024_27337.txt), proves component 1. 4.6% (local note: section 2(d)(2)(B)(ii) list as of November 25, 2024, L203)

```text
Xinjiang Habahe Ashele Copper Co., Ltd. (also known as Ashele Copper)
```

Evidence 9: document Doc 4 (fr_2025_00901.txt), proves component 1. 4.6% (local note: appendix 1, L84)

```text
This update also adds thirty-five entities to the section 2(d)(2)(B)(v) list of the UFLPA
```

Evidence 10: document Doc 4 (fr_2025_00901.txt), proves component 1. 4.6% (local note: Zijin Mining Group description, L197)

```text
Zijin Mining Group Co., Ltd. is a global mining company based in Shanghang County, Fujian that is principally engaged in the exploration and extraction of metals, including zinc, copper, lead, silver, gold, iron ore, and sulfuric acid.
```

Evidence 11: document Doc 6 (fr_2026_15628.txt), proves component 1. 4.6% (local note: summary, L21)

```text
This update adds forty-three new entities to the UFLPA Entity List, two of which appear on two separate sub-lists.
```

Evidence 12: document Doc 6 (fr_2026_15628.txt), proves component 1. 4.6% (local note: appendix 1, L76)

```text
The UFLPA Entity List as of August 3, 2026 is available in this appendix
```

Evidence 13: document Doc 6 (fr_2026_15628.txt), proves component 1. 4.6% (local note: appendix 1, L182)

```text
One hundred and eighty-seven entities that meet the criteria set forth in the four required lists
```

Evidence 14: document Doc 6 (fr_2026_15628.txt), proves component 1. 4.6% (local note: Baiyin paragraph, L135)

```text
Baiyin Nonferrous owns and sources material from at least one mine in the XUAR, which is operated by its wholly-owned subsidiary, Xinjiang Baiyin Mining Development Co., Ltd.
```

Evidence 15: document Doc 6 (fr_2026_15628.txt), proves component 1. 4.6% (local note: Baiyin paragraph, L135)

```text
that Baiyin Nonferrous and Xinjiang Baiyin are sourcing copper and molybdenum from the XUAR
```

Evidence 16: document Doc 6 (fr_2026_15628.txt), proves component 1. 4.6% (local note: SDIC paragraph, L153)

```text
SDIC Lop Nur and SDIC Lithium source potassium and lithium, respectively, from the brine from the Lop Nur Salt Lakebed
```

### Necessary documents

- Tick Doc 2 (fr_2024_27337.txt), role: Answer component
- Tick Doc 4 (fr_2025_00901.txt), role: Answer component
- Tick Doc 6 (fr_2026_15628.txt), role: Answer component

Leave unticked: Doc 1 (fr_2024_26481.txt), Doc 3 (fr_2024_29238.txt), Doc 5 (fr_2026_11296.txt), Doc 7 (fr_2026_17926.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Conditional filter, Entity resolution, Aggregation

Leave unticked: Unit normalization

### Targeted failure modes

#### Failure mode 1

Trap: Out-of-range period

How a careless solver fails: Uses the wrong period or date

#### Failure mode 2

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Out-of-range period: Doc 4 adds Ashele Copper in January 2025, but Doc 2's November 25, 2024 list already carries it; counting it gives 6 of 109, 5.5%. Look-alike measure: Doc 2's thirty sub-list additions include Xinjiang Daqo, listed since June 2022; thirty new entities gives 5 of 110, 4.5%.
```

(49 / 50 words.)
