# Blind solver A (packet solver-1), q01 rev 1 (2026-10-08)

Role: blind-solver, fresh context, input = root, packet path, question text.
tested_sha256: 6fa7875382f3e0998151a32334fa280b2f1f698e99c654aecb5fe82f95c7232a

Raw return (verbatim):

answer: 63.3%

confidence: high

path:
1. D03 is the July 6, 2026 memorandum granting preliminary approval (Doc. 176). File: D:\Agents\Docket\tasks\aq-01541\runs\q01-r1-v2-6fa7875382f3e0998151a32334fa280b2f1f698e99c654aecb5fe82f95c7232a\solver-1\text\D03.txt. It says who gets the automatic payment:
   - Line 63, p.5: "Members of the No Bankruptcy Group will receive an automatic payment of $100.00 without the need to submit a claim."
   - Line 64, p.5: "Members of the Aged Bankruptcy Group will not receive these automatic payments."
   So "members who also get the automatic payment" means the No Bankruptcy Group.
2. D03 line 66, p.5, on the valid-claim pot: "Approximately $2,882,000.00 of the Settlement Fund is reserved for payments to settlement class members (including both No Bankruptcy Group members and Aged Bankruptcy Group members) who submit valid claims... Each class members's payment will be calculated by dividing the class member's individual pro rata points by the aggregate total number of pro rata points assigned to all claiming class members."
3. D03 line 73, p.6, on points: "No Bankruptcy Group members who submit a valid claim will receive three pro rata points, and Aged Bankruptcy Group members who submit a valid claim will receive one individual pro rata point." Line 210, p.17 repeats this.
4. D03 footnotes 2–3 (lines 67–68) define both groups by "the analysis conducted by Plaintiff's expert Jonathan Jaffe and set forth in his April 22, 2025 Supplemental Report."
5. D07 is the December 2, 2025 decertification memorandum (Doc. 157). File: ...\solver-1\text\D07.txt. It gives the group sizes from that April 2025 report:
   - Line 47, p.4: the Thomson Reuters re-search "result[ed] in a class list of 57,233 individuals."
   - Line 49, p.4: "the 20,891 class members for whom Jaffe's search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters." This is the No Bankruptcy Group.
   - Line 61, p.5: "the 36,317 class members for whom Jaffe located a bankruptcy filing public record that preceded the applicable consumer report by more than ten years." This is the Aged Bankruptcy Group.
   - Line 127, fn 5, confirms "Jaffe's final report on April 22, 2025."
   - I checked these numbers against the source file docs\uscourts_paed_2_22_cv_00048_8.txt, and the figures in item 3 against docs\..._10.txt. They match.
6. Calculation, assuming everyone files a valid claim:
   - No Bankruptcy Group: 20,891 × 3 = 62,673 points.
   - Aged Bankruptcy Group: 36,317 × 1 = 36,317 points.
   - Total: 98,990 points.
   - Share: 62,673 / 98,990 = 0.63312, which is **63.3%**. That is about $1,824,665 of the $2,882,000 pot, or roughly $29.11 per point ($87.34 per No Bankruptcy claimant, $29.11 per Aged claimant). The answer does not depend on the dollar amount because the split is pro rata.
7. Cross-check from D03 lines 53, 82 and 101: $8,310,000 − $2,770,000 fees − $308,000 expenses − $50,000 service award − $210,000 administration − $2,882,000 claims pot = $2,090,000. At $100 each that is about 20,900 automatic payments, which fits 20,891 and the "approximately $2,100,000" figure.

minimal_documents: D03 + D07. D03 gives the payment structure but no group counts. D07 is the only document in the packet with both group counts, so there is no substitute for it. D01, D02, D04, D05 and D06 are certification-stage or sealing documents. My searches of them found only pre-class-list estimates (e.g., 22,141 files; 17,098 / 14,816; "tens of thousands").

readings:
- Take Aged as the total class list minus No Bankruptcy (57,233 − 20,891 = 36,342): 62,673 / 99,015 = 63.3%.
- Take No Bankruptcy as the total minus Aged (57,233 − 36,317 = 20,916): 62,748 / 99,065 = 63.3%.
- Back out the No Bankruptcy count from the approximate $2,100,000 / $100 = 21,000: 63,000 / 99,317 = 63.4%, or 63.5% if Aged is set to 57,233 − 21,000. This is weaker because the $2.1M is labelled "approximately" and exact counts exist.
- Use the superseded March 2025 PACER-only counts (22,212 and 35,941, D07 line 47): 66,636 / 102,577 = 65.0%. This is not the settlement's definition, which uses the April 22, 2025 report.
- Drop the two "TEST" records noted in D07 fn 9: still 63.3%.
- Reading it as a headcount share (20,891 / 57,208 = 36.5%) does not fit the question, which asks about "money."

gaps:
- The two group counts add to 57,208, which is 25 fewer than the stated class list of 57,233. Nothing in the packet explains this. It does not change the answer at one decimal place.
- The settlement agreement itself (Doc. 172-2) is not in the packet, so the group sizes come from the December 2025 memo rather than from the settlement. There is no data on opt-outs after notice.
- No PDFs or .layout.txt files are in the packet (the manifest says method "text"), so I could not check original pages. The text extraction around the decisive rows reads cleanly.
- Read in full: D03 and D07.
- Read in part:
  - D01 lines 1–25
  - D02 lines 1–25
  - D04 lines 1–140
  - D05 lines 1–110 and 305–384
  - D06 lines 1–25
- The rest of D01, D02, D04, D05 and D06 was covered only by regex searches across all text files. I searched for comma-formatted and 5–6 digit numbers, "thousand", group names, "automatic payment", "preliminary approval", and opt-out/exclusion/class-list terms. None turned up competing group counts.

contaminated: no. Nothing leaked; there was no answer, reasoning or source hint. The packet contains a question.txt, and I did not open it.
