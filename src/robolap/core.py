"""Shared geometry and bounded workspaces. Units are millimetres."""

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class Pose:
    x: float
    y: float
    z: float

    def __post_init__(self) -> None:
        if not all(isfinite(v) for v in (self.x, self.y, self.z)):
            raise ValueError("Pose coordinates must be finite")


@dataclass(frozen=True)
class Workspace:
    min_x: float
    max_x: float
    min_y: float
    max_y: float
    min_z: float
    max_z: float

    def __post_init__(self) -> None:
        bounds = (self.min_x, self.max_x, self.min_y, self.max_y, self.min_z, self.max_z)
        if not all(isfinite(v) for v in bounds):
            raise ValueError("Workspace bounds must be finite")
        if not (self.min_x < self.max_x and self.min_y < self.max_y and self.min_z < self.max_z):
            raise ValueError("Workspace min bounds must be smaller than max bounds")

    def contains(self, pose: Pose) -> bool:
        return (
            self.min_x <= pose.x <= self.max_x
            and self.min_y <= pose.y <= self.max_y
            and self.min_z <= pose.z <= self.max_z
        )
