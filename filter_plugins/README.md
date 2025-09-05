# filter_plugins/

Custom Jinja2 filters for templates and tasks.

- `string_filters.py` provides `titlecase`:
  ```jinja2
  {{ 'hello world' | titlecase }}  # -> 'Hello World'
  ```
