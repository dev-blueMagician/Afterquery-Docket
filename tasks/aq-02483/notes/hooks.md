# aq-02483 - cross-document hooks

Target: medium (user 2026-10-09: no Easy slot, "target medium and high"). Locations are text/DNN
lines (D0N = Doc N). Caller inventory h1-h12, written after a full read of all six documents;
independent author returns are appended when they arrive.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D05 L309-L329 (17 Legacy amendments approved as Alabama's version), L338-L341 (Contains both CCR and liquids, Infiltration, Liquids not approved); D06 L310-L320 (11 approved as Wisconsin's version) | Legacy all-unit amendments approved in both states = 9; WI-not-AL definitions = Infiltration, Liquids | Match then exclude; scatter | Subset assumption gives 11; AL's rejected trio gives "Contains both CCR and liquids" as a decoy for the which-items form | List comparison resembles list diffs measured too easy (aq-02208 q01); each list is explicit and numbered | sketch (i01) |
| h2 | D02 L268, D03 L226, D04 L291, D05 L276, D06 L294 STAG figures | Funding comparisons / totals | Tied decoys only (AL "anticipates ... total") | AL total 1,272,869 in the awarded figure's own sentence | Tied trap; lookups plus one step | reject as primary |
| h3 | Unit counts D02 L267, D03 L226, D04 L290, D05 L276 (no facility count), D06 L290; AL facilities only from the permit list D05 L397-L398 | Units per facility, totals | Hidden input (AL facility count) | AL omitted gives 62/22 | 8 permitted facilities = all AL facilities is inference, not a printed count | hold (fairness risk) |
| h4 | Publication/comment/hearing dates (DATES of D02-D06) | Actual comment days 62/63/60/62/60 vs printed "60-day" | Rule vs printed label | "60-day" decoy | Needs a stated counting convention, which removes the trap | reject |
| h5 | Application dates D02 L110, D03 L108/L144, D04 L111/L147-L148, D05 L162, D06 L152 | Application-to-proposal intervals | Edition-like date choice | VA original, LA original, WI supplement, WI letter date | "Most recent application" ambiguous for WI (Application Supplement) | reject |
| h6 | D05 L161 (ND final Nov 17, 2025), L402 (ND proposal May 16, 2025); D03 L333 (Sep 25, 2025 question to VA) | Days from ND proposal to EPA's question to Virginia = 132 | Untied date choice (two ND dates in different sections) | ND final date gives negative | "First"-type claims about EPA history are world claims beyond the bundle; plain two-date gap | hold, weak |
| h7 | D02 L302 / D04 L400 (no state CCR permits issued) x SI counts | SIs in states with no state CCR permits = 22 | Conditional filter | WI/VA/AL included | Keyword filter, two lookups | reject (too easy) |
| h8 | Penalties D02 L252, D04 L269-L270, D05 L265, D06 L266-L268 | Per-day penalty comparisons | Rule application | WI one-time reading | Legal interpretation ("environmental violations", response costs) | reject |
| h9 | WI rule effective Aug 1, 2022 -> plan modification due Feb 1, 2023 (D06 L456); AL 180 days after June 8, 2018 (D05 L396) | 184 vs 180 days | Derived interval vs printed | "six months = 180" gives 0 | Contrived comparison; tiny gold | reject |
| h10 | Rule cutoffs: WY Dec 14, 2020 (D02 L278), VA (D03 L242), LA mismatch (D04 L308 vs L315), AL Aug 28, 2020 + two Nov 2020 paragraphs (D05 L307), WI Aug 28, 2020 (D06 L308) | Amendments postdating a state's cutoff | Edition (D02 lists six amendments, D03-D06 seven) | D02's own list gives one fewer | Single-document answers (each later doc has both list and cutoff); LA internal mismatch | reject |
| h11 | Tribal counts D02 L118, D03 L114, D04 L117, D05 L117, D06 fn 3 (14 letters) | Tribes contacted | Letters vs tribes | 14 letters | Tribe counts per state are recallable public facts | reject |
| h12 | D03 fn 4 L147 vs D04 fn 4 L151 (components substituted in revised applications) | Component Virginia replaced that Louisiana kept: the Attorney General certification | What changed between versions | none strong | Short two-list diff | hold, weak |

The map is navigation; quotes come from text/DNN.txt. A short valid calculation or ID join is
eligible. Prior failures suggest tests/priority, not a universal veto.

## Independent author returns (2026-10-09, both origin claude, read-only, all six texts read)

- Author B (regulatory scope): b1 = definitions the 2024 Legacy Rule added that stay federal,
  Wyoming + Alabama summed = 20 (Alabama's three all-unit additions sit unlabelled in its "Second"
  list, D05 L337-L341; Wyoming's single grouped item D02 L282 is split only in D03/D04) -> reframed as
  i03 (Wyoming minus Virginia = 3); b2 = days between the newest amendments in Wyoming's and
  Wisconsin's adopted versions, 76 (decoy 108 from the Dec 14, 2020 cutoff) -> i02 / q01; b3 =
  Wyoming impoundment deadline vs Wisconsin landfill deadline, 199 days -> i04. Rejected list diffs,
  "in how many states" counts, exemptions, permit-shield counts, ND dates.
- Author A (numeric): a11 = landfills in states whose "Infiltration" version EPA approves, 16 -> i05;
  a12 = days from Wyoming's cutoff to the newest amendment as of August 2026, 1,884 (edition trap,
  but the Feb 10, 2026 amendment is printed in D03-D06, so no second indispensable document) ->
  rejected; a13 = same hook as b3 -> i04. Rejected Doc 1 links, STAG per-year averages, penalties,
  tribe counts, internal mismatches.
