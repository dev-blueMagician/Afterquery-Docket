---
name: docket-ask-for-the-capture-before-submit
description: "Docket hand-overs: the last message before any difficulty run must ask for the capture before Submit, so the declared failure modes can be matched to the wrong answers actually observed"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 7e830c73-4aaa-4282-b71a-077dd8904eff
  modified: 2026-10-14T01:47:43.445Z
---

In the last message I send before a Docket difficulty run, however short (including a re-hand-over after the user rewords the question), say: after the run, save the page and send it before pressing Submit, so the targeted failure modes can be matched to the wrong answers the solvers actually gave. Failure modes are outside the content a run measures, so changing them costs no run.

**Why:** it has now gone wrong twice. aq-02564 q02 (2026-10-10): the user submitted before the capture arrived and the modes went in as predicted. aq-03557 q01 (2026-10-12): I gave the offer once, in the first hand-over, and not in the two shorter hand-overs that followed the user's rewordings; the user submitted at Medium and then sent the capture ("submitted as medium tier. plz check arrived verdicts ... and upgrade your ability"). One declared mode (a wrong-kind decoy, answer 392) had caught no attempt, while the commonest wrong answers (301 and 71) were undeclared. A submitted question is frozen, so the mismatch stays unless a reviewer returns the task. The workspace note already had the rule; I applied it once per bundle instead of once per run. My interpretation: the user did not ask for this line, but they did ask for the miss to change my behaviour.

Third case, aq-03950 q02 (2026-10-13): the line was in my last message before the run, and the user still submitted first ("Successfully submitted as a medium tier. plz check arrived verdicts ..."). This time nothing was lost: I had declared one mode only, the answer the lazy default gives (titles alone, two names), and all nine recorded wrong answers were exactly that. Mine, not the user's words: the user submits as soon as the page says "You can submit now", so asking is not enough on its own.

Fourth case, aq-03993 q02 (2026-10-13): the same again. The line was in my last message, the user submitted at Medium and then sent the capture. Nothing was lost: the one declared mode was the lazy default (the report's 75 taken for the total of 77), and both recorded wrong answers were 75. The revision before it had declared a look-alike mode that no medium attempt took; I replaced it before the run after reading the earlier run's traces. So the single-lazy-default rule has now held twice with the capture arriving late.

**How to apply:** treat the line as part of every pre-run message, not of the first hand-over only. Write the modes so they hold without the capture: declare the one wrong answer the easiest reading gives, recomputed, and leave out any trap I have only predicted. If the user has already submitted when the capture arrives, do not edit the frozen file: log the observed routes and the evidence-backed replacement picks in `notes/feedback-qNN.md`, and say plainly that the modes went in unaligned. Workspace detail: `.claude/memory/docket-handover-all-form-fields.md` ("Failure modes after a difficulty run") in `D:\Projects\Projects\AfterQuery-Docket\10.8`. Related: [[docket-read-the-trace-before-naming-a-route]], [[docket-report-readings-do-not-clear-them]].
