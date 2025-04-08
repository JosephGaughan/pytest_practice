from lib.gratitudes import *

def test_gratitudes_append():
    instance_gratitudes = Gratitudes()
    instance_gratitudes.add("passion")

    # result = gratitudes.format()
    # assert result == "Be grateful for: passion"

    assert instance_gratitudes.gratitudes == ["passion"]

    #assert gratitudes.format() == "Be grateful for: passion"

def test_gratitudes_fortmat():
    gratitudes = Gratitudes()
    gratitudes.add("connection")
    result = gratitudes.format()
    assert result == "Be grateful for: connection"