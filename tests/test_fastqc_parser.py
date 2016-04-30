#!/usr/bin/env python
""" Test Classes """

import unittest
from os.path import join, dirname
import yaml
from io import StringIO

import pandas as pd

from fastqc_parser.parser import FastQC

CURRDIR = dirname(__file__)

class DefaultTestCase(unittest.TestCase):
    def setUp(self):
        # Import string represenation
        with open(join(CURRDIR, 'data/fastqc_data.txt'), 'r') as FH:
            self.fastqcString = FH.read()

        # Import dict represenation
        with open(join(CURRDIR, 'data/fastqc_data.yaml')) as FH:
            self.fastqcDict = yaml.load(FH)

        # Build FastQC object
        self.fastqc = FastQC(join(CURRDIR, 'data/fastqc_data.txt'))

    def test_FastQC_table(self):
        # check Table
        fqtbl = self.fastqc['Overrepresented_sequences']['table'].to_dict()
        tbl = self.fastqcDict['Overrepresented_sequences']['table']
        tbl = pd.read_csv(StringIO(tbl), sep='\t').to_dict()

        self.assertDictEqual(tbl, fqtbl)

    def test_FastQC_status(self):
        self.assertEqual(self.fastqc['Overrepresented_sequences']['status'], 
                        self.fastqcDict['Overrepresented_sequences']['status'])

if __name__ == '__main__':
    unittest.main()
