# coding: utf-8

############################################
# Author: Esteban F Ponce de Leon R        #
# Project: Al Tablero: Education Data Blog #
############################################

###############################################################
# About: This script was built in order to extract ids from   #
#        Colombian departments                                #
###############################################################

# import modules python 3
import re
from pandas import *

def removeNulls(mainList):
    mainList = filter(None, mainList)
    return list(mainList)
    
departamentos = []
ids = []

# Open text file with Colombian departments ids
with open('DepartamentosID.txt', 'r') as f:

  for line in f:
    location = re.findall(r'\w[a-z]\w.*', line)
    departamento_id = re.findall(r'\d+', line)
    for item in location:
      departamentos.append(item)
      departamentos = removeNulls(departamentos)
      
    for key in departamento_id:
      ids.append(key)
      ids = removeNulls(ids)
      
# Borrar index específico
del departamentos[0]

print ('Número total de departamentos registrados:', len(departamentos))
print ('Número total de ids registradas:', len(ids))

# Create a DataFrame
departamentos_and_ids = {'Geo id': Series(ids),
                         'Departamento': Series(departamentos)}
                         
df = DataFrame(departamentos_and_ids)
df.to_csv(path_or_buf='departamentos.csv', sep=',', header=True, index=True, index_label='index')
