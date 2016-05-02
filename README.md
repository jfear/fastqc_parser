# fastqc_parser

This is a parsing package for FASTQC. This package provides a python class for
handling FASTQC output data, it also includes a script to blast sequences identified
as overrepresented by FASTQC.

## Install
This program has been tested with python3+, but may work work with python2.7+.
The blastFastQC script requires Biopython. If you have trouble installing
Biopython I would suggest using [minconda](http://conda.pydata.org/miniconda.html).

To install run the following:
> pip install git+https://github.com/jfear/fastqc_parser

To run the blast program you will also need NCBI blast installed along with the nt database.

## blastFastQC

> blastFastQC --input ./fastqc_data.txt --output ./fastqc_overrepsented_blast.csv

To see additional options:

> blastFastQC -h
