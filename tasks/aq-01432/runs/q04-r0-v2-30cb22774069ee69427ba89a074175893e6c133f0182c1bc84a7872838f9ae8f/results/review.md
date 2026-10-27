# q04 rev 0 - independent review (fresh question-review subagent), 2026-10-08

Raw return as received (harness indent removed). Usage reported: 57 tool uses, about 891 s.

q04 (rev 0; tested_sha256: 30cb22774069ee69427ba89a074175893e6c133f0182c1bc84a7872838f9ae8f)

gold_verified: yes. I rebuilt the answer from the original passages before reading the author's gold.
- The universe is six illustrated services in Doc 5 (D04):
  - chapter 6, examples 1-3 (L428-432);
  - the 7.1 inline detection-bypass example (L444);
  - chapter 7, examples 1-2 (L448-452).
  A seventh, fringe candidate is 5.1(b), paid ranking prominence (L410-412). It is framed as misleading publication and fails anyway: no Part 465 route reaches it.
- In:
  - Example 1 is a paid recruiting broker. Doc 2 L63 says brokers of fake reviews fall under 465.2(a)'s selling prohibition, and 465.4 also applies if the pay is tied to sentiment (L35).
  - Example 2 sells purported-consumer reviews (L19, L31, L35).
  - Example 3 creates fake reviews (L35).
- Out: the 7.1 example and chapter 7 examples 1-2 write, create, sell or buy no review.
  - 465.8 covers selling or distributing influence metrics (L291-301; Doc 1 (g), (h), (j)).
  - Hosting is exempt (L71, L83), and nothing in 465.2-465.8 covers facilitation.
- Gold = 3 items. Membership counts recomputed: adding account set-up gives 4; all facilitation services give 5 or 6; dropping example 1 gives 2; applying the UK ban gives 6.

outcome: A: match; B: match. Both are fresh and uncontaminated, and each raised and rejected the two-item reading and the 465.8 reading. That gives two local matches.

closed-book: misses. It gave generic classes plus conditional 465.4/465.8 additions and named none of the guidance's examples, so it is not equivalent to the gold.

necessity:
- Doc 5 (D04) is the only source of the examples.
  - D09 L561-573 gives generic limbs and defers the examples to "separate guidance". D06 L15 points to the full guidance. D10 L83 and D11 L70/98/115/126 are generic.
  - Probe without Doc 5: unforced "can't fully answer"; forced guess generic classes, p 0.35. Miss.
- Doc 2 (D03): its unique fact is L63 (brokers = selling), which decides example 1. It is also the staff reading the question names.
  - Doc 1 (D01) repeats 465.2(a), 465.8, the definitions and the hosting exemption, but not L63. Doc 3 (D05) is pre-rule FTC Act guidance (L259, L594).
  - Probe without Doc 2: unforced "can't be fully determined"; forced guess two items p 0.5, gold p 0.3. Miss.
- No smaller set works. Doc 5 + Doc 1 leaves example 1 to inference.
- (c) Do not group Doc 1 with Doc 2 as alternatives. Doc 1 lacks the deciding broker reading and is not "FTC staff". Grouping also means ticking and quoting Doc 1, and how the Document check treats groups has not been observed.
- Residual risk: a decisive platform high model could still include example 1 without Doc 2. It could get there through Doc 1's "sell"/465.4, Doc 3 L594 (an intermediary that recruits "could be liable"), or recall of the November 2024 staff Q&A, which our closed-book solver said it recalls. I estimate a "may not be needed" flag on Doc 2 at about 30-40%. Fallbacks (an exclusion/condition-source role with a note, or grouping) would each need a new version and a new run.

shortcut: clear.
- The shortest route checks out: Doc 5 L424-432 (chapter 6, "acting as a broker"), then Doc 2 L61-63 and L33-35.
- No document maps the UK examples to the US rule. The UK documents carry no FTC or 465 terms, and the FTC documents carry no CMA or UK terms. The overview summaries reveal nothing.
- This is a difficulty risk, not a shortcut: the gold is chapter 6's entire example list, bridged by the shared word "broker", and the excluded items are the whole group labelled "facilitate".

source_assessment: no gaps. Intake shows 11/11 documents with incomplete: false and 0 gap characters; the report gives source_gaps [] (sha 4f53cda1...).
- One extraction artefact: in Doc 1, 465.2(a) has displaced words (L132-161), the same in the docs/ original.
- Doc 1 is neither ticked nor cited. The artefact touches only the path without Doc 2, where it makes the rule harder to read.
- It has no effect on premises, gold, exclusions, uniqueness, necessity of the ticked documents or the shortcut route.

difficulty: easy. This is below the medium target.
- On this bundle, a labelled-group join (q03) and a one-sentence rule application (q01) both measured Too easy, Low 5/5. q04 repeats that shape: the answer equals one labelled section, joined by a shared word.
- The decoys work only through a word match that both strong solvers called strained or weak.
- My odds for one run:

| Outcome | Estimate |
|---|---|
| Too easy | 55-65% |
| In band at Easy (before the gates) | ~30% |
| Usable Easy pass (after the Doc 2 risk) | ~15-20% |
| Medium | ≤5% (usable ~2-3%) |
| Other failures (Doc 2 flag, answer not supported, vague block) | the rest |

verdict: revise (light, form quality only). The gold, uniqueness, necessity and shortcut results stand locally.

(b) Minority readings:
- **Concealed-incentive branch of example 1 (two items):** the most plausible minority, but "would expose" is met by the fake-review branch, backed by L63, L424 and 465.4. Risk that both form solvers agree on it: ~3-6%. Risk of a reviewer "ambiguous" finding: ~5-10%. No question change is advisable: "could" would loosen the facilitation exclusions. The only fix is reasoning that says the fake-review branch alone suffices, which is fingerprinted.
- **Account set-up under 465.8:** weak (accounts are not metrics, and the account set-up service is about evading review detection). It is the declared trap, so leave it.
- **7.1 detection bypass:** weak; posting is not writing, creating or selling.
- **AI stock avatar (L137):** weak; that answer is about marketing avatars, while L19 covers a "purported consumer's evaluation".
- **"Isn't definitive" (L13):** a disclaimer, not a competing answer.
- **Figure 1 categories:** under 2%; "illustrates" matches D09 L573's "illustrative examples".
- Overall "too vague" block risk is about 5%.

failure_modes: Mode 1 is real but weak, and was never produced by any run.
- The passages exist (Doc 5 L448-450 against Doc 2 L297), and the wrong answer recomputes to 4 items.
- Trap "Linking across documents" is a defensible fit.
- Cause: "Misapplies a rule or premise" (misreading 465.8's scope, the first wrong step) fits better than "Wrong members in a list", which is the symptom. Change it; this is outside the fingerprint.
- The boxes total 298 words. Three phrasings overclaim:
  - Doc 2 "defines": it reports that "the rule defines" (L297).
  - "supplies only the accounts, so that its client's fake reviews avoid detection": L448 says "enable accounts to be set up"; the fake-review purpose comes from the chapter.
  - "calls brokering banned reviews": L424 says the element targets the broker business model.
- Do not declare a second mode. The two-item and avatar routes are unobserved with all documents, and declaring the two-item route would spotlight the branch ambiguity. The all-UK route is ruled out by the wording.
- The roles section is absent, so both documents default to Answer component, which is accurate.

findings:
1. **Q14 evidence tags.** Four exclusion/decoy rows tagged [c2] (Doc 2 L35 second sentence, L301, L297; Doc 5 L448) will show on the form as support for "selling bot-generated reviews". L297's "generated by bots" invites reading c2 as resting on 465.8, contrary to Step 3, and the L448 row supports no component. Risk: the "Evidence supports its component" advisory or a reviewer returning it for "Wrong / missing evidence". Fix: drop the rows or attach them neutrally. Evidence is fingerprinted, so re-prepare and re-run A, B, the closed-book solve, the shortcut audit and both probes.
2. **Optional, same revision:** a clause in Step 3 on example 1's concealed-incentive branch. Also tighten Step 4's analogy: L71 is about a retailer hosting reviews, while the UK platform hosts sellers whose reviews are posted elsewhere.
3. **Q2 Doc 2 platform risk** as above. It is stated, not demonstrated: both local probes missed unforced.
4. **Q15** cause and wording edits as above (outside the fingerprint).
5. **Records:** all six are rev 0 / 30cb2277. The current file recomputes to 30cb2277, and the form hash bfda43f9 equals the snapshot. Probe packets in q04-r0-alt-k8 have byte-identical document bodies (sampled) and question bytes. Floor: 0 FAIL, 1 WARN (origin; export accepts origin: user only, and that tick is the user's decision).
6. **Platform:** pending, no platform record, status draft. Easy is below the medium target, so whether to use the open Easy slot is the user's decision. Never submit with q02 (same family). The 5-15% odds above are local judgement, not platform evidence.
7. **Disclosure:** I wrote one temporary script in the session scratchpad, outside the workspace, for the token-overlap check (max 0.30 vs q02, longest shared run 5). Nothing in the workspace was written.

Files: d:\Agents\Docket\tasks\aq-01432\questions\q04.md; d:\Agents\Docket\tasks\aq-01432\runs\q04-r0-v2-30cb22774069ee69427ba89a074175893e6c133f0182c1bc84a7872838f9ae8f\results\; d:\Agents\Docket\tasks\aq-01432\runs\q04-r0-alt-k8\
