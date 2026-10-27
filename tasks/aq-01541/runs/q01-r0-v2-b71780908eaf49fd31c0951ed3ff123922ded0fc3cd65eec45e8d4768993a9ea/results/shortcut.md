# Shortcut auditor (packet shortcut), q01 rev 0 (2026-10-08)

Role: shortcut-auditor, fresh context, input = root, packet path, question text.
tested_sha256: b71780908eaf49fd31c0951ed3ff123922ded0fc3cd65eec45e8d4768993a9ea

Raw return (verbatim):

answer: 63.3%. If every class member filed a valid claim, the No Bankruptcy Group (the members who also get the automatic $100 payment) would receive 63.3% of the valid-claim pool, about $1.82M of the roughly $2.882M.

verdict: clear

shortest_path:
1. D03 (text\D03.txt = docs\uscourts_paed_2_22_cv_00048_10.txt, Doc. 176, preliminary-approval memo dated 7/6/26, pp. 5–6) gives the payment structure:
   - "Members of the No Bankruptcy Group will receive an automatic payment of $100.00 without the need to submit a claim."
   - "Members of the Aged Bankruptcy Group will not receive these automatic payments."
   - "Approximately $2,882,000.00 ... is reserved for payments to settlement class members ... who submit valid claims."
   - "No Bankruptcy Group members who submit a valid claim will receive three pro rata points, and Aged Bankruptcy Group members ... one individual pro rata point."
   - Footnotes 2–3 define both groups "according to the analysis ... set forth in his [Jaffe's] April 22, 2025 Supplemental Report."
2. D07 (text\D07.txt = docs\uscourts_paed_2_22_cv_00048_8.txt, Doc. 157, decertification memo dated 12/2/25, pp. 4–6) gives the group sizes after the April 2025 Thomson Reuters search:
   - "the 20,891 class members for whom Jaffe's search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters"
   - "the 36,317 class members for whom Jaffe located a bankruptcy filing public record that preceded the applicable consumer report by more than ten years"
   - The class list is "57,233 individuals."
   - Check: 20,891 × $100 ≈ the "approximately $2,100,000" automatic-payment reserve in D03.
3. Calculation: 3 × 20,891 = 62,673 points. Adding 36,317 gives 98,990 points in total. 62,673 / 98,990 = 0.63312, so 63.3%.
   - Robustness: if the 57,233 total is paired with either count, the share is 62,673/99,015 = 63.30% or 62,748/99,065 = 63.34%. Both round to 63.3%.

sufficient_documents: D03 + D07. Neither works alone and I found no alternative pair.
- D03 has the 3:1 points and the definitions, but no Aged Bankruptcy Group count or total class size. The approximately $2.1M reserve gives only a rough No Bankruptcy Group count.
- D07 predates the settlement and has no point structure.
- D01, D02, D04, D05 and D06 do not contribute inputs. D05 contains only distractor sample numbers.

searches:
- Literal terms in text\ and docs\: 20,891; 36,317; 57,233; 22,212; 35,941; "920 individuals"; 2,100,000; 2,882,000; "pro rata point"; "automatic payment".
- A regex listing every comma-formatted number in text\, to find all candidate counts.
- Concept terms: No Bankruptcy / Aged Bankruptcy, stale bankruptcy, "no bankruptcy records," class list, Thomson Reuters, valid claim, points.
- Read text\manifest.json and D01–D07 in full; the docs\ greps returned the same figures.
- No answer-shaped summary, percentage or ranking exists anywhere. D07 never uses the group names. You have to link it to D03 by matching the group definitions and the April 22, 2025 report.
- I did not open question.txt or anything outside the packet's docs\ and text\.

readings/gaps:
- Main trap: the March 2025 counts in the same D07 passage (22,212 / 35,941) give 66,636/102,577 = 65.0%. I rejected these because they come before the Thomson Reuters exclusion, and the settlement defines the groups by the April 22, 2025 report.
- Rounding risk: using D03's approximate reserve ($2.1M / $100 = 21,000) gives 63,000/99,317 = 63.4%, or 63,000/99,233 = 63.5% with the 57,233 total. I rejected this because the reserve is labelled "approximately" and the exact counts are available.
- Other wrong readings:
  - The June 2022 sample in D05 (270 vs 311) gives 72.3%.
  - An unweighted headcount gives 36.5%.
  - Reversing the points (1 for No Bankruptcy, 3 for Aged) gives 16.1%.
- Gaps:
  - 20,891 + 36,317 = 57,208, which is 25 short of the 57,233 class list. Nothing in the documents explains this; it does not change the one-decimal answer.
  - The settlement agreement itself (Doc. 172-2) and any updated settlement class list are not in the packet, so I could not confirm the final group counts. The court's memo ties the groups to the April 2025 report.
  - The exhibit pages in D01 are image-only with no text; they are irrelevant here.
- Difficulty risk: once D07's counts are found, the arithmetic is a simple weighted share. The two-document join is still necessary.
- Contamination: none.
  - No CLAUDE.md, memory, notes, key or prior solve output appeared in my context.
  - The auto-attached git status showed only workspace filenames, with no content.
  - question.txt appeared in the directory listing but I did not open it.

Files:
- D:\Agents\Docket\tasks\aq-01541\runs\q01-r0-v2-b71780908eaf49fd31c0951ed3ff123922ded0fc3cd65eec45e8d4768993a9ea\shortcut\text\D03.txt
- D:\Agents\Docket\tasks\aq-01541\runs\q01-r0-v2-b71780908eaf49fd31c0951ed3ff123922ded0fc3cd65eec45e8d4768993a9ea\shortcut\text\D07.txt
- D:\Agents\Docket\tasks\aq-01541\runs\q01-r0-v2-b71780908eaf49fd31c0951ed3ff123922ded0fc3cd65eec45e8d4768993a9ea\shortcut\text\D05.txt (distractor samples)
