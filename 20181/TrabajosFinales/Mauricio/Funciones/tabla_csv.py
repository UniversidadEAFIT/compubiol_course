# Función para montar los resultados en un archivo .csv

## Mauricio Serna
### 6 junio 2018

# Paquete para leer y escribir archivos.csv
import csv

# Función crear la info para la tabla desde el diccionario
def info_para_tabla(diccionario):
    valores=list(diccionario.values())
    nombres=list(diccionario.keys())
    header = ['Nombre_abi','Numero_acceso','Nombre','E_value','%_identidad']
    i = 0
    while i<len(valores):
        valores[i].insert(0,nombres[i])
        i=i+1
    valores.insert(0,header)
    return valores 

# Función hacer la tabla a partir de un diccionario
# Esta función devuelve un archivo.csv llamado Resultados.csv en el directorio de trabajo 
def tabla_csv(diccionario):
    valores = info_para_tabla(diccionario)
    csvfile = open('Resultados.csv', 'w')
    csvwriter = csv.writer(csvfile, delimiter=';', dialect='excel')
    for item in valores:
        csvwriter.writerow(item)
    return csvfile.close()
    