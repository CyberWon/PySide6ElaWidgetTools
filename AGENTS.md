# Agent Instructions

## Builds

- **Never run local CMake, Ninja, make, MSVC, Shiboken, or PyInstaller builds.** Local builds freeze the user's machine.
- Always push the intended commit and monitor the resulting GitHub Actions runs with `gh`.
- Only lightweight non-build validation is allowed, such as syntax checks and read-only repository audits.
