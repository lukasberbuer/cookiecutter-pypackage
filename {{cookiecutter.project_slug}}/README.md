# {{ cookiecutter.project_name }}

[![CI](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/CI/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions)
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest)](https://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/?badge=latest)
{% if cookiecutter.use_pypi == 'y' -%}
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }})](https://pypi.org/project/{{ cookiecutter.project_slug }})
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }})](https://pypi.org/project/{{ cookiecutter.project_slug }}){%- endif %}
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

{{ cookiecutter.project_short_description }}

- Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io

{% if cookiecutter.use_pypi == 'y' -%}
## Installation

Install the latest version from PyPI:

```
pip install {{ cookiecutter.project_slug }}
```

{%- endif %}
## Development setup

After cloning the repository, you can easily install the development environment and tools
([black](https://github.com/psf/black), [pylint](https://www.pylint.org), [mypy](http://mypy-lang.org), [pytest](https://pytest.org), [tox](https://tox.readthedocs.io))
with:

```
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
pip install -e .[dev]
```

And run the checks & tests with tox:

```
tox
```

The documentation is built with [sphinx](https://www.sphinx-doc.org):

```
cd docs

# Windows
.\make.bat clean
.\make.bat html

# Linux
make clean html
```
