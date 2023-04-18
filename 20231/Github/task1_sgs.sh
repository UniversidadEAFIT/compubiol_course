#!/bin/bash
#14 de febrero 2023 - Santiago Giraldo. 
ls -oh *sh
open sequence.txt
echo "El total de nucleotidos dentro de la secuencia es de (bp):"
echo $1
grep -v ">" $1 | tr -d "\n" | wc -c
