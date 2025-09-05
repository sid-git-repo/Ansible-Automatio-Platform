# Role: windows

The `windows` role is applied to hosts in the `windows` group.

## Features
- Ensures Notepad++ is installed via Chocolatey (`win_chocolatey` module).

## Requirements
- WinRM must be enabled and accessible from the Ansible controller.
- Chocolatey should be present (installer will run if missing).

## Usage
Automatically included in `playbooks/site.yml` for the `windows` group:
```yaml
- name: Site - windows baseline
  hosts: windows
  roles:
    - role: windows
```
