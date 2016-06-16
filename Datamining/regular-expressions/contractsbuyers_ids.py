# coding: utf-8

############################################
# Author: Esteban F Ponce de Leon R        #
# Project: Al Tablero: Education Data Blog #
############################################

###############################################################
# About: This script was built in order to extract ids from   #
#        all public buyers                                    #
###############################################################

# import modules python 3
import re
from pandas import *

def removeNulls(mainList):
    mainList = filter(None, mainList)
    return list(mainList)

entidades = []
ids = []

with open('EntidadCompradora.txt', 'r') as f:
    
    for line in f:
        
        entidad = re.findall(r'.*\w[A-Z]+\w', line)
        entidad_id = re.findall(r'\b\d{5,15}\b', line)
        for item in entidad:
            entidades.append(item)
            entidades = removeNulls(entidades)
        for key in entidad_id:
            ids.append(key)
            ids = removeNulls(ids)

print ('Número total de entidades compradoras registradas:', len(entidades))
print ('Número total de ids registradas:', len(ids))

entidades_and_ids = {'Clave id': Series(ids),
                     'Entidad': Series(entidades)}

df = DataFrame(entidades_and_ids)
df.to_csv(path_or_buf='entidades.csv', sep=',', header=True, index=True, index_label='index')
