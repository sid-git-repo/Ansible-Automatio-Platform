# Contributing

Thanks for considering a contribution!

## Quick Start
1. Fork and clone the repo.
2. Create a Python venv and install deps:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt -r requirements-dev.txt
   pre-commit install
   ```
3. Make changes on a feature branch:
   ```bash
   git checkout -b feat/scope-short-desc
   ```
4. Lint and test:
   ```bash
   make lint
   cd roles/common && molecule test
   ```
5. Commit using Conventional Commits (recommended):
   - `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`, etc.
6. Open a Pull Request with a clear description of changes and testing.

## Style & Quality
- Python: formatted by **black** via pre-commit.
- YAML: **yamllint** and **ansible-lint** run in CI and locally.
- Ansible: prefer FQCN, idempotent tasks, `changed_when`/`check_mode` where appropriate.

## Tests
- **Linux** Molecule (Docker driver) runs by default.
- **Windows** Molecule (delegated) can be run manually with `MOLECULE_INVENTORY_FILE`.

## CI
- GitHub Actions runs on push/PR.
- Windows path is optional via `workflow_dispatch`.
- Jenkinsfile provided for Jenkins users.

## Security & Secrets
- Do **not** commit real credentials or vault files.
- Use environment variables, Ansible Vault, or sops for secrets.
