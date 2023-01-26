# this is a file necessary for 'summary-4.py'

def main():
    print(hello("world"))
    print(bye("world"))

def hello(name):
    return (f"Hello {name}!")

def bye(name):
    return (f"Goodbye {name}")

# this code means, it will ONLY allow to execute main()
# when it's being run from terminal
# if you call a method (ex: 'hello()') from this file (4-greet.py) from another file
# main() will not be executed
if __name__ == "__main__":
    main()