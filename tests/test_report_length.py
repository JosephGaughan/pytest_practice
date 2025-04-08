from lib.report_length import *

def test_report_length_string():
    result = report_length("cat")
    assert result == "This string was 3 characters long."

def test_report_length_int():
    result = report_length(10)
    assert result == "This string was 2 characters long."