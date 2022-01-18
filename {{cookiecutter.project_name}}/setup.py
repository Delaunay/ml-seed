#!/usr/bin/env python
from setuptools import setup, find_packages


if __name__ == "__main__":
    setup(
        name="seedproject",
        version="0.0.0",
<<<<<<< HEAD
        description="seeddescription",
        author="seedauthor",
=======
        description="{{cookiecutter.description}}",
        author="{{cookiecutter.author}}",
>>>>>>> 5654791815516697995be3f7358d7d5f38515013
        packages=find_packages(),
        setup_requires=["setuptools"],
    )
