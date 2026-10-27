# Blind solver B (packet solver-2), q01 rev 0 (2026-10-08)

Role: blind-solver, fresh context, input = root, packet path, question text.
tested_sha256: b71780908eaf49fd31c0951ed3ff123922ded0fc3cd65eec45e8d4768993a9ea

Raw return (verbatim):

answer: 63.3%

confidence: high

path:
1. **D03, Doc. 176 (preliminary approval memorandum, 07/06/26), p. 5.** Automatic payments: "Members of the No Bankruptcy Group will receive an automatic payment of $100.00 without the need to submit a claim." "Approximately $2,100,000.00 … is reserved to provide No Bankruptcy Group class members with automatic payments." "Members of the Aged Bankruptcy Group will not receive these automatic payments." So the members who also get the automatic payment are the No Bankruptcy Group (NB).
2. **D03, pp. 5–6.** Money for valid claims: "Approximately $2,882,000.00 of the Settlement Fund is reserved for payments to settlement class members (including both No Bankruptcy Group members and Aged Bankruptcy Group members) who submit valid claims." Each payment is the member's "individual pro rata points by the aggregate total number of pro rata points assigned to all claiming class members." "No Bankruptcy Group members who submit a valid claim will receive three pro rata points, and Aged Bankruptcy Group members who submit a valid claim will receive one individual pro rata point." The $2,882,000 cancels out, so NB's share is 3·NB / (3·NB + AB).
3. **D03, p. 5, footnotes 2–3.** Both groups are defined "according to the analysis conducted by … Jonathan Jaffe and set forth in his April 22, 2025 Supplemental Report." NB means "no locatable public record of a bankruptcy with the same nine-digit SSN." The Aged Bankruptcy Group (AB) means the only such record "was filed more than ten years prior to the date of that report."
4. **D07, Doc. 157 (12/02/25), pp. 4–5.** These give the group sizes after Jaffe's April 2025 Thomson Reuters search:
   - "the 20,891 class members for whom Jaffe's search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters" (NB).
   - "the 36,317 class members for whom Jaffe located a bankruptcy filing public record that preceded the applicable consumer report by more than ten years" (AB).
   - Cross-check: 20,891 × $100 = $2,089,100, which matches the "approximately $2,100,000" reserve.
5. **Calculation:**
   - NB points: 3 × 20,891 = 62,673.
   - AB points: 36,317.
   - Total points: 98,990.
   - NB share: 62,673 / 98,990 = 0.63312, which rounds to **63.3%** (about $1.82M of $2.882M).
   - I checked the arithmetic twice.

The figures in the original docs/ files match the text files: uscourts_paed_2_22_cv_00048_10.txt lines 62, 64, 71; uscourts_paed_2_22_cv_00048_8.txt lines 45, 47, 56, 59, 61.

minimal_documents: D03 + D07. Neither works alone. D03 has the points rule and group definitions but no count for the Aged Bankruptcy Group. D07 has the counts but not the settlement terms. I found no replacement in the rest of the packet: D05 has only single-month projections from the class-certification stage, and D04 has the 22,141 June 2022 files, which are not class counts.

readings:
- **Total class list instead of the AB count.** D07 also gives a class list of 57,233 (22,212 + 35,941 − 920). Then AB = 57,233 − 20,891 = 36,342, and 62,673 / 99,015 = 63.297%, which is still 63.3%.
- **NB count implied by the rounded reserve.** If NB = $2,100,000 / $100 = 21,000: with AB = 36,317, the share is 63,000 / 99,317 = 63.4%; with AB = 36,233, it is 63.5%. This is less precise because the reserve is described as "approximately."
- **March 2025 counts.** Using the pre-Thomson-Reuters figures of 22,212 and 35,941 gives 65.0%. This conflicts with the settlement's definitions, which use the April 22, 2025 report.
- **Estimated payments instead of points.** Weighting by the expected payments of about $1,000 and $350 gives 62.2%. I don't think this is defensible, because those estimates assume typical claim rates, not every member claiming.

gaps:
- 20,891 + 36,317 = 57,208, which is 25 fewer than the 57,233 class list. The documents don't explain the gap, and it doesn't change the answer at one decimal place.
- The packet gives no count of people who opted out after the May 2025 certification notice.
- The packet includes the court's summary but not the settlement agreement itself (Doc. 172-2).
- D07 footnote 9 mentions two "test subject" records in the class list; they have no effect at this precision.
- Coverage: I read D01, D02, D03, D04, D06 and D07 in full. For D05 I read lines 1–160 and 300–329, plus searches of the whole file for settlement terms and numbers. There were no PDFs; the sources are .txt files.

contaminated: no. The auto-attached git status listed workspace file names only; it contained no answer, reasoning or source hints.
