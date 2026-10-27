"""Regression tests for supplied Checks records, using temporary bundles only."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import platform_checks as pc


QUESTION = """---
id: q01
status: draft
origin: codex
asks: 1
answer_type: number
documents: D01, D02
tags: Cross-document join; Aggregation
levers: Calculate across documents
revision: 0
difficulty_target: easy
---
## Question
By how many million dollars did regional freight revenue change from calendar 2024 to calendar 2025? Give the signed difference to one decimal place.
## Answer
+$2.8 million
## Components
- c1: +$2.8 million
## Reasoning
Revenue rose from 409.8 million in 2024 to 412.6 million in 2025; 412.6 - 409.8 = 2.8 million dollars.
## Evidence
- D01 (table) [c1]: "Revenue for calendar 2024 was $409.8 million."
- D02 (table) [c1]: "Revenue for calendar 2025 was $412.6 million."
## Lever checks
Simple fixture, no claimed difficulty.
"""


def capture_text(overrides: dict | None = None, date: str = "2026-10-08 16:57", footer: str = "") -> str:
    overrides = overrides or {}
    return f"Saved: {date}\nChecks\n" + "\n".join(
        f"- {name}: {overrides.get(name, 'Passed')} \u00b7 1 hr ago \u2014 A warning, never a block."
        for name in pc.CHECKS) + "\n" + footer


class PlatformChecksTests(unittest.TestCase):
    def setUp(self):
        import docket_agent as da

        self.temp = tempfile.TemporaryDirectory(prefix="docket-checks-test-")
        self.addCleanup(self.temp.cleanup)
        self.bundle = Path(self.temp.name) / "tasks" / "freight"
        for name in ("docs", "text", "notes", "questions"):
            (self.bundle / name).mkdir(parents=True)
        manifest = {}
        for doc_id, year, amount in (("D01", "2024", "409.8"), ("D02", "2025", "412.6")):
            data = f"Revenue for calendar {year} was ${amount} million.\n".encode()
            for name in ("docs", "text"):
                (self.bundle / name / f"{doc_id}.txt").write_bytes(data)
            manifest[doc_id] = {"source": f"docs/{doc_id}.txt", "method": "text"}
        (self.bundle / "text/manifest.json").write_bytes(da.json_bytes(manifest))
        (self.bundle / "questions/q01.md").write_bytes(QUESTION.encode())
        self.prepared = da.prepare(self.bundle, "q01")
        self.fingerprint = self.prepared["tested_sha256"]
        self.capture = Path(self.temp.name) / "capture.txt"

    def record(self, text: str):
        self.capture.write_bytes(text.encode("utf-8"))
        return pc.record_capture(self.bundle, "q01", self.capture, 0, self.fingerprint)

    def report(self):
        return pc.summary(self.bundle, "q01", 0, self.fingerprint)

    def test_current_complete_capture_preserves_raw_and_is_separate_from_difficulty(self):
        text = capture_text()
        entry = self.record(text)
        report = self.report()
        self.assertTrue(report["current"])
        self.assertTrue(report["all_checks_passed"])
        self.assertEqual(report["blocking_clearance"], "clear")
        self.assertEqual(report["counts"]["passed"], 39)
        self.assertEqual((self.bundle / entry["capture_path"]).read_bytes(), text.encode())
        self.assertEqual((self.bundle / "questions/q01.md").read_text(), QUESTION)

    def test_actual_stale_37_of_39_capture_keeps_advisories_and_footer(self):
        source = (Path(__file__).resolve().parents[1]
                  / "tasks/aq-01650/archive/round1-q01/verdicts/AQ-01650_checks_2026-10-08_1657.txt")
        if not source.exists():
            self.skipTest("Historical capture not available in this checkout")
        parsed = pc.parse_capture(source.read_text(encoding="utf-8-sig"))
        self.assertEqual(parsed["counts"]["passed"], 37)
        self.assertEqual(parsed["counts"]["warning"], 1)
        self.assertEqual(parsed["counts"]["could_not_check"], 1)
        self.assertFalse(parsed["errors"])
        self.assertTrue(parsed["stale"])
        self.assertTrue(any("every document" in item for item in parsed["capture_blockers"]))

    def test_advisories_do_not_block_but_missing_rows_or_admin_results_do(self):
        self.record(capture_text({"Answer matches a stated figure": "Couldn't check",
                                  "Each description fits one thing": "Warning"}))
        report = self.report()
        self.assertEqual(report["blocking_clearance"], "clear")
        self.assertFalse(report["all_checks_passed"])
        self.assertEqual(len(report["advisory_issues"]), 2)
        self.record(capture_text({"Question in your own words": "Pending"}))
        self.assertEqual(self.report()["blocking_clearance"], "unknown")
        self.record(capture_text({"Reasoning in your own words": "Review \u00b7 advisory"}, date="2026-10-08 17:00"))
        self.assertEqual(self.report()["blocking_clearance"], "clear")
        self.record(capture_text().replace("- Which period:", "- Unrecognized period:"))
        self.assertEqual(self.report()["blocking_clearance"], "unknown")

    def test_duplicate_unknown_and_missing_checks_fail_closed(self):
        for text in (capture_text() + "\n- Question length: Passed\n",
                     capture_text() + "\n- New platform check: Passed\n",
                     capture_text().replace("- Which period: Passed", "Which period: Passed"),
                     capture_text({"Short answer": "Possibly passed"})):
            with self.subTest(text=text[-100:]):
                self.record(text)
                report = self.report()
                self.assertNotEqual(report["blocking_clearance"], "clear")
                self.assertTrue(report["errors"])

    def test_footer_blocks_even_with_39_passes_and_reload_is_stale(self):
        self.record(capture_text(footer="Still needed before you can submit:\n- Difficulty could not reach your answer.\n"))
        self.assertEqual(self.report()["blocking_clearance"], "blocked")
        self.record(capture_text(footer="Docket has been updated. Reload this page."))
        self.assertEqual(self.report()["blocking_clearance"], "stale")

    def test_latest_failure_and_changed_version_never_fall_back_to_pass(self):
        self.record(capture_text())
        self.record(capture_text({"One defensible answer": "Failed"}, date="2026-10-08 17:00"))
        self.assertEqual(self.report()["blocking_clearance"], "blocked")
        self.record(capture_text(date="2026-10-08 16:59"))
        self.assertEqual(self.report()["blocking_clearance"], "unknown")
        self.assertEqual(pc.summary(self.bundle, "q01", 1, self.fingerprint)["blocking_clearance"], "stale")
        self.assertEqual(self.report()["record_count"], 3)

    def test_capture_ledger_snapshot_and_corpus_tampering_fail_closed(self):
        entry = self.record(capture_text())
        raw_path = self.bundle / entry["capture_path"]
        raw = raw_path.read_bytes()
        raw_path.write_bytes(raw + b"altered")
        self.assertEqual(self.report()["blocking_clearance"], "unknown")
        raw_path.write_bytes(raw)
        snapshot_path = self.bundle / entry["snapshot_path"]
        snap = snapshot_path.read_bytes()
        snapshot_path.write_bytes(snap + b" ")
        self.assertEqual(self.report()["blocking_clearance"], "unknown")
        snapshot_path.write_bytes(snap)
        corpus = snapshot_path.parent / "corpus/text/D01.txt"
        original = corpus.read_bytes()
        corpus.write_bytes(b"altered")
        self.assertEqual(self.report()["blocking_clearance"], "unknown")
        corpus.write_bytes(original)
        ledger_path = self.bundle / "notes/platform-checks-q01.json"
        ledger = json.loads(ledger_path.read_bytes())
        ledger["records"][-1]["revision"] = 1
        ledger_path.write_bytes(json.dumps(ledger).encode())
        self.assertEqual(self.report()["blocking_clearance"], "unknown")

    def test_bad_bindings_paths_and_missing_preparation_are_rejected(self):
        self.capture.write_bytes(capture_text().encode())
        for qid, revision, digest in (("../q01", 0, self.fingerprint), ("q01", -1, self.fingerprint),
                                      ("q01", 0, "bad"), ("q01", 1, self.fingerprint)):
            with self.subTest(qid=qid, revision=revision, digest=digest):
                with self.assertRaises(ValueError):
                    pc.record_capture(self.bundle, qid, self.capture, revision, digest)
        for value in ("../outside", "D:/outside", "/outside"):
            with self.assertRaises(ValueError):
                pc._inside(self.bundle, value)
        self.assertFalse((self.bundle / "notes/platform-checks-q01.json").exists())


if __name__ == "__main__":
    unittest.main()
