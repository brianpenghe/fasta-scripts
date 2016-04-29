##################################
#                                #
# Last modified 10/31/2013       # 
#                                #
# Georgi Marinov                 #
#                                # 
##################################

import sys
import string

def main(argv):

    if len(argv) < 3:
        print 'usage: python %s fasta blockSize outputfilename [-replaceXwithN] [-replaceNames correspondence_file]' % argv[0]
        print '\t format of correspondence_file for sequence name replacement: <old name> <tab> <new name>'
        print '\t note: if the sequence name replacement option is used, sequences for which no new name is specified will be skipped'
        sys.exit(1)

    fasta = argv[1]
    blocksize = int(argv[2])
    outfilename = argv[3]

    doXtoN = False
    if '-replaceXwithN':
        doXtoN = True

    doReplaceNames = False
    if '-replaceNames':
        doReplaceNames = True
        print 'will replace sequence names'
        linelist = open(argv[argv.index('-replaceNames') + 1])
        ReplaceMentDict = {}
        for line in linelist:
            fields = line.strip().split('\t')
            if line.strip() == '':
                continue
            ReplaceMentDict[fields[0]] = fields[1]

    outfile = open(outfilename, 'w')
    
    inputdatafile = open(fasta)
    ID=''
    for line in inputdatafile:
        if line[0]=='>':
            if ID == '':
                ID = line.strip().split('>')[1]
            else:
                sequence = ''.join(sequence)
                if doXtoN:
                    sequence = sequence.replace('X','N').replace('x','n')
                if doReplaceNames:
                    if ReplaceMentDict.has_key(ID):
                        doSkip = False
                        ID = ReplaceMentDict[ID]
                    else:
                        doSkip = True
                if doSkip:
                    pass
                else:
                    outfile.write('>' + ID + '\n')
                    for i in range(0,len(sequence),blocksize):
                        outfile.write(sequence[i:min(i+blocksize, len(sequence))] + '\n')
                ID = line.strip().split('>')[1]
            sequence=[]
        else:
            sequence.append(line.strip())   
    sequence = ''.join(sequence)
    if doXtoN:
        sequence = sequence.replace('X','N').replace('x','n')
    if doReplaceNames:
        if ReplaceMentDict.has_key(ID):
            doSkip = False
            ID = ReplaceMentDict[ID]
        else:
            doSkip = True
    if doSkip:
        pass
    else:
        outfile.write('>' + ID + '\n')
        for i in range(0,len(sequence),blocksize):
            outfile.write(sequence[i:min(i+blocksize, len(sequence))] + '\n')
   
if __name__ == '__main__':
    main(sys.argv)
