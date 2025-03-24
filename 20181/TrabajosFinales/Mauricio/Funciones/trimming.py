## FUNCIÓN PARA TRIMAR SECUENCIAS SEGÚN LOS PHRED VALUE ##

## MAURICIO SERNA ##
## 31 mayo 2018 ##

# Importar librerías necesarias
from Bio import SeqIO
import numpy as np

# Función para importar abi de archivo
def importar(nombre):
    abi = SeqIO.read(nombre,'abi')
    return abi

# Función para extraer phred de abi
def extraerphred(abi):
    return(abi.letter_annotations['phred_quality'])

# Función para extraer la secuencia de abi
def extraerseq(abi):
    return(abi.seq)

#################################################
# RECORRER LA SECUENCIA SEGÚN PROMEDIOS DE PHRED #

# Promedios de los valores phred según rango (ventana) definido
def promediosporventana(phred, ventana):  # devuelve una lista con los promedios por el rango (ventana) indicada
    i = 0
    promedios = []
    while (i<len(phred)):
        promedios = promedios + [np.mean([phred[i:i+ventana]])]
        i = i + ventana
    return (promedios)

# Posiciones de trimaje
def primeraposicion (phred, ventana, umbral): # input: vector de phred, ventana de análisis ubral de phred=valores de phred deseados
    promedios = promediosporventana(phred, ventana) # calculo los promedios según la ventana deseada
    i = int(len(promedios)/2)  # comienzo a recorrer el vector desde la mitad
    while i >= 0:
        if promedios[i]<umbral and promedios[i-1]<umbral:
            posicion1 = i
            break
        i = i - 1 
    posicion1 = (posicion1+1)*ventana  # posición superior de la ventana que cumpla con la condición de dos ventanas con promedio inferior a 20
    return (posicion1)

def segundaposicion (phred, ventana, umbral):
    promedios = promediosporventana(phred, ventana) # calculo los promedios según la ventana deseada
    i = int(len(promedios)/2)  # comienzo a recorrer el vector desde la mitad
    while i < len(promedios):
        if promedios[i]<umbral and promedios[i+1]<umbral:
            posicion2 = i
            break
        i = i + 1 
    posicion = (posicion2)*ventana # posición inferior de la ventana que cumpla la condición de que dos ventanas sean menores a 20
    return(posicion)

# Entrega las posiciones de trimaje
def posiciones(phred, ventana, umbral):
    primera = primeraposicion(phred, ventana, umbral)
    segunda = segundaposicion(phred, ventana, umbral)
    return (primera,segunda)

#################################################
# FUNCIONES DE TRIMAJE #


# Función para trimar la secuencia
def trimming_seq(archivo,ventana,umbral):
    abi= importar(archivo)
    secuencia= extraerseq(abi)
    phred= extraerphred(abi)
    puntocorte_1= posiciones(phred, ventana,umbral)[0]
    puntocorte_2= posiciones(phred,ventana,umbral)[1]
    Seqtrimmed = secuencia[puntocorte_1:puntocorte_2]
    return (Seqtrimmed)

# Función para trimar los phred
def trimming_phred(archivo,ventana,umbral):
    abi= importar(archivo)
    phred= extraerphred(abi)
    puntocorte_1= posiciones(phred, ventana,umbral)[0]
    puntocorte_2= posiciones(phred,ventana,umbral)[1]
    Phredtrimmed = phred[puntocorte_1:puntocorte_2]
    return (Phredtrimmed)
