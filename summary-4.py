# on terminal, type 'pip install cowsay' to install 'cowsay'
# same goes as 'requests'
# because those area all an "external" python package
import cowsay
import requests

# if you want to import all components inside a library
import statistics
import json
import sys

# if you want to import certain component of a library
from random import choice, randint

# trying 'randint' from 'random'
print(randint(1,5))

# trying 'choice' from 'random'
print(choice(["water", "fire", "earth", "wind"]))

# trying one of 'statistics' component
print(statistics.mean([100, 80, 90, 80]))

# 'slices' get a subset from a list
sharks = ["great white", "whale", "nurse", "blue", "port jackson", "hammerhead"]
for small in sharks[2:5]:
    print(f"'{small}'", end=" ")
print()

# trying sys.argv (argument vector)
# run the script followed by any string, ex: python summary-4.py "Pink Floyd"
# it will output the code inside "else"
if (0 < len(sys.argv) < 2):
    pass
else:
    cowsay.cow(f"What's with this '{sys.argv[1]}' thing?")

# 'exit' from 'sys' to exit command
while True:
    ask_exit = input("Exit? (yes to proceed) ")
    if (ask_exit.lower() == "yes"):
        sys.exit("Have a nice day!")
    else:
        continue