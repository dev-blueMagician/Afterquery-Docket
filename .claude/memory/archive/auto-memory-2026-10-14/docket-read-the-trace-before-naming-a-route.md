---
name: docket-read-the-trace-before-naming-a-route
description: "Docket verdict read-outs: state why a solver attempt went wrong only after reading that attempt's own Full answer and Reasoning, never from its number or the platform's one-line note"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 0b0b5f34-8182-4765-8e60-457254c86714
  modified: 2026-10-13T14:26:42.822Z
---

When reporting a Docket difficulty capture, name a wrong attempt's route only from that attempt's own Full answer and Reasoning block. A committed number that equals a wrong route I predicted is not evidence of the route, and neither is the platform's "How it got there" line. If a Reasoning block was saved as "Loading the reasoning…", write "route unread" and ask for a new capture.

**Why:** user, 2026-10-12, on aq-02749 q02 (passed and submitted at Medium), sending a second capture of the same run: "plz check arrived verdicts, find out what you missed and improve your performance". My first read-out, the day before, said one middle-solver miss (6) was a list-length subtraction and the other (9) a miscount. Both were the same thing: one State's 17-entry list misread (wrong members; taken as the full 20). Both Reasoning blocks were already loaded in the first capture; I had read their opening lines and matched the numbers to my own predictions. I had also reduced the easier solver's failure to one inference when all five attempts failed two, and told the user a declared failure mode "caught no attempt" when its mechanism caught both misses. The wrong routes went into the report, the bundle notes and the lesson notes before the user asked me to look again.

**How to apply:** run `python tools/verdict_summary.py <capture> --q <question.md>` in `D:\Projects\Projects\AfterQuery-Docket\10.8`; it prints each attempt's line span, flags unloaded Reasoning and marks wrong attempts whose Full answer is a bare value. Read every wrong attempt's span before writing a route anywhere (chat, feedback note, memory). Read the strongest solver's every-document attempt too: it shows whether the gold has a second reading. Say which attempts I read in full. Workspace detail: `.claude/memory/docket-start-from-measured-misses.md` there. Related: [[docket-user-states-open-tier]] (take the user's report at face value; here, take the trace at face value over my prediction).

Further evidence, aq-03736 q01, 2026-10-13 (Easy, Low 1/5): the page's "Where it left your evidence" line called all four wrong attempts "the wrong application phase"; each Full answer places the company in the right phase, and none of the four traces contains the closing exception of that phase's sentence. Whether an attempt never reached a clause or read it and set it aside decides the repair, so `tools/verdict_summary.py --q` in the workspace now prints an "evidence echoed" line per attempt (share of each Evidence quote's wording that recurs, and "end not echoed"). It points to the span; it does not replace reading it.

Further evidence, aq-03170 q01, 2026-10-12 (two runs): the page's "Final answer" pick and its "Where it left your evidence" line misstated twelve attempts (they said the solver lacked an item its Full answer lists), and the page's own count of the commonest wrong answer was 4 where the Full answers show 9 and 14. Among the strongest solver's misses, look separately for "saw the passage and set it aside": one of four did, for a reason (a doubt about the reading and about whether a cited letter was a second one) that a reviewer could also raise. That attempt tells you which two passages the evidence rows must carry.
