import csv

#1- open and close a file
file = open('file_name.extension',mode,encoding)
file.close()

#2- read the file
reader = csv.reader(file)

#3- write to the file
writer = csv.writer(file)

#3- close the file automatically
with open("file_name", mode,encoding=) as file:
    print(file)

#4- print the headers and the first five rows
file = open('file_name.csv')
reader = csv.reader(file)
rows = list(reader)
headers = rows[0]
rows = rows[1:]

print(headers)
for row in range(5):
    print(rows[i])
file.close()    
    
    
#5- append the length of the name that be the first element of the list
file = open('file_name.csv')
reader = csv.reader(file)
reader = list(reader)
rows = reader[1:]

for row in rows:
    row.append(len(row[0]))

for i in range(5):
    print(rows[i])
    
file.close()    
    
#6- Convert the numeric string values from string type to float type
with open(file_name,mode="r",encoding="utf-8") as file:
    reader = csv.reader(file)
    reader = list(reader)
    rows = reader[1:]
    
    for row in rows:
        row[1] = float(row[1])
    
    for i in range(5):
        print(rows[i])
    
    print(type(rows[0][1]))


#7- #count how many of each item was sold
file = open(file_name)
reader = reader(file)
rows = list(reader)
sales_data = rows[1:]  # ignore column headers

# a frequency table with the sales
sales = {}
for data in sales_data:
    item_name = data[0]
    if item_name in sales:
        sales[item_name] += 1
    else:
        sales[item_name] = 1

# the frequencies
for key in sales:
    print(key)
file.close()    


#8- find out which neighborhoods have the most restaurants
file = open(file_name)
file_reader = reader(file)
rows = list(file_reader)[1:] # ignore column headers

#the frequency table
frequency = {}
for row in rows:
    neighborhood = row[1]
    if neighborhood in frequency:
        frequency[neighborhood] += 1
    else:
        frequency[neighborhood] = 1
# the maximum frequency and the correspoding restaurant
freq = 0
most_restaurants = None
for neighborhood,count in frequency.items():
    if count > freq:
        freq = count
        most_restaurants = neighborhood
print(freq)
print(most_restaurants)
file.close() 



#9- find two laptops on the list, such that their total price is exactly $5,000
file = open(file_name)
file_reader = reader(file)
rows = list(file_reader)[1:] # ignore column headers

# dictionary mapping the prices to the laptop names

price_to_name = {}
for row in rows:
    price = int(row[2])
    name = row[1]
    if price in price_to_name:
        price_to_name[price].append(name)
    else:
        price_to_name[price] = [name]
    
laptop1 = None
laptop2 = None
for row in rows:
    price = int(row[2])
    
    if price == 2500 and len(price_to_name[2500]) >= 2:
        laptop1 = price_to_name[2500][0]
        laptop2 = price_to_name[2500][1]
    elif 5000 - price in price_to_name:
        laptop1 = price_to_name[price][0]
        laptop2 = price_to_name[5000 - price][0]
        print(price)
    
file.close() 
   

    
#10- the function that returns the header index. If name of the header doesn't exist in the file, returns -1.
def find_col_index(csv_filename, col_name):
    #  read the CSV file
    file = open(csv_filename)
    reader = csv.reader(file)
    
    # the headers
    headers = list(reader)[0]
    
    # column index
    index = -1
    for header in headers:
        index += 1
        if col_name == header:
            return index
    return -1

# the value that wanted returns using the find_col_index function
def select(csv_filename, col_name, value):
    #  column index
    col_index = find_col_index(csv_filename, col_name)
    #  check if index is valid
    if col_index == -1:
        return None
    # CSV file without the header
    opened_file = open(csv_filename)
    read_file = reader(opened_file)
    rows = list(read_file)
    rows = rows[1:]
    # all matching rows
    result = []
    for row in rows:
        if row[col_index] == value:
            result.append(row)
    return result



#11- returns to read the number of rows that wanted
def read_partial_csv(csv_filename,num_rows=0):
    file = open(csv_filename)
    reader = csv.reader(file)
    rows = list(reader)
    if num_rows == 0:
        return rows
    else:
        return rows[:num_rows]