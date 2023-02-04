import sys
import random

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) # this is a 'tuple', not a 'list'
    # 'tuple' is an immutable object, the value CANNOT be changed
    # note: 'list' is mutable object, the value COULD be changed
    # note: 'dict' is a mutable object, the value COULD be changed

def try_tuple():
    student = get_student()
    if student[0].lower() == "padma":
        try:
            student[1] = "Ravenclaw" # this will cause error, because student is a tuple
            print(f"{student[0]} from {student[1]}")
        except TypeError:
            print("Can't change value of a tuple")
    else:
        print(f"{student[0]} from {student[1]}")

try_tuple()
print()

class Shark(): # conventionally, class starts Capitalized
    ...     # making class with no methods

def try_shark():
    shark = Shark() # assigning class to var
    # you can make any 'instance variable' if the class has no methods (...)
    shark.name = input("Shark: ") # assigning value to class's 'instance variable'
    shark.unique = input("Uniqueness: ")
    print(f"{shark.name} known for {shark.unique}") # get the value of the 'instance variable'

try_shark()
print()

class Student(): # making class with blueprint variable
    def __init__(self, name, house, patronum): # __init__ will automatically be executed when the class being called
        # 'self' need to be always assigned to the parameter if you want to have a blueprint of 'instance variable'
        self.name = name # the blueprint 'instance variable' need to be stated like this
        self.house = house
        self.patronum = patronum
    
    def __str__(self): # OPTIONAL. to do something when the class is being called as string. ex: print(Student(name, house))
        return (f'\nSnape\t: "{self.name} from {self.house}."\n{self.name}\t: "Expecto Patronum!"\n\n{self.charm()} !\n')

    def charm(self): # making custom method
        if (self.patronum).lower() == "stag":
            return "🦌"
        elif (self.patronum).lower() == "otter":
            return "🦔"
        elif (self.patronum).lower() == "dog":
            return "🐕"
        else:
            return "✨"

    # from here to below, we will set 'getter' & 'setter' method
    # the reason is so the variable inside the class stayed private, can't be changed directly (ex: student.name = 'Harry')
    # 'getter' method being used to get an 'instance variable' from a class
    # 'setter' method being used to set an 'instance variable' from a class

    @property # need to type this to make 'getter'
    def house(self): # the method name needs to be same as the 'instance variable'
        return self._house # used to return the desired 'instance variable'
        # underscore (_) before 'house' NEED to be typed by convention

    @house.setter # need to type this to make 'setter'
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house # used to update the 'instance variable' with the input argument

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name: # validating variable
            raise ValueError("Missing name")
        self._name = name

    @classmethod # jump to 'Hat' class far down below for the description of 'class method'
    def get(cls): # jump to 'Hat' class far down below for 'cls' description
        # this will make a method, that creates this class
        name = input("Name: ")
        house = input("House: ")
        patronum = input("Patronum: ")
        return cls(name, house, patronum) # will return this class, with input as within the method

def try_student():
    try:
        stud = Student.get() # if the 'instance variable' blueprint has been set, could pass the value directly to the parameter
        try:
            # set 'house' using 'setter'
            # don't need to use parentheses '()' to call a setter that stated with '@var.setter' (part of '@property')
            stud.house = input(f"\n{stud.name} wants to change House. Any suggestion? ")
        except ValueError:
            print("We all know there's no such of house.")
        else:
            # get 'name' and 'house' using 'getter'
            # don't need to use parentheses '()' to call a class method if it's stated with '@property'
            print(f"\n{stud.name} went to {stud.house}.")
    except ValueError:
        print("Some argument are invalid")
    else:
        print(stud) # will run '__str__' inside Student() class
    
try_student()

print(f"50 type is: {type(50)}") # 'type' used to see type of an input
print(f'"Hello" type is: {type("Hello")}')
print()

# direct below shows how to make a 'class method'

class Hat():

    # this is a 'class variable'
    # this variable always generated when the class is CALLED, so it could be accessed rightaway by the name of it's class
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod # 'class method' enable a method so it could be called rightaway by the name of it's class (ex: Hat.sort("Harry"))
    def sort(cls ,name): # cls means it uses 'class variable'
        return f"{name} is in {random.choice(cls.houses)}"

print(Hat.sort("Harry"))
print(f"List of houses: {Hat.houses}")
print()

# direct below shows the implementation of 'inheritance'

class Wizard():
    def __init__(self, name):
        if not name:
            raise ValueError("Name can't be empty")
        self.name = name

    def __str__(self):
        return f"{self.name} is a Wizard"

# 'Novice' and 'Professor' class will inherit a variable or even method from 'Wizard' using 'Inheritance'

class Novice(Wizard): # put the class to inherit as argument
    def __init__(self, name, house):
        super().__init__(name) # get the 'instance variable' (name) using this syntax
        self.house = house

    def __str__(self):
        return f"{self.name} is a {self.house}'s student"

class Professor(Wizard): # do the same as 'Novice' class
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"{self.name} teach {self.subject}"

print(Wizard("Dumbledore"))
print(Novice("Harry", "Gryffindor"))
print(Professor("Snape", "Technique of the Dark Art"))
print()

# direct below shows the implementation of 'Operator overloading'

class Vault():
    def __init__(self, galleons, sickles, knuts):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other): # this will override the default '__add__' (+) (substitution) method
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts

        return Vault(galleons, sickles, knuts)

harry_vault = Vault(100, 50, 25)
print(f"Harry: {harry_vault}")

ron_vault = Vault(25, 50, 150)
print(f"Ron: {ron_vault}")

total_vault = harry_vault + ron_vault
print(f"Total: {total_vault}") # call the overloaded '__add__' method