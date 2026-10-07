# q05 rev 0 - question-review

- Date: 2026-10-05
- tested_sha256: 6dc6f72e4e2b5888df2e7a9939451c1dc757c727b090ce5c67c691f380b413a7
- source_gaps_sha256 (as stated by the reviewer): 482e178fa029ca11a664427aba78990c8f2206303c7508fdadd711d962234b19
- Role: question-review, fresh context; input = root, slug, q05, rev 0, fingerprint, gap hash, target easy,
  the run's results/ files (solver-A, solver-B, shortcut-audit, closed-book), set context.
- Usage: 247,997 subagent tokens, 68 tool uses, 816 s.

## Raw return (verbatim)

q05 needs a revision, but a narrow one. The gold, both blind solves, the closed-book miss and the shortcut audit all hold. The only defect is in the reasoning field, and because that field is part of the fingerprint, fixing it means a new revision and fresh checks.

**q05 (rev 0; tested_sha256: 6dc6f72e4e2b5888df2e7a9939451c1dc757c727b090ce5c67c691f380b413a7)**

**gold_verified:** yes.
- I parsed D05 l.175 and D07 l.155 with a script. Both lines are byte-identical to the docs/ originals.
- **Premises hold.** Only two FY2026 outlooks fall in February or July 2026: "as of February 24, 2026" (D05 l.173) and "as of July 28, 2026" (D07 l.153). D03's July outlook is for 2025.
- **Universe.** 15 currencies appear in both lists. The Bangladeshi taka and Philippine peso appear only in February.
- **Change in units per dollar, February to July:** Peruvian sol 3.35 to 3.45: +2.985%; Ghanaian cedi: +1.724%; Euro: +1.176%; Kenyan shilling: +0.746%; CFA franc: 0; the other ten fell, meaning those currencies strengthened: Ugandan shilling −0.53, Canadian dollar −0.72, rand −2.35, Chilean peso −3.76, Mexican peso −4.89, real −6.36, Argentine peso −7.17, Colombian peso −8.19, guarani −10.00, naira −10.97.
- **Other convention.** Measured as each currency's dollar value, the sol falls 2.899%. The ranking is identical (the two measures always rank the same way).
- **Robustness.** The sol leads the cedi by 1.26 points. Taking the printed rates at their least favourable rounding, the sol's smallest possible rise (+2.68%) still beats every rival's largest (euro 2.37%, cedi 1.81%, Kenyan shilling 1.50%).

**outcome:** A: match; B: match.
- Both answered "Peruvian sol" with high confidence, on rev 0 with this fingerprint, from separate packets (solver-1, solver-2), and both report no contamination.
- Both raised the April-baseline reading (cedi, +7.27%) and correctly rejected it because the question names February.
- B noted that the two outlooks average over different windows. That does not create a second answer, since these are the only stated assumptions.
- That gives two fresh matches.

**closed-book:** misses. It answered "South African rand" with low confidence and no tool use. That is not equivalent to the gold, and the rand was in fact assumed to strengthen (−2.35%). No contamination.

**necessity:**
- **D05** is the only source of the February rates. The sol's 3.35 and the cedi's 11.60 are printed only at D05 l.175. Without it, the nearest baseline is April (D06), which gives the cedi. D07's currency paragraph (l.157) gives only consolidated dollar amounts "relative to the Company's prior 2026 outlook".
- **D07** is the only source of the July rates. The sol's 3.45 and the cedi's 11.80 are printed only at D07 l.155. Without it there is no rate after April.
- Some other rates recur in other editions (euro 0.85 in D06; euro 0.86 and naira 1,550 in D04). Those are different editions' assumptions and cannot stand in for the deciding pairs.
- No smaller valid set exists. D06 and D02–D04 are decoy editions only.

**shortcut:** clear. The shortest route I verified is the auditor's: D05 l.175 plus D07 l.155, 15 ratios, then the largest rise.
- I searched the whole bundle for weaken, depreciat, devalu, strength, appreciat, Peru and sol, and for each country name outside the rate lists. The hits are accounting "depreciation", CEO and risk-factor "strength", and South Africa Fiber passages. Nothing ranks or compares currency moves.
- The capture overview (D:\Dev\Docket\AQ-00964_2026-10-05_2031.md l.30–102; its hash matches intake) contains no currency names or rates.

**source_assessment:** All 151 labels are irrelevant to all six dimensions (source_gaps_sha256 482e178fa029ca11a664427aba78990c8f2206303c7508fdadd711d962234b19). The corpus stays labelled incomplete.

Evidence that applies to every group:
- The question's inputs (D05 l.173–175, D07 l.153–155) contain no markers. The first markers are at D05 l.439 and D07 l.419.
- Each rate list is one complete sentence with consecutive item letters: D05 (a)–(q), D07 (a)–(o), each ending "560 West African CFA Francs." So no list item is cut.
- Each document's marker sizes add up exactly to its stated shortfall (checked by script), so there is no unmarked omission.
- I checked the lines on either side of every marker; each sits between visible rows or headers of a table of actual results.

Per group:
- **G1, balance sheets (18):** D02 449/455/461; D03 449/455/461; D04 451/457/463; D05 439/445/451; D06 415/421/427; D07 419/425/431. Premises: quarter-end balances cannot date or define either outlook. Gold: they hold no assumed rates. Exclusions: they cannot add a July rate for the taka or peso, or change any visible rate. Uniqueness: no third rate set can sit here. Necessity: D07's balance sheet cannot restate February assumptions. Shortcut: account rows only.
- **G2, statements of operations (19):** D02 473/479/489; D03 473/479/489; D04 475/481/491; D05 463/469/479; D06 439/445/455; D07 443/449/453/457. Premises: actual-period lines only. Gold: currency effects appear only as one total unrealized gain or loss, in a visible label. Exclusions: they cannot change the 15-currency universe. Uniqueness: no per-currency rows. Necessity: the comparison columns are prior actual periods, not prior outlooks. Shortcut: line items only, no prose.
- **G3, cash flows (28):** D02 545/549/553/557/561; D03 541/545/549/553/557; D04 539/543/547/551/555; D05 527/531/535/539/543; D06 489/493/497/501; D07 487/491/495/499. Premises: actual cash movements only. Gold: no rates. Exclusions: D07 491 may hold the Philippines and Bangladesh sale proceeds; that explains, but does not decide, the two currencies leaving the list; the exclusion rests on the 15-item list itself. Uniqueness: no rate set. Necessity: cannot restate the February rates. Shortcut: dollar rows only.
- **G4, segment tables and Tenant Billings bridges (42):** D02 591/607/619/653/669/681; D03 587/603/615/649/665/677; D04 587/603/615/649/665/677; D05 573/589/601/629/645/657/685/701/713/743/759/771; D06 533/549/561/589/605/617; D07 535/551/563/593/609/621. Premises: actual quarter and year results by segment. Gold: the cut currency-impact rows are dollar amounts per region, not per currency; the sol (Latin America) and cedi (Africa & APAC) can't be ranked from them. Exclusions: they cannot change the 15-currency universe. Uniqueness: no third rate set. Necessity: they cannot restate the February or July assumptions. Shortcut: numeric rows only.
- **G5, reconciliations of actual Adjusted EBITDA, FFO and AFFO (24):** D02 711/737/741/787; D03 707/733/737/781; D04 707/733/737/783; D05 797/823/827/871; D06 643/663/667/691; D07 647/667/671/695. Premises: actuals only. Gold: currency gains and losses appear as totals in visible footnotes, not per currency. Exclusions: they cannot change the 15-currency universe. Uniqueness: no rate set. Necessity: the 2026 outlook reconciliations (D05 l.255–331, D07 l.237–313) are fully visible and contain no rates. Shortcut: numeric rows only.
- **G6, segment gross-margin reconciliations (14):** D02 801/815; D03 795/809; D04 797/811; D05 887/895/905/913; D06 701/709; D07 705/713. Premises: actual dollars by region. Gold: no rates. Exclusions: they cannot change the 15-currency universe. Uniqueness: no rate set. Necessity: cannot restate either outlook's rates. Shortcut: numeric rows only.
- **G7, document-level labels (6):** 7,808, 8,081, 8,464, 11,021, 7,412 and 8,075 characters. Each equals the sum of that document's markers above, so no cut exists anywhere else, including inside D05 l.175 or D07 l.155. D02–D04 predate the first 2026 outlook, so their cuts cannot hold one.

**difficulty:** easy. This is local suitability only, and the risk of a "too easy" verdict is high.
- **In favour:** the deciding rates exist only in this bundle and postdate the closed-book solver's cutoff; no passage or overview gives the answer away; getting the quote direction right decides the answer (reading it backwards gives the naira); measuring in percentages also decides it (absolute units give the Kenyan shilling among the weakening currencies, or the guarani overall); an April baseline gives the cedi.
- **Against:** the inputs are two parallel, labelled sentences that one search finds; the question names both months, so the April decoy only works on a misreading; the work is one standard ratio plus picking the largest; the same shape (labelled values in two documents, one standard step, a direction or sign trap) was returned "too easy" in trial-02 q01 and trial-07 q05.
- There is no platform evidence for this question yet.

**verdict:** revise.

**findings:**
1. **Reasoning field, form check.** Step 3 names no document but derives 2.99%, 1.72%, 1.18% and 0.75%. The Decoy line derives −10.97% without naming a document. None of these values is printed anywhere in the bundle. This is the pattern the form flagged on aq-docket-trial-01 rev 4 ("Which document says 10.123%? Add 'Doc N'"). Two secondary local-review risks: Steps 1 and 2 restate "February 2026" and "July 2026"; D05 and D07 only print February 24, 2026 and July 28, 2026. Step 3 spells out derived counts (fifteen, four, ten). Required: move the percentage and decoy calculations into steps that cite both documents, use printed dates in cited steps, and drop the spelled-out derived counts. Then: rev 1, a new prepare, and fresh A, B, closed-book, audit and review runs on the new fingerprint. The question, answer, components, evidence, documents and tags need no change.
2. **Records.** The Blind solve, Shortcut audit, Review and Source assessment sections of q05.md are empty, and `report` shows no records for this revision (`current_revision_records: []`). Whichever revision goes forward needs those entries, plus a per-label Source assessment JSON bound to 482e178f….
3. **Lever-check notes** (outside the fingerprint, so no retest needed): the taka and peso also appear in D02 l.175, D03 l.175 and D04 l.177, not only D05/D06; the exact margin over the cedi is 1.26 points, not 1.27; absolute units among the weakening currencies give the Kenyan shilling (+1), a route that isn't listed; February to April alone also gives the sol, so the edition lever only bites on the starting outlook.
4. **Set overlap.** This question uses evidence no sibling uses (the rate lists) and is the first in the set to need unit normalization. It still repeats the outlook-edition comparison family (all four live questions) and shares the D05/D07 pair with q04. Neither gives the other away. The wording "both … July 2026" mildly echoes q04. Holding back a5 (counting currencies, April to July) was right.
5. **Isolation.** `.claude/solver-scope.json` now points to q07's run, so the q05 binding at solve time can't be re-verified from current state. The packets contain only question.txt and corpus files matching the snapshot hashes, and the returns cite only packet paths. I found no sign of contamination.
6. **Platform-only checks, unknown:** how the form treats a step that cites two documents; restricted names, originality and duplicate checks; token window; the question-length-spread advisory (q01, q02, q04 and q05 are all 30–40 words); the comparison is pinned as "in percentage terms" but the base is not named. Both bases rank identically, so the advisory risk is low.

The mechanical floor shows 0 FAIL and 1 WARN. `origin: claude` is accurate, but the export tool only takes `user`, so whether to submit is your decision.
