import csv
import os
def make_own_your_data_source(**kwargs):
    valuesList = []
    for v in kwargs.values():
        valuesList.append(v)
    
    #If there are no headers in the existing file, it adds. It does not open the file that does not exist
    #You can make a maximum of 254 column headers
    #Example usage
    #make_own_your_data_source(colon/header='any header',colon/header2='any header',...file='products.csv',process='add-header') 
    if valuesList[-1] == 'add-header':
        with open(valuesList[-2],encoding='utf-8',mode='r+',newline='') as file:    
            valuesList.pop(-2)
            valuesList.pop(-1)
            reader = csv.reader(file)
            new_reader = list(reader)
            writer = csv.writer(file)
            file.seek(0)
            writer.writerow(valuesList)
            valuesList.clear()
            writer.writerows(new_reader)
    
    
    #If there is no file, it opens and if there is a file, it adds to it
    elif valuesList[-1] == 'append-data':
        with open(valuesList[-2],encoding='utf-8',mode='a',newline='') as file:
            valuesList.pop(-2)
            valuesList.pop(-1)
            writer = csv.writer(file)
            writer.writerow(valuesList)
            valuesList.clear()
            
    #Example usage
    #make_own_your_data_source(colon/header='ProductName',file='products.csv',process='get-data')     
    elif valuesList[-1] == 'get-data':  #as all values of wanted colon/header
        with open(valuesList[-2],encoding='utf-8',mode='r',newline='') as file:
            reader = csv.reader(file)
            new_reader = list(reader)
            a = 0
            for i in range(256):
                try:
                    if valuesList[-3] == new_reader[0][a]:
                        del new_reader[0]
                        for value in new_reader:
                            #It starts printing from index 1.
                            print(f"{valuesList[-3]} : {value[a]}")
                        break
                except IndexError:
                    if a > 254:
                        print('list index out of range')    
                a += 1
    
    #Example usage
    #make_own_your_data_source(index='1',header/key='ProductName',value='Phone',file='products.csv',process='replace-data')
    elif valuesList[-1] == 'replace-data':
        with open(valuesList[-2],encoding='utf-8',mode='r+',newline='') as file:
            reader = csv.DictReader(file)
            dictReader = list(reader)
            headers = [k for k in dictReader[0].keys()]
            writer = csv.DictWriter(file,headers)
            writerheaders = csv.writer(file)
            new_value = dictReader[int(valuesList[-5])][valuesList[-4]]=valuesList[-3]
            file.seek(0)
            writerheaders.writerow(headers)
            writer.writerows(dictReader)
            file.truncate()
    
    #Example usage
    #make_own_your_data_source(index='2',file='products.csv',process='get-data') 
    elif valuesList[-1] == 'delete-data':  #specified index as the row
        with open(valuesList[-2],encoding='utf-8',mode='r+',newline='') as file:
            reader = csv.reader(file)
            writer = csv.writer(file)
            new_reader = list(reader)
            new_reader[int(valuesList[-3])].clear()
            for i in range(len(new_reader[0])):
                new_reader[int(valuesList[-3])].append('Deleted')
            file.seek(0)
            writer.writerows(new_reader)
            file.truncate()
        
    else:       
        print('Invalid key.')
    

#instance
#make_own_your_data_source(colon='ID',colon2='BOOK NAME',colon3='AUTHOR',colon4='PUBLISHER',colon5='PAGE',file='books.csv',process='add-header')
#make_own_your_data_source(colon='1',colon2='Nature: Cause or Effect?',colon3='Bediüzzaman Said Nursi',colon4='Sözler',colon5='80',file='books.csv',process='append-data')

    
    
    
    
    
    
            