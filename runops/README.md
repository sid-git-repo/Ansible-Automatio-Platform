<p align="center">
  <img src="website/assets/logo-runops.svg" alt="RunOps" width="120"/><br/>
  <img src="website/assets/badge-runops.svg" alt="RunOps badge"/>
</p>

![RunOps Logo](https://img.shields.io/badge/RunOps-Automation-blueviolet?style=for-the-badge&logo=ansible)

# RunOps Automation Framework (Enhanced)

This framework combines **Ansible automation** with **Python tooling** and ready-made CI/CD.

## Features
- Multi-environment inventories (dev, stage, prod) with NTP/DNS vars.
- Roles:
  - **common**: Configures NTP/DNS on Linux & Windows.
  - **linux**: Baseline Linux packages.
  - **windows**: Baseline Windows setup.
- Molecule testing:
  - Linux: Docker-based (default).
  - Windows: Delegated scenario for real hosts.
- CI/CD:
  - Jenkins pipeline (`Jenkinsfile`).
  - GitHub Actions workflow with Linux default + optional Windows.
- Python CLI (`scripts/cli.py`) for wrapping common commands.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
python scripts/cli.py run playbook -p playbooks/site.yml -i inventories/dev/hosts.yml
```

## Extending
- Add more roles inside `roles/`.
- Extend inventories with real hosts.
- Add Molecule scenarios for other OS targets.

## What's included

- **Inventories** for dev, stage, prod with sample Linux/Windows hosts and environment-specific variables (`ntp_server`, `dns_servers`, etc.).
- **Roles**
  - `common`: cross-platform baseline with NTP (chrony/w32tm) and DNS configuration driven by inventory vars.
  - `linux`, `windows`: baseline skeleton roles to extend per OS.
- **Molecule**
  - Linux **default** Docker scenario with tests that verify chrony and resolv.conf templating.
  - Windows **delegated** scenario scaffold to validate NTP/DNS on a real Windows host.
- **CI**
  - **GitHub Actions**: Linux scenario on push/PR, optional Windows scenario via workflow_dispatch.
  - **Jenkinsfile**: stages for venv setup, lint, Molecule, packaging.
- **Plugins & Extensions**
  - `library/my_echo.py` custom module, `filter_plugins/string_filters.py`, `inventory_plugins/dynamic_example.py`.
- **Python CLI**
  - `scripts/cli.py` to run playbooks and common tasks.
