##################################
#                                #
# Last modified 03/21/2014       # 
#                                #
# Georgi Marinov                 #
#                                # 
##################################

import sys
import string

def run():

    if len(sys.argv) < 4:
        print 'usage: python %s fasta minLength blocksize outputfilename' % sys.argv[0]
        sys.exit(1)

    fasta = sys.argv[1]
    minLenSequence = int(sys.argv[2])
    blocksize = int(sys.argv[3])
    outfilename = sys.argv[4]

    outfile = open(outfilename, 'w')
    
    inputdatafile = open(fasta)
    ID=''
    for line in inputdatafile:
        if line[0]=='>':
            if ID == '':
                ID = line.strip().split('>')[1]
            else:
                sequence = ''.join(sequence)
                if len(sequence) < minLenSequence:
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
    if len(sequence) < minLenSequence:
        pass
    else:
        outfile.write('>' + ID + '\n')
        for i in range(0,len(sequence),blocksize):
            outfile.write(sequence[i:min(i+blocksize, len(sequence))] + '\n')
   
run()
