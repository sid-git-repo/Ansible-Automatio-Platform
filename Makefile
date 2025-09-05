
.PHONY: install lint test molecule format

install:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt -r requirements-dev.txt

lint:
	ansible-lint || true
	yamllint . || true

test:
	pytest -q

molecule:
	cd roles/common && molecule test

format:
	pre-commit run --all-files
