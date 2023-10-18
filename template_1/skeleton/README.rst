{% set is_open_source = values.open_source_license != 'Not open source' -%}
{% for _ in values.project_name %}={% endfor %}
{{ values.project_name }}
{% for _ in values.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ values.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ values.project_slug }}

.. image:: https://img.shields.io/travis/{{ values.github_username }}/{{ values.project_slug }}.svg
        :target: https://travis-ci.com/{{ values.github_username }}/{{ values.project_slug }}

.. image:: https://readthedocs.org/projects/{{ values.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ values.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status
{%- endif %}

{{values.cloud_provider }}

{{ values.description }}

{% if is_open_source %}
* Free software: {{ values.open_source_license }}
* Documentation: https://{{ values.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Credits
-------

This package was created with values_ and the `audreyr/values-pypackage`_ project template.

.. _values: https://github.com/audreyr/values
.. _`audreyr/values-pypackage`: https://github.com/audreyr/values-pypackage
