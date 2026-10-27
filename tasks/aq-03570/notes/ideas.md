# aq-03570 - lean candidate sketches

Current target: medium (hard where a design supports it); the user says the bundle has no Easy slot
(2026-10-12). Measured platform success pending. All sketches: origin claude. Hooks: notes/hooks.md.

## Round 1 (2026-10-12)

Mechanical sketch screen (docket_agent.py screen) passed for i01-i04: quotes verbatim, two or more
documents each. It checks structure only. No quick test or platform result yet.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i02 | [sketches/i02.md](sketches/i02.md): mean days between consecutive Sierra Club letters on the fund ESG proposal, co-signed ones counted -> 203 days (77, 352, 180; 609 / 3) | h1 | Wrong routes each fail a stated condition or a document's own heading: 214.5 (co-signed letter missed), 352 (two letters in hand), 304.5 (dual-proposal letter left out), 266 (first comments left out). D02, D07 and D12 each supply one letter no other document shows | PROMOTED to q01 rev 0 (three documents, non-round gold, most steps); quick test first |
| i01 | [sketches/i01.md](sketches/i01.md): days between the Sierra Club's last two letters, co-signed ones counted -> 180 days | h1 | 352 and 429 both fail the wording; D07 and D12 each necessary, D02 only a decoy carrier | Softer sibling of q01: use if q01 is blocked or too hard. 180 is a round value a closed-book guess could hit |
| i03 | [sketches/i03.md](sketches/i03.md): days since MFA's previous comments when it wrote in October 2023, multi-proposal letters counted -> 101 days | h2 | 441 (own account) fails the wording; D05 and D08 both necessary | Weaker (the hidden letter is an MFA document in hand); quick test to learn what this gate does alone |
| i04 | [sketches/i04.md](sketches/i04.md): Sierra Club's last gap minus MFA's last gap -> 79 days | h3 | Four documents, one date each; every wrong route has its own value (251, -12, -261, -89) | Hard-leaning; quick test with the others, write up if q01 lands below Medium |
| f1 | aq-01431 old q01 rev 2 wording (git 30c3f7e): "In the US SIF Foundation's 2022 figures, by how many trillion dollars did assets in funds addressing climate change exceed assets in funds addressing the ESG issue that ranked second by fund assets? Give two decimal places." -> $1.65 trillion | h4 | Rev 0 measured Between levels (Low 0/5, Medium 4/5); rev 1 blocked by the form; rev 2 unmeasured | Fallback; fifth quick-test slot |
| f2 | aq-01431 q01 rev 1 (tasks/aq-01431/questions/q01.md): Justice Department letter, 84.3 days | h5 | No platform result; Doc 4's only input is a public Federal Register date | Fallback, second in line; not in the first batch |

## After difficulty Run 1 on q01 rev 0 (2026-10-12)

Result: "Between levels", Low 0/5 · Medium 5/5 (routes in hooks.md and q01 Lever checks). Decisions:

- i02 / q01: REVISED to rev 1. One change: the clause "Counting co-signed letters" is replaced by naming the set,
  "comment letters that the Sierra Club signed". Gold and documents unchanged. Platform pending.
- i01 (last two letters, 180): RETIRED in its tested-family form. Its only gate, the co-signature under the clause,
  was cleared by four of five low attempts.
- i03 (MFA, 101) and i04 (Sierra Club minus MFA, 79): RETIRED. Their extra gate is a multi-proposal letter that is
  itself a document; all ten open-book attempts counted the Sierra Club's two-proposal letter, and the easier solver
  works from the documents in hand, which is where MFA's joint letter sits.
- f1 (US SIF half-step) and f2 (Justice Department): unchanged fallbacks, untested on this task.

## After difficulty Run 2 on q01 rev 1 (2026-10-13)

Result: "Answer not supported", Low 0/5 · Medium 2/4, every-document attempts 266 three times. Decisions:

- q01 (i02): DROPPED at rev 1. The open term was whether a letter the documents report but do not include counts;
  with it settled either way the only step left is the co-signature, which Run 2 shows cleared by every medium and
  every-document attempt and by no low attempt. No third wording prepared.
- f2 -> q02 rev 0 (PROMOTED): "On average, how many days separated the Justice Department's April 2023 comment
  letter from the Federal Register publication of the three SEC equity-market-structure proposals under whose file
  numbers it was filed? Give one decimal place." -> 84.3 days (98, 81, 74). Necessary: Doc 6 and Doc 4. Readings
  still possible, with answers, are listed in q02 Lever checks (91.7, 86.0, 94.0, 89.0, 85.3). Platform pending.
- f1 (US SIF, $1.65 trillion): last fallback, not written up. Its ladder so far is exact label -> Between levels
  (Low 0/5, Medium 4/5) and no label -> form block; the untested middle wording is a change of label strength.

## After the quick test of q02 rev 0 (2026-10-13)

User report: "too easy for quick test" (no panel). Decision: q02 REVISED to rev 1, one change: "under whose file
numbers it was filed" -> "it covered". Gold 84.3 days and every other field unchanged. The named trio (91.7) is now
rejected only by the documents, not by the question's words. Next: quick test, then the form's full checks. If rev 1 is
too easy as well, h5 is closed (a more explicit wording was already too easy) and f1 is the only hook left.

## After the form Checks on q02 rev 1 (2026-10-13)

"One defensible answer" Failed: both form solvers 91.7 days (ICI's named three). Two advisories on the same reading.
Decision: q02 REVISED to rev 2, one change: the question opens "Judging by all these letters together," (the evidence
named, no identifier, no clause; the opening that cleared the same block on aq-03170 q01). Ladder on h5: file numbers
named -> quick-test too easy; nothing named -> blocked; evidence named -> pending. A second block closes h5, leaving f1.

## After the quick test of q02 rev 2 (2026-10-13)

User report: "too easy for quick test". q02 DROPPED, h5 closed (three wordings: too easy, blocked, too easy).
f1 -> q03 rev 0 (PROMOTED): "By fund assets in US SIF's 2022 report, how many trillion dollars separated funds
addressing climate change from those addressing the second-ranked ESG issue? Give two decimal places." -> $1.65
trillion. Necessary: Doc 7 and Doc 12. Fall-back wording if the form blocks it: "climate change/carbon". This is the
last hook on these bytes with any measured result short of too easy; if it fails, recommend release.

## After difficulty Run 3 on q03 rev 0 (2026-10-13)

Result: "Between levels", Low 0/5 · Medium 0/6 · High 5/6 (too hard for medium, too easy for high). Ladder on h4 now:
exact label "climate change/carbon" -> Low 0/5 · Medium 4/5 (aq-01431); "climate change" -> Medium 0/6 · High 5/6;
no label -> form block. q03 REVISED to rev 1, one change: the scope is named, "In US SIF's 2022 figures for ESG fund
assets by issue"; the label stays "climate change". The page's own suggestion (the exact label) is not adopted: it
is the wording that measured too easy for the medium solver. Platform pending.

## After the form Checks on q03 rev 1 (2026-10-13)

"One defensible answer" Failed: "Two materially different answers are defensible" (3.45 alone against the combined
4.8). q03 REVISED to rev 2, one change: "funds addressing climate change as a stand-alone issue". Ladder on h4:
exact label -> Low 0/5 · Medium 4/5 (aq-01431); short label -> Run 3 Medium 0/6 · High 5/6, then judged ambiguous by
the form; stand-alone wording -> pending. If rev 2 also lands outside Medium and Hard, every hook on these bytes has
a result.

## After difficulty Run 4 on q03 rev 2 (2026-10-13)

Result: "Answerable without the documents"; the closed-book attempt committed 1.65 from recalled figures of
about 3.41 and 1.76, and no solver with documents ran, so the stand-alone wording still has no difficulty
result. q03 REVISED to rev 3, one change: the gap is asked as a percentage of the second-ranked issue's figure,
to one decimal place (gold 91.7%). Ladder on h4: exact label -> Low 0/5 · Medium 4/5 (aq-01431); short label ->
Run 3 Medium 0/6 · High 5/6, then judged ambiguous by the form; stand-alone wording -> not measured (Run 4
closed-book); stand-alone wording with the percentage form -> pending.

## After the quick test of q03 rev 3 (2026-10-13)

User report: "too easy for quick test". q03 DROPPED at rev 3, h4 closed (exact label -> Low 0/5 · Medium 4/5;
short label -> Medium 0/6 · High 5/6, then judged open; one-reading wording -> too easy).

## Round 4 (2026-10-13)

Built on the one recipe with a Medium result on comment-letter bundles (aq-03170 q01: evidence named, a list
where a commenter's own account undercounts). Mechanical screen passed for i05-i07; sketches only until the
user reports a quick-test survivor.

| ID | Sketch | Hook | Reading still possible | Decision |
| --- | --- | --- | --- | --- |
| i05 | [sketches/i05.md](sketches/i05.md): organisations with at least three letters on the fund ESG proposal by the end of November 2023 -> Investment Company Institute, Managed Funds Association, Sierra Club | h9 | letters in hand only -> "Investment Company Institute" | quick test pending |
| i06 | [sketches/i06.md](sketches/i06.md): days between MFA's October 2023 letter and its previous letter on the proposal -> 101 days | h2 | MFA's own account -> 441 days | quick test pending; also measures i05's MFA step |
| i07 | [sketches/i07.md](sketches/i07.md): signers of the April 2022 joint letter that went on to comment on the proposal -> ICI, MFA, SIFMA AMG, U.S. Chamber of Commerce | h8 | the Chamber left out as a different body from its Center for Capital Markets -> three names | quick test pending |

Held back: i04 (Sierra Club's last gap minus MFA's, 79 days) needs i06's MFA step to hold first; its other
step (the co-signature) held no medium attempt in Runs 1 and 2.

## After the quick tests of Round 4 (2026-10-13)

User report: "i05 failed, i06 survived"; nothing on i07.

- i05: RETIRED (h9 closed). The easier solver produced all three names, so it counted a reported letter and a
  multi-proposal letter in hand for both MFA and the Sierra Club.
- i06: survived once. Its only unpointed step is the MFA joint letter, which i05 also needs, so the survival is
  one screen against one contrary screen. Second quick test requested; no write-up before it.
- i07: still untested; asked again.
- i08 ([sketches/i08.md](sketches/i08.md)): i04 reworded with no clause, set named by "signed": gap between the
  Sierra Club's last two signed letters minus MFA's -> 79 days (Docs 4, 7, 8, 12). Offered now that i06 has one
  survival. Reading still possible: co-signed letter missed -> 251. Its co-signature step held 0 of 5 low and
  7 of 7 medium and every-document attempts on q01, so only the MFA step can divide the middle solver.

## After the second round of Round 4 quick tests (2026-10-13)

User report: "all three survived" (i06 a second time, i07, i08).

- i08 -> q04 rev 0 (PROMOTED), 79 days, Docs 4, 7, 8, 12, tested_sha256 7bc2b8bb...8ad4; form Checks and one
  difficulty run pending. Chosen over i06 because it contains i06's gap and adds two documents.
- i06: held as the fall-back for q04 (same MFA step alone); not written up beside it (shared answer path).
- i07: next write-up, as a second question (different family). Open before its form goes out: the ticks for
  the two decoys whose letters other documents cite (IAA in D05, AIC in D01), and the Chamber reading.
- Reading of the screens so far: the easier solver missed the MFA joint letter in three screens of the
  "previous letter" frame and reached it inside i05's "at least three letters" frame; on q01 it found the
  Sierra Club's own two-proposal letter every time. Nothing yet measures the medium solver on this step.

## After difficulty Run 5 on q04 rev 0 (2026-10-13)

Result: "Too easy", Low — · Medium 5/6 · High —. q04 DROPPED, i06 RETIRED, h2 and h3 closed: every recorded
medium attempt cleared MFA's joint letter and the co-signature held one of six.
i07 -> q05 rev 0 (PROMOTED): the signers list with "if any" added, gold ICI, MFA, SIFMA AMG, U.S. Chamber of
Commerce; Docs 5, 8, 12; tested_sha256 1a6e81ed...9601. It is the last sketch with any result short of too easy.
Its steps are a fan-out (25 listed names through the other letters), which no capture on this page measures.

## After difficulty Run 6 on q05 rev 0 (2026-10-13)

Result: "Too easy", Low — · Medium 5/9 · High —, one wrong attempt short of the medium band (two solvers right
twice). Misses: authors only (1), the IAA decoy taken (4), SIFMA AMG's sentence in Doc 12 missed (8). Attempts 5
and 8 quote the opening as their reason to take cited commenters in. Repair as sketch i09, one change: the
search cue "Judging by all these letters together" comes out and the scope stays as "do these letters show"
(the aq-03169 q02 move from "say anywhere in its response" to "response say"). q05 stays at rev 0 until the
quick test and the form's "One defensible answer" have read the new sentence.
Quick test of i09 (2026-10-14): survived. As a rewording of a below-target wording it is a sibling, so a second
quick test comes before the write-up. Second quick test: survived. i09 -> q05 rev 1 (tested_sha256
facb3459...1d72); Step 3 labels SIFMA as the decoy.

## After difficulty Run 8 on q05 rev 1 (2026-10-14)

Result: "Too easy", High 3/3, after Run 7 (not captured) also too easy. q05 DROPPED, h8 closed. Every hook on
these bytes now has a result outside Medium and Hard: h1 (Between levels, then Answer not supported), h2-h3
(Too easy, Medium 5/6), h4 (Between levels, then judged open, then closed-book, then too easy), h5 (too easy,
blocked, too easy), h8 (Too easy at Medium, then at High), h9 (quick-test too easy). What divided the medium
solver on this page was only an open term or a letter the set merely reports, both fairness faults. h6 and h7
stay unsketched: h6 rests on look-alike file numbers and a lone small count, h7 on two lookups and a sum. No
fair untested sketch remains: release recommended.

Not sketched (reasons in hooks.md): h6 (who cites whom, lone small integer), h7 (the form's own idea
panel proposes it).

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Allow one focused repair per distinct observed failure; a repeated failure means change
the hook.
