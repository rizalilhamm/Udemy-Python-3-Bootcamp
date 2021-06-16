# LIST
"""
Storing data in a variable with any type / 
Just a collection or grouping of items

Objectives
1. Describe, create and access a list of data structure
2. use built in methods to modify and copy list
3. iterate over lists using loops and list comprehensions
4. Work with nested list to build more complec data structures
"""

# Creating List
items = ["Python Language", "Java", "JavaScript"]
demo_list = [1, "This is a string", 1.0]

print(items)
print('Len of string', len(items))

r = range(1, 10)
print(list(r)) # use builtin function


# Accessing data in list
friends = ['Rizal', 'Ilham', 'Rizal Ilham']
rizal = friends[0]
ri = friends[2]
print(ri)
# accessing from the end of list
ilham = friends[-2]
print(ilham)
# check if a value in list
print('Rizal' in friends)
# Accessing all values in a list using for loop
result = []
for name in friends:
    result.append(name)
print(result)

# accessing all values using while loop
index = 0
while index < len(name):
    print(name[index])
    index += 1
    
# ITERATING OVE LISTS
# Quis
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = ''
for i in sounds:
    result += i.upper()
    
# LIST METHODS
"""
1. append
2. extend
3. insert
"""
data = [1,2,4,3]
data.append(5) #insert data at the end of list
data.append('purple')
print(data)
data.extend([10, 20, 30]) #insert multiple at the end of list 
print(len(data))
data.insert(2, 'Using insert') #insert a data into given position insert(position, data)
data.insert(-1, 'Before The end!')
data.insert(len(data), 'The end!')
print(data)

# Quis
# Create a list called instructors
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"

instructors = ['Colt', 'Blue', 'Lisa']
# Run the tests to make sure you've done this correctly!
print(instructors)

# LIST METHODS 2
"""
1. clear  = remove all data in the list
            if no index specified it will remove last item and return it
2. pop    = remove the item at the given position
3. remove = remove the first ite from the list whose value in x
            Throws ValueError if the item is not found
"""
print(data.pop(2))
last_item = data.pop()
print(data)
print(last_item)
data.remove(1) # remove 1 from list
print(data)
data.clear() #delete all data in the list

# LIST METHODS 3
"""
1. Index   = return the index of the specified item in the list
2. Count   = return the number of times x appears in the list
3. Sort    = sort the items of the list (in-place)
4. Reverse = reverse the element of the list (in-place)
5. Join    = (it is string method) used to join list to be a single string
             it return new string
"""
numbers = [5, 5, 6, 7, 8, 8, 9, 10]
print(numbers.index(6)) #2
print(numbers.index(9)) #4
print(numbers.index(5, 1)) # 1 | return index of 5 is in index 1
print(numbers.index(8, 4, 6)) #6 | return index of 5 between 4 to 6 
print(numbers.count('rizal')) #2
print(numbers)

numbers.reverse() #reverse
print(numbers)
numbers.sort() # sort
print(numbers)

words = ['Coding', 'is', 'fun']
print(' '.join(words)) # use space
print('. '.join(words)) # use .
print(' '.join(str(numbers)))