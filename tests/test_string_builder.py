from lib.string_builder import *

def test_sting_builder_add():
    build = StringBuilder()
    build.add("EXTRA")
    assert build.output() == "EXTRA"

def test_string_builder_size():
    build = StringBuilder()
    assert build.size() == 0