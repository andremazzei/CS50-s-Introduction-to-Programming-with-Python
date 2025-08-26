from bank import value

def test_values():
    assert value("hello") == 0
    assert value("hack") == 20
    assert value("mack") == 100

def test_cases():
    assert value("HELLO") == 0
    assert value("HACK") == 20
    assert value("MACK") == 100

def test_spaces():
    assert value("    HELLO") == 0
    assert value("  HACK  ") == 20
    assert value("MACK   ") == 100


