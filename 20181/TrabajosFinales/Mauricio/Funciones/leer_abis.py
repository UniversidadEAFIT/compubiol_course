# EXTRAER ABIS DE UNA CARPETA"
# Mauricio Serna #
# 31 mayo 2018 #

# Función extraer abis de una carpteta. 
def leerabis(carpeta):
    import os
    abis = []
    for file in os.listdir(carpeta):
        if file.endswith(".ab1"):
            x = [os.path.join(carpeta,file)]
            abis= abis + x
    return abis