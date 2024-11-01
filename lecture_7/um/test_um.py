from um import count

def test_spaces():
    assert count("um") == 1
    assert count(" um") == 1
    assert count(" um ") == 1

def test_words():
    assert count("Mum") == 0
    assert count(" album ") == 0
    assert count("My album um") == 1

def test_none():
    assert count("cat") == 0
    assert count("ajksljdd") == 0

def test_phrase():
    assert count("Um, thanks for the album. um, um!") == 3
