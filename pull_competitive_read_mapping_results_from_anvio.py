#!/usr/bin/env python

# Julian Damashek, Hamilton College Biology department
# jdamashe@hamilton.edu, juliandamashek@gmail.com

# Written with python 2.7.16 (not upgraded to python3 yet...)

# This script takes anvi'o output with number of reads hitting each "bin" in competitive read mapping
# and puts it in a spreadsheet so it's easy to paste into a master Excel sheet.
#
# The input is the stdout output from anvi-get-short-reads-from-bam, looped over all genomes/bins/clades etc. and all samples.
# For one genome and sample, it produces 6 lines of output that look like this:
# Input BAM file(s) ............................: 08D-hitstoallmgiimgiii.bam
# Collection ID ................................: mgiimgiii_sapelo_hits_genera
# Bin(s) .......................................: O1
# Number of splits .............................: 3926
# Output file for all short reads ..............: 08D-reads-to-O1.fasta
# Num reads stored .............................: 19485

# Usage: pull_competitive_read_mapping_results_from_anvio.py [ANVIO_OUTPUT_FILE.txt]

import sys

clades = [] #make list of clades in file

with open(str(sys.argv[1]),'r') as hits:
	for line in hits:
		if line.startswith("Bin"):
			if not(line.strip('\r\n').split(': ')[1] in clades):
				clades.append(line.strip('\r\n').split(': ')[1])
	#print(clades)
	num_clades = len(clades)

clade_lines = []
for i in range(len(clades)):
	clade_lines.append(2+6*i) #line numbers with clade information
#print(clade_lines)

hits_lines = []
for i in range(len(clades)):
	hits_lines.append(5+6*i) #line numbers with hits to clades
#print(hits_lines)
		
samps = [] #make list of samples		
with open(str(sys.argv[1]),'r') as hits:
	for line in hits:		
		if line.strip('\r\n').endswith(str(clades[0]+".fasta")):
			samps.append(line.strip('\r\n').split(': ')[1].split('-')[0])
	#print(samps)
	num_samps = len(samps)
	#print(num_samps)

samps_line = {}
for i in range(len(samps)):
	samps_line[samps[i]] = (6*num_clades*i)
#print(samps_line)	

#make and populate dictionary for each sample
#first make list of lines in file where clade names are stored (every 6 lines, starting at line 3)
samps_clades = {}
with open(str(sys.argv[1]),'r') as hits:
	lines = [line.rstrip("\r\n").replace(",","") for line in hits]
	for s in samps:
		samp_data = lines[samps_line[s]:samps_line[s]+6*num_clades] #isolate data from sample
		
		samps_clades[s] = [] #create list for each sample
		samps_clades[s].append(str(s)) #save file name as first column
		
		for i in hits_lines:
			samps_clades[s].append(str(samp_data[i].split(': ')[1])) #add counts for clades (in order) from each file
			
#create output file
with open(str(sys.argv[1].split('.txt')[0])+"_formatted.txt",'w') as outfile:
	#first write the header (clade names)
	outfile.write('\t')
	for i in range(len(clades)):
		if i != len(clades)-1:
			outfile.write(clades[i] + '\t')
		else:
			outfile.write(clades[i] + '\n')
				
	#then write the data, including sample names			
	for s in samps:
		for i in range(len(samps_clades[s])):
			if i != len(hits_lines):
				outfile.write(samps_clades[s][i] + '\t')
			else: 
				outfile.write(samps_clades[s][i] + '\n')
				
print("\n" + "HOORAY! Your exciting results have been simplified into the fancy new file \"" + str(sys.argv[1].split('.txt')[0]) + "_formatted.txt.\" Enjoy." + "\n")
