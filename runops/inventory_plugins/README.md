# inventory_plugins/

Dynamic inventory scripts or plugins.

- `dynamic_example.py`: Minimal example returning localhost in a linux group.
Use with:
```bash
ansible-inventory -i inventory_plugins/dynamic_example.py --list
```
