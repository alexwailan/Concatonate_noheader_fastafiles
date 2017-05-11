import os
from os import path
import sys
import argparse
from pathlib import Path

#Created: 11.05.17 - Alexander Wailan
print('START')
# input data
parser = argparse.ArgumentParser(
	description = 'Simply taking a multiple individual files, concatenating all files and writing the fasta header as the file basename',
	usage = 'Concatonate_files_with_headers single_files ')
parser.add_argument('single_files', nargs='*', help = 'Invidiual files as input') #Input data as multiple files in a list
options = parser.parse_args()


for infile in options.single_files:
    with open(infile) as datafile:
        for line in datafile:
            filebasename = str(os.path.splitext(infile)[0]) #using the basename of file for the fasta header
            outfile = open("output.fa", 'a')
            fastatowrite = '>' + filebasename + "\n" + line
            print(fastatowrite)
            outfile.write(fastatowrite)
