##################################
#                                #
# Last modified 09/17/2014       # 
#                                #
# Georgi Marinov                 #
#                                # 
##################################

import sys
import string

def getReverseComplement(preliminarysequence):
    
    DNA = {'A':'T','T':'A','G':'C','C':'G','N':'N','a':'t','t':'a','g':'c','c':'g','n':'n'}
    sequence=''
    for j in range(len(preliminarysequence)):
        sequence=sequence+DNA[preliminarysequence[len(preliminarysequence)-j-1]]
    return sequence

def main(argv):

    if len(argv) < 3:
        print 'usage: python %s fasta inputfilename outpurfilename [-seqradius bp] [-usepeak fieldID|bed] [-chrfield fieldID] [-first number] [-name fieldID(s)] [-strand fieldID] [-narrowPeak]' % argv[0]
        print '\tby default the forward strand is outputted' 
        print '\tdefault sequence names format is chr:start-stop format' 
        print '\tuse the -name option if you want to change the sequence output format - the content of the fields indicated will be used and the sequence name construct from those separated by "::"' 
        sys.exit(1)

    fieldID=1
    if '-chrfield' in argv:
        fieldID = int(argv[argv.index('-chrfield') + 1])
    
    doName = False
    if '-name' in argv:
        doName = True
        fields = argv[argv.index('-name') + 1].split(',')
        nameFields=[]
        for ID in fields:
            nameFields.append(int(ID))

    doStrand = False
    if '-strand' in argv:
        doStrand = True
        strandField = int(argv[argv.index('-strand') + 1])

    doPeak = False
    if '-usepeak' in argv:
        doPeak = True
        doBed = False
        if argv[argv.index('-usepeak') + 1] == 'bed':
            doBed = True
        else:
            peakFieldID = int(argv[argv.index('-usepeak') + 1])
    if '-seqradius' in argv:
        radius = int(argv[argv.index('-seqradius') + 1])

    doNarrowPeak=False
    if '-narrowPeak' in argv:
        doNarrowPeak=True
        doPeak=True

    fasta = argv[1]
    inputfilename = argv[2]
    outfilename = argv[3]

    outfile = open(outfilename, 'w')
    
    RegionDict={}

    doFirst=False   
    if '-first' in argv: 
        doFirst=True
        firstN = int(argv[argv.index('-first') + 1])

    i=0
    inputdatafile = open(inputfilename)
    for line in inputdatafile:
        i+=1
        if doFirst and i >= firstN+1:
            continue
        if line[0]=='#':
            continue
        if 'random' in line:
            continue
        fields = line.strip().split('\t')
        if doPeak:
            if doNarrowPeak:
                if len(fields) < 9:
                    continue
                chr = fields[0]
                peak = int(fields[1]) + int(fields[9])
                start = peak-radius
                stop = peak+radius
            else:
                if doBed:
                    peak = int((int(fields[fieldID + 1]) + int(fields[fieldID + 2]))/2.0)
                else:
                    peak = int(fields[peakFieldID].strip())
                chr = fields[fieldID].strip()
                start = peak-radius
                stop = peak+radius
        else:
            chr = fields[fieldID].strip()
            start = int(fields[fieldID+1].strip())
            stop = int(fields[fieldID+2].strip())
        if RegionDict.has_key(chr):
            pass
        else:
            RegionDict[chr]={}
        sense = '+'
        if doStrand:
            strand=fields[strandField]
            if strand == 'F' or strand == '+':
                sense='+'
            if strand == 'R' or strand == '-':
                sense='+'
        if doName:
            ID = '>'
            for f in nameFields:
                ID = ID + fields[f] + '::'
            ID = ID[0:-2]
        else:
            ID = '>'+chr+':'+str(start)+'-'+str(stop)
        RegionDict[chr][ID]=(chr,start,stop,sense)

#    print RegionDict

    inputdatafile = open(fasta)
    Keep=False
    for line in inputdatafile:
        if line[0]=='>':
            if Keep:
                sequence = ''.join(sequence)
                for ID in RegionDict[chr].keys():
                    outfile.write(ID + '\n')
                    (chr,start,stop,sense) = RegionDict[chr][ID]
                    regionSequence = sequence[start:stop]
                    if sense == '-':
                        regionSequence  = getReverseComplement(regionSequence)
                    outfile.write(regionSequence + '\n')
            chr = line.strip().split('>')[1]
            print chr
            sequence=[]
            Keep=False
            if RegionDict.has_key(chr):
                Keep=True
            continue
        else:
            sequence.append(line.strip())
    sequence = ''.join(sequence)
    if RegionDict.has_key(chr):
        for ID in RegionDict[chr].keys():
            outfile.write(ID + '\n')
            (chr,start,stop,sense) = RegionDict[chr][ID]
            regionSequence = sequence[start:stop]
            if sense == '-':
                regionSequence = getReverseComplement(regionSequence)
            outfile.write(regionSequence + '\n')
   
if __name__ == '__main__':
    main(sys.argv)
