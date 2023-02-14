#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:40:00 2018
Usage: python3 readmacrogene.py <folder> windows_size minscore
@author: isabel
"""
from Bio import SeqIO

import sys
import os

clear = lambda: os.system('clear')


def getOptimumWindowCenter(phr, windowSize):
    i = 0
    promMax = 0
    promMaxPos = 0
    while i <= len(phr)- windowSize:
        prom= sum(phr[i:i+windowSize])/float(windowSize)
        if prom > promMax:
            promMax = prom
            promMaxPos = i
        i = i + 1
    return promMax, promMaxPos + int(windowSize / 2.0)
    
def getTrimmedPhred(phr, n, score):
    promMax, optimumWindowPosition = getOptimumWindowCenter(phr,n)    
    der= optimumWindowPosition
    izq= optimumWindowPosition 
    izqend=False
    derend=False
    while izq >=0 and der < len(phr)-1:
        promizq= sum(phr[izq-n:izq])/float(n)
        promder= sum(phr[der:der+n])/float(n)        
        if promizq >=score: 
            izq = izq - 1
        else:
            izqend=True
        if promder >=score: 
            der = der + 1
        else:
            derend=True
        if izqend and derend: 
            break
    return phr[izq:der], optimumWindowPosition, izq, der

def existecarpeta(carpeta): return os.path.isdir(carpeta)

def existeArchivo(archivo): return os.path.exists(archivo)

def listToString(alist):
    s=""
    for c in alist:
        s = s + c
    return s

def saveResultToFile(filename,strTrimSeq):
    f = open ("./resultados/"+filename+".txt","w")
    f.write(strTrimSeq)
    f.close()


def getrimedSeqence(abirecord, izq, der ):
    trimedListSeq = []
    idx = izq
    while idx <= der:
        trimedListSeq.append(abirecord.seq[idx])
        idx = idx + 1
    return listToString(trimedListSeq)

def procesarArchivoAbi(carpeta, filename, n, score):
    print(filename, "procesado.")
    nombrecompletoarchivo = os.path.join(carpeta,filename)
    abirecord = SeqIO.read(nombrecompletoarchivo,'abi')
    phr = abirecord.letter_annotations["phred_quality"]    
    phrtrimado, orig, izq, der = getTrimmedPhred(phr, n, score)    
    strTrimSeq = getrimedSeqence(abirecord, izq, der )   
    saveResultToFile(filename,strTrimSeq)
#    print("consultando en Blast de NCBI...")
#    infoBL = BLAST_e_info(strTrimSeq)
#    print("guardando info Blast...")
#    print(infoBL)
    return

def listarCarpetas(carpetaraiz):
    listdir = []
    for dirname, dirnames, filenames in os.walk(carpetaraiz):
        for subdirname in dirnames:
            listdir.append(os.path.join(dirname, subdirname))
        return listdir

def procesarAbisDeCarpeta(carpeta, n, score):
    print("procesando carpeta = ",carpeta,"...")
    for file in os.listdir(carpeta):
        if file.endswith(".ab1"):
           procesarArchivoAbi(carpeta, file , n, score)
    print("carpeta procesada.")
    return

def procesarCarpetas(listaCarpetas, n, score):
    for carpeta in listaCarpetas:
        procesarAbisDeCarpeta(carpeta, n, score)

def generarAbisTrimados():
       carpeta = sys.argv[1].strip()
       n = int(sys.argv[2].strip())
       score = int(sys.argv[3].strip())
#       carpeta = "/Users/isabel/Documents/TESIS/idcepas"
#       n = 6
#       score = 30 
       if existecarpeta(carpeta):
           listadecarpetas = listarCarpetas(carpeta)
           procesarCarpetas(listadecarpetas, n, score)

def main():
    clear()
    generarAbisTrimados()

if __name__ == "__main__":
    main()
