from calc import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4 # 'assert' used for unit testing (testing function)
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")

# other summary is on the other file & folder inside 'summary-5' folder
# to run all test in 'test' folder, run 'pytest test' or 'pytest ./summary-5/test' respectively to your current directory 

if __name__ == "__main__":
    main()