from lib.greet import *

def test_greet():
    result = greet("Joe")
    assert result == "Hello, Joe!"