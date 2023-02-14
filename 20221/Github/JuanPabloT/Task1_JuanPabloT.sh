#!/bin/bash
#8 febrero/Juan Pablo Tobon

\#!/bin/bash 

echo "enter the file"

read file  

sed "1d"  $file > tmp.txt 

tr -d '\n' < tmp.txt > tmpA.txt

echo "The number of nucleotides is:"

wc -m tmpA.txt | tr -dc '0-9'

rm tmp.txt
rm tmpA.txt
