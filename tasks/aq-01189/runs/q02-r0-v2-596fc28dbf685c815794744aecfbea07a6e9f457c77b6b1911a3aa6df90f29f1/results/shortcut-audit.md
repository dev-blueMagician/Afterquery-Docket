# q02 rev 0 - shortcut auditor (fresh shortcut-auditor context, packet shortcut)

Date: 2026-10-05. tested_sha256: 596fc28dbf685c815794744aecfbea07a6e9f457c77b6b1911a3aa6df90f29f1
Task message: workspace root, packet path shortcut, exact question text only.

Raw return (verbatim):

**answer:** Pampa Norte (Spence) and NSW Energy Coal (NSWEC). Both came in outside the FY26 production guidance that was in force on 2 April 2026, the day the Carajás divestment completed.

**verdict:** clear

**shortest_path:**
1. **Divestment date.** D01 line 123 says: "The divestment of Carajás to a subsidiary of CoreX Holding was completed on 2 April 2026". D02 repeats this at lines 95, 348 and 477.
2. **Guidance in force that day.** D01 was released on 22 April 2026 (lines 17 and 45), which is after 2 April. Its guidance table (lines 75–90) has separate "Previous" and "Current" columns. Line 93 says: "Updates with respect to FY26 production guidance since the HY26 Results Announcement are shown in italics." So the "Previous" column is what applied on 2 April. Line 107 confirms the Spence change: "lowered to between 210 and 220 kt (from between 230 and 250 kt previously)". The ranges in force on 2 April were:
   - Escondida: 1,200–1,275 kt
   - Spence: 230–250 kt
   - Copper South Australia: 310–340 kt
   - WAIO: 251–262 Mt (284–296 Mt on a 100% basis)
   - BMA: 18–20 Mt (36–40 Mt on a 100% basis)
   - NSWEC: 14–16 Mt
   - Carajás: "-" (no guidance)
3. **Operated assets only.** D01 line 480 and D02 line 943 both say: "Our non-operated assets include Antamina, Resolution, Samarco and Vicuña." Those are excluded.
4. **FY26 production (D02 lines 80–92, matching the detailed tables at lines 375, 387, 410, 485, 512 and 522):**
   - Escondida: 1,261.2 kt, within range
   - **Spence: 212.6 kt, below 230 (17.4 kt short)**
   - Copper South Australia: 320.7 kt, within range
   - WAIO: 256.9 Mt (291.2 Mt on a 100% basis), within range
   - BMA: 18.6 Mt (37.3 Mt on a 100% basis), within range
   - **NSWEC: 16,361 kt (16.4 Mt), above 16 (0.361 Mt over).** D02 line 187 states this directly: "NSWEC exceeding the top end of production guidance in FY26."

**sufficient_documents:** D01 and D02 are both needed, and there is no alternative pair.
- D02 only shows the revised Spence range (210–220). The string "230 – 250" does not appear anywhere in D02.
- D01 has no full-year production figures.
- D03 and D04 are Freeport-McMoRan releases with no mentions of BHP, Carajás or any BHP asset.

**searches:**
- I read D01 and D02 in full, plus the manifest. I did not open question.txt.
- I searched D03 and D04 for BHP, Carajás, CoreX, Spence, NSWEC, Escondida, Antamina, Samarco, Pampa, WAIO and BMA. There were no hits.
- I searched D02 for "230", "250", lowered, previous, exceed, outside, top end and bottom end. The only hits were Spence's FY27 range of 210–230, the unit cost table and the NSWEC sentence.
- I checked the key rows in the docs/ originals and they match text/ exactly: the Spence, NSWEC, Antamina and Samarco guidance rows, the "2 April 2026" footnotes, the HY26 note and the non-operated disclaimer.
- Coverage: every packet document was either read in full or searched for the relevant terms.

**readings/gaps:**
- **Using the guidance revised on 22 April** (D01 "Current", or D02's FY26e column) gives NSWEC only, because Spence's 212.6 kt falls inside 210–220. That is wrong for this question, since the revision came after 2 April.
- **Ignoring the "BHP-operated" condition** adds Antamina (151.5 kt against 140–150) and Samarco (7.8 Mt against 7–7.5).
- **Combining both mistakes** gives NSWEC and Samarco.
- **Naming:** the guidance row is labelled "Pampa Norte (Spence)". Pampa Norte also includes Cerro Colorado, which is in care and maintenance.
- **Gap:** the HY26 Results Announcement itself is not in the packet. Treating "Previous" as the guidance on 2 April relies on D01's note. Nothing in the packet suggests a revision between HY26 and 22 April.
- **Difficulty risk, not a shortcut:** D02's NSWEC sentence gives away half the answer. The Spence half needs D01's earlier range plus the reasoning that 2 April comes before 22 April. Neither document alone gives the complete answer.

Files used (as reported): shortcut\text\D01.txt, shortcut\text\D02.txt
