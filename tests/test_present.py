import pytest
from lib.present import *



def test_wrap_exception():
    present = Present()
    present.wrap("socks")
    with pytest.raises(Exception) as e:
        present.wrap("book")
    error_message = str(e.value)
    assert error_message == ("A contents has already been wrapped.")

def test_wrap():
    present = Present()
    present.wrap("socks")
    assert present.contents == "socks"

def test_unwrap_exeption():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_unwrap():
    present = Present()
    present.contents = "socks"
    assert present.unwrap() == "socks"