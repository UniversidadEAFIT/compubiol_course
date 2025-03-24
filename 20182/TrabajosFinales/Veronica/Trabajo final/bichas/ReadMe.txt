BICHAS

COMANDOS PARA USAR EN LA CONSOLA 

La consola puede consultar informaci�n de taxonom�a, organismos, secuencias; y los comandos actualmente disponibles para cada uno son:

	TAXONOM�A (conectada a la librer�a de taxonom�a del NCBI)

		taxon.leer		Este comando requiere el par�metro Id= Muestra el nombre del organismo buscado.
		taxon.listarcampos	Este comando fija las �rdenes de listar campos. Muestra los campos de informaci�n que trae el registro.
		taxon.data		Este comando requiere solo un par�metro (campo). Muestra la informaci�n contenida en el campo especificado.

		taxon.			Este comando fija el tipo de acci�n.
		taxon..			Este comando quita un tipo de acci�n fijo.
		taxon.data.		Este comando fija el tipo de acci�n.
		taxon.data..		Este comando quita un tipo de acci�n fijo.


	ORGANISMOS (conectada a la librer�a de datos de nucle�tidos del NCBI)

		organismo.leer		Este comando requiere el par�metro Id= Muestra el nombre del organismo buscado.
		organismo.listarcampos	Este comando fija las �rdenes de listar campos. Muestra los campos de informaci�n que trae el registro.
		organismo.data		Este comando requiere solo un par�metro (campo). Muestra la informaci�n contenida en el campo especificado.

		organismo.		Este comando fija el tipo de acci�n.
		organismo..		Este comando quita un tipo de acci�n fijo.
		organismo.data.		Este comando fija el tipo de acci�n.
		organismo.data..	Este comando quita un tipo de acci�n fijo.


	SECUENCIAS (conectada a la librer�a de nucle�tidos del NCBI)

		secuencias.leer		Este comando requiere el par�metro orgn=(organismo). Muestra el n�mero de registros de secuencias para ese organismo.
		secuencias.listarcampos Este comando fija las �rdenes de listar campos. Muestra los campos de informaci�n que trae el registro.
		secuencias.data		Este comando requiere solo un par�metro (campo). Muestra la informaci�n contenida en el campo especificado.			

		secuencias.		Este comando fija el tipo de acci�n.
		secuencias..		Este comando quita un tipo de acci�n fijo.
		secuencias.data.	Este comando fija el tipo de acci�n.
		secuencias.data..	Este comando quita un tipo de acci�n fijo.


	COMANDOS GENERALES

		limpiar			Este comando fija el tipo de acci�n: Limpiar la pantalla, pero seguir dentro de la consola.
		fin			Este comando fija el tipo de acci�n: Salir de la consola BICHAS.


Nota:	Los comandos con . (un punto) al final, son para permanecer de forma fija dentro del comando dado.
	Los comandos con .. (dos puntos) al final, son para salir del comando fijado previamente y utilizar otro comando distinto.


