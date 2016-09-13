##################################
#                                #
# Last modified 09/12/2016       #
#                                #
# Peng He                        #
#                                #
##################################

import sys
from sets import Set

try:
	import psyco
	psyco.full()
except:
	pass

def run():

    if len(sys.argv) < 2:
        print 'usage: python %s inputfilename outfilename [split]' % sys.argv[0]
        print '   this script will by default replace all intervals in fasta ID lines with an _ character so that IDs are not truncated by bowtie or other programs, otherwise it just returns the first tab-delimited field'
        sys.exit(1)

    inputfilename = sys.argv[1]
    outputfilename = sys.argv[2]

    outfile = open(outputfilename, 'w')

    lineslist = open(inputfilename)
    i=0
    for line in lineslist:
        i+=1
        if i % 10000000 == 0:
            print str(i/1000000) + 'M lines processed'
        if line.startswith('>'):
            if len(sys.argv) < 3:
			    line=line.split()[0] + '\n'
            else:
			    line=line.replace(' ','_')
        outfile.write(line)
    outfile.close()

run()
