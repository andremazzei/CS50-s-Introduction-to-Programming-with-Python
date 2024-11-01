from plates import is_valid

def test_maxmin():
    assert is_valid("AA12345") == False
    assert is_valid("AA") == True
    assert is_valid("AA1234") == True

def test_middle_num():
    assert is_valid("A12A34") == False
    assert is_valid("1AA123") == False
    assert is_valid("1234AA") == False

def test_punctuation():
    assert is_valid("AA12 4") == False
    assert is_valid("AA.123") == False
    assert is_valid("AA123!") == False

def test_correct():
    assert is_valid("AAA123") == True
    assert is_valid("AAAA12") == True
    assert is_valid("AA1234") == True

def test_alpha():
    assert is_valid("12355") == False

def test_zero():
    assert is_valid("AA0555") == False

def test_numbers():
    assert is_valid("AAAAAA") == True
    assert is_valid("AA22") == True
    assert is_valid("AA2") == True
    assert is_valid("AA2AAA") == False
