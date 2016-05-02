##################################
#                                #
# Last modified 07/25/2014       # 
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

def main(argv):

    if len(argv) < 2:
        print 'usage: python %s inputfilename bpToKeep [-Nto A|C|T|G] [-renameIDs prefix]' % argv[0]
        print '\tUse - to specify standard input; the script will print to standard output by default'
        sys.exit(1)

    inputfilename = argv[1]
    trim = int(argv[2])
    doNto=False
    if '-Nto' in argv:
        doNto=True
        N=argv[argv.index('-Nto')+1]

    doStdInput = False
    if inputfilename == '-':
        doStdInput = True

    doRenameIDs = False
    if '-renameIDs' in argv:
        doRenameIDs = True
        RID = '>' + argv[argv.index('-renameIDs') + 1]

    if doStdInput:
        listoflines = sys.stdin
    else:
        listoflines = open(inputfilename)
    i = 0
    for line in listoflines:
        if line[0]=='>':
            i+=1
            if doRenameIDs:
                print RID + str(i)
            else:
                print line.strip()
        else:
            line = line.split('\n')[0].split('\t')[0]
            if doNto:
                print line[0:trim].replace('N',N)
            else:
                print line[0:trim]

if __name__ == '__main__':
    main(sys.argv)

