from bank import value


def test_upper():
    assert value("HELLO") == 0
    assert value("HI") == 20
    assert value("WHAT'S UP?") == 100

def test_lower():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("what's up?") == 100

def test_etc():
    assert value(" hi ") == 20
    assert value("...") == 100
    assert value("1") == 100
