# aq-03169 q02: feedback after submission

questions/q02.md is frozen from 2026-10-13: the user reported it submitted at the Hard tier. The file is left
byte for byte as it was at revision 4 (saved status `checked`, tested_sha256
d020902e0730964355141dead5c422d48c0e1dd9d4d701792905a190834511c1, runs/q02-r4-v2-d020902e...-platform). Everything
that arrived after that is recorded here.

## Status observations

- 2026-10-13, user chat: "submitted as Hard tier. please check the arrived verdicts by using your feedback skill and
  improve your performance". observed_platform_status: unknown (submitted by the user's report; no acceptance or
  rejection has been seen). A difficulty pass is not acceptance.

## Platform validation (recorded here because the question file is frozen)

- 2026-10-13 | rev: 4 | platform difficulty check | tested_sha256: d020902e0730964355141dead5c422d48c0e1dd9d4d701792905a190834511c1 | platform_verdict: pass | passed_tier: hard | tiers: Low 0/5 · Medium 1/7 · High 3/6 | feedback: The difficulty check finished: In band — Hard tier. The solvers reached your answer some of the time, which is the difficulty you want. You can submit now. +$25 Medium+ bonus if accepted. Low model: 0 of 5 attempts right. Medium model: 1 of 7 attempts right. High model: 3 of 6 attempts right (the question landed here). The difficulty check passes on the current content. (Run 5, Oct 13, 2026, 10:41 AM, Version 96eed6; raw verdicts/AQ-03169_difficulty_2026-10-13_1118.txt; bound to rev 4 by "What changed before this run: question: removed “Thornton”; added “Thornton's response”", the question quoted word for word eight times and "Your answer" equal to the gold; reasoning and evidence boxes are not in the capture)

## Run 5, capture verdicts/AQ-03169_difficulty_2026-10-13_1118.txt (saved 11:18, 60 attempts read)

Platform, verbatim: "10 of 15 runs left · 10 of 60 runs used in the last 24 h (all tasks)"; "Solver summary: Run 5 · In
band · 4 of 18 right"; "2 of 18 gave the same wrong answer: “- Split UK firms into audit only and non-audit services
practices”."; "4 wrong attempts quoted the same passage: Doc 4 (“Immediate impact on market concentration”)."
Closed-book: "Needed the documents ✓". Document check: with every document, one "Did not reach your answer ✗" and one
"Reached your answer ✓"; "Needed document 4 ✓" twice; "Needed document 2 ✓" twice.

What was read: the Full answer of every attempt that has one, in full; the Reasoning of the two every-document
attempts for their handling of joint audits; the Reasoning of the low and medium attempts only for use of Annex 2.
Six high-level attempts and Medium 3 and 4 have no recorded text ("only right or wrong was recorded"): routes unread.

- High model, every document, not reached (lines 2989-3222): seven measures. Sources named as "GT's Annex 2 and main
  response". Concentration: break-up and all-clients ban. It weighed joint audits from the reply (15.4, 15.7 "the least
  concentrated in Europe", 23.5 quoted only as far as "a more dynamic market") and set it aside: "GT implies joint
  audits would help reduce concentration, but it's not explicit enough." Quality: NAO-style auditor, split. The
  sentence in the gold's evidence (D04 L349, "a more dynamic and less concentrated market") is not quoted.
- High model, every document, reached (3223-3471): six measures. Same passages (15.4, 15.7, 23.5), concluded "GT does
  say joint audits could help reduce concentration". All five members. L349's sentence is not quoted here either.
- High model, without Doc 4 (two attempts): "Grant Thornton's response is not among the ... input documents". Without
  Doc 2 (two attempts): answered from the annex without the rating set (one added the market share cap).
- Medium 1, wrong: six measures. Concentration: break-up and joint audits (quotes L349); all-clients ban missing.
  Quality: NAO-style auditor, split.
- Medium 2, right: six measures. Annex rows 2, 9, 3, 15; joint audits from the reply ("the least concentrated in
  Europe", "a more dynamic market").
- Medium 5, wrong: six measures. Concentration: all three. Quality: NAO-style auditor, split, plus the all-clients ban
  (the audit-client ban's remark about audits "which were less effective").
- Medium 6, wrong: six measures. Concentration: break-up and all-clients ban, the annex rows only; joint audits
  missing. Quality: NAO-style auditor, split.
- Medium 7, wrong: six measures. Concentration: break-up and joint audits (executive summary and annex row 5, "implying
  reduced concentration"); all-clients ban missing. Quality: NAO-style auditor, split.
- Low 1 to 5, wrong: all listed seven measures. None used the annex rows. Concentration: joint audits (Low 2, 3, 5) or
  none (Low 1, 4). Quality: split in all five, with the break-up (Low 1, 2, 4), joint audits (Low 1, 4), the
  all-clients ban (Low 1, 5) or tendering reform (Low 4), several resting on phrases the page lists under other
  respondents' documents ("enormously detrimental to audit quality", "fall between the cracks").

Author's reading (not the platform's):

- The one changed term did what it was written for. On rev 3 ("does Grant Thornton say") all three every-document
  attempts answered from the annex and never weighed joint audits. On rev 4 ("does Grant Thornton's response say")
  both went to "Annex 2 and main response" and weighed it; one accepted it, one judged it not explicit enough.
- Neither every-document attempt quoted the explicit sentence at L349; both stopped at the first sentence of paragraph
  23.5. So the high model's split is on whether an implied link counts, while the gold rests on a stated one. If a
  reviewer asks, the support is L349 (evidence row 7) and the reasoning's Step 3.
- Declared failure modes against this run: mode 1 (annex alone or reply alone gives a partial list) is the miss in
  Medium 1, 6 and 7, the unreached every-document attempt and all five low attempts. Mode 2 (the NAO-style auditor's
  cost after a page break) is not seen in any recorded medium or high attempt of this run; the low attempts lack that
  member because they never used the annex. Medium 5's extra member (the all-clients ban under quality) is a third
  route, the audit-client ban's remark carried to the wider measure; it was seen in Runs 3 and 4 as well and was not
  declared.
- Every recorded medium attempt again listed six measures and left tendering reform out of Deloitte's set; all low
  attempts listed seven. It cost nothing because tendering reform is in neither group.

## Scope ladder measured on this question (same gold, same evidence)

| Wording | Run | Result |
|---|---|---|
| "does Grant Thornton say anywhere in its response" (rev 2) | 3 | Between levels: Low 0/5, Medium 4/5 |
| "does Grant Thornton say" (rev 3) | 4 | Answer not supported: Low 0/5, Medium 1/4, high model 0 of 3 with every document |
| "does Grant Thornton's response say" (rev 4) | 5 | In band, Hard: Low 0/5, Medium 1/7, High 3/6 |

## What the five runs cost and what would have saved them

- Run 1 (q01): a lone small whole number as the gold; closed-book guessed it. Rule on file since then.
- Run 2 (q02 rev 0): the members could all be read from one place (the annex). Easy.
- Form round (rev 1): gold written as two labelled sentences; blocking "Short answer". The floor now warns
  (`short-answer`).
- Run 3 (rev 2): a completeness word in the question. The floor now warns (`cue`).
- Run 4 (rev 3): scope dropped on the platform's suggested wording, against WORKFLOW section 6 item 5, which was on
  file. Author's error.
- Run 5 (rev 4): scope named. Hard.
With the design of rev 1, a plain comma-list gold and the scope named from the start, the same question needed two
difficulty runs, not five.
