# **Simulación de Análisis filogenético del orden Squamata propuesto por Townsend et al. (2004) utilizando el marcador nuclear RAG-1 y el marcador mitocondrial ND2**
##### Mariana Echeverri y Sebastián Gómez
##### Fundamentos de Biología computacional - Universidad EAFIT
###### 19 de abril del 2022 
   ---
### Introducción

El orden squamata es un grupo diverso que incluye a todos los reptiles conocidos comúnmente como lagartos y a tes grupos sin extremidades: serpientes, anfisbénidos y dibámidos. Este orden sirve como un sistema modelo para el estudio evolutivo de los rasgos morfológicos y comportamentales, adicionalmente, comprender la filogenia de este grupo es crucial para resolver incertidumbres asociadas a dicho orden. A pesar de esto, pocos estudios moleculares han abordado las relaciones de alto nivel dentro de este orden, esto se debe a que la mayoría de estudios que se ocupan de las relaciones entre las familias de escuamados han tenido un muestreo muy limitado de grupos externos y por ende, estos no son tan útiles para producir una filogenia completa de nivel superior. 

El objetivo de este trabajo era simular los análisis filogenéticos del orden Squamata propuestos por Townsend et al. (2004) utilizando el marcador molecular RAG-1 y el marcador mitocondrial ND2. Para realizar las simulaciones se utilizaron programas y herramientas diferentes a las sugeridas por Townsend et al. (2004) con el fin de comparar las filogenias arrojadas al ser realizadas por medio de diferentes metodologías y saber cuál es el marcador ideal para resolver las relaciones filogenéticas del orden Squamata.

### Pregunta de investigación

**¿Cuál es el marcador ideal para resolver las relaciones filogenéticas del orden Squamata?**

Las relaciones filogenéticas entre muchas taxa dentro del orden Squamata siguen siendo inciertas, es por esto que estamos interesados en saber cuál es el marcador ideal para resolver las relaciones filogenéticas de este orden de vertebrados. Con base en lo anterior, se buscaron en la literatura artículos que detallaran análisis filogenéticos a nivel de orden que incluyeran varios marcadores moleculares.

### Metodología
Era necesario encontrar una cantidad considerable de especies para las cuales existieran ambos marcadores y se cubrieran la mayoría de los grupos dentro de este orden, por lo que se buscó en la base de datos del Genbank aquellas especies que cumplieran con estas características. A continuación, en la tabla 1 se muestran las especies incluidas en el análisis filogenético y los respectivos códigos de acceso para cada gen. 

Así:

|Especie         |Gen mitocondrial: ND2 Número de acceso|Gen nuclear: RAG-1 Número de acceso|
|:---------------|:------------------------------------|:----------------------------------|
|Cyanocitta cristata (outgroup)|KY495244.1|AY443280.1|
|Calumma brevicornis|HF570480.1|AY662579.1|
|Brookesia thieli|	FJ975177.1|	AY662577.1|
|Anolis paternus|	AF055965.2|	AY662589|
|Japalura tricarinata|	MW133364.1|	AY662585.1|
|Trioceros rudis|	EF014297.1|	AY662578.1|
|Phrynocephalus raddei|	KF691653.1|	AY662586.1|
|Uromastyx acanthinura|	AB113801.1|	AY662588.1|
|Phrynosoma mcallii|	DQ385355.1|	DQ385417.1|
|Mabuya aurata|	GU931546.1	|AY662629.1|
|Xantusia vigilis|	EU130279.1|	AY662642.1|
|Calotes calotes|	AF128482.1| AY662584.1|
|Leiolepis belliana|	U82689.1|	FJ356734.1|
|Enyalioides laticeps|	EU586749.1|	EU586773.1|
|Basiliscus plumifrons|	MF624304.1|	AY662599.1|
|Ophisaurus attenuatus|	AF085625.1|	AY662602.1|
|Heloderma suspectum|	AF085603.1|	AY662606.1|
|Cylindrophis ruffus |	MK198843.1|	AY662613.1|
|Bipes biporus	|U71335.1|	AY662616.1|
|Amphisbaena xera	|AY662541.1|	AY662619.1|
|Eumeces anthracinus|	AY662552.1|	AY662634.1|
|Chalcides ocellatus|	AY662557.1|	AY662638.1|
|Typhlosaurus lomii|	AY662554.1|	AY662641.1|
|Eublepharis turcmenicus|	AF114248.1|	AY662622.1|
|Gekko gecko|	MT554166.1|	AY662625.1|
|Crenadactylus ocellatus|	AY369016.1|	AY662627.1|
|Lialis jicari|AY662546.1|AY662628.1|

Para obtener todas las secuencias al mismo tiempo y en formato deseado, se descargó el programa Entrez Direct (EDirect) el cual brinda acceso al conjunto de bases de datos interconectadas del NCBI desde una ventana de terminal Unix. Para descargar este programa se utilizó el siguiente comando:
~~~
sh -c "$(curl -fsSL ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)" 
~~~~
Una vez descargado e instalado, se puede proceder a realizar la búsqueda de los códigos de acceso en el formato deseado. El código en donde se específica el programa específico que realizará la función de búsqueda, la base de datos en la que se desea realizar la búsqueda, los códigos de accesión de cada gen, y el formato deseado es mostrado a continuación para ambos set de datos:

~~~~
efetch -db sequences -id KY495244.1, HF570480.1, FJ975177.1, AF055965.2, MW133364.1, EF014297.1, KF691653.1, AB113801.1, DQ385355.1, GU931546.1, EU130279.1, AF128482.1, U82689.1, EU586749.1, MF624304.1, AF085625.1, AF085603.1, MK198843.1, U71335.1, AY662541.1, AY662552.1, AY662557.1, AY662554.1, AF114248.1, MT554166.1, AY369016.1, AY662546.1  -format fasta 

efetch -db sequences -id AY443280.1, AY662579.1, AY662577.1, AY662589.1, AY662585.1, AY662578.1, AY662586.1, AY662588.1, DQ385417.1, AY662629.1, AY662642.1, AY662584.1, FJ356734.1, EU586773.1, AY662599.1, AY662602.1, AY662606.1, AY662613.1, AY662616.1, AY662619.1, AY662634.1, AY662638.1, AY662641.1, AY662622.1, AY662625.1, AY662627.1, AY662628.1 -format fasta 
~~~~
Los resultados de cada búsqueda se guardaron en archivos de texto separados en formato .fasta.

Posteriormente, se utilizó el software Geneious Prime 2022.1.1 y la información asociada a cada secuencia para ser editada; en este punto solo se trimaron las regiones que no hacían parte del gen.

El paso siguiente fue realizar un alineamiento para cada marcador teniendo en cuenta el código genético y marco de lectura con el fin de verificar que el alineamiento estuviera correcto. Para esto se utilizó el ClustalW el cual es un programa para realizar múltiples alineamientos para DNA o proteínas. 

Para instalar ClustalW se utilizó el siguiente comando:
~~~~
conda install -c bioconda clustalw
~~~~
Para realizar los respectivos alineamientos para cada set de datos, fue necesario especificar el archivo de entrada, el formato de salida y el tipo de datos (DNA o proteínas). Vale la pena mencionar que en este punto se siguieron los valores de gap open penalty = 15 y gap extensión penalty = 0.2 propuestos en el artículo. A continuación se muestran los códigos utilizados para cada alineamiento:
~~~~
clustalw -INFILE=ND2_edited.fasta -ALIGN -OUTPUT=FASTA -GAPOPEN=15 -GAPEXT=0.2 -TYPE=DNA

clustalw -INFILE=RAG1_edited.fasta -ALIGN -OUTPUT=FASTA -GAPOPEN=15 -GAPEXT=0.2 -TYPE=DNA
~~~~
Una vez obtenidos los alineamientos para cada set de datos, se realizó un análisis filogenético utilizando el programa RAxML (Randomized Axelerated Maximum Likelihood) version 8.2.12 y usando el método de Maximum Likelihood (ML). Para instalar y activar este programa, fue necesario acudir a los siguientes enlaces: 
[RAxML github](https://github.com/stamatak/standard-RAxML)
[Instalación y activación](https://www.youtube.com/watch?v=4sRqS7MxHzc)

Posteriormente se corrieron los análisis utilizando los ajustes más similares a los propuestos por Townsend et al. (2004). A continuación, se mencionan los parámetros utilizados en el análisis filogenético. 

~~~~
-f a: rapid Bootstrap analysis and search for best¬scoring ML tree in one program run

-A: Specify one of the secondary structure substitution models implemented in RAxML. The same nomenclature as in the PHASE manual is used, available models: S6A, S6B, S6C, S6D, S6E, S7A, S7B, S7C, S7D, S7E, S7F, S16, S16A, S16B 
DEFAULT: 16¬state GTR model (S16)

-x: Specify an integer number (random seed) and turn on rapid bootstrapping CAUTION: unlike in previous versions of RAxML will conduct rapid BS replicates under the model of rate heterogeneity you specified via ¬m and not by default under CAT 

-#: Specify the number of alternative runs on distinct starting trees
In combination with the "¬b" option, this will invoke a multiple bootstrap analysis

-k: Specifies that bootstrapped trees should be printed with branch lengths. The bootstraps will run a bit longer, because model parameters will be optimized at the end of each replicate under GAMMA or GAMMA+P-Invar respectively. 

-m: Model of Binary (Morphological), Nucleotide, Multi¬State, or Amino Acid 

-p: Specify a random number seed for the parsimony inferences. This allows you to reproduce your results and will help me debug the program. 

-o:  Specify the name of a single outgroup or a comma¬separated list of outgroups, e.g., ¬o Rat or o Rat,Mouse, in case that multiple outgroups are not monophyletic the first name in the list will be selected as outgroup, don't leave spaces between taxon names! 

-s: Specify the name of the alignment data file in PHYLIP or FASTA format 

-n:  Specifies the name of the output file. 
~~~~
Los códigos utilizados en RAxML fueron los siguientes:

**Para RAG-1:**
~~~~
RAxML was called as follows 

raxmlHPC -f a -A S16B -x 1000 -# 100 -k -m GTRGAMMA -p 4000000 -o Cyanocitta_cristata -s RAG1_aligned.fasta -n RAG1_TREE 

Overall execution time for full ML analysis: 338.490890 secs or 0.094025 hours or 0.003918 days
~~~~~

**Para ND2:**
~~~~
RAxML was called as follows:

raxmlHPC -f a -A S16B -x 1000 -# 100 -k -m GTRGAMMA -p 4000000 -o Cyanocitta_cristata -s ND2_aligned.fasta -n ND2_TREE 

Overall execution time for full ML analysis: 326.337131 secs or 0.090649 hours or 0.003777 days
~~~~

Finalmente, se visualizaron los archivos de los mejores árboles de ambos marcadores en el programa FigTree versión - v1.4.4 y se compararon con las filogenias presentadas en el artículo.

### Resultados y discusión
Los análisis filogenéticos realizados en la plataforma RAxML soportan la hipótesis en donde el marcador nuclear RAG1 explica la filogenia a nivel de orden ya que con las secuencias utilizadas  se logran ver relaciones filogenéticas similares a las propuestas en el artículo de Townsend et al. (2004) (ver figura 1). Por el contrario, con el marcador mitocondrial no se obtuvieron resultados tan similares a los propuestos en el artículo (ver figura 2). Si bien algunos grupos concuerdan, algunas familias no representan las relaciones evolutivas correctas e incluso especies de la misma familia aparecen en regiones diferentes de la filogenia, es por esto que en principio se podría descartar a ND2 como marcador molecular que pueda explicar las relaciones del clado Squamata a nivel de orden. Además, los resultados del marcador nuclear del análisis filogenético propuesto también se asemejan a las relaciones evolutivas propuestas en el trabajo de Pyron et al. (2013) en donde también utilizan los mismos marcadores nucleares y mitocondriales. Con lo anterior, se podría inferir que los genes nucleares poseen tasas de sustitución adecuadas para reconstruir las relaciones filogenéticas a niveles más basales como en este caso en el orden Squamata (Springer et al. 2001).

![Figura 1](https://raw.githubusercontent.com/mecheverrd/Biologia_computacional/main/RAG1.png) 
**Figura 1:** Filogenia del orden Squamata utilizando el marcador nuclear RAG-1 propuesta por Townsend et al. (2004). Los números a la derecha corresponden a los principales grupos dentro del orden: 1. Chamaeleonidae; 2. Agamidae; 3. Iguanidae; 4. Anguidae; 5. Helodermatidae; 6. Xenosauridae; 7. Varanidae; 8. Shinisauridae; 9.Serpentes; 10. Lacertidae; 11. Amphisbaenia; 12. Teiidae; 13. Gymnophthalmidae; 14. Scincidae; 15. Xantusiidae; 16. Cordylidae; 17. Dibamidae; 18. Gekkonidae.

![Figura 2](https://raw.githubusercontent.com/mecheverrd/Biologia_computacional/main/RAG1_RAxML.png)
**Figura 2:** Filogenia del orden Squamata utilizando el marcador nuclear RAG-1 realizada en RAxML.

![Figura 3](https://raw.githubusercontent.com/mecheverrd/Biologia_computacional/main/ND2.png)
**Figura 3:** Filogenia del orden Squamata utilizando el marcador mitocondrial ND2 propuesta por Townsend et al. (2004). Los números a la derecha corresponden a los principales grupos dentro del orden previamente mencionados en la figura 1.

![Figura 4](https://raw.githubusercontent.com/mecheverrd/Biologia_computacional/main/ND2_RAxML.png)
**Figura 4:** Filogenia del orden Squamata utilizando el marcador mitocondrial ND2 realizada en RAxML. Los clados en rojo no concuerdan con los propuestos por Townsend et al. (2014) en la figura 3.

### Conclusiones

Una filogenia clara de este orden podría representar un gran avance en diversos campos de estudio como la morfología, el comportamiento y la ecología. Es por esto que es necesario tener bases de datos completas, confiables y con una buena calidad de datos que permitan hacer análisis filogenéticos rigurosos que incluyan la mayor cantidad de muestras/datos con el fin de disminuir sesgos o posibles errores por falta de datos o calidad de los mismos.

En cuanto al análisis y trabajo computacional, se pudo replicar correctamente uno de los resultados del artículo utilizando algunos programas y herramientas diferentes a las sugeridas. Lo anterior revela el potencial de este tipo de herramientas computacionales debido a que no existe una única manera correcta de hacer las cosas. Si bien esta amplia posibilidad de aproximaciones computacionales a un mismo problema puede resultar compleja, esta diversidad de rutas hacia la misma solución es uno de los factores que robustecen cada día más las ciencias computacionales.


### Referencias
* Geneious Prime 2022.1.1 

* RAxML version 8.2.12 released by Alexandros Stamatakis on May 2018

* FigTree - Latest Version - v1.4.4

* Kans J. Entrez Direct: E-utilities on the Unix Command Line. 2013 Apr 23 [Updated 2022 Apr 7]. In: Entrez Programming Utilities Help [Internet]. Bethesda (MD): National Center for Biotechnology Information (US); 2010-. Available from: https://www.ncbi.nlm.nih.gov/books/NBK179288/

* Larkin MA, Blackshields G, Brown NP, Chenna R, McGettigan PA, McWilliam H, Valentin F, Wallace IM, Wilm A, Lopez R, Thompson JD, Gibson TJ, Higgins DG.
(2007). Clustal W and Clustal X version 2.0. Bioinformatics, 23, 2947-2948.

* Pyron, R. A., F. T. Burbrink, and J. J. Wiens. 2013. A phylogeny and revised classification of Squamata, including 4161 species of lizards and snakes. BMC Evol. Biol. 13:1–54. BioMed Central.

* Townsend, T. M., A. Larson, E. Louis, and J. R. Macey. 2004. Molecular Phylogenetics of Squamata: The Position of Snakes, Amphisbaenians, and Dibamids, and the Root of the Squamate Tree. Syst. Biol. 53:735–757. Oxford Academic.


* Springer, M. S., R. W. DeBry, C. Douady, H. M. Amrine, O. Madsen, W. W. de Jong, and M. J. Stanhope. 2001. Mitochondrial Versus Nuclear Gene Sequences in Deep-Level Mammalian Phylogeny Reconstruction. Mol. Biol. Evol. 18:132–143. Society for Molecular Biology and Evolution.

* Stamatakis A. (2014). RAxML version 8: a tool for phylogenetic analysis and post-analysis of large phylogenies. Bioinformatics (Oxford, England), 30(9), 1312–1313. https://doi.org/10.1093/bioinformatics/btu033








