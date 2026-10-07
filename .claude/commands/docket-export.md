---
description: Export only questions with current local validation, an observed platform pass at their target and eligible authorship
argument-hint: <slug>
model: claude-opus-5-5
effort: max
---

Read applicable memory and newer-guide checks. For the named bundle, use report/checker to
verify each question's current revision and submitted-content fingerprint. Local review is
separate from observed Easy/Medium/Hard survival, authorship and submission permission.

1. Run python tools/check_questions.py tasks/<slug> --export. The tool exports ready questions
   with no FAIL and eligible origin: user. Other origins retain their actual agent/collaboration label;
   never relabel them to bypass export. A valid explicit platform pass must meet that question's
   target; reached/attempted tier counts alone are insufficient.
2. Report dist/<slug>.md, exported/skipped ids, reasons, target and observed result. The sheet
   is the exact checked copy of record; avoid retyping form fields into chat.
3. Report applicable unavailable platform checks accurately. Do not attest personal authorship
   or user review. Preparation does not authorize external testing or submission.
4. Only on confirmed actual submission of an editable question set submitted, update session
   and freeze the entire question file. Once submitted/accepted, preserve every byte, including
   metadata and logs. Later submission/acceptance observations go in notes/feedback-qNN.md.
   Export alone never establishes submission. Preserve platform and local records tied to the
   exported fingerprint for later feedback.
