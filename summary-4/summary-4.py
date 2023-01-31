# on terminal, type 'pip install cowsay' to install 'cowsay'
# same goes as 'requests'
# because those area all an "external" python package
import cowsay
import requests

# if you want to import all components inside a library
import statistics
import json
import sys

# import '4-greet.py' that has already made inside this repository
# and change the name using 'as'
import greet

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

# get a response from an API request & display in a pretty JSON format
if (0 < len(sys.argv) < 2):
    pass
else:
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1]) # to connect API & get data
    json_response = response.json() # to convert the response to json
    print(json.dumps(json_response, indent=2)) # to view json in a prettier format
    print()

# to get a specific requested json information
print(f"{sys.argv[1]}'s songs: ")
for result in json_response["results"]:
    print(result["trackName"])
print()

# using some method from a '.py' script that is already written in this repository (greet4.py)
goodbye = greet.bye(sys.argv[1])

# 'exit' from 'sys' to exit command
while True:
    ask_exit = input("Exit? (yes to proceed) ")
    if (ask_exit.lower() == "yes"):
        # calling some 'greet.py' method
        sys.exit(f"{goodbye}'s!")
    else:
        continue