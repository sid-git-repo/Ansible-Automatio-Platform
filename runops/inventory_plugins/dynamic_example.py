
#!/usr/bin/env python3
# Minimal dynamic inventory example (returns localhost for any env)
import json, sys

def main():
    data = {
        "all": {
            "children": {
                "linux": {
                    "hosts": {"localhost": {"ansible_connection": "local"}}
                },
                "windows": {"hosts": {}}
            }
        }
    }
    print(json.dumps(data))

if __name__ == "__main__":
    main()
