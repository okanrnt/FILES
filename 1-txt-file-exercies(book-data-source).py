# -*- coding: utf-8 -*-
import os

# shows current path
os.getcwd()

# takes to wanted path
os.chdir(path)

#opens a new file
def open_file(file_name):
    with open(file_name,encoding='utf - 8',mode='w') as f:
        f.write('ID,BOOK_NAME,AUTHOR,PUBLISHER,PAGE_COUNT')

#makes to save the book informations in the file.
def add_and_save_book(file_name):
        with open(file_name,encoding='utf - 8',mode='r') as f:
             data = f.readlines()
             ID = str(len(data))
             book_name = input('BOOK NAME: ')
             author = input('AUTHOR: ')
             publisher = input('PUBLISHER: ')
             page_count = input('PAGE COUNT: ')
             text = ['\n' + ID,book_name,author,publisher,page_count]
             new_text = ','.join(text)
        
        with open(file_name,encoding='utf - 8',mode='a') as f:
            f.write(new_text.title())
            print(f'The book has been added. ID NO: {ID}')
            
#deletes wanted book in the file.              
def del_book(file_name):
    while True:
        try:
            with open(file_name,encoding='utf - 8',mode='r+') as f:
                data = f.readlines()
                ID = int(input("BOOK'S 'ID NO: "))
                data.pop(ID)
                data.insert(ID,'Deleted,Deleted,Deleted,Deleted,Deleted\n')
                f.seek(0)
                f.writelines(data)
                f.truncate()
                print('The book has been deleted.')
                break
        except ValueError:
            print('Enter a number.')
        except IndexError:
            print('Pop index out of range.')
            
#updates the book information.
def update_information(file_name):
    while True:
        try:
            ID = int(input('ID NO: '))
            old = input('Which informations do you want to update?: ')
            new = input('New information: ')
            with open(file_name,encoding='utf - 8',mode='r+') as f:
                data = f.readlines()
                check_data = data[ID].split(',')
                new_data = data[ID].replace(old.title(), new.title())
                if old.title() in check_data:
                    data.pop(ID)
                    data.insert(ID, new_data)
                    f.seek(0)
                    f.writelines(data)
                    f.truncate()
                    print('Successful')
                    break
                else:
                    print('Wrong key.')
        except ValueError:
            print('Value Error.')
        except IndexError:
            print('Index Error.')

# gets wanted colon information in the file.
def get_information(file_name):
    while True:
        try:
            ID = int(input('ID NO: '))
            inf_colon = input('Which colons do you want to get?: ').upper()
            with open(file_name,encoding='utf - 8',mode='r') as f:
                data = f.readlines()
                for_index = data[0].split(',')
                new_list = data[ID].split(',')
                if inf_colon == 'PAGE_COUNT':
                    result = new_list[-1]
                    print(result)
                    break
                else:
                    find_index = for_index.index(inf_colon)
                    result = new_list[find_index]
                    print(result)
                    break
        except ValueError:
             print('Value Error.')
        except IndexError:
            print('Index Error.')

#gets all informations of the book in the file.
def get_all_informations_the_book(file_name):
    flag = True
    while flag:
        try:
            ID = int(input('ID NO: '))
            with open(file_name,encoding='utf - 8',mode='r') as f:
                data = f.readlines()
                inf_dict = {k : v for k in data[0].split(',') for v in data[ID].split(',') if data[0].split(',').index(k) == data[ID].split(',').index(v)}
                for k,v in inf_dict.items():
                    if k == 'PAGE_COUNT\n':
                        print(f"PAGE_COUNT : {v}")
                        flag = False   
                    else:
                        print(f"{k} : {v}")
        except ValueError:
             print('Value Error.')
        except IndexError:
            print('Index Error.')

#gives all book informations of inputed colon.                     
def get_all_informations_as_colon(file_name):
    flag = True
    while flag:
        try:
            colon_name = input('COLON NAME: ').upper()
            with open(file_name,encoding='utf - 8',mode='r') as f:
                data = f.readlines()
                new_data = data[0].split(',')
                data.pop(0)
                for i,v in enumerate(data,start=1):
                    new_v = v.split(',')
                    if colon_name == 'PAGE_COUNT':
                        print(f"ID NO: {i} <---> {colon_name}: {new_v[-1]}")
                        flag = False
                    else:
                        index_no = new_data.index(colon_name)
                        print(f"ID NO: {i} <---> {colon_name}: {new_v[index_no]}")
                        flag = False
        except ValueError:
            print('Value Error.')
            
#shows the data source(file).    
def show_data_source(file_name):
    os.system(file_name)
#Instance book: 1,Words,Bediüzzaman Said Nursi,Envar,--