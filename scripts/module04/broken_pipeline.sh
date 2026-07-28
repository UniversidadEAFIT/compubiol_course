#!/usr/bin/env bash
# Script deliberadamente defectuoso para la actividad C4.
input=$1
output=results/stats.tsv
for f in $input/*.fasta; do
  grep -c '^>' $f > $output
done
echo terminado
