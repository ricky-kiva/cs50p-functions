import argparse

# 'argparse' could manage the 'argument vector' (argv)
# making function with 'argparse'

def main():
    parser = argparse.ArgumentParser(description="Meow like a cat") # initiate argument parser with it's desc
    parser.add_argument("-t", default=1, type=int, help="number of times to meow") # add a unique character ('-t') to be the 'key' of the 'argument vector'
    args = parser.parse_args() # parsing the added argument, and state it to a var

    for _ in range(args.t): # make use of the caught '-t' argument vector
        print("meow", end=". ")

main()