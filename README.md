# Cookiecutter PyPackage

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for Python package.

## Features

- `src` project structure - [how and why](https://bskinn.github.io/My-How-Why-Pyproject-Src)
- Checks & tests with [tox](https://tox.readthedocs.io)
  - Formatting with [black](https://github.com/psf/black)
  - Check sorted imports with [isort](https://pycqa.github.io/isort/)
  - Code analysis with pylint [pylint](https://www.pylint.org)
  - Type checks with [mypy](http://mypy-lang.org)
  - Testing with [pytest](https://pytest.org)
- `pyproject.toml` for configuration
- CI and deployment to PyPI with [GitHub Actions](https://github.com/features/actions)
- Documentation with [Sphinx](https://www.sphinx-doc.org)
  - Easy API documentation with [autosummary](https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html)
  - Leverage type annoations for docs with [sphinx-autodoc-typehints](https://github.com/agronholm/sphinx-autodoc-typehints)
- Changelog based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```
pip install -U cookiecutter
```

Generate a Python package project:

```
cookiecutter https://github.com/lukasberbuer/cookiecutter-pypackage.git
```

Then:
- Follow instructions in generated README to set up development environment
- Create a GitHub repository and push it there
- [Register](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives) your project with PyPI
- Add API tokens as GitHub secrets for [PyPI](https://pypi.org/) (`PYPI_API_TOKEN`) and [Test PyPI](https://test.pypi.org/) (`TEST_PYPI_API_TOKEN`) for automated publishing
- Add the repo to your [Read the Docs](https://readthedocs.org/) account and activate the service hook
- Release your package by pushing a new tag to master
