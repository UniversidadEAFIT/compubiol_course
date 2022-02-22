#!/bin/bash
#06022022

#calculate the number of nucleotides in a sequence

grep -v ">" sequence.fasta | awk '{s+=length($1)}END{print s}'
