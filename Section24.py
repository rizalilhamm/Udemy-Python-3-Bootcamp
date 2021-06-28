""" DEFINING CLASS AND OBJECT
    > Class a blueprint for object, Classes can contain methods (functions) and attribute
    > Object that are contructed from a class blueprint that contain there class's methods and properties

    > Abstraction and Encaptulation
        cards { public method }
        _cards { private int attribute }
        _max_cards_list {privave list attribute }
    
    > Encaptulation
        Grouping public and private attribute and method into a programmatic class, making abstraction possible
    > Abstraction
        Exposing only "relevant" data in a class interface, hiding ptivate attributes and method from users
"""

class User:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


user1 = User("Rizal", "Ilham", 21)
user2 = User("Kasmadi","Rmadhan", 20)
user3 = User("Aulia", "Sabri", 20)

print(user1.firstname)
print(user2.firstname)
print(user3.firstname)

""" UNDERSCORES: DUNDER METHOD. NAME MAGLING, AND MORE """
class Person:
    # _name
    # __name
    # __name__
    def __init__(self):
        self.name = 'Rizal Ilham'
        self._secret = 'Hi!'
        self.__msg = 'I like turtles!'
        self.__lol = 'HAHAHA'
    # def dorman(self, guess):
        # if guess == self._secret:
            # let them in

p = Person()
print(p.name)
print(p._secret)
print(dir(p))
print(p._Person__msg)
print(p._Person__lol)

# Quis 1
# define the Vehicle class below:
# instantiate a new Vehicle and save it to a variable called car:
# instantiate a new Vehicle and save it to a variable called boat:
class Vehicle:
    pass
car = Vehicle()
boat = Vehicle()

# Quis 2
# Define the Comment class below:
class  Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes


""" ADDING INSTANCE METHOD """
class Pengguna:
    # Class attribute
    pengguna_active = 0
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        Pengguna.pengguna_active += 1

    def full_name(self):
        return f'{self.firstname} {self.lastname}'
    
    def initials(self):
        return f'{self.firstname[0]}.{self.lastname[0]}.'

    def likes(self, thing):
        return f'{self.firstname} likes: {thing}'

    def is_senior(self):
        return self.age >= 50

print("PENGGUNA AKTIF: {}".format(Pengguna.pengguna_active))
p1 = Pengguna("Rizal", "Ilham", 21)
p2 = Pengguna("Joko", "Widodo", 50)
print(p1.full_name())
print(p1.initials())
print(p1.likes("Ice Cream"))
print("Senior: {}".format(p1.is_senior()))

print(p2.full_name())
print(p2.initials())
print(p2.likes("Jengkol"))
print("Senior: {}".format(p2.is_senior()))
print("PENGGUNA AKTIF: {}".format(Pengguna.pengguna_active))

# Quis 1
# Define Bank Account Below:
class BankAccount:
    jumlah_nasabah = 0
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
        BankAccount.jumlah_nasabah += 1
    
    def deposit(self, ammount):
        self.balance += ammount
        return self.balance
    
    def withdraw(self, ammount):
        self.balance -= ammount
        return self.balance

    def logout(self):
        BankAccount.jumlah_nasabah -= 1
        return f'{self.owner} has logout!'

print("Nasabah aktif: {}".format(BankAccount.jumlah_nasabah))
nasabah1 = BankAccount("Rusdi")
print(nasabah1.owner)
print("Jumlah uang nasabah setelah penambahan : {}".format(nasabah1.deposit(10)))
print("Jumlah uang nasabah setelah pengambilan: {}".format(nasabah1.withdraw(5)))
print("Nasabah aktif: {}".format(BankAccount.jumlah_nasabah))
nasabah1.logout()
print("Nasabah aktif: {}".format(BankAccount.jumlah_nasabah))

""" CLASS ATTRIBUTES CONTINUES """
class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")

# Quis
class Chicken:
    total_eggs = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0
    
    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs


""" Class Methods """

class Manusia:
    # Constructor
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    # classmethod
    @classmethod
    def from_string(cls, text):
        firstname, lastname, age = text.split(",")
        return cls(firstname, lastname.replace(' ', ''), int(age))

    # Representation
    def __repr__(self):
        return f"User: {self.firstname} {self.lastname}"

# Panggil jika tidak menggunakan class method
# nama = Manusia.from_string(Manusia, "Rizal, Ilham, 21")

# Panggil jika menggunakan class method
nama = Manusia.from_string("Ronaldo, Wati, 20")
print(nama.firstname)
print(nama.lastname)
print(nama.age)