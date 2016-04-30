#!/usr/bin/env python
""" Files need for FASTQC summary files. """
import sys
import re

if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

import pandas as pd


MODULES = ['Basic_Statistics',
           'Per_base_sequence_quality',
           'Per_tile_sequence_quality',
           'Per_sequence_quality_scores',
           'Per_base_sequence_content',
           'Per_sequence_GC_content',
           'Per_base_N_content',
           'Sequence_Length_Distribution',
           'Sequence_Duplication_Levels',
           'Overrepresented_sequences',
           'Adapter_Content',
           'Kmer_Content']


PATTERN = """##FastQC\t[0-9\.]+
>>Basic Statistics\t(?P<Basic_Statistics_status>\w+)
#(?P<Basic_Statistics_table>.*?)
>>END_MODULE
>>Per base sequence quality\t(?P<Per_base_sequence_quality_status>\w+)
#(?P<Per_base_sequence_quality_table>.*?)
>>END_MODULE
>>Per tile sequence quality\t(?P<Per_tile_sequence_quality_status>\w+)
#(?P<Per_tile_sequence_quality_table>.*?)
>>END_MODULE
>>Per sequence quality scores\t(?P<Per_sequence_quality_scores_status>\w+)
#(?P<Per_sequence_quality_scores_table>.*?)
>>END_MODULE
>>Per base sequence content\t(?P<Per_base_sequence_content_status>\w+)
#(?P<Per_base_sequence_content_table>.*?)
>>END_MODULE
>>Per sequence GC content\t(?P<Per_sequence_GC_content_status>\w+)
#(?P<Per_sequence_GC_content_table>.*?)
>>END_MODULE
>>Per base N content\t(?P<Per_base_N_content_status>\w+)
#(?P<Per_base_N_content_table>.*?)
>>END_MODULE
>>Sequence Length Distribution\t(?P<Sequence_Length_Distribution_status>\w+)
#(?P<Sequence_Length_Distribution_table>.*?)
>>END_MODULE
>>Sequence Duplication Levels\t(?P<Sequence_Duplication_Levels_status>\w+)
#Total Deduplicated Percentage\t(?P<Sequence_Duplication_Levels_dedup>[\d\.]+)
#(?P<Sequence_Duplication_Levels_table>.*?)
>>END_MODULE
>>Overrepresented sequences\t(?P<Overrepresented_sequences_status>\w+)
#(?P<Overrepresented_sequences_table>.*?)
>>END_MODULE
>>Adapter Content\t(?P<Adapter_Content_status>\w+)
#(?P<Adapter_Content_table>.*?)
>>END_MODULE
>>Kmer Content\t(?P<Kmer_Content_status>\w+)
#(?P<Kmer_Content_table>.*?)
>>END_MODULE
"""

class FastQC(object):
    """ Class to hold the FASTQC Summary Data """
    def __init__(self, fname):
        with open(fname, 'r') as fh:
            raw = fh.read()
        pattern = re.compile(PATTERN, re.DOTALL)
        mDict = re.match(pattern, raw).groupdict()
        
        self._modules = dict()
        for module in MODULES:
            self._modules[module] = self.store(module, mDict)

    def store(self, module, mDict):
        d = dict()
        d['status'] = mDict[module + '_status']
        d['table'] = self.makeTable(mDict[module + '_table'])
        if module == 'Sequence_Duplication_Levels':
            d['dedup'] = mDict[module + '_dedup']
        return d

    def makeTable(self, tbl):
        """ """
        return pd.read_csv(StringIO(tbl), sep='\t')

    def __getitem__(self, name):
        return self._modules.get(name, None)

    def __str__(self):
        return str(self._modules)


