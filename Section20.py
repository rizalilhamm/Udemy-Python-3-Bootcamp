""" Lambda and Built in Function """

def square(num): return num * num

# using lambda
square2 = lambda num: num * num
print(square2(3))

# Map = a standard funtion that accept at least two argument, a function and aa "iterable"
nums = [2, 4, 6, 8, 10]
doubles = map(lambda x: x*2, nums)
result = []
for i in doubles:
    result.append(i)
print(result)

peoples = ['Rizal', 'Ilham', 'Ronaldo', 'Pak Selamat']
peoples_upper = map(lambda name: name.upper(), peoples)
result = []
for people in peoples_upper:
    result.append(people)
print(result)

names = [
    {'name': 'Marhdatika', 'school': 'Bustanul Ulum'},
    {'name': 'Rizal Ilham', 'school': 'UIN Ar-Raniry'},
    {'name': 'Kasmadi Ramadhan', 'school': 'Ubudiah'}
]

students = map(lambda name: name['name'], names)
result = []
for s in students:
    result.append(s)

print(result)
# Quis
def decrement_list(l):
    return list(map(lambda n: n-1, l))


# Filter = return filter object which can be convered into other iterables
names = ['aldo', 'anggi', 'radi']
a = filter(lambda name: name[0] == 'a', names)
print(list(a))

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#extract inactive users using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))

#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]

# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]
# Quis
def remove_negatives(nums):
    return list(filter(lambda x: x >= 0, nums))

# Implement your is_all_strings function below:
def is_all_strings(values):
    return all(type(i) == str for i in values)


# SORTED
# sorted = used to sort all type of collection
# sort = only available for list data structure
numbers = (1,3,2,6,5,4)
print(sorted(numbers))  # return a sorted list 
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

# To sort users by their username
sorted(users,key=lambda user: user['username'])

# Finding our most active users...
# Sort users by number of tweets, descending
sorted(users,key=lambda user: len(user["tweets"]), reverse=True)

# ANOTHER EXAMPLE DATA SET==================================
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# To sort songs by playcount
sorted(songs, key=lambda s: s['playcount'])


# MIN AND MAX
names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# finds the minimum length of a name in names
min(len(name) for name in names) # 3

# find the longest name itself
max(names, key=lambda n:len(n)) #Ollivander

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
min(songs, key=lambda s: s['playcount']) #{"title": "happy birthday", "playcount": 1}

# Finds the title of the most played song
max(songs, key=lambda s: s['playcount'])['title'] #YMCA

# Define extremes below:
def extremes(values):
    return (min(values), max(values))

# LEN
values  = [1,2,3,5]
print(values.__len__())
class SpecialList:
 
    def __init__(self, data):
        self.__data = data
 
    def __len__(self):  # JUST LOOK AT THIS LINE
        return max(self.__data)

l1 = SpecialList([1,40,30,100,30,1,2,3,4])
l2 = SpecialList([1,3,4,5]) 

print(len(l1)) #50
print(len(l2)) #50

def max_magnitude(nums):
    return max((abs(num) for num in nums))

def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)

'''
sum_floats(1.5, 2.4, 'awesome', [], 1) # 3.9
sum_floats(1,2,3,4,5) # 0
'''

def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)



# ZIP
midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']


# returns dict with {student:highest score} USING LIST COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}


# returns dict with {student:highest score} USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = dict(
	zip(
		students,
		map(
			lambda pair: max(pair),
			zip(midterms, finals)
		)
	)
)

# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
	zip(
		students,
		map(
			lambda pair: ((pair[0]+pair[1])/2),
			zip(midterms, finals)
		)
	)
)
print(avg_grades)
# Quis
def interleave(value1, value2):
    return ''.join(''.join(x) for x in zip(value1, value2))