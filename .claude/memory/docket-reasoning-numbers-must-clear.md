---
name: docket-reasoning-numbers-must-clear
description: User 2026-10-09 - genuine reasoning mistakes the form's number check catches ("Step N: Doc X doesn't mention Y") must never reach a hand-over; the floor FAILs them (tools/form_numbers.py); a figure the cited document states in words or deep, in an evidence quote, is an expected false alarm (WARN), not a mistake
metadata:
  type: feedback
  updated: 2026-10-09
---

The form's reasoning number check ("Step N: Doc X doesn't mention Y. Check the document number.",
"Step N: Which document says Y? Add 'Doc N'.") used to catch genuine mistakes in my hand-overs: a
wrong Doc number, a derived value cited to one document, unit words or a restated result after "=",
a reused percent-typed result. Those must never reach the user again. The user, 2026-10-09, showing
aq-02505 q01 rev 0's two flags: "I met this kind of situation so many times... Don't make such
mistakes anymore." Then, same day: "Ok, this time, it is not your fault. the reason I showed you this
screenshot is not that I didn't know that they were wrong warnings but I just recalled that you used
to make mistakes which are alarmed by the input verification. If you fixed such an issue in this
project, then it's ok for me."

**Why:** such flags reached the user on more than ten questions (aq-00949, aq-01321, aq-01543,
aq-01960, aq-02028, aq-02102, aq-02157, aq-02220, aq-02486). The emulator lived in task helper
folders (form_check_v5 to v10) and ran only when remembered. aq-02505 q01's two flags were different:
Doc 2 and Doc 6 state the totals only in words ("One hundred and seven entities"), which the form's
digit matching cannot see. The user knew those were wrong warnings.

**How to apply:**

- The floor (`check_questions.py`, hence `--handover` and `prepare`) runs `tools/form_numbers.py`.
  Every miss a rewording could fix is a FAIL with its cause (it names the Doc that does print a
  wrongly cited number). Never hand over with a form-numbers FAIL.
- A figure the cited document really states, only in words or past the form's read depth, inside a
  passage quoted as evidence from that document, is an expected false alarm: a WARN. Say in the
  hand-over that the form will show it and why; do not call it a mistake or redesign for it alone.
  Unquoted, the same case stays a FAIL: quote the passage if it is the source.
- At sketch time prefer operands printed in digits near the start of their documents
  (`docket_agent.py screen` warns), since every such false alarm is an orange line on the form.
- A `ready` question (measured with that reasoning) gets WARNs only, since an edit voids its pass.
- The emulation is evidence-built, not the platform's code: read the form after pasting, and log
  any new flag or false alarm in [[docket-form-automated-checks]] with the exact step text.

Related: [[docket-handover-all-form-fields]], [[docket-user-prefers-derived-numeric]].
