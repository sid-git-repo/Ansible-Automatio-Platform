# Molecule: Windows (Delegated)

This scenario is a scaffold for testing the `common` role on a real Windows host.

## Usage
1. Prepare an inventory file pointing to your Windows host (WinRM enabled).
2. Run with:

```bash
cd roles/common
MOLECULE_INVENTORY_FILE=/path/to/windows_inventory.yml molecule test -s windows
```

## Notes
- The default CI pipeline does not run this scenario automatically.
- Designed for manual or ad-hoc testing.
