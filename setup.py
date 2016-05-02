#!/usr/bin/env python
import os
import sys
from setuptools import setup

requirements = open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).readlines()

setup(
    name = 'fastqc_parser',
    version = '1.0.1beta',
    author = 'Justin Fear',
    author_email = 'justin.m.fear@gmail.com',
    description = 'A small utility for parsing FASTQC output',
    install_requires = requirements,
    packages=['fastqc_parser'],
    package_dir={'fastqc_parser': 'fastqc_parser'},
    scripts=['bin/blastFastQC'],
)
