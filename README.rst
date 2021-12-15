Machine Learning Seed Repository
===============================

Features
~~~~~~~~

* Sphinx doc generation

  * Read the docs ready

* Github CI

  * Test Coverage + Doctest
  * black formating
  * pylint
  * isort
  * docs8

* slurm launch script

* pip installable

Get started
~~~~~~~~~~~

.. code-block:: bash

   pip install cookiecutter
   cookiecutter https://github.com/Delaunay/ml-seed
    

Example
~~~~~~~

`slurm-examples <https://github.com/Delaunay/slurm-examples>`_ is an example of reposity than can be generated
using this cookie cutter.

Automation
~~~~~~~~~~

Auto format your code before pushing

.. code-block:: bash

   tox -e run-block

   tox -e run-isort

Contributing
~~~~~~~~~~~~

To update this template you should modify `slurm-examples <https://github.com/Delaunay/slurm-examples>`_
the change will automatically be ported to the cookiecutter version

To update the documentation of this template you should fork this project.

