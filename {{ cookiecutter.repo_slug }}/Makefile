.PHONY: help{% if cookiecutter.django_module %}
.PHONY: dev{% endif %}
.PHONY: docs
.PHONY: tests
.PHONY: test
.PHONY: tox
.PHONY: hook
.PHONY: lint{% if cookiecutter.django_module %}
.PHONY: migrate
.PHONY: migrations{% endif %}
.PHONY: Makefile

# Trick to allow passing commands to make
# Use quotes (" ") if command contains flags (-h / --help)
args = `arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:-${1}}`

# If command doesn't match, do not throw error
%:
	@:

define helptext

  Commands:
{% if cookiecutter.django_module %}
  dev                  Serve manual testing server{% endif %}
  docs                 Serve mkdocs for development.
  tests                Run all tests with coverage.
  test <name>          Run all tests maching the given <name>
  tox                  Run all tests with tox.
  hook                 Install pre-commit hook.
  lint                 Run pre-commit hooks on all files.{% if cookiecutter.django_module %}
  migrate              Run pre-commit hooks on all files.
  migrations           Run pre-commit hooks on all files.{% endif %}

  Use quotes (" ") if command contains flags (-h / --help)
endef

export helptext

help:
	@echo "$$helptext"
{% if cookiecutter.django_module %}
dev:
	@poetry run python manage.py runserver localhost:8000{% endif %}

docs:
	@poetry run mkdocs serve -a localhost:8080

tests:
	@poetry run coverage run -m pytest

test:
	@poetry run pytest -k $(call args, "")

tox:
	@poetry run tox

hook:
	@poetry run pre-commit install

lint:
	@poetry run pre-commit run --all-files
{% if cookiecutter.django_module %}
migrate:
	@poetry run python manage.py migrate

migrations:
	@poetry run python manage.py makemigrations{% endif %}
