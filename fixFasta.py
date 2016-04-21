##################################
#                                #
# Last modified 11/28/2011       # 
#                                #
# Georgi Marinov                 #
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
        print 'usage: python %s inputfilename outfilename' % sys.argv[0]
        print '   this script will replace all intervals in fasta ID lines with an _ character so that IDs are not truncated by bowtie or other programs' 
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
            #line=line.replace(' ','_')
			line=line.split()[0] + '\n'
        outfile.write(line)
    outfile.close()

run()

