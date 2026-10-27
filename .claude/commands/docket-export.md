---
description: Export questions with a clean mechanical floor, an exact-content platform pass at target and eligible authorship
argument-hint: <slug>
model: claude-opus-5-5
effort: max
---

Read applicable memory and newer-guide checks. The export command verifies the current
revision, submitted-content fingerprint and mechanical floor. Do not launch local models or
refresh historical diagnostics. Platform survival, authorship and submission remain separate.

1. Run python tools/check_questions.py tasks/<slug> --export. The tool exports ready questions
   with no FAIL and eligible origin: user. Other origins retain their actual agent/collaboration label;
   never relabel them to bypass export. A valid explicit platform pass must meet that question's
   target; reached/attempted tier counts alone are insufficient.
2. Report dist/<slug>.md, exported/skipped ids, reasons, target and observed result. The sheet
   is the exact checked copy of record; avoid retyping form fields into chat. It holds every
   form field in the form's order (the --handover renderer), Targeted failure modes included;
   a ready question without them fails the floor. For other origins, --handover writes the same
   fields to notes/handover-qNN.md with the authorship stated, and it is not an export.
3. Report applicable unavailable platform checks accurately. Do not attest personal authorship
   or user review. Preparation does not authorize external testing or submission.
4. Only on confirmed actual submission of an editable question set submitted, update session
   and freeze the entire question file. Once submitted/accepted, preserve every byte, including
   metadata and logs. Later submission/acceptance observations go in notes/feedback-qNN.md.
   Export alone never establishes submission. Preserve platform and local records tied to the
   exported fingerprint for later feedback.
