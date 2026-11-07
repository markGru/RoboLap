"""Command-line demonstration: simulation only; no camera or physical driver."""

from __future__ import annotations

import argparse

from robolap.core import Pose, Workspace
from robolap.robots import SimulatedArm
from robolap.skills import PickAndPlace


def demo() -> None:
    workspace = Workspace(-250, 250, -250, 250, 0, 300)
    left_arm = SimulatedArm("left", workspace, Pose(0, 0, 150))

    print("RoboLap SIMULATION ONLY — no physical hardware connected")
    left_arm.arm()
    try:
        PickAndPlace(clearance_mm=40).execute(
            left_arm,
            source=Pose(-100, 0, 25),
            destination=Pose(100, 0, 25),
        )
    finally:
        left_arm.disarm()

    for event in left_arm.history:
        print(event)
    print("Demo finished: simulated pick-and-place; real grasp not verified.")


def main() -> None:
    parser = argparse.ArgumentParser(description="RoboLap (safe simulation only)")
    parser.add_argument("command", nargs="?", choices=["demo"], default="demo")
    parser.parse_args()
    demo()


if __name__ == "__main__":
    main()
