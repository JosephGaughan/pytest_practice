from lib.add_five import *

def test_add_five_returns_eight_for_three():
    result = add_five(3)
    assert result == 8

def test_multiply_two_returns_one_hundred_for_fifty():
    result = multiply_two(50)
    assert result == 100