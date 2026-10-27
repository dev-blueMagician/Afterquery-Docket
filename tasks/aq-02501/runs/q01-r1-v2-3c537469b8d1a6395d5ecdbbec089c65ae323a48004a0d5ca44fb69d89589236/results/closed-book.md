# Closed-book solve, q01 rev 1 (tested_sha256 3c537469b8d1a6395d5ecdbbec089c65ae323a48004a0d5ca44fb69d89589236)

Date: 2026-10-09. Role: closed-book-solver (claude-opus-5-5, fresh context, omitClaudeMd, hook denies tools).
Input: question text only (closed-book/question.txt), passed verbatim as the prompt.
Reason for running: concrete unresolved issue, rev 0's blocking platform check "Needs the documents" failed
(notes/platform-feedback/q01-rev0-checks-2026-10-09.png); rev 1 is the focused repair.

Raw return (verbatim):

answer: Other-than-honorable (OTH) discharges and bad-conduct discharges from special courts-martial. These are the separations VA reviews through character-of-discharge determinations. General (under honorable conditions) discharges were already eligible. Dishonorable discharges and bad-conduct discharges from general courts-martial are still barred by statute.
confidence: medium
basis: Memory of VA's April 2024 final rule, effective June 25, 2024, which amended 38 CFR 3.12. It added a compelling-circumstances exception to the willful-and-persistent-misconduct and moral-turpitude bars, defined those terms, and removed the homosexual-acts bar. VA's regulatory bars only apply to OTH and special-court-martial bad-conduct discharges. That the DARB's "less than honorable" covers general, OTH, bad-conduct and dishonorable discharges is my inference; I don't remember the DARB's exact wording.
contaminated: no. The only extra context was an auto-attached git status (workspace file names) and the user's email. No document text, hints, answer key or earlier results. No tools were used other than this handback.

Caller adjudication: misses. Gold = OTH discharges, bad-conduct discharges and dropped-from-the-rolls separations;
the return omits dropped-from-the-rolls separations (Doc 5's uncharacterized membership plus Doc 3 section IV),
matching declared failure mode 2. A miss is not a tier result and does not predict the platform's own check.
