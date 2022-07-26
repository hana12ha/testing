"""Algo file"""
from src import algo


def test_area():
    """Test area of a rectangle"""
    output = algo.area_of_rectangle(2, 5)
    assert output == 10
