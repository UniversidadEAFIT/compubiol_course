Hola,

Adjunto mi tarea.
Aquí está el ejecutable

#!/bin/bash

echo "Inserte el nombre del archivo"
read file

sed '1d' $file > tmp.txt 

tr -d '\n' < tmp.txt > tmpA.txt

echo "El numero de nucleotidos es"

wc -m tmpA.txt | tr -dc '0-9'

rm tmp.txt
rm tmpA.txt

Saludos, 
Natalia
