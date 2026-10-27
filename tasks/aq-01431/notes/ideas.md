# aq-01431 - lean candidate sketches (fresh start, 2026-10-08)

Current target: medium (hard where a design supports it); the user says the bundle has no usable
Easy slot. Measured platform success pending. All sketches below: origin claude.

## Round 1 (2026-10-08)

Caller hooks h1-h10 (notes/hooks.md) plus two independent question-author runs: A (derived numerics)
and B (participants, named periods, qualitative levers, entity resolution). Closed-book screens are
fresh question-only closed-book-solver runs (each noted an auto-attached git-status/email context
unrelated to the question; treated as uncontaminated for sketch screening only).

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| c1 | h1 agenda vs adoption | Months the climate rule trailed its Fall 2022 agenda target -> 11 | D03 l22; D11 l118 | Calculate across documents | Public dates | DROPPED: closed-book reached 11 (medium) |
| c2 | h2 co-signer petitions | Courts of the co-signers' petitions -> D.C. Cir., 2d Cir. | D12 l120-136; D11 l67-69, l83, l126-129 | Entity resolution (NRDC split/abbreviated) | Inferable without D12; recallable | DROPPED: closed-book reached (medium) |
| c3 | h3 Si2 vs Morningstar | Si2 2020-22 category below Morningstar's 2022 E&S average -> Paris-compliant strategy (26.4%) | D02 l25-29; D07 l76 | Named period; filter | Two lookups | closed-book missed (low); Easy-leaning; hold |
| A-i01 | ICI asset series selected by ICI's own April 2024 list of its ESG letters | Growth of 1940 Act fund assets from the last listed letter before Nov 2023 to Apr 2024 -> 14.3% (30.1 -> 34.4) | D11 fn 7 l36, fn 1 l14; D06 fn 1 l12 | Same series, right edition; match then exclude (decoy D01 $31.2T unlisted -> 10.3%) | Selection through a document list is document-centric (rule 10); "listed" cues the check; the world-fact version ("letters in the ESG comment file") is unsettled because D01's posting files are unknown | author: Medium ~8%; caller: hold (rule-10 risk) |
| A-i02 | Treasury-clearing comment dates | Days between MFA (Dec 21) and ICI (Dec 23, 2022) letters -> 2 | D01 l129; D05 l740-744 | Calculate across documents | Small integer; lookup | author: Medium ~3%; drop |
| A-i03 | Sierra Club letter -> petition | Days from Oct 19, 2023 letter to Mar 13, 2024 petition -> 146 | D07 l3; D11 l129 | Calculate across documents | Petition date recallable (D11 removal risk) | author: Medium ~3%; drop |
| A-i04 | Si2 minimum minus Morningstar 2023 | 26.4 - 20 = 6.4 percentage points | D02 l29; D07 l76-78 | Calculate across documents | Arbitrary-looking comparison; lookup | author: Medium ~3%; drop |

| B-i01 | Justice Department comment: its file numbers vs ICI's narrative trio (h11) | "In April 2023 the Justice Department's Antitrust Division filed one comment letter covering three of the SEC's equity-market-structure proposals. On average, how many days had passed between those three proposals' publication in the Federal Register and that letter? Give one decimal place." -> 84.3 (81, 98, 74) | D01 fn 23 l147 (File Nos. S7-29-22; S7-31-22; S7-32-22, Apr. 11, 2023); D01 fn 2 l15 (S7-30-22 = Reg NMS; S7-31-22 = Order Competition Rule Letter); D01 fn 13 l100-101 (Best Execution = S7-32-22; FR dates Dec 29, Jan 3, Jan 27); D05 fn 15 l141 (letter in the s7-29-22 file, "market structure proposals"); D05 fn 16 l160-161 (four proposals; Disclosure of Order Execution Information 88 FR 3786, Jan. 20, 2023) | Linking across documents (file numbers); wrong members in a list. Decoys: narrative trio 91.7; all four 89.0; list-order mapping 94.0; inclusive count 85.3 | Doc 4 removal: Rule 605's FR date may be recalled; form "too vague" block if both form solvers take the narrative trio; "Answer not supported" if the high model never checks the file numbers | author B: Medium-or-higher 20-30%; caller recompute 253/3 = 84.33; PROMOTE after sketch probes |
| B-i02 | ICI outside-US share, month bridges via MFA's July 2023 letter and the stay | -1.52 pp (8.8/38.9 -> 9.2/43.6) | D06 l12; D11 l14; bridge D05 l6 or D01 fn 4 | Same series; unit normalization | Bridge from an unticked duplicated document; 56 words | author: Medium ~10%; drop |
| B-i03 | Sierra Club first climate comment -> D.C. Circuit petition | 636 days (June 16, 2022 -> Mar 13, 2024) | D02 fn 1 l15; D11 l129 | Calculate across documents | Petition recallable (D11 removal); two lookups | author: Too easy ~50%; drop |

Author C (2026-10-08), a systematic hunt for other "citation identifiers vs adjacent narrative" instances:
none qualifies. Full read of D01-D09, D11, D12 (D10 body and references, tables grepped), machine sweeps of
every S7 file number, release number, Federal Register cite, comment-URL id, docket number and footnote
cross-reference. Rejected, closest first: Market Data Infrastructure release vs FR date (121 days; public,
no decoy); Fund ESG release vs FR date anchored on a commenter (82 vs decoy 59; May 25, 2022 public and
carried by three ICI letters); Han linking (author answer or duplicated figure); D01 fn 4's single file
cite for MFA's 13-proposal letter (resolves inside D05); cybersecurity file numbers (no single answer;
public gaps); joint-letter signatories vs petitioners (famous answer); climate proposal release vs FR
(public); tailored shareholder reports (public); stay-order precedents (outside knowledge); one-document
structures; Stech chronology (FR date recalled); Hall and Grimes (organisation unstated); error-based asks;
official and title changes. New error finding: D01 fn 7's "April 28, 2022" memo date is probably 2023 by
its comment id, so caller hook h5 is dropped. Recommendation: no further rounds on this family.

Author B's conclusion (2026-10-08): the only cross-document trap found is the Justice Department letter's
file numbers set against ICI's narrative list; most "who took part" lists sit inside one letter or have
author or recallable answers.

Author A's conclusion (2026-10-08): outside the reserved US SIF grouped-vs-split family, no document
prints a value in force over a period with a later same-label replacement, and no other grouped figure
is split elsewhere; Medium is unlikely. Raw arithmetic scripts in the session scratchpad only.

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.
