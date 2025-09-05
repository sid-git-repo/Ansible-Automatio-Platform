
# Dev + CI container for Ansible + Python framework
FROM python:3.12-slim

# Install system deps
RUN apt-get update && apt-get install -y     sshpass openssh-client git curl vim     && rm -rf /var/lib/apt/lists/*

# Create workspace
WORKDIR /workspace

# Install Python deps
COPY requirements.txt requirements-dev.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt -r requirements-dev.txt

# Default command: bash shell
CMD ["/bin/bash"]
