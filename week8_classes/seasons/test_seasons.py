import pytest
from seasons import date_validation

def test_date():
    with pytest.raises(SystemExit):
        date_validation("19850707")
    with pytest.raises(SystemExit):
        date_validation("July 7, 1985")

def test_date_correct():
    assert date_validation("1985-07-07") == ("1985","07","07")

