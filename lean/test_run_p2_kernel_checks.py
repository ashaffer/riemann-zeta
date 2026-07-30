#!/usr/bin/env python3
"""Mock-only regression tests for p=2 runner process cleanup."""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from unittest import mock


RUNNER_PATH = Path(__file__).with_name("run_p2_kernel_checks.py")
SPEC = importlib.util.spec_from_file_location("run_p2_kernel_checks", RUNNER_PATH)
assert SPEC is not None and SPEC.loader is not None
runner = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = runner
SPEC.loader.exec_module(runner)


def _process_is_running(pid: int) -> bool:
    """Treat a gone or zombie mock child as no longer running."""

    try:
        state = Path(f"/proc/{pid}/stat").read_text(encoding="utf-8").split()[2]
    except (FileNotFoundError, IndexError, ProcessLookupError):
        return False
    return state not in {"X", "Z"}


class ProcessCleanupTests(unittest.TestCase):
    def test_term_resistant_descendant_is_killed_after_leader_exits(self) -> None:
        child_code = (
            "import signal,time; "
            "signal.signal(signal.SIGTERM, signal.SIG_IGN); "
            "print('ready', flush=True); "
            "time.sleep(60)"
        )
        leader_code = (
            "import subprocess,sys,time; "
            f"p=subprocess.Popen([sys.executable,'-c',{child_code!r}],"
            "stdout=subprocess.PIPE,text=True); "
            "assert p.stdout.readline().strip() == 'ready'; "
            "print(p.pid, flush=True); "
            "time.sleep(60)"
        )
        leader = subprocess.Popen(
            [sys.executable, "-c", leader_code],
            stdout=subprocess.PIPE,
            text=True,
            start_new_session=True,
        )
        assert leader.stdout is not None
        child_pid = int(leader.stdout.readline().strip())
        real_killpg = os.killpg
        sent_signals: list[int] = []

        def recording_killpg(pgid: int, sig: int) -> None:
            sent_signals.append(sig)
            real_killpg(pgid, sig)

        try:
            with mock.patch.object(runner.os, "killpg", recording_killpg):
                runner._terminate_process_group(
                    leader,
                    term_grace_seconds=0.15,
                    kill_grace_seconds=1.0,
                )
            deadline = time.monotonic() + 1.0
            while _process_is_running(child_pid) and time.monotonic() < deadline:
                time.sleep(0.02)
            self.assertIsNotNone(leader.poll())
            self.assertFalse(_process_is_running(child_pid))
            non_probe_signals = [sig for sig in sent_signals if sig != 0]
            self.assertEqual(non_probe_signals[0], signal.SIGTERM)
            self.assertIn(signal.SIGKILL, non_probe_signals[1:])
        finally:
            leader.stdout.close()
            try:
                real_killpg(leader.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            try:
                os.kill(child_pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            try:
                leader.wait(timeout=1.0)
            except subprocess.TimeoutExpired:
                leader.kill()
                leader.wait()

    def test_cancelled_reservation_kills_process_registered_late(self) -> None:
        controller = runner.ActiveRunController()
        controller.reserve(7)
        self.assertEqual(controller.cancel_all(), 1)
        process = subprocess.Popen(["sleep", "60"], start_new_session=True)
        try:
            controller.register(7, process)
            self.assertIsNotNone(process.poll())
            self.assertTrue(controller.was_cancelled(7))
        finally:
            runner._terminate_process_group(
                process, term_grace_seconds=0.1, kill_grace_seconds=0.5
            )

    def test_leaf_keyboard_interrupt_uses_single_foreground_group(self) -> None:
        class InterruptingProcess:
            pid = 987654321
            returncode = None

            def wait(self, timeout: float | None = None) -> None:
                raise KeyboardInterrupt

            def poll(self) -> None:
                return None

        process = InterruptingProcess()
        controller = runner.ActiveRunController()
        controller.reserve(1)
        target = runner.Target(Path("/mock/P2Mock.lean"), "RHBridge/P2Mock.lean")
        with tempfile.TemporaryDirectory() as directory:
            output_path = Path(directory) / "leaf.log"
            metrics_path = Path(directory) / "leaf.time"
            metrics_path.touch()
            with (
                mock.patch.object(runner.subprocess, "Popen", return_value=process)
                as popen,
                mock.patch.object(runner, "_terminate_process_group") as terminate,
                self.assertRaises(KeyboardInterrupt),
            ):
                runner._run_one(
                    target,
                    60.0,
                    output_path,
                    metrics_path,
                    True,
                    controller,
                    1,
                )

        command = popen.call_args.args[0]
        timeout_index = command.index("/usr/bin/timeout")
        self.assertEqual(command[timeout_index + 1], "--foreground")
        self.assertTrue(controller.was_cancelled(1))
        self.assertGreaterEqual(terminate.call_count, 1)

    def test_pending_interrupt_after_spawn_sees_registered_process(self) -> None:
        class SpawnedProcess:
            pid = 987654322
            returncode = None

            def wait(self, timeout: float | None = None) -> None:
                raise AssertionError("pending SIGINT should fire before wait")

            def poll(self) -> None:
                return None

        process = SpawnedProcess()
        controller = runner.ActiveRunController()
        controller.reserve(2)
        target = runner.Target(Path("/mock/P2Mock.lean"), "RHBridge/P2Mock.lean")
        with tempfile.TemporaryDirectory() as directory:
            output_path = Path(directory) / "leaf.log"
            metrics_path = Path(directory) / "leaf.time"
            metrics_path.touch()
            with (
                mock.patch.object(runner.subprocess, "Popen", return_value=process),
                mock.patch.object(
                    runner.signal,
                    "pthread_sigmask",
                    side_effect=[set(), KeyboardInterrupt()],
                ),
                mock.patch.object(runner, "_terminate_process_group") as terminate,
                self.assertRaises(KeyboardInterrupt),
            ):
                runner._run_one(
                    target,
                    60.0,
                    output_path,
                    metrics_path,
                    True,
                    controller,
                    2,
                )

        self.assertTrue(controller.was_cancelled(2))
        self.assertGreaterEqual(terminate.call_count, 1)


if __name__ == "__main__":
    unittest.main()
