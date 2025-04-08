import pytest
from lib.password_checker import *



def test_password_exception():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("test")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."