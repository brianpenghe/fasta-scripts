##################################
#                                #
# Last modified 05/29/2010       # 
#                                #
# Georgi Marinov                 #
#                                # 
##################################

import sys
import string

def main(argv):

    if len(argv) < 3:
        print 'usage: python %s inputfilename <max piece size> <outfile prefix>' % argv[0]
        sys.exit(1)

    inputfilename = argv[1]
    MaxSequence = int(argv[2])
    outputfileprefix = argv[3]

    lineslist = open(inputfilename)

    sequenceDict={}
    i=0
    ID=''
    sequence=''
    for line in lineslist:
        if i % 100000 == 0:
            print i, 'lines processed'
        i+=1
        if line[0]=='>':
            sequenceDict[ID]=sequence
            ID=line.strip()
            sequence=''
        else:
            sequence=sequence+line.strip()

    print 'finished inputting sequence'
   
    IDList=sequenceDict.keys()
    IDList.sort()
    TotalSequence=0
    i=1
    outfile=open(outputfileprefix+'.'+str(i)+'.fa', 'w')
    for ID in IDList:
        TotalSequence=TotalSequence+len(sequenceDict[ID])
        if TotalSequence>=MaxSequence:
            outfile.close()
            TotalSequence=0
            i+=1
            outfile=open(outputfileprefix+'.'+str(i)+'.fa', 'w')
            print 'outputting file', i
            outfile.write(ID+'\n')
            outfile.write(sequenceDict[ID]+'\n')
        else:
            outfile.write(ID+'\n')
            outfile.write(sequenceDict[ID]+'\n')

if __name__ == '__main__':
    main(sys.argv)

