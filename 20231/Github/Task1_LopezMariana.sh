#!/bin/bash
#14 de febrero 2023 - Mariana López G. 
ls -oh *sh
open Genoma_SARSCov2.txt
echo "El total de nucleotidos dentro de la secuencia es de (bp):"
#grep -v ">" Genoma_SARSCov2.txt | tr -d "\n" | wc -c
echo $1
grep -v ">" $1 | tr -d "\n" | wc -c
