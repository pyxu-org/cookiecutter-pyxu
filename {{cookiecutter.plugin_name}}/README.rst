{{cookiecutter.plugin_name}}
{{ '=' * (cookiecutter.plugin_name | length) }}

.. image:: https://img.shields.io/pypi/l/{{cookiecutter.plugin_name}}.svg?color=green
   :target: https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}/raw/main/LICENSE
   :alt: License {{cookiecutter.license}}
.. image:: https://img.shields.io/pypi/v/{{cookiecutter.plugin_name}}.svg?color=green
   :target: https://pypi.org/project/{{cookiecutter.plugin_name}}
   :alt: PyPI
.. image:: https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}/workflows/tests/badge.svg
   :target: https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}/actions
   :alt: tests
.. image:: https://codecov.io/gh/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}
   :alt: codecov
.. image:: https://img.shields.io/endpoint?url=https://api.pyxu-fair.org/shields/{{cookiecutter.plugin_name}}
   :target: file:///home/joan/Documents/git/pyxu/build/html/fair/plugins/{{cookiecutter.plugin_name}}.html
   :alt: pyxu fair

{{cookiecutter.short_description}}
{{ '-' * (cookiecutter.short_description | length) }}

This `pyxu`_ plugin was generated with `Cookiecutter`_ using `pyxu`_'s `cookiecutter-pyxu`_ template.

.. comment::
   Don't miss the full getting started guide to set up your new package:
   https://pyxu-org.github.io/fair/contribute.html
   and review the Pyxu developer notes:
   https://pyxu-org.github.io/fair/dev_notes.html

Installation
------------

You can install ``{{cookiecutter.plugin_name}}`` via `pip`_:

.. code-block:: bash

   pip install {{cookiecutter.plugin_name}}

{% if cookiecutter.github_repository_url != 'provide later' %}
To install latest development version :

.. code-block:: bash

   pip install git+https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}.git
{% endif %}

Contributing
------------

Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `{{cookiecutter.license}}`_ license,
``{{cookiecutter.plugin_name}}`` is free and open source software

Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _pyxu: https://github.com/matthieumeo/pyxu
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _MIT: http://opensource.org/licenses/MIT
.. _BSD-3: http://opensource.org/licenses/BSD-3-Clause
.. _GNU GPL v3.0: http://www.gnu.org/licenses/gpl-3.0.txt
.. _GNU LGPL v3.0: http://www.gnu.org/licenses/lgpl-3.0.txt
.. _Apache Software License 2.0: http://www.apache.org/licenses/LICENSE-2.0
.. _Mozilla Public License 2.0: https://www.mozilla.org/media/MPL/2.0/index.txt
.. _cookiecutter-pyxu: https://github.com/matthieumeo/cookiecutter-pyxu
{% if cookiecutter.github_repository_url != 'provide later' %}
.. _file an issue: https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}/issues
{% endif %}
.. _tox: https://tox.readthedocs.io/en/latest/
.. _pip: https://pypi.org/project/pip/