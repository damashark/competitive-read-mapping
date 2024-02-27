#!/usr/bin/env python

# Julian Damashek
# Hamilton College
# jdamashe@hamilton.edu, juliandamashek@gmail.com
#
# Parse JSON file (output from mOTUlize.py) into a table
# parse_mOTUliser_json_output.py [file from mOTUlize.py] [name for output files, no extensions]
# For example, $ parse_mOTUliser_json_output.py Thaum_mOTUlize_output.txt Thaum_mOTUs 
#		produces the files "Thaum_mOTUs_info.txt" and "Thaum_mOTUs_table.txt"

import sys
import json

with open(str(sys.argv[1]),'r') as infile: 
	with open(str(sys.argv[2]+'_info.txt'), 'w') as outfile: #file to save all info from mOTUs
		with open(str(sys.argv[2]+'_table.txt'), 'w') as outfile2: #file to save # and names of genomes in each mOTU as table
			outfile2.write('mOTU'+'\t'+'Num_Genomes'+'\t'+'Genome_Names'+'\n') #header for output table
			
			mOTU_dict = json.loads(infile.read()) #read in mOTUlize.py output file to python format (dictionary)
			
			for key in mOTU_dict:
				#first, save all mOTUlizer.py data in *_info.txt file
				outfile.write("\n--------------------\n"+key+"\n--------------------\n")
				for k in mOTU_dict[key]:
					outfile.write(str(k)+": "+str(mOTU_dict[key][k])+"\n")
					#print(k, mOTU_dict[key][k]) #print data from JSON dictionary
				
				#then, save number and identity of genomes only from each mOTU
				mOTU_num = mOTU_dict[key]['nb_genomes'] #count number of genomes in mOTU
				
				outfile2.write(str(key)+'\t'+str(mOTU_num)+'\t') #save mOTU name and number of genomes
				
				if mOTU_num==1:
					outfile2.write(str(mOTU_dict[key]['genomes'][0]['name'])+'\n')
				else:
					for g in range(mOTU_num):
						if g<mOTU_num-1:
							outfile2.write(str(mOTU_dict[key]['genomes'][g]['name'])+',')
						else:
							outfile2.write(str(mOTU_dict[key]['genomes'][g]['name'])+'\n')
					#outfile2.write('\n')

