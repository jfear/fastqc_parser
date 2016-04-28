#!/usr/bin/env python

import unittest
import yaml
import fastqc_parser


class DefaultTestCase(unittest.TestCase):
    def setup(self):
        with open('data/fastqc_data.txt', 'r') as FH:
            self.fastqc = FH.read()

        with open('data/fastqc_data.yaml', 'r') as FH:
            self.yaml = FH.read()

    def test_fastqc_parser_io_read(self):
        pass

