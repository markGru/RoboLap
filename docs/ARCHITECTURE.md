# Architecture — RoboLap 0.1

## Design rule

**Planning AI is never a raw motor controller.** Skills receive structured goals. All physical commands, when implemented, must pass deterministic bounds, safety and validation checks. Version 0.1 is **simulation only**.

```text
Task / Human command
         |
Skill registry and planner (planned)
         |
Vision observations (planned) -----> PickAndPlace skill (implemented)
                                            |
                                 RobotArm interface
                                            |
                                  SimulatedArm (implemented)
                                  SO-101 adapter (not built)
```

## Modules

- `core.py`: `Pose` and `Workspace`, millimetres.
- `robots.py`: `RobotArm` protocol, explicit arm/disarm, latched emergency stop in simulator.
- `skills.py`: preflight checks and simulated pick-and-place sequence.
- `cli.py`: deterministic example without hardware.

## Next interfaces

1. `VisionProvider`: timestamped object detections, camera calibration and confidence.
2. `HardwareAdapter`: hardware capability descriptor, joint limits, power status, model-appropriate end-effector.
3. `SkillRegistry`: task preconditions, executor and explicit success checker.
4. `BimanualCoordinator`: world-coordinate transforms, collision zones, sequenced execution.
5. `DataRecorder`: synchronized camera, action, robot-state and human evaluation.
6. `LearningPipeline`: optional LeRobot ACT or other imitation learning after useful demonstration data exists.

Units: millimetres in the simulator. A future physical adapter must validate transformations and not assume simulator coordinate conventions match motor coordinates.

## Non-goals of v0.1

- No physical motion, servo firmware or automatic camera.
- No grasp-force verification, closed-loop motion, trajectory smoothing, collision detection or bimanual coordination.
- No guarantee that the SO-101 can pick up real socks or tile.
