import pytest

from working import convert


def test_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_midnight_midday():
    assert convert("12 AM to 5 PM") == "00:00 to 17:00"
    assert convert("9:00 PM to 12 PM") == "21:00 to 12:00"

def test_value_error():
    with pytest.raises(ValueError):
        convert("12 AM 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 PM to 12 PM")


