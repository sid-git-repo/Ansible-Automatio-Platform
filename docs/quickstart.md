# Quickstart

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
pre-commit install
```

## Run
```bash
python scripts/cli.py run playbook -p playbooks/site.yml -i inventories/dev/hosts.yml
```

## Test
```bash
cd roles/common && molecule test
```

## CI/CD
- GitHub Actions: Linux runs automatically on push/PR
- Windows: trigger manually via workflow_dispatch
