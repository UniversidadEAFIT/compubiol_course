Entendimiento de las relaciones filogenética de los microorganismos
reductores y oxidadores de sulfuro
================
María José Pino & Amalia Munera
18/4/2022

## Introducción

La idea de que la vida se restringe a un rango estrecho de temperatura,
presión, acidez, alcalinidad, salinidad, u otras características
ambientales ha sido desmentida desde que los microbiólogos empezaron a
buscar microorganismos interesantes y otras formas de vida, y lograron
aislarlos no sólo de ambientes moderados. La naturaleza contiene
múltiples ambientes extremos, como las aguas termales o ácidas, lagos
salinos, desiertos, lagos alcalinos y el fondo del océano.

Los descubrimientos progresivos en los últimos años en ambientes
controlados por estas y otras condiciones extremas como la radiación, la
hiperacidez y la salinidad, la contaminación intensa o la muy baja
disponibilidad de nutrientes, ha revelado que los organismos
extremófilos son abundantes y diversos.

Además, los seres humanos siempre hemos sido muy antropocéntricos en
nuestro pensamiento y nuestra concepción de la vida tanto en la tierra
como en el universo. Tenemos como tarea conservar los organismos
extremófilos en beneficio de la humanidad y el ecosistema, ya que
encontrar nuevas formas de vida contribuirá al desarrollo de la ciencia
básica y nuevas tecnologías.

## Pregunta Investigación

¿Las diferencias metabólicas de los microorganismos partícipes en el
ciclo del sulfuro están evidenciadas en sus relaciones filogenéticas?

## Metodología

Con base en la literatura se seleccionaron un total de 17 géneros y una
especie de microorganismos reductores y oxidadores de sulfuro (13
reductores y 5 oxidadores). Para cada uno de estos organismos, se
descargó la secuencia del gen 16s por medio de la plataforma de NCBI. A
continuación los números de acceso para cada uno:

| Organismo               | Número de acceso |
|-------------------------|------------------|
| Thiobacillus sp         | X97534.1         |
| Achromatium sp          | MN990460.1       |
| Begiatoa sp             | AF064543.1       |
| Thiovulum sp            | AH003133.2       |
| Sulfurimonas sp         | MF563476.1       |
| Geovibrio sp            | KJ877729.1       |
| Dethiosulfovibrio sp    | KT799836.2       |
| Aquifex sp              | KY483456.1       |
| Ammonifex sp            | JX073595.1       |
| Desulfitobacterium sp   | X81032.1         |
| Shewanella sp           | OM319583.1       |
| Sulfurospirillum sp     | LC379579.1       |
| Wolinella sp            | DQ017139.1       |
| Geobacter sp            | MW063652.1       |
| Desulfurella sp         | MT022217.1       |
| Pelobacter sp           | AJ296616.1       |
| Desulfofuromonas sp     | M80618.1         |
| *Pseudomonas mendocina* | L28162.1         |

Para obtener cada uno de los organismos se descargó el archivo FASTA con
la secuencia de 16S y fueron almacenadas en una misma carpeta. Teniendo
todas las secuencias, se corrió el comando para reunirlas en un mismo
archivo.

     cat *.fasta > sequence_16s.fa

Posteriormente para poder realizar los análisis filogenéticos se
corrieron los siguientes comandos para así instalar los paquetes
necesarios.

    conda install -c bioconda raxml
    conda install -c bioconda modeltest-ng
    conda install -c bioconda raxml-ng

Una vez se terminó la instalación de los paquetes, se comenzó con el
alineamiento de las secuencias, esto se realizó utilizando el paquete
mafft de la siguiente forma:

    mafft --thread 4 sequence_16s.fa > 16s_alignment.fa

Posteriormente se utilizó el paquete modeltest-ng para poder observar el
modelo más propicio para realiar el análisis filogenético, de acuerdo
con los resultados se decidió utilizar el modelo GTR+G4

    modeltest-ng -i 16s_alignment.fa -d nt -o model_16s.txt

    Partition 1/1:
                             Model         Score        Weight
    ----------------------------------------------------------
           BIC             TIM3+G4    24923.6707        0.6414
           AIC              GTR+G4    24697.0829        0.8751
          AICc              GTR+G4    24699.0829        0.8751

Se coninuó obteniendo el primer análisis filogenético, este se obtuvo
por medio del paquete raxml-ng que nos permite obtener árboles a partir
de *Maximum Likelihood*. Para este las únicas indicaciones que se dieron
fue el modelo que se debe usar.

    raxml-ng --msa 16s_alignment.fa --model GTR+G4

A continuación, se realizó un segundo análisis filogenético por *Maximum
Likelihood* con el paquete raxmlHPC. En este se utilizó un mayor número
de especificaciones mostradas a continuación

    raxmlHPC -f a -x 1000 -#100 -k -m GTRCAT -p 50000  -s 16s_alignment.fa -n 16s_tree1

Para la último árbol filogenético se utilizó la herramienta de Mr.Bayes
en Geneious debido auqe desde la terminal se presentaron problemas.

Finalmente, los dos árboles filógenéticos de *Maximum Likelihood* fueron
observados en Geneious para así analizar los resultados.

## Resultados y discusión

Como se observó en la metodología, al momento de la selcción con base en
la literatura, se obtuvieron un mayor número de organismos reductores en
comparación con los oxidadores, a pesar de esto, se observó una
tendencia de agrupación de acuerdo al metabolismo entre los
microorganismos más cercanos, sin embargo, no se observó una tendencia
en la que ambos grupos tuvieran una separación filogenética. Esto se
puede ver en las tres filogénias obtenidas.

Si tomamos como ejemplo los organismos oxidadores del sulfuro (azul),
podemos ver que en todos los casos forman grupos monofiléticos en las
filogénias a pesar de no estar todos agrupados. Cabe resaltar que para
futuros análisis de este tipo se debe hacer una mayor selección de
organismos de forma que se tenga un equilibrio entre la cantidad de
organismos para cada grupo.

Para dar respuesta a nuestra pregunta de investigación, los análisis
filogenéticos realizados muestran una evidencia de la cercanía evolutiva
de los hábitos metabólicos de los organismos, a pesar de esto, no se
pudo observar una formación de grupos monofiléticos de acuerdo a estas
tendencias.

![**Figura 1**. Árbol filógenetico obtenido por medio del paquete
raxml-ng. Naranja: microorganismos reductores de sulfato. Azul:
microorganismos oxidadores de
sulfato.](/Users/OEDENADOR/desktop/raxml1.jpg)

![**Figura 2**. Árbol filógenetico obtenido por medio del paquete raxml
(NPG). Naranja: microorganismos reductores de sulfato. Azul:
microorganismos oxidadores de
sulfato.](/Users/OEDENADOR/desktop/raxml2.jpg)

![**Figura 3**. Árbol filógenetico obtenido por Mr. Bayes. Naranja:
microorganismos reductores de sulfato. Azul: microorganismos oxidadores
de sulfato.](/Users/OEDENADOR/desktop/bayesian.jpg)

## Conclusiones

*1.* Es necesario realizar más estudios filogenéticos que nos permitan
entender si las relaciones evolutivas se ven afectadas por las
tendencias metabolicas de los microroganismos respecto al sulfuro.

*2.* Se pudo realizar de forma exitosa un análisis filogenético que nos
permitiera entender las relaciones evolutivas presenten entre organismos
reductores y oxidadores del sulfuro.

*3.* Se debe continuar el estudio de este tipo de microorganimos debido
a que la información presente en literatura es escaza y es necesario
conocer estas tendencia para así poder reconocer la diversidad de
microorganismos que podemos encontrar en un ecosistema.

## Referencias

Mardigan, M. T., Martinko, J. M., Bender, K. S., Buckley, D. H., &
Stahl, D. A. (2015). Brock Biology of Microorganisms (14th ed.).
Pearson. <https://doi.org/10.1017/cbo9780511549984.016>
