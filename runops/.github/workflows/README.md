# GitHub Actions CI

- Runs **Linux Molecule** on every `push` and `pull_request`.
- Optional **Windows Molecule (delegated)** via `workflow_dispatch`:
  - Input `run_windows_scenario=true`
  - Provide `windows_inventory_path` to an inventory file with a reachable Windows host.

Artifacts: none by default; rely on Molecule output and job logs.
