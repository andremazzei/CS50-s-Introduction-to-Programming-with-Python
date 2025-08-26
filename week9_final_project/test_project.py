import project
from unittest.mock import patch


def test_currency():
    assert project.get_currency("Brazil") == ["BRL"]
    assert project.get_currency("Spain") == ["EUR"]
    assert project.get_currency("CA") == ["CAD"]
    
@patch("project.input", side_effect=["Portuguese"])
def test_languages(mock_input):
    assert project.get_language() == ("Portuguese", "pt")

@patch("project.input", side_effect=["1","5","10"])
def test_categories(mock_input):
    assert project.get_category() == ("business")
    assert project.get_category() == ("entertainment")
    assert project.get_category() == ("other")