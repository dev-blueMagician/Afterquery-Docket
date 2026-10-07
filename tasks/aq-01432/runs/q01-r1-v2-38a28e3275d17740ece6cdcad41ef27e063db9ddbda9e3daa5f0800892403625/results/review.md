# q01 rev 1 - independent review (fresh question-review subagent), 2026-10-06

Raw return as received:

q01 (rev 1; tested_sha256: 38a28e3275d17740ece6cdcad41ef27e063db9ddbda9e3daa5f0800892403625)

gold_verified: yes (recounted from the original texts with a script). Doc 11's "Pressure selling" heading (D10 L89-L91) names seven behaviours (five after "for example by", two after "You mustn't"). Doc 9 maps them to banned practices 14 (L577), 24 (L679; 31 at L739 also fits), 27, 28, 26, 30 and 32; banned practice number = Schedule 20 paragraph (D09 L573; D08 L63/L159; D11 L70; D04 L113). The offences list (L1387-L1391) covers every banned practice with marker [footnote 112]; note 112 (L1885) and note 39 (L1593) exclude paragraphs 12, 13 and 30. Only practice 30 (children) is in the theme: 7 − 1 = 6. Other readings: no exclusion 7; five examples 5; "ordered" as 31 still 6; old 2008 numbering (paragraph 30 = livelihood) excludes the wrong item but still gives 6.

outcome: A: match; B: match. Both packets held the verbatim rev 1 question and corpus-identical text; high confidence; practice 30 excluded via notes 112/39; both rejected 5, the any-offence 7 and the practice-31 mapping; only outside context the harness's file-name git status. Two uncontaminated matches.

closed-book: misses ("5 (best guess)", low, 6 only as an alternative). A count has no rounding band, so the platform grades 5 as different (trial-03 q03 precedent: key named as an alternative is a miss with some exposure). It got the guide's list wrong (added a limited-time item the guide files under misleading claims; left out the risk and invoice items) but recalled the children exception. All three question-only runs ("All of them", "4", "5") missed. Exposure low to moderate: ~10% that the platform's low model lands on 6.

necessity:
- Doc 11 (D10): the only source of the theme's members (D09 L95 names "pressure selling" with no members; D08 only the refusal to leave; all others silent). Probe without it could not answer; forced guess 6 (p 0.25) from D09's run 26-32 (seven items including 30) plus an inference from the question's form. Doc 9 never calls that run pressure selling, and it differs from the guide's set (the guide includes practice 14 and files the correspondence duty, practice 29, under after-sales care, D10 L95).
- Doc 9 (D09): the only source of criminal status (offences list, notes 112 and 39); elsewhere D10 L57 civil fines only, D11 enforcement without criminal status, D08 L91 an offence under the 2013 regulations. Probe without it could not answer; forced guess 6 (p 0.6) from the 2008 Regulations' exceptions.
- No smaller source set, no substitute.

shortcut: clear. Shortest route: D10 L71, L89-L91 → D09 L1391 marker → note 112 L1885 (or note 39) → practice 30 L729 → subtract. No passage or overview gives the count; searches on offence/criminal/prosecut, pressure, children, Schedule 20, paragraph 30 find inputs only.

source_assessment: no gaps (source_gaps [], hash 4f53cda1... = hash of "[]"; intake 11/11 complete, gap_characters 0). Misnumbered note markers (~116-119) and the repeated phrase in note 39 touch no input.

difficulty: easy (local suitability, below the Medium target). Tied trap (the note marker sits on the line the 7-decoy comes from; note 39 repeats the exclusion inside the banned-practices chapter); "prosecuted" leads to a "criminal offence" search that finds both notes; list under a heading the question names; trivial mapping; recallable exception; rev 1 removed the theme ambiguities that were the other wrong-answer routes (aq-00949 q04 lesson). Odds: Too easy ~40%, Easy ~45%, Medium ~10%, Hard ~3%, Too hard / "Answer not supported" ~2%. Separately: document check flags a document ~35-45% (Doc 9 30-40%, Doc 11 ~10%); closed-book reaches 6 ~10%. Clean Medium pass with no flag ~6%.

verdict: ready (correctness and fairness only; status stays checked; no platform evidence).

findings:
1. Readings: rev 1 removes the eight-item reading ("special offer will finish soon", D10 L79, sits under "Misleading promotional claims"); the five-item reading becomes a misreading (both sentences under one heading; other themes also span several "You must not / You mustn't" sentences, L79). Also shut: "prosecuted" excludes civil action (note 39 "can attract civil action"); "for breaching the banned practice involved" excludes the aggressive-practices route; "Put unfair pressure" is the theme's general description, not a banned practice. One defensible answer: 6.
2. Closed-book misses (the near-answer rule covers estimates of continuous figures; an off-by-one integer count resting on an invented list is not one).
3. Doc 9 risk real (all four question-only or no-Doc-9 runs recalled the children exception); the platform's unforced high model may answer 6, 7 or "cannot be determined". No wording fix inside this mechanism (other themes have no non-criminal member — trust marks, promotional claims, illegal products, after-sales care — or split between paragraphs 13 and 25, giving two answers). Only the reviewer note helps; the prepared note is accurate (whole-bundle search); enter it only if the check flags Doc 9 (any edit clears it). If the form lets a necessary document carry an excluded item, consider attaching paragraph 30 to Doc 9 (platform treatment untested).
4. Doc 11 risk lower (the forced guess rested on the 26-32 coincidence plus the question's form; the platform does not force a guess). No change. If flagged, the true note fact: only Doc 11 assigns behaviours to the theme (it includes practice 14 and files the correspondence duty under after-sales care).
5. Form number rule emulated by script — every step complies: Step 1 no numbers; Steps 2-3 numbers (9, 12-14, 20, 24, 26-28, 30, 32, 39, 112) printed in Doc 9; Step 4 "= 6" follows "=" (6 also in both cited documents as "6 April 2025"); Decoy line 6 and 1 in Doc 9, 7 after "="; no counts spelled out. Step 4's left side is a phrase rather than a sum (form treatment unconfirmed; passes either way).
6. Lever works: omitting notes 112/39 gives 7; the children decoy plausible because the body's offences list covers every banned practice; no other member maps to 12 or 13; "Scatter the pieces" holds.
7. Rule 10 / length: 38 words; counts conduct, not documents; "groups the banned practices" is a verb. Overlap with workspace questions ≤ 0.175, longest shared run 2 tokens. The form's stated-figure advisory may misfire on Doc 11's "32 banned practices" (false positive).
8. Set: do not submit q01 with i06 (same exclusion) or i08 (same theme-to-paragraph step); q02 independent; one Easy slot for two Easy-leaning candidates.
9. Records: all four rev 1 records and both probe packets carry the rev 1 question and fingerprint; report recomputes 38a28e32....
10. Target: not a suitable difficulty for Medium under the gate; quick test before a difficulty run (8 left); without target-suitable difficulty it goes forward only as an Easy candidate, if the user accepts Easy.

Not runnable locally: restricted names, Original question / Not a duplicate, token window.
