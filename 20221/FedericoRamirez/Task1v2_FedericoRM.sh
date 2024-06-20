#! /bin/bash #08/02/2022/ FedericoRamirezM/Version2
echo 'Número de nuecleotidos:'
grep -v '>' sequence.fasta | sed -e 's/\(.\)/&\n/g' | wc | awk '{print $3-$1}'
echo 'Explicación:grep -v me aisla la linea que con el código, y sed me la elimina. wc me cuenta la totalidad de lineas y caracteres como saltos de linea, así que con el awk  le restamos a la totalidad de caracteres el salto de linea'
