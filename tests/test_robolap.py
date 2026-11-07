"""Hardware-free safety and skill tests."""

import unittest

from robolap.core import Pose, Workspace
from robolap.robots import SimulatedArm
from robolap.skills import PickAndPlace


class RoboLapTests(unittest.TestCase):
    def setUp(self):
        self.workspace = Workspace(-250, 250, -250, 250, 0, 300)
        self.arm = SimulatedArm("test", self.workspace, Pose(0, 0, 150))

    def test_disarmed_motion_rejected(self):
        with self.assertRaises(RuntimeError):
            self.arm.move_to(Pose(10, 0, 100))

    def test_workspace_motion_limit(self):
        self.arm.arm()
        with self.assertRaises(ValueError):
            self.arm.move_to(Pose(900, 0, 100))

    def test_emergency_stop_is_latched(self):
        self.arm.arm()
        self.arm.emergency_stop()
        with self.assertRaises(RuntimeError):
            self.arm.arm()
        with self.assertRaises(RuntimeError):
            self.arm.set_gripper("closed")

    def test_pick_and_place_simulation(self):
        self.arm.arm()
        PickAndPlace().execute(self.arm, Pose(-100, 0, 20), Pose(100, 0, 20))
        self.arm.disarm()
        self.assertEqual(self.arm.gripper, "open")
        self.assertEqual(self.arm.pose, Pose(100, 0, 60))
        self.assertIn("gripper:closed", self.arm.history)
        self.assertFalse(self.arm.armed)

    def test_skill_preflights_entire_path(self):
        self.arm.arm()
        initial_events = list(self.arm.history)
        with self.assertRaises(ValueError):
            PickAndPlace().execute(self.arm, Pose(-100, 0, 290), Pose(100, 0, 20))
        self.assertEqual(self.arm.history, initial_events)

    def test_invalid_gripper_command_rejected(self):
        self.arm.arm()
        with self.assertRaises(ValueError):
            self.arm.set_gripper("squeeze-harder")

    def test_nonfinite_position_rejected(self):
        with self.assertRaises(ValueError):
            Pose(float("nan"), 0, 0)


if __name__ == "__main__":
    unittest.main()
