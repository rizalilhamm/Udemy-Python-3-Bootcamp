""" Function Exertise """

# 1. define product below:
def product(p1, p2):
    return p1 * p2

# 2. return day
def return_day(day):
    result = None
    if day == 1:
        
        result = "Sunday"
    elif day == 2:
        result = "Monday"
    elif day == 3:
        result = "Tuesday"
    elif day == 4:
        result = "Wednesday"
    elif day == 5:
        result = "Thursday"
    elif day == 6:
        result = "Friday"
    elif day == 7:
        result = "Saturday"
    
    return result

# 3. last element
def last_element(values):
    try:
        return values.pop()
    except IndexError as e:
        return None

# 4. number_compare
def number_compare(a,b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"

# 5. Single letter count
def single_letter_count(string,letter):
    return string.lower().count(letter.lower())

# 6. multiple letter count
def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

# 7. list namipulation
def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection

# 8. is_palindrome
def is_palindrome(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]