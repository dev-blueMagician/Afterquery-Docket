# Independent question-author, round 1 (2026-10-06)

Runtime: Claude Code question-author subagent (claude-opus-5-5), fresh context, brief listed the
target (medium), the measured mechanisms and the shapes already failed on this bundle. It read all
seven documents and the capture overview; it wrote no files. Return verbatim below. origin: claude.

---

I read all seven documents in full and checked the capture's overview. The bundle supports one mechanism that could plausibly reach Medium: the event-selects-edition trap, with the decoy in the event's own document. I'm returning three sketches built on it, ranked. None has been tested, and no files were written. **origin: claude** for all three.

## Hook inventory (for notes/hooks.md)

| Hook | Inputs | Decision |
|---|---|---|
| h1 | D03 L1981: a Gas Pipeline Advisory Committee meeting scheduled Nov 27–Dec 1, 2023 (only in D03). Idled-pipeline rule (RIN 2137-AF52) NPRM: D01 L787 `11/00/23`, D03 L2007 `02/00/24`, D04 L663 `12/00/24` | **i01** |
| h2 | D04 L711: train consist rule (RIN 2137-AF21) comment period ended `08/28/23` (only in D04). Same AF52 values as h1 | **i02**, an alternative to i01 (same gold) |
| h3 | D04 L415: repair-station drug-testing rule (RIN 2120-AK09) extended comment period ended `04/05/24` (only in D04). Self-insurance rule (RIN 2126-AC58) NPRM: D01 L581 `06/00/23`, D03 L1811 `10/00/24`, D04 L545 `06/00/25` | **i03** |

Rejected hooks:
- **Gas distribution NPRM of 09/07/23 as the event:** it is printed in both D03 and D04, so neither document is individually necessary.
- **Refund and train-crew final rules as events:** both are famous, so models recall the dates.
- **Train-crew "60 to 146 days" reconciliation:** general knowledge.
- **Comment-end conflicts for the refund rule (03/28/23 vs 11/21/22) and the leak-detection rule (07/17/23 vs 08/16/23):** no passage resolves them.
- **D06/D07 inconsistencies** ("credible" vs "clear and convincing"; "(a) and (c)" vs "(a) and (d)"; Dec 20 vs Dec 7, 2020): either one document answers alone or the documents conflict with no resolution.
- **D06+D07 date gaps from 2025–26:** two lookups plus a subtraction, joining unrelated events.
- **Section 610 plan + 14 CFR part 399:** D06 and D07 duplicate each other, and the plan structure is recalled closed-book.
- **RFI respondents vs commenters:** D07 alone answers.
- **D02 and D05:** no natural join to the DOT documents.
- **Using D02 (Nov 17, 2023) or D05 (Sept 2024) as the event:** an arbitrary cross-agency anchor, or the gold is in the latest edition with no decoy.

Date mapping was checked by script against the Federal Register dates: D01 Jul 27, 2023; D03 Feb 9, 2024; D04 Aug 16, 2024.
- Nov 27–Dec 1, 2023 falls 123–127 days after D01 and 70–74 days before D03.
- Aug 28, 2023 falls 32 days after D01 and 165 days before D03.
- Apr 5, 2024 falls 56 days after D03 and 133 days before D04.

---

**id: i01** (rank 1)
- **difficulty_target:** medium
- **question (44 words):** PHMSA scheduled an advisory committee meeting to discuss its gas pipeline leak detection and repair proposal. According to DOT's regulatory agenda current on the scheduled meeting dates, in what month and year was PHMSA expected to propose its rule on idled pipelines' operational status?
- **answer:** November 2023
- **facts:**
  - D03 L1981, inside entry 410 "Gas Pipeline Leak Detection and Repair [2137- AF51]": "has scheduled a Gas Pipeline Advisory Committee meeting to discuss the NPRM for November 27 through December 1, 2023"
  - D03 L5: FR date "Friday, February 9, 2024"
  - D01 L5: "Thursday, July 27, 2023"
  - D01 L777 "152. +Pipeline Safety: Pipeline Operational Status [2137-AF52]", L787 "NPRM.... 11/00/23"
  - D03 L1997/L2007 "NPRM.... 02/00/24"
  - D04 L653/L663 "NPRM.... 12/00/24"
  - The abstracts (D01 L781) define it as "an idled operational status"
- **documents:** D03, D01. D04 is not necessary; it holds only a decoy.
- **dependency:** D03 is the only source of the meeting dates. "Advisory Committee" elsewhere appears only for the airline committee (D04 L87, D03 L1605). D01 is the only source of `11/00/23` for AF52.
- **selected_levers:** Same series, right edition; Scatter the pieces.
- **lever_checks:**
  - Event-document route: AF52's entry 411 sits directly after the meeting sentence in entry 410 of D03 and gives **February 2024**.
  - Latest-edition route gives **December 2024**.
  - D03's own text puts the meeting in the future ("has scheduled"), and D04 L109 calls D03 the "Fall 2023" agenda. Both pull toward D03. The publication date (Feb 9, 2024) rules D03 out. Nothing in D03 ties the meeting to AF52, so the trap is untied.
- **arithmetic_check:** The script mapping above. Convention: the agenda current is the latest one published on or before the dates. Outside the bundle, I believe the Fall 2023 agenda went online on Dec 6, 2023; that gives the same answer.
- **removal test:**
  - Without D01: the remaining values are Feb 2024 and Dec 2024, so the answer is wrong and D01 is needed.
  - Without D03: the meeting dates are unknown. A high model could infer "after the July 2023 comment close, so late 2023, so the D01 value" and land on the gold. This is a **moderate risk**. Run the local removal probe on it.
- **closed-book:** The agenda's projected NPRM month is not public memory. Low risk. One residual: the answer matches the meeting's own month, so a forced guess could hit it.
- **shortcut_search:**
  - Searched: advisory committee, November 27, December 1, 2023, operational status, idled, leak detection, consist, and the RINs.
  - No passage links the meeting to AF52.
  - The overview for Doc 1 lists "November 2023" without linking it to AF52 (weak exposure). The overview for Doc 3 lists "Fall 2023".
  - Strongest route: meeting dates from D03, then compare Federal Register dates, then D01's AF52 entry. That is three lookups and one date comparison. The low model may follow it, which is the Easy risk.
- **tags:** Temporal alignment; Cross-document join; Entity resolution (the same rule under RIN 2137-AF52 in three editions).
- **completeness:** All seven documents read in full. The capture is complete with no gaps.
- **portfolio:** Same answer path as i02; submit only one of the two. i03 uses the same mechanism with a different event, target and gold.
- **unresolved:** The external release date (Dec 6) is not needed for the answer. Removal risk for D03. A less likely right-for-wrong-reason route: D03's AF51 line "Analyzing Comments 11/00/23". Possible variant: ask for the agenda's listed contact for AF52 instead (Palabrica in D01 L793; decoy Setzer in D03/D04). That removes the November coincidence but reads more like trivia. Fairness fallback wording, "most recently published agenda", probably makes it easier.

**id: i02** (rank 2; an alternative to i01)
- **difficulty_target:** medium
- **question (35 words):** When the comment period closed on PHMSA's proposal to require real-time train consist information, in what month and year did DOT's then-current regulatory agenda expect PHMSA to propose its rule on idled pipelines' operational status?
- **answer:** November 2023
- **facts:**
  - D04 L697 "173. Hazardous Materials: FAST Act Requirements for Real-Time Train Consist Information [2137-AF21]"
  - D04 L711 "NPRM.... 06/27/23 88 FR 41541 NPRM Comment Period End.... 08/28/23"
  - AF52 values as in i01
- **documents:** D04, D01
- **dependency:** AF21 appears only in D04. Nothing in D01 or D03 can date this event.
- **selected_levers:** Same series, right edition; Scatter the pieces.
- **lever_checks:**
  - Event-document route gives **December 2024**.
  - The D03 route gives **February 2024**.
  - Weakness: D04 was published 354 days after the event, so it does not look current. This trap is weaker than i01's.
- **arithmetic_check:** Aug 28, 2023 maps to D01 (script).
- **removal test:**
  - Without D01: the answer comes out wrong, so D01 is needed.
  - Without D04: a model that recalls PHMSA's June 2023 train consist NPRM infers a close in August 2023 and lands on the gold. This is a **moderate-high risk**, because the event is a public 2023 rulemaking date.
- **closed-book:** Low risk.
- **shortcut_search:** "consist" in a rail sense appears only in D04. No linking passage. Doc 1's overview "November 2023" applies here too.
- **tags:** Temporal alignment; Cross-document join; Entity resolution.
- **portfolio:** Shares the target and gold with i01. A variant targets the train crew final rule (gold Feb 2024 from D01 L637; decoys D03 Mar 2024 and D04 actual 04/09/24), but closed-book risk is about 20%.
- **unresolved:** Recall of the AF21 dates.

**id: i03** (rank 3)
- **difficulty_target:** medium
- **question (41 words):** When the extended comment period closed on FAA's proposal to require drug and alcohol testing of repair-station employees outside the United States, in what month and year did DOT's then-current regulatory agenda expect FMCSA to propose its self-insurance cost recovery rule?
- **answer:** October 2024
- **facts:**
  - D04 L401: AK09 title. D04 L415 "End of Extended Comment Period...... 04/05/24"
  - AC58 values: D03 L1811 `10/00/24`; D04 L545 `06/00/25`; D01 L581 `06/00/23` (stale at the event)
- **documents:** D04, D03
- **selected_levers:** Same series, right edition; Scatter the pieces.
- **lever_checks:**
  - Event-document route gives **June 2025**. D04 was published 133 days after the event, so it looks current.
  - D01's June 2023 is ruled out naturally as already past.
- **removal test:**
  - Without D03: the answer comes out wrong, so D03 is needed.
  - Without D04: D03 is the latest remaining agenda, and its AK09 entry shows an NPRM projected for Dec 2023, so a 2024 close is inferred and the gold follows. This is a **high risk**.
- **closed-book:** Low risk.
- **shortcut_search:** The event appears only in D04, with no linking passage.
- **tags:** Temporal alignment; Cross-document join; Entity resolution (AK09's title changes from "Certain Maintenance Provider" to "Certificated Repair Station").
- **portfolio:** AK09 was the subject of two earlier failed questions on this bundle. This sketch uses a different dependency, but the overlap is worth knowing.
- **unresolved:** Removal risk for D04.

---

**Assessment.** i01 is the only sketch whose event is both obscure and in a single document, and whose gold sits outside the latest edition that remains after the event document is removed. That structure is what passed elsewhere (aq-00964 q01, aq-00745 q09), and the local model underrated both of those.

The main threats to i01:
- **Too easy:** the Federal Register dates are prominent, so the low model may just compare them.
- **Document check:** the D03 removal risk described above.

I recommend a local removal probe on i01 with D03 treated as absent (forced guess with probability), then a platform quick test of i01 before write-up.

Beyond this trap family, I found no fair cross-document hook that holds up. The rest of the bundle offers lookups, unresolvable conflicts, general-knowledge dates, or single-document answers.

Files used: `D:\Dev\Docket\tasks\aq-docket-trial-03\text\D01.txt`, `D03.txt`, `D04.txt` (inputs); `D:\Dev\Docket\AQ-DOCKET-TRIAL-03_2026-10-05_1519.md` (overview check, lines 22–94).
