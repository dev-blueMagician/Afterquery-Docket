---
name: docket-check-repeat-bundle-before-starting
description: "Docket: a newly assigned task may be an already-tried bundle under a new ID; compare its documents to earlier bundles first, and if familiar, ask the user whether to proceed"
metadata:
  node_type: memory
  type: feedback
  originSessionId: f5e29108-bfa2-4e9a-81a3-64064bec37f4
  modified: 2026-10-12T21:51:54.995Z
---

When the user assigns a new Docket task, first check whether its bundle was tried before. If it is familiar, say so and ask whether to proceed; the user decides. Do not start mapping, sketching or authoring until they answer. (User, 2026-10-12, standing instruction: "after checking, if it is a familiar one, ask me if you would proceed with it or not and let me decide.")

**Why:** The task ID increases with each claim regardless of the bundle, so the name never shows a repeat. The user re-claims bundles they already tried, partly because a newer model may now solve one that failed before, so a repeat is neither an automatic skip nor an automatic go.

**How to apply:**
- Identify by document content, never by ID. Compare the new bundle's documents against every earlier one: per-document `source_sha256` in `tasks/*/notes/intake.json`, plus the `docs/` filename set as a fallback for a re-capture whose bytes differ.
- Search the current workspace and the older snapshots beside it. On 2026-10-12 these were `D:\Projects\Projects\AfterQuery-Docket\10.6`, `10.7` and `10.8`; a few bundles exist only in the older ones (e.g. aq-01542), so check that the folders still exist rather than assuming.
- When it matches, report the earlier ID(s) and what the records show happened there (questions written, platform results, status), then ask. Mine, not the user's: treat a partial document overlap as familiar too, and ingesting the capture just to run the comparison is fine since nothing is authored.
- When nothing matches, say so in one line and carry on.

Evidence the pattern is real (10.8 on 2026-10-12, identical `docs/` filename sets under different IDs): aq-02102/02165/02198/02360; aq-02483/02626/02749; aq-02706/02780; aq-02220/02367.

Related: [[docket-user-states-open-tier]] (another decision the user keeps for themselves).
