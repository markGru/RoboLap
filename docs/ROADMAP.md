# Research roadmap

## Phase 0 — Reproducible simulator (in progress)
- [x] Python package and CLI demo
- [x] Guarded virtual arm + bounded workspace
- [x] Unit tests and CI configuration
- [ ] Add reproducible multi-arm simulation with shared workspace and collision checks

## Phase 1 — RoboSocks / real hardware
- [ ] Confirm two identical SO-101 follower variants, power supplies and grippers
- [ ] Implement and bench-test one real-arm adapter, **manual-enable only**
- [ ] Mount laptop camera; calibrate image coordinates to table coordinates
- [ ] Detect 3 pairs of visually distinct socks
- [ ] Measure pick-and-place success across 20 trials, with human supervision

## Phase 2 — Reusable skills
- [ ] Publish a skill registry with preconditions and outcome checks
- [ ] Add safe, validated two-arm coordination and fallback recovery
- [ ] Apply the same pick-and-place interface to colored blocks
- [ ] Log task success rate, cycle time and failure categories

## Phase 3 — Learning by demonstration
- [ ] Evaluate LeRobot integration on the exact SO-101 build
- [ ] Record timestamp-synchronized camera and arm datasets with consent
- [ ] Train and evaluate a task-specific imitation-learning model
- [ ] Benchmark against deterministic baseline on held-out objects

## Phase 4 — Industrial demonstrators
- [ ] RoboAssembly: light plug-together parts
- [ ] RoboTile: *small dry sample tiles only*; inspect placement/fuges in mm
- [ ] Plan professional hardware and safety review before any real construction use

**Success criterion:** reconfigure a working pick-and-place skill for a different object class without rewriting motor control.
