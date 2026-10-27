# aq-03557 - lean candidate sketches

Current target: medium, Hard welcome (user, 2026-10-12: "there is no slot for Easy Tier for this bundle, we should
target medium and high"). Measured platform success pending. Hooks are in notes/hooks.md; facts and checks are in
the linked sketches.

## Round 1 (2026-10-12): four sketches, one written up

| ID | Sketch | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 -> q01 | [sketches/i01.md](sketches/i01.md) | h1: supermarkets under banners said to run no loyalty programme, 376 (Doc 7 + Doc 3) | 392 adds Chemist Warehouse, a pharmacy chain (fails "supermarkets"); 372 omits Raeward Fresh (status in Doc 3 only, count in Doc 7 only); 301 or 305 omits the franchise figure. Doc 7 holds every count, Doc 3 the status of Raeward Fresh and FreshChoice | written up as q01. Rev 0 on the form 2026-10-12: "Question in your own words" Failed, "One defensible answer" Passed. Rev 1 = the user's rewording ("Using Woolworths’ store counts ..."; the possessive could mean Woolworths' own stores, 71). Rev 2 = the user's "With the number of stores Woolworths provides, ..." with rev 0's second half. Difficulty Run 1 on rev 2: "In band — Medium tier", Low 0/5, Medium 1/5; submitted at Medium 2026-10-12 (frozen; notes/feedback-q01.md) |
| i02 | [sketches/i02.md](sketches/i02.md) | h2: share of NERA's dropped products in Woolworths' five "notable omissions" categories, 83.3% (Doc 8 + Doc 7) | 84.6% counts cough medicine, which is not among the 69; 100.0% assumes tobacco; 75.0% leaves the toaster out of general merchandise (the one judgment in the design) | sketch only; untested (q01 was submitted first) |
| i04 | [sketches/i04.md](sketches/i04.md) | h2, second form: products NERA's test would cover with The Warehouse Group's additions kept, 63 (Doc 8 + Doc 5) | No reading found that changes 63 (cough medicine cancels; no general merchandise category involved). Sibling of i02: at most one of the two is submitted | sketch only; untested |
| i03 | [sketches/i03.md](sketches/i03.md) | h3: Countdown discount types on both Woolworths' and Consumer NZ's accounts: Specials, Club Prices, Multibuys (Doc 7 + Doc 1) | "Great Price" is on both lists but is a standard shelf price; Clearance Prices and personalised offers are Woolworths' only. Compares two accounts (rule 10 advisory risk); not numeric | sketch only; untested |

All four pass the mechanical sketch screen (quotes found, two documents each; no warnings). That screen proves
neither uniqueness nor difficulty.

Why these and in this order: q01 is the preferred shape (one derived count across two documents) and rests on two
dependencies that have measured results elsewhere: a member that only another party's document establishes, with
the counting rule stated in the question, and one grouped figure among separate ones. i02 and i04 need a category
mapped onto a product list plus one thing that is not there (tobacco in Woolworths' list; cough medicine among the
69). i03 is a membership question with one decoy and one member under another name.

Rejected without a sketch (reasons in notes/hooks.md): h4 and h14 (the answer would name or count submitters,
against the newer guide's rule 10); h5 (which questions each respondent answered: about the papers); h6 and h7
(figures the documents do not connect); h8 (a lone small number); h9 (shares q01's counts and turns on the two
Metros); h10 and h11 (one bridge into a labelled fact, and recallable); h12 ("~25km" is not said to be a radius);
h13 (list differences between the two co-operatives).

## After Run 1 (2026-10-12)

q01 rev 2 measured "In band — Medium tier" (Low 0/5, Medium 1/5) and the user submitted it. What the capture
shows, from each attempt's own text (notes/feedback-q01.md): no low attempt read Doc 3's sentence on FreshChoice and
SuperValue, one line below the Raeward Fresh sentence four of them used, and none found Raeward Fresh's count in Doc
7's list of small rivals; three attempts read the opening as Woolworths' own stores (71); the pharmacy decoy caught
nobody. i02, i04 and i03 were never tested. i02 and i04 are a different family (a product list against scope
categories) and are the next sketches if another question is wanted on this bundle; neither reuses q01's passages.

## Repairs held, one per observed failure (historical: q01 is frozen)

- q01 blocked as "too vague" with both form solvers on 372 or 301: the rule is already in the question ("any
  retailer's submission"); the next step is a different hook, not a named banner.
- q01 "too easy" at the quick test: do not add banners or stores of the same kind (a solved family stays solved);
  move to whichever of i02, i04, i03 survived.
- q01 below Medium at the difficulty check: read every attempt's own answer first (`tools/verdict_summary.py`).
