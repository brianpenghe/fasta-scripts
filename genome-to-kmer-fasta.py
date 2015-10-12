import random
import sys
import string
import numpy


def seqfromfile(fasta):

    inputdatafile = open(fasta)
    sequence = []
    for line in inputdatafile:
        if line[0]!='>':
            sequence.append(line.strip())
    sequence = ''.join(sequence)
    return sequence

def sequence_to_klist(sequence,kmer):
    klist = []
    for i in range(len(sequence)-kmer+1):
        klist.append(sequence[i:i+kmer])
    return klist

def output(klist, outfilename, readsNo):
    outfile = open(outfilename, 'w')
    biglist = numpy.random.choice(klist,readsNo,True)
    ID = 1
    for m in biglist:
        outfile.write('>' + str(ID) + '\n')
        outfile.write(m + '\n')
        ID = ID + 1

def run():
    if len(sys.argv) < 5:
        print 'usage: python %s fasta outfilename 30 100000' % sys.argv[0]
        sys.exit(1)
    fasta = sys.argv[1]
    outfilename = sys.argv[2]
    kmer = int(sys.argv[3])
    readsNo = int(sys.argv[4])
    output(sequence_to_klist(seqfromfile(fasta),kmer),outfilename,readsNo)

run()

