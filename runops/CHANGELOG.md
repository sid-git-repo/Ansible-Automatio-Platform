# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-09-04
### Added
- READMEs across repo (inventories, roles, playbooks, Molecule scenarios, CI, scripts, plugins).
- Environment-specific inventory variables (NTP/DNS) and templating in `common` role.
- Linux Molecule tests for NTP/DNS; Windows delegated Molecule scenario.
- GitHub Actions workflow with optional Windows job via `workflow_dispatch`.
- Idempotent Windows NTP configuration in `common` role.
- Dev Container support (`.devcontainer/`) for reproducible VS Code environment.

## [0.1.0] - 2025-09-04
### Added
- Initial Ansible + Python framework: roles (`common`, `linux`, `windows`), inventories (dev/stage/prod), playbooks, CLI.
- Linting, Molecule (Linux), Jenkinsfile, GitHub Actions, plugins (custom module, filter, dynamic inventory).
