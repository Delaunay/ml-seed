#!/usr/bin/env python
from setuptools import setup, find_packages


if __name__ == "__main__":
    setup(
        name="{{cookiecutter.project_name}}",
        version="0.0.0",
        description="{{cookiecutter.description}}",
        author="{{cookiecutter.author}}",
        packages=find_packages(),
        setup_requires=["setuptools"],
    )
