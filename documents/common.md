# Role: common

The `common` role is applied to **all hosts** and provides baseline configuration.

## Features
- **Greeting**: Displays combined `greeting` + `common_message`.
- **NTP**:
  - Linux: installs `chrony` and configures `/etc/chrony/chrony.conf` with `ntp_server`.
  - Windows: sets NTP peer list via `w32tm` (idempotent).
- **DNS**:
  - Linux: configures `/etc/resolv.conf` using `dns_servers`.
  - Windows: applies DNS servers on all adapters via `win_dns_client`.

## Variables
Defined in `inventories/*/group_vars/all.yml`:
- `ntp_server` (string): NTP server hostname or IP.
- `dns_servers` (list): DNS server IP addresses.
- `greeting` (string): environment greeting.
- `common_message` (string): default message from role.

## Usage
Automatically included in `playbooks/site.yml` for **all hosts**:
```yaml
- name: Site - common baseline
  hosts: all
  roles:
    - role: common
```
