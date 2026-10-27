# Blind solver A (packet solver-1), q01 rev 0 (2026-10-08)

Role: blind-solver, fresh context, input = root, packet path, question text.
tested_sha256: b71780908eaf49fd31c0951ed3ff123922ded0fc3cd65eec45e8d4768993a9ea

Raw return (verbatim):

answer: 63.3%

confidence: high

path:
1. Settlement and preliminary approval: D03 (Doc. 176, filed 07/06/26), line 10: "the Court grants Plaintiff's motion for preliminary approval."
2. Who gets the automatic payment (D03 lines 63–64): "Members of the No Bankruptcy Group will receive an automatic payment of $100.00 without the need to submit a claim." and "Members of the Aged Bankruptcy Group will not receive these automatic payments." So "the members who also get the automatic payment" means the No Bankruptcy (NB) Group.
3. Money for valid claims and how it is split (D03 line 66): "Approximately $2,882,000.00 of the Settlement Fund is reserved for payments to settlement class members (including both No Bankruptcy Group members and Aged Bankruptcy Group members) who submit valid claims." Each payment is "calculated by dividing the class member's individual pro rata points by the aggregate total number of pro rata points assigned to all claiming class members." D03 line 73: "No Bankruptcy Group members who submit a valid claim will receive three pro rata points, and Aged Bankruptcy Group members who submit a valid claim will receive one individual pro rata point."
4. How the groups are defined (D03 footnotes 2–3, lines 67–68): both groups are set "according to the analysis conducted by Plaintiff's expert Jonathan Jaffe and set forth in his April 22, 2025 Supplemental Report."
5. Group sizes (D07, Doc. 157, decertification memo dated 12/02/25). Line 41 identifies "Jaffe Apr. 22, 2025 Report (Doc. No. 139-4, 'Jaffe April 2025 Report')". Line 47: the Thomson Reuters search led to "the elimination of 920 individuals ... resulting in a class list of 57,233 individuals." Line 49: "the 20,891 class members for whom Jaffe's search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters" (the NB Group). Line 61: "the 36,317 class members for whom Jaffe located a bankruptcy filing public record that preceded the applicable consumer report by more than ten years" (the Aged Bankruptcy (AB) Group).
   Cross-check: 20,891 × $100 = $2,089,100, which fits D03's "Approximately $2,100,000.00" set aside for automatic payments.
6. Calculation, assuming every member files a valid claim:
   - NB points = 3 × 20,891 = 62,673
   - AB points = 1 × 36,317 = 36,317
   - Total points = 98,990
   - NB share = 62,673 / 98,990 = 0.633125, or 63.3%
   - In dollars, this is about $1,824,665 of the roughly $2,882,000. The percentage does not depend on the dollar amount.

minimal_documents: D03 + D07. D03 is the only document with the settlement terms. D07 is the only document with class-wide counts for each group; none of the other documents can replace it.

readings:
- Total class list (57,233) minus 20,891 NB gives 36,342 AB: 62,673 / 99,015 = 63.30%, so 63.3%.
- 57,233 minus 36,317 AB gives 20,916 NB: 62,748 / 99,065 = 63.34%, so 63.3%.
- NB estimated as $2.1M / $100 = 21,000 (an approximate figure):
  - with 36,317 AB: 63,000 / 99,317 = 63.4%
  - with 57,233 − 21,000 = 36,233 AB: 63,000 / 99,233 = 63.5%
  These rely on the rounded dollar figure, so they are weaker.
- Superseded March 2025 counts from the PACER-only search (D07 line 47: 22,212 with no bankruptcy and 35,941 with an aged bankruptcy): 66,636 / 102,577 = 65.0%. These are not the April 22, 2025 report that the settlement definitions cite.

gaps:
- D03 itself gives no group counts. The counts come from D07's description of Jaffe's April 2025 results, and I am assuming the settlement class matches that list.
- 20,891 + 36,317 = 57,208, which is 25 fewer than the 57,233 class list. The documents don't explain the gap, and it doesn't change the answer at one decimal.
- D07 footnote 9 mentions two "test subject" records in the class list without saying which group they are in. The effect is negligible.
- The $2,882,000 is described as "Approximately."
- Coverage: I read all of D03, plus D07 lines 1–129 and 185–229. I did not fully read D01, D02, D04, D05, D06 or the rest of D07. I searched all seven documents for the group names (these appear only in D03), for the specific counts, and for every comma-formatted number. D05's figures are only 2024 sample-month estimates. D01, D02, D04 and D06 have no group counts. The packet is text only, with no PDFs to inspect.

contaminated: no. No answer, reasoning or source hint reached me. The harness-attached git status listed workspace file names only, with no content. I did not open the packet's question.txt.
