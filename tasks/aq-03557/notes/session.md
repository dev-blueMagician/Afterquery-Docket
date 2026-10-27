# Current bundle checkpoint

Working memory for resuming aq-03557. Updated 2026-10-12 (q01 submitted at Medium; verdict read and recorded).

- Goal and user constraints: user, 2026-10-12: "there is no slot for Easy Tier for this bundle, we should target
  medium and high. do your best." Easy is not usable and is not to be offered or re-asked.
- Verification target / measured platform tier: medium (Hard welcome) / q01 rev 2 "In band — Medium tier", Low
  0/5 · Medium 1/5 · High — (Run 1, Version d8243a). Page 17:18 showed "Hard 0/2 · Medium 1/3 · Easy 0/1".
  Difficulty runs 14 of 15 left.
- Prepared run / tested_sha256: q01 rev 2 runs/q01-r2-v2-114f324f...-platform /
  114f324f94a54e12d54cca42851d4d249f827dc0d4f5408a4b32b75b972080dd (rev 0 8e203179..., rev 1 c31b1263...: history).
- Bundle / documents / extraction: aq-03557; nine papers from the NZ Commerce Commission's grocery market study.
  Local ids differ from Doc numbers (table in doc-map.md). No gaps; charts and Table A.1's shading are absent.
- Phase: submitted (q01); review outcome pending.
- Questions:
  - q01 (i01, h1), status submitted, accepted_tier: Medium Tier, rev 2, origin user+claude. FROZEN: do not edit;
    later observations go to notes/feedback-q01.md. Question (the user's wording): "With the number of stores
    Woolworths provides, how many supermarkets trade under banners that any retailer's submission says have no
    loyalty programme?" Gold 376 supermarkets (56 + 245 + 71 + 4). Necessary: Doc 7, Doc 3.
  - Sketches, never tested: i02 (83.3%, Doc 8 + Doc 7), i04 (63 products, Doc 8 + Doc 5; sibling of i02), i03
    (Specials, Club Prices and Multibuys, Doc 7 + Doc 1).
- What Run 1 showed (each attempt's own text; notes/feedback-q01.md): low attempts 301 four times and 71 once;
  none read Doc 3's FreshChoice sentence or found Raeward Fresh's count in Doc 7. Medium: 71 twice (opening
  read as Woolworths' own stores), 372 once (route unread), one output loop with every input found, one right.
  High with every document: 376. Both documents needed. Closed-book missed. The pharmacy decoy caught nobody.
- Open findings: (1) three Reasoning blocks were saved unloaded (Medium 2, Medium 3, one removal attempt).
  (2) Declared mode 2 (392) caught no attempt and the modes were not aligned before Submit. (3) No evidence row
  quotes Woolworths calling Chemist Warehouse a pharmacy retailer. (4) The submitted form and the Checks on
  rev 2 were not captured. All four are logged as soft spots; nothing can be changed unless the task is returned.
- Decisions and constraints: answers that name or count submitters are out (newer guide rule 10); questions at
  about 20 words. Rejected hooks are in hooks.md.
- Active feedback index / issue ids: notes/feedback-index.md: aq-03557-q01-D1 (Medium, submitted), -F1, -F2, -P1.
- Five-candidate trial / timing: not enrolled; short timers for i01 in the ledger, reading untimed (partial).
- Efficiency ledger / candidate ID / active timer ID: ../../../notes/efficiency.json / i01 / none.
- Next action: wait for the review outcome. If "Revision requested" arrives, log the panel word for word in
  notes/feedback-q01.md first, then revise in place as rev 3 and change only what is asked. If another question
  is wanted here, quick-test i04 and i02 (a different family from q01).
- Runtime/model/effort: Claude Opus 5.5 (claude-opus-5-5), VS Code extension; pinned in .claude/settings.json.
- Optional diagnostic: none run.
