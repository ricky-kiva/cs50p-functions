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

def drink(n: int) -> str: # this parameter is being 'type hints'-ed, means the argument needs to be an int
    # '->' states that it will return a 'str'

    # below is a 'docstring', a convention to document a function
    """
    Meow n times.

    : param n           : Number of times to meow
    : type  n           : int
    : raise TypeError   : If n is not an int
    : return            : A string of n meows, all in one line
    : rtype             : str

    """

    return "sip. " * n

# install 'mypy' 'pip install mypy'
# test this with 'mypy' libraries in terminal, ex: 'mypy summary-9.py'
# mypy could check 'type hints' error prettier

glass: int = int(input("How much glass? ")) # 'type hints' could be called like this also
sip: str = drink(glass) # assigning return value of function to var with 'type hints'
print(sip, end='\n')
print()

# > the implementation on 'argparse' library could be checked on meow.py

# below is an implementation of 'unpacking'

def usd_idr(sawbuck, dollar, cents):
    return (sawbuck * 150950) + (dollar * 15095) + (cents * 7)

purse = [1, 13, 89]
wallet = {"sawbuck": 1, "dollar": 13, "cents":89}

print(f"IDR in purse: {usd_idr(*purse)} Rupiah") # type '*' to unpack a list
print(f"IDR in wallet: {usd_idr(**wallet)} Rupiah") # type '**' to unpack a dictionary
print()

# ('*args' works almost like 'tuple') '*args' passes 'variable number' of 'non-keyworded argument', on which the operation of a 'tuple' can be performed
# ('**kwargs' works almost like 'dict') '*kwargs' passes 'number of keyword arguments dictionary', on which the operation of a 'dict' can be performed
# user can rename the '*args' parameter name, such '*sharks'
# same goes for '**kwargs'

def pos(*args, **kwargs):
    print("Args\t: ", args)
    print("Kwargs\t: ", kwargs)

# '*args' will capture the 'non-keyworded arguments' like list, while '**kwargs' will capture 'keyworded arguments' to dictionary
pos("Persian", "Domestic", "Sphynx", Head = "Hammerhead", Tail= "Thresher", Mouth = "Whale") # calling '*args' & '**kwargs'
print()

# usage of 'map' function

def yell(*words):
    uppercased = map(str.upper, words) # this will 'str.upper' to all value inside '*words'
    print(*uppercased)

yell('This', 'is', 'CS50', '!')

# usage of the pythonic 'list comprehension'

def yell2(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

yell2('This', 'is', "Harvard's",'CS50', '!')
print()

# filtering using 'list comprehension'

def gryffindors(students):
    gryffindors = [student["name"] for student in students if student["house"] == "Gryffindor"]
    print(*gryffindors, sep=", ", end="\n")

gryffindors(students)

# filtering using 'filter'

def is_gryffindor(arr):
    return arr["house"] == "Gryffindor"

gryffindors2 = filter(is_gryffindor, students) # 'filter' will take the data from the 2nd parameter, pass it as an argument for function in the 1st parameter, filtering each data by it's boolean output (True or False)
# the function passed in the 1st argument is NOT using parentheses '()' because the 'filter' that is going to call the function
# you can also define it using lambda expression (without is_gryffindor() function) like this:
# filter(lambda s: s["house"] == "Gryffindor", students)

print(*[student["name"] for student in sorted(gryffindors2, key=lambda s: s["name"])], sep=", ", end="\n")
print()

# usage of the pythonic 'dictionary comprehension'

gryffin_stud = ["Hermione", "Harry", "Ron"]
print(*[{"name": student, "house": "Gryffindor"} for student in gryffin_stud], sep=", ", end="\n")
print()

# usage of 'enumerate'

for num, i in enumerate(gryffin_stud):
    print((num+1), i)
print()