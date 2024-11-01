from twttr import shorten


def test_capital():
    assert shorten("CARALHO") == "CRLH"
    assert shorten("PIROCA") == "PRC"

def test_lower():
    assert shorten("sao paulo") == "s pl"
    assert shorten("paralelepipido") == "prllppd"

def test_numbers():
    assert shorten("152") == "152"
    assert shorten("1852354 984652") == "1852354 984652"

def test_punctuation():
    assert shorten(".,!@?") == ".,!@?"
