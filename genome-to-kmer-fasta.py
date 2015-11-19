import random
import sys
import string
import numpy


def output(klist, outfilename, readsNo):
    outfile = open(outfilename, 'a')
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
    
    inputdatafile = open(fasta)
    ID=''
    klist = []
    outfile = open(outfilename, 'w')
    outfile.close()
    for line in inputdatafile:
        if line[0]=='>':
            if ID != '':
                sequence = ''.join(sequence)
                for i in range(len(sequence)-kmer+1):
                    klist.append(sequence[i:i+kmer]) 
            ID = line.strip().split('>')[1]
            sequence=[]
        else:
            sequence.append(line.strip())   
    sequence = ''.join(sequence)
    for i in range(len(sequence)-kmer+1):
        klist.append(sequence[i:i+kmer]) 
    output(klist, outfilename, readsNo)

run()

