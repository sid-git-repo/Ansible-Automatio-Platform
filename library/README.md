# library/

Custom Ansible modules written in Python.

- `my_echo.py`: Example module that echoes a message.
  ```yaml
  - name: Echo message
    my_echo:
      message: "Hello"
  ```
Place additional modules here and call them by their module name.
