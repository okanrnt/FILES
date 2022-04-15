import json
import os
#1- Convert from JSON to Python
y = json.loads(x)

#2- Convert from Python to JSON
y = json.dumps(x)
# the result is a JSON string

#3-define the numbers of indents
json.dumps(x, indent=4)

#4- change the default separator
json.dumps(x, indent=4, separators=(". ", " = "))

#5-specify if the result should be sorted or not
json.dumps(x, indent=4, sort_keys=True)



#Practice
'''make a user repository with json file'''

class User:
    def __init__(self,name,surname,status):
        self.name = name
        self.surname = surname
        self.status = status
          
class Repository:
    def __init__(self):
        self.userList = list()
        self.saveToFile()
    
    def register(self):
        name = input('NAME: ')
        surname = input('SURNAME: ')
        status = input('STATUS: ')
        
        user = User(name, surname, status)
        self.userList.append(user)
        self.saveToFile()
        print('User registered')

    def saveToFile(self):
        newUser = []
        for user in self.userList:
            user = json.dumps(user.__dict__)
            newUser.append(user)
        
        with open('try.json',encoding='utf-8',mode='w') as file:
            json.dump(newUser, file, ensure_ascii=False,indent=4)
    
    def loadsFile(self,key,value):
        if os.path.exists('try.json'):
            with open('try.json',encoding='utf-8',mode='r') as file:
                loadUser = json.load(file)
            for user in loadUser:
                user = json.loads(user)
                if user[key] == value:
                    print(user)
            
repo = Repository()            

while True:
    choose = input('1- Register\n2- Display the User\nq- Exit\nchoose: ')
    if choose == '1':
        repo.register()
        
    elif choose == '2':
        #If key and value are equivalent it prints the informations of the user
        key = input('Key: ')
        value = input('Value: ')
        repo.loadsFile(key, value)
        
    elif choose == 'q':
        print('Exit is successful')
        break

    else:
        print('Wrong key.')