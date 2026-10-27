# Blind solver B (packet solver-2), q01 rev 1 (2026-10-08)

Role: blind-solver, fresh context, input = root, packet path, question text.
tested_sha256: 6fa7875382f3e0998151a32334fa280b2f1f698e99c654aecb5fe82f95c7232a

Raw return (verbatim):

answer: 63.3%

confidence: high

path:
1. Who gets the automatic payment. D03 is the preliminary approval memorandum (Doc. 176, filed 07/06/26), p.5: "Members of the No Bankruptcy Group will receive an automatic payment of $100.00 without the need to submit a claim." It also says: "Approximately $2,100,000.00 of the Settlement Fund is reserved to provide No Bankruptcy Group class members with automatic payments. ... Members of the Aged Bankruptcy Group will not receive these automatic payments." So the members who also get the automatic payment are the No Bankruptcy Group.
2. The valid-claim fund and how it is split. D03 p.5: "Approximately $2,882,000.00 of the Settlement Fund is reserved for payments to settlement class members (including both No Bankruptcy Group members and Aged Bankruptcy Group members) who submit valid claims." Each payment is "calculated by dividing the class member's individual pro rata points by the aggregate total number of pro rata points assigned to all claiming class members." D03 p.6: "No Bankruptcy Group members who submit a valid claim will receive three pro rata points, and Aged Bankruptcy Group members who submit a valid claim will receive one individual pro rata point."
3. Which head counts apply. D03 footnotes 2 and 3 define both groups "according to the analysis conducted by Plaintiff's expert Jonathan Jaffe and set forth in his April 22, 2025 Supplemental Report."
4. The head counts. D07 is the decertification memorandum (Doc. 157, filed 12/02/25). On pp.3–5 it reports that the April 2025 (Thomson Reuters) search gave "a class list of 57,233 individuals". It refers to "the 20,891 class members for whom Jaffe's search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters" (No Bankruptcy Group) and "the 36,317 class members for whom Jaffe located a bankruptcy filing public record that preceded the applicable consumer report by more than ten years" (Aged Bankruptcy Group). Decertification was denied, and no later document revises these counts. I checked these figures against the source file docs/uscourts_paed_2_22_cv_00048_8.txt and they match.
5. Cross-check: 20,891 × $100 = $2,089,100, which fits D03's "Approximately $2,100,000.00" automatic-payment reserve.
6. Calculation: No Bankruptcy Group points = 3 × 20,891 = 62,673. Aged Bankruptcy Group points = 1 × 36,317 = 36,317. Total = 98,990. Share = 62,673 / 98,990 = 0.63312, or 63.3%. That is about $1,824,665 of the $2,882,000. One point is worth about $29.11, so each No Bankruptcy Group claimant would get about $87.34.

minimal_documents: D03 + D07.
- D03 alone is not enough: it gives no Aged Bankruptcy Group count, and the No Bankruptcy Group count can only be estimated from the approximate $2.1M reserve.
- D07 is the only document with April-2025 group counts. D05 (Doc. 116, class certification, 08/01/24) and D04 have only certification-stage sample figures (22,141 files; 1,100; 17,098; 14,816; projected 4,736/5,471 and so on), so they cannot replace D07.
- D01, D02 and D06 are sealing or Daubert rulings with no relevant counts.

readings:
- If the Aged Bankruptcy Group is taken as the rest of the stated class list (57,233 − 20,891 = 36,342), the share is 62,673 / 99,015 = 63.30%, which still rounds to 63.3%. Note that 20,891 + 36,317 = 57,208, which is 25 short of 57,233; D07 gives 22,212 + 35,941 − 920 = 57,233. The answer is the same at one decimal place either way.
- If the No Bankruptcy Group is estimated as 21,000 from "approximately" $2.1M ÷ $100, the share is 63,000 / 99,317 = 63.4%, or 63.5% with an Aged Bankruptcy Group of 36,233. This is weaker because the reserve figure is rounded.
- The March 2025 report counts (22,212 no-bankruptcy; 35,941 aged) give 66,636 / 102,577 = 65.0%. I rejected this because the settlement defines the groups by the April 22, 2025 report.
- A simple head-count share that ignores the points (20,891 / 57,208 = 36.5%) does not measure money, so I rejected it.

gaps:
- The 25-person gap between 57,233 and 20,891 + 36,317 is not explained in the packet. It does not change the answer.
- The settlement agreement itself (Doc. 172-2) and the Jaffe report are not in the packet. The counts come from D07's description of the April 2025 report.
- D03 says Trans Union will provide an "updated class list" after preliminary approval, but the packet has no updated counts.
- The hypothetical ignores uncashed checks and any second distribution.
- Coverage: I read D03 in full and D07 pp.1–5 and 18–27. In D05 I read only the header and the numerosity and data-sample passages. For D01, D02, D04 and D06 I read only the headers, then searched them for the group names, "automatic", "preliminar", class-list terms and comma-formatted counts. I did not read them in full.
- The documents are text-method files (no PDFs or layout files), so there was no extraction problem.

contaminated: no. The packet folder contains a question.txt, which I did not open. I worked only from the question as the caller gave it.
