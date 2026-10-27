"""Tests for tools/lever_mine.py: the mechanical comparisons behind notes/mine.md.

Usage: python tools/test_lever_mine.py (also run by tools/test_docket_agent.py)
Builds throwaway bundles in a temp directory; no model, platform or workspace task data is touched.
"""
from __future__ import annotations

import contextlib
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import docket_agent as da
import lever_mine as lm

REQUOTE = ("Additional categories of wholesale clients may be considered in line with foreign jurisdictions. "
           "For example, non-residents of Australia ought to be considered wholesale clients if they meet {insert}"
           "certain consent criteria. By adding this additional category of wholesale clients, {who} of the view "
           "that this may assist in attracting further foreign investment into Australian-domiciled schemes.")


class LeverMineTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="docket-mine-test-"))
        self.bundle = self.root / "tasks" / "demo"
        (self.bundle / "text").mkdir(parents=True)

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def docs(self, *texts: str) -> dict:
        manifest = {}
        for number, text in enumerate(texts, 1):
            doc_id = f"D{number:02d}"
            (self.bundle / "text" / f"{doc_id}.txt").write_bytes(
                f"# {doc_id} | docs/{doc_id}.txt\n\n{text}\n".encode("utf-8"))
            manifest[doc_id] = {"source": f"docs/{doc_id}.txt", "method": "text"}
        (self.bundle / "text" / "manifest.json").write_bytes(json.dumps(manifest).encode("utf-8"))
        return lm.mine(self.bundle)

    def test_a_clause_inserted_in_a_requoted_passage_is_listed_with_both_sides(self):
        # aq-04466 (row 32): AIMA's bullet re-quoted by another submitter with "their local definitions and" added.
        result = self.docs(REQUOTE.format(insert="", who="AIMA is"),
                           "Our view: - " + REQUOTE.format(insert="their local definitions and ", who="we are"))
        edits = [edit for passage in result["passages"] for edit in passage.edits]
        inserted = [edit for edit in edits if edit.right == "their local definitions and"]
        self.assertEqual(len(inserted), 1)
        self.assertEqual((inserted[0].kind, inserted[0].left), ("wording", ""))
        self.assertIn("[D01: - | D02: their local definitions and]", lm.markdown(result))
        # "non-residents" against "nonresidents" is one word, not an edit.
        self.assertFalse([edit for edit in edits if "residents" in edit.left + edit.right])

    def test_a_results_sentence_rolled_forward_is_a_frame_but_a_revised_figure_is_listed(self):
        frame = ("For the three months ended {date}, 2026, revenue from franchise and management fees was {amount} "
                 "million, driven by higher royalty rates across the franchised system and steady growth in the "
                 "number of rooms open and operating in every region the company serves.")
        result = self.docs(frame.format(date="March 31", amount="$412.6"),
                           frame.format(date="June 30", amount="$440.8"))
        self.assertEqual(result["passages"], [])
        self.assertEqual(sum(result["templates"].values()), 1)
        outlook = ("Management now expects full-year 2026 revenue of {low} million to {high} million and continues to "
                   "expect capital expenditures at the bottom of the range it gave with its annual results.")
        result = self.docs(outlook.format(low="$1,660", high="$1,710"), outlook.format(low="$1,685", high="$1,735"))
        kinds = [edit.kind for passage in result["passages"] for edit in passage.edits]
        self.assertEqual(kinds, ["figure", "figure"])
        # aq-05821: Wyndham's Q2 filing rewrote "Rooms grew 4%" as "Global rooms grew 3%, or 4% excluding Revo";
        # the figures move with the period, the inserted qualifier is the change worth reading.
        rooms = ("For the three months ended {date}, 2026, rooms grew {growth} compared to the prior year, including "
                 "flat growth in the U.S. and 12% direct-franchised growth in our Asia Pacific region, while the "
                 "pipeline reached another record level.")
        result = self.docs(rooms.format(date="March 31", growth="4%"),
                           rooms.format(date="June 30", growth="3%, or 4% excluding Revo,"))
        edits = [(edit.kind, edit.right) for passage in result["passages"] for edit in passage.edits]
        self.assertIn(("qualifier", "excluding Revo,"), edits)
        self.assertTrue(all(passage.effective(edit) == 0 for passage in result["passages"] for edit in passage.edits
                            if edit.kind == "figure"), "figures that move with the period score nothing")

    def test_an_exception_in_only_one_of_two_parallel_rules_ranks_first(self):
        # aq-02562 (Hard): the MASC rule's "unless ..." against the ASCF rule's plain cap, in different words.
        masc = ("A person or legal entity, other than a joint venture or general partnership, will not be eligible "
                "to receive a program payment if the average adjusted gross income of the person exceeds $900,000 "
                "for 2021, 2022 and 2023, unless at least 75 percent of that income comes from farming operations.")
        ascf = ("In addition, a person or legal entity, other than a joint venture or general partnership, is "
                "ineligible for grant payments if the person's average adjusted gross income, using the 2021, 2022 "
                "and 2023 tax years, exceeds $900,000.")
        result = self.docs(masc, ascf)
        first = result["parallels"][0]
        self.assertEqual((first["doc_a"], first["doc_b"]), ("D01", "D02"))
        self.assertEqual(first["markers_a"], ["at least", "not", "unless"])
        self.assertIn("only D01 says 'at least', 'not', 'unless'", lm.markdown(result))

    def test_quarters_printed_only_cumulatively(self):
        result = self.docs(
            "Revenue for the year ended December 31, 2025 was $1,640.2 million, up from the prior year.",
            "Revenue for the nine months ended September 30, 2025 was $1,210.5 million.\n"
            "Revenue for the three months ended June 30, 2026 was $440.8 million.\n"
            "Net cash provided by operating activities for the six months ended June 30, 2026 was $50.1 million.")
        derived = result["periods"]["derived"]
        self.assertEqual([(d["quarter_end"], d["cumulative"]) for d in derived],
                         [("September", "9 months"), ("December", "12 months")])
        self.assertIn("9 months ended September (D02)", derived[1]["less"])
        self.assertEqual([c["doc"] for c in result["periods"]["cash_only"]], ["D02"])

    def test_restatement_statements_but_not_a_restated_credit_agreement(self):
        result = self.docs("Prior-period amounts have been recast to conform to the current presentation.\n"
                           "On June 28, 2024, the Company entered into a Second Amended and Restated Credit Agreement.\n"
                           "The Restated Credit Agreement increased the commitments under the Revolver.\n"
                           "A reconciliation of net income to adjusted EBITDA is represented below:",
                           "Beginning in the second quarter of 2025, we revised our reporting methodology to exclude "
                           "rooms under one master licensee.")
        self.assertEqual([(h["doc"], h["line"], h["kind"]) for h in result["restated"]],
                         [("D01", 3, "restated or recast"), ("D02", 3, "definition or basis changed")])

    def test_abbreviations_used_bare_elsewhere_and_name_variants(self):
        result = self.docs("Higher Mass Limits (HML) allow heavier axles. Prospectuses and Product Disclosure "
                           "Statements (PDS) were reviewed. Cedars-Sinai joined the venture.",
                           "Operators want HML on more roads, each PDS is long, and Cedars Sinai is a partner.",
                           "Product Disclosure Statements are long.")
        found = {item["short"]: item for item in result["abbreviations"]}
        self.assertEqual(found["HML"]["full"], "Higher Mass Limits")
        self.assertEqual(found["HML"]["short_only"], ["D02"])
        self.assertEqual((found["PDS"]["full"], found["PDS"]["full_only"]), ("Product Disclosure Statements", ["D03"]))
        variants = [set(item["variants"]) for item in result["names"]]
        self.assertIn({"cedars-sinai", "cedars sinai"}, variants)

    def test_a_restated_row_is_listed_only_when_the_two_documents_share_a_period(self):
        early = ("Total revenues | 1,200.0 1,100.0\nOperating income | 300.5 280.2\nInterest expense | 50.1 45.3\n"
                 "Net income attributable | 210.4 190.1\nAdjusted EBITDA | 400.2 380.9")
        later = ("Total revenues | 1,300.0 1,200.0\nOperating income | 320.0 300.5\nInterest expense | 55.0 50.1\n"
                 "Net income attributable | 230.0 210.4\nAdjusted EBITDA | 420.0 388.0")
        rows = self.docs(early, later)["rows"]
        self.assertEqual([(r["label"], r["values_a"], r["values_b"]) for r in rows],
                         [("adjusted ebitda", ["400.2", "380.9"], ["420", "388"])])
        unrelated = later.replace("1,200.0", "1,250.0").replace("300.5", "305.0").replace("50.1", "51.0") \
            .replace("210.4", "215.0")
        self.assertEqual(self.docs(early, unrelated)["rows"], [], "no shared period, so no restatement signal")

    def test_rounded_prose_notes_counts_and_summary_only_figures(self):
        # Lines: 1 header, 2 blank, 3 heading, 4 highlight, 5 heading, 6-7 table, 8 note, 9 prose.
        result = self.docs("Financial highlights\n- Shareholder returns reached $1.4 billion in the second quarter, "
                           "including dividends and buybacks across all programs and markets served.\n"
                           "Results of operations\nDividends paid | 900 850\nRepurchases of common stock | 495 400\n"
                           "(1) Excludes securities without readily determinable fair values.\n"
                           "The board noted that approximately $543 million remained under the program after the "
                           "quarter, and that eight people joined the audit committee during the year.")
        self.assertEqual([h["line"] for h in result["rounded"]], [4, 9])
        self.assertEqual([h["line"] for h in result["notes"]], [8])
        self.assertEqual([h["line"] for h in result["counts"]], [9])
        self.assertEqual([(h["line"], h["figure"]) for h in result["summary_only"]], [(4, "$1.4 billion")])

    def test_mine_writes_notes_only_inside_a_named_bundle(self):
        self.docs("Revenue for the year ended December 31, 2025 was $1,640.2 million.",
                  "Revenue for the nine months ended September 30, 2025 was $1,210.5 million.")
        with mock.patch.object(da, "ROOT", self.root), contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(da.main(["mine", str(self.bundle)]), 0)
        summary = json.loads(out.getvalue())
        self.assertEqual(summary["counts"]["derived_periods"], 2)  # Q4 (year less nine months) and Q3
        text = (self.bundle / "notes" / "mine.md").read_text(encoding="utf-8")
        self.assertIn("The quarter ending December is never printed as three months", text)
        self.assertIn("Navigation only", text)
        with mock.patch.object(da, "ROOT", self.root), contextlib.redirect_stderr(io.StringIO()) as err:
            self.assertEqual(da.main(["mine", str(self.bundle), "--q", "q01"]), 1)
            template = self.root / "tasks" / "template-task"
            (template / "text").mkdir(parents=True)
            self.assertEqual(da.main(["mine", str(template)]), 1)
        self.assertIn("not the template", err.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=2)
