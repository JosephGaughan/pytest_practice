from lib.counter import *

def test_counter_ten():
    counter = Counter()
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 10 so far."

def test_counter_100():
    counter = Counter()
    counter.add(50)
    counter.add(50)
    result = counter.report()
    assert result == "Counted to 100 so far."
