import pytest
from calc5 import square

# to run this pytest, run 'pytest test_calc5.py'

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0