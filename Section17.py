"""
SECCTION PART 1

What is function?
   > A Process to executing a task
   > it can accept input and return output
   > useful for executing similar procedures over and over

Why use function?
    > stay DRY (do not repeat yourself)
    > clean up and prevent code duplication
    > 
"""

# built in function
colors = ['red', 'green', 'yellow', 'blue']
print(colors)
colors.clear()
print(colors)


# Defining Function
def function_name():
    name = "Rizal Ilham"
    print("This is how to define function")
    print("Yourname is {name}")

function_name()

# first quis
def make_noise():
    print("THE CROWD GOES WILD")

make_noise()

# The magic of return Keyword
def print_square_of_7(): #This function does not return anything
        print(7**2)

print_square_of_7()

def square_of_7(): 
        print("I AM BEFORE THE RETURN!")
        return 7**2
        print("I AM AFTER THE RETURN!")

result = square_of_7()
print(result)

# 150. Writing a coin flip funtion using random library
from random import random

def flip_coin():
    if random() > 0.5:
        return "HEADS"
    else:
        return "TAILS"
print(flip_coin())

# Quis
def speak_pig():
    return "oink"

# Quis 2
def generate_evens():
    result = [i for i in range(1, 50) if i % 2 == 0]
    return result
    
# 153. Function Parameters
def square(num=10, name="Rizal Ilham"):
        print(f"Your name {name}")
        return num * num

print(square(4))
print(square(8))

def divide(num1, num2):
        return num1/num2

print(divide(2,5))
print(divide(5,2))

# Quis 
def yell(text):
    return '{}!'.format(text.upper())
    
    
# 155. Common mistakes
#OLD-VERSION----OLD-VERSION----OLD-VERSION-----
def sum_odd_numbers(numbers): 
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
        return total #Returning too early :(
#OLD-VERSION----OLD-VERSION----OLD-VERSION-----


# NEW AND IMPROVED VERSION :)
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

print(sum_odd_numbers([1,2,3,4,5,6,7]))

# quis
# Without adding any new lines of code, make count_dollar_signs work as intended
def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count
    

# Default parameter
def information_user(name="Rizal Ilham", is_instructor=False):
    if name == "Rizal Ilham" and is_instructor:
        return f"Wellcome back Instructor {name}"
    elif name == "Rizal Ilham" and not is_instructor:
        return f"Wellcome back {name}"
    return f"Hello {name}"
    
information_user(name='Rizal Ilham', is_instructor=True)

# quis
# Define speak below:
def speak(animal='dog'):
    if animal == 'pig':
        return 'oink'
    elif animal == 'duck':
        return 'quack'
    elif animal == 'cat':
        return 'meow'
    elif animal == 'dog':
        return 'woof'
    else:
        return '?'
    return 'dog'
    

# Keyword argument

def exponent(num, power=2):
        return num ** power

# Order doesn't matter anymore, if we use key word arguments:
print(exponent(num=2,power=3)) #8
print(exponent(power=3, num=2)) #8

# Without keywords args, order still matters:
print(exponent(3,4)) #81
print(exponent(4,3)) #64


# Scode global and local variable
name = "Rizal Ilham" #global variable
def get_age():
    
    age = input("Your name?") #local variable
    print(age)
    
## global
total = 0
def up():
    global total #to update global variable use must use 'global' keyword
    total += 1
    return total
    
print(up())

## nonlocal
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()
