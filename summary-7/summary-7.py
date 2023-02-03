import re

mail = input("Email: ")
if (re.search(r"^[\w\.]+@[a-z\.]+\.[a-z]+$", mail, re.IGNORECASE)):
    # list of regex patterns here: https://www.w3schools.com/python/python_regex.asp
    # 're.IGNORECASE' considered as 'flag' parameter
    print("Valid")
else:
    print("Invalid")

name = input("Your name in US format? ") # asking for 'Pacino, Al' format
if matches := re.search(r"^([a-z]+),\s*([a-z]+)", name, re.IGNORECASE):
    print(f"Hello {matches.group(2)} {matches.group(1)}") # extract string from group
else:
    print("Not the right format, I guess?")

twitter = input("Twitter profile url: ")
if re.search(r"twitter\.com\/", twitter, re.IGNORECASE):
    username = re.sub(r"(^https?:\/\/)?(www\.)?twitter\.com\/", "", twitter)
    # 'sub' will substitute the 1st argument, with the 2nd argument, from the 3rd argument
    print(f"Twitter username: {username}")
else:
    print("Invalid url")

# another way to get twitter username
insta = input("Instagram profile url: ")
if username := re.search(r"(?:(?:^https?:\/\/)?(?:www\.)?)?instagram\.com\/(\w+)", insta, re.IGNORECASE):
    # (?:__string__)? will exclude the group from the group list
    print(f"Instagram username: {username.group(1)}")
else:
    print("Invalid url")

# 're.findall' to search every matching pattern on the string