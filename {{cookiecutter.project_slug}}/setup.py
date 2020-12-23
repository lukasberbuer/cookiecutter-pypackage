from setuptools import setup, find_packages
from pathlib import Path

HERE = Path(__file__).parent

with open(HERE / "README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    # add requirements here
]

EXTRAS_REQUIRE = {
    "docs": [
        "sphinx>3.1",
        "sphinx-autodoc-typehints",
        "sphinx-rtd-theme",
        "m2r2",  # mdinclude directive
    ],
    "tests": [
        "coverage>=5",  # pyproject.toml support
        "pytest>=6",  # pyproject.toml support
    ],
    "tools": [
        "black",
        "isort",
        "mypy",
        "pylint>=2.5",  # pyproject.toml support
        "tox>=3.4",  # pyproject.toml support
    ],
}

EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["docs"] + EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["tools"]

setup(
    name="{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.version }}",
    description="{{ cookiecutter.project_short_description }}",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=[
        # add keywords here
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    project_urls={
        "Bug Reports": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues",
        "Source": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    },
)
