# aq-02447 - cross-document hooks

Target: medium (user 2026-10-09: "there is no slot for Easy Tier for this bundle, we should target
medium and high. do your best."; page slots Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions, 0 of 10
quick tests, 10 of 10 runs). Caller inventory h1-h12 (Claude Opus 5.5, 2026-10-09), written before
reading the two independent authors' returns. The page says it is short of "Rounding and sign" and
"Picking the right measure" questions; its only suggested shape is "Pub. L. 108-11" (D01/D02 authority
citations), which no document explains (general knowledge only), so it is not used.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | 0694-0088 per-submission burden: D01 L94 29.4 ("Multi-Purpose Application"), D02 L295 29.6 (same title), D03 L116 29.4 (SNAP), D06 L104 29.7 (SNAP) | change in BIS's per-application estimate between two named rules (0.3 or 0.1 minutes) | same series, right edition; entity resolution (two titles, one control number) | other editions' values; title mismatch | two lookups plus one subtraction; tiny answer | weak; keep as fallback |
| h2 | h1 plus an event dated in D06 (Sep 2024 Major Defense Partner; May 2025 technology deal) selecting "the estimate in force then" | untied edition trap (D06 prints its own later 29.7) | same series, right edition | D06 29.7, D03 29.4 just after Sep 2024 | bundle holds 5 of hundreds of BIS rules: "most recent estimate at date X" is not settled by the bundle in the real world; MDP date is public | dropped (incomplete series) |
| h3 | license-application changes: D02 +20 (5 + 15, L108/L125/L295), D03 "ten" (L116), D06 about -50, -25 h, -$950 (L103) | net yearly burden-hour change of two rules (e.g., D03 +4.9 h, D06 -25 h -> -20 at whole hours) | calculate across documents; rounding and sign | printed 25 vs computed 24.75 (agree only at whole hours); D03's 33,133 total as look-alike | short lookup path; only whole-hour precision is unambiguous | weak (likely too easy) |
| h4 | D06 implied $950 / 25 h = $38 per hour or $19 per application, applied to D02/D03 counts | cost of another rule's applications | calculate across documents | $19/app vs $38/h routes differ | several defensible routes; contrived | dropped (ambiguous) |
| h5 | D01 L233/L272/L290: case-by-case review for China/Macau end users headquartered in A:5/A:6; D06 L49: UAE added to A:5 | review policy for a UAE-headquartered fab operator in Macau after Jul 10, 2026 | rule applied to an instance across documents | presumption of denial (UAE's pre-2026 status) | two-option answer a guess hits; 2023 text's currency in 2026 not stated | dropped as asked; no numeric form found |
| h6 | D04 L28 "32 entities" vs distinct organizations (HK Fudan under China/Singapore/Taiwan; Smart Mail under Iran/UAE) = 29 | distinct organizations added | part vs total; look-alike measure | printed 32 | single document; no natural second-document input found (UAE via D06 = printed "(2)") | single-doc only |
| h7 | D04 HIT/NWPU rows cite "87 FR 62202, 10/13/22"; D01/D03 date the Oct 7 rule to Oct 13, 2022 (87 FR 62186) | which corrected entries the Oct 2022 rule had amended | who belongs where | entries citing 88 FR 13675 (Mar 2023) | FR-citation question (rule 10 risk); page 62202 inside the rule is inferred; Oct 2022 entities recallable; D01 replaceable by memory | dropped |
| h8 | D03 L188-191 data-center VEU report deadlines (Jul 15 for Jan-Jun; Jan 15 for Jun 30-Dec 31); D06 effective Jul 10, 2026 | first report due after the UAE rule took effect and its period | temporal alignment | Jan 15, 2027 report | unnatural link (UAE approvals are not VEUs); one-step application | weak |
| h9 | D04 corrected entries' "first added" dates (L117-139) vs D02 effective date | entries first added after the SDN rule | temporal filter | none real | printed per-item dates = keyword filter; D02 date public | dropped |
| h10 | D01 seven Macau ECCNs (L67) vs D06 seventeen ECCNs (L276) / 742.6(a)(6)(iii)(B) (L264) | ECCNs in both / missing one (3B090) | match then exclude | 3E001 in (iii)(B) but not in D06's chart list | list diff of two printed lists; sub-paragraph scope (3A090.b vs 3A090) ambiguous | dropped |
| h11 | D03 Supp. 7 Samsung/SK hynix "Excluded from 744.6(c)(2)(i-iii) ..." vs D01's nine 744.6(c)(2) activities and 744.23(a)(2)(iii) criteria | activities still licensed for the excluded fabs; NAND/DRAM thresholds | rule applied to instance | (iv)-(vi) "do not know" cases | legal judgement, thresholds recallable (128 layers, 18 nm) | dropped |
| h12 | D05 export notification $106 per country, SNUN costs; BIS destination counts | cross-agency cost | none | n/a | guide: "a figure that exists only by multiplying numbers the documents never connect" | dropped |

Shared-ground summary: the only numerically connected series across documents is OMB collection
0694-0088 (h1-h4); other links are regulatory (Country Groups, Macau, UAE, Entity List, 744.6/744.23).

## Independent authors (claude, 2026-10-09), summarised

Author A (numeric focus) and author B (rule/instance focus) each read all six texts without the caller's
notes. Both found the same structure: no shared organization, address or alias across documents except
"UAE"; the only numerically connected series is OMB 0694-0088; D05 has no fair link.
- B-H1 (new, promoted as i01): § 742.6(a)(6) across two revisions, D01 L224/L229-230 (2023, 9 ECCNs) vs
  D06 L256/L263-264 (2026 (iii)(B), 18 ECCNs); look-alikes D01 L67 (seven ECCNs) and D06 L276 (17 charts,
  no 3E001).
- B-H3/H7/H8/H9/H11/H13, A-H5/H6/H7/H8/H10/H12: country-group applications, VEU exemptions, APP thresholds,
  reasons for control, Oct 2022 citations, 744.21 military end users, first-added date buckets, the two
  "Supplement no. 8" lists: rejected (two-option answers, recallable facts, single-document answers, or
  unchanged-text assumptions).
- A-H1/H2 (= caller h1-h4): A-i01 -893 minutes, held. A-H4/B-H5: UAE parties (Doc 4 vs Doc 6), A-i02 301 days
  and B-i02 27 organizations, dropped.
