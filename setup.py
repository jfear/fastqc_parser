#!/usr/bin/env python
import os
import sys
from sequptools import setup

requirements = open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).readlines()

setup(
    name = 'fastqc_parser',
    version = '0.1',
    author = 'Justin Fear',
    author_email = 'justin.m.fear@gmail.com',
    description = 'A small utility for parsing FASTQC output',
    install_requires = requirements,
    packages=['fastqc_parser'],
    package_dir={'fastqc_parser': 'fastqc_parser'},
)
