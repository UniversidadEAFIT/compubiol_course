!/bin/bash
12Feb/Andrea Carrillo
#nombre archivo secuencia
secuencia=sequence.fasta
#contar nucleotidos
nucleotidos=$(grep -v ">" $secuencia | tr -d "\n" | wc -m)
#imprimir resultado
echo "La secuencia de ADN tiene $nucleotidos nucleotidos."
