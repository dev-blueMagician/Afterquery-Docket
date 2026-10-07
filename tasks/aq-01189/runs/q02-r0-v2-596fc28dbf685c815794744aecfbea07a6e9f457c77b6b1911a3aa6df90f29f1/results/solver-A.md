# q02 rev 0 - blind solver A (fresh blind-solver context, packet solver-1)

Date: 2026-10-05. tested_sha256: 596fc28dbf685c815794744aecfbea07a6e9f457c77b6b1911a3aa6df90f29f1
Task message: workspace root, packet path solver-1, exact question text only.

Raw return (verbatim):

answer: Pampa Norte (Spence) and NSW Energy Coal (NSWEC)

confidence: high

path:
1. **Divestment date.** D01 (Q3 FY26 review, 22 April 2026), "Other copper" section: "The divestment of Carajás to a subsidiary of CoreX Holding was completed on 2 April 2026". D02 says the same in footnote 1 to its production table and in Appendix 2.
2. **Guidance in force on 2 April 2026.** D01 came out on 22 April, after that date. Its FY26 guidance table has "Previous" and "Current" columns, with the note "Updates with respect to FY26 production guidance since the HY26 Results Announcement are shown in italics." The 22 April release is where the changes are announced: Spence "has been lowered to between 210 and 220 kt (from between 230 and 250 kt previously)", and for Antamina "We now expect … between 150 and 160 kt (from 140 to 150 kt previously)". So the "Previous" column applied on 2 April:
   - Escondida: 1,200–1,275 kt
   - Pampa Norte (Spence): 230–250 kt
   - Copper South Australia: 310–340 kt
   - Antamina: 140–150 kt
   - Carajás: "-" (no guidance)
   - WAIO: 251–262 Mt (284–296 Mt on a 100% basis)
   - Samarco: 7–7.5 Mt
   - BMA: 18–20 Mt (36–40 Mt on a 100% basis)
   - NSWEC: 14–16 Mt
3. **Operated filter.** Both D01 and D02 say: "Our non-operated assets include Antamina, Resolution, Samarco and Vicuña." That removes Antamina and Samarco.
4. **FY26 production vs 2 April guidance.** From D02's production table and Appendix 2:
   - Escondida: 328.9+317.2+303.2+311.9 = 1,261.2 kt. Inside the range.
   - Spence: 55.8+57.7+44.6+54.5 = 212.6 kt. Below 230, so **outside**.
   - Copper SA: net copper 72.6+75.1+82.8+90.2 = 320.7 kt. Inside.
   - WAIO: 256,877 kt = 256.9 Mt (291.2 Mt on a 100% basis). Inside on both bases.
   - BMA: 18,626 kt = 18.6 Mt (37.3 Mt on a 100% basis). Inside on both bases.
   - NSWEC: 3,518+4,610+4,037+4,196 = 16,361 kt = 16.4 Mt. Above 16, so **outside**. D02 confirms: "NSWEC exceeded the top end of its production guidance range."
5. **Excluded candidates.**
   - Antamina (151.5 kt, above 140–150) and Samarco (7.84 Mt, above 7–7.5) are outside the range but non-operated.
   - Carajás produced 6.8 kt but had no guidance range.
   - WA Nickel was suspended and had no guidance.
   - Group copper (1,952.8 kt) and iron ore (264.7 Mt) are totals, not assets, and are inside their ranges anyway.

minimal_documents: D01 + D02. D01 is the only source for the guidance in force before 22 April; D02 is the only source for full-year FY26 production. Neither can replace the other. D03 and D04 are Freeport-McMoRan releases and don't mention BHP, Carajás or any of these assets.

readings:
- Using the post-22 April guidance (D01 "Current", which matches D02's FY26e column, Spence 210–220): only NSWEC, since 212.6 kt is inside 210–220.
- Ignoring the "BHP-operated" filter, with 2 April guidance: Spence, NSWEC, Antamina, Samarco.
- Ignoring the filter, with current guidance: NSWEC and Samarco.

gaps:
- The packet doesn't give the date of the HY26 Results Announcement. It also shows no guidance update between that announcement and 22 April. My conclusion that "Previous" applied on 2 April rests on the 22 April wording ("has been lowered", "now expect") and the italics note.
- The italics that marked the updates are lost in the text, but the Previous/Current columns and the narrative make the changes explicit.
- There are no PDFs in the packet; the sources are .txt and the docs/ copies match the text/ rows.
- I read D01 and D02 in full. I checked D03 and D04 only by keyword search (BHP, Carajás, the asset names, CoreX), not full reading.

contaminated: no

Files used (as reported): solver-1\text\D01.txt, solver-1\text\D02.txt
