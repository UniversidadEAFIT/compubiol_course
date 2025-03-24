# Construcción filogenética de abejorros (_Bombus_), utilizando el gen 16S y comparando los resultados arrojados por distintos árboles. 
### _Brian Hincapie_

## Introduction
En la actualidad los servicios complementarios de polinización de cultivos son proporcionados predominantemente por un puñado de especies de abejas, como lo son las abejas melíferas (_Apis mellifera_) y, en menor medida, por algunas especies de abejorros (p. ej., _Bombus terrestris_L., _Bombus impatiens_ Cresson y _Bombus ignitus_ Smith; Hymenoptera: Apidae) y abejas sin aguijón (Hymenoptera: Apidae: Meliponini) (Cooley y Vallejo Marín, 2021).

Los abejorros (_Bombus_ Latreille) son organismos que ocupan una gran diversidad de hábitats, desde praderas alpinas hasta bosques tropicales, y sin embargo parecen tener una morfología similar en toda su área de distribución, lo que sugiere que las adaptaciones de comportamiento desempeñan un papel más importante en la colonización de diversos hábitats (Cameron et. al. 2007).

A pesar de la aparente limitación de la diversidad estructural, los abejorros muestran una sorprendente variación inter e intraespecífica en los patrones de color a lo largo de su área de distribución (Sladen, 1998), pero la similitud morfológica general entre las especies ha dificultado la resolución completa de la filogenia de los abejorros y la interpretación de su evolución (Michener, 2000). El esclarecimiento de las relaciones filogenéticas entre los abejorros no es del todo sencilla, ya que las diferentes especies son morfológicamente "monótonas" (Michener, 1990), especialmente entre las hembras.


Por lo que para dilucidar la evolución de la diversidad es necesario conocer el patrón histórico de variación, lo que, a su vez, proporciona una visión única de los procesos evolutivos que subyacen al patrón de variación. Una filogenia robusta de _Bombus_, el objetivo de este análisis es comparar la construcción propuesta con el gen 16 S de algunas especies de _Bombus_ utilizando herramientas bioinformáticas con base al trabajo realizado por Cameron y otros investigadores (2007). 
## Objetivo general 
- Identificación y análisis de relaciones evolutivas utilizando distintos métodos para crear las filogenias de _Bombus_.

## Objetivos específicos 
- Explorar las relaciones evolutivas de algunas especies del género _Bombus_.
- Contrastar los métodos para la creación de filogenia con base a información sobre los _Bombus_

## Pregunta 
¿Cuáles son las relaciones filogenéticas de Bombus utilizando el gen 16S?

## Metodología
Se extraen secuencias existentes en GenBank que es un plataforma ampliamente utilizada para una gran diversidad análisis de secuencias entre ellos la consulta de secuencias de nucleótidos, donde se pueden descargar secuencias en este caso en formato FASTA, que contiene información de las especies a evaluar a las cuales se les ha asignado en la plataforma un  número de acceso o un identificador que se obtuvieron de estudios anteriores correspondientes al trabajo realizado por Cameron y otros investigadores (2007) las secuencias utilizadas se encuentran en la tabla 1 y una secuencia de _Bombus_ atratus con sus correspondientes grupos externos marcados en negrilla.

Las secuencias utilizadas se encuentran en la siguiente tabla:
[![fdsafa.jpg](https://i.postimg.cc/vTkm2g7k/fdsafa.jpg)](https://postimg.cc/wR5H7BGQ)
Se procede a realizar la construcción filogenética estableciendo los siguientes parámetros:
([![Aspose-Words-f757404c-5665-465c-ad9c-29978b72fa3f-001.png](https://i.postimg.cc/sDsDnzRT/Aspose-Words-f757404c-5665-465c-ad9c-29978b72fa3f-001.png)](https://postimg.cc/ThN6wZ1b)

Se utiliza el programa software Molecular Evolutionary Genetics Analysis (MEGA) que tiene una gran colección de métodos y herramientas de evolución molecular computacional. Siendo una de las herramientas más completas para construir árboles de tiempo de especies, patógenos y familias. Obteniendo de este sofware el alineamiento mediante MUSCLE con las siguientes características:
[![2321123.jpg](https://i.postimg.cc/1zrZVn8P/2321123.jpg)](https://postimg.cc/qtqF97cZ)

Muestra valores altos en algunos grupos de la filogenia y comparándolo con la filogenia de Cameron y otros investigadores la mayoría de los géneros coinciden con la agrupación encontrada pero tiene igualmente valores bajos en algunos grupos y los grupos externos se encuentran en la filogenia. 
[![Por-fin.png](https://i.postimg.cc/9XtqXJmN/Por-fin.png)](https://postimg.cc/yWxNvhSF)

Para el otro árbol se utilizo la herramienta software Geneious que corresponde donde se construye otro árbol con el mismo alineamiento obtenido mediante Muscle, ingresando los siguientes parámetros: 
[![datos-genius.png](https://i.postimg.cc/25SxnyGh/datos-genius.png)](https://postimg.cc/68FRX9Dp)

Mostrando el siguiente árbol con unos mejores valores que el anterior y con los grupos externos en la ubicación correcta además de coincidir en casi todos los subgeneros de _Bombus_ en contraste con la literatura. Por lo que se concluye que este quedó mejor elaborado. 
[![Filogenia.png](https://i.postimg.cc/xCkyFZWd/Filogenia.png)](https://postimg.cc/Kk2M10cX)


## Conclusión
Los árboles contrastados tienen valores de Bootstrap bastante altos en algunos grupos y al compararlos con literatura como el trabajo de (Kawakita et al., 2003) ha recuperado relaciones filogenéticas robustas entre la mayoría de los principales linajes de Bombus con solo el gen 16 S, aunque el trabajo mencionado es mucho más robusto y valido ya que los investigadores basándose en tres genes nucleares, rodopsina de longitud de onda larga (LW Rh), arginina quinasa (ArgK), y la copia F2 del factor de elongación-1a (EF-1a) y otras especies construyen un árbol con mejores explicacioens evolutivas. Esto puede ser explicado debido a que además, las elevadas tasas de sustitución y la composición de bases sesgada del ADN mitocondrial de las abejas ADN de abejas impiden una resolución suficiente de la filogenia de alto nivel.
## References
Cooley, H., & Vallejo-Marín, M. (2021). Buzz-Pollinated Crops: A Global Review and Meta-analysis of the Effects of Supplemental Bee Pollination in Tomato. Journal of Economic Entomology, 114(2), 505–519. https://doi.org/10.1093/jee/toab009 

Tamura K, Stecher G, and Kumar S (2021) MEGA11: Molecular Evolutionary Genetics Analysis version 11. Molecular Biology and Evolution 38:3022-3027.

Cameron, S. A., Hines, H. M., & Williams, P. H. (2007). A comprehensive phylogeny of the bumble bees (Bombus). Biological Journal of the Linnean Society, 91(1), 161–188. https://doi.org/10.1111/j.1095-8312.2007.00784.

Sladen FWL. (1912). The humble-bee. London: Macmillan.

Michener, C.D., 2000. The Bees of the World. John Hopkins. University Press, Baltimore

Michener, C. D. (1990). Classification of the Apidae (hymenoptera). The University of Kansas Science Bulletin, 54(4), 75.

Kawakita, A., Sota, T., Ascher, J.S., Ito, M., Tanaka, H., Kato, M., 2003. Evolution and phylogenetic utility of alignment gaps within intron sequences of three nuclear genes in bumble bees (Bombus). Mol. Biol. Evol. 20, 87–92






