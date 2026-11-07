# Safety rules

## Current version

RoboLap 0.1 has **no driver for real motors**. The in-memory emergency stop is a test-state latch, **not a physical safety device**.

## Before future hardware testing

- Verify manufacturer-specified power, wiring, controller and firmware for each exact arm.
- Install an **independent hardware power cut-off / emergency stop** reachable by the operator.
- Secure both robot bases; keep children and pets out of the operating area.
- Start with low speed and no load; exclude sharp, hot, heavy or breakable objects.
- Calibrate each arm separately before any overlap between workspaces.
- Add mechanical/joint/workspace constraints, obstacle checks and safe retreat behavior.
- Require explicit operator enable before motion; never execute free-form language or unvalidated model output as motor commands.
- Test loss of USB connection, sensor errors and failed grasp recovery.
- Record date, hardware variant, firmware version and incident reports.

This document is design guidance, not certification. No CE or safety conformity claim is made.
