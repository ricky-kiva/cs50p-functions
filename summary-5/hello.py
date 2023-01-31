def main():
    name = input("x: ")
    print(hello(name))

def hello(name="World"):
    return (f"Hello, {name}")

if __name__ == "__main__":
    main()