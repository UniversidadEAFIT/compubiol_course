from Bio import Entrez

def leerCampoSecuencia(entrezResponse, campo):
    data = entrezResponse.get(campo)
    lista = []
    if data is dict:
        for entry in data:
            lista.append(entry)
        return lista
    else:
        return data

def leerCampoTaxon(entrezResponse, campo):
    data = entrezResponse[0].get(campo)
    lista = []
    if data is dict:
        for entry in data:
            lista.append(entry)
        return lista
    else:
        return data

def leerCampoOrganismo(entrezResponse, campo):
    data = entrezResponse[0].get(campo)
    return data

def listarCampos(entrezResponse):
    lista = []
    for campo in entrezResponse.keys():
        lista.append(campo)
    return lista

def leerOrganismo(params):
    Entrez.email = 'vvelezs@eafit.edu.co' 
    ident = ""
    if "id" in params:
        ident = params["id"]
    else:
        ident = params[""]
    handle = Entrez.efetch(db="nucleotide", id=ident, rettype="gb", retmode="XML")
    return Entrez.read(handle)

def leerIdSecuencias(params):
    Entrez.email = 'vvelezs@eafit.edu.co'
    consulta=None
    if "orgn" in  params:
        consulta= params["orgn"]+"[ORGN]"
    handle = Entrez.esearch(db="nucleotide", term=consulta, idtype="acc")
    return Entrez.read(handle)

def leerRegistroDeTaxonomia(params):
    Entrez.email = 'vvelezs@eafit.edu.co' 
    id = ""
    if "id" in params:
        id = params["id"]
    else:
        id = params[""]
    handle = Entrez.efetch('taxonomy', id=id, rettype='xml')
    response = Entrez.read(handle)
    return response
