# Blind solver A (packet solver-1), q02 rev 0 (2026-10-08)

Role: blind-solver, fresh context, input = root, packet path, question text.
tested_sha256: d365e12cebaacccf10f8577bf36789068835211c27b54c21ec657de3a6094c07

Raw return (verbatim):

answer: $29.1 per claimant (Aged Bankruptcy Group member, 1 pro rata point): $2,882,000 / 98,990 points = $29.114.

confidence: high

path:
1. Court's figure for the valid-claim money. D03 (Doc. 176, preliminary-approval memorandum, July 6, 2026, p.5): "Approximately $2,882,000.00 of the Settlement Fund is reserved for payments to settlement class members (including both No Bankruptcy Group members and Aged Bankruptcy Group members) who submit valid claims." Each payment is "calculated by dividing the class member's individual pro rata points by the aggregate total number of pro rata points assigned to all claiming class members."
2. Points. D03 p.6: "No Bankruptcy Group members who submit a valid claim will receive three pro rata points, and Aged Bankruptcy Group members who submit a valid claim will receive one individual pro rata point."
3. Who gets no automatic payment. D03 p.5: No Bankruptcy Group members "will receive an automatic payment of $100.00 without the need to submit a claim … Members of the Aged Bankruptcy Group will not receive these automatic payments." So the claimants with no automatic payment are the Aged Bankruptcy Group, at 1 point each.
4. Group definitions. D03 footnotes 2 and 3 define both groups "according to the analysis conducted by Plaintiff's expert Jonathan Jaffe and set forth in his April 22, 2025 Supplemental Report."
5. Group sizes from that April 2025 report. D07 (Doc. 157, decertification memorandum, Dec. 2, 2025, pp.4–5): "the 20,891 class members for whom Jaffe's search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters" (No Bankruptcy Group), and "the 36,317 class members for whom Jaffe located a bankruptcy filing public record that preceded the applicable consumer report by more than ten years" (Aged Bankruptcy Group). Both figures were checked in the docs/ source file uscourts_paed_2_22_cv_00048_8.txt.
6. Calculation with every member claiming: 3 × 20,891 = 62,673; 62,673 + 36,317 = 98,990 points. $2,882,000 / 98,990 = $29.114 per point. An Aged Bankruptcy Group claimant gets 1 point, or $29.1. As a check, No Bankruptcy Group claimants would get about $87.34 each, and 20,891 × 87.34 + 36,317 × 29.11 ≈ $2,882,000.

minimal_documents: D03 and D07. I found no substitute. D07 is the only document with the April 2025 group counts, and D03 is the only one with the settlement terms. D06 only names the April 22, 2025 report as a sealed exhibit and gives no counts.

readings:
- Class-list total. D07 also says "resulting in a class list of 57,233 individuals." That is 25 more than 20,891 + 36,317 = 57,208. Adding the 25 to the Aged group gives $2,882,000 / 99,015 = $29.107. Adding them to the No Bankruptcy group gives $2,882,000 / 99,065 = $29.092. Both round to $29.1, so the answer does not change.
- Group size inferred from the automatic-payment reserve. "Approximately $2,100,000" divided by $100 gives about 21,000 No Bankruptcy members. With 36,317 Aged members the result is $2,882,000 / 99,317 = $29.018. With 57,233 − 21,000 = 36,233 Aged members it is $29.043. Both round to $29.0. This reading is weaker because the reserve is stated as approximate and the groups are expressly defined by the April 2025 report.
- Rebuilding the reserve from the fund instead of using the court's figure. $8,310,000 − 2,770,000 (fees) − 308,000 (expenses) − 50,000 (service award) − 210,000 (administration) − 2,100,000 (automatic payments) = $2,872,000, which is $10,000 less than the court's $2,882,000. That gives $2,872,000 / 98,990 = $29.013, or $29.0. The question rules this out by asking for "the court's figure."
- Superseded March 2025 counts. 22,212 no-record and 35,941 aged (D07 p.4) give $2,882,000 / 102,577 = $28.096, or $28.1. The April report replaced these after eliminating 920 people, and D03 ties the groups to the April report, so this reading is not defensible.
- An unweighted per-head split ($2,882,000 / 57,208 ≈ $50.38) ignores the 3:1 points rule, so it is not a defensible reading.

gaps:
- The settlement agreement (Doc. 172-2) and the Jaffe reports are not in the packet. The group counts therefore come from the court's December 2025 description of the April 2025 class list. The settlement class could differ slightly, for example through the two "test subject" records D07 mentions or later changes, but small changes do not move the answer at one decimal.
- The 25-person gap (57,233 vs 57,208) is not explained in the documents.
- Coverage: I read D03, D06 and D07 in full. I did not read D01, D02, D04 or D05 in full; I searched them with patterns for comma-formatted numbers, group names and class-list terms. They are July–August 2024 sealing, expert and class-certification rulings that predate the class list; D05's figures are only June 2022 samples and extrapolations.
- The packet has only text files (manifest method "text", no PDFs or layout files), so I could not inspect PDF pages. No extraction problem showed up in the decisive figures.
- I did not read question.txt.

contaminated: no. The auto-attached git status listed file names from an unrelated task (aq-00949). Nothing about this question's answer, reasoning or sources leaked.

Files:
D:\Agents\Docket\tasks\aq-01541\runs\q02-r0-v2-d365e12cebaacccf10f8577bf36789068835211c27b54c21ec657de3a6094c07\solver-1\text\D03.txt
D:\Agents\Docket\tasks\aq-01541\runs\q02-r0-v2-d365e12cebaacccf10f8577bf36789068835211c27b54c21ec657de3a6094c07\solver-1\text\D07.txt
D:\Agents\Docket\tasks\aq-01541\runs\q02-r0-v2-d365e12cebaacccf10f8577bf36789068835211c27b54c21ec657de3a6094c07\solver-1\docs\uscourts_paed_2_22_cv_00048_10.txt
D:\Agents\Docket\tasks\aq-01541\runs\q02-r0-v2-d365e12cebaacccf10f8577bf36789068835211c27b54c21ec657de3a6094c07\solver-1\docs\uscourts_paed_2_22_cv_00048_8.txt
