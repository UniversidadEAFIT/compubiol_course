#! /bin/bash
#usage: global_alig.py [txt seqs_one_by_row]
#output: matrix and aligment
#author: Jorge Jonson
#course: Computational biology, EAFIT University 
import os.path
import sys

class Celda:
    valorIzq = None
    valorArr = None
    valorDiag = None
    valor = None
    rutaArr = False
    rutaIzq = False
    rutaDiag = False
    esNodo = False

class Alineador:        
    
    def __init__(self):
        self.__GAP = -2
        self.__NOMATCH = -1
        self.__MATCH = +1
        self.__BIFDIAG = 0
        self.__BIFARR = 1
        self.__BIFIZQ = 2
        self.__ZERO = 0
        self.__alineamientos = []
        self.__nombreArchivoSecuencias = None
        self.__Matriz = [[]] 
    ### 
    ### las dos secuencias se leen desde un archivo plano, y deben estar separadas por un salto de línea
    ###
    def __leerSecuenciasDesdeArchivo(self):
        file = open(self.__nombreArchivoSecuencias,'r')
        self.__sequenciaHorizontal = "-"+file.readline().strip()
        self.__sequenciaVertical = "-"+file.readline().strip()

    ###-----
    ### Crea una matriz con tantas columnas como una de las secuencias
    ### y con tantas filas como la otra de las secuencias
    ###
    def __crearMatriz (self):
        self.__totalColumnas = len(self.__sequenciaHorizontal)
        self.__totalFilas = len(self.__sequenciaVertical)
        self.__Matriz = [
                            [None for fil in range(0,self.__totalColumnas)] 
                            for col in range(0,self.__totalFilas)
                        ]
        self.__establecerValorBaseGap()
    ###-----
    ### La intersección gap-gap debe llevar un valor concreto para poder comenzar
    ###   
    def __establecerValorBaseGap(self):
        celda = Celda()
        celda.valor = self.__ZERO
        self.__Matriz[0][0] = celda
        

    ###----- 
    ### La primera fila de la matriz debe estar cargada con valores a partir de gap
    ###
    def __cargarFilaBase(self):
        gap = self.__Matriz[0][0].valor
        for idxCol in range(1,self.__totalColumnas):
            gap += self.__GAP 
            celda = Celda()
            celda.valor = gap
            self.__Matriz[0][idxCol] = celda

    ###----- 
    ### La primera columna de la matriz debe estar cargada con valores a partir de gap
    ###
    def __cargarColumnaBase(self):
        gap = self.__Matriz[0][0].valor
        for idxFil in range(1,self.__totalFilas):
            gap += self.__GAP 
            celda = Celda()
            celda.valor = gap
            self.__Matriz[idxFil][0] = celda

    ###
    ### Esta función calcula los valores para toda la matriz, basándose en 
    ### la existencia de la función calcular celda. SE debe tener cuidado, 
    ### ya que una celda no puede ser calculada sino cuando tenga calculada la
    ### celda de arriba, la de la izquierda y la de abajo
    def __calcularValoresMatriz(self):
        for c in range(1,self.__totalColumnas):
            for f in range(1,self.__totalFilas):
                self.__calcularCelda(f, c)
                self.__marcarBifurcacionesCelda(f, c)
                self.__marcarCeldaComoNodoSiEsNodo(f, c)
       
    ###
    ### Un elemento de la matriz se calcula con la función mayor.
    ###  función mayor es el mayor entre:
    ###         valor de arriba + gap
    ###         valor de la izquierda + gap
    ###         valor de la diagonal + gap
    ###         cero + gap (sólo para alineamiento local)
    ###    
    def __calcularCelda(self, f, c):
        celda = Celda()
        celda.valorIzq = self.__Matriz[f][c-1].valor + self.__GAP
        celda.valorArr = self.__Matriz[f-1][c].valor + self.__GAP

        nuclCol = self.__sequenciaHorizontal[c]
        nuclFil = self.__sequenciaVertical[f]
        match = self.__MATCH if nuclFil == nuclCol else self.__NOMATCH
        celda.valorDiag = self.__Matriz[f-1][c-1].valor + match

        celda.valor = max(celda.valorIzq,celda.valorDiag,celda.valorArr)
        self.__Matriz[f][c] = celda
        return

   
    ###
    ### Marca las rutas de conexión entre celdas para saber
    ### desde dónde se seleccionaron los mayores.
    def __marcarBifurcacionesCelda(self, f, c):
        maxVal = self.__Matriz[f][c].valor
        self.__Matriz[f][c].rutaArr  = (maxVal == self.__Matriz[f][c].valorArr )
        self.__Matriz[f][c].rutaIzq  = (maxVal == self.__Matriz[f][c].valorIzq )
        self.__Matriz[f][c].rutaDiag = (maxVal == self.__Matriz[f][c].valorDiag)

    ###
    ### Cuando la función mayor da como resultado más de una via, esto genera
    ### ramas, lo que implica que la celda es un nodo de un grafo o árbol
    ### En este caso la celda se marca como NODO
    def __marcarCeldaComoNodoSiEsNodo (self, f,c):
        self.__Matriz[f][c].esNodo = ( 
            self.__Matriz[f][c].rutaArr and self.__Matriz[f][c].rutaIzq  or
            self.__Matriz[f][c].rutaArr and self.__Matriz[f][c].rutaDiag or
            self.__Matriz[f][c].rutaIzq and self.__Matriz[f][c].rutaDiag 
        )


    def establecerArchivo(self,nombreArchivo):
        if os.path.isfile(nombreArchivo): 
            self.__nombreArchivoSecuencias = nombreArchivo
        else:
            print("Archivo No Existe: ", nombreArchivo)
            raise
        
    def mostrarMatriz(self):
        print('   ',end='')
        for c in range(0,self.__totalColumnas):
            print(" {:>3s} ".format(self.__sequenciaHorizontal[c]), end='')
        for i in range(0,self.__totalFilas):
            print()
            print(' '+self.__sequenciaVertical[i]+' ',end='')
            for j in range(0,self.__totalColumnas):
                print(" {0:>3d} ".format(self.__Matriz[i][j].valor), end='')
        print()
  
    
    ###
    ### presenta en consola los posibles alineamientos calculados
    ###
    def mostrarAlineamientos(self):
        for al in self.__alineamientos:
            print()
            print (al[0])
            print (al[1])


    ###
    ### Se recorre la matriz según algoritmo de alineamiento para generar
    ### las posibles secuencias de alineamiento
    ###
    def alinear(self):
        haymas = True
        while haymas:
            f =  self.__totalFilas-1
            c =  self.__totalColumnas-1
            alineaH = ""
            alineaV = ""
            ultNodo = None
            while c >= 0 and f >= 0:
                celdaBifurca = self.__Matriz[f][c].esNodo
                if self.__Matriz[f][c].rutaDiag:
                     alineaV = self.__sequenciaVertical[f]+alineaV
                     alineaH = self.__sequenciaHorizontal[c]+alineaH
                     if celdaBifurca: ultNodo = [f,c,self.__BIFDIAG]
                     f-= 1
                     c-= 1
                elif self.__Matriz[f][c].rutaIzq:
                     alineaH = self.__sequenciaHorizontal[c]+alineaH
                     alineaV = '-'+alineaV
                     if celdaBifurca: ultNodo = [f,c,self.__BIFIZQ]
                     c-= 1
                elif self.__Matriz[f][c].rutaArr:
                     alineaH = '-'+alineaH
                     alineaV = self.__sequenciaVertical[f]+alineaV
                     if celdaBifurca: ultNodo = [f,c,self.__BIFARR]
                     f-= 1
                else:
                    if f == 0 and c >= 0:
                       alineaH = self.__sequenciaHorizontal[c]+alineaH
                       alineaV = '-'+alineaV
                       c-= 1
                    elif c == 0 and f >= 0:
                         alineaH = '-'+alineaH
                         alineaV = self.__sequnciaVertical[f]+alineaV
                         f-= 1
            self.__alineamientos.append([alineaH,alineaV])
            if ultNodo != None:
                f = ultNodo[0]
                c = ultNodo[1]
                ultBif = ultNodo[2]
                if ultBif == self.__BIFDIAG:
                   self.__Matriz[f][c].rutaDiag = False
                elif ultBif == self.__BIFARR:
                   self.__Matriz[f][c].rutaArr = False
                elif ultBif == self.__BIFIZQ:
                   self.__Matriz[f][c].rutaIzq = False
                self.__marcarCeldaComoNodoSiEsNodo (f,c)
            else:
                haymas = False


    def preparar(self):
        self.__leerSecuenciasDesdeArchivo ()
        self.__crearMatriz()
        self.__cargarFilaBase()
        self.__cargarColumnaBase()
        self.__calcularValoresMatriz()
        
# --- fin de la clase

### programa de punto de entrada

def alinear(archivo):
    objAlineador = Alineador()
    objAlineador.establecerArchivo(archivo)
    objAlineador.preparar()
    objAlineador.mostrarMatriz()
    objAlineador.alinear()
    objAlineador.mostrarAlineamientos()
            
def main():
    if len(sys.argv) == 1:
       print ("Falta el nombre del archivo de secuencias")
       return
   
    nombreArchivo = sys.argv[1] 
    if not os.path.isfile(nombreArchivo): 
       print("Archivo No Existe: ", nombreArchivo)
       return
   
    alinear(nombreArchivo)

if __name__ == "__main__":
   main()
