# coding: utf-8

############################################
# Author: Esteban F Ponce de Leon R        #
# Project: Al Tablero: Education Data Blog #
############################################

######################################################################
# About: This script was built in order to extract public contracts. #
#        It allows to insert specific fields as department, city,    #
#        period of time, buyer, amount, etc.                         #
######################################################################

# import modules python 2.7

from bs4 import BeautifulSoup
import mechanize, csv, re
import time

# Creating empty lists for urls and items | web scraping

iframe = []
contractLinks = []
titleTables = []
textTables = []
documents = []


# Defining functions to clean text data | web scraping

# This function return 'n' number of lists within a list selecting 'x' number of items
def splitList(mainList):

    fields = [mainList[x:x+9] for x in range(0, len(mainList), 9)] # specifically we need to return a new list every 9 items
    return fields # This function will be use to clean Odd and Even text from results and then write a CSV file


# Url from contratos.gov.co
url = 'https://www.contratos.gov.co/consultas/inicioConsulta.do'


# Using Mechanize module to read url
br = mechanize.Browser()

# Browser options
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 )
br.addheaders = [('User-agent', 'Googlebot')]
# br.addheaders = [('User-agent', 'Firefox')]
# br.addheaders = [('User-agent', 'Feedfetcher-Google')]

# Reading the url
br.open(url)

# Display items
print ''
print 'Initiating Program', time.ctime()
print ''
print 'Opening main url'
print url
print ''


# Select and fill html form called 'parametros'
br.select_form('parametros')

# Display items
print ''
print 'Filling "Parametros" form'
print ''

# Select a specific Entidad Compradora
while True:
    print 'Do you want to enter an ID for an Entidad Compradora?'
    validation = raw_input('y / n: ').lower()
    print ''
    if validation == 'y':
        entidad_compradora = raw_input("Write the Entidad Compradora's ID: ")
        print 'is the ID correct:', entidad_compradora, '?'
        id_confirmation = raw_input('y / n: ').lower()
        print ''
        if id_confirmation == 'y':
            
            # Fixing html form for Entidad Compradora
            br.form.new_control( '_select', 'entidad', { 'value': entidad_compradora } )
            br.form.fixup()
            
            break
        
        elif id_confirmation == 'n':
            continue
            
        else:
            print 'Please type y or n'
            print ''
            continue
            
    elif validation == 'n':
        break
        
    else:
        print 'Please type y or n'
        print ''
        continue

# Select a specific service o product
while True:
    print 'Do you want to enter an ID for a specific product or service?'
    validation = raw_input('y / n: ').lower()
    print ''
    if validation == 'y':
        servicio = raw_input("Write the service or product's ID: ")
        print ''
        print 'is the ID correct:', servicio, '?'
        id_confirmation = raw_input('y / n: ').lower()
        print ''
        if id_confirmation == 'y':
            
            # Filling Products y Services values
            br.form['objeto'] = [servicio]
            
            break
            
        elif id_confirmation == 'n':
            continue
        
        else:
            print 'Please type y or n'
            print ''
            continue
    
    elif validation == 'n':
        break
        
    else:
        print 'Please type y or n'
        print ''
        continue

# Select 'Tipo de proceso'
while True:
    print 'Do you want to enter an ID for a specific "Tipo de Proceso"?'
    validation = raw_input('y / n: ').lower()
    print ''
    if validation == 'y':
        tipo_proceso = raw_input("Write the ID of 'Tipo de Proceso': ")
        print 'is the ID correct:', tipo_proceso, '?'
        id_confirmation = raw_input('y / n: ').lower()
        print ''
        if id_confirmation == 'y':
            
            # Fixing html form for Tipo de Proceso
            br.form.new_control( '_select', 'tipoProceso', { 'value': tipo_proceso } )
            br.form.fixup()
            
            break
            
        elif id_confirmation == 'n':
            continue
        
        else:
            print 'Please type y or n'
            print ''
            continue

    elif validation == 'n':
        break
        
    else:
        print 'Please type y or n'
        print ''
        continue

# Select a specific department
while True:
    print 'Do you want to enter an ID for a specific Colombian department?'
    validation = raw_input('y / n: ').lower()
    print ''
    if validation == 'y':
        departamento = raw_input("Write the department's ID: ")
        print ''
        print 'is the ID correct:', departamento, '?'
        id_confirmation = raw_input('y / n: ').lower()
        print ''
        if id_confirmation == 'y':
                
            # Fixing html form for Departamentos
            br.form.new_control( '_select', 'departamento', { 'value': departamento } )
            br.form.fixup()
            
            break
            
        elif id_confirmation == 'n':   
            continue
            
        else:
            print 'Please type y or n'
            print ''
            continue
    
    elif validation == 'n':
        break
        
    else:
        print 'Please type y or n'
        print ''
        continue
        
# Select a specific municipality
while True:
    print 'Do you want to enter an ID for a specific municipality from this ' + str(departamento) + ' Department id?' 
    validation = raw_input('y / n: ').lower()
    print ''
    if validation == 'y':    
        municipio = raw_input("Write the municipality's ID: ")
        print ''
        print 'is the ID correct:', municipio, '?'
        id_confirmation = raw_input('y / n: ').lower()
        print ''
        if id_confirmation == 'y':
                    
            # Fixing html form for Municipios
            br.form.new_control( '_select', 'municipio', { 'value': municipio } )
            br.form.fixup()
                
            break
                    
        elif id_confirmation == 'n':       
            continue
            
        else:
            print 'Please type y or n'
            print ''
            continue
            
    elif validation == 'n':
        break
        
    else:
        print 'Please type y or n'
        print ''
        continue

# Select a period of time
while True:
    print 'Select a period of time. This field must be filled'
    print ''
    Inicio = raw_input('From (dd/mm/yyyy): ')
    Final = raw_input('To (dd/mm/yyyy): ')
    print ''
    print 'Is the period of time correct:', 'From', Inicio, 'To', Final, '?'
    validation = raw_input('y / n: ').lower()
    print ''
    if validation == 'y':
        
        br.find_control("fechaInicial").readonly = False
        br.form['fechaInicial'] = Inicio
        
        br.find_control("fechaFinal").readonly = False
        br.form['fechaFinal'] = Final
        
        break
        
    elif validation == 'n':
        continue
        
    else:
        print 'Please type y or n'
        print ''
        continue

# Select a specific amount
while True:
    print 'Do you want to enter a specific amount?'
    validation = raw_input('y / n: ').lower()
    print ''
    if validation == 'y':
        one =   '$0 - $100,000,000'
        two =   '$100,000,001 - $300,000,000'
        three = '$300,000,001 - $500,000,000'
        four =  '$500,000,001 - $1,000,000,000'
        five =  'More than $1,000,000,000'
        print 'Enter 1 for', one
        print 'Enter 2 for', two
        print 'Enter 3 for', three
        print 'Enter 4 for', four
        print 'Enter 5 for', five
        print ''
        cantidad = raw_input("Select one option mentioned above: ")
        print ''
        if cantidad == '1':
            print 'You choose ' + str(one) + '. ' + 'Is correct?'
            confirmation = raw_input('y / n: ').lower()
            print ''
            if confirmation == 'y':
                
                # Filling amount field
                br.form['cuantia'] = [cantidad]
                
                break
            
            elif confirmation == 'n':       
                continue
                
            else:
                print 'Please type y or n'
                print ''
                continue
        
        elif cantidad == '2':
            print 'You choose ' + str(two) + '. ' + 'Is correct?'
            confirmation = raw_input('y / n: ').lower()
            print ''
            if confirmation == 'y':
                
                # Filling amount field
                br.form['cuantia'] = [cantidad]
                
                break
            
            elif confirmation == 'n':
                continue
                
            else:
                print 'Please type y or n'
                print ''
                continue
        
        elif cantidad == '3':
            print 'You choose ' + str(three) + '. ' + 'Is correct?'
            confirmation = raw_input('y / n: ').lower()
            print ''
            if confirmation == 'y':

                # Filling amount field
                br.form['cuantia'] = [cantidad]
                
                break
            
            elif confirmation == 'n':
                continue
                
            else:
                print 'Please type y or n'
                print ''
                continue
                
        elif cantidad == '4':
            print 'You choose ' + str(four) + '. ' + 'Is correct?'
            confirmation = raw_input('y / n: ').lower()
            print ''
            if confirmation == 'y':
                
                # Filling amount field
                br.form['cuantia'] = [cantidad]
                
                break
            
            elif confirmation == 'n':
                continue
                
            else:
                print 'Please type y or n'
                print ''
                continue
                
        elif cantidad == '5':
            print 'You choose ' + str(five) + '. ' + 'Is correct?'
            confirmation = raw_input('s / n: ').lower()
            print ''
            if confirmation == 's':
                
                # Filling amount field
                br.form['cuantia'] = [cantidad]
                
                break

            elif confirmation == 'n':
                continue
                
            else:
                print 'Please type y or n'
                print ''
                continue
                
        else:
            print 'Please type a single value: 1 to 5'
            print ''
            continue
    
    elif validation == 'n':
        break
        
    else:
        print 'Please type y or n'
        print ''
        continue

# Number of result per page
br.form['registrosXPagina'] = ['50']

# Submit information
print 'Submiting information'
print ''
    
response = br.submit()

# Creating a variable with the submit information and read it | 
# Search 1 = Primer formulario en https://www.contratos.gov.co/consultas/inicioConsulta.do
searchOne = response.read()

# First sleep parameter
time.sleep(10)

# Calling BeautifulSoup to find the iframe tag | It contains the url from Search 1
soup = BeautifulSoup(searchOne, 'lxml')
iframes = soup.findAll('iframe')

# A for loop to get iframe's src
for src in iframes:

    result = src.get('src')
    href = 'https://www.contratos.gov.co/consultas/' + str(result)
    iframe.append(href)
    
# display items
print ''
print 'Display search url'
print ''
print iframe[2]
print ''


# Reading search url
scndUrl = iframe[2]
searchTwo = br.open(scndUrl).read()

# Second sleep parameter
time.sleep(15)

# Calling BeautifulSoup to find 'total number of results'
beauty = BeautifulSoup(searchTwo, 'lxml')
pages = beauty.findAll('p', {'class': 'resumenResultados'})

for t in pages:
    
    text = t.text.replace('\t', '').replace('\n', '').replace('\r', '').encode('utf-8')
    
    # Using re module to find digits anywhere within the text (i.e. h33llo and 77) | Result = 33 and 77
    allDigits = re.findall(r'[-+]?\d+[\.]?\d*', text)

resultados = int(allDigits[0]) # item [0] represents the total number of results
print ''
print 'The total number of results are', resultados

# Display items
print ''
print 'Getting number of pages...'
print ''

# Finding the total number of pages
resultsPerPage = 50
totalResults = resultados
totalOfPages = (float(totalResults) / float(resultsPerPage)) + 1 # + 1 represents the sum = total number of pages
rangePages = int(totalOfPages) + 1 # + 1 represents the sum = stop range

# Display items
print 'The total number of pages are ' + str(int(totalOfPages))
print ''

# Total number of pages range
i = range(1, rangePages)

# Select html form called 'resultados' | Extract titles from results table
# All titles are the same for each page
br.select_form('resultados')
br.find_control("paginaActual").readonly = False
br.form['paginaActual'] = '1'
br.find_control("paginaObjetivo").readonly = False
br.form['paginaObjetivo'] = '1'

# Submit form | Response 2 from Second form
scndResponse = br.submit()

# Display items
print 'Extracting titles...'
print ''

# Creating a variable with the submit information and read it | Search 3
searchThree = scndResponse.read()

# Calling BeautifulSoup to extract titles from tables
getTitle = BeautifulSoup(searchThree, 'lxml')
titleTable = getTitle.findAll('div', {'align': 'center'})

for title in titleTable:

    titles = title.text.encode('utf-8')
    titleTables.append(titles)
    
# Append new element
titleTables.insert(0, 'url')
titleTables.append('Documento')
titleTables.append('Documento Representante')
titleTables[1] = 'Item id'
titleTables[5] = 'Entidad Compradora'
titleTables[7] = 'Localidad'

# Display items
print 'The total number of titles are', len(titleTables)
print ''


# Create a CSV file to save data
while True: 
    print ''
    print 'Save information in CSV file.'
    print ''
    CSVfileName = 'data/' + raw_input('Write CSV filename: ') + '.csv'
    print ''
    print 'Path and CSV filename: ' + '"' + CSVfileName + '"' + ' is correct?'
    validation = raw_input('y / n: ').lower()
    print ''
    if validation == 'y':
        break
    elif validation == 'n':
        continue
    else:
        print 'Please type y or n'
        print ''
        continue

# Display items
print 'CSV filename saved'
print ''

# Write CSV file with the items from titleTables
print 'Writing titles on CSV file'
print ''

with open(CSVfileName, 'ab') as f:
         writer = csv.writer(f, delimiter=',')
         writer.writerow(titleTables)


# Create a text file to save all contracts links
while True: 
    print ''
    print 'Save contracts links in text file.'
    print ''
    txtFileName = 'data/' + raw_input('Write text filename: ') + '.txt'
    print ''
    print 'Path and text filename: ' + '"' + txtFileName + '"' + ' is correct?'
    validation = raw_input('y / n: ').lower()
    print ''
    if validation == 'y':
        break
    elif validation == 'n':
        continue
    else:
        print 'Please type y or n'
        print ''
        continue

# Display items
print 'Text filename saved'
print ''

# Third sleep parameter
time.sleep(15)

# Extract contract links from all number of pages

##############################
# Bloque 1: contracts links  #
##############################

print ''
print 'Start', time.ctime()
print ''

for page in range(len(i)):
    
    # Select html form called 'resultados'
    br.select_form('resultados')
    br.find_control("paginaActual").readonly = False
    br.form['paginaActual'] = str(i[page])
    br.find_control("paginaObjetivo").readonly = False
    br.form['paginaObjetivo'] = str(i[page])
    
    # Submit form | Response 3 from Second form
    thrdResponse = br.submit()
    
    # Creating a variable with the submit information and read it | Search 4
    searchFour = thrdResponse.read()
    print 'Reading and saving links from page number ' + str(i[page]) + ' of ' + str(int(totalOfPages))
    
    # Calling BeautifulSoup to find all <a> tags and get 'href' links
    getHref = BeautifulSoup(searchFour, 'lxml')
    linkContracts = getHref.findAll('a')
    
    for contract in linkContracts:
        
        # Get href
        contra = contract.get('href')
        
        # Add the base url
        href = 'https://www.contratos.gov.co' + str(contra)
        
        # Replace the items we do not need from href content
        contractLink = href.replace("javascript: ", "").replace("popUpSecop('", "").replace("')", "")
        
        # Save results in contractLinks list
        contractLinks.append(contractLink)
        
        ###################################
        # save contractLinks in text file #
        ###################################
        
        savetxt = open(txtFileName, 'a')
        savetxt.write(str(contractLink) + '\n')
        savetxt.close()

# Display items
print ''
print 'All links are saved in:', txtFileName
print ''
print 'End', time.ctime()
print ''

# Third sleep parameter
time.sleep(60)

# Extract text | Relevant elements from contracts.

#############################################
# Bloque 2: Extract text from table results #
#############################################

print ''
print 'Start', time.ctime()
print ''

for page in range(len(i)):
    
    # Select html form called 'resultados'
    br.select_form('resultados')
    br.find_control("paginaActual").readonly = False
    br.form['paginaActual'] = str(i[page])
    br.find_control("paginaObjetivo").readonly = False
    br.form['paginaObjetivo'] = str(i[page])
    
    # Submit form | Response 4 from Second form
    fourResponse = br.submit()
    
    # Creating a variable with the submit information and read it | Search 5
    searchFive = fourResponse.read()
    print 'Reading information from page number ' + str(i[page]) + ' of ' + str(int(totalOfPages))
    
    # Calling BeautifulSoup to extract text from Odd fields
    getTextOdd = BeautifulSoup(searchFive, 'lxml')
    textTableOdd = getTextOdd.findAll('td', {'class': 'tablaslistOdd'})
    
    for textoOdd in textTableOdd:

        # Append text from Odd fields to textTables list
        resultOdd = textoOdd.text.replace("\t", "").replace("\r", "").replace('\n', '').encode('utf-8')
        textTables.append(resultOdd)
        
    # Calling BeautifulSoup to extract text from Even fields
    getTextEven = BeautifulSoup(searchFive, 'lxml')
    textTableEven = getTextEven.findAll('td', {'class': 'tablaslistEven'})
    
    for textoEven in textTableEven:

        # Append text from Even fields to textTables list
        resultEven = textoEven.text.replace("\t", "").replace("\r", "").replace('\n', '').encode('utf-8')
        textTables.append(resultEven)
        
# Create a new variable which contains 'textTables' items using 'splitList' function
textResults = splitList(textTables)
    
# Display items
print ''
print 'All the information is read.'
print ''
print 'End', time.ctime()
print ''

# Third sleep parameter
time.sleep(180)

# Extract documents | Nit & Citizen id from all links

################################
# Bloque 3: Nit and Citizen id #
################################

print ''
print 'Start', time.ctime()
print ''

for link in range(len(contractLinks)):
    
    # Reading links from contractLinks list  | Search 6
    searchSix = br.open(contractLinks[link])
    fiveResponse = searchSix.read()
    
    print 'Reading and saving documents from link: ' + str(link + 1) + ' of ' + str(len(contractLinks))
    
    sopa = BeautifulSoup(fiveResponse, 'lxml')
    
    temp_doc = []
    
    for t in sopa.findAll('td', {'class': 'tablaslistOdd'}):
        
        texto = t.text.replace("\t", "").replace("\r", "").replace('\n', '').encode('utf-8')
        
        # Searching for Nit and Document - Citizen id within links
        nit = re.search('(Nit de.*)', texto)
        documento = re.search('(Cédula de.*)', texto)
        carnet = re.search('(Carné Diplomático.*)', texto)
        
        if nit:
            
            temp_doc.append(nit.group())
            
        elif documento:
            
            temp_doc.append(documento.group())
        
        elif carnet:
            
            temp_doc.append(carnet.group())
            
    if len(temp_doc) == 0:
        temp_doc.append('Null')
        temp_doc.append('Null')
        documents.append(temp_doc)
    
    elif len(temp_doc) == 1:
        temp_doc.append('Null')
        documents.append(temp_doc)
    
    else:
        documents.append(temp_doc)

# Display items
print ''
print 'All documents are saved in documents list.'
print ''
print 'documents list contains', len(documents), 'lists.'
print ''
print 'End', time.ctime()
print ''


# Sort lists from textResults list by index[0] = Item ID
textResults.sort(key=lambda z: int(z[0]))

# Append items from contractLinks list to textResults lists
for i in range(0, len(textResults)):
    textResults[i].insert(0, contractLinks[i])

# Append items from documents list to textResults lists
for i in range(0, len(textResults)):
    textResults[i].extend(documents[i])


# Writing CSV file with all data
for result in textResults:
    
    # Add text results
    with open(CSVfileName, 'ab') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(result)

print ''
print 'CSV file is saved in', CSVfileName
print ''
print 'Program Ending', time.ctime()
