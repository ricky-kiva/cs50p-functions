x = 24
y = 1
z = 23

# if-else conditionals
if x > y:
    print(x, ">", y)
elif x < y:
    print(x, "<", y)
else:
    print(x, "=", y)

# 'and' operator
if x > y and x > z:
    print(x, "IS the greater than", y, "&", z)
else:
    print(x, "IS NOT greater than", y, "&", z)

# chaining comparison
if y < x > z:
    print("(chaining)", x, "IS the greater than", y, "&", z)
else:
    print("(chaining)", x, "(chaining) IS NOT greater than", y, "&", z)

# 'or' operator
if y > x or y > z:
    print(y, "IS the greater than", x, "&", z)
else:
    print(y, "IS NOT greater than", x, "&", z)

# not equals
if x != (y+z):
    print(x, "IS NOT the sum of", y, "&", z)
else:
    print(x, "IS the sum of", y, "&", z)

# function that will return boolean
# is also using pythonic expression
def is_even(n):
    return True if (n % 2 == 0) else False

# check even with boolean function is_even()
if (is_even(x)):
    print(x, "is even")
else:
    print(x, "is odd")

if (is_even(z)):
    print(z, "is even")
else:
    print(z, "is odd")

# match syntax (only works on python 3.10 >=)
# will give ERROR if your python below version 3.10
name = input("Tell me any Harry Potter Character: ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor!")
    case "Draco":
        print("Slytherin!")
    case _:
        print("Who?")