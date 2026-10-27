# aq-02486 - lean candidate sketches

Current target: medium (user 2026-10-09: no Easy slot, "target medium and high"); measured platform
success pending. Hooks in notes/hooks.md; origin claude unless stated.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | notes/sketches/i01.md | h1: ONCD's proposed FOIA charge minus the Access Board's for photocopied pages to a news reporter: 225 pages, $12.50 (rev 0); 216 pages, $11.60 (rev 1) | Competing: -12.50 (Access Board's inclusive $25.00 no-fee rule missed, or read as strict), 0 (rule wrongly applied to ONCD, whose $25 is notice only), +22.50 (ONCD Privacy Act copying rule), -22.50 (free pages dropped). Necessity: D05 only source of ONCD's rules, D07 of the Access Board's; removal probes both "not answerable" (forced gold p 0.25 / 0.15 by assumption) | promoted to q01; rev 0 (36d0dfd0...) drew the form flag "Step 1: Which document says 225?" (f1); rev 1 (35dd0246...) 216 pages, Run 1 In band Easy, Low 2/5 (f2); rev 2 (f377c49c...) asks the total paid, checked; quick test first |
| i02 | (no file) | h3: minutes more NRC bills than the Peace Corps for one 6 h 20 min search, 45 | superseded by i04 (author A's sharper version) | closed |
| i03 | notes/sketches/i03.md | h9: FLRA's FOIA fee minus NRC's for 1,400 paper pages after a one-hour search, nonprofit advocacy group willing to pay all fees, $65 (1,400 printed in Doc 1; 500 was printed in neither) | NRC's PDR $0.30 (L630) beside its FOIA $0.20 (L660) flips the sign (-$65); priority -$130; FLRA $25 deemed agreement excluded by wording (-$235); no free pages $70. Recall risk for both older rates; D03 inputs deep (88-97k chars) | screen passed; quick-test sketch only |
| i04 | notes/sketches/i04.md | h3 (author A): minutes more counted toward fees at NRC than the Peace Corps, nonprofit group's 5 h 22 min search, 45 | 30 (last 7 min charged), 38 (exact), -15 (NRC nearest hour). D02 not unique: D01 L179 prints the same more-than-half sentence (Document-check FAIL risk); probe without D02 required before any difficulty run | screen passed; quick-test sketch only, ranked below i03 |

Independent authors (2026-10-09), each having read all seven texts:
- A (numeric emphasis): no design fits a measured Medium recipe (no untied anchor: proposals never take effect
  in the bundle, final rules print no earlier text; every numeric design is parallel fee rules applied to one
  request). Sharpened h1 (combined charge, $12.50) and h3 (i04). Flags: NRC 9.37(d)(4) exempts news media and
  educational requesters from duplication fees without the template's missed-deadline condition (L689), so no
  NRC news-media design; D05 2200.10 "shall waive" (L303); D05 2200.1 vs 2201.7 conflict for first-party
  requests; D02 no per-page rate. Rejected: Access Board vs ONCD crossover page (D07 collection-cost rule),
  prepayment thresholds, I-246 vs 43% (gold flips between printed 387 and recomputed), D04 percentage filters,
  in-force $14/hr anchors, CPI-U cross-application, agency-name filters.
- B (qualitative levers): FLRA's fee minus ONCD's, 320 pages, $33 (shares q01's ONCD path; one ONCD question
  per set) and Copyright Office minus NRC PDR fax charges, $48 (D04 prose prices fax delivery at $10 while the
  codified row says per page: a too-vague risk). Hedge words attach only to practice statements; D06 isolated.
Closed: h6 (parse-heavy table filter), h7 (agency-name answer), h8 (date lookup of citations), B's fax design.
