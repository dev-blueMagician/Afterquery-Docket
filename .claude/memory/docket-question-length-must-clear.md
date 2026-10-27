---
name: docket-question-length-must-clear
description: "User, 2026-10-08: the form's question-length-spread warning blocks their progress in practice; never dismiss it as non-blocking; write new questions well below the band it names, about 12-20 words"
metadata:
  type: feedback
  updated: 2026-10-08
---

## Current rule

Treat the Question box's orange length warning ("Your questions so far all come out about the same
length — 6 of them between 28 and 47 words ... A good question can be much shorter ... a sharp
twelve-word question ...") as a requirement, not an advisory. Write new questions short from the
start, aiming at about 12-20 words and always well below the lowest number the warning names. Keep
exactness by cutting setup phrases (copied document wording, restated units such as "in dollars",
"temporary"), not the conditions that pin the answer.

**Why:** the user, 2026-10-08 (aq-02028): "Hey, you always say question length is just a warning but
not a blocking but it actually blocks our way when other tests all passed. We could pass because of
the question length even with 27. If you don't change your attitude, we can't pass forever." The form
labels the check "only a warning", and I had repeated that three times while the user's submissions
stalled on it. A 34-word question still drew it ("this one is 34" against a 35-47 band), so it tracks
the user's recent lengths and the safe target is clearly shorter than all of them.

**How to apply:** at sketch time, draft the question at 20 words or fewer; if the conditions cannot
fit, simplify the design rather than accept a long question. After the user pastes, check the
Question box for the warning before anything else. See [[docket-form-automated-checks]] for the
reasoning-box number check, which the same user also needs clean.

## Evidence and history

- 2026-10-08, aq-02028: q01 revs 1, 3 and 4 (47, 47 and 34 words) and q02 rev 0 (34 words) all drew the
  warning; q01 rev 2 (27 words) drew the user's "too easy. the previous state was better". q02 rev 1 was cut
  to 20 words; the form's reaction is pending.
