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

def main(argv):

    if len(argv) < 4:
        print 'usage: python %s inputfilename minpolyAlength minresiduallength outfilename [-Amismatches number] [-first number_reads]' % argv[0]
        sys.exit(1)

    inputfilename = argv[1]
    minpolyA = int(argv[2])
    minresidualread = int(argv[3])
    outputfilename = argv[4]
    Amismatches=0
    if '-Amismatches' in argv:
        Amismatches=int(argv[argv.index('-Amismatches')+1])

    polyT=''
    polyA=''
    for i in range(minpolyA):
        polyA=polyA+'A'
        polyT=polyT+'T'
    listoflines = open(inputfilename)
    lineslist = listoflines.readlines()
    first=len(lineslist)
    if '-first' in argv:
        first=2*int(argv[argv.index('-first')+1])

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

if __name__ == '__main__':
    main(sys.argv)

