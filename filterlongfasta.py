#This script filters out transcripts long than your cutoff

import random
import sys
import string
import numpy


def main(argv):
    if len(argv) < 4:
        print 'usage: python %s fasta outfilename 300' % argv[0]
        sys.exit(1)
    fasta = argv[1]
    outfilename = argv[2]
    cutoff = int(argv[3])
    
    inputdatafile = open(fasta)
    outfile = open(outfilename, 'w')
    ID=''
    for line in inputdatafile:
        if line[0]=='>':
            if ID != '':
                sequence = ''.join(sequence)
                if len(sequence) > cutoff:
                    outfile.write('>' + ID + '\n')
                    outfile.write(sequence + '\n')
            ID = line.strip().split('>')[1]
            sequence=[]
        else:
            sequence.append(line.strip())   
    sequence = ''.join(sequence)
    if len(sequence) > cutoff:
        outfile.write('>' + ID + '\n')
        outfile.write(sequence + '\n')


if __name__ == '__main__':
    main(sys.argv)

