##################################
#                                #
# Last modified 05/23/2011       # 
#                                #
# Georgi Marinov                 #
#                                # 
##################################

import sys
import string
import random

try:
	import psyco
	psyco.full()
except:
	pass

def main(argv):

    if len(argv) < 2:
        print 'usage: python %s inputfilename outfilename' % argv[0]
        sys.exit(1)

    inputfilename = argv[1]
    outputfilename = argv[2]

    outfile = open(outputfilename, 'w')

    listoflines = open(inputfilename)
    for line in listoflines:
        if line.startswith('>'):
            outfile.write(line)
        else:
            sequence=line.strip()
            s=list(sequence)
            random.shuffle(s)
            shuffled=''.join(s)
            outfile.write(shuffled.upper()+'\n')
    outfile.close()

if __name__ == '__main__':
    main(sys.argv)

