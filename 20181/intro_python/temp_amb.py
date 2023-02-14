#! /usb/bin/env python
# Tomando como ejemplo el siguiente script, modificar el codigo para retornar un texto diciendo: esta haciendo mucho calor o mucho frio
# Introduccion a la biologia, disculpen la falta de tildes. Es para no crear perturbacion en el codigo
# Autor: Universidad EAFIT
# Uso: python temp_amb.py

#Creacion de variable que se recibe de la consola el valor en grados fahrenheit de la temperatura ambiente
#Se cambia el tipo de objeto de str a float, averiguar que es esto
temp_actual = float(input("Entre la temperatura en grados Fahrenheit: "))

#funcion para cambiar de Fahrenheit a Celsus
def change_fatoce(temp_actual):
    TC = (temp_actual - 32.0) * 5/9
    return TC
    
#Guardo el valor calculado en celsus
TF = change_fatoce(temp_actual)


#Imprimo el resultado
print ("La temperatura en grados celsus es: " + str(TF) + "C")
#Porque hubo necesidad de volver TF un string?

# Apartir de aca hacer su propio codigo
# Pista: Utilicen los condicionales if, elif para evaluar si la temperatura esta muy baja o muy alta para nosotros

