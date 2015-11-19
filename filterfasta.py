import random
import sys
import string
import numpy


def run():
    if len(sys.argv) < 4:
        print 'usage: python %s fasta outfilename 300' % sys.argv[0]
        sys.exit(1)
    fasta = sys.argv[1]
    outfilename = sys.argv[2]
    cutoff = int(sys.argv[3])
    
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


run()

