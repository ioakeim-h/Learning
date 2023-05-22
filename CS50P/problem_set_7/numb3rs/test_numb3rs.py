from numb3rs import validate


def test_true():

    assert validate("0.0.0.0") == True
    assert validate("000.000.000.000") == True
    assert validate("250.250.250.250") == True




def test_false():

    assert validate("") == False
    assert validate("cat") == False
    assert validate("1..1..1..1") == False
    assert validate("cat.cat.cat.cat") == False
    assert validate("1 1 1 1") == False
    assert validate("1.22.333.4444") == False
    assert validate("275.300.500.600") == False
    assert validate("1.-1.-1.-1") == False
    assert validate("0000.0000.0000.0000") == False



def test_etc():
    assert validate("192.168.5.cat") == False
    assert validate("192.x.x.x") == False
    assert validate("x.1.2.3") == False
    assert validate("75.456.76.65") == False