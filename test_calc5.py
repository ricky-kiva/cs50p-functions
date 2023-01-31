import pytest
from calc5 import square, hello

# to run this pytest, run 'pytest test_calc5.py'

def test_square():
    assert square(2) == 4
    assert square(3) == 9

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError): # 'raises'will catch error in test file
        square("cat")

def test_hello():
    assert hello("Roger") == "Hello, Roger"
    assert hello() == "Hello, World"