from um import count

def test_valid():
    assert count("Hi, my name is um... Jo") == 1
    assert count("What comes after um, shall remain unknown") == 1
    assert count("UM") == 1
    assert count(".um.") == 1
 
def test_valid_b():
    assert count("Yum yum, um, yum") == 1
    assert count("um... UM ... um") == 3
    assert count("um, uM, Yum") == 2
    

def test_invalid():
    assert count("Mum") == 0
    assert count("mum mum mum ") == 0
    assert count("microsporangium") == 0
    assert count("circumspect") == 0
















