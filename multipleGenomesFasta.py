##################################
#                                #
# Last modified 03/01/2012       # 
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

def main(argv):

    if len(argv) < 2:
        print 'usage: python %s <list of files filename> outfilename ' % argv[0]
        print 'input file format: filename <tab> label, i.e.: file.fa <tab> mm9'
        sys.exit(1)

    inputfilename = argv[1]
    outputfilename = argv[2]

    outfile = open(outputfilename, 'w')

    listoflines = open(inputfilename)
    for line1 in listoflines:
        fields=line1.strip().split('\t')
        label = fields[1]
        print fields[0]
        linelist = open(fields[0])
        for line in linelist:
            if line.startswith('>'):
                outline = '>' + label + ':' + line.strip().split('>')[1] + '\n'
                outfile.write(outline)
            else:
                outfile.write(line)

    outfile.close()

if __name__ == '__main__':
    main(sys.argv)
