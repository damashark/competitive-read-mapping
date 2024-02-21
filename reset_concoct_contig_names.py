#!/usr/bin/env python

# Julian Damashek, Hamilton College
# jdamashe@hamilton.edu, juliandamashek@gmail.com

# Takes the *concoct_scaffolds2bin.tsv file for DAS-Tool input coming from CONCOCT.
# Changes the contig names back to their original names so that DAS-Tool is happy.

# Note, this still runs in python2 (2.7.16 was the last test). Hasn't been updated to python3 yet...

# Usage: reset_concoct_contig_names.py [*concoct_scaffolds2bin.tsv]

import sys

line_list = []

with open(str(sys.argv[1]), 'r') as concoct_file:
	with open(str(sys.argv[1].split('.tsv')[0]+'_fixed.tsv'), 'w') as out_file:
		for line in concoct_file:
			if not line.startswith('contig_id'): 
				contig = line.strip('\r\n').split('.')[0]
				sample_name = contig.split('_0000000')[0]
				bin_id = line.strip('\r\n').split('\t')[1]
				
				if not bin_id.startswith(sample_name):
					bin_id_fixed = str(sample_name) + '_' + str(bin_id)
				else:
					bin_id_fixed = str(bin_id)
				new_line = str(contig) + '\t' + bin_id_fixed + '\n'
				
				if new_line not in line_list:
					line_list.append(new_line)
					out_file.write(new_line)
			
