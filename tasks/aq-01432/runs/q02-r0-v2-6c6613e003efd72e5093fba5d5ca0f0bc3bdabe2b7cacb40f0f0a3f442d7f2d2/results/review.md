# q02 rev 0 - independent review (fresh question-review subagent), 2026-10-06

Raw return as received:

q02 (rev 0; tested_sha256: 6c6613e003efd72e5093fba5d5ca0f0bc3bdabe2b7cacb40f0f0a3f442d7f2d2)

gold_verified: yes. Recomputed from the originals: D04 L285-L301 (= docs/ L389-L405) has six commissioning examples. Applied to D03's § 465.4 answers: Ex1 ("five-star", L287) and ex3 ("five-star", L291) breach (L145-L147 "would violate Section 465.4"); ex5 ("positive review", L299) breaches (condition stated outright, L143 and L155 apply); ex2 does not (no sentiment requirement, L143 "does not prohibit"); ex4 does not (L161-L163 "No", repeated L261-L263); ex6 buys bot output from a vendor, outside the asked-about set. Answer {1, 3, 5} matches the key.

outcome: A: match; B: match. Both named examples 1, 3 and 5 with descriptions (equivalent to the key), high confidence, both rejected {1, 3, 4, 5} citing L161-L163; separate fresh packets; only extra context was git-status file names, no answer. Two valid matches.

closed-book: misses ("None", low confidence; recalled § 465.4 and the staff Q&A generally, not the CMA examples).

necessity:
- D04 (Doc 5) needed: the only list of commissioning examples. Without it D06 L15 and D09 L573 only point to "the full fake reviews guidance"/"separate guidance"; D06 L33's single example (money, a free stay, a freebie) has no sentiment condition, so the answer becomes "None" (probe "None", p 0.4).
- D03 (Doc 2) needed: the only FTC staff reading of the rule and the only exclusion of ex4. Without it D01 L185 plus D05 L526 and L509 pull ex4 in (probe {1, 3, 4, 5} p 0.6, key only 0.3). D05 (June 2023, Endorsement Guides, never mentions Part 465) cannot stand in.
- D01 rightly unlisted (D03 L35 and L143 restate the standard). Two documents is the smallest set.

shortcut: clear. Confirmed shortest route D04 L285-L301 then D03 L139-L167 (L143, L145-L147, L155, L161-L163). No passage links the regimes (UK documents never mention the FTC or Part 465; US documents never mention the CMA or the UK). The capture overview exposes nothing deciding. Ex1, ex3 and ex5 findable by keyword: difficulty risk, not a Guide violation.

source_assessment: no gaps. intake.json shows all 11 documents complete (gap_characters 0, matching hashes); snapshot source_gaps empty (4f53cda1…). The capture's "Docket has been updated" reload notice changes no text bytes. Nothing to map.

difficulty: easy. Tier odds: Too easy ~45%, Easy ~40%, Medium ~8%, Hard ~3%, Too hard / answer not supported ~2-3%.

verdict: ready (local fairness only; status stays checked; on local evidence not suited to the Medium target).

findings:
1. Universe: "offering customers or other consumers something" fixes D04 examples 1-5 (ex6 drops out). D04 2.10 (L168-L191) and 3.7 (L309-L313) carry no sentiment condition; D04 fn8 (L181) prize draw "unlikely to amount to commissioning"; submitting examples (L276-L278) and 4.4(a)(iv) (L360) are not commissioning; D06 L33 and D07 L71 no sentiment condition; D09 BP12 example (L523) is a testimonial (D03 L149-L151 outside § 465.4). However broadly read, the answer stays {1, 3, 5}. No action.
2. Excluding ex4: the only defensible reading under "As FTC staff read". L163 covers the exact scenario ("paying consumers to change or remove truthful negative reviews may violate the FTC Act") with "No" for the rule; L261-L263 repeats. Ex4's "no longer reflective of their genuine experience" points to § 465.2(b), outside the question's "ban on incentives tied to a review's sentiment", and staff's "the rule" answer covers it too. The sentiment-tied reading survives only by ignoring the named staff reading (the no-D03 probe confirms its source). No action.
3. Answer shape passes: three items of 8, 9 and 8 words, 172 characters, commas only; "List them in any order" and "if any" cover order and the empty case; components are answer pieces; evidence quotes 12 of 12 verbatim. Small risks: a numbers-only answer ("1, 3 and 5") may be hard to grade; form acceptance of "in any order" not yet seen; only c1 capitalised (cosmetic).
4. US rule applied to UK examples: fair and self-contained (the Guide's "apply a rule to a case"; each item maps onto a staff answer about a nearly identical scenario; rule 10 holds, items are practices). Most likely reviewer objection: a literal "a US rule cannot reach UK traders, so none" reading; the hypothetical "would breach" does not support it. No change required.
5. Tier odds reasons — leans easy: tied trap (L161 sits 14 lines below L147 inside the same § 465.4 section the question's sentiment phrase leads to; L261 repeats); ex1, ex3, ex5 print the deciding words; plain staff sentences applied to numbered items match two shapes measured Too easy at Low 5/5 (aq-00949 q03, aq-00745 q01); the only measured Medium pass needed a decoy that looks current (aq-00964 q01), which this bundle lacks. For it: ex4 is an answer-shaped decoy (sentiment-tied on the rule text and the question's own phrase); extra slip routes (ex6 against § 465.4's "Buying …" heading; ex3 against the influencer carve-out L149-L151); all-or-nothing list. Quick-test before any difficulty run. No fair rewording of this mechanism reaches Medium (dropping the sentiment pin lets § 465.2 readings of ex1 and ex4 in).
6. Two reasoning quotes not verbatim (Q14; affects "Derive the rest"): Step 2's "isn't" uses a straight apostrophe where D03 L143 has a curly one; the decoy line's "conditioned expressly or by implication on" appears in D01 only with doubled spaces, and D01 is unlisted. Possible effects: "Derive the rest" may not tie Step 2's first quote and may propose Doc 1. Fix: make each reasoning quote byte-identical to a cited passage (D03 L35 prints the standard with single spaces) or remove the quotation marks; any edit means rev 1 and fresh A/B, closed-book and audit. Otherwise check the form's proposals by hand. Non-blocking.
7. D03 might fail the platform's document check (~20-30%): without Doc 2 the high model, not forced to guess, might still land on {1, 3, 5} by reading "writing or creation" as excluding edits or by recalling the November 2024 Q&A. Reviewer-note option fits (Doc 2 holds the only exclusion of ex4).
8. Ex3 does not say where the five-star reviews appear (Q12): natural reading treats star ratings as consumer reviews; D03 L147 says the ban applies "whether the reviews appear on your website or third-party review platforms". Low risk.
9. Shape/originality: 47 words (above the 20-45 aim, below the 60 warning); closest workspace question token ratio 0.28, longest shared run 5 tokens (aq-docket-trial-05 q01).
10. Set: q01 uses different documents (D10, D09) and asks for a count; sketch i02 shares D03 L155 and D04 fn8 — do not promote it beside q02.
11. Records: rev 0 and fingerprint 6c6613e0… consistent across snapshot, both solver records, closed-book and audit; report recomputes the same value. Probes bound to q02-r0-probe-h8 as supplementary evidence. No platform record (Q13 unknown); platform-only checks unknown (restricted names, duplicates, token window, AI-use).
