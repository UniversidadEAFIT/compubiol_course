#!/bin/bash #080222/SebastianGomez

grep -v ">" sequence.fasta | wc | awk '{print $3-$1}'
