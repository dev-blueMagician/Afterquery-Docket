# q02 rev 0 - blind solver B (fresh blind-solver context, packet solver-2)

Date: 2026-10-05. tested_sha256: 596fc28dbf685c815794744aecfbea07a6e9f457c77b6b1911a3aa6df90f29f1
Task message: workspace root, packet path solver-2, exact question text only.

Raw return (verbatim):

**answer:** Pampa Norte (Spence) and NSW Energy Coal (NSWEC)

**confidence:** high

**path:**
1. **Divestment date.** D02, footnote under the production table (line 95): "The divestment of Carajás was completed on 2 April 2026." D01 line 123 gives the same date: "The divestment of Carajás to a subsidiary of CoreX Holding was completed on 2 April 2026".
2. **Guidance in force on 2 April 2026.** D01 is dated "22 April 2026", which is after the divestment. Its production table splits FY26 guidance into "Previous" and "Current" columns, with the note "Updates with respect to FY26 production guidance since the HY26 Results Announcement are shown in italics" (line 93). The Spence change is first announced in this release: "Production guidance for FY26 has been lowered to between 210 and 220 kt (from between 230 and 250 kt previously)" (line 107). So on 2 April the "Previous" column applied (D01 lines 79–92):
   - Escondida 1,200–1,275 kt
   - Pampa Norte (Spence) 230–250 kt
   - Copper South Australia 310–340 kt
   - Antamina 140–150 kt
   - Carajás "-" (no range)
   - WAIO 251–262 Mt (284–296 Mt on a 100% basis)
   - Samarco 7–7.5 Mt
   - BMA 18–20 Mt (36–40 Mt on a 100% basis)
   - NSWEC 14–16 Mt
3. **Which assets BHP operates.** D01 line 480 and D02 line 943 both say: "Our non-operated assets include Antamina, Resolution, Samarco and Vicuña." That leaves six operated assets with guidance: Escondida, Spence, Copper SA, WAIO, BMA and NSWEC.
4. **FY26 production (D02 lines 80–92; I re-added the quarterly figures in Appendix 2 and they match the totals):**
   - Escondida: 1,261.2 kt (328.9+317.2+303.2+311.9). Inside 1,200–1,275.
   - **Spence: 212.6 kt** (55.8+57.7+44.6+54.5). **Below 230–250 by 17.4 kt, so outside.**
   - Copper SA: 320.7 kt net (330.6 kt total). Inside 310–340 either way.
   - WAIO: 256.9 Mt (291.2 Mt at 100%). Inside both ranges.
   - BMA: 18.6 Mt (37.3 Mt at 100%). Inside both ranges.
   - **NSWEC: 16.4 Mt** (16,361 kt = 3,518+4,610+4,037+4,196). **Above 14–16, so outside.** D02 says this directly: "NSWEC exceeded the top end of its production guidance range" (line 70).
5. **Excluded:**
   - Antamina (151.5 kt against 140–150) and Samarco (7.8 Mt against 7–7.5) were both outside their ranges, but BHP does not operate them.
   - Carajás had no guidance range.
   - WA Nickel produced nothing and had no guidance.
   - The group copper and iron ore lines are commodity totals, not assets. Both were inside their ranges anyway (1,952.8 kt; 264.7 Mt).

**minimal_documents:** D01 and D02 together.
- D01 is the only source for the guidance in force before 22 April (Spence 230–250), but it only has production to March.
- D02 has full-year production, but only the post-update guidance (Spence 210–220).
- D03 and D04 are Freeport-McMoRan releases. A search for BHP, Carajás, Escondida, Spence and NSWEC found nothing in either, so they cannot replace D01 or D02.

**readings:**
- **Year-end guidance instead of 2 April guidance** (D01 "Current" / D02 "FY26e"): Spence's 212.6 kt falls inside 210–220, so the answer would be NSWEC only. This ignores the date the question specifies.
- **Including non-operated assets** with the 2 April ranges: the answer would add Antamina and Samarco, giving Spence, NSWEC, Antamina and Samarco.

**gaps:**
- The italics that mark guidance changes are lost in the text files. The Previous/Current columns and the "Lowered"/"Increased" labels still make the changes clear.
- No document in the packet confirms the date of the HY26 Results Announcement, or rules out a separate guidance change between that announcement and 22 April. Nothing suggests one, and D01 presents the Spence cut as new.
- I read D01 and D02 in full. D03 and D04 were only keyword-searched, not read in full.
- There are no layout files or original PDFs in this packet (the manifest lists text sources only).
- I deliberately did not open the packet's question.txt.

**contaminated:** no

Files used (as reported): solver-2\text\D01.txt, solver-2\text\D02.txt, solver-2\text\manifest.json
