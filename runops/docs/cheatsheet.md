# RunOps – Quick Reference Cheat Sheet

## Setup
```bash
# Create venv & install deps
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

## Run Playbooks
```bash
# Run site.yml against dev inventory
python scripts/cli.py run playbook -p playbooks/site.yml -i inventories/dev/hosts.yml

# Ping all hosts in stage
python scripts/cli.py run ping --inventory inventories/stage/hosts.yml
```

## Molecule Tests
```bash
# Test common role (Linux, Docker)
cd roles/common && molecule test

# Run Windows delegated scenario
MOLECULE_INVENTORY_FILE=inventory.yml molecule test -s windows
```

## Linting
```bash
# Run all linters (YAML + Ansible + Python)
make lint
```

## CI/CD
```bash
# GitHub Actions: Linux scenario auto-runs on push/PR
# Trigger Windows scenario manually:
workflow_dispatch: run_windows_scenario=true
```
