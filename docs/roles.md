# Roles

## Common
- Applies to all hosts
- Configures NTP and DNS cross-platform
- Variables: `ntp_server`, `dns_servers`, `greeting`

## Linux
- Applies to `linux` group
- Installs baseline packages (curl, vim, git)

## Windows
- Applies to `windows` group
- Installs Notepad++ via Chocolatey
- Requires WinRM enabled

These roles are wired into `playbooks/site.yml` automatically.
