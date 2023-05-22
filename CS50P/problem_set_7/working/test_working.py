from working import convert
import pytest


def test_hours():

    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("09:00 AM to 05:00 PM") == "09:00 to 17:00"

    assert convert("5 PM to 9 AM") == "17:00 to 09:00"    
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("05:00 PM to 09:00 AM") == "17:00 to 09:00"
    
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"


    with pytest.raises(ValueError):
        convert("0 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("5:00 AM to 0:00 PM")

    with pytest.raises(ValueError):
        convert("00:00 AM to 05:00 PM")

    with pytest.raises(ValueError):
        convert("13 AM to 12 PM")

    with pytest.raises(ValueError):
        convert("12:00 AM to 13:00 PM")


def test_minutes():
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"

    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9: AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:xx AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("5:60 AM to 9:60 PM")
    

def test_etc():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("c AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9:cs AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM to 05:00 cs")

    


 







