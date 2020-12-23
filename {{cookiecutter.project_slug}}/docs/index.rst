{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}

.. autosummary::
    :caption: Library documentation
    :toctree: generated
    :recursive:

    {{ cookiecutter.project_slug }}

.. toctree::
    :caption: Development
    :hidden:

    changelog
    GitHub <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
