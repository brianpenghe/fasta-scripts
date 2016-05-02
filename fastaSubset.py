##################################
#                                #
# Last modified 11/04/2012       # 
#                                #
# Georgi Marinov                 #
#                                # 
##################################
# This script takes out fastasubset based on > ID list
import sys
import string

def main(argv):

    if len(argv) < 4:
        print 'usage: python %s wanted fieldID fasta outputfilename' % argv[0]
        sys.exit(1)

    wanted = argv[1]
    fieldID = int(argv[2])
    fasta = argv[3]
    outfilename = argv[4]

    WantedDict = {}
    linelist = open(wanted)
    for line in linelist:
        fields = line.strip().split('\t')
        WantedDict[fields[fieldID]] = 1

    outfile = open(outfilename, 'w')
    
    inputdatafile = open(fasta)
    Keep = False
    for line in inputdatafile:
        if line[0]=='>':
            ID = line.strip().split('>')[1]
            if WantedDict.has_key(ID):
                Keep = True
            else:
                Keep = False
        else:
            pass
        if Keep:
            outfile.write(line)   

    outfile.close()
   
if __name__ == '__main__':
    main(sys.argv)
