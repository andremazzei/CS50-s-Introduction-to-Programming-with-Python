import pytest

from fuel import convert, gauge

def test_convert():
    assert convert("4/4") == 100
    assert convert("99/100") == 99
    assert convert("3/4") == 75
    assert convert("2/4") == 50
    assert convert("1/4") == 25
    assert convert("1/100") == 1
    assert convert("0/100") == 0

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/1")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"







