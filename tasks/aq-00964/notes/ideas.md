# aq-00964 - candidate evidence plans

Current target: easy (change explicitly to medium or hard). Platform success: unmeasured.
Generate different dependency mechanisms before polished wording. Every plan includes facts
with quotes and locations, operations/intermediate results, complete membership/exclusions,
all-bundle document necessity tests, a computed natural wrong route, actual shortcut probes,
precision/readings, source completeness and accurate authorship.

All plans below: origin claude (caller, Claude Code, Opus 5.5), round 1, 2026-10-05. Line
numbers are text/Dnn.txt lines; Dnn = platform Doc N. Outlook figures are in narrative/outlook
sections, which the map confirms are never cut; gaps sit only in statement/reconciliation tables.

| ID | Family/world fact | Question and short gold | Necessary dependencies | Natural wrong answer and deciding fact | Actual cheapest route found | Source gaps | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| i1 | Edition bridge into a middle edition | Outlook in effect at the Philippines sale, Africa & APAC 2026 midpoint -> $1,605M | D07 sale date + segment footnote; D06 outlook dated April 28, 2026 | 1,630 (D07's own July 28 outlook, same document as the sale); 1,545 (D05); 1,740 (Latin America) | "June 15, 2026" only in D07 l.117; no passage joins the sale to an outlook | none relevant | q01 r0 checked: A/B match, audit clear, closed-book misses, review revise (capture gaps only), easy marginal |
| i2 | Prose mentions vs actual segment raises | Segments raised at both 2026 updates -> Latin America, Africa & APAC | D05, D06, D07 segment ranges | Prose route: Latin America (Apr) + Data Centers (Jul); Data Centers raised only in July | No passage states segment-level changes; prose names LatAm, Data Centers only; audit: one grep on footnote (1) finds all inputs | none relevant | q04 r0: A/B match, audit clear, closed-book misses (answered Data Centers); review running |
| i3 | Inferred non-FX residual with a sign flip | 2025 property revenue midpoint change net of cited FX, three updates -> +$25M | D02 (50/50), D03 (165/130), D04 (40/50) | 35 (treat Oct "primarily FX" as all FX, or drop negative); 45 (abs); 255; 230 | "core outperformance" only D03 l.181, no amount; nothing prints a residual | none relevant | q02 r0: A/B match, audit clear, closed-book misses (+$100M guess); review running |
| i4 | Reconstruct an out-of-bundle edition | Actual FY2025 Adj. EBITDA minus pre-April 2025 outlook midpoint -> $240M | D02 midpoint 6,920 and stated $30M raise; D05 actual 7,130 | 210 (take D02's April outlook as the one in place); 90 (Jul); 44.5 (Oct) | "6,890" printed nowhere; overview prints 7,130 (Doc 5) | none relevant | q03 r0 DROPPED: closed-book reached "About $240 million" by estimation (inputs wrong, difference right); family closed |

## Round 1 additions (2026-10-05)

- i5 (caller, origin claude; hook h5): currency assumed to weaken most between the February and July 2026 outlooks -> Peruvian sol (+2.99% units per USD); decoys Nigerian naira (largest move, a strengthening), Paraguayan guarani (largest absolute), Ghanaian cedi (April base). Sketch screen passed; promoted to q05 r0 (A/B match, audit clear, closed-book misses; review running).
- question-author round 1 (independent agent, origin claude; returned 5 candidates, wrote no files):
  - a1 definition applied to an instance: the 242 sites bought in Q1 2025 stop counting as "new sites" once the prior-year comparison period starts after Q1 2025; last quarter still counting them = Q1 2026; author asked U.S. & Canada New Site Tenant Billings ($1M). Caller variant: company total ($12M) because the U.S. & Canada value (1) coincides with the acquisition-quarter decoy (Q1 2025 = 1). Decoys: Q2 2026 13, Q4 2025 10, Q1 2025 10. -> promote as q06.
  - a2 segment midpoints that fell Apr -> Jul 2026 once international pass-through is excluded -> Africa & APAC, Europe. Held: third question on the same 2026 segment outlook data as q01/q04.
  - a3 AFFO raises above the cited currency benefit -> October 2025, July 2026. Not promoted: same raise-vs-FX evidence as q02; each item decided inside one release (per-item filter risk).
  - a4 July 2026 expected straight-line revenue (components table (66)) minus 2025 actual $101.0M -> -$167M; sign trap: reconciliations print "66" as a positive add-back (-> -35). -> promote as q07.
  - a5 count of currencies against which the dollar was assumed weaker Apr -> Jul 2026 -> 7. Not promoted: same FX-list family as q05 (keep one).

## Round 1 outcomes (2026-10-05, local only; platform pending)

| Q | Mechanism | Gold | Local result | Quick-test plan |
| --- | --- | --- | --- | --- |
| q06 | definition applied to an event (New Site cutoff) | $12 million | checked, review ready; risk moderate-high | batch 1 |
| q01 | date bridge into the middle 2026 edition | $1,605 million | READY: platform difficulty check Run 1 "In band — Medium tier" (Low 0/5 · Medium 1/5), all wrong attempts took the same-release July outlook (1,630); v2.1 review ready + per-label Source assessment | passed |
| q04 | segments raised at both 2026 updates vs prose | Latin America, Africa & APAC | checked, review ready; risk moderate-high | batch 1 |
| q05 | FX quote direction across two editions | Peruvian sol | checked, review revise (reasoning form only); risk high | batch 1 |
| q02 | 2025 outlook change net of cited FX (sign flip) | +$25 million | checked, review ready; risk high | batch 1 |
| q07 | straight-line sign convention vs 2025 actual | -$167 million | checked, review revise (cut D05 row may move gold) | held |
| q03 | reconstructed pre-April outlook vs actual | $240 million | dropped (closed-book reached) | none |

Survivors of a quick test get rev 1 fixes (q02/q05 uncited calculation steps, q04 reasoning phrase,
q07 re-pin) before full write-up and the final exact-content difficulty check.

## i1 - outlook in effect when the Philippines subsidiary was sold

- Draft wording (33 words): "When American Tower completed the sale of its Philippines subsidiary,
  what full-year 2026 property revenue midpoint was its then-current outlook projecting for the
  segment that included that subsidiary?" Gold: $1,605 million.
- Evidence: D07 l.117 "On June 15, 2026, the Company completed the sale of its subsidiary in the
  Philippines (“ATC Philippines”)"; D07 l.531/l.567 segment header "Africa & APAC(1)" with
  "(1)Includes results of Bangladesh and the Philippines through dates of sale."; D07 l.153
  "expectations as of July 28, 2026"; D06 l.149 "expectations as of April 28, 2026"; D06 l.173
  "Africa & APAC property revenue of $1,595 million to $1,615 million" -> (1,595+1,615)/2 = 1,605.
  D07 l.41 CEO: "raise our full-year outlook for the second time this year" (no other 2026 update
  between April 28 and July 28).
- Dependencies: sale date (D07 only) decides the edition; the edition (D06 only) supplies the
  range. D07 cannot back out the April segment midpoint: its stated raises (l.159) are
  consolidated only. D05 is a decoy, not needed.
- Counterfactuals: no date check -> D07 1,620-1,640 = 1,630; earliest 2026 outlook -> D05
  1,535-1,555 = 1,545; wrong segment -> D06 Latin America 1,740.
- Readings: "then-current" = latest outlook issued on or before June 15, 2026 = April 28. Segment
  identity is also ordinary geography (Philippines in Asia-Pacific); D07 footnote confirms.
- Probes: "Philippine" hits D02-D06 only in FX-rate lists (l.175/177/151); D07 l.117, 567, 675.
  "1,605" hits only beginning-cash 1,605.2 (D06 l.507, D07 l.505). Overview Doc 7 lists "ATC
  Philippines" and "June 15, 2026" separately, no outlook figures.
- Risk: three lookups plus a date comparison; the lever is the date relation, not printed.

## i2 - segments raised at both 2026 outlook updates

- Draft wording (34 words): "Which of American Tower's property segments had the midpoint of
  their full-year 2026 property revenue outlook raised at both the April 2026 and the July 2026
  outlook updates? List them in any order." Gold: Latin America, Africa & APAC.
- Evidence: D05 l.195, D06 l.173, D07 l.177 (segment ranges). Midpoints D05/D06/D07: U.S. &
  Canada 5,090/5,090/5,090; Latin America 1,655/1,740/1,800; Africa & APAC 1,545/1,605/1,630;
  Europe 1,040/1,040/1,040; Data Centers 1,185/1,185/1,210. Sums 10,515/10,660/10,770 match the
  consolidated midpoints. Prose: D06 l.155 "accelerating straight-line revenue in Latin America";
  D07 l.159 "Data Center outperformance and one-time expense benefits".
- Universe: the five 2026 outlook segments. Included: LatAm (+85, +60), Africa & APAC (+60, +25).
  Excluded: Data Centers (0, +25), U.S. & Canada (0, 0), Europe (0, 0).
- Counterfactual: prose-only route -> Latin America and Data Centers (or Latin America alone).
- Necessity: D05 needed for the April deltas, D06 for both, D07 for July. No substitute.

## i3 - 2025 property revenue outlook change net of FX

- Draft wording (37 words): "Across American Tower's April, July and October 2025 updates to its
  full-year 2025 outlook, what was the combined change in the total property revenue midpoint
  after removing the estimated foreign-exchange effect each update cited? Give the sign."
  Gold: +$25 million.
- Evidence: D02 l.177 FX "approximately $50 million" (property revenue) and l.181 raise "$50
  million"; D03 l.177 FX "$130 million", l.181 raise "$165 million"; D04 l.179 FX "$50 million",
  l.183 raise "$40 million ... primarily as a result of estimated positive foreign currency".
  Residuals 0, +35, -10 -> +25. Midpoints confirm raises: 10,045 -> 10,210 -> 10,250.
- Counterfactuals: 35 (October treated as all FX / negative dropped); 45 (absolute values); 255
  raises; 230 FX. D02 and D04 print the same FX set ($50M/$30M/$20M/$0.04): mixing them up gives
  other totals.
- Readings: FX figures are "approximately"; answer is approximate by construction. Pin "after
  removing the estimated FX effect each update cited". 2025 guidance may be known closed-book.

## i4 - actual 2025 Adjusted EBITDA vs the outlook in place before the Q1 2025 release

- Draft wording (33 words): "By how much did American Tower's actual 2025 Adjusted EBITDA exceed
  the midpoint of the full-year 2025 outlook the company had in place before it reported its
  first-quarter 2025 results?" Gold: $240 million.
- Evidence: D02 l.195 "Adjusted EBITDA(3) 6,885 to 6,955" (midpoint 6,920); l.181 raising
  Adjusted EBITDA midpoint "by ... $30 million" relative to "prior 2025 outlook" (l.177); D05 l.43
  "Adjusted EBITDA increased 4.7% to $7,130 million". 6,920 - 30 = 6,890; 7,130 - 6,890 = 240.
- Counterfactuals: 210 (D02 midpoint taken as the outlook in place); 90 (D03 7,040); 44.5 (D04).
- Risks: general knowledge of AMT's February 2025 guidance and FY2025 actual (closed-book check
  needed); "in place before" must not read as D02 itself.
