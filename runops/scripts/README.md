# scripts/

Python helper CLI (Click) for common workflows.

## Commands
```bash
python scripts/cli.py run playbook -p playbooks/site.yml -i inventories/dev/hosts.yml
python scripts/cli.py run ping --inventory inventories/dev/hosts.yml
python scripts/cli.py lint
python scripts/cli.py molecule
```
The CLI wraps `ansible`/`ansible-playbook` with the repo's `ansible.cfg`.
