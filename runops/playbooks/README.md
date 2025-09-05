# Playbooks

- `site.yml` orchestrates roles by group:
  - `common` → all hosts
  - `linux`  → `linux` group
  - `windows` → `windows` group
- `ping.yml` for quick connectivity checks.

Run with:
```bash
python scripts/cli.py run playbook -p playbooks/site.yml -i inventories/dev/hosts.yml
```
