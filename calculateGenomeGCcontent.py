##################################
#                                #
# Last modified 6/9/2009         # 
#                                #
# Georgi Marinov                 #
#                                # 
##################################

import sys
import os
import string

def run():

    if len(sys.argv) < 3:
        print 'usage: python %s genome_directory outfilename' % sys.argv[0]
        sys.exit(1)

    directory = sys.argv[1]
    outfilename = sys.argv[2]

    outfile = open(outfilename, 'w')

    files = os.listdir(directory)
    for filename in files:
        length=0.0
        GC=0.0
        file=open(direcotry+'/'+filename)
        listlines=file.readlines()
        for line in listlines:
            line=string.upper(line.strip())
            length=length+len(line)
            G=line.split('G')
            C=line.split('C')
            GC=GC+len(G)-1+len(C)-1
        print 'chromosomelength= ', length
        k=GC/length
        print 'GC%= ', k
        outline=filename+': GC%= '+str(k) + '\n'
        outfile.write('outline')

    outfile.close()

run()

