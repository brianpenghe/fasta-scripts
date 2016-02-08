##################################
#                                #
# Last modified 05/25/2011       # 
#                                #
# Georgi Marinov                 #
#                                # 
##################################

import sys
import string

def run():

    if len(sys.argv) < 2:
        print 'usage: python %s inputfastafilename outfilename' % sys.argv[0]
        sys.exit(1)

    fastafilename = sys.argv[1]
    outfilename = sys.argv[2]

    outfile = open(outfilename, 'w')

    A=0.0
    C=0.0
    T=0.0
    G=0.0

    listoflines = open(fastafilename)
    for line in listoflines:
        if line.startswith('>'):
            continue
        sequence=line.strip()
        sequence=sequence.upper()
        A+=sequence.count('A')
        C+=sequence.count('C')
        T+=sequence.count('T')
        G+=sequence.count('G')

    outline='A' + '\t' + str(A/(A+C+T+G))+'\n'
    outfile.write(outline)
    outline='C' + '\t' + str(C/(A+C+T+G))+'\n'
    outfile.write(outline)
    outline='T' + '\t' + str(T/(A+C+T+G))+'\n'
    outfile.write(outline)
    outline='G' + '\t' + str(G/(A+C+T+G))+'\n'
    outfile.write(outline)

    outfile.close()

run()

