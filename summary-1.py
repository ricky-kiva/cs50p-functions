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