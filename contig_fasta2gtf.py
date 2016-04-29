##################################
#                                #
# Last modified 11/08/2010       # 
#                                #
# Georgi Marinov                 #
#                                # 
##################################

import sys
import string

def main(argv):

    if len(argv) < 2:
        print 'usage: python %s <contig fasta file> <output gtf file name> ' % argv[0]
        sys.exit(1)
    
    inputfilename = argv[1]
    outfilename = argv[2]

    outfile = open(outfilename, 'w')

    linelist = open(inputfilename)
    
    NotFirst=False
    First=True
    for line in linelist:
       if line.startswith('>'):
           if First:
               header = line.strip().split('>')[1].split(' ')[0]
               sequence=''
               First=False
               NotFirst=True
               continue
           else:
               pass
           if NotFirst:
               outline=header+'\t'+'Contigs'+'\texon\t1\t'+str(len(sequence))+'\t.\t.\t.\t'+'gene_id "'+header+'"; transcript_id "'+header+'"; exon_number "1"; gene_name "'+header+'";'
               outfile.write(outline+'\n')
           header = line.strip().split('>')[1].split(' ')[0]
           sequence=''
       else:
           seq=line.strip()
           sequence=sequence+seq
   
if __name__ == '__main__':
    main(sys.argv)
