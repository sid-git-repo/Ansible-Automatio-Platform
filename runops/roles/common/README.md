# Role: common

Cross-platform baseline role:

- **Linux**
  - Installs **chrony**
  - Templates `/etc/chrony/chrony.conf` using `ntp_server`
  - Templates `/etc/resolv.conf` using `dns_servers`
  - Handler to restart **chrony**
- **Windows**
  - Idempotently configures NTP via `w32tm` only when `ntp_server` differs
  - Sets DNS servers on all adapters via `win_dns_client`

## Variables
- `ntp_server`: NTP server (string)
- `dns_servers`: DNS servers (list of IPv4 addresses)
- `env`, `greeting`, `app_name` (from inventory `group_vars/all.yml`)

## Tags
- `ntp`, `dns`, `linux`, `windows`, `common`

## Molecule testing
- **Linux**: `roles/common/molecule/default`
- **Windows**: `roles/common/molecule/windows` (delegated, requires real host)
