
#!/bin/bash

echo "BIENVENIDO AL CONTADOR DE NUCLEOTIDOS EN BASH"
echo ""
echo "HECHO POR JUAN JOSE PICON COSSIO"
echo ""

# contador
COUNT=0

# Iteramos pero primero borramos los espacios en blanco
# Asi evitar que itere en los headers de los genes.
for LINE in $(cat $1| tr -d " ")

do
CHAR=`echo "$LINE" | cut -c 1` # tomamos el primer byte del texto que vendria siendo el primer caracter
if test "$CHAR" = ">"; then
echo "$COUNT"
echo ""
echo "$LINE"
COUNT=0

else
# Eliminamos character de nueva linea y contamos
CHAR_LINE=`echo "$LINE" | tr -d "\n" | wc -m`
COUNT=$((COUNT + CHAR_LINE))
fi
done
echo "$COUNT"
