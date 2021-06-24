""" Dictionary Exertice """
# Question 1
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {}
# answer
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
     
answer = {list1[i]: list2[i] for i in range(0,3)}

# Question 2
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# use the person variable in your answer
answer = None #(?)
# answer
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}

# Question 3
# make sure your solution is assigned to the answer variable so the tests can work!
answer = {}
# answer | dictionary compherention
answer = {char:0 for char in 'aeiou'}
# answer | dic.fromkeys()
answer = dict.fromkeys("aeiou", 0)