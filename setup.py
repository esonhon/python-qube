#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_packages
import sys
import warnings

dynamic_requires = []

version = 0.1

setup(
    name='qube',
    version=0.2,
    author='Matthew Garrett',
    author_email='mjg59@srcf.ucam.org',
    url='http://github.com/mjg59/python-qube',
    packages=find_packages(),
    scripts=[],
    description='Python API for controlling Qube LED bulbs',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    zip_safe=False,
)
