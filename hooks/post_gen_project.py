import os
import shutil


use_pypi = "{{ cookiecutter.use_pypi }}" == "y"
use_readthedocs = "{{ cookiecutter.use_readthedocs }}" == "y"


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if not use_pypi:
    remove(".github/workflows/publish.yml")

if not use_readthedocs:
    remove(".readthedocs.yml")
