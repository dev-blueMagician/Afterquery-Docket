# q01 platform form feedback, received 2026-10-08 (unbound)

Two screenshots from the user, sent to the session that revised q01 to rev 9. Saved unchanged:

- `form-question-box.png` (sha256 5a26d6c2...): the Question box.
- `form-components-evidence-panel.png` (sha256 ea13fca9...): the "Components, evidence, documents and tags" panel.

## What the screenshots show (transcribed verbatim)

Question box text: "In 2024, what was coal's share of Poland's electricity generation minus coal's share of
Bulgaria's, in percentage points to one decimal place?" Below it: "Needs more than one place · Not a keyword
search · Self-contained wording · Nothing given away" and "22 words · Aim as short as it can be and stay exact
— short is good. Over 60 words gets a warning; over 80 can't be submitted." Then the "Pin it down (rule 9)"
box, whose second bullet reads: "Name the period exactly: the quarter or year, and "fiscal" or "calendar" when
the fiscal year doesn't end in December."

Red message under the Question box:

> Working the question from the documents does not give this answer. Check which figure, period and entity the
> question asks for, and that each value comes from the right row and column.

Components panel: "1. 22.8 percentage points · 5 quote(s)"; "Needs: Doc 1 · ccg_energy_cleantech_sectors_bulgaria.txt"
and "Doc 2 · ccg_energy_cleantech_sectors_poland.txt"; "Tags: Cross-document join, Temporal alignment, Unit
normalization". Orange message:

> The quote from document 1 for component 1 ("From September 2024 to August 2025, electricity consumption...")
> does not seem to support that component. The quote covers September 2024 to August 2025 and gives a nuclear
> share of 40.38%, which is a different period and figure than the 2024 annual 41.6% used in the calculation. It
> is not used by the component. Use a quote that gives the value, or a figure or fact you used to work it out.

"Suggested passages (0)" ... "No missing passages found."

## Identity

The question, gold component and necessary documents match q01 revs 1-8 (unchanged in all of them). The
reasoning box is not shown, so the revision cannot be pinned between revs 1 and 8 (rev 8's hand-over was the
latest generated). The form's evidence held five quotes; every local revision has four, and none quotes the
September 2024-August 2025 paragraph. Revs 0-5 had a reasoning "Decoy" line naming that paragraph's 27.6%, and
the page keeps evidence rows between pastes, so the fifth row most likely came from an earlier "Derive the rest"
proposal (the pattern recorded for aq-01650 q01). No local fingerprint matches the tested form state, so no
platform validation record is bound to it. No difficulty check was run.
