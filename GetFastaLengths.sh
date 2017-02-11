#!/bin/bash
#This script prints out the sizes of each sequence from a fasta file
#Source: Daniel E. Cook
#usage:   GetFastaLenghts.sh fastafile
cat $1 | awk '$0 ~ ">" {print c; c=0;printf substr($0,2,100) ","; } $0 !~ ">" {c+=length($0);} END { print c; }'
