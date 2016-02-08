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

def run():

    if len(sys.argv) < 2:
        print 'usage: python %s inputfilename bpToKeep [-Nto A|C|T|G] [-renameIDs prefix]' % sys.argv[0]
        print '\tUse - to specify standard input; the script will print to standard output by default'
        sys.exit(1)

    inputfilename = sys.argv[1]
    trim = int(sys.argv[2])
    doNto=False
    if '-Nto' in sys.argv:
        doNto=True
        N=sys.argv[sys.argv.index('-Nto')+1]

    doStdInput = False
    if inputfilename == '-':
        doStdInput = True

    doRenameIDs = False
    if '-renameIDs' in sys.argv:
        doRenameIDs = True
        RID = '>' + sys.argv[sys.argv.index('-renameIDs') + 1]

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

run()

