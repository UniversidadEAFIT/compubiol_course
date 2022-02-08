#!/bin/bash #7-02-22/Mariana_Echeverri

grep -v ">" sequence.fasta | wc | awk '{print $3-$1}' 

 

