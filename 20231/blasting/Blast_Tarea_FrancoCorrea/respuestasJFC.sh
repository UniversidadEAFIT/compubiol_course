¿Cuantos genes parálogos hay en el genoma? 
En el genoma no parecen haber genes parálogos, es decir, copias/duplicaciones del gen de la beta-tubulina. Esto lo podemos decir ya que, aunque los porcentajes de identidad de las secuencias son buenos teniendo en cuenta que son organismos no tan cercanamente relacionados, las secuencias son bastante cortas. De esto podemos decir que se trata de regiones que coinciden o son similares al gen de la beta tubulina más no al gen completo. También se podría explicar esta similitud ya que como son secuencias tan cortas, puede deberse a similitud por azar y no por ser “cicatriz” o residuo de un evento de duplicación del gen. 
Por otro lado, la secuencia con un 84% de identidad podría ser relacionado al gen de la beta tubulina, ya que si es de una longitud más alta. Sin embargo, al ser el único, no sería considerado como parálogo. 

¿Cumplirán la misma función? 
Los genes parálogos no suelen cumplir la misma función, ya que suelen estar expuestos a diferentes presiones y por ende la copia del gen “original” suele terminar cumpliendo otra función. 

¿Con cual trabajaría para hacer filogenética? 
Para hacer filogenética es mejor utilizar genes ortólogos, es decir, aquellos que vienen del mismo ancestro común y por ende puede ser más fácil trazar las relaciones filogenéticas y los cambios acumulados a través de eventos de especiación (en forma de mutaciones o modificaciones a la secuencia). 

¿Cómo extraer las secuencias de estos genes?
Para extraer las secuencias de los genes ortólogos, se puede tener como referencia la proteína o el CDS de la proteína de un organismo referencia que se sepa relacionado con el que se va a analizar (relacionado cercanamente puede ser más ideal), realizar un alineamiento local del genoma (idealmente en BLASTP) para encontrar los que tengan un porcentaje de identidad bastante alto (más del 95-98%) y seleccionar estos como los genes ortólogos. 
Otra forma, a partir de los resultados ya obtenidos con el blast realizado, es usar las coordenadas obtenidas (ej: LATX01002120.1) para buscar la posición específica en la secuencia de referencia. Con ayuda de una función o líneas de comando, se puede leer el archivo, llegar a la posición que indica la coordenada y copiar la secuencia (usando el tamaño indicado en los resultados ya mencionados) en un archivo nuevo. 

