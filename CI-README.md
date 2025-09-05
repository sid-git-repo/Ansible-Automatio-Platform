# CI Overview

## GitHub Actions
- Linux job: install deps, lint, run Molecule default scenario.
- Windows job: manual trigger with delegated host.

## Jenkinsfile
Stages:
1. Checkout
2. Setup venv & install deps
3. Lint
4. Molecule tests (Linux)
5. Package and archive `artifact.tar.gz`

Adjust the Jenkins `tools` or switch to containerized agents as needed.
