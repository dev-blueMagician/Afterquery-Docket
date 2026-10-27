# Independent review, q03 rev 0 (2026-10-08)

Role: question-review (fresh context; frozen fields, corpus, raw returns and floor output).
tested_sha256: 5096099312ef09a6e6330c159a9eac06f76bebba5e88106ba107169b9ff5deaf

Raw return (verbatim):

q03 (rev 0; tested_sha256: 5096099312ef09a6e6330c159a9eac06f76bebba5e88106ba107169b9ff5deaf)

gold_verified: yes. I recomputed it from the original passages with inline Decimal and float runs (no files written).
- June 2022 share: 270/581 = 46.4716%. D05 l.312 says the method "located 581 class members". D05 l.316 gives 270 with no bankruptcy plus 311 with only a stale one, which is 581.
- List share: 20,891/57,233 = 36.5017%. D07 l.47 gives the list of 57,233 after the April Thomson Reuters re-run, and l.49 the 20,891. Three passages date it: the motion on July 31, 2025 (l.67), fn 5 l.127 ("final report on April 22, 2025"), and D06 l.33, which lists that report as Exhibit B to the motion.
- Difference: −9.9699, so −10.0. On the sum-of-groups base (20,891 + 36,317 = 57,208) it is −9.9540, also −10.0.
- All 7 evidence quotes appear word for word in text/ and in the docs/ originals. The original also reads "97330", so solver B's aside that it reads "973" is wrong, but it does not matter.

Rounding routes (result at one decimal):
- Full precision, any rounding mode, either base: −10.0.
- Shares rounded to 1 or 3 decimals: −10.0.
- Shares rounded to 2 decimals: on 57,233 the gap is −9.97, so −10.0 in every mode. On 57,208 it is −9.95 exactly. Half-up and half-even give −10.0; half-down and float give −9.9 (36.52−46.47 = −9.9499999…). Shares as 4-decimal fractions hit the same tie.
- Whole-percent shares: −9.0 on both bases. This is premature rounding.
- A route the record does not list: taking the June share from the printed percentages, 27.7/(27.7+32.0) = 46.40%, gives −9.90 on 57,233 and −9.88 on 57,208. That is −9.9 in every mode, with no tie involved.

Precision decision: this is an acceptable stated risk, not a One-clear-answer defect.
- Both −9.9 routes swap stated exact inputs for rounded or computed ones. The exact counts 270, 311 and 581 sit in the same paragraph, and the 57,233 list is stated outright. The platform's own send-back list includes "gold computed from rounded inputs", and no local run produced either route.
- Two decimals would be worse: the two bases split, −9.97 against −9.95.
- Whole points is the only precision that brings every route except whole-percent rounding to −10. The traps would stay distinct (+9, −8, −8, +12, −9). Keep it as the fallback if a platform check or reviewer raises the ±0.1 split; switching costs a full re-test.

outcome: A: match; B: match. Both answered −10.0 with high confidence from distinct fresh packets, and each question.txt matches the snapshot exactly. Both named and rejected +8.8, −8.3 and +12.0, and both checked the 57,208 base. The only injected context was git-status file names, so neither run is contaminated. Their D05/D02/D04 reading was partial but backed by searches, and nothing relevant was missed.

closed-book: misses. It answered "unknown" and declined to guess. Residual risk: −10.0 is a focal round number, and the platform's low model must give an answer (about 3–5% risk). An optional forced-guess closed-book run would measure it.

necessity:
- Doc 4 (D05) alone holds 581, 270 and 311. Elsewhere, D04 has only 22,141 Trans Union files and the 30/50-file samples, and D02 only "6/30/2022" column headings.
- Doc 6 (D07) alone holds 57,233 and 20,891. D03's "Approximately $2,100,000.00" at $100 each implies about 21,000 members but gives no total, D06 has only the report title, and D05 says only "tens of thousands".
- No smaller set works. The pair D03 + D07 using the reserve gives −9.8.
- Removal probes: I hash-checked both packets as byte copies minus the removed document; the no-Doc 4 packet is renumbered, the no-Doc 6 packet needed none. Without Doc 4: unforced "not answerable", forced +26.5 (p 0.05). Without Doc 6: unforced "not answerable", forced +2.6 (p 0.02). Both miss.

shortcut: clear. The verified shortest route is D05 l.312/l.316 (or l.148) giving 46.47%, then D07 l.47/l.49 with l.67 giving 36.50%, then the subtraction. No passage states either share or the difference. The only printed "no bankruptcy" share is 27.7%, which is on the wrong base. The capture's overview for Doc 6 lists 57,233 next to the March 22,212: that is a decoy pairing, not the answer. Near-copy check against every workspace question: highest token ratio 0.24, longest shared run 3 tokens, no reused closing sentence.

source_assessment: no gaps. The capture is complete: intake shows all 7 documents with matches_capture true and gap_characters 0, and source_gaps is [] with a matching hash.

difficulty: easy (marginal toward medium).
- Design: two answer-changing traps, one on each side of the subtraction. The basis trap (27.7%) gives +8.8; the March count gives −7.7 or −8.3. Each is a printed figure with the asked label that a reader meets first.
- Both are tied: the fact that rules each out sits in the same paragraph, and the question's "class list" and "class members located" lead straight to the right sentences.
- Calibrated estimate: Too easy ~18%, Easy ~45%, Medium ~15%, Between levels ~12%, High ~5%, Too hard/Answer not supported ~5%. Usable for this set (Medium or High) is about 20%. That is slightly stronger than q01, which has one trap.
- Calibration basis: tied traps measured Easy (aq-00745 q01, aq-01320 q01, aq-01433 q01). A printed same-label scope decoy reached Medium only under a vague tie phrase (aq-01278 q02).
- Other platform risks: form "too vague" block ~5% (both decoys are excluded by the question's description), removal flag ~3%, "Answer matches a stated figure" advisory low (27.7% is on files, and the gold uses the stated 57,233).

verdict: ready. This is local readiness only. There is no platform result yet, so keep the status at checked until an exact-content pass at Medium or Hard.

failure_modes:
- FM1, Unit or basis / Takes the wrong line item: real. 36.5017−27.7 = +8.80, and the unrounded 270/973 gives +8.75, still +8.8.
  - Not ruled out by the wording: only Doc 4 shows that the 973 base holds 392 files outside the 581, and l.148 itself calls the 1,100 files "potential class members".
  - The claims are true: it is the only printed "no bankruptcy" percentage, "97330" is 973 plus the footnote 30 marker, and l.312 and l.316 are one paragraph split by a page break.
  - Label fits (Part vs total would be the alternative). 229 words.
  - Mild risk that a reviewer calls it ruled out by "class members located".
- FM2, Superseded date or version / Uses the wrong period or date: real. 22,212/57,233 gives −7.66, so −7.7; the March pair 22,212/58,153 gives −8.28, so −8.3. Not ruled out, because the reader has to date the lists.
  - Claims are true. One nit: "the same paragraph … in his April 22, 2025 report" relies on the report name defined at l.41, and the 20,891 sits in the next paragraph (l.49). The sentence reads as a separate assertion, so it is not an overclaim.
  - The local solvers' reading was −8.3, but the box leads with −7.7. 212 words.
- Necessary-documents roles are not written, so both default to Answer component, which matches how each document is used. Both FM2 traps share a type with q01/q02's modes. Whether "Each trap once per task" means per question or per bundle is unknown.

findings:
1. Q4 record, outside the fingerprint: Lever checks should add the printed-percentage route (−9.9 in every mode) and the precision decision above; it currently covers only the 57,208 tie. No re-test is needed.
2. Q9 pinning holds.
   - "No bankruptcy record found at all" maps to 20,891 (none in PACER or Thomson Reuters) and 270 (none in PACER). The expert samples of 50 and 400 cannot give full-group counts, and removing the two TEST records still gives −9.97.
   - "In place when" is a firm anchor for the April list.
   - "Located … at certification" means 581; the 1,100 are only "potential" members.
   - "Minus" fixes the sign; reversed would be +10.0.
3. Q10 and rule 10: 52 words, below the 60-word warning but above the 20–45 aim. No wording about the document set, and the answer is a number. Q1–Q3, Q5–Q8, Q12 and Q14 pass: one component, both documents quoted, tags apt (Conditional filter is the weakest).
4. Optional, inside the fingerprint (re-test if changed): Step 5 jumps from "36.50 − 46.47" to "−10.0" without showing −9.97. Small risk on the "Reasoning reaches the answer" check.
5. Record nit: the necessity note says D04's 22,141 files had "no PACER results". They are Trans Union files lacking a public-record entry.
6. Set: q03 shares D07 l.47/l.49 and the March trap with q01/q02, but it asks a different fact, gives none of their answers away, and adds Doc 4 plus a new trap type. Submit it with at most one of q01/q02.
7. Fingerprint: the current file computes to 5096…, and all six records (A, B, closed-book, two probes, audit) are rev 0 on it. Writing the Necessary-documents roles would change the fingerprint.
8. Platform-only, unknown: restricted names, cross-task originality and the admin own-words checks. Authorship is a separate matter: origin is claude, and the export tool accepts user only.

Files are in D:\Agents\Docket\tasks\aq-01541\:
- questions\q03.md
- runs\q03-r0-v2-5096099312ef09a6e6330c159a9eac06f76bebba5e88106ba107169b9ff5deaf\results\
- text\D05.txt, text\D07.txt
