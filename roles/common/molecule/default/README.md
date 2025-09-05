# Molecule: default (Linux, Docker)

Runs the `common` role against a Docker container and verifies:
- `/etc/chrony/chrony.conf` contains the `ntp_server`
- `/etc/resolv.conf` contains all `dns_servers`

## Commands
```bash
cd roles/common
molecule test              # full cycle
molecule converge          # create + apply
molecule verify            # run tests only
```
