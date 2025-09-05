
#!/usr/bin/env python3
import subprocess, sys, os, click

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANSIBLE_CFG = os.path.join(REPO_ROOT, "ansible.cfg")

def run(cmd, env=None):
    print("+", " ".join(cmd))
    res = subprocess.run(cmd, cwd=REPO_ROOT, env=env or os.environ.copy())
    sys.exit(res.returncode)

@click.group()
def cli():
    """Helper CLI for common automation tasks."""

@cli.group()
def run():
    """Run playbooks."""

@run.command("playbook")
@click.option("--playbook", "-p", default="playbooks/site.yml", help="Path to playbook")
@click.option("--inventory", "-i", default=None, help="Inventory file or plugin")
@click.option("--extra-vars", "-e", default=None, help="Extra vars (JSON or k=v)")
def run_playbook(playbook, inventory, extra_vars):
    cmd = ["ansible-playbook", playbook]
    if inventory:
        cmd.extend(["-i", inventory])
    if extra_vars:
        cmd.extend(["-e", extra_vars])
    run(cmd, env={"ANSIBLE_CONFIG": ANSIBLE_CFG, **os.environ})

@run.command("ping")
@click.option("--inventory", "-i", default=None, help="Inventory path")
def ping(inventory):
    cmd = ["ansible", "-m", "ping", "all"]
    if inventory:
        cmd.extend(["-i", inventory])
    run(cmd, env={"ANSIBLE_CONFIG": ANSIBLE_CFG, **os.environ})

@cli.command()
def lint():
    run(["make", "lint"])

@cli.command()
def molecule():
    run(["make", "molecule"])

if __name__ == "__main__":
    cli()
