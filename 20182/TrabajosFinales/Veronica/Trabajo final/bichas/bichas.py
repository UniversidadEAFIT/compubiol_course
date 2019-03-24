import listaNCBI
import os
import platform

responseTaxon = None
responseSecuencias = None
responseOrganismo = None
ayudaPrompt = ""

def limpiarPantalla():
    if platform.system() == "Darwin" or platform.system() == "Linux":
        os.system("clear")
    if platform.system() == "Windows":
        os.system("cls")


def taxonLeer(params):
    global responseTaxon
    if params == None:
        print("ERROR: falta criterio de búsqueda")
        return

    print("\nConsultando base de datos en el servidor NCBI (puede tardar)...")
    responseTaxon = listaNCBI.leerRegistroDeTaxonomia(params)
    if len(responseTaxon) == 0:
        print("no se encontró nada con ese criterio.")
    else:
        print("---------------")
        taxonMostrarData("ScientificName")
    return

def leerOrganismo(params):
    global responseOrganismo
    if params == None:
        print("ERROR: falta id")
        return
    print("\nConsultando base de datos en el servidor NCBI (puede tardar)...")
    responseOrganismo = listaNCBI.leerOrganismo(params)
    if len(responseOrganismo) == 0:
        print("no se encontró nada con ese criterio.")
    else:
        print("---------------")
        organismoMostrarData("GBSeq_organism")
    return responseOrganismo

def leerIdSecuencias(params):
    global responseSecuencias

    if params == None:
        print("ERROR: falta criterio de búsqueda")
        return
  
    print("\nConsultando base de datos en el servidor NCBI (puede tardar)...")
    responseSecuencias = listaNCBI.leerIdSecuencias(params)
    if len(responseSecuencias) == 0:
        print("no se encontró nada con ese criterio.")
    else:
        print("---------------")
        print(responseSecuencias["Count"], "registros que cumplen.")
    return

def organismoListarCampos():
    global responseOrganismo   
    if responseOrganismo == None:
        print("no ha consultado nada. Use el comando 'leer'.")
        return
    print()
    print("------------------")
    organismoMostrarData("GBSeq_definition")
    print("------------------")
    lista = listaNCBI.listarCampos(responseOrganismo[0])
    for dato in lista:
        print(dato,end='\n')
    print()
    return

def taxonListarCampos():
    global responseTaxon   
    if responseTaxon == None:
        print("no ha consultado nada. Use el comando 'leer'.")
        return
    print()
    print("------------------")
    taxonMostrarData("ScientificName")
    print("------------------")
    lista = listaNCBI.listarCampos(responseTaxon[0])
    for dato in lista:
        print(dato,end='\n')
    print()
    return

def secuenciasListarCampos():
    global responseSecuencias   
    if responseSecuencias == None:
        print("no ha consultado nada. Use el comando 'leer'.")
        return
    print()
    print("------------------")
    secuenciasMostrarData("QueryTranslation")
    print("------------------")
    lista = listaNCBI.listarCampos(responseSecuencias)
    for dato in lista:
        print(dato,end='\n')
    print()
    return

def organismoMostrarData(campo):
    global responseOrganismo   
    if responseOrganismo == None:
        print("no ha consultado nada. Use el comando 'leer'.")
        return
    if campo == None:
        print("ERROR: falta campo")
        return
    dato = listaNCBI.leerCampoOrganismo(responseOrganismo, campo)
    print(dato)
    print()
    return

def taxonMostrarData(campo):
    global responseTaxon   
    if responseTaxon == None:
        print("no ha consultado nada. Use el comando 'leer'.")
        return
    if campo == None:
        print("ERROR: falta campo")
        return
    dato = listaNCBI.leerCampoTaxon(responseTaxon, campo)
    print(dato)
    print()
    return

def secuenciasMostrarData(campo):
    global responseSecuencias   
    if responseSecuencias == None:
        print("no ha consultado nada. Use el comando 'leer'.")
        return
    if campo == None:
        print("ERROR: falta campo")
        return
    dato = listaNCBI.leerCampoSecuencia(responseSecuencias, campo)
    print(dato,end='\n')
    return


def finalizar():
    global nomas 
    nomas = True
    return

def partacomando(linea):
    global nomas
    partes = linea.split(' ')
    dic={}
    if len(partes) > 1:
       comando = partes[0].upper()
       params = partes[1].split(';')
       for p in params:
           namevalue = p.split("=")
           if len(namevalue)<2:
               if not namevalue[0] in dic:
                   dic[""] = namevalue[0]
           else:
               if not namevalue[0] in dic:
                    dic[namevalue[0]] = namevalue[1]
    else:
       comando = partes[0].upper()
    return comando, dic

def leerComando(linea):
    global ayudaPrompt
    if len(linea)==0:
        return
    comando, params = partacomando(linea.strip())

    #comandos para que el usuario no tenga que escribir mucho....

    #comandos para fijar el tipo de acción...
    if comando == "TAXON.": ayudaPrompt="taxon."; return
    if comando == "ORGANISMO.": ayudaPrompt="organismo."; return
    if comando == "SECUENCIAS.": ayudaPrompt="secuencias."; return
    if comando == "TAXON.DATA.": ayudaPrompt="taxon.data"; return
    if comando == "ORGANISMO.DATA.": ayudaPrompt="organismo.data"; return
    if comando == "SECUENCIAS.DATA.": ayudaPrompt="secuencias.data"; return

    #comandos para quitar un tipo de acción fijo...
    if comando == "TAXON..": ayudaPrompt=""; return
    if comando == "ORGANISMO..": ayudaPrompt=""; return
    if comando == "SECUENCIAS..": ayudaPrompt=""; return
    if comando == "TAXON.DATA..": ayudaPrompt="taxon."; return
    if comando == "ORGANISMO.DATA..": ayudaPrompt="organismo."; return
    if comando == "SECUENCIAS.DATA..": ayudaPrompt="secuencias."; return

    #comandos para fijar las órdenes de listar campos...
    if comando == "TAXON.LISTARCAMPOS": taxonListarCampos(); return
    if comando == "ORGANISMO.LISTARCAMPOS": organismoListarCampos(); return
    if comando == "SECUENCIAS.LISTARCAMPOS": secuenciasListarCampos(); return
    if comando == "LIMPIAR": limpiarPantalla(); return
    if comando == "FIN": finalizar(); return

    if len(params) > 0:
        #comandos que requieren sólo un parámetro por el momento.....
        if comando == "TAXON.DATA": taxonMostrarData(params[""]);return
        if comando == "ORGANISMO.DATA": organismoMostrarData(params[""]);return
        if comando == "SECUENCIAS.DATA": secuenciasMostrarData(params[""]);return

        #comandos que necesitan parámetros
        if comando == "TAXON.LEER" : taxonLeer(params);return
        if comando == "ORGANISMO.LEER" : leerOrganismo(params);return
        if comando == "SECUENCIAS.LEER" :leerIdSecuencias(params);return

    print("Comando sin efecto, o falta parámetro, o el comando es desconocido.")


def pedirComando():
    global ayudaPrompt
    while (not nomas):
        linea = input("Bichas > "+ayudaPrompt)
        linea = ayudaPrompt+linea
        leerComando(linea)

def main():
    global nomas
    nomas = False
    pedirComando()

main()