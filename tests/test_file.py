# Copyright (C) 2022 Oracle and/or its affiliates. All rights reserved.
"""Test file"""
import pytest

from src import file


def test_addition() -> None:
    """Test addition of two numbers."""

    result1 = file.addition(46, 6)
    assert result1 == 52


def test_capitalize() -> None:
    """Test addition of two numbers."""

    result = file.capital_case("hanane")
    assert result == "Hanane"


def test_raises_exception_on_non_string_arguments():
    """Raise exception"""

    with pytest.raises(TypeError):
        file.capital_case(9)
