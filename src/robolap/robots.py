"""Robot-arm contract and a guarded simulator; NO physical motor driver."""

from __future__ import annotations

from typing import Protocol

from robolap.core import Pose, Workspace


class RobotArm(Protocol):
    """Abstraction: real hardware adapters must enforce their own safety gates."""

    @property
    def workspace(self) -> Workspace: ...

    def arm(self) -> None: ...

    def disarm(self) -> None: ...

    def move_to(self, target: Pose) -> None: ...

    def set_gripper(self, state: str) -> None: ...

    def emergency_stop(self) -> None: ...


class SimulatedArm:
    """Log arm motions in memory. Does not communicate with physical hardware."""

    def __init__(self, name: str, workspace: Workspace, home: Pose) -> None:
        if not workspace.contains(home):
            raise ValueError("Home pose must be inside the workspace")
        self.name = name
        self.workspace = workspace
        self.pose = home
        self.gripper = "open"
        self.armed = False
        self.stopped = False
        self.history: list[str] = []

    def arm(self) -> None:
        if self.stopped:
            raise RuntimeError("Emergency stop is latched")
        self.armed = True
        self.history.append("armed")

    def disarm(self) -> None:
        self.armed = False
        self.history.append("disarmed")

    def _require_ready(self) -> None:
        if not self.armed or self.stopped:
            raise RuntimeError("Robot is disarmed or emergency-stopped")

    def move_to(self, target: Pose) -> None:
        self._require_ready()
        if not self.workspace.contains(target):
            raise ValueError(f"Target outside allowed workspace: {target}")
        self.pose = target
        self.history.append(f"move:{target.x},{target.y},{target.z}")

    def set_gripper(self, state: str) -> None:
        self._require_ready()
        if state not in ("open", "closed"):
            raise ValueError("Gripper state must be 'open' or 'closed'")
        self.gripper = state
        self.history.append(f"gripper:{state}")

    def emergency_stop(self) -> None:
        self.stopped = True
        self.armed = False
        self.history.append("EMERGENCY_STOP")
