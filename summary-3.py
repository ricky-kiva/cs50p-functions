# Compile Time Error: an error that caused by invalid semantics or syntax
# example: 
# - SyntaxError: caused by a wrongly typed the sequence of syntax in certain programming language

# Runtime Error: an error caused by unintended input that could be handled by defensively writing alternative code for that certain error
# example: 
# - ValueError error: an error caused by false input

# catching exception using "try-except-else"
try:
    x = int(input("Some number? "))
except ValueError:
    print("that is not a number") # do this on value error
else:
    print("x is", x) # do this when there is no error

# try-except with loop
while True:
    try:
        x = int(input("Some number? "))
    except ValueError:
        pass # will do nothing when there is error
    else:
        break

print("x is", x)