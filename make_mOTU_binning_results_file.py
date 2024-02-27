#!/usr/bin/env python

# Julian Damashek
# Hamilton College
# jdamashe@hamilton.edu, juliandamashek@gmail.com
#
# Take the output table of mOTUs from mOTUlizer_parse_json.py script and
#	make the corresponding binning_results.txt file for anvi'o.
# Input is a list of contigs (one per line), mOTUs table file, and a prefix for naming the binning_results_mOTUs.txt output file.
# make_mOTU_binning_results_file.py [contigs.txt file] [mOTUs _table.txt file] [prefix]
#
# Requires python3 (last tested with 3.10.13)
#

import sys
import re

contigs = [] #list for genome names
mOTU_id = {} #dictionary for mOTU identity for each genome

with open(str(sys.argv[3]+"_binning_results_mOTUs.txt"),'w') as outfile: #make output file
	for line in open(str(sys.argv[1]),'r'): #loop over contig names
		line=line.strip('\r\n')
		contigs.append(line)
		
	counter = 0	

	for contig in contigs:
		contig_name=contig.split('_c_')[0]
		for line in open(str(sys.argv[2]),'r'): #loop over lines in mOTUlize.py output file
			line_elements=line.strip('\r\n').split('\t')
			if contig_name in line_elements[2].split(','):
				mOTU_id[contig]=line_elements[0]
				outfile.write(str(contig)+'\t'+str(mOTU_id[contig])+'\n')
				counter += 1
		if counter == 0:
			print(("Contigs not added to binning results file: "+str(contig_name)))
					
print((str("mOTU IDs saved to ")+str(sys.argv[3]+"_binning_results_mOTUs.txt")+". Yippee!"))					
