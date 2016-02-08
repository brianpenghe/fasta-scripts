##################################
#                                #
# Last modified 08/30/2013       # 
#                                #
# Georgi Marinov                 #
#                                # 
##################################

import sys
import string

def run():

    if len(sys.argv) < 2:
        print 'usage: python %s fasta outpurfilename' % sys.argv[0]
        sys.exit(1)

    fasta = sys.argv[1]
    outfilename = sys.argv[2]

    GenomeDict={}
    sequence=''
    inputdatafile = open(fasta)
    for line in inputdatafile:
        if line[0]=='>':
            if sequence != '':
                GenomeDict[chr] = ''.join(sequence)
            chr = line.strip().split('>')[1]
            sequence=[]
            Keep=False
            continue
        else:
            sequence.append(line.strip())
    GenomeDict[chr] = ''.join(sequence)

    outfile = open(outfilename, 'w')
    outfile.write('#chr\tlength\tGC%\n')

    chromosomes = GenomeDict.keys()
    chromosomes.sort()

    for chr in chromosomes:
        GenomeDict[chr] = GenomeDict[chr].upper()
        length = len(GenomeDict[chr])
        GC = GenomeDict[chr].count('G') + GenomeDict[chr].count('C')
        outline = chr + '\t' + str(length) + '\t' + str(GC/(0.0 + length))
        outfile.write(outline + '\n')

    outfile.close()
   
run()
