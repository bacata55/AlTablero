# coding: utf-8

############################################
# Author: Esteban F Ponce de Leon R        #
# Project: Al Tablero: Education Data Blog #
############################################

###############################################################
# About: This script was built in order to extract ids from   #
#        Colombian municipalities                             #
###############################################################

# import modules python 3
import re
from pandas import *

def removeNulls(mainList):
    mainList = filter(None, mainList)
    return list(mainList)

municipios = []
ids = []

with open('MunicipiosID.txt', 'r') as f:
    
    for line in f:
        
        location = re.findall(r'.*\w[a-z]+\w', line)
        municipio_id = re.findall(r'\d+', line)
        for item in location:
            municipios.append(item)
            municipios = removeNulls(municipios)
        for key in municipio_id:
            ids.append(key)
            ids = removeNulls(ids)

# Delete even or odd items
del ids[2::2]

print ('Número total de municipios registrados:', len(municipios))
print ('Número total de ids registradas:', len(ids))

municipios_and_ids = {'Geo id': Series(ids), 
                      'Municipio': Series(municipios)}

df = DataFrame(municipios_and_ids)
df.to_csv(path_or_buf='municipios.csv', sep=',', header=True, index=True, index_label='index')
