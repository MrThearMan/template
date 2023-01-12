# Cookiecutter template for writing libraries with poetry

> This template is meant for personal use for my own projects.

## How to use

```shell
pip install cookiecutter
cookiecutter gh:MrThearMan/template
```

## Options

| Setting        | Description                                                                                                |
|----------------|------------------------------------------------------------------------------------------------------------|
| `project_name` | Used for README title, mkdocs site name, and index page title.                                             |
| `project_slug` | Derived from `project_name`, separator is "-". Used in generating `module_slug`, `repo_slug`, `pypi_name`. |
| `module_slug`  | Derived from `project_slug`, separator is "_". Used to generate the project folder and module folder.      |
| `repo_slug`    | Derived from `project_slug`, separator is "-". Used to generate links to the repo.                         |
| `pypi_name`    | Derived from `repo_slug`, separator is "-". Used to for the poetry project name and pip links.             |
| `description`  | Short description for the project. Used for README and mkdocs index page description.                      |
