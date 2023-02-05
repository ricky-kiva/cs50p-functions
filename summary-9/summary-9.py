students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

houses = set() # a 'set' is an array to store ONLY unique value
for student in students:
    houses.add(student["house"])

print(sorted(houses))
print()

# from here to several code below shows the use of 'global'

balance = 0 # this intended to be a 'global' variable for several function below

def bank():
    print(f"Before\t: {balance}")
    deposit(100)
    withdraw(25)
    print(f"After\t: {balance}")

def deposit(n):
    global balance # state this so the function knows it is a 'global' variable
    balance += n

def withdraw(n):
    global balance
    balance -= n

bank()
print()

GUN = 2 # by convention, this is a 'constant', a variable that is prohibited to be changed
# a 'constant' needs to be capitalized

for _ in range(GUN):
    print("One, 21 Guns")
print()

class Cat:
    MEOWS = 3 # making 'constant' for a class

    def meow(self):
        for _ in range(Cat.MEOWS): # calling 'constant' for a class
            print("meow", end=". ")
        print()

cat = Cat()
cat.meow()
print()
