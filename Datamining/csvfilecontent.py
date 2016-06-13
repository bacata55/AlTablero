# coding: utf-8

############################################
# Author: Esteban F Ponce de Leon R        #
# Project: Al Tablero: Education Data Blog #
############################################

######################################################################
# About: This script was built in order to extract specific content  #
#         about education. We select key words in order to build a   #
#         dataset with education as a target.                        #
######################################################################

# import modules python 3

from pandas import DataFrame, Series
import pandas, time, re

def csv_grabber(filename):
    data = pandas.read_csv('data/' + filename + '.csv', low_memory=False, encoding='latin-1')
    
    # Create a new dataframe with education fields
    education_data = data[data['Objeto'].str.contains('PROGRAMA DE ALIMENTACI', flags = re.IGNORECASE)]
    
    if len(education_data) > 0:
        
        new_csvfile = education_data[ ['url', 'Número de Proceso', 'Tipo de Proceso', 'Estado',
                                       'Entidad Compradora', 'Objeto', 'Localidad', 'Cuantía',
                                       'Fecha  (dd-mm-aaaa)', 'Documento', 'Documento Representante'] ]
        
        while True:
            
            print ('')
            print ('Insert subject.')
            print ('')
            new_filename = filename
            subject = input('subject: ')
            print ('')
            print ('Are the subject ok:', subject + '?')
            validation = input('y / n: ').lower()
            print ('')
            
            if validation == 'y':
                
                new_csvfile.to_csv(path_or_buf = 'data/education_data/PAE/' + new_filename + '_' + subject + '.csv', sep=',',
                                   header=True, index=True, index_label='Index')
                
                print ('csvfile is saved')
                
                break
            
            else:
                continue
                
    else:
        
        print ('Database is empty')
        
    pass

if __name__ == '__main__':
    csv_grabber('QuibdoServiciosAlimentos')
