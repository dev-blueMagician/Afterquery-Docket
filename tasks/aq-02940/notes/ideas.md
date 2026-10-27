# aq-02940 - lean candidate sketches

Current target: medium (Hard welcome); measured platform success pending. User, 2026-10-11: "there is no slot
for Easy Tier for this bundle, we should target medium and high. do you best."
Hooks are in [hooks.md](hooks.md). Document numbers are the task page's. Quick tests reported: q03, q01, q02
"too easy" and i09 "survived" (user, 2026-10-11, no panels; i09b and i08 not reported). Sketch rounds used: 2 of 3.
One independent question-author run (2026-10-11) returned three sketches from the sources; its first became i06,
its second i07 (re-asked as i08), its third (h12) was not taken.

## Round 2 (active): sketches only, no write-up before a quick test survives

Round 1 measured that the easier solver does a two- to four-step numeric join whenever the question names its
ingredients (a rate and its base; a share beside a look-alike pair). Round 2 therefore leaves the rules unnamed
or makes two unstated scope facts decide the answer.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i09 | [sketches/i09.md](sketches/i09.md). "Had the Commerce Commission's final decision come the day submissions closed, what is the earliest date the caps could start while satisfying both ASB's and Westpac's timing requests?" Gold 1 April 2027 | h13 | Competing: 1 March 2027 (Westpac's printed date) fails ASB's eight months (13 March 2027); 13 March 2027 fails Westpac's first-of-month request; the survey's closing day (29 June 2026) is not when submissions closed. Necessity: Doc 1 alone states the 13 July 2026 deadline; Doc 4 alone the eight months; Doc 14 alone the 1 March floor and the first-of-month request | quick test 2026-10-11: survived (user: "i09 survived"). Promoted: [q04](../questions/q04.md) asks the same case as a day count from the stated deadline (262 days; the date answer does not need Doc 1), [q05](../questions/q05.md) keeps the tested wording. Difficulty Run 1 on q04 rev 0 (2026-10-11): "Between levels", Low 0/5, Medium 5/5. q04 rev 1 (384 days) replaces ASB's lead time with Mastercard's pair for the caps exempt from the limiting mechanism; q05 dropped. rev 1 was quick-tested by the user: "too easy"; rev 2 restores rev 0's "first start while satisfying both". Quick test, then Run 2 |
| i11 | Sibling of q04 rev 2 (same gold, steps and documents; only the way the caps are named differs). "Had the Commerce Commission's final decision come on its deadline for submissions, how many days later could the highest of its proposed caps first start while satisfying both Mastercard's minimum lead times and Westpac's timing requests?" Gold 384 days | h13 | The highest proposed cap is 1.50%, foreign-issued online (D13 L103), so Mastercard's twelve months for cross-border changes applies; then Westpac's first of the month. Easier identification than q04's (a table value instead of the limiting mechanism's scope) | quick test 2026-10-11: survived, while q04 rev 2 (limiting-mechanism wording) was too easy. Adopted as q04 rev 3. Two-ask sibling i12 = [q06](../questions/q06.md): lowest and highest caps, 292 and 384 days. Difficulty Run 2 on q06 (2026-10-11): "In band - Easy tier", Low 3/5, below target. Hook h13 exhausted for Medium: Between levels with ASB, Easy with Mastercard |
| i09b | Sibling in sketches/i09.md (two asks). "Had the Commerce Commission's final decision come the day submissions closed, what are the earliest dates its domestic and its foreign-issued caps could start under Mastercard's minimum lead times and Westpac's effective-date conditions?" Gold 1 May 2027 (domestic) and 1 August 2027 (foreign-issued) | h13 | Mastercard's nine months for domestic and twelve for cross-border changes (Doc 10), then Westpac's first of the month (Doc 14). Names "minimum lead times" because Mastercard's release-cycle request has no dates in the bundle | active sibling of i09: use one of the two at most |
| i08 | [sketches/i08.md](sketches/i08.md). "If the Commerce Commission adopted the interim differential Mastercard asks for pending American Express's designation, by how many percentage points would the implied average interchange on foreign-issued commercial credit exceed the domestic one?" Gold 0.29 percentage points (1.37% against 1.08%) | h11 | Competing: 0.59 (nothing or both moved), 0.39 (whole 0.20% premium swapped), 0.19 (0.40% added on top); each fails a document fact (D13 L591-593, L812; D08 L17, L80). Necessity: Doc 10 alone prints the 40 basis points; Doc 1 alone the foreign-issued 1.37% | active; mechanical screen eligible (Doc 1 figures past character 46,000); quick test first |
| i10 | "By Mastercard's stated minimum for cross-border changes, how many days short was the notice the Commission's July 2025 final decision gave before its caps on foreign-issued commercial debit cards took effect?" Gold 77 days (17 July 2025 + 12 months = 17 July 2026; start 1 May 2026) | h14 | Competing: 137 or 228 (the domestic date, 1 December 2025), -14 (nine months), 20 (the 21 May 2025 early notification). Necessity: Doc 8 alone prints "1st May 2026" (D06 L746); Doc 10 the twelve months; 17 July 2025 is in Docs 1, 8 and 10 | spare: a date count with its rule named; shares Mastercard's twelve months with i09b |
| i04 | "In percentage terms, how much deeper is the cut the Commerce Commission's caps imply for average domestic commercial credit interchange than the cut Australia's consumer credit cap makes to its average, to the nearest point?" Gold 8 percentage points (43.9% against 36.2%) | h9 | As recorded in round 1; four lookups, three operations, ingredients named | spare: same family as the round-1 failures |

## Round 1 (closed)

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md); [q01](../questions/q01.md). Spanish-study response applied to the proposed caps, "fell by the percentage ... per 1% interchange cut". Gold $26.5 million | h1 | Docs 1 and 8 both necessary; wrong routes 19.5, 40 | quick test 2026-10-11: too easy; dropped |
| i02 | [q02](../questions/q02.md): the same with "finding on how merchant service fees respond to interchange cuts". Gold $26.5 million | h1 | as i01 | quick test 2026-10-11: too easy; dropped; hook h1 closed |
| i03 | Percent form of h1 (15.6%) | h1 | easier sibling | closed with h1 |
| i05 | Interchange share of all card acceptance costs after the caps (63.3%) | h6 | soft inputs | closed: same family as q03 |
| i06 | [q03](../questions/q03.md): commercial credit merchant service fees' share of everything businesses pay to accept Visa and Mastercard, less its share of total transaction value. Gold 9 percentage points | h10 | Docs 16 and 1 both necessary; decoy 11 | quick test 2026-10-11: too easy; dropped; hook h10 closed |
| i07 | Independent author's wording of h11 (0.3 points below the current 1.39%) | h11 | Doc 10 states the 10-to-40 swap itself | superseded by i08 |

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.

Closed without a sketch (see hooks.md): h2, h3, h4, h5, h7, h8, h12.
