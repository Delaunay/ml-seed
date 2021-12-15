#!/usr/bin/env python
from setuptools import setup, find_packages


if __name__ == "__main__":
    setup(
        name="{{cookiecutter.project_name}}",
        version="0.0.0",
        description="{{cookiecutter.author}}",
        author="seedauthor",
        packages=find_packages(),
        setup_requires=["setuptools"],
    )
