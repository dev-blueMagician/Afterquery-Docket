# Shortcut auditor (packet shortcut), q03 rev 0 (2026-10-08)

Role: shortcut-auditor, fresh context, input = root, packet path, question text.
tested_sha256: 5096099312ef09a6e6330c159a9eac06f76bebba5e88106ba107169b9ff5deaf

Raw return (verbatim):

answer: -10.0 percentage points. About 36.5% of the class list in place at decertification had no bankruptcy record found at all, compared with about 46.5% of the 581 June 2022 class members at certification.

verdict: clear

shortest_path:
1. D05 is the certification memo (Doc. 116, Aug 1, 2024).
   - Page 12 says: "out of the 1,100 potential class members from June 2022 ... at least 270 lacked a public record of a bankruptcy action on PACER ... Additionally, 311 individuals had a public record of a bankruptcy that was more than 10 years old in June 2022."
   - Page 26 says: "In the month of June 2022 alone, Plaintiff's proposed method for determining class membership located 581 class members." 270 + 311 = 581, so the counts agree.
   - Share with no record: 270/581 = 46.47%.
2. D07 is the memo denying decertification (Doc. 157, Dec 2, 2025).
   - Pages 3-4: Jaffe's April 22, 2025 Thomson Reuters re-run "resulting in a class list of 57,233 individuals."
   - Page 4: "the 20,891 class members for whom Jaffe's search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters."
   - Page 5: "the 36,317 class members for whom Jaffe located a bankruptcy filing public record that preceded the applicable consumer report by more than ten years."
   - This is the list in place when Trans Union moved. The motion was filed July 31, 2025, and footnote 5 calls the April 22, 2025 report Jaffe's "final report."
   - Share with no record: 20,891/57,233 = 36.50%.
3. 36.50 - 46.47 = -9.97, which rounds to -10.0 percentage points.

sufficient_documents: D05 and D07 together are the minimum. Neither works alone:
- D05 predates the 2025 class list.
- D07 never repeats the 270/311/581 figures (checked by search).
- D03 (settlement memo, July 6, 2026) defines the No Bankruptcy and Aged Bankruptcy Groups from the April 22, 2025 report. Its $2,100,000 reserve for $100 automatic payments implies roughly 21,000 members, but it gives no class total, so it can't stand in for D07.
- D01, D02, D04 and D06 contain none of the inputs.

searches:
- Literal terms: 270, 311, 581, 973, 1,100, "June 2022", 20,891, 57,233, 36,317, 22,212, 35,941, 58,153, "class list", "No Bankruptcy Group", "Aged Bankruptcy", "located", "%", "percent", "one-third".
- Concepts: no-record share, stale or aged bankruptcy share, decertification-era class list, settlement groups.
- Coverage: I read manifest.json and all of D01-D07 in full. I did not open the docs/ originals; the manifest says these are plain text extractions with no page images.
- No document states either share or the difference directly. The only nearby stated share is D05 page 27, "270 of 973 ... or 27.7%," which uses a different denominator and works as a trap.

readings/gaps:
- If the June 2022 share used the court's stated 27.7% (270 of 973 files with nine-digit SSNs), the result would be +8.8. I reject this because the question asks about the class members located (581), not files.
- Using 270/1,100 = 24.5% gives +12.0. I reject this because those are potential members, not class members.
- Using Jaffe's March 2025 list (22,212/58,153 = 38.20%) gives -8.3. I reject this because the April 22, 2025 report replaced it as the final list before the July 31, 2025 motion.
- D07's own counts don't quite add up: 20,891 + 36,317 = 57,208, which is 25 short of the stated 57,233. With 57,208 as the denominator the share is 36.52% and the difference is -9.954, which still rounds to -10.0. The only risk is double rounding: 36.52 - 46.47 = -9.95, which floating-point rounding could turn into -9.9. With the stated list size of 57,233 the result is -9.970, so -10.0 holds.
- Difficulty risk, not a shortcut: the question's wording closely tracks the source text ("located ... June 2022" matches D05's "located 581 class members," and "class list" appears in D07), and the arithmetic is a simple two-ratio difference. Each half still needs a different document.
- Contamination check: I did not read question.txt, notes, other packets or earlier outputs. The environment automatically injected a git-status snapshot that listed file names from another task (aq-00949) and repository config files. It contained no content about this question or its answer, so I don't consider the run contaminated. I can't confirm the invocation settings (non-fork, omitClaudeMd) from inside the run.

Packet path: D:\Agents\Docket\tasks\aq-01541\runs\q03-r0-v2-5096099312ef09a6e6330c159a9eac06f76bebba5e88106ba107169b9ff5deaf\shortcut\text\ (D05.txt, D07.txt)
