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
        

    Automation
    ~~~~~~~~~~

    Auto format your code before pushing

    .. code-block:: bash

       tox -e run-block

       tox -e run-isort

