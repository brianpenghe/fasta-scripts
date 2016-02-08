##################################
#                                #
# Last modified 09/06/2011       # 
#                                #
# Georgi Marinov                 #
#                                # 
##################################

import sys
import string

def run():

    if len(sys.argv) < 3:
        print 'usage: python %s chrom.sizes windowSize outfilename' % sys.argv[0]
        sys.exit(1)

    chromsizes = sys.argv[1]
    window=int(sys.argv[2])
    outfilename = sys.argv[3]

    outfile = open(outfilename, 'w')

    listoflines = open(chromsizes)
    chrLengthDict={}
    for line in listoflines:
        fields = line.strip().split('\t')
        chr = fields[0]
        chrsize = int(fields[1])
        i = 0
        while i <= chrsize:
            outline = chr + '\t' + str(i) + '\t' + str(i+window)
            outfile.write(outline + '\n')
            i+=window

    outfile.close()

run()

