"""Behavioral tests for actual-work tracking, using temporary ledgers only.

These tests run no models, platform checks, or authoring diagnostics. Clock control
keeps elapsed-time assertions deterministic without sleeping or estimating work.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import docket_efficiency as efficiency


class DocketEfficiencyTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="docket-efficiency-test-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.ledger = self.root / "notes" / "efficiency.jsonl"
        self.now = datetime(2026, 10, 8, 9, tzinfo=timezone.utc)
        clock = mock.patch.object(efficiency, "utc_now", side_effect=lambda: self.now)
        clock.start()
        self.addCleanup(clock.stop)
        self.event_number = 0
        efficiency.init(self.ledger)

    def event(self, kind, *, bundle="bundle-a", candidate="i01", **fields):
        self.event_number += 1
        return {
            "kind": kind,
            "event_id": f"fixture-{self.event_number}",
            "bundle": bundle,
            "candidate": candidate,
            "source": "temporary test observation",
            **fields,
        }

    def record(self, kind, **fields):
        return efficiency.record(self.ledger, self.event(kind, **fields))

    def work(self, seconds, *, bundle="bundle-a", candidate="i01", phase="sketch",
             discard=False):
        started = efficiency.start(self.ledger, bundle, candidate, phase)
        self.now += timedelta(seconds=seconds)
        return efficiency.stop(self.ledger, started["session_id"], discard=discard)

    def row(self, *, bundle="bundle-a", candidate="i01"):
        report = efficiency.report(self.ledger)
        return next(row for row in report["candidates"] + report["unpromoted_candidates"]
                    if row["bundle"] == bundle and row["candidate"] == candidate)

    def test_init_does_not_enroll_history_or_backfill_unknown_work(self):
        historical = self.root / "tasks" / "old-bundle" / "questions"
        historical.mkdir(parents=True)
        (historical / "q01.md").write_text("status: accepted\nrevision: 8\n", encoding="utf-8")
        self.ledger = self.root / "notes" / "fresh-efficiency.jsonl"
        efficiency.init(self.ledger)
        report = efficiency.report(self.ledger)
        self.assertEqual(report["candidates"], [])
        self.assertEqual(report["unpromoted_candidates"], [])
        self.assertEqual(report["trial"]["enrolled"], 0)
        self.assertIsNone(report["trial"]["accepted_per_authoring_hour"])

        efficiency.promote(self.ledger, "bundle-a", "i01", "q01")
        row = self.row()
        self.assertEqual(row["authoring_seconds"], 0)
        self.assertEqual(row["timing_coverage"], "unknown")
        self.assertIsNone(row["reported_tokens"])
        self.assertEqual(row["outcome"], "pending")

    def test_stopped_intervals_measure_work_and_exclude_platform_wait(self):
        self.work(60)
        self.now += timedelta(hours=2)  # No authoring interval during platform wait.
        self.work(120, phase="draft")
        efficiency.promote(self.ledger, "bundle-a", "i01", "q01")
        row = self.row()
        self.assertEqual(row["authoring_seconds"], 180)
        self.assertEqual(row["phase_seconds"]["sketch"], 60)
        self.assertEqual(row["phase_seconds"]["draft"], 120)
        self.assertEqual(efficiency.report(self.ledger)["trial"]["authoring_seconds"], 180)

    def test_open_sessions_are_excluded_and_global_overlap_is_rejected(self):
        self.work(20)
        started = efficiency.start(self.ledger, "bundle-a", "i01", "revision")
        self.now += timedelta(hours=1)
        before = self.ledger.read_bytes()
        with self.assertRaises(ValueError):
            efficiency.start(self.ledger, "another-bundle", "i02", "sketch")
        self.assertEqual(self.ledger.read_bytes(), before)
        report = efficiency.report(self.ledger)
        self.assertEqual(report["active_session"]["session_id"], started["session_id"])
        self.assertEqual(self.row()["authoring_seconds"], 20)
        self.assertNotEqual(self.row()["timing_coverage"], "complete")

    def test_discarded_intervals_never_count_as_work_or_complete_timing(self):
        self.work(30)
        self.work(900, discard=True)
        efficiency.promote(self.ledger, "bundle-a", "i01", "q01")
        row = self.row()
        self.assertEqual(row["authoring_seconds"], 30)
        self.assertEqual(row["timing_coverage"], "partial")
        self.assertIsNone(efficiency.report(self.ledger)["active_session"])

    def test_five_promotions_are_global_and_repromoting_keeps_the_same_slot(self):
        for number in range(5):
            efficiency.promote(self.ledger, f"bundle-{number}", "i01", "q01")
        before = self.ledger.read_bytes()
        efficiency.promote(self.ledger, "bundle-0", "i01", "q01")
        self.assertEqual(self.ledger.read_bytes(), before)
        with self.assertRaises(ValueError):
            efficiency.promote(self.ledger, "bundle-5", "i01", "q01")
        self.assertEqual(self.ledger.read_bytes(), before)
        self.work(60, bundle="bundle-5")
        report = efficiency.report(self.ledger)
        self.assertEqual(report["trial"]["target"], 5)
        self.assertEqual(report["trial"]["enrolled"], 5)
        self.assertEqual({row["slot"] for row in report["candidates"]}, {1, 2, 3, 4, 5})
        self.assertEqual(report["trial"]["authoring_seconds"], 0)
        self.assertEqual(report["unpromoted"]["authoring_seconds"], 60)

    def test_receipt_replay_does_not_double_count_and_conflict_is_atomic(self):
        event = self.event("usage", total_tokens=123)
        self.assertTrue(efficiency.record(self.ledger, event)["recorded"])
        before = self.ledger.read_bytes()
        self.assertFalse(efficiency.record(self.ledger, event)["recorded"])
        self.assertEqual(self.ledger.read_bytes(), before)
        with self.assertRaises(ValueError):
            efficiency.record(self.ledger, {**event, "total_tokens": 124})
        self.assertEqual(self.ledger.read_bytes(), before)
        self.assertEqual(self.row()["reported_tokens"], 123)

    def test_attempt_and_revision_receipts_deduplicate_without_implying_acceptance(self):
        efficiency.promote(self.ledger, "bundle-a", "i01", "q01", revision=0)
        for _ in range(2):
            self.record("revision", revision=1, tested_sha256="a" * 64)
            self.record("platform_attempt", attempt_id="difficulty-run-1", stage="difficulty",
                        revision=1, tested_sha256="a" * 64)
        self.record("revision", revision=0, tested_sha256="b" * 64)
        self.record("platform_attempt", attempt_id="quality-run-1", stage="quality",
                    revision=1, tested_sha256="a" * 64)
        row = self.row()
        self.assertEqual(row["revision_rounds"], 1)
        self.assertEqual(row["platform_attempts"], 2)
        self.assertEqual(row["platform_stage_attempts"]["difficulty"], 1)
        self.assertEqual(row["platform_stage_attempts"]["quality"], 1)
        self.assertEqual(row["outcome"], "pending")
        self.assertEqual(efficiency.report(self.ledger)["trial"]["accepted"], 0)
        self.assertIsNone(efficiency.report(self.ledger)["trial"]["accepted_per_authoring_hour"])

    def test_invalid_usage_and_unbound_observations_do_not_mutate_the_ledger(self):
        bad_events = [self.event("usage", total_tokens=value)
                      for value in (True, -1, 1.5, float("nan"), float("inf"))]
        bad_events.extend([
            self.event("usage", total_tokens=1, source=""),
            self.event("platform_attempt", attempt_id="run-1", stage="difficulty", revision=0),
            self.event("platform_attempt", stage="quality", revision=0, tested_sha256="a" * 64),
            self.event("revision", revision=True, tested_sha256="a" * 64),
            self.event("revision", revision=-1, tested_sha256="a" * 64),
            self.event("revision", revision=1, tested_sha256="not-a-hash"),
            self.event("outcome", outcome="passed_difficulty"),
            self.event("session", seconds=300),  # Imported durations are not measured intervals.
        ])
        missing_source = self.event("usage", total_tokens=1)
        del missing_source["source"]
        bad_events.append(missing_source)
        for event in bad_events:
            with self.subTest(event=event):
                before = self.ledger.read_bytes()
                with self.assertRaises(ValueError):
                    efficiency.record(self.ledger, event)
                self.assertEqual(self.ledger.read_bytes(), before)

    def test_rate_waits_for_five_settled_candidates_and_complete_positive_timing(self):
        for number in range(5):
            candidate = f"i{number + 1:02}"
            efficiency.promote(self.ledger, "bundle-a", candidate, f"q{number + 1:02}")
            self.work(360, candidate=candidate)
            if number < 4:
                self.record("coverage", candidate=candidate, timing="complete", tokens="unknown")
                self.record("outcome", candidate=candidate,
                            outcome="accepted" if number < 2 else "rejected")
            self.assertIsNone(efficiency.report(self.ledger)["trial"]["accepted_per_authoring_hour"])

        self.record("outcome", candidate="i05", outcome="rejected")
        self.assertIsNone(efficiency.report(self.ledger)["trial"]["accepted_per_authoring_hour"])
        self.record("coverage", candidate="i05", timing="complete", tokens="unknown")
        trial = efficiency.report(self.ledger)["trial"]
        self.assertEqual(trial["settled"], 5)
        self.assertEqual(trial["accepted"], 2)
        self.assertEqual(trial["authoring_seconds"], 1800)
        self.assertAlmostEqual(trial["accepted_per_authoring_hour"], 4.0)
        self.work(10, candidate="i05", phase="revision")
        self.assertIsNone(efficiency.report(self.ledger)["trial"]["accepted_per_authoring_hour"])

    def test_unknown_token_usage_differs_from_an_explicit_zero(self):
        efficiency.promote(self.ledger, "bundle-a", "i01", "q01")
        self.assertIsNone(self.row()["reported_tokens"])
        self.record("usage", total_tokens=0)
        self.assertEqual(self.row()["reported_tokens"], 0)
        self.record("coverage", timing="unknown", tokens="complete")
        self.assertEqual(self.row()["token_coverage"], "complete")
        self.record("usage", total_tokens=2)
        self.assertEqual(self.row()["reported_tokens"], 2)
        self.assertEqual(self.row()["token_coverage"], "partial")

    def test_tracker_neither_reads_nor_rewrites_question_and_source_files(self):
        bundle = self.root / "tasks" / "bundle-a"
        fixtures = {
            bundle / "questions" / "q01.md": b"status: accepted\nFrozen wording.\n",
            bundle / "questions" / "q01.json": b'{"Question":"Frozen input value"}\n',
            bundle / "docs" / "original.txt": b"Original bundle source.\n",
        }
        for path, content in fixtures.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        original_open = Path.open

        def guarded_open(path, *args, **kwargs):
            if path in fixtures:
                self.fail(f"Efficiency tracker accessed a question or source: {path}")
            return original_open(path, *args, **kwargs)

        with mock.patch.object(Path, "open", guarded_open):
            self.work(60)
            efficiency.promote(self.ledger, "bundle-a", "i01", "q01")
            self.record("usage", total_tokens=42)
            self.record("outcome", outcome="accepted")
            efficiency.report(self.ledger)
        for path, content in fixtures.items():
            self.assertEqual(path.read_bytes(), content)


if __name__ == "__main__":
    unittest.main()
