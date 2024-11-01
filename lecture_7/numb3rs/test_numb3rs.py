from numb3rs import validate

def test_true():
    assert validate("255.255.255.255") == True
    assert validate("1.1.1.1") == True

def test_false():
    assert validate("355.355.355.355") == False
    assert validate("1.1.1") == False
    assert validate("10.10.01.15.10") == False
    assert validate("55.355.55.55") == False
    assert validate("55.55.355.55") == False
    assert validate("55.55.55.355") == False
