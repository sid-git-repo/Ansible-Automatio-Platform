# Role: linux

The `linux` role is applied to hosts in the `linux` group.

## Features
- Installs baseline packages:
  - curl
  - vim
  - git

## Variables
No defaults required.

## Usage
Automatically included in `playbooks/site.yml` for the `linux` group:
```yaml
- name: Site - linux baseline
  hosts: linux
  roles:
    - role: linux
```
