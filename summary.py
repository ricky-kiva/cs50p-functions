# print() function parameters (sep & end)
# (\) before (") means ignore the use of the actual (")
print("So what's your", "\"full name\"", sep=" ", end="?\n")

# get input to variable, remove unnecessary space (strip)
# and capitalize each sentence (title) using str methods
name = input("My name is ").strip().title()

# split the name and put it into 2 variable (,)
first, last = name.split(" ")

# print the name using new python features (f"{}")
# (\n) means new line
print(f"\n{last}, The name is {first} {last}")