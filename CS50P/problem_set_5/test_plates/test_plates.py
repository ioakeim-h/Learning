from plates import is_valid


def test_start():
    assert is_valid("C") == False
    assert is_valid("c") == False

    assert is_valid("CS") == True
    assert is_valid("cs") == True

    assert is_valid("5") == False
    assert is_valid("50") == False

    assert is_valid("C5") == False
    assert is_valid("5C") == False

    assert is_valid("c5") == False
    assert is_valid("5c") == False

    assert is_valid("CS50") == True
    assert is_valid("cs50") == True

    assert is_valid("50CS") == False
    assert is_valid("50cs") == False


def test_range():
    assert is_valid("lensix") == True
    assert is_valid("LENSIX") == True

    assert is_valid("toomanywords") == False
    assert is_valid("TOOMANYWORDS") == False

    assert is_valid("22") == False
    assert is_valid("4444") == False
    assert is_valid("12") == False
    assert is_valid("1") == False


def test_iszero():
    assert is_valid("CS05") == False
    assert is_valid("cs05") == False


def test_end():
    assert is_valid("5CS1") == False
    assert is_valid("C50S") == False
    assert is_valid("C5S1") == False

    assert is_valid("CS50P") == False
    assert is_valid("CS50p") == False



def test_punc():
    assert is_valid("CS50!") == False
    assert is_valid("?CS50") == False
    assert is_valid("CS&50") == False
    assert is_valid(" CS50") == False
    assert is_valid("CS50 ") == False
    assert is_valid("CS 50") == False
    assert is_valid("($$*") == False




 





