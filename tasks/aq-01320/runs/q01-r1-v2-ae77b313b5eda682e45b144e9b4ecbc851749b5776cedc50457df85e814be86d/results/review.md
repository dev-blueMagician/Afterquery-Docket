# q01 rev 1 independent review (fresh question-review agent), 2026-10-06

I found no blocking issue in q01, so the verdict is ready, but only locally. The Medium target has not been measured, so status stays checked. I wrote no files.

    q01 (rev 1; tested_sha256: ae77b313b5eda682e45b144e9b4ecbc851749b5776cedc50457df85e814be86d)

gold_verified: yes. Recomputed with exact fractions from the original passages.
- Range: D04 l.139 (docs l.146) $10.62 to $10.82, midpoint 10.72.
- Actual: D06 l.49 $10.44 (l.173 and l.271 agree). 10.44 − 10.72 = −0.28, exact. 1,213.7 / 116.3 = 10.436 also gives 10.44.
- Dates: Q2 ended 2025-11-23; 13 weeks later 2026-02-22 (D05 l.11). Q4 2026-02-23 to 2026-05-31: 98 days, 14 weeks, consistent with D06's 53-week year. D04 issued 67 days before Q4 began, D05 24 days after.
- Wrong routes: D05 outlook −0.01; adjusted −0.16 or −0.18 (reported actual vs adjusted midpoint), +0.04 or +0.02 (adjusted vs adjusted); net EPS incl. discontinued −0.34; basic EPS from continuing operations −0.21; basic net EPS or the sum of the four quarters −0.27; reversed subtraction +0.28. Every input is a single exact figure, so rounding cannot split the answer.

outcome: A: match; B: match. Both −0.28, high confidence, separate packets. All four packets hold the same question bytes and only the corpus, no notes or key. Both rejected −0.01 on the explicit dates and the adjusted routes on "reported". The flagged gap (no proof of an update between Dec 18 and Feb 23) does not produce a second answer.

closed-book: misses. "+$0.02 (a guess)", not equivalent. It worked out from memory that the December outlook was in force when Q4 began, as did the two earlier probes; it recalled neither the reported range nor the actual.

necessity:
- D04 (Doc 10) needed: only source of 10.62 and 10.82 (one hit each). D05 says only "updated"; D06 gives only a FY2027 outlook. Without D04: −0.01 or not determinable. No subset of D05's adjustment items produces the −0.12 net adjustment needed to rebuild 10.72.
- D06 (Doc 12) needed: only FY2026 actual. Stand-ins from D05's outlook give −0.27 (midpoint, also 6.91 + 3.54), −0.32 or −0.22; all miss at the stated precision.
- D05 (Doc 11) correctly unlisted: only document printing "February 22, 2026", but D04's Q2 end places Dec 18 inside Q3 and D06's 53-week year gives a 14-week Q4. Without D05 the answer stays −0.28.
- No smaller set; Darden appears nowhere outside D04-D06.

shortcut: clear. Auditor route verified: D05 l.11 (or D04 l.11 plus 13 weeks, or D06 l.13), D04 l.139, D06 l.49, subtraction. No passage prints 10.72, 21.44, "midpoint" or −0.28 for Darden ("0.28" only in D01 and D08). D06 never compares the actual with an outlook. The overview (capture L99-118) shows only adjusted figures. The edition step can be worked out from general knowledge: a difficulty risk, not a shortcut.

source_assessment: no gaps (source_gaps [], sha 4f53cda1...). Intake: all 12 captured in full, captured hash = source hash, 0 gap characters. Cited spans match docs/. Nearby artifact: footnote digit on the adjusted bullets ("$10.703", "$10.674", D04/D05 l.90); no effect on premises, gold, exclusions, uniqueness, necessity or shortcuts because the question asks for "reported".

difficulty: medium (marginal), local suitability only.
- For: aq-00964 q01 mechanism (measured Medium); D05's headline does not tie the update to the Q4 start; second layer: the reported range sits only in a reconciliation table while headline bullets and the overview show adjusted figures.
- Against: all three closed-book runs worked out the edition without documents; D05's first sentence prints both deciding dates; the anchor is a calendar boundary, not an event to find; then a midpoint and one subtraction.
- Estimate: Too easy about 15%, Easy about 50%, Medium about 25%, higher about 10%. Medium needs Low 0/5. Local reviews have underrated this mechanism before (aq-00964 q01, aq-00745 q09); quick-test first.

verdict: ready (locally checked; platform Medium result pending).

findings:
1. Signed wording fixes direction; "to the nearest cent" states rounding and implies dollars; one ask; unit carried. Both reported midpoints exceed the actual, so the sign does not reveal the edition; adjusted routes remain live wrong answers. One defensible answer; a bare "$0.28" is a sign error. No change needed.
2. Form number rule: Steps 1, 3 and 4 pass; derived operands (21.44, 10.72, 20.90, 10.45) sit in steps naming their source (accepted once, aq-00949 q05). Unconfirmed risks: (a) if the form merges the unnumbered decoy paragraphs into Step 5, that step carries four "=" results (aq-00949 q03 rejected a second "=" result in one step; 20.90 is printed nowhere; 10.45 and 0.01 pass only by coincidence, D06 l.269, D05 l.129); (b) whether "= -0.28" counts as straight after "=" (0.28 printed in neither Doc 10 nor Doc 12). Check the reasoning box after pasting; if flagged, give each decoy line its own numbered step (new revision, fresh checks).
3. Verbatim evidence D04 l.139: de-piped quote passes the floor; platform text unconfirmed; no prose alternative; D04 stays cited by its dateline. Save passage before submitting; any evidence change is a new revision.
4. Mark only Doc 10 and Doc 12; decline "Derive the rest" adding Doc 11. Residual unknown: whether the platform's high model recalls the December reported range or the June 2026 actual (local closed-book recalled neither).
5. Premise: no document rules out an outlook change between Dec 18, 2025 and Feb 23, 2026; within the bundle the gold is the only supported answer; recorded; not blocking.
6. Set: sketch i04 (Darden tax rate) reuses q01's anchor and edition path; submit at most one (already in ideas.md).
7. Records: rev 1 A, B, closed-book and audit carry ae77b313; report recomputes the same fingerprint; floor 0 FAIL, 2 WARN answered.
8. Platform-only: restricted names, originality, token window, Save-passage text, form reasoning parsing. origin: claude accurate; export accepts only user; "I wrote this question myself" cannot truthfully be ticked; user's decision. Nothing here is a platform pass.
