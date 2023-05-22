
from twttr import shorten


def test_lower():
    assert shorten("twitter") == "twttr"


def test_upper():
    assert shorten("TWITTER") == "TWTTR"


def test_white_space():
    assert shorten(" TWITTER ") == " TWTTR "


def test_number():
    assert shorten("Ioakeim 1996") == "km 1996"


def test_punc():
    assert shorten("Hi,") == "H,"


# Run pytest test_twttr.py

