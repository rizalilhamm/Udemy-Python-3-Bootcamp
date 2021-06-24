""" Introduction to *args used for tuple """

# COURSE 176
print('MANUAL PARAMETHER')
def sum_all_num(num1, num2, num3, num4=0, num5=0):
    result = num1 + num2 + num3 + num4 + num5
    return result
print(sum_all_num(num1=1, num2=2, num3=3))

print('USING *ARGS')
def sum_all_num2(*args):
    print(type(args))  # this is will return Tuple
    total = 0
    for num in args:
        total += num

    return total
print(sum_all_num2(1,2,3,5,5))

# Another example
def ensure_correct_info(*args):
    print(args)
    if 'Rizal' in args and 'Ilham' in args:
        return 'Hello {} {}'.format('Rizal', 'Ilham')
    return "You are anonymous!"

print(ensure_correct_info())
print(ensure_correct_info('Rizal', 'Ilham'))

# Quis
def contains_purple(*args):
    if 'purple' in args: return True
    return False

print(contains_purple(25, 'purple'))
print(contains_purple('green', False, 37, 'blue', 'hello world'))


""" Introduction to **kwargs (keyword and argument) used for dictonary"""
print('LEARNING **KWARGS')
def nilai(**nilai):
    print(nilai)

def print_student_score(**hasil_ujian):
    for person, nilai in hasil_ujian.items():
        print(f"{person} mendapatkan nilai {nilai}")

nilai(rizal=1, ilham=2, aldo=3, wati=19)
print_student_score(rizal=100, ilham=200, andi=300, tika=12)

def special_greeting(**kwargs):
    if 'David' in kwargs and kwargs['David'] == 'special': 
        return 'You got a special greeting David'
    elif 'David' in kwargs:
        return f"{kwargs['David']} David!"
    return 'Not sure who is this...'
print(special_greeting(David='Hello'))
print(special_greeting(Rizal='Hello there'))
print(special_greeting(David='special'))

# Quis
# Define combine_words below:
"""
if prefix:
    return prefix followed by the [word]
if suffix:
    return profix followed by the [suffix]
return word
"""
def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word
# Ordering paremeter
"""
1. Parameters
2. *args
3. default parameters
4. **kwargs
"""
def display_info(a, b, *args, intructor='Colt', **kwargs):
    # return all values in list 
    return [a, b, args, intructor, kwargs]

print(display_info(1, 2, 3, last_name='Steele', job='Intructor'))

# Tuple Unpacking (using * as an argument tuple unpacking)
def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)

num = [1,2,3,4,5] 
# user *args parameters
sum_all_values(*num)
# Quis
# NO TOUCHING! =================================================================
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# NO TOUCHING! =================================================================

# Write your code below:
result1 = count_sevens(1,2,7)
result2 = count_sevens(*nums)

# Dictionary Unpacking (using ** as an argument dictionary unpacking)
def display(first, second):
    return f'{first.upper()} say hello to {second.upper()}'

name = {'first': 'Rizal Ilham', 'second': 'aulia'}
print(display(**name))

def add_and_multiply_number(a, b, c, **kwargs):
    print(a*b*c)
    print("OTHER STUFF")
    print(kwargs)
data = dict(a=1, b=2, c=3, d=55, name='Rizal Ilham', score='1000')
add_and_multiply_number(**data)

# Quis
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final