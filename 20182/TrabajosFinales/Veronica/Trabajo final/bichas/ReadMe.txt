BICHAS

COMANDOS PARA USAR EN LA CONSOLA 

La consola puede consultar información de taxonomía, organismos, secuencias; y los comandos actualmente disponibles para cada uno son:

	TAXONOMÍA (conectada a la librería de taxonomía del NCBI)

		taxon.leer		Este comando requiere el parámetro Id= Muestra el nombre del organismo buscado.
		taxon.listarcampos	Este comando fija las órdenes de listar campos. Muestra los campos de información que trae el registro.
		taxon.data		Este comando requiere solo un parámetro (campo). Muestra la información contenida en el campo especificado.

		taxon.			Este comando fija el tipo de acción.
		taxon..			Este comando quita un tipo de acción fijo.
		taxon.data.		Este comando fija el tipo de acción.
		taxon.data..		Este comando quita un tipo de acción fijo.


	ORGANISMOS (conectada a la librería de datos de nucleótidos del NCBI)

		organismo.leer		Este comando requiere el parámetro Id= Muestra el nombre del organismo buscado.
		organismo.listarcampos	Este comando fija las órdenes de listar campos. Muestra los campos de información que trae el registro.
		organismo.data		Este comando requiere solo un parámetro (campo). Muestra la información contenida en el campo especificado.

		organismo.		Este comando fija el tipo de acción.
		organismo..		Este comando quita un tipo de acción fijo.
		organismo.data.		Este comando fija el tipo de acción.
		organismo.data..	Este comando quita un tipo de acción fijo.


	SECUENCIAS (conectada a la librería de nucleótidos del NCBI)

		secuencias.leer		Este comando requiere el parámetro orgn=(organismo). Muestra el número de registros de secuencias para ese organismo.
		secuencias.listarcampos Este comando fija las órdenes de listar campos. Muestra los campos de información que trae el registro.
		secuencias.data		Este comando requiere solo un parámetro (campo). Muestra la información contenida en el campo especificado.			

		secuencias.		Este comando fija el tipo de acción.
		secuencias..		Este comando quita un tipo de acción fijo.
		secuencias.data.	Este comando fija el tipo de acción.
		secuencias.data..	Este comando quita un tipo de acción fijo.


	COMANDOS GENERALES

		limpiar			Este comando fija el tipo de acción: Limpiar la pantalla, pero seguir dentro de la consola.
		fin			Este comando fija el tipo de acción: Salir de la consola BICHAS.


Nota:	Los comandos con . (un punto) al final, son para permanecer de forma fija dentro del comando dado.
	Los comandos con .. (dos puntos) al final, son para salir del comando fijado previamente y utilizar otro comando distinto.


