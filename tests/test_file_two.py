# Copyright (C) 2022 Oracle and/or its affiliates. All rights reserved.
"""Test file two"""
from src import file2


def test_sub() -> None:
    """Test sub of two numbers."""

    result1 = file2.subtraction(10, 6)
    assert result1 == 4


def test_sub_less_than_zero() -> None:
    """Test sub of two numbers."""

    result1 = file2.subtraction(6, 10)
    assert result1 == -4
