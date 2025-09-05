# Inventories

This folder contains inventories for **dev**, **stage**, and **prod**. Each environment includes:
- `hosts.yml` with **linux** and **windows** groups and example hosts.
- `group_vars/all.yml` providing environment-specific variables:
  - `ntp_server`: used by the common role to configure chrony (Linux) or w32tm (Windows).
  - `dns_servers`: used to generate `/etc/resolv.conf` (Linux) or set DNS on Windows adapters.

## Usage
Run with a specific environment:
```bash
python scripts/cli.py run playbook -p playbooks/site.yml -i inventories/dev/hosts.yml
python scripts/cli.py run playbook -p playbooks/site.yml -i inventories/stage/hosts.yml
python scripts/cli.py run playbook -p playbooks/site.yml -i inventories/prod/hosts.yml
```
Replace IPs and credentials in `hosts.yml` with real values.
