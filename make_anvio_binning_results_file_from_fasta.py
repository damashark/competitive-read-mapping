#!/usr/bin/env python

# Julian Damashek, Hamilton College
# jdamashe@hamilton.edu, juliandamashek@gmail.com

Usage = """,
Julian Damashek, Hamilton College

Take a fasta file and make the "*binning_results.txt" file for anvi'o.
The name of each contig (sequence) is used as the "bin" name.
This script was designed to work when mapping reads to a database containing MANY genomes (competitive read mapping),
	and this script will take the fasta file used as the mapping database to make this needed *binning_results.txt file
	to summarize mapped reads with anvi'o.
Use this for mapping to genomes but not for binning itself...

Requires python3 (last tested with 3.10.13)

Usage:
  > make_anvio_binning_results_file_from_fasta.py [fasta file]
""",

import sys
import csv
import numpy as np
from Bio import SeqIO

#user input of fasta file to count
if len(sys.argv)<1:
	print(Usage)	
else:
	ffile = sys.argv[1]

fas = open(ffile, 'r')

outfilename = ffile.split('.f')[0] + "_binning_results.txt"
outfile = open(outfilename, 'w')

counter = 0
for r in SeqIO.parse(fas, "fasta"):
	outfile.write(str(r.name) + '\t' + str(r.name.split('_c_')[0]) + '\n')
	counter += 1

fas.close()
outfile.close()

print("Saved %i sequence names to %s" % (counter, outfilename))
