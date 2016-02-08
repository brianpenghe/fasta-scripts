##################################
#                                #
# Last modified 11/28/2009         # 
#                                #
# Georgi Marinov                 #
#                                # 
##################################

import sys

try:
	import psyco
	psyco.full()
except:
	pass

def getComplementarySequence(preliminarysequence):
    
    DNA = {'A':'T','T':'A','G':'C','C':'G','N':'N'}
    sequence=''
    for i in range(len(preliminarysequence)):
        sequence=sequence+DNA[preliminarysequence[len(preliminarysequence)-i-1]]
    return sequence

def run():

    if len(sys.argv) < 4:
        print 'usage: python %s inputfilename minpolyAlength minresiduallength outfilename [-Amismatches number] [-first number_reads]' % sys.argv[0]
        sys.exit(1)

    inputfilename = sys.argv[1]
    minpolyA = int(sys.argv[2])
    minresidualread = int(sys.argv[3])
    outputfilename = sys.argv[4]
    Amismatches=0
    if '-Amismatches' in sys.argv:
        Amismatches=int(sys.argv[sys.argv.index('-Amismatches')+1])

    polyT=''
    polyA=''
    for i in range(minpolyA):
        polyA=polyA+'A'
        polyT=polyT+'T'
    listoflines = open(inputfilename)
    lineslist = listoflines.readlines()
    first=len(lineslist)
    if '-first' in sys.argv:
        first=2*int(sys.argv[sys.argv.index('-first')+1])

    outfile = open(outputfilename, 'w')
    i=0
    Atailedreads=0
    for line in lineslist[0:first]:
        if line[0]=='>':
            continue
        if i % 100000 == 0:
            print i
        i+=1
        read=line.strip()
        if read.startswith(polyT):
            read=getComplementarySequence(read)
        if read.endswith(polyA):
            Astart=read.find(polyA)
            if Astart<minresidualread:
                continue
            else:
                nAs=read[Astart:len(read)].count('A')
                if nAs < len(read)-Astart-Amismatches:
                    continue
                else:
                    trimmedread=read[0:Astart]
                    outfile.write(lineslist[lineslist.index(line)-1])
                    outfile.write(trimmedread+'\n')
                    Atailedreads+=1
        else:
            continue            
    print Atailedreads, 'reads with an A-tail found'
    outfile.close()

run()

