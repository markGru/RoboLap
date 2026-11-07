"""Reusable skills with preflight validation.

This is a kinematic toy simulation, not collision avoidance or force feedback.
"""

from __future__ import annotations

from dataclasses import dataclass

from robolap.core import Pose
from robolap.robots import RobotArm


@dataclass(frozen=True)
class PickAndPlace:
    """Move one simulated object between two known tabletop poses."""

    clearance_mm: float = 40.0

    def execute(self, arm: RobotArm, source: Pose, destination: Pose) -> None:
        if self.clearance_mm <= 0:
            raise ValueError("clearance_mm must be positive")

        src_above = Pose(source.x, source.y, source.z + self.clearance_mm)
        dst_above = Pose(destination.x, destination.y, destination.z + self.clearance_mm)
        waypoints = (src_above, source, src_above, dst_above, destination, dst_above)

        # Check every commanded pose BEFORE any motion happens.
        if not all(arm.workspace.contains(pose) for pose in waypoints):
            raise ValueError("Pick/place path leaves configured workspace")

        arm.set_gripper("open")
        arm.move_to(src_above)
        arm.move_to(source)
        arm.set_gripper("closed")
        arm.move_to(src_above)
        arm.move_to(dst_above)
        arm.move_to(destination)
        arm.set_gripper("open")
        arm.move_to(dst_above)
