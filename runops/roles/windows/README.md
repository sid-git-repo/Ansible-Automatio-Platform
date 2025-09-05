# Role: windows

Baseline Windows role to extend for OS-specific tasks.

## Current tasks
- Ensures **Notepad++** is installed via Chocolatey

## Requirements
- WinRM reachable from controller
- Chocolatey available (install if necessary)

## Use
Included by `playbooks/site.yml` for the `windows` group.
