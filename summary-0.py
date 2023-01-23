# print() function parameters (sep & end)
# (\) before (") means ignore the use of the actual (")
print("So what's your", "\"full name\"", sep=" ", end="?\n")

# get input to variable, remove unnecessary space (strip)
# and capitalize each sentence (title) using str methods
name = input("My name is ").strip().title()

# split the name and put it into 2 variable (,)
first, last = name.split(" ")

# print the name using new python format features (f"{}")
# (\n) means new line
print(f"\n{last}, The name is {first} {last}\n")

# typecast & int
print("I'm not sure, lets test your math.")
x = int(input("First number: "))
y = int(input("Second number: "))
print(f"\n{name}: It's {(x+y):,}!\n")

# float & it's method
print("Wow, is it? But how about floats!")
f1 = float(input("First decimal: "))
f2 = float(input("Second decimal: "))
print(f"\n{name}: Must be around {round(f1+f2)}!\n")

# division & format features
print("Give me 3 points precision division!")
d1 = float(input("First decimal: "))
d2 = float(input("Second decimal: "))
print(f"\n{name}: Easy. {(d1/d2):.3f}!\n")

print("All right, now is the 'main' challenge, square this!")

# making the main function
def main():
    x = int(input("Number to be squared: "))
    print(f"Surely {square(x)}!")

def square(n):
    return pow(n,2) # pow will square a number

main() # calling the main function
