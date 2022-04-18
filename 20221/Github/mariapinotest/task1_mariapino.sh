#!/bin/bash
#04/02/22/Maria Jose Pino 
grep -v ">" sequence.fasta | wc | awk '{print $3-$1}'
	
