# RoboLap — Universal Robotics AI Lab

A modular, hardware-independent robotics playground for learning transferable robot skills: **see → plan → grasp → verify**.

**Status: experimental.** The repository currently implements only a **software simulator**, not an operational SO-101 hardware driver, camera perception, AI model, or autonomous bimanual manipulation.

## Goals

- Start with two SO-101 **follower** robotic arms, USB serial controllers and an existing laptop camera.
- Build reusable skills rather than one-off movement scripts.
- Grow from `RoboSocks` (sorting socks) to `RoboSort`, `RoboAssembly` and a miniature `RoboTile` demonstrator.
- Keep the planning, perception, motion and hardware interfaces separate.
- Make safety and reproducible tests mandatory before any real motors move.

## Quick start — simulation only

Prerequisite: Python 3.10+.

```bash
git clone https://github.com/markGru/RoboLap.git
cd RoboLap
python -m pip install -e .
robolap demo
python -m unittest discover -s tests -v
```

`robolap demo` performs a simulated pick-and-place run with a **single virtual arm**. It never commands physical motors. No camera is required.

## Structure

```
src/robolap/
  core.py             # Robot positions and bounds
  robots.py           # Protocol and guarded simulation robot
  skills.py           # Reusable, testable pick-and-place skill
  cli.py              # Simulator entry point
tests/                # Unit tests
docs/ARCHITECTURE.md  # Planned system boundaries and extension points
docs/ROADMAP.md       # RoboSocks → RoboTile stages
docs/SAFETY.md        # Rules for any future hardware connection
```

## Hardware roadmap

The first physical target is **two SO-101 follower arms**, not a leader/follower pair. Before connecting motors, confirm controller, voltage, powered USB/serial links, calibrated workspaces, gripper limits, firmware and emergency-stop procedure. **No physical driver is supplied yet.**

For demonstration-based learning, see [Hugging Face LeRobot](https://huggingface.co/docs/lerobot/index). Software interfaces and compatibility must be verified for the exact purchased SO-101 variant.

## Contribution and license

Contributions and issue discussions are welcome. **A software license has not yet been chosen**; public visibility alone does not grant permission to reuse code. We will choose an open-source license (for example MIT or Apache-2.0) before inviting external code contributions.
