## FunciÃ³n #

#leer capeta, trimar secuencias, blast del trimmed y extraer info del BALST ##

## Mauricio Serna ##
## 31 mayo 2018 ##

##
## La función recibe una carpeta donde tiene que haber arcivos .ab1
## Devuelve un archivo.csv llamado Resultados.csv donde esta la info del BLAST


from trimming import trimming_seq
from leer_abis import leerabis
from blast import BLAST_e_info
from tabla_csv import tabla_csv

def main(carpeta):
    Abis = leerabis(carpeta)
    results = {}
    for abi in Abis:
        abi_name = abi.split("/")[-1]
        trimmed_seq = trimming_seq(abi,5,20)
        info = BLAST_e_info(trimmed_seq)
        results[abi_name] = info 
    return tabla_csv(results)
