# VS Code Dev Container for Ansible + Python
FROM mcr.microsoft.com/devcontainers/python:3.12

# Install system deps for Ansible/Molecule and Docker client
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive     && apt-get install -y --no-install-recommends        git ssh sudo curl make jq        gcc build-essential        python3-dev        docker.io docker-compose-plugin        iputils-ping     && rm -rf /var/lib/apt/lists/*

# Optional: create a non-root user is already provided by base image (vscode)
# Pre-create workspace directories
WORKDIR /workspaces/project

# No requirements install here; use postCreateCommand to keep it fresh per repo
