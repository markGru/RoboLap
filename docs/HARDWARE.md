# Hardware integration checklist (future work)

Target: **two SO-101 follower arms**, each with a gripper, controller, data cable, suitable external PSU and rigid desk mount. Exact components vary by seller; confirm the full bill of materials before purchasing.

## Before connecting motors

- Record manufacturer, exact kit variant, motor IDs, firmware, serial settings and supplied power specifications.
- Confirm whether two independent USB serial connections are available and stable on the laptop.
- Check safe reachable table area and pinch points for each arm; verify bases remain rigid under load.
- Use an independent physical emergency power cut-off and an operator-present enable procedure.
- Never drive motors directly from LLM text. Validate action targets and joint limits in a separate control layer.
- Test one arm at a time at low speed with a lightweight, unbreakable object; add the second only after each is calibrated.
- For the existing laptop camera, test whether table coverage and perspective allow repeatable 2D-to-3D calibration. An overhead camera may eventually be required.

## Software integration

A future `SO101Adapter` should implement `RobotArm` while adding hardware-specific calibration, state feedback, watchdog, collision limits, error handling and independent e-stop. **Do not use the simulator's nominal Cartesian coordinates as raw servo positions.**

## Recording

Log task ID, target positions, observed positions, grasp success, run time, collisions avoided, failed actions and manual interventions. Never publish video with identifiable bystanders without consent.
