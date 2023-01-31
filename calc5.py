def main():
    x = input("x: ")
    print(square(x))

def square(n):
    return (n*n)

def hello(x="World"):
    return (f"Hello, {x}")

if __name__ == "__main__":
    main()