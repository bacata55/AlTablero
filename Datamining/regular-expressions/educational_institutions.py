# coding: utf-8

############################################
# Author: Esteban F Ponce de Leon R        #
# Project: Al Tablero: Education Data Blog #
############################################

################################################################
# About: This script was built in order to extract educational #
#        institutions ids from html file.                      #
################################################################

# import modules python 3
import re
from pandas import *

def removeNulls(mainList):
    mainList = filter(None, mainList)
    return list(mainList)

establecimientos = []
ids = []

with open('EstablecimientosQuibdo.txt', 'r') as f:
    
    for line in f:
        
        establecimiento = re.compile(r'">\d+(.*?)</option>')
        result = establecimiento.findall(line)
        establecimientos.extend(result)
        est_id = re.findall(r'"(\d+)"', line)
        ids.extend(est_id)
        
print ('')
print ('Número total de establecimientos registrados:', len(establecimientos))
print ('Número total de ids registradas:', len(ids))

establecimientos_and_ids = {'Clave id': Series(ids),
                            'Establecimiento': Series(establecimientos)}

df = DataFrame(establecimientos_and_ids)
df.to_csv(path_or_buf='establecimientos_quibdo.csv', sep=',', header=True, index=True, index_label='index')
