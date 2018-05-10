#!/usr/bin/env python

# specific imports
from setuptools import setup

# parse requirments
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# install
setup(
    name='python_package',
    version='1.0',
    install_requires=requirements,
    packages=[
        'foolib'
    ]
)

