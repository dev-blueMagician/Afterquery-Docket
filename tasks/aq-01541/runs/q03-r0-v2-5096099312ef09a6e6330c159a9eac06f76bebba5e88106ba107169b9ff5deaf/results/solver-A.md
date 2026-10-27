# Blind solver A (packet solver-1), q03 rev 0 (2026-10-08)

Role: blind-solver, fresh context, input = root, packet path, question text.
tested_sha256: 5096099312ef09a6e6330c159a9eac06f76bebba5e88106ba107169b9ff5deaf

Raw return (verbatim):

answer: -10.0 percentage points. The decertification-time share was about 36.5% and the June 2022 share at certification was about 46.5%.

confidence: high

path:
1. D07 is the decertification memo (Dec. 2, 2025, Doc. 157). It confirms the motion date, line 67: "Trans Union moved for decertification on July 31, 2025."
2. D07 identifies the class list in place then, line 47. Jaffe's April 2025 Thomson Reuters search "resulted in the elimination of 920 individuals from the initial Step Two search, resulting in a class list of 57,233 individuals." Line 127 calls this "Jaffe's final report on April 22, 2025." D03 (lines 67-68) also ties class groups to the "April 22, 2025 Supplemental Report."
3. D07 gives the no-record count, line 49: "the 20,891 class members for whom Jaffe's search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters." Line 61 gives the stale-bankruptcy count: "the 36,317 class members for whom Jaffe located a bankruptcy filing public record that preceded the applicable consumer report by more than ten years."
   - Share: 20,891 / 57,233 = 36.502%.
   - Check: 20,891 + 36,317 = 57,208, which is 25 fewer than 57,233. Using 57,208 as the denominator gives 36.518%. Both round to 36.5%.
4. D05 is the certification memo (Aug. 1, 2024, Doc. 116). Line 312: "In the month of June 2022 alone, Plaintiff's proposed method for determining class membership located 581 class members. (See Doc. No. 107-29 ¶¶ 9–10.)"
5. D05 line 148 splits those 581: "at least 270 lacked a public record of a bankruptcy action on PACER (Id. ¶ 9.) Additionally, 311 individuals had a public record of a bankruptcy that was more than 10 years old." 270 + 311 = 581.
   - Share: 270 / 581 = 46.472%.
6. Calculation: 36.502 − 46.472 = −9.970, which rounds to −10.0 pp. With the 57,208 denominator it is −9.954, also −10.0. Subtracting the rounded figures (36.5 − 46.5) also gives −10.0.
7. Extraction note: D05 line 316 prints "270 of 97330 such files... or 27.7%... 311 of those files, or 32.0%". The "30" is a footnote marker run into "973." Footnote 30 (line 322) says "only 973 of the 1,100 input/output logs from June 2022 contained a nine-digit social security number." The checks agree: 270/973 = 27.7% and 311/973 = 32.0%.

minimal_documents: D05 and D07. Both are needed and no other document can replace either one. D07 has no June 2022 figures. D05 predates the class list. D03 only defines the No Bankruptcy and Aged Bankruptcy Groups by reference to the April 22, 2025 report and gives no counts. Its $2.1M reserve for $100 automatic payments implies roughly 21,000 members, which fits 20,891 but cannot stand in for it. D01, D02, D04 and D06 have no relevant counts.

readings:
- (a) Use D05's printed 27.7% as the June 2022 share: 36.5 − 27.7 = +8.8 pp. I think this is wrong. 27.7% is 270 out of 973 searched files with nine-digit SSNs, and those files include 392 non-class members whose bankruptcies fell within ten years. The question asks for the share "among the class members located," which is 581.
- (b) Use Jaffe's superseded March 2025 PACER-only list: 22,212 no-record SSNs and 35,941 stale, from D07 line 47. That gives 22,212 / 58,153 = 38.2%, and 38.196 − 46.472 = −8.3 pp. This is weaker because the April 2025 list of 57,233 replaced it before the July 31, 2025 motion.
- (c) Use the 1,100 June 2022 potential members as the denominator: 270 / 1,100 = 24.5%, giving +12.0 pp. This is not supportable, because D05 says only 581 were class members.
- Sign: the question is the decertification share minus the certification share, so the answer is negative. Reported as a size alone it would be 10.0 pp.

gaps:
- The documents do not explain the 25-person difference between 57,233 and 20,891 + 36,317 = 57,208. It does not change the answer at one decimal.
- D05 says "at least 270," but every other D05 passage treats 270 as the count.
- Coverage:
  - Read in full: D01, D03, D06, D07.
  - D05: read lines 1–339 and 396–407. Lines 340–395 and 408 to the end were covered only by searches for 270, 311, 581, 973, "June 2022" and "decertif", which found no other relevant figures.
  - D02 (a sealing order): read the first 40 lines, plus a number search that found nothing.
  - D04 (the Wodzinski Rule 702 memo): read lines 1–12 and 86–115, plus searches.
- I did not open the docs/ .txt originals separately. All files were extracted with method "text," and there are no PDFs or page images in the packet to check.

contaminated: no. The session context included a git-status list of workspace file names, mostly from another task (aq-00949). It held no content, answer or hint for this question. I read no notes, question files or outside material.

Relevant files (all under D:\Agents\Docket\tasks\aq-01541\runs\q03-r0-v2-5096099312ef09a6e6330c159a9eac06f76bebba5e88106ba107169b9ff5deaf\solver-1\text\):
- D05.txt
- D07.txt
- D03.txt
- manifest.json
