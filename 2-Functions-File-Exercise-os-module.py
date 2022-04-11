# -*- coding: utf-8 -*-
import os

#file_name = input('Please enter a path or file name: ')   # optional

def open_file(file_name):   #1
    
    with open(file_name,encoding='utf-8',mode = 'w') as f:   
        f.write('ID,NAME,SURNAME,YEAR_OF_BIRTH')

def add_member_and_save_to_file(file_name,number): #2 
    for i in range(int(number)):  #Number of members to add 
        with open(file_name,encoding='utf-8',mode = 'r') as f:
            data = f.readlines()        # read the file as a list.
            ID = str(len(data))        #  assignment length of the file as ID specify.
            NAME = input('NAME: ').upper()
            SURNAME = input('SURNAME: ').upper()
            YEAR_OF_BIRTH = input('YEAR OF BIRTH: ')
            string = ['\n' + ID,NAME,SURNAME,YEAR_OF_BIRTH]
            new_string = ','.join(string) #convert the list to a string.
            print(f"The member added. Member's ID No is {ID}.") 
            with open(file_name,encoding='utf-8',mode = 'a') as f:
                f.write(new_string)  # append the string statement the file.
        
def update_information(file_name,ID,exist,change):   #3
    
    exist = exist.upper()
    change = change.upper()
    ID = int(ID)
    
    with open(file_name,encoding='utf-8',mode = 'r+') as f:
        data = f.readlines()            # read the file as a list.
        new_data = data[ID].replace(exist,change)   # access inside the list informations with ID.
        data.insert(ID,new_data)# insert the changed information using the insert method of the list class
                                #to the data list.
        data.pop(ID + 1)        # remove the floating index because of the insert method.
        del new_data        #delete that made above string statement.
        f.writelines(data)  
        
    with open(file_name,encoding='utf-8',mode = 'w') as f:
        f.writelines(data) 
        print('Updated information.')
        
def delete_member(file_name,ID):   #4
    
    with open(file_name,encoding='utf-8',mode = 'r+') as f:
        data = f.readlines()
        data.pop(ID)
        data.insert(ID,"Deleted,Deleted,Deleted,Deleted\n")
        f.seek(0)    #reset cursor
        f.writelines(data)  # write the data as a list to the file.
        f.truncate()     # clean the discards.
        print('Deleted the member.')
        

def get_information(file_name,ID,want):   #5
    
    want = want.upper()
    if want == 'YEAR_OF_BIRTH':
        want = 'YEAR_OF_BIRTH\n'
    with open(file_name,encoding='utf-8',mode = 'r') as f:
        data = f.readlines()    # read the file as a list.
        try_data = data[0].split(',')  # separate with comma by convert the zeroth index of the list 
                                        #a list using the split method.
        want1 = try_data.index(want)    # get the index of the wanted.
        new_data = data[ID].split(',')    
        want2 = new_data[want1]
        if want == 'YEAR_OF_BIRTH\n':
            print(f"The YEAR OF BIRTH of the member is {want2}")
        else:
            print(f"The {want} of the member is {want2}.")
    
def get_all_information(file_name,ID):    #6
    
    with open(file_name,encoding='utf-8',mode = 'r') as f:
        data = f.readlines()
        print(data[0] + data[ID])
    
def get_all_informations_as_colon(file_name,colon_name):  #7
    if colon_name == 'YEAR_OF_BIRTH':
        colon_name = 'YEAR_OF_BIRTH\n'
        
    with open(file_name,encoding='utf-8',mode = 'r') as f:
        
        data = f.readlines()
        colon_data = data[0].split(',')
        colon_index = colon_data.index(colon_name)
        data.pop(0)
        for i,strr in enumerate(data, start=1):
            str_list = strr.split(',')
            if colon_name == 'YEAR_OF_BIRTH\n':
                print(f"ID NO: {i} --- YEAR_OF_BIRTH: {str_list[colon_index]}")
                
            else:
                
                print(f"ID NO: {i} --- {colon_name}: {str_list[colon_index]}")
    

def display_the_file(file_name):   #8
    
    os.system(file_name)