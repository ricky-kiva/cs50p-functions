# while loop
i = 0
while i < 3:
    print("meow", end=" ")
    i += 1
print()

# for loop
for _ in range(3):
    print("meow", end=" ") # use "_" if you don't care about the iterating variable
print()

for struggler in ["Guts", "Casca", "Puck"]: # it can iterate through list
    print(struggler, end=" ")
print()

# validating input
while True:
    mew = int(input("How much? "))
    if mew > 0:
        break # break the loop if mew > 0

for _ in range(mew):
    print("meow", end=" ")

# len
strugglers = ["Guts", "Casca", "Puck", "Thorfinn"]

for i in range(len(strugglers)): # 'len' will return the length number of a list
    if (struggler == "Puck"):
        continue # to skip iteration on certain condition
    print(struggler, end=" ")
print()

# dict
characters = {
    "Guts": "Berserk",
    "Thorfinn": "Vinland Saga",
    "Edward": "Full Metal Alchemist",
    "Tenma": "Monster"
} # dict saves a key (left) and a value (right)

for i in characters: # to print the key
    print(i, end=" ")
print()

for i in characters: # to print the value
    print(characters[i], end=" ")
print()

# list of dict
readings = [
    {"name": "Monster", "protagonist": "Tenma", "antagonist": "Johan"},
    {"name": "Berserk", "protagonist": "Guts", "antagonist": "Griffith"},
    {"name": "Full Metal Alchemist", "protagonist": "Edward", "antagonist": "7 sins"},
    {"name": "Vinland Saga", "protagonist": "Thorfinn", "antagonist": None}
]

for book in readings:
    print(book["protagonist"], book["antagonist"], book["name"], sep=" | ")
print()

# nested loops (making block from a loop)
for i in range(3):
    for j in range(6):
        print("#", end="")
    print()

print()

for i in range(3): # making using pythonic ways
    print("#" * 6)
