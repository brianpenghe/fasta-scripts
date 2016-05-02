##################################
#                                #
# Last modified 09/06/2011       # 
#                                #
# Georgi Marinov                 #
#                                # 
##################################

import sys
import string

def main(argv):

    if len(argv) < 3:
        print 'usage: python %s chrom.sizes windowSize outfilename' % argv[0]
        sys.exit(1)

    chromsizes = argv[1]
    window=int(argv[2])
    outfilename = argv[3]

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

if __name__ == '__main__':
    main(sys.argv)

