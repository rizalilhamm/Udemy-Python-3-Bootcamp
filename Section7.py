# STRING CONCATENATION 
firstname = "Rizal"
lastname = "Ilham"
fullname = firstname + " " + lastname
print(fullname);


# STRING FORMATTING
username = "Rizal Ilham"
score = 90
print(f"Hey {username} your score is {score}")

# quis
first = "Rizal"
last = "Ilham"
formatted = "First Name: {}, Last Name: {}".format(first, last)
print(formatted)


# STRING AND INDEXES
print("lol"[1])
answer = "yessir"
print(answer[0])
print("Call perindex 0 is {}, last index {}".format(answer[0], answer[len(answer)-1]))
# Note: if you call using - ex: -1, -2 it begin from last caracter


# CONVERTING DATA TYPE
num = 10  # int
num = float(num)  # float
num = str(num)  # str
print("Type of \"NUM\" is {}".format(type(num)))

# Building a Mileage with User Input
print("How many kilometers did you circle today?")
kms = input()
miles = float(kms) / 1.60934
miles = round(miles, 2) # return 2 character after comma
print(f"Your {kms}km ride was {miles}mi")