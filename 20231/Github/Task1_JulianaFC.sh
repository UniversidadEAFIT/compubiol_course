!/bin/bash
date 
echo "Juliana Franco Correa"
echo "Calcularemos el tamaño de nucleótidos de una seq fasta dada"
sed 1d sequence.fasta > count.fasta #Para borrar primera línea y meter en archivo nuevo. 
wc -m count.fasta #Cálculo del nucleotide size.
chmod 755 Task1_JulianaFC.sh #Para volver el archivo ejecutable, se cambian los permisos. 	

